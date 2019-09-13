%def_disable snapshot
%def_disable docs

%define _name granite
%define rdn_name io.elementary.%_name
%define ver_major 5.2
%define api_ver 1.0
%define sover 5

Name: libgranite
Version: %ver_major.5
Release: alt1

Summary: Extension of GTK+3 libraries
Group: System/Libraries
License: GPLv3+
Url: https://github.com/elementary/%_name

%if_disabled snapshot
Source: %url/archive/%version/%_name-%version.tar.gz
%else
#VCS: https://github.com/elementary/granite.git
Source: %_name-%version.tar
%endif

%define gtk_ver 3.22

BuildRequires(pre): meson rpm-build-gir
BuildRequires: vala-tools libgtk+3-devel >= %gtk_ver libgee0.8-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libgtk+3-gir-devel libgee0.8-gir-devel
%{?_enable_docs:BuildRequires: gtk-doc valadoc}

%description
Granite is an extension of GTK+. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens, AppMenus,
search bars, and more found in elementary apps.

This package contains the shared library.

%package devel
Summary: Extension of GTK+ libraries (development files)
Group: Development/GNOME and GTK+

Requires: %name = %version-%release

%description devel
Granite is an extension of GTK+. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens, AppMenus,
search bars, and more found in elementary apps.

This package contains header files.

%package vala
Summary: Vala language bindings for the granite library
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release

%description vala
This package provides Vala language bindings for the granite library.

%package -n granite-demo
Summary: Extension of GTK+ libraries (demo binary)
Group: Development/GNOME and GTK+

Requires: %name = %version-%release

%description -n granite-demo
Granite is an extension of GTK+. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens, AppMenus,
search bars, and more found in elementary apps.

This package contains a small demo application to show Granite Widgets.

%package gir
Summary: GObject introspection data for the granite library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the granite library.

%package gir-devel
Summary: GObject introspection devel data for the granite library.
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the granite library.

%prep
%setup -n %_name-%version

%build
%meson %{?_enable_docs:-Ddocumentation=true}
%meson_build

%install
%meson_install
%find_lang %_name

%files -f %_name.lang
%doc AUTHORS README*
%_libdir/*.so.*

%files devel
%_includedir/%_name/
%_libdir/*.so
%_pkgconfigdir/%_name.pc

%files -n %_name-demo
%_bindir/*
%_desktopdir/%rdn_name.demo.desktop
%_datadir/icons/hicolor/*/*/*.svg

%files gir
%_typelibdir/Granite-%api_ver.typelib

%files gir-devel
%_girdir/Granite-%api_ver.gir

%files vala
%_datadir/vala/vapi/%_name.deps
%_datadir/vala/vapi/%_name.vapi

%changelog
* Sun Sep 08 2019 Yuri N. Sedunov <aris@altlinux.org> 5.2.5-alt1
- 5.2.5

* Mon Jul 08 2019 Yuri N. Sedunov <aris@altlinux.org> 5.2.4-alt1
- 5.2.4

* Fri Feb 15 2019 Yuri N. Sedunov <aris@altlinux.org> 5.2.3-alt1
- 5.2.3 (ported to Meson build system)

* Thu Dec 20 2018 Yuri N. Sedunov <aris@altlinux.org> 5.2.2-alt1
- 5.2.2

* Fri Nov 09 2018 Yuri N. Sedunov <aris@altlinux.org> 5.2.1-alt1
- 5.2.1

* Sun Nov 04 2018 Yuri N. Sedunov <aris@altlinux.org> 5.2.0-alt1
- 5.2.0

* Thu Aug 30 2018 Yuri N. Sedunov <aris@altlinux.org> 5.1.0-alt1
- 5.1.0

* Mon Jun 25 2018 Yuri N. Sedunov <aris@altlinux.org> 5.0-alt1
- updated to 5.0-21-g4e84fc7

* Mon Nov 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt1
- 0.5

* Wed May 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Fri Mar 31 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.0.1-alt2
- fixed build with vala-0.36

* Thu Sep 29 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4.0.1-alt1
- 0.4.0.1

* Sun Sep 06 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Mon Mar 03 2014 Igor Zubkov <icesik@altlinux.org> 0.2.3-alt1
- 0.2.3

* Mon Nov 11 2013 Igor Zubkov <icesik@altlinux.org> 0.2.2-alt6
- Fix FTBFS with new cmake

* Mon Sep 16 2013 Igor Zubkov <icesik@altlinux.org> 0.2.2-alt5
- Fix typo in spec file

* Mon Sep 16 2013 Igor Zubkov <icesik@altlinux.org> 0.2.2-alt4
- Cleanup spec file
- Update build requires

* Thu Aug 22 2013 Igor Zubkov <icesik@altlinux.org> 0.2.2-alt3
- Cleanup build requires

* Tue Aug 20 2013 Igor Zubkov <icesik@altlinux.org> 0.2.2-alt2
- Fix summaries and descriptions

* Sun Aug 11 2013 Igor Zubkov <icesik@altlinux.org> 0.2.2-alt1
- 0.1.0 -> 0.2.2

* Sun Aug 11 2013 Igor Zubkov <icesik@altlinux.org> 0.1.0-alt1
- build for Sisyphus

