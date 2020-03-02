%define rname elisa

%define sover 0
%define libelisalib libelisalib%sover

Name: kde5-%rname
Version: 19.12.2
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: Music player
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: kf5-kirigami

Source: %rname-%version.tar
Patch1: alt-install.patch

# Automatically added by buildreq on Fri Feb 28 2020 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 gtk-update-icon-cache kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libglvnd-devel libgpg-error libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickcontrols2 libqt5-quicktemplates2 libqt5-quicktest libqt5-quickwidgets libqt5-sql libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms perl python-modules python2-base python3 python3-base qt5-base-devel qt5-declarative-devel rpm-build-python3 rpm-build-qml sh4 xml-common xml-utils
#BuildRequires: appstream extra-cmake-modules kf5-kcmutils-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdoctools-devel kf5-kfilemetadata-devel kf5-ki18n-devel kf5-kio-devel kf5-kirigami-devel kf5-kpackage-devel libssl-devel python-modules-compiler python3-dev qt5-multimedia-devel qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: qt5-declarative-devel qt5-multimedia-devel qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel
BuildRequires: kf5-kcmutils-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel
BuildRequires: kf5-kdoctools-devel kf5-kfilemetadata-devel kf5-ki18n-devel kf5-kio-devel
BuildRequires: kf5-kirigami-devel kf5-kpackage-devel


%description
Elisa is a simple music player aiming to provide a nice experience for its users.
You can build and play your own playlist.

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

%package -n %libelisalib
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libelisalib
%name library

%prep
%setup -n %rname-%version
%patch1 -p1
sed -i '/find_package.*LIBVLC/s|LIBVLC|LIBVLC_disabled|' CMakeLists.txt
sed -i '/find_package.*KF5Baloo/s|KF5Baloo|KF5Baloo_disabled|' CMakeLists.txt
sed -i '/find_package.*UPNPQT/s|UPNPQT|UPNPQT_disabled|' CMakeLists.txt

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files
%_K5bin/elisa
%_K5qml/org/kde/elisa/
%_K5xdgapp/*elisa*.desktop
%_K5icon/*/*/apps/elisa.*
%_datadir/qlogging-categories5/*elisa*.*categories

#%files devel
#%_K5inc/elisa_version.h
#%_K5inc/elisa/
#%_K5link/lib*.so
#%_K5lib/cmake/elisa
#%_K5archdata/mkspecs/modules/qt_elisa.pri

%files -n %libelisalib
%_K5lib/libelisaLib.so.%sover
%_K5lib/libelisaLib.so.*

%changelog
* Fri Feb 28 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt1
- initial build
