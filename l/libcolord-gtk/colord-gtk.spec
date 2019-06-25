%define _name colord
%define api_ver 1.0

%def_enable introspection
%def_enable vala
%def_enable man
%def_enable docs
%def_enable tests
%def_disable check

Name: lib%_name-gtk
Version: 0.2.0
Release: alt1

Summary: GTK+3 support library for colord daemon
License: GPLv2+
Group: System/Libraries

URL: http://www.freedesktop.org/software/%name/
Source: http://www.freedesktop.org/software/colord/releases/%_name-gtk-%version.tar.xz

%define glib_ver 2.32
%define colord_ver 0.1.27

Requires: lib%_name >= %colord_ver

BuildRequires(pre): meson rpm-build-gir
%{?_enable_vala:BuildRequires(pre): rpm-build-vala}
BuildRequires: glib2-devel >= %glib_ver
BuildRequires: lib%_name-devel >= %colord_ver libgtk+3-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel lib%_name-gir-devel}
%{?_enable_vala:BuildRequires: vala-tools lib%_name-vala}
%{?_enable_man:BuildRequires: xsltproc docbook5-style-xsl}
%{?_enable_docs:BuildRequires: gtk-doc}

%description
colord is a low level system activated daemon that maps color devices to color
profiles in the system context.

This package provides GTK+3 library for interaction with colord.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
colord is a low level system activated daemon that maps color devices to color
profiles in the system context.

This package provides development files for the %_name-gtk library.

%package gir
Summary: GObject introspection data for the %_name-gtk  library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %_name-gtk library.

%package gir-devel
Summary: GObject introspection devel data for the %_name-gtk library
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %_name-gtk library.

%package vala
Summary: Vala Bindings for %_name-gtk
Group: Development/C
BuildArch: noarch
Requires: %name-devel = %version-%release

%description vala
This package provides Vala language bindings for %_name-gtk library.

%package devel-doc
Summary: Development documentation for %_name-gtk
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package contains development documentation for  %_name-gtk library.

%prep
%setup -n %_name-gtk-%version

%build
%meson \
	%{?_enable_vala:-Dvapi=true} \
	%{?_disable_man:-Dman=false} \
	%{?_disable_docs:-Ddocs=false} \
	%{?_disable_tests:-Dtests=false}
%meson_build

%install
%meson_install
%find_lang %_name-gtk

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files  -f %_name-gtk.lang
%_bindir/cd-convert
%{?_enable_man:%_man1dir/cd-convert.1.*}
%_libdir/%name.so.*

%files devel
%_includedir/%_name-1/%_name-gtk.h
%_includedir/%_name-1/%_name-gtk/
%_libdir/%name.so
%_pkgconfigdir/%_name-gtk.pc

%if_enabled introspection
%files gir
%_typelibdir/ColordGtk-%api_ver.typelib

%files gir-devel
%_girdir/ColordGtk-%api_ver.gir
%endif

%if_enabled vala
%files vala
%_datadir/vala/vapi/%_name-gtk.*
%endif

%if_enabled docs
%files devel-doc
%_datadir/gtk-doc/html/%_name-gtk/
%endif


%changelog
* Thu Jun 20 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0 (ported to Meson build system)
- new -devel-doc subpackage

* Sat Jun 04 2016 Yuri N. Sedunov <aris@altlinux.org> 0.1.26-alt1
- 0.1.26

* Sun Jun 08 2014 Yuri N. Sedunov <aris@altlinux.org> 0.1.25-alt2
- rebuilt against libcolord.so.2

* Sat Mar 23 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.25-alt1
- 0.1.25

* Sat Feb 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.24-alt2
- rebuilt against libcolord.so.2

* Mon Dec 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.24-alt1
- 0.1.24

* Tue Sep 04 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.23-alt1
- 0.1.23

* Sun Jul 01 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.22-alt1
- first build for Sisyphus

