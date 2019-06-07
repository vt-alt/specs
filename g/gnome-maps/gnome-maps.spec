%define ver_major 3.32
%define api_ver 1.0
%define _libexecdir %_prefix/libexec
%define xdg_name org.gnome.Maps

Name: gnome-maps
Version: %ver_major.2.1
Release: alt1

Summary: Maps is a map application for GNOME
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Maps

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%set_typelibdir %_libdir/%name/girepository-1.0

%define glib_ver 2.39.3
%define gjs_ver 1.51.90
%define tracker_ver 2.0
%define geocode_ver 3.20.0
%define geoclue_ver 2.4.0
%define champlain_ver 0.12.19

Requires: geoclue2 >= %geoclue_ver
Requires: libgeocode-glib-gir >= %geocode_ver
Requires: libchamplain-gir >= %champlain_ver

# find ./ -name "*.js" |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
Requires: typelib(Champlain)
Requires: typelib(Clutter)
Requires: typelib(Gdk)
Requires: typelib(GdkPixbuf)
Requires: typelib(Geoclue)
Requires: typelib(GeocodeGlib)
Requires: typelib(GFBGraph)
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GnomeMaps)
Requires: typelib(Goa)
Requires: typelib(GObject)
Requires: typelib(Gtk)
Requires: typelib(GtkChamplain)
Requires: typelib(GtkClutter)
Requires: typelib(GWeather)
Requires: typelib(Pango)
Requires: typelib(PangoCairo)
Requires: typelib(Rest)
Requires: typelib(Secret)
Requires: typelib(Soup)
Requires: typelib(WebKit2)

BuildRequires(pre): meson rpm-build-gir
BuildRequires: yelp-tools libappstream-glib-devel
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgjs-devel >= %gjs_ver gobject-introspection-devel
BuildRequires: pkgconfig(geoclue-2.0) >= %geoclue_ver
BuildRequires: libgee0.8-devel libfolks-devel libgeocode-glib-devel libchamplain-gtk3-devel
BuildRequires: libgeocode-glib-gir-devel libchamplain-gtk3-gir-devel librest-gir-devel
BuildRequires: libclutter-gir-devel libcogl-gir-devel

%description
Maps is a map application for GNOME.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_libdir/%name/
%_desktopdir/%xdg_name.desktop
%_datadir/%name/
%_iconsdir/hicolor/scalable/apps/%xdg_name.svg
%_iconsdir/hicolor/symbolic/apps/%{xdg_name}*.svg
%_datadir/dbus-1/services/%xdg_name.service
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml
%doc README NEWS

%exclude %_libdir/%name/*.so
%exclude %_datadir/%name/gir-1.0/GnomeMaps-%api_ver.gir

%changelog
* Fri May 24 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2.1-alt1
- 3.32.2.1

* Mon May 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Sun Mar 31 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Thu Dec 20 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.3-alt1
- 3.30.3

* Thu Nov 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2.1-alt1
- 3.30.2.1

* Mon Oct 22 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Mon Sep 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Tue Oct 31 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Mon May 29 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3

* Tue May 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Mon Apr 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Nov 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Thu Sep 01 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3.1-alt1
- 3.20.3.1

* Mon Aug 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Sun Jul 31 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Sun Oct 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Fri Sep 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0.1-alt1
- 3.18.0.1

* Sun Sep 20 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue May 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1.2-alt1
- 3.14.1.2

* Fri Oct 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Wed Nov 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Thu Aug 01 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.5-alt1
- first build for people/gnome

