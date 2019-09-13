%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name pango
%define ver_major 1.44
%define api_ver 1.0
%define module_ver 1.8.0
%def_disable static
%def_enable docs
%def_enable introspection
%def_enable installed_tests
%def_enable fontconfig
%def_disable check

Name: lib%_name
Version: %ver_major.6
Release: alt1

Summary: System for layout and rendering of internationalized text
License: %lgpl2plus
Group: System/Libraries
Url: http://www.pango.org/

%if_disabled snapshot
Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

Source10: pango-compat.map
Source11: pango-compat.lds
Source12: pangoft2-compat.map
Source13: pangoft2-compat.lds
Source14: pangocairo-compat.map
Source15: pangocairo-compat.lds

Patch: pango-1.44.3-alt-compat-version-script.patch

Provides: %_name = %version
Obsoletes: %_name < %version
Obsoletes: gscript

# From meson.build
%define glib_ver 2.60
%define cairo_ver 1.12.10
%define gtk_doc_ver 1.0
%define xft_ver 2.0.0
%define fontconfig_ver 2.11.91
%define freetype_ver 2.1.4
%define gi_ver 0.9.5
%define hb_ver 2.0.0
%define thai_ver 0.1.9
%define fribidi_ver 0.19.7

BuildRequires(pre): meson rpm-build-gnome rpm-build-licenses gtk-doc
BuildRequires: gcc-c++ 
BuildPreReq: libfreetype-devel >= %freetype_ver
BuildPreReq: libXft-devel >= %xft_ver
BuildPreReq: libcairo-devel >= %cairo_ver libcairo-gobject-devel
BuildPreReq: glib2-devel >= %glib_ver libgio-devel
BuildPreReq: libharfbuzz-devel >= %hb_ver
BuildPreReq: libfribidi-devel >= %fribidi_ver
BuildPreReq: libthai-devel >= %thai_ver}
BuildRequires: help2man /proc
%{?_enable_fontconfig:BuildPreReq: fontconfig-devel >= %fontconfig_ver}
%{?_enable_docs:BuildRequires: gtk-doc >= %gtk_doc_ver}
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= %gi_ver}
%{?_enable_check:BuildRequires: fonts-otf-abattis-cantarell fonts-ttf-thai-scalable-waree}

%description
A library to handle unicode strings as well as complex bidirectional
or context dependent shaped strings.

%package devel
Summary: Development libraries and header files for pango
Group: Development/C
Provides: %_name-devel = %version
Obsoletes: %_name-devel < %version
Requires: %name = %version-%release

%description devel
The pango-devel package includes the libraries and header files
for the pango package.

%package devel-doc
Summary: Development documentation for Pango
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
Pango is a library to handle unicode strings as well as complex
bidirectional or context dependent shaped strings.

This package contains development documentation for Pango.

%if_enabled static
%package devel-static
Summary: Static libraries for pango
Group: Development/C

%description devel-static
The pango-devel package includes the static libraries for the pango package.
%endif

%package gir
Summary: GObject introspection data for the Pango library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Pango library

%package gir-devel
Summary: GObject introspection devel data for the Pango library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Pango library

%package tests
Summary: Tests for the Pango library
Group: Development/Other
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed Pango library.


%prep
%setup -n %_name-%version
%patch -b .vs
install -p -m644 %_sourcedir/pango{,ft2,cairo}-compat.{map,lds} pango/

%build
%meson \
    %{?_enable_fontconfig:-Duse_fontconfig=true} \
    %{?_enable_introspection:-Dintrospection=true} \
    %{?_enable_docs:-Dgtk_doc=true} \
    %{?_enable_installed_tests:-Dinstall-tests=true}
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_bindir/%_name-list
%_bindir/%_name-view
%_libdir/%name-%api_ver.so.*
%_libdir/%{name}cairo-%api_ver.so.*
%_libdir/%{name}ft2-%api_ver.so.*
%_libdir/%{name}xft-%api_ver.so.*
%_man1dir/%_name-view.*
%doc NEWS README*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled introspection
%files gir
%_typelibdir/Pango-%api_ver.typelib
%_typelibdir/PangoCairo-%api_ver.typelib
%_typelibdir/PangoFc-%api_ver.typelib
%_typelibdir/PangoFT2-%api_ver.typelib
%_typelibdir/PangoOT-%api_ver.typelib
%_typelibdir/PangoXft-%api_ver.typelib

%files gir-devel
%_girdir/*
%endif

%if_enabled docs
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%if_enabled static
%files devel-static
%_libdir/*.a
%_libdir/%_name/%module_ver/*/*.a
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name/
%_datadir/installed-tests/%_name/
%endif


%changelog
* Tue Sep 03 2019 Yuri N. Sedunov <aris@altlinux.org> 1.44.6-alt1
- 1.44.6

* Wed Aug 14 2019 Yuri N. Sedunov <aris@altlinux.org> 1.44.5-alt1
- 1.44.5 (ported to Meson build system)

* Mon Aug 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.42.4-alt1
- 1.42.4

* Mon Jul 30 2018 Yuri N. Sedunov <aris@altlinux.org> 1.42.3-alt1
- 1.42.3

* Thu Jul 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1.42.2-alt1
- 1.42.2

* Sat Apr 07 2018 Yuri N. Sedunov <aris@altlinux.org> 1.42.1-alt1
- 1.42.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 1.42.0-alt1
- 1.42.0

* Thu Nov 16 2017 Yuri N. Sedunov <aris@altlinux.org> 1.40.14-alt1
- 1.40.14

* Sat Oct 28 2017 Yuri N. Sedunov <aris@altlinux.org> 1.40.13-alt1
- 1.40.13

* Mon Sep 04 2017 Yuri N. Sedunov <aris@altlinux.org> 1.40.12-alt1
- 1.40.12

* Sat Aug 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.40.11-alt1
- 1.40.11

* Wed Aug 16 2017 Yuri N. Sedunov <aris@altlinux.org> 1.40.10-alt1
- 1.40.10

* Fri Aug 11 2017 Yuri N. Sedunov <aris@altlinux.org> 1.40.9-alt1
- 1.40.9

* Mon Aug 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.40.8-alt1
- 1.40.8

* Tue Jul 18 2017 Yuri N. Sedunov <aris@altlinux.org> 1.40.7-alt1
- 1.40.7

* Mon May 29 2017 Yuri N. Sedunov <aris@altlinux.org> 1.40.6-alt1
- 1.40.6

* Sat Apr 08 2017 Yuri N. Sedunov <aris@altlinux.org> 1.40.5-alt1
- 1.40.5

* Wed Mar 01 2017 Yuri N. Sedunov <aris@altlinux.org> 1.40.4-alt1
- 1.40.4

* Tue Sep 13 2016 Yuri N. Sedunov <aris@altlinux.org> 1.40.3-alt1
- 1.40.3

* Mon Aug 29 2016 Yuri N. Sedunov <aris@altlinux.org> 1.40.2-alt1
- 1.40.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1.40.1-alt1
- 1.40.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.40.0-alt1
- 1.40.0

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 1.38.1-alt1
- 1.38.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 1.38.0-alt1
- 1.38.0

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 1.36.8-alt1
- 1.36.8
- libthai support enabled

* Thu Sep 04 2014 Yuri N. Sedunov <aris@altlinux.org> 1.36.7-alt1
- 1.36.7

* Thu Aug 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.36.6-alt1
- 1.36.6

* Tue Jun 24 2014 Yuri N. Sedunov <aris@altlinux.org> 1.36.5-alt1
- 1.36.5

* Tue Mar 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.36.3-alt1
- 1.36.3

* Wed Feb 05 2014 Yuri N. Sedunov <aris@altlinux.org> 1.36.2-alt1
- 1.36.2

* Mon Nov 11 2013 Yuri N. Sedunov <aris@altlinux.org> 1.36.1-alt1
- 1.36.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 1.36.0-alt1
- 1.36.0

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 1.34.1-alt1
- 1.34.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 1.34.0-alt1
- 1.34.0

* Thu Jan 17 2013 Yuri N. Sedunov <aris@altlinux.org> 1.32.6-alt2
- aen@: reverted http://git.gnome.org/browse/pango/commit/?id=2dc0c3dbb1c389c3a3ba12a5c5c85f21dca46e84 (ALT #28355)

* Thu Jan 10 2013 Yuri N. Sedunov <aris@altlinux.org> 1.32.6-alt1
- 1.32.6

* Tue Dec 18 2012 Yuri N. Sedunov <aris@altlinux.org> 1.32.5-alt1
- 1.32.5

* Fri Dec 07 2012 Yuri N. Sedunov <aris@altlinux.org> 1.32.4-alt1
- 1.32.4

* Tue Nov 20 2012 Yuri N. Sedunov <aris@altlinux.org> 1.32.3-alt1
- 1.32.3

* Wed Nov 14 2012 Yuri N. Sedunov <aris@altlinux.org> 1.32.2-alt1
- 1.32.2

* Thu Nov 08 2012 Dmitry V. Levin <ldv@altlinux.org> 1.32.1-alt2
- Packaged %_libdir/%_name/%_name-querymodules hard link to
  %_bindir/%_name-querymodules, changed %%post script
  to use this hard link (closes: #25938).

* Fri Sep 28 2012 Yuri N. Sedunov <aris@altlinux.org> 1.32.1-alt1
- 1.32.1

* Tue Jun 05 2012 Yuri N. Sedunov <aris@altlinux.org> 1.30.1-alt1
- 1.30.1
- removed obsolete pango-1.28.4-alt-modules.patch
- added --system option to pango-querymodules in %%post

* Sun May 20 2012 Yuri N. Sedunov <aris@altlinux.org> 1.30.0-alt2
- made check.defs always true

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 1.30.0-alt1
- 1.30.0

* Wed Nov 23 2011 Yuri N. Sedunov <aris@altlinux.org> 1.29.5-alt1
- 1.29.5

* Tue Oct 11 2011 Yuri N. Sedunov <aris@altlinux.org> 1.29.4-alt2
- applied patch proposed by ldv@ for ALT #25938

* Tue Oct 11 2011 Yuri N. Sedunov <aris@altlinux.org> 1.29.4-alt1
- 1.29.4

* Mon Oct 10 2011 Dmitry V. Levin <ldv@altlinux.org> 1.28.4-alt1
- Updated to 1.28.4.
- /etc/pango/pango.modules: do not store absolute pathnames
  for default modules (closes: #25938).

* Wed Mar 02 2011 Yuri N. Sedunov <aris@altlinux.org> 1.28.3-alt4
- fixed CVE-20100-00{20,64} (ALT #25181)

* Sat Feb 12 2011 Alexey Tourbin <at@altlinux.ru> 1.28.3-alt3
- rebuilt for debuginfo
- disabled symbol versioning

* Sun Jan 09 2011 Yuri N. Sedunov <aris@altlinux.org> 1.28.3-alt2
- added missing pango_gravity_get_for_script_and_width (ALT #24881)

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 1.28.3-alt1
- 1.28.3

* Tue Jun 15 2010 Yuri N. Sedunov <aris@altlinux.org> 1.28.1-alt1
- 1.28.1
- updated version script for PANGOFT2_1.28.1

* Wed Mar 31 2010 Yuri N. Sedunov <aris@altlinux.org> 1.28.0-alt1
- 1.28.0

* Tue Mar 09 2010 Yuri N. Sedunov <aris@altlinux.org> 1.26.2-alt2
- rebuild using rpm-build-gir

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 1.27.1-alt2
- rebuild using rpm-build-gir

* Tue Feb 23 2010 Yuri N. Sedunov <aris@altlinux.org> 1.27.1-alt1
- 1.27.1

* Tue Dec 15 2009 Yuri N. Sedunov <aris@altlinux.org> 1.26.2-alt1
- 1.26.2

* Wed Nov 18 2009 Yuri N. Sedunov <aris@altlinux.org> 1.26.1-alt1
- 1.26.1

* Tue Nov 10 2009 Yuri N. Sedunov <aris@altlinux.org> 1.26.0-alt2
- shaba@: new gir{,-devel} packages

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 1.26.0-alt1
- 1.26.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 1.25.6-alt1
- 1.25.6

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 1.25.5-alt1
- 1.25.5

* Tue Aug 18 2009 Yuri N. Sedunov <aris@altlinux.org> 1.25.4-alt1
- 1.25.4

* Thu Aug 13 2009 Yuri N. Sedunov <aris@altlinux.org> 1.25.3-alt1
- 1.25.3

* Tue Aug 11 2009 Yuri N. Sedunov <aris@altlinux.org> 1.25.2-alt1
- 1.25.2
- updated buildreqs

* Tue Jul 21 2009 Yuri N. Sedunov <aris@altlinux.org> 1.24.5-alt1
- 1.24.5

* Tue Jun 30 2009 Yuri N. Sedunov <aris@altlinux.org> 1.24.4-alt1
- 1.24.4

* Mon Jun 22 2009 Yuri N. Sedunov <aris@altlinux.org> 1.24.3-alt1
- 1.24.3 

* Tue May 05 2009 Yuri N. Sedunov <aris@altlinux.org> 1.24.2-alt1
- 1.24.2

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 1.24.1-alt1
- 1.24.1

* Wed Mar 18 2009 Yuri N. Sedunov <aris@altlinux.org> 1.24.0-alt1
- 1.24.0
- updated version script for PANGOFT2

* Tue Dec 16 2008 Yuri N. Sedunov <aris@altlinux.org> 1.22.4-alt1
- 1.22.4

* Sun Nov 23 2008 Yuri N. Sedunov <aris@altlinux.org> 1.22.3-alt1
- 1.22.3
- remove obsolete ldconfig in %%post{,un}

* Wed Oct 29 2008 Yuri N. Sedunov <aris@altlinux.org> 1.22.2-alt1
- 1.22.2

* Tue Oct 21 2008 Yuri N. Sedunov <aris@altlinux.org> 1.22.1-alt1
- 1.22.1
- don't rebuild documentation

* Fri Sep 26 2008 Alexey Shabalin <shaba@altlinux.ru> 1.22.0-alt1
- 1.22.0

* Wed Jul 02 2008 Yuri N. Sedunov <aris@altlinux.org> 1.20.5-alt1
- 1.20.5

* Sun Jun 08 2008 Yuri N. Sedunov <aris@altlinux.org> 1.20.3-alt1
- 1.20.3

* Tue Mar 11 2008 Alexey Rusakov <ktirf@altlinux.org> 1.20.0-alt1
- New version (1.20.0).

* Wed Mar 05 2008 Alexey Rusakov <ktirf@altlinux.org> 1.19.4-alt1
- New version (1.19.4).
- Added symbols versioning.
- Massive spec cleanup.
- Added tests invocation when building.

* Thu Sep 20 2007 Igor Zubkov <icesik@altlinux.org> 1.18.2-alt1
- 1.16.2 -> 1.18.2

* Wed May 16 2007 Alexey Rusakov <ktirf@altlinux.org> 1.16.2-alt1
- new version (1.16.2)
- updated dependencies; removed some from -devel subpackage, letting
  pkgconfig to do the work; expect some small sisy-quake.

* Wed Jan 31 2007 Alexey Rusakov <ktirf@altlinux.org> 1.14.10-alt1
- new version 1.14.10 (with rpmrb script)

* Mon Dec 25 2006 Alexey Rusakov <ktirf@altlinux.org> 1.14.9-alt1
- new version 1.14.9 (with rpmrb script)

* Sat Oct 14 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.14.7-alt1
- new version 1.14.7 (with rpmrb script)

* Fri Oct 13 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.14.6-alt1
- new version 1.14.6 (with rpmrb script)

* Fri Oct 06 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.14.5-alt1
- new version (1.14.5)
- fixed building on x86_64.

* Sat Sep 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.14.4-alt1
- new version 1.14.4 (with rpmrb script)

* Tue Sep 05 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.14.3-alt1
- new version 1.14.3 (with rpmrb script)

* Thu Aug 24 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.14.2-alt1
- new version 1.14.2 (with rpmrb script)

* Thu Aug 10 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.14.0-alt2
- updated versions of required packages.
- made the list of files more accurate.

* Wed Aug 09 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.14.0-alt1
- new version 1.14.0 (with rpmrb script)

* Fri Jul 21 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.13.0-alt1
- new version 1.13.0, for GTK-on-DirectFB project.

* Sun May 28 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.12.3-alt1
- new version 1.12.3 (with rpmrb script)

* Sun Apr 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.12.2-alt1
- new version 1.12.2 (with rpmrb script)

* Sat Apr 08 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.12.1-alt1
- new version 1.12.1 (with rpmrb script)

* Wed Mar 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.12.0-alt1
- new version 1.12.0 (with rpmrb script)

* Sun Mar 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.11.99-alt1
- new version (1.11.99)

* Wed Feb 22 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.11.6-alt1
- new version

* Sun Feb 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.11.5-alt1
- new version

* Sat Feb 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.11.4-alt1
- new version
- the viewer is now gtk-based and is included in libpango package.

* Tue Oct 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.10.1-alt1
- new version

* Mon Aug 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Sat Mar 05 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Thu Dec 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Fri Dec 03 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.7.0-alt1
- 1.7.0
- documentation moved to devel-doc subpackage. 

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Wed Mar 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Tue Mar 09 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.3.6-alt1
- 1.3.6
- prereqs libXft (close #3794)

* Tue Mar 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.3.5-alt1
- 1.3.5

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.3.3-alt1
- 1.3.3

* Fri Jan 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Fri Jan 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.3.1-alt2
- make relaxed libXft dependencies.

* Wed Dec 31 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2.5-alt1
- 1.2.5
- do not package .la files.

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Tue Jun 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Fri May 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2.2-alt1
- 1.2.2
- groups changed to System/Libraries.

* Tue Feb 18 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt2
- Add caching of fontsets (patch from cvs).

* Mon Feb 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Sat Dec 21 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Tue Dec 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Wed Dec 11 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Wed Dec 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Sun Nov 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Tue Oct 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Thu Oct 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.1-alt1
- 1.1.1
- Building static libraries disabled to prevent dependencies on
  Xft version 1.

* Fri Sep 20 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.4-alt2
- Removed wrong dependencies (#1287).

* Mon Sep 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.4-alt1
- 1.0.4
- (inger) made qt-viewer building optional (use --with viewer to build it)
- (inger) update buildreqs

* Mon Jun 24 2002 Igor Androsov <blake@altlinux.ru> 1.0.3-alt2
- Removed "fixed-ltmains.sh"
	+ SMP-compatible build
	+ other small fixes and cleanups.
- Rename source package (libpango -> pango)	
- rebuild with new freetype2

* Fri Jun 14 2002 Igor Androsov <blake@altlinux.ru> 1.0.3-alt1
- New release

* Sun Jun 02 2002 Igor Androsov <blake@altlinux.ru> 1.0.2-alt3
- Fixed lost gtk-doc documentation

* Wed May 29 2002 Igor Androsov <blake@altlinux.ru> 1.0.2-alt2
- Return removed in 1.0.1-alt2 "fixed-ltmains.sh" - fixed no building package if host wheare building not have libpango.

* Tue May 28 2002 Igor Androsov <blake@altlinux.ru> 1.0.2-alt1
- New release

* Wed May 22 2002 Igor Androsov <blake@altlinux.ru> 1.0.1-alt2
- Fix gtk-doc dir

* Sun Mar 31 2002 AEN <aen@logic.ru> 1.0.1-alt1
- new version

* Wed Mar 27 2002 AEN <aen@logic.ru> 1.0.0-alt1
- release

* Thu Jan 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.23.90-alt2
- fix bug #0000091

* Wed Jan 09 2002 AEN <aen@logic.ru> 0.23.90-alt1
- new version

* Wed Oct 17 2001 AEN <aen@logic.ru> 0.20-alt1
- new version

* Tue Sep 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.18-alt2
- Corrected requires.

* Fri Sep 21 2001 Stanislav Ievlev <inger@altlinux.ru> 0.18-alt1
- 0.18

* Mon Aug 13 2001 AEN <aen@logic.ru> 0.17-alt2
- freetype2 patch

* Mon Jun 18 2001 AEN <aen@logic.ru> 0.17-alt1
- new version
- revised reauires

* Thu May 31 2001 Stanislav Ievlev <inger@altlinux.ru> 0.16-alt1
- 0.16

* Fri Apr 20 2001 Stanislav Ievlev <inger@altlinux.ru> 0.15-alt1
- Up to 0.15

* Fri Mar 30 2001 Stanislav Ievlev <inger@altlinux.ru> 0.13-alt1
- Spec bugfix, librification and upgrade to 0.13

* Tue Jan 16 2001 AEN <aen@logic.ru>
- RE adaptations

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.9-3mdk
- automatically added BuildRequires

* Tue Apr 18 2000 Pixel <pixel@mandrakesoft.com> 0.9-2mdk
- fix %% post (was writing to %%/var/lib/pango instead of /var/lib/pango)

* Sat Apr 08 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 0.9-1mdk
- updated to 0.9
- corrected conflicts in %files section
- added orphaned directories & files

* Fri Mar 31 2000 John Buswell <johnb@mandrakesoft.com> 0.8-1mdk
- Initial Mandrake Release
- spec-helper
- fixed groups

* Fri Feb 11 2000 Owen Taylor <otaylor@redhat.com>
- Created spec file

