%define _name totem-pl-parser
%define ver_major 3.26
%define api_ver 1.0
%define _libexecdir %_prefix/libexec

%def_enable gtk_doc
%def_enable introspection
%def_enable libgcrypt
%def_disable quvi

Name: lib%_name
Version: %ver_major.3
Release: alt2

Summary: Shared libraries of the Totem media player play list parser
Group: System/Libraries
License: GPL
Url: http://www.hadess.net/%_name.php3

#Source: %_name-%version.tar
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

%define glib_ver 2.34
%define soup_ver 2.43
%define quvi_ver 0.9.1
%define archive_ver 3.0

%{?_enable_quvi:Requires: libquvi-scripts0.9 >= %quvi_ver}

BuildRequires(pre): meson
BuildRequires: gtk-doc libgio-devel >= %glib_ver
BuildRequires: libarchive-devel >= %archive_ver
BuildRequires: libgcrypt-devel libxml2-devel
%{?_enable_libgcrypt:BuildRequires: libgcrypt-devel}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= 0.9.5}
%{?_enable_quvi:BuildRequires: libquvi0.9-devel >= %quvi_ver}

%description
Shared libraries that come with the Totem media player.

%package devel
Summary: Development files for Totem media player play list parser
Group: Development/C
Requires: %name = %version-%release

%description devel
Totem is simple movie player for the Gnome desktop based on Xine.
This package provides files needed to build applications using Totem
libraries.

%package devel-doc
Summary: Development documentation for Totem media player play list parser
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
Totem is simple movie player for the Gnome desktop based on Xine.
This package contains documentation needed to develop applications using Totem
libraries.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Totem playlist parser library

%package gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Totem playlist parser library


%prep
%setup -n %_name-%version

%build
%meson \
	%{?_enable_gtk_doc:-Denable-gtk-doc=true} \
	%{?_enable_libgcrypt:-Denable-libgcrypt=yes} \
	%{?_enable_quvi:-Denable-quvi=yes}
%meson_build

%install
%meson_install

%find_lang --with-gnome --output=%name.lang %_name %_name-2.0

%files -f %name.lang
%_libdir/*.so.*
%if_enabled quvi
%dir %_libexecdir/%_name
%_libexecdir/%_name/99-%_name-videosite
%endif
%doc AUTHORS NEWS README

%files -n %name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n %name-devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_typelibdir/TotemPlParser-%api_ver.typelib

%files gir-devel
%_girdir/TotemPlParser-%api_ver.gir
%endif

%changelog
* Mon Jul 15 2019 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt2
- disabled obsolete quvi support

* Tue Mar 05 2019 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt1
- 3.26.3

* Wed Jan 16 2019 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Thu Jun 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Thu Sep 14 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Wed Jun 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.10.8-alt1
- 3.10.8

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.10.7-alt1
- 3.10.7

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.10.6-alt1
- 3.10.6

* Thu Apr 30 2015 Yuri N. Sedunov <aris@altlinux.org> 3.10.5-alt1
- 3.10.5

* Tue Feb 17 2015 Yuri N. Sedunov <aris@altlinux.org> 3.10.4-alt1
- 3.10.4

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.3-alt1
- 3.10.3

* Mon Sep 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt2
- rebuilt against libquvi-0.9-0.9.4.so

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2
- use current automake

* Tue Feb 18 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Wed Nov 06 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt2
- use automake-1.11

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.4.5-alt1
- 3.4.5

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.4.4-alt1
- 3.4.4

* Mon Mar 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt2
- rebuilt against libarchive.so.13

* Tue Sep 18 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt1
- 3.4.3

* Sat May 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt2
- rebuild against libquvi.so.7 (libquvi-0.4.1)

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Wed Apr 18 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt2
- removed obsolete Provides/Conflicts (ALT #27241)

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Feb 20 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Sep 20 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.6-alt1
- 2.32.6

* Fri Jul 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.5-alt2
- rebuild aganst quvi-0.2.8

* Thu May 12 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.5-alt1
- 2.32.5

* Tue Mar 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.4-alt1
- 2.32.4

* Fri Jan 28 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt1
- 2.32.2

* Mon Nov 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt2
- rebuild for update dependencies

* Mon Oct 18 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Thu Oct 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Thu Sep 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.92-alt1
- 2.31.2

* Mon Sep 13 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Wed Aug 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Wed May 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Mon Mar 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.1-alt2
- rebuild using rpm-build-gir

* Wed Jan 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.1-alt1
- 2.29.1

* Fri Dec 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Tue Sep 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1
- buildreqs glib2-devel >= 2.21.6

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Tue Sep 15 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92
- updated buildreqs

* Mon May 04 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Tue Mar 31 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Tue Mar 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Thu Mar 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Fri Jan 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.1-alt1
- 2.25.1

* Mon Dec 08 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3
- removed obsolete %%post{,un}_ldconfig

* Thu Oct 30 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- new devel-doc noarch subpackage

* Tue Oct 07 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Mon Sep 29 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0
- fixed url
- don't rebuild documentation
- remove excess buildreqs

* Wed May 28 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.3-alt2
- Add conflicts with libtotem-xine and libtotem-gstreamer

* Fri May 09 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.3-alt1
- 2.22.3

* Wed Apr 09 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.2-alt1
- 2.22.2

* Tue Mar 11 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.1-alt1
- 2.22.1
