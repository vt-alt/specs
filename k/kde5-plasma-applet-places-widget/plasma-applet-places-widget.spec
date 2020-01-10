%define rname plasma-applet-places-widget

Name: kde5-%rname
Version: 1.3
Release: alt2
%K5init altplace

Group: Graphical desktop/KDE
Summary:  User places widget
Url: https://github.com/dfaust/plasma-applet-places-widget
License: GPLv2
BuildArch: noarch

Requires: kf5-filesystem

Source: %rname-%version.tar
Source1: ru.po
Patch1: alt-metadata.patch
Patch2: alt-auto-width.patch
Patch3: alt-defaults.patch

# Automatically added by buildreq on Mon Aug 21 2017 (-bi)
# optimized out: cmake cmake-modules gcc-c++ kf5-kconfig-devel kf5-kcoreaddons-devel libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-quick libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python-modules python3 python3-base qt5-base-common qt5-base-devel rpm-build-python3
#BuildRequires: extra-cmake-modules kf5-ki18n-devel kf5-kpackage-devel kf5-kservice-devel kf5-kwindowsystem-devel kf5-plasma-framework-devel python-module-google python3-dev python3-module-zope ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules kf5-ki18n-devel kf5-kpackage-devel kf5-kservice-devel kf5-kwindowsystem-devel kf5-plasma-framework-devel

%description
Plasma 5 widget that gives access to user places.

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1

mkdir -p po/ru
install -m 0644 %SOURCE1 po/ru/plasma_applet_org.kde.placesWidget.po

cat >>CMakeLists.txt <<__EOF__
find_package(KF5I18n CONFIG REQUIRED)
ki18n_install(po)
__EOF__


%build
%K5build

%install
%K5install
%find_lang %name --all-name

%files -f %name.lang
%_K5data/plasma/plasmoids/org.kde.placesWidget/
%_K5srv/plasma-applet-org.kde.placesWidget.desktop

%changelog
* Fri Dec 27 2019 Sergey V Turchin <zerg@altlinux.org> 1.3-alt2
- update russian translation

* Wed Jun 19 2019 Sergey V Turchin <zerg@altlinux.org> 1.3-alt1
- new version

* Fri Dec 22 2017 Sergey V Turchin <zerg@altlinux.org> 1.2-alt0.1
- remove baloo searches

* Mon Aug 21 2017 Sergey V Turchin <zerg@altlinux.org> 1.1-alt3
- fix build requires

* Wed Jul 05 2017 Sergey V Turchin <zerg@altlinux.org> 1.1-alt2
- set automatic widget width

* Mon Oct 31 2016 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- initial build
