%def_disable snapshot

%define rdn_name io.github.pragha-music-player

%def_disable libxfce4ui
%def_enable grilo
# works only with rygel-2.2
%def_disable rygel

Name: pragha
Version: 1.3.99.1
Release: alt1

Summary: Pragha is a "Fork" of consonance Music manager
License: GPLv3
Group: Sound
Url: http://pragha-music-player.github.io/

%if_disabled snapshot
Source: https://github.com/%name-music-player/%name/releases/download/v%version/%name-%version.tar.bz2
%else
# VCS: https://github.com/pragha-music-player/pragha.git
Source: %name-%version.tar
%endif
# adapt to newer keybinder
Patch: pragha-1.3.3-alt-configure.patch

%define gtk_ver 3.14

Requires: gst-plugins-base1.0
Requires: gst-plugins-good1.0

BuildRequires: libcddb-devel libcdio-devel libcdio-paranoia-devel libclastfm-devel
BuildRequires: libexo-devel libglyr-devel
BuildRequires: libkeybinder-devel libnotify-devel libtag-devel
BuildRequires: gstreamer1.0-devel gst-plugins1.0-devel libgtk+3-devel >= %gtk_ver
BuildRequires: libpeas-devel libtotem-pl-parser-devel
BuildPreReq: libgudev-devel libsoup-devel libjson-glib-devel libmtp-devel
%{?_enable_rygel:BuildRequires: rygel-devel}
%{?_enable_grilo:BuildRequires: libgrilo-devel}
%{?_enable_libxfce4ui:BuildRequires: libxfce4ui-devel}
# requires for autogen.sh
BuildRequires: xfce4-dev-tools

%description
Pragha is a reproducer and administrator of music for GNU/Linux, based
on Gtk, sqlite, and completely written in C, constructed to be fast,
light, and simultaneously complete without obstructing the daily work.

%prep
%setup
%patch
subst 's/%name.appdata/%rdn_name.metainfo/' data/Makefile.am

%build
%add_optflags -D_FILE_OFFSET_BITS=64 
NOCONFIGURE=1 xdt-autogen
%configure \
	%{subst_enable libxfce4ui} \
	LIBS="%(pkg-config taglib_c --libs) %(pkg-config gio-2.0 --libs)"
%make_build V=1

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang

%_bindir/*
%_libdir/%name/
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/pragha*
%_man1dir/%name.1.*
%_pixmapsdir/%name
%_datadir/metainfo/*
%doc ChangeLog FAQ NEWS README

#devel
%exclude %_includedir/lib%name
%exclude %_pkgconfigdir/lib%name.pc

%changelog
* Fri Aug 16 2019 Yuri N. Sedunov <aris@altlinux.org> 1.3.99.1-alt1
- 1.3.99.1

* Sat Oct 06 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.99-alt1
- 1.3.99

* Sat May 12 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.92-alt1
- updated to v1.3.92-11-gbd864d3

* Sat Apr 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.91.1-alt1
- updated to v1.3.91.1-3-g3a51015

* Fri Jan 12 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.90-alt1
- updated to V1.3.90-16-g8ecf44b

* Sun Mar 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.3-alt3
- rebuilt for new gnome-3.20 without grilo support

* Sun Jan 24 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.3-alt2
- fixed files list

* Fri Sep 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.3.3-alt1
- 1.3.3

* Mon Sep 07 2015 Yuri N. Sedunov <aris@altlinux.org> 1.3.2.2-alt2
- rebuilt against libgrilo-0.2.so.10

* Sun Aug 09 2015 Yuri N. Sedunov <aris@altlinux.org> 1.3.2.2-alt1
- 1.3.2.2 release
- updated {build,}reqs
- disabled xfce integration to avoid using GTK+2 and GTK+3 in the same process.

* Sat Sep 27 2014 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt2.git20140727
- rebuilt without rygel support, not ready for 2.4

* Fri Sep 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20140727
- Version 1.3.1

* Sun Dec 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.1
- Disabled -Werror flag

* Fri Apr 20 2012 Egor Glukhov <kaman@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sun Aug 21 2011 Egor Glukhov <kaman@altlinux.org> 0.8.9-alt1
- 0.8.9

* Tue Jun 07 2011 Egor Glukhov <kaman@altlinux.org> 0.8.6-alt2
- Fixed build

* Thu Mar 24 2011 Egor Glukhov <kaman@altlinux.org> 0.8.6-alt1
- 0.8.6

* Sun Aug 08 2010 Egor Glukhov <kaman@altlinux.org> 0.8.0.2-alt1
- Initial build for Sisyphus
