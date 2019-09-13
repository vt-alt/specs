%define _libexecdir %_prefix/libexec

%define _name amtk
%define ver_major 5.0
%define api_ver 5

%def_disable static
%def_disable gtk_doc
%def_enable introspection
%def_disable check

Name: lib%_name
Version: %ver_major.1
Release: alt1

Summary: Actions, Menus and Toolbars Kit for GTK+ applications
License: %lgpl2plus
Group: System/Libraries
Url:  https://wiki.gnome.org/Projects/Amtk

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz

%define gtk_ver 3.22
%define gi_ver 1.42

BuildRequires(pre): rpm-build-gnome rpm-build-licenses rpm-build-gir
BuildRequires: gtk-doc
BuildRequires: libgtk+3-devel >= %gtk_ver
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= %gi_ver libgtk+3-gir-devel}

%description
Amtk is the acronym for "Actions, Menus and Toolbars Kit". It is a basic
GtkUIManager replacement based on GAction. It is suitable for both a
traditional UI or a modern UI with a GtkHeaderBar.

%package devel
Summary: Development environment for Amtk
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the necessary components to develop with Amtk
library.

%package devel-doc
Summary: Development documentation for Amtk
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
Amtk is the acronym for "Actions, Menus and Toolbars Kit". It is a basic
GtkUIManager replacement based on GAction. It is suitable for both a
traditional UI or a modern UI with a GtkHeaderBar.

This package contains development documentation for Amtk.

%package devel-static
Summary: Stuff for developing with Amtk
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains the necessary components to develop statically
linked software for Amtk.

%package gir
Summary: GObject introspection data for the Amtk library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Amtk library.

%package gir-devel
Summary: GObject introspection devel data for the Amtk
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Amtk library.


%prep
%setup -n %_name-%version

%build
%autoreconf
%configure %{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable introspection}

%make_build

%install
%makeinstall_std
%find_lang --output=%_name.lang %_name %{_name}-%api_ver

%check
%make check

%files -f %_name.lang
%_libdir/%name-%api_ver.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc

%files devel-doc
%_datadir/gtk-doc/html/%_name-%{api_ver}.0/

%if_enabled static
%files devel-static
%_libdir/%name-%api_ver.a
%endif

%if_enabled introspection
%files gir
%_typelibdir/Amtk-%api_ver.typelib

%files gir-devel
%_girdir/Amtk-%api_ver.gir
%endif

%changelog
* Fri Sep 06 2019 Yuri N. Sedunov <aris@altlinux.org> 5.0.1-alt1
- 5.0.1

* Mon Jul 16 2018 Yuri N. Sedunov <aris@altlinux.org> 5.0.0-alt1
- first build for Sisyphus




