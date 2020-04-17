Name: libdqlite
Version: 1.4.0
Release: alt1
Summary: Library for distributed SQLite database
License: Apache-2.0
Group: Development/Databases
URL: https://github.com/CanonicalLtd/dqlite

Source0: %name-%version.tar

BuildRequires: libuv-devel
BuildRequires: libraft-devel
BuildRequires: libco-devel
# Patched libsqlite3 version is required
BuildRequires: liblxd_sqlite3-devel

%define _unpackaged_files_terminate_build 1

%description
This package provides the `dqlite` C library (libdqlite), which can be used
to expose a SQLite database over the network and replicate it across a cluster
of peers, using the Raft algorithm.

%package devel
Summary: Library for distributed SQLite database (development files)
Group: Development/Databases
Requires: %name = %version-%release

%description devel
This package provides the `dqlite` C library (libdqlite), which can be used
to expose a SQLite database over the network and replicate it across a cluster
of peers, using the Raft algorithm.

%prep
%setup -q -n %name-%version

%build
%autoreconf
%configure --enable-replication --disable-static

%make_build all

%install
%make_install install DESTDIR=%buildroot

%files
%doc AUTHORS README.md LICENSE
%_libdir/%name.so.*

%files devel
%_includedir/dqlite.h
%_libdir/%name.so
%_pkgconfigdir/dqlite.pc

%changelog
* Tue Apr 14 2020 Alexey Shabalin <shaba@altlinux.org> 1.4.0-alt1
- Updated

* Tue Nov 12 2019 Denis Pynkin <dans@altlinux.org> 1.1.0-alt1
- Updated
- Added new build/runtime requirements to libraft and libco

* Sun Sep 29 2019 Denis Pynkin <dans@altlinux.org> 1.0.0-alt1
- Version 1.0.0

* Fri Jan 11 2019 Denis Pynkin <dans@altlinux.org> 0.2.5-alt1
- Initial version for ALTLinux
