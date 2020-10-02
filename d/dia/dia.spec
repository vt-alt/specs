# INFO: For update, do git merge -s ours with new tag rom upstream repo
%ifndef e2k
%define e2k e2k e2kv4 e2kv5 e2kv6 e2k4c e2k8c e2k1cp e2k8c2 e2k12c e2k16c e2k2c3
%endif

%define major 0.97
Name: dia
Version: %major.4
Release: alt0.7.1

Summary: A gtk+ based diagram creation program
Summary(ru_RU.UTF-8): Программа для создания диаграмм, основанная на GTK+

License: GPL
Group: Office
Url: http://www.gnome.org/projects/dia

Packager: Valery Inozemtsev <shrek@altlinux.ru>

%py_provides dia
Obsoletes: %name-gnome %name-python

# Do not use: http://ftp.gnome.org/pub/gnome/sources/dia/%major/%name-%version.tar
# Source-git: https://git.gnome.org/browse/dia/
Source: %name-%version.tar
Source2: ru.po

#Patch: %name-%version-%release.patch
Patch: alt-dia-fix-help.patch
Patch2: alt-dia-improve-translation.patch
Patch3: CVE-2019-19451-adapted-fix.patch

BuildRequires: dblatex docbook-style-xsl docbook-utils gcc-c++ intltool libart_lgpl-devel libgtk+2-devel libxslt-devel
BuildRequires: python-devel python-module-PyXML python-module-pygtk python-modules-email python-modules-encodings xsltproc
%ifnarch %e2k
BuildRequires: libEMF-devel
%endif
BuildRequires: libpng-devel
BuildRequires: desktop-file-utils

%description
Dia is a GNU program designed to be much like the Windows
program 'Visio'. It can be used to draw different kind of diagrams.

It can be used to draw a variety of diagram types, including UML, Network,
flowchart and others.  The native file format for Dia is XML (optionally
gzip compressed).  It has print support, and can export to a number of
formats such as EPS, SVG, CGM and PNG.

%description -l ru_RU.UTF-8
Программа Dia разработана как альтернатива Visio для Windows(TM). Dia
можно использовать для рисования различных типов диаграмм, она
включает поддержку структурных статических диаграмм UML (диаграмм
классов), моделирование отношений объектов и сетевых диаграмм. Dia
может загружать и сохранять диаграммы в собственном формате и в
формате .xml, а также экспортировать их в различные форматы, такие как
PostScript(TM), SVG, CGM или PNG.

%add_findprov_lib_path %_libdir/%name

%prep
%setup
#patch -p1
%patch -p1
%patch2 -p1
%patch3 -p1

cp -f %SOURCE2 po/ru.po

install -m644 data/icons/48x48/apps/%name.png app/pixmaps/%name-app.png

%build
intltoolize --force
%autoreconf
%configure  \
	--enable-db2html \
	--with-hardbooks \
	--disable-gnome \
	--without-python \
%ifarch x86_64 %e2k
	--disable-libemf \
%endif
	--disable-static
%make_build

%install
%makeinstall_std
rm -rf %buildroot%_libdir/dia/*.la

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Graphics \
	--add-category=Office \
	--add-category=Chart \
	%buildroot%_desktopdir/dia.desktop

%files -f %name.lang
%doc README TODO NEWS AUTHORS
%_docdir/dia/
%docdir %_docdir/dia/
%_bindir/%name
%dir %_libdir/%name
%_libdir/%name/*.so
%_datadir/%name/
%_datadir/mime-info/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_man1dir/*
%_mandir/fr/man1/*

%changelog
* Fri Oct 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.97.4-alt0.7.1
- Applied security fix from upstream (Fixes: CVE-2019-19451).

* Mon Jan 21 2019 Ivan Razzhivin <underwit@altlinux.org> 0.97.4-alt0.7
- improve translation

* Tue Jan 15 2019 Ivan Razzhivin <underwit@altlinux.org> 0.97.4-alt0.6
- improve translation

* Wed Nov 21 2018 Ivan Razzhivin <underwit@altlinux.org> 0.97.4-alt0.5
- improve translation

* Tue Nov 13 2018 Ivan Razzhivin <underwit@altlinux.org> 0.97.4-alt0.4
- improve translation

* Fri Sep 14 2018 Ivan Razzhivin <underwit@altlinux.org> 0.97.4-alt0.3
- fix help

* Wed May 30 2018 Michael Shigorin <mike@altlinux.org> 0.97.4-alt0.2
- %%e2k: disable libEMF too (archdep)

* Thu Mar 24 2016 Vitaly Lipatov <lav@altlinux.ru> 0.97.4-alt0.1
- real build pre 0.97.4 from git 050e8f6d631de7eff

* Wed Sep 24 2014 Vitaly Lipatov <lav@altlinux.ru> 0.97.3-alt1
- new version 0.97.3 (with rpmrb script)

* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.97.2-alt2
- fix Bug 694025 - GLib drop support for adding interfaces after class_init (ALT bug #28807)
- cleanup build

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.97.2-alt1.1
- Rebuilt with libpng15

* Sat May 26 2012 Vitaly Lipatov <lav@altlinux.ru> 0.97.2-alt1
- build new version (ALT bug #27156)

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.97.1-alt2.2
- Fixed build with new glib2

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.97.1-alt2.1.qa1.1
- Rebuild with Python-2.7

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.97.1-alt2.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for dia

* Sun Mar 27 2011 Michael Shigorin <mike@altlinux.org> 0.97.1-alt2.1
- NMU: re-added missing BR: libpng-devel

* Mon Feb 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.97.1-alt2
- x86_64: disabled libemf

* Tue Jan 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.97.1-alt1
- 0.97.1

* Tue Sep 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.97-alt5
- updated Russian translation (closes: #21476)

* Tue Jun 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.97-alt4
- rebuild with libpng12 1.2.37-alt2

* Sun May 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.97-alt3
- integrated mode by default

* Sun May 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.97-alt2
- 0.97 release

* Mon Apr 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.97-alt1.pre3
- 0.97 pre3

* Mon Mar 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.97-alt1.pre2
- 0.97 pre2

* Fri Dec 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.96.1-alt3
- fixed build with new auto*

* Sun Jul 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.96.1-alt2
- build help (close #5807)

* Sat Mar 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.96.1-alt1
- 0.96.1

* Wed Mar 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.96-alt1
- 0.96 release

* Thu Mar 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.96-alt0.0pre9
- 0.96-pre9

* Sat Mar 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.96-alt0.0pre8
- 0.96-pre8

* Sun Jan 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.96-alt0.0pre1
- 0.96-pre1

* Tue Aug 15 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.95-alt0.1cvs20060813
- CVS snapshot 2006-08-13
- spec cleanup

* Mon May 29 2006 Vitaly Lipatov <lav@altlinux.ru> 0.95-alt0.1cvs20060514
- CVS snapshot
- fix Source URL
- disable translations

* Sat Apr 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0.95-alt0.1cvs20060408
- CVS snapshot about dia 0.9.5pre8

* Tue Feb 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt13cvs20051206
- CVS snapshot about dia 0.9.5pre4
- update ALT patch
- remove INSTALL

* Tue Dec 06 2005 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt12cvs20051206
- new CVS snapshot
- some spec changes

* Mon Oct 03 2005 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt12cvs20051003
- new CVS snapshot (fixes some segfaults)
- change russian description (get from PLD :))
- add autotest after build (disabled by default)
- Note: http://bugzilla.gnome.org/show_bug.cgi?id=317637 is not fixed yet?

* Tue Sep 06 2005 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt11cvs20050825
- change %_libdir to %_libdir
- hack SegFault: mark danger places where object is undefined
- change autosave time to every 1 minute

* Mon Aug 29 2005 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt10cvs20050825
- fix bug #7774
- fix broken export via GUI dialog
- move scrollkeeper to -gnome package

* Thu Aug 25 2005 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt9cvs20050825
- new CVS snapshot

* Mon Aug 01 2005 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt9cvs20050730
- new CVS snapshot
- fix bug #7075 (broken eps export in non C locale)
- move to dia-gnome some libs linked with gnome

* Fri Jul 08 2005 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt8cvs20050313.1
- x86_64 support from mouse@ (fix bug# 7266)

* Mon Mar 21 2005 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt8cvs20050313
- add buildrequire for python version 2.4

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt7cvs20050313
- fix SegFault during exit (thanks crux@)
- build with python 2.4

* Sun Mar 13 2005 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt6cvs20050313
- fix bug #2441 (there is new problem with SigFault during exit :( )

* Sun Feb 06 2005 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt5cvs20050205
- CVS version (really only from this build)
- patch for filename encoding issues

* Fri Dec 31 2004 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt4
- fix spec for libdia.so is gtk only compiled

* Sun Dec 26 2004 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt3
- disable GNOME build for main dia package
- add dia-gnome package (with all GNOME dependenses)

* Tue Nov 30 2004 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt2
- disable python support due libpython2.3a missing
- spec file comformed to GNOME program packaging policy
- add patch for encoding issues

* Thu Sep 02 2004 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt1
- release
- remove old patches (upstreamed)
- fixed bug #4938

* Fri Jul 23 2004 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt0.3pre2
- new version (pre2)
- update ru.po
- add patch for fix filedialog's encoding issues

* Sun Jun 20 2004 Vitaly Lipatov <lav@altlinux.ru> 0.93-alt3
- add patch for fix batch mode (bug #2441)
- add patch for recoding console messages

* Sat May 29 2004 Vitaly Lipatov <lav@altlinux.ru> 0.93-alt2
- change URL (Dia page moved to gnome.org)
- update ru.po
- remove oaf-slay from pre script

* Thu May 20 2004 Vitaly Lipatov <lav@altlinux.ru> 0.93-alt1
- new version
- remove COPYING from doc

* Sun Jan 04 2004 Vitaly Lipatov <lav@altlinux.ru> 0.92-alt2
- add gcc-c++ in requires
- rebuild with gcc 3.3

* Fri Oct 24 2003 Vitaly Lipatov <lav@altlinux.ru> 0.92-alt1
- release of 0.92

* Wed Sep 24 2003 Vitaly Lipatov <lav@altlinux.ru> 0.92-alt0.2pre
- new version

* Tue Apr 01 2003 Vitaly Lipatov <lav@altlinux.ru> 0.91-alt2
- remove incorrect stylesheets.xml before build
- remove .so loading from xslt plug-in

* Tue Mar 18 2003 Vitaly Lipatov <lav@altlinux.ru> 0.91-alt1
- new version (Gnome2)
- ru.po update

* Thu Jan 30 2003 Vitaly Lipatov <lav@altlinux.ru> 0.90-alt6
- build without python support via pygtk2 problems (bug #2052)
- buildrequires update

* Mon Jan 06 2003 Vitaly Lipatov <lav@altlinux.ru> 0.90-alt5
- moved to Office/Graphs menu group
- add genericname
- built with python again

* Thu Nov 14 2002 AEN <aen@altlinux.ru> 0.90-alt4
- rebuilt in curent environment w/o python

* Mon Oct 28 2002 Vitaly Lipatov <lav@altlinux.ru> 0.90-alt3
- spec cleanup
- ru.po update
- tested with gcc-3.2

* Sun Jun 04 2002 Vitaly Lipatov <lav@altlinux.ru> 0.90-alt2
- ru.po update
- spec cleaned
- patch for old russian files detected
- NB! old files are not supported for libxml1 problem

* Mon Jun 03 2002 AEN <aen@logic.ru> 0.90-alt1
- new version
- fonts patch updated

* Wed Mar 13 2002 AEN <aen@logic.ru> 0.88.1-alt6
- crash in meny tools fixed

* Tue Jan 29 2002 AEN <aen@logic.ru> 0.88.1-alt5
- rebuilt with python-2.2.

* Fri Dec 27 2001 AEN <aen@logic.ru> 0.88.1-alt4
- builtwith python
- mdk patches

* Thu Oct 11 2001 AEN <aen@logic.ru> 0.88.1-alt3
- rebuilt with libpng.so.3
- PreReq: oaf

* Wed May 22 2001 AEN <aen@logic.ru> 0.88.1-alt2
- restore conv patch

* Wed May 22 2001 AEN <aen@logic.ru> 0.88.1-alt1
- new version

* Mon May 14 2001 AEN <aen@logic.ru> 0.88-alt1
- new version
- printing fixed

* Wed Feb 28 2001 AEN <aen@logic.ru> 0.86-ipl6mdk
- rebuild with new libraries

* Sat Jan 20 2001 AEN <aen@logic.ru>
- add missing files

* Sat Jan 13 2001 AEN <aen@logic.ru>
- RE adaptation
- new fonts patch

* Thu Oct 26 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 0.86-3mdk
- recompiled with gnome-print 0.24

* Thu Sep  7 2000 Vincent Saugey <vince@mandrakesoft.com> 0.86-2mdk
- Adding many icons on various format

* Mon Aug  7 2000 Vincent Saugey <vince@mandrakesoft.com> 0.86-1mdk
- Up to 0.86

* Tue Jul 25 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.85-2mdk
- macroszification
- rebuild for BM

* Fri May 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.85-1mdk
- Up to 0.85

* Mon May 15 2000 Pixel <pixel@mandrakesoft.com> 0.84-6mdk
- add buildrequires libxml

* Fri May  5 2000 Vincent Saugey <vince@mandrakesoft.com> 0.84-5mdk
- Remove locale to prevent crash

* Fri Apr 28 2000 Vincent Saugey <vince@mandrakesoft.com> 0.84-4mdk
- Add dependencie to ISO font

* Mon Apr 17 2000 Vincent Saugey <vince@mandrakesoft.com> 0.84-3mdk
- Corrected group
- Add icon

* Mon Mar 27 2000 Vincent Saugey <vince@mandrakesoft.com> 0.84-2mdk
- add menu

* Mon Mar 07 2000 Vincent Saugey <vince@mandrakesoft.com> 0.84-1mdk
- v0.84

* Mon Jan 03 2000 Lenny Cartier <lenny@mandrakesoft.com>
- v0.83
- used srpm provided by Gwenael Letellier <gwenael@linux-mandrake.com>

* Mon Dec 20 1999 Lenny Cartier <lenny@mandrakesoft.com>

- bz2 archive

* Fri Dec 17 1999 Frederic Lepied <flepied@mandrakesoft.com>

- 0.82
- first mandrake version.

* Sun Oct 17 1999 Miles Lott <milos@insync.net>

- Build for 0.80
- added version string to setup line

* Sun Sep 05 1999 James Henstridge <james@daa.com.au>

- added $(prefix)/share/dia to files list.

* Thu Apr 29 1999 Enrico Scholz <enrico.scholz@wirtschaft.tu-chemnitz.de>

- Made %%setup quiet
- Enabled build from cvs
- Removed superfluous mkdir's
- using DESTDIR and install-strip

* Fri Aug 28 1998 Francis J. Lacoste <francis@Contre.COM>

- First RPM release.

