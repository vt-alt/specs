Name: libcaf
Version: 0.16.2
Release: alt2

Summary: An Open Source Implementation of the Actor Model in C++

Group: Networking/Other
License: BSD / Boost
Url: http://www.actor-framework.org/

# Source-url: https://github.com/actor-framework/actor-framework/archive/%version.tar.gz
Source: %name-%version.tar
Patch: libcaf-0.16.2-fix-linking.patch

BuildRequires: gcc-c++ libcurl-devel libssl-devel
%ifnarch ppc64le
BuildRequires: ocl-icd-devel
%endif

BuildRequires(pre): cmake

%description
CAF is an open source C++11 actor model implementation
featuring lightweight & fast actor implementations,
pattern matching for messages, network transparent messaging, and more.

%package devel
Summary: Development file for %name
Requires: %name = %EVR
Group: Networking/Other

%description devel
This package contains the header files for %name.


%prep
%setup
%patch -p1
# TODO: LIB_DESTINATION
%__subst "s|LIBRARY DESTINATION lib|LIBRARY DESTINATION %_lib|" */CMakeLists.txt

%build
%cmake \
%ifarch ppc64le
    -DCAF_NO_OPENCL:BOOL=yes
%endif

%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/libcaf_*.so.*

%files devel
%_includedir/caf/
%_libdir/libcaf_*.so
%_datadir/caf/


%changelog
* Tue Oct 08 2019 Alexey Shabalin <shaba@altlinux.org> 0.16.2-alt2
- disable build with opencl support for ppc64le

* Sun Dec 16 2018 Vitaly Lipatov <lav@altlinux.ru> 0.16.2-alt1
- initial build for ALT Sisyphus
