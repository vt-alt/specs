%define build_type RelWithDebInfo
%define _cmake %cmake -DCMAKE_BUILD_TYPE=%build_type -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON

Name: glslang
Version: 7.12.3352
Release: alt1

Summary: OpenGL and OpenGL ES shader front end and validator
Group: Development/C++
License: BSD

Url: https://www.khronos.org/opengles/sdk/tools/Reference-Compiler/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: https://github.com/KhronosGroup/%name/archive/%version/%name-%version.tar.gz
Patch0: %{name}-alt-soname.patch
Patch1: %{name}-alt-shared-opt.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: python3-devel libspirv-tools-devel = 2019.4

%description
glslang is the official reference compiler front end for the OpenGL
ES and OpenGL shading languages. It implements a strict
interpretation of the specifications for these languages.

spirv-remap is a utility to improve compression of SPIR-V binary
files via entropy reduction, plus optional stripping of debug
information and load/store optimization. It transforms SPIR-V to
SPIR-V, remapping IDs. The resulting modules have an increased ID
range (IDs are not as tightly packed around zero), but will compress
better when multiple modules are compressed together, since
compressor's dictionary can find better cross module commonality.

%package -n lib%{name}0
Summary: %{name} shared libraries
Group: Development/C++

%description -n lib%{name}0
Contains shared libraries used by %{name}.

%package devel
Summary: %name development headers and libraries
Group: Development/C++
Requires: %name = %EVR

%description devel
%name development headers and libraries.

%prep
%setup
%patch0 -p2
%patch1 -p2

%build
%_cmake \
  -DBUILD_SHARED_LIBS:BOOL=TRUE \
  -DCMAKE_INSTALL_LIBDIR=%_libdir
%cmake_build
%cmakeinstall_std

%files
%doc README-spirv-remap.txt
%_bindir/*

%files -n lib%{name}0
%_libdir/*.so.*

%files devel
%doc README.md
%_libdir/lib*.so
%_includedir/%name
%_includedir/SPIRV

%changelog
* Thu Aug 29 2019 L.A. Kostis <lakostis@altlinux.ru> 7.12.3352-alt1
- stable release August 20, 2019 (7.12.3352).
- added strict dependency to spirv-tools.

* Fri May 03 2019 L.A. Kostis <lakostis@altlinux.ru> 7.11.3188-alt2
- Try to fix build w/ shared libspirv-tools.

* Thu May 02 2019 L.A. Kostis <lakostis@altlinux.ru> 7.11.3188-alt1
- bump to stable release April 5, 2019 (7.11.3188).
- .spec: cleanups
- build shared libs.

* Sun Mar 11 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.2.2596-alt2%%ubt
- fix install paths

* Sat Mar 10 2018 Nazarov Denis <nenderus@altlinux.org> 6.2.2596-alt1%%ubt
- Version 6.2.2596

* Tue Apr 18 2017 Nazarov Denis <nenderus@altlinux.org> 3.0-alt1.M80P.1
- Build for branch p8

* Sun Apr 16 2017 Nazarov Denis <nenderus@altlinux.org> 3.0-alt2
- Update to latest from git

* Sun Apr 16 2017 Nazarov Denis <nenderus@altlinux.org> 3.0-alt1
- Initial build for ALT Linux
