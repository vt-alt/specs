%global appid net.lutris.Lutris
Name: lutris
Version: 0.5.3
Release: alt1
Summary: Manager for game installation and execution
License: GPL-3.0
Group: Games/Other
Url: http://lutris.net

Source: http://lutris.net/releases/lutris_%version.tar.xz
Patch: lutris-python3-pixbuf-path.patch

# Automatically added by buildreq on Fri Aug 30 2019 (-bi)
# optimized out: bash4 bashrc kmod perl python-base python-modules python3 python3-base python3-dev python3-module-pkg_resources rpm-build-python3 sh4 tzdata xz
BuildRequires: eject fuse python3-module-setuptools rpm-build-gir unzip xlsfonts
#BuildRequires: gobject-introspection-devel icon-theme-hicolor python3-devel python3-module-pygobject3 python3-module-pygobject3-pygtkcompat libgdk-pixbuf-gir-devel libgtk+3-gir libwebkit2gtk-gir libnotify-gir libgnome-desktop3-gir python3-module-distutils-extra python3-module-setuptools
Requires: cabextract fluid-soundfont-gm python3-module-Pillow python3-module-yaml python3-module-pygobject python3-module-requests winetricks libgdk-pixbuf-gir psmisc libgnome-desktop3-gir xrandr pciutils
# controller support
Requires: python3-module-evdev

BuildArch: noarch

%description
Lutris allows to gather and manage (install, configure and launch)
all games acquired from any source, in a single interface.
This includes, for example, Steam or Desura games, Windows games (WINE),
or emulated console games and browser games.

%prep
%setup -n %name
%patch -p2

%build
%python3_build

%install
%python3_install

%files
%doc README.rst CONTRIBUTING.md AUTHORS
%doc LICENSE
%_bindir/%name
%_bindir/lutris-wrapper
%_datadir/%name/
%_desktopdir/%appid.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/??x??/apps/%name.png
%_datadir/polkit-1/actions/*
%python3_sitelibdir/%name-*.egg-info
%python3_sitelibdir/%name/
%dir %_datadir/metainfo/
%_datadir/metainfo/%appid.appdata.xml

%changelog
* Mon Sep 09 2019 Leontiy Volodin <lvol@altlinux.org> 0.5.3-alt1
- New version (0.5.3) with rpmgs script.

* Fri Aug 30 2019 Leontiy Volodin <lvol@altlinux.org> 0.5.2.2-alt1
- Initial build for ALT Sisyphus (thanks opensuse for this spec) (ALT #37168).
