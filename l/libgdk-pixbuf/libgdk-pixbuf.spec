%def_disable snapshot

%define _name gdk-pixbuf
%define api_ver 2.0
%define binary_ver 2.10.0
%define ver_major 2.38
%define _libexecdir %_prefix/libexec

%def_enable gtk_doc
%def_enable man
%def_enable introspection
%def_enable x11
%def_enable libjasper
%def_enable installed_tests
%def_enable check

Name: lib%_name
Version: %ver_major.2
Release: alt1

Summary: An image loading and rendering library for Gdk
Group: System/Libraries
License: LGPL
Url: http://www.gtk.org

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif
Patch: %_name-2.37.92-alt-compat-version-script.patch
Patch1: %_name-2.38.1-alt-tests_timeouts.patch

Source1: %_name.map
Source2: %_name.lds

%define glib_ver 2.48.0
%define gi_ver 0.9.5

Requires: %name-locales = %version

Provides: %name-loaders = %version
Obsoletes: %name-loaders <= %version

BuildRequires(pre): meson rpm-build-gir
BuildRequires: /proc libgio-devel >= %glib_ver
BuildRequires: libjpeg-devel libpng-devel libtiff-devel
BuildRequires: docbook-utils gtk-doc
%{?_enable_x11:BuildRequires: libX11-devel}
%{?_enable_libjasper:BuildRequires: libjasper-devel}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= %gi_ver}

%description
The GdkPixBuf library provides a number of features:
+ Image loading facilities.
+ Rendering of a GdkPixBuf into various formats:
  drawables (windows, pixmaps), GdkRGB buffers.

%package xlib
Summary: An image loading and rendering library for Gdk
Group: System/Libraries
Requires: %name = %version-%release

%description xlib
The GdkPixBuf library provides a number of features:
+ Image loading facilities.
+ Rendering of a GdkPixBuf into various formats:
  drawables (windows, pixmaps), GdkRGB buffers.

This package provides Xlib version of %name.

%package locales
Summary: Internationalization for GdkPixBuf library
Group: System/Internationalization
Conflicts: %name < %version-%release
BuildArch: noarch

%description locales
This package provides internationalization support for GdkPixBuf,
an image loading and rendering library for Gdk.

%package devel
Summary: Development files for GdkPixBuf applications
Group: Development/C
Requires: %name = %version-%release
Requires: %name-xlib = %version-%release

%description devel
GdkPixBuf is an image loading and rendering library for Gdk.

This package provides include files needed for developing GdkPixBuf
applications.

%package devel-doc
Summary: Development documentation for GdkPixBuf library
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
GdkPixBuf is an image loading and rendering library for Gdk.

This package provides documentation needed for developing GdkPixBuf
applications.

%package gir
Summary: GObject introspection data for the GdkPixBuf library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GdkPixBuf library

%package gir-devel
Summary: GObject introspection devel data for the GdkPixBuf library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the GdkPixBuf library

%package tests
Summary: Tests for the GdkPixBuf library
Group: Development/Other
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed GdkPixBuf library.


%prep
%setup -n %_name-%version
%patch -p1 -b .alt
%patch1 -b .timeout

install -p -m644 %_sourcedir/%_name.map %_name/compat.map
install -p -m644 %_sourcedir/%_name.lds %_name/compat.lds

%build
%ifarch %e2k
# till lcc ~1.23
export LIBS=-lcxa
%endif
%meson \
	%{?_enable_gtk_doc:-Ddocs=true} \
	%{?_enable_man:-Dman=true} \
	%{?_enable_introspection:-Dgir=true} \
	%{?_enable_x11:-Dx11=true} \
	%{?_enable_libjasper:-Djasper=true} \
	%{?_disable_installed_tests:-Dinstalled_tests=false} \
	-Dbuiltin_loaders='png'

%meson_build

%install
%meson_install

ln %buildroot%_bindir/%_name-query-loaders %buildroot%_libdir/%_name-%api_ver/%binary_ver/

# rpm posttrans filetriggers
mkdir -p %buildroot%_rpmlibdir
cat > %buildroot%_rpmlibdir/gdk-pixbuf-loaders.filetrigger << '@@@'
#!/bin/sh -efu

LC_ALL=C sed -rn 's|(^/usr/lib(64)?)/gdk-pixbuf.*/loaders/.*|\1|p' | sort -u | while read L; do
       if [ -x "$L/%_name-%api_ver/%binary_ver/%_name-query-loaders" ]; then
              $L/%_name-%api_ver/%binary_ver/%_name-query-loaders --update-cache
       fi
done
@@@
chmod 755 %buildroot%_rpmlibdir/gdk-pixbuf-loaders.filetrigger
touch %buildroot%_libdir/%_name-%api_ver/%binary_ver/loaders.cache

%find_lang %_name

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files
%_bindir/gdk-pixbuf-query-loaders
%_bindir/gdk-pixbuf-thumbnailer
%_libdir/libgdk_pixbuf-2.0.so.*
%dir %_libdir/%_name-%api_ver
%dir %_libdir/%_name-%api_ver/%binary_ver
%dir %_libdir/%_name-%api_ver/%binary_ver/loaders
%_libdir/%_name-%api_ver/%binary_ver/%_name-query-loaders
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-ani.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-bmp.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-gif.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-icns.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-ico.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-jpeg.so
#%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-png.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-pnm.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-qtif.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-tga.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-tiff.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-xbm.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-xpm.so
%{?_enable_libjasper:%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-jasper.so}
%ghost %_libdir/%_name-%api_ver/%binary_ver/loaders.cache
%_datadir/thumbnailers/gdk-pixbuf-thumbnailer.thumbnailer
%_man1dir/gdk-pixbuf-query-loaders*
%_rpmlibdir/gdk-pixbuf-loaders.filetrigger

%if_enabled x11
%files xlib
%_libdir/libgdk_pixbuf_xlib-2.0.so.*
%endif
%doc NEWS README.md

%files locales -f %_name.lang

%files devel
%_bindir/gdk-pixbuf-csource
%_bindir/%_name-pixdata
%_libdir/*.so
%dir %_includedir/%_name-%api_ver
%_includedir/%_name-%api_ver/%_name
%_pkgconfigdir/%_name-%api_ver.pc
%if_enabled x11
%_includedir/%_name-%api_ver/%_name-xlib
%_pkgconfigdir/%_name-xlib-%api_ver.pc
%endif
%_man1dir/gdk-pixbuf-csource*

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_typelibdir/GdkPixbuf-%api_ver.typelib
%_typelibdir/GdkPixdata-%api_ver.typelib

%files gir-devel
%_girdir/GdkPixbuf-%api_ver.gir
%_girdir/GdkPixdata-%api_ver.gir
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name/
%_datadir/installed-tests/%_name/
%endif


%changelog
* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 2.38.2-alt1
- 2.38.2

* Fri Apr 05 2019 Yuri N. Sedunov <aris@altlinux.org> 2.38.1-alt1.1
- tests/meson.build: x10 timeouts for overloaded girar

* Thu Feb 28 2019 Yuri N. Sedunov <aris@altlinux.org> 2.38.1-alt1
- 2.38.1
- enabled %check again

* Fri Jan 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2.38.0-alt4
- disabled %%check

* Thu Jan 10 2019 Yuri N. Sedunov <aris@altlinux.org> 2.38.0-alt3
- tests/pixbuf-threads: use g_fopen instead of fopen (fixed by upstream)

* Sun Sep 23 2018 Yuri N. Sedunov <aris@altlinux.org> 2.38.0-alt2
- updated to 2.38.0-26-g9f7d6969

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 2.38.0-alt1
- 2.38.0

* Mon Jun 25 2018 Yuri N. Sedunov <aris@altlinux.org> 2.36.12-alt2
- rebuilt against libjasper.so.4

* Sun Apr 08 2018 Yuri N. Sedunov <aris@altlinux.org> 2.36.12-alt1
- 2.36.12

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 2.36.11-alt1
- 2.36.11

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 2.36.10-alt1
- 2.36.10

* Sat Aug 19 2017 Yuri N. Sedunov <aris@altlinux.org> 2.36.9-alt1
- 2.36.9

* Mon Aug 07 2017 Yuri N. Sedunov <aris@altlinux.org> 2.36.8-alt1
- 2.36.8

* Tue Jul 18 2017 Yuri N. Sedunov <aris@altlinux.org> 2.36.7-alt1
- 2.36.7

* Sun Mar 26 2017 Yuri N. Sedunov <aris@altlinux.org> 2.36.6-alt1
- 2.36.6

* Fri Mar 17 2017 Michael Shigorin <mike@altlinux.org> 2.36.5-alt1.1
- E2K: force linking against -lcxa

* Mon Feb 13 2017 Yuri N. Sedunov <aris@altlinux.org> 2.36.5-alt1
- 2.36.5

* Mon Jan 16 2017 Yuri N. Sedunov <aris@altlinux.org> 2.36.4-alt1
- 2.36.4

* Wed Jan 11 2017 Yuri N. Sedunov <aris@altlinux.org> 2.36.3-alt2
- updated to 2.36.3-8-gbab37cd (fixed BGO ##442452, 768062, 776945)
- enabled %%check again
- fixed build without x11 support (ALT #32987)

* Fri Jan 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.36.3-alt1
- 2.36.3
- built with included png module

* Tue Dec 20 2016 Yuri N. Sedunov <aris@altlinux.org> 2.36.2-alt1
- 2.36.2

* Wed Dec 14 2016 Yuri N. Sedunov <aris@altlinux.org> 2.36.1-alt2
- updated to 2.36.1-10-g9e7cd8b

* Tue Dec 13 2016 Yuri N. Sedunov <aris@altlinux.org> 2.36.1-alt1
- 2.36.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 2.36.0-alt1
- 2.36.0

* Thu Mar 24 2016 Yuri N. Sedunov <aris@altlinux.org> 2.34.0-alt1
- 2.34.0

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 2.32.3-alt1
- 2.32.3

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt1
- 2.32.2

* Fri Sep 25 2015 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Sep 01 2015 Yuri N. Sedunov <aris@altlinux.org> 2.31.7-alt1
- 2.31.7

* Mon Jul 20 2015 Yuri N. Sedunov <aris@altlinux.org> 2.31.5-alt1
- 2.31.5

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 2.31.4-alt1
- 2.31.4

* Sun Mar 08 2015 Yuri N. Sedunov <aris@altlinux.org> 2.31.3-alt1
- 2.31.3

* Wed Nov 26 2014 Yuri N. Sedunov <aris@altlinux.org> 2.31.2-alt1
- 2.31.2 (some tests failed, check temporarily disabled)

* Sat Sep 27 2014 Yuri N. Sedunov <aris@altlinux.org> 2.31.1-alt1
- 2.31.1

* Wed Sep 10 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.30.8-alt2
- Fix gdk-pixbuf-loaders.filetrigger.

* Tue May 27 2014 Yuri N. Sedunov <aris@altlinux.org> 2.30.8-alt1
- 2.30.8

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 2.30.7-alt1
- 2.30.7

* Tue Mar 04 2014 Yuri N. Sedunov <aris@altlinux.org> 2.30.6-alt1
- 2.30.6
- glebfm@:
  packaged %%_libdir/%%_name-%%api_ver/%%binary_ver/%%_name-query-loaders
  hard link to %%_bindir/gdk-pixbuf-query-loaders, changed filetrigger
  to use this hardlink.

* Tue Feb 18 2014 Yuri N. Sedunov <aris@altlinux.org> 2.30.5-alt1
- 2.30.5

* Tue Feb 04 2014 Yuri N. Sedunov <aris@altlinux.org> 2.30.4-alt1
- 2.30.4

* Tue Jan 14 2014 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Tue Dec 17 2013 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Mon Nov 11 2013 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Sat Jun 08 2013 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Sat Nov 10 2012 Yuri N. Sedunov <aris@altlinux.org> 2.26.5-alt1
- 2.26.5

* Tue Sep 18 2012 Yuri N. Sedunov <aris@altlinux.org> 2.26.4-alt1
- 2.26.4

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Sat Apr 14 2012 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Sat Dec 31 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sat Aug 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Tue Aug 16 2011 Yuri N. Sedunov <aris@altlinux.org> 2.23.5-alt1
- 2.23.5

* Sat Jun 25 2011 Yuri N. Sedunov <aris@altlinux.org> 2.23.4-alt2
- fixed CVE-2011-2485 (ALT #25816)

* Tue Jun 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.23.4-alt1
- 2.23.4

* Thu Mar 31 2011 Yuri N. Sedunov <aris@altlinux.org> 2.23.3-alt1
- 2.23.3

* Sat Mar 05 2011 Yuri N. Sedunov <aris@altlinux.org> 2.23.1-alt1
- 2.23.1

* Thu Feb 17 2011 Alexey Tourbin <at@altlinux.ru> 2.23.0-alt2
- merged libgdk-pixbuf-loaders into libgdk-pixbuf
- split libgdk-pixbuf-locales noarch subpackage
- disabled symbol versioning

* Thu Dec 23 2010 Yuri N. Sedunov <aris@altlinux.org> 2.23.0-alt1
- 2.23.0

* Sat Nov 06 2010 Yuri N. Sedunov <aris@altlinux.org> 2.22.1-alt1
- 2.22.1

* Tue Oct 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt3
- try to unset GDK_PIXBUF_MODULEDIR before gdk-pixbuf-query-loaders call

* Mon Oct 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt2
- reduced priority for gdk-pixbuf-query-loaders-2.0.filetrigger
  (closes #24352)

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt1
- 2.22.0

* Fri Sep 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.7-alt1
- 2.21.7

* Tue Aug 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.6-alt1
- 2.21.6

* Tue Jun 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.5-alt1
- first build for Sisyphus

