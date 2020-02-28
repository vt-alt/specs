%define rname xdg-desktop-portal-kde

Name: plasma5-%rname
Version: 5.18.1
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE5 xdg-desktop-portal
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: xdg-desktop-portal-kde = %version-%release

Requires: xdg-desktop-portal

Source: %rname-%version.tar
Source1: env.sh

# Automatically added by buildreq on Thu Feb 20 2020 (-bi)
# optimized out: clang7.0 cmake cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libdbusmenu-qt52 libglvnd-devel libgpg-error libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-svg libqt5-texttospeech libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libwayland-client libwayland-server libxcbutil-keysyms pipewire-libs pkg-config python-modules python2-base python3 python3-base qt5-base-devel qt5-declarative-devel rpm-build-python3 sh4
#BuildRequires: appstream extra-cmake-modules kf5-kdeclarative-devel kf5-ki18n-devel kf5-kio-devel kf5-kirigami-devel kf5-knotifications-devel kf5-kpackage-devel kf5-kwayland-devel kf5-plasma-framework-devel libcups-devel libepoxy-devel libgbm-devel libssl-devel pipewire-libs-devel python3-dev qt5-wayland-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: qt5-wayland-devel
BuildRequires: libcups-devel glib2-devel libepoxy-devel libgbm-devel libssl-devel pipewire-libs-devel
BuildRequires: extra-cmake-modules kf5-kdeclarative-devel kf5-ki18n-devel kf5-kio-devel kf5-kirigami-devel
BuildRequires: kf5-knotifications-devel kf5-kpackage-devel kf5-kwayland-devel kf5-plasma-framework-devel
# python3-dev


%description
A backend implementation for [xdg-desktop-portal](http://github.com/flatpak/xdg-desktop-portal)
that is using Qt/KF5.


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data xdg-desktop-portal-kde
mkdir -p %buildroot/%_K5xdgconf/plasma-workspace/env/
install -m 0755 %SOURCE1 %buildroot/%_K5xdgconf/plasma-workspace/env/%{name}.sh
%find_lang %name --all-name

%files -f %name.lang
%doc COPYING* README.md
%_K5xdgapp/*portal*.desktop
%_K5libexecdir/*portal*kde*
%_K5dbus_srv/*portal*kde*.service
%_K5data/xdg-desktop-portal-kde/
%_datadir/xdg-desktop-portal/portals/kde.portal
%config(noreplace) %_K5xdgconf/plasma-workspace/env/*.sh

%changelog
* Wed Feb 19 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.1-alt1
- new version

* Thu Jan 09 2020 Sergey V Turchin <zerg@altlinux.org> 5.17.5-alt1
- new version

* Thu Dec 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.4-alt1
- new version

* Wed Nov 13 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.3-alt1
- new version

* Fri Nov 01 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.2-alt1
- new version

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.1-alt1
- new version

* Thu Oct 17 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.5-alt1
- new version

* Thu Aug 01 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.4-alt1
- new version

* Thu Jul 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.3-alt1
- new version

* Wed Jun 26 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.2-alt1
- new version

* Tue Jun 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.1-alt1
- new version

* Tue Jun 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt4
- don't export $GTK_USE_PORTAL by default

* Fri Jun 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt3
- fix environment script

* Fri Jun 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt2
- export environment variable to turn on portal

* Wed Feb 7 2018 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt1
- initial build
