%define rname kiten

%define soname 5
%define libkiten libkiten%soname

Name: kde5-%rname
Version: 19.04.3
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: Japanese reference/learning tool
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
# Automatically added by buildreq on Tue Jun 09 2020 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 gtk-update-icon-cache kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libdbusmenu-qt52 libglvnd-devel libgpg-error libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-texttospeech libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms python-modules python2-base python3 python3-base python3-dev qt5-base-devel rpm-build-python3 sh4 xml-common xml-utils
#BuildRequires: appstream extra-cmake-modules kf5-karchive-devel kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-khtml-devel kf5-kio-devel kf5-kjs-devel kf5-knotifications-devel kf5-kparts-devel kf5-ktextwidgets-devel libssl-devel python3-module-mpl_toolkits qt5-wayland-devel
BuildRequires: extra-cmake-modules qt5-base-devel qt5-wayland-devel
BuildRequires: kf5-karchive-devel kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-khtml-devel
BuildRequires: kf5-kio-devel kf5-kjs-devel kf5-knotifications-devel kf5-kparts-devel kf5-ktextwidgets-devel

%description
Kiten is a Japanese reference/learning tool with features:
    * Search with english keyword, Japanese reading, or a Kanji string on a list of EDICT files.
    * Search with english keyword, Japanese reading, number of strokes, grade number, or a Kanji on a list of KANJIDIC files.
    * Comes with all necessary files.
    * Very fast.
    * Limit searches to only common entries.
    * Nested searches of results possible.
    * Compact, small, fast interface.
    * Global KDE keybindings for searching highlighted strings.
    * Learning dialog. (One can even open up multiple ones and have them sync between each other.)
    * Browse Kanji by grade.
    * Add Kanji to a list for later learning.
    * Browse list, and get quizzed on them.

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

%package -n %libkiten
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkiten
%name library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%K5install_move data kiten
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files
%_K5bin/kiten*
%_K5data/kiten/
%_K5icon/*/*/apps/kiten.*
%_K5xdgapp/org.kde.kiten*.desktop
%_K5xmlgui/kiten*
%_K5cfg/kiten*

%files devel
#%_K5inc/kiten_version.h
%_K5inc/libkiten/
%_K5link/lib*.so
#%_K5lib/cmake/kiten
#%_K5archdata/mkspecs/modules/qt_kiten.pri

%files -n %libkiten
%_K5lib/libkiten.so.%soname
%_K5lib/libkiten.so.*

%changelog
* Tue Jun 09 2020 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- initial build
