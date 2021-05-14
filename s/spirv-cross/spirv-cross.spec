%define build_type RelWithDebInfo
%define _cmake %cmake -DCMAKE_BUILD_TYPE=%build_type -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON -DCMAKE_INSTALL_LIBDIR=%_datadir
%define sover 0
%def_disable static

Name: spirv-cross
Version: 2020.06.29
Release: alt0.1

Summary: tool to parse and convert SPIR-V to other shader languages
Group: Development/C++
License: Apache-2.0

URL: https://github.com/KhronosGroup/SPIRV-Cross
Packager: L.A. Kostis <lakostis@altlinux.org>

Source: %name-%version.tar
Patch: %name-alt-cmake-path.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++

%description
SPIRV-Cross is a practical tool and library for performing reflection on SPIR-V
and disassembling SPIR-V back to high level languages.

%package -n lib%{name}-devel
Summary: %name devel libraries and headers
Group: Development/C++
Requires: lib%{name}-c-shared%{sover} = %EVR

%description -n lib%{name}-devel
%name development libraries and headers

%package -n lib%{name}-c-shared%{sover}
Summary: %name support libraries
Group: System/Libraries
Provides: lib%{name} = %EVR

%description -n lib%{name}-c-shared%{sover}
%name support libraries

%prep
%setup -n %name-%version
%patch -p1

%build
%_cmake \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
%if_disabled static
  -DSPIRV_CROSS_STATIC=OFF \
  -DSPIRV_CROSS_CLI=OFF \
%endif
  -DSPIRV_CROSS_SHARED=ON
%cmake_build
%cmakeinstall_std

%files -n lib%{name}-c-shared%{sover}
%_libdir/*.so.*

%files -n lib%{name}-devel
%_includedir/spirv_cross
%_pkgconfigdir/*.pc
%_libdir/*.so
%_datadir/cmake/*

%changelog
* Tue Sep 08 2020 L.A. Kostis <lakostis@altlinux.ru> 2020.06.29-alt0.1
- Initial build for Sisyphus.
