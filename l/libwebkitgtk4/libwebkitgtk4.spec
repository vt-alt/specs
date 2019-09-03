%set_verify_elf_method textrel=relaxed
%define _gtk_docdir %_datadir/gtk-doc/html
%define _libexecdir %_prefix/libexec
%define api_ver 4.0
%define pkglibexecdir %_libexecdir/webkit2gtk-%api_ver
%define ver_major 2.24
%define gtk_ver 3.0
%define gst_ver 1.14.3

%define oname webkit
%define _name webkitgtk

%def_disable gtkdoc
%def_enable gold
%def_enable x11
%def_enable wayland
# since 2.19.x in some build environments
# while build webki2gtk-dep typelibs this error appears
# FATAL: Could not allocate gigacage memory with maxAlignment = ..
# To avoid it set GIGACAGE_ENABLED=0
%def_enable gigacage

%define smp %__nprocs

Name: libwebkitgtk4
Version: %ver_major.4
Release: alt1

Summary: Web browser engine
Group: System/Libraries
License: %bsd %lgpl2plus
Url: https://www.webkitgtk.org/

Source: %url/releases/%_name-%version.tar.xz
Source1: webkit2gtk.env

Requires: gst-plugins-base1.0 >= %gst_ver gst-plugins-good1.0 gst-plugins-bad1.0 gst-libav
Requires: hyphen-en hyphen-ru

BuildRequires(pre): rpm-build-licenses rpm-build-gir
BuildRequires: /proc gcc-c++ cmake ccache libicu-devel >= 5.6.1 bison perl-Switch perl-JSON-PP zlib-devel
BuildRequires: chrpath
BuildRequires: flex >= 2.5.33
BuildRequires: gperf libjpeg-devel libpng-devel libwebp-devel libopenjpeg2.0-devel openjpeg-tools2.0
BuildRequires: libxml2-devel >= 2.6
BuildRequires: libXt-devel
BuildRequires: libgtk+3-devel >= 3.4.0 libepoxy-devel
BuildRequires: libgail3-devel >= 3.0
BuildRequires: libenchant2-devel >= 2.2.3
BuildRequires: libsqlite3-devel >= 3.0
BuildRequires: libxslt-devel >= 1.1.7
BuildRequires: gstreamer1.0-devel >= %gst_ver gst-plugins1.0-devel >= %gst_ver gst-plugins-bad1.0-devel
BuildRequires: librsvg-devel >= 2.2.0
BuildRequires: gtk-doc >= 1.10
BuildRequires: libsoup-devel >= 2.61.90
BuildRequires: libsecret-devel
BuildRequires: libpango-devel >= 1.21.0 libcairo-devel >= 1.10 libcairo-gobject-devel
BuildRequires: fontconfig-devel >= 2.4 libfreetype-devel libharfbuzz-devel libwoff2-devel
BuildRequires: libgio-devel >= 2.25.0
BuildRequires: python-modules-json
BuildRequires: ruby ruby-stdlibs libruby-devel
BuildRequires: libGL-devel libXcomposite-devel libXdamage-devel
BuildRequires: gobject-introspection-devel >= 0.9.5 libgtk+3-gir-devel libsoup-gir-devel
BuildRequires: geoclue2-devel libgeoclue2-devel
BuildRequires: libenchant-devel libhyphen-devel
BuildRequires: libat-spi2-core-devel at-spi2-atk-devel
BuildRequires: libgtk+2-devel libpixman-devel libexpat-devel

BuildRequires: libXdmcp-devel libxshmfence-devel libXxf86vm-devel
BuildRequires: libXinerama-devel libXi-devel libXrandr-devel
BuildRequires: libXcursor-devel libxkbcommon-devel
%{?_enable_wayland:BuildRequires: libwayland-server-devel libwayland-cursor-devel libwayland-egl-devel}
BuildRequires: libnotify-devel libgnutls-devel libnettle-devel
BuildRequires: libtasn1-devel libp11-kit-devel libgcrypt-devel
# for battery status
BuildRequires: libupower-devel

%description
WebKit is an open source web browser engine.
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%package -n libwebkit2gtk
Summary: WebKit2 is a new API layer for WebKit
Group: System/Libraries
Provides: %name = %version-%release
Requires: libjavascriptcoregtk4 = %version-%release

%description -n libwebkit2gtk
WebKit2 is a new API layer for WebKit designed from the ground up to support a split process model,
where the web content (JavaScript, HTML, layout, etc) lives in a separate process from the application UI.
This model is very similar to what Google Chrome offers, with the major difference being
that we have built the process split model directly into the framework, allowing other clients of WebKit to use it.

%package -n %_name-minibrowser
Summary: Simple WebKit browser
Group: Networking/WWW
Requires: libwebkit2gtk = %version-%release

%description -n %_name-minibrowser
This package provides simple browser from webkitgtk project.

%package -n libwebkit2gtk-devel
Summary: Development files for WebKit GTK+ port
Group: Development/C++
Provides: %name-devel = %version-%release
Requires: libwebkit2gtk = %version-%release
Requires: libjavascriptcoregtk4-devel = %version-%release

%description -n libwebkit2gtk-devel
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux. This package contains development headers.

%package -n libwebkit2gtk-devel-doc
Summary: Development documentation for WebKit2GTK
Group: Development/Documentation
BuildArch: noarch
Conflicts: libwebkit2gtk < %version-%release

%description -n libwebkit2gtk-devel-doc
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

This package provides development documentation for WebKit2GTK.

%package -n libjavascriptcoregtk4
Summary: GTK+3 version of the JavaScriptCore engine
Group: System/Libraries

%description -n libjavascriptcoregtk4
This package provides GTK+3 version of the JavaScriptCore engine from
WebKit package.

%package -n libjavascriptcoregtk4-devel
Summary: Development files for JavaScriptCore library
Group: Development/C++
Requires: libjavascriptcoregtk4 = %version-%release

%description -n libjavascriptcoregtk4-devel
This package provides development files for GTK+3 version of the
JavaScriptCore engine.

%package -n jsc4
Summary: JavaScriptCore shell for WebKit GTK+
Group: Development/GNOME and GTK+
Requires: libjavascriptcoregtk4 = %version-%release
# since 2.14.1 jsc moved to %pkglibexecdir
#Conflicts: jsc

%description -n jsc4
jsc is a shell for JavaScriptCore, WebKit's JavaScript engine. It
allows you to interact with the JavaScript engine directly.

%package -n libwebkit2gtk-gir
Summary: GObject introspection data for the Webkit2GTK library
Group: System/Libraries
Requires: libwebkit2gtk = %version-%release
Requires: libjavascriptcoregtk4 = %version-%release
Requires: libjavascriptcoregtk4-gir  = %version-%release

%description -n libwebkit2gtk-gir
GObject introspection data for the Webkit2GTK library

%package -n libwebkit2gtk-gir-devel
Summary: GObject introspection devel data for the Webkit2GTK library
Group: Development/Other
BuildArch: noarch
Requires: libwebkit2gtk-gir = %version-%release
Requires: libwebkit2gtk-devel = %version-%release
Requires: libjavascriptcoregtk4-gir = %version-%release
Requires: libjavascriptcoregtk4-devel = %version-%release
Requires: libjavascriptcoregtk4-gir-devel = %version-%release

%description -n libwebkit2gtk-gir-devel
GObject introspection devel data for the Webkit2GTK library

%package -n libjavascriptcoregtk4-gir
Summary: GObject introspection data for the JavaScriptCore library
Group: System/Libraries
Requires: libjavascriptcoregtk4 = %version-%release

%description -n libjavascriptcoregtk4-gir
GObject introspection data for the JavaScriptCore library

%package -n libjavascriptcoregtk4-gir-devel
Summary: GObject introspection devel data for the JavaScriptCore library
Group: Development/Other
BuildArch: noarch
Requires: libjavascriptcoregtk4-gir = %version-%release
Requires: libjavascriptcoregtk4-devel = %version-%release

%description -n libjavascriptcoregtk4-gir-devel
GObject introspection devel data for the JavaScriptCore library

%prep
%setup -n %_name-%version
# Remove bundled libraries
rm -rf Source/ThirdParty/gtest/
rm -rf Source/ThirdParty/qunit/

subst 's|Q\(unused-arguments\)|W\1|' Source/cmake/WebKitCompilerFlags.cmake

%build
# Decrease debuginfo verbosity and use linker flags to reduce memory consumption
%define optflags_debug -g1
%add_optflags -Wl,--no-keep-memory
%{?_disable_gold: %add_optflags -Wl,--reduce-memory-overheads}
%ifarch %ix86
%add_optflags -D_FILE_OFFSET_BITS=64
# since 2.24.1 sse2 required for %%ix86
%add_optflags -msse2 -mfpmath=sse
%endif

%ifarch x86_64
n=%smp
[  "$n"  -lt  16  ]  ||  n=16
%if_disabled gigacage
export GIGACAGE_ENABLED=0
%endif
%endif

%cmake \
-DPORT=GTK \
-DCMAKE_BUILD_TYPE=Release \
-DENABLE_MINIBROWSER=ON \
%{?_enable_gtkdoc:-DENABLE_GTKDOC:BOOL=ON} \
%{?_enable_x11:-DENABLE_X11_TARGET:BOOL=ON} \
%{?_enable_wayland:-DENABLE_WAYLAND_TARGET:BOOL=ON} \
%{?_disable_gold:-DUSE_LD_GOLD:BOOL=OFF}
#-DENABLE_TOUCH_EVENTS:BOOL=ON \
#-DENABLE_TOUCH_ICON_LOADING:BOOL=ON \
#-DENABLE_TOUCH_SLIDER:BOOL=ON \
#-Dbmalloc_LIBRARIES:STRING=-ldl
# automatically enabled on x86_64
#-DENABLE_FTL_JIT:BOOL=ON
#-DENABLE_FTPDIR:BOOL=ON \
#-DENABLE_TELEPHONE_NUMBER_DETECTION:BOOL=ON \
#-DENABLE_BATTERY_STATUS:BOOL=ON \
#-DENABLE_DEVICE_ORIENTATION:BOOL=ON \
#-DENABLE_ORIENTATION_EVENTS:BOOL=ON
%ifarch x86_64
%make -j $n -C BUILD
%else
%cmake_build
%endif

%install
%cmakeinstall_std
%if_disabled gigacage
install -pD -m755 %SOURCE1 %buildroot%_rpmmacrosdir/webki2gtk.env
%endif

%find_lang WebKit2GTK-%api_ver

%files -n libwebkit2gtk -f WebKit2GTK-%api_ver.lang
%_bindir/WebKitWebDriver
%_libdir/libwebkit2gtk-%api_ver.so.*
%dir %pkglibexecdir
%pkglibexecdir/WebKitNetworkProcess
%pkglibexecdir/WebKitPluginProcess
%pkglibexecdir/WebKitPluginProcess2
%pkglibexecdir/WebKitWebProcess
%dir %_libdir/webkit2gtk-%api_ver
%dir %_libdir/webkit2gtk-%api_ver/injected-bundle
%_libdir/webkit2gtk-%api_ver/injected-bundle/libwebkit2gtkinjectedbundle.so
%doc NEWS

%files -n %_name-minibrowser
%pkglibexecdir/MiniBrowser

%files -n libwebkit2gtk-devel
%_libdir/libwebkit2gtk-%api_ver.so
%dir %_includedir/webkitgtk-%api_ver
%_includedir/webkitgtk-%api_ver/webkit2
%_includedir/webkitgtk-%api_ver/webkitdom
%_pkgconfigdir/webkit2gtk-%api_ver.pc
%_pkgconfigdir/webkit2gtk-web-extension-%api_ver.pc
%{?_disable_gigacage:%_rpmmacrosdir/webki2gtk.env}

%if_enabled gtkdoc
%files -n libwebkit2gtk-devel-doc
%_gtk_docdir/*
%endif

%files -n libjavascriptcoregtk4
%_libdir/libjavascriptcoregtk-%api_ver.so.*

%files -n libjavascriptcoregtk4-devel
%_includedir/webkitgtk-%api_ver/jsc/
%_includedir/webkitgtk-%api_ver/JavaScriptCore/
%_libdir/libjavascriptcoregtk-%api_ver.so
%_pkgconfigdir/javascriptcoregtk-%api_ver.pc

%files -n jsc4
%pkglibexecdir/jsc*

%files -n libwebkit2gtk-gir
%_typelibdir/WebKit2-%api_ver.typelib
%_typelibdir/WebKit2WebExtension-%api_ver.typelib

%files -n libwebkit2gtk-gir-devel
%_girdir/WebKit2-%api_ver.gir
%_girdir/WebKit2WebExtension-%api_ver.gir

%files -n libjavascriptcoregtk4-gir
%_typelibdir/JavaScriptCore-%api_ver.typelib

%files -n libjavascriptcoregtk4-gir-devel
%_girdir/JavaScriptCore-%api_ver.gir


%changelog
* Wed Aug 28 2019 Yuri N. Sedunov <aris@altlinux.org> 2.24.4-alt1
- 2.24.4

* Tue Jul 02 2019 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Fri May 24 2019 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2 (fixed CVE-2019-8595, CVE-2019-8607, CVE-2019-8615)

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1 (fixed CVE-2019-6251)

* Wed Mar 13 2019 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Fri Mar 01 2019 Yuri N. Sedunov <aris@altlinux.org> 2.22.7-alt1
- 2.22.7

* Sat Feb 09 2019 Yuri N. Sedunov <aris@altlinux.org> 2.22.6-alt1
- 2.22.6

* Tue Dec 18 2018 Yuri N. Sedunov <aris@altlinux.org> 2.22.5-alt1
- 2.22.5

* Thu Nov 22 2018 Yuri N. Sedunov <aris@altlinux.org> 2.22.4-alt1
- 2.22.4

* Tue Oct 30 2018 Yuri N. Sedunov <aris@altlinux.org> 2.22.3-alt1
- 2.22.3

* Sat Sep 22 2018 Yuri N. Sedunov <aris@altlinux.org> 2.22.2-alt1
- 2.22.2

* Thu Sep 20 2018 Yuri N. Sedunov <aris@altlinux.org> 2.22.1-alt1
- 2.22.1

* Sun Sep 16 2018 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt1.1
- rebuilt with atk-2.30.0

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt1
- 2.22.0

* Mon Aug 13 2018 Yuri N. Sedunov <aris@altlinux.org> 2.20.5-alt1
- 2.20.5

* Mon Aug 06 2018 Yuri N. Sedunov <aris@altlinux.org> 2.20.4-alt2
- 2.20.4 (fixed CVE-2018-4261, CVE-2018-4262, CVE-2018-4263,
  CVE-2018-4264, CVE-2018-4265, CVE-2018-4266, CVE-2018-4267,
  CVE-2018-4270, CVE-2018-4272, CVE-2018-4273, CVE-2018-4278,
  CVE-2018-4284)

* Wed Jul 25 2018 Yuri N. Sedunov <aris@altlinux.org> 2.20.3-alt2
- rebuilt against libicu*.so.62

* Mon Jun 11 2018 Yuri N. Sedunov <aris@altlinux.org> 2.20.3-alt1
- 2.20.3 (fixed  CVE-2018-4190, CVE-2018-4199, CVE-2018-4218,
  CVE-2018-4222, CVE-2018-4232, CVE-2018-4233, CVE-2018-4246,
  CVE-2018-11646)

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 2.20.2-alt1
- 2.20.2 (fixed CVE-2018-4200)

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 2.20.1-alt1
- 2.20.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 2.20.0-alt1
- 2.20.0

* Wed Jan 24 2018 Yuri N. Sedunov <aris@altlinux.org> 2.18.6-alt1
- 2.18.6 (fixed CVE-2018-4088, CVE-2017-13885, CVE-2017-7165,
  CVE-2017-13884, CVE-2017-7160, CVE-2017-7153, CVE-2017-7153,
  CVE-2017-7161, CVE-2018-4096)

* Wed Jan 10 2018 Yuri N. Sedunov <aris@altlinux.org> 2.18.5-alt1
- 2.18.5 (fixed CVE-2017-5753, CVE-2017-5715)

* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 2.18.4-alt2
- rebuilt against libicu*.so.60

* Wed Dec 20 2017 Yuri N. Sedunov <aris@altlinux.org> 2.18.4-alt1
- 2.18.4 (fixed CVE-2017-13866, CVE-2017-13870, CVE-2017-7156, CVE-2017-13856)

* Sat Nov 11 2017 Yuri N. Sedunov <aris@altlinux.org> 2.18.3-alt1
- 2.18.3 (fixed CVE-2017-13798, CVE-2017-13788, CVE-2017-13803)

* Fri Oct 27 2017 Yuri N. Sedunov <aris@altlinux.org> 2.18.2-alt1
- 2.18.2

* Wed Oct 18 2017 Yuri N. Sedunov <aris@altlinux.org> 2.18.1-alt1
- 2.18.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 2.18.0-alt1
- 2.18.0

* Thu Jul 27 2017 Yuri N. Sedunov <aris@altlinux.org> 2.16.6-alt1
- 2.16.6 (fixed CVE-2017-7039, CVE-2017-7018, CVE-2017-7030,
  CVE-2017-7037, CVE-2017-7034, CVE-2017-7055, CVE-2017-7056,
  CVE-2017-7064, CVE-2017-7061, CVE-2017-7048, CVE-2017-7046)

* Fri Jun 30 2017 Yuri N. Sedunov <aris@altlinux.org> 2.16.5-alt1
- 2.16.5

* Thu Jun 22 2017 Yuri N. Sedunov <aris@altlinux.org> 2.16.4-alt1
- 2.16.4 (fixed CVE-2017-2538)

* Sat May 27 2017 Yuri N. Sedunov <aris@altlinux.org> 2.16.3-alt1
- 2.16.3 (fixed CVE-2017-2496, CVE-2017-2539, CVE-2017-2510)

* Tue May 09 2017 Yuri N. Sedunov <aris@altlinux.org> 2.16.2-alt1
- 2.16.2

* Tue Apr 04 2017 Yuri N. Sedunov <aris@altlinux.org> 2.16.1-alt1
- 2.16.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 2.16.0-alt1
- 2.16.0

* Thu Feb 16 2017 Yuri N. Sedunov <aris@altlinux.org> 2.14.5-alt1
- 2.14.5

* Fri Feb 10 2017 Yuri N. Sedunov <aris@altlinux.org> 2.14.4-alt1
- 2.14.4 (fixed CVE-2017-2365, CVE-2017-2366, CVE-2017-2373, CVE-2017-2363,
  CVE-2017-2362, CVE-2017-2350, CVE-2017-2350, CVE-2017-2354, CVE-2017-2355,
  CVE-2017-2356, CVE-2017-2371, CVE-2017-2364, CVE-2017-2369)

* Tue Jan 17 2017 Yuri N. Sedunov <aris@altlinux.org> 2.14.3-alt1
- 2.14.3 (fixed CVE-2016-7656, CVE-2016-7635, CVE-2016-7654, CVE-2016-7639,
  CVE-2016-7645, CVE-2016-7652, CVE-2016-7641, CVE-2016-7632, CVE-2016-7599,
  CVE-2016-7592, CVE-2016-7589, CVE-2016-7623, CVE-2016-7586)

* Thu Nov 03 2016 Yuri N. Sedunov <aris@altlinux.org> 2.14.2-alt1
- 2.14.2
- MiniBrowser moved to separate subpackage

* Tue Oct 11 2016 Yuri N. Sedunov <aris@altlinux.org> 2.14.1-alt1
- 2.14.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 2.14.0-alt1
- 2.14.0

* Mon Sep 05 2016 Yuri N. Sedunov <aris@altlinux.org> 2.12.5-alt1
- 2.12.5

* Wed Aug 24 2016 Yuri N. Sedunov <aris@altlinux.org> 2.12.4-alt1
- 2.12.4 (fixed CVE-2016-4622, CVE-2016-4624, CVE-2016-4591, CVE-2016-4590)

* Tue May 31 2016 Yuri N. Sedunov <aris@altlinux.org> 2.12.3-alt1
- 2.12.3 (fixed VE-2016-1857, CVE-2016-1856)

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 2.12.2-alt1
- 2.12.2

* Thu Apr 14 2016 Yuri N. Sedunov <aris@altlinux.org> 2.12.1-alt1
- 2.12.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 2.12.0-alt1
- 2.12.0

* Thu Mar 17 2016 Yuri N. Sedunov <aris@altlinux.org> 2.10.9-alt1
- 2.10.9

* Fri Mar 11 2016 Yuri N. Sedunov <aris@altlinux.org> 2.10.8-alt1
- 2.10.8 (CVE-2016-1726)

* Tue Feb 09 2016 Yuri N. Sedunov <aris@altlinux.org> 2.10.7-alt2
- rebuild against libicu*.so.56

* Sun Jan 31 2016 Yuri N. Sedunov <aris@altlinux.org> 2.10.7-alt1
- 2.10.7

* Thu Jan 21 2016 Yuri N. Sedunov <aris@altlinux.org> 2.10.5-alt1
- 2.10.5 (CVE-2015-7096, CVE-2015-7098)

* Wed Nov 11 2015 Yuri N. Sedunov <aris@altlinux.org> 2.10.4-alt1
- 2.10.4

* Tue Oct 27 2015 Yuri N. Sedunov <aris@altlinux.org> 2.10.3-alt1
- 2.10.3

* Thu Oct 15 2015 Yuri N. Sedunov <aris@altlinux.org> 2.10.2-alt1
- 2.10.2

* Wed Oct 14 2015 Yuri N. Sedunov <aris@altlinux.org> 2.10.1-alt1
- 2.10.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 2.10.0-alt1
- 2.10.0

* Fri Aug 07 2015 Yuri N. Sedunov <aris@altlinux.org> 2.8.5-alt1
- 2.8.5

* Wed Jul 08 2015 Yuri N. Sedunov <aris@altlinux.org> 2.8.4-alt1
- 2.8.4

* Sun Jun 07 2015 Yuri N. Sedunov <aris@altlinux.org> 2.8.3-alt3
- fixed BWO #145385

* Tue May 19 2015 Yuri N. Sedunov <aris@altlinux.org> 2.8.3-alt2
- fixed build with gcc-5 (fc patch)

* Fri May 15 2015 Yuri N. Sedunov <aris@altlinux.org> 2.8.3-alt1
- 2.8.3

* Tue May 12 2015 Yuri N. Sedunov <aris@altlinux.org> 2.8.2-alt1
- 2.8.2

* Sun Apr 19 2015 Yuri N. Sedunov <aris@altlinux.org> 2.8.1-alt2
- packaged MiniBrowser in -devel subpackage

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 2.8.1-alt1
- 2.8.1

* Tue Mar 24 2015 Yuri N. Sedunov <aris@altlinux.org> 2.8.0-alt1
- 2.8.0

* Thu Jan 15 2015 Yuri N. Sedunov <aris@altlinux.org> 2.6.5-alt1
- 2.6.5

* Wed Nov 26 2014 Yuri N. Sedunov <aris@altlinux.org> 2.6.4-alt2
- enabled touch (slider/icon loading) support

* Fri Nov 21 2014 Yuri N. Sedunov <aris@altlinux.org> 2.6.4-alt1
- 2.6.4

* Wed Nov 12 2014 Yuri N. Sedunov <aris@altlinux.org> 2.6.3-alt1
- 2.6.3

* Wed Oct 22 2014 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt1
- 2.6.2

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 2.6.1-alt1
- 2.6.1

* Tue Oct 07 2014 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt2
- libwebkitgtk4* subpackages renamed to libwebkit2gtk*

* Thu Sep 25 2014 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Fri Sep 19 2014 Yuri N. Sedunov <aris@altlinux.org> 2.5.90-alt1
- 2.5.90

* Sat Aug 23 2014 Yuri N. Sedunov <aris@altlinux.org> 2.5.3-alt1
- first build for Sisyphus

