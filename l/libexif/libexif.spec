%define soname 12
%def_disable static

Name: libexif
Version: 0.6.22
Release: alt3

Summary: libexif is a library for parsing, editing, and saving EXIF data
License: LGPLv2+
Group: System/Libraries
Url: http://libexif.github.io
Packager: Dmitriy Khanzhin <jinn@altlinux.org>

# Source code: https://github.com/libexif/libexif/releases
Source: %name-%version.tar
Patch0: libexif-0.6.16-pkgconfig.patch
Patch1: libexif-0.6.22-upstream-fix-CVE-2020-0198.patch
Patch2: libexif-0.6.22-upstream-fix-use_the_correct_integer_type.patch
Patch3: libexif-0.6.22-upstream-fix-CVE-2020-0452.patch

# Automatically added by buildreq on Tue Jun 12 2007
BuildRequires: doxygen gcc-c++

%description
libexif is a library for parsing, editing, and saving EXIF data. It is
intended to replace lots of redundant implementations in command-line
utilities and programs with GUIs.

%package devel
Summary: Development file for %name library
Group: Development/C
Requires: %name = %version-%release

%description devel
libexif is a library for parsing, editing, and saving EXIF data. It is
intended to replace lots of redundant implementations in command-line
utilities and programs with GUIs.
This package contains all files which are needs to compile programs using
the %name library.

%package devel-static
Summary: Static %name library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
libexif is a library for parsing, editing, and saving EXIF data. It is
intended to replace lots of redundant implementations in command-line
utilities and programs with GUIs.
This package contains libraries which are needs to compile programs statically
linked against %name library.

%prep
%setup
%patch0 -p1 -b .pkgconfig
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall
%find_lang --output=%name.lang %name-%soname
/bin/rm -rf %buildroot%_datadir/doc/%name
/bin/bzip2 -9 ChangeLog

%files -f %name.lang
%doc AUTHORS NEWS README ChangeLog.bz2
%_libdir/*.so.*

%files devel
%_includedir/%name
%_libdir/*.so
%_libdir/pkgconfig/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Tue Jan 19 2021 Dmitriy Khanzhin <jinn@altlinux.org> 0.6.22-alt3
- added upstream commit:
  + fixed a incorrect overflow check that could be optimized away
    (fixes CVE-2020-0452)

* Fri Aug 21 2020 Dmitriy Khanzhin <jinn@altlinux.org> 0.6.22-alt2
- added upstream commits:
  + fixed another unsigned integer overflow (fixes CVE-2020-0198)
  + use correct integer type on PowerPC/RISC-based systems

* Wed May 27 2020 Dmitriy Khanzhin <jinn@altlinux.org> 0.6.22-alt1
- 0.6.22 (fixes: CVE-2016-6328, CVE-2017-7544, CVE-2019-9278, CVE-2020-0093,
  CVE-2020-12767, CVE-2020-13112, CVE-2020-13113, CVE-2020-13114,
  CVE-2018-20030)
- changed Url

* Sat Oct 27 2012 Dmitriy Khanzhin <jinn@altlinux.org> 0.6.21-alt1
- 0.6.21
- fixed CVE-2012-2812, CVE-2012-2813, CVE-2012-2814, CVE-2012-2836,
  CVE-2012-2837, CVE-2012-2840, CVE-2012-2841, CVE-2012-2845

* Sun Mar 13 2011 Dmitriy Khanzhin <jinn@altlinux.ru> 0.6.20-alt2
- rebuilt for debuginfo

* Thu Jan 06 2011 Dmitriy Khanzhin <jinn@altlinux.ru> 0.6.20-alt1
- 0.6.20 (closes: #24855)

* Wed Oct 13 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 0.6.19-alt2
- rebuilt for soname set-versions

* Fri Aug 27 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 0.6.19-alt1
- 0.6.19 (closes: #23961)

* Tue Dec 09 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 0.6.17-alt1
- 0.6.17 (closes: #17994)
- dropped unnecessary patches
- removed %%autoreconf (and package cvs from BuildRequires)
- bzip2 ChangeLog
- removed obsolete post{,un}_ldconfig calls

* Wed Apr 16 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 0.6.16-alt3
- cleanup spec
- supplemented some a descriptions
- added Packager tag
- renamed patches for fix previous CVE's

* Mon Dec 17 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 0.6.16-alt2
- security fixes:
  + CVE-2007-6351, CVE-2007-6352 (upstream patches)
  + thanks ldv@ for information
- licence tag changed to LGPLv2+

* Tue Jun 12 2007 Michael Shigorin <mike@altlinux.org> 0.6.16-alt1
- 0.6.16: major security fixes
  + this version fixes an integer overflow reported by iDefense
  + thanks ldv@ for heads up
- updated patch3
- disabled patch4, updated buildrequires (added doxygen)

* Mon May 14 2007 Michael Shigorin <mike@altlinux.org> 0.6.14-alt1
- 0.6.14: security fixes
  + http://secunia.com/advisories/25235/
    an error exists within the handling of malformed EXIF information;
    this can be exploited to crash an application using the library and may
    allow execution of arbitrary code
  + thanks Valery Inozemtsev (shrek@) for alerting
- s/autoconf/autoreconf -fisv/
- updated buildrequires
- got back translations (apparently missed in 0.6.13 due to
  packaging thinko re minor/soname during 0.6.12 with .so.12)
- demacrified Url:

* Thu Aug 10 2006 Michael Shigorin <mike@altlinux.org> 0.6.13-alt1
- 0.6.13
- removed patch0 (applied upstream), patch1 and patch2 (failed to apply)
- applied patch3, patch4 from Gentoo

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.6.12-alt3.1
- Rebuilt for new pkg-config dependencies.

* Thu Jun 16 2005 Michael Shigorin <mike@altlinux.org> 0.6.12-alt3
- rebuilt for Sisyphus, thanks Led for preparing fixed package
- *fixed* #6943 (libexif failed to handle quite some JPEGs)
-  fixed  #6681 (s/GPL/LGPL/)

* Tue May 24 2005 Yuri N. Sedunov <aris at altlinux.ru> 0.6.12-alt2
- fixed #6943

* Tue May 24 2005 Led <led@linux.kiev.ua> 0.6.12-alt1.1
- Prevent infinite recursion (#156365)
- Fix MakerNote handling (#153282)

* Mon Apr 11 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.6.12-alt1
- 0.6.12

* Mon Sep 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.6.10-alt1
- 0.6.10
- do not build devel-static subpackage by default.

* Thu Nov 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5.12-alt2
- Do not package .la files.

* Fri Sep 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5.12-alt1
- new version

* Mon Jan 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5.9-alt1
- new version

* Wed Oct 23 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.5.6-alt1
- 0.5.6
- Rebuilt in new environment

* Mon Mar 04 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.5.0-alt1
- First build for Sisyphus
