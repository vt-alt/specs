%define _name flare

Name: %_name-engine
Version: 1.11
Release: alt1

Summary: A simple game engine for single-player 2D action RPGs
License: %gpl3plus
Group: Games/Adventure

URL: http://flarerpg.org/
# https://github.com/flareteam/flare-engine.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses rpm-macros-cmake
BuildRequires: gcc-c++ cmake libSDL2-devel libSDL2_image-devel libSDL2_mixer-devel libSDL2_ttf-devel

%define _unpackaged_files_terminate_build 1

%description
Flare (Free Libre Action Roleplaying Engine) is a simple game engine
built to handle a very specific kind of game: single-player 2D action
RPGs. Flare is not a reimplementation of an existing game or engine.
It is a tribute to and exploration of the action RPG genre.
Rather than building a very abstract, robust game engine, the goal of
this project is to build several real games and harvest an engine from
the common, reusable code.

%prep
%setup
%patch -p1

%build
%cmake -DBINDIR=bin -DDATADIR=share/%_name
cd BUILD
%make_build VERBOSE=1
cd -

%install
cd BUILD
%makeinstall_std
cd -

%files
%_bindir/%_name
%_datadir/%_name/
%_desktopdir/%_name.desktop
%_iconsdir/hicolor/scalable/apps/%_name.svg
%_man6dir/*

%changelog
* Fri Aug 16 2019 Mikhail Efremov <sem@altlinux.org> 1.11-alt1
- Use gnu++11 flag.
- Use verbose output for make.
- Updated to 1.11.

* Tue May 21 2019 Mikhail Efremov <sem@altlinux.org> 1.10-alt1
- Updated to 1.10.

* Fri Dec 14 2018 Mikhail Efremov <sem@altlinux.org> 1.09.01-alt1
- Updated to 1.09.01.

* Mon Dec 10 2018 Mikhail Efremov <sem@altlinux.org> 1.09-alt1
- Updated to 1.09.

* Tue Sep 18 2018 Mikhail Efremov <sem@altlinux.org> 1.08-alt1
- Updated to 1.08.

* Wed Sep 05 2018 Mikhail Efremov <sem@altlinux.org> 1.07-alt1
- Updated to 1.07.

* Tue May 29 2018 Mikhail Efremov <sem@altlinux.org> 1.06-alt1
- Updated to 1.06.

* Thu May 03 2018 Mikhail Efremov <sem@altlinux.org> 1.05-alt1
- Updated to 1.05.

* Wed Apr 18 2018 Mikhail Efremov <sem@altlinux.org> 1.03-alt1
- Patches from upstream:
   - Fix crash when teleporting to map hero_pos with a summoned
     creature.
   - Fix regression where book text would be cut off when justify
     != left.
- Updated to 1.03.

* Wed Mar 14 2018 Mikhail Efremov <sem@altlinux.org> 1.0-alt1
- Updated URL.
- Patch from upstream:
    + Force minions to move away from blocked player when player
      is close.
- Updated to 1.0.

* Sat Aug 30 2014 Mikhail Efremov <sem@altlinux.org> 0.19-alt1
- Updated from upstream git.
- Updated to 0.19.

* Fri Nov 22 2013 Mikhail Efremov <sem@altlinux.org> 0.18-alt1
- Initial build.

