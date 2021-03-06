%define rname qmlkonsole

Name: kde5-%rname
Version: 21.06
Release: alt2
%K5init

Group: Graphical desktop/KDE
Summary: Mobile terminal application
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: qt5-qmltermwidget
Conflicts: cool-retro-term <= 1.0.1-alt1

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Jun 11 2021 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-svg libqt5-test libqt5-widgets libqt5-xml libsasl2-3 libssl-devel libstdc++-devel python-modules python2-base python3 python3-base python3-module-paste qt5-base-common qt5-base-devel qt5-declarative-devel rpm-build-python3 sh4 tzdata
#BuildRequires: appstream extra-cmake-modules kf5-kconfig-devel kf5-ki18n-devel kf5-kirigami-devel python3-dev python3-module-mpl_toolkits qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires: kf5-kconfig-devel kf5-ki18n-devel kf5-kirigami-devel

%description
Terminal application offering additional keyboard buttons useful on touch devices.

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

%package -n libkf5qmlkonsole
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkf5qmlkonsole
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/qmlkonsole
%_K5xdgapp/*qmlkonsole*.desktop
%_K5cfg/*terminalsettings*

#%files devel
#%_K5inc/qmlkonsole_version.h
#%_K5inc/qmlkonsole/
#%_K5link/lib*.so
#%_K5lib/cmake/qmlkonsole
#%_K5archdata/mkspecs/modules/qt_qmlkonsole.pri

#%files -n libkf5qmlkonsole
#%_K5lib/libqmlkonsole.so.*

%changelog
* Tue Jun 15 2021 Sergey V Turchin <zerg@altlinux.org> 21.06-alt2
- add conflict with cool-retro-term

* Fri Jun 11 2021 Sergey V Turchin <zerg@altlinux.org> 21.06-alt1
- initial build
