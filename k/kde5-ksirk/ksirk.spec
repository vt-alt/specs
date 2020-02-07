%define rname ksirk

%define iris_ksirk_sover 0
%define libiris_ksirk libiris_ksirk%iris_ksirk_sover

Name: kde5-%rname
Version: 19.12.1
Release: alt1
%K5init

Group: Games/Strategy
Summary: World Domination Strategy Game
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: alt-libiris-so-version.patch

# Automatically added by buildreq on Thu Dec 21 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libEGL-devel libGL-devel libgpg-error libqca-qt5 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules qt5-base-common qt5-base-devel xml-common xml-utils
#BuildRequires: extra-cmake-modules gtk-update-icon-cache kde5-libkdegames-devel kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-knewstuff-devel kf5-kwallet-devel libqca-qt5-devel libssl-devel qt5-declarative-devel qt5-phonon-devel qt5-svg-devel zlib-devel
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-declarative-devel qt5-phonon-devel qt5-svg-devel
BuildRequires: libqca-qt5-devel libssl-devel zlib-devel
BuildRequires: kde5-libkdegames-devel
BuildRequires: kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-ki18n-devel kf5-kiconthemes-devel
BuildRequires: kf5-kio-devel kf5-knewstuff-devel kf5-kwallet-devel

%description
The goal of the game is simply to conquer the World... It is done by attacking your neighbors
with your armies.

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

%package -n %libiris_ksirk
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libiris_ksirk
%name library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%K5install_move data ksirk ksirkskineditor
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_datadir/qlogging-categories5/*.*categories

%files
%config(noreplace) %_K5xdgconf/*rc
%_K5bin/ksirk*
%_K5xdgapp/org.kde.ksirk*.desktop
%_K5data/ksirk/
%_K5data/ksirkskineditor/
%_K5xmlgui/ksirk/
%_K5xmlgui/ksirkskineditor/
%_K5icon/*/*/apps/ksirk.*
%_K5cfg/ksirk*.kcfg

%files -n %libiris_ksirk
%_K5lib/libiris_ksirk.so.%iris_ksirk_sover
%_K5lib/libiris_ksirk.so.*

%changelog
* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Fri Aug 30 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Wed May 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Fri Mar 22 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Thu Feb 28 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Fri Jul 27 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Mon May 28 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Thu Jan 18 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.1-alt1%ubt
- new version

* Mon Dec 25 2017 Sergey V Turchin <zerg@altlinux.org> 17.12.0-alt2%ubt
- fix conflict with KDE4 (ALT#34385)

* Wed Dec 20 2017 Sergey V Turchin <zerg@altlinux.org> 17.12.0-alt1%ubt
- initial build
