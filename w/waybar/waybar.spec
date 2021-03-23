Name: waybar
Version: 0.9.5
Release: alt1
License: MIT
Summary: Highly customizable Wayland bar for Sway and Wlroots based compositors
URL: https://github.com/Alexays/Waybar.git
Group: Graphical desktop/Other

Source: %name-%version.tar
Source1: xkb-layout.py
Source2: clock.py

Patch0: waybar-config.patch
Patch1: 0001-Drop-the-clock-module-and-the-date-dependency.patch

BuildRequires(pre): rpm-build-xdg

BuildRequires: cmake meson
BuildRequires: gcc-c++
BuildRequires: jsoncpp-devel
BuildRequires: libfmt-devel
BuildRequires: libgtkmm3-devel
BuildRequires: libinput-devel
BuildRequires: libsigc++2-devel
BuildRequires: libspdlog-devel
BuildRequires: libstdc++-devel-static
BuildRequires: libwayland-client-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: wayland-protocols

# sni module
BuildRequires: libdbusmenu-gtk3-devel
BuildRequires: libgio-devel

# pulseaudio module
BuildRequires: libpulseaudio-devel

# backlight
BuildRequires: libudev-devel

# network module
BuildRequires: libnl-devel

# mpd module
# BuildRequires: libmpdclient-devel

%define _libexecdir %_prefix/libexec
%define helperdir %_libexecdir/%name

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%meson \
	-Drfkill=enabled \
	-Dgtk-layer-shell=disabled \
	-Dsystemd=disabled
%meson_build

%install
%meson_install

mkdir -p -- %buildroot/%helperdir
install -m 755 -- %SOURCE1 %buildroot/%helperdir/
install -m 755 -- %SOURCE2 %buildroot/%helperdir/

%check
%meson_test

%files
%_bindir/%name
%dir %_xdgconfigdir/%name
%config(noreplace) %_xdgconfigdir/%name/config
%config(noreplace) %_xdgconfigdir/%name/style.css
%helperdir

%changelog
* Fri Jan 08 2021 Alexey Gladkov <legion@altlinux.ru> 0.9.5-alt1
- New version (0.9.5)
- Replace clock module by custom version.

* Sat Dec 28 2019 Alexey Gladkov <legion@altlinux.ru> 0.9.0-alt1
- New version (0.9.0)
- Add xkb-layout module

* Thu Aug 08 2019 Alexey Gladkov <legion@altlinux.ru> 0.7.2-alt1
- New version (0.7.2)

* Wed May 22 2019 Alexey Gladkov <legion@altlinux.ru> 0.6.6-alt1
- 0.6.6

* Sat May 18 2019 Alexey Gladkov <legion@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Tue Apr 02 2019 Alexey Gladkov <legion@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Thu Jan 03 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.3-alt1
- Initial build.
