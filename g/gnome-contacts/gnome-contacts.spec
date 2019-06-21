%def_disable snapshot

%define ver_major 3.32
%define _libexecdir %_prefix/libexec
%define gst_api_ver 1.0
%define _name org.gnome.Contacts
%def_with cheese

Name: gnome-contacts
Version: %ver_major.1
Release: alt2

Summary: Contacts manager for GNOME
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Contacts

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

Patch: %name-3.32.1-up-libhandy.patch

%define glib_ver 2.44
%define gtk_ver 3.24
%define vala_ver 0.17.2
%define tp_glib_ver 0.17.5
%define folks_ver 0.12.1
%define eds_ver 3.13.90
%define cheese_ver 3.5.90
%define geocode_ver 3.15.3

BuildRequires(pre): meson
BuildRequires: yelp-tools docbook-dtds docbook-style-xsl libappstream-glib-devel valadoc
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver libtelepathy-glib-devel >= %tp_glib_ver
BuildRequires: libfolks-devel >= %folks_ver libvala-devel >= %vala_ver libgnome-desktop3-devel
BuildRequires: libgnome-online-accounts-devel libgee0.8-devel evolution-data-server-devel >= %eds_ver
BuildRequires: libgeocode-glib-devel >= %geocode_ver libchamplain-gtk3-devel libclutter-gtk3-devel
%{?_with_cheese:BuildRequires: gstreamer%gst_api_ver-devel libcheese-devel >= %cheese_ver}
BuildRequires: gobject-introspection-devel vala-tools libgtk+3-gir-devel
BuildRequires: libhandy-devel

# for build from git
BuildRequires: libfolks-vala

%description
%name is a standalone contacts manager for GNOME desktop.

%prep
%setup
%patch -p1

%build
%meson %{?_without_cheese:-Dcheese=false}
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_libexecdir/gnome-contacts-search-provider
%_datadir/applications/%_name.desktop
%_datadir/glib-2.0/schemas/%_name.gschema.xml
%_datadir/dbus-1/services/%_name.service
%_datadir/dbus-1/services/%_name.SearchProvider.service
%_datadir/gnome-shell/search-providers/%_name.search-provider.ini
%_iconsdir/hicolor/*/*/*
%_man1dir/%name.1.*
%_datadir/metainfo/%_name.appdata.xml
%doc AUTHORS NEWS README*

%changelog
* Thu Jun 20 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt2
- fixed build against libhandy-0.0.10

* Wed Apr 24 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32-alt1
- 3.32

* Wed Dec 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Tue Sep 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30-alt1
- 3.30

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Fri Apr 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Wed Jan 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26-alt1
- 3.26

* Wed Sep 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt2
- rebuilt against libedataserver-1.2.so.22

* Tue May 17 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Apr 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.19.91-alt2
- updated to 3.19.91-25-gf3dafae

* Thu Feb 25 2016 Yuri N. Sedunov <aris@altlinux.org> 3.19.91-alt1
- 3.19.91

* Thu Nov 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Wed Sep 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed Apr 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Thu Apr 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10-alt1
- 3.10.0

* Tue Jul 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Fri May 31 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Nov 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Mon Oct 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue May 08 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Thu Oct 20 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Wed Oct 19 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0.1-alt1
- 3.2.0.1

* Fri Sep 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.4.1-alt1
- first build for Sisyphus

