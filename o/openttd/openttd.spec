%define daterev 20200413
%define gitsnapshot 7f77b8c1e27f3d102b1f665d2a3c500598245c3b

Name: openttd
Version: 1.10.1
Release: alt1

Summary: An open source clone of the Microprose game "Transport Tycoon Deluxe".
License: GPLv2
Group: Games/Strategy
URL: https://www.openttd.org/
Requires: TiMidity++
Requires: fonts-ttf-dejavu
Requires: %name-data = %EVR
Requires: openttd-3rd-party >= 0.6.0

Source: %name-%version.tar
Source1: %name.watch

Patch0: %name-%version-alt.patch

BuildRequires: libSDL2-devel libpng-devel libfreetype-devel fontconfig-devel gcc-c++ liblzo2-devel liblzma-devel libxdg-basedir-devel libfluidsynth-devel

%description
An open source clone of the Microprose game "Transport Tycoon Deluxe".

%package data
Buildarch: noarch
Summary: Data files for %name
Requires: %name
Group: Games/Strategy
Requires: %name-3rd-party

%description data
Data files for %name

%prep
%setup
%patch0 -p1

%build
echo "%version	%daterev	0	%gitsnapshot	1	1" >.ottdrev

./configure \
    --prefix-dir=%_prefix \
    --with-sdl \
    --with-png \
    --with-freetype \
    --with-fontconfig \
#
    
%make_build WITH_SDL=1 UNIX=1 RELEASE=%version INSTALL=1 WITH_NETWORK=1 ISTAG=1 ISSTABLETAG=1 \
    USE_HOMEDIR=1 VERBOSE=1 PERSONAL_DIR=.%name \
    PREFIX=%_prefix DATA_DIR=share/games/%name \
	
%install
mkdir -p %buildroot%_prefix/games
mkdir -p %buildroot%_datadir/games/%name/gm
mkdir -p %buildroot%_datadir/games/%name/lang
mkdir -p %buildroot%_datadir/games/%name/ai
mkdir -p %buildroot%_man6dir

install -m755 -s bin/%name %buildroot%_prefix/games/%name
cp -a bin/baseset %buildroot%_datadir/games/%name
cp -a bin/ai/*.nut %buildroot%_datadir/games/%name/ai/
cp -a bin/lang/*.lng %buildroot%_datadir/games/%name/lang
chmod -x %buildroot%_datadir/games/%name/baseset/*

#menu

install -dm 755 %buildroot%_datadir/applications
install -m644 media/%name.desktop %buildroot%_datadir/applications/%name.desktop

# icons
install -pD -m644 media/%name.16.png %buildroot%_miconsdir/%name.png
install -pD -m644 media/%name.32.png %buildroot%_niconsdir/%name.png
install -pD -m644 media/%name.48.png %buildroot%_liconsdir/%name.png
install -pD -m644 docs/%name.6 %buildroot%_man6dir/


%files
%_prefix/games/%name

%files data
%doc docs/* bin/scripts README.md known-bugs.txt changelog.txt COPYING.md
%_datadir/games/%name
%_datadir/applications/%name.desktop
%_niconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png
%_man6dir/*

%changelog
* Thu Apr 16 2020 Anton Farygin <rider@altlinux.ru> 1.10.1-alt1
- 1.10.1

* Mon Apr 06 2020 Anton Farygin <rider@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Sat Sep 21 2019 Anton Farygin <rider@altlinux.ru> 1.9.3-alt1
- 1.9.3

* Tue Aug 06 2019 Anton Farygin <rider@altlinux.ru> 1.9.2-alt1
- 1.9.2

* Wed Apr 10 2019 Anton Farygin <rider@altlinux.ru> 1.9.1-alt1
- 1.9.1

* Wed Apr 03 2019 Anton Farygin <rider@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Wed Mar 20 2019 Anton Farygin <rider@altlinux.ru> 1.8.0-alt3
- rebuilt with libicu 6.3.1-alt1

* Mon Sep 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.0-alt2
- NMU: fixed build with new ICU.

* Mon Apr 09 2018 Anton Farygin <rider@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Sun Jun 18 2017 Anton Farygin <rider@altlinux.ru> 1.7.1-alt1
- new version

* Fri May 05 2017 Anton Farygin <rider@altlinux.ru> 1.7.0-alt1
- new version

* Mon Jul 04 2016 Anton Farygin <rider@altlinux.ru> 1.6.1-alt1
- new version

* Thu Jun 16 2016 Anton Farygin <rider@altlinux.ru> 1.6.0-alt1
- new version

* Fri Oct 30 2015 Anton Farygin <rider@altlinux.ru> 1.5.2-alt1
- new version

* Thu Jun 25 2015 Anton Farygin <rider@altlinux.ru> 1.5.1-alt1
- new version

* Tue Apr 07 2015 Anton Farygin <rider@altlinux.ru> 1.5.0-alt1
- new version

* Tue Nov 18 2014 Anton Farygin <rider@altlinux.ru> 1.4.4-alt1
- new version

* Wed Oct 15 2014 Anton Farygin <rider@altlinux.ru> 1.4.3-alt1
- new version

* Mon Sep 01 2014 Anton Farygin <rider@altlinux.ru> 1.4.2-alt1
- new version

* Tue Jun 24 2014 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1
- new version

* Thu Apr 10 2014 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1
- new version

* Tue Dec 17 2013 Anton Farygin <rider@altlinux.ru> 1.3.3-alt1
- new version

* Fri Aug 16 2013 Anton Farygin <rider@altlinux.ru> 1.3.2-alt1
- new version

* Tue Jun 25 2013 Anton Farygin <rider@altlinux.ru> 1.3.1-alt1
- new version

* Wed Sep 19 2012 Anton Farygin <rider@altlinux.ru> 1.2.2-alt1
- new version

* Mon Jul 30 2012 Anton Farygin <rider@altlinux.ru> 1.2.1-alt2
- added compat libs for AI
- removed openttd-installer (obsoleted by openttd-3rd-party)

* Fri Jul 20 2012 Anton Farygin <rider@altlinux.ru> 1.2.1-alt1
- new version

* Sun Sep 19 2010 Anton Farygin <rider@altlinux.ru> 1.0.4-alt1
- new version

* Tue Aug 31 2010 Anton Farygin <rider@altlinux.ru> 1.0.3-alt1
- new version (fixed CVE-2010-2534)

* Tue Jun 29 2010 Anton Farygin <rider@altlinux.ru> 1.0.2-alt1
- new version

* Thu Jun 17 2010 Anton Farygin <rider@altlinux.ru> 1.0.1-alt1
- new version

* Wed Jan 27 2010 Anton Farygin <rider@altlinux.ru> 0.7.5-alt1
- new version (CVE-2009-4007 fixed)

* Fri Oct 09 2009 Anton Farygin <rider@altlinux.ru> 0.7.3-alt1
- new version

* Wed Sep 02 2009 Anton Farygin <rider@altlinux.ru> 0.7.2-alt2
- use niconsdir instead of iconsdir
- fixed desktop file

* Tue Sep 01 2009 Anton Farygin <rider@altlinux.ru> 0.7.2-alt1
- new version

* Tue Jun 30 2009 Anton Farygin <rider@altlinux.ru> 0.7.1-alt1
- new version

* Sat Apr 11 2009 Anton Farygin <rider@altlinux.ru> 0.7.0-alt2
- 0.7.0

* Thu Mar 26 2009 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1.r15828
- 0.7.0-rc2

* Mon Mar 16 2009 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1.r15737
- 0.7.0-rc1

* Fri Mar 13 2009 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1.r15697
- updated snapshot (fixed some crash issues)

* Thu Mar 12 2009 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1.r15676
- new snapshot (0.7.0-beta2)

* Tue Mar 03 2009 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1.r15601
- new snapshot
- default fonts changed and warning about DejaVu removed

* Sat Feb 28 2009 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1.r15592
- new snapshot

* Thu Feb 26 2009 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1.r15587
- new snapshot (0.7.0-beta1)
- use official revision number (0.7.0-beta1) for playing over network

* Wed Feb 25 2009 Anton Farygin <rider@altlinux.ru> 0.6.3-alt3.r15578
- new snapshot
- squirrel included to maintree

* Fri Feb 20 2009 Anton Farygin <rider@altlinux.ru> 0.6.3-alt2.r15529
- new snapshot

* Mon Feb 16 2009 Anton Farygin <rider@altlinux.ru> 0.6.3-alt2.r15495
- fixed revision in game
- noarch content moved to %name-data subpackage

* Sat Feb 14 2009 Anton Farygin <rider@altlinux.ru> 0.6.3-alt1.svn15476
- new snapshot from svn
- added russian towns

* Fri Feb 13 2009 Anton Farygin <rider@altlinux.ru> 0.6.3-alt1.svn15465
- new snapshot from svn
- Xdialog added to requires

* Wed Feb 11 2009 Anton Farygin <rider@altlinux.ru> 0.6.3-alt1.svn15447
- new snapshot from svn
- added data downloader and installer
- menu file changed to desktop file

* Tue Feb 03 2009 Anton Farygin <rider@altlinux.ru> 0.6.3-alt1
- new version (from svn 15322)
- post-scripts removed 

* Fri Jun 06 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.6.1-alt1
- New release

* Wed Apr 02 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.6.0-alt1
- New release
- Fonts patch updated (and enabled AA)

* Wed Oct 03 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.5.3-alt1
- New release
- Fonts patch was reworked (fontconfig support seems to be fixed, so 
  hardcoded font paths were removed; uses font names now)
- Spec updates (to conform openttd's fs hier)

* Wed Apr 25 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.5.1-alt2
- New release

* Fri Mar 23 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.5.1-alt1.RC2
- Bugfix RC2
- Spec cleanups

* Thu Mar 01 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.5.0-alt2
- Release

* Sun Feb 04 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.5.0-alt1.svn8588
- New version from SVN
- Updated buildreqs
- Spec cleanups
- Correct man placement
- New patch (use correct, but hardcoded fonts)
- Added missed docs

* Fri Oct 06 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.4.8-alt1
- 0.4.8
- Updated buildreqs.

* Thu Jan 27 2005 Kachalov Anton <mouse@altlinux.ru> 0.3.6-alt1
- 0.3.6
  + some scenarios in docs/scenario
  + scripts example in docs/scripts

* Tue Dec 28 2004 Kachalov Anton <mouse@altlinux.ru> 0.3.5-alt1
- 0.3.5

* Wed Jun 09 2004 Kachalov Anton <mouse@altlinux.ru> 0.3.2.1-alt1
- first build for Sisyphus
