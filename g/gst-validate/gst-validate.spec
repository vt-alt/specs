%define _name gstvalidate
%define ver_major 1.16
%define gst_api_ver 1.0
%define api_ver 1.0

%def_enable python3

Name: gst-validate
Version: %ver_major.1
Release: alt1

Summary: GStreamer Validate Tools and Library
Group: System/Libraries
License: GPLv2+ and LGPLv2+
Url: http://cgit.freedesktop.org/gstreamer/gst-devtools/

Source: http://gstreamer.freedesktop.org/src/%name/%name-%version.tar.xz

%define gst_ver %version

Requires: lib%name = %version-%release
Requires: gst-plugins-base%gst_api_ver

%if_enabled python3
# use python3
AutoReqProv: nopython
%define __python %nil
%add_python3_path %_libdir/%name-launcher/python
%endif

BuildRequires(pre): rpm-build-gir
BuildRequires: gcc-c++ gst-plugins%gst_api_ver-devel >= %gst_ver gst-plugins-base%gst_api_ver libxml2-devel
BuildRequires: libcairo-devel gobject-introspection-devel gst-plugins%gst_api_ver-gir-devel
BuildRequires: libjson-glib-devel
BuildRequires: gtk-doc
%if_enabled python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%description
The goal of GstValidate is to be able to detect when elements are not
behaving as expected and report it to the user so he knows how things are
supposed to work inside a GstPipeline. In the end, fixing issues found by
the tool will ensure that all elements behave all together in the
expected way.

%package -n lib%name
Summary: GStreamer Validate library
License: LGPLv2+
Group: System/Libraries

%description -n lib%name
GStreamer Validate library.

%package -n lib%name-devel
Summary: Development files for %name
License: LGPLv2+
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides libraries and header files for developing
applications that use Gst Validate library.

%package -n lib%name-devel-doc
Summary: Gst Validate development documentation
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name-devel < %version

%description -n lib%name-devel-doc
This package contains documentation necessary to develop applications
that use Gst Validate library.

%package -n lib%name-gir
Summary: GObject introspection data for the Gst Validate
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Gst Validate library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Gst Validate
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Gst Validate library.


%prep
%setup

%build
%autoreconf
%configure --enable-gtk-doc \
	--disable-sphinx-doc \
	%{?_enable_python3:PYTHON=%__python3}

%make_build

%install
%makeinstall_std

%find_lang %name

%files
%_bindir/%name-launcher
%_bindir/gst-validate-%api_ver
%_bindir/gst-validate-media-check-%api_ver
%_bindir/gst-validate-transcoding-%api_ver
%_bindir/%name-images-check-%api_ver
%_libdir/%name-launcher/
%_libdir/gstreamer-%gst_api_ver/lib%{_name}tracer.so
%_datadir/gstreamer-%gst_api_ver/validate/

%exclude %_libdir/gstreamer-%gst_api_ver/*.la

%files -n lib%name -f %name.lang
%_libdir/lib%_name-%api_ver.so.*
#%_libdir/lib%{_name}_preload-%api_ver.so.*
%_libdir/lib%_name-default-overrides-%api_ver.so.*
%_libdir/lib%{_name}video-%api_ver.so.*
%dir %_libdir/gstreamer-%gst_api_ver/validate/
%_libdir/gstreamer-%gst_api_ver/validate/*.so
%exclude %_libdir/gstreamer-%gst_api_ver/validate/*.la
%doc ChangeLog README

%files -n lib%name-devel
%_includedir/gstreamer-%gst_api_ver/gst/validate/
%_includedir/gstreamer-%gst_api_ver/lib/validate/
%_libdir/lib%_name-%api_ver.so
#%_libdir/lib%{_name}_preload-%api_ver.so
%_libdir/lib%_name-default-overrides-%api_ver.so
%_libdir/lib%{_name}video-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc

%files -n lib%name-gir
%_typelibdir/GstValidate-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/GstValidate-%api_ver.gir

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/%name-%api_ver/
%_datadir/gtk-doc/html/%name-plugins-%api_ver/

%changelog
* Tue Sep 24 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Fri Apr 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Fri Apr 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.90-alt1
- 1.15.90

* Sat Mar 09 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.2-alt1
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

* Sat Sep 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sat Sep 19 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.90-alt2
- rebuilt with libcairo

* Fri Aug 21 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.90-alt1
- 1.5.90

* Thu Jun 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Tue Nov 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt2
- disabled build of incomplete docs for launcher

* Tue Nov 04 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- first build for Sisyphus

