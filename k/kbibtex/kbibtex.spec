%define Name KBibTeX
%define oname kbibtex

Name: kbibtex
Version: 0.9
Release: alt1.1
Summary: A BibTeX editor for Qt5 and KDE5
License: %gpl2plus
Group: Publishing
URL: http://home.gna.org/%oname
Source: %oname-%version.tar
#Patch: %oname-%version-%release.patch
Requires: lib%{oname}part9 = %EVR
Packager: Evgeny Sinelnikov <sin@altlinux.ru>

BuildRequires(pre): rpm-build-licenses rpm-build-kf5 rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake extra-cmake-modules
BuildRequires: qt5-xmlpatterns-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kwallet-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-ktexteditor-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: libpoppler-qt5-devel
BuildRequires: libxslt-devel xml-utils xorg-cf-files

Conflicts: kde3-kbibtex

%description
%Name is a BibTeX editor for Qt5 and KDE5 to edit bibliographies
used with LaTeX. Features include comfortable input masks, starting
web queries (e. g. Google or PubMed) and exporting to PDF, PostScript,
RTF and XML/HTML. As %Name is using KDE's KParts technology.

%package -n lib%{oname}part9
Summary: %Name KParts BibTeX library for Qt5 and KDE5
Group: System/Libraries
Conflicts: lib%{oname}part3
Obsoletes: lib%{oname}part4

%description -n lib%{oname}part9
%Name is a BibTeX library for Qt5 and KDE5 to edit bibliographies
used with LaTeX. Features include comfortable input masks, starting
web queries (e. g. Google or PubMed) and exporting to PDF, PostScript,
RTF and XML/HTML. This package contains KDE's KParts technology library.

%prep
%setup -n %oname-%version
#patch -p1

%build
%K5build

%install
%K5cmake
%K5install

%find_lang --with-kde %oname

%files -f %oname.lang
%doc LICENSE README TODO
%_datadir/%oname
%_K5xdgapp/*
%_K5xdgmime/*
%_K5bin/%oname
%_K5icon/*/*/apps/*
%_K5xmlgui/%oname
%_datadir/metainfo/*

%files -n lib%{oname}part9
%_libdir/*.so*
%_K5link/lib*.so
%_K5xdgconf/*
%_K5xmlgui/%{oname}part
%_K5plug/*.so
%_K5srv/*

%changelog
* Wed Dec 25 2019 Anton Midyukov <antohami@altlinux.org> 0.9-alt1.1
- require libkbibtexpart9 again
- obsoletes libkbibtexpart4 (needed for upgrade)
- fix descriptions

* Tue Sep 17 2019 Anton Midyukov <antohami@altlinux.org> 0.9-alt1
- build last stable release for Qt5 and KDE5 (Closes: 36079)

* Wed Jun 26 2013 Evgeny Sinelnikov <sin@altlinux.ru> 0.4.1-alt1
- build last stable release for Qt4 and KDE4

* Mon Jun 24 2013 Evgeny Sinelnikov <sin@altlinux.ru> 0.2.3.91-alt1
- update to last stable release for Qt3 and KDE3

* Sun Jun 23 2013 Evgeny Sinelnikov <sin@altlinux.ru> 0.2.3-alt2
- build with Trinity libraries

* Wed Aug 26 2009 Sergey V Turchin <zerg@altlinux.org> 0.2.3-alt1
- new version

* Wed Mar 11 2009 Led <led@altlinux.ru> 0.2.1.91-alt1
- 0.2.2.91 (0.2.2 Beta 2)

* Sun Feb 01 2009 Led <led@altlinux.ru> 0.2.1.90-alt1
- 0.2.2.90 (0.2.2 Beta 1)

* Sun Dec 28 2008 Led <led@altlinux.ru> 0.2.1.81-alt1
- 0.2.1.81
- cleaned up spec

* Sun Oct 26 2008 Led <led@altlinux.ru> 0.2.1.80-alt2
- fixed build with g++ 4.3

* Sun Sep 14 2008 Led <led@altlinux.ru> 0.2.1.80-alt1
- 0.2.1.80
- updated kbibtex-0.2.1.80-alt-makefile.patch
- added kbibtex-0.2.1.80-alt-format.patch

* Thu Jun 26 2008 Led <led@altlinux.ru> 0.2.1-alt1
- initial build
