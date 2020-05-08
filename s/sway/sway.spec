%define _unpackaged_files_terminate_build 1

Name: sway
Version: 1.4
Release: alt1.1.p9
Epoch:   1
Summary: i3wm drop-in replacement for Wayland
License: MIT
Url: http://swaywm.org/
Group: Graphical desktop/Other

# https://github.com/swaywm/sway
# git://git.altlinux.org/gears/s/sway.git
Source0: %name-%version.tar
Source1: startsway
Source2: Sway_Wallpaper_Gray.png

Patch00: sway-config.patch

BuildRequires: gcc-c++
BuildRequires: asciidoc-a2x
BuildRequires: cmake
BuildRequires: libcap-devel
BuildRequires: libdbus-devel
BuildRequires: libevdev-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: libjson-c-devel
BuildRequires: libpam-devel
BuildRequires: libpango-devel
BuildRequires: libpcre-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libwlc0-devel
BuildRequires: libwlc-devel >= 0.0.10
BuildRequires: libwlroots-devel >= 0.10.1-alt2
BuildRequires: libGLES-devel
BuildRequires: meson
BuildRequires: scdoc
BuildRequires: time

# swaybg is now distributed as a standalone program which is compatible with many Wayland compositors (sway 1.1-rc1)
Requires: swaybg

# swayidle, a new idle management daemon, is available separately (sway 1.0)
Requires: swayidle

Requires: dmenu-wl
Requires: %name-data

%description
Sway is a drop-in replacement for the i3 window manager, but for Wayland
instead of X11. It works with your existing i3 configuration and
supports most of i3's features, and a few extras.

%package data
Summary: i3wm drop-in replacement for Wayland - data files
Group: Graphical desktop/Other
BuildArch: noarch

%description data
This package contains data files.

%prep
%setup
%patch00 -p2

%build
%meson \
	-Dwerror=false \
	#
%meson_build

%install
%meson_install

mkdir -p %buildroot/%_sysconfdir/%name/config.d

install -p -m0755 -D %SOURCE1 %buildroot/%_bindir/
install -p -m0644 -D %SOURCE2 %buildroot/%_datadir/backgrounds/%name/

rm -rf -- \
	%buildroot/%_datadir/bash-completion \
	%buildroot/%_datadir/fish \
	%buildroot/%_datadir/zsh \
	#

%files
%doc LICENSE
%doc README.md
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/config.d
%dir %_sysconfdir/%name/security.d
%config(noreplace) %_sysconfdir/%name/config
%config(noreplace) %_sysconfdir/%name/security.d/00-defaults
%_bindir/sway
%_bindir/startsway
%_bindir/swaybar
%_bindir/swaymsg
%_bindir/swaynag
%_man1dir/*
%_man5dir/*
%_man7dir/*
%_datadir/wayland-sessions/sway.desktop

%files data
%dir %_datadir/backgrounds/%name
%_datadir/backgrounds/%name/*

%changelog
* Wed Apr 29 2020 Andrey Cherepanov <cas@altlinux.org> 1:1.4-alt1.1.p9
- Backport new version to p9 branch.

* Fri Mar 27 2020 Alexey Gladkov <legion@altlinux.ru> 1:1.4-alt2
- Remove privilege escalation.

* Wed Mar 25 2020 Alexey Gladkov <legion@altlinux.ru> 1:1.4-alt1
- New version (1.4)

* Sat Dec 07 2019 Alexey Gladkov <legion@altlinux.ru> 1:1.2-alt2
- Fix BuildRequires.

* Wed Nov 06 2019 Alexey Gladkov <legion@altlinux.ru> 1:1.2-alt1
- New version (1.2)

* Fri Aug 09 2019 Alexey Gladkov <legion@altlinux.ru> 1.2.rc1-alt1
- New version (1.2-rc1)

* Thu Aug 08 2019 Alexey Gladkov <legion@altlinux.ru> 1.1.1-alt2
- Rewrite startsway script:
  + Set XDG_* env variables to some default values
  + Start dbus session (optional)
- Require dmenu-wl

* Tue Jun 04 2019 Alexey Gladkov <legion@altlinux.ru> 1.1.1-alt1
- New version (1.1.1)

* Wed May 22 2019 Alexey Gladkov <legion@altlinux.ru> 1.1-alt1.rc3
- New version (1.1-rc3)

* Sun Mar 24 2019 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1
- New version (1.0)

* Thu Jan 03 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt0.beta.2.0.75.g4a3ada30.1
- Updated to 1.0-beta.2-75-g4a3ada30.

* Mon Apr 16 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.15.2-alt1
- 0.15.2
- added startsway script

* Mon Jul 31 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.14.0-alt1
- 0.14.0
- fixed capabilities setting

* Wed May 10 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.13.0-alt1
- 0.13.0

* Sat Apr 08 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.12.2-alt1
- 0.12.2
- set CAP_SYS_TTY_CONFIG to sway binary

* Wed Mar 15 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.12-alt2
- added swaylock.
- fixed post requires type.
- removed control file.

* Sat Mar 11 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.12-alt1
- 0.12
- fixed: set CAP_SYS_PTRACE to sway binary
- upstream changes:
 + %%_sysconfdir/%%name/security config is no longer used by sway
 + added security configs dir: %%_sysconfdir/%%name/security.d

* Tue Feb 28 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.11-alt1
- 0.11
- fixed: system configs are noreplace now

* Sat Oct 29 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.10-alt1
- 0.10

* Thu Sep 22 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9-alt1
- Initial build
