%define ver_major 2.1

Name: rawstudio
Version: %ver_major
Release: alt0.5

Summary: Rawstudio is an open source raw-image converter written in GTK+
License: GPLv2+
Group: Graphics

URL: http://rawstudio.org/
#VCS: https://github.com/rawstudio/rawstudio
Source: %name-%version.tar
#Source: http://rawstudio.org/files/release/rawstudio-%version.tar.gz

Patch1: rawstudio-2.0-fc-lensfun.patch
Patch2: rawstudio-2.1-alt-lfs.patch
Patch3: rawstudio-2.1-exiv2-0.27.patch

BuildRequires: gcc-c++ libappstream-glib-devel libGConf-devel libdbus-devel libexiv2-devel libfftw3-devel libflickcurl-devel
BuildRequires: libgphoto2-devel libgtk+3-devel libjpeg-devel liblcms-devel liblensfun-devel libpng-devel
BuildRequires: libsqlite3-devel libssl-devel libtiff-devel libosm-gps-map-devel libxml2-devel

%description
Rawstudio can read and convert RAW-images from most digital cameras.

%prep
%setup
%patch1 -p1
%patch2
%patch3 -p1 -b .exiv2

[ ! -d m4 ] && mkdir m4

%build
glib-gettextize -c -f
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_libdir/%name/
%_datadir/%name/
%_libdir/lib%name-%ver_major.so
%_libdir/lib%name.so
%_datadir/rawspeed/
%_pixmapsdir/*
%_iconsdir/%name.png
#%_liconsdir/*
%_desktopdir/%name.desktop
%_datadir/appdata/%name.appdata.xml

%exclude %_includedir/%name-%ver_major/
#%exclude %_libdir/*.so
%exclude %_pkgconfigdir

%changelog
* Sun Aug 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2.1-alt0.5
- rebuilt against libexiv2.so.27

* Mon Sep 25 2017 Yuri N. Sedunov <aris@altlinux.org> 2.1-alt0.4
- updated to v2.0-589-g003dd4f (ported to GTK+3)
- built against libexiv2.so.26

* Thu Jan 21 2016 Yuri N. Sedunov <aris@altlinux.org> 2.1-alt0.3
- rebuilt against liblensfun.so.1

* Mon Jun 29 2015 Yuri N. Sedunov <aris@altlinux.org> 2.1-alt0.2
- rebuilt against libexiv2.so.14

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.1-alt0.1.1
- Rebuilt for gcc5 C++11 ABI.

* Thu Feb 19 2015 Yuri N. Sedunov <aris@altlinux.org> 2.1-alt0.1
- 2.1 snapshot

* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0-alt6
- rebuilt against libexiv2.so.13

* Fri Jan 25 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0-alt5
- rebuilt against libexiv2.so.12
- enabled lfs support
- don't use chrpath to fix RPATH problem

* Mon Oct 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt4.1
- Rebuilt with libpng15

* Fri Apr 06 2012 Victor Forsiuk <force@altlinux.org> 2.0-alt4
- Fix g_thread_init() issue with glib 2.32+.

* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 2.0-alt3
- Fix RPATH issue.

* Wed Nov 02 2011 Yuri N. Sedunov <aris@altlinux.org> 2.0-alt2
- rebuilt against libexiv2.so.11

* Fri Apr 08 2011 Victor Forsiuk <force@altlinux.org> 2.0-alt1
- 2.0

* Tue Jun 01 2010 Victor Forsiuk <force@altlinux.org> 1.2-alt5
- Rebuild with libexiv2.so.9.

* Mon Jan 04 2010 Victor Forsyuk <force@altlinux.org> 1.2-alt4
- Rebuild with libexiv2.so.6.

* Fri Nov 13 2009 Victor Forsyuk <force@altlinux.org> 1.2-alt3
- Package icon that accessed by rawstudio but does not installed by Makefile.

* Mon Jul 20 2009 Victor Forsyuk <force@altlinux.org> 1.2-alt2
- Rebuild with libexiv2.so.5.

* Tue Jun 09 2009 Victor Forsyuk <force@altlinux.org> 1.2-alt1
- 1.2

* Thu Oct 23 2008 Victor Forsyuk <force@altlinux.org> 1.1.1-alt1
- 1.1.1

* Tue Sep 16 2008 Victor Forsyuk <force@altlinux.org> 1.1-alt1
- 1.1

* Wed Apr 30 2008 Victor Forsyuk <force@altlinux.org> 1.0-alt1
- 1.0

* Mon Apr 14 2008 Victor Forsyuk <force@altlinux.org> 0.7-alt2
- Desktop file mime entry fix.

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 0.7-alt1
- 0.7

* Wed Sep 05 2007 Victor Forsyuk <force@altlinux.org> 0.6-alt1
- 0.6

* Wed Mar 21 2007 Victor Forsyuk <force@altlinux.org> 0.5.1-alt1
- 0.5.1

* Thu Feb 08 2007 Victor Forsyuk <force@altlinux.org> 0.5-alt1
- 0.5

* Fri Sep 29 2006 Victor Forsyuk <force@altlinux.ru> 0.4.1-alt1
- Initial build.
