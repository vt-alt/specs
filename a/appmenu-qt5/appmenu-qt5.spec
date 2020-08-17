
%define rname appmenu-qt5
Name: appmenu-qt5
Version: 0.3.1
Release: alt0.5

Group: Graphical desktop/Other
Summary: Global application menu to Qt
Url: http://launchpad.net/appmenu-qt5
License: LGPLv3

Source: %rname-%version.tar
Patch1: alt-qt59.patch

# Automatically added by buildreq on Wed Aug 17 2016 (-bi)
# optimized out: elfutils fontconfig fontconfig-devel gcc-c++ glib2-devel kde5-akonadi-devel kde5-libkleo-devel kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjs-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libEGL-devel libGL-devel libX11-devel libXext-devel libXrender-devel libatk-devel libcairo-devel libdbusmenu-qt52 libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libpango-devel libqt5-core libqt5-dbus libqt5-gui libqt5-widgets libstdc++-devel libudev-devel libwayland-client libwayland-server perl pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-phonon-devel qt5-script-devel qt5-webchannel-devel qt5-webkit-devel qt5-xmlpatterns-devel rpm-build-python3 ruby ruby-stdlibs xorg-xproto-devel
#BuildRequires: kde5-akonadi-calendar-devel kde5-calendarsupport-devel kde5-eventviews-devel kde5-gpgmepp-devel kde5-grantleetheme-devel kde5-incidenceeditor-devel kde5-kalarmcal-devel kde5-kblog-devel kde5-kcalcore-devel kde5-kcalutils-devel kde5-kcontacts-devel kde5-kdgantt2-devel kde5-kholidays-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kldap-devel kde5-kmailtransport-devel kde5-kmbox-devel kde5-kmime-devel kde5-kontactinterface-devel kde5-kpimtextedit-devel kde5-ktnef-devel kde5-libgravatar-devel kde5-libkcddb-devel kde5-libkdepim-devel kde5-libksieve-devel kde5-mailcommon-devel kde5-mailimporter-devel kde5-messagelib-devel kde5-pim-apps-libs-devel kde5-pimcommon-devel kde5-pimlibs-devel kde5-syndication-devel kf5-bluez-qt-devel kf5-kactivities-devel kf5-kactivities-stats-devel kf5-karchive-devel kf5-kcmutils-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdesu-devel kf5-kdewebkit-devel kf5-kdnssd-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kpeople-devel kf5-kplotting-devel kf5-kpty-devel kf5-kross-devel kf5-krunner-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwayland-devel kf5-kwindowsystem-devel kf5-kxmlrpcclient-devel kf5-libkgapi-devel kf5-libkscreen-devel kf5-modemmanager-qt-devel kf5-networkmanager-qt-devel kf5-sonnet-devel kf5-threadweaver-devel libdbusmenu-qt5-devel libgtk+2-devel libinput-devel libmtdev-devel libts-devel libxkbcommon-devel python-module-google python3-dev qt5-base-devel-static qt5-connectivity-devel qt5-multimedia-devel qt5-quick1-devel qt5-sensors-devel qt5-serialport-devel qt5-svg-devel qt5-tools-devel qt5-webengine-devel qt5-websockets-devel qt5-x11extras-devel rpm-build-ruby
BuildRequires: qt5-base-devel-static qt5-x11extras-devel
BuildRequires: pkgconfig(dbusmenu-qt5)
BuildRequires: pkgconfig(gtk+-2.0) pkgconfig(xkbcommon) pkgconfig(udev) pkgconfig(mtdev) pkgconfig(libinput) libts-devel

%description
This package allows Qt to export its menus over DBus.

%prep
%setup -qn %rname-%version
%patch1 -p1

echo "load(qt_build_config)" >>.qmake.conf

%build
%qmake_qt5
%make_build

%install
%installqt5

%files
%doc README
%_qt5_plugindir/platformthemes/libappmenu-qt5.so

%changelog
* Fri Aug 14 2020 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt0.5
- fix compile wit Qt 5.15

* Fri Jun 14 2019 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt0.4
- don't use ubt macro

* Mon Nov 26 2018 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt0.3
- fix to build

* Thu Oct 19 2017 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt0.2

* Thu Oct 19 2017 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt0.2

* Mon Mar 20 2017 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt0.1
- update to 0.3.1 20170216

* Thu Aug 18 2016 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt0.2
- fix build requires

* Wed Aug 17 2016 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt0.1
- initial build of 0.3.0 20160628 snapshot

