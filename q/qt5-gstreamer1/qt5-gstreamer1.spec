%def_disable quick1

Name:    qt5-gstreamer1
Version: 1.2.0
Release: alt8

Summary: C++ bindings for GStreamer with a Qt-style API
License: LGPLv2+
Group:   System/Libraries
URL:     http://gstreamer.freedesktop.org/modules/qt-gstreamer.html

Requires: gst-plugins-base1.0 gst-plugins-good1.0

Source: qt-gstreamer-%version.tar
# upstream
Patch4: 004-boost160.patch
# OpenBSD
Patch10: openbsd-qgst_caps.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: flex
BuildRequires: boost-devel
BuildRequires: gstreamer1.0-devel
BuildRequires: gst-plugins1.0-devel
BuildRequires: qt5-base-devel qt5-declarative-devel
%if_enabled quick1
BuildRequires: qt5-quick1-devel
%endif
BuildRequires: libGL-devel libGLES-devel
BuildRequires: doxygen kde-common-devel

%description
QtGStreamer provides C++ bindings for GStreamer with a Qt-style
API, plus some helper classes for integrating GStreamer better
in Qt applications.

%package -n libqt5-glib
Group:   System/Libraries
Summary: C++ bindings for Glib with a Qt-style API
Conflicts: qt5-gstreamer1 <= 1.2.0-alt4
%description -n libqt5-glib
QtGStreamer provides C++ bindings for GLib with a Qt-style API

%package devel
Summary:        Header files and development documentation for %name
Group:          Development/C++
Requires:       %name = %version-%release
Requires:       boost-devel
Requires:       gst-plugins1.0-devel
Requires:       qt5-base-devel qt5-declarative-devel
%description devel
This package contains the header files and development documentation
for %name.

%prep
%setup -qn qt-gstreamer-%version
%patch4 -p1
%patch10 -p0

%build
%Kbuild \
    -DQT_VERSION=5 \
    -DQTGSTREAMER_STATIC=OFF \
    -DQTGSTREAMER_TESTS=OFF \
    -DQTGSTREAMER_EXAMPLES=OFF \
    -DQTGSTREAMER_CODEGEN=OFF \
    -DUSE_GST_PLUGIN_DIR=ON \
    -DUSE_QT_PLUGIN_DIR=ON \
    #

%install
%Kinstall

%files
%doc COPYING README
%_libdir/gstreamer-1.0/libgst*.so
%_libdir/libQt5GStreamer-1.0.so.0
%_libdir/libQt5GStreamer-1.0.so.1*
%_libdir/libQt5GStreamerUi-1.0.so.0
%_libdir/libQt5GStreamerUi-1.0.so.1*
%_libdir/libQt5GStreamerUtils-1.0.so.0
%_libdir/libQt5GStreamerUtils-1.0.so.1*
%_libdir/libQt5GStreamerQuick-1.0.so.0
%_libdir/libQt5GStreamerQuick-1.0.so.1*
%if_enabled quick1
%_qt5_importdir/QtGStreamer/
%endif
%_qt5_archdatadir/qml/QtGStreamer/

%files -n libqt5-glib
%_libdir/libQt5GLib-2.0.so.0
%_libdir/libQt5GLib-2.0.so.1.*

%files devel
%doc HACKING
%_includedir/Qt5GStreamer
%_libdir/cmake/Qt5GStreamer
%_libdir/libQt5GLib-2.0.so
%_libdir/libQt5GStreamer-1.0.so
%_libdir/libQt5GStreamerUi-1.0.so
%_libdir/libQt5GStreamerUtils-1.0.so
%_libdir/libQt5GStreamerQuick-1.0.so
%_libdir/pkgconfig/Qt5GLib-*.pc
%_libdir/pkgconfig/Qt5GStreamer*.pc


%changelog
* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt8
- fix to build with new gstreamer

* Thu Mar 29 2018 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt7
- build without Quick1

* Thu Aug 24 2017 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt6
- fix build requires

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt5
- package Qt5Glib separately

* Thu Feb 04 2016 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt4
- apply upstream fixes

* Fri Oct 16 2015 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt3
- fix against ugly gstreamer includes placement

* Fri Sep 26 2014 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt2
- fix requires

* Thu Sep 04 2014 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt0.M70P.1
- build for M70P

* Tue Aug 26 2014 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt1
- new version

* Mon Jun 30 2014 Sergey V Turchin <zerg@altlinux.org> 1.1.90-alt0.M70P.1
- built for M70P

* Thu Jun 26 2014 Sergey V Turchin <zerg@altlinux.org> 1.1.90-alt1
- initial build
