Name: libofx
Version: 0.9.15
Release: alt1

Summary: The OFX parser library
Group: System/Libraries
License: GPLv2
Url: http://libofx.sourceforge.net

Source: http://download.sourceforge.net/%name/%name-%version.tar.gz
Source1: %name.watch

BuildRequires: libOpenSP-devel gcc-c++ libcurl-devel
BuildRequires: libxml++2-devel gengetopt help2man

%description
This is the LibOFX library. It is a API designed to allow applications
to very easily support OFX command responses, usually provided by
financial institutions. See http://www.ofx.net/ for details and
specification.

%package devel
Summary: The OFX parser development library
Group: Development/C++
Requires: %name = %version-%release
Provides: %name-docs = %version-%release
Obsoletes: %name-docs

%description devel
This is the LibOFX library.  It is a API designed to allow applications
to very easily support OFX command responses, usually provided
by financial institutions.  See http://www.ofx.net/ for details
and specification. LibOFX is based on the excellent OpenSP library
written by James Clark, and now part of the OpenJADE
http://openjade.sourceforge.net/ project.  OpenSP by itself is not
widely distributed.  OpenJADE 1.3.1 includes a version on OpenSP that
will link, however, it has some major problems with LibOFX and isn't
recommended. Since LibOFX uses the generic interface to OpenSP, it
should be compatible with all recent versions of OpenSP (It has been
developed with OpenSP-1.5pre5). LibOFX is written in C++, but provides
a C style interface usable transparently from both C and C++ using
a single include file.

Headers, documentation and other files for development with libofx.

%prep
%setup
rm -f ofxdump/ofxdump.1

%build
%add_optflags -std=c++11
%autoreconf
%configure --disable-static
%make

%install
%makeinstall_std

%check
%make check

%files
%_bindir/ofxdump
%_bindir/ofxconnect
%_bindir/ofx2qif
%_libdir/*.so.*
%_datadir/%name
%_man1dir/ofxdump.1*
%_man1dir/ofxconnect.1*

%files devel
%doc AUTHORS NEWS README totest.txt
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/%name.pc
%_docdir/%name/

%changelog
* Thu May 28 2020 Andrey Cherepanov <cas@altlinux.org> 0.9.15-alt1
- New version.

* Sun Mar 10 2019 Andrey Cherepanov <cas@altlinux.org> 0.9.14-alt1
- New version.

* Tue Dec 18 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.13-alt1
- New version.

* Thu Jun 02 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.10-alt1.3
- support any extension for man pages

* Wed Sep 30 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.10-alt1.2
- rebuilt against newer libxml++

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.10-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Feb 24 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.10-alt1
- 0.9.10

* Sat Nov 23 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.9-alt1
- 0.9.9
- %%check section

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt2.1
- Removed bad RPATH

* Tue Sep 06 2011 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt2
- Move libofx-docs to libofx-devel

* Tue Sep 06 2011 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1
- New version 0.9.4

* Wed Nov 10 2010 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt3
- rebuld

* Tue Nov 25 2008 Andrey Cherepanov <cas@altlinux.ru> 0.9.0-alt2
- fixed build for gcc4.3

* Thu Sep 25 2008 Lebedev Sergey <barabashka@altlinux.org> 0.9.0-alt1
- new version 0.9.0

* Wed Feb 14 2007 Igor Muratov <migor@altlinux.org> 0.8.3-alt1
- new version

* Tue Jun 20 2006 Igor Muratov <migor@altlinux.org> 0.8.0-alt4
- Rebuild with new OpenSP

* Mon Apr 03 2006 Igor Muratov <migor@altlinux.org> 0.8.0-alt3
- Build with gcc4

* Tue Jan 10 2006 Igor Muratov <migor@altlinux.org> 0.8.0-alt2
- patch for makefiles

* Mon Aug 22 2005 Igor Muratov <migor@altlinux.org> 0.8.0-alt1
- new version

* Mon Jan 17 2005 Igor Muratov <migor@altlinux.org> 0.7.0-alt3
- Spec cleanup

* Mon Jan 10 2005 Igor Muratov <migor@altlinux.org> 0.7.0-alt2
- Split packet

* Sun Jan  2 2005 Igor Muratov <migor@altlinux.org> 0.7.0-alt1
- Initial build for ALT

* Sat Nov 23 2002 Chris Lyttle <chris@wilddev.net>
- Created spec file
