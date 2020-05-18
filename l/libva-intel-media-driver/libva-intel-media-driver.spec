%define soname 7
Name: libva-intel-media-driver
Version: 20.1.1
Release: alt1

Summary: Intel(R) Media Driver for VAAPI
License: MIT
Group: System/Libraries
Url: https://github.com/intel/media-driver/

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: libdrm-devel libX11-devel libGL-devel libEGL-devel gcc-c++ libpciaccess-devel
BuildRequires: libva-devel >= 2.3.0
BuildRequires: cmake rpm-macros-cmake
BuildRequires: intel-gmmlib-devel >= 18.3.0
ExclusiveArch: x86_64

%description
The Intel(R) Media Driver for VAAPI is a new VA-API (Video Acceleration API) user
mode driver supporting hardware accelerated decoding, encoding, and video post
processing for GEN based graphics hardware.

%package -n libigfxcmrt%soname
Group: System/Libraries
Summary: C bindings for media runtime

%description -n libigfxcmrt%soname
cmrtlib is a runtime library needed when user wants to execute their own GPU 
kernels on render engine. It calls iHD media driver to load the kernels and
allocate the resources. It provides a set of APIs for user to call directly from application.

%package -n libigfxcmrt-devel
Summary: Development files for libigfxcmrt%soname
Group: Development/C
Requires: libigfxcmrt%soname = %EVR

%description -n libigfxcmrt-devel
This package provides the development environment for libigfxcmrt

%prep
%setup
%patch0 -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc LICENSE.md README.md
%_libdir/dri/*.so

%files -n libigfxcmrt%soname
%_libdir/libigfxcmrt.so.%soname
%_libdir/libigfxcmrt.so.%soname.*

%files -n libigfxcmrt-devel
%_libdir/libigfxcmrt.so
%_includedir/igfxcmrt
%_pkgconfigdir/igfxcmrt.pc

%changelog
* Mon Apr 20 2020 Anton Farygin <rider@altlinux.ru> 20.1.1-alt1
- 20.1.1

* Mon Jan 13 2020 Anton Farygin <rider@altlinux.ru> 19.4.0-alt1
- 19.4.0

* Wed Nov 13 2019 Anton Farygin <rider@altlinux.ru> 19.3.1-alt1
- 19.3.1

* Sat Oct 12 2019 Anton Farygin <rider@altlinux.ru> 19.3.0-alt1
- 19.3.0

* Thu Aug 15 2019 Anton Farygin <rider@altlinux.ru> 19.2.1-alt1
- 19.2.1

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 19.1.0-alt2
- NMU: remove rpm-build-ubt from BR:

* Fri Apr 26 2019 Anton Farygin <rider@altlinux.ru> 19.1.0-alt1
- 19.1.0

* Mon Feb 18 2019 Anton Farygin <rider@altlinux.ru> 18.4.1-alt1
- 18.4.1

* Mon Oct 08 2018 Anton Farygin <rider@altlinux.ru> 18.3.0-alt1
- first build for ALT

