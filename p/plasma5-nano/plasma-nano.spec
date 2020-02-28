%define rname plasma-nano

Name: plasma5-nano
Version: 5.18.1
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Plasma 5 minimal shell
Url: http://www.kde.org
License: GPL-2.0-or-later AND LGPL-2.1-or-later

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Feb 20 2020 (-bi)
# optimized out: cmake cmake-modules elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kconfig-devel kf5-kcoreaddons-common kf5-kcoreaddons-devel kf5-kjobwidgets-common kf5-kwidgetsaddons-common kf5-kwindowsystem-devel libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-quick libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libwayland-client libxcbutil-keysyms perl python-modules python2-base python3 python3-base qt5-base-common qt5-base-devel qt5-declarative-devel rpm-build-python3 rpm-build-qml sh4
#BuildRequires: appstream extra-cmake-modules kf5-ki18n-devel kf5-kpackage-devel kf5-kservice-devel kf5-kwayland-devel kf5-plasma-framework-devel libssl-devel python-modules-compiler python3-dev qt5-translations qt5-wayland-devel rpm-build-gir
BuildRequires(pre): rpm-build-kf5
BuildRequires: qt5-base-devel qt5-wayland-devel
BuildRequires: extra-cmake-modules kf5-ki18n-devel kf5-kpackage-devel kf5-kservice-devel kf5-kwayland-devel
BuildRequires: kf5-plasma-framework-devel

%description
A minimal plasma shell package intended for embedded devices.

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

%package -n libplasma-nano
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libplasma-nano
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --all-name

%files -f %name.lang
%doc COPYING*
%_K5qml/org/kde/plasma/private/nanoshell/
%_K5data/plasma/packages/org.kde.plasma.nano.desktoptoolbox/
%_K5data/plasma/shells/org.kde.plasma.nano/
%_K5srv/*nano*.desktop

%changelog
* Thu Feb 20 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.1-alt1
- initial build
