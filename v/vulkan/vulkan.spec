%define build_type RelWithDebInfo
%define _cmake %cmake -DCMAKE_BUILD_TYPE=%build_type -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON

Name: vulkan
Version: 1.1.121
Release: alt1.1
Summary: Khronos group Vulkan API SDK

Group: System/Libraries
License: ASL 2.0
Url: http://www.khronos.org/

# https://github.com/KhronosGroup/Vulkan-Loader
Source0: vulkan-loader.tar.xz
# https://github.com/KhronosGroup/Vulkan-Headers
Source1: vulkan-headers.tar.xz
# https://github.com/KhronosGroup/Vulkan-Tools
Source2: vulkan-tools.tar.xz
# https://github.com/KhronosGroup/Vulkan-ValidationLayers
Source3: vulkan-layers.tar.xz

BuildRequires: bison chrpath
BuildRequires(pre): cmake gcc-c++ rpm-build-python3
BuildRequires: libImageMagick-devel libpciaccess-devel libsystemd-devel
BuildRequires: python3-devel libxcb-devel libXau-devel libXdmcp-devel libX11-devel libXrandr-devel
BuildRequires: wayland-devel libwayland-server-devel libwayland-client-devel libwayland-cursor-devel libwayland-egl-devel
# strict requires due internal dependency
BuildRequires: glslang-devel = 7.12.3352
BuildRequires: libspirv-tools-devel = 2019.4

# textrel due asm optimisation in loader code
%ifarch i586
%set_verify_elf_method textrel=relaxed
%endif

# filter out self-provided requires
%add_python3_req_skip spec_tools.util

%description
Vulkan is a new generation graphics and compute API that provides
high-efficiency, cross-platform access to modern GPUs used in a wide
variety of devices from PCs and consoles to mobile phones and embedded
platforms.

This package contains the reference ICD loader and API validation layer for
Vulkan.

%package -n lib%{name}1
Summary: Vulkan loader libraries
Group: System/Libraries
Requires: vulkan-filesystem = %version-%release
Provides: %name = %version-%release
Obsoletes: %name

%description -n lib%{name}1
Vulkan is a new generation graphics and compute API that provides
high-efficiency, cross-platform access to modern GPUs used in a wide
variety of devices from PCs and consoles to mobile phones and embedded
platforms.

This package contains the reference ICD loader for Vulkan.

%package validation-layers
Summary: Vulkan API validation layers
Group: Development/C++
Requires: lib%{name}1 = %version-%release

%description validation-layers
Vulkan API validation layer for developers.

%package -n lib%name-devel
Summary: Vulkan development package
Group: Development/C++
Requires: lib%{name}1 = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel

%description -n lib%name-devel
Development headers for Vulkan applications.

%package filesystem
Summary: Vulkan filesystem package
Group: System/Base
BuildArch: noarch

%description filesystem
Filesystem for Vulkan API.

%package tools
Summary: Vulkan tools and utilities
Group: System/X11
Requires: lib%{name}1 = %version-%release
Obsoletes: %name-demos

%description tools
Tools and utilities that can assist development by enabling developers to
verify their applications correct use of the Vulkan API.

%prep
%setup -n %name-loader -b0 -b1 -b2 -b3
pushd ../vulkan-layers
# sigh inttypes
sed -i 's/inttypes.h/cinttypes/' layers/*.{cpp,h}
popd

%build
# vulkan-headers first
pushd %_builddir/vulkan-headers
%_cmake
%cmake_build
%cmakeinstall_std
popd

# then vulkan-loader and layers
for dir in loader layers; do
pushd %_builddir/vulkan-"$dir"
%_cmake \
           -DSPIRV_TOOLS_SEARCH_PATH=%_libdir \
           -DSPIRV_TOOLS_OPT_SEARCH_PATH=%_libdir \
	   -DVULKAN_HEADERS_INSTALL_DIR=%buildroot \
	   -DGLSLANG_INSTALL_DIR=%_prefix \
	   -DVulkanHeaders_INCLUDE_DIR=%buildroot%_includedir
%cmake_build
%cmakeinstall_std
popd
done

# end finally -tools
pushd %_builddir/vulkan-tools
%_cmake \
	   -DCMAKE_PREFIX_PATH=%buildroot%prefix \
	   -DGLSLANG_INSTALL_DIR=%_prefix
%cmake_build
%cmakeinstall_std
popd

%install
# do it again
for dir in headers layers loader tools; do
pushd %_builddir/vulkan-"$dir"
%cmakeinstall_std
popd
done
mkdir -p %buildroot%_sysconfdir/vulkan/explicit_layer.d
mkdir -p %buildroot%_datadir/vulkan/{explicit,implicit}_layer.d/ ||:
mkdir -p %buildroot%_datadir/vulkan/icd.d ||:

# remove RPATH
chrpath -d %buildroot%_bindir/vulkaninfo

%files tools
%_bindir/*

%files -n lib%{name}1
%doc README.md LICENSE.txt
%_libdir/libvulkan.so.1*

%files -n lib%name-devel
%dir %_includedir/vulkan
%_includedir/vulkan
%_libdir/libvulkan.so
%_pkgconfigdir/vulkan.pc
%_datadir/vulkan/registry
# requires vulkan-docs tools
%exclude %_datadir/vulkan/registry/genvk.py

%files validation-layers
%_includedir/*
%exclude %_includedir/vulkan
%_datadir/vulkan/explicit_layer.d/*.json
%_libdir/libVkLayer*.so
%_libdir/libVkLayer*.a

%files filesystem
%dir %_sysconfdir/vulkan
%dir %_sysconfdir/vulkan/explicit_layer.d
%dir %_datadir/vulkan
%dir %_datadir/vulkan/icd.d
%dir %_datadir/vulkan/explicit_layer.d
%dir %_datadir/vulkan/implicit_layer.d

%changelog
* Thu Aug 29 2019 L.A. Kostis <lakostis@altlinux.ru> 1.1.121-alt1.1
- Fix python3 requires.

* Thu Aug 29 2019 L.A. Kostis <lakostis@altlinux.ru> 1.1.121-alt1
- Updated to v1.1.121.
- .spec: relocate some dirs from -validation-layers to -filesystem.

* Mon May 06 2019 L.A. Kostis <lakostis@altlinux.ru> 1.1.107-alt1
- Updated to v1.1.107:
  + vulkan-headers v1.1.107.
  + vulkan-loader v1.1.107.
  + vulkan-tools v1.1.107.
  + vulkan-validation-layers v1.1.106.

* Fri May 03 2019 L.A. Kostis <lakostis@altlinux.ru> 1.1.101-alt3
- Relax glslang/libspirv-tools requires.

* Thu May 02 2019 L.A. Kostis <lakostis@altlinux.ru> 1.1.101-alt2
- Rebuild w/ system glslang and spirv-tools.

* Tue Mar 05 2019 L.A. Kostis <lakostis@altlinux.ru> 1.1.101-alt1
- Updated to SDK 1.1.101:
  + spirv-tools GIT 5994ae2a0.
  + spirv-headers GIT 79b6681aa.
  + vulkan-headers GIT 8e2c4cd55.
  + vulkan-loader GIT 3d7d8dc83.
  + vulkan-tools GIT 18ac58d9c.

* Wed Jan 02 2019 L.A. Kostis <lakostis@altlinux.ru> 1.1.96-alt1
- Updated to SDK 1.1.96:
  - headers v1.1.96
  - loader GIT 15e3d18ce
  - layers GIT b458d8622
  - tools GIT 9d4727c6a
- Rewrote .spec for new code infrastructure:
  - simplify build flags
  - demos->tools
  - added registry to -devel
  - added extra headers and libs for -layers
  - enable optimisation for glslang.

* Fri Mar 16 2018 L.A. Kostis <lakostis@altlinux.ru> 1.1.70-alt1
- Updated to vulkan sdk-1.1.70.

* Mon Mar 12 2018 L.A. Kostis <lakostis@altlinux.ru> 1.0.68-alt0.1
- Updated to vulkan sdk-1.0.68:
  + glslang 2651cca.
  + spirv-tools 9e19fc0.
  + spirv-headers ce30920.

* Sun Oct 08 2017 L.A. Kostis <lakostis@altlinux.ru> 1.0.61-alt0.2
- i586: Don't check for textrel due asm optimization in loader code.

* Sat Oct 07 2017 L.A. Kostis <lakostis@altlinux.ru> 1.0.61-alt0.1
- Updated to vulkan sdk-1.0.61:
  + glslang 3a21c88.
  + spirv-tools 7e2d26c.
  + spirv-headers 2bb92e6.

* Wed Jun 07 2017 L.A. Kostis <lakostis@altlinux.ru> 1.0.51-alt0.2.115665a
- Fix Obsoletes.
- libvulkan->libvulkan1 in accordance with ALT Shared Libs Policy.

* Wed Jun 07 2017 L.A. Kostis <lakostis@altlinux.ru> 1.0.51-alt0.1.115665a
- Bumped to vulkan sdk GIT 115665a:
  + glslang 136b1e2.
  + spirv-tools e7aff80.
  + spirv-headers 63e1062.

* Tue Jun 06 2017 L.A. Kostis <lakostis@altlinux.ru> 1.0.42-alt0.2
- .spec re-write:
  + sync with Fedora packaging.
  + remove rpath from vk (patch taken from debian.org).
  + split libvulkan and validation layers.
  + move demos to separate package (as for Mesa).

* Sun Mar 19 2017 L.A. Kostis <lakostis@altlinux.ru> 1.0.42-alt0.1
- Updated to vulkan sdk-1.0.42:
  + glslang dfbdd9.
  + spirv-tools c3caa5.
  + spirv-headers f61848.
- SPIRV-Tools: use python3 by default.

* Wed Dec 28 2016 L.A. Kostis <lakostis@altlinux.ru> 1.0.37-alt0.3
- .spec: use cmake macros instead of ugly hacks.

* Mon Dec 26 2016 L.A. Kostis <lakostis@altlinux.ru> 1.0.37-alt0.2
- Updated builreq: added wayland.

* Mon Dec 26 2016 L.A. Kostis <lakostis@altlinux.ru> 1.0.37-alt0.1
- Updated to vulkan sdk-1.0.37:
  + glslang 6a60c2.
  + spirv-tools 945e9f.
  + spirv-headers c470b6.

* Sat Oct 01 2016 L.A. Kostis <lakostis@altlinux.ru> 1.0.26-alt0.1
- First build for ALTLinux.

* Tue Feb 16 2016 Adam Jackson <ajax@redhat.com> - 1.0.3-2
- Update loader to not build cube or tri. Drop bundled LunarGLASS and llvm
  since they're only needed for those demos.

* Tue Feb 16 2016 Adam Jackson <ajax@redhat.com> - 1.0.3-1
- Initial packaging
