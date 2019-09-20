Name: poco
Version: 1.9.4
Release: alt1
Summary: POrtable COmponents C++ Libraries
License: Boost Software License v1.0
Group: Development/C++
Url: http://pocoproject.org/

# https://github.com/pocoproject/poco.git
Source: %name-%version.tar

BuildPreReq: gcc-c++ cmake libsqlite3-devel zlib-devel libpcre-devel
BuildPreReq: libexpat-devel libssl-devel libmariadb-devel
BuildPreReq: libunixODBC-devel libiodbc-devel

%description
POrtable COmponents C++ Libraries are:

* A collection of C++ class libraries, conceptually similar to the Java
  Class Library, the .NET Framework or Apple's Cocoa.
* Focused on solutions to frequently-encountered practical problems.
* Focused on 'internet-age' network-centric applications.
* Written in efficient, modern, 100%% ANSI/ISO Standard C++.
* Based on and complementing the C++ Standard Library/STL.
* Highly portable and available on many different platforms.
* Open Source, licensed under the Boost Software License.

%package -n lib%name
Summary: POrtable COmponents C++ Libraries
Group: System/Libraries

%description -n lib%name
POrtable COmponents C++ Libraries are:

* A collection of C++ class libraries, conceptually similar to the Java
  Class Library, the .NET Framework or Apple's Cocoa.
* Focused on solutions to frequently-encountered practical problems.
* Focused on 'internet-age' network-centric applications.
* Written in efficient, modern, 100%% ANSI/ISO Standard C++.
* Based on and complementing the C++ Standard Library/STL.
* Highly portable and available on many different platforms.
* Open Source, licensed under the Boost Software License.

%package -n lib%name-net
Summary: POrtable COmponents C++ Libraries (net)
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-net
POrtable COmponents C++ Libraries: Poco network library

%package -n lib%name-data
Summary: POrtable COmponents C++ Libraries (data)
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-data
POrtable COmponents C++ Libraries: Poco data library

%package -n lib%name-crypto
Summary: POrtable COmponents C++ Libraries (crypto)
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-crypto
POrtable COmponents C++ Libraries: Poco crypto library

%package -n lib%name-mysql
Summary: POrtable COmponents C++ Libraries (mysql)
Group: Development/C++
Requires: lib%name-data = %EVR

%description -n lib%name-mysql
POrtable COmponents C++ Libraries: Poco mysql library

%package -n lib%name-sqlite
Summary: POrtable COmponents C++ Libraries (sqlite)
Group: Development/C++
Requires: lib%name-data = %EVR

%description -n lib%name-sqlite
POrtable COmponents C++ Libraries: Poco sqlite library

%package -n lib%name-odbc
Summary: POrtable COmponents C++ Libraries (odbc)
Group: Development/C++
Requires: lib%name-data = %EVR

%description -n lib%name-odbc
POrtable COmponents C++ Libraries: Poco odbc library

%package -n lib%name-mongodb
Summary: POrtable COmponents C++ Libraries (mongodb)
Group: Development/C++
Requires: lib%name-net = %EVR

%description -n lib%name-mongodb
POrtable COmponents C++ Libraries: Poco mongodb library

%package -n lib%name-zip
Summary: POrtable COmponents C++ Libraries (zip)
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-zip
POrtable COmponents C++ Libraries: Poco zip library

%package -n lib%name-redis
Summary: POrtable COmponents C++ Libraries (redis)
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-redis
POrtable COmponents C++ Libraries: Poco redis library

%package -n lib%name-util
Summary: POrtable COmponents C++ Libraries (util)
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-util
POrtable COmponents C++ Libraries: Poco util library

%package -n lib%name-ssl
Summary: POrtable COmponents C++ Libraries (ssl)
Group: Development/C++
Requires: lib%name = %EVR
Requires: lib%name-crypto = %EVR
Requires: lib%name-net = %EVR
Requires: lib%name-util = %EVR

%description -n lib%name-ssl
POrtable COmponents C++ Libraries: Poco ssl network library

%package -n lib%name-devel
Summary: Development files of POrtable COmponents C++ Libraries
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
POrtable COmponents C++ Libraries are:

* A collection of C++ class libraries, conceptually similar to the Java
  Class Library, the .NET Framework or Apple's Cocoa.
* Focused on solutions to frequently-encountered practical problems.
* Focused on 'internet-age' network-centric applications.
* Written in efficient, modern, 100%% ANSI/ISO Standard C++.
* Based on and complementing the C++ Standard Library/STL.
* Highly portable and available on many different platforms.
* Open Source, licensed under the Boost Software License.

This package contains development files of POrtable COmponents C++
Libraries.

%package -n lib%name-devel-docs
Summary: Documentation for POrtable COmponents C++ Libraries
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
POrtable COmponents C++ Libraries are:

* A collection of C++ class libraries, conceptually similar to the Java
  Class Library, the .NET Framework or Apple's Cocoa.
* Focused on solutions to frequently-encountered practical problems.
* Focused on 'internet-age' network-centric applications.
* Written in efficient, modern, 100%% ANSI/ISO Standard C++.
* Based on and complementing the C++ Standard Library/STL.
* Highly portable and available on many different platforms.
* Open Source, licensed under the Boost Software License.

This package contains development documentation for POrtable COmponents
C++ Libraries.

%prep
%setup

%build
%add_optflags -I%_includedir/pcre -fno-strict-aliasing
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DPCRE_INCLUDE_DIR:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DPOCO_UNBUNDLED:BOOL=ON \
	.
%make_build VERBOSE=1


%install
%makeinstall_std

mkdir -p usr/%_lib
for i in %buildroot%_libdir/*.so*; do
	ln -s $i usr/%_lib/
done

export POCO_BASE=$PWD
%make -C CppParser DESTDIR=%buildroot LIBDIR=%_libdir LINKMODE=RELEASE
#make -C PocoDoc DESTDIR=%buildroot LIBDIR=%_libdir LINKMODE=RELEASE

cp -fR CppParser/include/Poco/CppParser %buildroot%_includedir/Poco/
cp -P usr/%_lib/libPocoCppParser.so* %buildroot%_libdir/

%files -n lib%name
%doc CHANGELOG CONTRIBUTORS libversion LICENSE NEWS README* VERSION
%_libdir/libPocoFoundation*.so.*
%_libdir/libPocoXML*.so.*
%_libdir/libPocoJSON*.so.*
%_libdir/libPocoCppParser*.so.*
%_libdir/libPocoEncodings*.so.*

%files -n lib%name-data
%_libdir/libPocoData*.so.*
%exclude %_libdir/libPocoDataMySQL.so.*
%exclude %_libdir/libPocoDataSQLite.so.*
%exclude %_libdir/libPocoDataODBC.so.*

%files -n lib%name-net
%_libdir/libPocoNet*.so.*
%exclude %_libdir/libPocoNetSSL.so.*

%files -n lib%name-ssl
%_libdir/libPocoNetSSL*.so.*

%files -n lib%name-crypto
%_libdir/libPocoCrypto*.so.*

%files -n lib%name-mysql
%_libdir/libPocoDataMySQL*.so.*

%files -n lib%name-sqlite
%_libdir/libPocoDataSQLite*.so.*

%files -n lib%name-mongodb
%_libdir/libPocoMongoDB*.so.*

%files -n lib%name-odbc
%_libdir/libPocoDataODBC*.so.*

%files -n lib%name-util
%_libdir/libPocoUtil*.so.*

%files -n lib%name-zip
%_libdir/libPocoZip*.so.*

%files -n lib%name-redis
%_libdir/libPocoRedis*.so.*

%files -n lib%name-devel
%_bindir/*
%_includedir/*
%_libdir/*.so
%_libdir/cmake/*

#files -n lib%name-devel-docs

%changelog
* Wed Sep 18 2019 Alexei Takaseev <taf@altlinux.org> 1.9.4-alt1
- 1.9.4 (Fixes CVE-2019-15903)

* Wed Aug 21 2019 Alexei Takaseev <taf@altlinux.org> 1.9.3-alt1
- 1.9.3

* Tue Jul 02 2019 Alexei Takaseev <taf@altlinux.org> 1.9.2-alt1
- 1.9.2

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.9.0-alt2.1
- NMU: Rebuild with new openssl 1.1.0.

* Fri Jun 15 2018 Alexei Takaseev <taf@altlinux.org> 1.9.0-alt2
- Build with MariaDB client libraries

* Fri Mar 09 2018 Alexei Takaseev <taf@altlinux.org> 1.9.0-alt1
- 1.9.0

* Wed Jan 10 2018 Alexei Takaseev <taf@altlinux.org> 1.8.1-alt1
- 1.8.0

* Sun Nov 12 2017 Alexei Takaseev <taf@altlinux.org> 1.8.0.1-alt1
- 1.8.0.1
- Add subpackage redis

* Tue Sep 12 2017 Alexei Takaseev <taf@altlinux.org> 1.7.9-alt1
- 1.7.9

* Fri Jun 23 2017 Alexei Takaseev <taf@altlinux.org> 1.7.8p3-alt1
- 1.7.8p3

* Thu Apr 20 2017 Alexei Takaseev <taf@altlinux.org> 1.7.8p2-alt1
- 1.7.8p2

* Tue Feb 21 2017 Alexei Takaseev <taf@altlinux.org> 1.7.7-alt1
- 1.7.7

* Sat Oct 22 2016 Alexei Takaseev <taf@altlinux.org> 1.7.6-alt1
- 1.7.6

* Mon Aug 29 2016 Alexei Takaseev <taf@altlinux.org> 1.7.5-alt1
- 1.7.5

* Fri Aug 26 2016 Pavel Vainerman <pv@altlinux.ru> 1.7.4-alt2
- split to subpackages

* Sat Jul 30 2016 Alexei Takaseev <taf@altlinux.org> 1.7.4-alt1
- 1.7.4

* Wed May 04 2016 Alexei Takaseev <taf@altlinux.org> 1.7.3-alt1
- 1.7.3

* Mon Mar 21 2016 Alexei Takaseev <taf@altlinux.org> 1.7.2-alt1
- 1.7.2

* Tue Mar 15 2016 Alexei Takaseev <taf@altlinux.org> 1.7.1-alt1
- 1.7.1

* Tue Mar 08 2016 Alexei Takaseev <taf@altlinux.org> 1.7.0-alt1
- 1.7.0

* Wed Sep 30 2015 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt1
- 1.6.1

* Wed Sep 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.3-alt1.git20140701
- Initial build for Sisyphus

