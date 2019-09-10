%define rname xdg-desktop-portal-kde

Name: plasma5-%rname
Version: 5.16.5
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE5 xdg-desktop-portal
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Provides: xdg-desktop-portal-kde = %version-%release

Requires: xdg-desktop-portal

Source: %rname-%version.tar
Source1: env.sh

# Automatically added by buildreq on Fri Jun 07 2019 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libGL-devel libdbusmenu-qt52 libglvnd-devel libgpg-error libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-texttospeech libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 sh4
#BuildRequires: appstream extra-cmake-modules glib2-devel kf5-ki18n-devel kf5-kio-devel kf5-knotifications-devel kf5-kwayland-devel kf5-kwindowsystem-devel libcups-devel libepoxy-devel libgbm-devel libssl-devel python3-dev qt5-wayland-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel qt5-wayland-devel
BuildRequires: kf5-ki18n-devel kf5-kio-devel kf5-knotifications-devel kf5-kwayland-devel kf5-kwindowsystem-devel
BuildRequires: libcups-devel glib2-devel libepoxy-devel libgbm-devel libssl-devel pipewire-libs-devel


%description
A backend implementation for [xdg-desktop-portal](http://github.com/flatpak/xdg-desktop-portal)
that is using Qt/KF5.


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
mkdir -p %buildroot/%_K5xdgconf/plasma-workspace/env/
install -m 0755 %SOURCE1 %buildroot/%_K5xdgconf/plasma-workspace/env/%{name}.sh
%find_lang %name --all-name

%files -f %name.lang
%doc COPYING* README.md
%_K5libexecdir/*portal*kde*
%_K5dbus_srv/*portal*kde*.service
%_datadir/xdg-desktop-portal/portals/kde.portal
%config(noreplace) %_K5xdgconf/plasma-workspace/env/*.sh

%changelog
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
