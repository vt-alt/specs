%define rname calindori

%define sover 0
%define libcalindori libcalindori%sover

Name: kde5-%rname
Version: 1.1
Release: alt1
%K5init altplace no_appdata

Summary: Calendar application for Plasma Mobile
License: GPL-3.0-only
Group: Office
Url: https://anongit.kde.org/calindori.git

Requires: kf5-kirigami

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Mar 19 2020 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kconfig-devel kf5-kcoreaddons-devel libdb4-devel libdbusmenu-qt52 libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-quick libqt5-quickcontrols2 libqt5-svg libqt5-test libqt5-texttospeech libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms pkg-config python-modules python2-base python3 python3-base qt5-base-devel qt5-declarative-devel rpm-build-python3 sh4
#BuildRequires: appstream extra-cmake-modules git-core kf5-kcalcore-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kirigami-devel kf5-knotifications-devel kf5-kservice-devel libssl-devel python3-dev qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel
BuildRequires: kf5-kcalcore-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kirigami-devel kf5-knotifications-devel
BuildRequires: kf5-kservice-devel

%description
Calindori is a touch friendly calendar application. It has been designed for mobile devices but it can also run on desktop environments. It offers:
* Monthly agenda
* Multiple calendars
* Event management
* Task management
* Calendar import

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install

%find_lang --all-name --with-qt %name

%files -f %name.lang
%_K5bin/calind*
%_K5xdgapp/*calind*.desktop
%_K5start/*calind*.desktop
%_K5icon/*/*/apps/*calind*.*
%_K5notif/*calind*.notifyrc

%changelog
* Thu Mar 19 2020 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- initial build
