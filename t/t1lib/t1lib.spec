Name: t1lib
Version: 5.1.2
Release: alt6

Summary: Type 1 font rasterizer
License: LGPL
Group: System/Libraries

Url: ftp://sunsite.unc.edu/pub/Linux/libs/graphics/
# ftp://ibiblio.org/pub/Linux/libs/graphics/%name-%version.tar.gz
Source: %name-%version.tar
Source1: t1lib-CP1251.enc
Source2: t1lib-KOI8-R.enc
Source3: t1lib-KOI8-U.enc
Patch2: t1lib-5.1.2-alt-makefile-doc.patch
Patch3: t1lib-5.1.2-alt-config.patch
Patch4: t1lib-5.1.2-deb-alt-fixes.patch

# Patches from Gentoo
Patch100: t1lib-5.1.2-CVE-2010-2642_2011-0433_2011-5244.patch
Patch101: t1lib-5.1.2-CVE-2011-0764.patch
Patch102: t1lib-5.1.2-CVE-2011-1552_1553_1554.patch
Patch103: t1lib-5.1.2-format-security.patch

# Automatically added by buildreq on Sat May 10 2008
BuildRequires: imake libXaw-devel libXpm-devel texlive-context texlive-collection-latexrecommended xorg-cf-files libXext-devel
BuildPreReq: libSM-devel libXmu-devel

%def_disable static

%package x
Summary: Type 1 font rasterizer X.Org libraries
Group: System/Libraries
Requires: %name = %EVR

%package devel
Summary: Type 1 font rasterizer development files
Group: Development/C
Requires: %name = %EVR

%package devel-static
Summary: Type 1 font rasterizer static libraries
Group: Development/C
Requires: %name-devel = %EVR

%package utils
Summary: Utilities for manipulating Type 1 fonts
License: GPL
Group: Graphics
Requires: %name = %EVR

%description
T1lib is a library for generating character and string-glyphs from
Adobe Type 1 fonts under UNIX.  T1lib uses most of the code of the X11
rasterizer donated by IBM to the X11-project.  But some disadvantages of
the rasterizer being included in X11 have been eliminated.  T1lib also
includes a support for antialiasing.

%description x
T1lib is a library for generating character and string-glyphs from
Adobe Type 1 fonts under UNIX.
This package contains X.Org-dependent libraries.

%description devel
This package contains development files required for building
%name-based software.

%description devel-static
This package contains static libraries required for building
statically linked %name-based software.

%description utils
This package contains the programs "xglyph" and "type1afm"
It also contains the "t1libconfig" script used to configure %name.

%prep
%setup
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1

%patch2 -p1
%patch3 -p1
%patch4 -p2

%build
autoconf
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' configure
%configure %{subst_enable static}
%make_build without_doc

pushd doc
	make clean
	make pdf
	bzip2 -9 t1lib_doc.pdf
popd

%install
%make_install DESTDIR=%buildroot install
mkdir -p %buildroot%_datadir/t1lib/enc
install -pm644 Fonts/enc/*  %buildroot%_datadir/%name/enc
install -pm644 %SOURCE1 %buildroot%_datadir/%name/enc/CP1251.enc
install -pm644 %SOURCE2 %buildroot%_datadir/%name/enc/KOI8-R.enc
install -pm644 %SOURCE3 %buildroot%_datadir/%name/enc/KOI8-U.enc

%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir
install -pm644 Changes README.t* doc/t1lib_doc.pdf.bz2 %buildroot%docdir/

%files
%_libdir/libt1.so.*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.config
%dir %_datadir/%name
%_datadir/%name/*
%dir %docdir
%doc %docdir/[A-Z]*

%files x
%_libdir/libt1x.so.*

%files devel
%_libdir/*.so
%_includedir/*
%dir %docdir
%doc %docdir/t1lib_doc.pdf.bz2

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%files utils
%_bindir/*

# TODO:
# - merge type1afm.1 manpage from debian patch

%changelog
* Wed Oct 21 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.2-alt6
- Applied security fixes from Gentoo (Fixes: CVE-2010-2642, CVE-2011-0433,
  CVE-2011-0764, CVE-2011-1552, CVE-2011-1553, CVE-2011-1554, CVE-2011-5244).

* Sat Mar 03 2018 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt5.1
- NMU: rebuild with TeXLive instead of TeTeX

* Thu Jan 19 2012 Michael Shigorin <mike@altlinux.org> 5.1.2-alt5
- drop RPATH
- minor spec cleanup

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.2-alt4.1
- Rebuilt for soname set-versions

* Thu Oct 29 2009 Grigory Batalov <bga@altlinux.ru> 5.1.2-alt4
- Split into t1lib and t1lib-x packages (latter is X.Org-dependent).

* Mon Dec 01 2008 Michael Shigorin <mike@altlinux.org> 5.1.2-alt3
- fixed build (libXext-devel)

* Mon Nov 10 2008 Michael Shigorin <mike@altlinux.org> 5.1.2-alt2
- rebuilt against current libXaw-devel (added to BR too)

* Sat May 10 2008 Michael Shigorin <mike@altlinux.org> 5.1.2-alt1
- 5.1.2
- updated patch2, patch3, patch4
- disabled patches1, patch5 (fixed upstream)
- removed old autoconf requirement (fixed upstream)
- updated Packager:
- added Url:
- buildreq
- spec cleanup

* Wed Sep 26 2007 Michael Shigorin <mike@altlinux.org> 5.1.1-alt1
- 5.1.1 (still needs a separate patch for the issue fixed
  in 5.0.2-alt1.1)

* Wed Sep 26 2007 Michael Shigorin <mike@altlinux.org> 5.0.2-alt1.1
- applied Debian patch to fix CVE-2007-4033
- spec macro abuse cleanup

* Mon Apr 12 2004 Dmitry V. Levin <ldv@altlinux.org> 5.0.2-alt1
- Updated to 5.0.2, rediffed patches.
- Fixed library linkage to avoid undefined symbols.
- Merged fixes from debian t1lib package.

* Thu Nov 27 2003 Alexey Tourbin <at@altlinux.ru> 5.0.0-alt2
- Do not package .la files.
- Do not package devel-static by default.

* Sat Oct 18 2003 Yury A. Zotov <yz@altlinux.ru> 5.0.0-alt1
- 5.0.0
- t1lib-config.patch updated
- install encodings in /usr/share/t1lib/enc
- added CP1251.enc, KOI8-R.enc, KOI8-U.enc

* Mon Oct 06 2003 Yury A. Zotov <yz@altlinux.ru> 1.3.1-alt3
- BuildRequires updated for Sisyphus 20031005
- BuildReReq: autoconf_2.13
- build with hasher

* Sun Oct 13 2002 Yury A. Zotov <yz@altlinux.ru> 1.3.1-alt2
- build with gcc3.2
- new BuildRequires

* Fri Jun 14 2002 Yury A. Zotov <yz@altlinux.ru> 1.3.1-alt1
- new version

* Mon Oct 29 2001 AEN <aen@logic.ru> 1.3-alt1
- new verson 

* Mon Sep 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.2-alt1
- 1.2
- Moved configuration to %_sysconfdir/%name (FHS).
- Moved static libraries to devel-static subpackage.
- Moved utilities to utils subpackage.
- Corrected interpackage requires.
- Repackage documentation.

* Wed Oct 18 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.1-ipl1mdk
- FHSification.

* Wed Apr  5 2000 Dmitry V. Levin <ldv@fandra.org>
- RE adaptions.

* Thu Mar 23 2000 Daouda Lo <daouda@mandrakesoft.com> 0.9.2-3mdk
- fix group.

* Thu Jan 13 2000 Pixel <pixel@mandrakesoft.com>
- libtoolize --force.

* Sat Oct 30 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- updated to version 0.9.2.

* Thu Aug 12 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- added PostScript documentation.
- split into main and devel package.

* Sun Aug 1 1999 Richard D. Jackson <richardj@1gig.net>
- first release of t1lib-0.9.1
