Name: libxml2
Version: 2.9.10
Release: alt6
Epoch: 1

Summary: The library for manipulating XML files
License: MIT
Group: System/Libraries
Url: http://xmlsoft.org/

%def_with python3
%def_disable static
%define srcname %name-%version

Source: %srcname.tar
# https://www.w3.org/XML/Test/xmlts20130923.tar.gz
Source1: xmlts.tar
Patch: %name-%version-%release.patch

Requires: xml-common

# Automatically added by buildreq on Sun Feb 27 2011
BuildRequires: liblzma-devel python-devel python-modules-compiler python-modules-xml zlib-devel

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%package devel
Summary: Development environment for building applications manipulating XML files
Group: Development/C
Requires: %name = %EVR

%package devel-static
Summary: Static library for building applications manipulating XML files
Group: Development/C
Requires: %name-devel = %EVR

%package -n xml-utils
Summary: Various XML utilities
Group: Text tools
Requires: %name = %EVR
Provides: xmllint = %epoch:%version
Obsoletes: xmllint < %epoch:%version

%package -n python-module-%name
Summary: Python bindings for the %name library
Group: Development/Python
Requires: %name = %EVR
Provides: libxml2-python = %epoch:%version, python-modules-%name = %epoch:%version
Obsoletes: libxml2-python < %epoch:%version, python-modules-%name < %epoch:%version

%package -n python3-module-%name
Summary: Python3 bindings for the %name library
Group: Development/Python3
Requires: %name = %EVR

%package doc
Summary: Documentation for the %name library
Group: Development/C
Conflicts: %name < %epoch:%version, %name > %epoch:%version
BuildArch: noarch

%description
This library allows to manipulate XML files.  It includes support
to read, modify and write XML and HTML files.  There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified.  The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select subnodes or ranges.  A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

This package contains the shared library required to run
applications manipulating XML files.

%description devel
This library allows to manipulate XML files.  It includes support
to read, modify and write XML and HTML files.  There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified.  The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select subnodes or ranges.  A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

This package contains the libraries, include and other files
you can use to develop applications manipulating XML files.

%description devel-static
This library allows to manipulate XML files.  It includes support
to read, modify and write XML and HTML files.  There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified.  The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select subnodes or ranges.  A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

This package contains the static library you can use to develop
statically linked applications manipulating XML files.

%description -n xml-utils
This package contains xml tools:
+ xmllint - utility for parsing and validating XML files;
+ xmlcatalog - command line tool to parse and manipulate XML or SGML
catalog files.

%description -n python-module-%name
This package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the %name library to manipulate XML files.

This library allows to manipulate XML files.  It includes support
to read, modify and write XML and HTML files.  There is DTDs support
this includes parsing and validation even with complex DTDs, either
at parse time or later once the document has been modified.

%description -n python3-module-%name
This package contains a module that permits applications
written in the Python3 programming language to use the interface
supplied by the %name library to manipulate XML files.

This library allows to manipulate XML files.  It includes support
to read, modify and write XML and HTML files.  There is DTDs support
this includes parsing and validation even with complex DTDs, either
at parse time or later once the document has been modified.

%description doc
This package contains documentation on the XML C library.

%prep
%setup -n %srcname -a1
%patch -p1

%build
export ac_cv_path_WGET=/usr/bin/wget
export ac_cv_path_XMLLINT=/usr/bin/xmllint
export ac_cv_path_XSLTPROC=/usr/bin/xsltproc
# disable dependency on binutils-devel
export ac_cv_header_ansidecl_h=no
mkdir -p m4
%autoreconf

mkdir build
cd build
ln -s ../xmlconf
%define _configure_script ../configure

%configure \
    --with-python=%_bindir/python2 \
    --with-python-install-dir=%python_sitelibdir \
    --with-html-dir=%_docdir \
    --with-html-subdir=%name-%version \
    %{subst_enable static} \
    --disable-silent-rules
%make_build DOC_MODULE=%name-%version

%if_with python3
mkdir ../python3
cd ../python3
%configure \
	--with-python=%_bindir/python3 \
	--with-python-install-dir=%python3_sitelibdir \
	--with-html-dir=%_docdir \
	--with-html-subdir=%name-%version \
	--disable-static \
	--disable-silent-rules
cp -la ../build/{*.la,.libs} .
%make_build -C python
%endif

%check
%make_build DOC_MODULE=%name-%version -k check -C build

%install
%makeinstall_std DOC_MODULE=%name-%version -C build
%if_with python3
%makeinstall_std -C python3/python
rm %buildroot%python3_sitelibdir/*.la
%endif

mv %buildroot%_datadir/aclocal/libxml{,2}.m4

%define pkgdocdir %_docdir/%name-%version
install -p -m644 AUTHORS Copyright NEWS README %buildroot%pkgdocdir/
install -p -m644 doc/*.html %buildroot%pkgdocdir/

%files
%_libdir/*.so.*
%dir %pkgdocdir
%pkgdocdir/AUTHORS
%pkgdocdir/Copyright
%pkgdocdir/NEWS
%pkgdocdir/README

%files -n xml-utils
%_bindir/xmllint
%_bindir/xmlcatalog
%_man1dir/xmllint.*
%_man1dir/xmlcatalog.*

%files devel
%_bindir/*-config
%_libdir/*.so
%_libdir/*.sh
%_includedir/*
%_pkgconfigdir/*
%_libdir/cmake/*
%_aclocaldir/*
%_man1dir/*-config*
%_man3dir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif	#enabled static

%files -n python-module-%name
%python_sitelibdir/*
%dir %pkgdocdir
%dir %pkgdocdir/python
%pkgdocdir/python/TODO
%pkgdocdir/python/examples

%if_with python3
%files -n python3-module-%name
%python3_sitelibdir/*.*
%python3_sitelibdir/__pycache__/*
%endif

%files doc
%dir %pkgdocdir
%pkgdocdir/*.html
%pkgdocdir/*.gif
%pkgdocdir/*.png
%pkgdocdir/*.xml
%pkgdocdir/*.xsl
%pkgdocdir/*.c
%pkgdocdir/*.res
%pkgdocdir/html
%pkgdocdir/examples
%pkgdocdir/tutorial
%doc %_datadir/gtk-doc/html/libxml2/

%changelog
* Sun Feb 14 2021 Ivan A. Melnikov <iv@altlinux.org> 1:2.9.10-alt6
- Address upstream #132 by cherry-picking the fix from master; see:
  + https://gitlab.gnome.org/GNOME/libxml2/-/issues/132
  + https://github.com/shlomif/perl-XML-LibXSLT/issues/2

* Wed Jan 27 2021 Grigory Ustinov <grenka@altlinux.org> 1:2.9.10-alt5
- Add patch for python3.9 support.

* Fri Nov 06 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.9.10-alt4
- Applied security fixes from upstream (Fixes: CVE-2019-20388, CVE-2020-7595,
  CVE-2020-24977).

* Mon Dec 23 2019 Ivan A. Melnikov <iv@altlinux.org> 1:2.9.10-alt3
- Fix building without python-base.

* Sat Nov 02 2019 Dmitry V. Levin <ldv@altlinux.org> 1:2.9.10-alt2
- xml2-config: fixed regressions introduced in v2.9.10.

* Fri Nov 01 2019 Alexey Shabalin <shaba@altlinux.org> 1:2.9.10-alt1
- Updated to v2.9.10

* Wed May 22 2019 Alexey Shabalin <shaba@altlinux.org> 1:2.9.9.0.52.f824-alt1
- v2.9.4-12-ge905f08 -> v2.9.9-52-gf824a4bd
  (fixes: CVE-2017-9047, CVE-2017-9048, CVE-2017-9049, CVE-2017-9050,
  CVE-2017-5969, CVE-2018-14404, CVE-2018-9251, CVE-2018-14567).

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.9.4.0.12.e905-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Mar 03 2017 Dmitry V. Levin <ldv@altlinux.org> 1:2.9.4.0.12.e905-alt1
- v2.9.3-5-g65112cb -> v2.9.4-12-ge905f08
  (fixes: CVE-2016-1833, CVE-2016-1834, CVE-2016-1835, CVE-2016-1836,
  CVE-2016-1837, CVE-2016-1838, CVE-2016-1839, CVE-2016-1840,
  CVE-2016-3627, CVE-2016-3705, CVE-2016-4449, CVE-2016-4483,
  CVE-2016-4658, CVE-2016-5131).

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:2.9.3.0.5.6511-alt1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:2.9.3.0.5.6511-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Mar 11 2016 Dmitry V. Levin <ldv@altlinux.org> 1:2.9.3.0.5.6511-alt1
- v2.9.3 -> v2.9.3-5-g65112cb.

* Fri Nov 20 2015 Dmitry V. Levin <ldv@altlinux.org> 1:2.9.3-alt1
- Updated to v2.9.3.

* Wed Nov 12 2014 Dmitry V. Levin <ldv@altlinux.org> 1:2.9.2-alt1
- Updated to v2.9.2-5-g7580ce0 (closes: #30267).
- Built and packaged python3-module-%name.

* Wed Mar 27 2013 Dmitry V. Levin <ldv@altlinux.org> 1:2.9.0-alt1
- Updated to v2.9.0-42-gf7aeda2.

* Tue Jul 17 2012 Dmitry V. Levin <ldv@altlinux.org> 1:2.8.0-alt1
- Updated to v2.8.0-3-g549f06a.
- Unexported 13 internal functions which are not supposed to be exported.

* Thu Feb 09 2012 Dmitry V. Levin <ldv@altlinux.org> 1:2.7.8-alt8
- Updated to v2.7.8-48-gca03efc.

* Thu Jan 12 2012 Dmitry V. Levin <ldv@altlinux.org> 1:2.7.8-alt7
- Updated to v2.7.8-41-g81809d5.
- tests: added w3.org xmlts testsuite for runxmlconf.

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:2.7.8-alt6.1
- Rebuild with Python-2.7

* Mon Apr 25 2011 Dmitry V. Levin <ldv@altlinux.org> 1:2.7.8-alt6
- Updated to v2.7.8-15-gd7958b2.

* Sun Feb 27 2011 Alexey Tourbin <at@altlinux.ru> 1:2.7.8-alt5
- Disabled dependency on zlib-devel.

* Mon Feb 07 2011 Alexey Tourbin <at@altlinux.ru> 1:2.7.8-alt4.1
- Rebuilt for debuginfo.

* Wed Jan 12 2011 Dmitry V. Levin <ldv@altlinux.org> 1:2.7.8-alt4
- Fixed structured error handlers interoperability regression introduced
  between 2.7.3 and 2.7.4 libxml2 releases (closes: #24379).

* Mon Dec 27 2010 Dmitry V. Levin <ldv@altlinux.org> 1:2.7.8-alt3
- Updated to v2.7.8-7-gfec31bc (fixes CVE-2010-4494).

* Wed Dec 15 2010 Dmitry V. Levin <ldv@altlinux.org> 1:2.7.8-alt2
- Build without libbfd-devel.

* Fri Nov 05 2010 Dmitry V. Levin <ldv@altlinux.org> 1:2.7.8-alt1
- Updated to v2.7.8-1-g0081987.

* Thu Oct 07 2010 Alexey Tourbin <at@altlinux.ru> 1:2.7.7-alt1
- 2.7.3 -> v2.7.7-11-gd2190fa
- libxml2.lds: fixup transition to upstream ABI versioning

* Fri Nov 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.7.3-alt2.1
- Rebuilt with python 2.6

* Mon Aug 17 2009 Dmitry V. Levin <ldv@altlinux.org> 1:2.7.3-alt2
- Applied FICORA #245608 patches for CVE-2009-2414 and CVE-2009-2416.
- xmlversion.h: Removed ATTRIBUTE_PRINTF redefinition.
- Fixed some compiler warnings.

* Sat Mar 07 2009 Alexey Tourbin <at@altlinux.ru> 1:2.7.3-alt1
- 2.7.2+svn3803 -> 2.7.3

* Tue Nov 25 2008 Alexey Tourbin <at@altlinux.ru> 1:2.7.2-alt2
- updated to svn revision 3803 (fixes CVE-2008-4225, CVE-2008-4226)

* Tue Oct 07 2008 Alexey Tourbin <at@altlinux.ru> 1:2.7.2-alt1
- 2.6.32 -> 2.7.2
- made libxml2-doc subpackage noarch

* Mon Sep 01 2008 Alexey Tourbin <at@altlinux.ru> 1:2.6.32-alt3
- upstream update for CVE-2008-3281 to avoid ABI issues

* Thu Aug 21 2008 Alexey Tourbin <at@altlinux.ru> 1:2.6.32-alt2
- applied upstream fix for recursive evaluation of entities (CVE-2008-3281)

* Tue Apr 22 2008 Alexey Tourbin <at@altlinux.ru> 1:2.6.32-alt1
- 2.6.31 -> 2.6.32

* Sat Feb 09 2008 Grigory Batalov <bga@altlinux.ru> 1:2.6.31-alt1.1
- Rebuilt with python-2.5.

* Mon Jan 14 2008 Alexey Tourbin <at@altlinux.ru> 1:2.6.31-alt1
- 2.6.30+svn3661 -> 2.6.31 (fixes CVE-2007-6284)

* Fri Oct 26 2007 Alexey Tourbin <at@altlinux.ru> 1:2.6.30-alt2
- 2.6.30+svn3659 -> 2.6.30+svn3661 (20071016)
- python-module-libxml2: removed manual dependency on python

* Tue Oct 02 2007 Alexey Tourbin <at@altlinux.ru> 1:2.6.30-alt1
- 2.6.29+svn3647 -> 2.6.30+svn3659 (20070904)

* Sun Aug 05 2007 Alexey Tourbin <at@altlinux.ru> 1:2.6.29-alt2
- 2.6.29+svn3644 -> 2.6.29+svn3647 (20070801)
- enabled 'make check' by default, except for W3C XML Schema tests

* Thu Jul 19 2007 Alexey Tourbin <at@altlinux.ru> 1:2.6.29-alt1
- updated to svn revision 3644 (20070718)
- changed src.rpm packaging to keep separate tarball with svn snapshot

* Thu Apr 19 2007 Alexey Tourbin <at@altlinux.ru> 1:2.6.28-alt1
- updated to 2.6.28 release
- linked libxml2mod.so python module with libpython

* Sun Mar 18 2007 Alexey Tourbin <at@altlinux.ru> 1:2.6.27-alt4
- updated to svn revision 3591 (20070314)
- renamed python-modules-libxml2 package to python-module-libxml2,
  to match python policy

* Tue Feb 20 2007 Alexey Tourbin <at@altlinux.ru> 1:2.6.27-alt3
- updated to svn revision 3586 (20070216)

* Sun Jan 07 2007 Alexey Tourbin <at@altlinux.ru> 1:2.6.27-alt2
- updated to 20061214 cvs snapshot

* Mon Oct 30 2006 Alexey Tourbin <at@altlinux.ru> 1:2.6.27-alt1
- 2.6.26 -> 2.6.27+
- imported cvs sources into git and built with gear
- introduced symbol versioning for the shared library, starting with
  2.6.13 release (LIBXML2_2.6.13, LIBXML2_2.6.14, ..., LIBXML2_2.6.27)
- removed libxml.so.2 provides and symlink
- ChangeLog not packaged, NEWS is just good enough

* Sun Jun 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.26-alt2
- Patch2: unescape file URIs for I/O, leave others intact

* Thu Jun 08 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.26-alt1
- Release 2.6.26
- Patch1: in libxml-2.0.pc, move internally used libraries to Libs.private
  (bug 9448)
- Patch2 has gone upstream

* Thu Jun 01 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.24-alt1
- Release 2.6.24
- Patch1 went upstream
- Patch2: fix a typo in configure

* Tue Apr 18 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.23-alt2
- Patch1: honor --nonet when --postvalid is given (GNOME bug 337483)

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1:2.6.23-alt1.1
- Rebuilt for new pkg-config dependencies.

* Sun Jan 08 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.23-alt1
- 2.6.23

* Thu Sep 15 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.22-alt1
- 2.6.22
- Added gtk-doc files to the doc package
- buildreq

* Mon Sep 05 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.21-alt1
- New upstream release

* Tue Jul 12 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.20-alt1
- New upstream release

* Tue Apr 05 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.19-alt1
- New upstream release

* Mon Mar 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.18-alt1
- New upstream release
- Built with new Python

* Mon Jan 17 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.17-alt1
- New upstream release

* Thu Dec 16 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.16-alt2
- Fixed docs install
- Patch0 considered harmful

* Thu Nov 11 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.16-alt1
- New upstream release

* Sun Oct 31 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.15-alt1
- New upstream release
- Patch1 is obsolete

* Wed Oct 27 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.14-alt2
- Fixes for buffer overflows from SuSE, provided by LDV [Patch1]

* Fri Oct 01 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.14-alt1
- New upstream release

* Mon Sep 20 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.13-alt1
- New upstream release

* Tue Aug 24 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.12-alt1
- New upstream release
- Grouped xml-utils under 'Text tools'

* Thu Jul 15 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.11-alt2
- Python package renamed to comply with the New Policy

* Thu Jul 08 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.11-alt1
- New upstream release

* Mon Apr 19 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.9-alt1
- New upstream release

* Sun Mar 28 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.8-alt1
- New upstream release

* Tue Feb 24 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.7-alt1
- New upstream release

* Fri Feb 13 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.6-alt1
- New upstream release
- Patch1 gone upstream

* Wed Feb 04 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.5-alt2
- Patch from CVS to prevent an XInclude-related crash in the XML::LibXML
  test suite and elsewhere (GNOME bug #133106) [Patch1]

* Tue Jan 27 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.5-alt1
- New upstream release
- Patch1 gone upstream
- Disable check because test target is broken

* Wed Jan 21 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.4-alt3
- Buildreq against Python 2.3

* Thu Jan 01 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.4-alt2
- Fix XInclude bugs [Patch1]
- buildreq

* Wed Dec 31 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.4-alt1
- New upstream release
- Patch1 gone upstream
- Happy New Year :)

* Thu Dec 25 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.3-alt2
- CVS patch to fix an XInclude problem (GNOME bug #129932) [Patch1]

* Thu Dec 11 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.3-alt1
- New upstream release
- Patch1 is obsolete
- Patch2 gone upstream

* Thu Dec 11 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.2-alt3
- Bugfix from CVS for Gnome Bugzilla bug #126817 [Patch2]

* Thu Nov 27 2003 Alexey Tourbin <at@altlinux.ru> 1:2.6.2-alt2
- Do not package .la files.

* Mon Nov 10 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.6.2-alt1
- Updated to 2.6.2
- Make the tests pass [Patch1]

* Tue Sep 16 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.5.11-alt1
- Upstream release 2.5.11

* Mon Aug 18 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.5.10-alt1
- New version
- Eliminated duplication of doc files

* Sat Jul 12 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.5.8-alt1
- New version

* Sat Jun 21 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.5.7-alt2
- Fixed up the anachronistic aclocal m4 file, by request from Alexey Morozov.
  Renamed the file libxml2.m4

* Mon May 05 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.5.7-alt1
- New version

* Fri Apr 04 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.5.6-alt1
- 2.5.6

* Fri Jan 17 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.5.1-alt1
- Updated to 2.5.1
- Manpage patch gone upstream

* Fri Dec 13 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.4.30-alt1
- Updated to 2.4.30

* Thu Dec 05 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.4.28-alt2
- Applied cvs patch from Marcus Clarke fixing a problem in entities
  parsing that was detected in KDe documentations environment.

* Sat Nov 30 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.4.28-alt1
- 2.4.28
- doc subpackage

* Thu Nov 21 2002 Dmitry V. Levin <ldv@altlinux.org> 1:2.4.27-alt1
- 2.4.27
- Added dependence on xml-common.

* Sun Nov 03 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1:2.4.26-alt0.1
- 2.4.26, I hope it will behave now
- disable static build by default

* Wed Oct 09 2002 Stanislav Ievlev <inger@altlinux.ru> 1:2.4.24-alt2
- increase release to satisfy rpm
  (rpm ignore serial if version and release of old and new package a same)

* Wed Oct 09 2002 Stanislav Ievlev <inger@altlinux.ru> 1:2.4.24-alt1
- rollback to 2.4.24: new version is too buggy.

* Mon Oct 07 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4.25-alt1
- 2.4.25
- Fixed doc installation.

* Thu Sep 12 2002 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.24-alt1
- 2.4.24

* Mon Jul 22 2002 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.23-alt1
- 2.4.23
- Fixed doc installation

* Sat Jun 08 2002 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.22-alt1
- 2.4.22

* Sat May 04 2002 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.21-alt1
- 2.4.21
- Fixed BuildRequires
- postun_ldconfig

* Sat Apr 27 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.20-alt1
- 2.4.20

* Tue Mar 19 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.18-alt1
- 2.4.18.
- Repackaged docs.

* Wed Feb 20 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.16-alt1
- 2.4.16.

* Tue Feb 12 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.15-alt1
- 2.4.15.

* Mon Feb 11 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.14-alt1
- 2.4.14.
- Added python subpackage.

* Wed Jan 16 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.13-alt1
- 2.4.13

* Tue Nov 27 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.4.11-alt1
- 2.4.11

* Mon Nov 12 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.4.10-alt1
- 2.4.10

* Tue Nov 06 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.4.8-alt1
- 2.4.8
- Renamed xmllint subpackage to xml-utils.

* Mon Nov 05 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.4.7-alt1
- 2.4.7
- Packaged xmlcatalog.
- Packaged %_libdir/pkgconfig/* files.

* Fri Oct 12 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.6-alt1
- 2.4.6

* Mon Sep 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.5-alt1
- 2.4.5

* Thu Sep 13 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Mon Aug 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Fri Aug 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.2-alt2
- Rebuilt.

* Thu Aug 16 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Thu Jul 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Wed Jul 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Thu Jul 05 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.3.13-alt1
- 2.3.13

* Mon Jun 18 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.3.11-alt1
- 2.3.11

* Mon Jun 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.3.10-alt1
- 2.3.10

* Tue May 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.3.9-alt1
- 2.3.9
- Moved static library to devel-static subpackage.

* Sat May 05 2001 Rider <rider@altlinux.ru> 2.3.8-alt1
- 2.3.8

* Tue Mar 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.3.5-alt1
- 2.3.5

* Sun Mar 11 2001 Dmitry V. Levin <ldv@fandra.org> 2.3.4-ipl1mdk
- 2.3.4

* Sun Mar 04 2001 Dmitry V. Levin <ldv@fandra.org> 2.3.3-ipl1mdk
- 2.3.3

* Mon Feb 26 2001 Dmitry V. Levin <ldv@fandra.org> 2.3.2-ipl1mdk
- 2.3.2

* Sat Feb 17 2001 Dmitry V. Levin <ldv@fandra.org> 2.3.1-ipl1mdk
- 2.3.1

* Sun Feb 11 2001 Dmitry V. Levin <ldv@fandra.org> 2.3.0-ipl2mdk
- Provides libxml.so.2 for compatibility.

* Fri Feb 09 2001 Dmitry V. Levin <ldv@fandra.org> 2.3.0-ipl1mdk
- 2.3.0
- Removed "Conflicts: libxml-devel" tag from %name-devel package.

* Sat Jan 27 2001 Dmitry V. Levin <ldv@fandra.org> 2.2.12-ipl1mdk
- 2.2.12

* Sun Jan 07 2001 Dmitry V. Levin <ldv@fandra.org> 2.8.11-ipl3mdk
- 2.8.11
- Moved xmllint to separate subpackage.
- Specfile cleanup; updated URL, summaries and descriptions.
- Added libxml.m4 and manpages.
- Relocated html documentation.

* Wed Nov 29 2000 AEN <aen@logic.ru>
- build for RE

* Tue Nov 14 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.2.8-1mdk
- bump up the version.

* Fri Nov 03 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.2.7-1mdk
- new and shiny version.

* Sun Oct 29 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.2.6-1mdk
- shiny version.

* Sun Oct 15 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.2.4-1mdk
- very new and shiny version.

* Sat Aug 26 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 2.2.2-2mdk
- corrected bug reported by
  Reinhard Katzmann <reinhard.katzmann@neckar-alb.de> :
  Requires : %name = {PACKAGE_VERSION}

* Tue Aug 22 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 2.2.2-1mdk
- updated to libxml version 2.2.2

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.8.9-3mdk
- automatically added BuildRequires

* Fri Jul 28 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.8.9-2mdk
- rebuild

* Sat Jul 22 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 1.8.9-1mdk
- new version
- big move

* Thu Jul  6 2000 dam's <damien@mandrakesoft.com> 1.8.8-4mdk
- spec cleanup.

* Thu Jul 06 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 1.8.8-3mdk
- use some macros

* Tue Jul  4 2000 dam's <damien@mandrakesoft.com> 1.8.8-2mdk
- moved xml-config to devel package. Thanx to Stefan

* Tue Jul  4 2000 dam's <damien@mandrakesoft.com> 1.8.8-1mdk
- updated.
- spec cleanup.

* Tue Apr 18 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.8.7-1mdk
- fix release tag

* Sun Apr 16 2000 Daouda Lo <daouda@mandrakesoft.com> 1.8.7-1mdk
- release from helix stuffs.

* Wed Mar 22 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.8.6-2mdk
- fix group

* Sun Feb 20 2000 Axalon Bloodstone <axalon@mandrakesoft.com> 1.8.6-1mdk
- 1.8.6

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- SMP build/check
- 1.7.3

* Fri Sep 24 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- 1.7.1

* Thu Jul 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.4.

* Wed Jun 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.2.0.

* Tue May 11 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Thu Mar 04 1999 Michael Fulbright <drmike@redhat.com>
- version 1.0.0

* Fri Feb 12 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.5 built against gnome-libs-0.99.8

* Wed Feb 03 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.5

* Wed Jan 06 1999 Michael Fulbright <drmike@redhat.com>
- made clean section work again

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- bumped to 0.99.0 for GNOME freeze

* Sun Oct  4 1998 Daniel Veillard <Daniel.Veillard@w3.org>
- Added xml-config to the package

* Thu Sep 24 1998 Michael Fulbright <msf@redhat.com>
- Built release 0.30
