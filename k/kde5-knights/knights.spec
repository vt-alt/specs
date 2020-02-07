%define rname knights

Name: kde5-%rname
Version: 19.12.1
Release: alt1
%K5init no_altplace

Group: Games/Boards
Summary: Chess board
Url: http://www.kde.org
License: GPLv2+

Provides: knights = %EVR
Obsoletes: knights < %EVR
Requires: gnuchess

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Jun 28 2019 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 gtk-update-icon-cache kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libGL-devel libdbusmenu-qt52 libglvnd-devel libgpg-error libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-sql libqt5-svg libqt5-texttospeech libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel rpm-build-python3 sh4 xml-common xml-utils
#BuildRequires: appstream extra-cmake-modules kde5-libkdegames-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-kio-devel kf5-kpackage-devel kf5-kplotting-devel kf5-ktextwidgets-devel kf5-kwallet-devel kf5-plasma-framework-devel libssl-devel python3-dev qt5-speech-devel qt5-svg-devel qt5-wayland-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel qt5-speech-devel qt5-svg-devel qt5-wayland-devel
#BuildRequires: appstream
BuildRequires: libssl-devel
BuildRequires: kde5-libkdegames-devel
BuildRequires: kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel
BuildRequires: kf5-kio-devel kf5-kpackage-devel kf5-kplotting-devel kf5-ktextwidgets-devel
BuildRequires: kf5-kwallet-devel kf5-plasma-framework-devel

%description
Knights supports local and Internet play against a human being or a computer engine.

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

%package -n libkf5nights
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n libkf5nights
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSE*
%config(noreplace) %_K5xdgconf/*.knsrc
%_K5bin/knights
%_datadir/knights/
%_K5icon/hicolor/*/apps/knights.*
%_K5cfg/knights.kcfg
%_K5xmlgui/knights/
%_K5xdgapp/*knights*.desktop
%_datadir/metainfo/*knights*.xml
%_datadir/qlogging-categories5/*.categories

#%files devel
#%_K5inc/knights_version.h
#%_K5inc/knights/
#%_K5link/lib*.so
#%_K5lib/cmake/knights
#%_K5archdata/mkspecs/modules/qt_knights.pri

#%files devel
#%_K5dbus_iface/*nights*.xml

%changelog
* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Fri Aug 30 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jun 27 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- initial build

