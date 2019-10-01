
Name: telepathy-accounts-signon
Version: 2.0
Release: alt1

Group: System/Libraries
Summary: Telepathy providers for libaccounts/libsignon borrowed from Empathy
Url: https://gitlab.com/accounts-sso/telepathy-accounts-signon
License: LGPLv2

Source: %name-%version.tar

# Automatically added by buildreq on Mon Oct 19 2015 (-bi)
# optimized out: elfutils glib2-devel kf5-attica-devel kf5-kjs-devel libaccounts-glib libdbus-devel libdbus-glib libdbus-glib-devel libgio-devel libsignon-glib1 libtelepathy-glib libtelepathy-glib-devel libtelepathy-mission-control pkg-config python-base python-module-google python3 python3-base qt5-base-devel qt5-declarative-devel qt5-phonon-devel qt5-script-devel qt5-webkit-devel ruby ruby-stdlibs
#BuildRequires: kde5-akonadi-calendar-devel kde5-gpgmepp-devel kde5-kalarmcal-devel kde5-kblog-devel kde5-kcalcore-devel kde5-kcalutils-devel kde5-kcontacts-devel kde5-kholidays-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kldap-devel kde5-kmailtransport-devel kde5-kmbox-devel kde5-kmime-devel kde5-kontactinterface-devel kde5-kpimtextedit-devel kde5-ktnef-devel kde5-pimlibs-devel kde5-syndication-devel kf5-bluez-qt-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdesu-devel kf5-kdewebkit-devel kf5-kdnssd-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kpeople-devel kf5-kplotting-devel kf5-kpty-devel kf5-kross-devel kf5-krunner-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-kxmlrpcclient-devel kf5-libkgapi-devel kf5-libkscreen-devel kf5-modemmanager-qt-devel kf5-networkmanager-qt-devel kf5-solid-devel kf5-sonnet-devel kf5-threadweaver-devel libaccounts-glib-devel libtelepathy-mission-control-devel qt5-connectivity-devel qt5-multimedia-devel qt5-quick1-devel qt5-sensors-devel qt5-serialport-devel qt5-svg-devel qt5-tools-devel qt5-websockets-devel qt5-x11extras-devel qt5-xmlpatterns-devel rpm-build-python3 rpm-build-ruby signon-glib-devel
BuildRequires: gcc-c++ rpm-macros-qt5 libaccounts-glib-devel libtelepathy-mission-control-devel signon-glib-devel
BuildRequires: meson

%description
%summary.

%prep
%setup -q

%build
#export PATH=%_qt5_bindir:$PATH
%meson
%meson_build

%install
%meson_install

%files
%doc README*
%_libdir/mission-control-plugins.0/mcp-account-manager-accounts-sso.so

%changelog
* Mon Sep 30 2019 Sergey V Turchin <zerg@altlinux.org> 2.0-alt1
- new version

* Mon Oct 19 2015 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build
