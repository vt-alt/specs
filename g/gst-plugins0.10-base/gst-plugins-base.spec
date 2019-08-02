%define gst_plugins gst-plugins0.10
%define ver_major 0.10

%define _gst_libdir %_libdir/gstreamer-%ver_major
%define _gtk_docdir %_datadir/gtk-doc/html

Name: %gst_plugins-base
Version: %ver_major.36
Release: alt2
Summary: An essential set of GStreamer plugins (legacy version)
Group: System/Libraries
License: LGPL
URL: http://gstreamer.freedesktop.org/

Requires: lib%gst_plugins = %version-%release
Requires: gstreamer

Provides: gstreamer(audio-hardware-sink) = %version
Provides: gstreamer(audio-hardware-source) = %version

Provides: %name-audio-filters = %version-%release
Provides: %name-test = %version-%release
Provides: %name-video-filters = %version-%release
Provides: %name-network = %version-%release
Provides: %name-subtitle = %version-%release
Provides: %gst_plugins-all = %version-%release
Provides: %gst_plugins-network = %version-%release
Provides: %gst_plugins-subtitle = %version-%release
Provides: %gst_plugins-test = %version-%release
Provides: %gst_plugins-audio-filters = %version-%release
Provides: %gst_plugins-audio-formats = %version-%release
Provides: %gst_plugins-video-filters = %version-%release
Provides: %gst_plugins-video-formats = %version-%release
Provides: %gst_plugins-video-effects = %version-%release
Provides: %gst_plugins-container-formats = %version-%release
Provides: %gst_plugins-alsa = %version-%release
Provides: %gst_plugins-cdparanoia = %version-%release
Provides: %gst_plugins-ogg = %version-%release
Provides: %gst_plugins-theora = %version-%release
Provides: %gst_plugins-vorbis = %version-%release
Provides: %gst_plugins-ximagesink = %version-%release
Provides: %gst_plugins-xvideo = %version-%release
Provides: %gst_plugins-libvisual = %version-%release
Provides: %gst_plugins-visualization = %version-%release
Provides: %gst_plugins-gnomevfs = %version-%release
Provides: %gst_plugins-gio = %version-%release
Provides: %gst_plugins-pango = %version-%release

Obsoletes: %gst_plugins-all < %version
Obsoletes: %gst_plugins-network < %version
Obsoletes: %gst_plugins-subtitle < %version
Obsoletes: %gst_plugins-test < %version
Obsoletes: %gst_plugins-audio-formats < %version
Obsoletes: %gst_plugins-audio-filters < %version
Obsoletes: %gst_plugins-video-formats < %version
Obsoletes: %gst_plugins-video-filters < %version
Obsoletes: %gst_plugins-video-effects < %version
Obsoletes: %gst_plugins-container-formats < %version
Obsoletes: %gst_plugins-libvisual < %version
Obsoletes: %gst_plugins-visualization < %version
Obsoletes: %gst_plugins-gnomevfs < %version
Obsoletes: %gst_plugins-gio < %version
Obsoletes: %gst_plugins-pango < %version

Source: %name-%version.tar
Source1: common.tar
Patch: %name-%version-%release.patch

BuildRequires: gstreamer0.10-devel gtk-doc intltool libSM-devel libXext-devel libXv-devel libalsa-devel libgtk+2-devel
BuildRequires: libcdparanoia-devel liboil-devel libtheora-devel libvorbis-devel orc liborc-test-devel gstreamer0.10-gir-devel
BuildRequires: python-module-PyXML python-modules-encodings gobject-introspection-devel

%description
GStreamer Base Plug-ins is a well-groomed and well-maintained
collection of GStreamer plug-ins and elements, spanning the range of
possible types of elements one would want to write for GStreamer. A
wide range of video and audio decoders, encoders, and filters are
included.

%package -n lib%name
Summary: GStreamer plugin libraries (legacy version)
Group: System/Libraries
Conflicts: %gst_plugins-bad <= 0.10.9

%description -n lib%name
Helper libraries for GStreamer plugins, containing base classes useful for elements

%prep
%setup -q -a1
%patch -p1

touch ABOUT-NLS config.rpath
subst '/.PHONY/d' Makefile.am

%build
%autoreconf
%configure \
	--with-default-audiosrc=pulsesrc \
	--with-default-audiosink=pulsesink \
	--with-default-videosrc=v4l2src \
	--with-default-videosink=xvimagesink \
	--disable-examples \
	--disable-valgrind \
	--disable-gtk-doc \
	--disable-experimental \
	--enable-gio \
	--disable-debug \
	--disable-static \
	--with-html-dir=%_gtk_docdir
%make_build

%install
%make DESTDIR=%buildroot install

%files -n lib%name
%_libdir/*.so.*

%changelog
* Wed Jul 24 2019 Andrey Cherepanov <cas@altlinux.org> 0.10.36-alt2
- Rename and package only libraries for legacy software.

* Tue Feb 21 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.10.36-alt1
- 0.10.36

* Fri Jun 17 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.35-alt1
- 0.10.35

* Sun May 15 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.33-alt1
- 0.10.33

* Wed Mar 09 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.32-alt2
- rebuilt for debuginfo

* Sat Jan 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.32-alt1
- 0.10.32

* Wed Dec 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.31-alt3
- rebuild with orc-0.4.11

* Wed Dec 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.31-alt2
- added provides/obsoletes gst-plugins-test

* Tue Nov 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.31-alt1
- 0.10.31

* Fri Jul 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.30-alt1
- 0.10.30

* Thu May 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.29-alt2
- added support for On2 VP8

* Wed Apr 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.29-alt1
- 0.10.29

* Thu Apr 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.28-alt2
- rebuild

* Tue Mar 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.28-alt1
- 0.10.28

* Sat Mar 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.27-alt1
- 0.10.27

* Thu Feb 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.26-alt1
- 0.10.26

* Tue Oct 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.25-alt2
- build with gobject-introspection

* Mon Oct 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.25-alt1
- 0.10.25

* Mon Aug 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.24-alt2
- build cdparanoia plugin

* Wed Aug 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.24-alt1
- 0.10.24

* Mon May 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.23-alt1
- 0.10.23

* Wed Feb 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.22-alt3
- updated build dependencies

* Fri Jan 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.22-alt2
- fixed conflicts with gst-plugins-bad (close #18608)

* Tue Jan 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.22-alt1
- 0.10.22

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.21-alt3
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Oct 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.21-alt2
- enabled GIO plugin

* Fri Oct 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.21-alt1
- 0.10.21

* Wed Jun 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.20-alt1
- 0.10.20

* Thu May 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.19-alt2
- rebuild

* Thu Apr 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.19-alt1
- 0.10.19

* Sun Mar 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.18-alt1
- 0.10.18

* Sat Feb 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.17-alt4
- real fix provides

* Fri Feb 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.17-alt3
- fixed provides

* Thu Feb 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.17-alt2
- join together subpackage

* Thu Feb 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.17-alt1
- 0.10.17
- spec cleanup
- update build dependencies

* Wed Jan 09 2008 Igor Zubkov <icesik@altlinux.org> 0.10.14-alt3
- add workaround for broken XV support in video drivers.
  if XV support broken in video driver,
  export GST_VIDEOSINK_XLIB=1 and gstreamer will use ximagesink
  instead xvimagesink

* Wed Jan 09 2008 Igor Zubkov <icesik@altlinux.org> 0.10.14-alt2
- fix playing small ogg files (alt#13267, gnome#466717)

* Mon Sep 10 2007 Igor Zubkov <icesik@altlinux.org> 0.10.14-alt1
- 0.10.12 -> 0.10.14

* Tue Mar 13 2007 Igor Zubkov <icesik@altlinux.org> 0.10.12-alt1
- 0.10.11 -> 0.10.12

* Tue Feb 20 2007 Igor Zubkov <icesik@altlinux.org> 0.10.11-alt1
- 0.10.9 -> 0.10.11

* Wed Aug 23 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.9-alt1
- Release 0.10.9

* Tue Jun 13 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.8-alt1
- Release 0.10.8

* Sun May 28 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.7-alt1
- Updated to 0.10.7
- Renamed gst-plugins-x11 to gst-plugins-ximagesink

* Fri Apr 14 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.5-alt1
- Release 0.10.5

* Sun Mar 12 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.4-alt1
- Release 0.10.4

* Sat Feb 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.3-alt1
- 0.10.3
- Renamed debug to test
- Renamed effects to filters
- Buildreq

* Wed Jan 18 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.2-alt1
- 0.10.2
- Enabled cdparanoia back after the upstream
- Added the cdparanoia plugin package in earnest

* Wed Dec 28 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.1-alt1
- 0.10.1
- Disabled cdparanoia after the upstream

* Sat Dec 10 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.0-alt1
- Updated to 0.10.0
- Added pango plugin

* Fri Nov 25 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.9.6-alt1
- Initial release for Sisyphus of plugins as split in 0.9
