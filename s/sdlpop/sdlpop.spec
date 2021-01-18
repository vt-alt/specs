#
# spec file for package sdlpop
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name: sdlpop
Version: 1.21
Release: alt1

Summary: An open-source port of Prince of Persia
License: GPLv3
Group: Games/Arcade

Url: http://www.popot.org/get_the_games.php?game=SDLPoP
Source: https://github.com/NagyD/SDLPoP/archive/v%version.tar.gz#/%name-%version.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig
BuildRequires: pkgconfig(SDL2_image)
BuildRequires: pkgconfig(SDL2_mixer)
BuildRequires: pkgconfig(sdl2)

%description
SDLPoP is an open-source port of Prince of Persia 1,
that runs natively under Linux. It is based on the DOS
version of the game, and uses SDL.

Run the prince executable in a path were the original
game data files are located.

%prep
%setup -n SDLPoP-%version
sed -i 's/\r$//' doc/*.txt

%build
cd src
%cmake
%make_build
sed -e 's,\$ROOT,%_libexecdir/%name,g' \
    -e 's,SDLPoP,Prince of Persia,' \
    < SDLPoP.desktop.template > SDLPoP.desktop

%install
install -d %buildroot%_bindir
install -Dm0755 prince %buildroot%_libexecdir/%name/%name
install -pDm644 src/SDLPoP.desktop %buildroot%_desktopdir/%name.desktop
install -Dm0644 data/icon.png \
	%buildroot%_datadir/icons/hicolor/32x32/apps/%name.png
install -d %buildroot%_libexecdir/%name
mv data/ %buildroot%_libexecdir/%name

# Install Wrapper
cat > %buildroot%_bindir/%name << EOF
#!/bin/sh
exec "%_libexecdir/%name/\${0##*/}" \$@
EOF

%files
%doc doc/Readme.txt doc/ChangeLog.txt doc/bugs.txt
%doc doc/gpl-3.0.txt
%attr(0755,root,root) %_bindir/sdlpop
%_libexecdir/%name
%_datadir/icons/hicolor/32x32/apps/sdlpop.png
%_datadir/applications/sdlpop.desktop

%changelog
* Sat Jan 16 2021 Michael Shigorin <mike@altlinux.org> 1.21-alt1
- built for ALT (thanks openSUSE)

* Sat Aug 22 2020 Martin Hauke <mardnh@gmx.de>
- Update to version 1.21
  Fixed:
  * Skeletons not on level 3 did not behave like skeletons.
  * Don't crash if the intro music is interrupted by Tab in PC
    Speaker mode.
  * Don't switch to PC Speaker mode if there is a mod name in the
    replay file.
  * Don't draw the right edge of loose floors on the left side of a
    potion or sword.
  * A guard standing on a door top (with floor) should not become
    inactive.
  * Left jump (top-left) didn't work on some gamepads.
  * Replaying from the command line did not work if there were no
    replay files in the replay folder.
  Done:
  * Detect guard skill customizations in PRINCE.EXE. (Used in
    Illusions of Persia, for example.)
  * Added support for gamecontrollerdb.txt file.
  * Detect changes of the shadow's starting positions and
    automatic moves in PRINCE.EXE.
  * Added "Restart Game" to the pause menu, so now it's possible
    to restart the game using a controller.
  * Added fast forward.
  Added:
  * You can now use quicksave and quickload while recording a
    replay.
- Drop patch:
  * 184.patch (fixed by upstream)
* Wed Oct 23 2019 Martin Hauke <mardnh@gmx.de>
- Do not longer use rpm macros that are not longer needed on
  recent distros:
  * %%desktop_database_post
  * %%icon_theme_cache_post
* Tue Oct 15 2019 Martin Hauke <mardnh@gmx.de>
- Update to version 1.20
  * Fixed crash on Linux when the prince fell out of the level
    while a guard was active.
  * FIXED: With start_in_blind_mode enabled, moving objects were
    not displayed until blind mode was toggled off+on.
  * Fix upside-down screen when using PRINCE.EXE from v1.3 or v1.4.
  * Added customization option for loose floor delay. (Used in
    Neon Persia.)
  * Fix detection of "allow triggering any tile" hack.
  * Enable use_custom_options by default in the INI.
  * Fix priorities of sword and spike sounds. (As in PoP 1.3.)
    The "spiked" sound didn't interrupt the normal spikes sound when
    the prince ran into spikes. With PoP 1.3 sounds, the "guard hurt"
    sound didn't play when you hit a guard directly after parrying.
- Add patch:
  * 184.patch (CMake: Don't link SDL2main on Linux)
    https://github.com/NagyD/SDLPoP/pull/184/files
* Sun Mar 31 2019 Martin Hauke <mardnh@gmx.de>
- Update to version 1.19
  * Fix looping "sword moving" sound if the player leaves a room
    exactly when a guard attacks.
  * Support 8-bpp images in DAT files. For example the Pyramid mod
    contains some of these.
  * Improved map-making on levels with broken room links: If a room
    is mapped to an already used place, then put it to the bottom of
    the map.
  * Better support for high-DPI (Retina) displays.
  * Disable integer scaling menu item if SDL version is too old.
  * Made the exit door fix configurable.
  * Torches appearing in the leftmost column are now animated. (They
    are actually in the rightmost column of the left-side room.)
  New Features:
  * Load custom options from DOS PRINCE.EXE files.
  * Added a hotkey to display SDL versions. (Ctrl-C)
  * Save screenshots and maps into a separate folder and add numbers
    to the filenames.
  * Added support for PC speaker sounds. Use command-line parameter
    "stdsnd".
  * Added support for colored torch flames.
* Sun Jun 10 2018 mardnh@gmx.de
- Use CMake for building
- Package data files
- Update to version 1.18.1
* Sat Jul 15 2017 mailaender@opensuse.org
- update to version 1.17
- add .desktop file with icon
* Sat May 21 2016 mailaender@opensuse.org
- use source tarballs https://github.com/NagyD/SDLPoP/issues/62
* Sat Mar 26 2016 mailaender@opensuse.org
- initial packaging of version 1.16
