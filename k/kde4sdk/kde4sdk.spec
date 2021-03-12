
%add_findpackage_path %_K4bindir
%add_findreq_skiplist %_K4apps/lokalize/scripts/*.py
%add_findreq_skiplist %_K4bindir/kdedoc
%add_findreq_skiplist %_K4bindir/package_crystalsvg

%def_disable kio_svn

%define rname kdesdk
Name: kde4sdk
%define major 15
%define minor 12
%define bugfix 2
Version: %major.%minor.%bugfix
Release: alt4

Group: Graphical desktop/KDE
Summary: K Desktop Environment - Software Development Kit
License: GPL
Url: ftp://ftp.kde.org/pub/kde/stable/%version/src/
Packager: Sergey V Turchin <zerg at altlinux dot org>

#Requires: %name-core = %version-%release
#Requires: %name-lokalize = %version-%release
#Requires: %name-kapptemplate = %version-%release
#Requires: %name-kuiviewer = %version-%release
Requires: %name-scripts = %version-%release
#Requires: %name-strigi-analyzer = %version-%release
Requires: %name-po2xml = %version-%release
#Requires: %name-umbrello = %version-%release
#Requires: %name-cervisia = %version-%release
#Requires: %name-kompare = %version-%release
#Requires: %name-kmtrace = %version-%release
#Requires: %name-kcachegrind = %version-%release
#Requires: %name-dolphin = %version-%release
#Requires: %name-okteta = %version-%release
#Requires: %name-thumbnailers = %version-%release


Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%rname-%version.tar
Patch1: kdesdk-4.0.2-alt-find-libsvn.patch
Patch2: %rname-alt-castxml-compat.patch
Patch3: %rname-alt-gcc6.patch

# Remove 'gccxml' from 'Requires'
%define __find_provides sh -c '/usr/lib/rpm/find-provides | sort | uniq'
%define __find_requires sh -c '/usr/lib/rpm/find-requires | sort | uniq | sed "/^gccxml$/d"'

BuildRequires(pre): kde4libs-devel
%if_enabled kio_svn
BuildRequires: libsubversion-devel
%endif
BuildRequires: perl-XML-DOM perl-Switch libldap-devel libltdl-devel gcc-c++
BuildRequires: rpm-build-python python-modules-encodings
BuildRequires: libiberty-devel libjpeg-devel libxslt-devel bzlib-devel
BuildRequires: gettext-tools
BuildRequires: boost-devel libhunspell-devel desktop-file-utils perl-Pod-Parser
BuildRequires: kde4libs-devel
#BuildRequires: kde4pimlibs-devel libkomparediff2-devel
#BuildRequires: kde4base-workspace-devel kde4base-devel

%description
Software Development Kit for the K Desktop Environment.

%package common
Summary: Common empty package for %rname
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common >= %major.%minor
Conflicts: kdesdk-common <= 3.5.12-alt1
%description common
Common empty package for %rname

%package core
Summary: Core files needed for %rname
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description core
Core files needed for %rname

%package okteta
Summary: Byte level data editor
Group: Development/Tools
Requires: %name-common = %version-%release
Provides: kde4utils-okteta = %version-%release
Obsoletes: kde4utils-okteta < %version-%release
%description okteta
Viewing and editing of data on the byte level

%package -n libokteta1core4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libokteta1core4
KDE 4 library

%package -n libokteta1gui4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libokteta1gui4
KDE 4 library

%package -n libkasten2okteta1controllers4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkasten2okteta1controllers4
KDE 4 library

%package -n libkasten2okteta1core4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkasten2okteta1core4
KDE 4 library

%package -n libkasten2okteta1gui4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkasten2okteta1gui4
KDE 4 library

%package lokalize
Group: Development/Tools
Summary: Computer-aided translation system
Requires: %name-core = %version-%release
Provides: %name-localize = %version-%release
%description lokalize
Computer-aided translation system

%package kapptemplate
Summary: Template for KDE Application Development
Group: Development/KDE and QT
Requires: %name-core = %version-%release
%description kapptemplate
KAppTemplate is a set of modular shell scripts that will create a
framework for any number of KDE application types. At it's base
level, it handles creation of things like the automake/autoconf
framework, lsm files, RPM spec files, and po files. Then, there
are individual modules that allow you to create a skeleton KDE
application, a KPart application, a KPart plugin, or even convert
existing source code to the KDE framework.

%package kuiviewer
Summary: UI Files Viewer
Group: Development/KDE and QT
Provides: kuiviewer4
Requires: %name-core = %version-%release
%description kuiviewer
Displays Qt Designer UI files

%package scripts
Summary: Script From kdesdk
Group: Development/KDE and QT
BuildArch: noarch
#Requires: %name-core = %version-%release
%description scripts
This package contains the scripts for KDE development which are
contained in the %rname module.

%package kbugbuster
Summary: kbugbuster
Group: Development/KDE and QT
Provides: kbugbuster4
Requires: %name-core = %version-%release
%description kbugbuster
Kbugbuster

%package strigi-analyzer
Summary: Strigi Analyzer
Group: Development/KDE and QT
Requires: %name-common = %version-%release
%description strigi-analyzer
Strigi analyzer

%package po2xml
Summary: Xml2po and vice versa converters
Group: Development/KDE and QT
Requires: %name-common = %version-%release
%description po2xml
An xml2po and vice versa converters.

%package devel
Summary: Header files for %rname
Group: Development/KDE and QT
Requires: %name-common = %version-%release
Requires: kde4-kate-devel
%description devel
This package includes the header files you will need to compile
applications for %rname.

%package umbrello
Summary: UML Modeller
Group: Development/Tools
Requires: %name-core = %version-%release
%description umbrello
Umbrello UML Modeller is a UML diagramming tool for KDE.

%package cervisia
Summary: CVS client part
Group: Development/Tools
Requires: %name-common = %version-%release
%description cervisia
CVS client part.

%package kompare
Summary: KDE diff graphic tool
Group: Development/Tools
Requires: %name-core = %version-%release
%description kompare
kompare is a KDE diff graphic tool

%package kmtrace
Summary: Memory Allocation Debugging Tool
Group: Development/Tools
Requires: %name-core = %version-%release
%description kmtrace
Memory Allocation Debugging Tool

%package kcachegrind
Summary: KCachegrind
Group: Development/Tools
Requires: %name-core = %version-%release
%ifarch %ix86
Requires: valgrind
%endif
%description kcachegrind
KCachegrind is a visualisation tool for the profiling data generated by
Cachegrind and Calltree (they profile data file format is upwards compatible).
Calltree extends Cachegrind, which is part of Valgrind.

%package dolphin
Summary: Dolphin plugins for development
Group: Development/Tools
Requires: kde4base-dolphin
%description dolphin
Dolphin plugins for development

%package thumbnailers
Summary: Thumbnailers for various development files
Group: Development/Tools
Requires: kde4base-dolphin
%description thumbnailers
Thumbnailers for various development files

%package libs
Summary: %name core libraries
Group: System/Libraries
#Requires: %name-common = %version-%release
%description libs
%name core libraries

%package -n libkasten2controllers4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkasten2controllers4
%name library.

%package -n libkasten2core4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkasten2core4
%name library.

%package -n libkasten2gui4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkasten2gui4
%name library.

%package -n libkompareinterface4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkompareinterface4
%name library.

%package -n libktrace4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libktrace4
%name library.


%prep
%setup -q -n %rname-%version
#%patch1 -p1
%patch2 -p1
%patch3 -p1

# build only scripts and po2xml
rm -rf cervisia dolphin-plugins kapptemplate kcachegrind kde-dev-utils kdesdk-kioslaves \
 kdesdk-strigi-analyzers kdesdk-thumbnailers kompare lokalize okteta umbrello

%build
export PATH=%_kde4_bindir:$PATH
ls -d1 * | \
while read d
do
    [ -f "$d"/CMakeLists.txt ] || continue
    pushd $d
    %K4build \
	-DKDE4_BUILD_TESTS=OFF \
	-DBUILD_KF5=OFF \
	-DHUNSPELL_INCLUDE_DIR=%_includedir \
	-DHUNSPELL_LIBRARIES=%_libdir/libhunspell.so
    popd
done

%install
export PATH=%_kde4_bindir:$PATH

ls -d1 * | \
while read d
do
    [ -f "$d"/CMakeLists.txt ] || continue
    pushd $d
    %K4install
    popd
done

# fix scripts for strong /usr/lib/rpm/find-requires
pushd %buildroot/%_K4bindir
for f in `(file ./* | grep bash; file ./* | grep shell) | awk -F: '{print $1}' | xargs grep -l ^=head`
do
    mv "$f" "$f.tmp"
    awk 'BEGIN{found=0;} /^=head/ {if (found==0){print "cat <<\\__EOF__";found=1;};} {print} END{if (found!=0) print "__EOF__";}' <"$f.tmp" >"$f"
    rm -f "$f.tmp"
    chmod a+x $f
done
popd

# resilve conflict with subversion-tools
mv %buildroot/%_K4bindir/svn-clean %buildroot/%_K4bindir/svnclean




%files
%files common

%files scripts
%_K4bindir/adddebug
%_K4bindir/build-progress.sh
%_K4bindir/draw_lib_dependencies
%_K4bindir/cheatmake
%_K4bindir/colorsvn
%_K4bindir/create_cvsignore
%_K4bindir/create_makefile
%_K4bindir/create_makefiles
%_K4bindir/create_svnignore
%_K4bindir/cvs-clean
%_K4bindir/cvsaddcurrentdir
%_K4bindir/cvsbackport
%_K4bindir/cvsblame
%_K4bindir/cvscheck
%_K4bindir/cvsforwardport
%_K4bindir/cvslastchange
%_K4bindir/cvslastlog
%_K4bindir/cvsrevertlast
%_K4bindir/cvsversion
%_K4bindir/cxxmetric
%_K4bindir/extend_dmalloc
%_K4bindir/extractattr
%_K4bindir/extractrc
%_K4bindir/findmissingcrystal
%_K4bindir/fix-include.sh
%_K4bindir/fixkdeincludes
%_K4bindir/fixuifiles
%_K4bindir/includemocs
%_K4bindir/kde_generate_export_header
#_K4bindir/kde-systemsettings-tree.py
%_K4bindir/kdedoc
%_K4bindir/kdekillall
%_K4bindir/kdelnk2desktop.py
%_K4bindir/kdemangen.pl
%_K4bindir/krazy-licensecheck
%_K4bindir/makeobj
%_K4bindir/noncvslist
%_K4bindir/nonsvnlist
%_K4bindir/optimizegraphics
%_K4bindir/package_crystalsvg
%_K4bindir/png2mng.pl
%_K4bindir/pruneemptydirs
%_K4bindir/qtdoc
%_K4bindir/reviewboard-am
%_K4bindir/svnclean
%_K4bindir/svnbackport
%_K4bindir/svnchangesince
%_K4bindir/svnforwardport
%_K4bindir/svngettags
%_K4bindir/svnintegrate
%_K4bindir/svnlastchange
%_K4bindir/svnlastlog
%_K4bindir/svnrevertlast
%_K4bindir/svnversions
%_K4bindir/wcgrep
%_K4bindir/zonetab2pot.py

%files po2xml
%_K4bindir/po2xml
%_K4bindir/swappo
%_K4bindir/split2po
%_K4bindir/xml2pot


%changelog
* Fri Feb 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 15.12.2-alt4
- Disabled parts of kde4sdk depending on PyKDE4.

* Mon Jan 14 2019 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt3
- build only scripts and po2xml

* Mon Sep 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 15.12.2-alt2
- Patched struct2osd script to work with castxml.

* Mon Mar 14 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Mon Jan 25 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version
- temporary dont build kio-svn

* Tue Nov 17 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Thu Oct 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Tue Sep 15 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Wed Jun 10 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.1-alt2
- rebuild with new strigi

* Thu May 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.1-alt1
- new version

* Thu Apr 23 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.0-alt1
- new version

* Fri Mar 13 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.3-alt1
- new version

* Fri Jan 30 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.1-alt1
- new version

* Wed Oct 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.2-alt1
- new version

* Thu Sep 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.1-alt1
- new version

* Fri Aug 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Tue Jul 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.3-alt1
- new version

* Wed Jun 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.2-alt1
- new version

* Wed May 14 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.1-alt1
- new version

* Wed Apr 23 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Tue Apr 01 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.4-alt0.M70P.1
- built for M70P

* Mon Mar 31 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.4-alt1
- new version

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt0.M70P.1
- built for M70P

* Tue Mar 11 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt1
- new version

* Tue Feb 04 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt1
- new version

* Mon Jan 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.11.5-alt0.M70P.1
- built for M70P

* Mon Jan 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.11.5-alt1
- new version

* Tue Dec 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt0.M70P.1
- built for M70P

* Tue Dec 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt1
- new version

* Fri Nov 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt0.M70P.1
- built for M70P

* Fri Nov 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt0.M70P.1
- built for M70P

* Mon Sep 09 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Fri Jul 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt1
- new version

* Wed Jun 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.4-alt1
- new version

* Tue May 14 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.3-alt1
- new version

* Tue Apr 09 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt1
- new version

* Mon Mar 11 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt1
- new version

* Wed Dec 19 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Thu Oct 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt2
- build with antlr (ALT#27427); thanks viy@alt

* Thu Oct 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Fri Jun 22 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt0.M60P.1
- built for M60P

* Thu Jun 07 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Thu May 31 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt0.M60P.1
- built for M60P

* Thu May 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Thu Apr 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Thu Apr 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Tue Mar 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Fri Jan 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.7.1-alt1.1
- Rebuild with Python-2.7

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Wed Sep 14 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Wed Jul 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version

* Thu Jun 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Fri May 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Thu Apr 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Thu Mar 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version

* Tue Feb 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 4.5.3-alt1.1
- rebuilt with perl 5.12

* Wed Nov 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Thu Oct 07 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Tue Aug 31 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Mon Aug 09 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Mon Aug 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt2
- fix subpackages requires (ALT#23808)

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Tue May 11 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Tue Mar 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Thu Feb 11 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Mon Jan 25 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Tue Dec 03 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.3-alt1.1
- Rebuilt with python 2.6

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Thu Nov 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Tue Sep 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Wed Aug 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Mon Jul 20 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Mon Jun 08 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Tue May 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Mon Apr 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Thu Mar 05 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Wed Jan 28 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Tue Jan 20 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version
- removed deprecated macroses from specfile

* Fri Nov 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Wed Oct 08 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- new version

* Fri Sep 05 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt1
- new version

* Sat Aug 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt1
- new version

* Tue Jun 03 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.80-alt1
- 4.1 beta1

* Tue May 13 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.72-alt1
- new version

* Wed Apr 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.3-alt1
- new version

* Mon Mar 31 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt2
- fix to package main package

* Thu Mar 13 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt1
- built for ALT

