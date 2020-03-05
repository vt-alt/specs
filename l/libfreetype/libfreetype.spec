%def_disable static

Name: libfreetype
Version: 2.10.1
Release: alt1
Summary: A free and portable font rendering engine
License: FTL or GPLv2+
Group: System/Libraries
Url: http://www.freetype.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

PreReq: libharfbuzz
Provides: freetype2 = %version
Obsoletes: freetype2 < %version

Source0: http://download.savannah.gnu.org/releases/freetype/freetype-%version.tar.xz
Source2: http://download.savannah.gnu.org/releases/freetype/freetype-doc-%version.tar.xz
Source1: http://download.savannah.gnu.org/releases/freetype/ft2demos-%version.tar.xz
Source3: ftconfig.h

Patch3: freetype-2.4.10-alt-fttrigon.patch
Patch6: ft2demos-2.6.2-alt-snprintf.patch
Patch11: freetype-2.10.0-enable-subpixel-rendering.patch
Patch12: freetype-2.10.0-enable-valid.patch
Patch13: ft2demos-2.4.10-rh-more-demos.patch
Patch14: freetype-2.10.0-alt-e2k.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: bzlib-devel libX11-devel libharfbuzz-devel libpng-devel zlib-devel

%description
The FreeType engine is a free and portable TrueType font rendering
engine, developed to provide TrueType support for a variety of
platforms and environments.  FreeType is a library which can open
and manages font files as well as efficiently load, hint and render
individual glyphs.  FreeType is not a font server or a complete
text-rendering library.

%package devel
Summary: Header files and library for development with FreeType2
Group: Development/C
Requires: %name = %version-%release
# harfbuzz is required in pkg-config file
Requires: libharfbuzz-devel
Provides: freetype2-devel = %version
Obsoletes: freetype2-devel < %version

%description devel
This package contains the header files and development libraries needed
to develop programs that use the FreeType2 library.

%package devel-static
Summary: The FreeType2 static library
Group: Development/C
Requires: %name-devel = %version-%release
Provides: freetype2-devel-static = %version
Obsoletes: freetype2-devel-static < %version

%description devel-static
This package contains the FreeType2 static library.

%package demos
Summary: A collection of FreeType demonstration programs
Group: Development/C
Requires: %name = %version-%release
Provides: freetype2-demos = %version
Obsoletes: freetype2-demos < %version
Conflicts: freetype

%description demos
The FreeType engine is a free and portable TrueType font rendering
engine, developed to provide TrueType support for a variety of
platforms and environments.  FreeType is a library which can open
and manages font files as well as efficiently load, hint and render
individual glyphs.  FreeType is not a font server or a complete
text-rendering library.

This package contains collection of FreeType demonstration programs.

%prep
%setup -n freetype-%version -a1 -b2
ln -s ft2demos-%version ft2demos

%patch3 -p1
%patch6 -p1

%patch11 -p1
%patch12 -p1
%patch13 -p0

%ifarch %e2k
# lcc 1.23.12 lacks vector_shuffle gcc extension
%patch14 -p1 -b .alt-e2k
%endif

%build
%add_optflags -fno-strict-aliasing %(getconf LFS_CFLAGS)
%configure \
	--enable-freetype-config \
	%{subst_enable static}

# get rid of RPATH
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' builds/unix/libtool

%make_build
%make_build -C ft2demos-%version TOP_DIR=..

%install
%make DESTDIR=%buildroot install

for f in ft2demos-%version/bin/.libs/ft*; do
	install -pD -m755 $f %buildroot%_bindir/${f##*/}
done

wordsize=$(echo $(echo -e '#include <bits/wordsize.h>\n__WORDSIZE' | cpp -P))
[ "$wordsize" -ge 32 ]
mv %buildroot%_includedir/freetype2/freetype/config/ftconfig{,-$wordsize}.h
install -pm644 %_sourcedir/ftconfig.h \
	%buildroot%_includedir/freetype2/freetype/config/ftconfig.h

%define docdir %_docdir/%name-%version
%define develdocdir %_docdir/%name-devel-%version
mkdir -p %buildroot%docdir
mkdir -p %buildroot%develdocdir
cp -a docs/* %buildroot%develdocdir/
pushd %buildroot%develdocdir
	bzip2 -9 CHANGES raster.txt
	rm INSTALL* release
popd
mv %buildroot%develdocdir/{FTL.TXT,LICENSE.TXT,CHANGES.bz2} %buildroot%docdir/

%set_verify_elf_method strict

#triggerin devel -- %name-devel < 2.6.2-alt2
%pre devel
[ ! -L %_includedir/freetype2/freetype ] || \
	rm -f %_includedir/freetype2/freetype

%files
%docdir
%_libdir/*.so.*

%files devel
%develdocdir
%_bindir/*-config
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_datadir/aclocal/*.m4

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%files demos
%_bindir/ft*

%changelog
* Wed Sep 11 2019 Valery Inozemtsev <shrek@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Sun Apr 07 2019 Michael Shigorin <mike@altlinux.org> 2.10.0-alt2
- E2K: fix build (lcc lacks vector_shuffle extension), adjust wordsize test

* Mon Mar 18 2019 Valery Inozemtsev <shrek@altlinux.ru> 2.10.0-alt1
- 2.10.0 (closes: #36288)

* Thu May 03 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.9.1-alt1.S1
- 2.9.1

* Mon Jan 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.9-alt1.S1
- 2.9

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8-alt4
- Updated runtime dependencies of devel package.

* Wed Sep 13 2017 Dmitry V. Levin <ldv@altlinux.org> 2.8-alt3
- Added export of FT_Done_GlyphSlot symbol for libInventor.

* Wed Sep 13 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.8-alt2
- Reenabled upstream list of global symbols exported by the library.
- Added export of FT_Stream_Pos and FT_Stream_Seek symbols for NX.

* Tue Sep 12 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.8-alt0.M80P.1
- backport to p8 branch

* Wed May 31 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.8-alt1
- 2.8

* Wed Jan 11 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Sun Sep 18 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7-alt1
- 2.7

* Wed Jul 13 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.5-alt1
- 2.6.5

* Sat Feb 20 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Thu Jan 14 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.2-alt2
- fixed ftconfig.h

* Tue Jan 12 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Sun Nov 01 2015 Valery Inozemtsev <shrek@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Wed Jun 10 2015 Valery Inozemtsev <shrek@altlinux.ru> 2.6-alt1
- 2.6

* Thu Jan 08 2015 Valery Inozemtsev <shrek@altlinux.ru> 2.5.5-alt1
- 2.5.5

* Sun Dec 07 2014 Valery Inozemtsev <shrek@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Wed Mar 12 2014 Valery Inozemtsev <shrek@altlinux.ru> 2.5.3-alt2
- prereq libharfbuzz

* Tue Mar 11 2014 Valery Inozemtsev <shrek@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Fri Dec 20 2013 Valery Inozemtsev <shrek@altlinux.ru> 2.5.2-alt3
- %name-devel: real fixed problem upgrading

* Wed Dec 11 2013 Valery Inozemtsev <shrek@altlinux.ru> 2.5.2-alt2
- %name-devel: Fixed problem upgrading from 2.5.2 less (closes: #29648)

* Mon Dec 09 2013 Valery Inozemtsev <shrek@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Thu Dec 05 2013 Valery Inozemtsev <shrek@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Fri Aug 30 2013 Valery Inozemtsev <shrek@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Wed Aug 07 2013 Dmitry V. Levin <ldv@altlinux.org> 2.4.12-alt2
- Backported fixes from FC.

* Mon May 13 2013 Valery Inozemtsev <shrek@altlinux.ru> 2.4.12-alt1
- 2.4.12

* Tue Mar 19 2013 Fr. Br. George <george@altlinux.ru> 2.4.11-alt1.1
- Fix i586 FILE64 build

* Fri Dec 21 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.4.11-alt1
- 2.4.11

* Mon Oct 08 2012 Dmitry V. Levin <ldv@altlinux.org> 2.4.10-alt2
- Fixed freetype-config script to use pkg-config (closes: #27761).
- Fixed multilib issues.
- Fixed fttrigon.h
- Packaged more demos.
- Applied demos fixes from Debian.
- Dropped rh-bitmap-foundry.patch.
- Rediffed patches, cleaned up specfile.
- Disabled build and packaging of static library.

* Wed Jul 18 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.4.10-alt1
- 2.4.10

* Sun Apr 01 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.4.9-alt1
- 2.4.9

* Sat Dec 10 2011 Dmitry V. Levin <ldv@altlinux.org> 2.4.8-alt2
- Fixed RPATH issue (closes: #26693).

* Wed Nov 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.4.8-alt1
- 2.4.8

* Sun Oct 23 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.4.7-alt1
- 2.4.7

* Fri Aug 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.4.6-alt1
- 2.4.6

* Sun Jun 26 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.4.5-alt1
- 2.4.5

* Wed Mar 02 2011 Alexey Tourbin <at@altlinux.ru> 2.4.4-alt4
- disabled dependency on zlib-devel

* Tue Feb 08 2011 Alexey Tourbin <at@altlinux.ru> 2.4.4-alt3
- added ld script to mitigate symbol versioning issues

* Tue Feb 08 2011 Alexey Tourbin <at@altlinux.ru> 2.4.4-alt2
- rebuilt for debuginfo
- disabled symbol versioning

* Wed Dec 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.4.4-alt1
- added some upstream patches

* Mon Oct 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.4.3-alt2
- added some upstream patches

* Fri Oct 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Thu Aug 19 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Sat Aug 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.4.1-alt2
- fixed CVE-2010-2805, CVE-2010-2806, CVE-2010-2807, CVE-2010-2808

* Fri Jul 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Mon Feb 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.3.12-alt1
- 2.3.12

* Sat Oct 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.3.11-alt2
- fixed pcf font names (closes: #21972)

* Sun Oct 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.3.11-alt1
- 2.3.11 (closes: #21909)

* Fri Oct 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.3.10-alt1
- 2.3.10

* Wed Apr 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.3.9-alt2
- fixed CVE-2009-0946

* Mon Mar 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.3.9-alt1
- 2.3.9

* Mon Jan 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.3.8-alt1
- 2.3.8

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.3.7-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Jul 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.3.7-alt1
- 2.3.7

* Wed Jun 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.3.6-alt1
- 2.3.6

* Tue Feb 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.3.5-alt2.1
- don't use logical OR to concatenate error codes

* Sun Jul 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.5-alt2
- fixed version script

* Sat Jul 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.5-alt1
- 2.3.5

* Fri May 18 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.4-alt2
- fixed CVE-2007-2754

* Tue Apr 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Fri Apr 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.3-alt2
- added freetype-2.3.3-cvs-ftbitmap.patch: fix buffer-overwrite bug

* Thu Apr 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.3-alt1
- 2.3.3:
  + fixed CVE-2007-1351

* Wed Mar 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.2-alt2
- added freetype-2.3.2-cvs-bdflib.patch: fixed potential buffer overflow in dbflib

* Sat Mar 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Wed Jan 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.1-alt1
- 2.3.1
- drop upstream patches

* Tue Jan 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.0-alt3
- returned freetype-2.2.1-memcpy-fix.patch
- added freetype-2.3.0-cvs-limit-check.patch,
	freetype-2.3.0-cvs-SHZ.patch

* Thu Jan 18 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.0-alt2
- enable subpixel rendering

* Wed Jan 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.0-alt1
- 2.3.0
- introduced FREETYPE_2.3.0 ABI for new functions in libfreetype.so.6

* Sat Jan 13 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt9
- fixed %%docdir
- install documentations
- drop 	freetype-2.2.1-suse-bugzilla-159166-reduce-embolden-distance.patch
- merge patches from RH:
  + freetype-2.2.1-enable-valid.patch
  + freetype-composite.patch
  + freetype-more-composite.patch

* Wed Dec 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt8
- fixed error code on rendering a space character (#10414)

* Tue Dec 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt7
- merge patches from RH:
  + freetype-2.2.1-ttcmap.patch
  + freetype-2.2.1-memcpy-fix.patch

* Fri Jul 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt6
- merge patches from SuSE

* Sat Jul 15 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt5
- removed freetype2-bitmap-foundry.patch

* Wed Jun 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt4
- updated freetype-2.2.1-cvs-memleak.patch

* Wed May 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt3
- fixed #9647, #9648

* Sun May 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt2
- added freetype-2.2.1-cvs-memleak.patch

* Thu May 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt1
- 2.2.1
- added freetype-2.2.1-cvs-perfloadgluph.patch

* Mon Apr 24 2006 Alexey Tourbin <at@altlinux.ru> 2.1.10-alt4
- NMU: introduced FREETYPE_2.1.10 ABI for new functions in libfreetype.so.6;
  also restricted the list of symbols exported by the library

* Sun Apr 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.10-alt3
- merge patches from SuSE

* Fri Mar 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.10-alt2
- renamed to libfreetype
- fixed #8923, #8869
- updated build dependencies

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.1.10-alt1.1
- Rebuilt for new pkg-config dependencies.

* Wed Nov 09 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.1.10-alt1
- merge patches from RedHat

* Mon Oct 03 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.1.10-alt0.1
- 2.1.10

* Wed Jun 22 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.1.9-alt4
- merge patches from SuSE

* Fri Mar 18 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.1.9-alt3
- enable static

* Wed Oct 27 2004 Dmitry V. Levin <ldv@altlinux.org> 2.1.9-alt2
- Fixed build dependencies.
- Packaged translations.
- Build ft2demos.
- Moved documentation for developers to -devel subpackage.

* Wed Oct 20 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.1.9-alt1
- Updated to 2.1.9.

* Tue Dec 02 2003 Dmitry V. Levin <ldv@altlinux.org> 2.1.4-alt3
- Fix crash with non-format-0 hdmx tables (RH).
- Do not build static library by default.
- Do not package .la files.
- Specfile cleanup.

* Tue Jun 03 2003 AEN <aen@altlinux.ru> 2.1.4-alt2
- some internal headers added for pfaedit

* Sat Apr 12 2003 AEN <aen@altlinux.ru> 2.1.4-alt1
- new version
- patches 1,2 obsoletes now

* Tue Mar 11 2003 AEN <aen@altlinux.ru> 2.1.3-alt2
- enable bytecode interpreter

* Fri Feb 28 2003 AEN <aen@altlinux.ru> 2.1.3-alt1
- new verson
- patches from RH

* Mon Sep 02 2002 AEN <aen@altlinux.ru> 2.1.2-alt2
- patches from Rawhide (2.1.2-9) for hinting quality added

* Wed Jun 26 2002 AEN <aen@logic.ru> 2.1.2-alt1
- new version

* Tue Jun 17 2002 AEN <aen@logic.ru> 2.1.1-alt1
- new version
- patch regenerated

* Thu Mar 28 2002 AEN <aen@logic.ru> 2.0.9-alt1
- new version

* Fri Jan 18 2002 AEN <aen@logic.ru> 2.0.6-alt1
- new version

* Mon Oct 29 2001 AEN <aen@logic.ru> 2.0.5-alt1
- new version

* Wed Jul 4 2001 AEN <aen@logic.ru> 2.0.4-alt1
- new version

* Thu Jun 21 2001 AEN <aen@logic.ru> 2.0.3-alt3
- ttf hinting enabled

* Mon Jun 18 2001 AEN <aen@logic.ru> 2.0.3-alt2
- requirements fixed (thnx to Aleksey Voinov)

* Thu May 31 2001 AEN <aen@logic.ru> 2.0.3-alt1
- 2.0.3

* Wed Apr 4 2001 AEN <aen@logic.ru> 2.0.2-ipl1mdk
- 2.0.2 final

* Mon Dec 18 2000 AEN <aen@logic.ru>
- new snapshot for building XFree86-4.0.2

* Mon Nov 28 2000 AEN <aen@logic.ru>
- build for RE

* Tue Nov 21 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0-3mdk
- Include all modules in lib (no longer apply patch1)

* Tue Nov 21 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0-2mdk
- Add config script to devel package
- correctly configure package

* Fri Nov 10 2000 Geoffrey Lee <snailtalk@manrakesoft.com> 2.0-1mdk
- really 2.0 release.

* Wed Nov  8 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0-0.8.1mdk
- First mandrake release

* Thu Oct  5 2000 Ramiro Estrugo <ramiro@eazel.com>
- Created this thing

