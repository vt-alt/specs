%define policy_name alt
%define date 20201102
%define seconf %_sysconfdir/selinux/config
%define default_mode permissive

Summary: SELinux %policy_name policy
Name: selinux-policy-alt
Version: 0.0.52
Release: alt1
License: Distributable
Group: System/Base
Source: %name-%date.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
Requires(pre): libsemanage
Requires(pre): policycoreutils
Requires(pre): policycoreutils-newrole

Requires: policycoreutils-newrole
Requires: checkpolicy
Requires: policycoreutils-mcstransd
Requires: policycoreutils-restorecond
Requires: libshell
Requires: m4
Requires: netlabel_tools
Requires: setools-console
Conflicts: selinux-policy-altlinux
Conflicts: selinux-policy
Obsoletes: selinux-policy-altlinux
Provides: selinux-policy-altlinux

%define policy_conf %_sysconfdir/selinux/%policy_name
%define policy_data %_datadir/selinux/%policy_name

%set_findreq_skiplist /lib/systemd/selinux-autorelabel
%add_findreq_skiplist %_bindir/slrun2

%description
SELinux %policy_name policy

%prep 
%setup -n %name

%install
mkdir %buildroot
cp -a * %buildroot

# Ghost files. Do not actually pack them.
tmpfile=$(mktemp)
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/contexts/files/file_contexts
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/contexts/files/file_contexts.bin
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/contexts/files/file_contexts.homedirs
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/contexts/files/file_contexts.homedirs.bin
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/contexts/files/file_contexts.local
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/contexts/files/file_contexts.local.bin
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/contexts/netfilter_contexts
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/semanage.read.LOCK
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/semanage.trans.LOCK
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/seusers
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/policy/policy.28
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/policy/policy.29
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/active/base.pp
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/active/commit_num
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/active/file_contexts
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/active/file_contexts.homedirs
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/active/file_contexts.template
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/active/homedir_template
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/active/netfilter_contexts
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/active/seusers
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/active/policy.kern
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/active/seusers.final
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/active/users_extra
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/policy/policy.28
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/policy/policy.29

# modules
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/active/modules/dolphin.pp
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/active/modules/xorg.pp
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/active/modules/psql.pp
install -D -m0644 "$tmpfile" %buildroot/%policy_conf/modules/active/modules/allow_smb.pp

#
# %%post
#

%post

# XXX bug in 'semodule'
mkdir -p %policy_conf/contexts/files
touch %policy_conf/contexts/files/file_contexts.local
# XXX

# Check SeLinux mode and status
# Possible cases:
# 1. SeLinux is enabled, Enforcing is On, current policy is active
# 2. SeLinux is enabled, Enforcing if Off, current policy is active
# 3. SeLinux is enabled, Enforcing is On, another policy is active
# 4. SeLinux is enabled, Enforcing is Off, another policy is active
# 5. SeLinux is disabled

enforce_mode="$(getenforce)"
echo -e "\tCurrent SeLinux enforce mode is: $enforce_mode"

if ! selinuxenabled; then
   echo -e "\tSeLinux is disabled."
fi

# Cleanup previous modules. Existing modules may be a problem to install base policy.
modules="$(semodule -l -s %policy_name | sed -n -e '/[[:digit:]]\+\.[[:digit:]]\+\.[[:digit:]]\+/ s/[[:space:]].*$//p' | tr '\n' ' ' )"
if [ -n "${modules// /}" ]; then
    echo -e "\tRemove all current (even 3rd party) modules for '%policy_name' policy:"
fi
for i in $modules; do
    echo -e "\t\t* Remove previous module '$i'"
    semodule -n -s %policy_name -r $i
done

# Always install new policy
semodule -n -s %policy_name -i %policy_data/base.pp

# Always install all modules
echo -e "\tActivate modules for '%policy_name' policy:"
for i in %policy_data/modules/*.pp; do
    echo -e "\t\t* Install module '$(basename "$i")'" 
    semodule -n -s %policy_name -i "$i"
done

policy_name_active="$(sestatus | sed -n -e '/policy name/ s/^.\+[[:space:]]//p')"
# Upgrade
if [ $1 -eq 2 ]; then
    if [ "$policy_name_active" = "%policy_name" ]; then
        echo -e "\tSeLinux policy has been updated. Please do a reboot."
    fi
fi

# XXX: suppose there are no other working policy.
# Install
if [ $1 -eq 1 ]; then
    echo "Warning:"
    echo -e "\tSeLinux config '%seconf' is updated with 'SELINUX=%default_mode'"
    ( . shell-config; shell_config_set "%seconf" "SELINUX" "%default_mode" )
    ( . shell-config; shell_config_set "%seconf" "SELINUXTYPE" "%policy_name" )

    # Relabel all FileSystem
    echo -e "\tMake sure to:"
    echo -e "\t\t * Enable SeLinux in kernel."
    echo -e "\t\t * Configure PAM for SeLinux."
    echo -e "\tIt is necessary to relabel FS. Please do a reboot."
    echo -e "\tFor more information visit: http://www.altlinux.org/sl"
    touch /.autorelabel
fi

exit 0 # End of %%post section

#
# %%preun
#
%preun

policy_name_active="$(sestatus | sed -n -e '/policy name/ s/^.\+[[:space:]]//p')"

# The last version of a package is erased
if [ $1 = 0 ]; then
    # Cleanup installed modules
    modules="$(semodule -l -s %policy_name | sed -n -e '/[[:digit:]]\+\.[[:digit:]]\+\.[[:digit:]]\+/ s/[[:space:]].*$//p' | tr '\n' ' ' )"
    if [ -n "${modules// /}" ]; then
       echo -e "\tCleanup all installed (even 3rd party) modules for '%policy_name' policy:"
    fi
    for i in $modules; do
       echo -e "\t\t* Cleanup module '$i'"
        semodule -n -s %policy_name -r $i
    done
    if [ "$policy_name_active" = "%policy_name" ]; then
        echo "Warning:"
        echo -e "\tSeLinux is disabled in config: %seconf"
        ( . shell-config; shell_config_set "%seconf" "SELINUX" "disabled" )
        echo -e "\tSeLinux policy package '$policy_name_active' is uninstalled completely."
        echo -e "\tPlease reboot computer as soon as possible."
    fi
fi

exit 0 # End of %%preun section

%files
%doc usr/share/doc/selinux-policy-alt/commit-id
%config(noreplace) %_sysconfdir/selinux/config
%dir %policy_conf
%dir %policy_conf/contexts
%dir %policy_conf/contexts/users
%dir %policy_conf/contexts/files
%dir %policy_conf/modules
%dir %policy_conf/modules/active
%dir %policy_conf/modules/active/modules
%dir %policy_conf/modules/policy
%dir %policy_conf/policy
%dir %policy_data
%dir %policy_data/support
%dir %policy_data/modules
%dir %_sysconfdir/security/alt.newrole

%policy_conf/contexts/dbus_contexts
%policy_conf/contexts/default_contexts
%policy_conf/contexts/default_type
%policy_conf/contexts/x_contexts
%policy_conf/contexts/netfilter_contexts
%policy_conf/contexts/securetty_types
%policy_conf/contexts/sepgsql_contexts
%config(noreplace) %policy_conf/setrans.conf

%policy_conf/contexts/users/*

%policy_data/*.pp
%policy_data/modules/*.pp
%policy_data/*.if

%policy_data/support/*.spt
%policy_data/Makefile

%attr(0755,root,root) %_sysconfdir/security/alt.newrole/helper
%attr(0755,root,root) %_sysconfdir/security/alt.newrole/mkdirs
%config(noreplace) %_sysconfdir/security/alt.newrole/dirs
%config(noreplace) %_sysconfdir/security/alt.newrole/config
%config(noreplace) %_sysconfdir/security/namespace.d/namespace-selinux.conf

%_bindir/slrun
%_bindir/slrun2

/lib/systemd/selinux-autorelabel
%_unitdir/selinux-autorelabel-mark.service
%_unitdir/selinux-autorelabel.service
%_unitdir/sysinit.target.wants/selinux-autorelabel.service
%dir %_unitdir/systemd-modules-load.service.d
%_unitdir/systemd-modules-load.service.d/*.conf

# Files that are auto created at installation step.
# Let's take care of them.
# List them here, to be removed at rpm-remove stage.
%ghost %policy_conf/contexts/files/file_contexts
%ghost %policy_conf/contexts/files/file_contexts.bin
%ghost %policy_conf/contexts/files/file_contexts.homedirs
%ghost %policy_conf/contexts/files/file_contexts.homedirs.bin
%ghost %policy_conf/contexts/files/file_contexts.local
%ghost %policy_conf/contexts/files/file_contexts.local.bin
%ghost %policy_conf/contexts/netfilter_contexts
%ghost %policy_conf/modules/semanage.read.LOCK
%ghost %policy_conf/modules/semanage.trans.LOCK
%ghost %policy_conf/seusers
%ghost %policy_conf/modules/policy/policy.28
%ghost %policy_conf/modules/policy/policy.29
%ghost %policy_conf/modules/active/base.pp
%ghost %policy_conf/modules/active/commit_num
%ghost %policy_conf/modules/active/file_contexts
%ghost %policy_conf/modules/active/file_contexts.homedirs
%ghost %policy_conf/modules/active/file_contexts.template
%ghost %policy_conf/modules/active/homedir_template
%ghost %policy_conf/modules/active/netfilter_contexts
%ghost %policy_conf/modules/active/seusers
%ghost %policy_conf/modules/active/policy.kern
%ghost %policy_conf/modules/active/seusers.final
%ghost %policy_conf/modules/active/users_extra
%ghost %policy_conf/policy/policy.28
%ghost %policy_conf/policy/policy.29

# modules
%ghost %policy_conf/modules/active/modules/dolphin.pp
%ghost %policy_conf/modules/active/modules/xorg.pp
%ghost %policy_conf/modules/active/modules/psql.pp
%ghost %policy_conf/modules/active/modules/allow_smb.pp

%changelog
* Mon Nov 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.52-alt1
- Merged changes by Denis Medvedev (nbr@).

* Fri Sep 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.51-alt1
- Update policy for current Sisyphus

* Thu Apr 16 2020 Anton Farygin <rider@altlinux.ru> 0.0.50-alt4
- FTBFS: change License tag to Distributable

* Thu Aug 08 2019 Denis Medvedev <nbr@altlinux.org> 0.0.50-alt3
- to sisyphus

* Thu Jul 25 2019 Denis Medvedev <nbr@altlinux.org> 0.0.50-alt2
- to sisyphus

* Tue Jul 02 2019 Denis Medvedev <nbr@altlinux.org> 0.0.50-alt1
- to sisyphus

* Wed Apr 10 2019 Denis Medvedev <nbr@altlinux.org> 0.0.50-alt0.M80C.1
- to c8

* Sat Mar 30 2019 Denis Medvedev <nbr@altlinux.org> 0.0.49-alt0.M80C.1
- to c8

* Thu Jan 31 2019 Denis Medvedev <nbr@altlinux.org> 0.0.48-alt0.M80C.1
- to c8

* Mon Jan 14 2019 Denis Medvedev <nbr@altlinux.org> 0.0.47-alt0.M80C.1
- to c8

* Mon Mar 19 2018 Denis Medvedev <nbr@altlinux.org> 0.0.45-alt0.M80C.1
- to c8

* Mon Mar 19 2018 Denis Medvedev <nbr@altlinux.org> 0.0.45-alt1
- fix creation of level subdirs when system has strictier
permissions on files

* Tue Mar 06 2018 Denis Medvedev <nbr@altlinux.org> 0.0.44-alt1
- allow network operations for smb and ftp access using udiskd

* Tue Aug 08 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.43-alt1
- CD and USB flash mounting via gvfs fixed

* Wed Mar 29 2017 Anton Farygin <rider@altlinux.ru> 0.0.42-alt1
- fixed policy name in /etc/selinux/config

* Wed Mar 29 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.41-alt3
- make /etc/selinux/config noreplace

* Wed Mar 29 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.41-alt2
- confict with selinux-policy added

* Mon Mar 27 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.41-alt1
- break dep on selinux-policy

* Mon Mar 20 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.40-alt1
- make nscd trusted_t

* Mon Mar 20 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.39-alt1
- make named trusted_t
- protect systemd units
- set contexts for /var/s{1,2,3}

* Tue Mar 07 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.38-alt1
- bug with categories ranges fixed

* Mon Feb 13 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.37-alt1
- non-user-visible places now not translated

* Fri Feb 10 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.36-alt1
- no more spaces in setrans.conf

* Fri Feb 10 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.35-alt1
- user-dirs improvements

* Thu Feb 09 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.34-alt1
- dbus improvements from sbolshakov

* Wed Feb 01 2017 Anton Farygin <rider@altlinux.ru> 0.0.33-alt1
- new version

* Tue Jan 24 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.32-alt1
- allow system-config-printer-applet to communicate with system dbus

* Wed Jan 18 2017 Anton Farygin <rider@altlinux.ru> 0.0.31-alt1
- new version
- renamed to alt

* Tue Jan 17 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.30-alt1
- devpts is not secure now

* Tue Jan 17 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.29-alt1
- systemd.te.in: systemd_t now mlstrustedsubject

* Mon Jan 16 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.28-alt2
- merge with previous policy.git

* Wed Jan 11 2017 Sergey V Turchin <zerg@altlinux.org> 0.0.28-alt1
- create alternate HOME for current level

* Thu Dec 01 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.27-alt1
- fixes from rider@

* Tue Nov 22 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.26-alt1
- compatibilituy with policycoreutils 2.4

* Tue Jul 12 2016 Sergey V Turchin <zerg@altlinux.org> 0.0.25-alt1
- set object_r:trusted_exec_t:s0 for /usr/sbin/crond

* Wed Mar 02 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.24-alt1
- allow transition from officer_r:officet_t to generic_r:generic_t

* Mon Sep 21 2015 Andriy Stepanov <stanv@altlinux.ru> 0.0.23-alt1
- Deny untrasted network connections
  Deny write protected data RW USB devices
  Deny write protected files to file-systems

* Mon Feb 16 2015 Andriy Stepanov <stanv@altlinux.ru> 0.0.21-alt1
- Introduce officer_exec_t, utempter screen hard link

* Fri Feb 13 2015 Andriy Stepanov <stanv@altlinux.ru> 0.0.20-alt1
- Add alterator-selinux-users backend to trusted_exec_t

* Wed Apr 23 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.19-alt2
- Remove policycoreutils-gui build requirements

* Fri Apr 18 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.19-alt1
- Add Postgres module

* Fri Apr 11 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.18-alt1
- 20140411

* Thu Apr 10 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.17-alt1
- 20140410

* Tue Apr 08 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.16-alt1
- 20140408

* Mon Apr 07 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.15-alt1
- 20140407

* Thu Apr 03 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.14-alt1
- 20140403

* Fri Feb 07 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.12-alt2
- Remove dependency from kde4libs & systemd

* Wed Jan 22 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.12-alt1
- 20140122

* Fri Jan 17 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.11-alt1
- 20140117 (service's methods)

* Fri Jan 17 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.10-alt1
- 20140117

* Mon Jan 13 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.9-alt1
- Build: 20140113

* Fri Jan 10 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.8-alt1
- Build: 20140110

* Fri Dec 20 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.7-alt1
- Build: 20131220

* Wed Dec 11 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.6-alt1
- Build: 20131211

* Tue Dec 10 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.5-alt1
- Build: 20131210

* Fri Nov 29 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.4-alt1
- Network stuff

* Fri Nov 29 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt5
- Build: 20131129

* Thu Nov 28 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt4
- Build: 20131128

* Wed Nov 27 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt3
- Add more %%ghost files to RPM spec

* Wed Nov 27 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt2
- Update RPM spec

* Mon Nov 25 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt1
- Build: 20131125

* Fri Nov 08 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt8
- Build: 20131108

* Thu Sep 19 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt7
- Build: 20130919

* Tue Sep 17 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt6
- Build: 20130917

* Thu Sep 12 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt5
- Build: 20130912

* Thu Sep 05 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt4
- Build: 20130905

* Thu Jul 25 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt3
- Build: 20130725

* Wed Jun 19 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt2
- Post script for modules

* Wed Jun 19 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt1
- Build: 20130619

* Mon May 20 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt4
- Build: 20130520

* Wed Apr 24 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt3
- Build: 20130425

* Fri Apr 19 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt2
- Build: 20130422

* Wed Apr 17 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt1
- Initial. Build version from: 20130417
