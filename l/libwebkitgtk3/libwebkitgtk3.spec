#%%set_verify_elf_method textrel=relaxed
%define _gtk_docdir %_datadir/gtk-doc/html
%define _libexecdir %_prefix/libexec
%add_verify_elf_skiplist %_libexecdir/WebKitPluginProcess
%define api_ver 3.0
%define gtk_ver 3.0

%define oname webkit
%define _name webkitgtk

# none/opengl/cairo/clutter
%define acceleration_backend opengl
%def_enable introspection
%def_enable geolocation
%def_enable web_audio
%def_enable spellcheck
%def_disable webkit2

%define smp %__nprocs

Name: libwebkitgtk3
Version: 2.4.11
Release: alt7

Summary: Web browser engine
Group: System/Libraries
License: %bsd %lgpl2plus

Url: http://www.webkitgtk.org

Source: %url/releases/%_name-%version.tar.xz
Patch1: webkitgtk-2.4.0-alt-link.patch
Patch2: webkitgtk-2.4.9-fc-abs.patch
# https://bugs.webkit.org/show_bug.cgi?id=171612
Patch3: webkitgtk-2.4.11-icu59.patch
# https://bugs.webkit.org/show_bug.cgi?id=126985
Patch4: webkitgtk-x86-assembler-fix.patch
Patch5: webkitgtk-2.4.10-suse-aarch64.patch

Obsoletes: %name-webinspector
Provides: %name-webinspector = %EVR

Requires: libjavascriptcoregtk3 = %version-%release

BuildRequires(pre): rpm-build-licenses rpm-build-gir
BuildRequires: gcc-c++ libicu-devel bison perl-Switch zlib-devel
BuildRequires: chrpath
BuildRequires: flex >= 2.5.33
BuildRequires: gperf libjpeg-devel libpng-devel libwebp-devel
BuildRequires: libxml2-devel >= 2.6
BuildRequires: libXt-devel
BuildRequires: libgtk+3-devel >= 3.4.0
BuildRequires: libgail3-devel >= 3.0
BuildRequires: libenchant-devel >= 0.22
BuildRequires: libsqlite3-devel >= 3.0
BuildRequires: libxslt-devel >= 1.1.7
BuildRequires: gstreamer1.0-devel >= 1.0.3 gst-plugins1.0-devel >= 1.0.3
BuildRequires: librsvg-devel >= 2.2.0
BuildRequires: gtk-doc >= 1.10
BuildRequires: libsoup-devel >= 2.40.0
BuildRequires: libsecret-devel
BuildRequires: libpango-devel >= 1.21.0 libcairo-devel >= 1.10 libcairo-gobject-devel
BuildRequires: fontconfig-devel >= 2.4 libfreetype-devel libharfbuzz-devel
BuildRequires: libgio-devel >= 2.25.0
BuildRequires: python-modules-json
BuildRequires: ruby ruby-stdlibs


%if %acceleration_backend == opengl
BuildRequires: libGL-devel libXcomposite-devel libXdamage-devel
%endif

%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= 0.9.5 libgtk+3-gir-devel libsoup-gir-devel}
%{?_enable_geolocation:BuildPreReq: geoclue2-devel}
%{?_enable_spellcheck:BuildPreReq: libenchant-devel}
%{?_enable_webkit2:BuildPreReq: libat-spi2-core-devel >= 2.2.1  libgtk+2-devel libgail-devel}

# for check
BuildRequires: xvfb-run python-module-pygobject3

%description
WebKit is an open source web browser engine.
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%package devel
Summary: Development files for WebKit GTK+ port
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Requires: libjavascriptcoregtk3-devel = %version-%release

%description devel
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux. This package contains development headers.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

This package provides development documentation for %name.

%package -n libjavascriptcoregtk3
Summary: GTK+3 version of the JavaScriptCore engine
Group: System/Libraries

%description -n libjavascriptcoregtk3
This package provides GTK+3 version of the JavaScriptCore engine from
WebKit package.

%package -n libjavascriptcoregtk3-devel
Summary: Development files for JavaScriptCore library
Group: Development/GNOME and GTK+
Requires: libjavascriptcoregtk3 = %version-%release

%description -n libjavascriptcoregtk3-devel
This package provides development files for GTK+3 version of the
JavaScriptCore engine.

%package -n libwebkit2gtk
Summary: WebKit2 is a new API layer for WebKit
Group: System/Libraries
Requires: libjavascriptcoregtk3 = %version-%release

%description -n libwebkit2gtk
WebKit2 is a new API layer for WebKit designed from the ground up to support a split process model,
where the web content (JavaScript, HTML, layout, etc) lives in a separate process from the application UI.
This model is very similar to what Google Chrome offers, with the major difference being
that we have built the process split model directly into the framework, allowing other clients of WebKit to use it.

%package -n libwebkit2gtk-devel
Summary: WebKit2 is a new API layer for WebKit
Group: Development/GNOME and GTK+
Requires: libwebkitgtk3-devel = %version-%release
Requires: libjavascriptcoregtk3-devel = %version-%release
Requires: libwebkit2gtk = %version-%release

%description -n libwebkit2gtk-devel
WebKit2 is a new API layer for WebKit designed from the ground up to support a split process model,
where the web content (JavaScript, HTML, layout, etc) lives in a separate process from the application UI.
This model is very similar to what Google Chrome offers, with the major difference being
that we have built the process split model directly into the framework, allowing other clients of WebKit to use it.


%package jsc
Summary: JavaScriptCore shell for WebKit GTK+
Group: Development/GNOME and GTK+
Requires: libjavascriptcoregtk3 = %version-%release

%description jsc
jsc is a shell for JavaScriptCore, WebKit's JavaScript engine. It
allows you to interact with the JavaScript engine directly.

%package gir
Summary: GObject introspection data for the WebkitGTK library
Group: System/Libraries
Requires: %name = %version-%release
Requires: libjavascriptcoregtk3 = %version-%release
Requires: libjavascriptcoregtk3-gir  = %version-%release

%description gir
GObject introspection data for the WebkitGTK library

%package gir-devel
Summary: GObject introspection devel data for the WebkitGTK library
Group: Development/GNOME and GTK+
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: libjavascriptcoregtk3-gir = %version-%release
Requires: libjavascriptcoregtk3-devel = %version-%release
Requires: libjavascriptcoregtk3-gir-devel = %version-%release

%description gir-devel
GObject introspection devel data for the WebkitGTK library

%package -n libjavascriptcoregtk3-gir
Summary: GObject introspection data for the JavaScriptCore library
Group: System/Libraries
Requires: libjavascriptcoregtk3 = %version-%release

%description -n libjavascriptcoregtk3-gir
GObject introspection data for the JavaScriptCore library

%package -n libjavascriptcoregtk3-gir-devel
Summary: GObject introspection devel data for the JavaScriptCore library
Group: Development/GNOME and GTK+
BuildArch: noarch
Requires: libjavascriptcoregtk3-gir = %version-%release
Requires: libjavascriptcoregtk3-devel = %version-%release

%description -n libjavascriptcoregtk3-gir-devel
GObject introspection devel data for the JavaScriptCore library

%package -n libwebkit2gtk-gir
Summary: GObject introspection data for the Webkit2 library
Group: System/Libraries
Requires: libwebkit2gtk = %version-%release

%description -n libwebkit2gtk-gir
GObject introspection data for the Webkit2 library

%package -n libwebkit2gtk-gir-devel
Summary: GObject introspection data for the Webkit2 library
Group: Development/GNOME and GTK+
BuildArch: noarch
Requires: libwebkit2gtk-gir = %version-%release
Requires: libwebkit2gtk-devel = %version-%release

%description -n libwebkit2gtk-gir-devel
GObject introspection data for the Webkit2 library

%prep
%setup -n %_name-%version
%patch1
%patch2 -p1
%patch3
%patch4 -p2
%patch5 -p1

# fix build translations
%__subst 's|^all-local:|all-local: stamp-po|' GNUmakefile.am
rm -f Source/autotools/{compile,config.guess,config.sub,depcomp,install-sh,ltmain.sh,missing,libtool.m4,ltoptions.m4,ltsugar.m4,ltversion.m4,lt~obsolete.m4,gsettings.m4,gtk-doc.m4}

%build
%add_optflags -Wno-expansion-to-defined -Wno-implicit-fallthrough
# Use linker flags to reduce memory consumption
%add_optflags -Wl,--no-keep-memory -Wl,--reduce-memory-overheads
%ifarch ppc ppc64 ppc64le
%add_optflags -DENABLE_YARR_JIT=0
%endif

# Build with -g1 on all platforms to avoid running into 4 GB ar format limit
# https://bugs.webkit.org/show_bug.cgi?id=91154
%define optflags_debug -g1

echo "GTK_DOC_CHECK([1.10])" >> configure.ac
gtkdocize --copy
%autoreconf -I Source/autotools
%configure \
%ifarch ppc ppc64 ppc64le
	--disable-jit \
%endif
	--enable-video \
	--with-acceleration-backend=%acceleration_backend \
	--enable-webgl \
	%{subst_enable introspection} \
	%{subst_enable geolocation} \
	%{?_enable_web_audio:--enable-web-audio} \
	%{subst_enable webkit2} \
	--with-gtk=%gtk_ver

mkdir -p DerivedSources/webkit
mkdir -p DerivedSources/ANGLE
mkdir -p DerivedSources/WebKit2/webkit2gtk/webkit2
mkdir -p DerivedSources/InjectedBundle
mkdir -p DerivedSources/webkitdom
mkdir -p DerivedSources/Platform
mkdir -p Programs/resources

n=%smp
[  "$n"  -lt  16  ]  ||  n=16
%make -j $n

%install
%makeinstall_std
%find_lang WebKitGTK-3.0

mkdir -p %buildroot%_libexecdir/%_name
install -m755 Programs/GtkLauncher %buildroot%_libexecdir/%_name/
chrpath --delete %buildroot%_libexecdir/%_name/GtkLauncher
%if_enabled webkit2
install -m755 Programs/MiniBrowser %buildroot%_libexecdir/%_name/
chrpath --delete %buildroot%_libexecdir/%_name/MiniBrowser
%endif

%files -f WebKitGTK-3.0.lang
%_libdir/libwebkitgtk-%api_ver.so.*
%_libexecdir/%_name/GtkLauncher
%dir %_datadir/webkitgtk-%api_ver
%_datadir/webkitgtk-%api_ver/images
%_datadir/webkitgtk-%api_ver/resources

%files devel
%_libdir/libwebkitgtk-%api_ver.so
%dir %_includedir/webkitgtk-%api_ver
%_includedir/webkitgtk-%api_ver/webkit
%_includedir/webkitgtk-%api_ver/webkitdom
%_pkgconfigdir/webkitgtk-%api_ver.pc

%files devel-doc
%_gtk_docdir/*

%files -n libjavascriptcoregtk3
%_libdir/libjavascriptcoregtk-%api_ver.so.*

%files -n libjavascriptcoregtk3-devel
%_includedir/webkitgtk-%api_ver/JavaScriptCore
%_libdir/libjavascriptcoregtk-%api_ver.so
%_pkgconfigdir/javascriptcoregtk-%api_ver.pc

%if_enabled webkit2
%files -n libwebkit2gtk
%_libdir/libwebkit2gtk-%api_ver.so.*
%_libexecdir/WebKitPluginProcess
%_libexecdir/WebKitWebProcess
%_libexecdir/WebKitNetworkProcess
%_libexecdir/%_name/MiniBrowser
%_libdir/webkit2gtk-%api_ver

%files -n libwebkit2gtk-devel
%_libdir/libwebkit2gtk-%api_ver.so
%_includedir/webkitgtk-%api_ver/webkit2
%_pkgconfigdir/webkit2gtk-%api_ver.pc
%_pkgconfigdir/webkit2gtk-web-extension-%api_ver.pc

%if_enabled introspection
%files -n libwebkit2gtk-gir
%_typelibdir/WebKit2-%api_ver.typelib
%_typelibdir/WebKit2WebExtension-%api_ver.typelib

%files -n libwebkit2gtk-gir-devel
%_girdir/WebKit2-%api_ver.gir
%_girdir/WebKit2WebExtension-%api_ver.gir
%endif
%endif

%files jsc
%_bindir/jsc*

%if_enabled introspection
%files gir
%_typelibdir/WebKit-%api_ver.typelib

%files gir-devel
%_girdir/WebKit-%api_ver.gir

%files -n libjavascriptcoregtk3-gir
%_typelibdir/JavaScriptCore-%api_ver.typelib

%files -n libjavascriptcoregtk3-gir-devel
%_girdir/JavaScriptCore-%api_ver.gir
%endif


%changelog
* Fri May 31 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.4.11-alt7
- Fixed build on ppc architectures.

* Mon Oct 22 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.11-alt6
- rebuilt against libicu*.so.63

* Wed Jul 25 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.11-alt5
- rebuilt against libicu*.so.62

* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.11-alt4
- rebuilt against libicu*.so.60

* Tue Jun 20 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.11-alt3
- rebuilt against libwebp.so.7

* Sun Jan 29 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.11-alt2
- fixed build with gcc6

* Fri Aug 19 2016 Yuri N. Sedunov <aris@altlinux.org> 2.4.11-alt1
- 2.4.11

* Mon Mar 14 2016 Yuri N. Sedunov <aris@altlinux.org> 2.4.10-alt1
- 2.4.10 (CVE-2015-1120, CVE-2015-1076, CVE-2015-1071, CVE-2015-1081,
  CVE-2015-1122, CVE-2015-1155, CVE-2014-1748, CVE-2015-3752,
  CVE-2015-5809, CVE-2015-5928, CVE-2015-3749, CVE-2015-3659,
  CVE-2015-3748, CVE-2015-3743, CVE-2015-3731, CVE-2015-3745,
  CVE-2015-5822, CVE-2015-3658, CVE-2015-3741, CVE-2015-3727,
  CVE-2015-5801, CVE-2015-5788, CVE-2015-3747, CVE-2015-5794,
  CVE-2015-1127, CVE-2015-1153, CVE-2015-1083)

* Wed Feb 10 2016 Yuri N. Sedunov <aris@altlinux.org> 2.4.9-alt4
- rebuild against libicu*.so.56

* Sun Jan 24 2016 Yuri N. Sedunov <aris@altlinux.org> 2.4.9-alt3
- rebuilt against libwebp.so.6

* Wed May 27 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.9-alt2
- rebuilt for updated dependencies

* Wed May 20 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.9-alt1
- 2.4.9
- dropped upstreamed patches

* Sun Apr 05 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.8-alt2
- fixed build with glib-2.44

* Sat Jan 10 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.8-alt1
- 2.4.8

* Sat Oct 25 2014 Yuri N. Sedunov <aris@altlinux.org> 2.4.7-alt1
- 2.4.7

* Mon Oct 06 2014 Yuri N. Sedunov <aris@altlinux.org> 2.4.6-alt1
- 2.4.6
- disabled webkit2

* Fri Aug 29 2014 Yuri N. Sedunov <aris@altlinux.org> 2.4.5-alt1
- 2.4.5

* Tue Jul 08 2014 Yuri N. Sedunov <aris@altlinux.org> 2.4.4-alt1
- 2.4.4

* Fri Jun 06 2014 Yuri N. Sedunov <aris@altlinux.org> 2.4.3-alt1
- 2.4.3

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 2.4.2-alt1
- 2.4.2

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Tue Mar 18 2014 Yuri N. Sedunov <aris@altlinux.org> 2.3.92-alt1
- 2.3.92

* Fri Feb 21 2014 Yuri N. Sedunov <aris@altlinux.org> 2.2.5-alt1
- 2.2.5

* Tue Jan 21 2014 Yuri N. Sedunov <aris@altlinux.org> 2.2.4-alt1
- 2.2.4

* Sat Jan 04 2014 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt2
- rebuilt against libwebp.so.5

* Wed Dec 04 2013 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt1
- 2.2.3

* Mon Nov 11 2013 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Wed Oct 16 2013 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Fri Sep 27 2013 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Thu Sep 19 2013 Yuri N. Sedunov <aris@altlinux.org> 2.1.92-alt1
- 2.1.92
- no more separate -webinspector subpackage

* Fri Aug 23 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.4-alt2
- rebuild against new harfbuzz
- enabled webaudio

* Sun Jul 21 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.4-alt1
- 2.0.4

* Wed Jun 12 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- 2.0.3

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Mon Apr 01 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt2
- update symbols.filter for WebkitPluginProcess

* Wed Mar 27 2013 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Thu Mar 21 2013 Alexey Shabalin <shaba@altlinux.ru> 1.11.92-alt1
- 1.11.92

* Thu Mar 07 2013 Alexey Shabalin <shaba@altlinux.ru> 1.11.91-alt1
- 1.11.91

* Fri Feb 22 2013 Alexey Shabalin <shaba@altlinux.ru> 1.11.90-alt1
- 1.11.90

* Wed Feb 20 2013 Alexey Shabalin <shaba@altlinux.ru> 1.11.5-alt1
- 1.11.5

* Mon Dec 17 2012 Alexey Shabalin <shaba@altlinux.ru> 1.10.2-alt1
- 1.10.2
- fixed CVE-2012-5112, CVE-2012-5133

* Wed Nov 14 2012 Alexey Shabalin <shaba@altlinux.ru> 1.10.1-alt2
- rebuild with libicu-5.1

* Fri Oct 19 2012 Alexey Shabalin <shaba@altlinux.ru> 1.10.1-alt1
- 1.10.1

* Mon Sep 24 2012 Alexey Shabalin <shaba@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Wed Aug 29 2012 Alexey Shabalin <shaba@altlinux.ru> 1.8.3-alt1
- 1.8.3

* Mon Aug 06 2012 Alexey Shabalin <shaba@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Fri May 25 2012 Alexey Shabalin <shaba@altlinux.ru> 1.8.1-alt2
- update and cleanup configure option
- enable some features:
  + page-visibility-api
  + style-scoped
  + link-prefetch
  + animation-api
- add and fixed webkit2 support, but not enable; welcome for tests

* Fri May 11 2012 Alexey Shabalin <shaba@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Wed Mar 28 2012 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Tue Feb 07 2012 Alexey Shabalin <shaba@altlinux.ru> 1.6.3-alt1
- 1.6.3

* Wed Feb 01 2012 Alexey Shabalin <shaba@altlinux.ru> 1.6.2-alt1
- 1.6.2
- drop upstreamed patch3

* Fri Oct 28 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt4
- add %%set_verify_elf_method textrel=relaxed and don't apply patch2

* Thu Oct 27 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt3
- fix webkit.pc

* Tue Oct 25 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt2
- add javascriptcoregtk3* subpackages

* Mon Oct 17 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Wed Aug 31 2011 Alexey Shabalin <shaba@altlinux.ru> 1.4.3-alt1
- 1.4.3

* Tue Jul 12 2011 Alexey Shabalin <shaba@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Fri Apr 29 2011 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Tue Mar 22 2011 Alexey Shabalin <shaba@altlinux.ru> 1.3.13-alt1
- 1.3.13

* Thu Mar 10 2011 Alexey Shabalin <shaba@altlinux.ru> 1.3.12-alt1
- 1.3.12
- disable image resize
- update conditions

* Thu Jan 20 2011 Alexey Shabalin <shaba@altlinux.ru> 1.3.10-alt1
- 1.3.10
- enable blob

* Wed Dec 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.3.7-alt1
- 1.3.7
- enable mathml, 3D-transforms, geolocation, coverage

* Mon Oct 04 2010 Alexey Shabalin <shaba@altlinux.ru> 1.3.4-alt1
- 1.3.4

* Mon Jul 19 2010 Alexey Shabalin <shaba@altlinux.ru> 1.3.3-alt1
- 1.3.3
- build with libgtk+3
- rename to libwebkitgtk3

* Sun Jul 18 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.3-alt1
- 1.2.3
- disable patch1(webkit-1.1.23-alt-icu4.4.patch); upstream fixed
- fixed the following CVEs (thanks to the Debian security team):
  + CVE-2010-1386 CVE-2010-1392 CVE-2010-1405 CVE-2010-1407
  + CVE-2010-1416 CVE-2010-1417 CVE-2010-1665 CVE-2010-1418
  + CVE-2010-1421 CVE-2010-1422 CVE-2010-1501 CVE-2010-1767
  + CVE-2010-1664 CVE-2010-1758 CVE-2010-1759 CVE-2010-1760
  + CVE-2010-1761 CVE-2010-1762 CVE-2010-1770 CVE-2010-1771
  + CVE-2010-1772 CVE-2010-1773 CVE-2010-1774

* Tue May 18 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Thu Apr 22 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- current stable release 1.2.0

* Tue Mar 30 2010 Alexey Shabalin <shaba@altlinux.ru> 1.1.90-alt1
- 1.1.90

* Mon Mar 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.1.23-alt2
- rebuild with icu-4.4
- disable Patch0 WebKit-alt-plugins.patch

* Fri Mar 12 2010 Alexey Shabalin <shaba@altlinux.ru> 1.1.23-alt1
- 1.1.23
- package gir-devel as noarch

* Wed Feb 24 2010 Alexey Shabalin <shaba@altlinux.ru> 1.1.22-alt1
- 1.1.22

* Tue Feb 09 2010 Alexey Shabalin <shaba@altlinux.ru> 1.1.21-alt1
- 1.1.21
- new gir{,-devel} subpackages

* Thu Dec 03 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.15.4-alt1
- 1.1.15.4

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.15.3-alt1
- 1.1.15.3

* Fri Oct 09 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.15.2-alt1
- 1.1.15.2

* Wed Sep 23 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.15.1-alt1
- 1.1.15.1

* Thu Sep 10 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.14-alt1
- 1.1.14

* Tue Aug 25 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.13-alt1
- release 1.1.13

* Thu Aug 20 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.12-alt1.r46499
- 1.1.12
- nightly builds r46499

* Tue Jul 14 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.11-alt1.r45855
- nightly builds r45855
- fixed CVE-2009-1724, CVE-2009-1725, webkit: #27136,#27110,#26918,#27071 (ALT#20761)

* Tue Jun 23 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.10-alt2.r44815
- rebuild with libpng12

* Sat Jun 20 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.10-alt1.r44815
- nightly builds r44815
- drop gtklauncher package
- build with freetype font backend

* Thu May 14 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.7-alt1.r43663
- nightly builds r43663

* Wed May 06 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.6-alt1.r43284
- nightly builds r43284

* Tue May 05 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.6-alt1.r43000
- nightly builds r43000
- update BuildRequires

* Sun Apr 05 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.4-alt1.r42162
- nightly builds r42162
- update buildrequires
- build with gnome-keyring support
- thx to shrek@ :
  + fixed plugins path
  + fixed install GtkLauncher

* Fri Jan 16 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1.r39953
- nightly builds 39953
- webinspector package

* Mon Dec 08 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1.r39060
- nightly builds 39090
- drop obsolete post scripts

* Sat Oct 25 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt0.3.r37790
- nightly builds 37790
- http_backend soup
- font_backend pango

* Sun Sep 07 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt0.2.r36247
- nightly builds 36247

* Mon Sep 01 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt0.2.r35933
- nightly builds r35933

* Fri Aug 22 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt0.2.r35417
- fix build for x86_64
- define libexecdir as /usr/libexec

* Thu Aug 21 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt0.1.r35417
- 1.0.2 (r35704)
- cleanup spec
- rename package from libwebkit-gtk to libwebkit
- add package %name-gtklauncher and %name-jsc

* Tue Mar 11 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.r30716-alt1 
- new version
- libWebKitGtk.so placed into -devel package.
- changed includes dir

* Fri Nov 16 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.r27953-alt1 
- initital build.

