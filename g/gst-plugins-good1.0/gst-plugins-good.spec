%define _name gst-plugins
%define ver_major 1.16
%define api_ver 1.0

%define _gst_datadir %_datadir/gstreamer-%api_ver
%define _gst_libdir %_libdir/gstreamer-%api_ver
%define _gtk_docdir %_datadir/gtk-doc/html

%def_enable jack
%def_enable pulse
%def_enable qt5

%def_disable gtk_doc
%def_disable debug
%def_disable examples
%ifarch %ix86 x86_64 aarch64
%def_enable valgrind
%endif
%def_disable check

Name: %_name-good%api_ver
Version: %ver_major.1
Release: alt1

Summary: A set of GStreamer plugins considered good
Group: System/Libraries
License: LGPL
Url: http://gstreamer.freedesktop.org/

Source: http://gstreamer.freedesktop.org/src/%_name-good/%_name-good-%version.tar.xz

Provides: %_name-good = %version-%release

BuildRequires(pre): meson
BuildRequires: bzlib-devel gcc-c++ gst-plugins%api_ver-devel >= %version
BuildRequires: gtk-doc libSM-devel libXdamage-devel libXext-devel libXfixes-devel
BuildRequires: libXv-devel libavc1394-devel libcairo-devel libdv-devel libflac-devel libiec61883-devel libjpeg-devel
BuildRequires: libshout2-devel libsoup-devel libtag-devel libv4l-devel libwavpack-devel
BuildRequires: python-module-PyXML python-modules-email python-modules-encodings python-modules-distutils
BuildRequires: liborc-devel orc libgdk-pixbuf-devel
BuildRequires: libpng-devel libcairo-gobject-devel libgudev-devel libspeex-devel zlib-devel libvpx-devel
BuildRequires: libmpg123-devel liblame-devel
BuildRequires: libgtk+3-devel
BuildRequires: liborc-test-devel
%{?_enable_valgrind:BuildRequires: valgrind-tool-devel}
%{?_enable_jack:BuildRequires: libjack-devel}
%{?_enable_pulse:BuildRequires: libpulseaudio-devel}
%{?_enable_qt5:BuildRequires: qt5-base-devel qt5-declarative-devel qt5-x11extras-devel qt5-wayland-devel}
%{?_enable_check:BuildRequires: /proc gstreamer%api_ver}

%description
GStreamer Good Plug-ins is is a set of plug-ins that the developers consider
to have good quality code, correct functionality, and their preferred license
(LGPL for the plug-in code, LGPL or LGPL-compatible for the supporting
library).

%package qt5
Summary: Qt5 plugin for GStreamer
Group: System/Libraries
Requires: gst-plugins-base%api_ver >= %version

%description qt5
This package contains Qt5 GL plugin for Gstreamer.


%package devel-doc
Summary: Development documentation for GStreamer Good plugins
Group: Development/Documentation
BuildArch: noarch
Provides: %_name-good-devel-doc = %version-%release

%description devel-doc
This package contains development documentation for GStreamer Good Plugins

%prep
%setup -n %_name-good-%version

%build
%meson \
	-Dexamples=disabled \
	%{?_enable_check:-Dtests=enabled} \
	%{?_disable_gtk_doc:-Dgtk_doc=disabled} \
	%{?_enable_debug:-Dgst_debug=true}

%meson_build

%install
%meson_install
%find_lang %_name-good-%api_ver

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files -f %_name-good-%api_ver.lang
%_gst_libdir/*.so
%{?_enable_qt5:%exclude %_gst_libdir/libgstqmlgl.so}
%_gst_datadir/*
%doc AUTHORS NEWS README RELEASE

%if_enabled qt5
%files qt5
%_gst_libdir/libgstqmlgl.so
%endif

%if_enabled gtk_doc
%files devel-doc
%_gtk_docdir/*
%endif

%changelog
* Tue Sep 24 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Sat Apr 20 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1.1
- mike@: disable BR: valgrind-tool-devel on non-primary arches (rather missing)

* Fri Apr 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Fri Apr 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.90-alt1
- 1.15.90

* Tue Mar 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.2-alt2
- new -qt5 subpackage (ALT #36313)

* Thu Feb 28 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.2-alt1
- 1.15.2

* Tue Feb 26 2019 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt2
- rebuild against libvpx.so.6

* Fri Oct 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt1
- 1.14.4

* Mon Sep 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.3-alt1
- 1.14.3

* Fri Jul 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt1
- 1.14.2

* Tue Jun 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt2
- rebuild against libvpx.so.5

* Thu May 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1

* Tue Mar 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1.13.91-alt1
- 1.13.91

* Thu Dec 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.4-alt1
- 1.12.4

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- 1.12.3

* Thu Aug 03 2017 Michael Shigorin <mike@altlinux.org> 1.12.2-alt2
- BOOTSTRAP: introduce jack, pulse knobs (on by default)

* Fri Jul 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- 1.12.2

* Tue Jun 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1

* Thu May 04 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Thu Feb 23 2017 Yuri N. Sedunov <aris@altlinux.org> 1.10.4-alt1
- 1.10.4

* Mon Jan 30 2017 Yuri N. Sedunov <aris@altlinux.org> 1.10.3-alt1
- 1.10.3

* Tue Nov 29 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.2-alt1
- 1.10.2

* Thu Nov 17 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.1-alt1
- 1.10.1

* Tue Nov 01 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Fri Aug 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt1
- 1.8.3

* Thu Jun 09 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Wed Apr 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Sat Mar 12 2016 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt2
- rebuilt against libvpx.so.3

* Mon Jan 25 2016 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Fri Oct 30 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Sat Sep 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sat Sep 19 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.91-alt1
- 1.5.91

* Thu Aug 20 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.90-alt1
- 1.5.90

* Thu Jun 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Mon Jun 08 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Sun Dec 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.5-alt1
- 1.4.5

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.4-alt1
- 1.4.4

* Wed Sep 24 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Fri Sep 19 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Thu Aug 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Jul 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Sun Apr 20 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4

* Mon Feb 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Sun Dec 29 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Wed Nov 13 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Fri Aug 30 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.10-alt1
- 1.0.10

* Fri Jul 12 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.8-alt1
- 1.0.8

* Sat Apr 27 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1
- 1.0.7

* Fri Mar 22 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Tue Jan 08 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5

* Sat Nov 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt2
- 1.0.3

* Tue Nov 06 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt2
- built lost vp8 plugins

* Thu Oct 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sun Oct 07 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Sep 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11.99-alt1
- 0.11.99

* Fri Sep 14 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11.94-alt1
- first build for Sisyphus

