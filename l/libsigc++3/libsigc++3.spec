%def_disable snapshot

%define _name libsigc++
%define ver_major 3.0
%define api_ver 3.0
%def_enable check

Name: %{_name}3
Version: %ver_major.0
Release: alt1

Summary: The Typesafe Callback Framework for C++
License: LGPLv2+
Group: System/Libraries
Url: https://libsigcplusplus.github.io/libsigcplusplus/

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
#VCS: https://github.com/libsigcplusplus/libsigcplusplus.git
Source: %_name-%version.tar
%endif

BuildRequires: gcc-c++ mm-common >= 0.9.12
BuildRequires: docbook-style-xsl doxygen graphviz xsltproc

%description
libsigc++ implements a typesafe callback system for standard C++.
It allows you to define signals and to connect those signals to any
callback function, either global or a member function, regardless of
whether it is static or virtual.

%package devel
Summary: Development files for libsigc++ library
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package contains development files for the software development
using libsigc++ library.

%package doc
Summary: Documentation for libsigc++ library
Group: Books/Other
BuildArch: noarch

%description doc
This package provides API documentation of libsigc++ library.

%prep
%setup -n %_name-%version

%build
mm-common-prepare -f
%autoreconf
%configure --disable-static
%make_build DOCBOOK_STYLESHEET=/usr/share/xml/docbook/xsl-stylesheets/html/chunk.xsl

%install
%makeinstall_std
%define docdir %_docdir/libsigc++-%api_ver
install -pm644 AUTHORS NEWS README* %buildroot%docdir/

%check
%make_build -k check

%files
%_libdir/*.so.*
%dir %docdir
%docdir/[ANR]*

%files devel
%_libdir/*.so
%_libdir/sigc*
%_includedir/*
%_pkgconfigdir/*

%files doc
%docdir
%exclude %docdir/[ANR]*
%doc %_datadir/devhelp/books/*

%changelog
* Thu Sep 05 2019 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Jun 12 2019 Yuri N. Sedunov <aris@altlinux.org> 2.99.13-alt1
- 2.99.13

* Sat Mar 09 2019 Yuri N. Sedunov <aris@altlinux.org> 2.99.12-alt1.1
- fixed %%url (ALT #36250)

* Tue Oct 30 2018 Yuri N. Sedunov <aris@altlinux.org> 2.99.12-alt1
- 2.99.12

* Thu May 31 2018 Yuri N. Sedunov <aris@altlinux.org> 2.99.11-alt1
- 2.99.11

* Thu Jan 11 2018 Yuri N. Sedunov <aris@altlinux.org> 2.99.10-alt1
- 2.99.10

* Mon Aug 07 2017 Yuri N. Sedunov <aris@altlinux.org> 2.99.9-alt1
- 2.99.9

* Sun Sep 04 2016 Yuri N. Sedunov <aris@altlinux.org> 2.99.7-alt1
- 2.99.7

* Tue Jun 07 2016 Yuri N. Sedunov <aris@altlinux.org> 2.99.6-alt1
- 2.99.6

* Wed Mar 09 2016 Yuri N. Sedunov <aris@altlinux.org> 2.99.1-alt1
- 2.99.1

* Fri Nov 13 2015 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt1
- 2.6.2

* Mon Sep 28 2015 Yuri N. Sedunov <aris@altlinux.org> 2.6.1-alt1
- 2.6.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Thu May 21 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt2
- rebuilt with gcc5

* Sat Feb 28 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Sat Oct 04 2014 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Sun Apr 07 2013 Dmitry V. Levin <ldv@altlinux.org> 2.3.1-alt1
- Updated to 2.3.1-2-g7c6ff31.

* Wed Oct 03 2012 Dmitry V. Levin <ldv@altlinux.org> 2.2.11-alt1
- Updated to 2.2.11.

* Fri Aug 19 2011 Dmitry V. Levin <ldv@altlinux.org> 2.2.10-alt1
- Updated to 2.2.10.

* Fri Jul 01 2011 Dmitry V. Levin <ldv@altlinux.org> 2.2.9-alt1
- Updated to 2.2.9-1-g471d4a5.
- Fixed build in network isolation.

* Sat Feb 26 2011 Dmitry V. Levin <ldv@altlinux.org> 2.2.8-alt2
- Updated to 2.2.8-8-g18d3559.

* Fri Nov 19 2010 Dmitry V. Levin <ldv@altlinux.org> 2.2.8-alt1
- Switched to http://git.gnome.org/libsigc++2/.
- Updated to 2.2.8-6-ge3a3dd7.
- Cleaned up specfile.
- Enabled test suite.

* Thu May 06 2010 Vitaly Lipatov <lav@altlinux.ru> 2.2.7-alt1
- new version 2.2.7 (with rpmrb script) (ALT bug #23294)
- update buildreqs, migrate to build from git

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.2.3-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libsigc++2.0
  * postun_ldconfig for libsigc++2.0
  * postclean-05-filetriggers for spec file

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.3-alt1
- new version 2.2.3 (with rpmrb script)

* Sat Apr 12 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt1
- new version 2.2.2 (with rpmrb script)

* Sun Jan 13 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.18-alt1
- new version 2.0.18 (with rpmrb script)
- cleanup spec, remove COPYING, enable SMP-build

* Tue Feb 21 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.17-alt0.1
- new version (2.0.17)

* Sun Sep 11 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.16-alt1
- new version

* Sun Jul 17 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.15-alt1
- new version

* Wed Mar 02 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.10-alt1
- new version

* Mon Feb 21 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.9-alt1
- new version

* Thu Jan 20 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.6-alt2
- rebuild with gcc3.4
- disable build static library

* Wed Oct 13 2004 Vitaly Lipatov <lav@altlinux.ru> 2.0.6-alt1
- new version

* Sat Sep 04 2004 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- new version
- use a macro for ldconfig

* Wed Jun 02 2004 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version

* Mon May 24 2004 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- new version for Sisyphus (thanks Mandrake)
- without tests and examples (can't build)

* Tue May 04 2004 Abel Cheung <deaddog@deaddog.org> 2.0.1-1mdk
- New version
- Split doc as subpackage

* Tue Apr 27 2004 Abel Cheung <deaddog@deaddog.org> 2.0.0-1mdk
- New major release
- Add lib64* Provides

* Tue Sep  2 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2.5-5mdk
- don't use "libsigc" in binary package but "libsigc++", it's the real
  name of the package anyway

* Wed Aug 13 2003 Abel Cheung <maddog@linux.org.hk> 1.2.5-4mdk
- Convert this spec to UTF-8
- mklibname
- Don't provide libsigc++-devel, that's sigc++ 1.0's job
- examples package gone for good. It is moved to %%doc of devel
  package -- an utter mess

* Wed Jul  9 2003 Götz Waschk <waschk@linux-mandrake.com> 1.2.5-3mdk
- make the devel package require pkgconfig

* Tue Jul 8 2003 Austin Acton <aacton@yorku.ca> 1.2.5-2mdk
- from andi payn <payn@myrealbox.com> :
  - Don't obsolete libsigc++-devel, so 1.2 and 1.0 can coexist.

* Wed Jun 04 2003 Frederic Crozat <fcrozat@mandrakesoft.com> - 1.2.5-1mdk
- Release 1.2.5

* Sat Apr  5 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2.4-1mdk
- the 1.2 generation (for gtkmm2)

* Tue Aug 13 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.0.4-5mdk
- Automated rebuild with gcc 3.2-0.3mdk

* Tue Jul 30 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.4-4mdk
- take Goetz Waschk <waschk@informatik.uni-rostock.de> patch in order to
  build again (disable `windres' use, seems to be a ms-windows only
  binary)

* Tue Jul  2 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.0.4-3mdk
- Costlessly make check in %%build stage

* Mon May 06 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.0.4-2mdk
- Automated rebuild in gcc3.1 environment

* Sat Dec 29 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.0.4-1mdk
- 1.0.4 (some strange stuff with centericq + 1.0.3).

* Tue Oct 16 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.3-3mdk
- fix obsolete-tag Copyright
- fix summary-too-long
- fix description-line-too-long

* Thu Aug 30 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.3-2mdk
- rebuild to fix distribution tag and provides
- need to change Makefile.am since libtool can't see it needs to
  dynamically link with libstdc++ :-(

* Sat Feb 17 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.3-1mdk
- 1.0.3
- make provides qualifying version

* Tue Nov 28 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.2-3mdk
- Correct Obsoletes

* Mon Nov 27 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.2-2mdk
- fix descriptions

* Mon Nov 27 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.2-1mdk
- 1.0.2
- new lib policy

* Tue Nov  7 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-6mdk
- fix summaries and inter-dependency

* Fri Nov  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-5mdk
- recompile against newest libstdc++

* Tue Oct  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-4mdk
- fix spelling-error-in-description

* Wed Aug 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-3mdk
- automatically added packager tag

* Tue Jul 18 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-2mdk
- macros

* Fri Jun  2 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-1mdk
- 1.0.1

* Sat Apr 15 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-1mdk
- 1.0.0 (was released to accompany the release of gtkmm-1.2.0)

* Sun Apr  2 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.8.6-3mdk
- fixed wrong group for libsigc++-examples.

* Sun Apr  2 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.8.6-2mdk
- fix. now it does work with gtkmm.

* Mon Mar 06 2000 Lenny Cartier <lenny@mandrakesoft.com>
- oops the 0.8.6 release was out

* Mon Mar 06 2000 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- mandrake build

* Sat Dec 25 1999 Herbert Valerio Riedel <hvr@gnu.org>
- fixed typo of mine
- added traditional CUSTOM_RELEASE stuff
- added SMP support

* Thu Dec 23 1999 Herbert Valerio Riedel <hvr@gnu.org>
- adjusted spec file to get tests.Makefile and examples.Makefile from scripts/

* Fri Oct 22 1999 Dmitry V. Levin <ldv@fandra.org>
- split into three packages: %name, %name-devel and %name-examples

* Thu Aug 12 1999 Karl Nelson <kenelson@ece.ucdavis.edu>
- updated source field and merged conflicts between revisions.

* Tue Aug 10 1999 Dmitry V. Levin <ldv@fandra.org>
- updated Prefix and BuildRoot fields

* Thu Aug  5 1999 Herbert Valerio Riedel <hvr@hvrlab.dhs.org>
- made sure configure works on all alphas

* Wed Jul  7 1999 Karl Nelson <kenelson@ece.ucdavis.edu>
- Added autoconf macro for sigc.

* Fri Jun 11 1999 Karl Nelson <kenelson@ece.ucdavis.edu>
- Made into a .in to keep version field up to date
- Still need to do release by hand

* Mon Jun  7 1999 Dmitry V. Levin <ldv@fandra.org>
- added Vendor and Packager fields

* Sat Jun  5 1999 Dmitry V. Levin <ldv@fandra.org>
- updated to 0.8.0

* Tue Jun  1 1999 Dmitry V. Levin <ldv@fandra.org>
- initial revision
