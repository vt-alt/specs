%define ver_major 0.10
%define _libexecdir %_prefix/libexec

Name: gstreamer%ver_major
Version: %ver_major.36
Release: alt2
Summary: GStreamer streaming media framework runtime (legacy version)
License: LGPL
Group: System/Libraries
URL: http://gstreamer.freedesktop.org
Packager: Andrey Cherepanov <cas@altlinux.org>

Requires: lib%name = %version-%release

Source: gstreamer-%version.tar
Source1: common.tar
Patch: gstreamer-%version-%release.patch
Patch1: gstreamer-0.10.36-bison3.patch

BuildRequires: docbook-utils flex gcc-c++ ghostscript-utils glib2-devel gtk-doc intltool libcheck-devel libxml2-devel
BuildRequires: python-modules sgml-common transfig xml-utils gobject-introspection-devel

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

%package -n lib%name
Summary: Shared libraries of GStreamer (legacy version)
Group: System/Libraries

%description -n lib%name
This package contains the shared libraries of the GStreamer media framework

%package -n lib%name-gir
Summary: GObject introspection data for the GStreamer library (legacy version)
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the GStreamer library

%package devel
Summary: Development files for GStreamer streaming-media framework (legacy version)
Group: Development/C
Requires: lib%name = %version-%release

%description devel
This package contains the libraries and header files necessary to
develop applications and plugins for GStreamer

%package gir-devel
Summary: GObject introspection devel data for the GStreamer library (legacy version)
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the GStreamer library

%prep
%setup -q -a1 -n gstreamer-%version
%patch -p1
%patch1 -p1

touch ABOUT-NLS config.rpath
subst '/.PHONY/d' Makefile.am

%build
%autoreconf
%configure \
	--with-package-name=GStreamer \
	--with-package-origin=%name \
	--disable-examples \
	--disable-valgrind \
	--disable-docbook \
	--disable-gtk-doc \
	--disable-rpath \
	--disable-tests \
	--disable-debug \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name-%ver_major

%files -f %name-%ver_major.lang
%doc AUTHORS NEWS README RELEASE
%_libexecdir/gstreamer-%ver_major
%dir %_libdir/gstreamer-%ver_major
%_libdir/gstreamer-%ver_major/*.so

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-gir
%_libdir/girepository-1.0/*.typelib

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/aclocal/*

%files gir-devel
%_datadir/gir-1.0/*.gir

%changelog
* Wed Jul 24 2019 Andrey Cherepanov <cas@altlinux.org> 0.10.36-alt2
- Rename to gstreamer0.10.
- Package minimal bundle for for legacy applications like VMware-Horizon-Client.
- Fix build with bison3.

* Tue Feb 21 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.10.36-alt1
- 0.10.36

* Fri Jun 17 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.35-alt1
- 0.10.35

* Sun May 15 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.34-alt1
- 0.10.34

* Sat May 14 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.33-alt1
- 0.10.33

* Wed Feb 16 2011 Alexey Tourbin <at@altlinux.ru> 0.10.32-alt2
- rebuilt for debuginfo

* Sat Jan 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.32-alt1
- 0.10.32

* Tue Nov 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.31-alt1
- 0.10.31

* Fri Nov 19 2010 Dmitry V. Levin <ldv@altlinux.org> 0.10.30-alt2
- Minor specfile cleanup.
- Rebuilt for soname set-versions.

* Fri Jul 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.30-alt1
- 0.10.30

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
- enabled gobject-introspection

* Mon Oct 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.25-alt1
- 0.10.25

* Wed Aug 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.24-alt1
- 0.10.24

* Mon May 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.23-alt1
- 0.10.23

* Thu Feb 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.22-alt2
- enabled gst-debug (close #18905)

* Tue Jan 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.22-alt1
- 0.10.22

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.21-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Tue Nov 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.21-alt0.M41.1
- build for branch 4.1

* Fri Oct 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.21-alt1
- 0.10.21

* Wed Jun 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.20-alt1
- 0.10.20

* Thu May 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.19-alt2
- disable gst-debug

* Thu Apr 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.19-alt1
- 0.10.19

* Sat Mar 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.18-alt1
- 0.10.18

* Thu Feb 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.17-alt1
- 0.10.17
- spec cleanup
- update build dependencies

* Fri Jan 25 2008 Igor Zubkov <icesik@altlinux.org> 0.10.14-alt2
- merge changes from inger@

* Fri Dec 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.10.14-alt1.M40.1
- remove cm-fonts-super-pfb from buildreqs

* Mon Sep 10 2007 Igor Zubkov <icesik@altlinux.org> 0.10.14-alt1
- 0.10.13 -> 0.10.14

* Tue Jun 19 2007 Igor Zubkov <icesik@altlinux.org> 0.10.13-alt2
- fix build requires

* Tue Jun 19 2007 Igor Zubkov <icesik@altlinux.org> 0.10.13-alt1
- 0.11.12 -> 0.11.13
- remove set_verify_elf_method textrel=relaxed
- buildreq and update build requires

* Tue Mar 13 2007 Igor Zubkov <icesik@altlinux.org> 0.10.12-alt1
- 0.10.11 -> 0.11.12

* Wed Feb 21 2007 Igor Zubkov <icesik@altlinux.org> 0.10.11-alt2
- add check to build requires

* Thu Dec 21 2006 Igor Zubkov <icesik@altlinux.org> 0.10.11-alt1
- 0.10.10 -> 0.10.11

* Fri Dec 01 2006 Igor Zubkov <icesik@altlinux.org> 0.10.10-alt1
- 0.10.9 -> 0.10.10 

* Wed Aug 23 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.9-alt1
- Release 0.10.9
- Dropped 0.10 from package names

* Fri Jun 16 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.8-alt2
- x86_64 fix: exclude the documentation not installed for some murky reason

* Mon Jun 12 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.8-alt1
- Updated to 0.10.8

* Fri Jun 02 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.6-alt2
- Require check built with -fPIC

* Sun May 28 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.6-alt1
- Updated to 0.10.6
- Retired Patch0

* Sun Mar 12 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.4-alt1
- Release 0.10.4
- Added a buildreq ignore pattern to avoid getting all installed plugins

* Sat Feb 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.3-alt1
- 0.10.3

* Wed Jan 18 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.2-alt1
- 0.10.2

* Wed Dec 28 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.1-alt1
- 0.10.1

* Sat Dec 10 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.0-alt1
- Updated to 0.10.0
- Renamed to gstreamer0.10 to install in parallel to gstreamer 0.8
  for the time being
- Removed rpm macros and install scripts as the utilities they use are gone
- Retired the cache directory

* Fri Nov 25 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.9.6-alt1
- Updated to 0.9.6 (unstable)

* Mon Sep 05 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.8.11-alt1
- 0.8.11
- Removed obsolete libmmx conditional
- Disabled valgrind

* Mon Jun 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.8.10-alt1
- 0.8.10

* Wed Feb 09 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.8.9-alt1
- 0.8.9

* Fri Jan 21 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.8.8-alt1.1
- fixed rpm macros.

* Thu Dec 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.8-alt1
- 0.8.8
- documentation moved to devel-doc subpackage.

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.7-alt1
- 0.8.7

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.5-alt1
- 0.8.5

* Mon Jun 07 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.3-alt1
- 0.8.3

* Fri Apr 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Fri Apr 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Sun Feb 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.7.5-alt1
- 0.7.5

* Sat Jan 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.7.3-alt2.1
- fix %%post and macros.

* Sun Jan 18 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.3-alt2
- Fix incorrect dependencies causing a rebuild on make install [Patch0]
- Don't build PDF and PS documentation, this process is brittle,
  pulls in a ton of dependencies, and produces only extra copies
  in addition to HTML [Patch1]
- Corrected doc installation, include manuals, faq and examples
- Buildreq
- aris:
    + removed unusual devhelp stuff

* Sat Dec 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7.3-alt1
- 0.7.3

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.4-alt2
- do not package .la files.
- do not build devel-static subpackage by default.

* Mon Oct 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.4-alt1
- 0.6.4

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Sat Jun 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Sun Apr 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Sun Feb 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Wed Jan 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5.2-alt1
- new version.

* Mon Jan 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5.1-alt1.2
- fixed dependece for devel-static subpackage.

* Thu Jan 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5.1-alt1.1
- removed cycle dependence.

* Wed Jan 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5.1-alt1
- new version.
- utils subpackage to fix %%postun processes for gstreamer-plugins.

* Thu Dec 12 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Fri Nov 08 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.2-alt0.6
- Fixed build (SMP-incompatible build)
- %%post improved.
- Added %%gst_compprep macro.

* Sat Nov 02 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.2-alt0.5
- 0.4.2

* Wed Apr 24 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.3.4-alt0.1
- First build for Sisyphus.
