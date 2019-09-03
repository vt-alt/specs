%define api_ver 0.0

%def_disable check

Name: libhandy
Version: 0.0.11
Release: alt1

Summary: Library with GTK+3 widgets for mobile devices
Group: System/Libraries
License: LGPLv2+
Url: https://source.puri.sm/Librem5/libhandy/

#VCS: https://source.puri.sm/Librem5/libhandy.git
Source: https://source.puri.sm/Librem5/libhandy/-/archive/v%version/%name-v%version.tar.bz2

%define gtk_ver 3.24.1

BuildRequires(pre): meson rpm-build-gir
BuildRequires: gtk-doc
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gladeui-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk+-3.0) >= %gtk_ver
BuildRequires: gir(Gtk) = 3.0
BuildRequires: vala-tools
%{?_enable_check:BuildRequires: xvfb-run}

%description
libhandy provides GTK+3 widgets and GObjects to ease developing
applications for mobile devices.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the handy library.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the handy library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %EVR

%description devel-doc
This package contains development documentation for handy library.

%prep
%setup -n %name-v%version

%build
%meson \
	-Dgtk_doc=true \
	-Dexamples=false
%meson_build

%install
%meson_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
xvfb-run -s -noreset %meson_test

%files
%_libdir/%name-%api_ver.so.*
%doc README.md

%files devel
%_includedir/%name-%api_ver/
%_libdir/glade/modules/libglade-handy.so
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%_datadir/glade/catalogs/%name.xml
%_vapidir/%name-%api_ver.*

%files gir
%_typelibdir/Handy-%api_ver.typelib

%files gir-devel
%_girdir/Handy-%api_ver.gir

%files devel-doc
%_datadir/gtk-doc/html/%name/

%changelog
* Fri Aug 30 2019 Yuri N. Sedunov <aris@altlinux.org> 0.0.11-alt1
- 0.0.11

* Wed Jun 19 2019 Yuri N. Sedunov <aris@altlinux.org> 0.0.10-alt1
- 0.0.10

* Fri Mar 08 2019 Yuri N. Sedunov <aris@altlinux.org> 0.0.9-alt1
- 0.0.9

* Sat Feb 16 2019 Yuri N. Sedunov <aris@altlinux.org> 0.0.8-alt1
- 0.0.8

* Thu Feb 07 2019 Yuri N. Sedunov <aris@altlinux.org> 0.0.7-alt1
- first build for sisyphus

