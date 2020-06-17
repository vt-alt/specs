#%%set_verify_elf_method textrel=relaxed
%define _gtk_docdir %_datadir/gtk-doc/html
%define _libexecdir %_prefix/libexec
%define api_ver 1.0
%define gtk_ver 2.0

%define _name webkitgtk
# none/opengl/cairo/clutter
%define acceleration_backend opengl
%def_enable introspection
%def_enable geolocation
%def_enable web_audio
%def_disable media_stream
%def_enable spellcheck
%ifarch ppc64le
%def_disable jit
%endif
%def_disable check

%define smp %__nprocs

Name: libwebkitgtk2
Version: 2.4.11
Release: alt10

Summary: Web browser engine
License: LGPL-2.0 and LGPL-2.1 and BSD-2-Clause
Group: System/Libraries
Url: http://www.webkitgtk.org/

Source: http://webkitgtk.org/releases/webkitgtk-%version.tar.xz
Patch: webkitgtk-2.1.92-alt-gtk2_compatibility.patch
Patch3: webkitgtk-2.4.0-alt-link.patch
Patch4: webkitgtk-2.4.9-fc-abs.patch
# https://bugs.webkit.org/show_bug.cgi?id=171612
Patch5: webkitgtk-2.4.11-icu59.patch
# https://bugs.webkit.org/show_bug.cgi?id=126985
Patch6: webkitgtk-x86-assembler-fix.patch
Patch7: webkitgtk-2.4.10-suse-aarch64.patch
Patch8: webkitgtk-2.4.11-alt-build.patch
# python->python2
Patch9: webkitgtk-2.4.11-alt-python2.patch

Requires: libjavascriptcoregtk2 = %version-%release
%{?_enable_geolocation:Requires: geoclue2}

Provides: webkitgtk = %version-%release
Provides: libwebkit-gtk = %version-%release
Provides: libwebkit = %version-%release
Obsoletes: libwebkit-gtk < %version
Obsoletes: libwebkit < %version
Obsoletes: %name-webinspector
Provides: %name-webinspector = %EVR

BuildRequires(pre): rpm-build-licenses rpm-build-gir
BuildRequires: gcc-c++ libicu-devel bison perl-Switch zlib-devel
BuildRequires: flex >= 2.5.33
BuildRequires: gperf libjpeg-devel libpng-devel libwebp-devel
BuildRequires: libxml2-devel >= 2.6
BuildRequires: libXt-devel
BuildRequires: libgtk+2-devel >= 2.24.10
BuildRequires: libgail-devel >= 1.8
BuildRequires: libenchant-devel >= 0.22
BuildRequires: libsqlite3-devel >= 3.0
BuildRequires: libxslt-devel >= 1.1.7
BuildRequires: gstreamer1.0-devel >= 1.0.3 gst-plugins1.0-devel >= 1.0.3
BuildRequires: librsvg-devel >= 2.2.0
BuildRequires: gtk-doc >= 1.10
BuildRequires: libsoup-devel >= 2.42.0
BuildRequires: libsecret-devel
BuildRequires: libpango-devel >= 1.30.0 libcairo-devel >= 1.10 libcairo-gobject-devel
BuildRequires: fontconfig-devel >= 2.5 libfreetype-devel libharfbuzz-devel >= 0.9.7
BuildRequires: libgio-devel >= 2.25.0
BuildRequires: /usr/bin/python2 python-modules-json
BuildRequires: ruby ruby-stdlibs

%if %acceleration_backend == opengl
BuildRequires: libGL-devel libXcomposite-devel libXdamage-devel
%endif

%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= 1.32.0 libgtk+2-gir-devel libsoup-gir-devel}
%{?_enable_geolocation:BuildPreReq: geoclue2-devel}
%{?_enable_spellcheck:BuildPreReq: libenchant-devel}
%{?_enable_media_stream:BuildPreReq: farstream0.2-devel}
%{?_enable_check:BuildRequires: xvfb-run python-module-pygobject3}

%description
WebKit is an open source web browser engine.
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%package devel
Summary: Development files for WebKit GTK+ port
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Requires: libjavascriptcoregtk2-devel = %version-%release
Provides: webkitgtk-devel = %version-%release
Provides: libwebkit-gtk-devel = %version-%release
Provides: libwebkit-devel = %version-%release
Obsoletes: libwebkit-gtk-devel < %version
Obsoletes: libwebkit-devel < %version

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

%package -n libjavascriptcoregtk2
Summary: GTK+2 version of the JavaScriptCore engine
Group: System/Libraries

%description -n libjavascriptcoregtk2
This package provides GTK+2 version of the JavaScriptCore engine from
WebKit package.

%package -n libjavascriptcoregtk2-devel
Summary: Development files for JavaScriptCore library
Group: Development/GNOME and GTK+
Requires: libjavascriptcoregtk2 = %version-%release

%description -n libjavascriptcoregtk2-devel
This package provides development files for GTK+2 version of the
JavaScriptCore engine.

%package jsc
Summary: JavaScriptCore shell for WebKit GTK+
Group: Development/GNOME and GTK+
Requires: libjavascriptcoregtk2 = %version-%release
Provides: libwebkit-jsc = %version-%release
Obsoletes: libwebkit-jsc < %version

%description jsc
jsc is a shell for JavaScriptCore, WebKit's JavaScript engine. It
allows you to interact with the JavaScript engine directly.

%package gir
Summary: GObject introspection data for the WebkitGTK library
Group: System/Libraries
Requires: %name = %version-%release
Requires: libjavascriptcoregtk2 = %version-%release
Requires: libjavascriptcoregtk2-gir  = %version-%release
Provides: libwebkit-gir = %version-%release
Obsoletes: libwebkit-gir < %version

%description gir
GObject introspection data for the WebkitGTK library

%package gir-devel
Summary: GObject introspection devel data for the WebkitGTK library
Group: Development/GNOME and GTK+
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: libjavascriptcoregtk2-gir = %version-%release
Requires: libjavascriptcoregtk2-devel = %version-%release
Requires: libjavascriptcoregtk2-gir-devel = %version-%release
Provides: libwebkit-gir-devel = %version-%release
Obsoletes: libwebkit-gir-devel < %version

%description gir-devel
GObject introspection devel data for the WebkitGTK library

%package -n libjavascriptcoregtk2-gir
Summary: GObject introspection data for the JavaScriptCore library
Group: System/Libraries
Requires: libjavascriptcoregtk2 = %version-%release

%description -n libjavascriptcoregtk2-gir
GObject introspection data for the JavaScriptCore library

%package -n libjavascriptcoregtk2-gir-devel
Summary: GObject introspection devel data for the JavaScriptCore library
Group: Development/GNOME and GTK+
BuildArch: noarch
Requires: libjavascriptcoregtk2-gir = %version-%release
Requires: libjavascriptcoregtk2-devel = %version-%release

%description -n libjavascriptcoregtk2-gir-devel
GObject introspection devel data for the JavaScriptCore library

%prep
%setup -n webkitgtk-%version
%patch
%patch3
%patch4 -p1
%patch5
%patch6 -p2
%patch7 -p1
%patch8 -b .orig
%patch9 -p1

# fix build translations
%__subst 's|^all-local:|all-local: stamp-po|' GNUmakefile.am
rm -f Source/autotools/{compile,config.guess,config.sub,depcomp,install-sh,ltmain.sh,missing,libtool.m4,ltoptions.m4,ltsugar.m4,ltversion.m4,lt~obsolete.m4,gsettings.m4,gtk-doc.m4}

%build
%ifarch ppc64le
%add_optflags -DENABLE_YARR_JIT=0
%endif
%add_optflags -Wno-expansion-to-defined -Wno-implicit-fallthrough
# Use linker flags to reduce memory consumption
%add_optflags -Wl,--no-keep-memory -Wl,--reduce-memory-overheads

# Build with -g1 on all platforms to avoid running into 4 GB ar format limit
# https://bugs.webkit.org/show_bug.cgi?id=91154
%define optflags_debug -g1

echo "GTK_DOC_CHECK([1.10])" >> configure.ac
gtkdocize --copy
export PYTHON=python2
%autoreconf -I Source/autotools
%configure \
	--enable-video \
	--with-acceleration-backend=%acceleration_backend \
	--enable-webgl \
	%{subst_enable introspection} \
	%{subst_enable geolocation} \
	%{?_enable_web_audio:--enable-web-audio} \
	%{?_enable_media_stream:--enable-media-stream} \
	--with-gtk=%gtk_ver \
	--disable-webkit2 \
	%{subst_enable jit} \
	PYTHON=%_bindir/python2

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

#cleanup
rm -rf %buildroot%_includedir/webkitgtk-1.0/webkit2

%find_lang WebKitGTK-2.0

%check
xvfb-run make check

%files -f WebKitGTK-2.0.lang
%_libdir/lib%_name-%api_ver.so.*
%dir %_datadir/%_name-%api_ver
%_datadir/%_name-%api_ver/images
%_datadir/%_name-%api_ver/resources

%files devel
%_libdir/lib%_name-%api_ver.so
%dir %_includedir/%_name-%api_ver
%_includedir/%_name-%api_ver/webkit/
%_includedir/%_name-%api_ver/webkitdom/
%_pkgconfigdir/webkit-%api_ver.pc

%files devel-doc
%_gtk_docdir/*

%files -n libjavascriptcoregtk2
%_libdir/libjavascriptcoregtk-%api_ver.so.*

%files -n libjavascriptcoregtk2-devel
%_includedir/%_name-%api_ver/JavaScriptCore/
%_libdir/libjavascriptcoregtk-%api_ver.so
%_pkgconfigdir/javascriptcoregtk-%api_ver.pc

%files jsc
%_bindir/jsc*

%if_enabled introspection
%files gir
%_typelibdir/WebKit-%api_ver.typelib

%files gir-devel
%_girdir/WebKit-%api_ver.gir

%files -n libjavascriptcoregtk2-gir
%_typelibdir/JavaScriptCore-%api_ver.typelib

%files -n libjavascriptcoregtk2-gir-devel
%_girdir/JavaScriptCore-%api_ver.gir
%endif

%changelog
* Sat Apr 11 2020 Yuri N. Sedunov <aris@altlinux.org> 2.4.11-alt10
- switched to python2 for build

* Wed Mar 18 2020 Yuri N. Sedunov <aris@altlinux.org> 2.4.11-alt9
- rebuilt against icu-66 libraries
- fixed license tag

* Tue Oct 22 2019 Yuri N. Sedunov <aris@altlinux.org> 2.4.11-alt8
- rebuilt against icu-65.1 libraries

* Mon Feb 11 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.4.11-alt7
- Fixed build on ppc64le architecture.

* Mon Oct 22 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.11-alt6
- rebuilt against libicu*.so.63

* Wed Jul 25 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.11-alt5
- rebuilt against libicu*.so.62

* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.11-alt4
- rebuilt against libicu*.so.60

* Tue Jun 20 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.11-alt3
- rebuilt against libwebp.so.7

* Mon Jan 30 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.11-alt2.1
- really disabled JIT compilation for %%ix586

* Sun Jan 29 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.11-alt2
- fixed build with gcc6
- disabled JIT compilation for %%ix586 (ALT #32732)

* Sun Apr 10 2016 Yuri N. Sedunov <aris@altlinux.org> 2.4.11-alt1
- 2.4.11 (CVE-2015-1120, CVE-2015-1076, CVE-2015-1071, CVE-2015-1081, CVE-2015-1122,
 CVE-2015-1155, CVE-2014-1748, CVE-2015-3752, CVE-2015-5809, CVE-2015-5928, CVE-2015-3749,
 CVE-2015-3659, CVE-2015-3748, CVE-2015-3743, CVE-2015-3731, CVE-2015-3745, CVE-2015-5822,
 CVE-2015-3658, CVE-2015-3741, CVE-2015-3727, CVE-2015-5801, CVE-2015-5788, CVE-2015-3747,
 CVE-2015-5794, CVE-2015-1127, CVE-2015-1153, CVE-2015-1083)

* Wed Feb 10 2016 Yuri N. Sedunov <aris@altlinux.org> 2.4.9-alt4
- rebuild against libicu*.so.56

* Sun Jan 24 2016 Yuri N. Sedunov <aris@altlinux.org> 2.4.9-alt3
- rebuilt against libwebp.so.6

* Wed May 27 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.9-alt2
- rebuilt for updated dependencies

* Wed May 20 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.9-alt1
- 2.4.9
- dropped upstreamed patches

* Tue May 05 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.8-alt3
- rebuilt with geoclue2

* Sun Apr 05 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.8-alt1
- 2.4.8
- fixed build with glib-2.44

* Wed Oct 01 2014 Yuri N. Sedunov <aris@altlinux.org> 2.2.8-alt1
- 2.2.8

* Sat Feb 22 2014 Yuri N. Sedunov <aris@altlinux.org> 2.2.5-alt1
- 2.2.5

* Sat Jan 04 2014 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt2
- rebuilt against libwebp.so.5

* Wed Dec 04 2013 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt1
- 2.2.3

* Fri Sep 27 2013 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Thu Sep 19 2013 Yuri N. Sedunov <aris@altlinux.org> 2.1.92-alt1
- 2.1.92
- no more separate -webinspector subpackage

* Mon Jul 29 2013 Alexey Shabalin <shaba@altlinux.ru> 2.0.4-alt1
- 2.0.4
- enable web audio

* Wed Apr 10 2013 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Tue Dec 18 2012 Alexey Shabalin <shaba@altlinux.ru> 1.10.2-alt1
- 1.10.2
- fixed CVE-2012-5112, CVE-2012-5133

* Wed Nov 14 2012 Alexey Shabalin <shaba@altlinux.ru> 1.10.1-alt2
- rebuild with libicu-5.1

* Fri Oct 19 2012 Alexey Shabalin <shaba@altlinux.ru> 1.10.1-alt1
- 1.10.1

* Mon Oct 08 2012 Alexey Shabalin <shaba@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Wed Aug 29 2012 Alexey Shabalin <shaba@altlinux.ru> 1.8.3-alt1
- 1.8.3

* Mon Aug 06 2012 Alexey Shabalin <shaba@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Fri May 11 2012 Alexey Shabalin <shaba@altlinux.ru> 1.8.1-alt1
- 1.8.1
- sync spec with libwebkitgtk3

* Wed Feb 08 2012 Alexey Shabalin <shaba@altlinux.ru> 1.6.3-alt1
- 1.6.3
- drop upstreamed patch3

* Fri Oct 28 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt4
- add %%set_verify_elf_method textrel=relaxed and don't apply patch2

* Thu Oct 27 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt3
- fix webkit.pc

* Tue Oct 25 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt2
- add javascriptcoregtk2* subpackages

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

* Fri Mar 04 2011 Alexey Shabalin <shaba@altlinux.ru> 1.3.12-alt1
- 1.3.12
- disable image resize

* Fri Jan 21 2011 Alexey Shabalin <shaba@altlinux.ru> 1.3.10-alt1
- 1.3.10
- enable blob

* Mon Dec 13 2010 Alexey Shabalin <shaba@altlinux.ru> 1.3.7-alt1
- 1.3.7

* Wed Nov 17 2010 Alexey Shabalin <shaba@altlinux.ru> 1.3.6-alt1
- 1.3.6
- enable mathml, 3D-transforms, geolocation, coverage

* Tue Oct 19 2010 Alexey Shabalin <shaba@altlinux.ru> 1.3.4-alt2
- fix obsoletes

* Mon Oct 04 2010 Alexey Shabalin <shaba@altlinux.ru> 1.3.4-alt1
- 1.3.4
- build with libgtk+2
- rename to libwebkitgtk2

* Mon Oct 04 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Sun Jul 18 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.3-alt2
- package webinspector as noarch
- fix manual provides to libwebkit-1.0.so.2.17.5

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

