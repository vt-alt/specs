%def_with debug

Name: 	 qcad
Version: 3.24.3.7
Release: alt1
Summary: A professional CAD system
Summary(ru_RU.UTF-8): Профессиональная система CAD

Url: 	 http://www.ribbonsoft.com/qcad.html
# VCS:   https://github.com/qcad/qcad.git
# TODO: remove bundled fonts or specify their licenses  
License: GPL-3.0 with Qt-GPL-exception-1.0 and CC-BY-3.0 and GPL-2.0+ and MIT and BSD-2-Clause and ALT-Public-Domain
Group:   Graphics

Packager: Andrey Cherepanov <cas@altlinux.org>

Source0: qcad-%version.tar
Patch:   %name-%version-%release.patch
Patch1:  qcad-qt5-unbundle_libraries.patch
Patch2:  qcad-alt-use-system-zlib.patch

BuildRequires: gcc-c++ qt5-base-devel python
BuildRequires: desktop-file-utils
BuildRequires: libdbus-devel
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: libssl-devel
BuildRequires: qt5-designer
BuildRequires: qt5-imageformats
BuildRequires: qt5-script-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-tools-devel-static
BuildRequires: qt5-webengine-devel
BuildRequires: qt5-webkit-devel
BuildRequires: qt5-xmlpatterns-devel
BuildRequires: zlib-devel
BuildRequires: libquazip-qt5-devel
BuildRequires: spatialindex-devel

Requires: qt5-translations qt5-imageformats

%description
QCad is a professional CAD System. With QCad you can easily construct
and change drawings with ISO-text and many other features and save them
as DXF-files. These DXF-files are the interface to many CAD-systems such
as AutoCAD(TM) and many others.

%description -l ru_RU.UTF-8
QCad это профессиональная CAD система. С QCad вы можете легко создавать
и изменять рисунки с вставленным текстом и сохранять это в DXF файлы.
Через DXF файлы есть возможность обмениваться данными с другими CAD
системами (например, AutoCAD).

%prep
%setup -q
%patch -p1
%patch1 -p1
%patch2 -p1
rm -rf src/3rdparty/opennurbs/zlib
%if_with debug
echo 'DEFINES -= QT_NO_DEBUG_OUTPUT' >> shared.pri
%endif
%qmake_qt5
#lupdate-qt5 %name.pro

%define fallback_qt_version 5.12.3
if [ ! -e src/3rdparty/qt-labs-qtscriptgenerator-%_qt5_version ] ; then
    pushd src/3rdparty
    cp -ar qt-labs-qtscriptgenerator-%fallback_qt_version qt-labs-qtscriptgenerator-%_qt5_version
    mv qt-labs-qtscriptgenerator-%_qt5_version/qt-labs-qtscriptgenerator-%fallback_qt_version.pro qt-labs-qtscriptgenerator-%_qt5_version/qt-labs-qtscriptgenerator-%_qt5_version.pro
    popd
fi

%build
#export NPROCS=1
%make_build

%install
%installqt5
# Main executable
install -Dm755 release/qcad-bin %buildroot%_libdir/%name/qcad-bin

# Make executable wrapper
install -Dm0755 qcad %buildroot%_bindir/qcad

# Libraries
install -d %buildroot%_libdir
cp release/lib*.so %buildroot%_libdir

# Translations
install -d %buildroot%_libdir/%name/ts
cp ts/*.qm %buildroot%_libdir/%name/ts

# Documentation
install -Dm644 readme.txt %buildroot%_libdir/%name/readme.txt

echo other stuff
# Other stuff
cp -a   examples \
	fonts \
	libraries \
	linetypes \
	patterns \
	plugins \
	scripts \
	"%buildroot%_libdir/%name/"

# Desktop file
install -Dm644 qcad.desktop %buildroot%_desktopdir/%name.desktop

# Icon
install -Dm644 ./support/doc/api/qcad_icon.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png

# Add localization fo qcad.lang
for l in $(find %buildroot%_libdir/%name/qm -name \*.qm); do
	echo -n $l | sed 's,.*_\(.*\)\.qm,%%lang\(\1\) ,' >> %name.lang
	echo $l | sed "s,%buildroot,," >> %name.lang
done

%files
%doc gpl-3.0-exceptions.txt gpl-3.0.txt README.md LICENSE.txt
%_bindir/%name
%dir %_libdir/%name
%_libdir/lib*.so*
%_libdir/%name/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Thu May 28 2020 Andrey Cherepanov <cas@altlinux.org> 3.24.3.7-alt1
- New version.

* Sat May 23 2020 Andrey Cherepanov <cas@altlinux.org> 3.24.3.6-alt1
- New version.

* Sun Apr 26 2020 Andrey Cherepanov <cas@altlinux.org> 3.24.3.4-alt1
- New version.

* Fri Apr 17 2020 Andrey Cherepanov <cas@altlinux.org> 3.24.3.3-alt1
- New version.

* Wed Mar 18 2020 Andrey Cherepanov <cas@altlinux.org> 3.24.3.0-alt1
- New version.
- Build with system zlib (ALT #38141).

* Thu Feb 20 2020 Andrey Cherepanov <cas@altlinux.org> 3.24.2.6-alt1
- New version.

* Wed Feb 12 2020 Andrey Cherepanov <cas@altlinux.org> 3.24.2.4-alt1
- New version.

* Thu Feb 06 2020 Andrey Cherepanov <cas@altlinux.org> 3.24.2.3-alt1
- New version.

* Tue Jan 21 2020 Andrey Cherepanov <cas@altlinux.org> 3.24.2.1-alt1
- New version.

* Mon Jan 06 2020 Andrey Cherepanov <cas@altlinux.org> 3.24.1.0-alt1
- New version.

* Mon Dec 23 2019 Andrey Cherepanov <cas@altlinux.org> 3.24.0.1-alt1
- New version.

* Wed Dec 18 2019 Andrey Cherepanov <cas@altlinux.org> 3.24.0.0-alt1
- New version.

* Mon Dec 16 2019 Andrey Cherepanov <cas@altlinux.org> 3.23.0.11-alt1
- New version.
- Fix open file(s) with spaces (ALT #34893).
- Fix license tag.
- Use wrapper and desktop files directly, not as external sources.

* Thu Dec 12 2019 Andrey Cherepanov <cas@altlinux.org> 3.23.0.10-alt1
- New version.

* Mon Dec 02 2019 Andrey Cherepanov <cas@altlinux.org> 3.23.0.9-alt1
- New version.

* Sun Oct 27 2019 Andrey Cherepanov <cas@altlinux.org> 3.23.0.5-alt1
- New version.

* Mon Oct 07 2019 Andrey Cherepanov <cas@altlinux.org> 3.23.0.3-alt1
- New version.

* Tue Sep 10 2019 Andrey Cherepanov <cas@altlinux.org> 3.23.0.2-alt1
- New version.

* Fri Jul 19 2019 Andrey Cherepanov <cas@altlinux.org> 3.23.0.0-alt1
- New version.

* Mon Jul 15 2019 Andrey Cherepanov <cas@altlinux.org> 3.22.1.6-alt1
- New version.

* Wed Jul 10 2019 Andrey Cherepanov <cas@altlinux.org> 3.22.1.4-alt1
- New version.

* Sat Jun 29 2019 Andrey Cherepanov <cas@altlinux.org> 3.22.1.3-alt1
- New version.

* Thu Jun 13 2019 Andrey Cherepanov <cas@altlinux.org> 3.22.1.2-alt1
- New version.

* Tue May 21 2019 Andrey Cherepanov <cas@altlinux.org> 3.22.1.0-alt1
- New version.
- Set default UI language according to system locale (ALT #36764).

* Thu May 16 2019 Andrey Cherepanov <cas@altlinux.org> 3.22.0.12-alt1
- New version.

* Thu May 09 2019 Andrey Cherepanov <cas@altlinux.org> 3.22.0.11-alt1
- New version.

* Thu May 02 2019 Andrey Cherepanov <cas@altlinux.org> 3.22.0.10-alt1
- New version.

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 3.22.0.9-alt1
- New version.

* Sun Apr 14 2019 Andrey Cherepanov <cas@altlinux.org> 3.22.0.7-alt1
- New version.

* Thu Apr 04 2019 Andrey Cherepanov <cas@altlinux.org> 3.22.0.6-alt1
- New version.

* Wed Mar 27 2019 Andrey Cherepanov <cas@altlinux.org> 3.22.0.5-alt1
- New version.

* Sat Mar 23 2019 Andrey Cherepanov <cas@altlinux.org> 3.22.0.4-alt1
- New version.

* Tue Mar 19 2019 Andrey Cherepanov <cas@altlinux.org> 3.22.0.3-alt1
- New version.

* Sat Mar 09 2019 Andrey Cherepanov <cas@altlinux.org> 3.22.0.2-alt1
- New version.

* Thu Jan 17 2019 Andrey Cherepanov <cas@altlinux.org> 3.22.0.0-alt1
- New version.

* Tue Dec 18 2018 Andrey Cherepanov <cas@altlinux.org> 3.21.3.14-alt1
- New version.

* Fri Dec 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.21.3.12-alt1
- New version.

* Sun Dec 09 2018 Andrey Cherepanov <cas@altlinux.org> 3.21.3.11-alt1
- New version.

* Tue Nov 27 2018 Andrey Cherepanov <cas@altlinux.org> 3.21.3.10-alt1
- New version.

* Mon Nov 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.21.3.9-alt1
- New version.

* Mon Nov 19 2018 Andrey Cherepanov <cas@altlinux.org> 3.21.3.7-alt1
- New version.

* Tue Oct 16 2018 Andrey Cherepanov <cas@altlinux.org> 3.21.3.2-alt2
- Build with system libquazip-qt5 (ALT #35510). (thanks antohami@)
- Remove duplicate categories in desktop file. (thanks antohami@)

* Fri Oct 05 2018 Andrey Cherepanov <cas@altlinux.org> 3.21.3.2-alt1
- New version.

* Tue Sep 25 2018 Andrey Cherepanov <cas@altlinux.org> 3.21.3.1-alt1
- New version.

* Tue Sep 18 2018 Andrey Cherepanov <cas@altlinux.org> 3.21.3.0-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.21.2.9-alt1
- New version.

* Fri Aug 24 2018 Andrey Cherepanov <cas@altlinux.org> 3.21.2.6-alt1
- New version.

* Tue Aug 14 2018 Sergey V Turchin <zerg@altlinux.org> 3.21.2.3-alt2
- Rebuild with new Qt.

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.21.2.3-alt1
- New version.

* Tue Jul 10 2018 Andrey Cherepanov <cas@altlinux.org> 3.21.2.1-alt1
- New version.

* Sun Jul 01 2018 Andrey Cherepanov <cas@altlinux.org> 3.21.1.0-alt1
- New version.

* Tue Jun 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.21.0.0-alt1
- New version.

* Fri Jun 22 2018 Andrey Cherepanov <cas@altlinux.org> 3.20.2.0-alt1
- New version.

* Thu Jun 21 2018 Andrey Cherepanov <cas@altlinux.org> 3.20.1.7-alt1
- New version.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.20.1.6-alt1
- New version.

* Sun May 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.20.1.3-alt2
- Use Qt file dialogs for any unknown WM (KDE in some cases) (ALT #34805).

* Sat May 05 2018 Andrey Cherepanov <cas@altlinux.org> 3.20.1.3-alt1
- New version.
- Fix open file from command line (ALT #34807).

* Sat Apr 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.20.1.0-alt1
- New version.

* Thu Apr 12 2018 Andrey Cherepanov <cas@altlinux.org> 3.20.0.0-alt1
- New version.

* Tue Mar 20 2018 Andrey Cherepanov <cas@altlinux.org> 3.19.2.8-alt1
- New version.

* Thu Feb 01 2018 Andrey Cherepanov <cas@altlinux.org> 3.19.2.3-alt1
- New version.

* Tue Jan 09 2018 Andrey Cherepanov <cas@altlinux.org> 3.19.2.2-alt1
- New version.

* Thu Dec 21 2017 Andrey Cherepanov <cas@altlinux.org> 3.19.2.0-alt0.M80P.1
- Backport new version to p8 branch

* Wed Dec 20 2017 Andrey Cherepanov <cas@altlinux.org> 3.19.2.0-alt1
- New version.

* Wed Nov 29 2017 Anton Midyukov <antohami@altlinux.org> 3.19.1.0-alt1.M80P.1
- Backport new version to p8 branch

* Wed Nov 29 2017 Anton Midyukov <antohami@altlinux.org> 3.19.1.0-alt2
- Fix icon name in desktop file

* Mon Nov 13 2017 Andrey Cherepanov <cas@altlinux.org> 3.19.1.0-alt1
- New version

* Tue Nov 07 2017 Andrey Cherepanov <cas@altlinux.org> 3.19.0.0-alt1
- New version

* Fri Oct 20 2017 Andrey Cherepanov <cas@altlinux.org> 3.18.1.3-alt1
- New version

* Thu Oct 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.18.1.0-alt1
- New version

* Mon Oct 02 2017 Andrey Cherepanov <cas@altlinux.org> 3.18.0.2-alt1
- New version

* Sat Sep 23 2017 Andrey Cherepanov <cas@altlinux.org> 3.18.0.0-alt0.M80P.1
- Backport new version to p8 branch

* Sat Sep 23 2017 Andrey Cherepanov <cas@altlinux.org> 3.18.0.0-alt1
- New version

* Thu Sep 07 2017 Andrey Cherepanov <cas@altlinux.org> 3.17.3.8-alt1
- New version

* Tue Aug 15 2017 Andrey Cherepanov <cas@altlinux.org> 3.17.3.7-alt0.M80P.1
- Backport new version to p8 branch (ALT #33767)

* Tue Aug 15 2017 Andrey Cherepanov <cas@altlinux.org> 3.17.3.7-alt1
- New version

* Sun Jul 23 2017 Andrey Cherepanov <cas@altlinux.org> 3.17.3.6-alt1
- New version

* Mon Jul 17 2017 Andrey Cherepanov <cas@altlinux.org> 3.17.3.4-alt1
- New version

* Fri Jul 14 2017 Andrey Cherepanov <cas@altlinux.org> 3.17.3.3-alt1
- New version

* Tue Jul 11 2017 Andrey Cherepanov <cas@altlinux.org> 3.17.3.1-alt1
- New version

* Wed Jul 05 2017 Sergey V Turchin <zerg@altlinux.org> 3.17.1.1-alt0.M80P.2
- Rebuild with new Qt

* Sat Jul 01 2017 Andrey Cherepanov <cas@altlinux.org> 3.17.3.0-alt1
- New version

* Sun Jun 25 2017 Andrey Cherepanov <cas@altlinux.org> 3.17.2.0-alt1
- New version

* Tue Jun 13 2017 Andrey Cherepanov <cas@altlinux.org> 3.17.1.5-alt1
- New version

* Fri Jun 09 2017 Andrey Cherepanov <cas@altlinux.org> 3.17.1.4-alt1
- New version

* Tue May 23 2017 Andrey Cherepanov <cas@altlinux.org> 3.17.1.1-alt0.M80P.1
- Backport new version to p8 branch

* Tue May 23 2017 Andrey Cherepanov <cas@altlinux.org> 3.17.1.1-alt1
- New version

* Fri May 19 2017 Andrey Cherepanov <cas@altlinux.org> 3.17.0.0-alt0.M80P.1
- Backport new version to p8 branch

* Fri May 19 2017 Andrey Cherepanov <cas@altlinux.org> 3.17.0.0-alt1
- New version

* Wed Mar 22 2017 Andrey Cherepanov <cas@altlinux.org> 3.16.7.0-alt1
- New version

* Wed Mar 01 2017 Andrey Cherepanov <cas@altlinux.org> 3.16.5.3-alt1
- New version

* Sat Feb 04 2017 Andrey Cherepanov <cas@altlinux.org> 3.16.5.0-alt1
- new version 3.16.5.0

* Sun Jan 29 2017 Andrey Cherepanov <cas@altlinux.org> 3.16.4.4-alt1
- new version 3.16.4.4

* Thu Jan 19 2017 Sergey V Turchin <zerg@altlinux.org> 3.16.4.0-alt1.1
- rebuild with new Qt

* Tue Jan 17 2017 Andrey Cherepanov <cas@altlinux.org> 3.16.4.0-alt1
- new version 3.16.4.0

* Tue Jan 03 2017 Andrey Cherepanov <cas@altlinux.org> 3.16.3.1-alt1
- new version 3.16.3.1

* Mon Dec 26 2016 Andrey Cherepanov <cas@altlinux.org> 3.16.2.4-alt1
- new version 3.16.2.4

* Thu Oct 27 2016 Andrey Cherepanov <cas@altlinux.org> 3.15.5.7-alt1
- new version 3.15.5.7

* Thu Oct 06 2016 Andrey Cherepanov <cas@altlinux.org> 3.15.5.3-alt0.M80P.1
- Backport new version to p8 branch

* Thu Oct 06 2016 Andrey Cherepanov <cas@altlinux.org> 3.15.5.3-alt1
- new version 3.15.5.3

* Sun Aug 14 2016 Andrey Cherepanov <cas@altlinux.org> 3.15.4.3-alt1
- new version 3.15.4.3

* Wed Jul 06 2016 Andrey Cherepanov <cas@altlinux.org> 3.15.4.1-alt1
- new version 3.15.4.1

* Tue Jun 14 2016 Andrey Cherepanov <cas@altlinux.org> 3.15.3.0-alt1
- new version 3.15.3.0
- require Qt translations for correct localization

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 3.15.2.2-alt1
- New version

* Fri Mar 11 2016 Andrey Cherepanov <cas@altlinux.org> 3.12.8.2-alt1
- New version

* Mon Feb 15 2016 Andrey Cherepanov <cas@altlinux.org> 3.12.6.1-alt1
- New version

* Wed Jan 20 2016 Andrey Cherepanov <cas@altlinux.org> 3.12.4.9-alt1
- New version
- Disable debug output in runtime

* Fri Dec 18 2015 Andrey Cherepanov <cas@altlinux.org> 3.12.4.2-alt1
- New version

* Tue Dec 08 2015 Andrey Cherepanov <cas@altlinux.org> 3.12.3.3-alt1
- New version

* Fri Nov 13 2015 Andrey Cherepanov <cas@altlinux.org> 3.12.1.0-alt1
- New version

* Mon Nov 02 2015 Andrey Cherepanov <cas@altlinux.org> 3.11.6.0-alt1
- New version
- Built with Qt5

* Sat Oct 17 2015 Andrey Cherepanov <cas@altlinux.org> 3.11.3.0-alt1
- New version

* Thu Oct 01 2015 Andrey Cherepanov <cas@altlinux.org> 3.10.2.0-alt1
- New version

* Wed Jul 08 2015 Andrey Cherepanov <cas@altlinux.org> 3.9.4.0-alt1
- New version (ALT #29086)

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0.5.0-alt6.qa3
- NMU: rebuilt for updated dependencies.

* Sat May 21 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.0.5.0-alt6.qa2
- NMU: fix desktop permissions

* Tue May 17 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.0.5.0-alt6.qa1
- NMU (by repocop): the following fixes applied:
  * freedesktop-desktop-file-proposed-patch for qcad

* Mon Oct 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.0.5.0-alt6
- fixed build with gcc4.3

* Thu May 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.0.5.0-alt5
- drop old menu, added freedesktop menu
- build translations
- install help
- added Tango icons by default
- updated build dependencies

* Sun Oct 01 2006 Michail Yakushin <silicium@altlinux.ru> 2.0.5.0-alt4
- support x86_64
- fix bug 10051

* Mon May 29 2006 Michail Yakushin <silicium@altlinux.ru> 2.0.5.0-alt3
- gcc4.1

* Tue Mar 21 2006 Michail Yakushin <silicium@altlinux.ru> 2.0.5.0-alt2
- dependense cleanup (fix bug 9274) 

* Wed Mar 08 2006 Michail Yakushin <silicium@altlinux.ru> 2.0.5.0-alt1
- new version

* Sun Feb 20 2005 Michail Yakushin <silicium@altlinux.ru> 2.0.4.0-alt2
- fix bug 6023

* Wed Nov 17 2004 Michail Yakushin <silicium@altlinux.ru> 2.0.4.0-alt1
- new version

* Wed Jun 30 2004 Michail Yakushin <silicium@altlinux.ru> 2.0.3.1-alt3
- fix bug 4539

* Wed May 26 2004 Michail Yakushin <silicium@altlinux.ru> 2.0.3.1-alt2
- fixes in spec for python 

* Sun Mar 28 2004 Michail Yakushin <silicium@altlinux.ru> 2.0.3.1-alt1
- new version 

* Sat Feb 07 2004 Michail Yakushin <silicium@altlinux.ru> 2.0.2.0-alt1
- new version

* Sat Jan 10 2004 Michail Yakushin <silicium@altlinux.ru> 2.0.1.3-alt2
- fix spec

* Wed Dec 10 2003 Michail Yakushin <silicium@altlinux.ru> 2.0.1.3-alt1
- new version

* Mon Dec 01 2003 Michail Yakushin <silicium@altlinux.ru> 2.0.1.2-alt1
- new version

* Fri Oct 31 2003 Michail Yakushin <silicium@altlinux.ru> 2.0.1.1-alt1
- new version

* Mon Oct 20 2003 Michail Yakushin <silicium@altlinux.ru> 2.0.1.0-alt1
- new version,
- some cleanup in requries

* Sat Oct 05 2002 Rider <rider@altlinux.ru> 1.5.4-alt1
- new version

* Fri Sep 20 2002 Rider <rider@altlinux.ru> 1.5.3-alt1
- new version

* Wed Aug 14 2002 Rider <rider@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Tue Jan 29 2002 Rider <rider@altlinux.ru>
- specfile bugfix and cleanup
- russian summary and description

* Tue Apr 10 2001 Rider <rider@altlinux.ru>
- 1.4.7

* Sat Dec 16 2000 AEN <aen@logic.ru>
- 1.4.4
- new gcc296 patch

* Sat Nov 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.4.1-5mdk
- fix gcc2.96 compilation.

* Fri Sep 08 2000 Enzo Maggi <enzo@mandrakesoft.com> 1.4.1-4mdk
- recompiled with the right flags

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.4.1-3mdk
- automatically added BuildRequires

* Thu Jul 27 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.4.1-2mdk
- macroszifications
- rebuild for the BM

* Tue Jun 20 2000 Enzo Maggi <enzo@mandrakesoft.com> 1.4.1-1mdk
- packaged version 1.4.1

* Wed May 03 2000 Geoffrey Lee <snailtalk@linux-mandrake.com>
- _prefix && _tmppath

* Wed Apr 26 2000 Enzo Maggi <enzo@mandrakesoft.com> 1.3.3-5mdk
- Adapted to the new location of the qt2 includes

* Tue Apr 11 2000 Enzo Maggi <enzo@mandrakesoft.com> 1.3.3-4mdk
- Changed group
- New menu entry

* Thu Jan 27 2000 Camille BИgnis <camille@mandrakesoft.com> 1.3.3-2mdk
- fixed typo in qcad.kdelink

* Thu Dec 30 1999 Giuseppe GhibР <ghibo@linux-mandrake.com>
- Updated to version 1.3.3.

* Mon Nov  8 1999 Giuseppe GhibР <ghibo@linux-mandrake.com>
- First spec file for Mandrake distribution.
