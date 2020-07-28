%define sysmodprobedir /lib/modprobe.d
%define _libexecdir  /usr/libexec
%define _localstatedir %_var

%ifnarch %arm %mips %e2k riscv64
%def_enable dma_coherent
%else
%def_disable dma_coherent
%endif


Name: rdma-core
Version: 30.0
Release: alt3
Summary: RDMA core userspace libraries and daemons
Group: System/Base

# Almost everything is licensed under the OFA dual GPLv2, 2 Clause BSD license
#  providers/ipathverbs/ Dual licensed using a BSD license with an extra patent clause
#  providers/rxe/ Incorporates code from ipathverbs and contains the patent clause
#  providers/hfi1verbs Uses the 3 Clause BSD license
License: GPL-2.0-only OR BSD-2-Clause
Url: https://github.com/linux-rdma/rdma-core
Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires: binutils
BuildRequires: cmake >= 2.8.11 rpm-macros-cmake
BuildRequires: ninja-build rpm-macros-ninja-build
BuildRequires: libudev-devel
BuildRequires: pkgconfig(libnl-3.0)
BuildRequires: pkgconfig(libnl-route-3.0)
BuildRequires: libsystemd-devel
BuildRequires: /usr/bin/rst2man
BuildRequires: pandoc
Conflicts: infiniband-diags < 2.0.0

%define docdir %_docdir/%name-%version

%description
RDMA core userspace infrastructure and documentation, including initialization
scripts, kernel driver-specific modprobe override configs, IPoIB network
scripts, and the rdma-ndd utility.

%package devel
Summary: RDMA core development libraries and headers
Group: Development/C
Requires: %name = %EVR
Requires: libibverbs = %EVR
Provides: libibverbs-devel = %EVR
Obsoletes: libibverbs-devel < %EVR
Requires: libibumad = %EVR
Provides: libibumad-devel = %EVR
Obsoletes: libibumad-devel < %EVR
Requires: librdmacm = %EVR
Provides: librdmacm-devel = %EVR
Obsoletes: librdmacm-devel < %EVR
Requires: ibacm = %EVR
Provides: ibacm-devel = %EVR
Obsoletes: ibacm-devel < %EVR
Requires: libibmad = %EVR
Provides: libibmad-devel = %EVR
Obsoletes: libibmad-devel < %EVR
Provides: libibnetdisc-devel = %EVR
Obsoletes: libibnetdisc-devel < %EVR
Provides: libinfiniband-diags-devel = %EVR
Obsoletes: libinfiniband-diags-devel < %EVR

%description devel
RDMA core development libraries and headers.

%package -n libibverbs
Summary: A library and drivers for direct userspace use of RDMA (InfiniBand/iWARP/RoCE) hardware
Group: System/Libraries
Provides: libcxgb4 = %EVR
Obsoletes: libcxgb4 < %EVR
Provides: libipathverbs = %EVR
Obsoletes: libipathverbs < %EVR
%if_enabled dma_coherent
Provides: libmlx4 = %EVR
Obsoletes: libmlx4 < %EVR
%ifnarch s390x
Provides: libmlx5 = %EVR
Obsoletes: libmlx5 < %EVR
%endif
%endif
Provides: libmthca = %EVR
Obsoletes: libmthca < %EVR

%description -n libibverbs
libibverbs is a library that allows userspace processes to use RDMA
"verbs" as described in the InfiniBand Architecture Specification and
the RDMA Protocol Verbs Specification.  This includes direct hardware
access from userspace to InfiniBand/iWARP adapters (kernel bypass) for
fast path operations.

Device-specific plug-in ibverbs userspace drivers are included:

- libcxgb4: Chelsio T4 iWARP HCA
- libhfi1: Intel Omni-Path HFI
- libhns: HiSilicon Hip06 SoC
- libi40iw: Intel Ethernet Connection X722 RDMA
- libipathverbs: QLogic InfiniPath HCA
- libmlx4: Mellanox ConnectX-3 InfiniBand HCA (except arm, s390)
- libmlx5: Mellanox Connect-IB/X-4+ InfiniBand HCA (except arm, s390, s390x)
- libmthca: Mellanox InfiniBand HCA
- libocrdma: Emulex OneConnect RDMA/RoCE Device
- libqedr: QLogic QL4xxx RoCE HCA
- librxe: A software implementation of the RoCE protocol
- libsiw: A software implementation of the iWarp protocol
- libvmw_pvrdma: VMware paravirtual RDMA device

%package -n libibverbs-utils
Summary: Examples for the libibverbs library
Group: System/Base
Requires: libibverbs = %EVR

%description -n libibverbs-utils
Useful libibverbs example programs such as ibv_devinfo, which
displays information about RDMA devices.

%package -n ibacm
Summary: InfiniBand Communication Manager Assistant
Group: Networking/Other
Requires: %name = %EVR

%description -n ibacm
The ibacm daemon helps reduce the load of managing path record lookups on
large InfiniBand fabrics by providing a user space implementation of what
is functionally similar to an ARP cache.  The use of ibacm, when properly
configured, can reduce the SA packet load of a large IB cluster from O(n^2)
to O(n).  The ibacm daemon is started and normally runs in the background,
user applications need not know about this daemon as long as their app
uses librdmacm to handle connection bring up/tear down.  The librdmacm
library knows how to talk directly to the ibacm daemon to retrieve data.

%package -n iwpmd
Summary: iWarp Port Mapper userspace daemon
Group: Networking/Other
Requires: %name = %EVR

%description -n iwpmd
iwpmd provides a userspace service for iWarp drivers to claim
tcp ports through the standard socket interface.

%package -n libibumad
Summary: OpenFabrics Alliance InfiniBand umad (userspace management datagram) library
Group: System/Libraries

%description -n libibumad
libibumad provides the userspace management datagram (umad) library
functions, which sit on top of the umad modules in the kernel. These
are used by the IB diagnostic and management tools, including OpenSM.

%package -n libibmad
Summary: library to encode, decode, and dump IB MAD packets
Group: System/Libraries
Conflicts: libinfiniband-diags =< 2.2.0-alt1 

%description -n libibmad
libibmad is a convenience library to encode, decode, and dump IB MAD packets.
It is implemented on top of libibumad.

%package -n libibnetdisc
Summary: Infiniband Net Discovery runtime library
Group: System/Libraries
Conflicts: libinfiniband-diags =< 2.2.0-alt1 

%description -n libibnetdisc
This package contains the Infiniband Net Discovery runtime library needed
mainly by infiniband-diags.

%package -n librdmacm
Summary: Userspace RDMA Connection Manager
Group: System/Libraries

%description -n librdmacm
librdmacm provides a userspace RDMA Communication Management API.

%package -n librdmacm-utils
Summary: Examples for the librdmacm library
Group: System/Base
Requires: librdmacm = %EVR

%description -n librdmacm-utils
Example test programs for the librdmacm library.

%package -n infiniband-diags
Summary: OpenFabrics InfiniBand Diagnostic Tools
Group: System/Base
Provides: openib-diags = %version
Obsoletes: openib-diags
Conflicts: libinfiniband-diags =< 2.2.0-alt1 

%description -n infiniband-diags
This package provides IB diagnostic programs and scripts needed to
diagnose an IB subnet.

%package -n infiniband-diags-compat
Group: System/Base
Summary: OpenFabrics Alliance InfiniBand Diagnostic Tools

%description -n infiniband-diags-compat
Deprecated scripts and utilities which provide duplicated functionality, most
often at a reduced performance. These are maintained for the time being for
compatibility reasons.

%package -n srp_daemon
Summary: Tools for using the InfiniBand SRP protocol devices
Group: Networking/Other
Obsoletes: srptools <= 1.0.3
Provides: srptools = %EVR
Requires: %name = %EVR

%description -n srp_daemon
In conjunction with the kernel ib_srp driver, srp_daemon allows you to
discover and use SCSI devices via the SCSI RDMA Protocol over InfiniBand.

%prep
%setup
%patch -p1

%build

# Pass all of the rpm paths directly to GNUInstallDirs and our other defines.
%cmake_insource \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_BINDIR:PATH=%_bindir \
    -DCMAKE_INSTALL_SBINDIR:PATH=%_sbindir \
    -DCMAKE_INSTALL_LIBDIR:PATH=%_libdir \
    -DCMAKE_INSTALL_LIBEXECDIR:PATH=%_libexecdir \
    -DCMAKE_INSTALL_LOCALSTATEDIR:PATH=%_localstatedir \
    -DCMAKE_INSTALL_SHAREDSTATEDIR:PATH=%_sharedstatedir \
    -DCMAKE_INSTALL_INCLUDEDIR:PATH=%_includedir \
    -DCMAKE_INSTALL_INFODIR:PATH=%_infodir \
    -DCMAKE_INSTALL_MANDIR:PATH=%_mandir \
    -DCMAKE_INSTALL_SYSCONFDIR:PATH=%_sysconfdir \
    -DCMAKE_INSTALL_SYSTEMD_SERVICEDIR:PATH=%_unitdir \
    -DCMAKE_INSTALL_INITDDIR:PATH=%_initdir \
    -DCMAKE_INSTALL_RUNDIR:PATH=%_runtimedir \
    -DCMAKE_INSTALL_DOCDIR:PATH=%docdir \
    -DCMAKE_INSTALL_UDEV_RULESDIR:PATH=%_udevrulesdir \
    -DCMAKE_INSTALL_PERLDIR:PATH=%perl_vendor_privlib \
    -DENABLE_IBDIAGS_COMPAT:BOOL=True \

%ninja_build

%install
%ninja_install

mkdir -p %buildroot%_sysconfdir/rdma

mkdir -p %buildroot%_sysconfdir/udev/rules.d
mkdir -p %buildroot%_libexecdir
mkdir -p %buildroot%_udevrulesdir
mkdir -p %buildroot%sysmodprobedir
install -D -m0644 redhat/rdma.conf %buildroot%_sysconfdir/rdma/rdma.conf
install -D -m0644 redhat/rdma.sriov-vfs %buildroot%_sysconfdir/rdma/sriov-vfs
%if_enabled dma_coherent
install -D -m0644 redhat/rdma.mlx4.conf %buildroot%_sysconfdir/rdma/mlx4.conf
install -D -m0644 redhat/rdma.mlx4.sys.modprobe %buildroot%sysmodprobedir/libmlx4.conf
install -D -m0755 redhat/rdma.mlx4-setup.sh %buildroot%_libexecdir/mlx4-setup.sh
%endif
install -D -m0755 alt/rdma.init %buildroot%_initdir/rdma
install -D -m0644 redhat/rdma.service %buildroot%_unitdir/rdma.service
install -D -m0644 redhat/rdma.udev-rules %buildroot%_udevrulesdir/98-rdma.rules
install -D -m0755 alt/rdma.kernel-init %buildroot%_libexecdir/rdma-init-kernel
install -D -m0755 redhat/rdma.sriov-init %buildroot%_libexecdir/rdma-set-sriov-vf

install -D -m0755 alt/ibacm.init %buildroot%_initdir/ibacm
install -D -m0755 alt/iwpmd.init %buildroot%_initdir/iwpmd
install -D -m0755 alt/rdma-ndd.init %buildroot%_initdir/rdma-ndd
install -D -m0755 alt/srpd.init %buildroot%_initdir/srpd
ln -r -s %buildroot%_unitdir/srp_daemon.service %buildroot%_unitdir/srpd.service

# ibacm
LD_LIBRARY_PATH="lib" bin/ib_acme -D . -O
install -D -m0644 ibacm_opts.cfg %buildroot%_sysconfdir/rdma/

# copy linux kernel headers to /usr/include/rdma
cp -r kernel-headers/rdma %buildroot%_includedir/

%post -n ibacm
%post_service ibacm
%preun -n ibacm
%preun_service ibacm

%post -n srp_daemon
%post_service srp_daemon
%preun -n srp_daemon
%preun_service srp_daemon

%post -n iwpmd
%post_service iwpmd
%preun -n iwpmd
%preun_service iwpmd

%files
%dir %docdir
%dir %_sysconfdir/rdma
%dir %_sysconfdir/rdma/modules
%docdir/README.md
%docdir/rxe.md
%docdir/udev.md
%docdir/tag_matching.md
%if_enabled dma_coherent
%config(noreplace) %_sysconfdir/rdma/mlx4.conf
%config(noreplace) %_sysconfdir/modprobe.d/mlx4.conf
%sysmodprobedir/libmlx4.conf
%_libexecdir/mlx4-setup.sh
%endif
%config(noreplace) %_sysconfdir/rdma/modules/infiniband.conf
%config(noreplace) %_sysconfdir/rdma/modules/iwarp.conf
%config(noreplace) %_sysconfdir/rdma/modules/opa.conf
%config(noreplace) %_sysconfdir/rdma/modules/rdma.conf
%config(noreplace) %_sysconfdir/rdma/modules/roce.conf
%config(noreplace) %_sysconfdir/rdma/rdma.conf
%config(noreplace) %_sysconfdir/rdma/sriov-vfs
%config(noreplace) %_sysconfdir/udev/rules.d/*
%config(noreplace) %_sysconfdir/modprobe.d/truescale.conf
%_unitdir/rdma-hw.target
%_unitdir/rdma-load-modules@.service
%_unitdir/rdma.service
%_initdir/rdma
%_udevrulesdir/../rdma_rename
%_udevrulesdir/60-rdma-ndd.rules
%_udevrulesdir/60-rdma-persistent-naming.rules
%_udevrulesdir/75-rdma-description.rules
%_udevrulesdir/90-rdma-hw-modules.rules
%_udevrulesdir/90-rdma-ulp-modules.rules
%_udevrulesdir/90-rdma-umad.rules
%_udevrulesdir/98-rdma.rules
%_libexecdir/rdma-init-kernel
%_libexecdir/rdma-set-sriov-vf
%_libexecdir/truescale-serdes.cmds
%_sbindir/rdma-ndd
%_unitdir/rdma-ndd.service
%_initdir/rdma-ndd
%_man7dir/rxe*
%_man8dir/rdma-ndd.*

%files devel
%docdir/MAINTAINERS
%dir %_includedir/infiniband
%dir %_includedir/rdma
%_includedir/infiniband/*
%_includedir/rdma/*
%_libdir/lib*.so
%_pkgconfigdir/*.pc
%_man3dir/ibv_*
%_man3dir/rdma*
%_man3dir/umad*
%_man3dir/*_to_ibv_rate.*
%_man7dir/rdma_cm.*
%_man3dir/ibnd_*
%if_enabled dma_coherent
%_man3dir/efadv*
%_man7dir/efadv*
%_man3dir/mlx5dv*
%_man7dir/mlx5dv*
%_man3dir/mlx4dv*
%_man7dir/mlx4dv*
%endif

%files -n libibverbs
%dir %_sysconfdir/libibverbs.d
%dir %_libdir/libibverbs
%_libdir/libibverbs*.so.*
%_libdir/libibverbs/*.so
%if_enabled dma_coherent
%_libdir/libefa.so.*
%_libdir/libmlx5.so.*
%_libdir/libmlx4.so.*
%endif
%config(noreplace) %_sysconfdir/libibverbs.d/*.driver
%docdir/libibverbs.md

%files -n libibverbs-utils
%_bindir/ibv_*
%_man1dir/ibv_*

%files -n ibacm
%config(noreplace) %_sysconfdir/rdma/ibacm_opts.cfg
%_bindir/ib_acme
%_sbindir/ibacm
%_man1dir/ib_acme.*
%_man7dir/ibacm.*
%_man7dir/ibacm_prov.*
%_man8dir/ibacm.*
%_unitdir/ibacm.service
%_unitdir/ibacm.socket
%_initdir/ibacm
%dir %_libdir/ibacm
%_libdir/ibacm/*
%docdir/ibacm.md

%files -n iwpmd
%_sbindir/iwpmd
%_unitdir/iwpmd.service
%_initdir/iwpmd
%config(noreplace) %_sysconfdir/rdma/modules/iwpmd.conf
%config(noreplace) %_sysconfdir/iwpmd.conf
%_udevrulesdir/90-iwpmd.rules
%_man8dir/iwpmd.*
%_man5dir/iwpmd.*

%files -n libibumad
%_libdir/libibumad*.so.*

%files -n libibmad
%_libdir/libibmad*.so.*

%files -n libibnetdisc
%_libdir/libibnetdisc*.so.*

%files -n librdmacm
%_libdir/librdmacm*.so.*
%dir %_libdir/rsocket
%_libdir/rsocket/*.so*
%docdir/librdmacm.md
%_man7dir/rsocket.*

%files -n librdmacm-utils
%_bindir/cmtime
%_bindir/mckey
%_bindir/rcopy
%_bindir/rdma_client
%_bindir/rdma_server
%_bindir/rdma_xclient
%_bindir/rdma_xserver
%_bindir/riostream
%_bindir/rping
%_bindir/rstream
%_bindir/ucmatose
%_bindir/udaddy
%_bindir/udpong
%_man1dir/cmtime.*
%_man1dir/mckey.*
%_man1dir/rcopy.*
%_man1dir/rdma_client.*
%_man1dir/rdma_server.*
%_man1dir/rdma_xclient.*
%_man1dir/rdma_xserver.*
%_man1dir/riostream.*
%_man1dir/rping.*
%_man1dir/rstream.*
%_man1dir/ucmatose.*
%_man1dir/udaddy.*
%_man1dir/udpong.*

%files -n infiniband-diags-compat
%_sbindir/ibcheckerrs
%_man8dir/ibcheckerrs*
%_sbindir/ibchecknet
%_man8dir/ibchecknet*
%_sbindir/ibchecknode
%_man8dir/ibchecknode*
%_sbindir/ibcheckport
%_man8dir/ibcheckport.*
%_sbindir/ibcheckportwidth
%_man8dir/ibcheckportwidth*
%_sbindir/ibcheckportstate
%_man8dir/ibcheckportstate*
%_sbindir/ibcheckwidth
%_man8dir/ibcheckwidth*
%_sbindir/ibcheckstate
%_man8dir/ibcheckstate*
%_sbindir/ibcheckerrors
%_man8dir/ibcheckerrors*
%_sbindir/ibdatacounts
%_man8dir/ibdatacounts*
%_sbindir/ibdatacounters
%_man8dir/ibdatacounters*
%_sbindir/ibdiscover.pl
%_man8dir/ibdiscover*
%_sbindir/ibswportwatch.pl
%_man8dir/ibswportwatch*
%_sbindir/ibqueryerrors.pl
%_sbindir/iblinkinfo.pl
%_sbindir/ibprintca.pl
%_man8dir/ibprintca*
%_sbindir/ibprintswitch.pl
%_man8dir/ibprintswitch*
%_sbindir/ibprintrt.pl
%_man8dir/ibprintrt*
%_sbindir/set_nodedesc.sh

%files -n infiniband-diags
%_sbindir/ibaddr
%_man8dir/ibaddr*
%_sbindir/ibnetdiscover
%_man8dir/ibnetdiscover*
%_sbindir/ibping
%_man8dir/ibping*
%_sbindir/ibportstate
%_man8dir/ibportstate*
%_sbindir/ibroute
%_man8dir/ibroute.*
%_sbindir/ibstat
%_man8dir/ibstat.*
%_sbindir/ibsysstat
%_man8dir/ibsysstat*
%_sbindir/ibtracert
%_man8dir/ibtracert*
%_sbindir/perfquery
%_man8dir/perfquery*
%_sbindir/sminfo
%_man8dir/sminfo*
%_sbindir/smpdump
%_man8dir/smpdump*
%_sbindir/smpquery
%_man8dir/smpquery*
%_sbindir/saquery
%_man8dir/saquery*
%_sbindir/vendstat
%_man8dir/vendstat*
%_sbindir/iblinkinfo
%_man8dir/iblinkinfo*
%_sbindir/ibqueryerrors
%_man8dir/ibqueryerrors*
%_sbindir/ibcacheedit
%_man8dir/ibcacheedit*
%_sbindir/ibccquery
%_man8dir/ibccquery*
%_sbindir/ibccconfig
%_man8dir/ibccconfig*
%_sbindir/dump_fts
%_man8dir/dump_fts*
%_sbindir/ibhosts
%_man8dir/ibhosts*
%_sbindir/ibswitches
%_man8dir/ibswitches*
%_sbindir/ibnodes
%_man8dir/ibnodes*
%_sbindir/ibrouters
%_man8dir/ibrouters*
%_sbindir/ibfindnodesusing.pl
%_man8dir/ibfindnodesusing*
%_sbindir/ibidsverify.pl
%_man8dir/ibidsverify*
%_sbindir/check_lft_balance.pl
%_man8dir/check_lft_balance*
%_sbindir/dump_lfts.sh
%_man8dir/dump_lfts*
%_sbindir/dump_mfts.sh
%_man8dir/dump_mfts*
%_sbindir/ibclearerrors
%_man8dir/ibclearerrors*
%_sbindir/ibclearcounters
%_man8dir/ibclearcounters*
%_sbindir/ibstatus
%_man8dir/ibstatus*
%_man8dir/infiniband-diags*
%perl_vendor_privlib/IBswcountlimits.pm
%config(noreplace) %_sysconfdir/infiniband-diags/error_thresholds
%config(noreplace) %_sysconfdir/infiniband-diags/ibdiag.conf


%files -n srp_daemon
%config(noreplace) %_sysconfdir/srp_daemon.conf
%config(noreplace) %_sysconfdir/rdma/modules/srp_daemon.conf
%_libexecdir/srp_daemon/start_on_all_ports
%_unitdir/srp_daemon.service
%_unitdir/srpd.service
%_unitdir/srp_daemon_port@.service
%_initdir/srpd
%_sbindir/ibsrpdm
%_sbindir/srp_daemon
%_sbindir/run_srp_daemon
%_udevrulesdir/60-srp_daemon.rules
%_man5dir/srp_daemon.service.*
%_man5dir/srp_daemon_port@.service.*
%_man8dir/ibsrpdm.*
%_man8dir/srp_daemon.*
%docdir/ibsrpdm.md

%changelog
* Mon Jul 27 2020 Alexey Shabalin <shaba@altlinux.org> 30.0-alt3
- add provides and obsoletes libinfiniband-diags-devel to devel package

* Wed Jul 22 2020 Alexey Shabalin <shaba@altlinux.org> 30.0-alt2
- not provides and obsoletes of libinfiniband-diags

* Thu Jul 02 2020 Alexey Shabalin <shaba@altlinux.org> 30.0-alt1
- 30.0

* Sat Apr 18 2020 Alexey Shabalin <shaba@altlinux.org> 29.0-alt1
- 29.0

* Fri Feb 21 2020 Alexey Shabalin <shaba@altlinux.org> 28.0-alt1
- 28.0

* Sun Dec 15 2019 Alexey Shabalin <shaba@altlinux.org> 27.0-alt1
- 27.0
- merged infiniband-diags project

* Wed Jul 03 2019 Nikita Ermakov <arei@altlinux.org> 24.0-alt3
- fix build on riscv64

* Fri Jun 14 2019 Rustem Bapin <rbapin@altlinux.org> 24.0-alt2
- move efa* in %files under dma_coherent define for fix build on mipsel

* Sat Jun 01 2019 Alexey Shabalin <shaba@altlinux.org> 24.0-alt1
- 24.0

* Mon May 27 2019 Michael Shigorin <mike@altlinux.org> 22-alt2.1
- fix build on e2k

* Sat Jan 19 2019 Alexey Shabalin <shaba@altlinux.org> 22-alt2
- add symlinks to linux kernel headers
- fixed path in pkconfig files

* Thu Jan 17 2019 Alexey Shabalin <shaba@altlinux.org> 22-alt1
- 22

* Tue Oct 30 2018 Alexey Shabalin <shaba@altlinux.org> 20.1-alt1
- 20.1

* Wed Jun 27 2018 Alexey Shabalin <shaba@altlinux.ru> 18.1-alt1
- 18.1

* Tue Mar 13 2018 Alexey Shabalin <shaba@altlinux.ru> 17.1-alt1
- Initial build

