# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: xchm
Version: 1.31
Release: alt1

Summary: xCHM - the CHM viewer for UNIX
License: GPL-2.0-or-later
Group: Office

URL: http://xchm.sourceforge.net
Source: %name-%version.tar
Source1: xchm.desktop

BuildRequires: gcc-c++
BuildRequires: libchm-devel
BuildRequires: libwxGTK3.0-devel
BuildRequires: libssl-devel

%description
xCHM - the CHM files viewer for UNIX.

%prep
%setup

%build
%autoreconf
%configure \
	--enable-debug \
	--enable-optimize
%make_build

%install
%makeinstall_std
install -pD -m644 %SOURCE1 %buildroot%_desktopdir/xchm.desktop

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog README
%_bindir/xchm
%_datadir/metainfo/*
%_desktopdir/xchm.desktop
%_iconsdir/hicolor/*/apps/*
%_man1dir/*

%changelog
* Wed May 20 2020 Anton Midyukov <antohami@altlinux.org> 1.31-alt1
- New version 1.31
- build with wxGTK3.0
- fix License tag

* Wed May 13 2020 Andrey Cherepanov <cas@altlinux.org> 1.23-alt4.1
- NMU: Build without libxmlrpcxx

* Thu Aug 09 2018 Anton Midyukov <antohami@altlinux.org> 1.23-alt4
- Rebuilt with compat-wxGTK3.0-gtk2
- enable unpackaged files terminate build
- fix desktop categories

* Sun Oct 04 2015 Anton Midyukov <antohami@altlinux.org> 1.23-alt3
- Rebuilt for new gcc5 C++11 ABI.

* Mon Jul 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.23-alt2
- Rebuilt with gcc5

* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.23-alt1
- Version 1.23
- Built with wxGTK3.1 instead of wxGTK2.9

* Thu Aug 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.20-alt1.3
- Rebuilt with wxGTK2.9 2.9.5

* Fri May 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.20-alt1.2
- Rebuilt with new wxGTK 2.9

* Tue Jul 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.20-alt1.1
- Rebuilt with updated wxGTK2.9

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 1.20-alt1
- 1.20

* Wed Apr 27 2011 Victor Forsiuk <force@altlinux.org> 1.19-alt1
- 1.19

* Thu Dec 09 2010 Victor Forsiuk <force@altlinux.org> 1.18-alt1
- 1.18

* Wed Aug 26 2009 Victor Forsyuk <force@altlinux.org> 1.17-alt2
- Rebuild due to ALT#20451.

* Thu Jun 18 2009 Victor Forsyuk <force@altlinux.org> 1.17-alt1
- 1.17

* Mon Jan 12 2009 Victor Forsyuk <force@altlinux.org> 1.14-alt4
- Fix desktop file repocop warnings.

* Wed Dec 17 2008 Victor Forsyuk <force@altlinux.org> 1.14-alt3
- Remove obsolete install time scripts.

* Mon Apr 14 2008 Victor Forsyuk <force@altlinux.org> 1.14-alt2
- Desktop file mime entry fix.

* Tue Jan 08 2008 Victor Forsyuk <force@altlinux.org> 1.14-alt1
- 1.14

* Tue May 08 2007 Victor Forsyuk <force@altlinux.org> 1.13-alt1
- 1.13

* Wed Mar 21 2007 Victor Forsyuk <force@altlinux.org> 1.11-alt1
- 1.11

* Thu Feb 15 2007 Victor Forsyuk <force@altlinux.org> 1.10-alt1
- 1.10
- Install pixmaps for system menus.
- Switch from debian-style menu entry to freedesktop one.

* Wed Jun 07 2006 Andrey Semenov <mitrofan@altlinux.ru> 1.9-alt1
- 1.9

* Wed May 24 2006 Andrey Semenov <mitrofan@altlinux.ru> 1.8-alt1
- 1.8

* Wed Apr 19 2006 Andrey Semenov <mitrofan@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Fri Mar 24 2006 Andrey Semenov <mitrofan@altlinux.ru> 1.5-alt1
- 1.5

* Wed Mar 01 2006 Andrey Semenov <mitrofan@altlinux.ru> 1.4-alt1
- 1.4

* Mon Feb 20 2006 Andrey Semenov <mitrofan@altlinux.ru> 1.3-alt1
- 1.3

* Thu Dec 22 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.2-alt3
- update builreq

* Thu Dec 15 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.2-alt2
- rebuild

* Mon Nov 28 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.2-alt1
- new version

* Tue Jun 07 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.0-alt1
- 1.0

* Fri Feb 25 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Sat Jan 08 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Mon Oct 25 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.9.6-alt1
- new version

* Wed Sep 22 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.9.5-alt1
- new version
- added support for context sensitive help
- code contributed by Eamon Millman from PCI Geomatics

* Fri Sep 03 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.9.4-alt1
- new version
- fixed contents parsing problem

* Wed Jul 21 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.9.3-alt1
- new version
- fixed 'MS-ITS:' link handling
- corrected a contents tree bug

* Thu Jul 15 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.9.2-alt2
- rebuild

* Mon Jul 12 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.9.2-alt1
- new version
- fixed a fonts dialog bug

* Tue May 11 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.9.1-alt2
- rebuild with gcc-3.3

* Mon Apr 5 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.9.1-alt1
- 0.9.1
- fixed an index bug
- added translations for Italian, German, Portuguese and Russian

* Fri Jan 23 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.9-alt1
- 0.9
- added i18n support
- added Romanian and French translations of xCHM's interface
- no more warnings on wxWidgets 2.5.1 compilations

* Fri Jan 23 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.8.11-alt1
- 0.8.11
- bugfix release

* Tue Jan 6 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.8.10-alt1
- 0.8.10
- fixed a horizontal scrollbar repainting bug that occured in the search and index tabs.

* Mon Dec 8 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.8.9-alt1
- 0.8.9
- bugs fixed

* Sun Nov 8 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.8.8-alt1
- 0.8.8
- all the wxListBox widgets have been replaced with wxListCtrl derived controls
- suppressed unhelpful error messages while loading a page

* Sun Oct 26 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.8.7-alt1
- 0.8.7
- the contents panel sash position persists between sessions
- decreased the default application font size from 14 to 12
- added opened files history support

* Tue Oct 14 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.8.6-alt1
- 0.8.6
- bugs fixed

* Thu Oct 9 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.8.5-alt1
- 0.8.5
- made xCHM properly handle weird charset languages (Russian, Chinese)

* Thu Oct 2 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.8.4-alt1
- 0.8.4
- corrected a bug that crashed xchm if the user tried to open a .chm file that is not present on disk

* Mon Sep 29 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.8.3-alt1
- 0.8.3
- fixed a relative path bug both for HTML pages and imaged
- fixed the tree control to display contents in the native font encoding

* Wed Sep 24 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.8.2-alt1
- 0.8.2
- added a popup menu with common options (back, forward, copy selection, find in page)
- beautified the tree control and enabled variable sizes for the tree items

* Mon Sep 15 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.8.1-alt1
- 0.8.1
- added support for 'javascript:fullSize' URLs
- beautified the font dialog a bit
- fixed empty title in the titlebar bug
- refined the synchronization between the contents tree and the wxHtmlWindow displayed page

* Wed Sep 10 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.8-alt1
- 0.8
- major feature enhancements
- added bookmark support

* Mon Sep 1 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.7.1-alt1
- 0.7.1
- fixed bugs in the full document HTML search
- added a 'Search titles only' checkbox

* Thu Aug 28 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.7-alt1
- 0.7
- added a full search panel and changed the layout of the contents panel

* Wed Aug 27 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Mon Aug 11 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.6.1-alt1
- 0.6.1
- fixed Unicode bug

* Thu Aug 7 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.6-alt1
- 0.6
- added a custom selection font chooser dialog

* Tue Aug 5 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.5.2-alt1
- First version of RPM package.
