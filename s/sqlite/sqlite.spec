%def_enable devel
%def_disable static

Name: sqlite
Version: 2.8.17
Release: alt2.4.1

Summary: An Embeddable SQL Database Engine, version 2
License: Public Domain
Group: Development/Databases

URL: http://www.sqlite.org
Source: sqlite-%version.tar.gz
Patch0: sqlite-2.8.17-cvs20070108.patch
Patch1: sqlite-2.8.17-CVE-2007-1888.patch
Patch2: sqlite-2.8.17-alt-libdir.patch
Patch3: sqlite-2.8.17-alt-tcl.patch
Patch4: sqlite-2.8.17-alt-sort+4.patch
Patch5: sqlite-2.8.17-deb-unsigned-char.patch
Patch6: sqlite-2.8.17-fc-64bit-fixes.patch
Patch7: sqlite-2.8.17-fc-test.patch
# https://sources.debian.org/data/main/s/sqlite/2.8.17-15/debian/patches/09-tcl8.6_compat.patch
Patch8: sqlite-2.8.17-deb-tcl8.6_compat.patch
Patch9: sqlite-2.8.17-fc-ppc64.patch
Patch10: sqlite-2.8.17-fc-cleanup-temp-c.patch
# https://sources.debian.org/data/main/s/sqlite/2.8.17-15/debian/patches/05-link_with_LDFLAGS.patch
Patch11: sqlite-2.8.17-deb-link_with_LDFLAGS.patch
Patch12: sqlite-2.8.17-suse-alt-cleanups.patch
Patch13: sqlite-2.8.17-suse-detect-sqlite3.patch
# prepare to GCC 10
Patch14: sqlite-2.8.17-fc-gcc10.patch
Patch15: sqlite-2.8.15-fc-arch-double-differences.patch

Requires: lib%name = %version-%release

# Automatically added by buildreq on Mon Feb 14 2011
BuildRequires: libncurses-devel libreadline-devel tcl-devel

%package -n lib%name
Summary: An Embeddable SQL Database Engine, version 2 (shared library)
Group: System/Libraries
Conflicts: %name < %version

%package -n lib%name-devel
Summary: An Embeddable SQL Database Engine, version 2 (header files)
Group: Development/Databases
Requires: lib%name = %version-%release
Provides: %name-devel = %version
Obsoletes: %name-devel < %version

%package -n lib%name-devel-static
Summary: An Embeddable SQL Database Engine, version 2 (static library)
Group: Development/Databases
Requires: lib%name-devel = %version-%release
Provides: %name-devel-static = %version
Obsoletes: %name-devel-static < %version

%package tcl
Summary: An Embeddable SQL Database Engine, version 2 (Tcl bindings)
Group: Development/Tcl
Requires: lib%name = %version-%release

%package doc
Summary: An Embeddable SQL Database Engine, version 2 (documentation)
Group: Development/Documentation
Conflicts: %name < %version
Buildarch: noarch

%description
SQLite is a C library that implements an SQL database engine.
Programs that link with the SQLite library can have SQL database
access without running a separate RDBMS process.

%description -n lib%name
SQLite is a C library that implements an SQL database engine.
Programs that link with the SQLite library can have SQL database
access without running a separate RDBMS process.

%description -n lib%name-devel
SQLite is a C library that implements an SQL database engine.
Programs that link with the SQLite library can have SQL database
access without running a separate RDBMS process.

%description -n lib%name-devel-static
SQLite is a C library that implements an SQL database engine.
Programs that link with the SQLite library can have SQL database
access without running a separate RDBMS process.

%description tcl
SQLite is a C library that implements an SQL database engine.
Programs that link with the SQLite library can have SQL database
access without running a separate RDBMS process.

%description doc
SQLite is a C library that implements an SQL database engine.
Programs that link with the SQLite library can have SQL database
access without running a separate RDBMS process.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

# lemon is now in sqlite3
rm doc/lemon.html

%build
export CFLAGS="%optflags"
autoreconf -fisv
%configure --enable-utf8 --enable-tempdb-in-ram %{subst_enable static}
%make_build all doc
%make_build libtcl%name.la tcllibdir=%_tcllibdir

%install
%makeinstall_std
install -pD -m644 %name.1 %buildroot%_man1dir/%name.1

mkdir -p %buildroot%_tcllibdir %buildroot%_tcldatadir/%name
./libtool --mode=install install -p libtcl%name.la %buildroot%_tcllibdir/

dll=$(relative %_tcllibdir/libtcl%name.so %_tcldatadir/%name/pkgIndex.tcl)
echo "package ifneeded sqlite 2.0 [list load [file join \$dir $dll]]" \
	>%buildroot%_tcldatadir/%name/pkgIndex.tcl

%define pkgdocdir %_docdir/sqlite-2.8
mkdir -p %buildroot%pkgdocdir
install -p -m644 doc/*.* %buildroot%pkgdocdir/

%check
rm test/date.test
make test

%files
%_bindir/%name
%_man1dir/%name.*

%files -n lib%name
%_libdir/lib%name.so.?*

%if_enabled devel
%files -n lib%name-devel
%_includedir/%name.h
%_libdir/lib%name.so
#_libdir/lib%name.la
%_pkgconfigdir/%name.pc
%endif

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%files tcl
%_tcllibdir/libtcl%name.so*
#_tcllibdir/libtcl%name.a
#_tcllibdir/libtcl%name.la
%dir %_tcldatadir/%name
%_tcldatadir/%name/pkgIndex.tcl

%files doc
%dir %pkgdocdir
%pkgdocdir/*.*

%changelog
* Fri Mar 06 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.8.17-alt2.4.1
- Backported from Sisyphus.
- Built with devel subpackage.

* Tue Feb 25 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.8.17-alt2.5
- Built without devel and devel-static subpackages.
- spec: Added export CFLAGS with %%optflags to %%build section.
- Enabled tests (without date.test).
- Applied a lot of patches from Debian, Fedora and openSUSE project.

* Mon Feb 04 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.8.17-alt2.4
- Fixed build on architectures with unsigned char.

* Fri Mar 24 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.8.17-alt2.3
- rebuilt against Tcl/Tk 8.6

* Mon Feb 14 2011 Alexey Tourbin <at@altlinux.ru> 2.8.17-alt2.2
- rebuilt for debuginfo
- made sqlite-doc noarch

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 2.8.17-alt2.1
- rebuild (with the help of girar-nmu utility)

* Fri Dec 12 2008 Denis Smirnov <mithraen@altlinux.ru> 2.8.17-alt2
- remove post_ldconfig/postun_ldconfig
- cleanup spec

* Wed Mar 26 2008 Alexey Tourbin <at@altlinux.ru> 2.8.17-alt1
- 2.8.16 -> 2.8.17+cvs20070108
- fix for buffer overflow in sqlite_decode_binary (CVE-2007-1888)
- split package sqlite-doc, renamed sqlite-devel to libsqlite-devel
- built with tcl 8.5

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 2.8.16-alt1.1.0
- Automated rebuild.

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.8.16-alt1.1
- Rebuilt with libreadline.so.5.

* Sat Mar 12 2005 Denis Smirnov <mithraen@altlinux.ru> 2.8.16-alt1
- version update

* Thu Feb 10 2005 Denis Smirnov <mithraen@altlinux.ru> 2.8.15-alt2
- fix version in sqlite.pc

* Fri Feb 04 2005 Denis Smirnov <mithraen@altlinux.ru> 2.8.15-alt1
- version update
- build requires rpm-build-tcl

* Sat Sep 04 2004 Denis Smirnov <mithraen@altlinux.ru> 2.8.13-alt5
- x86_64 build fixed

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
