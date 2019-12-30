%define qdoc_found %{expand:%%(if [ -e %_qt5_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtwayland

Name: qt5-wayland
Version: 5.12.6
Release: alt1

Group: System/Libraries
Summary: Qt5 - Wayland platform support and QtCompositor module
Url: http://qt.io/
License: LGPLv2 / GPLv3

Source: %qt_module-everywhere-src-%version.tar

# Automatically added by buildreq on Thu Jul 17 2014 (-bi)
# optimized out: elfutils fontconfig glibc-devel-static libGL-devel libX11-devel libXfixes-devel libcloog-isl4 libfreetype-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-quick libstdc++-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-egl libwayland-server pkg-config python-base qt5-base-devel qt5-declarative-devel qt5-script-devel ruby ruby-stdlibs wayland-devel xorg-compositeproto-devel xorg-fixesproto-devel xorg-xproto-devel
#BuildRequires: fontconfig-devel gcc-c++ git-core glib2-devel libEGL-devel libXcomposite-devel libXext-devel libXrender-devel libudev-devel libwayland-cursor-devel libwayland-egl-devel libwayland-server-devel libxkbcommon-devel python-module-protobuf qt5-base-devel-static qt5-phonon-devel qt5-quick1-devel qt5-tools-devel qt5-webkit-devel qt5-xmlpatterns-devel rpm-build-ruby
BuildRequires(pre): rpm-build-ubt rpm-macros-qt5 qt5-tools
BuildRequires: fontconfig-devel gcc-c++ zlib-devel glib2-devel libEGL-devel libGLES-devel libXcomposite-devel libXext-devel libXrender-devel
BuildRequires: libinput-devel libts-devel libmtdev-devel
BuildRequires: libudev-devel libxkbcommon-devel
BuildRequires: libwayland-client-devel libwayland-cursor-devel libwayland-egl-devel libwayland-server-devel
BuildRequires: qt5-base-devel-static qt5-declarative-devel qt5-tools-devel

%description
%summary.

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
Requires: qt5-base-devel
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: %name-devel
%description devel-static
%summary.

%package doc
BuildArch: noarch
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-compositor
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
%description -n libqt5-compositor
%summary

%package -n libqt5-waylandcompositor
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
%description -n libqt5-waylandcompositor
%summary

%package -n libqt5-waylandclient
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
%description -n libqt5-waylandclient
%summary

%prep
%setup -qn %qt_module-everywhere-src-%version
#for d in gl nogl; do
#mkdir $d
#done

%build
#qmake_qt5 CONFIG+=wayland-compositor
%qmake_qt5 QT_BUILD_PARTS-=examples

%make_build
%if %qdoc_found
export QT_HASH_SEED=0
%make docs
%endif

%install
%install_qt5
%if %qdoc_found
%make INSTALL_ROOT=%buildroot install_docs ||:
%endif

%files common
%doc LICENSE*EXCEPT*

%files
%_qt5_plugindir/platforms/*
%_qt5_plugindir/wayland-decoration-client/
%_qt5_plugindir/wayland-graphics-integration-server/
%_qt5_plugindir/wayland-graphics-integration-client/
%_qt5_plugindir/wayland-shell-integration/
%_qt5_qmldir/QtWayland/Compositor/

#%files -n libqt5-compositor
#%_qt5_libdir/libQt?Compositor.so.*
%files -n libqt5-waylandcompositor
%_qt5_libdir/libQt?WaylandCompositor.so.*
%files -n libqt5-waylandclient
%_qt5_libdir/libQt?WaylandClient.so.*

%files devel
%doc LICENSE*EXCEPT*
%_qt5_bindir/qtwaylandscanner*
%_bindir/qtwaylandscanner*
%_qt5_headerdir/Qt*/
%_qt5_libdir/libQt*.so
%_qt5_libdatadir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_libdatadir/libQt*.prl
%_qt5_libdir/cmake/Qt*/
%_qt5_libdir/pkgconfig/Qt*.pc
%_qt5_archdatadir/mkspecs/modules/*.pri

%files doc
%if %qdoc_found
%_qt5_docdir/*
%endif

%changelog
* Mon Dec 16 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1
- new version

* Mon Oct 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1
- new version

* Mon Jun 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1
- new version

* Thu Apr 25 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version

* Mon Mar 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Mon Feb 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt2
- fix to build

* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Mon Sep 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Fri Aug 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt1%ubt
- new version

* Wed Jun 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.6-alt1%ubt
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt2%ubt
- rebuild with new libwayland-egl

* Tue Apr 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Thu Jan 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Tue Dec 05 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Fri Oct 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Thu Dec 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1%ubt
- new version

* Sun Oct 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt0.M80P.1
- build for M80P

* Wed Oct 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1
- new version

* Mon Jun 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Thu Mar 24 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Tue Jul 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Tue Jun 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Tue Dec 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Thu Jul 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- initial build
