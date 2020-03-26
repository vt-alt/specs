%define _unpackaged_files_terminate_build 1

Name: kchmviewer
Version: 7.7
Release: alt3

Summary: A CHM (Winhelp) and EPUB viewer
License: %gpl3plus
Group: Office
Url: http://kchmviewer.net

Source: %name-%version.tar
Patch1: %name-%version-qtwebengine.patch
Patch2: %name-%version-alt-underlinking.patch

BuildRequires(pre): rpm-build-licenses rpm-macros-make
BuildRequires: gcc-c++ libchm-devel libzip-devel qt5-base-devel
BuildRequires: qt5-webengine-devel
BuildRequires: libXxf86misc-devel

Obsoletes: kchmviewer4 <= 4.0-alt3
Obsoletes: kchmviewer-nokde
Provides: kchmviewer4 = %EVR

%description
Kchmviewer is a CHM (aka MS HTML help) and EPUB viewer written in C++.
The main advantage of KchmViewer is extended support for non-English
languages. Unlike others, KchmViewer in most cases correctly detects chm
file encoding, correctly shows tables of context of Russian, Korean,
Chinese and Japanese help files. It also correctly searches text in
non-English help files, including Korean, Chinese and Japanese.

%prep
%setup
%patch1 -p1
%patch2 -p2

%build
%add_optflags -I%_includedir/libzip
%qmake_qt5
%make_build

%install
%installqt5
install -pD -m755 bin/kchmviewer %buildroot%_bindir/%name
install -pD -m644 packages/kchmviewer.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png
install -pD -m644 packages/kchmviewer.desktop %buildroot%_desktopdir/%name.desktop

%files
%_bindir/%name
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/%name.desktop
%doc ChangeLog DBUS-bindings FAQ README
%doc COPYING

%changelog
* Thu Mar 19 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 7.7-alt3
- Fixed epub support.

* Wed Mar 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 7.7-alt2
- Rebuilt with qtwebengine instead of qtwebkit.

* Tue Feb 05 2019 Slava Aseev <ptrnine@altlinux.org> 7.7-alt1
- Version 7.7

* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.0-alt1.beta1.svn20140803
- Version 7.0beta1

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 5.2-alt1.qa1
- NMU: rebuilt for updated dependencies.

* Sat Feb 05 2011 Ivan A. Melnikov <iv@altlinux.org> 5.2-alt1
- 5.2
- patch updated
- added patch 1 to fix cmake build
- rebuild with new Qt to fix crash with QWebKit

* Sun Dec 20 2009 Andrey Rahmatullin <wrar@altlinux.ru> 5.1-alt1
- 5.1

* Tue Dec 15 2009 Andrey Rahmatullin <wrar@altlinux.ru> 5.0-alt1
- 5.0

* Sun Oct 25 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.2-alt1
- 4.2

* Thu Sep 10 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.1-alt2
- move icons from crystalsvg/ to hicolor/

* Tue Jul 21 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.1-alt1
- 4.1

* Sat May 30 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt5
- don't conflict with ocular >= 4.2.3-alt1

* Sun Mar 15 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt4
- rename back to kchmviewer
- update description
- build a version without KDE support (closes: #12407)

* Tue Dec 02 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt3
- 4.0 release

* Sat Aug 09 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt2.beta3
- enable KDE4_ENABLE_FINAL

* Tue Jun 10 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt1.beta3
- 4.0beta3
- Sisyphus build

* Thu Mar 20 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt1.beta2
- add update_desktopdb/clean_desktopdb calls (found by repocop)
- fix desktop file according to desktop-file-validate

* Tue Feb 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt0.beta2
- 4.0 beta2

* Sat Sep 22 2007 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt0.beta1
- 4.0 beta1

* Sun Jun 17 2007 Andrey Rahmatullin <wrar@altlinux.ru> 3.1-alt1
- 3.1-2

* Sun Apr 01 2007 Andrey Rahmatullin <wrar@altlinux.ru> 3.0-alt1
- 3.0

* Thu Dec 07 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.7-alt1
- 2.7

* Thu Oct 05 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.6-alt1
- 2.6
- take from orphaned
- build with KDE
- spec fixes and cleanup
- enable installing of translation files
- enable _unpackaged_files_terminate_build

* Wed Apr 19 2006 Andrey Semenov <mitrofan@altlinux.ru> 2.5-alt1
- 2.5

* Tue Feb 07 2006 Andrey Semenov <mitrofan@altlinux.ru> 2.0-alt1
- new version

* Mon Nov 28 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.3-alt1
- new version

* Wed Nov 02 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.1-alt1
- new version

* Mon Sep 12 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.0-alt2
- add file menu

* Fri Jul 29 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.0-alt1
- 1.0

* Thu Jun 30 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.92-alt1
- 0.92

* Mon Jun 20 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.91-alt1
- 0.91

* Wed Jun 08 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.9-alt1
- 0.9

* Thu May 12 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.3-alt1
- 0.3

* Mon Apr 25 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.2-alt1
- 0.2

* Thu Apr 21 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.1-alt1
- First version
