%define _unpackaged_files_terminate_build 1
%define ver_major 3.32
%define xdg_name org.gnome.SoundRecorder
%define gst_api_ver 1.0

Name: gnome-sound-recorder
Version: %ver_major.1
Release: alt1

Summary: Sound Recorder for GNOME
Group: Sound
License: GPLv2+
Url: https://wiki.gnome.org/Design/Apps/SoundRecorder

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch

Obsoletes: gnome-media-common
Obsoletes: gnome-media-grecord
Provides:  gnome-media-grecord = %version-%release

%define glib_ver 2.31.10
%define gtk_ver 3.10.8
%define gjs_ver 1.48

Requires: libgjs >= %gjs_ver
Requires: gst-plugins-base%gst_api_ver gst-plugins-good%gst_api_ver gst-plugins-bad%gst_api_ver
Requires: gstreamer%gst_api_ver-utils
# find ./ -name "*.js" |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
Requires: typelib(Gdk)
Requires: typelib(GdkPixbuf)
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GObject)
Requires: typelib(Gst)
Requires: typelib(GstAudio)
Requires: typelib(GstPbutils)
Requires: typelib(Gtk)
Requires: typelib(Pango)
# explicitly required to avoid installation old version
Requires: libgst-plugins%gst_api_ver-gir

BuildRequires(pre): meson
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libgjs-devel libgtk+3-gir-devel yelp-tools
BuildRequires: gst-plugins%gst_api_ver-devel
BuildRequires: gstreamer%gst_api_ver-utils gst-plugins-base%gst_api_ver
BuildRequires: gst-plugins-good%gst_api_ver gst-plugins-bad%gst_api_ver

%description
The GNOME application for record and play sound files.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/%xdg_name.appdata.xml
%doc NEWS README*


%changelog
* Tue Jun 04 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Feb 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt2
- applied upstream patch to "Fix crashes when selecting a recording"
  (ALT #36071)

* Fri Jan 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Sun Sep 16 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt2
- fixed for gjs-1.54

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Feb 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.27.90-alt1
- 3.27.90

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Sep 13 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.92-alt1
- 3.21.92

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Thu Apr 28 2016 Yuri N. Sedunov <aris@altlinux.org> 3.19.92-alt1
- 3.19.92

* Sun Feb 28 2016 Yuri N. Sedunov <aris@altlinux.org> 3.19.91-alt1
- 3.19.91

* Sun Nov 08 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Tue Oct 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.17.92-alt1
- 3.17.92

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Sat Feb 07 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt2
- explicitly required libgst-plugins1.0-gir to avoid 0.10 version

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Wed Sep 17 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0.1-alt1
- 3.14.0.1

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Mon May 05 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt2
- obsoletes/provides gnome-media-grecord

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Feb 04 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.5-alt1
- first build for Sisyphus

