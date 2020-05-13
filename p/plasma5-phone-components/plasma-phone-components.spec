%define rname plasma-phone-components
%def_disable dialer

Name: plasma5-phone-components
Version: 5.18.5
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: UI components for Plasma Phone
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar
Patch1: alt-kwinwrapper.patch
Patch2: alt-def-shell.patch
Patch3: alt-no-dialer.patch

# Automatically added by buildreq on Fri Feb 21 2020 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gstreamer1.0-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-common kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-common kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-common kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libdbusmenu-qt52 libglvnd-devel libgpg-error libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-svg libqt5-test libqt5-texttospeech libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libtelepathy-qt5-farstream0 libtelepathy-qt5-service0 libtelepathy-qt50 libwayland-client libxcbutil-keysyms pkg-config python-modules python2-base python3 python3-base qt5-base-common qt5-base-devel qt5-declarative-devel rpm-build-gir rpm-build-python3 rpm-build-qml sh4
#BuildRequires: appstream extra-cmake-modules gst-plugins1.0-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-ki18n-devel kf5-kio-devel kf5-knotifications-devel kf5-kpackage-devel kf5-kpeople-devel kf5-kwayland-devel kf5-plasma-framework-devel libssl-devel python-modules-compiler python3-dev qt5-translations qt5-wayland-devel telepathy-qt5-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel qt5-wayland-devel
BuildRequires: gst-plugins1.0-devel telepathy-qt5-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-ki18n-devel kf5-kio-devel kf5-knotifications-devel
BuildRequires: kf5-kpackage-devel kf5-kpeople-devel kf5-kwayland-devel kf5-plasma-framework-devel

%if_enabled dialer
BuildRequires: phonenumber-devel
%endif

%description
UI components for Plasma Phone.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libplasma-phone-components
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libplasma-phone-components
%name library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%if_disabled dialer
%patch3 -p1
sed -i 's|\(.*add_subdirectory.*dialer.*\)|#\1|' CMakeLists.txt
%endif

%build
%K5build \
    -DLIBEXEC_INSTALL_DIR:PATH=%_K5exec \
    #

%install
%K5install
%K5install_move data kwin sounds wallpapers
%find_lang %name --all-name

%files -f %name.lang
%doc COPYING* README.md
%_K5bin/kwinwrapper
%_K5plug/plasma/applets/*.so
%_K5qml/QtQuick/VirtualKeyboard/Styles/Plasma/
%_K5srv/*.desktop
%_K5data/plasma/look-and-feel/org.kde.plasma.phone/
%_K5data/plasma/plasmoids/*/
%_K5data//kwin/scripts/org.kde.phone.multitasking/
%_K5data/plasma/shells/org.kde.plasma.phone/
%_K5snd/sitter/
%_K5wall/org.kde.plasma.phone.lockers/
%_datadir/wayland-sessions/plasma-mobile.desktop

%changelog
* Thu May 07 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.5-alt1
- new version

* Thu Apr 02 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.4-alt1
- new version

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.3-alt1
- new version

* Thu Mar 05 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.1-alt3
- update defaults

* Thu Mar 05 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.1-alt2
- update defaults

* Thu Feb 20 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.1-alt1
- initial build
