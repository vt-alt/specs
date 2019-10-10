%define _name gst-plugins
%define ver_major 1.16
%define api_ver 1.0

%define _gst_datadir %_datadir/gstreamer-%api_ver
%define _gst_libdir %_libdir/gstreamer-%api_ver
%define _gtk_docdir %_datadir/gtk-doc/html

%def_disable gtk_doc
%def_disable debug
%def_disable examples
%def_disable check

Name: %_name-ugly%api_ver
Version: %ver_major.1
Release: alt1

Summary: A set of encumbered GStreamer plugins
Group: System/Libraries
License: LGPL
Url: http://gstreamer.freedesktop.org/

Provides: %_name-ugly = %version-%release

Requires: gstreamer%api_ver >= %ver_major
Requires: lib%_name%api_ver >= %ver_major

Provides: %_name%api_ver-lame = %version-%release
Provides: %_name%api_ver-mad = %version-%release

Source: http://gstreamer.freedesktop.org/src/%_name-ugly/%_name-ugly-%version.tar.xz

BuildRequires(pre): meson
BuildRequires: gcc-c++ orc liborc-test-devel gst-plugins%api_ver-devel >= %version
BuildRequires: gtk-doc liba52-devel libcdio-devel libid3tag-devel
BuildRequires: libmad-devel libmpeg2-devel liboil-devel libx264-devel
BuildRequires: python-module-PyXML python-modules-encodings python-modules-distutils
BuildRequires: libopencore-amrnb-devel libopencore-amrwb-devel libdvdread-devel

%description
GStreamer Ugly Plug-ins is a set of plug-ins that have good quality
and correct functionality, but distributing them might pose problems.
The license on either the plug-ins or the supporting
libraries might not be how the developers would like.
The code might be widely known to present patent problems.

%package devel-doc
Summary: Development documentation for GStreamer Ugly plugins
Group: Development/Documentation
BuildArch: noarch
Provides: %_name-ugly-devel-doc = %version-%release

%description devel-doc
This package contains development documentation for GStreamer Ugly plugin
collection.

%prep
%setup -n %_name-ugly-%version

%build
%meson \
	-Dexamples=disabled \
	%{?_enable_check:-Dtests=enabled} \
	%{?_disable_gtk_doc:-Dgtk_doc=disabled} \
	%{?_enable_debug:-Dgst_debug=true}

%meson_build

%install
%meson_install
%find_lang %_name-ugly-%api_ver

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files -f %_name-ugly-%api_ver.lang
%doc AUTHORS NEWS README RELEASE
%_gst_libdir/*.so
%_datadir/gstreamer-%api_ver/*

%if_enabled gtk_doc
%files devel-doc
%_gtk_docdir/%_name-ugly-plugins-%api_ver/*
%endif

%changelog
* Tue Sep 24 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Fri Apr 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Fri Apr 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.90-alt1
- 1.15.90

* Mon Mar 04 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.2-alt1
- 1.15.2

* Fri Oct 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt1
- 1.14.4

* Mon Sep 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.3-alt1
- 1.14.3

* Fri Jul 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt1
- 1.14.2

* Thu May 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1

* Tue Mar 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1.13.91-alt1
- 1.13.91

* Fri Jan 12 2018 Yuri N. Sedunov <aris@altlinux.org> 1.12.4-alt2
- rebuilt against libcdio.so.18

* Thu Dec 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.4-alt1
- 1.12.4

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- 1.12.3

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
- rebuilt against libx264.so.148

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

* Mon Jul 20 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt2
- rebuilt against libcdio.so.16

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

* Tue May 13 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.4-alt2
- rebuilt with recent x264, again

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

* Wed Sep 11 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.10-alt2
- rebuilt with recent x264

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

* Sat Nov 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Thu Oct 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sun Oct 14 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- first build for Sisyphus

