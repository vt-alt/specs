%def_disable static

Name: linux-atm
Version: 2.5.1
Release: alt6

Summary: Asynchronous Transfer Mode tools
License: GPL
Group: System/Libraries
Url: http://linux-atm.sourceforge.net/


Source: %name-%version-%release.tar

Requires: libatm = %version-%release
BuildRequires: flex, glibc-kernheaders

%description
This package contains tools to support ATM (Asynchronous Transfer Mode)
networking and some types of DSL modems.
ATM (Asynchronous Transfer Mode) networking for Linux is still under
development now but it works quite stable now and has been already
included in 2.4.x series kernels.

%package -n libatm
Summary: ATM (Asynchronous Transfer Mode) support library
License: LGPL
Group: System/Libraries
Provides: lib%name = %version-%release
Obsoletes: lib%name

%description -n libatm
This package contains libraries for
support ATM (Asynchronous Transfer Mode)
networking and some types of DSL modems.

%package -n libatm-devel
Summary: ATM development library
License: LGPL
Group: Development/C
Requires: libatm = %version-%release
Provides: lib%name-devel = %version-%release
Obsoletes: lib%name-devel

%description -n libatm-devel
This package contains development files needed to compile programs with libatm.

%package -n libatm-devel-static
Summary: ATM static library
License: LGPL
Group: Development/C
Requires: libatm-devel = %version-%release
Provides: lib%name-devel-static = %version-%release
Obsoletes: lib%name-devel-static

%description -n libatm-devel-static
This package contains libatm static library.

%prep
%setup

%build
%autoreconf
%configure %{subst_enable static}
make

%install
%makeinstall
bzip2 -9k ChangeLog

%files
%doc AUTHORS BUGS ChangeLog.bz2 NEWS README THANKS
%doc COPYING src/ilmid/COPYRIGHT src/lane/COPYRIGHT.TUT
%config(noreplace) %_sysconfdir/atmsigd.conf
%_bindir/*
%_sbindir/*
%_mandir/man?/*

%files -n libatm
%_libdir/*.so.*

%files -n libatm-devel
%_includedir/*
%_libdir/*.so

%if_enabled static
%files -n libatm-devel-static
%_libdir/*.a
%endif

%changelog
* Mon Jul 08 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.1-alt6
- fixed build with recent glibc-kernheaders, again

* Tue Dec 25 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.1-alt5
- fixed build with recent glibc-kernheaders

* Thu Oct 11 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.1-alt4
- rebuilt for debuginfo

* Thu Nov 11 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.1-alt3
- updated from CVS @20091130

* Mon Jun 29 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.1-alt2
- fix build breakage with recent bison

* Wed Dec 10 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.1-alt1
- 2.5.1 released

* Mon Jan 22 2007 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt6
- improve libatm description (fix bug #10654)

* Thu Dec 21 2006 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt5
- use glibc-kernheaders

* Tue Oct 24 2006 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt4
- add patches from PLD
- revert from orphaned

* Fri Feb 03 2006 Dmitry V. Levin <ldv@altlinux.org> 2.4.1-alt3.1
- Fixed build with fresh autotools.
- Cleaned up licenses, compressed changelog.
- Renamed lib%name{,-devel} to libatm{,-devel}.
- Corrected package scripts and interpackage dependencies.

* Sat Apr 16 2005 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt3
- fix URL

* Fri Apr 15 2005 Kachalov Anton <mouse@altlinux.ru> 2.4.1-alt2.1
- x86_64 support
- rebuild with kernel-headers-std26-up

* Tue Jan 18 2005 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt2
- fix spec
- use a macro for ldconfig
- rebuild with libstdc++.so.6

* Sat Dec 13 2003 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- first build for Sisyphus

* Fri Aug 08 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 2.4.1-3mdk
- rebuild

* Tue Jul 08 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 2.4.1-2mdk
- rebuild for new rpm devel computation

* Fri Jun 13 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 2.4.1-1mdk
- 2.4.1

* Sun Apr 30 2003 Stefan van der Eijk <stefan@eijk.nu> 2.4.0-3mdk
- BuildRequires

* Sat Jan 04 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 2.4.0-2mdk
- rebuild

* Wed Aug 21 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 2.4.0-1mdk
- first mdk release
