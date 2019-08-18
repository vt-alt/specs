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

%define _libexecdir %_prefix/libexec

%def_enable vala
%def_enable rotation
%def_enable zeitgeist
%def_enable introspection
%def_enable lirc
%def_enable python

Name: xplayer
Version: 2.2.2
Release: alt1

Summary: Xplayer is a generic media player.
Group: Video
License: %gpl2only
URL: https://github.com/linuxmint/xplayer

Source: %name-%version.tar

# use python3
AutoReqProv: nopython
%define __python %nil

Provides: %name-backend = %version %name-backend-gstreamer = %version %name-backend-xine = %version

Requires: lib%name = %version-%release
Requires: libpeas-python-loader
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

BuildRequires(pre): rpm-build-licenses
BuildPreReq: rpm-build-gnome gnome-common gtk-doc
BuildPreReq: intltool >= 0.40.0
BuildRequires: libappstream-glib-devel
%{?_enable_nvtv:BuildRequires: libnvtv-devel >= 0.4.5}

BuildRequires: gstreamer%gst_api_ver-devel >= %gst_ver
BuildRequires: gst-plugins%gst_api_ver-devel >= %gst_plugins_ver
BuildRequires: gstreamer%gst_api_ver-utils >= %gst_ver
BuildRequires: gst-plugins-base%gst_api_ver
BuildRequires: gst-plugins-good%gst_api_ver
BuildRequires: gst-plugins-bad%gst_api_ver-devel

BuildPreReq: iso-codes-devel gnome-icon-theme
BuildPreReq: glib2-devel >= %glib_ver libgtk+3-devel >= %gtk_ver libgio-devel libpeas-devel >= %peas_ver
BuildPreReq: libxplayer-plparser-devel
BuildPreReq: libXtst-devel libXrandr-devel libXxf86vm-devel xorg-xproto-devel
BuildPreReq: libclutter-devel >= %clutter_ver
BuildPreReq: libclutter-gtk3-devel >= %clutter_gtk_ver
BuildPreReq: libclutter-gst3.0-devel >= %clutter_gst_ver
BuildRequires: libgrilo-devel >= %grilo_ver
%{?_enable_python:BuildRequires: rpm-build-python python-devel python3-module-pygobject3-devel pylint-py3}
%{?_enable_vala:BuildRequires: libvala-devel >= 0.14 vala-tools}
BuildRequires: libdbus-devel gsettings-desktop-schemas-devel
%{?_enable_lirc:BuildRequires: liblirc-devel}
%{?_enable_zeitgeist:BuildRequires: libzeitgeist2.0-devel}
%{?_enable_introspection:BuildRequires: libxplayer-plparser-gir-devel libgtk+3-gir-devel libclutter-gtk3-gir-devel libpeas-gir-devel}
BuildRequires: libxapps-devel

BuildRequires: desktop-file-utils db2latex-xsl yelp-tools gcc-c++
BuildRequires: libX11-devel libXext-devel libXi-devel
BuildRequires: libICE-devel libSM-devel

%description
Xplayer is a generic media player. It features a simple playlist, a full-screen
mode, seek and volume controls, as well as a pretty complete keyboard navigation.

%package -n lib%name
Summary: Xplayer Library
License: LGPLv2+
Group: System/Libraries

%description -n lib%name
This package provides shared library for Xplayer movie player.

%package -n lib%name-devel
Summary: Development files for Xplayer Library
License: LGPLv2+
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides files required to develop programs that use
Xplayer library.

%package -n lib%name-gir
Summary: GObject introspection data for the Xplayer library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Xplayer library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Xplayer library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Xplayer library

%package plugins
Summary: default plugins for Xplayer
Group: Video
Requires: %name = %version-%release

%description plugins
A default plugins for Xplayer:
	gromit
	ontop
	screensaver
	skipto
	properties
	media-player-keys
	pythonconsole
	opensubtitles
	grilo

%package plugins-lirc
Summary: LIRC (Infrared remote) plugin for Xplayer
Group: Video
Requires: %name = %version-%release

%description plugins-lirc
A plugin to add LIRC (Infrared remote) support to Xplayer.

%package plugins-rotation
Summary: Rotation plugin for Xplayer
Group: Video
Requires: %name = %version-%release

%description plugins-rotation
A plugin to allow videos to be rotated if they're in the wrong orientation.

%package plugins-zeitgeist
Summary: Zeitgeist plugin for Xplayer
Group: Video
Requires: %name = %version-%release
Requires: zeitgeist

%description plugins-zeitgeist
A plugin sending events to Zeitgeist

%package plugins-tracker
Summary: Tracker-based video search plugin for Xplayer
Group: Video
Requires: %name = %version-%release

%description plugins-tracker
A plugin to allow searching local videos, based on their tags, metadata,
or filenames, as indexing by the Tracker indexer.

%package plugins-gromit
Summary: Gromit Annotations plugin for xplayer
Group: Video
Requires: %name = %version-%release
Requires: gromit

%description plugins-gromit
This package contains presentation helper to make annotations on screen via Gromit

%package plugins-brasero
Summary: Video disc recorder plugin for Xplayer
Group: Video
Requires: %name = %version-%release
Requires: brasero

%description plugins-brasero
This package contains plugin that allow record (S)VCDs or video DVDs
with Brasero

%package video-thumbnailer
Summary: Xplayer video thumbnailer
Group: Video
Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
Requires: gst-plugins-ugly%gst_api_ver
Requires: gst-libav
Requires: iso-codes

%description video-thumbnailer
This package provides a video thumbnailer from Xplayer package that can be
used by other applications like filemanagers.

%prep
%setup

%build
export ac_cv_path_PYLINT=%_bindir/pylint.py3
%autoreconf
%configure \
	--disable-schemas-compile \
	%{subst_enable python} \
	%{subst_enable vala} \
	--disable-browser-plugins \
	--disable-static \
	--disable-Werror \
   --enable-introspection		\
	%{?_enable_snapshot:--enable-gtk-doc}

# Fix build on beekeeper machines
export NPROCS=1
%make_build

%install
%makeinstall_std
find %buildroot%_libdir -name \*.la -delete

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%exclude %_bindir/%name-video-thumbnailer
%dir %_libdir/%name
%_libexecdir/%name/%name-bugreport.py
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/*/*/*.svg
%_datadir/%name/
%_man1dir/*
%exclude %_man1dir/%name-video-thumbnailer.1.*
%config %_datadir/glib-2.0/schemas/org.x.player.gschema.xml
%config %_datadir/glib-2.0/schemas/org.x.player.enums.xml
%doc AUTHORS NEWS README TODO

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%if_enabled introspection
%files -n lib%name-gir
%_libdir/girepository-1.0/*.typelib

%files -n lib%name-gir-devel
%_datadir/gir-1.0/*.gir
%endif

%files plugins
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/dbus/
%_libdir/%name/plugins/ontop/
%_libdir/%name/plugins/screensaver/
%_libdir/%name/plugins/skipto/
%_libdir/%name/plugins/properties/
%_libdir/%name/plugins/media-player-keys/
%_libdir/%name/plugins/pythonconsole/
%_libdir/%name/plugins/opensubtitles/
%_libdir/%name/plugins/screenshot/
%_libdir/%name/plugins/im-status/
%_libdir/%name/plugins/apple-trailers/
%_libdir/%name/plugins/autoload-subtitles/
%_libdir/%name/plugins/recent/
%_libdir/%name/plugins/vimeo/
%_libdir/%name/plugins/chapters/
# Grilo plugin now doesn't work. See:
# https://github.com/linuxmint/xplayer/issues/22
%_libdir/%name/plugins/grilo/
%config %_datadir/glib-2.0/schemas/org.x.player.plugins.opensubtitles.gschema.xml
%config %_datadir/glib-2.0/schemas/org.x.player.plugins.pythonconsole.gschema.xml

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

%files plugins-gromit
%_libdir/%name/plugins/gromit/

%files plugins-brasero
%_libdir/%name/plugins/brasero-disc-recorder/

%files video-thumbnailer
%_bindir/%name-video-thumbnailer
%_man1dir/%name-video-thumbnailer.1.*
%_datadir/thumbnailers/%name.thumbnailer

%changelog
* Wed Jul 31 2019 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt1
- 2.2.2

* Wed Jul 10 2019 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt1
- 2.2.1

* Wed Jun 26 2019 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- fix build on beekeeper machines

* Mon Jan 28 2019 Vladimir Didenko <cow@altlinux.org> 2.0.2-alt1.1
- fix build on beekeeper machines

* Wed Dec 26 2018 Vladimir Didenko <cow@altlinux.org> 2.0.2-alt1
- 2.0.2

* Wed Dec 5 2018 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- 2.0.1

* Wed Nov 21 2018 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1
- 2.0.0

* Wed Jul 4 2018 Vladimir Didenko <cow@altlinux.org> 1.8.3-alt1
- 1.8.3

* Wed Jun 13 2018 Vladimir Didenko <cow@altlinux.org> 1.8.1-alt1
- 1.8.1

* Mon May 7 2018 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt1
- 1.8.0

* Thu Nov 23 2017 Vladimir Didenko <cow@altlinux.org> 1.6.1-alt1
- 1.6.1

* Tue Jul 4 2017 Vladimir Didenko <cow@altlinux.org> 1.4.3-alt1
- 1.4.3

* Mon Jun 5 2017 Vladimir Didenko <cow@altlinux.org> 1.4.2-alt1
- 1.4.2

* Fri May 19 2017 Vladimir Didenko <cow@altlinux.org> 1.4.1-alt1
- 1.4.1

* Wed Dec 14 2016 Vladimir Didenko <cow@altlinux.org> 1.2.2-alt1
- 1.2.2

* Sun Nov 13 2016 Vladimir Didenko <cow@altlinux.org> 1.2.1-alt1
- 1.2.1-1-gbf68bda

* Tue Sep 27 2016 Vladimir Didenko <cow@altlinux.org> 1.0.7-alt1
- 1.0.7-4-g772ae2e

* Thu Jun 23 2016 Vladimir Didenko <cow@altlinux.org> 1.0.6-alt1
- New version

* Thu May 26 2016 Vladimir Didenko <cow@altlinux.org> 1.0.5-alt1
- New version

* Tue May 17 2016 Vladimir Didenko <cow@altlinux.org> 1.0.4-alt1
- New version

* Wed Mar 2 2016 Vladimir Didenko <cow@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
