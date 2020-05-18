%define _unpackaged_files_terminate_build 1
%define soversion 11
ExclusiveArch: x86_64
Name:     intel-gmmlib
Version:  20.1.1
Release:  alt1
Summary:  Intel(R) Graphics Memory Management Library
License:  MIT
Group:    System/Libraries
Url:      https://github.com/intel/gmmlib
Source:   %name-%version.tar
BuildRequires: cmake rpm-macros-cmake gcc-c++
%description
The Intel(R) Graphics Memory Management Library provides device specific and buffer
management for the Intel(R) Graphics Compute Runtime for OpenCL(TM) and 
the Intel(R) Media Driver for VAAPI.

%package -n libigdgmm%soversion
Summary:  Intel(R) Graphics Memory Management Library
Group:    System/Libraries
%description -n libigdgmm%soversion
The Intel(R) Graphics Memory Management Library provides device specific and buffer
management for the Intel(R) Graphics Compute Runtime for OpenCL(TM) and
the Intel(R) Media Driver for VAAPI.

%package devel
Summary: Development files for %name
Group: Development/C
%description devel
This package provides the development environment for %name

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_STATIC_LIBS=OFF
%cmake_build

%install
%cmakeinstall_std
rm -f %buildroot/%_libdir/*.a

%files -n libigdgmm%soversion
%_libdir/*.so.%{soversion}*

%files devel
%doc README.rst
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%changelog
* Tue Apr 07 2020 Anton Farygin <rider@altlinux.ru> 20.1.1-alt1
- 20.1.1

* Mon Jan 13 2020 Anton Farygin <rider@altlinux.ru> 19.4.1-alt1
- 19.4.1

* Wed Nov 13 2019 Anton Farygin <rider@altlinux.ru> 19.3.4-alt1
- 19.3.4

* Fri Oct 04 2019 Anton Farygin <rider@altlinux.ru> 19.3.2-alt1
- 19.3.2

* Wed Sep 11 2019 Anton Farygin <rider@altlinux.ru> 19.2.4-alt1
- 19.2.4

* Thu Aug 15 2019 Anton Farygin <rider@altlinux.ru> 19.2.3-alt1
- 19.2.3

* Sat May 18 2019 Anton Farygin <rider@altlinux.ru> 19.1.2-alt1
- 19.1.2

* Mon Feb 18 2019 Anton Farygin <rider@altlinux.ru> 18.4.1-alt1
- 18.4.1

* Mon Oct 08 2018 Anton Farygin <rider@altlinux.ru> 18.3.0-alt1
- first build for ALT

