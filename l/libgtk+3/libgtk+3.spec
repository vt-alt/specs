%def_disable snapshot

%define _name gtk+
%define ver_major 3.24
%define api_ver 3.0
%define binary_ver 3.0.0
%define _libexecdir %_prefix/libexec

%def_enable xkb
%def_disable static
%def_disable gtk_doc
%def_enable man
%def_enable introspection
%def_enable colord
# wayland gdk backend
%def_enable wayland
# broadway (HTML5) gdk backend
%def_enable broadway
%def_enable cloudprint
%def_disable cloudproviders
%def_enable installed_tests
%def_disable debug

Name: libgtk+3
Version: %ver_major.11
Release: alt1

Summary: The GIMP ToolKit (GTK+)
Group: System/Libraries
License: %lgpl2plus
Url: http://www.gtk.org

%if_enabled snapshot
Source: %_name-%version.tar
%else
Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz
%endif
Source5: gtk-icon-cache.filetrigger

Patch: gtk+-2.16.5-alt-stop-spam.patch
# move cloudproviders flags from gdk to gtk
Patch1: gtk+-3.24.9-alt-build.patch

%define glib_ver 2.58
%define gi_ver 1.41.0
%define cairo_ver 1.14.0
%define pango_ver 1.42.0
%define atk_ver 2.15.1
%define atspi_ver 2.8.1
%define pixbuf_ver 2.36.3
%define fontconfig_ver 2.2.1-alt2
%define gtk_doc_ver 1.20
%define colord_ver 0.1.9
%define cups_ver 1.7
%define wayland_ver 1.10.0
%define wayland_protocols_ver 1.14
%define epoxy_ver 1.4
%define cloudproviders_ver 0.2.5
%define fribidi_ver 0.19.7

Provides: libgtk3-engine-adwaita = %version-%release
Obsoletes: libgtk3-engine-adwaita < 3.13.0

Requires: %name-schemas = %version-%release
Requires: gtk-update-icon-cache = %version-%release
Requires: icon-theme-adwaita
# ALT #32028
Requires: gtk+3-themes-incompatible
%{?_enable_colord:Requires: colord}

BuildRequires(pre): rpm-build-licenses rpm-build-gnome rpm-build-gir
BuildRequires: glib2-devel >= %glib_ver libgio-devel
BuildRequires: libcairo-devel >= %cairo_ver
BuildRequires: libcairo-gobject-devel >= %cairo_ver
BuildRequires: libpango-devel >= %pango_ver
BuildRequires: libatk-devel >= %atk_ver
BuildRequires: at-spi2-atk-devel >= %atspi_ver
BuildRequires: libgdk-pixbuf-devel >= %pixbuf_ver
BuildRequires: fontconfig-devel >= %fontconfig_ver
BuildRequires: gtk-doc >= %gtk_doc_ver
BuildRequires: libcups-devel >= %cups_ver
BuildRequires: libepoxy-devel >= %epoxy_ver
BuildRequires: docbook-utils zlib-devel
BuildRequires: sassc
BuildRequires: libXdamage-devel libXcomposite-devel libX11-devel libXcursor-devel
BuildRequires: libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel
BuildRequires: libXrender-devel libXt-devel
BuildRequires: libfribidi-devel >= %fribidi_ver
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= %gi_ver libpango-gir-devel libatk-gir-devel >= %atk_ver libgdk-pixbuf-gir-devel}
%{?_enable_colord:BuildRequires: libcolord-devel >= %colord_ver}
%{?_enable_wayland:BuildRequires: libwayland-client-devel >= %wayland_ver libwayland-cursor-devel libEGL-devel libwayland-egl-devel libxkbcommon-devel wayland-protocols >= %wayland_protocols_ver}
%{?_enable_cloudprint:BuildRequires: librest-devel libjson-glib-devel}
%{?_enable_cloudproviders:BuildRequires: libcloudproviders-devel >= %cloudproviders_ver}
# for examples
BuildRequires: libcanberra-gtk3-devel libharfbuzz-devel
# for check
BuildRequires: /proc dbus-tools-gui xvfb-run icon-theme-hicolor gnome-icon-theme-symbolic

%description
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package contains X11 part of GTK+. It is required for GNOME 3 desktop
and programs.

%package schemas
Summary: GSettings schemas used by GTK+3/4
Group: System/Libraries
Requires: dconf
BuildArch: noarch

%description schemas
This package provides a set of GSettings schemas for settings shared by
GTK+3 and GTK+4.

%package -n gtk-update-icon-cache
Summary: Icon theme caching utility for GTK+
Group: System/Libraries

%description -n gtk-update-icon-cache
gtk-update-icon-cache creates mmap()able cache files for icon themes.
GTK+ can use the cache files created by gtk-update-icon-cache to avoid
a lot of system call and disk seek overhead when the application starts.

%package devel
Summary: Development files and tools for GTK+ applications
Group: Development/C
Requires: %name = %version-%release
Requires: gtk-builder-convert

%description devel
This package contains development files for GTK+, X11 version. Use this to
build programs that use GTK+.

%package -n gtk3-demo
Summary: GTK+ widgets demonstration program
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description -n gtk3-demo
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
This package contains a program, along with its source code, that
demonstrates GTK+ variety of all its widgets.

%package -n %name-devel-doc
Summary: Development documentation for GTK+
Group: Development/Documentation
Conflicts: %name < %version, %name > %version
BuildArch: noarch

%description -n %name-devel-doc
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
This package contains documentation needed for developing GTK+ applications.

%package -n %name-devel-doc-examples
Summary: Examples for developing applications which will use GTK+
Group: Development/GNOME and GTK+
Conflicts: %name < %version-%release
BuildArch: noarch

%description -n %name-devel-doc-examples
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
This package contains sources for example programs.

%package -n %name-devel-static
Summary: Static libraries for GTK+ (GIMP ToolKit) applications
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description -n %name-devel-static
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
This package contains the static libraries for GTK+.

%package gir
Summary: GObject introspection data for the GTK+ library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GTK+ library

%package gir-devel
Summary: GObject introspection devel data for the GTK+ library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the GTK+ library

%package -n libgail3
Summary: Accessibility implementation for GTK+ and GNOME libraries
Group: System/Libraries
Requires: %name = %version-%release

%description -n libgail3
GAIL implements the abstract interfaces found in ATK for GTK+ and GNOME libraries,
enabling accessibility technologies such as at-spi to access those GUIs.

%package -n libgail3-devel
Summary: Files to compile applications that use GAIL
Group: Development/GNOME and GTK+
Requires: libgail3 = %version-%release
Requires: %name-devel = %version-%release

%description -n libgail3-devel
This package contains the files required to develop applications against
the GAIL libraries.

%package -n libgail3-devel-static
Summary: Static libraries of GAIL
Group: Development/GNOME and GTK+
Requires: libgail3-devel = %version-%release

%description -n libgail3-devel-static
This package contains the libraries required to compile applications
statically linked against the GAIL libraries.

%package -n libgail3-devel-doc
Summary: Development documentation for GAIL
Group: Development/Documentation
Conflicts: libgail3-devel < %version-%release
BuildArch: noarch

%description -n libgail3-devel-doc
GAIL implements the abstract interfaces found in ATK for GTK+ and GNOME
libraries, enabling accessibility technologies such as at-spi to access
those GUIs.

This package contains development documentation for GAIL.

%package tests
Summary: Tests for the GTK+3 packages
Group: Development/Other
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed GTK+3 packages.


%define fulllibpath %_libdir/gtk-%api_ver/%binary_ver

%prep
%setup -n %_name-%version
%patch -p1
%patch1 -b .cloudprov

%{?_enable_snapshot:touch README INSTALL}

%build
%{?_disable_static:export lt_cv_prog_cc_static_works=no}
%{?_enable_static:export lt_cv_prog_cc_static_works=yes}
%add_optflags -D_FILE_OFFSET_BITS=64
%autoreconf
%configure \
    %{subst_enable static} \
    %{subst_enable man} \
    --enable-x11-backend \
    %{subst_enable xkb} \
    --disable-schemas-compile \
    %{?_enable_gtk_doc:--enable-gtk-doc} \
    %{?_enable_snapshot:--enable-gtk-doc} \
    %{subst_enable colord} \
    %{?_enable_wayland:--enable-wayland-backend} \
    %{?_enable_broadway:--enable-broadway-backend} \
    %{?_enable_installed_tests:--enable-installed-tests} \
    %{subst_enable cloudprint} \
    %{?_enable_debug:--enable-debug=yes}
%make_build

# bad logic in configure.ac, fix it later
#    %{?_disable_cloudproviders:--enable-cloudproviders=no} \
#    %{subst_enable cloudproviders} \

%install
%makeinstall_std
install -d %buildroot{%_sysconfdir/gtk-%api_ver,%_libdir/gtk-%api_ver/%binary_ver/engines}

# posttransfiletrigger for update icons cache
install -pD -m755 {%_sourcedir,%buildroot%_rpmlibdir}/gtk-icon-cache.filetrigger

touch %buildroot%_libdir/gtk-%api_ver/%binary_ver/immodules.cache
# posttransfiletrigger to update immodules cache
cat <<EOF > filetrigger
#!/bin/sh -e

dir=%fulllibpath/immodules
grep -qs '^'\$dir'' && %_bindir/gtk-query-immodules-%api_ver --update-cache ||:
EOF

install -pD -m 755 filetrigger %buildroot%_rpmlibdir/gtk-%api_ver-immodules-cache.filetrigger

# system wide gtkrc
cat <<__RC__ > %buildroot%_sysconfdir/gtk-%api_ver/gtkrc
# This enables editing of menu accelerators by pressing
# an accelerator over the menu item.
gtk-can-change-accels = 1
__RC__

# The license
ln -sf %_licensedir/LGPL-2 COPYING

%find_lang --output=gtk30.lang gtk30 gtk30-properties
%find_lang --output=gail.lang gail

bzip2 -9kf NEWS

mkdir %buildroot%_libdir/gtk-%api_ver/modules

# examples
mkdir -p %buildroot/%_docdir/%name-devel-%version/examples
cp examples/*.c examples/Makefile* %buildroot/%_docdir/%name-devel-%version/examples/

%check
#xvfb-run %make check

%files -f gtk30.lang
%{?_enable_broadway:%_bindir/broadwayd}
%_bindir/gtk-query-immodules-%api_ver
%_bindir/gtk-query-settings
%_bindir/gtk-launch
%_bindir/gtk-encode-symbolic-svg
%_libdir/libgdk-3.so.*
%_libdir/libgtk-3.so.*
%dir %_libdir/gtk-%api_ver/modules
%dir %fulllibpath
%dir %fulllibpath/engines
%dir %fulllibpath/immodules
%fulllibpath/immodules/im-am-et.so
%fulllibpath/immodules/im-cedilla.so
%fulllibpath/immodules/im-cyrillic-translit.so
%fulllibpath/immodules/im-inuktitut.so
%fulllibpath/immodules/im-ipa.so
%fulllibpath/immodules/im-thai.so
%fulllibpath/immodules/im-ti-er.so
%fulllibpath/immodules/im-ti-et.so
%fulllibpath/immodules/im-viqr.so
%fulllibpath/immodules/im-multipress.so
%fulllibpath/immodules/im-wayland.so
%fulllibpath/immodules/im-waylandgtk.so
%fulllibpath/immodules/im-xim.so
%{?_enable_broadway:%fulllibpath/immodules/im-broadway.so}
%dir %fulllibpath/printbackends
%fulllibpath/printbackends/libprintbackend-*.so
%dir %_datadir/themes/*/gtk-%{api_ver}*
%_datadir/themes/*/gtk-%{api_ver}/*.css
%dir %_sysconfdir/gtk-%api_ver
%config(noreplace) %_sysconfdir/gtk-%api_ver/gtkrc
%config(noreplace) %_sysconfdir/gtk-%api_ver/im-multipress.conf
%ghost %_libdir/gtk-%api_ver/%binary_ver/immodules.cache
%{?_enable_broadway:%_man1dir/broadwayd.1.*}
%_man1dir/gtk-query-immodules*
%_man1dir/gtk-query-settings.1.*
%_man1dir/gtk-launch.*
%_man1dir/gtk-encode-symbolic-svg.1.*
%_rpmlibdir/gtk-%api_ver-immodules-cache.filetrigger
%doc --no-dereference COPYING
%doc AUTHORS NEWS.bz2 README

%files schemas
%config %_datadir/glib-2.0/schemas/org.gtk.Settings.FileChooser.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gtk.Settings.ColorChooser.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gtk.Settings.Debug.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gtk.Settings.EmojiChooser.gschema.xml

%files -n gtk-update-icon-cache
%_bindir/gtk-update-icon-cache
%_man1dir/gtk-update-icon-cache*
%_rpmlibdir/gtk-icon-cache.filetrigger

%files devel
%_bindir/gtk-builder-tool
%_includedir/gtk-%api_ver/
%_libdir/libgdk-3.so
%_libdir/libgtk-3.so
%_pkgconfigdir/gtk+-%api_ver.pc
%_pkgconfigdir/gtk+-x11-%api_ver.pc
%_pkgconfigdir/gdk-%api_ver.pc
%_pkgconfigdir/gdk-x11-%api_ver.pc
%_pkgconfigdir/gtk+-unix-print-%api_ver.pc
%dir %_datadir/gtk-%api_ver
%_datadir/gtk-%api_ver/gtkbuilder.rng
%_datadir/aclocal/gtk-%api_ver.m4
%_datadir/gettext/its/gtkbuilder.its
%_datadir/gettext/its/gtkbuilder.loc
%_man1dir/gtk-builder-tool.1*

%if_enabled wayland
%_pkgconfigdir/gtk+-wayland-%api_ver.pc
%_pkgconfigdir/gdk-wayland-%api_ver.pc
%endif

%if_enabled broadway
%_pkgconfigdir/gdk-broadway-3.0.pc
%_pkgconfigdir/gtk+-broadway-3.0.pc
%endif

%files -n gtk3-demo
%_desktopdir/gtk3-demo.desktop
%_desktopdir/gtk3-widget-factory.desktop
%_desktopdir/gtk3-icon-browser.desktop
%_bindir/gtk3-demo
%_bindir/gtk3-demo-application
%_bindir/gtk3-widget-factory
%_bindir/gtk3-icon-browser
%_datadir/glib-2.0/schemas/org.gtk.Demo.gschema.xml
%_iconsdir/hicolor/*x*/apps/gtk3-demo*.png
%_iconsdir/hicolor/*x*/apps/gtk3-widget*.png
%_man1dir/gtk3-demo.1.*
%_man1dir/gtk3-widget-factory.1.*
%_man1dir/gtk3-icon-browser.1.*
%_man1dir/gtk3-demo-application.1.*
%config %_datadir/glib-2.0/schemas/org.gtk.exampleapp.gschema.xml

%files devel-doc
%_datadir/gtk-doc/html/*
%exclude %_datadir/gtk-doc/html/gail-libgail-util3

%files devel-doc-examples
%doc %_docdir/%name-devel-%version/examples

%if_enabled static
%files -n %name-devel-static
%_libdir/*.a
%fulllibpath/*/*.a

%files -n libgail3-devel-static
%_libdir/libgailutil.a
%endif

%files -n libgail3 -f gail.lang
%_libdir/libgailutil-3.so.*

%files -n libgail3-devel
%_includedir/gail-%api_ver
%_libdir/libgailutil-3.so
%_pkgconfigdir/gail-%api_ver.pc

%files -n libgail3-devel-doc
%_datadir/gtk-doc/html/gail-libgail-util3

%if_enabled introspection
%files gir
%_typelibdir/*

%files gir-devel
%_girdir/*
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/gtk+/
%_datadir/installed-tests/gtk+/
%endif

%exclude %fulllibpath/*/*.la

%changelog
* Wed Sep 04 2019 Yuri N. Sedunov <aris@altlinux.org> 3.24.11-alt1
- 3.24.11

* Thu Jul 04 2019 Yuri N. Sedunov <aris@altlinux.org> 3.24.10-alt1
- 3.24.10

* Tue Jun 18 2019 Yuri N. Sedunov <aris@altlinux.org> 3.24.9-alt1
- 3.24.9

* Thu Apr 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.24.8-alt1
- 3.24.8

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.24.7-alt1
- 3.24.7

* Mon Feb 04 2019 Yuri N. Sedunov <aris@altlinux.org> 3.24.5-alt1
- 3.24.5

* Mon Jan 21 2019 Yuri N. Sedunov <aris@altlinux.org> 3.24.4-alt1
- 3.24.4

* Mon Jan 14 2019 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3

* Mon Dec 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt2
- applied fixes related to
  https://gitlab.gnome.org/GNOME/gtk/issues/1280 (ALT #35804)

* Tue Dec 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Wed Sep 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Fri Sep 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt2
- rebuilt against libatk-2.30.0
  (see https://gitlab.gnome.org/GNOME/pygobject/issues/258)

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Fri Jun 29 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.30-alt3
- downgraded to 3.22.30 release in anticipation of 3.24

* Mon May 28 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.30-alt2
- updated to 3.22.30-83-gd354000

* Tue Apr 17 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.30-alt1
- 3.22.30

* Sat Mar 17 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.29-alt2
- updated to 3.22.29-17-g7fd9f2d
- temporarily disabled buggy cloudproviders support

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.29-alt1
- 3.22.29

* Thu Feb 15 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.28-alt2
- new gtk-update-icon-cache subpackage moved from gtk+2

* Thu Feb 15 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.28-alt1
- 3.22.28

* Wed Feb 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.27-alt1
- 3.22.27

* Tue Nov 07 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.26-alt1
- 3.22.26

* Sun Oct 29 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.25-alt1
- updated to 3.22.25-3-g5b8a3ba

* Wed Oct 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.24-alt1
- 3.22.24

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.21-alt1
- 3.22.21

* Mon Sep 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.20-alt1
- 3.22.20

* Tue Aug 22 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.19-alt1
- 3.22.19

* Tue Aug 08 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.18-alt1
- 3.22.18

* Wed Jul 19 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.17-alt1
- 3.22.17

* Wed Jun 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.16-alt1
- 3.22.16

* Thu May 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.15-alt1
- 3.22.15

* Wed May 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.14-alt1
- 3.22.14

* Tue May 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.13-alt1
- 3.22.13

* Sat Apr 08 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.12-alt1
- 3.22.12
- moved *.gschema to separate subpackage to share it with libgtk+4

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.11-alt1
- 3.22.11

* Tue Mar 14 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.10-alt1
- 3.22.10

* Wed Mar 01 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.9-alt1
- 3.22.9

* Mon Feb 13 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.8-alt1
- 3.22.8

* Mon Jan 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.7-alt1
- 3.22.7

* Fri Jan 06 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.6-alt1
- 3.22.6

* Fri Dec 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.5-alt1
- 3.22.5

* Sat Nov 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.4-alt1
- 3.22.4

* Mon Nov 07 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Mon Oct 24 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Sat Oct 01 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Wed Aug 17 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.9-alt1
- 3.20.9

* Thu Aug 04 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.8-alt1
- 3.20.8

* Mon May 30 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.6-alt1
- 3.20.6

* Thu May 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.5-alt1
- 3.20.5

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.4-alt1
- 3.20.4

* Wed Apr 27 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt2
- reqs: added gtk+3-themes-incompatible metapackage
  with conflicts on restricted themes for current gtk+3 (ALT #320028)

* Tue Apr 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Thu Mar 31 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Fri Mar 25 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Thu Mar 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.9-alt2
- rebuilt for broken rpm-4.0.4-alt100.89

* Thu Mar 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.9-alt1
- 3.18.9

* Wed Feb 24 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.8-alt2
- updated to 3.18.8-2-g1d0ca71 (fixed BGO ## 677329, 761474)

* Wed Feb 24 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.8-alt1
- 3.18.8

* Thu Jan 28 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.7-alt1
- 3.18.7

* Sat Dec 05 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.6-alt1
- 3.18.6

* Mon Nov 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.5-alt1
- 3.18.5

* Thu Nov 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.4-alt1
- 3.18.4

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Sun Oct 04 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Fri Sep 18 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.7-alt1
- 3.16.7

* Mon Jul 27 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.6-alt2
- applied patch from BGO #740554

* Tue Jul 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.6-alt1
- 3.16.6

* Thu Jul 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.5-alt2
- updated to 3.16.5_7c35d52f

* Tue Jul 07 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.5-alt1
- 3.16.5

* Wed Jun 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.4-alt1
- 3.16.4

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Fri Apr 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1.1
- updated to 3-16_95e80ef6 (fixed BGO #747539, 747471, RHBZ #1173904, 1176339)

* Tue Apr 07 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Tue Apr 07 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1.1
- updated to 3-16_28cc8dc7

* Thu Mar 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Thu Mar 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.10-alt1
- 3.14.10

* Thu Feb 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.9-alt1
- 3.14.9

* Sun Feb 01 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.8-alt1
- 3.14.8

* Sun Jan 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.7-alt1
- 3.14.7

* Sat Dec 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.6-alt1
- 3.14.6

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.5-alt1
- 3.14.5

* Wed Oct 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.4-alt1
- 3.14.4

* Fri Oct 17 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt2
- update to 3.14.3_c25e8cefa (fixed BGO #738636, 737986)

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt1
- 3.14.3

* Wed Oct 08 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2 release

* Tue Oct 07 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt0.1
- updated to 3.14.2_ea205f75

* Tue Sep 30 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Sun Jun 08 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt2
- rebuilt against libcolord.so.2

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Sat Apr 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1 release

* Wed Apr 09 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt0.2
- updated to b7d55bfe (fixed BGO ##727662, 727643, 727244, 727414)

* Mon Mar 31 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt0.1
- 3.12.1 snapshot (a0f2e6990fa3)

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Jan 28 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.7-alt1
- 3.10.7

* Thu Dec 05 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.6-alt1
- 3.10.6

* Wed Nov 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.5-alt1
- 3.10.5

* Fri Nov 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.4-alt1
- 3.10.4

* Mon Nov 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.3-alt1
- 3.10.3

* Wed Oct 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Fri Oct 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Sun Sep 29 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt0.1
- git snapshot (fixed BGO #702196)

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0
- optional -tests subpackage

* Fri Aug 30 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0
- enabled wayland and broadway backends

* Tue Jan 08 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.4-alt1
- 3.6.4

* Fri Jan 04 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt1
- 3.6.3

* Thu Dec 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt2
- added rpm posttrans filetrigger to update im-modules cache (ALT #28279)

* Sun Nov 11 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon Jul 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.4-alt1
- 3.4.4 release

* Wed May 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt2
- updated from upsream git

* Sat May 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt1
- 3.4.3

* Mon May 07 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Sat Apr 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Sun Mar 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.20-alt2
- rebuilt against newest libX11/libXi/cairo

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.20-alt1
- 3.3.20

* Mon Mar 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.4-alt1
- 3.2.4

* Wed Jan 04 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt1
- 3.2.3

* Sat Nov 12 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Sat Oct 15 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Aug 09 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.12-alt1
- 3.0.12

* Tue Jun 07 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.11-alt1
- 3.0.11

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.10-alt1
- 3.0.10

* Fri Apr 15 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.9-alt1
- 3.0.9

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.8-alt1
- 3.0.8

* Sun Apr 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.7-alt2
- applied some fixes from upstream git

* Sat Apr 02 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.7-alt1
- 3.0.7

* Sat Mar 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.6-alt1
- 3.0.6

* Thu Mar 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.5-alt1
- 3.0.5
- updated buildreqs

* Mon Mar 21 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.4-alt1
- 3.0.4

* Mon Mar 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Mon Mar 07 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Feb 22 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Feb 11 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Feb 02 2011 Yuri N. Sedunov <aris@altlinux.org> 2.99.3-alt1
- 2.99.3

* Wed May 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.90.1-alt1
- 2.90.1

* Tue May 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.90.0-alt1
- first build for Sisyphus

