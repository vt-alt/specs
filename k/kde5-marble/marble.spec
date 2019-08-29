%define rname marble

%define marblewidget_sover 28
%define libmarblewidget libmarblewidget-qt5%marblewidget_sover

Name: kde5-%rname
Version: 19.08.0
Release: alt1
%K5init

Group: Education
Summary: A virtual globe and world atlas
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: alt-astro-static.patch
Patch2: alt-clean-maps.patch

# Automatically added by buildreq on Thu Mar 17 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libgst-plugins1.0 libjson-c libqt5-concurrent libqt5-core libqt5-dbus libqt5-designer libqt5-gui libqt5-location libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-sensors libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-script-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils zlib-devel
#BuildRequires: extra-cmake-modules kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-kpackage-devel kf5-kparts-devel kf5-krunner-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel libgps-devel libshape-devel python-module-google python3.3-site-packages qt5-location-devel qt5-phonon-devel qt5-quick1-devel qt5-svg-devel qt5-tools-devel qt5-webkit-devel rpm-build-ruby zlib-devel-static
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-location-devel qt5-phonon-devel qt5-quickcontrols2-devel qt5-svg-devel qt5-tools-devel qt5-serialport-devel
BuildRequires: qt5-webengine-devel
#BuildRequires: libwlocate-devel
BuildRequires: libgps-devel libshape-devel zlib-devel libprotobuf-devel protobuf-compiler
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-kpackage-devel
BuildRequires: kf5-kparts-devel kf5-krunner-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel

%description
Marble is a Virtual Globe and World Atlas that you can use to learn more
about Earth: You can pan and zoom around and you can look up places and
roads. A mouse click on a place label will provide the respective
Wikipedia article.

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

%package -n %libmarblewidget
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libmarblewidget
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1
#%patch2 -p1

sed -i '/add_subdirectory(marble-qt)/d' src/apps/CMakeLists.txt

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    -DKDE_INSTALL_CONFDIR=%_K5xdgconf \
    -DBUILD_MARBLE_TOOLS=YES \
    -DBUILD_MARBLE_EXAMPLES=NO \
    -DMARBLE_DATA_PATH=%_K5data/marble \
    -DMARBLE_PRI_INSTALL_USE_QT_SYS_PATHS=YES \
    #


%install
%K5install
%K5install_move data marble config.kcfg icons

mv %buildroot/%_K5xdgmime/geo{,-kde5}.xml

mkdir -p %buildroot/%_K5xdgapp
mv %buildroot/%_desktopdir/*.desktop %buildroot/%_K5xdgapp/
mkdir -p %buildroot/%_K5inc
mv %buildroot/%_includedir/marble %buildroot/%_K5inc/


rm -rf %buildroot/%_datadir/locale/*/LC_MESSAGES/*_qt.qm
rm -rf %buildroot/%_K5i18n/*/LC_MESSAGES/*_qt.qm
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%config(noreplace) %_K5xdgconf/marble.knsrc
%_K5cfg/marble.kcfg
%_K5xdgmime/geo-kde5.xml

%files
%_K5lib/libmarbledeclarative.so
%_K5bin/marble
#%_K5bin/marble-qt
%_K5plug/*marble*.so
%_K5data/marble/
%_K5data/plasma/*/org.kde.plasma.*world*/
%_K5lib/marble/
%_K5qml/org/kde/marble/
%_K5srv/*marble*.desktop
%_K5srv/*world*.desktop
%_K5xdgapp/*marble*.desktop
%_K5icon/*/*/apps/marble.*
%_iconsdir/*/*/apps/marble.*
%_K5xmlgui/marble/

%files devel
#%_K5plug/designer/lib*.so
#%_K5inc/marble_version.h
#%_K5inc/astro/
%_K5inc/marble/
%_K5link/lib*.so
%_K5lib/cmake/Marble/
%_K5archdata/mkspecs/modules/qt_Marble.pri

%files -n %libmarblewidget
%_K5lib/libmarblewidget-qt5.so.%marblewidget_sover
%_K5lib/libmarblewidget-qt5.so.*

%changelog
* Thu Aug 29 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Fri Jul 19 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Wed May 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Thu Mar 21 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Thu Feb 28 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt2
- build with qtwebengine

* Thu Feb 28 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Thu Jul 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Wed May 30 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt2%ubt
- build without qtwebkit

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Mon May 14 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 17.12.3-alt2%ubt
- NMU: rebuilt with new libshape.

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Thu Aug 31 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Thu Aug 31 2017 Oleg Solovyov <mcpain@altlinux.org> 17.04.2-alt2%ubt
- fix political map

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Wed Jun 07 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Mon Jun 05 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt2%ubt
- clean maps

* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Sep 22 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
