%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define ver_major 3.32
%define api_ver 1.0
%def_with introspection
%def_with vapi
%def_disable gtk_doc
%def_disable check

Name: libdazzle
Version: %ver_major.3
Release: alt1

Summary: A library to delight your users with fancy features
Group: System/Libraries
License: LGPLv3
Url: https://wiki.gnome.org/Apps/Builder

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.55.0

BuildRequires(pre): meson
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel
%{?_with_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel}
%{?_with_vapi:BuildRequires: vala-tools}
%{?_enable_gtk_doc:BuildRequires: gtk-doc}

%description
%name is a collection of fancy features for GLib and Gtk+ that
aren't quite ready or generic enough for use inside those libraries.
This is often a proving ground for new widget prototypes. Applications
such as Builder tend to drive development of this project.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name library

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the %name library

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for %name

%prep
%setup

%build
%meson %{?_without_introspection:-Dwith-introspection=false} \
	%{?_without_vapi:-Dwith-vapi=false} \
	%{?_enable_gtk_doc:-Denable-gtk_doc=true}
%meson_build

%install
%meson_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files
%_bindir/dazzle-list-counters
%_libdir/%name-%api_ver.so.*
%doc AUTHORS README.md NEWS

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%{?_with_vapi:%_vapidir/*}

%if_with introspection
%files gir
%_typelibdir/Dazzle-%api_ver.typelib

%files gir-devel
%_girdir/Dazzle-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%name/
%endif

%changelog
* Thu Jul 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.3-alt1
- 3.32.3

* Tue May 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Thu Apr 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Wed Mar 13 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Wed Oct 31 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Tue Sep 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Tue Sep 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt2
- rebuilt for (ALT #35396)

* Wed Sep 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Sat Jul 28 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.5-alt1
- 3.28.5

* Fri Jul 27 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.4-alt1
- 3.28.4

* Tue Jun 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt1
- 3.28.3

* Thu May 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Thu Feb 01 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt1
- 3.26.3

* Thu Jan 11 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Wed Oct 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Sat Aug 26 2017 Yuri N. Sedunov <aris@altlinux.org> 3.25.91-alt1
- first build for Sisyphus


