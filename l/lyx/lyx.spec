Name: lyx
Version: 2.3.4.4
Release: alt2

Summary: LyX - a WYSIWYM word processor for the Desktop Environment.
# LGPL-2.1+: src/support/gzstream.* src/support/weighted_btree.h
License: GPL-2.0-or-later and LGPL-2.1-or-later
Group: Publishing
Epoch: 2
Url: http://www.lyx.org

Source: %name-%version.tar
Source1: %name.desktop
Source2: %{name}16.xpm
Source3: %{name}32.xpm
Source4: %{name}48.xpm
Source5: lyxcat

Patch2: lyx-2.1.2-xdg_open.patch
Patch3: 0004-Use-python3-internally-in-the-C-code-as-well.patch
Patch4: 0006-Fix-os.popen-for-Python-3.patch
Patch5: %name-%version-alt-boost-1.73.0-compat.patch

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++ imake libaspell-devel libSM-devel python3-devel bc
BuildRequires: libaiksaurus-devel boost-signals-devel boost-devel boost-filesystem-devel
BuildRequires: qt5-base-devel qt5-x11extras-devel qt5-svg-devel
BuildRequires: zlib-devel libenchant-devel libhunspell-devel libmythes-devel

Provides: lyx-common lyx-qt lyx-latex-beamer
Obsoletes: lyx-common lyx-qt lyx-latex-beamer

%description
LyX is a modern approach to writing documents which breaks with the
obsolete "typewriter paradigm" of most other document preparation
systems.

It is designed for people who want professional quality output
with a minimum of time and effort, without becoming specialists in
typesetting.

The major innovation in LyX is WYSIWYM (What You See Is What You Mean).
That is, the author focuses on content, not on the details of
formatting.
This allows for greater productivity, and leaves the final typesetting
to the backends (like LaTeX) that are specifically designed
for the task.

With LyX, the author can concentrate on the contents of his writing,
and let the computer take care of the rest.

%package -n lyx-tex
Summary: Virtual package that install required set of tex packages for LyX.
Group: Publishing
Requires: lyx
Requires: texlive-latex-recommended texlive-extra texlive-lang-cyrillic texlive-fonts-recommended fonts-ttf-latex-xft 
BuildArch: noarch

%description -n lyx-tex
Virtual package that install required set of tex packages for LyX.

%prep
%setup
find 3rdparty -not -type d -not -name Makefile.in -delete
find lib \( -name '*.py' -or -name '*.py.in' \) \
	-execdir sed -i '1i #!/usr/bin/python3' {} \+
sed -i 's|#! */usr/bin/env python|#!/usr/bin/env python3|' \
	lib/lyx2lyx/lyx2lyx \
	lib/scripts/listerrors \
	#
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p2

%build
%autoreconf
export PYTHON=python3
%configure \
	--without-included-boost \
	--with-enchant \
	--with-hunspell \
	--enable-qt5 \
	#

%make_build

%install
%makeinstall_std
%find_lang %name

# This one is optional and python2-only.
rm %buildroot%_datadir/%name/lyx2lyx/profiling.py

install -d -m 755 %buildroot%_desktopdir
install -m 644 %SOURCE1 %buildroot%_desktopdir/
install -d -m 755 %buildroot%_miconsdir
install -d -m 755 %buildroot%_niconsdir
install -d -m 755 %buildroot%_liconsdir
install -m 644 %SOURCE2 %buildroot%_miconsdir/%name.xpm
install -m 644 %SOURCE3 %buildroot%_niconsdir/%name.xpm
install -m 644 %SOURCE4 %buildroot%_liconsdir/%name.xpm
install -m 755 %SOURCE5 %buildroot%_bindir/

#
# Set up the lyx-specific class files where TeX can see then
#
TEXMF=%_datadir/texmf
mkdir -p %buildroot$TEXMF/tex/latex
cp -ar %buildroot%_datadir/%name/tex %buildroot$TEXMF/tex/latex/%name

desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Office:WordProcessor:KDE:Qt \
	--add-category=Office \
	--add-category=WordProcessor \
	--add-category=KDE \
	--add-category=Qt \
	%buildroot%_desktopdir/lyx.desktop

rm %buildroot%_datadir/icons/hicolor/scalable/apps/lyx.svg
rm %buildroot%_datadir/%name/scripts/prefTest.pl.in

%define _unpackaged_files_terminate_build 1

%post
# configure Lyx in new way
cd %_datadir/%name
python3 configure.py

%files -f %name.lang
%doc ANNOUNCE COPYING INSTALL* README* NEWS UPGRADING RELEASE-NOTES
%_bindir/*
%_man1dir/*
%_datadir/%name
%_datadir/texmf/tex/latex/lyx
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_desktopdir/*.desktop

%files -n lyx-tex

%changelog
* Thu Jun 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2:2.3.4.4-alt2
- Rebuilt with boost-1.73.0.

* Wed May 20 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 2:2.3.4.4-alt1
- Updated to 2.3.4.4.
- Switched to python3.

* Fri Aug 16 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2:2.3.3-alt1
- Updated to 2.3.3.

* Thu Mar 28 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2:2.3.2-alt1
- Fixed package version.

* Mon Mar 25 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2:2.3.1-alt1
- Updated to 2.3.2 (ALT#36303).
- Rebuilt with qt5 instead of qt4.
- Built with system libmythes.
- Removed R: texlive-latex-recommended from the main package (ALT#34631).

* Wed Oct 03 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:2.2.3-alt1.1.1
- rebuilt with hunspell-1.6.2

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2:2.2.3-alt1.1
- NMU: rebuilt with boost-1.67.0

* Fri May 26 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2:2.2.3-alt1
- Updated to 2.2.3.
- Built with enchant and hunspell instead of aspell (ALT#22053).

* Fri Oct 09 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2:2.1.4-alt1
- Updated to 2.1.4.

* Mon Feb 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.0.5.1-alt1.1
- Rebuilt with Boost 1.53.0

* Wed Jan 09 2013 Alex Karpov <karpov@altlinux.ru> 2:2.0.5.1-alt1
- new version

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.0.4-alt1.2
- Rebuilt with Boost 1.52.0

* Fri Sep 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.0.4-alt1.1
- Rebuilt with Boost 1.51.0

* Sun Sep 02 2012 Alex Karpov <karpov@altlinux.ru> 2:2.0.4-alt1
- new version

* Thu Apr 05 2012 Alex Karpov <karpov@altlinux.ru> 2:2.0.3-alt1.1
- rebuild with new boost

* Thu Mar 15 2012 Alex Karpov <karpov@altlinux.ru> 2:2.0.3-alt1
- new version

* Sun Jan 15 2012 Alex Karpov <karpov@altlinux.ru> 2:2.0.2-alt1
- new version

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.0.1-alt1.2
- Rebuilt with Boost 1.48.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2:2.0.1-alt1.1
- Rebuild with Python-2.7

* Mon Sep 05 2011 Alex Karpov <karpov@altlinux.ru> 2:2.0.1-alt1
- new version

* Wed Aug 24 2011 Alex Karpov <karpov@altlinux.ru> 2:2.0.0-alt2
- 2.0.0 release.

* Sat Jul 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:2.0.0-alt1.rc3.2.qa2
- Rebuilt with Boost 1.47.0

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2:2.0.0-alt1.rc3.2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for lyx

* Wed Apr 20 2011 Alex Karpov <karpov@altlinux.ru> 2:2.0.0-alt1.rc3.2
- added texlive-latex-recommended requirement (#25466)

* Mon Apr 18 2011 Alex Karpov <karpov@altlinux.ru> 2:2.0.0-alt1.rc3.1
- lyx-tex package now builds as noarch

* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 2:2.0.0-alt0.rc3.qa1
- NMU: dropped obsolete menu entry; added desktop categories

* Tue Apr 12 2011 Alex Karpov <karpov@altlinux.ru> 2:2.0.0-alt0.rc3
- new release candidate

* Sun Apr 03 2011 Alex Karpov <karpov@altlinux.ru> 2:2.0.0-alt0.rc2
- new release candidate

* Mon Mar 21 2011 Alex Karpov <karpov@altlinux.ru> 2:2.0.0-alt0.rc1
- new release candidate 
    + fixed typo in summary (thanks to mike@)

* Mon Mar 14 2011 Alex Karpov <karpov@altlinux.ru> 2:1.6.9-alt1.1
- rebuild with new boost

* Thu Feb 17 2011 Alex Karpov <karpov@altlinux.ru> 2:1.6.9-alt1
- new version

* Thu Dec 16 2010 Alexey Morsov <swi@altlinux.ru> 2:1.6.8-alt2
- rebuild with new boost

* Fri Nov 19 2010 Alexey Morsov <swi@altlinux.ru> 2:1.6.8-alt1
- new version

* Fri Oct 08 2010 Alexey Morsov <swi@altlinux.ru> 2:1.6.7-alt1
- new version

* Thu Jan 21 2010 Alexey Morsov <swi@altlinux.ru> 2:1.6.5-alt1
- new version
- fix spec (repocop, macros)

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:1.6.4.1-alt1.1
- Rebuilt with python 2.6

* Tue Sep 01 2009 Alexey Morsov <swi@altlinux.ru> 2:1.6.4.1-alt1
- new version

* Sat Apr 25 2009 Alexey Morsov <swi@altlinux.ru> 2:1.6.2-alt1
- new version
- now build with system boost

* Fri Nov 14 2008 Alexey Morsov <swi@altlinux.ru> 2:1.6.0-alt1
- new version

* Sat May 17 2008 Alexey Morsov <swi@altlinux.ru> 2:1.5.5-alt1
- new version
- fix desktop file to correspond with policy

* Wed Feb 27 2008 Alexey Morsov <swi@altlinux.ru> 2:1.5.4-alt1
- 1.5.4
- New Russian translation of the user interface.
- New example files that demonstrate how to create serial letters with
  the KOMA letter class.
- The on-screen appearance of spaces has been improved.
- New shortcut "C-M-n" to create numbered formulas.
- Character counting added to "Count Words" function
- New toolbar button to create boxes.
- Keyboard shortcuts for TOC window buttons were introduced.
- Improve cursor movement around lines with ending line-breaks.

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 2:1.5.3-alt1.1
- Rebuilt with python-2.5.

* Mon Dec 17 2007 Alexey Morsov <swi@altlinux.ru> 2:1.5.3-alt1
- 1.5.3
- Now collapsable insets (footnotes, comments etc) take the 
  whole screen width as soon as they contain more than one 
  row of text. Users of Mac/PPC and of Unices with slow 
  X11 server should feel a significant boost in performance 
  thanks to this change.
- The pixmap cache that was introduced in LyX 1.5.2 to 
  improve performance can now be switched on and off in
  Preferences
- It is now possible to enter greek and cyrillic characters and 
  have them typeset without switching to the proper language
- fix bug with lyx2lyx trouble in koi8r locale


* Tue Oct 30 2007 Alexey Morsov <swi@altlinux.ru> 2:1.5.2-alt4
- class latex-beamer now included in lyx (fix bug #13246)

* Mon Oct 22 2007 Alexey Morsov <swi@altlinux.ru> 2:1.5.2-alt3
- fix patch forming from git

* Fri Oct 19 2007 Alexey Morsov <swi@altlinux.ru> 2:1.5.2-alt2
- fix bug #11540 (lyx2lyx encoding failure)

* Fri Oct 12 2007 Alexey Morsov <swi@altlinux.ru> 2:1.5.2-alt1
- Add a pixmap cache to speed up text drawing on screen.
- Improved on screen rendering of some toolbar images.
- Fix performance problem related to Clipboard and Selection on X11
  platforms (bug 4045).
- many other bug/crash fixes.

* Mon Sep 24 2007 Alexey Morsov <swi@altlinux.ru> 2:1.5.1-alt2
- add update_menus

* Tue Aug 28 2007 Alexey Morsov <swi@altlinux.ru> 2:1.5.1-alt1
- version 1.5.1
- Fix output of LyX files on windows when Document>Compressed is set.
  This is a dataloss bug that was the main reason for releasing 1.5.1
	earlier than anticipated.
- Get rid of annoying LaTeX error after changing the document language.
- Fix crashes relating to command line export
- Fix crash with TOC and child documents
- Fix export to FAT32 under Linux
- Fix pasting a selection from the same LyX document with middle mouse
  button.
- many other bug fixes.

* Mon Jul 30 2007 Alexey Morsov <swi@altlinux.ru> 2:1.5.0-alt1
- release 1.5.0
- Lots of long-lasting bugs have been fixed, as documented in LyX
  bugzilla.

* Tue Jun 19 2007 Alexey Morsov <swi@altlinux.ru> 1:1.5.0-alt3.rc1
- fix crash on click Content in Tutorial (bug #12063)
- fix koi8-r for lyx2lyx (bug# 11540)

* Sat Jun 09 2007 Alexey Morsov <swi@altlinux.ru> 1:1.5.0-alt1.rc1
- new version 1.5.0-rc1

* Fri Jun 08 2007 Alexey Morsov <swi@altlinux.ru> 1.5.0-alt3.beta1
- add patch for qt4-4.3 (from lyx-devel)

* Wed Apr 18 2007 Alexey Morsov <swi@altlinux.ru> 1.5.0-alt2.beta1
- fix Provide, Obsoletes for correct replacing of lyx < 1.5

* Fri Apr 06 2007 Alexey Morsov <swi@altlinux.ru> 1.5.0-alt1.beta1
- new version (unicode support, new file format)

* Fri Apr 14 2006 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt0.1
- new version (1.4.1)
- Note: localization disabled, lyx-gost class is not yet supported
- dropped all additional feautures in ALT build
- dropped lyx-xforms (too obsolete)

* Fri Aug 26 2005 Vitaly Lipatov <lav@altlinux.ru> 1.3.6-alt0.2
- add patch for russian names

* Thu Aug 25 2005 Vitaly Lipatov <lav@altlinux.ru> 1.3.6-alt0.1
- new version
- fix python-strict requires (thanks ns@)
- set default tmp dir as $TMPDIR
- add dia files support

* Thu Mar 17 2005 Vitaly Lipatov <lav@altlinux.ru> 1.3.5-alt1
- rebuild with python 2.4

* Fri Jan 21 2005 Vitaly Lipatov <lav@altlinux.ru> 1.3.5-alt0.2
- new version
- build with gcc3.4 (and old libqt3)
- check hacks
- remove XFree86 requires
- fix gv argument

* Tue Sep 14 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt3
- add requires for instant preview of formulae (-preview, bc)
- build with aiksaurus (english thesaurus) support

* Fri Jun 18 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt2
- fix post/postun section with texhash
- add depend for latex-xft-fonts to lyx-qt
- add lyxcat script for preview lyx file in text mode
- move to Applications/Publishing menu

* Thu Feb 26 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt1
- new version
- change requires from python23 to python
- remove COPYING from doc
- if you want math mode symbols to show up properly (instead of red ERT text)
  see http://wiki.lyx.org/pmwiki.php/FAQ/Qt and try fix...
  or use xforms version

* Fri Jan 02 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt5
- move requires to tetex from lyx-common to lyx package
- fix language entry in ru_TOC.lyx
- add partially translated ru_UserGuide.lyx
- resave russian docs in LyX format 1.3
- build with gcc3.3

* Tue Nov 11 2003 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt4.1
- fix spec (my stupid bug with copying languages.template)

* Sat Nov 01 2003 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt4
- fix requires
- fix languages patch

* Thu Oct 30 2003 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt3.1
- fix spec

* Mon Oct 27 2003 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt3
- fix error in lib/languages filtering
- patch for fix russian filenames in graphics applied

* Thu Oct 09 2003 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt2.1
- fix spec for build in hasher
- remove libpspell dependences

* Sat Oct 04 2003 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt2
- add support for latex2rtf
- add lyx package for all lyx package install
- fix an error in patch
- now lyx is qt version by default

* Thu Oct 02 2003 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt1
- new version
- add patch for filenames translation
- add patch for correct language charset

* Fri Apr 04 2003 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt2
- remove really unneeded buildreqs

* Fri Mar 31 2003 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- new version
- split package in lyx-common, lyx-xforms, lyx-qt
- ru.po update
- non koi8-r input broken again in lyx-xforms
- stricted support of russian filenames

* Mon Dec 23 2002 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version
- ru.po update (some errors in 1.2.2 release)

* Thu Dec 05 2002 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt3
- move to Publishing group
- move to section Office/Wordprocessors in menu
- build with new tetex-2.0
- spec cleanup
- ru.po update
- add generic name
- update requires

* Sun Nov 03 2002 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt2
- correct bug with input in cp1251 locale
- new tuning for ru/ua locale
- rebuild for correct problem with incorrect path to locale dir
- add FAQ russian translation

* Mon Oct 07 2002 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version
- update ru_Intro.lyx, ru.po
- some patches for cyrillic purposes

* Tue Sep 24 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2.0-alt1.1
- rebuild with new xforms and XFree (patch5,
  configure hack should be removed after new XFree build)
- added packager tag.

* Sun May 28 2002 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- version 1.2.0 release
- updated ru_splash.lyx ru_Intro.lyx, ru_Tutorial.lyx agaist 1.2.0 release
- updated ru.po agaist 1.2.0 release
- cp1251 documents now have names like ru.CP1251_splash.lyx
- removed doc2lyx support with hope that wvCleanLatex works correctly
- update spec

* Sun May 05 2002 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt0
- version 1.2.0 from CVS
- modified old patches for 1.2.0 release
  + russian input support for 1.2.0 release

* Sun Apr 14 2002 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt11
- add ru_Intro.lyx, ru_Tutorial.lyx, ru_RU_Intro.lyx, ru_RU_Tutorial.lyx
- ru.po update
- remove mozilla browser from detect in configure

* Mon Feb 18 2002 AEN <aen@logic.ru> 1.1.6-alt10
- new ru.po patch from Vitaly Lipatov

* Tue Jan 29 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.1.6-alt9
- Rebuilt with Python-2.2

* Sun Jan 19 2002 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt8
- 1.1.6fix4 patch
- ru.po update
- restructured common -alt patch

* Sun Dec 23 2001 Sergey Vlasov <vsu@altlinux.ru> 1.1.6-alt7
- spec file cleanup
- fixed compilation options, added -fno-exceptions and -D_NOTHREADS
- updated ALT patch:
  + fixed cyrillic.bind to include all keysyms with and without Shift
    (needed to make Caps Lock work correctly with cyrillic characters)
  + fixed ru_RU_splash.lyx file name
- patch in configure.in to avoid picking up libpt from the [lib]pwlib package
- patch to fix problem with entering cyrillic text into a table cell
- patch to get better-looking << and >> quotes

* Sun Dec 16 2001 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt6
- update ru.po
- patch in lib/configure for
  + correct russian default settings
  + recognize temporarily convertor doc2lyx (wait for correct wxLatex)
  + recognize some web browsers
  + key F11 for toggle internal keyboard layout by default
- new koi8-r_win.kmap for Win keyboard layout
- update ru_Splash.lyx

* Wed Jun 27 2001 Sergie Pugachev <fd_rag@altlinux.ru> 1.1.6-alt5
- Rebuilt with python-2.1

* Mon Jun 18 2001 AEN <aen@logic.ru> 1.1.6-alt4
- Requires: xforms-devel

* Thu Jun 14 2001 AEN <aen@logic.ru> 1.1.6-alt3
- io added in cyrillic.bind

* Mon Jun 4 2001 AEN <aen@logic.ru> 1.1.6-alt2
- pt154 fixed
- ru.po fixed

* Wed May 30 2001 AEN <aen@logic.ru> 1.1.6-alt1
- 1.1.6fix2
- new patch

* Sun Dec 24 2000 AEN <aen@logic.ru>
- back to 1.1.5 with two fixes
- new ipl patch:
  + new languages
  + new encodings
  + new cyrillic.bind
  + splach for CP1251
- gcc patch

* Wed Nov 08 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 1.1.6-0.2mdk
- fixed xforms lftp command for ports

* Fri Oct 27 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.6-0.1mdk
- new release
- daouda cleaning
- gcc-2.96 build

* Thu Oct 19 2000 Daouda Lo <daouda@mandrakesoft.com> 1.1.5-5mdk
- include fix2 (Kees report) : a lot of fixes!
- correct handling of icons

* Sat Oct 07 2000 Daouda Lo <daouda@mandrakesoft.com> 1.1.5-4mdk
- force icons to appear (big titi suX)

* Tue Sep 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.5-3mdk
- really install icon (fuc**** crashing ke which losts files)

* Tue Sep 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.5-2mdk
- uses find_lang
- fix Requires
- really install the menu icon (me sucks :-( )

* Mon Sep 18 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.5-1mdk
- many fixes
- BM

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.1.4-7mdk
- automatically added BuildRequires

* Thu Apr 27 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.4-6mdk
- add menu entry
- use spec-helper
- explain in spec how to build it (this needs to be compiled against static
  libxforms (which is authorized by its owners) because we cannot provide
  xforms.

* Thu Apr 27 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.4-5mdk
- various fixes (crash after repeated use of the backspace key, font tags,
  truncated images filename)
- add requires on tetex for post-install script

* Mon Apr 10 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.4-4mdk
- oops! half the locales were forgetted ...

* Thu Mar 30 2000 Thierry Vignaud <tvignaud@mandrakesoft.com>
- new group name (same as klyx)
- fix compilation problems with new autoconf
- fix post-install scripts
- fix installation of i18n po files
- fix some bugs :
	* fix warnings about missing return type in X headers for some
     gcc/egcs versions.
	* fix parsing of LaTeX log files, where some errors got unnoticed.
	* add support for textclasses with more than 128 layouts (yes some
	  people do that!)
	* fix bug with filenames containing more that one "." (for example,
	  a.b.lyx was exported to a.ps).
	* fix partly bug with bibtex files located in the directory of
	  the document (now using an absolute path works).
	* bug in math editor, where greek letters (and some other symbols)
	  had too much spacing around them.

* Thu Mar 02 2000 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix some bugs (i18n, non-gnu dvips handling, and a few others)
- add some warning in spec file in order to explain why we don't provide
  xforms. Hopefully, devel LyX-1.5 is getting independance from xforms ...
- fix compilation with newer g++-2.95.2

* Thu Feb 03 2000 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 1.1.14

* Fri Dec 02 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 1.1.13

* Wed Sep 01 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- rewritten %files (it had conflicts with filesystem package !)
- bzip2'ed man pages
- corrected prefix path; now it find the translation files again

* Wed Aug 18 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- initial spec


