%define rname kdegraphics-thumbnailers

Name: kde5-graphics-thumbnailers
Version: 21.04.1
Release: alt1
%K5init no_appdata

Group: Graphical desktop/KDE
Summary: KDE Graphics Thumbnailers
Url: http://www.kde.org
License: GPL-2.0-or-later and LGPL-2.0-or-later

# for PDF/PS
Requires: /usr/bin/gs

Source: %rname-%version.tar

# Automatically added by buildreq on Wed May 26 2021 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libctf-nobfd0 libglvnd-devel libgpg-error libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-svg libqt5-waylandclient libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor libxcbutil-keysyms python-modules python2-base python3 python3-base python3-module-paste qt5-base-devel rpm-build-python3 sh4
#BuildRequires: appstream extra-cmake-modules git-core kde5-libkdcraw-devel kde5-libkexiv2-devel kf5-karchive-devel kf5-kio-devel python-modules-encodings python3-dev python3-module-mpl_toolkits qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires: kde5-libkdcraw-devel kde5-libkexiv2-devel
BuildRequires: kf5-karchive-devel kf5-kio-devel

%description
%summary.


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5plug/*thumbnail*.so
%_K5srv/*thumbnail*.desktop
#%_K5cfg/*.kcfg

%changelog
* Wed May 26 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- initial build
