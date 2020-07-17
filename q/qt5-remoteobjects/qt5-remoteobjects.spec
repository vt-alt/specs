%define qdoc_found %{expand:%%(if [ -e %_qt5_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtremoteobjects

Name:    qt5-remoteobjects
Summary: Qt5 - Qt Remote Objects
Group: System/Libraries
Version: 5.12.9
Release: alt1

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPLv2 with exceptions or GPLv3 with exceptions
Url:     http://www.qt.io

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt5 qt5-tools
BuildRequires: qt5-base-devel >= %version
BuildRequires: qt5-declarative-devel

%description
Qt Remote Objects (QtRO) is an inter-process communication (IPC)
module developed for Qt.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: qt5-base-common
BuildArch: noarch
%description common
Common package for %name

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name = %EVR
Requires: qt5-base-devel

%description devel
%summary.

%package doc
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-remoteobjects
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
%description -n libqt5-remoteobjects
%summary

%prep
%setup -n %qt_module-everywhere-src-%version

%build
%qmake_qt5
%make_build
%if %qdoc_found
%make docs
%endif

%install
%install_qt5
%if %qdoc_found
%make INSTALL_ROOT=%buildroot install_docs ||:
%endif

# remove libtool files
rm -fr %buildroot%_qt5_libdir/*.la


%files common

%files
%doc LICENSE.*
%_qt5_bindir/repc
%_bindir/repc-qt5
## split out? -- rex
%_qt5_qmldir/QtQml/RemoteObjects/
%_qt5_qmldir/QtRemoteObjects/

%files -n libqt5-remoteobjects
%_qt5_libdir/libQt5RemoteObjects.so.*

%files devel
%_qt5_headerdir/QtRemoteObjects/
%_qt5_headerdir/QtRepParser/
%_qt5_libdir/libQt?R*.prl
%_qt5_libdatadir/libQt?R*.prl
%_qt5_libdir/cmake/Qt5RemoteObjects/
%_qt5_libdir/cmake/Qt5RepParser/
%_qt5_libdir/pkgconfig/Qt?R*.pc
%_qt5_archdatadir/mkspecs/features/*.pr*
%_qt5_archdatadir/mkspecs/modules/qt_lib_r*.pr*
%_qt5_libdir/libQt*.so
%_qt5_libdatadir/libQt*.so

%files doc
%if %qdoc_found
%_qt5_docdir/*
%endif
%_qt5_examplesdir/*

%changelog
* Mon Jun 22 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.9-alt1
- new version

* Thu Apr 09 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt1
- new version

* Tue Mar 24 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version

* Sun Aug 25 2019 Anton Midyukov <antohami@altlinux.org> 5.12.4-alt1
- Initial build for ALT
