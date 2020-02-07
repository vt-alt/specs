%define rname kreversi

Name: kde5-%rname
Version: 19.12.1
Release: alt1
%K5init

Group: Games/Boards
Summary: Old reversi board game, also known as othello
Url: http://www.kde.org
License: GPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Mon Jul 01 2019 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 gtk-update-icon-cache kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libGL-devel libglvnd-devel libgpg-error libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-svg libqt5-test libqt5-texttospeech libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel rpm-build-python3 rpm-build-qml sh4 xml-common xml-utils
#BuildRequires: appstream extra-cmake-modules kde5-libkdegames-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kpackage-devel libssl-devel python3-dev qt5-svg-devel qt5-wayland-devel rpm-build-gir
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel qt5-svg-devel qt5-wayland-devel
BuildRequires: kde5-libkdegames-devel
BuildRequires: kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdelibs4support
BuildRequires: kf5-kdoctools-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kpackage-devel

%description
KReversi is a simple one player strategy game played against the computer.
If a player's piece is captured by an opposing player, that piece is turned over
to reveal the color of that player. A winner is declared when one player has more
pieces of his own color on the board and there are no more possible moves.

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

%package -n libkf5reversi
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n libkf5reversi
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data kreversi
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/kreversi
%_K5data/kreversi/
%_K5icon/hicolor/*/apps/*kreversi*.*
%_K5icon/hicolor/*/actions/*moves*.*
%_K5xdgapp/*kreversi*.desktop
%_K5notif/*kreversi*

%changelog
* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Fri Aug 30 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Mon Jul 01 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- initial build

