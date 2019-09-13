%def_disable static

Name: sqlite3
Version: 3.29.0
Release: alt1
Summary: An Embeddable SQL Database Engine
License: Public Domain
Group: Development/Databases
URL: http://www.sqlite.org/

Requires: lib%name = %version-%release

Source0: sqlite-%version.tar

Patch1: 0001-FEDORA-no-malloc-usable-size.patch
Patch2: 0002-FEDORA-percentile-test.patch
Patch3: 0003-FEDORA-ALT-datetest-2.2c.patch
Patch4: 0004-DEBIAN-fix-division-by-zero-in-the-query-planner.patch
Patch5: 0005-ALT-tcl.patch
Patch6: 0006-ALT-build-dependencies.patch

BuildRequires(Pre): tcl-devel
BuildRequires: libreadline-devel
# need for test
BuildRequires: zlib-devel unzip

%define _unpackaged_files_terminate_build 1

%description
SQLite is a C library that implements an SQL database engine.
Programs that link with the SQLite library can have SQL database
access without running a separate RDBMS process.

%package -n lib%name
Summary: An Embeddable SQL Database Engine (shared library)
Group: System/Libraries
Provides: sqlite(SECURE_DELETE) sqlite(COLUMN_METADATA) sqlite(FTS3) sqlite(UNLOCK_NOTIFY)
Provides: %name-fts3 = %version-%release
Obsoletes: %name-fts3 < %version-%release

%description -n lib%name
SQLite is a C library that implements an SQL database engine.
Programs that link with the SQLite library can have SQL database
access without running a separate RDBMS process.

%package -n lib%name-devel
Summary: An Embeddable SQL Database Engine (header files)
Group: Development/Databases
Requires: lib%name = %version-%release

%description -n lib%name-devel
SQLite is a C library that implements an SQL database engine.
Programs that link with the SQLite library can have SQL database
access without running a separate RDBMS process.

%package -n lib%name-devel-static
Summary: An Embeddable SQL Database Engine (static library)
Group: Development/Databases
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
SQLite is a C library that implements an SQL database engine.
Programs that link with the SQLite library can have SQL database
access without running a separate RDBMS process.

%package tcl
Summary: An Embeddable SQL Database Engine (TCL bindings)
Group: Development/Tcl
Requires: lib%name = %version-%release

%description tcl
SQLite is a C library that implements an SQL database engine.
Programs that link with the SQLite library can have SQL database
access without running a separate RDBMS process.

%package doc
Summary: An Embeddable SQL Database Engine (documentation)
Group: Development/Documentation
Conflicts: %name < 3.3.8-alt1
BuildArch: noarch

%description doc
SQLite is a C library that implements an SQL database engine.
Programs that link with the SQLite library can have SQL database
access without running a separate RDBMS process.

%package -n lemon
Summary: The Lemon Parser Generator
Group: Development/Other

%description -n lemon
Lemon is an LALR(1) parser generator for C or C++. It does the same
job as bison and yacc. But lemon is not another bison or yacc
clone. It uses a different grammar syntax which is designed to reduce
the number of coding errors. Lemon also uses a more sophisticated
parsing engine that is faster than yacc and bison and which is both
reentrant and thread-safe. Furthermore, Lemon implements features
that can be used to eliminate resource leaks, making is suitable for
use in long-running programs such as graphical user interfaces or
embedded controllers.

%prep
%setup -q -n sqlite-%version
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2
%patch5 -p2
%patch6 -p2

%build
export TCLLIBDIR=%_tcllibdir
export TCLDATADIR=%_tcldatadir/%name
export CFLAGS="%optflags \
	-DSQLITE_CORE=1 \
	-DSQLITE_ENABLE_API_ARMOR=1 \
	-DSQLITE_ENABLE_COLUMN_METADATA=1 \
	-DSQLITE_ENABLE_DBSTAT_VTAB=1 \
	-DSQLITE_ENABLE_DESERIALIZE=1 \
	-DSQLITE_ENABLE_FTS3=1 \
	-DSQLITE_ENABLE_JSON1=1 \
	-DSQLITE_ENABLE_UNLOCK_NOTIFY=1 \
	-DSQLITE_SECURE_DELETE=1 \
	-fno-strict-aliasing "
%ifarch %e2k
# FIXME: lcc-1.23 lacks some gcc5 builtins
cc --version | grep -q '^lcc:1.21' || export CFLAGS+="-D__INTEL_COMPILER=1"
%endif
autoreconf -i
%configure \
	%{subst_enable static} \
	--disable-amalgamation \
	--enable-fts5 \
	--enable-load-extension \
	--enable-readline \
	--enable-threadsafe \
	#

%make_build all

%check
subst 's|-DSQLITE_ENABLE_FTS3=1||' Makefile
%make test

%install
%make_install install tcl_install DESTDIR=%buildroot

install -pD -m644 %name.1 %buildroot%_man1dir/%name.1

install -pD -m755 lemon %buildroot%_bindir/lemon
install -pD -m644 lempar.c %buildroot%_datadir/lemon/lempar.c

# for perl-DBD-SQLite
install -p -m644 ext/fts3/fts3.h ext/fts3/fts3_*.h %buildroot%_includedir/

%define pkgdocdir %_docdir/%name
mkdir -p %buildroot%pkgdocdir
cp -a doc %buildroot%pkgdocdir/html
install -pD -m644 doc/lemon.html %buildroot%_docdir/lemon/lemon.html

%files
%_bindir/%name
%_man1dir/%name.*

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/sqlite3.h
%_includedir/sqlite3ext.h
%_includedir/fts3.h
%_includedir/fts3_*.h
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif # static

%files tcl
%_tcllibdir/libtcl%name.so*
%_tcllibdir/sqlite3

%files doc
%pkgdocdir

%files -n lemon
%dir %_docdir/lemon
%_docdir/lemon/lemon.html
%_bindir/lemon
%_datadir/lemon

%changelog
* Tue Sep 03 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.29.0-alt1
- 3.29.0.
- Fixed loading of sqlite3 Tcl extension (pointed nbr@).
- Applied patch 40-fix-division-by-zero-in-the-query-planner.patch from Debian.
- Made more proper patch to disable date test 2.2c on ix86.
- Rediffed patches.

* Sun Jun 02 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.28.0-alt1
- 3.28.0 (Fixes: CVE-2019-9936, CVE-2019-9937)

* Fri Mar 22 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.27.2-alt1
- 3.27.2 (closes: #36341)
- enabled API armor and deserialize interface
- explicitly enabled readline
- disabled static library build

* Fri Feb 01 2019 Alexandr Antonov <aas@altlinux.org> 3.26.0-alt2
- Enable JSON1

* Sat Jan 12 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.26.0-alt1
- 3.26.0

* Wed Jan 09 2019 Michael Shigorin <mike@altlinux.org> 3.25.2-alt3
- E2K: avoid gcc5 builtins not implemented in lcc-1.23

* Tue Oct 16 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.25.2-alt2
- Enable DBSTAT_VTAB

* Thu Sep 27 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.25.2-alt1
- 2.25.2

* Thu Sep 06 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.24.0-alt1
- 3.24.0
- Drop patches that were based on upstream commits cause the are alredy in the
  source code:
  + sqlite3-3.22.0-fedora-int-float-compare.patch
  + sqlite3-3.22.0-fedora-corrupt-schema.patch
- Sync sqlite-3.7.7.1-fedora-stupid-openfiles-test.patch with Fedora

* Sun Mar 25 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.22.0-alt1
- 3.22.0
- Patches from Fedora:
  + sqlite-3.7.7.1-stupid-openfiles-test.patch
  + sqlite-3.22.0-int-float-compare.patch
  + sqlite-3.22.0-corrupt-schema.patch
- Fixes:
  + CVE-2017-15286 a NULL pointer dereference in tableColumnList

* Wed Sep 13 2017 Mikhail Efremov <sem@altlinux.org> 3.20.1-alt2
- Enable FTS5 support (closes: #33885).

* Mon Aug 28 2017 Mikhail Efremov <sem@altlinux.org> 3.20.1-alt1
- 3.20.1.

* Fri Jul 14 2017 Mikhail Efremov <sem@altlinux.org> 3.19.3-alt1
- 3.19.3.

* Mon Apr 03 2017 Mikhail Efremov <sem@altlinux.org> 3.18.0-alt1
- Disable test date-2.2c on i586.
- 3.18.0.

* Tue Jan 10 2017 Mikhail Efremov <sem@altlinux.org> 3.16.2-alt1
- 3.16.2.

* Tue Nov 29 2016 Mikhail Efremov <sem@altlinux.org> 3.15.2-alt1
- 3.15.2.

* Thu Nov 10 2016 Mikhail Efremov <sem@altlinux.org> 3.15.1-alt1
- 3.15.1.

* Wed Oct 26 2016 Mikhail Efremov <sem@altlinux.org> 3.15.0-alt1
- 3.15.0.

* Wed Sep 14 2016 Mikhail Efremov <sem@altlinux.org> 3.14.2-alt1
- 3.14.2.

* Mon Aug 22 2016 Mikhail Efremov <sem@altlinux.org> 3.14.1-alt1
- 3.14.1.

* Mon Jun 20 2016 Mikhail Efremov <sem@altlinux.org> 3.13.0-alt1
- 3.13.0.

* Fri Apr 22 2016 Mikhail Efremov <sem@altlinux.org> 3.12.2-alt1
- Update sqlite3-fedora-no-malloc-usable-size.patch.
- 3.12.2 (closes: #31984).

* Fri Mar 04 2016 Mikhail Efremov <sem@altlinux.org> 3.11.1-alt1
- 3.11.1.

* Wed Mar 02 2016 Mikhail Efremov <sem@altlinux.org> 3.11.0-alt1
- 3.11.0.

* Fri Jan 22 2016 Mikhail Efremov <sem@altlinux.org> 3.10.2-alt1
- 3.10.2.

* Mon Jan 11 2016 Mikhail Efremov <sem@altlinux.org> 3.10.0-alt1
- 3.10.0.

* Thu Dec 17 2015 Mikhail Efremov <sem@altlinux.org> 3.9.2-alt1
- 3.9.2.

* Wed May 27 2015 Mikhail Efremov <sem@altlinux.org> 3.8.10.2-alt1
- Update sqlite3-fedora-no-malloc-usable-size.patch.
- 3.8.10.2.

* Wed Apr 29 2015 Mikhail Efremov <sem@altlinux.org> 3.8.9-alt1
- Update sqlite3-fedora-no-malloc-usable-size.patch.
- Drop obsoleted fts3 patch.
- 3.8.9.

* Wed Feb 19 2014 Mikhail Efremov <sem@altlinux.org> 3.8.3.1-alt1
- Patches from Fedora:
  + Temporary workaround for failed percentile test.
  + Disable malloc_usable_size() usage.
- Drop sqlite3-alt-version-script.patch.
- 3.8.3.1.

* Tue Jan 15 2013 Valery Inozemtsev <shrek@altlinux.ru> 3.7.15.2-alt1
- 3.7.15.2 (closes: #27231)

* Mon Apr 25 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.7.6.2-alt2
- fixed fts3 patch

* Mon Apr 25 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.7.6.2-alt1
- 3.7.6.2

* Tue Feb 15 2011 Alexey Tourbin <at@altlinux.ru> 3.7.4-alt2
- rebuilt for debuginfo
- disabled symbol versioning
- packaged fts3 headers, for perl-DBD-SQLite

* Tue Jan 25 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.7.4-alt1
- 3.7.4

* Thu Nov 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 3.7.2-alt2
- rebuild

* Tue Sep 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 3.7.2-alt1
- 3.7.2

* Thu Aug 12 2010 Valery Inozemtsev <shrek@altlinux.ru> 3.7.0.1-alt1
- 3.7.0.1

* Thu Jul 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 3.6.23.1-alt3
- added provides sqlite(SECURE_DELETE), sqlite(COLUMN_METADATA), sqlite(FTS3), sqlite(UNLOCK_NOTIFY)

* Wed Jun 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 3.6.23.1-alt2
- enabled unlock notify

* Thu May 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 3.6.23.1-alt1
- 3.6.23.1

* Wed Jan 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 3.6.22-alt1
- 3.6.22

* Tue Dec 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.6.21-alt1
- 3.6.21

* Thu Nov 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.6.20-alt1
- 3.6.20

* Mon Oct 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.6.19-alt1
- 3.6.19

* Mon Sep 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.6.18-alt3
- don't hide "sqlite3[A-Z]*" symbols

* Sun Sep 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.6.18-alt2
- enabled column metadata

* Sun Sep 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.6.18-alt1
- 3.6.18

* Wed Sep 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.6.17-alt2
- moved "make test" to %%check section

* Wed Aug 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.6.17-alt1
- 3.6.17
- enabled tests

* Tue Jun 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.6.16-alt1
- 3.6.16
- full-text search extension compiled in library

* Sun Oct 12 2008 Alexey Tourbin <at@altlinux.ru> 3.5.9-alt3
- backported from cvs:
  + fix for DISTINCT on indexes (RH#463061, deb#500792)
  + improved NaN testing for highly optimized GCC on x86 (deb#488864)
  + tclsqlite.test works reliably with tcl 8.5.4
- set correct version in pkgIndex.tcl (deb#483990)

* Fri Jul 04 2008 Alexey Tourbin <at@altlinux.ru> 3.5.9-alt2
- sqlite3.pc: provide full version (#16268)
- made sqlite3-doc package noarch

* Sat May 24 2008 Alexey Tourbin <at@altlinux.ru> 3.5.9-alt1
- 3.4.2 -> 3.5.9
- upgraded fts2 subpackage to fts2
- merged new documentation from http://sqlite.org/docsrc/

* Fri Aug 17 2007 Alexey Tourbin <at@altlinux.ru> 3.4.2-alt1
- 3.4.1+cvs20070803 -> 3.4.2

* Sun Aug 05 2007 Alexey Tourbin <at@altlinux.ru> 3.4.1-alt2
- 3.4.1+cvs20070720 -> 3.4.1+cvs20070803

* Sat Jul 21 2007 Alexey Tourbin <at@altlinux.ru> 3.4.1-alt1
- 3.3.17+ -> 3.4.1+cvs20070720 (fixes multiple vulnerabilities
  discovered by the Google Security team)
- changed src.rpm packaging to keep separate tarball with cvs snapshot

* Fri Apr 27 2007 Alexey Tourbin <at@altlinux.ru> 3.3.17-alt1
- 3.3.15 -> 3.3.17+

* Tue Apr 10 2007 Alexey Tourbin <at@altlinux.ru> 3.3.15-alt1
- 3.3.14+ -> 3.3.15
- re-enabled exclusive2.test

* Tue Apr 03 2007 Alexey Tourbin <at@altlinux.ru> 3.3.14-alt1
- 3.3.13+ -> 3.3.14+
- disabled -fno-strict-aliasing since the code has been fixed
- disabled exclusive2.test and types3.test

* Tue Feb 20 2007 Alexey Tourbin <at@altlinux.ru> 3.3.13-alt1
- 3.3.12 -> 3.3.13+

* Sun Jan 28 2007 Alexey Tourbin <at@altlinux.ru> 3.3.12-alt1
- 3.3.11 -> 3.3.12

* Tue Jan 23 2007 Alexey Tourbin <at@altlinux.ru> 3.3.11-alt1
- 3.3.10+ -> 3.3.11
- sqlite3-doc: packaged missing html files

* Thu Jan 11 2007 Alexey Tourbin <at@altlinux.ru> 3.3.10-alt1
- 3.3.8+ -> 3.3.10+

* Wed Nov 15 2006 Alexey Tourbin <at@altlinux.ru> 3.3.8-alt2
- 3.3.8+ cvs snapshot
- enabled full text search backend (sqlite3-fts2 package)

* Sat Oct 21 2006 Alexey Tourbin <at@altlinux.ru> 3.3.8-alt1
- imported cvs sources with git-cvsimport; applied my changes
  to the source tree and built with gear
- this release is based on sqlite version 3.3.8
- changed documentation packaging: introduced sqlite3-doc package; moved
  lemon.html to lemon package; added COPYING, which was compiled from
  various sources; sqlite is still public domain, with a few minor issues

* Sun Aug 13 2006 Alexey Tourbin <at@altlinux.ru> 3.3.7-alt1
- 3.3.6 -> 3.3.7

* Wed Jun 07 2006 Alexey Tourbin <at@altlinux.ru> 3.3.6-alt1
- 3.3.5 -> 3.3.6
- compiled with -fno-strict-aliasing (debian #364196)
- linked libtclsqlite3.so with libtcl.so

* Sun Apr 16 2006 Alexey Tourbin <at@altlinux.ru> 3.3.5-alt1
- 3.3.4 -> 3.3.5; sync debian sqlite3_3.3.5-0.1
- urgency=high (for lib%name >= 3.3): hacked sqlite3_prepare() to keep
  old code work; try "sqlite3_prepare nBytes" web search for details
- restricted list of symbols exported by the library;
  introduced symbol versioning
- fixed libtcl%name linkage (eliminated internal lib%name copy)
- improved temporary file handling
- new package: lemon (LALR parser generator)

* Thu Mar 09 2006 Denis Smirnov <mithraen@altlinux.ru> 3.3.4-alt1
- 3.2.6 -> 3.3.4

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.2.6-alt1.1
- Rebuilt with libreadline.so.5.

* Sat Sep 24 2005 Alexey Tourbin <at@altlinux.ru> 3.2.6-alt1
- 3.2.5 -> 3.2.6; urgency=medium

* Mon Aug 29 2005 Alexey Tourbin <at@altlinux.ru> 3.2.5-alt1
- 3.2.2 -> 3.2.5

* Fri Jun 24 2005 Alexey Tourbin <at@altlinux.ru> 3.2.2-alt1
- 3.2.1 -> 3.2.2
- enabled thread-safety (--enable-threadsafe configure option)
- removed --enable-utf8 configure option (has no effect)

* Wed Apr 06 2005 Alexey Tourbin <at@altlinux.ru> 3.2.1-alt1
- 3.1.3 -> 3.2.1

* Fri Mar 04 2005 Alexey Tourbin <at@altlinux.ru> 3.1.3-alt1
- 3.0.8 -> 3.1.3

* Fri Nov 26 2004 Alexey Tourbin <at@altlinux.ru> 3.0.8-alt1.1
- fixed tcl bindings (patch by Sergey Bolshakov)

* Thu Oct 21 2004 Alexey Tourbin <at@altlinux.ru> 3.0.8-alt1
- 3.0.6 -> 3.0.8
- alt-makefile.patch merged upstream (sqlite ticket #903 for `mkdir -p',
  sqlite ticket #904 for libdir/lib64)
- added post/postun ldconfig scripts

* Thu Sep 16 2004 Alexey Tourbin <at@altlinux.ru> 3.0.6-alt1
- 3.0.4 -> 3.0.6
- hopefully should build on x86_64

* Fri Aug 13 2004 Alexey Tourbin <at@altlinux.ru> 3.0.4-alt1
- 2.8.13 -> 3.0.4 (beta), renamed to sqlite3

* Fri Jun 04 2004 Denis Smirnov <mithraen@altlinux.ru> 2.8.13-alt4
- Rebuild

* Thu Jun 03 2004 Denis Smirnov <mithraen@altlinux.ru> 2.8.13-alt2
- Fix for correcting update

* Mon May 31 2004 Denis Smirnov <mithraen@altlinux.ru> 2.8.13-alt1
- Some minor packaging fixes
- Tcl binding bugfix

* Sun Apr 11 2004 Denis Smirnov <mithraen@altlinux.ru> 2.8.5-alt3
- Tcl binding build

* Sat Dec 13 2003 Ott Alex <ott@altlinux.ru> 2.8.5-alt2
- Remove .la files

* Sun Jul 27 2003 Ott Alex <ott@altlinux.ru> 2.8.5-alt1
- New version

* Tue Jul 22 2003 Ott Alex <ott@altlinux.ru> 2.8.4-alt1
- Initial build
