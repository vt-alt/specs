Name: libntirpc
Version: 1.7.3
Release: alt1

Summary: New Transport Independent RPC Library

Group: System/Libraries
License: BSD
Url: https://github.com/nfs-ganesha/ntirpc

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/nfs-ganesha/ntirpc/archive/v%version/ntirpc-%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: libjemalloc-devel
BuildRequires: libkrb5-devel
BuildRequires: libnsl2-devel

# libtirpc has /etc/netconfig, most machines probably have it anyway
# for NFS client
Requires: libtirpc

%description
This package contains a new implementation of the original libtirpc,
transport-independent RPC (TI-RPC) library for NFS-Ganesha. It has
the following features not found in libtirpc:
 1. Bi-directional operation
 2. Full-duplex operation on the TCP (vc) transport
 3. Thread-safe operating modes
 3.1 new locking primitives and lock callouts (interface change)
 3.2 stateless send/recv on the TCP transport (interface change)
 4. Flexible server integration support
 5. Event channels (remove static arrays of xprt handles, new EPOLL/KEVENT
    integration)

%package devel
Summary: Development headers for %name
Requires: %name = %version
Group: Development/Other

%description devel
Development headers and auxiliary files for developing with %name.

%prep
%setup

%build
%cmake -DOVERRIDE_INSTALL_PREFIX=%prefix -DTIRPC_EPOLL=1 -DUSE_GSS=ON "-GUnix Makefiles"

%make_build -C BUILD

%install
%makeinstall_std -C BUILD

rm -f %buildroot%_includedir/ntirpc/misc/winpthreads.h
ln -s %name.so.%version %buildroot%_libdir/%name.so.1

%files
%_libdir/libntirpc.so.*
%doc COPYING
%doc NEWS README

%files devel
%_libdir/libntirpc.so
%_includedir/ntirpc/
%_pkgconfigdir/libntirpc.pc

%changelog
* Fri May 17 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.3-alt1
- new version 1.7.3 (with rpmrb script)

* Wed Mar 27 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- new version 1.7.2 (with rpmrb script)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt1
- new version 1.7.1 (with rpmrb script)

* Sun Sep 30 2018 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- new version 1.7.0 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt1
- new version 1.6.2 (with rpmrb script)

* Fri Jul 28 2017 Vitaly Lipatov <lav@altlinux.ru> 1.5.3-alt1
- new version 1.5.3 (with rpmrb script)

* Sun Jun 11 2017 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- new version 1.5.2 (with rpmrb script)

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- new version 1.4.1 (with rpmrb script)

* Thu Jul 21 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt2
- cleanup install

* Thu Jul 21 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- initial build for ALT Linux Sisyphus

* Mon Feb 29 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> 1.4.0-0.2pre2
- libntirpc 1.4.0-pre2

* Fri Feb 5 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> 1.4.0-0.1pre1
- libntirpc 1.4.0-pre1, correct release

* Fri Feb 5 2016 Kaleb S. KEITHLEY <kkeithle at redhat.com> 1.4.0-1pre1
- libntirpc 1.4.0-pre1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 9 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com>
- Requires: libtirpc for /etc/netconfig (most already have it)

* Mon Oct 26 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 1.3.1-1
- libntirpc 1.3.1 GA

* Fri Oct 9 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 1.3.0-3
- libntirpc 1.3.0 GA, w/ -DTIRPC_EPOLL=ON

* Wed Sep 9 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 1.3.0-2
- libntirpc 1.3.0 GA, w/ correct top-level CMakeList.txt

* Wed Sep 9 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 1.3.0-1
- libntirpc 1.3.0 GA

* Thu Jul 16 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 1.2.1-3
- RHEL 6 finally has new enough cmake
- use -isystem ... to ensure correct <rpc/rpc*.h> are used
- ensure -DTIRPC_EPOLL is defined for correct evchan functionality

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Kaleb S. KEITHLEY <kkeithle at redhat.com> 1.2.1-1
- Initial commit
