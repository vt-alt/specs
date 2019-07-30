%define _unpackaged_files_terminate_build 1

Name: labplot
Version: 2.5.0
Release: alt3

Summary: Function and Data Plotter
License: GPL
Group: Sciences/Other

Url: https://labplot.kde.org/
# git://anongit.kde.org/labplot
Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: ccmake gcc-c++ extra-cmake-modules
BuildRequires: qt5-base-devel qt5-svg-devel 
BuildRequires: kf5-karchive-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kdoctools-devel kf5-ki18n-devel kf5-kiconthemes-devel
BuildRequires: kf5-kdelibs4support-devel kf5-kio-devel kf5-knewstuff-devel kf5-ktextwidgets-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kxmlgui-devel
BuildRequires: libXScrnSaver-devel libXau-devel libXcomposite-devel
BuildRequires: libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel
BuildRequires: libXtst-devel libXv-devel libXxf86misc-devel 
BuildRequires: libgsl-devel libhdf5-devel libnetcdf-devel
BuildRequires: libxkbfile-devel xorg-xf86vidmodeproto-devel
BuildRequires: qt5-serialport-devel
BuildRequires: kf5-syntax-highlighting-devel 

Conflicts: labplot1.6
Requires: ImageMagick-tools gsl pstoedit

%description
This is a program for plotting of functions and data manipulation.

A versatile spreadsheet for data import and editing was added.
Also a better 3 dimensional plot with rotation and colormaps is available.
Newly supported are data set operations and image manipulations. One can now
import over 80 different images formats and export directly to ps, eps or pdf.
The plots now use double buffering and LabPlot supports scripting using QSA.

%prep
%setup
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -name '*.cpp' -o -name '*.h' | xargs sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%K5build \
    -DINCLUDE_INSTALL_DIR=%_K5inc \
    -DLIBEXEC_INSTALL_DIR=%_K5exec \
    -DDATA_INSTALL_DIR=%_K5data

%install
%K5install
%find_lang %name --with-kde

%files -f %name.lang
%doc AUTHORS README COPYING ChangeLog
%config(noreplace) %_K5xdgconf/*.knsrc
%_K5bin/*
%_K5data/%{name}2/
%_K5xdgapp/*
%_K5icon/hicolor/*/apps/*
%_K5xmlgui/%{name}2/
%_K5xdgmime/%{name}2.xml
%_K5doc/*/%{name}2/
%_datadir/metainfo/*.xml

%changelog
* Thu May 23 2019 Michael Shigorin <mike@altlinux.org> 2.5.0-alt3
- E2K: strip UTF-8 BOM for lcc < 1.24
- minor spec cleanup

* Mon Oct 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.0-alt2
- Updated runtime dependencies.

* Mon Aug 29 2018 Pavel Moseev <mars@altlinux.org> 2.5.0-alt1
- Updated to upstream version 2.5.0.

* Mon Aug 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.0-alt1
- Updated to upstream version 2.4.0.
- Rebuilt with qt5 and kde5.
- Cleaned up spec.

* Thu May 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.svn20140201
- Version 2.0.1

* Wed Nov 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt8.beta1.svn20131107
- Version 2.0.0.beta1

* Tue Jul 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt7.svn20090921
- Rebuilt with new libhdf5

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt6.svn20090921
- Rebuilt with libhdf5-7-seq 1.8.8-alt2

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt5.svn20090921
- Fixed build

* Thu Sep 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.8
- Rebuilt with libhdf5-7

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.7
- Rebuilt with libnetcdf7

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.6
- Rebuilt for debuginfo

* Mon Feb 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.5
- Fixed build

* Tue Nov 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.4
- Rebuilt for soname set-versions

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.3
- Built without system liborigin

* Tue Jul 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.2
- Rebuilt with Qt 4.7

* Tue Nov 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.1
- Rebuilt with gsl 1.13-alt1

* Thu Nov 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921
- New snapshot
- Added SciDAvis (experimental Qt frontend)

* Wed Jun 03 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2
- rebuild with libnetcdf-4.0.1

* Mon Jan 05 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version (2.0.0)
- build with libnetcdf-4.0

* Mon Jan 05 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.0.2-alt1
- new version (1.6.0.2)

* Tue Oct 04 2005 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt0.4
- new version

* Mon Dec 27 2004 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version

* Mon Nov 08 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- release

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.1-alt0.1pre2.1
- Rebuilt with libtiff.so.4.

* Sat Jul 31 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt0.1pre2
- new version
- add russian translation

* Sat Jun 19 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- first build for Sisyphus

