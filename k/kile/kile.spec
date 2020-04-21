%def_disable shared
%def_enable static
%def_disable rpath
%def_disable debug

%define Name Kile
%define oname kile
Name: kile
Version: 2.9.93
Release: alt1
Summary: LaTeX source editor - TeX shell
Group: Publishing
License: %gpl2plus
URL: http://%name.sourceforge.net
Source: %oname-%version.tar
#Patch: %oname-%version-%release.patch
Packager: Evgeny Sinelnikov <sin@altlinux.ru>

Requires: libkbibtexpart9
Requires: kde5-okular
Requires: %_bindir/asy %_bindir/convert %_bindir/dblatex
Requires: %_bindir/bibtex %_bindir/dvipdfm %_bindir/dvipng
Requires: %_bindir/dvips %_bindir/latex %_bindir/latex2html
Requires: %_bindir/lilypond %_bindir/makeindex %_bindir/mpost
Requires: %_bindir/pdflatex %_bindir/pdftex %_bindir/ps2pdf
Requires: %_bindir/tex

BuildRequires(pre): rpm-build-licenses rpm-build-kf5
BuildRequires: doxygen gcc-c++
BuildRequires: cmake extra-cmake-modules
BuildRequires: qt5-base-devel
BuildRequires: qt5-script-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kinit-devel
BuildRequires: kf5-khtml-devel kf5-kjs-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-ktexteditor-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kde5-okular-devel
BuildRequires: libXt-devel libjpeg-devel xml-utils xorg-cf-files

Obsoletes: kde4-kile
Conflicts: kde3-kile

%description
%Name is a program for KDE 5, that integrates many tools needed to
develop documents with LaTeX, in just one application.

%prep
%setup -n %oname-%version
#patch -p1

%build
%K5cmake -DKILE_VERSION=%version
%K5build

%install
%K5install

%find_lang --with-kde %oname

rm -fr %buildroot%_docdir/%oname

%files -f %oname.lang
%doc AUTHORS ChangeLog README README.cwl %oname-remote-control.txt
%_K5bin/*
%_K5icon/*/*/apps/*
%_K5xdgapp/*
%_K5xdgconf/*
%_datadir/kconf_update/*
%_datadir/%oname
%_libdir/*.so
%_K5cfg/*
%_K5dbus_iface/*
%_K5doc/*/%oname
%_K5xdgmime/*
%_datadir/metainfo/*

%changelog
* Wed Dec 25 2019 Anton Midyukov <antohami@altlinux.org> 2.9.93-alt1
- update to 3.0 beta 3

* Tue Sep 17 2019 Anton Midyukov <antohami@altlinux.org> 2.9.92-alt1
- update to 3.0 beta 2

* Thu Jun 20 2013 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.3-alt1
- update to last stable release

* Tue Apr 27 2010 Evgeny Sinelnikov <sin@altlinux.ru> 2.1b4-alt1
- build new version

* Sun Mar 14 2010 Evgeny Sinelnikov <sin@altlinux.ru> 2.1b3-alt2
- add translations from l10n-kde4 SVN (revision 1055480 from Nov 28)
- fixed force termination when the main window is closed (Fedora#557436, kde#220343)

* Sun Mar 14 2010 Evgeny Sinelnikov <sin@altlinux.ru> 2.1b3-alt1
- build new version for KDE4

* Sun Dec 14 2008 Led <led@altlinux.ru> 2.0.3-alt1
- 2.0.3
- cleaned up spec
- fixed BuildRequires

* Sun Sep 14 2008 Led <led@altlinux.ru> 2.0.2-alt1
- 2.0.2
- updated BuildRequires

* Sat Aug 09 2008 Led <led@altlinux.ru> 2.0.1-alt3
- fixed %name.desktop
- fixed post scripts

* Thu Jun 26 2008 Led <led@altlinux.ru> 2.0.1-alt2
- added Requires (#9379)
- added %name-2.0.1-alt-tools_prio.patch

* Wed Jun 18 2008 Led <led@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Mon Mar 31 2008 Led <led@altlinux.ru> 2.0.1-alt0.1
- 2.0.1rc1
- fixed License

* Fri Feb 15 2008 Led <led@altlinux.ru> 2.0-alt0.1
- 2.0

* Fri Feb 15 2008 Led <led@altlinux.ru> 1.9.3-alt0.1
- 1.9.3
- cleaned up spec

* Mon Sep 25 2006 Mikerin Sergey <mikcor@altlinux.ru> 1.9.2-alt1
- 1.9.2

* Tue Jul 04 2006 Mikerin Sergey <mikcor@altlinux.ru> 1.9.1-alt1
- 1.9.1

* Wed Mar 22 2006 Mikerin Sergey <mikcor@altlinux.ru> 1.9-alt1
- 1.9
- new buildrequires

* Tue May 03 2005 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.8-alt0.1.b2
- 1.8b2

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.7.1-alt1.1.1
- Rebuilt with libstdc++.so.6.

* Wed Nov 17 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.7.1-alt1.1
- remove conflict files

* Fri Oct 22 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Wed Jun 02 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.6.3-alt1
- 1.6.3

* Sun Jan 25 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.6-alt3
- fix builrequires

* Sun Dec 14 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.6-alt2
- rebuilding without *.la

* Thu Nov 13 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.6-alt1
- 1.6
- new buildrequires and rebuilding in hasher

* Fri Aug 22 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Wed May 21 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.5-alt1
- 1.5

* Wed Mar 12 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.4-alt1
- 1.4

* Mon Jan 20 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.32-alt1
- 1.32
- new buildrequires

* Sun Dec 22 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.31-alt1
- 1.31

* Mon Oct 14 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.3beta-alt1
- 1.3beta

* Tue Sep 17 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2-alt1
- new version
- built with gcc3.2

* Mon Jun 17 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.0-alt1
- 1.0

- specfile cleanup

