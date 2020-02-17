%ifarch x86_64 %ix86 aarch64 ppc64le
%def_with libdpdk
%else
%def_without libdpdk
%endif
%def_with libgps
%def_enable apache
%def_enable bind
%def_enable cgi
%def_enable curl
%def_enable dbi
%def_enable ipmi
%def_enable virt
%def_enable memcached
%def_disable modbus
%def_enable mysql
%def_disable netlink
%def_enable nginx
%def_enable notify_desktop
%def_enable notify_email
%def_enable nut
%def_enable perl
%def_enable ping
%def_enable postgresql
%def_enable rrdcached
%def_enable rrdtool
%def_enable sensors
%def_enable snmp
%def_enable tokyotyrant
%def_disable xmms

%def_disable static

Name: collectd
Version: 5.10.0
Release: alt1

Summary: (Multi-)System statistics collection
License: GPLv2 AND MIT
Group: Monitoring

Url: http://collectd.org
Source0: %url/files/%name-%version.tar
Patch0: %name-%version-alt.patch

### NB: part of BRs is conditional (see subpackages below)
# Automatically added by buildreq on Thu May 14 2009 (-bi)
#BuildRequires: flex gcc-c++ iptables-devel libMySQL-devel libcurl-devel libdbi-devel libesmtp-devel libgcrypt-devel libnet-snmp-devel libnetlink-devel libnotify-devel liboping-devel libpcap-devel librrd-devel libsensors-devel libvirt-devel libxfs-devel libxml2-devel libxmms-devel nut-devel perl-devel perl-threads perl-Regexp-Common postgresql-devel
BuildRequires: flex gcc-c++ iptables-devel libgcrypt-devel libpcap-devel libxfs-devel
BuildRequires: libstatgrab-devel

%if_enabled perl
BuildRequires: perl-devel perl-threads perl-Regexp-Common perl-Pod-Parser perl-RRD

# http://mailman.verplant.org/pipermail/collectd/2008-April/001766.html
%set_perl_req_method relaxed
%endif

%set_verify_elf_method unresolved=relaxed textrel=relaxed
%add_verify_elf_skiplist %_libdir/%name/*/*

%define libname lib%{name}client
%define nginxdir %_sysconfdir/nginx/sites-enabled.d

%description
collectd is a small program written in C for performance. It reads various
system statistics and updates RRD files, creating them if neccessary.
Since it doesn't need to startup every time it wants to update the files
it's very fast and easy on the system. Also, the statistics are very
fine grained since the files are updated every 10 seconds.

WARNING: 5.x is INCOMPATIBLE with 4.x data!  You HAVE to perform
custom MIGRATION as described in documentation OR drop the HISTORY!
>> http://collectd.org/wiki/index.php/V4_to_v5_migration_guide <<

NB: syslog plugin might be helpful at configuration stage
but not in production since it generates LOTS of logfile records!

%package -n %libname
Summary: Shared library for %name clients
Group: System/Libraries

%description -n %libname
This package contains shared library for %name clients.

%package -n %libname-devel
Summary: Library headers to build %name clients
Group: Development/C
Requires: %libname = %version-%release

%description -n %libname-devel
This package contains development part of %libname.

%if_enabled perl
%package -n perl-Collectd
Summary: Perl module for %name
Group: Development/Perl
BuildArch: noarch

%description -n perl-Collectd
This package contains Perl part of %name.
%endif

%package cluster
Summary: Cluster metapackage for %name plugins
Group: Monitoring
BuildArch: noarch
%{?_enable_ipmi:Requires: %name-ipmi}
%{?_enable_modbus:Requires: %name-modbus}
%{?_enable_snmp:Requires: %name-snmp}

%description cluster
This package pulls in plugins which might be useful at a cluster

%package full
Summary: Meta package for %name plugins
Group: Monitoring
BuildArch: noarch
%{?_with_libgps:Requires: %name-gps}
%{?_enable_apache:Requires: %name-apache}
%{?_enable_bind:Requires: %name-bind}
%{?_enable_cgi:Requires: %name-cgi}
%{?_enable_curl:Requires: %name-curl}
%{?_enable_dbi:Requires: %name-dbi}
%{?_enable_ipmi:Requires: %name-ipmi}
%{?_enable_virt:Requires: %name-virt}
%{?_enable_mysql:Requires: %name-mysql}
%{?_enable_netlink:Requires: %name-netlink}
%{?_enable_nginx:Requires: %name-nginx}
%{?_enable_notify_desktop:Requires: %name-notify_desktop}
%{?_enable_notify_email:Requires: %name-notify_email}
%{?_enable_nut:Requires: %name-nut}
%{?_enable_ping:Requires: %name-ping}
%{?_enable_postgresql:Requires: %name-postgresql}
%{?_enable_rrdcached:Requires: %name-rrdcached}
%{?_enable_rrdtool:Requires: %name-rrdtool}
%{?_enable_sensors:Requires: %name-sensors}
%{?_enable_snmp:Requires: %name-snmp}
%{?_enable_tokyotyrant:Requires: %name-tokyotyrant}
%{?_enable_xmms:Requires: %name-xmms}

%description full
This package pulls in all the different plugins and might
come handy if you don't mind extra dependencies on the system

%if_with libdpdk
%package dpdk
Summary: DPDK support module for collectd
Group: Monitoring
BuildRequires: dpdk-devel

%description dpdk
This plugin provides DPDK support for collectd
%endif

%if_with libgps
%package gps
Summary: GPS support module for collectd
Group: Monitoring
BuildRequires: libgps-devel

%description gps
This plugin provides GPS support for collectd
%endif

%if_enabled apache
%package apache
Summary: apache2 support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
BuildRequires(pre): apache2-devel
BuildRequires(pre): rpm-macros-apache2

%description apache
This plugin provides apache 2.x support for collectd
%endif

%if_enabled bind
%package bind
Summary: ISC BIND support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
BuildRequires: libcurl-devel libxml2-devel

%description bind
This plugin provides ISC BIND support for collectd
%endif

%if_enabled cgi
%package cgi
Summary: CGI script for collectd
Group: Monitoring
Requires: collectd = %version
Requires: webserver-common perl-RRD perl-HTML-Parser
BuildRequires: perl-CGI
BuildRequires(pre): apache2-devel
BuildRequires(pre): rpm-macros-apache2
BuildArch: noarch

%description cgi
This CGI frontend for collectd allows to browse the stats online,
check out http://localhost/cgi-bin/%name/collection.cgi

%if_enabled apache
%package cgi-apache2
Summary: CGI script for collectd (apache2 config and glue)
Group: Monitoring
Requires: collectd-cgi = %version
Requires: apache2-base apache2-cgi-bin
BuildArch: noarch

%description cgi-apache2
apache2 configuration and glue to run collectd CGI script.

See %apache2_extra_available/%name.conf for details,
including access restrictions to be imposed.
%endif

%if_enabled nginx
%package cgi-nginx
Summary: CGI script for collectd (nginx config and glue)
Group: Monitoring
Requires: collectd-cgi = %version
Requires: nginx fcgiwrap spawn-fcgi
BuildArch: noarch

%description cgi-nginx
nginx configuration and glue to run collectd CGI script.

See %nginxdir/%name.conf for details,
including access restrictions to be imposed,
and %_sysconfdir/sysconfig/spawn-fcgi just in case

NB: this reconfigures spawn-fcgi and sets it to autostart!
%endif
%endif

%if_enabled curl
%package curl
Summary: CURL support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
BuildRequires: libcurl-devel

%description curl
This plugin provides CURL (proxy, etc) support for collectd
%endif

%if_enabled dbi
%package dbi
Summary: DBI support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
BuildRequires: libdbi-devel

%description dbi
This plugin provides DBI support for collectd
%endif

%if_enabled ipmi
%package ipmi
Summary: IPMI support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
Requires: libopenipmi
BuildRequires: libopenipmi-devel

%description ipmi
This plugin provides ipmi support for collectd
%endif

%if_enabled virt
%package virt
Summary: virt support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
BuildRequires: libvirt-devel libxml2-devel
Provides: %name-libvirt = %version
Obsoletes: %name-libvirt < %version

%description virt
This plugin provides virtual machines support for collectd
%endif

%if_enabled memcached
%package memcached
Summary: memcached support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
BuildRequires: libmemcached-devel

%description memcached
This plugin provides memcached support for collectd, see
http://collectd.org/wiki/index.php/Plugin:memcached
http://collectd.org/wiki/index.php/Plugin:memcachec
%endif

%if_enabled modbus
%package modbus
Summary: ModBus support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
# libmodbus-2.9.3+ is going to be supported when a stable version
# is available, 2.0.3 should get fixed with 4.10.3:
# http://www.mail-archive.com/collectd@verplant.org/msg01126.html
BuildRequires: libmodbus-devel < 2.9

%description modbus
This plugin provides ModBus support for collectd
%endif

%if_enabled mysql
%package mysql
Summary: MySQL support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
BuildRequires: libMySQL-devel

%description mysql
This plugin provides MySQL server support for collectd
%endif

%if_enabled netlink
%package netlink
Summary: netlink support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
BuildRequires: libnetlink-devel

%description netlink
This plugin provides netlink support for collectd
%endif

%if_enabled nginx
%package nginx
Summary: nginx support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
BuildRequires: libcurl-devel

%description nginx
This plugin provides nginx support for collectd
%endif

%if_enabled notify_desktop
%package notify_desktop
Summary: desktop notification support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
BuildRequires: libnotify-devel

%description notify_desktop
This plugin provides desktop notification support for collectd
%endif

%if_enabled notify_email
%package notify_email
Summary: email notification support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
BuildRequires: libesmtp-devel

%description notify_email
This plugin provides email notification support for collectd
%endif

%if_enabled nut
%package nut
Summary: Network UPS Tools support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
Requires: libnut
BuildRequires: libupsclient-devel

%description nut
This plugin provides UPS support for collectd (with NUT)
%endif

%if_enabled rrdcached
%package rrdcached
Summary: RRDCacheD support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
BuildRequires: librrd-devel >= 1.4

%description rrdcached
This plugin provides RRDCacheD support for collectd
(see http://collectd.org/wiki/index.php/Plugin:RRDCacheD)
%endif

%if_enabled rrdtool
%package rrdtool
Summary: rrdtool support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
Requires: rrdtool
BuildRequires: librrd-devel

%description rrdtool
This plugin provides RRD Tool support for collectd
%endif

%if_enabled ping
%package ping
Summary: ICMP support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
BuildRequires: liboping-devel

%description ping
This plugin provides ICMP (ping check) support for collectd
%endif

%if_enabled postgresql
%package postgresql
Summary: PostgreSQL support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
BuildRequires: postgresql-devel

%description postgresql
This plugin provides PostgreSQL support for collectd
%endif

%if_enabled sensors
%package sensors
Summary: lm_sensors support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
Requires: lm_sensors3
BuildRequires: libsensors3-devel >= 3.1.0-alt4

%description sensors
This plugin provides sensors support for collectd (with lm_sensors)
%endif

%if_enabled snmp
%package snmp
Summary: SNMP support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
Requires: libnet-snmp
BuildRequires: libnet-snmp-devel net-snmp-common

%description snmp
This plugin provides SNMP support for collectd
%endif

%if_enabled tokyotyrant
%package tokyotyrant
Summary: Tokyo Tyrant support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
BuildRequires: libtokyotyrant-devel

%description tokyotyrant
This plugin provides Tokyo Tyrant support for collectd
%endif

%if_enabled xmms
%package xmms
Summary: XMMS support module for collectd
Group: Monitoring
Requires: collectd = %version-%release
Requires: libxmms
BuildRequires: libxmms-devel

%description xmms
This plugin provides XMMS support for collectd
%endif

%package -n nagios-plugins-%name
Summary: Nagios plugin to use data from collectd
Group: Monitoring
Requires: nagios-common

%description -n nagios-plugins-%name
This Nagios plugin provides possibility to feed statistics
from collectd into nagios to avoid extra sensor-caused load

%prep
%setup
%patch0 -p1
mkdir libltdl

%build
./build.sh

# fixed warnings:
# python.so: underlinked libraries: /lib64/libpthread.so.0
# gmond.so: underlinked libraries: /lib64/libpthread.so.0
# rrdcached.so: underlinked libraries: /lib64/libpthread.so.0
# rrdtool.so: underlinked libraries: /lib64/libpthread.so.0
# notify_desktop.so: underlinked libraries: /usr/lib64/libgobject-2.0.so.0

# seems like mainstream uses /var for localstatedir, ALT uses /var/lib
%configure \
	--disable-apple_sensors \
	--disable-ascent \
	--disable-java \
	--without-java \
	--disable-debug \
	%{subst_with libdpdk} \
	%{subst_with libgps} \
	%{subst_enable apache} \
	%{subst_enable curl} \
	%{subst_enable dbi} \
	%{subst_enable ipmi} \
	%{subst_enable virt} \
	%if_enabled memcached
	--enable-memcachec \
	%endif
	%{subst_enable memcached} \
	%{subst_enable modbus} \
	%{subst_enable mysql} \
	%{subst_enable netlink} \
	%{subst_enable nginx} \
	%{subst_enable notify_desktop} \
	%{subst_enable notify_email} \
	%{subst_enable nut} \
	%{subst_enable perl} \
	%{subst_enable ping} \
	%{subst_enable postgresql} \
	%{subst_enable rrdcached} \
	%{subst_enable rrdtool} \
	%if_enabled sensors
	--with-libsensors=%_prefix \
	%{subst_enable sensors} \
	%endif
	%{subst_enable snmp} \
	%{subst_enable tokyotyrant} \
	%{subst_enable xmms} \
	%{subst_enable static} \
    --localstatedir=%_var

# </configure>
%make_build INSTALLMAN1DIR=%_man1dir

%install
%makeinstall_std INSTALLDIRS=vendor
install -pDm644 src/collectd.conf %buildroot%_sysconfdir/%name.conf
sed -i 's,/usr/var,%_var,g' %buildroot%_sysconfdir/%name.conf
install -pDm755 contrib/altlinux/%name.init %buildroot%_initdir/%name
install -d %buildroot%_libdir/%name/ %buildroot%_localstatedir/%name/
rm %buildroot%_libdir/%name/*.la

# TODO: package collection3 and maybe other frontends as well
# provide versionless pathname for now
ln -snr %buildroot%_defaultdocdir/%name-%version/contrib/collection3 %buildroot%_datadir/%name/
%if_enabled cgi
%if_enabled apache
install -pDm644 contrib/altlinux/%name.apache2 %buildroot%apache2_extra_available/%name.conf
%endif
%if_enabled nginx
install -pDm644 contrib/altlinux/%name.nginx %buildroot%nginxdir/%name.conf
%endif
install -pDm755 contrib/collection.cgi %buildroot%apache2_cgibindir/%name/collection.cgi
cat >> %buildroot%_sysconfdir/collection.conf << EOF
datadir: "%_localstatedir/%name"
libdir: "%_localstatedir/%name"
EOF
%endif

install -pDm644 contrib/systemd.collectd.service %buildroot%_unitdir/collectd.service

%pre
# Plugin libvirt renamed to virt in 5.5.0
sed -i "s/Plugin libvirt/Plugin virt/g" %_sysconfdir/%name.conf 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%post cgi-apache2
a2enmod cgi && a2enextra %name ||:

%preun cgi-apache2
a2disextra %name ||:

%post cgi-nginx
# FIXME: this must be properly done with control(8) in spawn-fcgi
echo -n "reconfiguring spawn-fcgi to use fcgiwrap... "
if sed -i \
	-e 's,^FCGIPROGRAM=.*$,FCGIPROGRAM="/usr/sbin/fcgiwrap",' \
	-e 's,^FCGILISTEN=.*$,#&,' \
	-e 's,^FCGIPORT=.*$,#&,' \
	-e 's,^#\(SOCKETGROUP=_nginx\)$,\1,' \
	-e 's,^#\(SOCKETMODE=0770\)$,\1,' \
	%_sysconfdir/sysconfig/spawn-fcgi;
then
	echo "done"
	echo "consider: chkconfig spawn-fcgi on && service spawn-fcgi start"
fi

%post rrdtool
service %name condrestart ||:

%postun rrdtool
service %name condrestart ||:

%files
%doc AUTHORS ChangeLog README ChangeLog
%doc contrib/
%config(noreplace) %_sysconfdir/%name.conf
%_initdir/%name
%_sbindir/%name
%_sbindir/collectdmon
%_bindir/collectdctl
%_bindir/collectd-tg
%_man1dir/*.1*
%_man5dir/*.5*
%_datadir/%name/
%dir %_localstatedir/%name/
%dir %_libdir/%name/
%_libdir/%name/*.so
%{?_with_libdpdk:%exclude %_libdir/%name/dpdk*.so}
%{?_with_libgps:%exclude %_libdir/%name/gps.so}
%{?_enable_apache:%exclude %_libdir/%name/apache.so}
%{?_enable_bind:%exclude %_libdir/%name/bind.so}
%{?_enable_curl:%exclude %_libdir/%name/curl.so}
%{?_enable_dbi:%exclude %_libdir/%name/dbi.so}
%{?_enable_ipmi:%exclude %_libdir/%name/ipmi.so}
%{?_enable_virt:%exclude %_libdir/%name/virt.so}
%{?_enable_memcached:%exclude %_libdir/%name/memcachec.so}
%{?_enable_memcached:%exclude %_libdir/%name/memcached.so}
%{?_enable_modbus:%exclude %_libdir/%name/modbus.so}
%{?_enable_mysql:%exclude %_libdir/%name/mysql.so}
%{?_enable_netlink:%exclude %_libdir/%name/netlink.so}
%{?_enable_nginx:%exclude %_libdir/%name/nginx.so}
%{?_enable_notify_email:%exclude %_libdir/%name/notify_email.so}
%{?_enable_notify_desktop:%exclude %_libdir/%name/notify_desktop.so}
%{?_enable_nut:%exclude %_libdir/%name/nut.so}
%{?_enable_ping:%exclude %_libdir/%name/ping.so}
%{?_enable_postgresql:%exclude %_libdir/%name/postgresql.so}
%{?_enable_rrdcached:%exclude %_libdir/%name/rrdcached.so}
%{?_enable_rrdtool:%exclude %_libdir/%name/rrdtool.so}
%{?_enable_sensors:%exclude %_libdir/%name/sensors.so}
%{?_enable_snmp:%exclude %_libdir/%name/snmp.so}
%{?_enable_tokyotyrant:%exclude %_libdir/%name/tokyotyrant.so}
%{?_enable_xmms:%exclude %_libdir/%name/xmms.so}
%_unitdir/collectd.service

%files -n %libname
%_libdir/%libname.so.*

%files -n %libname-devel
%_includedir/%name/
%_libdir/%libname.so
%_pkgconfigdir/*

%if_enabled perl
%files -n perl-Collectd
%dir %perl_vendor_privlib/Collectd
%perl_vendor_privlib/*.pm
%perl_vendor_privlib/*/*.pm
%endif

%if_with libdpdk
%files dpdk
%_libdir/%name/dpdk*.so
%endif

%if_with libgps
%files gps
%_libdir/%name/gps.so
%endif

%if_enabled apache
%files apache
%_libdir/%name/apache.so
%endif

%if_enabled bind
%files bind
%_libdir/%name/bind.so
%endif

%if_enabled cgi
%files cgi
%dir %apache2_cgibindir/%name/
%apache2_cgibindir/%name/collection.cgi
%config(noreplace) %_sysconfdir/collection.conf

%if_enabled apache
%files cgi-apache2
%config(noreplace) %apache2_extra_available/%name.conf
%endif

%if_enabled nginx
%files cgi-nginx
%config(noreplace) %nginxdir/%name.conf
%endif
%endif

%if_enabled curl
%files curl
%_libdir/%name/curl.so
%endif

%if_enabled dbi
%files dbi
%_libdir/%name/dbi.so
%endif

%if_enabled ipmi
%files ipmi
%_libdir/%name/ipmi.so
%endif

%if_enabled virt
%files virt
%_libdir/%name/virt.so
%endif

%if_enabled memcached
%files memcached
%_libdir/%name/memcachec.so
%_libdir/%name/memcached.so
%endif

%if_enabled modbus
%files modbus
%_libdir/%name/modbus.so
%endif

%if_enabled mysql
%files mysql
%_libdir/%name/mysql.so
%endif

%if_enabled netlink
%files netlink
%_libdir/%name/netlink.so
%endif

%if_enabled nginx
%files nginx
%_libdir/%name/nginx.so
%endif

%if_enabled notify_desktop
%files notify_desktop
%_libdir/%name/notify_desktop.so
%endif

%if_enabled notify_email
%files notify_email
%_libdir/%name/notify_email.so
%endif

%if_enabled nut
%files nut
%_libdir/%name/nut.so
%endif

%if_enabled ping
%files ping
%_libdir/%name/ping.so
%endif

%if_enabled postgresql
%files postgresql
%_libdir/%name/postgresql.so
%endif

%if_enabled rrdcached
%files rrdcached
%_libdir/%name/rrdcached.so
%endif

%if_enabled rrdtool
%files rrdtool
%_libdir/%name/rrdtool.so
%dir %_localstatedir/%name
%endif

%if_enabled sensors
%files sensors
%_libdir/%name/sensors.so
%endif

%if_enabled snmp
%files snmp
%_libdir/%name/snmp.so
%endif

%if_enabled tokyotyrant
%files tokyotyrant
%_libdir/%name/tokyotyrant.so
%endif

%if_enabled xmms
%files xmms
%_libdir/%name/xmms.so
%endif

%files cluster

%files full

%files -n nagios-plugins-%name
%_bindir/collectd-nagios

# TODO:
# - reenable netlink plugin
# - consider building with: libiokit, liboconfig (system),
#   libiptc [kernhdrs], libjvm?, libkvm, libcredis,
#   libnotify, librabbitmq, libvarnish, libyajl, ipvs
# - macroize repetitive sections

%changelog
* Wed Dec 25 2019 Anton Farygin <rider@altlinux.ru> 5.10.0-alt1
- 5.9.1 -> 5.10.0
- cleanup spec

* Fri Aug 30 2019 Alexey Shabalin <shaba@altlinux.org> 5.9.1-alt1
- 5.9.1
- delete arch depended dpdk package from noarch full package

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 5.8.1-alt5
- NMU: remove rpm-build-ubt from BR:

* Tue Mar 05 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.8.1-alt4
- rebuilt without x11amp plugin

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 5.8.1-alt3.1
- rebuild with new perl 5.28.1

* Fri Dec 21 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.8.1-alt3
- build with dpdk only on selected arches

* Wed Dec 19 2018 Anton Farygin <rider@altlinux.ru> 5.8.1-alt2
- temporary disabled format-truncation error to make gcc-8 happy

* Wed Oct 31 2018 Alexey Shabalin <shaba@altlinux.org> 5.8.1-alt1
- New version 5.8.1

* Mon Jun 04 2018 Anton Farygin <rider@altlinux.ru> 5.8.0-alt4
- rebuilt with new dpdk

* Wed May 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.8.0-alt3
- NMU: rebuilt with new nut.

* Wed Apr 18 2018 Michael Shigorin <mike@altlinux.org> 5.8.0-alt2
- add the missing libdpdk, libgps knobs

* Tue Apr 3 2018 Mikhail Savostyanov <mik@altlinux.ru> 5.8.0-alt1
- New version 5.8.0

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 5.7.2-alt3.1
- rebuild with new perl 5.26.1

* Tue Oct 31 2017 Sergey Y. Afonin <asy@altlinux.ru> 5.7.2-alt3
- cherry-pick from upstream 'apcups: allow to use plugin without explicit configuration'
  (ALT #33957)

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.7.2-alt2
- Rebuilt with libdbi-0.9.0.

* Mon Aug 07 2017 Anton Farygin <rider@altlinux.ru> 5.7.2-alt1
- 5.7.2

* Sat Jul 01 2017 Michael Shigorin <mike@altlinux.org> 5.5.2-alt1.3
- E2K: insist it's -std=c99, see e.g. cpu.c::cpu_commit_one();
  thanks imz@ and MCST guys for investigation
- fixed collectd.conf.pod for older pod2man (reported upstream)

* Fri Jun 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.5.2-alt1.2
- Updated build to support new toolchain

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 5.5.2-alt1.1
- rebuild with new perl 5.24.1

* Fri Oct 14 2016 Anton Farygin <rider@altlinux.ru> 5.5.2-alt1
- new version

* Sat Feb 27 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.5.0-alt1.3
- fix configfile path in systemd unit (closes: #31652)

* Wed Dec 02 2015 Andrey Cherepanov <cas@altlinux.org> 5.5.0-alt1.2
- rebuild with new libmemcached 1.0.18

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 5.5.0-alt1.1
- rebuild with new perl 5.22.0

* Tue Oct 27 2015 Sergey Y. Afonin <asy@altlinux.ru> 5.5.0-alt1
- new version (closes: #31402)
  + changed: libvirt plugin renamed to virt
- added perl-Collectd to requires of perl-based plugins
- added lsb init header (fixed repocop's warning)

* Sat Feb 28 2015 Anton Farygin <rider@altlinux.ru> 5.4.2-alt2
- cherry-pick from upstream 'snmp plugin: add hostname to "csnmp_instance_list_add" error message'
  close #30344 again.

* Thu Feb 26 2015 Anton Farygin <rider@altlinux.ru> 5.4.2-alt1
- new version (closes: #30668, #30344)

* Mon Jan 26 2015 Anton Farygin <rider@altlinux.ru> 5.4.1-alt3
- add unit file for systemd (closes: #28038)

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 5.4.1-alt2.1
- rebuild with new perl 5.20.1

* Tue Jun 17 2014 Anton Farygin <rider@altlinux.ru> 5.4.1-alt2
- fixed "no instance" error in collection3 for ethernet interfaces plugins

* Wed May 28 2014 Anton Farygin <rider@altlinux.ru> 5.4.1-alt1
- new version

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 5.2.1-alt4
- built for perl 5.18

* Wed Mar 13 2013 Michael Shigorin <mike@altlinux.org> 5.2.1-alt3
- fixed mysql deps

* Thu Feb 28 2013 Michael Shigorin <mike@altlinux.org> 5.2.1-alt2
- kludged pm installation (somehow these ended up in lib/ not share/)
- disabled monitorus plugin

* Fri Feb 08 2013 Michael Shigorin <mike@altlinux.org> 5.2.1-alt1
- 5.2.1
- fixed pod build (thanks viy@ for the encoding tip)

* Wed Nov 28 2012 Michael Shigorin <mike@altlinux.org> 5.2.0-alt1
- 5.2.0

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 5.1.0-alt5
- rebuilt for perl-5.16

* Tue Jul 17 2012 Michael Shigorin <mike@altlinux.org> 5.1.0-alt4
- disabled debug which breaks nagios plugin (closes: #27548)

* Wed Jun 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.0-alt3
- rebuild with libmemcached-1.0.8

* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 5.1.0-alt2
- re-enabled notify_desktop plugin

* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 5.1.0-alt1
- 5.1.0

* Tue Feb 28 2012 Michael Shigorin <mike@altlinux.org> 5.0.3-alt1
- 5.0.3

* Sat Jan 28 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0.1-alt6
- rebuild with libmemcached-1.0.4

* Tue Jan 10 2012 Michael Shigorin <mike@altlinux.org> 5.0.1-alt5
- temporarily disabled netlink plugin (rtnl_dump_filter FTBFS)

* Sat Oct 29 2011 Michael Shigorin <mike@altlinux.org> 5.0.1-alt4
- added "localhost only by default" access restrictions
  to the webserver configuration snippets provided within
  cgi-* subpackages (along with basic auth examples)

* Sat Oct 29 2011 Michael Shigorin <mike@altlinux.org> 5.0.1-alt3
- added nginx specific configuration as cgi-nginx subpackage
- enabled parallel build

* Sat Oct 29 2011 Michael Shigorin <mike@altlinux.org> 5.0.1-alt2
- CGI fixup:
  + added perl-HTML-Parser to cgi subpackage requires
  + added %_localstatedir/%name to rrdtool subpackage
  + moved apache2 specific configuration into cgi-apache2
    subpackage, added the remaining expected actions there too
- rrdtool subpackage will condrestart collectd upon (de)installation
  since it's enabled in default collectd.conf and will be rather
  silently ignored if missing (which might reesult in potential
  monitoring data not being collected while deemed being ok)

* Fri Oct 21 2011 Alexey Tourbin <at@altlinux.ru> 5.0.1-alt1.1
- rebuilt for perl-5.14

* Fri Oct 21 2011 Michael Shigorin <mike@altlinux.org> 5.0.1-alt1
- 5.0.1
  + assorted fixups all over the place

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 5.0.0-alt6
- rebuilt against libstatgrab-0.17
- added collectdctl

* Wed Sep 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0.0-alt5
- rebuilt adainst libmemcached-0.52

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 5.0.0-alt4
- rebuilt against current liboping

* Thu Aug 18 2011 Michael Shigorin <mike@altlinux.org> 5.0.0-alt3
- updated the warning in description for v5 (thx asy@)

* Tue Jun 14 2011 Michael Shigorin <mike@altlinux.org> 5.0.0-alt2
- rebuilt against current libmemcached

* Sat Jun 11 2011 Michael Shigorin <mike@altlinux.org> 5.0.0-alt1
- 5.0.0: new major release, data/config migration needed;
  see http://collectd.org/wiki/index.php/V4_to_v5_migration_guide

* Sat Jun 11 2011 Michael Shigorin <mike@altlinux.org> 4.10.3-alt4
- disabled notify_desktop plugin by default
  (FTBFS presumably due to gnome3 changes)

* Sun Mar 27 2011 Michael Shigorin <mike@altlinux.org> 4.10.3-alt3
- noarch subpackages specified as such

* Sun Mar 27 2011 Michael Shigorin <mike@altlinux.org> 4.10.3-alt2
- rebuilt

* Sat Mar 26 2011 Michael Shigorin <mike@altlinux.org> 4.10.3-alt1
- 4.10.3 (fixes and clarifications)

* Mon Mar 21 2011 Michael Shigorin <mike@altlinux.org> 4.10.2-alt6
- rebuilt with current libmemcached

* Fri Feb 25 2011 Michael Shigorin <mike@altlinux.org> 4.10.2-alt5
- added subpackages:
  + ganglia, tokyotyrant (enabled by default)
  + modbus (disabled by default so far, library version issue)
  + cluster (meta)
- fixed nut plugin build and reenabled it by default
- NB: prepare for 5.0 in advance, see
  http://collectd.org/wiki/index.php/Version_5.0/Plans

* Thu Jan 20 2011 Michael Shigorin <mike@altlinux.org> 4.10.2-alt4
- changed startup priority from 90 to 97 so as to start
  after OpenVZ containers (in case collectd server is there)

* Fri Jan 07 2011 Michael Shigorin <mike@altlinux.org> 4.10.2-alt3
- fixed BaseDir/datadir equality (second issue from #24866)

* Fri Jan 07 2011 Michael Shigorin <mike@altlinux.org> 4.10.2-alt2
- added perl-RRD to collectd-cgi dependencies (closes: #24866)

* Thu Dec 02 2010 Anton Farygin <rider@altlinux.ru> 4.10.2-alt1
- new version

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 4.10.1-alt2.1
- rebuilt with perl 5.12
- fixed build

* Tue Oct 05 2010 Anton Farygin <rider@altlinux.ru> 4.10.1-alt2
- rebuild with new libesmtp

* Thu Aug 05 2010 Michael Shigorin <mike@altlinux.org> 4.10.1-alt1.1
- added syslog plugin notice to %%description
  (should we disable it by default?)

* Thu Jul 22 2010 Michael Shigorin <mike@altlinux.org> 4.10.1-alt1
- 4.10.1
- rrdcached plugin moved to subpackage so that base collectd
  can get rid of libX11 dependency again
- added memcached subpackage (two separate plugins)

* Thu Jul 01 2010 Anton Farygin <rider@altlinux.ru> 4.10.0-alt1
- new version

* Tue Apr 27 2010 Sergey Y. Afonin <asy@altlinux.ru> 4.9.2-alt1.1
- rebuilt with rrd 1.4.3

* Mon Apr 26 2010 Michael Shigorin <mike@altlinux.org> 4.9.2-alt1
- 4.9.2

* Wed Mar 31 2010 Michael Shigorin <mike@altlinux.org> 4.9.1-alt3
- cherry-picked upstream fix for inconsistent perl plugins basedir
  in manpage (closes: #23235)

* Sun Mar 21 2010 Anton Farygin <rider@altlinux.ru> 4.9.1-alt2
- fixed build with perl (closes: #23195)

* Tue Jan 19 2010 Anton Farygin <rider@altlinux.ru> 4.9.1-alt1
- new version
- enabled IPMI and apache plugins
- added cgi package

* Mon Dec 21 2009 Michael Shigorin <mike@altlinux.org> 4.9.0-alt1
- 4.9.0
  + added plugins:
    NetApp, Python, RouterOS, ContextSwitch, Monitorus, OpenVZ
  + enhanced plugins:
    cURL, Ping, DF, Processes

* Mon Dec 21 2009 Michael Shigorin <mike@altlinux.org> 4.8.2-alt1
- 4.8.2

* Wed Oct 07 2009 Anton Farygin <rider@altlinux.ru> 4.8.1-alt1
- new version

* Wed Sep 23 2009 Anton Farygin <rider@altlinux.ru> 4.8.0-alt1
- new version

* Tue Jun 30 2009 Anton Farygin <rider@altlinux.ru> 4.7.1-alt1
- new version
- fixed build with new libsensors3-devel

* Mon Jun 01 2009 Anton Farygin <rider@altlinux.ru> 4.7.0-alt8
- collectd-sensors required lm_sensors3
- target "restart" fixed in initscrip

* Sat May 30 2009 Anton Farygin <rider@altlinux.ru> 4.7.0-alt7
- build with libstatgrab
- use collectdmon instead of collectd in initscript

* Fri May 29 2009 Anton Farygin <rider@altlinux.ru> 4.7.0-alt6
- allow use Debug in LogLevel (--enable-debug)
- merge collectd-4.7 branch from upstream, with fixes:
  rrdtool plugin: If `flush' cannot find the requested file, issue an `INFO'.
  src/utils_cache.c: Fix incorrect checking of persistent thresholds.

* Tue May 26 2009 Anton Farygin <rider@altlinux.ru> 4.7.0-alt5
- build from git
- fixed link with libsensors (Closes: #20162)

* Fri May 15 2009 Michael Shigorin <mike@altlinux.org> 4.7.0-alt4
- added v3-to-v4 migration link, thanks lav@

* Fri May 15 2009 Michael Shigorin <mike@altlinux.org> 4.7.0-alt3
- added perl subpackage

* Thu May 14 2009 Michael Shigorin <mike@altlinux.org> 4.7.0-alt2
- added dbi, libvirt, notify_desktop, notify_email, postgresql subpackages
- moved bind, curl, netlink, nginx, rrdtool plugins to subpackages
- added libesmtp support to notify_email plugin
- ping plugin built with system liboping
- optional libgcrypt/libpcap support for network plugin
- disabled ascent plugin (seems unneeded and a bit depsy)
- re-added specific XFS support to df plugin
- introduced "full" subpackage to pull in all the plugins
- prepared libstatgrab support (waits for #20040)
- considerable spec cleanup (thanks mplayer.spec for inspiration)
- fixed heaps of engrish

* Wed May 13 2009 Michael Shigorin <mike@altlinux.org> 4.7.0-alt1
- 4.7.0
- well, I took the plunge and moved to 4.x; however you will have
  to either handle transition yourself (it's about reading
  documentation and fiddling with migration scripts anyways,
  not much to be automated) 
- temporarily(tm) disabled -apache and -cgi subpackages:
  anyone knows where %%apache_cgibindir and %%apache_confdir
  macros live in this village?!
- temporarily disabled -nut subpackage: build troubles
- introduced client library subpackages

* Mon Jul 28 2008 Michael Shigorin <mike@altlinux.org> 4.4.2-alt1
- 4.4.2 (minor bugfixes)
- NB: this build was actually verified in production

* Thu Jun 26 2008 Michael Shigorin <mike@altlinux.org> 4.4.1-alt1
- 4.4.1: yeah, I've skipped quite a few 4.x releases while
  trying to get back to this package... now's about time ;-)

* Sun Feb 10 2008 Michael Shigorin <mike@altlinux.org> 4.2.4-alt3
- enabled features:
  + libnetlink, libstatgrab (core package)
  + snmp, nut, xmms (subpackages)

* Sun Feb 10 2008 Michael Shigorin <mike@altlinux.org> 4.2.4-alt2
- removed patches

* Tue Jan 22 2008 Michael Shigorin <mike@altlinux.org> 4.2.4-alt1
- 4.2.4 (major feature enhancements [over 4.0])
  + built for Daedalus
  + note http://collectd.org/migrate-v3-v4.shtml
    or wipe %_localstatedir/%name/ clean of collected data

* Tue Aug 14 2007 Michael Shigorin <mike@altlinux.org> 4.0.6-alt1
- 4.0.6 (major feature enhancements)
  + warning, there are major RRD- and CGI-related changes!
    you should not update the package blindly if it is used
  + please see contrib/migrate-3-4.px and associated README
- added apache2-devel, perl-devel to BuildRequires
- enabled apache2 subpackage by default
- introduced sample /etc/collection.conf (adapted from git)

* Thu May 31 2007 Michael Shigorin <mike@altlinux.org> 3.11.5-alt1
- 3.11.5 (security fixes)
  + fixed buffer overflow in the ntpd plugin
  + fixed support for Linux 2.4 in the disk plugin
  + added large file support (LFS)

* Tue Apr 03 2007 Michael Shigorin <mike@altlinux.org> 3.11.3-alt1
- 3.11.3 (minor bugfixes)

* Sat Feb 10 2007 Michael Shigorin <mike@altlinux.org> 3.11.1-alt1
- 3.11.1 (minor bugfixes)

* Sun Jan 28 2007 Michael Shigorin <mike@altlinux.org> 3.11.0-alt1
- 3.11.0
- removed patch1 (fixed upstream)
- fixed build with recent gcc4.1 (removed -Werror since -Wno-unused
  wouldn't  help)

* Fri Dec 22 2006 Michael Shigorin <mike@altlinux.org> 3.10.3-alt1
- thanks Vitaly Lipatov (lav@) for fixing build (patch sent upstream)
  and other improvements
- service off by default, see also [ru]:
  http://lists.altlinux.org/pipermail/devel/2006-December/039909.html

* Sat Dec 09 2006 Vitaly Lipatov <lav@altlinux.ru> 3.10.3-alt0.2
- NMU: set config as noreplace
- add post/preun service

* Mon Nov 20 2006 Vitaly Lipatov <lav@altlinux.ru> 3.10.3-alt0.1
- NMU: new version 3.10.3
- fix compiling (remove syslog redefine)
- fix default paths in /var (bug #10237)
- move cgi script to cgi/collectd dir
- add .htaccess, collectd.conf for apache

* Sun Sep 17 2006 Michael Shigorin <mike@altlinux.org> 3.10.1-alt2
- accepted spec patch from lakostis@
  + NMU.
  + .spec cleanup.
  + remove unwanted buildrequires.
  + build with system libltdl.
  + build with linux-libc-headers.
  + disable -static builds by default.
- fixed collectd.conf installation (source file moved)

* Sat Aug 05 2006 Michael Shigorin <mike@altlinux.org> 3.10.1-alt1
- 3.10.1

* Sun Jun 18 2006 Michael Shigorin <mike@altlinux.org> 3.9.3-alt1
- 3.9.3 (minor bugfixes)

* Mon May 15 2006 Michael Shigorin <mike@altlinux.org> 3.9.2-alt1
- 3.9.2 (minor bugfixes)
  + ping plugin would stop working after roughly one week
    with default settings

* Fri Apr 28 2006 Michael Shigorin <mike@altlinux.org> 3.9.1-alt1
- 3.9.1

* Sun Apr 23 2006 Michael Shigorin <mike@altlinux.org> 3.9.0-alt2
- macro control over modules (subpackages) built:
  apache, cgi, mysql, sensors (the rest is in the main package)

* Fri Apr 21 2006 Michael Shigorin <mike@altlinux.org> 3.9.0-alt1
- 3.9.0
- updated buildrequires for new plugins
- added mysql subpackage
- added cgi subpackage (WARNING: unrestricted out-of-box)
- patched hddtemp module regarding higher SCSI majors
- disabled apache support for the time being
- disabled apple sensors
- remove (unpackaged) *.la too

* Fri Apr 07 2006 Michael Shigorin <mike@altlinux.org> 3.8.3-alt1
- 3.8.3

* Wed Mar 15 2006 Michael Shigorin <mike@altlinux.org> 3.8.2-alt1
- 3.8.2
- built for Sisyphus
- sample configuration file taken from contrib/ now
  *and* moved to %_sysconfdir/%name.conf [3.8.1-1 spec]
- I've not got around to make this all work more out-of-box, spec fixes
  are welcome but maybe it's better as is (setup isn't that hard)

* Wed Mar 15 2006 Michael Shigorin <mike@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Jan 31 2006 Michael Shigorin <mike@altlinux.org> 3.7.0-alt0.M24.1
- 3.7.0

* Mon Dec 19 2005 Michael Shigorin <mike@altlinux.org> 3.5.1-alt0.M24.1
- 3.5.1
- spec cleanup

* Mon Dec 05 2005 Michael Shigorin <mike@altlinux.org> 3.4.0-alt0.M24.1
- 3.4.0

* Wed Nov 09 2005 Michael Shigorin <mike@altlinux.org> 3.3.0-alt0.M24.1
- 3.3.0

* Thu Oct 27 2005 Michael Shigorin <mike@altlinux.org> 3.2.0-alt0.M24.1
- 3.2.0

* Mon Oct 17 2005 Michael Shigorin <mike@altlinux.org> 3.1.0-alt0.M24.1
- built for ALT Linux Master 2.4
- spec cleanup

