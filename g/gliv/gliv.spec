%define git	 e7b0afc
%define ver      1.9.7
%define rel      alt4.%git

Summary: Graphics file browser utility
Name: gliv
Version: %ver
Release: %rel
License: LGPL-2
Group: Graphics
Url: http://guichaz.free.fr/gliv
Source: %name-%ver-%git.tar.bz2
Patch: gliv-gettext-ver.patch

Packager: L.A. Kostis <lakostis@altlinux.org>

# Automatically added by buildreq on Fri Apr 22 2005
BuildRequires: fontconfig freetype2 glib2-devel libatk-devel libgtk+2-devel libgtkglext-devel libpango-devel pkgconfig

%description
GLiv is an OpenGL image viewer, image loading is done via Gdk-pixbuf bundled
with GTK+-2.4, rendering  with OpenGL and the graphical user interface uses
GTK+ with GtkGLExt.  GLiv  is  very  fast  and smooth at rotating, panning  and
zooming  if  you have an OpenGL accelerated graphics board.

%prep
%setup -q -n %name-%version-%git
%patch -p2

%build
%autoreconf
%configure
%make_build

%install
%makeinstall MKINSTALLDIRS=../mkinstalldirs

install -d %buildroot%_datadir/pixmaps
install -d %buildroot%_datadir/applications
install -m 644 %name.png %buildroot%_datadir/pixmaps/%name.png
install -m 644 %name.svg %buildroot%_datadir/pixmaps/%name.svg
install -m 644 %name.desktop %buildroot%_datadir/applications/%name.desktop

%find_lang --with-man --output=%name.lang %name

%files -f %name.lang
%doc README COPYING NEWS THANKS
%_bindir/%name
%_datadir/pixmaps/*
%_datadir/applications/*
%_man1dir/%{name}.1*

%changelog
* Sat Mar 21 2020 L.A. Kostis <lakostis@altlinux.ru> 1.9.7-alt4.e7b0afc
- Update gettext patch.
- Update License tag.

* Thu May 02 2019 L.A. Kostis <lakostis@altlinux.ru> 1.9.7-alt3.e7b0afc
- bump gettext version requires.
- rebuild w/ recent autoconf (fixes #36667).
- added man page.

* Wed Dec 21 2016 L.A. Kostis <lakostis@altlinux.ru> 1.9.7-alt2.e7b0afc
- .spec: cleanup.

* Sun May 22 2016 L.A. Kostis <lakostis@altlinux.ru> 1.9.7-alt1.e7b0afc
- Ressurect again.
- .spec:
   + restructured sources
   + bump gettext version.

* Sat Jan 21 2012 L.A. Kostis <lakostis@altlinux.ru> 1.9.7-alt0.73.gf3892d1
- 1.9.7.
- Updated to GIT 73-gf3892d1 snapshot.
- Remove obsoleted patches and sources.

* Thu Apr 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.6-alt4
- fix build

* Sun Jun 28 2009 L.A. Kostis <lakostis@altlinux.ru> 1.9.6-alt3
- updated to GIT f3892d1.
- cleanup obsoleted macros.

* Tue Sep 02 2008 L.A. Kostis <lakostis@altlinux.ru> 1.9.6-alt2
- bring back from orphaned.

* Fri Aug 31 2007 LAKostis <lakostis at altlinux.ru> 1.9.6-alt1
- 1.9.6.

* Wed Mar 29 2006 LAKostis <lakostis at altlinux.org> 1.9.5-alt1
- 1.9.5;
- update buildreq (bump gtk+2 version);
- update russian translation (by Alexei V. Mezin);
- fix build with --as-needed ld option.

* Mon Feb 13 2006 LAKostis <lakostis at altlinux.org> 1.9.4-alt1.1
- update Buildreqires.

* Sun Jan 08 2006 LAKostis <lakostis at altlinux.org> 1.9.4-alt1
- 1.9.4.
- don't generate old menu entries.

* Sat Aug 13 2005 LAKostis <lakostis at altlinux.org> 1.9.3-alt1
- 1.9.3.

* Fri Apr 22 2005 LAKostis <lakostis at altlinux.org> 1.9.2-alt1
- 1.9.2.
- update Buildreqires.
- update man pages.

* Fri Jan 15 2005 LAKostis <lakostis at altlinux.org> 1.9.1-alt0.1
- 1.9.1.
- reformat description.

* Mon Oct 04 2004 LAKostis <lakostis at altlinux.org> 1.8.4-alt1.2
- #5276 (fix Requires).

* Sat Sep 25 2004 LAKostis <lakostis at altlinux.org> 1.8.4-alt1.1
- #5233
- update translation.

* Sat Sep 11 2004 LAKostis <lakostis at altlinux.org> 1.8.4-alt1
- initial build for Sisyphus.
