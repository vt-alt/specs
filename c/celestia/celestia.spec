Name: celestia
Version: 1.6.2.2
Release: alt1
Epoch: 1

Summary: A real-time visual space simulation

License: GPL-2.0
Group: Education
Url: https://celestia.space

Provides: celestia-ui = %EVR
Provides: celestia-qt = %EVR celestia-gtk = %EVR celestia-glut = %EVR
Obsoletes: celestia-qt < %EVR celestia-gtk < %EVR celestia-glut < %EVR

# Source-url: https://github.com/CelestiaProject/Celestia/archive/master.zip
Source: %name-%version.tar

Patch1: celestia-1.4.0-desktop-fix.patch
Patch2: celestia-1.6.1-alt-gcc4.6.patch
Patch3: celestia-1.6.1-alt-DSO.patch
Patch4: celestia-1.6.1-alt-libpng15.patch
Patch5: celestia-1.6.1-alt-glibc-2.16.patch
Patch6: celestia-1.6.1-alt-fix-build.patch
Patch7: celestia-1.6.1-alt-fix-subdir-build.patch
Patch8: celestia-1.6.1-alt-lua5.2.patch
Patch9: celestia-1.6.1-alt-fix-build-2.patch

BuildRequires: cmake gcc-c++ libstdc++-devel
BuildRequires: libGLEW-devel libXi-devel libXmu-devel libfreeglut-devel

BuildRequires: eigen3

BuildRequires: libjpeg-devel libpng-devel libtheora-devel
BuildRequires: zlib-devel liblua5-devel libssl-devel
BuildRequires: libfmt-devel

BuildRequires: libgtk+2-devel libgtkglext-devel

%description
Celestia is a free real-time space simulation that
lets you experienceour universe in three dimensions.
Unlike most planetarium software, Celestia does not
confine you to the surface of the Earth. You can
travelthroughout the solar system, to any of over
100,000 stars, or even beyondthe galaxy.

%package common
Group: Education
Summary: A real-time visual space simulation (common part)
#Requires: celestia-ui = %EVR
%description common
This is a common part of Celestia

Celestia is a free real-time space simulation that
lets you experienceour universe in three dimensions.
Unlike most planetarium software, Celestia does not
confine you to the surface of the Earth. You can
travelthroughout the solar system, to any of over
100,000 stars, or even beyondthe galaxy.

%package qt
Group: Education
Summary: A real-time visual space simulation (Qt5 frontend)
Requires: celestia-common = %EVR
Provides: celestia-ui = %version-%release
Provides: celestia = %version-%release
Obsoletes: celestia < %version-%release

%description qt
This is a Qt5 frontend to Celestia

Celestia is a free real-time space simulation that
lets you experienceour universe in three dimensions.
Unlike most planetarium software, Celestia does not
confine you to the surface of the Earth. You can
travelthroughout the solar system, to any of over
100,000 stars, or even beyondthe galaxy.

%package gtk
Group: Education
Summary: A real-time visual space simulation (GTK frontend)
Requires: celestia-common = %EVR
Provides: celestia-ui = %version-%release

%description gtk
This is a GTK frontend to Celestia

Celestia is a free real-time space simulation that
lets you experienceour universe in three dimensions.
Unlike most planetarium software, Celestia does not
confine you to the surface of the Earth. You can
travelthroughout the solar system, to any of over
100,000 stars, or even beyondthe galaxy.

%package glut
Group: Education
Summary: A real-time visual space simulation (GLUT frontend)
Requires: celestia-common = %EVR
Provides: celestia-ui = %version-%release

%description glut
This is a GLUT frontend to Celestia

Celestia is a free real-time space simulation that
lets you experienceour universe in three dimensions.
Unlike most planetarium software, Celestia does not
confine you to the surface of the Earth. You can
travelthroughout the solar system, to any of over
100,000 stars, or even beyondthe galaxy.

%prep
%setup
%autoreconf

%build
# drop some warnings from build log
%add_optflags -Wno-int-in-bool-context
%configure \
    --with-gnu-ld \
    --without-arts \
    --with-lua \
    --with-glut \
    --with-gtk \
    #
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_desktopdir
install src/celestia/kde/data/%name.desktop %buildroot%_desktopdir/
install -D -m 644 src/celestia/gtk/data/%name.png %buildroot%_liconsdir/%name.png
install -D -m 644 src/celestia/gtk/data/%name.svg %buildroot%_iconsdir/hicolor/scalable/%name.svg

install -d %buildroot/etc/alternatives/packages.d
cat >%buildroot/etc/alternatives/packages.d/%name-qt <<__EOF__
%_bindir/celestia      %_bindir/celestia-qt 20
__EOF__

cat >%buildroot/etc/alternatives/packages.d/%name-gtk <<__EOF__
%_bindir/celestia      %_bindir/celestia-gtk 10
__EOF__

cat >%buildroot/etc/alternatives/packages.d/%name-glut <<__EOF__
%_bindir/celestia      %_bindir/celestia-glut 30
__EOF__

%find_lang %name

rm -fv %buildroot%_libdir/libcelmodel.a

%pre
[ ! -d %_datadir/apps/%name ] || rm -fr %_datadir/apps/%name

%files -f %name.lang common
#_datadir/apps/*
#_datadir/applnk/*
#_datadir/config/*
##%_bindir/makestardb
##%_bindir/makexindex
##%_bindir/startextdump
%_datadir/locale/*/*/celestia_constellations.mo
#_datadir/mimelnk/*
#_datadir/services/*
%_datadir/%name/
%_liconsdir/%name.png
%_iconsdir/hicolor/scalable/%name.svg
%_desktopdir/%name.desktop
%doc ChangeLog TRANSLATORS README NEWS

%files
%_bindir/celestia

#%files gtk
#%_bindir/celestia-gtk
#/etc/alternatives/packages.d/%name-gtk

#%files glut
#%_bindir/celestia-glut
#/etc/alternatives/packages.d/%name-glut

#%files qt
#%_bindir/celestia-qt
#/etc/alternatives/packages.d/%name-qt

%changelog
* Thu Feb 25 2021 Sergey V Turchin <zerg@altlinux.org> 1:1.6.2.2-alt1
- new version

* Sat Feb 02 2019 Michael Shigorin <mike@altlinux.org> 1.6.9.git-alt2
- build with system libfmt

* Sat Dec 08 2018 Vitaly Lipatov <lav@altlinux.ru> 1.6.9.git-alt1
- new version (1.6.9.git) with rpmgs script
- cleanup spec, build gtk, glut, qt builds

* Wed Aug 29 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.6.1-alt6
- build without ancient libgnome-ui

* Fri Nov 17 2017 Oleg Solovyov <mcpain@altlinux.org> 1.6.1-alt5
- fix build

* Mon Jan 09 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.6.1-alt4.qa1
- Fixed build with lua5.3.

* Thu Nov 05 2015 Michael Shigorin <mike@altlinux.org> 1.6.1-alt4
- Rebuilt against gcc5-built qt3.

* Fri Dec 26 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.6.1-alt3
- Recovered celestia package for Sisyphus.
- Fixed build.

* Thu Mar 28 2013 Andrey Cherepanov <cas@altlinux.org> 1.6.1-alt2.4
- Fix build with new xorg version

* Tue Nov 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt2.3
- Fixed build with glibc 2.16

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt2.2
- Rebuilt with libpng15

* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt2.1
- Fixed build

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 1.6.1-alt2
- Build for TDE 3.5.13 release

* Wed Jun 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Fri Apr 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt6.1
- build fixd

* Mon Mar 14 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt6
- build fixed

* Fri Nov 19 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt5
- build fixed

* Sat Feb 06 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.6.0-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for celestia
  * postclean-05-filetriggers for spec file

* Tue Aug 18 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt4
- encoding bug fixed

* Wed Aug 12 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt3
- Theora support added
- two subpackages for gnome and kde interfaces

* Mon Aug 10 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt2
- russian in bookmarks fixed

* Mon Jul 27 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt1
- release 1.6.0

* Tue Jun 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.5.1-alt1.1
- rebuild with libpng.git=1.2.37-alt2

* Mon Jun 08 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.5.1-alt1
- release 1.5.1

* Fri Feb 22 2008 Eugine V. Kosenko <maverik@altlinux.ru> 1.5.0-alt2
- add i18n to new release

* Wed Feb 20 2008 Eugine V. Kosenko <maverik@altlinux.ru> 1.5.0-alt1
- release 1.5.0

* Fri Oct 19 2007 Eugene V. Horohorin <genix@altlinux.ru> 1.4.1-alt5
- fix requirement

* Thu Oct 18 2007 Eugene V. Horohorin <genix@altlinux.ru> 1.4.1-alt4
- added requirement to GConf2

* Mon Apr 09 2007 Eugine V. Kosenko <maverik@altlinux.ru> 1.4.1-alt3.i18n
- add trial i18n (fonts and fixes)

* Mon May 15 2006 Eugene V. Horohorin <genix@altlinux.ru> 1.4.1-alt2
- fix compile woth gcc4.1 (patch from fedoraproject.org)

* Sat Mar 25 2006 Eugene V. Horohorin <genix@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Sun Mar 12 2006 Eugene V. Horohorin <genix@altlinux.ru> 1.4.0-alt2
- fixed build with LDFLAGS="-Wl,--as-needed"
- removed .la->.so replacement
- fixed update from previous versions (thanks to shrek@)

* Sat Feb 18 2006 Eugene V. Horohorin <genix@altlinux.ru> 1.4.0-alt1
- new version (1.4.0)
- rebuild with new xorg (#8813)
- menu-file replaced with celestia.desktop
- installation fix (/usr/share/apps/celestia -> /usr/share/celestia)

* Tue Jan 18 2005 Eugene V. Horohorin <genix@altlinux.ru> 1.3.2-alt2
- this build make more gcc3.4 compatible

* Wed Sep 22 2004 Eugene V. Horohorin <genix@altlinux.org> 1.3.2-alt1
- new version

* Wed Jun 23 2004 Eugene V. Horohorin <genix@altlinux.ru> 1.3.1-alt2
- spec clean up

* Sat May 08 2004 Eugene V. Horohorin <genix@altlinux.ru> 1.3.1-alt1
- First build.

