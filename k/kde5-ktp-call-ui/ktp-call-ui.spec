%define rname ktp-call-ui

Name: kde5-%rname
Version: 19.04.3
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: Telepathy VoIP client GUI
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: kde5-ktp-common-internals-common

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Mar 30 2017 (-bi)
# optimized out: boost-devel-headers cmake cmake-modules elfutils gcc-c++ glib2-devel gstreamer1.0-devel kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kwidgetsaddons-devel libEGL-devel libGL-devel libdbus-devel libdbus-glib libdbus-glib-devel libdbusmenu-qt52 libfarstream0.2-devel libgio-devel libgpg-error libgst-plugins1.0 libqt5-core libqt5-dbus libqt5-glib libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-sql libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libtelepathy-farstream libtelepathy-glib libtelepathy-glib-devel libtelepathy-logger-qt5 libtelepathy-qt5-farstream0 libtelepathy-qt5-service0 libtelepathy-qt50 libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-gstreamer1 rpm-build-python3 telepathy-logger-qt5-devel telepathy-qt5-devel
#BuildRequires: extra-cmake-modules kde5-ktp-common-internals-devel kf5-kcmutils-devel kf5-kdeclarative-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-knotifications-devel kf5-kpackage-devel kf5-kservice-devel kf5-kwallet-devel kf5-kxmlgui-devel libtelepathy-farstream-devel python-module-google python3-dev qt5-gstreamer1-devel qt5-phonon-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: kde5-ktp-common-internals-devel libtelepathy-farstream-devel qt5-phonon-devel qt5-gstreamer1-devel
BuildRequires: kf5-kcmutils-devel kf5-kdeclarative-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-knotifications-devel
BuildRequires: kf5-kpackage-devel kf5-kservice-devel kf5-kwallet-devel kf5-kxmlgui-devel

%description
GUI VoIP client software which uses the telepathy framework underneath.


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data ktp-call-ui
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/ktp-dialout-ui
%_K5libexecdir/ktp-call-ui
%_K5data/ktp-call-ui/
%_K5xmlgui/ktp-call-ui/
%_datadir/telepathy/clients/KTp.CallUi.client
%_K5dbus_srv/org.freedesktop.Telepathy.Client.KTp.CallUi.service

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

* Thu Mar 16 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- initial build
