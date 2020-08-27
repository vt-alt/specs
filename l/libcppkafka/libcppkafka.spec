Name: libcppkafka
Version: 0.3.1
Release: alt1
Summary: high level C++ wrapper for rdkafka
Group: Development/C++
# https://github.com/mfontanini/cppkafka
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
License: BSD
Url: https://github.com/mfontanini/cppkafka
BuildRequires: gcc-c++ rpm-macros-cmake boost-devel cmake librdkafka-devel

%description
cppkafka allows C++ applications to consume and produce messages using the
Apache Kafka protocol. The library is built on top of librdkafka, and provides
a high level API that uses modern C++ features to make it easier to write code
while keeping the wrapper's performance overhead to a minimum.

%package devel
Group: Development/C++
Summary: Developmen environment for %name
Requires: %name = %version
%description devel
Development environment for %name, %summary

%prep
%setup
%patch0 -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%changelog
* Tue Jun 25 2019 Anton Farygin <rider@altlinux.ru> 0.3.1-alt1
- first build for ALT

