Name: libraft
Version: 0.9.17
Release: alt1
Summary: Fully asynchronous C implementation of the Raft consensus protocol.
License: Apache-2.0
Group: Development/C
URL: https://github.com/canonical/raft

Source0: %name-%version.tar

BuildRequires: libuv-devel
BuildRequires: btrfs-progs xfsprogs zfs-utils

%define _unpackaged_files_terminate_build 1

%description
Fully asynchronous C implementation of the Raft consensus protocol.
The library has modular design: its core part implements only the core Raft
algorithm logic, in a fully platform independent way. On top of that, a
pluggable interface defines the I/O implementation for networking (send/receive
RPC messages) and disk persistence (store log entries and snapshots).

%package devel
Summary: Fully asynchronous C implementation of the Raft consensus protocol (development files)
Group: Development/C
Requires: %name = %version-%release

%description devel
Fully asynchronous C implementation of the Raft consensus protocol.
The library has modular design: its core part implements only the core Raft
algorithm logic, in a fully platform independent way. On top of that, a
pluggable interface defines the I/O implementation for networking (send/receive
RPC messages) and disk persistence (store log entries and snapshots).

%prep
%setup -q -n %name-%version

%build
%autoreconf
%configure --disable-static --disable-fixture

%make_build all

%install
%make_install install DESTDIR=%buildroot

%files
%doc AUTHORS README.md LICENSE
%_libdir/%name.so.*

%files devel
%_includedir/raft.h
%dir %_includedir/raft
%_includedir/raft/*
%_libdir/%name.so
%_pkgconfigdir/raft.pc

%changelog
* Tue Apr 14 2020 Alexey Shabalin <shaba@altlinux.org> 0.9.17-alt1
- Update to 0.9.17

* Wed Nov 13 2019 Denis Pynkin <dans@altlinux.org> 0.9.9-alt1
- Update

* Sun Sep 29 2019 Denis Pynkin <dans@altlinux.org> 0.9.6-alt1
- Initial version for ALTLinux
