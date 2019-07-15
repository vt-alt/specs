%def_disable snapshot

%define _name gxml
%define ver_major 0.18
%define api_ver 0.18
%def_enable introspection
%def_enable docs
%def_enable check

Name: lib%_name
Version: %ver_major.1
Release: alt1

Summary: GXml provides a GObject API for manipulating XML
Group: System/Libraries
License: LGPLv2.1+
Url: https://wiki.gnome.org/GXml

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

%define glib_ver 2.32
%define vala_ver 0.34.6
%define gee_ver 0.10.5
%define xml2_ver 2.7

BuildRequires(pre): meson
BuildRequires: libvala-devel >= %vala_ver vala-tools
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgee0.8-devel >= %gee_ver
BuildRequires: libxml2-devel >= %xml2_ver
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgee0.8-gir-devel}
%{?_enable_docs:BuildRequires: valadoc yelp-tools graphviz gtk-doc}

%description
GXml provides a GObject API for manipulating XML. Most functionality
is provided through libxml2. Currently, GXml provides the DOM Level 1
Core API.

%package devel
Summary: Development files for GXml
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libraries and header files needed for
development using GXml.

%package gir
Summary: GObject introspection data for the GXml library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GXml library

%package gir-devel
Summary: GObject introspection devel data for the GXml library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the GXml library.

%package devel-doc
Summary: Development documentation for GXml
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for GXml library.

%prep
%setup -n %_name-%version
# to avoid "/usr/lib/rpm/debugedit: canonicalization unexpectedly shrank by one character" bug
find ./ -type f -print0| xargs -r0 subst 's|gxml//xlibxml.h|gxml/xlibxml.h|' --

%build
%meson \
	%{?_enable_docs:-Ddocs=true} \
	%{?_enable_introspection:-Dintrospection=true}
%meson_build

%install
%meson_install
%find_lang --output=%_name.lang %_name GXml-%api_ver

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files -f %_name.lang
%_libdir/%name-%api_ver.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%_vapidir/%_name-%api_ver.deps
%_vapidir/%_name-%api_ver.vapi

%if_enabled introspection
%files gir
%_typelibdir/GXml-%api_ver.typelib

%files gir-devel
%_girdir/GXml-%api_ver.gir
%endif

%if_enabled docs
%files devel-doc
#%_datadir/gtk-doc/html/%_name/
%_datadir/devhelp/books/GXml-%api_ver/
%endif

%changelog
* Mon Jul 08 2019 Yuri N. Sedunov <aris@altlinux.org> 0.18.1-alt1
- 0.18.1 (ported to Meson build system)

* Thu Jul 04 2019 Yuri N. Sedunov <aris@altlinux.org> 0.18.0-alt1
- 0.18.0

* Sat Jan 05 2019 Yuri N. Sedunov <aris@altlinux.org> 0.16.3-alt2
- updated to 0.16.3-3-ge51ce7b

* Mon Mar 05 2018 Yuri N. Sedunov <aris@altlinux.org> 0.16.3-alt1
- 0.16.3

* Wed Feb 07 2018 Yuri N. Sedunov <aris@altlinux.org> 0.16.1-alt1
- 0.16.1

* Wed Jan 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0

* Sat Apr 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.14.3-alt1
- 0.14.3

* Thu Apr 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.14.2-alt1
- 0.14.2

* Fri Mar 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Tue Sep 27 2016 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Fri Jan 15 2016 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2

* Wed Jan 13 2016 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Thu Jul 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- first build for Sisyphus



