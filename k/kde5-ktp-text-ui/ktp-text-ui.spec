%define rname ktp-text-ui

Name: kde5-%rname
Version: 19.12.1
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Telepathy text chat handler
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: telepathy-logger

Source: %rname-%version.tar
Patch1: alt-soname.patch

# Automatically added by buildreq on Thu Jun 18 2015 (-bi)
# optimized out: cmake cmake-modules elfutils kf5-kcmutils-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libgst-plugins1.0 libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libtelepathy-logger-qt5 libtelepathy-qt5 libtelepathy-qt5-devel libxcbutil-keysyms python-base python3 python3-base qt5-base-devel rpm-build-gir ruby ruby-stdlibs telepathy-logger-qt5-devel
#BuildRequires: extra-cmake-modules gcc-c++ kde5-ktp-common-internals-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kemoticons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kpeople-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libdb4-devel libtelepathy-qt5-devel python-module-google rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel qt5-webengine-devel qt5-speech-devel
BuildRequires: kde5-ktp-common-internals-devel telepathy-qt5-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kemoticons-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel
BuildRequires: kf5-knotifyconfig-devel kf5-kpeople-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel
BuildRequires: kf5-kcmutils-devel

%description
%summary

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem kde5-ktp-common-internals-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libktpchat5
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libktpchat5
KF5 library

%package -n libktpimagesharer5
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libktpimagesharer5
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build \
    -DLIBEXEC_INSTALL_DIR=%_K5exec \
    #

%install
%K5install
%K5install_move data ktelepathy ktp-log-viewer
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files
%_K5bin/ktp-log-viewer
%_K5exec/ktp-*
%_K5plug/ktptextui_*.so
%_K5plug/kcm_ktp*.so
%_K5data/ktelepathy/
%_K5data/ktp-log-viewer/
%_K5srv/kcm_ktp*.desktop
%_K5srv/ktptextui_*.desktop
%_K5srv/*.protocol
%_K5srvtyp/ktptxtui_*.desktop
%_K5xmlgui/ktp-text-ui/
%_K5xdgapp/org.kde.ktplogviewer.desktop
%_K5dbus_srv/org.freedesktop.Telepathy.Client.KTp.*.service
%_datadir/telepathy/clients/KTp.*.client

%files devel
#%_K5inc/ktp-text-ui_version.h
#%_K5inc/ktp-text-ui/
%_K5link/lib*.so
#%_K5lib/cmake/ktp-text-ui
#%_K5archdata/mkspecs/modules/qt_ktp-text-ui.pri

%files -n libktpchat5
%_K5lib/libktpchat.so.5
%_K5lib/libktpchat.so.*
%files -n libktpimagesharer5
%_K5lib/libktpimagesharer.so.5
%_K5lib/libktpimagesharer.so.*

%changelog
* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.2-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Tue Aug 13 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Wed Jun 19 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt2
- new version

* Tue May 07 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Thu Mar 21 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Tue Feb 26 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Wed Jul 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 21 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt2%ubt
- allow to build with Qt 5.6

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Tue Jun 06 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Tue Apr 04 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Wed Sep 21 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Fri Jul 15 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Mon Apr 04 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt2
- fix build requires

* Tue Mar 22 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Mon Feb 29 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Thu Jan 21 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Tue Dec 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Fri Nov 06 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt2
- fix LIBEXEC_INSTALL_DIR

* Thu Nov 05 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Tue Sep 08 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Thu Jul 09 2015 Sergey V Turchin <zerg@altlinux.org> 15.04.3-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.2-alt0.1
- initial build
