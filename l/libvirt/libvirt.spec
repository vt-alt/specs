%define _unpackaged_files_terminate_build 1

# like subst_with, but replacing '_' with '-'
%define subst_with_dash() %{expand:%%(echo '%%{subst_with %1}' | sed 's/_/-/g')}

%define _localstatedir /var
%define _libexecdir %_prefix/libexec
%define qemu_user  _libvirt
%define qemu_group  vmusers

# A client only build will create a libvirt.so only containing
# the generic RPC driver, and test driver and no libvirtd
# Default to a full server + client build

%ifarch %ix86 x86_64 ia64 armh aarch64 ppc64le
%def_enable server_drivers
%else
%def_disable server_drivers
%endif

# Always build with dlopen'd modules
%def_with driver_modules

%if_enabled server_drivers
# First the daemon itself
%def_with libvirtd

# Then the hypervisor drivers that run on local host
%def_with qemu
%def_with openvz
%def_with lxc
%if_with lxc
%def_with login_shell
%else
%def_without login_shell
%endif
%ifarch %ix86 x86_64
%def_with vbox
%else
%def_without vbox
%endif
%def_without libxl
%ifarch %ix86 x86_64
%def_with vmware
%else
%def_without vmware
%endif

# Then the hypervisor drivers that talk via a native remote protocol
%def_with phyp
%ifarch %ix86 x86_64
%def_with esx
%else
%def_without esx
%endif
%def_without hyperv
%def_without xenapi


# Then the secondary host drivers
%def_with network
%def_with storage_fs
%def_with storage_lvm
%def_with storage_scsi
%def_with storage_iscsi
%def_with storage_iscsi_direct
%def_with storage_disk
%ifarch x86_64 aarch64 ppc64le
%def_with storage_rbd
%else
%def_without storage_rbd
%endif
%def_with storage_mpath
%def_with storage_gluster
%def_with storage_zfs
%def_without storage_sheepdog
%def_without storage_vstorage
%ifarch %ix86 x86_64 ppc64le
%def_with numactl
%else
%def_without numactl
%endif
%def_with selinux

# A few optional bits
%def_without netcf
%def_with udev
%def_without hal
%def_with yajl
%def_with sanlock
%if_enabled lxc
%def_with fuse
%else
%def_without fuse
%endif
%def_with pm_utils

%else  #server_drivers
%def_without libvirtd
%def_without qemu
%def_without openvz
%def_without lxc
%def_without login_shell
%def_without vbox
%def_without libxl
%def_without vmware
%def_without phyp
%def_without esx
%def_without hyperv
%def_without xenapi
%def_without network
%def_without storage_fs
%def_without storage_lvm
%def_without storage_scsi
%def_without storage_iscsi
%def_without storage_iscsi_direct
%def_without storage_disk
%def_without storage_rbd
%def_without storage_mpath
%def_without storage_gluster
%def_without storage_zfs
%def_without storage_sheepdog
%def_without storage_vstorage
%def_without numactl
%def_with selinux

%def_without netcf
%def_without udev
%def_without hal
%def_with yajl
%def_without sanlock
%def_without fuse
%def_with pm_utils
%endif #server_drivers

%if_with  qemu
%def_with qemu_tcg

%ifarch %ix86 x86_64 armh aarch64 ppc64le
%def_with qemu_kvm
%endif
%endif

# A few optional bits
%def_with dbus
%def_with polkit
%def_with capng
%def_with firewalld
%def_without firewalld_zone

%if_with qemu || lxc
%def_with nwfilter
%def_with libpcap
%else
%def_without nwfilter
%def_without libpcap
%endif

%def_with libnl
%if_with qemu
%def_with macvtap
%else
%def_without macvtap
%endif

%def_with audit
%def_without dtrace

# Non-server/HV driver defaults which are always enabled
%def_with sasl
%def_with libssh

%def_without wireshark
%def_without bash_completion

# nss plugin depends on network
%if_with network
%def_with nss_plugin
%else
%def_without nss_plugin
%endif

Name: libvirt
Version: 5.6.0
Release: alt1
Summary: Library providing a simple API virtualization
License: LGPLv2+
Group: System/Libraries
Url: https://libvirt.org/
Source0: %name-%version.tar
Source1: gnulib-%name-%version.tar
Source2: keycodemapdb-%name-%version.tar

Source11: libvirtd.init
Source12: virtlockd.init
Source13: virtlogd.init
Source14: libvirt-guests.init

Patch1: %name-%version.patch


%{?_with_libvirtd:Requires: %name-daemon = %EVR}
%{?_with_network:Requires: %name-daemon-config-network = %EVR}
%{?_with_nwfilter:Requires: %name-daemon-config-nwfilter = %EVR}
%{?_with_qemu:Requires: %name-qemu-common = %EVR}
%{?_with_polkit:Requires: polkit}
Requires: %name-client = %EVR
Requires: %name-libs = %EVR

%{?_with_libxl:BuildRequires: xen-devel}
%{?_with_hal:BuildRequires: libhal-devel}
%{?_with_udev:BuildRequires: udev libudev-devel >= 219 libpciaccess-devel}
%{?_with_yajl:BuildRequires: libyajl-devel >= 2.0.1}
%{?_with_sanlock:BuildRequires: sanlock-devel >= 1.8}
%{?_with_libpcap:BuildRequires: libpcap-devel}
%{?_with_libnl:BuildRequires: libnl-devel}
%{?_with_selinux:BuildRequires: libselinux-devel}
%{?_with_network:BuildRequires: dnsmasq iptables iptables-ipv6 radvd openvswitch}
%{?_with_nwfilter:BuildRequires: ebtables}
%{?_with_sasl:BuildRequires: libsasl2-devel >= 2.1.6}
%{?_with_libssh:BuildRequires: pkgconfig(libssh) >= 0.7}
%{?_with_dbus:BuildRequires: libdbus-devel >= 1.0.0}
%{?_with_polkit:BuildRequires: polkit}
%{?_with_storage_fs:BuildRequires: util-linux}
%{?_with_qemu:BuildRequires: qemu-img}
%{?_with_storage_lvm:BuildRequires: lvm2}
%{?_with_storage_disk:BuildRequires: libparted-devel parted libuuid-devel dmsetup libdevmapper-devel}
%{?_with_storage_rbd:BuildRequires: ceph-devel}
%{?_with_storage_iscsi:BuildRequires: open-iscsi}
%{?_with_storage_iscsi_direct:BuildRequires: libiscsi-devel >= 1.18.0}
%{?_with_storage_mpath:BuildRequires: libdevmapper-devel}
%{?_with_storage_gluster:BuildRequires: libglusterfs6-devel}
%{?_with_storage_zfs:BuildRequires: zfs-utils}
%{?_with_storage_vstorage:BuildRequires: /usr/sbin/vstorage}
%{?_with_numactl:BuildRequires: libnuma-devel}
%{?_with_capng:BuildRequires: libcap-ng-devel}
%{?_with_phyp:BuildRequires: libssh2-devel}
%{?_with_netcf:BuildRequires: netcf-devel}
%{?_with_esx:BuildRequires: libcurl-devel}
%{?_with_hyperv:BuildRequires: libwsman-devel}
%{?_with_audit:BuildRequires: libaudit-devel}
%{?_with_fuse:BuildRequires: libfuse-devel >= 2.8.6}
%{?_with_pm_utils:BuildRequires: pm-utils}
%{?_with_wireshark:BuildRequires: glib2-devel wireshark tshark wireshark-devel >= 2.1.0}
%{?_with_bash_completion:BuildRequires: pkgconfig(bash-completion) >= 2.0}

BuildRequires: /proc
BuildRequires: bridge-utils libblkid-devel
BuildRequires: libgcrypt-devel libgnutls-devel >= 3.2.0 libp11-kit-devel
BuildRequires: libreadline-devel
BuildRequires: libtasn1-devel
BuildRequires: libattr-devel attr
BuildRequires: libacl-devel
BuildRequires: perl-Pod-Parser perl-XML-XPath
BuildRequires: libxml2-devel xml-utils xsltproc
BuildRequires: python3 python3-devel
BuildRequires: zlib-devel
BuildRequires: iproute2 perl-Pod-Parser
BuildRequires: dmidecode
BuildRequires: libtirpc-devel
BuildRequires: glibc-utils
BuildRequires: kmod
BuildRequires: radvd
BuildRequires: dnsmasq
BuildRequires: libxfs-devel

%description
Libvirt is a C toolkit to interact with the virtualization capabilities
of recent versions of Linux (and other OSes).
The main package includes the libvirtd server exporting the virtualization support.

%package docs
Summary: Documentation for libvirt library and daemon
Group: Development/Documentation
BuildArch: noarch

%description docs
Copy of the libvirt website documentation

%package daemon
Summary: Server side daemon and supporting files for libvirt library
Group: System/Servers
Requires: %name-libs = %EVR
Requires: iptables
%{?_with_pm_utils:Requires: pm-utils}
Requires: dmidecode
# libvirtd depends on 'messagebus' service
Requires: dbus

%description daemon
Server side daemon required to manage the virtualization capabilities
of recent versions of Linux. Requires a hypervisor specific sub-RPM
for specific drivers.

%package daemon-config-network
Summary: Default configuration files for the libvirtd daemon
Group: System/Servers
BuildArch: noarch
Requires: bridge-utils
Requires: dnsmasq
%if_with driver_modules
Requires: %name-daemon-driver-network = %EVR
%endif

%description daemon-config-network
Default configuration files for setting up NAT based networking

%package daemon-config-nwfilter
Summary: Network filter configuration files for the libvirtd daemon
Group: System/Servers
BuildArch: noarch
%if_with driver_modules
Requires: %name-daemon-driver-nwfilter = %EVR
%endif

%description daemon-config-nwfilter
Network filter configuration files for cleaning guest traffic

%if_with driver_modules
%if_with network
%package daemon-driver-network
Summary: Network driver plugin for the libvirtd daemon
Group: System/Libraries
Requires: %name-daemon = %EVR

%description daemon-driver-network
The network driver plugin for the libvirtd daemon, providing
an implementation of the virtual network APIs using the Linux
bridge capabilities.
%endif

%if_with nwfilter
%package daemon-driver-nwfilter
Summary: Nwfilter driver plugin for the libvirtd daemon
Group: System/Libraries
Requires: ebtables
Requires: %name-daemon = %EVR

%description daemon-driver-nwfilter
The nwfilter driver plugin for the libvirtd daemon, providing
an implementation of the firewall APIs using the ebtables,
iptables and ip6tables capabilities
%endif

%if_with udev
%package daemon-driver-nodedev
Summary: Nodedev driver plugin for the libvirtd daemon
Group: System/Libraries
Requires: %name-daemon = %EVR

%description daemon-driver-nodedev
The nodedev driver plugin for the libvirtd daemon, providing
an implementation of the node device APIs using the udev
capabilities.

%package daemon-driver-interface
Summary: Interface driver plugin for the libvirtd daemon
Group: System/Libraries
Requires: %name-daemon = %EVR

%description daemon-driver-interface
The interface driver plugin for the libvirtd daemon, providing
an implementation of the network interface APIs using the
netcf library or udev.
%endif

%package daemon-driver-secret
Summary: Secret driver plugin for the libvirtd daemon
Group: System/Libraries
Requires: %name-daemon = %EVR

%description daemon-driver-secret
The secret driver plugin for the libvirtd daemon, providing
an implementation of the secret key APIs.

%package daemon-driver-storage
Summary: Storage driver plugin including all backends for the libvirtd daemon
Group: System/Libraries
%if_with storage_fs
Requires: %name-daemon-driver-storage-fs = %EVR
%endif
%if_with storage_disk
Requires: %name-daemon-driver-storage-disk = %EVR
%endif
%if_with storage_lvm
Requires: %name-daemon-driver-storage-logical = %EVR
%endif
%if_with storage_scsi
Requires: %name-daemon-driver-storage-scsi = %EVR
%endif
%if_with storage_iscsi
Requires: %name-daemon-driver-storage-iscsi = %EVR
%endif
%if_with storage_iscsi_direct
Requires: %name-daemon-driver-storage-iscsi-direct = %EVR
%endif
%if_with storage_mpath
Requires: %name-daemon-driver-storage-mpath = %EVR
%endif
%if_with storage_gluster
Requires: %name-daemon-driver-storage-gluster = %EVR
%endif
%if_with storage_rbd
Requires: %name-daemon-driver-storage-rbd = %EVR
%endif
%if_with storage_sheepdog
Requires: %name-daemon-driver-storage-sheepdog = %EVR
%endif

%description daemon-driver-storage
The storage driver plugin for the libvirtd daemon, providing
an implementation of the storage APIs using files, local disks, LVM, SCSI,
iSCSI, and multipath storage.

%package daemon-driver-storage-core
Summary: Storage driver plugin including base backends for the libvirtd daemon
Group: System/Libraries
Requires: %name-daemon = %EVR
Requires: nfs-utils
# For mkfs
Requires: util-linux
%{?_with qemu:Requires: /usr/bin/qemu-img}

%description daemon-driver-storage-core
The storage driver plugin for the libvirtd daemon, providing
an implementation of the storage APIs.

%package daemon-driver-storage-fs
Summary: Storage driver plugin for fs
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR

%description daemon-driver-storage-fs
The storage driver backend adding implementation of the storage APIs for block
volumes using fs.

%package daemon-driver-storage-logical
Summary: Storage driver plugin for lvm volumes
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR
Requires: lvm2

%description daemon-driver-storage-logical
The storage driver backend adding implementation of the storage APIs for block
volumes using lvm.

%package daemon-driver-storage-disk
Summary: Storage driver plugin for disk
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR
Requires: parted
Requires: dmsetup

%description daemon-driver-storage-disk
The storage driver backend adding implementation of the storage APIs for block
volumes using the host disks.

%package daemon-driver-storage-scsi
Summary: Storage driver plugin for local scsi devices
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR

%description daemon-driver-storage-scsi
The storage driver backend adding implementation of the storage APIs for scsi
host devices.

%package daemon-driver-storage-iscsi
Summary: Storage driver plugin for iscsi
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR
Requires: iscsi-initiator-utils

%description daemon-driver-storage-iscsi
The storage driver backend adding implementation of the storage APIs for iscsi
volumes using the host iscsi stack.

%package daemon-driver-storage-iscsi-direct
Summary: Storage driver plugin for iscsi-direct
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR

%description daemon-driver-storage-iscsi-direct
The storage driver backend adding implementation of the storage APIs for iscsi
volumes using libiscsi direct connection.

%package daemon-driver-storage-mpath
Summary: Storage driver plugin for multipath volumes
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR
Requires: dmsetup
Requires: multipath-tools

%description daemon-driver-storage-mpath
The storage driver backend adding implementation of the storage APIs for
multipath storage using device mapper.

%package daemon-driver-storage-gluster
Summary: Storage driver plugin for gluster
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR
Requires: glusterfs6

%description daemon-driver-storage-gluster
The storage driver backend adding implementation of the storage APIs for gluster
volumes using libgfapi.

%package daemon-driver-storage-rbd
Summary: Storage driver plugin for rbd
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR

%description daemon-driver-storage-rbd
The storage driver backend adding implementation of the storage APIs for rbd
volumes using the ceph protocol.

%package daemon-driver-storage-sheepdog
Summary: Storage driver plugin for sheepdog
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR
Requires: sheepdog

%description daemon-driver-storage-sheepdog
The storage driver backend adding implementation of the storage APIs for
sheepdog volumes using.

%package daemon-driver-storage-zfs
Summary: Storage driver plugin for zfs
Group: System/Libraries
Requires: libvirt-daemon-driver-storage-core = %EVR

%description daemon-driver-storage-zfs
The storage driver backend adding implementation of the storage APIs for
zfs volumes using.

%if_with qemu
%package daemon-driver-qemu
Summary: Qemu driver plugin for the libvirtd daemon
Group: System/Libraries
Requires: %name-daemon-driver-network = %EVR
Requires: %name-daemon-driver-storage-fs = %EVR
Requires: /usr/bin/qemu-img
Requires: qemu-kvm-core
# For image compression
Requires: gzip
Requires: bzip2
Requires: xz

%description daemon-driver-qemu
The qemu driver plugin for the libvirtd daemon, providing
an implementation of the hypervisor driver APIs using
QEMU
%endif

%if_with lxc
%package daemon-driver-lxc
Summary: LXC driver plugin for the libvirtd daemon
Group: System/Libraries
Requires: %name-daemon-driver-network = %EVR
Requires: %name-daemon = %EVR

%description daemon-driver-lxc
The LXC driver plugin for the libvirtd daemon, providing
an implementation of the hypervisor driver APIs using
the Linux kernel
%endif

%if_with libxl
%package daemon-driver-libxl
Summary: Libxl driver plugin for the libvirtd daemon
Group: System/Libraries
Obsoletes: %name-daemon-driver-xen < 4.3.0
Requires: %name-daemon = %EVR

%description daemon-driver-libxl
The Libxl driver plugin for the libvirtd daemon, providing
an implementation of the hypervisor driver APIs using
Libxl
%endif

%if_with vbox
%package daemon-driver-vbox
Summary: VirtualBox driver plugin for the libvirtd daemon
Group: System/Libraries
Requires: %name-daemon = %EVR

%description daemon-driver-vbox
The vbox driver plugin for the libvirtd daemon, providing
an implementation of the hypervisor driver APIs using
VirtualBox
%endif

%endif #driver_modules

%package qemu-common
Summary: Server side daemon, driver & default configs required to run QEMU or KVM guests
Group: System/Servers
BuildArch: noarch
Requires: %name-daemon-config-network = %EVR
Requires: %name-daemon-driver-interface = %EVR
Requires: %name-daemon-config-nwfilter = %EVR
%if_with driver_modules
Requires: %name-daemon-driver-qemu = %EVR
Requires: %name-daemon-driver-nodedev = %EVR
Requires: %name-daemon-driver-secret = %EVR
Requires: %name-daemon-driver-storage-fs = %EVR
%endif

%description qemu-common
Server side daemon, driver and default network & firewall configs
required to manage the virtualization capabilities of QEMU or KVM.

%package qemu
Summary: Server side daemon, driver & default configs required to run QEMU guests
Group: System/Servers
BuildArch: noarch
Requires: %name-qemu-common = %EVR
Requires: qemu

%description qemu
Server side daemon, driver and default network & firewall configs
required to manage the virtualization capabilities of QEMU.

%package kvm
Summary: Server side daemon, driver & default configs required to run KVM guests
Group: System/Servers
BuildArch: noarch
Requires: %name-qemu-common = %EVR
Requires: qemu-kvm

%description kvm
Server side daemon, driver and default network & firewall configs
required to manage the virtualization capabilities of KVM.

%package lxc
Summary: Server side daemon, driver & default configs required to run LXC guests
Group: System/Servers
Requires: %name-daemon-config-network = %EVR
Requires: %name-daemon-config-nwfilter = %EVR
Requires: lxc
%if_with driver_modules
Requires: %name-daemon-driver-lxc = %EVR
Requires: %name-daemon-driver-nodedev = %EVR
Requires: %name-daemon-driver-secret = %EVR
Requires: %name-daemon-driver-storage = %EVR
%endif

%description lxc
Server side daemon, driver and default network & firewall configs
required to manage the virtualization capabilities of LXC.

%package xen
Summary: Server side daemon, driver & default configs required to run XEN guests
Group: System/Servers
BuildArch: noarch
Requires: %name-daemon-config-network = %EVR
Requires: %name-daemon-config-nwfilter = %EVR
Requires: xen
%if_with driver_modules
%if_with libxl
Requires: %name-daemon-driver-libxl = %EVR
%endif
Requires: %name-daemon-driver-nodedev = %EVR
Requires: %name-daemon-driver-secret = %EVR
Requires: %name-daemon-driver-storage = %EVR
%endif #driver_modules

%description xen
Server side daemon, driver and default network & firewall configs
required to manage the virtualization capabilities of Xen.

%package vbox
Summary: Server side daemon, driver & default configs required to run VirtualBox guests
Group: System/Servers
Requires: %name-daemon-config-network = %EVR
Requires: %name-daemon-config-nwfilter = %EVR
%if_with driver_modules
Requires: %name-daemon-driver-vbox = %EVR
Requires: %name-daemon-driver-nodedev = %EVR
Requires: %name-daemon-driver-secret = %EVR
Requires: %name-daemon-driver-storage = %EVR
%endif

%description vbox
Server side daemon, driver and default network & firewall configs
required to manage the virtualization capabilities of VirtualBox.

%package client
Summary: Client side utilities of the libvirt library
Group: System/Libraries
Requires: %name-libs = %EVR
# Needed by libvirt-guests init script.
Requires: gettext
# For virConnectGetSysinfo
Requires: dmidecode
Requires: gnutls-utils
# Needed for probing the power management features of the host.
Conflicts: %name < 0.9.11

%description client
The client binaries needed to access the virtualization
capabilities of recent versions of Linux (and other OSes).

%package libs
Summary: Client side libraries
Group: System/Libraries
# So remote clients can access libvirt over SSH tunnel
# (client invokes 'nc' against the UNIX socket on the server)
Requires: nc
Requires: /etc/sasl2

%description libs
Shared libraries for accessing the libvirt daemon.

%package admin
Summary: Set of tools to control libvirt daemon
Group: System/Servers
Requires: %name-libs = %EVR

%description admin
The client side utilities to control the libvirt daemon.

%package -n bash-completion-%name
Summary: Bash completion for %name utils
Group: Shells
BuildArch: noarch
Requires: bash-completion

%description -n bash-completion-%name
Bash completion for %name.

%package -n wireshark-plugin-%name
Summary: Wireshark dissector plugin for libvirt RPC transactions
Group: Networking/Other
Requires: wireshark
Requires: %name-libs = %EVR

%description -n wireshark-plugin-%name
Wireshark dissector plugin for better analysis of libvirt RPC traffic.

%package login-shell
Summary: Login shell for connecting users to an LXC container
Group: System/Libraries
Requires: %name-libs = %EVR

%description login-shell
Provides the set-uid virt-login-shell binary that is used to
connect a user to an LXC container when they login, by switching
namespaces.

%package devel
Summary: Libraries, includes, etc. to compile with the libvirt library
Group: Development/C
Requires: %name-libs = %EVR

%description devel
Includes and documentations for the C library providing an API to use
the virtualization capabilities of recent versions of Linux (and other OSes).

%package lock-sanlock
Summary: Sanlock lock manager plugin for QEMU driver
Group: System/Libraries
Requires: sanlock >= 2.4
#for virt-sanlock-cleanup require augeas
Requires: augeas
Requires: %name-libs = %EVR
Requires: %name-daemon = %EVR

%description lock-sanlock
Includes the Sanlock lock manager plugin for the QEMU
driver

%if_with nss_plugin
%package -n nss-%name
Summary: Libvirt plugin for Name Service Switch
Group: System/Libraries
Requires: %name-daemon-driver-network = %EVR

%description -n nss-%name
Libvirt plugin for NSS for translating domain names into IP addresses.
%endif

%prep
%setup -a1
mkdir -p src/keycodemapdb
tar -xf %SOURCE2 -C src/keycodemapdb --strip-components 1

%patch1 -p1
# git and rsync aren't needed for build.
sed -i '/^\(git\|rsync\)[[:space:]]/d' bootstrap.conf
# disable virnetsockettest test
sed -i 's/virnetsockettest //' tests/Makefile.am
# disable vircgrouptest test
sed -i 's/vircgrouptest //' tests/Makefile.am

%build
LOADERS_OLD="%_datadir/OVMF/OVMF_CODE.fd:%_datadir/OVMF/OVMF_VARS.fd"
LOADERS_NEW="%_datadir/edk2/ovmf/OVMF_CODE.fd:%_datadir/edk2/ovmf/OVMF_VARS.fd:%_datadir/edk2/aarch64/QEMU_EFI-pflash.raw:%_datadir/edk2/aarch64/vars-template-pflash.raw"
LOADERS="$LOADERS_OLD:$LOADERS_NEW"
%define with_loader_nvram $LOADERS

./bootstrap --no-git --gnulib-srcdir=gnulib-%name-%version
%configure \
		--disable-static \
		--disable-rpath \
		--with-packager-version="%release" \
		--with-init-script=systemd \
		--with-qemu-user=%qemu_user \
		--with-qemu-group=%qemu_group \
		--with-sysctl=check \
		%{subst_with libvirtd} \
		%{subst_with qemu} \
		%{subst_with openvz} \
		%{subst_with lxc} \
		%{subst_with_dash login_shell} \
		%{subst_with vbox} \
		%{subst_with libxl} \
		%{subst_with vmware} \
		%{subst_with phyp} \
		%{subst_with esx} \
		%{subst_with hyperv} \
		%{subst_with xenapi} \
		%{subst_with network} \
		%{subst_with_dash storage_fs} \
		%{subst_with_dash storage_lvm} \
		%{subst_with_dash storage_iscsi} \
		%{subst_with_dash storage_iscsi_direct} \
		%{subst_with_dash storage_scsi} \
		%{subst_with_dash storage_disk} \
		%{subst_with_dash storage_rbd} \
		%{subst_with_dash storage_mpath} \
		%{subst_with_dash storage_gluster} \
		%{subst_with_dash storage_zfs} \
		%{subst_with_dash storage_vstorage} \
		%{subst_with_dash storage_sheepdog} \
		%{subst_with numactl} \
		%{subst_with selinux} \
		%{subst_with netcf} \
		%{subst_with udev} \
		%{subst_with hal} \
		%{subst_with yajl} \
		%{subst_with sanlock} \
		%{subst_with fuse} \
		%{subst_with dbus} \
		%{subst_with_dash pm_utils} \
		%{subst_with polkit} \
		%{subst_with firewalld} \
		%{subst_with_dash firewalld_zone} \
		%{subst_with capng} \
		%{subst_with libpcap} \
		%{subst_with macvtap} \
		%{subst_with audit} \
		%{subst_with_dash driver_modules} \
		%{subst_with dtrace} \
		%{subst_with_dash wireshark} \
		%{subst_with_dash bash_completion} \
		%{subst_with_dash nss_plugin} \
		--with-loader-nvram=%with_loader_nvram \
		%{subst_with sasl}


%make_build
gzip -9 ChangeLog

%install
%makeinstall_std

# Install sysv init scripts
%if_with libvirtd
install -pD -m 755 %SOURCE11  %buildroot%_initdir/libvirtd
install -pD -m 755 %SOURCE12  %buildroot%_initdir/virtlockd
install -pD -m 755 %SOURCE13  %buildroot%_initdir/virtlogd
%endif
install -pD -m 755 %SOURCE14  %buildroot%_initdir/libvirt-guests

install -d -m 0755 %buildroot%_runtimedir/%name
rm -f %buildroot%_libdir/*.{a,la}
rm -f %buildroot%_libdir/%name/*/*.{a,la}

# delete docs
rm -rf %buildroot%_datadir/doc/libvirt

%if_with network
# We don't want to install /etc/libvirt/qemu/networks in the main %files list
# because if the admin wants to delete the default network completely, we don't
# want to end up re-incarnating it on every RPM upgrade.
install -d -m 0755 %buildroot%_datadir/libvirt/networks/
cp %buildroot%_sysconfdir/libvirt/qemu/networks/default.xml \
   %buildroot%_datadir/libvirt/networks/default.xml
rm -f %buildroot%_sysconfdir/libvirt/qemu/networks/default.xml
rm -f %buildroot%_sysconfdir/libvirt/qemu/networks/autostart/default.xml
# Strip auto-generated UUID - we need it generated per-install
sed -i -e "/<uuid>/d" %buildroot%_datadir/libvirt/networks/default.xml
%else
rm -f %buildroot%_sysconfdir/libvirt/qemu/networks/default.xml
rm -f %buildroot%_sysconfdir/libvirt/qemu/networks/autostart/default.xml
%endif

%if_without qemu
rm -f %buildroot%_datadir/augeas/lenses/libvirtd_qemu.aug
rm -f %buildroot%_datadir/augeas/lenses/tests/test_libvirtd_qemu.aug
rm -f %buildroot%_sysconfdir/libvirt/qemu.conf
rm -f %buildroot%_sysconfdir/logrotate.d/libvirtd.qemu
%endif
%if_without lxc
rm -f %buildroot%_datadir/augeas/lenses/libvirtd_lxc.aug
rm -f %buildroot%_datadir/augeas/lenses/tests/test_libvirtd_lxc.aug
rm -f %buildroot%_sysconfdir/libvirt/lxc.conf
rm -f %buildroot%_sysconfdir/logrotate.d/libvirtd.lxc
%endif
%if_without nwfilter
rm -rf %buildroot%_sysconfdir/libvirt/nwfilter
%endif
%if_without libxl
rm -f %buildroot%_sysconfdir/logrotate.d/libvirtd.libxl
%endif

%if_with nss_plugin
# Relocate nss library from %_libdir/libnss_libvirt.so.* to /%_lib/libnss_libvirt.so.* .
mkdir -p %buildroot/%_lib
mv %buildroot%_libdir/libnss_libvirt.so.* %buildroot/%_lib/
ln -sf ../../%_lib/libnss_libvirt.so.2 %buildroot%_libdir/libnss_libvirt.so
mv %buildroot%_libdir/libnss_libvirt_guest.so.2 %buildroot/%_lib/
ln -sf ../../%_lib/libnss_libvirt_guest.so.2 %buildroot%_libdir/libnss_libvirt_guest.so
%endif

%if_with libvirtd
# filetrigger that restart libvirtd after install any plugin
cat <<EOF > filetrigger
#!/bin/sh -e

dir=%_libdir/libvirt/
grep -qs '^'\$dir'' && /sbin/service libvirtd condrestart ||:
EOF
install -pD -m 755 filetrigger %buildroot%_rpmlibdir/%name.filetrigger

install -pD -m644 libvirtd.tmpfiles %buildroot/lib/tmpfiles.d/libvirtd.conf
%endif

%find_lang %name

# cleanup
rm -f %buildroot/usr/share/libvirt/test-screenshot.png

%if_without libvirtd
rm -rf %buildroot%_man7dir
%endif

%check
cd tests
%make
# These 1 tests don't current work
for i in daemon-conf
do
  rm -f $i
  printf "#!/bin/sh\nexit 0\n" > $i
  chmod +x $i
done
%make check ||:

%pre login-shell
%_sbindir/groupadd -r -f virtlogin

%if_with qemu
%pre daemon-driver-qemu
%_sbindir/groupadd -r -f %qemu_group
%_sbindir/useradd -M -r -d %_localstatedir/lib/%name -s /bin/false -c "libvirt user" -g %qemu_group %qemu_user >/dev/null 2>&1 || :
%endif

%post daemon
%post_service virtlockd
%post_service virtlogd

%preun daemon
%preun_service libvirtd
%preun_service virtlogd
%preun_service virtlockd


%triggerpostun daemon -- libvirt-daemon < 1.3.0
# In upgrade scenario we must explicitly enable virtlockd/virtlogd
# sockets, if libvirtd is already enabled and start them if
# libvirtd is running, otherwise you'll get failures to start
# guests
if [ $1 -ge 1 ] ; then
    if service libvirtd status; then
        chkconfig virtlogd on && service virtlogd start
        chkconfig virtlockd on && service virtlockd start
    fi
fi

%post daemon-config-network
if [ $1 -eq 1 ]; then
    if [ ! -f %_sysconfdir/libvirt/qemu/networks/default.xml ]; then
	UUID=`/usr/bin/uuidgen`
	sed -e "s,</name>,</name>\n  <uuid>$UUID</uuid>," \
         < %_datadir/libvirt/networks/default.xml \
         > /etc/libvirt/qemu/networks/default.xml
    fi
fi

%post client
%post_service libvirt-guests

%preun client
%preun_service libvirt-guests

%files

%files docs
%doc docs/*.xml
%doc %_datadir/gtk-doc/html/libvirt

%doc docs/html docs/devhelp docs/*.gif


%files client
%_bindir/virsh
%_bindir/virt-xml-validate
%_bindir/virt-pki-validate
%_bindir/virt-host-validate
%_man1dir/virsh.*
%_man1dir/virt-xml-validate.*
%_man1dir/virt-pki-validate.*
%_man1dir/virt-host-validate.*

%config(noreplace) %_sysconfdir/sysconfig/libvirt-guests
%_initdir/libvirt-guests
%_libexecdir/libvirt-guests.sh
%systemd_unitdir/libvirt-guests.service

%files libs -f %name.lang
%doc COPYING COPYING.LESSER
%config(noreplace) %_sysconfdir/libvirt/libvirt.conf
%config(noreplace) %_sysconfdir/libvirt/libvirt-admin.conf
%_libdir/lib*.so.*
%dir %_datadir/libvirt
%dir %_datadir/libvirt/schemas
%dir %_localstatedir/lib/libvirt
%_datadir/libvirt/schemas/*.rng
%_datadir/libvirt/cpu_map

%if_with sasl
%config(noreplace) %_sysconfdir/sasl2/libvirt.conf
%endif

%if_with libvirtd
%files daemon
%dir %attr(0700, root, root) %_sysconfdir/libvirt
%dir %_datadir/libvirt
%dir %attr(0700, root, root) %_logdir/libvirt
%dir %_runtimedir/%name
%dir %attr(0700, root, root) %_sysconfdir/libvirt/nwfilter
%config(noreplace) %_sysconfdir/sysconfig/libvirtd
%config /lib/tmpfiles.d/libvirtd.conf
%_unitdir/libvirtd*

%_unitdir/virt-guest-shutdown.target
%_initdir/libvirtd
%config(noreplace) %_sysconfdir/libvirt/libvirtd.conf
/lib/sysctl.d/*
%config(noreplace) %_sysconfdir/logrotate.d/libvirtd
%_rpmlibdir/%name.filetrigger

#virtlockd
%config(noreplace) %_sysconfdir/libvirt/qemu-lockd.conf
%config(noreplace) %_sysconfdir/sysconfig/virtlockd
%config(noreplace) %_sysconfdir/libvirt/virtlockd.conf
%_initdir/virtlockd
%_unitdir/virtlockd*
%_libdir/%name/lock-driver/lockd.so
%_sbindir/virtlockd
%_datadir/augeas/lenses/libvirt_lockd.aug
%_datadir/augeas/lenses/virtlockd.aug
%_datadir/augeas/lenses/tests/test_virtlockd.aug
%_man8dir/virtlockd*
%_man7dir/virkey*

#virtlogd
%config(noreplace) %_sysconfdir/libvirt/virtlogd.conf
%config(noreplace) %_sysconfdir/sysconfig/virtlogd
%_initdir/virtlogd
%_unitdir/virtlogd*
%_sbindir/virtlogd
%_datadir/augeas/lenses/tests/test_virtlogd.aug
%_datadir/augeas/lenses/virtlogd.aug
%_man8dir/virtlogd*

%if_with qemu
%_datadir/augeas/lenses/tests/test_libvirt_lockd.aug
%endif


%_libexecdir/libvirt_iohelper
%_sbindir/libvirtd
%_man8dir/libvirtd.*

%_datadir/augeas/lenses/libvirtd.aug
%_datadir/augeas/lenses/tests/test_libvirtd.aug

%dir %attr(0711, root, root) %_localstatedir/lib/libvirt/images
%dir %attr(0711, root, root) %_localstatedir/lib/libvirt/filesystems
%dir %attr(0711, root, root) %_localstatedir/lib/libvirt/boot
%dir %attr(0700, root, root) %_localstatedir/cache/libvirt
%dir %_libdir/libvirt
%dir %_libdir/libvirt/connection-driver
%dir %_libdir/libvirt/lock-driver

%if_with polkit
%_datadir/polkit-1/actions/org.libvirt.unix.policy
%_datadir/polkit-1/actions/org.libvirt.api.policy
%_datadir/polkit-1/rules.d/50-libvirt.rules
%endif

%if_with network
%files daemon-config-network
%dir %attr(0700, root, root) %_sysconfdir/libvirt/qemu
%dir %attr(0700, root, root) %_sysconfdir/libvirt/qemu/networks
%dir %attr(0700, root, root) %_sysconfdir/libvirt/qemu/networks/autostart
%dir %_datadir/libvirt/networks
%_datadir/libvirt/networks/default.xml
%dir %_runtimedir/%name/network
%dir %attr(0700, root, root) %_localstatedir/lib/libvirt/network
%dir %attr(0755, root, root) %_localstatedir/lib/libvirt/dnsmasq
%endif

%if_with nwfilter
%files daemon-config-nwfilter
%_sysconfdir/libvirt/nwfilter/*.xml
%endif

%if_with driver_modules
%if_with network
%files daemon-driver-network
%_libdir/%name/connection-driver/libvirt_driver_network.so
%_libexecdir/libvirt_leaseshelper
%endif

%if_with udev
%files daemon-driver-nodedev
%_libdir/%name/connection-driver/libvirt_driver_nodedev.so

%files daemon-driver-interface
%_libdir/%name/connection-driver/libvirt_driver_interface.so
%endif #if_with udev

%if_with nwfilter
%files daemon-driver-nwfilter
%_libdir/%name/connection-driver/libvirt_driver_nwfilter.so
%endif

%files daemon-driver-secret
%_libdir/%name/connection-driver/libvirt_driver_secret.so

%files daemon-driver-storage

%files daemon-driver-storage-core
%if_with storage_disk
%_libexecdir/libvirt_parthelper
%endif
%_libdir/%name/connection-driver/libvirt_driver_storage.so
%dir %_libdir/%name/storage-backend
%dir %_libdir/%name/storage-file
%_libdir/%name/storage-file/libvirt_storage_file_fs.so

%if_with storage_fs
%files daemon-driver-storage-fs
%_libdir/%name/storage-backend/libvirt_storage_backend_fs.so
%endif


%if_with storage_disk
%files daemon-driver-storage-disk
%_libdir/%name/storage-backend/libvirt_storage_backend_disk.so
%endif

%if_with storage_lvm
%files daemon-driver-storage-logical
%_libdir/%name/storage-backend/libvirt_storage_backend_logical.so
%endif

%if_with storage_scsi
%files daemon-driver-storage-scsi
%_libdir/%name/storage-backend/libvirt_storage_backend_scsi.so
%endif

%if_with storage_iscsi
%files daemon-driver-storage-iscsi
%_libdir/%name/storage-backend/libvirt_storage_backend_iscsi.so
%endif

%if_with storage_iscsi_direct
%files daemon-driver-storage-iscsi-direct
%_libdir/%name/storage-backend/libvirt_storage_backend_iscsi-direct.so
%endif

%if_with storage_mpath
%files daemon-driver-storage-mpath
%_libdir/%name/storage-backend/libvirt_storage_backend_mpath.so
%endif

%if_with storage_gluster
%files daemon-driver-storage-gluster
%_libdir/%name/storage-backend/libvirt_storage_backend_gluster.so
%_libdir/%name/storage-file/libvirt_storage_file_gluster.so
%endif

%if_with storage_rbd
%files daemon-driver-storage-rbd
%_libdir/%name/storage-backend/libvirt_storage_backend_rbd.so
%endif

%if_with storage_sheepdog
%files daemon-driver-storage-sheepdog
%_libdir/%name/storage-backend/libvirt_storage_backend_sheepdog.so
%endif

%if_with storage_zfs
%files daemon-driver-storage-zfs
%_libdir/%name/storage-backend/libvirt_storage_backend_zfs.so
%endif

%if_with qemu
%files daemon-driver-qemu
%_libdir/%name/connection-driver/libvirt_driver_qemu.so
%config(noreplace) %_sysconfdir/libvirt/qemu.conf
%config(noreplace) %_sysconfdir/logrotate.d/libvirtd.qemu
%dir %attr(0750, root, root) %_runtimedir/%name/qemu
%dir %attr(0750, %qemu_user, %qemu_group) %_localstatedir/lib/libvirt/qemu
%dir %attr(0750, %qemu_user, %qemu_group) %_cachedir/libvirt/qemu
%dir %attr(0700, root, root) %_logdir/libvirt/qemu
%dir %attr(0700, root, root) %_localstatedir/lib/libvirt/swtpm
%dir %attr(0700, root, root) %_logdir/swtpm/libvirt/qemu
%_datadir/augeas/lenses/libvirtd_qemu.aug
%_datadir/augeas/lenses/tests/test_libvirtd_qemu.aug
%endif

%if_with lxc
%files daemon-driver-lxc
%_libdir/%name/connection-driver/libvirt_driver_lxc.so
%config(noreplace) %_sysconfdir/libvirt/lxc.conf
%config(noreplace) %_sysconfdir/logrotate.d/libvirtd.lxc
%dir %_runtimedir/%name/lxc
%dir %attr(0700, root, root) %_localstatedir/lib/libvirt/lxc
%dir %attr(0700, root, root) %_localstatedir/log/libvirt/lxc
%_datadir/augeas/lenses/libvirtd_lxc.aug
%_datadir/augeas/lenses/tests/test_libvirtd_lxc.aug
%_libexecdir/libvirt_lxc
%endif

%if_with libxl
%files daemon-driver-libxl
%_libdir/%name/connection-driver/libvirt_driver_libxl.so
%dir %attr(0700, root, root) %_localstatedir/log/libvirt/libxl
%dir %attr(0700, root, root) %_localstatedir/lib/libvirt/libxl
%config(noreplace) %_sysconfdir/libvirt/libxl*.conf
%config(noreplace) %_sysconfdir/logrotate.d/libvirtd.libxl
%_datadir/augeas/lenses/libvirtd_libxl.aug
%_datadir/augeas/lenses/tests/test_libvirtd_libxl.aug
%endif

%if_with vbox
%files daemon-driver-vbox
%_libdir/%name/connection-driver/libvirt_driver_vbox.so
%endif
%endif #driver_modules

%if_with qemu
%files qemu-common
%if_with qemu_tcg
%files qemu
%endif
%if_with qemu_kvm
%files kvm
%endif

%endif #if_with qemu

%if_with lxc
%files lxc
%endif

%if_with libxl
%files xen
%endif #if_with libxl

%if_with vbox
%files vbox
%endif

%if_with sanlock
%files lock-sanlock
%_libdir/libvirt/lock-driver/sanlock.so

%if_with qemu
%config(noreplace) %_sysconfdir/libvirt/qemu-sanlock.conf
%endif

%if_with libxl
%config(noreplace) %_sysconfdir/libvirt/libxl-sanlock.conf
%endif

%_datadir/augeas/lenses/libvirt_sanlock.aug
%_datadir/augeas/lenses/tests/test_libvirt_sanlock.aug
%dir %attr(0770, root, sanlock) %_localstatedir/lib/libvirt/sanlock
%_sbindir/virt-sanlock-cleanup
%_man8dir/virt-sanlock-cleanup.*
%_libexecdir/libvirt_sanlock_helper
%endif #if_with sanlock
%endif #if_with libvirtd

%files admin
%_bindir/virt-admin
%_man1dir/virt-admin.1*

%if_with bash_completion
%files -n bash-completion-%name
%_datadir/bash-completion/completions/*
%endif

%if_with nss_plugin
%files  -n nss-%name
/%_lib/libnss_libvirt.so.*
/%_lib/libnss_libvirt_guest.so.*
%endif

%if_with wireshark
%files -n wireshark-plugin-%name
%_libdir/wireshark/plugins/%name.so
%endif

%if_with lxc
%if_with login_shell
%files login-shell
%config(noreplace) %_sysconfdir/libvirt/virt-login-shell.conf
%attr(4710, root, virtlogin) %_bindir/virt-login-shell
%_man1dir/virt-login-shell.*
%endif
%endif

%files devel
%_pkgconfigdir/*.pc
%_libdir/*.so
%_includedir/libvirt
%_datadir/libvirt/api

%changelog
* Mon Aug 19 2019 Alexey Shabalin <shaba@altlinux.org> 5.6.0-alt1
- 5.6.0

* Thu Jul 04 2019 Alexey Shabalin <shaba@altlinux.org> 5.5.0-alt1
- 5.5.0 (Fixes: CVE-2019-10161, CVE-2019-10166, CVE-2019-10167, CVE-2019-10168)
- build with glusterfs6

* Wed Jun 05 2019 Ivan A. Melnikov <iv@altlinux.org> 5.4.0-alt3
- fix build without server_drivers

* Tue Jun 04 2019 Alexey Shabalin <shaba@altlinux.org> 5.4.0-alt2
- move files of qemu,lxc,xen to daemon drivers

* Tue Jun 04 2019 Alexey Shabalin <shaba@altlinux.org> 5.4.0-alt1
- 5.4.0 (Fixes: CVE-2018-12126, CVE-2018-12127, CVE-2018-12130, CVE-2019-11091, CVE-2019-10132)

* Fri Apr 05 2019 Alexey Shabalin <shaba@altlinux.org> 5.2.0-alt1
- 5.2.0

* Thu Mar 14 2019 Alexey Shabalin <shaba@altlinux.org> 5.1.0-alt1
- 5.1.0
- fix build without server_drivers (ALT#36248)

* Thu Jan 31 2019 Alexey Shabalin <shaba@altlinux.org> 5.0.0-alt1
- 5.0.0

* Wed Jan 02 2019 Alexey Shabalin <shaba@altlinux.org> 4.10.0-alt1
- 4.10.0

* Thu Nov 29 2018 Alexey Shabalin <shaba@altlinux.org> 4.9.0-alt1
- 4.9.0
- add requires qemu-kvm-core to libvirt-daemon-driver-qemu (ALT#33801)

* Tue Oct 09 2018 Alexey Shabalin <shaba@altlinux.org> 4.8.0-alt1
- 4.8.0

* Thu Sep 13 2018 Alexey Shabalin <shaba@altlinux.org> 4.7.0-alt1
- 4.7.0
- add daemon-driver-storage-iscsi-direct package
  (instead of unsing iscsiadm, it uses libiscsi)

* Sat Aug 11 2018 Alexey Shabalin <shaba@altlinux.org> 4.6.0-alt1
- 4.6.0
- build with ceph storage support only for x86_64 and aarch64

* Wed Jul 11 2018 Alexey Shabalin <shaba@altlinux.ru> 4.5.0-alt1
- 4.5.0
- not install zfs storage support by default

* Tue Jun 05 2018 Alexey Shabalin <shaba@altlinux.ru> 4.4.0-alt1
- 4.4.0

* Mon Jun 04 2018 Alexey Shabalin <shaba@altlinux.ru> 4.3.0-alt1
- 4.3.0

* Sun Apr 01 2018 Alexey Shabalin <shaba@altlinux.ru> 4.2.0-alt1
- 4.2.0 (Fixes: CVE-2018-5748)
- Use Python 3 for building
- fix package login-shell

* Fri Mar 09 2018 Alexey Shabalin <shaba@altlinux.ru> 4.1.0-alt1
- 4.1.0 (Fixes: CVE-2018-6764, CVE-2017-5715)

* Fri Feb 02 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.0-alt2
- enabled server part on arm arches

* Sat Jan 27 2018 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt1
- 4.0.0 (Fixes: CVE-2018-5748)
- add filetrigger that restart libvirtd after install any plugin

* Fri Dec 08 2017 Alexey Shabalin <shaba@altlinux.ru> 3.10.0-alt1
- 3.10.0

* Mon Oct 30 2017 Alexey Shabalin <shaba@altlinux.ru> 3.8.0-alt1
- 3.8.0 (Fixes: CVE-2017-1000256)

* Mon Sep 04 2017 Alexey Shabalin <shaba@altlinux.ru> 3.7.0-alt1
- 3.7.0

* Tue Aug 08 2017 Alexey Shabalin <shaba@altlinux.ru> 3.6.0-alt1
- 3.6.0

* Tue Jul 11 2017 Alexey Shabalin <shaba@altlinux.ru> 3.5.0-alt1
- 3.5.0

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 3.4.0-alt1
- 3.4.0

* Tue Apr 25 2017 Alexey Shabalin <shaba@altlinux.ru> 3.2.0-alt2
- backport fixes from upstream master (ALT#33413)

* Thu Apr 13 2017 Alexey Shabalin <shaba@altlinux.ru> 3.2.0-alt1
- 3.2.0
- check running messagebus service before run libvirtd(ALT#32479)

* Fri Mar 10 2017 Alexey Shabalin <shaba@altlinux.ru> 3.1.0-alt2
- update R: for qemu-common

* Thu Mar 09 2017 Alexey Shabalin <shaba@altlinux.ru> 3.1.0-alt1
- 3.1.0
- split libvirt-daemon-driver-storage to subpackages

* Wed Feb 15 2017 Anton Farygin <rider@altlinux.ru> 3.0.0-alt2
- added patches from upstream to fix work with lvm

* Fri Jan 27 2017 Alexey Shabalin <shaba@altlinux.ru> 3.0.0-alt1
- 3.0.0

* Thu Jan 12 2017 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt2
- add new path to edk2 uefi nvram

* Wed Dec 07 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Tue Nov 22 2016 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt2
- libvirt-daemon must will update after all subpackes for restart successfuly

* Sat Nov 05 2016 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Fri Oct 28 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt2
- add requires dmidecode to daemon package
- drop generate host_uuid in post_install, default host_uuid_source = smbios

* Fri Oct 07 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Tue Aug 23 2016 Alexey Shabalin <shaba@altlinux.ru> 2.1.0-alt1
- 2.1.0
- build with sanlock
- move libs from libvirt-client to lilbvirt-libs
- add new subpackages:
  + libvirt-libs
  + libvirt-admin
  + libvirt-shell
  + libvirt-nss
  + libvirt-lock-sanlock

* Thu Jul 07 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Wed Jun 15 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.5-alt1
- 1.3.5 release

* Mon May 30 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.5-alt0.rc1
- 1.3.5-rc1

* Fri May 20 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.4-alt1
- 1.3.4
- build without xen support

* Tue Apr 05 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.2-alt3
- fixed typo in trigger

* Fri Mar 25 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.2-alt2
- add Requires dnsmasq, but disable autostart default network
- add Requires dbus to libvirt-daemon
- backport some patches from upstream

* Mon Mar 14 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.2-alt1
- 1.3.2
- build with zfs support

* Fri Dec 18 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0
- fixed CVE-2015-5313

* Thu Nov 05 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.21-alt1
- 1.2.21

* Thu Oct 22 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.20-alt1
- 1.2.20
- fixed CVE-2015-5247

* Tue Aug 11 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.18-alt1
- 1.2.18

* Wed Jun 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.16-alt2
- update OVMF nvram path

* Fri Jun 19 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.16-alt1
- 1.2.16
- build with firewalld support
- allow password-less access with polkit for 'vmusers' group
- define default OVMF nvram path

* Tue May 05 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.15-alt1
- 1.2.15
- build with glusterfs support

* Thu Apr 09 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.14-alt1
- 1.2.14

* Mon Mar 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.13-alt1
- 1.2.13

* Wed Feb 11 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.12-alt1
- 1.2.12
- fixed CVE-2015-0236

* Thu Dec 18 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.11-alt1
- 1.2.11
- fixed CVE-2014-7823,CVE-2014-8135,CVE-2014-8136,CVE-2014-8131

* Fri Nov 07 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.10-alt1
- 1.2.10

* Tue Oct 21 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.9-alt2
- rebuild with parted-3.2-alt1

* Fri Oct 03 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.9-alt1
- 1.2.9
- fixed CVE-2014-3633, CVE-2014-3657

* Thu Sep 11 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.8-alt1
- 1.2.8

* Wed Aug 06 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.7-alt1
- 1.2.7

* Fri Jul 04 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Mon Jun 02 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Mon May 12 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Tue Apr 01 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.3-alt1
- 1.2.3
- build with libxl

* Wed Mar 05 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.2-alt1
- 1.2.2
- fixed CVE-2013-6436, CVE-2013-6456, CVE-2013-6457, CVE-2013-6458, CVE-2014-1447, CVE-2014-0028
- add wireshark-plugin-libvirt package, but disabled now

* Mon Dec 02 2013 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0
- drop python module package

* Wed Nov 06 2013 Alexey Shabalin <shaba@altlinux.ru> 1.1.4-alt1
- 1.1.4
- fixed CVE-2013-4400, CVE-2013-4401

* Tue Oct 01 2013 Alexey Shabalin <shaba@altlinux.ru> 1.1.3-alt1
- 1.1.3
- fixed CVE-2013-4297, CVE-2013-4311, CVE-2013-4296

* Tue Sep 03 2013 Alexey Shabalin <shaba@altlinux.ru> 1.1.2-alt1
- 1.1.2
- fixed CVE-2013-4291, CVE-2013-4292, CVE-2013-5651

* Mon Aug 26 2013 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt2
- snapshot of v1.1.1-maint branch (fixed CVE-2013-4239)

* Thu Aug 08 2013 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt1
- 1.1.1
- fixed CVE-2013-2230, CVE-2013-4153, CVE-2013-4154

* Wed Jul 03 2013 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- v1.1.0-maint branch
- add vbox subpackages

* Mon May 20 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.5.1-alt1
- 1.0.5.1

* Mon May 06 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Tue Apr 30 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.4-alt2
- add workaround for paranoid permitions of dnsmasq

* Thu Apr 11 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.4-alt1
- 1.0.4
- add patches from v1.0.4-maint

* Wed Mar 13 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- 1.0.3 release

* Fri Mar 01 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt0.1.rc2
- upstream snapshot

* Wed Feb 20 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Nov 08 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt2
- build libvirt-daemon-driver-interface package

* Tue Nov 06 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- 1.0.0
- drop local systemd unit files, use upstream
- move tmpfiles to /lib

* Mon Oct 29 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10.2.1-alt1
- 0.10.2.1

* Mon Sep 24 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10.2-alt1
- 0.10.2

* Mon Sep 10 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10.1-alt1
- 0.10.1

* Wed Jul 18 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.13-alt1
- 0.9.13
- build drivers as loadable modules; split driver packages
- add storage backend RBD (RADOS Block Device) support

* Thu May 17 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.12-alt1
- 0.9.12

* Wed May 02 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.11.3-alt1
- 0.9.11.3

* Wed Apr 11 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.11-alt4
- fix update: add "Conflicts: libvirt < 0.9.11" to libvirt-client

* Mon Apr 09 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.11-alt3
- really fix post scripts

* Thu Apr 05 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.11-alt2
- fix post scripts

* Tue Apr 03 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.11-alt1
- 0.9.11
- refactor the libvirt spec
- split package to libvirt-client and libvirt-daemon( and qemu,kvm,lxc subpackages)
- install libvirt-guests systemd service

* Mon Mar 26 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.10-alt2
- fixed build for arm (patch by sbolshakov@)

* Tue Feb 14 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.10-alt1
- 0.9.10

* Fri Feb 03 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.9-alt1
- 0.9.9

* Thu Dec 08 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.6-alt1.1
- Rebuild with Python-2.7

* Thu Sep 29 2011 Anton Farygin <rider@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Wed Aug 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Wed Jun 15 2011 Anton Protopopov <aspsk@altlinux.org> 0.9.1-alt2
- Add dependency on dmidecode package (ALT 25752)
- Create vmusers group in %%pre (ALT 25751)

* Fri May 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.1-alt1
- 0.9.1
- add /etc/tmpfiles.d/libvirtd.conf for systemd and /var/run on tmpfs

* Fri Apr 15 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt3
- cleanup spec (/etc -> %_sysconfdir,/var -> %_localstatedir)
- add generate host_uuid for libvirtd.conf
- generate UUID for first rpm install only
- run qemu with "_libvirt" user and "vmusers" group privileges
- add systemd service file

* Mon Apr 11 2011 Anton Protopopov <aspsk@altlinux.org> 0.9.0-alt2
- implement rigth cond{stop,restart,reload} (ALT 23023)

* Wed Apr 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt1
- 0.9.0
- fixed CVE-2011-1146

* Sat Mar 26 2011 Anton Farygin <rider@altlinux.ru> 0.8.8-alt1
- new version

* Wed Feb 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.7-alt3
- rebuild with new libdevmapper

* Fri Jan 21 2011 Anton Farygin <rider@altlinux.ru> 0.8.7-alt2
- add (post,preun)_service, disabled by default
- added 'host' model to cpu list
- removed dnsmasq requires for system with bridged networks

* Tue Jan 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.7-alt1
- 0.8.7
- fix and enable polkit support
- build with udev support
- build with yajl support
- build with selinux support
- build with phyp (libssh2) support
- build with libpcap support
- build with libcap-ng support for manage capabilities
- build with audit support
- build with numa support

* Thu Dec 02 2010 Anton Farygin <rider@altlinux.ru> 0.8.6-alt1
- new version
- enabled xen support (closes: #24579)
- removed post-service (closes: #23023)

* Wed Nov 24 2010 Anton Farygin <rider@altlinux.ru> 0.8.5-alt2
- removed binaries from /usr/share

* Tue Nov 09 2010 Anton Farygin <rider@altlinux.ru> 0.8.5-alt1
- Release of 0.8.5

* Sat Oct 02 2010 Anton Farygin <rider@altlinux.ru> 0.8.4-alt1
- Release of 0.8.4

* Tue Jul 06 2010 Anton Protopopov <aspsk@altlinux.org> 0.8.2-alt2
- Add --with-storage-lvm (ALT #23580)

* Tue Jul 06 2010 Anton Protopopov <aspsk@altlinux.org> 0.8.2-alt1
- Release of 0.8.2

* Fri Jul 02 2010 Anton Protopopov <aspsk@altlinux.org> 0.8.1-alt1
- Release of 0.8.1

* Sun Apr 18 2010 Anton Protopopov <aspsk@altlinux.org> 0.8.0-alt2
- Close a reopened bug (ALT #22433).

* Tue Apr 13 2010 Anton Protopopov <aspsk@altlinux.org> 0.8.0-alt1
- Release of 0.8.0

* Mon Apr 12 2010 Anton Protopopov <aspsk@altlinux.org> 0.7.7-alt2
- Use 'notifemty' instead of 'minsize/size 100k' in logrotate config.
  This prevents logrotate from rotating empty logs (Closes: #22433).

* Sat Mar 20 2010 Aleksey Avdeev <solo@altlinux.ru> 0.7.7-alt1
- NMU
- Release of 0.7.7 (Closes: #23095)

* Wed Feb 10 2010 Aleksey Avdeev <solo@altlinux.ru> 0.7.6-alt2
- NMU
- Return %%_pkgconfigdir/libvirt.pc in subpackage %%name-devel (Closes: #22932)
  (thanks to Alexey Borovskoy <alb altlinux ru>)
- Fix status function in initscript (thanks to Alexey Borovskoy <alb altlinux ru>)

* Mon Feb 08 2010 Aleksey Avdeev <solo@altlinux.ru> 0.7.6-alt1
- NMU
- Release of 0.7.6

* Mon Feb 08 2010 Aleksey Avdeev <solo@altlinux.ru> 0.7.5-alt1
- NMU
- Release of 0.7.5

* Tue Nov 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt1.1
- Rebuilt with python 2.6

* Mon Nov 23 2009 Anton Protopopov <aspsk@altlinux.org> 0.7.4-alt1
- Release of 0.7.4

* Tue Sep 22 2009 Anton Protopopov <aspsk@altlinux.org> 0.7.1-alt2
- Provide libvirt-python

* Wed Sep 16 2009 Anton Protopopov <aspsk@altlinux.org> 0.7.1-alt1
- Release of 0.7.1

* Fri Sep 11 2009 Anton Protopopov <aspsk@altlinux.org> 0.7.0-alt2
- merge with upstream (more than 200 commits)
- Disable storage_mpath and add libdevmapper-devel to %%buildrequires
- update .gnulib

* Fri Aug 07 2009 Anton Protopopov <aspsk@altlinux.org> 0.7.0-alt1
- Release of 0.7.0
- Run libvirt with "devel" version of kvm

* Mon Aug 03 2009 Anton Protopopov <aspsk@altlinux.org> 0.6.5-alt1
- Migrate to new git sources

* Tue Jun 02 2009 Anton Protopopov <aspsk@altlinux.org> 0.6.4-alt1
- Release of 0.6.4

* Fri May 15 2009 Anton Protopopov <aspsk@altlinux.org> 0.6.3-alt1
- Update to svn head (>= 0.6.3)

* Tue Apr 14 2009 Anton Protopopov <aspsk@altlinux.org> 0.6.2-alt1
- Release of 0.6.2
- Use --config the same as --ostemplate

* Tue Mar 10 2009 Anton Protopopov <aspsk@altlinux.org> 0.6.1-alt1
- Release of 0.6.1

* Mon Mar 02 2009 Anton Protopopov <aspsk@altlinux.org> 0.6.0-alt2
- Fix python policy

* Sat Jan 31 2009 Anton Protopopov <aspsk@altlinux.org> 0.6.0-alt1
- Release of 0.6.0

* Tue Dec 23 2008 Anton Protopopov <aspsk@altlinux.org> 0.5.1-alt4
- Fix host MAC (Eugeny Sokolov)
- Remove static library (repocop)
- Remove RPM_BUILD_ROOTs

* Thu Dec 18 2008 Anton Protopopov <aspsk@altlinux.org> 0.5.1-alt3
- Fix openvz crash when setting vcpus & initialize mutex

* Mon Dec 08 2008 Anton Protopopov <aspsk@altlinux.org> 0.5.1-alt2
- Fix rpm install (by adding libgnutls26)

* Fri Dec 05 2008 Anton Protopopov <aspsk@altlinux.org> 0.5.1-alt1
- Release of 0.5.1
- Fix repocop warnings
- Link condrestart to restart

* Tue Nov 18 2008 Anton Protopopov <aspsk@altlinux.org> 0.4.6-alt3
- Merged with upstream to fix a bug in openvzWriteParam

* Thu Nov 13 2008 Anton Protopopov <aspsk@altlinux.org> 0.4.6-alt2
- Merged with upstream version with OpenVZ bridge support enabled

* Wed Sep 24 2008 Anton Protopopov <aspsk@altlinux.org> 0.4.6-alt1
- Release of 0.4.6

* Mon Sep 15 2008 Anton Protopopov <aspsk@altlinux.org> 0.4.5-alt1
- Release of 0.4.5

* Mon Sep 08 2008 Anton Protopopov <aspsk@altlinux.org> 0.4.4-alt1.1
- Merge with upstream
- fix %files

* Wed Jun 25 2008 Anton Protopopov <aspsk@altlinux.org> 0.4.4-alt1
- Release of 0.4.4

* Tue Jun 17 2008 Anton Protopopov <aspsk@altlinux.org> 0.4.3-alt1
- Release of 0.4.3

* Mon Apr 21 2008 Anton Protopopov <aspsk@altlinux.ru> 0.4.2-alt2
- Fixed bad permissions on /var/{run,log,lib}/libvirt

* Wed Apr 09 2008 Anton Protopopov <aspsk@altlinux.ru> 0.4.2-alt1
- Release of 0.4.2

* Mon Mar 31 2008 Anton Protopopov <aspsk@altlinux.ru> 0.4.1-alt1
- Release of 0.4.1

* Wed Mar 12 2008 Anton Protopopov <aspsk@altlinux.ru> 0.4.1-alt0.1
- Switch to 0.4.1

* Tue Dec 18 2007 Anton Protopopov <aspsk@altlinux.ru> 0.4.0-alt0.1
- Initial pre-build :)

* Tue Dec 18 2007 Daniel Veillard <veillard@redhat.com> - 0.4.0-1
- Release of 0.4.0
- SASL based authentication
- PolicyKit authentication
- improved NUMA and statistics support
- lots of assorted improvements, bugfixes and cleanups
- documentation and localization improvements

* Sun Sep 30 2007 Daniel Veillard <veillard@redhat.com> - 0.3.3-1
- Release of 0.3.3
- Avahi support
- NUMA support
- lots of assorted improvements, bugfixes and cleanups
- documentation and localization improvements

* Tue Aug 21 2007 Daniel Veillard <veillard@redhat.com> - 0.3.2-1
- Release of 0.3.2
- API for domains migration
- APIs for collecting statistics on disks and interfaces
- lots of assorted bugfixes and cleanups
- documentation and localization improvements

* Tue Jul 24 2007 Daniel Veillard <veillard@redhat.com> - 0.3.1-1
- Release of 0.3.1
- localtime clock support
- PS/2 and USB input devices
- lots of assorted bugfixes and cleanups
- documentation and localization improvements

* Mon Jul  9 2007 Daniel Veillard <veillard@redhat.com> - 0.3.0-1
- Release of 0.3.0
- Secure remote access support
- unification of daemons
- lots of assorted bugfixes and cleanups
- documentation and localization improvements

* Fri Jun  8 2007 Daniel Veillard <veillard@redhat.com> - 0.2.3-1
- Release of 0.2.3
- lot of assorted bugfixes and cleanups
- support for Xen-3.1
- new scheduler API

* Tue Apr 17 2007 Daniel Veillard <veillard@redhat.com> - 0.2.2-1
- Release of 0.2.2
- lot of assorted bugfixes and cleanups
- preparing for Xen-3.0.5

* Thu Mar 22 2007 Jeremy Katz <katzj@redhat.com> - 0.2.1-2.fc7
- don't require xen; we don't need the daemon and can control non-xen now
- fix scriptlet error (need to own more directories)
- update description text

* Fri Mar 16 2007 Daniel Veillard <veillard@redhat.com> - 0.2.1-1
- Release of 0.2.1
- lot of bug and portability fixes
- Add support for network autostart and init scripts
- New API to detect the virtualization capabilities of a host
- Documentation updates

* Fri Feb 23 2007 Daniel P. Berrange <berrange@redhat.com> - 0.2.0-4.fc7
- Fix loading of guest & network configs

* Fri Feb 16 2007 Daniel P. Berrange <berrange@redhat.com> - 0.2.0-3.fc7
- Disable kqemu support since its not in Fedora qemu binary
- Fix for -vnc arg syntax change in 0.9.0  QEMU

* Thu Feb 15 2007 Daniel P. Berrange <berrange@redhat.com> - 0.2.0-2.fc7
- Fixed path to qemu daemon for autostart
- Fixed generation of <features> block in XML
- Pre-create config directory at startup

* Wed Feb 14 2007 Daniel Veillard <veillard@redhat.com> 0.2.0-1.fc7
- support for KVM and QEmu
- support for network configuration
- assorted fixes

* Mon Jan 22 2007 Daniel Veillard <veillard@redhat.com> 0.1.11-1.fc7
- finish inactive Xen domains support
- memory leak fix
- RelaxNG schemas for XML configs

* Wed Dec 20 2006 Daniel Veillard <veillard@redhat.com> 0.1.10-1.fc7
- support for inactive Xen domains
- improved support for Xen display and vnc
- a few bug fixes
- localization updates

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 0.1.9-2
- rebuild against python 2.5

* Wed Nov 29 2006 Daniel Veillard <veillard@redhat.com> 0.1.9-1
- better error reporting
- python bindings fixes and extensions
- add support for shareable drives
- add support for non-bridge style networking
- hot plug device support
- added support for inactive domains
- API to dump core of domains
- various bug fixes, cleanups and improvements
- updated the localization

* Tue Nov  7 2006 Daniel Veillard <veillard@redhat.com> 0.1.8-3
- it's pkgconfig not pgkconfig !

* Mon Nov  6 2006 Daniel Veillard <veillard@redhat.com> 0.1.8-2
- fixing spec file, added %%dist, -devel requires pkgconfig and xen-devel
- Resolves: rhbz#202320

* Mon Oct 16 2006 Daniel Veillard <veillard@redhat.com> 0.1.8-1
- fix missing page size detection code for ia64
- fix mlock size when getting domain info list from hypervisor
- vcpu number initialization
- don't label crashed domains as shut off
- fix virsh man page
- blktapdd support for alternate drivers like blktap
- memory leak fixes (xend interface and XML parsing)
- compile fix
- mlock/munlock size fixes

* Fri Sep 22 2006 Daniel Veillard <veillard@redhat.com> 0.1.7-1
- Fix bug when running against xen-3.0.3 hypercalls
- Fix memory bug when getting vcpus info from xend

* Fri Sep 22 2006 Daniel Veillard <veillard@redhat.com> 0.1.6-1
- Support for localization
- Support for new Xen-3.0.3 cdrom and disk configuration
- Support for setting VNC port
- Fix bug when running against xen-3.0.2 hypercalls
- Fix reconnection problem when talking directly to http xend

* Tue Sep  5 2006 Jeremy Katz <katzj@redhat.com> - 0.1.5-3
- patch from danpb to support new-format cd devices for HVM guests

* Tue Sep  5 2006 Daniel Veillard <veillard@redhat.com> 0.1.5-2
- reactivating ia64 support

* Tue Sep  5 2006 Daniel Veillard <veillard@redhat.com> 0.1.5-1
- new release
- bug fixes
- support for new hypervisor calls
- early code for config files and defined domains

* Mon Sep  4 2006 Daniel Berrange <berrange@redhat.com> - 0.1.4-5
- add patch to address dom0_ops API breakage in Xen 3.0.3 tree

* Mon Aug 28 2006 Jeremy Katz <katzj@redhat.com> - 0.1.4-4
- add patch to support paravirt framebuffer in Xen

* Mon Aug 21 2006 Daniel Veillard <veillard@redhat.com> 0.1.4-3
- another patch to fix network handling in non-HVM guests

* Thu Aug 17 2006 Daniel Veillard <veillard@redhat.com> 0.1.4-2
- patch to fix virParseUUID()

* Wed Aug 16 2006 Daniel Veillard <veillard@redhat.com> 0.1.4-1
- vCPUs and affinity support
- more complete XML, console and boot options
- specific features support
- enforced read-only connections
- various improvements, bug fixes

* Wed Aug  2 2006 Jeremy Katz <katzj@redhat.com> - 0.1.3-6
- add patch from pvetere to allow getting uuid from libvirt

* Wed Aug  2 2006 Jeremy Katz <katzj@redhat.com> - 0.1.3-5
- build on ia64 now

* Thu Jul 27 2006 Jeremy Katz <katzj@redhat.com> - 0.1.3-4
- don't BR xen, we just need xen-devel

* Thu Jul 27 2006 Daniel Veillard <veillard@redhat.com> 0.1.3-3
- need rebuild since libxenstore is now versionned

* Mon Jul 24 2006 Mark McLoughlin <markmc@redhat.com> - 0.1.3-2
- Add BuildRequires: xen-devel

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.1.3-1.1
- rebuild

* Tue Jul 11 2006 Daniel Veillard <veillard@redhat.com> 0.1.3-1
- support for HVM Xen guests
- various bugfixes

* Mon Jul  3 2006 Daniel Veillard <veillard@redhat.com> 0.1.2-1
- added a proxy mechanism for read only access using httpu
- fixed header includes paths

* Wed Jun 21 2006 Daniel Veillard <veillard@redhat.com> 0.1.1-1
- extend and cleanup the driver infrastructure and code
- python examples
- extend uuid support
- bug fixes, buffer handling cleanups
- support for new Xen hypervisor API
- test driver for unit testing
- virsh --conect argument

* Mon Apr 10 2006 Daniel Veillard <veillard@redhat.com> 0.1.0-1
- various fixes
- new APIs: for Node information and Reboot
- virsh improvements and extensions
- documentation updates and man page
- enhancement and fixes of the XML description format

* Tue Feb 28 2006 Daniel Veillard <veillard@redhat.com> 0.0.6-1
- added error handling APIs
- small bug fixes
- improve python bindings
- augment documentation and regression tests

* Thu Feb 23 2006 Daniel Veillard <veillard@redhat.com> 0.0.5-1
- new domain creation API
- new UUID based APIs
- more tests, documentation, devhelp
- bug fixes

* Fri Feb 10 2006 Daniel Veillard <veillard@redhat.com> 0.0.4-1
- fixes some problems in 0.0.3 due to the change of names

* Wed Feb  8 2006 Daniel Veillard <veillard@redhat.com> 0.0.3-1
- changed library name to libvirt from libvir, complete and test the python
  bindings

* Sun Jan 29 2006 Daniel Veillard <veillard@redhat.com> 0.0.2-1
- upstream release of 0.0.2, use xend, save and restore added, python bindings
  fixed

* Wed Nov  2 2005 Daniel Veillard <veillard@redhat.com> 0.0.1-1
- created
