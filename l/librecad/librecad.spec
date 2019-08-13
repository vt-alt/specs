Name:     librecad
Version:  2.2.0
Release:  alt0.1.rc1

Summary:  Computer-aided design (CAD) system
Packager: Andrey Cherepanov <cas@altlinux.org>

Url: 	  http://www.librecad.org
License:  GPLv2
Group:    Graphics

Source:   librecad-%version.tar
Patch0:    0001-Adding-DXF-.desktop-file.patch
Patch1:   librecad-fix-desktop.patch
Patch2:   librecad-fix-build-with-qt5.11.patch

Requires: librecad-data

BuildRequires: boost-devel-headers gcc-c++
BuildRequires: libmuparser-devel
BuildRequires: libfreetype-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-sql-mysql qt5-sql-odbc qt5-sql-postgresql
BuildRequires: qt5-tools

%description
LibreCAD is an application for computer aided design (CAD) in two
dimensions (2D). With LibreCAD you can create technical drawings
such as plans for buildings, interiors, mechanical parts or schemas
and diagrams.

%package data
Group: Graphics
Summary: Platform independent files for %name
Requires: %name
BuildArch: noarch

%description data
Contains the platform-independent files for LibreCAD, including
fonts, patterns, translations.

#package doc
#Group:		Graphics
#Summary:	Documentation for %name
#Requires:	%name
#BuildArch:	noarch
#
#description doc
#Documentation for %name, a Qt4 application to design 2D CAD
#drawing based on the community edition of QCad.

%package plugins
Group: Graphics
Summary: Plugins libraries files for %name
Requires: %name

%description plugins
Contains the plugins files for LibreCAD.

%prep
%setup

%patch0 -p1
%patch1 -p1
%patch2 -p1
find . -type f -executable -a \( -name '*.cpp' -o -name '*.h' \) | xargs -i{} chmod 644 {}

%build
export PATH=%_qt5_bindir:$PATH
%qmake_qt5 librecad.pro
%make_build

pushd plugins
	%qmake_qt5
	%make_build plugins.pro
popd

%install
%makeinstall INSTALL_ROOT=%buildroot

install -m 755 -d %buildroot%_datadir/%name/doc
install -m 755 -d %buildroot%_datadir/%name/fonts
install -m 755 -d %buildroot%_datadir/%name/library
install -m 755 -d %buildroot%_datadir/%name/patterns
install -m 755 -d %buildroot%_datadir/%name/qm
install -m 755 -d %buildroot%_docdir/%name
install -m 755 -d %buildroot%_libdir/%name/plugins
install -m 755 -d %buildroot%_datadir/mime/packages

#cp unix/resources/doc/* %buildroot%_datadir/%name/doc/
cp unix/resources/fonts/*.lff %buildroot%_datadir/%name/fonts/
cp -r unix/resources/library/* %buildroot%_datadir/%name/library/
cp unix/resources/patterns/*.dxf %buildroot%_datadir/%name/patterns/
cp unix/resources/qm/*.qm %buildroot%_datadir/%name/qm/
cp unix/resources/plugins/* %buildroot%_libdir/%name/plugins/
find %buildroot%_datadir/%name -type f -exec chmod 644 {} \;

install -Dm 755 unix/%name %buildroot%_bindir/%name
install -Dm 644 desktop/%name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm 644 desktop/%name.sharedmimeinfo %buildroot%_datadir/mime/packages/%name.xml
install -Dm 644 desktop/graphics_icons_and_splash/Icon\ LibreCAD/Icon_Librecad.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/mime/packages/%name.xml

%files data
%dir %_datadir/%name/
%_datadir/%name/fonts/
%_datadir/%name/library/
%_datadir/%name/patterns/
%_datadir/%name/qm/

#files doc
#_datadir/%name/doc/*

%files plugins
%_libdir/%name/plugins/

%changelog
* Mon Aug 12 2019 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt0.1.rc1
- New version (2.2.0-rc1).

* Wed Sep 26 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.3-alt2
- Fix build with Qt 5.11.

* Thu Oct 06 2016 Andrey Cherepanov <cas@altlinux.org> 2.1.3-alt1
- new version 2.1.3

* Fri Aug 05 2016 Andrey Cherepanov <cas@altlinux.org> 2.1.1-alt1
- new version 2.1.1

* Wed Jun 15 2016 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- New version 2.1.0
- Build with Qt5

* Tue Apr 19 2016 Andrey Cherepanov <cas@altlinux.org> 2.0.10-alt1
- New version

* Mon Jan 18 2016 Andrey Cherepanov <cas@altlinux.org> 2.0.9-alt1
- New version

* Thu Aug 27 2015 Andrey Cherepanov <cas@altlinux.org> 2.0.8-alt1
- New version

* Fri Mar 06 2015 Andrey Cherepanov <cas@altlinux.org> 2.0.7-alt1
- New vesion

* Tue Sep 23 2014 Andrey Cherepanov <cas@altlinux.org> 2.0.5-alt1
- New version

* Sun Jun 08 2014 Andrey Cherepanov <cas@altlinux.org> 2.0.4-alt1
- New version

* Mon Mar 24 2014 Andrey Cherepanov <cas@altlinux.org> 2.0.3-alt1
- New version

* Mon Jan 13 2014 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1
- New version

* Tue Nov 05 2013 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt0.rc2
- 2.0.0 rc2

* Sat Jun 02 2012 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.alpha3
- build 2.0.0 alpha3

* Fri Jan 13 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

* Tue Jan 10 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1:1.0.0-1
+ Revision: 759355
- add Epoch: 1
- remove Makefile and spec.in
- remove BuildRoot tag, replace spaces with tabs
- 1.0.0 final release

* Wed Aug 17 2011 Alexandre Lissy <alissy@mandriva.com> 1.0.0rc1.99.2-1
+ Revision: 694859
- Updating to latest git snapshot

* Sat Aug 13 2011 Alexandre Lissy <alissy@mandriva.com> 1.0.0rc1.99.1-1
+ Revision: 694367
- Adding missing source package for 1.0.0rc1.99.1
- Update to latest snapshot, still pre RC2

* Sat Aug 06 2011 Alexandre Lissy <alissy@mandriva.com> 1.0.0rc1.99-1
+ Revision: 693531
- Updating to pre-RC2 snapshot and using new patches capabilities of gitrpm helper
- Using 'mdv' branch for desktop file
- Updating stuff for new gitrpm
- Update for latest rpm-common changes
- Introducing GitRPM funny stuff, see http://git.mandriva.com/projects/?p=users/alissy/gitrpm.git;a=summary

* Thu Jun 23 2011 Alexandre Lissy <alissy@mandriva.com> 1.0.0rc1_55_g4f9b7c5-1
+ Revision: 686840
- Updating from 1.0.0beta5 to 1.0.0rc1

* Tue Jun 07 2011 Alexandre Lissy <alissy@mandriva.com> 1.0.0beta5_144_g0046d99-1
+ Revision: 683100
- Updating to latest git revision
- Dropping obsolete french locale patch

* Sun Jun 05 2011 Alexandre Lissy <alissy@mandriva.com> 1.0.0beta5_132_gf21f8b2-1
+ Revision: 682785
- Updating to latest git tree, and dropping merged patches.

* Thu Jun 02 2011 Alexandre Lissy <alissy@mandriva.com> 1.0.0beta5_116_g88b5983-1
+ Revision: 682483
- Fix missing BuildRequires against qt4-linguist
- Fix missing BuildRequires against qt4-assistant (providing qcollectiongenerator)
- Importing LibreCAD.
- Created package structure for librecad.

