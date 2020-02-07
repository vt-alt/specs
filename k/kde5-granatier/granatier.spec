%define rname granatier

Name: kde5-%rname
Version: 19.12.1
Release: alt1
%K5init

Group: Games/Arcade
Summary: Bomberman game
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Jun 28 2019 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 gtk-update-icon-cache kf5-attica-devel kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kwidgetsaddons-devel libGL-devel libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-svg libqt5-texttospeech libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel rpm-build-python3 sh4 xml-common xml-utils
#BuildRequires: appstream extra-cmake-modules kde5-libkdegames-devel kf5-kcompletion-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-ki18n-devel kf5-knewstuff-devel kf5-kservice-devel kf5-kxmlgui-devel libssl-devel python3-dev qt5-svg-devel qt5-wayland-devel
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-svg-devel qt5-wayland-devel
BuildRequires: kde5-libkdegames-devel
BuildRequires: libssl-devel
BuildRequires: kf5-kcompletion-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdoctools-devel kf5-ki18n-devel kf5-knewstuff-devel
BuildRequires: kf5-kservice-devel kf5-kxmlgui-devel

%description
Bomberman game.

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

%package -n libkf5granatier
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n libkf5granatier
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data granatier
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/granatier
%_K5data/granatier
%_K5xdgapp/*granatier*.desktop
%_K5xmlgui/granatier/
%_K5cfg/granatier.kcfg
%_K5icon/hicolor/*/apps/granatier.*
%_datadir/qlogging-categories5/*.*categories

#%files devel
#%_K5inc/granatier_version.h
#%_K5inc/granatier/
#%_K5link/lib*.so
#%_K5lib/cmake/granatier
#%_K5archdata/mkspecs/modules/qt_granatier.pri

#%files -n libkf5granatier
#%_K5lib/libgranatier.so.*

%changelog
* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Fri Aug 30 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Mon Jul 01 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- initial build
