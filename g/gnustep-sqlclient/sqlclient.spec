# should use generic java rpath;
%def_without java
%set_verify_elf_method unresolved=strict
Name: gnustep-sqlclient
Version: 1.7.0
Release: alt8.svn20140221.1
Summary: Provide a simple interface to SQL databases for GNUstep applications
License: LGPLv3+
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
# gnustep is not built on aarch64
ExclusiveArch: %{ix86} x86_64

# http://svn.gna.org/svn/gnustep/libs/sqlclient/trunk/
Source: %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires: clang-devel gnustep-make-devel gnustep-base-devel
BuildRequires: libgnustep-objc2-devel gnustep-performance-devel /proc
BuildRequires: postgresql-devel libsqlite3-devel
BuildRequires: libMySQL-devel
%if_with java
BuildRequires: java-devel-default
%endif

Requires: lib%name = %version-%release
Requires: gnustep-back

%description
The SQLClient library is designed to provide a simple interface to SQL
databases for GNUstep applications. It does not attempt the sort of
abstraction provided by the much more sophisticated GDL2 library but
rather allows applications to directly execute SQL queries and
statements.

%package -n lib%name
Summary: Shared libraries of GNUstep SQLClient
Group: System/Libraries

%description -n lib%name
The SQLClient library is designed to provide a simple interface to SQL
databases for GNUstep applications. It does not attempt the sort of
abstraction provided by the much more sophisticated GDL2 library but
rather allows applications to directly execute SQL queries and
statements.

This package contains shared libraries of SQLClient.

%package -n lib%name-devel
Summary: Development files of GNUstep SQLClient
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release
Requires: %name = %version-%release

%description -n lib%name-devel
The SQLClient library is designed to provide a simple interface to SQL
databases for GNUstep applications. It does not attempt the sort of
abstraction provided by the much more sophisticated GDL2 library but
rather allows applications to directly execute SQL queries and
statements.

This package contains shared libraries of SQLClient.

%package doc
Summary: Documentation for GNUstep SQLClient
Group: Development/Documentation
BuildArch: noarch

%description doc
The SQLClient library is designed to provide a simple interface to SQL
databases for GNUstep applications. It does not attempt the sort of
abstraction provided by the much more sophisticated GDL2 library but
rather allows applications to directly execute SQL queries and
statements.

This package contains documentation for SQLClient.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

export LD_LIBRARY_PATH=$(dirname $(find %_jvmdir -name libjvm.so) \
	|egrep server)
%autoreconf
%configure \
	--libexecdir=%_libdir \
	--with-postgres-dir=%prefix \
	--with-additional-include=-I%_includedir/pgsql \
%if_with java
%ifarch x86_64
	--with-jre-architecture=amd64 \
%else
	--with-jre-architecture=i386 \
%endif
%endif
	--with-installation-domain=SYSTEM

libSQLClient=$PWD/obj/libSQLClient.so

buildIt() {
	%make_build \
		messages=yes \
		debug=yes \
		strip=no \
		shared=yes \
		CONFIG_SYSTEM_LIBS="$1 -lPerformance -lgnustep-base -lobjc2"
}

buildIt
for i in SQLite MySQL \
%if_with java
	JDBC_libs \
	JDBC \
%endif
	Postgres ECPG
do
	rm -f $(find ./ -name $i -type f)
done
buildIt $libSQLClient
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std messages=yes GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%doc ChangeLog README
%_libdir/GNUstep

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files doc
%_docdir/GNUstep

%changelog
* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt8.svn20140221.1
- NMU: disabled java support as it links and generates dependencies with
  JVM's name and release; should use /usr/lib/jvm/jre/lib/<jarch> as RPATH
  or do not link with JVM at all.

* Mon Jun 25 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt7.svn20140221.1
- NMU: rebuild with new openjdk java

* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt6.svn20140221.1
- NMU: rebuild with new openjdk java

* Sun Nov 08 2015 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt5.svn20140221.1
- rebuild with java-1.6.0-devel

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt5.svn20140221
- Fixed build

* Sat Jun 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt4.svn20140221.1
- rebuild with new openjdk java

* Wed Apr 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt4.svn20140221
- Rebuilt with postgresql9.3

* Tue Mar 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt3.svn20140221
- New snapshot

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt3.svn20130910
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt2.svn20130910
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt2.git20130910
- Rebuilt with new gnustep-gui

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.git20130910
- Version 1.7.0

* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.git20130304
- Version 1.6.1

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt3.git20121129
- Rebuilt with libobjc2 instead of libobjc

* Fri Dec 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt2.git20121129
- Rebuild with updated gnustep-mak

* Thu Dec 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20121129
- Initial build for Sisyphus

