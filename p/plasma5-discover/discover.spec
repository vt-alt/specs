%define rname discover

Name: plasma5-%rname
Version: 5.16.5
Release: alt2
%K5init no_altplace

Group: System/Configuration/Packaging
Summary: KDE Software Center
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: packagekit appstream-data
Requires: kf5-kirigami

Source: %rname-%version.tar
Source1: env-flatpak.sh
Patch1: alt-offline-updates.patch

# Automatically added by buildreq on Tue Aug 07 2018 (-bi)
# optimized out: appstream appstream-qt cmake cmake-modules elfutils fontconfig gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gtk-update-icon-cache kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-common kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-common kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-common kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgio-devel libgpg-error libjson-glib libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-common qt5-base-devel rpm-build-python3 rpm-build-qml ruby ruby-stdlibs sh3
#BuildRequires: appstream-qt-devel extra-cmake-modules kf5-karchive-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kio-devel kf5-kirigami-devel kf5-kitemmodels-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kpackage-devel kf5-plasma-framework-devel libflatpak-devel libssl-devel packagekit-qt-devel python3-dev qt5-declarative-devel qt5-translations rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: libssl-devel qt5-declarative-devel
BuildRequires: packagekit-qt-devel
BuildRequires: appstream-qt-devel
BuildRequires: libflatpak-devel
BuildRequires: extra-cmake-modules kf5-karchive-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kio-devel
BuildRequires: kf5-kirigami-devel kf5-kitemmodels-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kpackage-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-plasma-framework-devel

%description
KDE and Plasma resources management GUI.

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

%package flatpak
Summary: Plasma Discover flatpak support
Group: System/Configuration/Packaging
Requires: %name
Requires: flatpak
%description flatpak
Plasma Discover flatpak support.

%package -n libkf5discover
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5discover
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
mv %buildroot/%_libdir/plasma-discover/lib*.so* %buildroot/%_libdir/

%K5install_move data libdiscover discover locale knsrcfiles

mkdir -p %buildroot/%_K5xdgconf/plasma-workspace/env/
install -m 0755 %SOURCE1 %buildroot/%_K5xdgconf/plasma-workspace/env/%{name}-flatpak.sh

%find_lang %name --with-kde --all-name

%files -f %name.lang
%_libdir/libDiscover*.so
#
%doc COPYING*
#%config(noreplace) %_K5xdgconf/*.knsrc
%_K5data/knsrcfiles/*.knsrc
%config(noreplace) %_K5xdgconf/*.*categories
%_K5bin/*
%_K5exec/discover/runservice
%dir %_K5plug/discover-notifier/
%_K5plug/discover-notifier/DiscoverPackageKitNotifier.so
%dir %_K5plug/discover/
%_K5plug/discover/kns-backend.so
%_K5plug/discover/packagekit-backend.so
%_K5qml/org/kde/discovernotifier/
%_K5xdgapp/org.kde.discover.desktop
%_K5xdgapp/org.kde.discover.urlhandler.desktop
%_K5icon/*/*/apps/plasmadiscover.*
%_K5srv/*
%_K5xmlgui/*
%_K5notif/*.notifyrc
%dir %_K5data/libdiscover/
%dir %_K5data/libdiscover/categories/
%_K5data/libdiscover/categories/packagekit-backend-categories.xml
%_K5data/discover/
%_K5data/plasma/plasmoids/org.kde.discovernotifier/
%_datadir/metainfo/org.kde.discover.appdata.xml
%_datadir/metainfo/org.kde.discover.packagekit.appdata.xml
%_datadir/metainfo/org.kde.discovernotifier.appdata.xml


%files flatpak
%config(noreplace) %_K5xdgconf/plasma-workspace/env/*flatpak*.sh
%_K5plug/discover/flatpak-backend.so
%_datadir/metainfo/org.kde.discover.flatpak.appdata.xml
%_K5plug/discover-notifier/FlatpakNotifier.so
%_K5data/libdiscover/categories/flatpak-backend-categories.xml
%_K5xdgapp/org.kde.discover-flatpak.desktop
%_K5icon/*/*/apps/*flatpak*.*

%changelog
* Tue Sep 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.5-alt2
- using PackageKit offline updates by default

* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.5-alt1
- new version

* Thu Aug 01 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.4-alt1
- new version

* Thu Jul 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.3-alt1
- new version

* Thu Jun 27 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.2-alt2
- move files to more standard place

* Wed Jun 26 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.2-alt1
- new version

* Tue Jun 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.1-alt1
- new version

* Fri Jun 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt3
- export environment variable to add flatpak apps to menu

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt2
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt1
- new version

* Wed Apr 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.4-alt1
- new version

* Tue Mar 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt1
- new version

* Thu Jan 31 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt4
- require packagekit
- require flatpak for flatpak-backend

* Thu Jan 10 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt3
- require appstream-data

* Thu Dec 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt2
- rebuild

* Thu Sep 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version
- build flatpak support in separate package

* Tue Aug 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt2%ubt
- build without flatpak

* Tue Aug 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1%ubt
- initial build
