Name: libxslt
Version: 1.1.34
Release: alt1.p9.1

Summary: Library providing XSLT support
License: MIT
Group: System/Libraries
Url: http://xmlsoft.org/

%def_disable static
%def_enable python
%define srcname %name-%version

# git://git.gnome.org/libxslt.git
Source: %srcname.tar
# git://git.altlinux.org/gears/l/libxslt.git
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Mon Mar 21 2011
BuildRequires: libgcrypt-devel libxml2-devel python-devel python-module-libxml2

%package -n xsltproc
Summary: XSLT processor using libxslt
Group: Text tools
Requires: %name = %version-%release

%package devel
Summary: Development environment for XSLT
Group: Development/C
Requires: %name = %version-%release

%package devel-doc
Summary: Development documentation for XSLT
Group: Development/C
BuildArch: noarch

%package devel-static
Summary: Static library for XSLT
Group: Development/C
Requires: %name-devel = %version-%release

%setup_python_subpackage %name
%package -n %packagename
Summary: Python bindings for the %name library
Group: Development/Python
%setup_std_python_package_deps
Requires: %name = %version-%release
Requires: python-module-libxml2
Provides: python-modules-%name = %version-%release
Provides: libxslt-python = %version-%release
Obsoletes: python-modules-%name < %version-%release
Obsoletes: libxslt-python < %version-%release

%description
XSLT library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism.

This package provides shared library required for run XSLT-based software.

%description -n xsltproc
This package provides an XSLT processor based on the libxslt C library.
It allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism.

%description devel
XSLT library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism.

This package provides include files required for software development
with XSLT.

%description devel-doc
XSLT library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism.

This package provides documentation on software development
with the XSLT library.

%description devel-static
XSLT library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism.

This package provides static library required for development of
statically linked programs with XSLT.

%description -n python-module-%name
This package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libxslt library to apply XSLT transformations.

This library allows to parse sytlesheets, uses the %name-python
to load and save XML and HTML files. Direct access to XPath and
the XSLT transformation context are possible to extend the XSLT language
with XPath functions written in Python.

%prep
%setup -n %srcname
%patch -p1

%build
export ac_cv_path_XMLLINT=/usr/bin/xmllint
export ac_cv_path_XSLTPROC=/usr/bin/xsltproc
# disable dependency on binutils-devel
export ac_cv_header_ansidecl_h=no
%autoreconf
%configure \
	--with-html-dir=%_docdir \
	--with-html-subdir=%name-%version \
	%{subst_enable static}

# SMP-incompatible build.
make

%install
%makeinstall_std
# Replace libexslt.so symlink with a linker script.
rm %buildroot%_libdir/libexslt.so
cat > %buildroot%_libdir/libexslt.so << '__EOF__'
/* GNU ld script */
GROUP(libexslt.so.0 AS_NEEDED(-lxslt))
__EOF__
%define pkgdocdir %_docdir/%name-%version
install -pm644 AUTHORS COPYING FEATURES NEWS README %buildroot%pkgdocdir/

%check
make check

%files
%_libdir/*.so.*
%dir %pkgdocdir
%pkgdocdir/AUTHORS
%pkgdocdir/COPYING
%pkgdocdir/FEATURES
%pkgdocdir/NEWS
%pkgdocdir/README

%files -n xsltproc
%_bindir/xsltproc
%_man1dir/xsltproc.1*

%files devel
%_bindir/*-config
%_libdir/*.so
%_libdir/*.sh
%_includedir/*
%_libdir/pkgconfig/*
%_datadir/aclocal/*

%files devel-doc
%_man3dir/*
%dir %pkgdocdir
%pkgdocdir/*.html
%pkgdocdir/*.gif
%pkgdocdir/html
%pkgdocdir/tutorial*
%pkgdocdir/EXSLT

%if_enabled static
%files devel-static
%_libdir/*.a
%endif # enabled static

%if_enabled python
%files -n python-module-%name
%python_sitelibdir/*
%dir %pkgdocdir
%dir %pkgdocdir/python
%dir %pkgdocdir/python/examples
%pkgdocdir/python/examples/*.py
%pkgdocdir/python/examples/*.xml
%pkgdocdir/python/examples/*.xsl
%endif # enabled python

%changelog
* Mon Nov 16 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.1.34-alt1.p9.1
- Backported to p9 (fixes CVE-2019-11068, CVE-2019-13117 and CVE-2019-13118).

* Sun Mar 22 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.1.34-alt2
- Fixed FTBFS: built without Python module.

* Fri Nov 15 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.1.34-alt1
- Updated to 1.1.34.

* Thu Sep 12 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.1.33-alt2
- Fixes:
  + CVE-2019-11068 security framework bypass;
  + CVE-2019-13117 uninitialized read of xsl:number token;
  + CVE-2019-13118 uninitialized read with UTF-8 grouping chars.

* Tue Apr 09 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.1.33-alt1
- Update to 1.1.33 (ALT#36574).

* Wed Jan 31 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.1.32-alt2
- Actually updated source to 1.1.32.
- Upstream support for SOURCE_DATE_EPOCH (ALT#32814).
- Fixes:
  + CVE-2017-5029 generation of text nodes integer overflow,
  + CVE-2016-1684 integer overflow (mishandle the i format token for
    xsl:number),
  + CVE-2016-1683 out-of-bounds heap memory access (mishandle namespace nodes).

* Wed Nov 15 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.1.32-alt1
- Updated to 1.1.32.

* Sun Nov 22 2015 Dmitry V. Levin <ldv@altlinux.org> 1.1.28-alt4
- Updated to v1.1.28-46-g7ca19df.

* Tue Oct 06 2015 Sergey V Turchin <zerg@altlinux.org> 1.1.28-alt3
- Rebuild with libgcrypt.

* Wed Nov 12 2014 Dmitry V. Levin <ldv@altlinux.org> 1.1.28-alt2
- Updated to v1.1.28-36-g73e08bf.

* Wed Mar 27 2013 Dmitry V. Levin <ldv@altlinux.org> 1.1.28-alt1
- Updated to v1.1.28-3-g3fcf11e.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.26-alt4.1
- Rebuild with Python-2.7

* Thu Jul 14 2011 Dmitry V. Levin <ldv@altlinux.org> 1.1.26-alt4
- libxslt-devel: replaced libexslt.so symlink with a linker script.

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 1.1.26-alt3
- libxslt-devel: disabled deps on libgcrypt-devel libgpg-error-devel zlib-devel

* Fri Feb 25 2011 Dmitry V. Levin <ldv@altlinux.org> 1.1.26-alt2
- Rebuilt for debuginfo.

* Fri Nov 05 2010 Dmitry V. Levin <ldv@altlinux.org> 1.1.26-alt1
- Updated to v1.1.26-5-gc1c9859.
- Migrated to upstream ABI versioning.
- python: Fixed underlinking in libxsltmod.so.

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.24-alt2.1
- Rebuilt with python 2.6

* Sun Aug 02 2009 Dmitry V. Levin <ldv@altlinux.org> 1.1.24-alt2
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.
- Fixed build with fresh automake.
- Fixed python module packaging.

* Sat Aug 09 2008 Alexey Tourbin <at@altlinux.ru> 1.1.24-alt1
- 1.1.23 -> 1.1.24
- applied upstream fix for libexslt/crypto overflow (CVE-2008-2935)

* Tue Apr 22 2008 Alexey Tourbin <at@altlinux.ru> 1.1.23-alt1
- 1.1.22+svn1452 -> 1.1.23

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 1.1.22-alt2.1
- Rebuilt with python-2.5.

* Mon Jan 21 2008 Alexey Tourbin <at@altlinux.ru> 1.1.22-alt2
- 1.1.22+svn1447 -> 1.1.22+svn1452 (20071224)

* Sat Oct 27 2007 Alexey Tourbin <at@altlinux.ru> 1.1.22-alt1
- 1.1.21+svn1435 -> 1.1.22+svn1447 (20071025)
- python-module-libxslt: removed manual dependency on python;
  added manual dependency on python-module-libxml2

* Sun Aug 05 2007 Alexey Tourbin <at@altlinux.ru> 1.1.21-alt1
- 1.1.20+ -> 1.1.21+svn1435
- renamed python-modules-libxslt package to python-module-libxslt
- linked libxsltmod.so python module with libpython
- changed src.rpm packaging to keep separate tarball with svn snapshot

* Wed Feb 21 2007 Alexey Tourbin <at@altlinux.ru> 1.1.20-alt1
- 1.1.19+ -> 1.1.20+ (svn revision 1422)

* Mon Dec 11 2006 Alexey Tourbin <at@altlinux.ru> 1.1.19-alt1
- 1.1.18 -> 1.1.19+ (20061209)

* Tue Nov 14 2006 Alexey Tourbin <at@altlinux.ru> 1.1.18-alt1
- 1.1.17 -> 1.1.18
- imported cvs sources into git and built with gear

* Thu Jun 08 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.17-alt1
- Release 1.1.17
- Patch0: unescape the file URI in security checks (GNOME bug 337486)
- Patch1: remove internally used libraries from Libs: fields in .pc files

* Thu Jun 01 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.16-alt1
- Release 1.1.16
- Use the python directory macro
- Use the DESTDIR scheme in install
- Retired Patch1
- Updated and appended Patch2
- Patch3 went upstream
- Small spec cleanups

* Wed Oct 05 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.15-alt2
- Patch3: fix GNOME bug #316861

* Mon Sep 05 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.15-alt1
- New upstream release
- Separated documentation into devel-doc

* Tue Apr 05 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.14-alt1
- New upstream release

* Mon Mar 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.13-alt1
- New upstream release
- Built against Python 2.4

* Sun Jan 02 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.12-alt2
- Corrected documentation filelist
- Corrected required libxml version

* Sun Oct 31 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.12-alt1
- New upstream release

* Fri Oct 01 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.11-alt1
- New upstream release

* Mon Sep 20 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.10-alt1
- New upstream release
- buildreq

* Tue Aug 24 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.9-alt1
- New upstream release
- Grouped xsltproc under 'Text tools'

* Thu Jul 15 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.8-alt2
- Python package renamed to comply with the New Policy

* Thu Jul 08 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.8-alt1
- New upstream release

* Mon Apr 19 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.6-alt1
- New upstream release

* Sat Apr 03 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.5-alt1
- New upstream release

* Tue Feb 24 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.4-alt1
- New upstream release
- Built with python 2.3

* Wed Dec 31 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.2-alt1
- New upstream release
- Happy New Year :)

* Thu Dec 11 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.1-alt1
- New upstream release

* Fri Nov 28 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt2
- Do not package .la files.

* Mon Nov 10 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.0-alt1
- Upstream release 1.1.0

* Tue Sep 16 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.33-alt1
- Upstream release 1.0.33
- Patch0 has gone upstream

* Mon Aug 18 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.32-alt1
- New version
- Fix Bugzilla bug #114563 [Patch0]
- Do not let compiled example files in the filelist

* Sat Jul 12 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.31-alt1
- New version
- Patch0 has gone upstream

* Wed May 14 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.30-alt2
- Update from CVS fixing a few segfault bugs [Patch0]

* Mon May 05 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.30-alt1
- New version

* Sat Apr 05 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.29-alt1
- 1.0.29

* Fri Jan 17 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.24-alt2
- Removed ChangeLog that was included along with ChangeLog.bz2

* Thu Jan 16 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.24-alt1
- 1.0.24

* Thu Nov 21 2002 Dmitry V. Levin <ldv@altlinux.org> 1.0.23-alt1
- 1.0.23

* Sun Nov 03 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.22-alt1
- 1.0.22

* Wed Oct 09 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0.21-alt2
- rebuild with libxml2 2.4.24

* Mon Oct 07 2002 Dmitry V. Levin <ldv@altlinux.org> 1.0.21-alt1
- 1.0.21
- Fixed doc installation.

* Thu Sep 26 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.20-alt2
- Fixed pkgconfig file to exclude -I/usr/include
- Fixed xsltConf.sh to include libxml cflags
- Disabled static build by default

* Thu Sep 12 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.20-alt1
- 1.0.20
- patches are gone

* Tue Aug 20 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.19-alt2
- Fix for docbook users

* Thu Jul 25 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.19-alt1
- 1.0.19
- Fixed installation of HTML docs

* Wed Jun 12 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.18-alt1
- 1.0.18

* Sat May 04 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.17-alt1
- 1.0.17
- Separated xsltproc from the lib
- libxslt-devel-static shall NOT require libxml-devel-static
- Repackaged docs again: .py files should not be compiled,
  ugly renaming also not good
- make check

* Sat Apr 27 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.0.16-alt1
- 1.0.16

* Tue Mar 19 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.0.14-alt1
- 1.0.14

* Tue Feb 12 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.0.12-alt1
- 1.0.12

* Mon Feb 11 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.0.11-alt1
- 1.0.11
- Added python subpackage.

* Wed Jan 16 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.0.10-alt1
- 1.0.10

* Tue Nov 27 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0.8-alt1
- 1.0.8

* Mon Nov 12 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0.7-alt1
- 1.0.7

* Mon Nov 05 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0.6-alt1
- 1.0.6

* Fri Oct 12 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Thu Sep 13 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Mon Aug 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Aug 16 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Jul 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Wed Jul 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Thu Jul 05 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Mon Jun 18 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Mon Jun 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.11.0-alt1
- 0.11.0

* Tue May 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.10.0-alt1
- 0.10.0
- Moved static library to devel-static subpackage.

* Sat May 05 2001 Rider <rider@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Mon Jan 22 2001 Daniel.Veillard <Daniel.Veillard@imag.fr>
- created based on libxml2 spec file
