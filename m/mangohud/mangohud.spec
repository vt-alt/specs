%define uname   MangoHud
%define srcname %uname-v%version-Source

Name: mangohud
Version: 0.6.1
Release: alt1

Summary: A Vulkan overlay layer for monitoring FPS, temperatures, CPU/GPU load and more
License: MIT
Group: Games/Arcade

Url: https://github.com/flightlessmango/MangoHud
# DFSG tarball excludes nonfree nvml.h
Source: https://github.com/flightlessmango/MangoHud/releases/download/v%version/%srcname-DFSG.tar.gz

BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: glslang
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(x11)
BuildRequires: python3(mako)

%description
A Vulkan overlay layer for monitoring FPS, temperatures, CPU/GPU load and more.

To enable the MangoHud Vulkan overlay layer, set `MANGOHUD=1` in the shell,
or use the `mangohud` command to launch programs.
See '%_docdir/%name' for configuration details.
%ifarch %ix86 x86_64

The `goverlay` package provides a third-party GUI frontend for MangoHud.
%endif

%prep
%setup -n %srcname

%build
%meson \
  -Dinclude_doc=false \
  -Duse_system_vulkan=enabled \
  -Dwith_nvml=disabled \
  -Dwith_xnvctrl=disabled
# NVML is nonfree, XNVCtrl is not packaged yet (but could be enabled if it is)

%meson_build

%install
%meson_install

%files
%doc README.md bin/%uname.conf
%doc LICENSE
%_bindir/%name
%_libdir/%name/
%_datadir/vulkan/implicit_layer.d/%uname.json
%_man1dir/%name.1*

%changelog
* Wed Apr 21 2021 Michael Shigorin <mike@altlinux.org> 0.6.1-alt1
- initial build for ALT Sisyphus (thx Mageia)

* Wed Dec 30 2020 akien <akien> 0.6.1-1.mga8
+ Revision: 1665672
- Version 0.6.1

* Fri Oct 23 2020 akien <akien> 0.5.1-1.mga8
+ Revision: 1638865
- Version 0.5.1
- Require vulkan-loader lib explicitly

* Thu Jun 11 2020 akien <akien> 0.4.1-1.mga8
+ Revision: 1592504
- Version 0.4.1

* Fri Feb 14 2020 akien <akien> 0.2.0-1.mga8
+ Revision: 1519991
- imported package mangohud

