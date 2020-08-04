%define _unpackaged_files_terminate_build 1

%define pkgname	dirsrv
%define groupname %pkgname.target
%define _libexecdir %_usr/libexec

%def_without selinux
%def_with check
%def_with perl
%def_without debug
%def_with cockpit

Name: 389-ds-base
Version: 1.4.1.18
Release: alt1

Summary: 389 Directory Server (base)
License: GPLv3+
Group: System/Servers
# Source-git: https://pagure.io/389-ds-base.git
Url: http://port389.org
Packager: Andrey Cherepanov <cas@altlinux.org>

Source0: %name-%version.tar
%if_with cockpit
Source1: node_modules.tar.gz
%endif
Patch: %name-%version-alt.patch

ExcludeArch: %ix86
BuildRequires(pre): rpm-build-python3

BuildRequires: cracklib-devel
BuildRequires: doxygen
BuildRequires: gcc-c++
%if_with debug
BuildRequires: libasan5
%endif
BuildRequires: libdb4-devel
BuildRequires: libevent-devel
BuildRequires: libicu-devel
BuildRequires: libkrb5-devel
BuildRequires: libldap-devel
BuildRequires: libnet-snmp-devel
BuildRequires: libnspr-devel
BuildRequires: libnss-devel
BuildRequires: libpam0-devel
BuildRequires: libpcre-devel
BuildRequires: libsasl2-devel
BuildRequires: libsystemd-devel

BuildRequires: python3(build_manpages)
BuildRequires: python3(argcomplete)
BuildRequires: python3(ldap)
BuildRequires: python3(packaging)
BuildRequires: python3(six)

BuildRequires: rsync

%if_with cockpit
BuildRequires: npm
%endif

%if_with check
BuildRequires: /proc
BuildRequires: libcmocka-devel
%endif

%if_with perl
BuildRequires: perl-bignum
BuildRequires: perl-devel
BuildRequires: perl-Archive-Tar
BuildRequires: perl-DBM
BuildRequires: perl-Mozilla-LDAP
BuildRequires: perl-NetAddr-IP
%endif
# AutoReq: yes, noperl
%add_perl_lib_path %_libdir/%pkgname/perl
%add_findprov_skiplist %_datadir/%pkgname/script-templates/*
%add_findreq_skiplist %_datadir/%pkgname/script-templates/* %_sbindir/*-%pkgname

# use Python3 everywhere
%add_python3_path %_datadir/gdb/auto-load/
%add_python3_compile_exclude %_datadir/gdb/auto-load/

%add_python3_path %_libdir/%pkgname/python/
%add_python3_compile_exclude %_libdir/%pkgname/python/

# we don't want python gdb
%filter_from_requires /python3(gdb\(\..*\)\?)/d
# requires self
%add_python3_req_skip __main__

Requires: libjemalloc2
Requires: cracklib-words

%description
389 Directory Server is an LDAPv3 compliant server. The base package includes
the LDAP server and command line utilities for server administration.

%package -n 389-ds
Summary: 389 Directory, Administration, and Console Suite
Group: System/Servers
Requires: 389-ds-base
Requires: 389-admin
Requires: idm-console-framework
Requires: 389-console
Requires: 389-ds-console
Requires: 389-ds-console-doc
Requires: 389-admin-console
Requires: 389-admin-console-doc
Requires: 389-dsgw

%description -n 389-ds
The 389 Directory Server, Administration Server, and Console Suite
provide the LDAPv3 server, the httpd daemon used to administer the
server, and the console GUI application used for server and user/group
administration.

%package libs
Summary: Core libraries for 389 Directory Server
Group: System/Libraries
# svrcore has been merged into 389-ds
# https://pagure.io/389-ds-base/issue/49369
Provides: libsvrcore = 4.1.4
Obsoletes: libsvrcore <= 4.1.3
Conflicts: libsvrcore

%description libs
Core libraries for the 389 Directory Server base package. These libraries are
used by the main package and the -devel package. This allows the -devel package
to be installed with just the -libs package and without the main package.

%package devel
Summary: Development libraries for 389 Directory Server
Group: Development/C
Requires: %name = %EVR
# svrcore has been merged into 389-ds
# https://pagure.io/389-ds-base/issue/49369
Provides: libsvrcore-devel = 4.1.4
Obsoletes: libsvrcore-devel <= 4.1.3
Conflicts: libsvrcore-devel

%description devel
Development Libraries and headers for 389 Directory Server.

%package legacy-tools
Summary: Legacy utilities for 389 Directory Server
Group: System/Base
Obsoletes: %name <= 1.4.0.9
Requires: %name = %EVR

%description legacy-tools
Legacy (and deprecated) utilities for 389 Directory Server. This includes
the old account management and task scripts. These are deprecated in favour of
the dscreate, dsctl, dsconf and dsidm tools.

%package -n python3-module-lib389
Summary: A library for accessing, testing, and configuring the 389 Directory Server
BuildArch: noarch
Group: Development/Python3
Requires: nss-utils

%description -n python3-module-lib389
This module contains tools and libraries for accessing, testing, and
configuring the 389 Directory Server.

%if_with cockpit
%package -n cockpit-389-ds
Summary: Cockpit UI Plugin for configuring and administering the 389 Directory Server
BuildArch: noarch
Group: System/Base
Requires: cockpit
%py3_requires lib389

%description -n cockpit-389-ds
A cockpit UI Plugin for configuring and administering the 389 Directory Server
%endif

%prep
%setup
%patch -p1

%if_with cockpit
# node modules are intended for building Cockpit plugin
# and are not utilized in runtime
tar -xzf %SOURCE1 -C "./src/cockpit/389-console"
%endif

grep -qsF 'sysctldir = @prefixdir@/lib/sysctl.d' Makefile.am || exit 1
sed -i 's|sysctldir = .*|sysctldir = %_sysctldir|' Makefile.am

grep -qsr 'LD_PRELOAD=.*/libjemalloc.so.2' || exit 1
grep -rl 'LD_PRELOAD=.*/libjemalloc.so.2' | \
xargs sed -i 's|LD_PRELOAD=.*/libjemalloc.so.2|LD_PRELOAD=libjemalloc.so.2|g'

grep -qsr '/sasl2\( \|"\)' || exit 1
grep -rl '/sasl2\( \|"\)' | xargs sed -i 's/\/sasl2\( \|"\)/\/sasl2-3\1/g'

grep -qsr '/usr/bin/\(ls\|echo\)' || exit 1
grep -rl '/usr/bin/\(ls\|echo\)' | \
xargs sed -i 's/\/usr\(\/bin\/\(ls\|echo\)\)/\1/g'

grep -qs 'saslpath = "/usr/lib/aarch64-linux-gnu"' \
ldap/servers/slapd/ldaputil.c || exit 1
sed -i 's|\(saslpath = "/usr/\)lib\(/aarch64-linux-gnu"\)|\1lib64\2|g' \
ldap/servers/slapd/ldaputil.c

%build
%ifarch mipsel
export LDFLAGS='-latomic'
%endif
%ifarch %e2k
# 1.4.1.8: asm crc32
%add_optflags -U__SSE4_2__
%endif

%autoreconf

%configure  \
	--with-openldap \
        %{subst_with selinux} \
	--localstatedir=/var \
        --libexecdir=%_libexecdir/%pkgname \
 	--enable-autobind \
	--with-systemd \
	--with-systemdsystemunitdir=%_unitdir \
	--with-systemdsystemconfdir=%_sysconfdir/systemd/system \
	--with-systemdgroupname=%groupname \
        --with-tmpfiles-d=%_sysconfdir/tmpfiles.d \
%if_with debug
        --enable-asan \
        --enable-debug \
%endif
        %{?_with_perl:--enable-perl } \
        %{?_with_check:--enable-cmocka } \
        %nil

%make_build

%if_with cockpit
# cockpit plugin
SKIP_AUDIT_CI=yes %make 389-console
%endif

# Python3 bindings
pushd ./src/lib389
%python3_build
popd

# argparse-manpage dynamic man pages have hardcoded man v1 in header,
# need to change it to v8
sed -i  "1s/\"1\"/\"8\"/" ./src/lib389/man/ds{conf,ctl,idm,create}.8

%check
%make check || { cat test-suite.log; exit 1; }

%install
%makeinstall_std

# python stuff
pushd src/lib389
%python3_install
popd

# do not package lib389's tests
rm -r %buildroot%python3_sitelibdir_noarch/lib389/tests
rm %buildroot%python3_sitelibdir_noarch/lib389/topologies.py

mkdir -p %buildroot/{%_lockdir,%_localstatedir,%_logdir}/%pkgname

# for systemd
mkdir -p %buildroot%_sysconfdir/systemd/system/%groupname.wants

# remove libtool and static libs
find %buildroot -type f \( -name "*.la" -o -name "*.a" \) -delete

%if_with perl
# make sure perl scripts have a proper shebang
sed -i 's|#{{PERL-EXEC}}|#!%_bindir/perl|' %buildroot%_datadir/%pkgname/script-templates/template-*.pl
sed -i 's|File::Spec->tmpdir|"/tmp"|g' %buildroot%_libdir/%pkgname/perl/DSCreate.pm
%endif

# move main libraries to common directory
mv %buildroot%_libdir/%pkgname/*.so* %buildroot%_libdir/

# Copy in our docs from doxygen
mkdir -p %buildroot%_man3dir
cp man/man3/* %buildroot%_man3dir

# Fix path to systemctl in scripts
sed -i 's|%_bindir/systemctl|/bin/systemctl|' %buildroot%_sbindir/*-dirsrv

%if_without cockpit
# ends up unpackaged otherwise thus breaking build
rm -f %buildroot%_datadir/metainfo/389-console/org.port389.cockpit_console.metainfo.xml
%endif

%pre
%define _dirsrv_user dirsrv
%define _dirsrv_group dirsrv
%define _dirsrv_home %_localstatedir/dirsrv
/usr/sbin/groupadd -r -f %_dirsrv_group ||:
/usr/sbin/useradd -g %_dirsrv_group -c 'user for 389-ds-base' \
		  -d %_dirsrv_home -s /sbin/nologin -r %_dirsrv_user \
		  > /dev/null 2>&1 ||:

%post
sysctl --system &> /dev/null ||:

%post legacy-tools
%if_with perl
# Upgrade
echo "389-ds: Checking for upgrade"
if ! ( sd_booted && /bin/systemctl --version >/dev/null 2>&1 ); then
    echo "Likely, you are not using systemd. Please, stop all the dirsrv instances."
    echo "Then run an upgrade by %_sbindir/setup-ds.pl -u -s General.UpdateMode=offline"
    exit 0
fi

/bin/systemctl daemon-reload >/dev/null 2>&1 ||:
instances=""
num_inst=0
echo "Looking for Instances in %_sysconfdir/%pkgname"
for dir in %_sysconfdir/%pkgname/slapd-* ; do
    if [ ! -d "$dir" ] ; then continue ; fi
    case "$dir" in *.removed) continue ;; esac
    inst="%pkgname@$(echo $(basename $dir) | sed -e 's/slapd-//')"
    echo "Found Instance $inst"
    if /bin/systemctl -q is-active "$inst"; then
        echo "Instance $inst is running, stopping it"
        if ! /bin/systemctl stop "$inst"; then
            echo "Cannot stop Instance. Please check it and run an upgrade by %_sbindir/setup-ds.pl -u -s General.UpdateMode=offline"
            exit 0
        fi
        instances="$instances $inst"
    else
        echo "Instance $inst is not running"
    fi
    let "num_inst++"
done
if [ "$num_inst" -eq 0 ]; then
    echo "389-ds: There are no Instances to upgrade"
    exit 0
fi
echo "389-ds: Upgrading Instances"
if ! %_sbindir/setup-ds.pl -u -d -l %_logdir/%pkgname/upgrade.log -s \
General.UpdateMode=offline >%_logdir/%pkgname/upgrade.log 2>&1; then
    echo "Upgrade has not been completed successfully. Please check log file %_logdir/%pkgname/upgrade.log and run an upgrade by %_sbindir/setup-ds.pl -u -s General.UpdateMode=offline"
    exit 0
fi

for inst in $instances; do
    echo "Restarting Instance $inst"
    /bin/systemctl start "$inst" ||:
done

echo "389-ds: Upgrade has been completed successfully"
%endif
%post_service %pkgname-snmp

%preun
# Removal
if [ $1 -eq 0 ]; then
    # disabling all templated units
    /bin/systemctl -q disable %pkgname@
    # remove templated units
    rm -rf %_sysconfdir/systemd/system/%groupname.wants/* >/dev/null 2>&1 ||:
    # stopping by mask
    /bin/systemctl stop %pkgname@*.service
fi
%preun_service %pkgname-snmp

%ifnarch %e2k
# FIXME: got no 389-admin/console/dsgw and no idm-console-framework just yet
%files -n 389-ds
%endif

%files
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README.md
%dir %_sysconfdir/%pkgname
%dir %_sysconfdir/%pkgname/schema
%config(noreplace)%_sysconfdir/%pkgname/schema/*.ldif
%dir %_sysconfdir/%pkgname/config
%dir %_sysconfdir/systemd/system/%groupname.wants
%config(noreplace)%_sysconfdir/%pkgname/config/slapd-collations.conf
%config(noreplace)%_sysconfdir/%pkgname/config/certmap.conf
%config(noreplace)%_sysconfdir/%pkgname/config/ldap-agent.conf
%dir %_datadir/%pkgname
%_datadir/%pkgname/data/
%_datadir/%pkgname/inf/
%_datadir/%pkgname/mibs/
%_datadir/%pkgname/schema/
%_unitdir/dirsrv-snmp.service
%_unitdir/dirsrv.target
%_unitdir/dirsrv@.service
%dir %_unitdir/dirsrv@.service.d
%_unitdir/dirsrv@.service.d/custom.conf

%_bindir/dbscan
%_bindir/ds-replcheck
%_bindir/ds-logpipe.py
%_bindir/ldclt
%_bindir/logconv.pl
%_bindir/pwdhash
%_bindir/readnsstate

%_sbindir/bak2db
%_sbindir/db2bak
%_sbindir/db2index
%_sbindir/db2ldif
%_sbindir/dbverify
%_sbindir/ldap-agent
%_sbindir/ldif2db
%_sbindir/ldif2ldap
%_sbindir/ns-slapd
%_sbindir/restart-dirsrv
%_sbindir/start-dirsrv
%_sbindir/status-dirsrv
%_sbindir/stop-dirsrv
%_sbindir/upgradedb
%_sbindir/vlvindex

%dir %_libexecdir/%pkgname
%_libexecdir/%pkgname/ds_systemd_ask_password_acl
%dir %_libdir/%pkgname/python
%_libdir/%pkgname/python/*.py*
%dir %_libdir/%pkgname/plugins
%_libdir/%pkgname/plugins/*.so
%_datadir/gdb/auto-load/*
%_sysctldir/70-dirsrv.conf
%dir %_localstatedir/%pkgname
%dir %_logdir/%pkgname
%ghost %dir %_lockdir/%pkgname
%_man1dir/dbscan.1.*
%_man1dir/ds-replcheck.1.*
%_man1dir/ds-logpipe.py.1.*
%_man1dir/ldclt.1.*
%_man1dir/logconv.pl.1.*
%_man1dir/pwdhash.1.*
%_man1dir/readnsstate.1.*
%_man1dir/ldap-agent.1.*
%_man8dir/ldif2ldap.8.*
%_man8dir/ns-slapd.8.*
%_man8dir/bak2db.8.*
%_man8dir/db2bak.8.*
%_man8dir/db2index.8.*
%_man8dir/db2ldif.8.*
%_man8dir/dbverify.8.*
%_man8dir/ldif2db.8.*
%_man8dir/restart-dirsrv.8.*
%_man8dir/start-dirsrv.8.*
%_man8dir/status-dirsrv.8.*
%_man8dir/stop-dirsrv.8.*
%_man8dir/upgradedb.8.*
%_man8dir/vlvindex.8.*
%_man5dir/99user.ldif.5.*
%_man5dir/certmap.conf.5.*
%_man5dir/slapd-collations.conf.5.*
%_man5dir/dirsrv.5.*
%_man5dir/dirsrv.systemd.5.*

%files devel
%_includedir/%pkgname/
%_includedir/svrcore.h
%_libdir/libsvrcore.so
%_libdir/libslapd.so
%_libdir/libns-dshttpd.so
%_libdir/libnunc-stans.so
%_libdir/libsds.so
%_libdir/libldaputil.so
%_pkgconfigdir/dirsrv.pc
%_pkgconfigdir/libsds.pc
%_pkgconfigdir/svrcore.pc
%_pkgconfigdir/nunc-stans.pc
%_man3dir/*.3.*

%files libs
%dir %_libdir/%pkgname
%_libdir/libsvrcore.so.*
%_libdir/libns-dshttpd-*.so
%_libdir/libnunc-stans.so.*
%_libdir/libsds.so.*
%_libdir/libslapd.so.*
%_libdir/libldaputil.so.*

%files legacy-tools
%_bindir/infadd
%_bindir/ldif
%_bindir/migratecred
%_bindir/mmldif
%_bindir/rsearch

%_sbindir/dbmon.sh
%_sbindir/dn2rdn
%_sbindir/monitor
%_sbindir/restoreconfig
%_sbindir/saveconfig
%_sbindir/suffix2instance
%_sbindir/upgradednformat

%_libexecdir/%pkgname/ds_selinux_enabled
%_libexecdir/%pkgname/ds_selinux_port_query

%_man1dir/infadd.1.*
%_man1dir/ldif.1.*
%_man1dir/migratecred.1.*
%_man1dir/mmldif.1.*
%_man1dir/rsearch.1.*
%_man8dir/dbmon.sh.8.*
%_man8dir/dn2rdn.8.*
%_man8dir/monitor.8.*
%_man8dir/restoreconfig.8.*
%_man8dir/saveconfig.8.*
%_man8dir/suffix2instance.8.*
%_man8dir/upgradednformat.8.*

%if_with perl
%config(noreplace)%_sysconfdir/%pkgname/config/template-initconfig
%_man5dir/template-initconfig.5.*
%dir %_datadir/%pkgname/properties
%_datadir/%pkgname/properties/ns-slapd.properties
%_datadir/%pkgname/properties/*.res
%_datadir/%pkgname/script-templates
%_datadir/%pkgname/updates

%_bindir/cl-dump
%_bindir/cl-dump.pl
%_bindir/dbgen.pl
%_bindir/repl-monitor
%_bindir/repl-monitor.pl

%_sbindir/bak2db.pl
%_sbindir/cleanallruv.pl
%_sbindir/db2bak.pl
%_sbindir/db2index.pl
%_sbindir/db2ldif.pl
%_sbindir/fixup-linkedattrs.pl
%_sbindir/fixup-memberof.pl
%_sbindir/ldif2db.pl
%_sbindir/migrate-ds.pl
%_sbindir/ns-accountstatus.pl
%_sbindir/ns-activate.pl
%_sbindir/ns-inactivate.pl
%_sbindir/ns-newpwpolicy.pl
%_sbindir/remove-ds.pl
%_sbindir/schema-reload.pl
%_sbindir/setup-ds.pl
%_sbindir/syntax-validate.pl
%_sbindir/usn-tombstone-cleanup.pl
%_sbindir/verify-db.pl

%_man1dir/dbgen.pl.1.*
%_man1dir/repl-monitor.1.*
%_man1dir/repl-monitor.pl.1.*
%_man1dir/cl-dump.1.*
%_man1dir/cl-dump.pl.1.*
%_man8dir/bak2db.pl.8.*
%_man8dir/cleanallruv.pl.8.*
%_man8dir/db2bak.pl.8.*
%_man8dir/db2index.pl.8.*
%_man8dir/db2ldif.pl.8.*
%_man8dir/fixup-linkedattrs.pl.8.*
%_man8dir/fixup-memberof.pl.8.*
%_man8dir/ldif2db.pl.8.*
%_man8dir/migrate-ds.pl.8.*
%_man8dir/ns-accountstatus.pl.8.*
%_man8dir/ns-activate.pl.8.*
%_man8dir/ns-inactivate.pl.8.*
%_man8dir/ns-newpwpolicy.pl.8.*
%_man8dir/remove-ds.pl.8.*
%_man8dir/schema-reload.pl.8.*
%_man8dir/setup-ds.pl.8.*
%_man8dir/syntax-validate.pl.8.*
%_man8dir/usn-tombstone-cleanup.pl.8.*
%_man8dir/verify-db.pl.8.*

%_libdir/%pkgname/perl/
%endif

%files -n python3-module-lib389
%_sbindir/dsconf
%_sbindir/dscontainer
%_sbindir/dscreate
%_sbindir/dsctl
%_sbindir/dsidm
%_man8dir/dsconf.8.*
%_man8dir/dscreate.8.*
%_man8dir/dsctl.8.*
%_man8dir/dsidm.8.*
%python3_sitelibdir_noarch/lib389/
%python3_sitelibdir_noarch/lib389-*-py%_python3_version.egg-info/

%if_with cockpit
%files -n cockpit-389-ds
%dir %_datadir/metainfo/389-console
%_datadir/metainfo/389-console/org.port389.cockpit_console.metainfo.xml
%dir %_datadir/cockpit/389-console
%_datadir/cockpit/389-console/manifest.json
%_datadir/cockpit/389-console/*.html
%_datadir/cockpit/389-console/*.js
%_datadir/cockpit/389-console/*.js.map
%_datadir/cockpit/389-console/css/
%endif

%changelog
* Fri Apr 17 2020 Stanislav Levin <slev@altlinux.org> 1.4.1.18-alt1
- 1.4.1.16 -> 1.4.1.18.

* Mon Mar 23 2020 Stanislav Levin <slev@altlinux.org> 1.4.1.16-alt1
- 1.4.1.13 -> 1.4.1.16.

* Tue Jan 14 2020 Stanislav Levin <slev@altlinux.org> 1.4.1.13-alt1
- 1.4.1.12 -> 1.4.1.13.

* Mon Dec 09 2019 Stanislav Levin <slev@altlinux.org> 1.4.1.12-alt1
- 1.4.1.10 -> 1.4.1.12.

* Sun Nov 17 2019 Michael Shigorin <mike@altlinux.org> 1.4.1.10-alt2
- Fixed cockpit knob.
- Enabled parallel build.
- E2K:
  + disable SSE4.2 (crc32 assembly code needs porting);
  + disable 389-ds metapackage for now (deps lacking).

* Thu Nov 14 2019 Stanislav Levin <slev@altlinux.org> 1.4.1.10-alt1
- 1.4.1.9 -> 1.4.1.10 (fixes: CVE-2019-14824).

* Tue Nov 05 2019 Stanislav Levin <slev@altlinux.org> 1.4.1.9-alt1
- 1.4.1.8 -> 1.4.1.9.

* Fri Sep 27 2019 Stanislav Levin <slev@altlinux.org> 1.4.1.8-alt1
- 1.4.1.7 -> 1.4.1.8.

* Tue Sep 24 2019 Stanislav Levin <slev@altlinux.org> 1.4.1.7-alt1
- 1.4.1.6 -> 1.4.1.7.

* Mon Aug 05 2019 Stanislav Levin <slev@altlinux.org> 1.4.1.6-alt1
- 1.4.1.2 -> 1.4.1.6.

* Wed Jul 10 2019 Ivan A. Melnikov <iv@altlinux.org> 1.4.1.2-alt2
- Link with libatomic on mipsel.

* Tue May 21 2019 Stanislav Levin <slev@altlinux.org> 1.4.1.2-alt1
- 1.4.1.1 -> 1.4.1.2.

* Tue Jan 22 2019 Stanislav Levin <slev@altlinux.org> 1.4.1.1-alt1
- 1.3.9.0 -> 1.4.1.1.
- Stopped build for i586 arch.

* Wed Nov 28 2018 Stanislav Levin <slev@altlinux.org> 1.3.9.0-alt3
- Fixed initialization of plugin's hashtable.
- Dropped useless Provides of python 389-ds-tests.

* Thu Nov 08 2018 Stanislav Levin <slev@altlinux.org> 1.3.9.0-alt2
- Added enforced upgrade.

* Thu Nov 01 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.9.0-alt1
- New version.

* Thu Oct 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.8.10-alt1
- New version.
- Security fixes:
  + Ticket 49969 - DOS caused by malformed search operation
  + Ticket 49937 - Log buffer exceeded emergency logging msg is not thread-safe

* Fri Oct 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.8.8-alt3
- Remove python2.7(gdb) requirement.

* Thu Sep 20 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.3.8.8-alt2
- autoreconf moved inot %%build

* Thu Aug 30 2018 Stanislav Levin <slev@altlinux.org> 1.3.8.8-alt1
- 1.3.8.5 -> 1.3.8.8.
- Fix build with new openssl1.1.

* Fri Jul 27 2018 Stanislav Levin <slev@altlinux.org> 1.3.8.5-alt1
- 1.3.7.1 -> 1.3.8.5
- Build package for Python3

* Mon Nov 27 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.7.1-alt2
- Add dirsrv user during pre install step (thanks slev@) (ALT #34240)

* Wed Jul 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.7.1-alt1
- New version

* Wed Apr 26 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.7.0-alt1
- New version

* Mon Apr 24 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.6.4-alt1
- New version
- Fix path to systemctl in scripts (ALT #33392)

* Mon Mar 27 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.6.3-alt1
- New version
- Fix type conflict for snmptrap_oid and snmptrap_oid_len (ALT #33282)

* Sat Mar 18 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.6.2-alt1
- New version

* Wed Nov 02 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.6.1-alt1
- new version 1.3.6.1

* Sun Oct 16 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.5.14-alt1
- new version 1.3.5.14

* Thu Aug 11 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.5.13-alt1
- new version 1.3.5.13

* Thu Jul 21 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.5.11-alt1
- new version 1.3.5.11

* Mon Jul 04 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.5.10-alt1
- new version 1.3.5.10

* Sun Jun 19 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.5.6-alt1
- new version 1.3.5.6

* Fri Jun 10 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.5.4-alt2
- Fix 64-bit architecture check

* Tue Jun 07 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.5.4-alt1
- New version

* Thu May 12 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.5.3-alt1
- New version

* Mon Mar 28 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.5.1-alt1
- New version

* Thu Feb 18 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.4.8-alt1
- New version

* Thu Jan 28 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.4.7-alt1
- New version
- Conflicts: lprng

* Sun Jan 17 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.4.6-alt1
- New version

* Mon Nov 23 2015 Andrey Cherepanov <cas@altlinux.org> 1.3.4.5-alt1
- New version

* Thu Oct 15 2015 Andrey Cherepanov <cas@altlinux.org> 1.3.4.4-alt1
- New version
- Make 389-ds as metapackage for complete suite install
- Simplify spec
- SELinux support is disabled

* Wed Nov 05 2014 Michael Shigorin <mike@altlinux.org> 1.3.2.15-alt3.e9f86dab
- cherry-picked 9df31ed to fix https://fedorahosted.org/389/ticket/47589

* Mon May 19 2014 Timur Aitov <timonbl4@altlinux.org> 1.3.2.15-alt2.e9f86dab
- git e9f86dab

* Mon Apr 28 2014 Timur Aitov <timonbl4@altlinux.org> 1.3.2.15-alt1
- 1.3.2.15

* Tue Sep 17 2013 Sergey Y. Afonin <asy@altlinux.ru> 1.2.10.12-alt1.qa1.1
- NMU: rebuilt with cyrus-sasl 2.1.26

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.2.10.12-alt1.qa1
- NMU: rebuilt with libicuuc.so.50.

* Mon Jul 09 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.10.12-alt1
- 1.2.10.12

* Fri Jul 06 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.10.0-alt1
- 1.2.10.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.9.10-alt1.1
- Rebuild with Python-2.7

* Sat Sep 10 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.9.10-alt1
- 1.2.9.10

* Fri Aug 05 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.9.4-alt1
- 1.2.9.4

* Tue Jun 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.8.3-alt2
- rebuild with openldap-2.4.25

* Fri May 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.8.3-alt1
- 1.2.8.3

* Thu May 05 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.8.1-alt2
- fix build

* Mon Apr 11 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.8.1-alt1
- 1.2.8.1

* Wed Mar 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7.5-alt4
- repair build

* Wed Feb 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7.5-alt3
- CVE-2011-0019

* Thu Feb 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7.5-alt2
- build with openldap instead of mozldap

* Thu Dec 16 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7.5-alt1
- 1.2.7.5

* Mon Dec 13 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7.4-alt1
- 1.2.7.4

* Wed Dec 08 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7.3-alt1
- 1.2.7.3

* Mon Dec 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7.2-alt1
- 1.2.7.2
- rebuild with icu-4.6

* Fri Nov 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7.1-alt1
- 1.2.7.1

* Mon Nov 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7-alt1
- 1.2.7

* Tue Sep 28 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.6.1-alt1
- 1.2.6.1

* Wed Sep 08 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Tue Jul 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.6-alt0.rc3.1
- 1.2.6-rc3

* Thu Jun 17 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.5-alt2
- CVE-2010-2222

* Wed Jan 13 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Tue Nov 10 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Wed Oct 21 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.3-alt1
- 1.2.3
- remove /var/run/fedora-ds and /var/lock/fedora-ds from package
- post/preun_server fedora-ds-snmp

* Mon Oct 12 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.2-alt3
- fix build (add libicu-devel to buildreq)

* Wed Sep 23 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.2-alt2
- use autoreq (patched rpm-build-perl required)
- merge upstream de006310

* Mon Aug 24 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Mon Aug 17 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt2
- merge upstream 1.2.1

* Thu May 21 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Sat Apr 04 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0-alt2
- disabled pam_passthru plugin

* Fri Apr 03 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Wed Nov 05 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.3-alt1
- 1.1.3, libdb4.7

* Sat Sep 06 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Fri Aug 01 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt1
- 1.1.1
- set dependency to libdb4.4 (rebuild with 4.7 problems)
- fix #16370

* Wed May 07 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt3
- updated to fedora

* Sat Jan 26 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt2
- Fix libcollation and libacl plugin packaging (Bug #14173)

* Tue Jan 08 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1
- Fedora-DS 1.1 Final release
- Resolves bug 193724: "nested" filtered roles result in deadlock
- Resolves bug 367671: verify-db.pl : can't find dbverify
- Resolves bug 339041: migration : encryption key entries missing when source is 6.21
- Resolves bug 345711: migration : ignore idl switch value in 6.21 and earlier
- Resolves bug 197997: PTA config parsing broken
- Resolves bug 383141: listenhost: hostname associated with multiple addresses
- Resolves bug 388021: MMR breaks from master that has been reinited
- Resolves bug 371771: '.' (dot) in the server ID
- Resolves bug 345671: clu test failures
- Resolves bug 371751: verify-db.pl : can't find dbverify
- Resolves bug 238649: Hide nsslapd-db-transaction
- Resolves bug 316281: db2bak fails if the archive path exists and ends with '/'
- Resolves bug 237040: Remove obsolete makefiles
- Resolves bug 229576: clean up template-scriptname which is derived from template-scriptname.in
- Resolves bug 403351: LongDuration: Error log Rotation test suite causes slapd hang
- Resolves bug 231093: db2bak: crash bug
- Resolves bug 174776: Multiple restores from a non-existant directory could wipe out database
- Resolves bug 403751: command line scripts fine tuning
- Resolves bug 400421: unable to restart configDS via console
- Resolves bug 424381: migrate-ds-admin.pl script - not working
- Resolves bug 425861: Instance creation through console is broken
- Resolves bug 425849: migrate-ds-admin.pl spins at 100 cpu
- Resolves bug 297221: rhds71 Malformed Dynamic Authorization Group makes Directory Server Crash

* Tue Oct 30 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20071030
- CVS snapshot 20071030
- Resolves bug 305121: Server hangs when adding a group with two password entries
- Resolves bug 325281: Install SNMP subagent mibs.
- Resolves bug 244475: crash at startup with new ldap sdk on 64-bit platform
- migration starts instances now
- Clean up setup dialog text
- removed obsolete schema
- Resolves bug 288291: add an view object inside a view object that has an improper nsviewfilter crashes the server
- Resolves bug 238630: Remove changelog db file when replica config is removed.
- Resolves bug 193724: "nested" filtered roles result in deadlock
- Resolves bug 330121: uuid generator truncates clock_seq_hi_and_reserved field
- Resolves bug 328741: Ensure that we NULL terminate strings properly when processing config file settings.
- Resolves bug 327091: Migration/Upgrade fails when it's from 6.21 to 8.0 on the same OS/architecture
- Resolves bug 335081: Don't add mailGroup objectclass when sync'ing new group entries from AD.
- Resolves bug 185602: Netscape Console allows instance directory to be set as change log
- Resolves bug 219587: Fixed small non-recurring memory leak at startup.
- Resolves bug 333291: Do not allow direct migration if the source db index has old IDL format
- Resolves bug 250179: tmpwatch whacks stats
- Resolves bug 338611: Sleep longer when waiting for ldap-agent to start.
- Resolves bug 336871: Look for infadd data files in TEMPLATEDIR.
- Resolves bug 232910: ACI targetattr list parser is whitespace sensitive
- Resolves bug 297221: rhds71 Malformed Dynamic Authorization Group makes Directory Server Crash
- Resolves bug 336871: infadd tool won't start. Fails to load data file
- Resolves bug 338991: obsolete values migrated to target instance
- Resolves bug 339041: migration : encryption key entries missing when source is 6.21
- Resolves bug 336881: qualify warning message when cert8.db is missing

* Mon Oct 29 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20071008.1
- Rebuild with new ICU

* Mon Oct 08 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20071008
- CVS snapshot 20071008

* Mon May 28 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20070528
- Git clone, upstream update

* Thu Mar 22 2007 Stanislav Ievlev <inger@altlinux.org> 1.1.0-alt0.20070322
- Initial release

* Wed Mar  1 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.2-1
- Added admserv-conf-tmpl.patch and admserv-conf-admpw.patch to fix the use of admpw for basic auth

* Wed Feb 22 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.2-1
- Add patch to fix admin server httpd module load order; you
- must now run setup after an upgrade; copy in the new 00core.ldif
- schema file to the server instances

* Tue Dec  6 2005 Rich Megginson <rmeggins@redhat.com> - 1.0.1-1
- Use nosp version instead of gen version to get patch version numbers
- Patch the admin server in the post install section
- Remove the unnecessary log files after setup so they aren't packaged

* Wed Nov 09 2005 Nathan Kinder <nkinder@redhat.com> 7.1-2
- Changed cyrus-sasl dependency to >= 2.1.15 for RHEL3 compatibility

* Fri Nov 04 2005 Noriko Hosoi <nhosoi@redhat.com> 7.1-2
- Added a dependency: cyrus-sasl >= 2.1.19

* Wed Sep 14 2005 Nathan Kinder <nkinder@redhat.com> 7.1-2
- Added a dependency on the java-1.4.2-ibm package

* Tue May 10 2005 Richard Megginson <rmeggins@redhat.com> 7.1-2
- Change release to 2

* Fri Apr  8 2005 Rich Megginson <rmeggins@redhat.com> 7.1-1
- check for last version removal in preun

* Tue Apr  5 2005 Rich Megginson <rmeggins@redhat.com> 7.1-1
- make rpm name .flavor.rpm - flavor must be defined in rpmbuild

* Tue Apr  5 2005 Rich Megginson <rmeggins@redhat.com> 7.1-1
- Removed all of the setup and build stuff - just use the regular DS build process for that

* Tue Apr  5 2005 Rich Megginson <rmeggins@redhat.com> 7.1-1
- use platform specific packaging directory; add preun to do uninstall

* Fri Apr  1 2005 Rich Megginson <rmeggins@redhat.com> 7.1-1
- use setup -q to suppress tar output

* Tue Mar 29 2005 Richard Megginson <rmeggins@redhat.com> 7.1-1
- use INTERNAL_BUILD=1 for internal builds - change rev to 1

* Tue Mar  8 2005 Richard Megginson <rmeggins@redhat.com> 7.1-0
- use ${prefix} instead of /opt/ldapserver - prefix is defined as /opt/%name

* Thu Jan 20 2005 Richard Megginson <rmeggins@redhat.com>
- Initial build.
