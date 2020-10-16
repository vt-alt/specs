Name: libjasper
Version: 2.0.22
Release: alt1

Summary: Implementation of the codec specified in the JPEG-2000 Part-1 standard
Summary(ru_RU.UTF8): Реализация кодеков по спецификации стандарта JPEG-2000, часть I

License: Modified BSD
Group: System/Libraries
Url: http://www.ece.uvic.ca/~mdadams/jasper/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/mdadams/jasper/archive/version-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake imake libGL-devel libXext-devel libXi-devel libXmu-devel libglut-devel libjpeg-devel

%description
JasPer is a collection
of software (i.e., a library and application programs) for the coding
and manipulation of images.  This software can handle image data in a
variety of formats.  One such format supported by JasPer is the JPEG-2000
format defined in ISO/IEC 15444-1:2000.

%package devel
Summary: Include Files for %name
Group: Development/C
Requires: %name = %version

%description devel
Libraries/include files for development with %name.

%package devel-doc
Summary: Documentation for %name
Group: Development/C
Requires: %name-devel-doc = %version-%release
BuildArch: noarch

%description devel-doc
Documentation for development with %name.

%package -n jasper
Summary: JasPer utilities
Group: Graphics
Requires: %name = %version-%release

%description -n jasper
JasPer is a collection
of software (i.e., a library and application programs) for the coding
and manipulation of images.  This software can handle image data in a
variety of formats.  One such format supported by JasPer is the JPEG-2000
code stream format defined in ISO/IEC 15444-1:2000.

%prep
%setup

%build
# TODO: -DJAS_ENABLE_HIDDEN=true
%cmake -DJAS_ENABLE_AUTOMATIC_DEPENDENCIES=OFF
%cmake_build

%install
%cmakeinstall_std

%files
%doc README LICENSE
%_libdir/lib*.so.*

%files -n jasper
%_bindir/*
%_man1dir/*

%files devel
%_includedir/jasper/
%_libdir/libjasper.so
%_pkgconfigdir/jasper.pc

%files devel-doc
%doc %_docdir/JasPer/

%changelog
* Thu Oct 08 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.22-alt1
- new version 2.0.22 (with rpmrb script)
- add -DJAS_ENABLE_AUTOMATIC_DEPENDENCIES=OFF
- upstream changes:
 + remove JPEG dummy codec
 + fix OpenGL/glut detection

* Thu Oct 08 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.21-alt1
- new version 2.0.21 (with rpmrb script)
- ZDI-15-529, CVE-2018-19541

* Thu Oct 08 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.20-alt1
- new version 2.0.20 (with rpmrb script)
- upstream changes:
 + fix several ISO/IEC 15444-4 conformance bugs
 + disable the MIF codec by default for security reasons
- CVE-2016-9398

* Wed Sep 02 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.19-alt1
- new version 2.0.19 (with rpmrb script)
- CVE-2018-9154, CVE-2018-19541, CVE-2016-9399, CVE-2017-13751
- CVE-2018-19540, CVE-2018-9055, CVE-2017-13748
- CVE-2017-5503, CVE-2017-5504, CVE-2017-5505
- CVE-2018-9252, CVE-2018-19139, CVE-2018-19543, CVE-2017-9782
- CVE-2018-20570, CVE-2018-20622, CVE-2016-9398, CVE-2017-14132
- CVE-2017-5499, CVE-2018-18873, CVE-2017-13750

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 2.0.16-alt1
- new version 2.0.16 (switched to github tarball)

* Sun Jun 24 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.14-alt1
- new version, use cmake, pack devel-doc

* Tue Dec 20 2016 Vitaly Lipatov <lav@altlinux.ru> 1.900.13-alt1
- new version 1.900.13 (with rpmrb script)
- drop all packages (incorporated)

* Thu Feb 06 2014 Vitaly Lipatov <lav@altlinux.ru> 1.900.1-alt3
- add patches against multiple security vulnerabilities (ALT bug #29241)
- add pkg-config file
- thanks, Fedora!

* Wed Mar 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.900.1-alt2.qa2
- rebuild for debuginfo

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.900.1-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Nov 18 2009 Vitaly Lipatov <lav@altlinux.ru> 1.900.1-alt2
- cleanup spec, update buildreqs, pack man pages

* Sat May 12 2007 Vitaly Lipatov <lav@altlinux.ru> 1.900.1-alt1
- new version 1.900.1 (with rpmrb script)

* Mon Dec 25 2006 Vitaly Lipatov <lav@altlinux.ru> 1.900.0-alt0.1
- new version 1.900.0 (with rpmrb script)
- pack include/jasper (fix bug 10510)
- update buildreq

* Tue Apr 26 2005 Vitaly Lipatov <lav@altlinux.ru> 1.701.0-alt2
- fix postun script (fix bug #6639)
- fix summary

* Sun Dec 26 2004 Vitaly Lipatov <lav@altlinux.ru> 1.701.0-alt1
- first build for ALT Linux Sisyphus

* Fri Oct 25 2002 Alexander D. Karaivanov <adk@medical-insight.com>
- spec file created
