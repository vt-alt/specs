%define soname 28
Summary: Command-line tools and library for transforming PDF files
Name: qpdf
Version: 10.0.1
Release: alt1
License: Apache-2.0
Group: System/Base
Url: http://qpdf.sourceforge.net/
Source0: http://downloads.sourceforge.net/sourceforge/qpdf/qpdf-%version.tar
Source1: %name.watch
Patch0: %name-%version-%release.patch

BuildRequires: zlib-devel xml-utils xsltproc docbook-style-xsl
BuildRequires: pcre-devel
BuildRequires: libjpeg-devel

BuildRequires: perl-base

# for autoreconf
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gcc-c++

Requires: lib%name%soname = %EVR

%package -n lib%name%soname
Summary: QPDF library for transforming PDF files
Group: System/Libraries

%package -n lib%name-devel
Summary: Development files for QPDF library
Group: Development/C
Requires: lib%name%soname = %EVR

%package doc
Summary: QPDF Manual
Group: Documentation
BuildArch: noarch

%description
QPDF is a command-line program that does structural, content-preserving
transformations on PDF files. It could have been called something
like pdf-to-pdf. It includes support for merging and splitting PDFs
and to manipulate the list of pages in a PDF file. It is not a PDF viewer
or a program capable of converting PDF into other formats.

%description -n lib%name%soname
QPDF is a C++ library that inspect and manipulate the structure of PDF files.
It can encrypt and linearize files, expose the internals of a PDF file,
and do many other operations useful to PDF developers.

%description -n lib%name-devel
Header files and libraries necessary
for developing programs using the QPDF library.

%description doc
QPDF Manual

%prep
%setup
%patch0 -p1

%build
%autoreconf -fisv -I m4/

%configure --disable-static \
	   --enable-html-doc \
	   --disable-check-autofiles \
	   --with-docbook-xsl=%_datadir/xml/docbook/xsl-stylesheets \
           --enable-show-failed-test-output

%make

%install
%makeinstall


%files
%_bindir/fix-qdf
%_bindir/qpdf
%_bindir/zlib-flate
%_mandir/man1/*

%files -n lib%name%soname
%doc README.md TODO ChangeLog LICENSE.txt
%_libdir/libqpdf*.so.%{soname}*

%files -n lib%name-devel
%doc examples/*.cc examples/*.c
%_includedir/*
%_libdir/libqpdf*.so
%_libdir/pkgconfig/libqpdf.pc

%files doc
%doc doc/qpdf-manual.html doc/stylesheet.css

%changelog
* Mon Apr 13 2020 Anton Farygin <rider@altlinux.ru> 10.0.1-alt1
- 10.0.1

* Tue Jan 28 2020 Anton Farygin <rider@altlinux.ru> 9.1.1-alt1
- 9.1.1

* Tue Nov 19 2019 Anton Farygin <rider@altlinux.ru> 9.1.0-alt1
- 9.1.0

* Tue Oct 15 2019 Anton Farygin <rider@altlinux.ru> 9.0.2-alt1
- 9.0.2

* Sun Sep 22 2019 Anton Farygin <rider@altlinux.ru> 9.0.1-alt1
- 9.0.1

* Tue Sep 03 2019 Anton Farygin <rider@altlinux.ru> 9.0.0-alt1
- 9.0.0

* Wed May 22 2019 Anton Farygin <rider@altlinux.ru> 8.4.2-alt1
- 8.4.2

* Mon May 06 2019 Anton Farygin <rider@altlinux.ru> 8.4.1-alt1
- 8.4.1

* Wed Feb 06 2019 Anton Farygin <rider@altlinux.ru> 8.4.0-alt1
- 8.4.0

* Sat Jan 19 2019 Anton Farygin <rider@altlinux.ru> 8.3.0-alt1
- 8.3.0

* Sun Sep 02 2018 Anton Farygin <rider@altlinux.ru> 8.2.1-alt1
- 8.2.1

* Tue Jun 26 2018 Anton Farygin <rider@altlinux.ru> 8.1.0-alt1
- 8.1.0

* Sat Mar 31 2018 Anton Farygin <rider@altlinux.ru> 8.0.2-alt1
- new version

* Fri Mar 02 2018 Anton Farygin <rider@altlinux.ru> 8.0.0-alt1
- new version
- library package renamed to match the shared libs policy

* Mon Feb 26 2018 Anton Farygin <rider@altlinux.ru> 7.1.1-alt1
- new version

* Mon Jan 29 2018 Anton Farygin <rider@altlinux.ru> 7.1.0-alt1
- new version

* Mon Sep 18 2017 Anton Farygin <rider@altlinux.ru> 7.0.0-alt1
- new version

* Tue May 10 2016 Anton Farygin <rider@altlinux.ru> 6.0.0-alt1
- new version

* Thu May 28 2015 Anton Farygin <rider@altlinux.ru> 5.1.3-alt1
- new version

* Mon Jun 16 2014 Anton Farygin <rider@altlinux.ru> 5.1.2-alt1
- new version

* Wed Feb 19 2014 Anton Farygin <rider@altlinux.ru> 5.1.1-alt1
- new version

* Fri Dec 27 2013 Anton Farygin <rider@altlinux.ru> 5.1.0-alt1
- new version

* Thu Oct 24 2013 Anton Farygin <rider@altlinux.ru> 5.0.1-alt1
- new version

* Fri Oct 11 2013 Anton Farygin <rider@altlinux.ru> 5.0.0-alt1
- new version

* Tue Sep 18 2012 Anton Farygin <rider@altlinux.ru> 3.0.2-alt1
- first build for Sisyphus
