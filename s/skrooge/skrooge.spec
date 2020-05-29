Name: 		skrooge
Version: 	2.22.1
Release: 	alt2
License: 	%gpl2plus
Summary: 	Personal finances manager for KF5
Group: 		Office
URL: 		http://skrooge.org/
Packager: 	Andrey Cherepanov <cas@altlinux.org> 

Source: 	%name-%version.tar.xz
Source1:	%name.po

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: grantlee5-devel
BuildRequires: kf5-kactivities-devel
BuildRequires: kf5-karchive-devel
BuildRequires: kf5-kauth-devel
BuildRequires: kf5-kbookmarks-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-kdelibs4support
BuildRequires: kf5-kdelibs4support-devel
BuildRequires: kf5-kdesignerplugin-devel
BuildRequires: kf5-kdoctools
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kdoctools-devel-static
BuildRequires: kf5-kemoticons-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kinit-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kitemmodels-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-knotifyconfig-devel
BuildRequires: kf5-kpackage-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-krunner-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-kunitconversion-devel
BuildRequires: kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-plasma-framework-devel
BuildRequires: kf5-solid-devel
BuildRequires: kf5-sonnet-devel
BuildRequires: libofx-devel
BuildRequires: libqca-qt5-devel
BuildRequires: libsqlite3-devel
BuildRequires: libsqlcipher-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-script-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-webkit-devel

Requires: libgrantlee_templates5
Requires: kf5-kinit kf5-kio

%description
Skrooge is a personal finances manager for KF5, aiming at being simple
and intuitive.

%prep
%setup
cp -f %SOURCE1 po/ru/skrooge.po

%build
%K5init no_altplace
%K5build -DSKG_CIPHER:BOOL=OFF

%install
%K5install
%find_lang --with-kde %name

%files -f %name.lang
%doc AUTHORS CHANGELOG COPYING README
%_K5bin/*
%_K5xdgconf/%{name}_*.knsrc
%_K5cfg/*
%_K5srv/*
%_K5srvtyp/*
%_K5lib/libskg*
%_qt5_plugindir/designer/libsk*.so*
%_qt5_plugindir/sqldrivers/libsk*.so
%_qt5_plugindir/sk*.so
%_K5xdgmime/*
%_K5xdgapp/*%name.desktop
%_iconsdir/*/*/*/*
%_K5xmlgui/*
%_K5plug/grantlee/*/grantlee_skgfilters.so
%_K5notif/%name.notifyrc
%_datadir/%name

%changelog
* Thu May 28 2020 Andrey Cherepanov <cas@altlinux.org> 2.22.1-alt2
- Complete Russian translation (thanks Olesya Gerasimenko).

* Sun Apr 12 2020 Andrey Cherepanov <cas@altlinux.org> 2.22.1-alt1
- new version 2.22.1

* Fri Dec 06 2019 Andrey Cherepanov <cas@altlinux.org> 2.21.1-alt1
- new version 2.21.1

* Thu Jul 04 2019 Andrey Cherepanov <cas@altlinux.org> 2.20.0-alt1
- new version 2.20.0

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 2.19.1-alt1
- new version 2.19.1

* Mon Apr 22 2019 Andrey Cherepanov <cas@altlinux.org> 2.19.0-alt1
- new version 2.19.0

* Fri Feb 15 2019 Andrey Cherepanov <cas@altlinux.org> 2.18.0-alt1
- new version 2.18.0

* Wed Dec 26 2018 Andrey Cherepanov <cas@altlinux.org> 2.17.0-alt1
- new version 2.17.0

* Wed Nov 07 2018 Andrey Cherepanov <cas@altlinux.org> 2.16.2-alt1
- new version 2.16.2

* Sun Aug 19 2018 Andrey Cherepanov <cas@altlinux.org> 2.15.0-alt1
- New version.

* Mon Jul 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.14.0-alt1
- new version 2.14.0

* Fri May 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.13.0-alt1
- new version 2.13.0

* Fri Mar 16 2018 Andrey Cherepanov <cas@altlinux.org> 2.12.0-alt1
- new version 2.12.0

* Fri Feb 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt1
- new version 2.11.0

* Fri Nov 10 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.5-alt1
- new version 2.10.5

* Wed Aug 16 2017 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt1
- new version 2.9.0

* Mon Jul 24 2017 Andrey Cherepanov <cas@altlinux.org> 2.8.1-alt1
- new version 2.8.1

* Fri Jan 27 2017 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- new version 2.7.0

* Tue Jan 03 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- new version 2.6.0

* Tue Oct 25 2016 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- new version 2.5.0

* Sun Jul 24 2016 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- new version 2.4.0

* Thu Mar 03 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- New version is based on KF5
- Build without sqlcipher support

* Mon Aug 03 2015 Andrey Cherepanov <cas@altlinux.org> 1.12.5-alt1
- New version 1.12.5
- Fix watch file for new stable version tarball

* Sun May 10 2015 Andrey Cherepanov <cas@altlinux.org> 1.12.0-alt1
- New version 1.12.0

* Fri Nov 14 2014 Andrey Cherepanov <cas@altlinux.org> 1.10.0-alt1
- new version 1.10.0

* Thu May 15 2014 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt1
- New version

* Thu Apr 03 2014 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt2
- Rebuild with new version of grantlee

* Sun Nov 24 2013 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- New version
- Build with libofx-0.9.9

* Mon Jul 29 2013 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- New version 1.7.1

* Tue Jan 22 2013 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- New version 1.4.0

* Wed Jan 18 2012 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version 1.2.0
- Add watch file

* Fri Sep 23 2011 Andrey Cherepanov <cas@altlinux.org> 0.9.1-alt1
- New version 0.9.1

* Tue Mar 01 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.0-alt1
- New version 0.8.0
- Return to Sisyphus

* Sat Nov 14 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.5.3-alt1
- initial build for Sisyphus
