Name:       hedgewars
Version:    0.9.25
Release:    alt2.1

Summary:    Game with heavily armed fighting hedgehogs
Summary(ru_RU.UTF-8): Игра в битвы тяжело-вооружённых воющих ёжиков

License:    GPLv2
Group:      Games/Strategy
URL:        http://www.hedgewars.org/

Packager:   Grigory Ustinov <grenka@altlinux.org>

Source:     %name-%version.tar
Patch:      fix_non_inline_ShiftWorld.patch
Patch1:     alt-qt5.15.patch

Requires:   %name-data = %EVR
Requires:   fonts-ttf-wqy-zenhei fonts-ttf-dejavu

BuildRequires: cmake fpc-units-gtk2 fpc-units-misc fpc-units-net
BuildRequires: libSDL2_image-devel libSDL2_mixer-devel libSDL2_net-devel libSDL2_ttf-devel
BuildRequires: libavformat-devel libffi-devel libfreeglut-devel libgmp-devel
BuildRequires: liblua5.1-compat-devel libphysfs-devel phonon-devel qt5-tools-devel
BuildRequires: desktop-file-utils chrpath libswresample-devel
BuildRequires: clang ghc7.6.1 libGLEW-devel ghc7.6.1-transformers ghc7.6.1-parsec

ExclusiveArch: x86_64 %ix86

%description
Each player controls a team of several hedgehogs. During the course of the
game, players take turns with one of their hedgehogs. They then use whatever
tools and weapons are available to attack and kill the opponents' hedgehogs,
thereby winning the game. Hedgehogs may move around the terrain in a variety
of ways, normally by walking and jumping but also by using particular tools
such as the "Rope" or "Parachute", to move to otherwise inaccessible areas.

Each turn is time-limited to ensure that players do not hold up the game
with excessive thinking or moving.
A large variety of tools and weapons are available for players during the
game: Grenade, Cluster Bomb, Bazooka, UFO, Shotgun, Desert Eagle, Minigun,
Baseball Bat, Dynamite, Mine, Rope, Pneumatic pick, Parachute, etc. Most weapons,
when used, cause explosions that deform the terrain, removing circular chunks.

The landscape is an island floating on a body of water, or a restricted cave
with water at the bottom. A hedgehog dies when it enters the water (either
by falling off the island, or through a hole in the bottom of it), it is
thrown off either side of the arena or when its health is reduced,
typically from contact with explosions, to zero (the damage dealt to the
attacked hedgehog or hedgehogs after a player's or CPU turn is shown only
when all movement on the battlefield has ceased).

%description -l ru_RU.UTF-8
Каждый игрок управляет командой из нескольких ёжиков. По ходу игры игроки делают
ходы одним из своих ёжиков. Они могут использовать всевозможные доступные
приспособления и оружие, чтобы атаковать и убивать ёжиков противника и таким
образом получить победу в игре. Ёжики могут передвигаться по локации множеством
способов, обычно с помощью ходьбы или прыжков, однако могут и использовать
различные приспособления, такие как верёвка или парашют, чтобы попасть в
труднодостижимые зоны.

Каждый ход ограничен по времени, чтобы гарантировать, что игроки не будут
задерживать игру излишними раздумьями или долгими передвижениями.
Во время игры игрокам доступен огромный ассортимент оружия и приспособлений:
гранаты, разрывные бомбы, базука, летающая тарелка, дробовик, пистолет,
пулемёт, бейсбольная бита, динамит, мина, верёвка, отбойный молоток, парашют,
всего не перечислить. Множество оружия при использовании вызывают взрывы,
которые разрушают локацию, выдирая из неё целые куски.

Локация представляет собой остров в воде или пещеру с водой внизу. Ёжик умрёт,
либо если зайдёт в воду или упадёт в неё с острова, либо если его здоровье
снизится до нуля от взрывов.

%package data
Summary: Resources for %name game
Summary(ru_RU.UTF-8): Файлы ресурсов для игры %name
Group:   Games/Strategy
BuildArch: noarch

%description data
This package contains all the data files for %name.
%description data -l ru_RU.UTF-8
Этот пакет содержит все файлы данных для игры %name.

%prep
%setup
%patch -p2
%patch1 -p1

# Make sure that we don't use bundled libraries
rm -r misc/liblua

%build
%remove_optflags -frecord-gcc-switches
%cmake_insource -DNOSERVER=1 -DPHYSFS_SYSTEM=1 \
-DDATA_INSTALL_DIR=%_datadir/%name -Dtarget_library_install_dir="%_libdir" \
-DFONTS_DIRS="/usr/share/fonts/ttf/wqy-zenhei;/usr/share/fonts/ttf/dejavu"
%make_build VERBOSE=true

%install
%makeinstall_std

# below is the desktop file and icon stuff.
mkdir -p %buildroot%_datadir/applications
desktop-file-install \
  --dir %buildroot%_datadir/applications \
  %buildroot%_datadir/hedgewars/Data/misc/hedgewars.desktop
mkdir -p %buildroot%_datadir/icons/hicolor/32x32/apps
install -p -m 644 misc/hedgewars_ico.png \
  %buildroot%_datadir/icons/hicolor/32x32/apps/hedgewars.png
mkdir -p %buildroot%_datadir/icons/hicolor/512x512/apps
install -p -m 644 misc/hedgewars.png \
  %buildroot%_datadir/icons/hicolor/512x512/apps/%name.png

# fix verify-elf's RPATH error
chrpath --delete %buildroot%_bindir/hwengine

%files
%doc README ChangeLog.txt CREDITS
%_bindir/*
%_libdir/*.so.*
%ifarch x86_64
%_libdir/libavwrapper.so
%endif
%_libdir/libphyslayer.so
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/32x32/apps/%name.png
%_datadir/icons/hicolor/512x512/apps/%name.png
%_datadir/appdata/%name.appdata.xml
%_pixmapsdir/%name.xpm

%files data
%_datadir/%name

%changelog
* Fri Sep 04 2020 Sergey V Turchin <zerg at altlinux dot org> 0.9.25-alt2.1
- Fix compile with Qt-5.15

* Mon Apr 15 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.25-alt2
- Reloaded upstream tarball (after several fixes they uploaded new one on
  previous place)
- Fixed building on %%ix86 (but without video recording).
- Fixed FTBFS (Closes: #36222).

* Wed Dec 12 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.25-alt1
- Built new version (only for 64bit arch), because in this version
  upstream made hard dependency on ghc modules for 32bit arch.

* Tue Nov 06 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.24.1-alt1
- Finally, built new version (Closes: #34082).
- Removed all previous patches.
- Transfered on qt5.
- Built without server support, because there are no needed ghc modules.
- Massive cleanup spec.

* Mon Jun 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.22-alt4
- Rebuilt with ffmpeg-4.

* Tue Jun 06 2017 Denis G. Samsonenko <ogion@altlinux.org> 0.9.22-alt3
- rebuild with ffmpeg
- %name-ffmpeg3.patch

* Thu Jan 05 2017 Denis G. Samsonenko <ogion@altlinux.org> 0.9.22-alt2
- fix some repocop warnings

* Tue Jan 03 2017 Denis G. Samsonenko <ogion@altlinux.org> 0.9.22-alt1
- new version

* Sun May 24 2015 Denis G. Samsonenko <ogion@altlinux.org> 0.9.21.1-alt1
- new version
- %name-no-bytestring.patch updated

* Wed Apr 23 2014 Denis G. Samsonenko <ogion@altlinux.org> 0.9.20.5-alt1
- new version
- %name-compiler-opts.patch removed

* Sat Jul 20 2013 Denis G. Samsonenko <ogion@altlinux.org> 0.9.19.3-alt2
- %name-data subpackage
- font copies replaced with symlinks to system versions (#25350)
- icon added to desktop file (#22690)
- man file packaged

* Sat Jul 20 2013 Denis G. Samsonenko <ogion@altlinux.org> 0.9.19.3-alt1
- new version
- %name-no-bytestring.patch adapted from Fedora package
- %name-compiler-opts.patch

* Sun Nov 20 2011 Anton Farygin <rider@altlinux.ru> 0.9.17-alt1
- new version

* Sun Sep 18 2011 Anton Farygin <rider@altlinux.ru> 0.9.16-alt1
- new version

* Sat Feb 12 2011 Anton Farygin <rider@altlinux.ru> 0.9.15-alt1
- new version

* Wed Sep 29 2010 Anton Farygin <rider@altlinux.ru> 0.9.13-alt2
- rebuild in new environment

* Sun Apr 04 2010 Anton Farygin <rider@altlinux.ru> 0.9.13-alt1
- new version

* Wed Mar 10 2010 Anton Farygin <rider@altlinux.ru> 0.9.12-alt2
- fixed build with new fpc-2.4.0

* Sun Nov 15 2009 Anton Farygin <rider@altlinux.ru> 0.9.12-alt1
- new version

* Mon May 25 2009 Anton Farygin <rider@altlinux.ru> 0.9.11-alt1
- new version

* Tue Apr 14 2009 Anton Farygin <rider@altlinux.ru> 0.9.10-alt1
- new version

* Sun Mar 15 2009 Anton Farygin <rider@altlinux.ru> 0.9.9-alt2
- build hedgewars-server too

* Mon Jan 26 2009 Ilya Mashkin <oddity@altlinux.ru> 0.9.9-alt1
- 0.9.9

* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 0.9.8-alt1.1
- Fix summary

* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Mon Nov 03 2008 Ilya Mashkin <oddity@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Mon Oct 06 2008 Ilya Mashkin <oddity@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Sun Jun 22 2008 Igor Zubkov <icesik@altlinux.org> 0.9.4-alt1
- build for Sisyphus
