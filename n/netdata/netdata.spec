# Please, update here commit id for release, from $ git log v1.5.0 -n 1 --format="%H"
%define release_commit 2c4146832061635273d153a5174c85fb1d967d57

%define netdatauser netdata
Name: netdata
Version: 1.16.0
Release: alt1

Summary: Real-time performance monitoring, done right!

License: GPLv3+
Group: Monitoring
Url: http://netdata.firehol.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/firehol/netdata.git
Source: %name-%version.tar

Source1: netdata.logrotate

# manually removed: python-module-google python-module-mwlib python3-dev python3-module-yieldfrom python3-module-zope ruby ruby-stdlibs
# Automatically added by buildreq on Fri Aug 05 2016
# optimized out: perl pkg-config python-base python-modules python3 python3-base
BuildRequires: libuuid-devel zlib-devel bash4 libcups-devel

Requires: bash4

BuildRequires: rpm-macros-intro-conflicts
BuildRequires: rpm-build-intro >= 2.1.1

%if_with nfacct
BuildRequires: libmnl-devel
BuildRequires: libnetfilter_acct-devel
%endif

AutoReq: yes, noshell

%add_findreq_skiplist %_libexecdir/%name/plugins.d/*.plugin
%add_findreq_skiplist %_libexecdir/%name/charts.d/*.sh

# FIXME netdata-postgres: Depends: python2.7(bases) but it is not installable
%add_python_req_skip bases
# python.d/python_modules/pyyaml3/__init__.py: invalid syntax (line 284)
#add_findreq_skiplist %_libexecdir/%name/python.d/python_modules/*/*.py
#if %_vendor != "alt"
#global __python %__python3
#endif

%description
netdata is the fastest way to visualize metrics. It is a resource
efficient, highly optimized system for collecting and visualizing any
type of realtime timeseries data, from CPU usage, disk activity, SQL
queries, API calls, web site visitors, etc.

netdata tries to visualize the truth of now, in its greatest detail,
so that you can get insights of what is happening now and what just
happened, on your systems and applications.

%package postgres
Summary: PostgreSQL module for %name
Group: Development/Python
Requires: %name = %EVR

%description postgres
PostgreSQL module for %name.

%prep
%setup

# https://bugzilla.altlinux.org/show_bug.cgi?id=32663
%if %_vendor == "alt"
for i in plugins.d/*.plugin plugins.d/*.sh charts.d/*.sh ; do
	test -s "$i" || continue
	%__subst "s|^#!/usr/bin/env bash$|#!/bin/bash4|g" "$i"
	%__subst "s|^#!/bin/bash$|#!/bin/bash4|g" "$i"
done
%endif

%build
%autoreconf
%configure \
	--docdir=%_docdir/%name-%version \
	--with-zlib \
	--with-math \
	%{?with_nfacct:--enable-plugin-nfacct} \
	--with-user=netdata

# TODO
#%ifarch i586 x86_64
#        --enable-plugin-freeipmi \
#%endif

%make_build

%install
%makeinstall_std

# drop python3 version
rm -rf %buildroot%_libexecdir/netdata/python.d/python_modules/pyyaml3/

mkdir -p %buildroot%_sysconfdir/%name/
install -m 644 -p system/netdata.conf %buildroot%_sysconfdir/%name/netdata.conf

# This should be opt-in, not opt-out. I do not believe most users would agree
# with sending usage data to Google Analytics, whether anonymized or not.
# Hence, disable statistics by default.
touch %buildroot%_sysconfdir/%name/.opt-out-from-anonymous-statistics

#mkdir -p %buildroot%_sysconfdir/%name/charts.d/

mkdir -p %buildroot%_logrotatedir/
%if %_vendor == "alt"
install -m 644 -p %SOURCE1 %buildroot%_logrotatedir/%name
%else
install -m 644 -p system/netdata.logrotate %buildroot%_logrotatedir/%name
%endif

find %buildroot -name .keep | xargs rm

install -d %buildroot%_unitdir/
install -m 644 -p system/netdata.service %buildroot%_unitdir/netdata.service

# /run vs /var/run workaround
#__subst "s|/run/netdata/netdata.pid|%_runtimedir/netdata/netdata.pid|" %buildroot%_unitdir/netdata.service

# fill with original commit id for %version release
echo "%release_commit" > %buildroot%_datadir/%name/web/version.txt

%pre
# TODO
#groupadd %netdatauser
#useradd %netdatauser -g %netdatauser -c netdata -s /sbin/nologin -d /
getent group %netdatauser >/dev/null || groupadd -r %netdatauser
getent passwd %netdatauser >/dev/null || useradd -r -g %netdatauser -c "%netdatauser user" -s /sbin/nologin -d / %netdatauser

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md LICENSE REDISTRIBUTED.md
%attr(0700,%netdatauser,%netdatauser) %dir %_cachedir/%name/
%attr(0770,root,%netdatauser) %dir %_logdir/%name/
%attr(0700,%netdatauser,%netdatauser) %dir %_sharedstatedir/%name/
%dir %_sysconfdir/%name/
%_sysconfdir/%name/.opt-out-from-anonymous-statistics
%_sysconfdir/%name/edit-config
#config(noreplace) %_sysconfdir/%name/netdata.conf
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/*.conf
#dir %_sysconfdir/%name/node.d/
#config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/node.d/*
%dir %_sysconfdir/%name/health.d/
#config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/health.d/*.conf
%dir %_sysconfdir/%name/python.d/
#config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/python.d/*.conf
#dir %_sysconfdir/%name/charts.d/
#config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/statsd.d/*.conf
%dir %_sysconfdir/%name/statsd.d/
#config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/charts.d/*.conf
%config(noreplace) %_logrotatedir/%name
%_sbindir/%name
%_unitdir/netdata.service
%dir %_libexecdir/%name/
%_libexecdir/%name/charts.d/
%_libexecdir/%name/node.d/
%_libexecdir/%name/plugins.d/
%_libexecdir/%name/python.d/
%exclude %_libexecdir/%name/python.d/postgres.chart.py
%dir %_datadir/%name
%dir %_libdir/%name/
%_libdir/%name/conf.d/

# override defattr for web files (see netdata.conf for web access user/group)
%defattr(644,root,%netdatauser,755)
%_datadir/%name/web/

%files postgres
%_libexecdir/%name/python.d/postgres.chart.py

%changelog
* Tue Jul 09 2019 Vitaly Lipatov <lav@altlinux.ru> 1.16.0-alt1
- new version 1.16.0 (with rpmrb script)

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1.15.0-alt1
- new version 1.15.0 (with rpmrb script)

* Fri May 17 2019 Vitaly Lipatov <lav@altlinux.ru> 1.14.0-alt1
- new version 1.14.0 (with rpmrb script)

* Thu Mar 21 2019 Vitaly Lipatov <lav@altlinux.ru> 1.13.0-alt1
- new version 1.13.0 (with rpmrb script)

* Fri Mar 08 2019 Vitaly Lipatov <lav@altlinux.ru> 1.12.1-alt1
- new version 1.12.1 (with rpmrb script)

* Sun Dec 23 2018 Vitaly Lipatov <lav@altlinux.ru> 1.11.1-alt1
- new version 1.11.1 (with rpmrb script)

* Wed Nov 14 2018 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt1
- new version 1.11.0 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 1.10.0-alt2
- adopt logrotate conf for ALT

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 1.10.0-alt1
- new version 1.10.0 (with rpmrb script)

* Mon Feb 26 2018 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt2
- fix pid file path in service file
- cleanup spec

* Wed Dec 20 2017 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- new version 1.9.0 (with rpmrb script)

* Wed Dec 20 2017 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt2
- use bash4 for all shells scripts
- cleanup spec, change user/group to %netdatauser

* Tue Oct 24 2017 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)

* Thu Jul 27 2017 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- new version (1.7.0) with rpmgs script

* Fri Jun 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- build new version

* Tue Mar 07 2017 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt3
- replace shell to /bin/bash4 only on ALT
- fill version.txt with commit id for the release

* Fri Mar 03 2017 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt2
- split postgres module to a subpackage
- fix log dir permission

* Mon Feb 27 2017 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)
- pack python modules (ALT bug 32662)
- pack /etc/netdata/charts.d/ (ALT bug 32663)
- set bash4 for bash4 using scripts (ALT bug 32663)

* Sat Oct 22 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt2
- fix packing

* Sat Oct 22 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)

* Mon Sep 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Thu May 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- initial build for ALT Linux Sisyphus

* Mon May 16 2016 Costa Tsaousis <costa@tsaousis.gr> - 1.2.0-1
- netdata is now 30%% faster.
- netdata now has a registry (my-netdata menu on the dashboard).
- netdata now monitors Linux containers.
- Several more improvements, new features and bugfixes.
* Wed Apr 20 2016 Costa Tsaousis <costa@tsaousis.gr> - 1.1.0-1
- Several new features (IPv6, SYNPROXY, Users, Users Groups).
- A lot of bug fixes and optimizations.
* Tue Mar 22 2016 Costa Tsaousis <costa@tsaousis.gr> - 1.0.0-1
- First public release.
* Sun Nov 15 2015 Alon Bar-Lev <alonbl@redhat.com> - 0.0.0-1
- Initial add.
