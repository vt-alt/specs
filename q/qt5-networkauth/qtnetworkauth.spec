%global qt_module qtnetworkauth

Name: qt5-networkauth
Version: 5.12.5
Release: alt1

Group: System/Libraries
Summary: Qt Network Authenticators
Url: http://qt.io/
License: GPLv3

Source: %qt_module-everywhere-src-%version.tar

BuildRequires: gcc-c++ glibc-devel
BuildRequires: qt5-base-devel qt5-tools

%description
Qt Network Authenticators; QtOAuth in particular.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt5-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt5-base-devel rpm-build-qml
%description devel
%summary.

%package doc
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-networkauth
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
%description -n libqt5-networkauth
%summary

%prep
%setup -n %qt_module-everywhere-src-%version

%build
%qmake_qt5
%make_build
%make docs

%install
%install_qt5
%make INSTALL_ROOT=%buildroot install_docs ||:

%files common

%files -n libqt5-networkauth
%_qt5_libdir/libQt5NetworkAuth.so.*
#%_qt5_plugindir/networkauth/
#%_qt5_qmldir/QtNetworkAuth/

%files devel
%_qt5_libdir/libQt*.so
%_qt5_libdatadir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_libdatadir/libQt*.prl
%_qt5_headerdir/Qt*/
%_qt5_archdatadir/mkspecs/modules/*.pr*
%_libdir/cmake/Qt*/
%_pkgconfigdir/Qt?NetworkAuth.pc

%files doc
%_qt5_docdir/*
%_qt5_examplesdir/*

%changelog
* Mon Oct 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1
- new version

* Mon Jun 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1
- new version

* Thu Apr 25 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version

* Thu Mar 14 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Thu Jan 31 2019 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- initial build
