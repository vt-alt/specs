Name: expat
Version: 2.2.10
Release: alt1

%def_disable static
%define pkgdocdir %_docdir/%name-%version

Summary: An XML parser written in C
License: MIT
Group: System/Base
Url: http://www.libexpat.org/
# http://downloads.sourceforge.net/project/expat/expat/%version/expat-%version.tar.bz2
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: lib%name = %version-%release

# for "make check"
BuildRequires: gcc-c++

%package -n lib%name
Summary: XML parser library
Group: System/Libraries

%package -n lib%name-devel
Summary: Development files for Expat, an XML parser library for C
Group: Development/C
Requires: lib%name = %version-%release
Provides: expat-devel = %version
Obsoletes: expat-devel

%package -n lib%name-devel-static
Summary: Static library for developing static applications which will manipulate XML files
Group: Development/C
Requires: lib%name-devel = %version-%release

%description
Expat is a stream-oriented XML parser written in C.

%description -n lib%name
Expat is a stream-oriented XML parser written in C.
This package provides the Expat parser as a shared library.

%description -n lib%name-devel
Expat is a stream-oriented XML parser written in C.
This package is needed if you want to build programs which use Expat
library.

%description -n lib%name-devel-static
Expat is a stream-oriented XML parser written in C.
This package provides the Expat parser as a library for static linking.

%prep
%setup
%patch -p1

%build
%autoreconf
export DOCBOOK_TO_MAN="xmlto man --skip-validation"
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

# Relocate shared library from /usr/lib to /lib.
mkdir -p %buildroot/%_lib
mv %buildroot%_libdir/libexpat.so.1* %buildroot/%_lib
rm %buildroot%_libdir/libexpat.so
ln -s ../../%_lib/libexpat.so.1 %buildroot%_libdir/libexpat.so

install -d -m755 %buildroot%pkgdocdir
install -p -m644 README.md COPYING Changes %buildroot%pkgdocdir/
install -p -m644 doc/*.{html,css,png} %buildroot%pkgdocdir/
install -d -m755 %buildroot%pkgdocdir/examples
install -p -m644 examples/*.c %buildroot%pkgdocdir/examples/

%check
%make_build -k check

%files
%_bindir/*
%_man1dir/*

%files -n lib%name
/%_lib/*.so.*
%dir %pkgdocdir
%pkgdocdir/Changes
%pkgdocdir/COPYING
%pkgdocdir/README.md

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%dir %pkgdocdir
%pkgdocdir/*.html
%pkgdocdir/*.css
%pkgdocdir/*.png
%pkgdocdir/examples

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif	# enabled static

%changelog
* Fri Oct 16 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.2.10-alt1
- Updated to 2.2.10.

* Sun May 31 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.2.9-alt1
- 2.2.4 -> 2.2.9 (fixes CVE-2018-20843 and CVE-2019-15903)
- Fixed license field according with SPDX

* Mon Aug 21 2017 Alexey Tourbin <at@altlinux.ru> 2.2.4-alt1
- 2.1.0 -> 2.2.4

* Wed Sep 12 2012 Dmitry V. Levin <ldv@altlinux.org> 2.1.0-alt1
- Updated to 2.1.0.
- Stopped build and packaging of libexpat-devel-static.

* Sat Feb 05 2011 Alexey Tourbin <at@altlinux.ru> 2.0.1-alt5
- relocated shared library from /usr/lib to /lib

* Mon Oct 11 2010 Alexey Tourbin <at@altlinux.ru> 2.0.1-alt4
- backported more bugfixes from cvs
- enabled "make check"

* Wed May 06 2009 Dmitry V. Levin <ldv@altlinux.org> 2.0.1-alt3
- Fixed build with fresh libtool.

* Fri Apr 10 2009 Alexey Tourbin <at@altlinux.ru> 2.0.1-alt2
- backported from cvs:
- parser crash with specially formatted UTF-8 sequences (expat-Bugs-1990430)
- xmlwf should return a non-zero code for parsing errors (expat-Bugs-2517938)

* Fri Apr 10 2009 Alexey Tourbin <at@altlinux.ru> 2.0.1-alt1
- updated to 2.0.1 release
- removed ldconfig scriptlets

* Sun Apr 08 2007 Alexey Tourbin <at@altlinux.ru> 2.0.1-alt0.1
- updated to 20061213 cvs snapshot

* Thu Jan 19 2006 Dmitry V. Levin <ldv@altlinux.org> 2.0.0-alt3.1
- Fixed recently added Provides for x86_64.

* Tue Jan 17 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.0.0-alt3
- Added triggerpostun to correct libexpat.so.0 symlink after an upgrade
  from a pre-2.0 version

* Tue Jan 17 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.0.0-alt2
- Provide libexpat.so.0 as a symlink for backward compatibility

* Thu Jan 12 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.0.0-alt1
- 2.0.0
- Consolidated documentation in one directory
- Improved summaries and descriptions
- Buildreq

* Fri Feb 11 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.95.8-alt2
- Formal rebuild to bring static library to Sisyphus [bug #6087]

* Mon Jul 26 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.95.8-alt1
- New upstream release
- Excluded *.la files

* Thu Oct 23 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.95.7-alt1
- New upstream release
- Patch0 is now obsolete

* Tue Apr 01 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.95.6-alt2
- Relocate an enum declaration for better buildability (Vitaly Lipatov)
  [Patch0]

* Thu Feb 20 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.95.6-alt1
- 1.95.6

* Mon Sep 23 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.95.5-alt1
- 1.95.5

* Tue Sep 03 2002 AEN <aen@altlinux.ru> 1.95.4-alt1
- new version

* Mon Sep 02 2002 AEN <aen@logic.ru> 1.95.2-alt3
- rebuilt with gcc-3.2.1

* Fri Mar 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.95.2-alt2
- Fixed build.

* Tue Jul 31 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.95.2-alt1
- 1.95.2
- Libification.

* Wed Dec 27 2000 Dmitry V. Levin <ldv@fandra.org> 1.95.1-ipl1
- 1.95.1
- Included new summaries and descriptions
  (from Alexander Bokovoy <ab@avilink.net>).

* Sat Dec 09 2000 Dmitry V. Levin <ldv@fandra.org> 1.1-ipl2
- RE adaptions.
- FHSification.
- Moved library and headers to devel subpackage.

* Mon Jan 10 2000 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions.

* Wed Jul 28 1999 Greg LaPolla <glapolla@earthlink.net>
- Made spec file
- Built on redhat 6.0
