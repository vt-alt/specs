Name: rocksndiamonds
Version: 4.1.3.0
Release: alt1

Summary: A boulderdash like game
License: GPL
Group: Games/Arcade

Url: http://www.artsoft.org/rocksndiamonds
Source: %name-%version.tar.gz
Source1: %name.desktop
Source2: %name.1
Source10: %name.16.png
Source11: %name.32.png
Source12: %name.48.png

Requires: %name-data = %version-%release

# Automatically added by buildreq on Tue Sep 09 2008 (-bi)
BuildRequires: libSDL2-devel libSDL2_image-devel libSDL2_mixer-devel libSDL2_net-devel
BuildRequires: zlib-devel libsmpeg-devel

%description
Arcade style game for Unix, DOS and Windows.

A game like "Boulderdash" (C64) or "Emerald Mine" (Amiga).
Included are many levels known from the games "Boulderdash",
"Emerald Mine", "Sokoban", "Supaplex" and "DX-Boulderdash",
level elements for "Diamond Caves II" style games
and a lot of new levels designed by other players.

Some features:
 - joystick support for Linux, FreeBSD and DOS/Windows
 - local multiplayer support for all supported platforms
 - network multiplayer support for Unix platform
 - soft scrolling with 50 frames/s
 - stereo sound effects and music
 - music module support for SDL version (Unix/Win32)
 - fullscreen support for SDL version (Unix/Win32)
 - lots of additional levels available (over 10.000)
 - complete source code included under GNU GPL

%package data
Summary: Rocks'N'Diamonds levels
License: GPL
Group: Games/Arcade
BuildArch: noarch

%description data
This package contains levels for Rocks'N'Diamonds

%prep
%setup

%build
%define _pkgdatadir %_gamesdatadir/%name
%make_build sdl2 OPTIONS="%optflags" X11_PATH="%_x11dir" RO_GAME_DIR="%_pkgdatadir"

%install
install -pD -m755 %name %buildroot%_gamesbindir/%name
test -r "%name.1" && \
install -pD -m644 %name.1 %buildroot%_mandir/man1/%name.1 || \
install -pD -m644 %SOURCE2 %buildroot%_mandir/man1/%name.1
install -pD -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot%_pkgdatadir
cp -a docs graphics levels sounds music  %buildroot%_pkgdatadir

install -m644 %SOURCE10 -D %buildroot/%_miconsdir/%name.png
install -m644 %SOURCE11 -D %buildroot/%_niconsdir/%name.png
install -m644 %SOURCE12 -D %buildroot/%_liconsdir/%name.png

%files
%_gamesbindir/*
%_desktopdir/%name.desktop
%_iconsdir/*/*/*/*.png
%doc ChangeLog
%_man1dir/*

%files data
%_pkgdatadir

%changelog
* Fri May 24 2019 Grigory Ustinov <grenka@altlinux.org> 4.1.3.0-alt1
- Build new version.

* Tue Mar 05 2019 Grigory Ustinov <grenka@altlinux.org> 4.1.2.0-alt1
- Build new version.

* Thu Jan 24 2019 Grigory Ustinov <grenka@altlinux.org> 4.1.1.0-alt1
- Build new version.

* Thu Mar 22 2018 Fr. Br. George <george@altlinux.ru> 4.0.1.4-alt1
- Autobuild version bump to 4.0.1.4

* Wed Sep 20 2017 Fr. Br. George <george@altlinux.ru> 4.0.0.2-alt1
- Autobuild version bump to 4.0.0.2
- Introduce editor help

* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 3.3.1.2-alt1
- Autobuild version bump to 3.3.1.2

* Sun Oct 27 2013 Fr. Br. George <george@altlinux.ru> 3.3.1.0-alt1
- Autobuild version bump to 3.3.1.0

* Sun Mar 13 2011 Fr. Br. George <george@altlinux.ru> 3.3.0.1-alt1
- Autobuild version bump to 3.3.0.1

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 3.2.4-alt3
- introduced noarch data subpackage

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 3.2.4-alt2
- applied repocop patch

* Tue Sep 09 2008 Michael Shigorin <mike@altlinux.org> 3.2.4-alt1
- 3.2.4 (traditional, not jue)
- fixed build (buildreq)
- replaced Debian menu file with original desktop one
- spec cleanup
- me as a Packager:

* Fri Jan 26 2007 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt1
- new version
- remove binary from tarball

* Mon Jul 17 2006 Sergey V Turchin <zerg at altlinux dot org> 3.2.0-alt1
- new version
- remove binary from tarball

* Tue Oct 11 2005 Sergey V Turchin <zerg at altlinux dot org> 3.1.1-alt1
- new version

* Wed May 05 2004 Sergey V Turchin <zerg at altlinux dot org> 3.0.8-alt1
- new version

* Wed Sep 03 2003 Sergey V Turchin <zerg at altlinux dot org> 3.0.2-alt1
- new version

* Fri Oct 25 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.1-alt1
- new version

* Tue Aug 06 2002 Sergey V Turchin <zerg@altlinux.ru> 2.0.1-alt1
- new version

* Sat May 18 2002 Sergey V Turchin <zerg@altlinux.ru> 2.0.0-alt5
- rebuild with new alsa

* Fri Aug 17 2001 Rider <rider@altlinux.ru> 2.0.0-alt4
- rebuid

* Sat Jun 09 2001 Sergey V Turchin <zerg@altlinux.ru> 2.0.0-alt3
- 2.0.0
- build with SDL

* Sun Jan 14 2001 Dmitry V. Levin <ldv@fandra.org> 1.4.0-ipl5mdk
- RE adaptions.

* Thu Oct 26 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.4.0-4mdk
- fix compile with gcc-2.96

* Wed Aug 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.4.0-3mdk
- automatically added packager tag

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.4.0-2mdk
- automatically added BuildRequires

* Wed Aug  2 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.4.0-1mdk
- first package for Linux-Mandrake
