%define _unpackaged_files_terminate_build 1

%def_disable static

%define	TDSVER 7.4
%define	name freetds
%define	release alt2
%define	version 1.2.17

Name:		%name
Version:	%version
Release:	%release

Summary:	An OpenSource implementation of the tubular data stream protocol
License:	GPL/LGPL
Group:		System/Libraries
URL:		http://www.freetds.org/

Source0:	%name-%version.tar
Source1:	%name.sh
Source2:	%name.csh

Patch1: %name-alt-revert-dblib-fix-TDS_DONE_RESULT-empty-rowsets.patch
Patch2: %name-alt-fix-datacopy-logging.patch

# Automatically added by buildreq on Sun Aug 19 2018
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libcom_err-devel libkrb5-devel libncurses-devel libtinfo-devel libunixODBC-devel-compat perl pkg-config python-base python-modules python3 python3-base python3-dev ruby sh3
BuildRequires: doxygen glibc-devel-static libgnutls-devel libreadline-devel libssl-devel libunixODBC-devel

%if_enabled static
BuildRequires: glibc-devel-static
%endif


%description
FreeTDS is a free (open source) implementation of Sybase's db-lib,
ct-lib, and ODBC libraries. Currently, dblib and ctlib are most mature.
Both of these libraries have several programs know to compile and run
against them.

This package is built with support of TDS version %TDSVER.

%package -n lib%name
Summary:	An OpenSource implementation of the tubular data stream protocol
License:	GPL/LGPL
Group:		System/Libraries
Provides:	%name

%description -n lib%name
FreeTDS is a free (open source) implementation of Sybase's db-lib,
ct-lib, and ODBC libraries. Currently, dblib and ctlib are most mature.
Both of these libraries have several programs know to compile and run
against them.

This package is built with support for TDS version %TDSVER.

%package -n lib%name-unixodbc
Summary:	FreeTDS driver for unixODBC. 
License:	GPL/LGPL
Group:		System/Libraries
Provides:	%name

%description -n lib%name-unixodbc
FreeTDS driver for unixODBC. FreeTDS is a free (open source) implementation
of Sybase's db-lib, ct-lib, and ODBC libraries. Currently, dblib and ctlib
are most mature. Both of these libraries have several programs know to compile
and run against them.

This package is built with support for TDS version %TDSVER.

%package -n lib%name-devel
Summary: 	An OpenSource implementation of the TDS protocol. Development files
License:	GPL/LGPL
Group: 		Development/C
PreReq:		lib%name = %EVR
Provides:	%name-devel

%description -n lib%name-devel
FreeTDS is a free (open source) implementation of Sybase's db-lib,
ct-lib, and ODBC libraries. The freetds-devel allows you to compile
applications with freetds libraries.

This package is built with support for TDS version %TDSVER.

%package -n lib%name-devel-static
Summary: 	An OpenSource implementation of the TDS protocol. Static libraries
License:	GPL/LGPL
Group: 		Development/C
PreReq:		lib%name-devel = %EVR
Provides:	%name-devel-static

%description -n lib%name-devel-static
FreeTDS is a free (open source) implementation of Sybase's db-lib,
ct-lib, and ODBC libraries. The freetds-devel allows you to compile
applications with freetds libraries. Package with static libraries.

This package is built with support for TDS version %TDSVER.


%package -n %name-utils
Summary:	An OpenSource implementation of the TDS protocol. Utilities
License:	GPL/LGPL
Group:		Databases
PreReq:		lib%name = %EVR
Provides:	%name-utils

%description -n %name-utils
FreeTDS is a free (open source) implementation of Sybase's db-lib,
ct-lib, and ODBC libraries. Currently, dblib and ctlib are most mature.  Both
of these libraries have several programs know to compile and run against them.

This package is built with support for TDS version %TDSVER and contains some
useful utilities.


%prep
%setup
%patch1 -p1
%patch2 -p2

%build
%add_optflags -fno-strict-aliasing
%autoreconf
%configure \
	--sysconfdir=%_sysconfdir/%name \
	--with-tdsver=%TDSVER \
	--enable-threadsafe \
	--enable-odbc \
	--disable-debug \
	--with-openssl \
	%{subst_enable static}

%make_build

%install
%makeinstall_std


%files -n lib%name
%_libdir/libct.so.4*
%_libdir/libsybdb.so.5*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/freetds.conf
%config(noreplace) %_sysconfdir/%name/locales.conf

%files -n lib%name-unixodbc
%_libdir/libtdsodbc.so.0*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files -n %name-utils
%doc %_docdir/%name/*
%config(noreplace) %_sysconfdir/%name/pool.conf
%_bindir/bsqlodbc
%_bindir/fisql
%_bindir/freebcp
%_bindir/tdspool
%_bindir/tsql
%_bindir/osql
%_bindir/bsqldb
%_bindir/defncopy
%_bindir/datacopy
%_man1dir/*
%_man5dir/*
%dir %_docdir/%name


%changelog
* Wed Dec 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.17-alt2
- Fixed datacopy functionality and logging.

* Wed Dec 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.17-alt1
- Updated to upstream version 1.2.17 (Fixes: CVE-2019-13508).

* Sun Sep 02 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.00.97-alt1
- New version

* Sun Aug 19 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.00.94-alt1
- New version (Closes: 32354)

* Mon Jun 10 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.91-alt3
- Rebuild with unixODBC 2.3.1

* Sun Apr 22 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.91-alt2
- Fix RPATH issues

* Wed Aug 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91-alt1
- Version 0.91

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.82-alt4
- Rebuilt for debuginfo

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.82-alt3
- Rebuilt for soname set-versions

* Sat Jun 13 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 0.82-alt2
- use OpenSSL instead of GnuTLS for built FreeTDS
- spec-file cleanup

* Tue Jun 10 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.82-alt1
- 0.82

* Thu Jan 24 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.64-alt3
- add configdir and configuration files, messed in alt2

* Mon Jan 14 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.64-alt2
- enable FreeTDS driver for unixODBC
- add libfreetds-unixodbc package

* Sat Dec 08 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 0.64-alt1
- new version -- 0.64

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.63-alt1.1.0
- Automated rebuild.

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.63-alt1.1
- Rebuilt with libreadline.so.5.

* Tue May 24 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 0.63-alt1
- new version -- 0.63
- do not build devel-static subpackage by default

* Tue Dec 21 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 0.62.4-alt1
- new version -- 0.62.4

* Sat May 22 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 0.62.3-alt1
- new version -- 0.62.3

* Mon Dec 15 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 0.61-alt2
- remove *.la files from package

* Wed Mar 05 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 0.61-alt1
- new version of FreeTDS -- 0.61

* Wed Oct 09 2002 Dmitry Lebkov <dlebkov@altlinux.ru> 0.60-alt1
- new version of FreeTDS

* Thu Mar 26 2002 Dmitry Lebkov <dima@sakhalin.ru> 0.53-alt1
- Package for ALT Linux
