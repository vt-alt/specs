%def_with doc

Name: cifs-utils
Version: 6.11
Release: alt1

Summary: Utilities for doing and managing mounts of the Linux CIFS filesystem
License: GPLv3+
Group: System/Kernel and hardware

Url: https://wiki.samba.org/index.php/LinuxCIFS_utils
Source: %name-%version.tar

# Patch from Fedora
Patch1: cifs-utils-destdir.patch

Patch2: cifs-utils-alt-python3.patch

BuildRequires(pre): rpm-macros-pam0
BuildRequires: libcap-ng-devel libkeyutils-devel libkrb5-devel libtalloc-devel libwbclient-devel libpam-devel
BuildRequires: python-module-docutils
Requires: keyutils
Conflicts: samba-client < 3.6.0-alt1

%description
This is the release version of cifs-utils, a package of utilities for
doing and managing mounts of the Linux CIFS filesystem. These programs
were originally part of Samba, but have now been split off into a
separate package.

%package devel
Summary: Files needed for building plugins for cifs-utils
Group: Development/C

%description devel
The SMB/CIFS protocol is a standard file sharing protocol widely deployed
on Microsoft Windows machines. This package contains the header file
necessary for building ID mapping plugins for cifs-utils.

%package -n pam_cifscreds
Summary: PAM module to manage NTLM credentials in kernel keyring
Group: System/Base

%description -n pam_cifscreds
The pam_cifscreds PAM module is a tool for automatically adding
credentials (username and password) for the purpose of establishing
sessions in multiuser mounts.

When a cifs filesystem is mounted with the "multiuser" option, and does
not use krb5 authentication, it needs to be able to get the credentials
for each user from somewhere. The pam_cifscreds module can be used to
provide these credentials to the kernel automatically at login.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure \
	--with-pamdir=/%_lib/security \
	--with-idmap-plugin=%_libdir/%name/idmap-plugin
%make_build

%install
install -d %buildroot/sbin
%makeinstall_std
mkdir -p %buildroot%_sysconfdir/request-key.d
install -pm644 contrib/request-key.d/cifs.{idmap,spnego}.conf %buildroot%_sysconfdir/request-key.d/

# Add alternatives for idmap-plugin
mkdir -p %buildroot/%_altdir
printf '%_libdir/%name/idmap-plugin\t%_libdir/%name/idmapwb.so\t10\n' > %buildroot/%_altdir/cifs-idmap-plugin-idmapwb

%files
/sbin/mount.cifs
/sbin/mount.smb3
%_sbindir/cifs.upcall
%_sbindir/cifs.idmap
%_bindir/cifscreds
%_bindir/getcifsacl
%_bindir/setcifsacl
%_bindir/smb2-quota
%_bindir/smbinfo
%dir %_libdir/%name
%_libdir/%name/idmapwb.so
%_altdir/cifs-idmap-plugin-idmapwb
%if_with doc
%_man8dir/cifs.idmap.8*
%_man8dir/cifs.upcall.8*
%_man8dir/mount.cifs.8*
%_man8dir/mount.smb3.8*
%_man8dir/idmapwb.8.*
%_man1dir/getcifsacl.1*
%_man1dir/setcifsacl.1*
%_man1dir/cifscreds.1*
%_man1dir/smb2-quota.1*
%_man1dir/smbinfo.1*
%endif
%doc AUTHORS ChangeLog README
%config(noreplace) %_sysconfdir/request-key.d/cifs.idmap.conf
%config(noreplace) %_sysconfdir/request-key.d/cifs.spnego.conf

%files devel
%_includedir/*

%files -n pam_cifscreds
%_pam_modules_dir/pam_cifscreds.so
%if_with doc
%_man8dir/pam_cifscreds.*
%endif

%changelog
* Thu Nov 19 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.11-alt1
- Updated to upstream version 6.11 (Fixes: CVE-2020-14342).

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 6.8-alt4
- NMU: remove rpm-build-ubt from BR:

* Thu Mar 28 2019 Michael Shigorin <mike@altlinux.org> 6.8-alt3
- introduced doc knob (on by default) to work around ftbfs on e2k
- added explicit BR(pre): rpm-macros-pam0
- dropped %%ubt macro
- minor spec cleanup

* Mon Sep 24 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 6.8-alt2%ubt
- build fixed

* Tue Aug 21 2018 Evgeny Sinelnikov <sin@altlinux.org> 6.8-alt1%ubt
- Update to latest release 6.8

* Mon Apr 10 2017 Evgeny Sinelnikov <sin@altlinux.ru> 6.7-alt1%ubt
- 6.7
- Build package with unified build tag aka ubt macros

* Tue Jun 14 2016 Alexey Shabalin <shaba@altlinux.ru> 6.5-alt1
- 6.5

* Mon Jul 28 2014 Alexey Shabalin <shaba@altlinux.ru> 6.4-alt1
- 6.4
- revert "move cifs.upcall to /sbin"

* Mon Feb 03 2014 Alexey Shabalin <shaba@altlinux.ru> 6.3-alt1
- 6.3
- add pam_cifscreds package
- add devel package

* Tue Apr 02 2013 Andrey Cherepanov <cas@altlinux.org> 5.7-alt2
- Build with renamed libwbclient-devel

* Wed Oct 31 2012 Michael Shigorin <mike@altlinux.org> 5.7-alt1
- 5.7 (closes: #27909)

* Sat Apr 28 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 5.4-alt1
- 5.4 (cifs-utils-5.3-19-ga91fb06)

* Tue Sep 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1-alt1
- 5.1

* Mon Aug 15 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0-alt3
- conflicts with samba-client < 3.6.0-alt1

* Mon Aug 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0-alt2
- CVE-2011-2724
- move cifs.upcall to /sbin
- build with libpcap and libwbclient

* Mon Aug 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0-alt1
- 5.0

* Sun Mar 20 2011 Michael Shigorin <mike@altlinux.org> 4.9-alt1
- 4.9
- fix BuildRequires:

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 4.8-alt1
- 4.8 (thanks force@)

* Wed Mar 31 2010 Michael Shigorin <mike@altlinux.org> 4.1-alt2
- added Conflicts: samba-client (should be removed after
  that package drops these files as anticipated)

* Wed Mar 31 2010 Michael Shigorin <mike@altlinux.org> 4.1-alt1
- built for ALT Linux
  + thanks ab@ for advice
  + somewhat based on Debian/Fedora/openSUSE packages
