%define rname ark

%define sover 19
%define libkerfuffle libkerfuffle%sover

Name: kde5-%rname
Version: 19.08.0
Release: alt1
%K5init altplace

Group: Archiving/Compression
Summary: KDE archivers frontend
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: unrar p7zip unzip zip

Source: %rname-%version.tar
Patch1: alt-clizip-priority.patch

# Automatically added by buildreq on Wed Aug 05 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python3 python3-base ruby ruby-stdlibs xml-common xml-utils zlib-devel
#BuildRequires: bzlib-devel extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-kglobalaccel-devel kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjs-devel kf5-knotifications-devel kf5-kparts-devel kf5-kpty-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libarchive-devel libdb4-devel liblzma-devel python-module-google qt5-base-devel rpm-build-python3 rpm-build-ruby zlib-devel-static
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: bzlib-devel libarchive-devel liblzma-devel zlib-devel
#BuildRequires: libzip-devel # wrong filenames decodings
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kitemmodels-devel
BuildRequires: kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kglobalaccel-devel kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-kjs-devel kf5-knotifications-devel kf5-kparts-devel kf5-kpty-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

%description
Frontend to many archivers.

%package common
Summary: %name common package
Group: System/Configuration/Other
#BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkerfuffle
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkerfuffle
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
mv %buildroot/%_K5xdgmime/kerfuffle{,5}.xml
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%dir %_K5plug/kf5/kfileitemaction/
%_K5xdgmime/kerfuffle5.xml
%_datadir/qlogging-categories5/*.*categories

%files
%_K5bin/ark
%_K5plug/arkpart.so
%_K5plug/kf5/kio_dnd/extracthere.so
%_K5plug/kf5/kfileitemaction/*.so
%_K5xmlgui/ark/
%_K5xdgapp/*ark*.desktop
%_K5srv/ark*.desktop
%_K5cfg/*ark*.kcfg
#%_K5srv/ServiceMenus/ark_*.desktop
%_K5icon/hicolor/*/apps/ark.*
#
%_K5plug/kerfuffle/
%_K5srvtyp/kerfuffle*.desktop

#%files devel
#%_K5inc/ark_version.h
#%_K5inc/ark/
#%_K5link/lib*.so
#%_K5lib/cmake/ark
#%_K5archdata/mkspecs/modules/qt_ark.pri

%files -n %libkerfuffle
%_K5lib/libkerfuffle.so.%sover
%_K5lib/libkerfuffle.so.*

%changelog
* Tue Aug 27 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Mon May 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Tue Feb 19 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Tue May 22 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Mar 06 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Mon Nov 13 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Tue Apr 25 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt0.1%ubt
- new version
- fix zip filenames encoding (ALT#33230)

* Thu Mar 23 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Nov 24 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt0.M80P.1
- build for M80P

* Wed Nov 23 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Tue Sep 06 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- new version

* Thu Jul 14 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Fri Jul 01 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Fri Feb 26 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Tue Dec 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Thu Aug 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Mon Aug 03 2015 Sergey V Turchin <zerg@altlinux.org> 15.7.80-alt1
- initial build
