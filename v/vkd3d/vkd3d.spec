%def_disable demos
%define major 1

Name: vkd3d
Version: 1.2
Release: alt1
Summary: The vkd3d 3D Graphics Library

Group: System/Libraries
License: LGPL-2.1
Url: https://source.winehq.org/git/vkd3d.git/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libvulkan-devel spirv-headers libwine-vanilla-devel
BuildRequires: libspirv-tools-devel spirv-tools
%if_enabled demos
BuildRequires: libxcb-devel libxcbutil-devel libxcbutil-keysyms-devel libxcbutil-icccm-devel
%endif

# same as wine
ExclusiveArch: %ix86 x86_64 aarch64

%description
Vkd3d is a 3D graphics library built on top of Vulkan. It has an API very
similar, but not identical, to Direct3D 12.

%package -n lib%{name}%{major}
Summary: %{name} libraries
Group: System/Libraries

%description -n lib%{name}%{major}
Vkd3d is a 3D graphics library built on top of Vulkan. It has an API very
similar, but not identical, to Direct3D 12.

%package devel
Summary: %name development package
Group: Development/C
Requires: lib%{name}%{major} = %EVR
Requires: %name-utils = %EVR

%description devel
Development headers for %name.

%package utils
Summary: %name utils
Group: Development/C
Requires: lib%{name}%{major} = %EVR

%description utils
%name utils.

%package demos
Summary: %name demos
Group: Development/C
Requires: lib%{name}%{major} = %EVR

%description demos
%name demos.

%prep
%setup
%patch -p1
%autoreconf
%configure \
  %{subst_enable demos} \
  --with-spirv-tools

%build
%make_build

%install
%makeinstall
%if_enabled demos
mkdir -p %buildroot%_bindir
for f in demos/{gears,triangle}; do
  cp -a "$i" %buildroot%_bindir/%{name}_"$f";
done
%endif

%files -n lib%{name}%{major}
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files utils
%_bindir/vkd3d-compiler

%if_enabled demos
%files demos
%_bindir/*
%exclude %_bindir/vkd3d-compiler
%endif

%changelog
* Fri Oct 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2-alt1
- Updated to upstream release version 1.2 (ALT #39002).

* Sun Jul 19 2020 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt0.6.g4bea4b8
- GIT 4bea4b8.
- Fix License.
- Add exclusivearch.

* Sat Jun 06 2020 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt0.5.gf68bf0d
- GIT f68bf0d.

* Sun May 10 2020 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt0.4.gc8c05c7
- GIT c8c05c7.

* Sun May 05 2019 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt0.3.gbe4ca96
- GIT be4ca96.

* Thu Feb 07 2019 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt0.2.gfd3d661
- GIT fd3d661.

* Mon Dec 03 2018 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt0.1
- Bump to 1.1 release.
- Disable demos and libxcb (can be enabled one day).

* Mon Jun 18 2018 L.A. Kostis <lakostis@altlinux.ru> 1.0-alt0.1.g04b9d19
- Initial build for ALTLinux.
