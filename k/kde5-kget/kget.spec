%define rname kget

%define sover 5
%define libkgetcore libkgetcore%sover

Name: kde5-%rname
Version: 19.12.2
Release: alt1
%K5init

Group: Networking/File transfer
Summary: Downloader for KDE
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: kf5-kio

Source: %rname-%version.tar
Patch1: alt-dbus-service.patch

# Automatically added by buildreq on Thu Dec 03 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gtk-update-icon-cache kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libgpg-error-devel libjson-c libkf5gpgmepp-pthread libqca-qt5 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms pkg-config python-base python-modules python3 python3-base qt5-base-devel ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: boost-devel-headers extra-cmake-modules gcc-c++ kde5-gpgmepp-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libgpgme-devel libmms-devel libqca-qt5-devel libsqlite3-devel python-module-google rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: boost-devel-headers libgpgme-devel libassuan-devel libmms-devel libqca-qt5-devel libsqlite3-devel
BuildRequires: plasma5-workspace-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel
BuildRequires: kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kservice-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel
BuildRequires: kf5-solid-devel kf5-sonnet-devel

%description
Dolphin is a file manager for KDE focusing on usability.

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

%package -n %libkgetcore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkgetcore
KF5 library

%prep
%setup -n %rname-%version
%patch1 -p1
sed -i '/^find_package(KF5Torrent/d' CMakeLists.txt

%build
%K5build \
    -DGENERIC_LIB_VERSION=4.97.0 \
    -DGENERIC_LIB_SOVERSION=%sover \
    #

%install
%K5install
%K5install_move data kget khtml kwebkitpart dolphinpart kconf_update
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_datadir/qlogging-categories5/*.*categories

%files
#%config(noreplace) %_K5xdgconf/*
%_K5bin/*
%_K5plug/kget/
%_K5plug/*kget*.so
%_K5icon/*/*/apps/kget.*
%_K5cfg/kget*
%_K5conf_up/kget*
%_K5data/kget/
%_K5xdgapp/*kget*
%_K5data/kwebkitpart//kpartplugins/kget*
%_K5data/dolphinpart/kpartplugins/kget*
%_K5data/khtml/kpartplugins/kget*
%_K5notif/kget*
%_K5xmlgui/kget/
%_K5srv/kget_*
%_K5srv/ServiceMenus/kget_*
%_K5srvtyp/kget_*
%_K5dbus_srv/*kget*

#%files devel
#%_K5inc/kget
#%_K5link/lib*.so
#%_K5lib/cmake/KGet/
#%_K5dbus_iface/org.freedesktop.KGet.xml

%files -n %libkgetcore
%_K5lib/libkgetcore.so.*
%_K5lib/libkgetcore.so.%sover

%changelog
* Fri Feb 14 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt1
- new version

* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Wed Aug 28 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Tue May 07 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Mon Feb 25 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Thu Jan 18 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.1-alt1%ubt
- new version

* Wed Dec 20 2017 Sergey V Turchin <zerg@altlinux.org> 17.12.0-alt2%ubt
- update translations

* Wed Dec 20 2017 Sergey V Turchin <zerg@altlinux.org> 17.12.0-alt1%ubt
- new version

* Tue Mar 21 2017 Sergey V Turchin <zerg@altlinux.org> 4.97.0-alt2%ubt
- update from frameworks branch

* Fri Dec 04 2015 Sergey V Turchin <zerg@altlinux.org> 4.97.0-alt1
- initial build
