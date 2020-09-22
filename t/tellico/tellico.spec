Name: 	 tellico
Version: 3.3.3
Release: alt1

Summary: A collection manager for KDE
License: GPL-2.0+
Group:   Graphical desktop/KDE
Url:     http://tellico-project.org/
# VCS:	 https://invent.kde.org/office/tellico.git

Source:  %name-%version.tar
ExclusiveArch: %ix86 x86_64

BuildRequires(pre): rpm-build-kf5
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: qt5-declarative-devel
BuildRequires: kde5-libkcddb-devel
BuildRequires: kde5-libksane-devel
BuildRequires: kf5-karchive-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kdoctools-devel-static
BuildRequires: kf5-kfilemetadata-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-khtml-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kitemmodels-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-kjs-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-solid-devel
BuildRequires: libdiscid-devel
BuildRequires: libexempi-devel
BuildRequires: libpoppler-qt5-devel
BuildRequires: libtag-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: libyaz-devel
BuildRequires: qimageblitz5-devel
BuildRequires: qjson-qt5-devel

%description
Tellico is a KDE application for organizing your collections. It
provides default templates for books, bibliographies, videos, music,
video games, coins, stamps, trading cards, comic books, and wines.

%prep
%setup -q

%build
%K5init no_altplace
%K5build

%install
%cmakeinstall_std

# fix python shebangs
find %buildroot -type f -print0 |
      xargs -r0 grep -lZ '^#![[:space:]]*%_bindir/.*python$' -- |
      xargs -r0 sed -E -i '1 s@^(#![[:space:]]*)%_bindir/(env[[:space:]]+)?python$@\1%__python3@'

%find_lang --with-kde %name

%files -f %name.lang
%doc AUTHORS README
%_K5bin/*
%_datadir/%name
%_K5xdgapp/*.desktop
%_K5icon/hicolor/*/apps/%name.png
%_K5icon/hicolor/*/mimetypes/application-x-%name.png
%_datadir/kconf_update/*
%_K5cfg/*.kcfg
%_K5xdgconf/%{name}*
%_K5xdgmime/%name.xml
%_K5xmlgui/%name
%_datadir/metainfo/org.kde.tellico.appdata.xml

%changelog
* Thu Sep 17 2020 Andrey Cherepanov <cas@altlinux.org> 3.3.3-alt1
- New version.

* Sat Aug 22 2020 Andrey Cherepanov <cas@altlinux.org> 3.3.2-alt1
- New version.

* Mon Jun 01 2020 Andrey Cherepanov <cas@altlinux.org> 3.3.1-alt1
- New version.
- Fix License tag according to SPDX.

* Sun Apr 26 2020 Andrey Cherepanov <cas@altlinux.org> 3.3-alt1
- New version.

* Mon Dec 02 2019 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt1
- New version.
- Package appdata file.

* Wed Jul 10 2019 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- New version.

* Sun Jun 02 2019 Andrey Cherepanov <cas@altlinux.org> 3.2-alt1
- New version.
- Remove old libraries required Qt4.
- Build only for Intel.

* Thu Dec 20 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.4-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.3-alt1
- New version.

* Wed Mar 28 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.2-alt1
- New version.

* Tue Jan 16 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1
- New version.

* Fri Nov 03 2017 Andrey Cherepanov <cas@altlinux.org> 3.1-alt1
- New version

* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 3.0.2-alt1.1
- NMU: rebuild with new libkcddb
- NMU: clean build requires

* Tue Mar 28 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- New version

* Tue Feb 21 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- new version 3.0.1

* Sun Jan 22 2017 Andrey Cherepanov <cas@altlinux.org> 3.0-alt1
- new version 3.0 for KF5

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.11-alt2
- Build without Nepomuk support

* Tue Dec 08 2015 Andrey Cherepanov <cas@altlinux.org> 2.3.11-alt1
- New version

* Sun Aug 23 2015 Vitaly Lipatov <lav@altlinux.ru> 2.3.10-alt2
- rebuild with new libyaz 5.13

* Sun Mar 08 2015 Andrey Cherepanov <cas@altlinux.org> 2.3.10-alt1
 Initial build in Sisyphus
