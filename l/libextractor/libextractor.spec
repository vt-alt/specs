%def_disable snapshot
%def_enable ffmpeg
# test_rpm failed
%def_disable check

Name: libextractor
Version: 1.9
Release: alt2

Summary: libextractor is a simple library for keyword extraction

Group: System/Libraries
License: GPLv2+
Url: http://www.gnu.org/software/%name/

%if_disabled snapshot
Source: ftp://ftp.gnu.org/gnu/%name/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Patch: %name-1.9-up-exiv2-0.27.patch

%define flac_ver 1.3

BuildRequires: gcc-c++ zlib-devel bzlib-devel glib2-devel libexiv2-devel libflac-devel >= %flac_ver
BuildRequires: libgsf-devel libltdl7-devel libgtk+3-devel
BuildRequires: libmpeg2-devel libtiff-devel libmp4v2-devel libqt4-devel librpm-devel
BuildRequires: libopus-devel libvorbis-devel libflac-devel
BuildRequires: iso-codes-devel libgif-devel libarchive-devel libtidy-devel
# requires libjpeg-8 API (jpeg_mem_src()) -- plugin disabled
BuildRequires: libjpeg-devel gst-plugins1.0-devel
%if_enabled ffmpeg
BuildRequires: libavcodec-devel libavutil-devel
BuildRequires: libavformat-devel libavresample-devel libswscale-devel
%endif
BuildRequires: makeinfo

%description
libextractor is a simple library for keyword extraction.
libextractor does not support all formats but supports a simple plugging
mechanism such that you can quickly add extractors for additional
formats, even without recompiling libextractor. libextractor typically
ships with a dozen helper-libraries that can be used to obtain keywords
from common file-types.

%package -n extract
Summary: extract is a simple command-line interface to libextractor
Group: File tools
Requires: %name = %version-%release

%description -n extract
libextractor is a simple library for keyword extraction.
This package privides the extract is a simple command-line interface to
libextractor.

%package devel
Summary: %name development files and libraries
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the files needed to build packages that depend on %name.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure --disable-static \
	%{subst_enable ffmpeg}
%make_build

%install
%makeinstall_std

# remove non-packaged files
rm -f %buildroot%_libdir/%name/*.la

%find_lang %name

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
export LIBEXTRACTOR_PREFIX=%buildroot%_libdir
# some tests failed in hasher -- need to investigate
%make check

%files -f %name.lang
%_libdir/*.so.*
%dir %_libdir/%name
%_libdir/%name/*.so
%doc AUTHORS README NEWS TODO

%files -n extract
%_bindir/extract
%_man1dir/*

%files devel
%_includedir/*
%_infodir/*
%_pkgconfigdir/*
%_libdir/*.so
%_man3dir/*

%changelog
* Sun Aug 11 2019 Yuri N. Sedunov <aris@altlinux.org> 1.9-alt2
- rebuilt against libexiv2.so.27

* Tue Feb 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1.9-alt1
- 1.9

* Wed Nov 28 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8-alt1
- 1.8

* Fri Jul 13 2018 Yuri N. Sedunov <aris@altlinux.org> 1.7-alt1
- 1.7

* Tue Oct 17 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6-alt1
- 1.6

* Wed Jun 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt1
- 1.4

* Tue Jun 06 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt3
- rebuilt against libexiv2.so.26

* Mon Nov 30 2015 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt2.1
- buildreqs: added makeinfo

* Mon Jun 29 2015 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt2
- rebuilt against libexiv2.so.14

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.3-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Jul 08 2014 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt1
- 1.3

* Thu Dec 05 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2-alt1
- 1.2

* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt3
- rebuilt against libexiv2.so.13

* Fri Mar 15 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt2
- rebuilt against libarchive.so.13

* Mon Jan 28 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1
- removed old hack&tricks, packager tag
- updated buildreqs

* Sun Jan 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt1
- Friendly NMU: new version

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.23-alt3.qa3
- Removed bad RPATH

* Thu Nov 03 2011 Michael Shigorin <mike@altlinux.org> 0.5.23-alt3.qa2
- rebuild with libexiv2 0.22

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.5.23-alt3.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Tue Jun 08 2010 Victor Forsiuk <force@altlinux.org> 0.5.23-alt3
- rebuild with libexiv2 0.20

* Wed Jan 06 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5.23-alt2
- rebuild with libexiv2 0.19

* Wed Nov 18 2009 Vitaly Lipatov <lav@altlinux.ru> 0.5.23-alt1
- new version 0.5.23 (with rpmrb script)
- update buildreqs

* Tue Apr 28 2009 Vitaly Lipatov <lav@altlinux.ru> 0.5.22-alt1
- new version 0.5.22 (with rpmrb script)

* Sat May 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.5.20b-alt1
- new version 0.5.20b (with rpmrb script)

* Thu Oct 11 2007 Vitaly Lipatov <lav@altlinux.ru> 0.5.18a-alt1
- new version 0.5.18a (with rpmrb script)

* Wed Jul 18 2007 Vitaly Lipatov <lav@altlinux.ru> 0.5.18-alt1
- new version 0.5.18 (with rpmrb script)

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.16-alt0.1
- new version 0.5.16
- remove fix links patch, update buildreq (add gtk)

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.15-alt0.1
- new version 0.5.15
- fix links

* Sun Apr 30 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.13-alt0.1
- new version 0.5.13 (with rpmrb script)

* Mon Feb 20 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.10-alt0.1
- new version (0.5.10)

* Sat Jan 07 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.9-alt1
- new version

* Sun Dec 18 2005 Vitaly Lipatov <lav@altlinux.ru> 0.5.7-alt1
- new version

* Thu Nov 17 2005 Vitaly Lipatov <lav@altlinux.ru> 0.5.6-alt1
- NMU: new version
- add lib/libextractor dir

* Thu Sep 15 2005 Anton Farygin <rider@altlinux.ru> 0.4.2-alt1.2
- rebuild with libMagick.so.9

* Mon Sep 12 2005 Anton Farygin <rider@altlinux.ru> 0.4.2-alt1.1
- rebuild with new libImageMagick

* Thu Mar 17 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Sun Jan 16 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.4.0-alt2
- fixed OLE plugin build.

* Sun Jan 16 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.4.0-alt1
- 0.4.0.

* Fri Sep 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3.7-alt1
- 0.3.7

* Wed Jun 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Tue Jun 01 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3.2-alt0.5
- 0.3.2

* Tue Apr 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt0.5
- 0.3.0
- plugins moved to separate directory.

* Wed Dec 17 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.6-alt0.6
- do not package .la files.

* Sat Nov 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.6-alt0.5
- First build for Sisyphus.
