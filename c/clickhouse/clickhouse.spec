Name: clickhouse
Version: 19.17.9.60
Release: alt2
Summary: Open-source distributed column-oriented DBMS
License: Apache-2.0
Group: Databases
Url: https://clickhouse.yandex/

# https://github.com/ClickHouse/ClickHouse.git
Source: %name-%version.tar
Source1: %name-%version-contrib-base64.tar
Source2: %name-%version-contrib-simdjson.tar
Source3: %name-%version-contrib-zlib-ng.tar
Patch0: %name-%version-%release.patch

BuildRequires: cmake, libicu-devel, libreadline-devel, python3, gperf, tzdata,  cctz-devel
BuildRequires: rpm-macros-cmake, liblz4-devel, /proc, libzstd-devel, libmariadb-devel
BuildRequires: farmhash-devel, metrohash-devel, libdouble-conversion-devel, librdkafka-devel, libssl-devel, libre2-devel
BuildRequires: libgsasl-devel, libcap-ng-devel, libxxhash-devel, boost-devel, libunixODBC-devel, libgperftools-devel
BuildRequires: libpoco-devel, libgtest-devel, libbrotli-devel, capnproto-devel, libxml2-devel, libcppkafka-devel
BuildRequires: libtinfo-devel, boost-filesystem-devel, boost-program_options-devel, boost-geometry-devel
BuildRequires: llvm-devel, gcc-c++, perl-JSON-XS, libb64-devel libasan-devel-static, boost-lockfree-devel
BuildRequires: libprotobuf-devel
BuildRequires: libstdc++-devel-static
BuildRequires: libsparsehash-devel
BuildRequires: rapidjson-devel
BuildRequires: boost-devel-static
%ifarch x86_64
BuildRequires: libhyperscan-devel
%endif

ExclusiveArch: aarch64 x86_64

%description
ClickHouse is an open-source column-oriented database management system that
allows generating analytical data reports in real time.

%package common-static
Group: Databases
Summary: Common files for %name
Provides: libclickhouse = %EVR
Conflicts: libclickhouse < %EVR
Obsoletes: libclickhouse < %EVR

%description common-static
This package provides common files for both clickhouse server and client.

%package server
Summary: Server binary for ClickHouse
Group: Databases
Requires: %name-common-static = %EVR

%description server
This package contains server binaries for ClickHouse DBMS.

%package client
Summary: Client binary for ClickHouse
Group: Databases
Requires: %name-common-static = %EVR

%description client
This package contains clickhouse-client , clickhouse-local and clickhouse-benchmark

%package test
Summary: ClickHouse tests
Group: Databases
Requires: %name-client = %EVR

%description test
ClickHouse tests

%prep
%setup -a1 -a2 -a3
%patch0 -p1

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DENABLE_UTILS=0 \
	-DCMAKE_VERBOSE_MAKEFILE=0 \
	-DUNBUNDLED=1 \
	-DUSE_STATIC_LIBRARIES=1 \
	-DUSE_UNWIND=0 \
	-DCLICKHOUSE_SPLIT_BINARY=0 \
	-DENABLE_JEMALLOC=0 \
	%nil

%cmake_build VERBOSE=1

%install
%cmakeinstall_std
install -Dm0644 debian/clickhouse-server.cron.d %buildroot%_sysconfdir/cron.d/clickhouse-server
install -Dm0644 debian/clickhouse.limits %buildroot%_sysconfdir/security/limits.d/clickhouse.conf
install -Dm0644 debian/clickhouse-server.service %buildroot%_unitdir/clickhouse-server.service
mkdir -p %buildroot%_localstatedir/clickhouse
mkdir -p %buildroot%_logdir/clickhouse-server
cp -r  dbms/programs/server/users.d %buildroot%_sysconfdir/clickhouse-server/

%pre server
%_sbindir/groupadd -r -f _clickhouse 2> /dev/null ||:
%_sbindir/useradd -r -g _clickhouse -d %_localstatedir/lib/%name -s /dev/null -c "ClickHouse User" _clickhouse 2> /dev/null ||:

%post server
%post_service clickhouse-server

%preun server
%preun_service clickhouse-server



%files common-static
%_bindir/clickhouse
%_bindir/clickhouse-odbc-bridge
%config(noreplace) %_sysconfdir/security/limits.d/clickhouse.conf

%files server
%config(noreplace) %_sysconfdir/cron.d/clickhouse-server
%config(noreplace) %_sysconfdir/clickhouse-server/config.xml
%config(noreplace) %_sysconfdir/clickhouse-server/users.xml
%dir %_sysconfdir/clickhouse-server/users.d
%config(noreplace) %_sysconfdir/clickhouse-server/users.d/*.xml
%_bindir/clickhouse-server
%_bindir/clickhouse-report
%_bindir/clickhouse-copier
%_bindir/config-processor
%_unitdir/clickhouse-server.service
%dir %attr(0750,_clickhouse,_clickhouse) %_logdir/clickhouse-server
%dir %attr(0750,_clickhouse,_clickhouse) %_localstatedir/clickhouse

%files client
%config(noreplace) %_sysconfdir/clickhouse-client/config.xml
%_bindir/clickhouse-client
%_bindir/clickhouse-local
%_bindir/clickhouse-compressor
%_bindir/clickhouse-benchmark
%_bindir/clickhouse-obfuscator
%_bindir/clickhouse-format
%_bindir/clickhouse-extract-from-config

%files test
%_bindir/clickhouse-test
%_bindir/clickhouse-test-server
%_bindir/clickhouse-performance-test
%_datadir/clickhouse-test
%config(noreplace) %_sysconfdir/clickhouse-client/client-test.xml
%config(noreplace) %_sysconfdir/clickhouse-server/server-test.xml

%changelog
* Tue Aug 25 2020 Nazarov Denis <nenderus@altlinux.org> 19.17.9.60-alt2
- Fix clickhouse-test-server pass

* Tue Mar 17 2020 Anton Farygin <rider@altlinux.ru> 19.17.9.60-alt1
-  19.17.8.54 -> 19.17.9.60

* Fri Feb 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 19.17.8.54-alt1
- Updated to stable upstream version 19.17.8.54.

* Thu Dec 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 19.16.2.2-alt2
- Rebuilt with boost-1.71.0.

* Wed Nov 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 19.16.2.2-alt1
- Updated to stable upstream version 19.16.2.2.
- Used bundled zlib-ng instead of system zlib library.
- Disabled building shared clickhouse library.
- Built single clickhouse binary.

* Thu Oct 03 2019 Anton Farygin <rider@altlinux.ru> 19.13.6.51-alt1
- 19.13.6.51

* Wed Sep 25 2019 Anton Farygin <rider@altlinux.ru> 19.13.5.44-alt1
- 19.13.5.44

* Tue Sep 10 2019 Anton Farygin <rider@altlinux.ru> 19.13.4.32-alt1
- 19.13.4.32

* Thu Aug 22 2019 Anton Farygin <rider@altlinux.ru> 19.13.3.26-alt1
- 19.13.3.26

* Wed Aug 14 2019 Anton Farygin <rider@altlinux.ru> 19.13.2.19-alt1
- 19.13.2.19

* Mon Aug 12 2019 Anton Farygin <rider@altlinux.ru> 19.13.1.11-alt1
- 19.13.1.11

* Wed Aug 07 2019 Anton Farygin <rider@altlinux.ru> 19.11.6.31-alt1
- 19.11.6.31-alt1

* Tue Aug 06 2019 Anton Farygin <rider@altlinux.ru> 19.11.5.28-alt2
- 19.11.5.28
- fixed build on aarch64 and ppc (thanx to Sergey Bolshakov)
- enabled rapidjson
- build by gcc

* Mon Jul 22 2019 Anton Farygin <rider@altlinux.ru> 19.9.5.36-alt1
- new version
- build without jemalloc

* Mon Jul 01 2019 Anton Farygin <rider@altlinux.ru> 19.9.2.4-alt2
- config files was marked for prevent rewrite during an update

* Tue Jun 25 2019 Anton Farygin <rider@altlinux.ru> 19.9.2.4-alt1
- updated to 19.9.2.4

* Wed Jun 19 2019 Anton Farygin <rider@altlinux.ru> 19.8.3.8-alt1
- first build for ALT

