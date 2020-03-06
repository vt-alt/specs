Name: catch2
Version: 2.11.1
Release: alt1

Summary: C++ Unit Test framework ("all in one header")

License: Boost Software License, Version 1.0
Group: Development/C++
Url: https://github.com/catchorg/Catch2

Packager: Pavel Vainerman <pv@altlinux.ru>
BuildArch: noarch

BuildRequires: rpm-macros-cmake cmake gcc-c++

# run tests
BuildRequires: ctest python-modules

# Source-url: https://github.com/catchorg/Catch2/archive/v%{version}.tar.gz
Source: %name-%version.tar

%description
Catch stands for C++ Automated Test Cases in Headers 
and is a multi-paradigm automated 
test framework for C++ and Objective-C (and, maybe, C). 
It is implemented entirely in a set of header files, 
but is packaged up as a single header for extra convenience.

%package devel
Summary: C++ Unit Test framework ("all in one header")
Group: Development/C++

%description devel
Catch stands for C++ Automated Test Cases in Headers 
and is a multi-paradigm automated 
test framework for C++ and Objective-C (and, maybe, C). 
It is implemented entirely in a set of header files, 
but is packaged up as a single header for extra convenience.

%prep
%setup
%__subst "s|set(CATCH_CMAKE_CONFIG_DESTINATION .*|set(CATCH_CMAKE_CONFIG_DESTINATION "%_datadir/cmake/Catch2")|" CMakeLists.txt

%build
%cmake -DCATCH_ENABLE_WERROR=OFF
%cmake_build

%install
%cmakeinstall_std

%check
cd BUILD
ctest -V

%files devel
%doc %_docdir/Catch2/
%dir %_includedir/catch2/
%_includedir/catch2/*.hpp
%_datadir/Catch2/
%_datadir/cmake/Catch2/
%_datadir/pkgconfig/catch2.pc

%changelog
* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 2.11.1-alt1
- new version 2.11.1 (with rpmrb script)

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 2.11.0-alt2
- fix cmake files placement

* Mon Nov 18 2019 Pavel Vainerman <pv@altlinux.ru> 2.11.0-alt1
- new version (2.11.0) with rpmgs script

* Sun Jun 10 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt2
- build with cmake, pack cmake modules and pkgconfig

* Sun Jun 03 2018 Pavel Vainerman <pv@altlinux.ru> 2.2.2-alt1
- new version (2.2.2) with rpmgs script
