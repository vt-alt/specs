%define _unpackaged_files_terminate_build 1

Name: tiled
Version: 1.4.2
Release: alt1
Summary: Tiled is a general purpose tile map editor
License: GPLv2
Group: Graphics
Url: http://www.mapeditor.org
# https://github.com/bjorn/tiled
Source: %name-%version.tar

BuildRequires(pre): rpm-build-xdg
BuildRequires: gcc-c++ qt5-base-devel qt5-tools zlib-devel
BuildRequires: qt5-declarative-devel

%description
Tiled is a general purpose tile map editor. It is meant to be used for
editing maps of any tile-based game, be it an RPG, a platformer or a
Breakout clone. Tiled is very flexible, for example there are no
restrictions on map size, tile size or the number of layers or tiles.
Also, it allows arbitrary properties to be set on the map, its layers,
the tiles or on the objects. Its map format (TMX) is relatively easy to
understand and allows a map to use multiple tilesets while also
allowing each tileset to grow or shrink as necessary later.

%package plugin-tbin
Summary: tBIN plugin for Tiled
Group: Graphics
Requires: %name = %EVR
%description plugin-tbin
A plugin for tiled which allows support for the tBIN map format.

%package plugin-droidcraft
Summary: Droidcraft plugin for Tiled
Group: Graphics
Requires: %name = %EVR
%description plugin-droidcraft
A plugin for tiled which allows to save maps as .dat droidcraft maps.

%package plugin-flare
Summary: Flare plugin for Tiled
Group: Graphics
Requires: %name = %EVR
%description plugin-flare
A plugin for tiled which allows to save maps as .txt flare maps.

%package plugin-replica-island
Summary: Replica Island plugin for Tiled
Group: Graphics
Requires: %name = %EVR
%description plugin-replica-island
A plugin for tiled which allows to save maps as .bin Replica Island maps.

%package plugin-t-engine4
Summary: T-Engine4 plugin for Tiled
Group: Graphics
Requires: %name = %EVR
%description plugin-t-engine4
A plugin for tiled which allows to export maps as .lua T-Engine4 maps.

%package plugin-defold
Summary: Defold plugin for Tiled
Group: Graphics
Requires: %name = %EVR
%description plugin-defold
A plugin for tiled which allows to export maps as .tilemap Defold maps.

%package plugin-gmx
Summary: GameMaker Studio plugin for Tiled
Group: Graphics
Requires: %name = %EVR
%description plugin-gmx
A plugin for tiled which allows to export maps as GameMaker Studio room files.

%prep
%setup

%build
%qmake_qt5 %name.pro -r RPATH=no PREFIX=%_prefix LIBDIR=%_libdir
%make_build

%install
%make INSTALL_ROOT=%buildroot install

# locale files
%find_lang %name --with-qt

%files -f %name.lang
%doc AUTHORS NEWS.md README.md COPYING LICENSE.GPL LICENSE.BSD
%_bindir/%name
%_bindir/terraingenerator
%_bindir/tmxrasterizer
%_bindir/tmxviewer
%_iconsdir/hicolor/*/apps/*%{name}*
%_iconsdir/hicolor/*/mimetypes/*%{name}*
%_datadir/applications/org.mapeditor.Tiled.desktop
%_datadir/metainfo/org.mapeditor.Tiled.appdata.xml
%_datadir/mime/packages/org.mapeditor.Tiled.xml
%dir %_datadir/%name/
%dir %_datadir/%name/translations
%_libdir/lib%name.so*

%dir %_libdir/%name/
%dir %_libdir/%name/plugins/

# Core plugins
%_libdir/%name/plugins/libcsv.so
%_libdir/%name/plugins/libjson.so
%_libdir/%name/plugins/liblua.so
%_libdir/%name/plugins/libjson1.so
%_libdir/%name/plugins/libdefoldcollection.so

%_mandir/man1/%name.1*
%_mandir/man1/tmxrasterizer.1*
%_mandir/man1/tmxviewer.1*
%dir %_datadir/thumbnailers
%_datadir/thumbnailers/%name.thumbnailer

# Fix post-install onowned files
%_iconsdir/hicolor/scalable
%_datadir/metainfo

%files plugin-tbin
%_libdir/%name/plugins/libtbin.so

%files plugin-droidcraft
%_libdir/%name/plugins/libdroidcraft.so

%files plugin-flare
%_libdir/%name/plugins/libflare.so

%files plugin-replica-island
%_libdir/%name/plugins/libreplicaisland.so

%files plugin-t-engine4
%_libdir/%name/plugins/libtengine.so

%files plugin-defold
%_libdir/%name/plugins/libdefold.so

%files plugin-gmx
%_libdir/%name/plugins/libgmx.so

%changelog
* Sun Aug 23 2020 Grigory Ustinov <grenka@altlinux.org> 1.4.2-alt1
- Automatically updated to 1.4.2.

* Sat Jun 27 2020 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1
- Automatically updated to 1.4.1.

* Sun Jun 21 2020 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt1
- Automatically updated to 1.4.0.

* Thu May 28 2020 Grigory Ustinov <grenka@altlinux.org> 1.3.5-alt1
- Automatically updated to 1.3.5.

* Mon Apr 27 2020 Grigory Ustinov <grenka@altlinux.org> 1.3.4-alt1
- Automatically updated to 1.3.4.

* Mon Mar 16 2020 Grigory Ustinov <grenka@altlinux.org> 1.3.3-alt1
- Automatically updated to 1.3.3.

* Wed Feb 05 2020 Grigory Ustinov <grenka@altlinux.org> 1.3.2-alt1
- new version 1.3.2

* Thu Nov 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Build new version.

* Sat Oct 12 2019 Grigory Ustinov <grenka@altlinux.org> 1.2.5-alt1
- Build new version.

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
