%define ver_major 0.4
%define api_ver %ver_major

%def_enable gtk_doc
%def_enable check

Name: lasem
Version: %ver_major.4
Release: alt1

Summary: C/Gobject based SVG/Mathml renderer and editor - tools
License: GPL
Group: Graphics

Url: https://gitlab.gnome.org/GNOME/lasem
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
#Source: %name-%version.tar

BuildRequires: libgio-devel libxml2-devel libcairo-devel libcairo-gobject-devel libgdk-pixbuf-devel libpango-devel
BuildRequires: libgdk-pixbuf-gir-devel libpango-gir-devel
BuildRequires: intltool bison flex gtk-doc

Requires(pre): lib%name = %version-%release

%description
Lasem aims to be a C/Gobject based SVG/Mathml renderer and editor,
supporting CSS style sheets. It uses cairo and pango as it's rendering
abstraction layer, and then support numerous output formats: xlib, PNG,
SVG, PDF, PS, EPS...

%package -n lib%name
Summary: C/Gobject based SVG/Mathml renderer and editor - library
Group: System/Libraries
# cmr10, cmmi10, cmex10 and cmsy10 fonts (see README)
Requires: fonts-ttf-latex-xft

%description -n lib%name
%summary

%package -n lib%name-devel
Summary: C/Gobject based SVG/Mathml renderer and editor - development files
Group: Development/C
Requires(pre): lib%name = %version-%release

%description -n lib%name-devel
%summary

%package -n lib%name-gir
Summary: GObject introspection data for the Lasem library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
%summary

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Lasem library
Group: Development/Other
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
%summary

%package -n lib%name-devel-doc
Summary: Development documentation for Lasem library
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name-devel < %version

%description -n lib%name-devel-doc
%summary

This package provides documentation needed for developing Lasem
applications.


%prep
%setup

%build
%autoreconf
%configure --disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%makeinstall_std
%find_lang %name-%api_ver

%check
%make check

%files
%_bindir/%name-render-%api_ver
%_man1dir/%name-render-*
%doc README ChangeLog AUTHORS NEWS

%files -n lib%name -f %name-%api_ver.lang
%_libdir/lib%name-%api_ver.so.*

%files -n lib%name-devel
%_includedir/%name-%api_ver
%_libdir/pkgconfig/%name-%api_ver.pc
%_libdir/lib%name-%api_ver.so

%files -n lib%name-gir
%_typelibdir/Lasem-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Lasem-%api_ver.gir

%if_enabled gtk_doc
%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/%name-%api_ver/
%endif

%exclude %_prefix/doc/%name-%api_ver/

%changelog
* Fri May 24 2019 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- 0.4.4

* Fri May 04 2018 Grigory Ustinov <grenka@altlinux.org> 0.4.3-alt1.1
- NMU: Rebuilt for e2k.

* Sun Feb 15 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Thu Feb 12 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Wed Dec 19 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1
- updated buildreqs
- added fonts-ttf-latex-xft to dependencies (see README)
- new -devel-doc subpackage

* Sat Nov 17 2012 Vladimir Lettiev <crux@altlinux.ru> 0.3.4-alt1
- New version 0.3.4 (Closes: #27993)
- Dropped patch

* Thu Jul 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.1
- Fixed build

* Sat Sep 11 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.0-alt1
- New version 0.3.0
- Added gir subpackages

* Thu Mar 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.0-alt1
- New version 0.2.0

* Tue Nov 03 2009 Vladimir Lettiev <crux@altlinux.ru> 0.1.2-alt1
- initial build

