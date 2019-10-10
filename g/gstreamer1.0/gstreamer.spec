%define _name gstreamer
%define ver_major 1.16
%define api_ver 1.0
%define _libexecdir %_prefix/libexec
%define api_ver 1.0

%def_enable gtk_doc
%def_disable debug
%def_disable libunwind
%def_disable libdw
%def_disable check

Name: %_name%api_ver
Version: %ver_major.1
Release: alt1

Summary: GStreamer streaming media framework runtime
License: LGPL
Group: System/Libraries
Url: http://gstreamer.freedesktop.org

Source: http://gstreamer.freedesktop.org/src/%_name/%_name-%version.tar.xz

Provides: %_name = %version-%release

Requires(pre): libcap-utils
Requires: lib%name = %version-%release

%define glib_ver 2.40.0

BuildRequires(pre): meson rpm-build-gir
BuildRequires: glib2-devel >= %glib_ver
BuildRequires: flex gcc-c++ ghostscript-utils gtk-doc libcheck-devel libxml2-devel
BuildRequires: python-modules sgml-common transfig xml-utils gobject-introspection-devel
BuildRequires: libcap-devel libcap-utils
BuildRequires: bash-completion
%{?_enable_libunwind:BuildRequires: libunwind-devel}
%{?_enable_libdw:BuildRequires: libdw-devel}

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

%package -n lib%name
Summary: Shared libraries of GStreamer
Group: System/Libraries
Provides: lib%_name = %version-%release

%description -n lib%name
This package contains the shared libraries of the GStreamer media framework

%package -n lib%name-gir
Summary: GObject introspection data for the GStreamer library
Group: System/Libraries
Provides: lib%_name-gir = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the GStreamer library

%package devel
Summary: Development files for GStreamer streaming-media framework
Group: Development/C
Provides: %_name-devel = %version-%release
Requires: lib%name = %version-%release

%description devel
This package contains the libraries and header files necessary to
develop applications and plugins for GStreamer

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the GStreamer library
Group: System/Libraries
BuildArch: noarch
Provides: lib%_name-gir-devel = %version-%release
Requires: lib%name-gir = %version-%release %name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the GStreamer library

%package devel-doc
Summary: Development documentation for GStreamer
Group: Development/C
BuildArch: noarch
Provides: %_name-devel-doc = %version-%release

%description devel-doc
This package contains development documentation for GStreamer

%package utils
Summary: GStreamer utilities
Group: System/Libraries
Provides: %_name-utils = %version-%release
Requires: lib%name = %version-%release

%description utils
This package contains some utilities used to register, analyze, and run
Gstreamer plugins.

%prep
%setup -n %_name-%version

%build
%ifarch e2k
# till lcc ~1.23
export LIBS=-lcxa
%endif
%meson \
	-Dpackage-name="GStreamer" \
	-Dpackage-origin=%name \
	-Dexamples=disabled \
	%{?_enable_check:-Dtests=enabled} \
	%{?_disable_gtk_doc:-Dgtk_doc=disabled} \
	%{?_enable_debug:-Dgst_debug=true} \
	-Dptp-helper-permissions="capabilities"
%meson_build

%install
%meson_install
%find_lang %_name-%api_ver

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%post
setcap cap_net_bind_service,cap_net_admin+ep %_libexecdir/%_name-%api_ver/gst-ptp-helper 2>/dev/null ||:

%files -f %_name-%api_ver.lang
%dir %_libexecdir/%_name-%api_ver
%_libexecdir/%_name-%api_ver/gst-plugin-scanner
%_libexecdir/%_name-%api_ver/gst-ptp-helper
%dir %_libdir/%_name-%api_ver
%_libdir/%_name-%api_ver/*.so
%doc AUTHORS NEWS README RELEASE

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-gir
%_typelibdir/Gst-%api_ver.typelib
%_typelibdir/GstBase-%api_ver.typelib
%_typelibdir/GstCheck-%api_ver.typelib
%_typelibdir/GstController-%api_ver.typelib
%_typelibdir/GstNet-%api_ver.typelib

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/aclocal/*
%if_enabled debug
%_datadir/gdb/auto-load/%_libdir/lib%name-%api_ver.so.*-gdb.py
%_datadir/glib-2.0/gdb/glib_gobject_helper.py
%_datadir/glib-2.0/gdb/gst_gdb.py
%endif

%files -n lib%name-gir-devel
%_girdir/Gst-%api_ver.gir
%_girdir/GstBase-%api_ver.gir
%_girdir/GstCheck-%api_ver.gir
%_girdir/GstController-%api_ver.gir
%_girdir/GstNet-%api_ver.gir

%files devel-doc
%_datadir/gtk-doc/html/*

%files utils
%_bindir/*
%_man1dir/*
# bash-completions
%_libexecdir/%_name-%api_ver/gst-completion-helper
%_datadir/bash-completion/completions/gst-inspect-%api_ver
%_datadir/bash-completion/completions/gst-launch-%api_ver
%_datadir/bash-completion/helpers/gst

%changelog
* Tue Sep 24 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Fri Apr 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Fri Apr 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.90-alt1
- 1.15.90

* Wed Feb 27 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.2-alt1
- 1.15.2

* Fri Oct 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt1
- 1.14.4

* Tue Sep 18 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.3-alt2
- packaged bash-completions

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

* Thu Dec 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.4-alt1
- 1.12.4

* Wed Sep 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt2
- rebuilt --with-ptp-helper-permissions=capabilities (ALT #33909)

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- 1.12.3
- mike@:
  E2K:
  initial architecture support
  force linking against -lcxa

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

* Sat Nov 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

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

