%define rname ktp-common-internals

%define sover 9
%define libktpcommoninternals libktpcommoninternals%sover
%define libktplogger libktplogger%sover
%define libktpmodels libktpmodels%sover
%define libktpotr libktpotr%sover
%define libktpwidgets libktpwidgets%sover

Name: kde5-ktp-common-internals
Version: 19.04.3
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Common internals for KDE Telepathy
Url: https://projects.kde.org/projects/extragear/network/telepathy/%rname
License: LGPLv2+

Source0: %rname-%version.tar

# Automatically added by buildreq on Fri May 22 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libdbus-glib libdbusmenu-qt52 libgcrypt-devel libgpg-error libgpg-error-devel libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-sql libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libtelepathy-glib libtelepathy-logger libtelepathy-logger-qt5 libtelepathy-qt5 libtelepathy-qt5-devel libxcbutil-keysyms python-base python3 python3-base qt5-base-devel qt5-declarative-devel ruby ruby-stdlibs
#BuildRequires: doxygen extra-cmake-modules gcc-c++ graphviz kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kpeople-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libdb4-devel libotr-devel libtelepathy-qt5-devel python-module-google rpm-build-python3 rpm-build-ruby telepathy-logger-qt5-devel
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: doxygen extra-cmake-modules gcc-c++ graphviz
BuildRequires: qt5-declarative-devel
BuildRequires: libotr-devel
# rpm-build-python3
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kpeople-devel kf5-kservice-devel kf5-ktexteditor-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel
BuildRequires: kf5-sonnet-devel
BuildRequires: telepathy-qt5-devel telepathy-logger-qt5-devel
BuildRequires: accounts-qt5-devel signon-devel kde5-kaccounts-integration-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Conflicts: kde4-ktp-common-internals-common
%description common
%name common package

%package core
Summary: Core files for %name
Group: System/Libraries
Requires: %name-common = %version-%release
%description core
Core files for %name

%package -n %libktpcommoninternals
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %version-%release
%description -n %libktpcommoninternals
%name library.

%package -n %libktplogger
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %version-%release
%description -n %libktplogger
%name library.

%package -n %libktpmodels
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %version-%release
%description -n %libktpmodels
%name library.

%package -n %libktpwidgets
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %version-%release
%description -n %libktpwidgets
%name library.

%package -n %libktpotr
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %version-%release
%description -n %libktpotr
%name library.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: kf5-filesystem
Requires: telepathy-qt5-devel
Requires: libtelepathy-logger-devel telepathy-logger-qt5-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -qn %rname-%version

%build
%K5build \
    -DLIBEXEC_INSTALL_DIR=%_K5exec \
    #

%install
%K5install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%dir %_datadir/telepathy/clients
%_K5icon/hicolor/*/actions/im-*.*
%_K5icon/hicolor/*/actions/sort-*.*
%_K5icon/hicolor/*/actions/show-*.*
%_K5icon/hicolor/*/apps/telepathy-kde.*

%files core
%dir %_K5plug/kaccounts/
%dir %_K5plug/kaccounts/daemonplugins/
%dir %_K5plug/kpeople/
%dir %_K5plug/kpeople/actions/
%dir %_K5plug/kpeople/datasource/
%dir %_K5plug/kpeople/widgets/
%_K5exec/ktp-proxy
%_K5qml/org/kde/telepathy/
%_K5plug/*/*/*plugin.so
%_K5plug/ktploggerplugin_tplogger.so
%_K5plug/kaccounts/daemonplugins/kaccounts_ktp_plugin.so
%_K5cfg/ktp-proxy-config.kcfg
#%_K5srv/*plugin.desktop
%_K5srv/ktploggerplugin_tplogger.desktop
%_K5srvtyp/ktp_logger_plugin.desktop
%_K5notif/*rc
%_K5dbus_srv/org.freedesktop.Telepathy.Client.KTp.Proxy.service
%_datadir/telepathy/clients/KTp.*

%files  -n %libktpcommoninternals
%_K5lib/libKTpCommonInternals.so.%sover
%_K5lib/libKTpCommonInternals.so.*
%files  -n %libktplogger
%_K5lib/libKTpLogger.so.%sover
%_K5lib/libKTpLogger.so.*
%files  -n %libktpmodels
%_K5lib/libKTpModels.so.%sover
%_K5lib/libKTpModels.so.*
%files  -n %libktpotr
%_K5lib/libKTpOTR.so.%sover
%_K5lib/libKTpOTR.so.*
%files  -n %libktpwidgets
%_K5lib/libKTpWidgets.so.%sover
%_K5lib/libKTpWidgets.so.*

%files devel
%_datadir/katepart5/syntax/*
%_K5bin/ktp-debugger
%_K5link/lib*.so
%_includedir/KTp/
%_libdir/cmake/KTp/

%changelog
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

* Wed May 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.2-alt1
- initial build
