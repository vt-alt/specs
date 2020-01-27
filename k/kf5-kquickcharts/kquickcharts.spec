%define rname kquickcharts

Name: kf5-%rname
Version: 5.66.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: High-performance charts QtQuick module
Url: http://www.kde.org
License: LGPL-2.1-or-later

#Requires: qml(org.kde.kirigami) >= 2.4

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Dec 18 2019 (-bi)
# optimized out: cmake cmake-modules elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libglvnd-devel libqt5-core libqt5-gui libqt5-network libqt5-qml libqt5-quick libqt5-quickcontrols2 libqt5-quicktemplates2 libsasl2-3 libstdc++-devel perl python-modules python2-base python3 python3-base python3-dev qt5-base-devel qt5-declarative-devel rpm-build-python3 rpm-build-qml sh4
#BuildRequires: appstream ccmake extra-cmake-modules git-core libssl-devel python-modules-compiler python3-module-mpl_toolkits qt5-quickcontrols2-devel qt5-wayland-devel rpm-build-kf5
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel qt5-quickcontrols2-devel
#BuildRequires: qt5-wayland-devel

%description
A QtQuick module providing high-performance charts.
The Quick Charts module provides a set of charts that can be used from QtQuick
applications. They are intended to be used for both simple display of data as
well as continuous display of high-volume data (often referred to as plotters).
The charts use a system called distance fields for their accelerated rendering,
which provides ways of using the GPU for rendering 2D shapes without loss of
quality.

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
Requires: %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5quickcharts
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n libkf5quickcharts
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --all-name
%K5find_qtlang %name --all-name

%files -f %name.lang
%doc COPYING* README.md
%_K5qml/org/kde/quickcharts/

%files devel
%_K5lib/cmake/KF5QuickCharts/

#%files -n libkf5quickcharts
#%_K5lib/libkquickcharts.so.*

%changelog
* Mon Jan 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.66.0-alt1
- new version

* Wed Dec 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.65.0-alt1
- initial build
