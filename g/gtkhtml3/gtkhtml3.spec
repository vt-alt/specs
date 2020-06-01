%define ver_major 3.32
%define origname gtkhtml
%def_disable static
%def_disable gtk_doc
%def_disable gtk3
%if_enabled gtk3
%define api_ver 4.0
%else
%define api_ver 3.14
%endif

Name: gtkhtml3
Version: %ver_major.2
Release: alt5

Summary: GtkHTML is a HTML rendering/editing library
License: GPL-2.0 and LGPL-2.0
Group: Graphical desktop/GNOME
Url: http://projects.gnome.org/evolution/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%origname/%ver_major/%origname-%version.tar.bz2
Source1: lib%{name}-%ver_major.map
Patch1: %name-%ver_major-alt-symver.patch
Patch2: %name-3.32.2-alt-deprecation.patch
Patch3: %name-3.32.2-alt3-deprecation.patch

# from configure.in
%define gtk_ver 2.21.6
%define gtk3_ver 2.90.4
%define gail_ver 1.1.0
%define gnome_icon_ver 2.22.0
%define libsoup_ver 2.31.6

BuildPreReq: gnome-common

BuildPreReq: intltool >= 0.36.3
%if_enabled gtk3
BuildPreReq: libgtk+3-devel >= %gtk3_ver
BuildPreReq: libgail3-devel
%else
BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildPreReq: libgail-devel >= %gail_ver
%endif
BuildPreReq: gnome-icon-theme >= %gnome_icon_ver
BuildPreReq: libsoup-devel >= %libsoup_ver
BuildPreReq: iso-codes-devel libenchant-devel >= 1.1.7
BuildPreReq: libGConf-devel

%description
GtkHTML is a HTML rendering/editing library. GtkHTML is not designed to
be the ultimate HTML browser/editor: instead, it is designed to be
easily embedded into applications that require lightweight HTML
functionality.

GtkHTML was originally based on KDE's KHTMLW widget, but is now
developed independently of it. The most important difference between
KHTMLW and GtkHTML, besides being GTK-based, is that GtkHTML is also an
editor. Thanks to the Bonobo editor component that comes with the
library, it's extremely simple to add HTML editing to an existing
application.

%package -n lib%name
Summary: Libraries for GtkHTML
Group: System/Libraries

%description -n lib%name
GtkHTML is a HTML rendering/editing library. GtkHTML is not designed to
be the ultimate HTML browser/editor: instead, it is designed to be
easily embedded into applications that require lightweight HTML
functionality.

This package contains libraries used by GtkHTML.

%package -n lib%name-devel
Provides: lib%name-devel
Summary: Development libraries, header files and utilities for GtkHTML
Group: Development/GNOME and GTK+
Requires: lib%name = %version-%release

%description -n lib%name-devel
GtkHTML is a HTML rendering/editing library. GtkHTML is not designed to
be the ultimate HTML browser/editor: instead, it is designed to be
easily embedded into applications that require lightweight HTML
functionality.

This package contains the files necessary to develop applications with GtkHTML.

%package -n lib%name-devel-static
Provides: lib%name-devel-static
Summary: Static libraries for GtkHTML
Group: Development/GNOME and GTK+

%description -n lib%name-devel-static
GtkHTML is a HTML rendering/editing library. GtkHTML is not designed to
be the ultimate HTML browser/editor: instead, it is designed to be
easily embedded into applications that require lightweight HTML
functionality.

This package contains the files necessary to develop applications
statically linked with GtkHTML.

%prep
%setup -q -n %origname-%version
install -p -m644 %SOURCE1 gtkhtml/libgtkhtml.map
%if_disabled gtk3
%patch1
%endif

%patch2
%patch3

%build
%autoreconf
export LDFLAGS="$LDFLAGS -lm"
%configure \
    %{subst_enable static} \
    %{?_enable_gtk_doc:--enable-gtk-doc} \
    %{subst_enable gtk3} \
    --disable-deprecated-warning-flags
%make_build

%install
%makeinstall_std
%find_lang %origname-%api_ver

%files -n lib%name -f %origname-%api_ver.lang
%_libdir/*.so.*
%_datadir/%origname-%api_ver
%doc AUTHORS ChangeLog NEWS README TODO

%files -n lib%name-devel
%_bindir/gtkhtml-editor-test
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%_libdir/%origname/*.a
%endif

%changelog
* Sun Mar 22 2020 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt5
- rebuilt with disabled deprecated-warning-flags
- fixed License tag

* Mon Feb 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt4
- explicitly link against libm

* Tue Apr 03 2012 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt3
- fixed build against glib2 >= 2.32

* Tue Nov 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt2
- fixed build against glib2 >= 2.30

* Mon Feb 07 2011 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Mon Nov 15 2010 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Thu Aug 12 2010 Yuri N. Sedunov <aris@altlinux.org> 3.30.3-alt1
- 3.30.3

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 3.29.92-alt1
- 3.29.92

* Mon Mar 01 2010 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt1
- 3.28.3

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 3.29.91-alt1
- 3.29.91

* Mon Feb 08 2010 Yuri N. Sedunov <aris@altlinux.org> 3.29.90-alt1
- 3.29.90

* Mon Jan 25 2010 Yuri N. Sedunov <aris@altlinux.org> 3.29.6-alt1
- 3.29.6
- updated version script for GTKHTML_3.29.6

* Mon Dec 14 2009 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Sun Oct 18 2009 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 3.27.92-alt1
- 3.27.92

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 3.27.91-alt1
- 3.27.91

* Tue Aug 11 2009 Yuri N. Sedunov <aris@altlinux.org> 3.27.90-alt1
- 3.27.90
- updated version script
- updated buildreqs

* Mon Jun 29 2009 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt1
- 3.26.3

* Mon May 18 2009 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 3.26.1.1-alt1
- 3.26.1.1

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Wed Mar 11 2009 Yuri N. Sedunov <aris@altlinux.org> 3.25.92-alt1
- 3.25.92
- updated version script

* Mon Jan 12 2009 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2
- removed obsolete *ldconfig from %%post{,un}

* Fri Nov 07 2008 Yuri N. Sedunov <aris@altlinux.org> 3.24.1.1-alt1
- 3.24.1.1

* Mon Oct 20 2008 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Tue Oct 07 2008 Alexey Shabalin <shaba@altlinux.ru> 3.24.0-alt2
- add versioning

* Sat Sep 27 2008 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0
- build --with-bonobo-editor
- updated buildreqs

* Mon Jun 30 2008 Alexey Shabalin <shaba@altlinux.ru> 3.18.3-alt1
- 3.18.3

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 3.18.2-alt1
- 3.18.2

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 3.18.1-alt1
- 3.18.1

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> 3.18.0-alt1.1
- build for Sisyphus

* Thu Mar 13 2008 Alexey Shabalin <shaba@altlinux.ru> 3.18.0-alt1
- 3.18.0

* Mon Nov 19 2007 Alexey Shabalin <shaba@altlinux.ru> 3.16.1-alt1
- update to 3.16.1

* Fri Oct 12 2007 Alexey Shabalin <shaba@altlinux.ru> 3.16.0-alt1
- update to 3.16.0

* Thu Aug 02 2007 Alexey Shabalin <shaba@altlinux.ru> 3.14.3-alt1
- update to 3.14.3

* Sat Feb 24 2007 Ilya Mashkin <oddity@altlinux.ru> 3.12.3-alt1
- update to 3.12.3

* Mon Jan 01 2007 Ilya Mashkin <oddity@altlinux.ru> 3.12.2-alt1
- New release 3.12.2

* Mon Oct 02 2006 Mikhail Zabaluev <mhz@altlinux.ru> 3.12.1-alt1
- Release 3.12.1

* Tue Sep 05 2006 Mikhail Zabaluev <mhz@altlinux.ru> 3.12.0-alt1
- Release 3.12.0
- Patch0 has gone upstream

* Thu Aug 31 2006 Mikhail Zabaluev <mhz@altlinux.ru> 3.10.3-alt1
- Release 3.10.3

* Thu Jun 01 2006 Mikhail Zabaluev <mhz@altlinux.ru> 3.10.2-alt1
- Release 3.10.2

* Sat May 27 2006 Mikhail Zabaluev <mhz@altlinux.ru> 3.10.1-alt1
- Release 3.10.1

* Wed Mar 15 2006 Mikhail Zabaluev <mhz@altlinux.ru> 3.10.0-alt1
- Release 3.10.0

* Sat Mar 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 3.9.92-alt3
- Patch0: correct linkage to avoid unresolved symbols

* Thu Mar 09 2006 Mikhail Zabaluev <mhz@altlinux.ru> 3.9.92-alt2
- Added gnome-icon-theme to build dependencies

* Sun Mar 05 2006 Mikhail Zabaluev <mhz@altlinux.ru> 3.9.92-alt1
- 3.9.92

* Thu Feb 16 2006 Mikhail Zabaluev <mhz@altlinux.ru> 3.9.91-alt1
- Updated to 3.9.91
- Buildreq

* Tue Nov 29 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.8.2-alt1
- 3.8.2

* Tue Nov 01 2005 Mikhail Zabaluev <4mhz@altlinux.ru> 3.8.1-alt3
- Fixed a mistake in dependencies (bug 7642)

* Wed Oct 19 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.8.1-alt2
- Added /usr/lib/gtkhtml to the file list (bug #8234)

* Tue Oct 04 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.8.1-alt1
- 3.8.1

* Tue Sep 06 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.8.0-alt1
- 3.8.0

* Fri Aug 26 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.7.7-alt0.1
- 3.7.7

* Mon Aug 08 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.7.6-alt0.1
- 3.7.6

* Fri Jul 29 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.7.5-alt0.1
- 3.7.5

* Fri Jul 15 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.7.4-alt0.1
- 3.7.4

* Mon Apr 04 2005 Yuri N. Sedunov <aris@altlinux.ru> 3.6.2-alt1
- 3.6.2

* Tue Mar 15 2005 Yuri N. Sedunov <aris@altlinux.ru> 3.6.1-alt1
- 3.6.1

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 3.6.0-alt1
- 3.6.0

* Wed Mar 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 3.5.7-alt1
- 3.5.7

* Fri Feb 18 2005 Yuri N. Sedunov <aris@altlinux.ru> 3.5.6-alt1
- 3.5.6

* Sat Dec 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 3.2.4-alt1
- 3.2.4

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 3.2.3-alt1
- 3.2.3

* Thu Sep 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 3.2.2-alt1
- 3.2.2

* Tue Jul 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 3.1.17-alt1
- 3.1.17

* Sat Jun 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 3.1.16-alt1
- 3.1.16

* Fri May 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 3.1.14-alt1
- 3.1.14

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 3.1.12-alt1
- 3.3.12

* Tue Apr 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 3.1.11-alt1
- 3.1.11

* Sat Mar 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 3.1.9-alt1
- 3.1.9

* Tue Feb 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 3.1.8-alt1
- 3.1.8

* Fri Jan 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 3.1.7-alt1
- 3.1.7

* Mon Sep 22 2003 AEN <aen@altlinux.ru> 3.0.8-alt2
- added requires on %name to devel package

* Tue Aug 05 2003 AEN <aen@altlinux.ru> 3.0.8-alt1
- new version

* Fri Jul 11 2003 AEN <aen@altlinux.ru> 3.0.7-alt1
- release

* Thu Jul 03 2003 AEN <aen@altlinux.ru> 3.0.6-alt1
- new version from gnome cvs

* Wed Jun 18 2003 AEN <aen@altlinux.ru> 3.0.5-alt1
- first build for sisyphus

