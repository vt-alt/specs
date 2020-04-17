Name: lxd_sqlite3
Version: 3.31.1
Release: alt1
Summary: An Embeddable SQL Database Engine with WAL replication
License: Public Domain
Group: Development/Databases
URL: https://github.com/CanonicalLtd/sqlite

Requires: lib%name = %version-%release

Source0: %name-%version.tar

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

%prep
%setup -q -n %name-%version

%build
autoreconf -i
%configure \
	--enable-replication \
	--disable-amalgamation \
	--disable-tcl \
	--libdir=%_libdir/lxd \
	--includedir=%_includedir/lxd


# Generate manifest files
date -r . --iso-8601=seconds > manifest
sha1sum manifest | cut -f 1 -d ' ' > manifest.uuid

%make_build all

%install
%make_install install DESTDIR=%buildroot
mkdir -p %buildroot/%_pkgconfigdir
mv %buildroot/%_libdir/lxd/pkgconfig/sqlite3.pc %buildroot/%_pkgconfigdir/%name.pc

# Remove unneeded
rm -f %buildroot/%_bindir/sqlite3
rm -f %buildroot/%_libdir/lxd/libsqlite3.*a
rm -rf %buildroot/%_libdir/lxd/pkgconfig

%files -n lib%name
%_libdir/lxd/libsqlite3.so.*

%files -n lib%name-devel
%_includedir/lxd/sqlite3.h
%_includedir/lxd/sqlite3ext.h
%_libdir/lxd/libsqlite3.so
%_pkgconfigdir/%name.pc

%changelog
* Tue Apr 14 2020 Alexey Shabalin <shaba@altlinux.org> 3.31.1-alt1
- Merged with version-3.31.1+replication4

* Tue Nov 12 2019 Denis Pynkin <dans@altlinux.org> 3.30.1-alt1
- Rebased on version-3.30.1+replication4 with unrelated history

* Sun Sep 29 2019 Denis Pynkin <dans@altlinux.org> 3.29.0-alt1
- Merged version-3.29.0+replication3

* Mon Apr 29 2019 Denis Pynkin <dans@altlinux.org> 3.26.0-alt2
- Removed unneeded provides

* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 3.26.0-alt1
- Version with enabled WAL replication needed for LXD.
- Based on original sqlite3 spec file for ALTLinux
