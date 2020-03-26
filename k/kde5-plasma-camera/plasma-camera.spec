%define rname plasma-camera

%define sover 0
%define libplasma_camera libplasma-camera%sover

Name: kde5-%rname
Version: 1.0
Release: alt1
%K5init altplace no_appdata

Group:  Video
Summary: Simple camera application for mobile devices
License: GPL-3.0-only
Url: https://anongit.kde.org/plasma-camera.git

Requires: kf5-kirigami

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Mar 20 2020 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libglvnd-devel libqt5-core libqt5-gui libqt5-network libqt5-qml libqt5-quick libqt5-quickcontrols2 libqt5-svg libqt5-test libqt5-widgets libsasl2-3 libstdc++-devel pkg-config python-modules python2-base python3 python3-base qt5-base-devel qt5-declarative-devel rpm-build-python3 sh4
#BuildRequires: appstream extra-cmake-modules git-core kf5-kirigami-devel libssl-devel python3-dev qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel
BuildRequires: extra-cmake-modules kf5-kirigami-devel

%description
Simple camera application for mobile devices.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install

%find_lang --all-name --with-qt %name

%files -f %name.lang
%_K5bin/*camera*
%_K5xdgapp/*camera*.desktop

%changelog
* Fri Mar 20 2020 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build
