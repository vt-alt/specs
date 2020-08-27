%global soname   2
Name: cctz
Version: 2.3
Release: alt1
License: ASL 2.0
Summary: Translating between absolute and civil times using time zone rules
Group: Development/C++
Url: https://github.com/google/cctz
Source0: %name-%version.tar
# https://sources.debian.org/patches/cctz/2.2+dfsg1-1/0001-Compile-shared-lib-and-install-it.patch/
Patch0: cctz-2.3-debian-compile-library-as-shared.patch
Patch1: cctz-2.3-debian-use_system_zoneinfo.patch
BuildRequires: tzdata
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ctest
BuildRequires: make
BuildRequires: libgtest-devel
BuildRequires: libgmock-devel
BuildRequires: libbenchmark-devel

Requires: tzdata

%description
CCTZ contains two libraries that cooperate with <chrono> to give C++
programmers all the necessary tools for computing with dates, times, and time
zones in a simple and correct manner. The libraries in CCTZ are:
  * The Civil-Time Library - This is a header-only library that supports
    computing with human-scale time, such as dates (which are represented by
    the cctz::civil_day class).
  * The Time-Zone Library - This library uses the IANA time zone database that
    is installed on the system to convert between absolute time and civil time.

%package devel
Summary: %summary
Group: Development/C++
Requires: %name%{?_isa} = %version-%release
Requires: cmake

%description devel
Development files for %name library.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
rm -f BUILD
%cmake -DVERSION=%version -DSOVERSION=%soname
%cmake_build

%install
%cmakeinstall_std

%check
cd BUILD
LD_LIBRARY_PATH=./ ctest -V

%files
%doc README.md LICENSE.txt
%_bindir/time_tool
%_libdir/libcctz.so.%soname
%_libdir/libcctz.so.%version

%files devel
%doc examples
%_includedir/cctz
%_libdir/libcctz.so
%_libdir/cmake/cctz

%changelog
* Thu Jun 20 2019 Anton Farygin <rider@altlinux.ru> 2.3-alt1
- first build for ALT
