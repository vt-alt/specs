Name: scribus
Version: 1.5.5
Release: alt9.c2aae6886
Epoch: 1

Summary: DeskTop Publishing application written in Qt

Group: Publishing
License: GPLv2+
Url: http://www.scribus.net/

Packager: Paul Wolneykien <manowar@altlinux.ru>

# Source-url: https://github.com/scribusproject/scribus/archive/master.zip
Source: %name-%version.tar

BuildRequires: cmake zlib-devel libssl-devel
BuildRequires: libpoppler-devel libpoppler-cpp-devel
BuildRequires: qt5-imageformats qt5-declarative-devel qt5-tools-devel

# Required from BUILDING file
BuildRequires: qt5-base-devel >= 5.5.0
BuildRequires: libfreetype-devel >= 2.1.7
BuildRequires: libcairo-devel >= 1.14.0
BuildRequires: libtiff-devel >= 3.6.0
BuildRequires: liblcms2-devel >= 2.1
BuildRequires: libjpeg-devel
BuildRequires: libharfbuzz-devel >= 0.9.42
BuildRequires: libicu-devel

# Recommended from BUILDING file
BuildRequires: libcups-devel
BuildRequires: fontconfig-devel >= 2.0
BuildRequires: libxml2-devel >= 2.6.0
BuildRequires: ghostscript > 9.0
BuildRequires: libhunspell-devel
BuildRequires: libpodofo-devel >= 0.9.6
# boost used only for 2geom
BuildRequires: boost-devel-headers
BuildRequires: GraphicsMagick
BuildRequires: libGraphicsMagick-c++-devel

BuildRequires: rpm-build-python3 python3-dev
BuildRequires: python3-module-Pillow

# TODO: build with OSG

# TODO: use system libs instead third_party
#BuildPreReq: libhyphen-devel lib2geom-devel

# For import filters
BuildRequires: libfreehand-devel libpagemaker-devel libmspub-devel libcdr-devel 
BuildRequires: libwmf-devel libvisio-devel libqxp-devel libzmf-devel

Requires: %name-doc >= %epoch:%version
Requires: %name-data >= %epoch:%version
Requires: aspell-en

%add_verify_elf_skiplist %_libdir/%name/plugins/*.so
%add_findreq_skiplist %_datadir/%name/samples/*
%add_findreq_skiplist %_datadir/%name/scripts/*

%description
Scribus is an desktop open source page layout program with
the aim of producing commercial grade output in PDF and
Postscript, primarily, though not exclusively for Linux.

While the goals of the program are for ease of use and simple easy to
understand tools, Scribus offers support for professional publishing
features, such as CMYK color, easy PDF creation, Encapsulated Postscript
import/export and creation of color separations.

%if 0
%package devel
Summary: Header files for Scribus
Group: Development/C++
BuildArch: noarch
Requires: %name = %epoch:%version-%release

%description devel
Header files for Scribus.
%endif

%package data
Summary: Data files of Scribus
Group: Publishing
BuildArch: noarch
Conflicts: %name < %epoch:%version

%description data
Data files of Scribus.

%package doc
Summary: Documentation files for Scribus
Group: Development/Tools
Conflicts: %name < %epoch:%version
BuildArch: noarch

%description doc
%summary

%prep
%setup

%ifarch %e2k
# until lcc-1.24: strip UTF-8 BOM
find -name '*.cpp' -o -name '*.h' | xargs sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%cmake \
%ifarch x86_64
	-DWANT_LIB64=true \
%endif
	-DWANT_NORPATH=true \
	-DWANT_DISTROBUILD=true \
	-DWANT_CCACHE=true \
	-DWANT_GRAPHICSMAGICK=true \
	-DFONTCONFIG_CONFIG:FILEPATH=%_pkgconfigdir/fontconfig.pc \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags"

%cmake_build VERBOSE=1

%install
%cmakeinstall_std

pushd %buildroot%_docdir/%name
for i in $(ls ChangeLog*); do
	bzip2 $i
done
popd

%files
%dir %_docdir/%name
%doc %_docdir/%name/AUTHORS
%doc %_docdir/%name/ChangeLog*
%doc %_docdir/%name/COPYING
%doc %_docdir/%name/README
#%doc %_docdir/%name/TODO
%_bindir/%name
%_desktopdir/scribus.desktop
%_datadir/metainfo/scribus.appdata.xml
%_datadir/mime/packages/scribus.xml
%_iconsdir/hicolor/*/apps/scribus.png
%_libdir/%name/
%attr(0755,root,root) %_libdir/%name/plugins/*.so
%_man1dir/*
%exclude %_mandir/de
%exclude %_mandir/pl

%files data
%_datadir/%name

#%files devel
#%doc AUTHORS COPYING
#%_includedir/%name

%files doc
%dir %_docdir/%name
#%_docdir/%name/BUILDING
#%_docdir/%name/NEWS
#%_docdir/%name/PACKAGING
%_docdir/%name/LINKS
%_docdir/%name/TRANSLATION
%_docdir/%name/en
%exclude %_docdir/%name/de
%exclude %_docdir/%name/it

%changelog
* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 1:1.5.5-alt9.c2aae6886
- update to c2aae688620fa3e75781b2ca4502408d22c1d343 fix build with poppler 0.84)
- switch to python3

* Thu Jan 02 2020 Paul Wolneykien <manowar@altlinux.org> 1:1.5.5-alt8.c29f478ab
- Fixed execute permission for *.so plugins (closes: 36962).

* Fri Sep 20 2019 Vitaly Lipatov <lav@altlinux.ru> 1:1.5.5-alt7.c29f478ab
- update to c29f478abf03dc5ac0fd9cd21d0feb589a91d7eb

* Mon Jul 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1:1.5.5-alt6
- fix build with poppler 0.76

* Thu Apr 18 2019 Vitaly Lipatov <lav@altlinux.ru> 1:1.5.5-alt5
- update to fa2519c93ed0d04bde0e41146849cc808f880ef6
- drop old patches

* Tue Apr 16 2019 Michael Shigorin <mike@altlinux.org> 1:1.5.5-alt4
- fix build on e2k: strip UTF-8 BOM

* Thu Apr 11 2019 Vitaly Lipatov <lav@altlinux.ru> 1:1.5.5-alt3
- fix build with poppler 0.75.0

* Sun Feb 17 2019 Vitaly Lipatov <lav@altlinux.ru> 1:1.5.5-alt2
- fix build with poppler 0.74.0 (ALT bug 36087)

* Fri Nov 30 2018 Vitaly Lipatov <lav@altlinux.ru> 1:1.5.5-alt1
- build 1.5.5.svn (head) (ALT bug 35677)

* Thu Aug 30 2018 Vitaly Lipatov <lav@altlinux.ru> 1:1.5.4-alt3
- rebuild with podofo 0.9.6
- fix build with poppler 0.64.0

* Sat Jul 07 2018 Vitaly Lipatov <lav@altlinux.ru> 1:1.5.4-alt2
- cleanup spec, fix build

* Thu May 17 2018 Vitaly Lipatov <lav@altlinux.ru> 1:1.5.4-alt1
- new version 1.5.4 (with rpmrb script)
- rebuild with libicu60

* Mon Nov 06 2017 Vitaly Lipatov <lav@altlinux.ru> 1:1.5.3-alt2
- rebuild with new poppler 0.60
- build with libfreehand, libpagemaker, libmspub

* Wed Aug 30 2017 Vitaly Lipatov <lav@altlinux.ru> 1:1.5.3-alt1
- new version (1.5.3) with rpmgs script

* Wed May 10 2017 Vitaly Lipatov <lav@altlinux.ru> 1:1.4.6-alt1
- new version 1.4.6 (with rpmrb script)
- rebuild with new libpodofo 0.9.5

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1:1.4.5-alt3
- rebuild with new libpodofo 0.9.4

* Sun Aug 23 2015 Vitaly Lipatov <lav@altlinux.ru> 1:1.4.5-alt2
- rebuild with new libpodofo 0.9.3
- drop patching _datadir/CMake/Modules/FindFreetype.cmake

* Mon Mar 02 2015 Paul Wolneykien <manowar@altlinux.org> 1:1.4.5-alt1
- Freshed up to v1.4.5 with the help of cronbuild and update-source-functions.

* Wed May 28 2014 Cronbuild Service <cronbuild@altlinux.org> 1:1.4.4-alt1
- Fresh up to v1.4.4 with the help of cronbuild and update-source-functions.

* Thu Apr 03 2014 Paul Wolneykien <manowar@altlinux.org> 1:1.4.3-alt2
- Rebuild with lcms2.

* Tue Dec 10 2013 Paul Wolneykien <manowar@altlinux.ru> 1:1.4.3-alt1
- Fresh up to v1.4.3 with the help of cronbuild and update-source-functions.

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 1:1.4.1-alt5
- rebuild with new libpodofo 0.9.1

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.4.1-alt4.1
- Rebuilt with libpng15

* Wed Jun 13 2012 Vitaly Lipatov <lav@altlinux.ru> 1:1.4.1-alt4
- rebuild with new libpodofo

* Fri May 18 2012 Paul Wolneykien <manowar@altlinux.ru> 1:1.4.1-alt3
- Fix the aspell-based spell-checking plugin.

* Thu May 17 2012 Paul Wolneykien <manowar@altlinux.ru> 1:1.4.1-alt2
- Use `mkdir -p` -- helps `rpmbuild --short-circuit`.
- Fix libdir and plugindir paths.
- Enable spell-checking plugins.

* Wed May 16 2012 Paul Wolneykien <manowar@altlinux.ru> 1:1.4.1-alt1
- Cronbuild: adapt to the top directory name modifications.
- Update the sources with the help of cronbuild scripts.

* Thu Feb 09 2012 Paul Wolneykien <manowar@altlinux.ru> 1:1.4.0-alt4
- Build the next version with the help of the packaged cronbuild scripts.
- Use upstream version of patched util_math.* (related with the EPSF problem).

* Tue Feb 07 2012 Paul Wolneykien <manowar@altlinux.ru> 1:1.4.0-alt3.rc6
- Build the next version with the help of the packaged cronbuild scripts.

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.4.0-alt2.rc5.2
- Fixed RPATH

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.4.0-alt2.rc5.1
- Rebuild with Python-2.7

* Tue Nov 01 2011 Paul Wolneykien <manowar@altlinux.ru> 1:1.4.0-alt2.rc5
- Fix the reading of the PS part size and length from an EPSF.

* Sat Aug 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.4.0-alt1.rc5
- Version 1.4.0.rc5

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.4.0-alt1.rc4
- Version 1.4.0.rc4

* Fri Apr 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.4.0-alt1.rc3
- Version 1.4.0.rc3

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.9-alt2
- Rebuilt for debuginfo
- Removed circular dependencies

* Fri Jan 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.9-alt1
- Version 1.3.9

* Tue Nov 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.8-alt4
- Rebuilt for soname set-versions

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.8-alt3
- Fixed underlinking

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.8-alt2
- Compressed ChangeLogs

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.8-alt1
- Version 1.3.8

* Fri Feb 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.5.1-alt6
- Linking libodtimplugin.so with libxml2 (ALT #22946)

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.5.1-alt5
- Rebuild with python 2.6
- Added russian translation into desktop file (ALT #21474)

* Sat Nov 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.5.1-alt4
- Fixed big-changelog, iconsdir, freedesktop-desktop,
  docdir-is-not-owned, arch-dep-package-has-big-usr-share repocop
  warnings

* Thu Nov 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.5.1-alt3
- Updated russian translation (ALT #21475), thnx Alexandre Prokoudine

* Wed Sep 02 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.3.5.1-alt2
- fix rpath for plugins (ALT #21346)
- fix localization (ALT #21365)

* Tue Aug 25 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.3.5.1-alt1
- Resurrect build, spec from FC12

* Sun Jan 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.4-alt6
- fixed odf plugin link (close #18490)

* Fri Mar 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.4-alt5
- added libgnutls-devel in BuildRequires. see #14778

* Wed Feb 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.4-alt4.1
- rebuild with python-2.5

* Thu Jan 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.4-alt3.M40.1
- build for branch 4.0

* Mon Jan 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.4-alt4
- drop ICC profiles, requires icc-profiles package
- build with cairo
- updated build dependencies

* Thu Jan 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.4-alt3
- build with system libhyphen

* Sat Dec 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.4-alt2
- use system hyphenation rules

* Thu Dec 13 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.4-alt0.M40.1
- build for branch 4.0

* Thu Dec 13 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.4-alt1
- 1.3.4

* Sun Jul 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.3.9-alt3
- rebuild for sisyphus

* Sun Jul 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.3.9-alt2.M40
- 1.3.3.9 stable release for branch 4.0

* Wed May 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.3.4-alt1
- 1.3.4

* Tue May 08 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.3.4-alt0.1cvs
- 1.3.4cvs

* Tue  May 08 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3.9-alt2
- update Tango icons

* Sun May 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3.9-alt1
- 1.3.3.9
- added Tango icons by default

* Wed Feb 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3.8-alt1
- 1.3.3.8

* Sat Feb 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3.7-alt2
- fixed build with python for x86_64

* Wed Jan 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3.7-alt1
- 1.3.3.7

* Mon Dec 04 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3.6-alt2
- fixed plugin files attributes

* Mon Dec 04 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3.6-alt1
- 1.3.3.6

* Sat Nov 11 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3.5-alt1
- 1.3.3.5

* Thu Oct 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3.4-alt1
- 1.3.3.4

* Tue Aug 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3.3-alt1
- 1.3.3.3

* Wed May 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3.2-alt2
- fixed build for x86_64

* Wed May 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3.2-alt1
- 1.3.3.2

* Mon Apr 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3.1-alt1
- 1.3.3.1

* Tue Mar 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3-alt1
- 1.3.3

* Fri Mar 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Tue Oct 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.3.1-alt0.1
- 1.3.1

* Sat Jul 16 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt0.1
- 1.3.0

* Wed Apr 06 2005 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.2.2-alt1.cvs20050405
- 1.2.2.cvs20050405

* Tue Mar 29 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.1-alt1.1.1
- Rebuilt with python-2.4.

* Wed Jan 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.1-alt1.1
- Rebuilt with libstdc++.so.6.

* Mon Jan 10 2005 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Thu Dec 16 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.2-alt1.2
- fix buildrequires

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.2-alt1.1
- Rebuilt with libtiff.so.4.

* Sun Sep 05 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.2-alt1
- 1.2 "aKademy Edition"
- Add additional templates for Scribus

* Wed Jun 23 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.1.7-alt2
- fix buildrequires and requires

* Wed Jun 09 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.1.7-alt1
- 1.1.7
- new russian translation from Alexandre Prokoudine <avp@altlinux.ru>

* Thu Jun 03 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.1.6-alt3
- fix buildrequires

* Tue Apr 13 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.1.6-alt2
- new russian translation from Alexandre Prokoudine <avp@altlinux.ru>

* Mon Mar 29 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Wed Feb 18 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Mon Dec 29 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.1.4-alt2
- rebuildind in new compiler

* Mon Dec 29 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Sun Dec 14 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.1.3-alt2
- rebuildind without *.la

* Mon Dec 08 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Thu Nov 13 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.1.2-alt1
- 1.1.2 and new buildrequires

* Thu Oct 16 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.1.1-alt1
- 1.1.1 and new script plugin 0.5.2

* Sun Sep 14 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.1.0-alt1
- 1.1.0 and new script plugin 0.5.1

* Wed Aug 27 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.0.1-alt2
- new russian translation from Alexandre Prokoudine <avp@altlinux.ru>

* Sun Aug 10 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.0.1-alt1
- 1.0.1
- russian translation from Alexandre Prokoudine <avp@altlinux.ru>

* Wed Jul 23 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.0-alt1
- 1.0 final
- added samples and new html and pdf help documents
- added new script plugin

* Wed Jul 16 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.0-alt1.RC1
- 1.0.RC1

* Sun Jun 22 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.9.11.1-alt1
- 0.9.11.1

* Mon Jun 16 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.9.11-alt1
- 0.9.11

* Wed May 21 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.9.10-alt1
- 0.9.10

* Thu May 01 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.9.9-alt1
- 0.9.9

* Mon Apr 14 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Wed Feb 19 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Thu Jan 23 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.9.6-alt2
- new requires and buildrequires
- remove plugins

* Wed Jan 15 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Sun Dec 22 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Wed Nov 27 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Thu Nov 14 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.9.1-alt1
- 0.9.1
- Script Plugin added

* Sun Oct 13 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.8-alt1
- 0.8

* Tue Sep 17 2002 Sergey V Turchin <zerg@altlinux.ru> 0.7.8-alt1
- new version
- build with gcc3.2

* Tue Aug 27 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.7.7-alt1 for AltLinux
- 0.7.7

* Tue Jul 02 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.7.5-alt1 for AltLinux
- 0.7.5

* Fri Jan 04 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.5-alt1 for AltLinux
- 0.5
- specfile cleanup
