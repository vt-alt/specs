%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name graphene
%define ver_major 1.10
%define api_ver 1.0

%def_disable static
%def_enable gtk_doc
%def_enable introspection
%def_enable installed_tests
%def_disable gcc_vector
%ifarch i586 %arm
%def_disable sse2
%endif
%ifnarch %arm
%def_disable neon
%endif

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: Graphene is a library of data types commonly used to implement 2D-in-3D or full 3D canvases
License: BSD-like
Group: System/Libraries
Url: https://ebassi.github.io/%_name

%if_disabled snapshot
Source: https://github.com/ebassi/%_name/releases/download/%version/%_name-%version.tar.xz
%else
# VCS: https://github.com/ebassi/graphene.git
Source: %_name-%version.tar
%endif

BuildRequires(pre): meson

%define __python %nil
BuildRequires: /proc
BuildRequires: python3 gobject-introspection-devel gtk-doc

%description
Graphene library provides a small set of mathematical types needed to
implement graphic libraries that deal with 2D and 3D transformations and
projections.

%package devel
Summary: Development libraries and header files for Graphene
Group: Development/C
Requires: %name = %version-%release

%description devel
This package package includes the libraries and header files
for the Graphene library.

%package devel-doc
Summary: Development documentation for Graphene
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
%summary
This package contains development documentation for Graphene library.

%package gir
Summary: GObject introspection data for the Graphene library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Graphene library.

%package gir-devel
Summary: GObject introspection devel data for the Graphene library
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Graphene library.

%package tests
Summary: Tests for the Grapnene library
Group: Development/Other
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed Graphene library.

%prep
%setup -n %_name-%version

%build
%meson \
    %{?_disable_introspection:-Dintrospection=false} \
    %{?_disable_sse2:-Dsse2=false} \
    %{?_disable_gcc_vector:-Dgcc_vector=false} \
    %{?_disable_neon:-Darm_neon=false} \
    %{?_enable_gtk_doc:-Dgtk_doc=true} \
    %{?_disable_installed_tests:-Dtests=false}
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_libdir/%name-%api_ver.so.*
%doc README.md

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%_name-%api_ver/
%_libdir/*.so
%_pkgconfigdir/%_name-%api_ver.pc
%_pkgconfigdir/%_name-gobject-%api_ver.pc

%if_enabled introspection
%files gir
%_typelibdir/Graphene-%api_ver.typelib

%files gir-devel
%_girdir/Graphene-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%_name/
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name-%api_ver/
%_datadir/installed-tests/%_name-%api_ver/
%endif


%changelog
* Sun Sep 08 2019 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Thu Aug 08 2019 Yuri N. Sedunov <aris@altlinux.org> 1.9.6-alt1
- 1.9.6

* Wed Jun 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.9.4-alt1
- 1.9.4

* Tue May 14 2019 Yuri N. Sedunov <aris@altlinux.org> 1.9.2-alt1
- 1.9.2

* Thu Mar 21 2019 Yuri N. Sedunov <aris@altlinux.org> 1.8.6-alt1
- 1.8.6

* Thu Jun 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Fri Feb 23 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0
- new -tests subpackage

* Thu Mar 02 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Tue Jan 10 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.4-alt1
- 1.5.4

* Mon Nov 28 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- updated to 1.5.2-7-g280d7b5

* Tue May 17 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- first build for Sisyphus

