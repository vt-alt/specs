%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define ver_major 3.32
%define xdg_name org.gnome.Totem
%define nautilus_extdir %_libdir/nautilus/extensions-3.0

%define parser_ver 3.10.1
%define gst_api_ver 1.0
%define gst_ver 1.4.2
%define gst_plugins_ver 1.2.4
%define gtk_ver 3.16.0
%define grilo_ver 0.2.12
%define glib_ver 2.36.0
%define clutter_ver 1.17.3
%define clutter_gtk_ver 1.5.5
%define clutter_gst_ver 2.99.2
%define peas_ver 1.1.0


%def_disable static
%def_enable vala

%if_enabled vala
%def_enable rotation
%endif
# removed in 3.31.x
%def_disable zeitgeist

%def_enable introspection
%def_enable gtk_doc
# in 3.31.91 nautilus properties page moved to nautilus module
%def_disable nautilus
%def_enable lirc
%def_disable tracker
%def_enable python
%def_disable coherence_upnp
%def_disable jamendo

Name: totem
Version: %ver_major.1
Release: alt1

Summary: Movie player for GNOME 3
Group: Video
License: GPLv2/LGPL
Url: https://wiki.gnome.org/Apps/Videos

%if_enabled snapshot
Source: %name-%version.tar
%else
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
%endif

Obsoletes: %name-gstreamer < %version %name-backend-gstreamer < %version %name-backend-xine < %version
Obsoletes: %name-plugins-mythtv  %name-plugins-galago
Obsoletes: %name-plugins-bemused  %name-plugins-youtube
Obsoletes: %name-plugins-publish  %name-plugins-iplayer %name-plugins-grilo
Obsoletes: mozilla-plugin-%name
Provides: %name-backend = %version %name-backend-gstreamer = %version %name-backend-xine = %version

Requires: lib%name = %version-%release
Requires: libpeas-python3-loader
Requires: %name-video-thumbnailer = %version-%release
Requires: dconf gnome-icon-theme
Requires: gstreamer%gst_api_ver >= %gst_ver
Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
Requires: gst-plugins-ugly%gst_api_ver
Requires: gst-libav
Requires: iso-codes
Requires: grilo-plugins

# use python3
AutoReqProv: nopython
%define __python %nil
%add_python3_compile_include %_libdir/%name/plugins

BuildRequires(pre): meson rpm-build-gnome rpm-build-gir
BuildRequires: gcc-c++ gtk-doc perl-podlators
BuildRequires: desktop-file-utils db2latex-xsl yelp-tools
BuildRequires: libappstream-glib-devel
%{?_enable_nvtv:BuildRequires: libnvtv-devel >= 0.4.5}

BuildRequires: gstreamer%gst_api_ver-devel >= %gst_ver
BuildRequires: gst-plugins%gst_api_ver-devel >= %gst_plugins_ver
BuildRequires: gstreamer%gst_api_ver-utils >= %gst_ver
BuildRequires: gst-plugins-base%gst_api_ver
BuildRequires: gst-plugins-good%gst_api_ver
BuildRequires: gst-plugins-bad%gst_api_ver-devel

BuildRequires: iso-codes-devel gnome-icon-theme
BuildRequires: glib2-devel >= %glib_ver libgtk+3-devel >= %gtk_ver libgio-devel libpeas-devel >= %peas_ver
BuildRequires: libtotem-pl-parser-devel >= %parser_ver
BuildRequires: libXtst-devel libXrandr-devel libXxf86vm-devel xorg-proto-devel
BuildRequires: libclutter-devel >= %clutter_ver
BuildRequires: libclutter-gtk3-devel >= %clutter_gtk_ver
BuildRequires: libclutter-gst3.0-devel >= %clutter_gst_ver
BuildRequires: libgrilo-devel >= %grilo_ver
BuildRequires: libgnome-desktop3-devel
%if_enabled python
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-pygobject3-devel pylint-py3
%endif
%{?_enable_vala:BuildRequires: libvala-devel >= 0.14 vala-tools}
BuildRequires: libdbus-devel gsettings-desktop-schemas-devel
%{?_enable_lirc:BuildRequires: liblirc-devel}
%{?_enable_tracker:BuildRequires: tracker-devel}
%{?_enable_nautilus:BuildRequires: libnautilus-devel}
%{?_enable_zeitgeist:BuildRequires: libzeitgeist2.0-devel}
%{?_enable_introspection:BuildRequires: libtotem-pl-parser-gir-devel libgtk+3-gir-devel libclutter-gtk3-gir-devel libpeas-gir-devel}
BuildRequires: libX11-devel libXrandr-devel libXi-devel

%description
Totem is simple movie player for the Gnome desktop.
It features a simple playlist, a full-screen mode, seek and volume
controls, as well as a pretty complete keyboard navigation.

%package -n lib%name
Summary: Totem Library
License: LGPLv2+
Group: System/Libraries

%description -n lib%name
This package provides shared library for Totem movie player.

%package -n lib%name-devel
Summary: Development files for Totem Library
License: LGPLv2+
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides files required to develop programs that use
Totem library.

%package -n lib%name-gir
Summary: GObject introspection data for the Totem library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Totem library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Totem library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Totem library

%package plugins
Summary: default plugins for Totem
Group: Video
Requires: %name = %version-%release

%description plugins
A default plugins for Totem:
	screensaver
	skipto
	properties
	media-player-keys
	pythonconsole
	opensubtitles

%package plugins-lirc
Summary: LIRC (Infrared remote) plugin for Totem
Group: Video
Requires: %name = %version-%release

%description plugins-lirc
A plugin to add LIRC (Infrared remote) support to Totem.

%package plugins-rotation
Summary: Rotation plugin for Totem
Group: Video
Requires: %name = %version-%release

%description plugins-rotation
A plugin to allow videos to be rotated if they're in the wrong orientation.

%package plugins-zeitgeist
Summary: Zeitgeist plugin for Totem
Group: Video
Requires: %name = %version-%release
Requires: zeitgeist

%description plugins-zeitgeist
A plugin sending events to Zeitgeist

%package plugins-tracker
Summary: Tracker-based video search plugin for Totem
Group: Video
Requires: %name = %version-%release

%description plugins-tracker
A plugin to allow searching local videos, based on their tags, metadata,
or filenames, as indexing by the Tracker indexer.

%package plugins-jamendo
Summary: Plugin for jamendo.com music collection
Group: Video
Requires: %name = %version-%release
%py_requires json

%description plugins-jamendo
A plugin to allow you to listen to the large collection of Creative
Commons licensed music on Jamendo

%package plugins-coherence_upnp
Summary: Coherence DLNA/UPnP totem plugin
Group: Video
Requires: %name = %version-%release
Requires: python-module-coherence coherence

%description plugins-coherence_upnp
This package contains a DLNA/UPnP client for Totem powered by Coherence

%package plugins-brasero
Summary: Video disc recorder plugin for Totem
Group: Video
Requires: %name = %version-%release
Requires: brasero

%description plugins-brasero
This package contains plugin that allow record (S)VCDs or video DVDs
with Brasero

%package devel-doc
Summary: Development documentation for Totem
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package provides Totem reference manual

%package nautilus
Summary: Nautilus extension for the Totem media player
Group: Video
Requires: %name-video-thumbnailer = %version-%release
Provides: totem-gstreamer-nautilus = %version-%release
Provides: totem-xine-nautilus = %version-%release
Provides: totem-nautilus = %version
Provides: nautilus-totem-gstreamer = %version-%release
Provides: nautilus-totem-xine = %version-%release
Provides: nautilus-totem = %version-%release
Obsoletes: totem-gstreamer-nautilus < %version-%release
Obsoletes: totem-xine-nautilus < %version-%release
Obsoletes: totem-nautilus < %version-%release

%description nautilus
This package provides integration with the Totem media player for
the Nautilus file manager.

%package video-thumbnailer
Summary: Totem video thumbnailer
Group: Video
Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
Requires: gst-plugins-ugly%gst_api_ver
Requires: gst-libav
Requires: iso-codes

%description video-thumbnailer
This package provides a video thumbnailer from Totem package that can be
used by other applications like filemanagers.

%prep
%setup
subst "s|'pylint'|'pylint.py3'|" meson.build

%build
%meson \
	%{?_enable_python:-Denable-python=yes} \
	%{?_enable_introspection:-Denable-introspection=yes} \
	%{?_disable_vala:-Denable-vala=no} \
	%{?_enable_nautilus:-Denable-nautilus=yes} \
	%{?_enable_gtk_doc:-Denable-gtk-doc=true}
# https://github.com/mesonbuild/meson/issues/1994
%meson_build -j1

%install
%meson_install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%exclude %_bindir/%name-video-thumbnailer
%dir %_libdir/%name
# depends on pygtk
#%_libexecdir/%name/totem-bugreport.py
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/*/*.svg
%_datadir/%name/
%_man1dir/*
%exclude %_man1dir/%name-video-thumbnailer.1.*
%_datadir/dbus-1/services/%xdg_name.service
%config %_datadir/glib-2.0/schemas/org.gnome.totem.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.totem.enums.xml
%_datadir/GConf/gsettings/totem.convert
%_datadir/metainfo/%xdg_name.appdata.xml
%doc AUTHORS NEWS README COPYING

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/*.typelib

%files -n lib%name-gir-devel
%_girdir/*.gir
%endif

%files plugins
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/dbus/
%_libdir/%name/plugins/screensaver/
%_libdir/%name/plugins/skipto/
%_libdir/%name/plugins/properties/
%_libdir/%name/plugins/media-player-keys/
%_libdir/%name/plugins/pythonconsole/
%_libdir/%name/plugins/opensubtitles/
%_libdir/%name/plugins/screenshot/
%_libdir/%name/plugins/save-file/
%_libdir/%name/plugins/im-status/
%_libdir/%name/plugins/apple-trailers/
%_libdir/%name/plugins/autoload-subtitles/
%_libdir/%name/plugins/recent/
%_libdir/%name/plugins/variable-rate/
%_libdir/%name/plugins/vimeo/
%config %_datadir/glib-2.0/schemas/org.gnome.totem.plugins.opensubtitles.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.totem.plugins.pythonconsole.gschema.xml
%_datadir/GConf/gsettings/opensubtitles.convert
%_datadir/GConf/gsettings/pythonconsole.convert

%if_enabled lirc
%files plugins-lirc
%_libdir/%name/plugins/lirc/
%endif

%if_enabled rotation
%files plugins-rotation
%_libdir/%name/plugins/rotation/
%endif

%if_enabled zeitgeist
%files plugins-zeitgeist
%_libdir/%name/plugins/zeitgeist-dp/
%endif

%if_enabled tracker
%files plugins-tracker
%_libdir/%name/plugins/tracker/
%endif

%if_enabled jamendo
%files plugins-jamendo
%_libdir/%name/plugins/jamendo/
%_datadir/glib-2.0/schemas/org.gnome.totem.plugins.jamendo.gschema.xml
%_datadir/GConf/gsettings/jamendo.convert
%endif

%if_enabled nautilus
%files nautilus
%nautilus_extdir/*
%endif

%if_enabled coherence_upnp
%files plugins-coherence_upnp
%_libdir/%name/plugins/coherence_upnp/
%endif

%files plugins-brasero
%_libdir/%name/plugins/brasero-disc-recorder/

%files devel-doc
%_datadir/gtk-doc/html/*

%files video-thumbnailer
%_bindir/%name-video-thumbnailer
%_libexecdir/%name-gallery-thumbnailer
%_man1dir/%name-video-thumbnailer.1.*
%_datadir/thumbnailers/%name.thumbnailer

%changelog
* Fri Jul 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Fri Mar 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Wed Dec 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Tue Jul 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Fri Jun 15 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.26.0-alt3.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Mar 06 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt3
- updated to V_3_26_0-31-gc84daa2
- built against libgnome-desktop-3.so.17

* Sun Nov 26 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt2
- updated to V_3_26_0-14-g621a387

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Fri Mar 03 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Sat Sep 17 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Wed Apr 13 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt2
- disabled gromit plugin
- fixed url

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Thu Mar 17 2016 Yuri N. Sedunov <aris@altlinux.org> 3.19.92-alt1
- 3.19.92

* Sat Mar 05 2016 Yuri N. Sedunov <aris@altlinux.org> 3.19.91-alt1
- 3.19.91

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.4-alt1
- 3.16.4

* Mon Sep 07 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt2
- rebuilt against libgrilo-0.2.so.10

* Mon Aug 31 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Mon Jun 29 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Thu May 07 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Jan 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Thu Nov 20 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Nov 18 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt2
- used APPSTREAM_XML instead of APPDATA_XML
- used python3
- packaged opensubtitles plugin again

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Fri Aug 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Sat Jun 07 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt2
- updated to 3.12.1_773e85fb

* Wed Apr 30 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0
- temporarily removed opensubtitles plugin

* Thu Jan 09 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt2
- updated to 2dc3096 (fixed BGO ##721054, 712153, 709905... )
- moved totem-video-thumbnailer to separate subpackage

* Mon Sep 30 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Sun Sep 29 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt2
- updated to 3.10.0_b252133

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Wed Sep 18 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.92-alt1
- 3.9.92

* Thu Jul 04 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt2
- added lost dependencies

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Thu Nov 08 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt1
- 3.6.3

* Thu Oct 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Wed Sep 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0
- removed obsolete publish and iplayer plugins

* Wed Jul 04 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt1
- 3.4.3

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Wed Apr 04 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt2.1
- enabled grilo plugin really

* Thu Mar 29 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt2
- enabled grilo plugin again

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Sun Mar 18 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92
- grilo plugin temporarily disabled

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.1-alt2.1
- Rebuild with Python-2.7

* Tue Nov 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt2
- some fixes from upstream git
- new grilo plugin (ALT #26538)

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Fri Jun 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt2
- replaced obsolete python-module-json by python-modules-json

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Apr 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Mar 29 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.93-alt1
- 2.91.93

* Sat Dec 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt2
- libbluez4-devel/libbluez-devel

* Mon Oct 18 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Wed May 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Mon Mar 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Wed Feb 24 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Mon Feb 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.5-alt2
- rebuild against new libgdata-0.6.0

* Wed Jan 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.4-alt1
- 2.29.4

* Tue Dec 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.5-alt1
- 2.28.5

* Fri Nov 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.4-alt1
- 2.28.4

* Sat Nov 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.3-alt1
- 2.28.3

* Mon Oct 26 2009 Alexey Shabalin <shaba@altlinux.ru> 2.28.1-alt3
- build again with coherence_upnp

* Mon Oct 26 2009 Alexey Shabalin <shaba@altlinux.ru> 2.28.1-alt2
- temporary build without coherence_upnp

* Tue Sep 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Tue Sep 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt4
- rebuild with new %%browser_plugins_path

* Thu Sep 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt3
- requires new pl-parser

* Thu Sep 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.0-alt2
- build youtube plugin

* Wed Sep 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.0-alt1
- 2.28.0

* Tue Jun 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Mon May 04 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Sat Apr 04 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt2
- properly linked skipto plugin
- separate gromit plugin
- updated reqs for lirc, galago, jamendo and coherence-upnp plugins

* Thu Apr 02 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Tue Mar 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Thu Mar 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92
- updated buildreqs
- new coherence_upnp, brasero plugins
- added builtin screenshot plugin in -plugins package
- new devel-doc noarch subpackage

* Fri Jan 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.3-alt1
- 2.25.3
- removed obsolete %%post{,un} scripts
- packaged opensubtitles and jamendo plugins

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.24.3-alt2.1
- NMU:
  * updated build dependencies

* Tue Nov 11 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.3-alt2
- clean description for youtube plugin (#17822)
- remove empty line in alternatives files(#17831)

* Wed Oct 29 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.3-alt1
- 2.24.3
- fix Provides/Obsoletes for totem-nautilus
- fix Provides libbaconvideowidget.so.0 for x86_64
- enable publish plugin

* Mon Oct 27 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt6
- rebuild against libtotem-plparser.so.12

* Wed Oct 22 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.2-alt5
- only one package mozilla-plugin-%%name , %%name-nautilus

* Tue Oct 21 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.2-alt4
- fix alternatives
- build gmyth plugin

* Mon Oct 13 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.2-alt3
- fix requires for gstreamer backend

* Fri Oct 10 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.2-alt2
- restructured for build xine and gstreamer backends from one spec
- subpackages of plugins
- build mozilla plugin
- define _libexecdir as  %_prefix/libexec
- disabled vala support (have only simple plugin now)
- TODO:
    - control for switch backend
    - publish plugin (need libepc-ui)
    - tracker plugin
    - gmyth plugin (need gmyth)

* Wed Oct 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.2-alt1
- 2.24.2
- remove "Dirty hack" (Provides: python%__python_version(atom) python%__python_version(gdata))
- add %%update_menus/%%clean_menus to %%post/%%postun
- build galago plugin
- build bemused plugin (bluez)
- TODO:
    - vala... support
    - libtotem, totem-*-plugin subpackages
    - publish plugin (need libepc-ui)
    - tracker plugin
    - gmyth plugin (need gmyth)

* Mon Sep 29 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0
- fixed source url
- updated buildreqs
- TODO:
    - galago, vala... support
    - libtotem, totem-*-plugin subpackages

* Thu May 22 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.2-alt2
- Correct requires

* Fri May 09 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.2-alt1
- 2.22.2

* Wed Apr 09 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.1-alt1
- 2.22.1

* Tue Mar 11 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.0-alt1
- 2.22.0

* Mon Jan 14 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.3-alt1
- 2.20.3

* Fri Oct 19 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.1-alt1
- 2.20.1

* Thu Sep 20 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.0-alt1
- 2.20.0

* Wed Sep 12 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.3-alt1
- 2.18.3

* Mon May 28 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.2-alt1
- 2.18.2

* Wed Apr 04 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.1-alt1
- 2.18.1

* Mon Mar 12 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.0-alt0.1
- 2.18.0

* Wed Mar 07 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.17.92-alt0.1
- 2.17.92 (!!!WARNING!!! this is an experimental build)

* Fri Feb 02 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.5-alt1
- 2.16.5

* Thu Nov 30 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.4-alt2
- Provides virtual totem-* packages
- Conflicts with *totem-gstreamer-*

* Wed Nov 29 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.4-alt1
- 2.16.4
- Add conflicts with libtotem* into libtotem-xine*

* Mon Nov 27 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.3-alt2
- 2.16.3

* Mon Oct 09 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.2-alt2
- 2.16.2

* Wed Oct 04 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.1-alt2
- separate lib* subpackages

* Fri Sep 08 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.1-alt1
- 2.16.1

* Tue Aug 15 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Mon May 15 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Thu Apr 20 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Wed Apr 19 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.2.1-alt4
- Spec cleanup

* Tue Mar 14 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.2.1-alt3
- ChangeLog corrected

* Tue Mar 07 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.2.1-alt2
- Disable --as-needed flag for linker

* Wed Dec 21 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.2.1-alt1
- 1.2.1
- build vanity utility
- remove freedesktop.pl menus

* Fri Oct 14 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.2.0-alt2
- repackage with xine backend

* Sat Sep 10 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.0-alt1
- 1.2.0
- Resurrected devel
- Separate binary package for nautilus extensions
- Added dependency on gstreamer-subtitle

* Sat Jul 16 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.4-alt1.1
- rebuild with new libnautilus-burn.so.1 .

* Sat Jul 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Mon Jun 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sat Apr 30 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Mar 22 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.0.1-alt1
- 1.0.1
- move vanity to separate subpackage (close #6269) and do not build it by default.

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.0-alt1
- 1.0

* Thu Jan 27 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.101-alt0.6
- 0.101.

* Tue Jan 04 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.100-alt0.5
- 0.100.

* Sat Nov 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.99.22-alt0.5
- 0.99.22

* Fri Oct 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.99.20-alt0.5
- 0.99.20

* Mon Jun 23 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.99.1-alt0.5
- 0.99.1
- summary, description by avp.

* Wed May 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.99.0-alt0.5
- First build for Sisyphus.

