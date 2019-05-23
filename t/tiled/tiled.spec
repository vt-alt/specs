%define _unpackaged_files_terminate_build 1

Name: tiled
Version: 1.2.4
Release: alt1
Summary: Tiled is a general purpose tile map editor
License: GPLv2
Group: Graphics
Url: http://www.mapeditor.org
# https://github.com/bjorn/tiled
Source: %name-%version.tar

BuildRequires(pre): rpm-build-xdg
BuildRequires: gcc-c++ qt5-base-devel qt5-tools zlib-devel

%description
Tiled is a general purpose tile map editor. It is meant to be used for
editing maps of any tile-based game, be it an RPG, a platformer or a
Breakout clone. Tiled is very flexible, for example there are no
restrictions on map size, tile size or the number of layers or tiles.
Also, it allows arbitrary properties to be set on the map, its layers,
the tiles or on the objects. Its map format (TMX) is relatively easy to
understand and allows a map to use multiple tilesets while also
allowing each tileset to grow or shrink as necessary later.

%prep
%setup

%build
%qmake_qt5 %name.pro -r PREFIX=%_prefix LIBDIR=%_libdir
%make_build

%install
%make INSTALL_ROOT=%buildroot install

%files
%_bindir/*
%_libdir/*.so*
%_libdir/%name
%_man1dir/*
%_datadir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*
%_xdgmimedir/packages/*.xml
%_datadir/thumbnailers/*.thumbnailer
%_datadir/metainfo/*.xml

%changelog
* Mon May 20 2019 Grigory Ustinov <grenka@altlinux.org> 1.2.4-alt1
- Build new version.

* Wed Mar 13 2019 Grigory Ustinov <grenka@altlinux.org> 1.2.3-alt1
- Build new version.

* Tue Jan 29 2019 Grigory Ustinov <grenka@altlinux.org> 1.2.2-alt1
- Build new version.

* Sun Jan 06 2019 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1
- Build new version.

* Mon Apr 02 2018 Dmitriy Zagrebin <dzagrebin@altlinux.org> 1.1.4-alt1
- Initial build for ALT
