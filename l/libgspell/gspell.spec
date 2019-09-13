%def_disable snapshot
%def_enable installed_tests
%{?_enable_snapshot:%def_enable gtk_doc}
%def_enable check

%define _name gspell
%define ver_major 1.8
%define api_ver 1

Name: lib%_name
Version: %ver_major.2
Release: alt1

Summary: A spell-checking library for GTK+ applications
Group: System/Libraries
License: LGPLv2.1+
Url: https://wiki.gnome.org/Projects/gspell

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

%define gtk_ver 3.20.0
%define enchant_ver 1.6.0

Requires: iso-codes

BuildRequires: autoconf-archive
BuildRequires: libgtk+3-devel >= %gtk_ver libenchant2-devel >= %enchant_ver iso-codes-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel vala-tools gtk-doc
%{?_enable_check:BuildRequires: xvfb-run hunspell-en valgrind}

%description
gspell library provides a flexible API to add spell checking to a GTK+
applications.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release
Requires: libenchant2-devel >= %enchant_ver

%description devel
Development files for %_name, spell-checking library for GTK+
applications.

%package gir
Summary: GObject introspection data for the Gspell
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Gspell library.

%package gir-devel
Summary: GObject introspection devel data for the Gspell
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the Gspell library.

%package devel-doc
Summary: Development documentation for Gspell
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package contains development documentation for Gspell library.

%package tests
Summary: Tests for Gspell library
Group: Development/Other
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed Gspell library.


%prep
%setup -n %_name-%version

%build
%configure \
    %{?_enable_gtk_doc:--enable-gtk-doc} \
    %{?_enable_installed_tests:--enable-installed-tests}

%install
%makeinstall_std
%find_lang --output=%name.lang %_name-%api_ver

%check
xvfb-run %make check

%files -f %name.lang
%_bindir/%_name-app1
%_libdir/%name-%api_ver.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%_vapidir/%_name-%api_ver.*

%files gir
%_typelibdir/Gspell-%api_ver.typelib

%files gir-devel
%_girdir/Gspell-%api_ver.gir

%files devel-doc
%_datadir/gtk-doc/html/%_name-*/

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name-%api_ver/
%_datadir/installed-tests/%_name-%api_ver/
%endif


%changelog
* Fri Sep 06 2019 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Sat Jun 16 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Sat Mar 10 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Thu Feb 15 2018 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1-1-g916fca8 with enchant2

* Sun Oct 29 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Sun Sep 10 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sat Aug 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Sun Apr 09 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Sat Mar 18 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Fri Feb 24 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Fri Dec 16 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Sun Nov 06 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Sun Sep 18 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Sat Jul 09 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Fri Jun 10 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sun Apr 10 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sun Mar 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sun Mar 13 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1
- 0.2.5

* Fri Feb 12 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- first build for sisyphus

