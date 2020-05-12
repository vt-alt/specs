Name: gsmlib
Version: 1.11
Release: alt5.041028

Summary: Library to access GSM mobile phones through GSM modems
License: LGPLv2
Group: System/Libraries

URL: http://www.pxh.de/fs/gsmlib
Source: http://www.pxh.de/fs/gsmlib/snapshots/gsmlib-pre1.11-041028.tar.gz

Patch1: gsmlib-template.patch
Patch2: gsmlib-1.11-fix-build-with-gettext-0.20.patch
Patch3: gsmlib-1.10-underlink.patch

# Patches from arc@help0.ru  Arcady Ivanov
# 28 Apr 2006
#
#1. In gsmsendsms added key "-u", which means, that sended string encoded in UNICODE
#2. Correct bugs in sending multipart SMS.

Patch10: gsmlib_me_ta.patch
Patch11: gsmlib_motor1.patch
Patch12: gsmsendsms.patch

# FTBFS fixes:
Patch100: gsmlib-1.11-gcc41.patch
Patch101: gsmlib-1.11-gcc43.patch

Obsoletes: gsmlib-ext <= %version
Provides: gsmlib-ext

# Automatically added by buildreq on Tue May 16 2006
BuildRequires: gcc-c++

%package utils
Summary: Utilities to access GSM mobile phones through GSM modems
Group: Communications

%package devel
Summary: Development tools for programs which will use the gsmlib library
Group: Development/C
Requires: gsmlib = %version-%release

%description
This distribution contains a library to access GSM mobile phones through GSM
modems. Features include:
 * modification of phonebooks stored in the mobile phone or on the SIM card
 * reading and writing of SMS messages stored in the mobile phone
 * sending and reception of SMS messages
Additionally, some simple command line programs are provided to use these
functionalities.

%description utils
Simple command line programs to access GSM mobile phones through GSM modems.

%description devel
The gsmlib-devel package includes the header files and static libraries
necessary for developing programs which use the gsmlib library.

%prep
%setup

%patch1 -p1
%patch2 -p2
%patch3 -p1

%patch11 -p0
%patch10 -p1
%patch12 -p1

%patch100 -p1
%patch101 -p1

# Play ghost-busters! :) gsmsstk is ghost that exist only in Makefile
subst 's/^gsmsstk/#gsmsstk/g; s/gsmsiexfer gsmsstk/gsmsiexfer/' ext/Makefile.am

%build
# supplied libtool is broken (C++ library linking)
%autoreconf
%configure --disable-static
%make_build CXX="g++ -DHAVE_LOCALE_H"

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_libdir/lib*.so.*
%doc README ext/README.sieme
%doc doc/README.developers doc/FAQ

%files utils
%_bindir/*
%_man1dir/*
%_man7dir/*
%_man8dir/*

%files devel
%_includedir/gsmlib
%_libdir/*.so

%changelog
* Wed May 06 2020 Anton Midyukov <antohami@altlinux.org> 1.11-alt5.041028
- Fix build with gettext 0.20

* Wed Jul 29 2015 Anton Farygin <rider@altlinux.ru> 1.11-alt4.041028.qa2
- rebuild for new gcc5 ABI

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.11-alt4.041028.qa1
- NMU: rebuilt for debuginfo.

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 1.11-alt4.041028
- Rebuilt for soname set-versions.

* Sat Jan 10 2009 Victor Forsyuk <force@altlinux.org> 1.11-alt3.041028
- Remove obsolete ldconfig calls.

* Tue Nov 04 2008 Victor Forsyuk <force@altlinux.org> 1.11-alt2.041028
- Fix FTBFS with gcc4.3.

* Wed Dec 26 2007 Victor Forsyuk <force@altlinux.org> 1.11-alt1.041028
- Fix FTBFS in current build environment.

* Mon Jan 22 2007 Victor Forsyuk <force@altlinux.org> 1.11-alt0.041028
- Update to pre1.11-041028.
- Split utilities to -utils package. Main package now contains only library.
  This fixes ALT#2662.
- Add patches from Arcady Ivanov <arc at help0 dot ru>.

* Tue May 16 2006 Victor Forsyuk <force@altlinux.ru> 1.10-alt11
- Fix FTBFS with gcc4.

* Tue Mar 21 2006 Victor Forsyuk <force@altlinux.ru> 1.10-alt10
- Fixed compilation error: "explicit qualification in declaration of..."
- Update generated configuration files (autoreconf) to fix broken C++ library linking.
- Add linking with libgsmme to libgsmext.

* Tue Mar 15 2005 Victor Forsyuk <force@altlinux.ru> 1.10-alt9
- Fixed build with gcc 3.4.
- Spec cleanups.
- Static libs moved to separate package.
- Merged gsmlib-ext with main package.

* Sat Sep 04 2004 Denis Smirnov <mithraen@altlinux.ru> 1.10-alt8
- fixed x86_64 build

* Fri Mar 19 2004 Denis Smirnov <mithraen@altlinux.ru> 1.10-alt7
- fixed assert() use

* Mon Oct 20 2003 Artem Pastukhov <past@altlinux.ru> 1.10-alt6
- Minor fixes in provide so.1

* Thu Oct 16 2003 Artem Pastukhov <past@altlinux.ru> 1.10-alt5
- Vendor set to ALT Linux Team

* Mon Oct  6 2003 Artem Pastukhov <past@altlinux.ru> 1.10-alt3
- Fixes, fixes, fixes in spec

* Wed Oct 1 2003 Artem Pastukhov <past@altlinux.ru> 1.10-alt3
- Fixes to build in hasher

* Wed Dec 4 2002 Artem Pastukhov <past@altlinux.ru> 1.10-alt2
- Fixes in spec

* Tue Dec 3 2002 Artem Pastukhov <past@altlinux.ru> 1.10-alt1
- Initial release for Sisyphus
