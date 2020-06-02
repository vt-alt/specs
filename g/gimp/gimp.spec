%define _libexecdir %_prefix/libexec

%define ver_major 2.10
%define oldver 2.0

%define mypaint_ver 1.3
%define brushes_ver 1.0

Name: gimp
Version: %ver_major.18
Release: alt2

Summary: The GNU Image Manipulation Program
License: %gpl3only
Group: Graphics
Url: http://www.gimp.org/

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Obsoletes: gimp2 < %version-%release
Provides: gimp2 = %version-%release
Conflicts: gimp2-perl create-resources <= 0.1.3-alt1
Requires: lib%name = %version-%release
Requires: icc-profiles mypaint-brushes%brushes_ver

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: bzlib-devel gcc-c++ gtk-doc gvfs intltool libXcursor-devel libXmu-devel libXpm-devel libalsa-devel libexpat-devel
BuildRequires: libgegl-devel libgexiv2-devel libgs-devel libgudev-devel liblcms2-devel liblzma-devel libmng-devel libopenjpeg2.0-devel
BuildRequires: libpoppler-glib-devel librsvg-devel libtiff-devel libwebkitgtk2-devel libwebp-devel libwmf-devel
BuildRequires: openexr-devel xdg-utils libpng-devel iso-codes-devel libheif-devel libXfixes-devel
BuildRequires: python-module-pycairo-devel python-module-pygtk-devel
BuildRequires: libmypaint-devel >= %mypaint_ver mypaint-brushes%brushes_ver-devel

%description
The GIMP (GNU Image Manipulation Program) is a powerful image
composition and editing program, which can be extremely useful for
creating logos and other graphics for Web pages.  The GIMP has many of
the tools and filters you would expect to find in similar commercial
offerings, and some interesting extras as well. The GIMP provides a
large image manipulation toolbox, including channel operations and
layers, effects, sub-pixel imaging and anti-aliasing, and conversions,
all with multi-level undo.

%package -n lib%name
Summary: GIMP libraries
Group: System/Libraries
License: %lgpl3only
Obsoletes: libgimp2 < %version-%release
Provides: libgimp2 = %version-%release

%description -n lib%name
Libraries used to communicate between The GIMP and other programs which
may function as "GIMP plugins".

%package -n lib%name-devel
Summary: GIMP plugin and extension development kit
Group: Graphics
Requires: lib%name = %version-%release
Obsoletes: libgimp2-devel < %version-%release
Provides: libgimp2-devel = %version-%release

%description -n lib%name-devel
Development libraries and header files for writing GIMP plugins and extensions.

%add_python_lib_path %_libdir/%name/%oldver/python

%prep
%setup -q
%patch -p1

%build
gtkdocize
%autoreconf
%configure \
	--with-gimpdir=%name \
	--enable-gtk-doc \
	--disable-gimp-console \
	--enable-python

%make_build V=1

%install
%make DESTDIR=%buildroot install

find %buildroot%_libdir/%name -name \*.la -delete

# Execute find_lang for all components and merge the resulting lists
%find_lang --output=global.lang gimp20 gimp20-libgimp gimp20-std-plug-ins gimp20-script-fu gimp20-tips gimp20-python

%files -f global.lang
%doc AUTHORS NEWS README README.i18n
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/%oldver
%config %_sysconfdir/%name/%oldver/*
%_bindir/%name
%_bindir/%name-*
%_libdir/%name
%_datadir/%name
%_datadir/metainfo/*.xml
%_iconsdir/hicolor/*/apps/*
%_desktopdir/%name.desktop
%_man1dir/*
%_man5dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_datadir/gtk-doc/html/*
%_includedir/*
%_bindir/gimptool*
%_libexecdir/gimp-debug-tool-2.0
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/aclocal/*

%changelog
* Wed Mar 18 2020 Valery Inozemtsev <shrek@altlinux.ru> 2.10.18-alt2
- rebuilt against libmypaint-1.5.1/mypaint-brushes1.0-1.3.1

* Mon Mar 02 2020 Valery Inozemtsev <shrek@altlinux.ru> 2.10.18-alt1
- 2.10.18

* Fri Nov 01 2019 Valery Inozemtsev <shrek@altlinux.ru> 2.10.14-alt1
- 2.10.14

* Thu Jun 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 2.10.12-alt1
- 2.10.12

* Mon Apr 08 2019 Valery Inozemtsev <shrek@altlinux.ru> 2.10.10-alt1
- 2.10.10

* Mon Nov 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.10.8-alt1
- 2.10.8

* Fri Aug 31 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.10.6-alt1
- 2.10.6

* Tue Aug 07 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.10.4-alt2
- update russian translation

* Thu Jul 05 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.10.4-alt1
- 2.10.4

* Wed Jun 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Tue May 08 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Mon May 29 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.8.22-alt1
- 2.8.22

* Mon May 15 2017 Anton Farygin <rider@altlinux.ru> 2.8.20-alt2
- NMU: rebuild with new libmng

* Wed Feb 08 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.8.20-alt0.M80P.1
- backport to p8 branch

* Wed Feb 01 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.8.20-alt1
- 2.8.20

* Tue Jul 26 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.8.18-alt1
- 2.8.18

* Fri Jul 15 2016 Andrey Cherepanov <cas@altlinux.org> 2.8.16-alt2
- Fix greenish border when antialiasing of text is on

* Sun Dec 20 2015 Valery Inozemtsev <shrek@altlinux.ru> 2.8.16-alt1
- 2.8.16
- compiled with liblcms2 (closes: #29940)

* Wed Aug 27 2014 Valery Inozemtsev <shrek@altlinux.ru> 2.8.14-alt1
- 2.8.14

* Sun Dec 01 2013 Valery Inozemtsev <shrek@altlinux.ru> 2.8.10-alt1
- 2.8.10

* Wed Nov 06 2013 Valery Inozemtsev <shrek@altlinux.ru> 2.8.8-alt1
- 2.8.8

* Tue Jun 25 2013 Valery Inozemtsev <shrek@altlinux.ru> 2.8.6-alt1
- 2.8.6

* Thu Feb 07 2013 Valery Inozemtsev <shrek@altlinux.ru> 2.8.4-alt1
- 2.8.4

* Fri Dec 28 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.8.2-alt2
- updated to gimp-2-8 git.29ca295

* Fri Aug 24 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.8.2-alt1
- 2.8.2

* Thu May 03 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.8.0-alt1
- 2.8.0 release

* Wed Apr 04 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.8.0-alt0.rc1
- 2.8.0 RC1

* Thu Feb 02 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.6.12-alt1
- 2.6.12

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.6.11-alt5.1
- Rebuild with Python-2.7

* Wed Aug 10 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.6.11-alt5
- fixed CVE-2011-1782

* Wed Apr 20 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.6.11-alt4
- updated build dependencies
- removed %_datadir/create/{brushes,gradients,patterns}

* Tue Feb 15 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.6.11-alt3
- rebuild with libpoppler-glib.so.6

* Fri Oct 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.6.11-alt2
- rebuild with libwebkitgtk-1.0.so.0

* Mon Oct 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.6.11-alt1
- 2.6.11

* Thu Aug 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.6.10-alt2
- rebuild with libpoppler-glib.so.5

* Sat Jul 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.6.10-alt1
- 2.6.10

* Thu Jul 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.6.9-alt2
- fixed crashes when clicking any scroll bar from combo boxes (closes: #23697)

* Wed Jun 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.6.9-alt1
- 2.6.9

* Tue Mar 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.6.8-alt4
- backport statusbar code needed for GTK+ >= 2.19.1

* Fri Jan 29 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.6.8-alt3
- fixed python provides (closes: #22852)

* Wed Dec 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.8-alt2
- rebuild without hal

* Sun Dec 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.8-alt1
- 2.6.8

* Sat Nov 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.7-alt6
- build without gnome-vfs

* Tue Nov 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.7-alt5
- fixed CVE-2009-3909

* Thu Nov 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.7-alt4
- fixed CVE-2009-1570

* Mon Oct 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.7-alt3
- rebuild with gegl-0.1.0

* Tue Sep 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.7-alt2
- rebuild with poppler-0.12.0

* Fri Aug 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.7-alt1
- 2.6.7

* Tue Jun 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.6-alt6
- rebuild with libpng12 1.2.37-alt2

* Mon May 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.6-alt5
- pdf plugin: build with poppler

* Sun May 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.6-alt4
- rebuild

* Sat May 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.6-alt3
- fixed help-browser

* Wed Apr 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.6-alt2
- rebuild with libwebkit-1.0.so.2

* Wed Mar 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.6-alt1
- 2.6.6

* Mon Feb 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.5-alt1
- 2.6.5

* Tue Jan 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.4-alt2
- enabled gimp-remote

* Thu Jan 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Tue Nov 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.6.2-alt2
- fixed gimptool (close #17783)

* Thu Oct 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Fri Oct 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Wed Oct 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Sat Aug 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.4.7-alt2
- build without poppler

* Fri Aug 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.4.7-alt1
- 2.4.7

* Sun Jun 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.4.6-alt1
- 2.4.6

* Thu May 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.4.5-alt2
- rebuild with poppler-0.8.0

* Sun Mar 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.4.5-alt1
- 2.4.5

* Fri Feb 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Mon Dec 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Sat Dec 08 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.4.2-alt2
- fixed menu (bug #13610)

* Thu Nov 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.4.2-alt0.M40.1
- build for branch 4.0
- added conflicts to gimp2-perl (close #13364)

* Wed Nov 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Sat Nov 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Wed Oct 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.4.0-alt1
- 2.4.0 release

* Fri Sep 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.4.0-alt0.rc3
- 2.4.0 RC3

* Mon Aug 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.2.17-alt2
- relocated gimprc.5 manpage to gimp
- added %%update_menus in %%post

* Mon Jul 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.2.17-alt0.M40
- build for branch 4.0

* Sun Jul 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.2.17-alt1
- Bugs fixed in GIMP 2.2.17:
    + fixed regression in PSD load plug-in (bug #456042)
    + fixed crash when loading a corrupt PSD file (bug #327444)
    + work around for Pango appending " Not-Rotated" to font names 
- Bugs fixed in GIMP 2.2.16:
    + improved input value validation in several file plug-ins (bug #453973)
    + improved handling of corrupt or invalid XCF files
    + guard against integer overflows in several file plug-ins (bug #451379)
    + fixed handling of background alpha channel in XCF files (bug #443097)
    + improved forward compatibility of the config parser
    + fixed crash when previewing some animated brushes (bug #446005)

* Tue Jul 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.2.15-alt2
- fixed CVE-2007-2949

* Mon May 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.2.15-alt1
- 2.2.15:
  + fixed parsing of GFig files with CRLF line endings (bug #346988)
  + guard against a possible stack overflow in the Sunras loader (bug #433902)
  + fixed definition of datarootdir in gimptool-2.0 (bug #436386)
  + fixed Perspective tool crash on Mac OS X (bug #349483)
  + fixed area resizing in the Image Map plug-in (bug #439222)
  + added missing library in gimptool-2.0 --libs output
  + added new localizations: Occitan and Persian

* Mon May 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.2.14-alt3
- build without gimp-print, used gimp-plugin-gutenprint

* Sun May 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.2.14-alt2
- added gimp-2.2.14-sunras-overflow.patch: avoid buffer overflow in sunras plugin

* Sat May 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.2.14-alt1
- 2.2.14
- rename gimp2 to gimp
- added Tango themes by defaults
- build with python

* Sun Feb 11 2007 Anatoly Yakushin <jaa@altlinux.ru> 2.2.13-alt2
- L. A. Kostis <lakostis@altlinux.ru> 2.2.13-alt2
   NMU:
    + move gimptool to -devel subpackage (closes #9955).

* Mon Oct 23 2006 Anatoly Yakushin <jaa@altlinux.ru> 2.2.13-alt1
- 2.2.13

* Mon Jun 19 2006 Anatoly Yakushin <jaa@altlinux.ru> 2.2.11-alt1
- 2.2.11

* Sun Jun 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.11-alt0.1
- 2.2.11
- updated build dependencies
- move to freedesktop menu
- disabled MMX/SSE

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.2.10-alt1.1
- Rebuilt for new pkg-config dependencies.

* Fri Jan 06 2006 Anatoly Yakushin <jaa@altlinux.ru> 2.2.10-alt1
- new version. Fixed russian translation bug # 123410

* Wed May 11 2005 Anatoly Yakushin <jaa@altlinux.ru> 2.2.7-alt1
- new stable version

* Mon Apr 25 2005 Anatoly Yakushin <jaa@altlinux.ru> 2.2.6-alt1
- update ru po
- Yuri N. Sedunov has added
  - 2.2.6
  - rebuild against libexif.so.12. 
  - svg support via librsvg2 enabled.
  - requires gtk+ >= 2.2.4
  - fixed source url.

* Sun Mar 13 2005 Anatoly Yakushin <jaa@altlinux.ru> 2.2.4-alt1
- new stable version, minor bugs fixed.

* Tue Jan 11 2005 Anatoly Yakushin <jaa@altlinux.ru> 2.2.2-alt1
- new stable version, minor bugs fixed.

* Mon Jan 10 2005 Anatoly Yakushin <jaa@altlinux.ru> 2.2.1-alt1
- new stable version
- update ru translation

* Sun Nov 21 2004 Anatoly Yakushin <jaa@altlinux.ru> 2.2-alt0.1.pre2
- new developer version

* Tue Nov 09 2004 Anatoly Yakushin <jaa@altlinux.ru> 2.2-alt0.1.pre1
- new developer version 

* Sun Oct 03 2004 Anatoly Yakushin <jaa@altlinux.ru> 2.0.5-alt1
- new stable version

* Tue Sep 07 2004 Anatoly Yakushin <jaa@altlinux.ru> 2.0.4-alt1
- new stable version

* Sat Jul 24 2004 Anatoly Yakushin <jaa@altlinux.ru> 2.0.3-alt2
- fixed bug - don't open and save non latin1 or utf-8 filename 

* Sun Jul 18 2004 Anatoly Yakushin <jaa@altlinux.ru> 2.0.3-alt1
- new version
- remove gimp.desktop from src.rpm.
- convert gimp.xpm to gimp.png, install it in /usr/share/pixmaps as menu icon
- remove unusual %%clean section.
- use post{un}_ldconfig macros for libgimp2 subpackage.
- optimize find-lang call.
- allow SMP build.
- clean %%install section
- fix %%files to remove %%_libdir/*.so from libgimp2 subpackage.
- clean .spec using cleanup_spec and manually.
- Special thanks Yuri N. Sedunov aka Aris for his help.

* Thu Jun 24 2004 Anatoly Yakushin <jaa@altlinux.ru> 2.0.2-alt1
- new version, bug # 3459 fixed

* Mon May 10 2004 Anatoly Yakushin <jaa@altlinux.ru> 2.0.1-alt2
- spec cleanup, po bugs fixed

* Wed Apr 21 2004 Anatoly Yakushin <jaa@altlinux.ru> 2.0.1-alt1
- Bugs fixed version GIMP 2.0.1

* Wed Mar 24 2004 Anatoly Yakushin <jaa@altlinux.ru> 2.0.0-alt1
- GIMP 2.0.0 new stable build

* Sun Mar 07 2004 Anatoly Yakushin <jaa@altlinux.ru> 2.0-alt0.3.pre4
- new version

* Sun Feb  8 2004 Anatoly Yakushin <jaa@altlinux.ru> 2.0-alt0.2.pre3
- add color proof

* Mon Nov 10 2003 Anatoly Yakushin <jaa@altlinux.ru> 1.3.22-alt1
- new version, spec cleanup

* Mon Oct 13 2003 Anatoly Yakushin <jaa@altlinux.ru> 1.3.21-alt1
- new version

* Sat Aug 30 2003 Anatoly Yakushin <jaa@altlinux.ru> 1.3.19-alt1
- new version

* Sun Jun 29 2003 Anatoly Yakushin <jaa@altlinux.ru> 1.3.16-alt1
- new version

* Wed May 28 2003 Anatoly Yakushin <jaa@altlinux.ru> 1.3.14-alt2
- fixed bugs in spec file, add new ru.po

* Sun Apr 13 2003 Anatoly Yakushin <jaa@altlinux.ru> 1.3.14-alt1
- package in Sisyphus

* Mon Mar 24 2003 Anatoly Yakushin <jaa@altlinux.ru> 1.3.13-alt0.1
- version 1.3.13

* Wed Mar 19 2003 Anatoly Yakushin <jaa@altlinux.ru> 1.3.12-alt0.1
- Adapted spec for AltLinux

* Fri Feb 14 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Reinvented the wheel, but packaged 1.3.11.

* Fri Apr 14 2000 Matt Wilson <msw@redhat.com>
- include subdirs in the help find
- remove gimp-help-files generation
- both gimp and gimp-perl own prefix/lib/gimp/1.1/plug-ins
- both gimp and gimp-devel own prefix/lib/gimp/1.1 and
  prefix/lib/gimp/1.1/modules

* Thu Apr 13 2000 Matt Wilson <msw@redhat.com>
- 1.1.19
- get all .mo files

* Wed Jan 19 2000 Gregory McLean <gregm@comstar.net>
- Version 1.1.15

* Wed Dec 22 1999 Gregory McLean <gregm@comstar.net>
- Version 1.1.14
- Added some auto %files section generation scriptlets

