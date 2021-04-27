Name: mapsoft
Version: 20210121
Release: alt0.1.p9
License: GPL3.0

Summary: mapsoft - programs for working with maps and geodata
Group: Sciences/Geosciences
Url: http://github.org/ushakov/mapsoft
Packager: Vladislav Zavjalov <slazav@altlinux.org>

Source: %name-%version.tar
Patch1: 0001-skip-convs_gtiles.patch
Patch2: 0002-alt-fix-build.patch

BuildRequires: boost-devel gcc-c++ libcurl-devel libzip-devel zlib-devel
BuildRequires: libcairomm-devel libpixman-devel libgtkmm2-devel
BuildRequires: libpng-devel libjpeg-devel libtiff-devel libgif-devel
BuildRequires: libusb-devel libyaml-devel libxml2-devel proj-devel
BuildRequires: libjansson-devel libshape-devel
BuildRequires: python-devel scons swig m4
BuildRequires: /usr/bin/gs netpbm transfig ImageMagick-tools /usr/bin/pod2man
BuildRequires: boost-geometry-devel perl-Text-Iconv

%package tools
Summary: mapsoft-tools - rarely-used tools from mapsoft package
Group: Sciences/Geosciences
Requires: %name = %version-%release

%package vmap
Summary: mapsoft-vmap - programs for working with vector maps
Group: Sciences/Geosciences
Requires: %name = %version-%release

%description
mapsoft - programs for working with maps and geodata

%description tools
mapsoft-tools - rarely-used tools from mapsoft package

%description vmap
mapsoft-vmap - programs for working with vector maps

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
# boost::spirit crashes with -O2 on 32-bit systems
%if "%_lib" == "lib64"
export CCFLAGS=-O2
%endif

scons -Q minimal=1

%install
scons -Q minimal=1 -Q prefix=%buildroot install

%files
%_bindir/mapsoft_convert
%_bindir/mapsoft_mapview
%_mandir/man1/mapsoft_convert.*
%_mandir/man1/mapsoft_mapview.*
%_desktopdir/mapsoft_mapview.*

%files tools
%_bindir/convs_*
%_bindir/mapsoft_toxyz
%_bindir/mapsoft_geofig
%_bindir/mapsoft_mkmap
%_mandir/man1/mapsoft_geofig.*
%_libdir/gimp/2.0/plug-ins/map-helper.py

%files vmap
%_bindir/mapsoft_vmap
%_bindir/vmap_copy
%_bindir/vmap_render
%dir %_datadir/mapsoft
%_datadir/mapsoft/*
%_datadir/xfig/Libraries/*
%_mandir/man1/mapsoft_vmap.*
%_bindir/map_rescale
%_bindir/*.sh
%_bindir/map_*_gk
%_bindir/map_*_nom
%_bindir/mapsoft_wp_parse

%changelog
* Sat Mar 27 2021 Andrey Cherepanov <cas@altlinux.org> 20210121-alt0.1.p9
- Backport new version to p9 branch.

* Thu Jan 21 2021 Vladislav Zavjalov <slazav@altlinux.org> 20210121-alt1
- scripts/mapsoft_wp_parse: fix name conversions
- skip convs_gtiles program in Altlinux build (build problem with new boost)
- vector/data: add new types: point 0x650B, 0x650C (glacier names)
- vector/vmap3/vmap_mmb_filter: convert glacier names to points
- vector/vmap3: add vmap_put_track and vmap_get_track programs
- programs/mapsoft_map2fig: put images into compound object; add 50px margins

* Sat Dec 12 2020 Vladislav Zavjalov <slazav@altlinux.org> 20201212-alt1
- img_io/gobj_vmap: draw pattens with solid color at small scales (A.Kazantsev)
- fix for gcc-10
- fix a few compilation warnings (with -Wall) and a couple of possible related errors
- remove -O2 flag on i586 and armh (problem with new boost::spirit)

* Sun Dec 01 2019 Vladislav Zavjalov <slazav@altlinux.org> 20191201-alt1
- fix a few problems in vmap_render and convs_gtiles (thanks to A.Kazantsev)
- add GPL3.0 license (Altlinux requires ambiguous license for all packages)
- fix python shebang (python -> python2)

* Sun Nov 10 2019 Vladislav Zavjalov <slazav@altlinux.org> 20191110-alt1
- add more scripts to mapsoft_vmap package

* Fri Oct 04 2019 Vladislav Zavjalov <slazav@altlinux.org> 20190916-alt2
- fix build with libproj 6.2.0 (use DACCEPT_USE_OF_DEPRECATED_PROJ_API_H)

* Mon Sep 16 2019 Vladislav Zavjalov <slazav@altlinux.org> 20190916-alt1
- Fix build with new scons/python
- mapsoft_geofig: --raw option
- mapsoft_mapview: add desktop file
- mapsoft_vmap: fix error in label creation introduced in 2018-06-16

* Fri Feb 15 2019 Vladislav Zavjalov <slazav@altlinux.org> 20190213-alt2
- rebuild with libproj 5.2.0

* Wed Feb 13 2019 Vladislav Zavjalov <slazav@altlinux.org> 20190213-alt1
- current snapshot

* Sun Jul 22 2018 Vladislav Zavjalov <slazav@altlinux.org> 20180722-alt1
- current snapshot

* Wed Feb 03 2016 Vladislav Zavjalov <slazav@altlinux.org> 20160202-alt1.1
- rebuild with new libproj

* Tue Feb 02 2016 Vladislav Zavjalov <slazav@altlinux.org> 20160202-alt1
- build fix (man page extensions, .gz -> .*)

* Mon Oct 19 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20150103-alt1.2
- build fixed

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 20150103-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Sat Jan 03 2015 Vladislav Zavjalov <slazav@altlinux.org> 20150103-alt1
- current snapshot

* Wed Mar 05 2014 Vladislav Zavjalov <slazav@altlinux.org> 20140305-alt2
- current snapshot

* Wed Mar 05 2014 Vladislav Zavjalov <slazav@altlinux.org> 20140305-alt1
- current snapshot

* Tue Apr 09 2013 Vladislav Zavjalov <slazav@altlinux.org> 20130409-alt1
- current snapshot:

* Thu Nov 29 2012 Vladislav Zavjalov <slazav@altlinux.org> 20121129-alt1
- current snapshot
  - viewer projection change from menu
  - conic projection support
  - improve large maps handling
  - kml read/write support
  - some fixes

* Tue Oct 09 2012 Vladislav Zavjalov <slazav@altlinux.org> 20121009-alt2
- one more fix for new gcc

* Tue Oct 09 2012 Vladislav Zavjalov <slazav@altlinux.org> 20121009-alt1
- current snapshot, fix for new gcc

* Wed Sep 19 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120919-alt1
- rebuld with libpng15
- current snapshot:
  - partial read/write kml support
  - fix errors in save_image action

* Mon Jun 25 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120625-alt1
- current snapshot
 - simple navigation mode
 - support for tiled maps, some examples
 - faster map rescaling
 - support for finnish KKJ maps
 - add map-helper and mapsoft_mkmap to mapsoft-tools package
 - increase thickness of viewer marks

* Wed Jun 20 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120620-alt1
- current snapshot (more bugs fixed)

* Wed Jun 20 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120619-alt1
- build current snapshot (some bugs fixed)

* Sun Jun 17 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120617-alt1
- build current snapshot

* Sun May 06 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120506-alt1
- build current snapshot

* Mon Mar 05 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120304-alt1
- build current snapshot

* Thu Feb 16 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120222-alt1
- build current snapshot (16-02-2012)

* Sun Feb 12 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120221-alt1
- build current snapshot (12-02-2012)

* Wed Feb 08 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120220-alt1
- build current snapshot (08-02-2012)

* Tue Jan 10 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120110-alt1
- build current snapshot

* Tue Nov 22 2011 Vladislav Zavjalov <slazav@altlinux.org> 20111122-alt1
- build current snapshot

* Thu Nov 19 2009 Vladislav Zavjalov <slazav@altlinux.org> 20091119-alt1
- first build for altlinux

