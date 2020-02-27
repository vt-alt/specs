%define _unpackaged_files_terminate_build 1

%global backends %nil
%define _pkgdocdir %_docdir/%name

Name: pdns
Version: 4.2.1
Release: alt1
Summary: A modern, advanced and high performance authoritative-only nameserver
Group: System/Servers
License: GPLv2
Url: http://powerdns.com
Source0: %name-%version.tar
Patch0: pdns-disable-secpoll.patch

BuildRequires: gcc-c++ boost-program_options-devel curl libcurl-devel libsqlite3-devel
BuildRequires: systemd-devel /bin/systemctl
BuildRequires: boost-devel
BuildRequires: liblua5-devel
BuildRequires: bison flex ragel
BuildRequires: libzeromq-devel
BuildRequires: openssl-devel
BuildRequires: libprotobuf-devel
BuildRequires: protobuf-compiler
Provides: powerdns = %version-%release
%global backends %backends bind random

%description
The PowerDNS Nameserver is a modern, advanced and high performance
authoritative-only nameserver. It is written from scratch and conforms
to all relevant DNS standards documents.
Furthermore, PowerDNS interfaces with almost any database.

%package tools
Summary: Extra tools for %name
Group: System/Servers

%description tools
This package contains the extra tools for %name

%package backend-mysql
Summary: MySQL backend for %name
Group: System/Servers
Requires: %name = %version-%release
BuildRequires: libmysqlclient-devel
%global backends %backends gmysql

%description backend-mysql
This package contains the gmysql backend for %name

%package backend-postgresql
Summary: PostgreSQL backend for %name
Group: System/Servers
Requires: %name = %version-%release
BuildRequires: postgresql-devel
%global backends %backends gpgsql

%description backend-postgresql
This package contains the gpgsql backend for %name

%package backend-pipe
Summary: Pipe backend for %name
Group: System/Servers
Requires: %name = %version-%release
%global backends %backends pipe

%description backend-pipe
This package contains the pipe backend for %name

%package backend-remote
Summary: Remote backend for %name
Group: System/Servers
Requires: %name = %version-%release
%global backends %backends remote

%description backend-remote
This package contains the remote backend for %name

%package backend-ldap
Summary: LDAP backend for %name
Group: System/Servers
Requires: %name = %version-%release
BuildRequires: openldap-devel
%global backends %backends ldap

%description backend-ldap
This package contains the ldap backend for %name

%package backend-lua
Summary: LUA backend for %name
Group: System/Servers
Requires: %name = %version-%release
%global backends %backends lua

%description backend-lua
This package contains the lua backend for %name

%package backend-lua2
Summary: LUA2 backend for %name
Group: System/Servers
Requires: %name = %version-%release
%global backends %backends lua2

%description backend-lua2
This package contains the lua2 backend for %name

%package backend-sqlite
Summary: SQLite backend for %name
Group: System/Servers
Requires: %name = %version-%release
BuildRequires: sqlite-devel
%global backends %backends gsqlite3

%description backend-sqlite
This package contains the SQLite backend for %name

%package backend-opendbx
Summary: OpenDBX backend for %name
Group: System/Servers
Requires: %name = %version-%release
BuildRequires: opendbx-devel
%global backends %backends opendbx

%description backend-opendbx
This package contains the opendbx backend for %name

%package backend-geoip
Summary: GeoIP backend for %name
Group: System/Servers
Requires: %name = %version-%release
BuildRequires: libGeoIP-devel
BuildRequires: libyaml-cpp-devel
%global backends %backends geoip

%description backend-geoip
This package contains the GeoIP backend for %name

%package backend-mydns
Summary: MyDNS backend for %name
Group: System/Servers
Requires: %name = %version-%release
%global backends %backends mydns

%description backend-mydns
This package contains the MyDNS backend for %name

%package backend-tinydns
Summary: TinyDNS backend for %name
Group: System/Servers
Requires: %name = %version-%release
BuildRequires: tinycdb-devel
%global backends %backends tinydns

%description backend-tinydns
This package contains the TinyDNS backend for %name

%package ixfrdist
Summary: A program to redistribute zones over AXFR and IXFR
Group: System/Servers

BuildRequires: libyaml-cpp-devel

%description ixfrdist
This package contains the ixfrdist program.


%prep
%setup
%patch0 -p1 -b .disable-secpoll

%build
export CPPFLAGS="-DLDAP_DEPRECATED"
export BUILDER_VERSION=%version
export PDNS_TEST_NO_IPV6=1

%autoreconf
%configure \
	--sysconfdir=%_sysconfdir/%name \
	--disable-static \
	--disable-dependency-tracking \
	--disable-silent-rules \
	--with-modules='' \
	--with-lua \
	--enable-lua-records \
	--with-dynmodules='%backends' \
	--enable-tools \
	--enable-remotebackend-zeromq \
	--enable-unit-tests \
	--enable-reproducible \
	--enable-systemd --with-systemd=%_unitdir \
	--enable-ixfrdist

%make_build

%install
%makeinstall_std

rm -f %buildroot%_libdir/%name/*.la
mv %buildroot%_sysconfdir/%name/pdns.conf{-dist,}

chmod 600 %buildroot%_sysconfdir/%name/pdns.conf

# rename zone2ldap to pdns-zone2ldap (#1193116)
mv %buildroot%_bindir/zone2ldap %buildroot%_bindir/pdns_zone2ldap
mv %buildroot%_man1dir/zone2ldap.1 %buildroot%_man1dir/pdns_zone2ldap.1

# change user/group to pdns
# change default backend to bind
sed -i \
    -e 's/# setuid=/setuid=pdns/' \
    -e 's/# setgid=/setgid=pdns/' \
    -e 's/# launch=/launch=bind/' \
    %buildroot%_sysconfdir/%name/pdns.conf

rm %buildroot%_bindir/stubquery

mkdir -p %buildroot%_localstatedir/%name

%check
%make_build -C pdns check || cat pdns/test-suite.log

%pre

%_sbindir/groupadd -r -f %name
%_sbindir/useradd -M -r -d %_localstatedir/%name -s /bin/false -c "PowerDNS user" -g %name %name >/dev/null 2>&1 ||:

%post
%post_service pdns

%preun
%preun_service pdns

%files
%doc COPYING README
%_bindir/pdns_control
%_bindir/pdnsutil
%_bindir/pdns_zone2ldap
%_bindir/zone2sql
%_bindir/zone2json
%_sbindir/pdns_server
%_man1dir/pdns_control.1.*
%_man1dir/pdns_server.1.*
%_man1dir/zone2sql.1.*
%_man1dir/zone2json.1.*
%_man1dir/pdns_zone2ldap.1.*
%_man1dir/pdnsutil.1.*
%_unitdir/pdns.service
%_unitdir/pdns@.service
%_libdir/%name/libbindbackend.so
%_libdir/%name/librandombackend.so
%dir %_libdir/%name
%dir %_sysconfdir/%name
%dir %attr(0750, root, %name) %_localstatedir/%name
%config(noreplace) %_sysconfdir/%name/pdns.conf

%files tools
%_bindir/calidns
%_bindir/dnsbulktest
%_bindir/dnsgram
%_bindir/dnspcap2calidns
%_bindir/dnspcap2protobuf
%_bindir/dnsreplay
%_bindir/dnsscan
%_bindir/dnsscope
%_bindir/dnstcpbench
%_bindir/dnswasher
%_bindir/dumresp
%_bindir/ixplore
%_bindir/pdns_notify
%_bindir/nproxy
%_bindir/nsec3dig
%_bindir/saxfr
%_bindir/sdig
%_man1dir/calidns.1.*
%_man1dir/dnsbulktest.1.*
%_man1dir/dnsgram.1.*
%_man1dir/dnspcap2calidns.1.*
%_man1dir/dnspcap2protobuf.1.*
%_man1dir/dnsreplay.1.*
%_man1dir/dnsscan.1.*
%_man1dir/dnsscope.1.*
%_man1dir/dnstcpbench.1.*
%_man1dir/dnswasher.1.*
%_man1dir/dumresp.1.*
%_man1dir/ixplore.1.*
%_man1dir/pdns_notify.1.*
%_man1dir/nproxy.1.*
%_man1dir/nsec3dig.1.*
%_man1dir/saxfr.1.*
%_man1dir/sdig.1.*

%files backend-mysql
%_pkgdocdir/schema.mysql.sql
%_pkgdocdir/dnssec-3.x_to_3.4.0_schema.mysql.sql
%_pkgdocdir/nodnssec-3.x_to_3.4.0_schema.mysql.sql
%_pkgdocdir/3.4.0_to_4.1.0_schema.mysql.sql
%_pkgdocdir/4.1.0_to_4.2.0_schema.mysql.sql
%_libdir/%name/libgmysqlbackend.so

%files backend-postgresql
%_pkgdocdir/schema.pgsql.sql
%_pkgdocdir/dnssec-3.x_to_3.4.0_schema.pgsql.sql
%_pkgdocdir/nodnssec-3.x_to_3.4.0_schema.pgsql.sql
%_pkgdocdir/3.4.0_to_4.1.0_schema.pgsql.sql
%_pkgdocdir/4.1.0_to_4.2.0_schema.pgsql.sql
%_libdir/%name/libgpgsqlbackend.so

%files backend-pipe
%_libdir/%name/libpipebackend.so

%files backend-remote
%_libdir/%name/libremotebackend.so

%files backend-ldap
%_pkgdocdir/dnsdomain2.schema
%_pkgdocdir/pdns-domaininfo.schema
%_libdir/%name/libldapbackend.so

%files backend-lua
%_libdir/%name/libluabackend.so

%files backend-lua2
%_libdir/%name/liblua2backend.so

%files backend-sqlite
%_pkgdocdir/schema.sqlite3.sql
%_pkgdocdir/dnssec-3.x_to_3.4.0_schema.sqlite3.sql
%_pkgdocdir/nodnssec-3.x_to_3.4.0_schema.sqlite3.sql
%_pkgdocdir/3.4.0_to_4.0.0_schema.sqlite3.sql
%_pkgdocdir/4.0.0_to_4.2.0_schema.sqlite3.sql
%_libdir/%name/libgsqlite3backend.so

%files backend-opendbx
%_libdir/%name/libopendbxbackend.so

%files backend-geoip
%_libdir/%name/libgeoipbackend.so

%files backend-mydns
%_pkgdocdir/schema.mydns.sql
%_libdir/%name/libmydnsbackend.so

%files backend-tinydns
%_libdir/%name/libtinydnsbackend.so

%files ixfrdist
%_bindir/ixfrdist
%_man1dir/ixfrdist.*
%_man5dir/ixfrdist.yml.*
%_sysconfdir/%name/ixfrdist.example.yml
%_unitdir/ixfrdist.service
%_unitdir/ixfrdist@.service

%changelog
* Sat Feb 22 2020 Alexey Shabalin <shaba@altlinux.org> 4.2.1-alt1
- 4.2.1 (Fixes: CVE-2017-15091, CVE-2018-10851, CVE-2018-14626, CVE-2019-3871, CVE-2019-10162, CVE-2019-10163)

* Mon Jan 14 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.0.3-alt3
- fix FTBFS due to transition to libmysqlclient21

* Tue Sep 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.3-alt2.3
- NMU: rebuilt with new yaml-cpp.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 4.0.3-alt2.2
- NMU: Rebuild with new openssl 1.1.0.

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.3-alt2.1
- NMU: rebuilt with boost-1.67.0

* Tue Mar 28 2017 Lenar Shakirov <snejok@altlinux.ru> 4.0.3-alt2
- Fake release up for make test

* Wed Feb 15 2017 Lenar Shakirov <snejok@altlinux.ru> 4.0.3-alt1
- New version (based on 4.0.3-3.fc26.src)

* Mon Apr 01 2013 Michael Shigorin <mike@altlinux.org> 2.9.22-alt1.2
- NMU: fixed MySQL client library dependencies

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 2.9.22-alt1.1
- rebuild with new libmysqlclient by request of libmysqlclient maintainer

* Thu Mar 25 2010 Pavel Shilovsky <piastry@altlinux.org> 2.9.22-alt1
- Import 2.9.22 sources
- Patch work
  + Rewrite patch #6
  + Delete patches #1, #3, #4
  + Change patch numbers (#2, #5, #6) to (#1, #2, #3)
- Change .gear-rules according to deleted patches

* Thu Sep 24 2009 ALT QA Team Robot <ldv@altlinux.org> 2.9.21.2-alt5.1
- Automated blind dumb rebuild with libldap-devel-2.4.16-alt4.4.

* Mon May 25 2009 Pavel Shilovsky <piastry@altlinux.org> 2.9.21.2-alt5
- fixed build errors on gcc 4.4

* Wed Mar  4 2009 Pavel Shilovsky <piastry@altlinux.org> 2.9.21.2-alt4
- fixed some bugs in patch #5

* Tue Mar  3 2009 Pavel Shilovsky <piastry@altlinux.org> 2.9.21.2-alt3
- bugfix #18871: added patch #5

* Sat Jan 24 2009 Pavel Shilovsky <piastry@altlinux.org> 2.9.21.2-alt2
- fixed missing backend-mysql package requires

* Sun Dec 14 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.9.21.2-alt1
- updated to new version 2.9.21.2

* Sun Dec 14 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.9.21.1-alt3
- fixed instaltions problems with devel package requires
- built pgsql backend

* Wed Oct 29 2008 Pavel Shilovsky <piastry@altlinux.org> 2.9.21.1-alt2
- fixed problems with g++ 4.3
   + add patch to support g++ 4.3

* Sun Oct 19 2008 Pavel Shilovsky <piastry@altlinux.org> 2.9.21.1-alt1
- updated to new version 2.9.21.1
   + add patch to support boost 1.36
   + add backend sqlite3

* Sun Apr 29 2007 Ilya Evseev <evseev@altlinux.ru> 2.9.21-alt1
- updated to new version 2.9.21
   + remove patch #3
   + boost 1.33 or later is required now

* Fri Jan 12 2007 Ilya Evseev <evseev@altlinux.ru> 2.9.20-alt3
- bugfix #10650: added patch #3

* Thu Jan  4 2007 Ilya Evseev <evseev@altlinux.ru> 2.9.20-alt2
- bugfix #10138

* Wed Sep 13 2006 Ilya Evseev <evseev@altlinux.ru> 2.9.20-alt1
- initial build for ALTLinux, based on 2.9.20-2mdk

## EOF ##

