%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name gdata
%define ver_major 0.17
%define api_ver 0.0

%def_enable gnome
%def_enable goa
%def_enable introspection
%def_enable vala
%def_enable gtk_doc
%def_enable installed_tests
%def_disable check

Name: lib%_name
Version: %ver_major.11
Release: alt1

Summary: Library for the GData protocol
Group: System/Libraries
License: LGPLv2+
Url: https://wiki.gnome.org/Projects/libgdata

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.44
%define soup_ver 2.42
%define goa_ver 3.8
%define uhttpmock_ver 0.5.0

BuildRequires(pre): meson
BuildRequires: gtk-doc
BuildRequires: glib2-devel >= %glib_ver libgdk-pixbuf-devel libgtk+3-devel liboauth-devel
BuildRequires: libjson-glib-devel libuhttpmock-devel >= %uhttpmock_ver
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libjson-glib-gir-devel libuhttpmock-gir-devel}
%{?_enable_vala:BuildRequires: vala-tools}
%{?_enable_gnome:BuildRequires: gcr-libs-devel libxml2-devel libsoup-gnome-devel >= %soup_ver libsoup-gnome-gir-devel}
%{?_enable_goa:BuildRequires: libgnome-online-accounts-devel >= %goa_ver libgnome-online-accounts-gir-devel}

%description
libgdata is a GLib-based library for accessing online service APIs using the
GData protocol --- most notably, Google's services. It provides APIs to access
the common Google services, and has full asynchronous support.

%package gir
Summary: GObject introspection data for the GData library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GData library.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-doc
Summary: Development documentation for the %name
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
libgdata is a GLib-based library for accessing online service APIs using the
GData protocol --- most notably, Google's services. It provides APIs to access
the common Google services, and has full asynchronous support.

This package contains development documentation for the %name.

%package gir-devel
Summary: GObject introspection devel data for the GData library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the GData library.

%package tests
Summary: Tests for %name
Group: Development/Other

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed %name.

%prep
%setup

%build
%meson \
	%{?_disable_gnome:-Dgnome=false} \
	%{?_disable_goa-Dgoa=false} \
	%{?_disable_gtk_doc:-Dgtk_doc=false} \
	%{?_disable_vala:-Dvapi=false} \
	%{?_disable_installed_tests:-Dinstalled_tests=false}
%meson_build

%install
%meson_install
%find_lang %_name

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files -f %_name.lang
%_libdir/*.so.*
%doc NEWS README AUTHORS

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/%name.pc
%{?_enable_vala:%_vapidir/%name.*}

%if_enabled introspection
%files gir
%_typelibdir/GData-%api_ver.typelib

%files gir-devel
%_girdir/GData-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%_name/
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%name/
%_datadir/installed-tests/%name/
%endif


%changelog
* Wed Aug 21 2019 Yuri N. Sedunov <aris@altlinux.org> 0.17.11-alt1
- 0.17.11
- new -tests subpackage

* Sat Feb 09 2019 Yuri N. Sedunov <aris@altlinux.org> 0.17.9-alt2
- fixed build with new autoconf-archive-2019.01.06

* Wed Aug 23 2017 Yuri N. Sedunov <aris@altlinux.org> 0.17.9-alt1
- 0.17.9

* Thu Apr 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.17.8-alt1
- 0.17.8

* Mon Mar 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.17.7-alt1
- 0.17.7

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 0.17.6-alt1
- 0.17.6

* Fri Sep 02 2016 Yuri N. Sedunov <aris@altlinux.org> 0.17.6-alt0.1
- updated to LIBGDATA_0_17_5-11-g2590c92

* Thu Jun 30 2016 Yuri N. Sedunov <aris@altlinux.org> 0.17.5-alt1
- 0.17.5

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 0.17.4-alt1
- 0.17.4

* Mon Sep 14 2015 Yuri N. Sedunov <aris@altlinux.org> 0.17.3-alt1
- 0.17.3_c192f1f3

* Fri Jul 10 2015 Yuri N. Sedunov <aris@altlinux.org> 0.17.2-alt1
- 0.17.2

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 0.16.1-alt1
- 0.16.1

* Thu Sep 18 2014 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0

* Fri Aug 22 2014 Yuri N. Sedunov <aris@altlinux.org> 0.15.2-alt1
- 0.15.2

* Wed May 28 2014 Yuri N. Sedunov <aris@altlinux.org> 0.14.3-alt1
- 0.14.3

* Thu Dec 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.1-alt1
- 0.14.1

* Thu Aug 29 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Tue Feb 26 2013 Yuri N. Sedunov <aris@altlinux.org> 0.13.3-alt1
- 0.13.3

* Sun Sep 30 2012 Yuri N. Sedunov <aris@altlinux.org> 0.13.2-alt1
- 0.13.2

* Mon Jul 30 2012 Yuri N. Sedunov <aris@altlinux.org> 0.13.1-alt1
- 0.13.1

* Sat Apr 14 2012 Yuri N. Sedunov <aris@altlinux.org> 0.13.0-alt1
- 0.13.0

* Mon Apr 02 2012 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Mon Mar 12 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11.1-alt1
- 0.11.1

* Mon Mar 12 2012 Yuri N. Sedunov <aris@altlinux.org> 0.10.2-alt1
- 0.10.2

* Thu Sep 15 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.1-alt1
- 0.10.1

* Sun May 29 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Tue Dec 14 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.6-alt1
- 0.6.6

* Fri Oct 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5-alt2
- updated build dependencies

* Thu Oct 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Thu Apr 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.4-alt2
- rebuild

* Tue Mar 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.4-alt1
- 0.6.4

* Tue Mar 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Tue Mar 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.2-alt2
- rebuild

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Tue Feb 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Mon Feb 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Mon Nov 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Thu Sep 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.0-alt1
- initial release

