%def_disable check
%define _unpackaged_files_terminate_build 1
%define _localstatedir %_var
%add_findreq_skiplist %_x11sysconfdir/xinit.d/*
%add_findreq_skiplist %_prefix/lib/kernel/install.d/*
%add_findreq_skiplist %_unitdir/local.service
%add_findreq_skiplist %_unitdir/rc-local.service
%add_findreq_skiplist %_unitdir/quotaon.service
%add_findreq_skiplist %_unitdir/initrd-switch-root.service
%add_findreq_skiplist %_unitdir/systemd-volatile-root.service

%def_enable static_libsystemd
%def_enable static_libudev
%def_enable elfutils
%def_enable libcryptsetup
%def_enable logind
%def_enable vconsole
%def_enable initrd
%def_enable quotacheck
%def_enable randomseed
%def_enable coredump
%def_enable pstore
%def_enable gcrypt
%def_disable qrencode
%def_enable microhttpd
%def_enable gnutls
%def_enable openssl
%def_enable libcurl
%def_disable libidn
%def_enable libidn2
%def_enable libiptc
%def_enable polkit
%def_enable efi
%def_enable homed
%def_enable pwquality
%def_enable networkd
%def_enable timesyncd
%def_enable resolve
%ifarch %{ix86} x86_64 aarch64 %arm
%def_enable gnuefi
%endif
%def_disable p11kit
%def_enable utmp
%def_enable xz
%def_enable zlib
%def_enable bzip2
%def_enable lz4
%def_enable zstd

%def_disable smack
%def_enable seccomp
%def_disable ima
%def_enable selinux
%def_disable apparmor

%define hierarchy unified
%def_enable kill_user_processes

%def_enable sysusers
%def_disable ldconfig
%def_enable firstboot
%def_disable standalone_binaries

%if_enabled sysusers
%def_enable ldconfig
%endif

%ifnarch riscv64
%def_enable kexec
%endif

# TODO: move libbpf to /lib
# from meson.build: bpf_arches = ['x86_64']
%ifarch x86_64
%def_disable bpf_framework
%else
%def_disable bpf_framework
%endif

%ifarch ia64 %ix86 ppc64le x86_64 aarch64
%define mmap_min_addr 65536
%else
%define mmap_min_addr 32768
%endif

%define ver_major 249

Name: systemd
Epoch: 1
Version: %ver_major
Release: alt1
Summary: System and Session Manager
Url: https://www.freedesktop.org/wiki/Software/systemd
Group: System/Configuration/Boot and Init
License: LGPLv2.1+


Packager: Alexey Shabalin <shaba@altlinux.ru>

Source: %name-%version.tar
Source2: systemd-sysv-install
Source4: altlinux-openresolv.path
Source5: altlinux-openresolv.service
Source6: altlinux-libresolv.path
Source7: altlinux-libresolv.service
Source10: systemd-udev-trigger-no-reload.conf
Source11: env-path-user.conf
Source12: env-path-system.conf
Source14: systemd-user.pam
Source19: udevd.init
Source22: scsi_id.config
Source23: var-lock.mount
Source24: var-run.mount
Source27: altlinux-first_time.service
Source30: 49-coredump-disable.conf
Source31: 60-raw.rules
# ALTLinux's default preset policy
Source34: 85-display-manager.preset
Source35: 90-default.preset
Source36: 99-default-disable.preset
Source37: 85-networkd.preset
Source38: 85-timesyncd.preset

Source44: 10-oomd-defaults.conf
Source45: 10-oomd-root-slice-defaults.conf
Source46: 10-oomd-user-service-defaults.conf

# simpleresolv
Source68: altlinux-simpleresolv.path
Source69: altlinux-simpleresolv.service

# rpm filetriggers
Source71: udev.filetrigger
Source72: udev-hwdb.filetrigger
Source73: systemd.filetrigger
Source74: systemd-tmpfiles.filetrigger
Source75: systemd-sysctl.filetrigger
Source76: systemd-binfmt.filetrigger
Source77: journal-catalog.filetrigger
Source78: systemd-sysusers.filetrigger
Source79: systemd-modules-load.filetrigger

Patch1: %name-%version.patch

%define dbus_ver 1.11.0

BuildRequires(pre): rpm-build-xdg meson >= 0.49
BuildRequires: glibc-kernheaders
BuildRequires: intltool >= 0.40.0
BuildRequires: gperf
BuildRequires: libcap-devel libcap-utils
BuildRequires: libpam-devel
BuildRequires: libacl-devel acl
BuildRequires: xsltproc docbook-style-xsl docbook-dtds python3-module-lxml
BuildRequires: python3(jinja2)
BuildRequires: libdbus-devel >= %dbus_ver
%{?_enable_seccomp:BuildRequires: pkgconfig(libseccomp) >= 2.3.1}
%{?_enable_selinux:BuildRequires: pkgconfig(libselinux) >= 2.1.9}
%{?_enable_apparmor:BuildRequires: pkgconfig(libapparmor)}
%{?_enable_elfutils:BuildRequires: elfutils-devel >= 0.158}
BuildRequires: libaudit-devel
%{?_enable_xz:BuildRequires: pkgconfig(liblzma)}
%{?_enable_zlib:BuildRequires: pkgconfig(zlib)}
%{?_enable_bzip2:BuildRequires: bzlib-devel}
%{?_enable_lz4:BuildRequires: pkgconfig(liblz4) >= 1.3.0}
%{?_enable_zstd:BuildRequires: pkgconfig(libzstd) >= 1.4.0}
BuildRequires: libkmod-devel >= 15 kmod
%{?_enable_kexec:BuildRequires: kexec-tools}
BuildRequires: quota
BuildRequires: pkgconfig(blkid) >= 2.24
# temporarily lower libmount version check
# util-linux 2.27.1's configure.ac still claims to be 2.27.0, which breaks our version check
BuildRequires: libmount-devel >= 2.30
BuildRequires: pkgconfig(mount) >= 2.27
BuildRequires: pkgconfig(xkbcommon) >= 0.3.0
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: libkeyutils-devel
BuildRequires: pkgconfig(fdisk) >= 2.33

%{?_enable_libcryptsetup:BuildRequires: libcryptsetup-devel >= 2.0.1}
%{?_enable_gcrypt:BuildRequires: libgcrypt-devel >= 1.4.5 libgpg-error-devel >= 1.12}
%{?_enable_openssl:BuildRequires: pkgconfig(openssl) >= 1.1.0}
%{?_enable_p11kit:BuildRequires: pkgconfig(p11-kit-1) >= 0.23.3}
%{?_enable_qrencode:BuildRequires: libqrencode-devel >= 4}
%{?_enable_microhttpd:BuildRequires: pkgconfig(libmicrohttpd) >= 0.9.33}
%{?_enable_gnutls:BuildRequires: pkgconfig(gnutls) >= 3.1.4}
%{?_enable_libcurl:BuildRequires: pkgconfig(libcurl) >= 7.32.0}
%{?_enable_libidn:BuildRequires: pkgconfig(libidn)}
%{?_enable_libidn2:BuildRequires: pkgconfig(libidn2) >= 2.0.0}
%{?_enable_libiptc:BuildRequires: pkgconfig(libiptc)}
%{?_enable_polkit:BuildRequires: pkgconfig(polkit-gobject-1)}
%{?_enable_gnuefi:BuildRequires: gnu-efi}
%{?_enable_pstore:BuildRequires: libacl-devel libdw-devel liblzma-devel liblz4-devel}
%{?_enable_pwquality:BuildRequires: pkgconfig(pwquality)}
%{?_enable_bpf_framework:BuildRequires: pkgconfig(libbpf) >= 0.2 /usr/bin/clang /usr/bin/llvm-strip bpftool}
# for make check
#BuildRequires: /proc
#BuildRequires: lz4

Requires: dbus >= %dbus_ver
Requires: filesystem >= 2.3.10-alt1
Requires: agetty
Requires: acl
Requires: util-linux >= 2.27.1
Requires: libseccomp >= 2.3.1
%{?_enable_libidn:Requires: libidn >= 1.33-alt2}
%{?_enable_libidn2:Requires: libidn2 > 2.0.4-alt3}


# Requires: selinux-policy >= 3.8.5
Requires: %name-utils = %EVR
Requires: %name-services = %EVR
%{?_enable_efi:Requires: %name-boot-efi = %EVR}
Requires: pam_%name = %EVR

Requires: libnss-myhostname = %EVR

# Copy from SysVinit
Requires: coreutils
Requires: /sbin/sulogin
Requires: sysvinit-utils

Obsoletes: systemd-units < 0:43-alt1
Provides: systemd-units = %EVR
Provides: syslogd-daemon

# SBAT generation number for ALT (refer to SBAT.md)
%define sbat_distro altlinux
%define sbat_distro_generation 1
%define sbat_distro_summary "ALT Linux"
%define sbat_distro_pkgname systemd-boot-efi
%define sbat_distro_version %version-%release
%define sbat_distro_url http://git.altlinux.org/gears/s/systemd.git

%description
systemd is a system and session manager for Linux, compatible with
SysV and LSB init scripts. systemd provides aggressive parallelization
capabilities, uses socket and D-Bus activation for starting services,
offers on-demand starting of daemons, keeps track of processes using
Linux cgroups, supports snapshotting and restoring of the system
state, maintains mount and automount points and implements an
elaborate transactional dependency-based service control logic. It can
work as a drop-in replacement for sysvinit.

%package -n libsystemd
Group: System/Libraries
Summary: Systemd Library

%description -n libsystemd
The libsystemd library provides a reference implementation of various
APIs for new-style daemons, as implemented by the systemd init system.

%package -n libsystemd-devel
Group: Development/C
Summary: Development headers for systemd Library
License: LGPLv2+ and MIT

Requires: libsystemd = %EVR

Provides: libsystemd-daemon-devel = %EVR
Provides: libsystemd-journal-devel = %EVR
Provides: libsystemd-login-devel = %EVR
Provides: libsystemd-id128-devel = %EVR
Provides: systemd-devel = %EVR

Obsoletes: libsystemd-daemon-devel < %EVR
Obsoletes: libsystemd-journal-devel < %EVR
Obsoletes: libsystemd-login-devel < %EVR
Obsoletes: libsystemd-id128-devel < %EVR
Obsoletes: systemd-devel < %EVR

%description -n libsystemd-devel
The libsystemd library provides a reference implementation of various
APIs for new-style daemons, as implemented by the systemd init system.

%package -n libsystemd-devel-static
Group: Development/C
Summary: Development static libraries for systemd
License: LGPLv2+ and MIT

%description -n libsystemd-devel-static
Static Library files for doing development with the systemd.

%package -n libnss-systemd
Group: System/Libraries
Summary: nss-systemd providing UNIX user and group name resolution for dynamic users and groups
Requires(pre): chrooted >= 0.3.5-alt1 chrooted-resolv sed
Requires(postun): chrooted >= 0.3.5-alt1 sed
Requires: systemd

%description -n libnss-systemd
nss-systemd is a plug-in module for the GNU Name Service Switch (NSS) functionality of the
GNU C Library glibc, providing UNIX user and group name resolution for dynamic users and
groups allocated through the DynamicUser= option in systemd unit files.

This module also ensures that the root and nobody users and groups (i.e. the users/groups with the UIDs/GIDs
0 and 65534) remain resolvable at all times, even if they aren't listed in /etc/passwd or
/etc/group, or if these files are missing.

To activate the NSS module, add systemd to the lines starting with
passwd: and group: in /etc/nsswitch.conf.

passwd: files systemd
group: files systemd

%package -n libnss-myhostname
Group: System/Libraries
Summary: nss-myhostname provide hostname resolution for the locally configured system hostname
Requires(pre): chrooted >= 0.3.5-alt1 chrooted-resolv sed
Requires(postun): chrooted >= 0.3.5-alt1 sed

%description -n libnss-myhostname
nss-myhostname is a plugin for the GNU Name Service Switch (NSS)
functionality of the GNU C Library (glibc) providing host name
resolution for the locally configured system hostname as returned by
gethostname(2). Various software relies on an always resolvable local
host name. When using dynamic hostnames this is usually achieved by
patching /etc/hosts at the same time as changing the host name. This
however is not ideal since it requires a writable /etc file system and
is fragile because the file might be edited by the administrator at
the same time. nss-myhostname simply returns all locally configure
public IP addresses, or -- if none are configured -- the IPv4 address
127.0.0.2 (wich is on the local loopback) and the IPv6 address ::1
(which is the local host) for whatever system hostname is configured
locally. Patching /etc/hosts is thus no longer necessary.

It is necessary to change "hosts" in /etc/nsswitch.conf to
hosts: files myhostname

%package -n libnss-mymachines
Group: System/Libraries
Summary: libnss-mymachines is plugin for local system host name resolution
Requires(pre): chrooted >= 0.3.5-alt1 chrooted-resolv sed
Requires(postun): chrooted >= 0.3.5-alt1 sed
Requires: dbus >= %dbus_ver
Requires: %name-services = %EVR
Requires: systemd-container

%description -n libnss-mymachines
nss-mymachines for automatically resolves the names
of all local registered containers to their respective IP addresses.

It is necessary to change "hosts" in /etc/nsswitch.conf to
hosts: files mymachines

%package -n libnss-resolve
Group: System/Libraries
Summary: nss-resolve is plugin for resolve hostnames via systemd-resolved
Requires(pre): chrooted >= 0.3.5-alt1 chrooted-resolv sed
Requires(postun): chrooted >= 0.3.5-alt1 sed
Requires: dbus >= %dbus_ver
Requires: %name-networkd = %EVR

%description -n libnss-resolve
NSS module "nss-resolve" has been added which can be used
instead of glibc's own "nss-dns" to resolve hostnames via
systemd-resolved. Hostnames, addresses and arbitrary RRs may
be resolved via systemd-resolved D-Bus APIs. In contrast to
the glibc internal resolver systemd-resolved is aware of
multi-homed system, and keeps DNS server and caches separate
and per-interface.

It is necessary to change "hosts" in /etc/nsswitch.conf to
hosts: files resolve

%package -n pam_%name
Group: System/Base
Summary: Register user sessions in the systemd login manager
Requires: dbus >= %dbus_ver
Conflicts: %name < 1:216-alt1

%description -n pam_%name
pam_systemd registers user sessions with the systemd login manager
systemd-logind.service, and hence the systemd control group hierarchy.

%package -n pam_%{name}_home
Group: System/Base
Summary: Automatically mount home directories managed by systemd-homed.service on login
Requires: dbus >= %dbus_ver

%description -n pam_%{name}_home
pam_systemd_home ensures that home directories managed by systemd-homed.service
are automatically activated (mounted) on user login,
and are deactivated (unmounted) when the last session of the user ends.

%package sysvinit
Group: System/Configuration/Boot and Init
Summary: systemd System V init tools
Requires: %name = %EVR
# Obsoletes: SysVinit
Provides: SysVinit = 2.88-alt0.1
#Obsoletes:      upstart
Conflicts: upstart
Conflicts: SysVinit
BuildArch: noarch

%description sysvinit
Drop-in replacement for the System V init tools of systemd.

%package utils
Group: System/Configuration/Boot and Init
Summary: systemd utils
Provides: /sbin/systemctl
Provides: /bin/systemctl
Provides: /usr/bin/systemctl
Provides: /bin/journalctl
Provides: /sbin/journalctl
Provides: journalctl = %EVR
Obsoletes: journalctl < %EVR
Obsoletes: libsystemd-shared < %EVR
Obsoletes: bash-completion-%name < %EVR
Obsoletes: bash-completion-journalctl < %EVR
Obsoletes: zsh-completion-%name < %EVR
Obsoletes: zsh-completion-journalctl < %EVR
%if_disabled standalone_binaries
Provides: systemd-modules-load-standalone = %EVR
Provides: systemd-tmpfiles-standalone = %EVR
Provides: systemd-sysctl-standalone = %EVR
Obsoletes: systemd-modules-load-standalone < %EVR
Obsoletes: systemd-tmpfiles-standalone < %EVR
Obsoletes: systemd-sysctl-standalone < %EVR
%endif

%description utils
This package contains utils from systemd:
 - systemd-binfmt
 - systemd-modules-load
 - systemd-sysctl
 - systemd-tmpfiles
 - systemd-firstboot
 - systemctl
 - journalctl

%package services
Group: System/Configuration/Boot and Init
Summary: systemd services
Conflicts: %name < %EVR
Requires: pam_%name = %EVR
Requires: %name-utils = %EVR
Requires: dbus >= %dbus_ver
Conflicts: service <= 0.5.25-alt1
Conflicts: chkconfig <= 1.3.59-alt3
Conflicts: ConsoleKit2 ConsoleKit2-x11

%description services
This package contains dbus services and utils from systemd:
 - systemd-hostnamed and hostnamectl
 - systemd-localed and localectl
 - systemd-logind and loginctl
 - systemd-oomd and oomctl
 - systemd-timedated and timedatectl
 - systemd-userdbd and userdbctl

%package networkd
Group: System/Base
Summary: System daemon that manages network configurations
Conflicts: %name < 1:214-alt13
Requires: %name = %EVR
Requires: iproute2
Provides: network-config-subsystem

%description networkd
systemd-networkd is a system service that manages networks.
It detects and configures network devices as they appear,
as well as creating virtual network devices.

%package oomd-defaults
Group: System/Base
Summary: Configuration files for systemd-oomd
BuildArch: noarch
Requires: %name = %EVR
 
%description oomd-defaults
A set of drop-in files for systemd units to enable action from systemd-oomd,
a userspace out-of-memory (OOM) killer.

%package timesyncd
Group: System/Configuration/Other
Summary: Network Time Synchronization
Conflicts: %name < 1:214-alt13
Requires: %name-networkd = %EVR
Requires: libnss-systemd = %EVR
Provides: ntp-client
Provides: ntp-server

%description timesyncd
systemd-timesyncd is a system service that may be used
to synchronize the local system clock with a Network Time Protocol Server.

%package container
Summary: Tools for containers and VMs
Group: System/Configuration/Other
Requires: %name = %EVR
#Requires: libnss-mymachines = %EVR
Provides: /lib/systemd/systemd-machined

%description container
Systemd tools to spawn and manage containers and virtual machines.

This package contains systemd-nspawn, machinectl, systemd-machined,
and systemd-importd.

%package portable
Summary: Tools for Portable Services
Group: System/Configuration/Other
Requires: %name = %EVR

%description portable
A portable service is ultimately just an OS tree, either inside of a directory
tree, or inside a raw disk image containing a Linux file system.

%package homed
Summary: Home Directory/User Account Manager
Group: System/Configuration/Other
Requires: %name = %EVR
Requires: pam_%{name}_home = %EVR

%description homed
systemd-homed is a system service that may be used
to create, remove, change or inspect home directories.

%package analyze
Group: System/Configuration/Boot and Init
Summary: Analyze tool for systemd.
Requires: %name = %EVR

%description analyze
Analyze tool for systemd.

%package journal-remote
Group: System/Servers
Summary: Journal Gateway Daemon
Requires: %name = %EVR
Requires: libnss-systemd  = %EVR
Requires: %name-stateless = %EVR
Provides: systemd-journal-gateway = %EVR
Obsoletes: systemd-journal-gateway < %EVR

%description journal-remote
This service provides access to the journal via HTTP and JSON.

%package boot-efi
Group: System/Kernel and hardware
Summary: systemd-boot and bootctl utils

%description boot-efi
systemd-boot and bootctl utils.

%package coredump
Group: System/Servers
Summary: systemd-coredump and coredumpctl utils
Requires: %name = %EVR

%description coredump
systemd-coredump and coredumpctl utils.

%package stateless
Group: System/Servers
Summary: systems that boot up with an empty /etc directory
Requires: %name = %EVR
%if_disabled standalone_binaries
Provides: systemd-sysusers-standalone = %EVR
Obsoletes: systemd-sysusers-standalone < %EVR
%endif

%description stateless
This package contains:
 - systemd-sysusers util and unit
 - ldconfig unit
 - systemd-update-done unit

systemd-sysusers tool creates system users and groups in /etc/passwd and
/etc/group, based on static declarative system user/group
definitions in /lib/sysusers.d/. This is useful to
enable factory resets and volatile systems that boot up with
an empty /etc directory, and thus need system users and
groups created during early boot. systemd now also ships
with two default sysusers.d/ files for the most basic
users and groups systemd and the core operating system
require.

%package -n udev
Group: System/Configuration/Hardware
Summary: udev - an userspace implementation of devfs
License: GPLv2+
Requires: shadow-utils dmsetup kmod >= 15 util-linux >= 2.27.1 losetup >= 2.19.1
Requires: systemd-utils = %EVR
Provides: hotplug = 2004_09_23-alt18
Obsoletes: hotplug
Provides: udev-extras = %EVR
Obsoletes: udev-extras < %EVR
Provides: udev-rules = %EVR
Obsoletes: udev-rules < %EVR
Provides: %_sysconfdir/udev/rules.d /lib/udev/rules.d
Provides: udev-hwdb = %EVR
Obsoletes: udev-hwdb < %EVR
Provides: %_sysconfdir/udev/hwdb.d /lib/udev/hwdb.d
Conflicts: util-linux <= 2.22-alt2
Conflicts: DeviceKit
Conflicts: make-initrd < 2.2.10
Obsoletes: bash-completion-udev < %EVR
Obsoletes: zsh-completion-udev < %EVR

%description -n udev
Starting with the 2.5 kernel, all physical and virtual devices in a
system are visible to userspace in a hierarchal fashion through
sysfs. /sbin/hotplug provides a notification to userspace when any
device is added or removed from the system. Using these two features,
a userspace implementation of a dynamic /dev is now possible that can
provide a very flexible device naming policy

%package -n libudev1
Summary: Shared library to access udev device information
Group: System/Libraries
License: LGPLv2.1+
Conflicts: libudev < 0:181-alt5

%description -n libudev1
This package provides shared library to access udev device information

%package -n libudev-devel
Summary: Libraries and headers for libudev
Group: Development/C
License: LGPLv2.1+
Requires: libudev1 = %EVR

%description -n libudev-devel
Shared library and headers for libudev

%package -n libudev-devel-static
Summary: Static Library for libudev
Group: Development/C
License: LGPLv2.1+

%description -n libudev-devel-static
Static library for libudev.

%package modules-load-standalone
Summary: Standalone systemd-modules-load binary for use in non-systemd systems
Group: System/Configuration/Boot and Init

%description modules-load-standalone
Standalone systemd-modules-load binary with no dependencies on the systemd-shared
library or other libraries from libsystemd.

%package sysctl-standalone
Summary: Standalone systemd-sysctl binary for use in non-systemd systems
Group: System/Configuration/Boot and Init

%description sysctl-standalone
Standalone systemd-sysctl binary with no dependencies on the systemd-shared
library or other libraries from libsystemd.

%package sysusers-standalone
Summary: Standalone systemd-sysusers binary for use in non-systemd systems
Group: System/Configuration/Boot and Init

%description sysusers-standalone
Standalone systemd-sysusers binary with no dependencies on the systemd-shared
library or other libraries from libsystemd.

%package tmpfiles-standalone
Summary: Standalone systemd-tmpfiles binary for use in non-systemd systems
Group: System/Configuration/Boot and Init

%description tmpfiles-standalone
Standalone systemd-tmpfiles binary with no dependencies on the systemd-shared
library or other libraries from libsystemd.

%prep
%setup -q
%patch1 -p1

%build

%meson \
	-Dmode=release \
	-Dlink-udev-shared=false \
	-Dlink-systemctl-shared=false \
	-Dlink-networkd-shared=false \
	-Dlink-timesyncd-shared=false \
	%{?_enable_static_libsystemd:-Dstatic-libsystemd=pic} \
	%{?_enable_static_libudev:-Dstatic-libudev=pic} \
	%{?_enable_standalone_binaries:-Dstandalone-binaries=true} \
	-Dxinitrcdir=%_sysconfdir/X11/xinit.d \
	-Drpmmacrosdir=no \
	-Drootlibdir=/%_lib \
	-Dpamlibdir=/%_lib/security \
	-Dsplit-usr=true \
	-Dsplit-bin=true \
	-Dsysvinit-path=%_initdir \
	-Dsysvrcnd-path=%_sysconfdir/rc.d \
	-Drc-local=%_sysconfdir/rc.d/rc.local \
	-Dinstall-sysconfdir=true \
	-Dkernel-install=true \
	-Dpamconfdir=%_sysconfdir/pam.d \
	-Ddebug-shell=/bin/bash \
	-Dquotaon-path=/sbin/quotaon \
	-Dquotacheck-path=/sbin/quotacheck \
	-Dkmod-path=/bin/kmod \
	%{?_enable_kexec:-Dkexec-path=/sbin/kexec} \
	-Dsulogin-path=/sbin/sulogin \
	-Dmount-path=/bin/mount \
	-Dumount-path=/bin/umount \
	-Dloadkeys-path=/bin/loadkeys \
	-Dsetfont-path=/bin/setfont \
	-Dtelinit-path=/sbin/telinit \
	-Dnologin-path=/sbin/nologin \
	-Dcompat-mutable-uid-boundaries=true \
	-Dsystem-uid-max=499 \
	-Dsystem-gid-max=499 \
	-Dadm-gid=4 \
	-Daudio-gid=81 \
	-Dcdrom-gid=22 \
	-Ddisk-gid=6 \
	-Dkmem-gid=9 \
	-Dlp-gid=7 \
	-Dtty-gid=5 \
	-Dusers-gid=100 \
	-Dutmp-gid=72 \
	-Dwheel-gid=10 \
	-Dnobody-user=nobody \
	-Dnobody-group=nobody \
	-Dbump-proc-sys-fs-file-max=false \
	-Dbump-proc-sys-fs-nr-open=false \
	%{?_enable_elfutils:-Delfutils=true} \
	%{?_enable_pwquality:-Dpwquality=true} \
	%{?_enable_xz:-Dxz=true} \
	%{?_enable_zlib:-Dzlib=true} \
	%{?_enable_bzip2:-Dbzip2=true} \
	%{?_enable_lz4:-Dlz4=true} \
	%{?_enable_zstd:-Dzstd=true} \
	%{?_enable_libcryptsetup:-Dlibcryptsetup=true} \
	%{?_enable_logind:-Dlogind=true} \
	%{?_enable_vconsole:-Dvconsole=true} \
	%{?_enable_initrd:-Dinitrd=true} \
	%{?_enable_quotacheck:-Dquotacheck=true} \
	%{?_enable_randomseed:-Drandomseed=true} \
	%{?_enable_bpf_framework:-Dbpf-framework=true} \
	%{?_enable_coredump:-Dcoredump=true} \
	%{?_enable_pstore:-Dpstore=true} \
	%{?_enable_smack:-Dsmack=true} \
	%{?_enable_gcrypt:-Dgcrypt=true} \
	%{?_enable_qrencode:-Dqrencode=true} \
	%{?_enable_microhttpd:-Dmicrohttpd=true} \
	%{?_enable_gnutls:-Dgnutls=true} \
	%{?_enable_openssl:-Dopenssl=true } \
	%{?_enable_p11kit:-Dp11kit=true } \
	%{?_enable_libcurl:-Dlibcurl=true} \
	%{?_enable_libidn:-Dlibidn=true} \
	%{?_enable_libidn2:-Dlibidn2=true} \
	%{?_enable_libiptc:-Dlibiptc=true} \
	%{?_enable_polkit:-Dpolkit=true} \
	%{?_enable_efi:-Defi=true} \
	-Dsbat-distro=%sbat_distro \
	-Dsbat-distro-generation=%sbat_distro_generation \
	-Dsbat-distro-summary=%sbat_distro_summary \
	-Dsbat-distro-pkgname=%sbat_distro_pkgname \
	-Dsbat-distro-version=%sbat_distro_version \
	-Dsbat-distro-url=%sbat_distro_url \
	%{?_enable_homed:-Dhomed=true} \
	%{?_enable_networkd:-Dnetworkd=true} \
	%{?_enable_resolve:-Dresolve=true} \
	-Ddns-servers="" \
	%{?_enable_timesyncd:-Dtimesyncd=true} \
	-Dntp-servers="" \
	%{?_enable_sysusers:-Dsysusers=true} \
	%{?_enable_ldconfig:-Dldconfig=true} \
	%{?_enable_firstboot:-Dfirstboot=true} \
	%{?_enable_gnuefi:-Dgnuefi=true} \
	%{?_enable_seccomp:-Dseccomp=true} \
	%{?_enable_ima:-Dima=true} \
	%{?_enable_selinux:-Dselinux=true} \
	%{?_enable_apparmor:-Dapparmor=true} \
	%{?_enable_utmp:-Dutmp=true} \
	%{?_disable_kill_user_processes:-Ddefault-kill-user-processes=false} \
	-Doomd=true \
	-Dfallback-hostname=localhost \
	-Ddefault-dnssec=no \
	-Ddefault-mdns=no \
	-Ddefault-llmnr=yes \
	-Ddefault-hierarchy=%hierarchy \
%ifnarch mipsel
	-Db_lto=true \
%else
	-Db_lto=false \
%endif
	-Db_pie=true \
	-Dman=true \
	-Dtests=true \
	-Dversion-tag=v%version-%release \
	-Dcertificate-root=/etc/pki/tls \
	-Ddocdir=%_defaultdocdir/%name-%version

%meson_build

%install
%meson_install

# remove .so file for the shared library, it's not supposed to be used
rm -f %buildroot/lib/systemd/libsystemd-shared.so
# remove systemd rpm macros
rm -f %buildroot/usr/lib/rpm/macros.d/macros.systemd
# remove linuxia32.elf.stub
# debugedit: Failed to update file: invalid section entry size
%ifarch %ix86
rm -f %buildroot/%_prefix/lib/systemd/boot/efi/linuxia32.elf.stub
%endif

%find_lang %name

# Make sure these directories are properly owned
mkdir -p %buildroot%_unitdir/{basic,dbus,default,graphical,poweroff,rescue,reboot,sysinit}.target.wants

install -m755 %SOURCE2 %buildroot/lib/systemd/systemd-sysv-install

ln -s rc-local.service %buildroot%_unitdir/local.service
install -m644 %SOURCE4 %buildroot%_unitdir/altlinux-openresolv.path
install -m644 %SOURCE5 %buildroot%_unitdir/altlinux-openresolv.service
install -m644 %SOURCE68 %buildroot%_unitdir/altlinux-simpleresolv.path
install -m644 %SOURCE69 %buildroot%_unitdir/altlinux-simpleresolv.service
ln -s ../altlinux-openresolv.path %buildroot%_unitdir/multi-user.target.wants
ln -s ../altlinux-simpleresolv.path %buildroot%_unitdir/multi-user.target.wants
install -m644 %SOURCE6 %buildroot%_unitdir/altlinux-libresolv.path
install -m644 %SOURCE7 %buildroot%_unitdir/altlinux-libresolv.service
ln -s ../altlinux-libresolv.path %buildroot%_unitdir/multi-user.target.wants
install -m644 %SOURCE27 %buildroot%_unitdir/altlinux-first_time.service
ln -s ../altlinux-first_time.service %buildroot%_unitdir/basic.target.wants
ln -s systemd-random-seed.service %buildroot%_unitdir/random.service
ln -s systemd-reboot.service %buildroot%_unitdir/reboot.service
ln -s systemd-halt.service %buildroot%_unitdir/halt.service
ln -s systemd-tmpfiles-setup.service %buildroot%_unitdir/tmpfiles.service

# Make sure the NTP units dir exists
mkdir -p %buildroot/lib/systemd/ntp-units.d
mkdir -p %buildroot%_sysconfdir/systemd/ntp-units.d

# restore bind-mounts /var/run -> run and /var/lock -> /run/lock
# we don't have those directories symlinked
install -m644 %SOURCE23 %buildroot%_unitdir/var-lock.mount
install -m644 %SOURCE24 %buildroot%_unitdir/var-run.mount
ln -r -s %buildroot%_unitdir/var-lock.mount %buildroot%_unitdir/local-fs.target.wants
ln -r -s %buildroot%_unitdir/var-run.mount %buildroot%_unitdir/local-fs.target.wants

# turn off tmp.mount by default (ALT#29066)
rm -f %buildroot%_unitdir/tmp.mount
rm -f %buildroot%_unitdir/local-fs.target.wants/tmp.mount

find %buildroot \( -name '*.la' \) -exec rm {} \;
mkdir -p %buildroot/{sbin,bin}
ln -r -s %buildroot/lib/systemd/systemd %buildroot/sbin/systemd

ln -r -s %buildroot/lib/systemd/systemd-{binfmt,modules-load,sysctl} %buildroot/sbin/
# for compatibility with older systemd pkgs which expected it at /sbin/:
ln -r -s %buildroot/bin/systemctl %buildroot/sbin/
ln -r -s %buildroot/bin/systemctl %buildroot%_bindir/
ln -r -s %buildroot/bin/journalctl %buildroot/sbin/

# add defaults services
ln -r -s %buildroot%_unitdir/remote-fs.target %buildroot%_unitdir/multi-user.target.wants
ln -r -s %buildroot%_unitdir/machines.target %buildroot%_unitdir/multi-user.target.wants
ln -r -s %buildroot%_unitdir/systemd-quotacheck.service %buildroot%_unitdir/local-fs.target.wants
ln -r -s %buildroot%_unitdir/quotaon.service %buildroot%_unitdir/local-fs.target.wants
%if_enabled pstore
ln -r -s %buildroot%_unitdir/systemd-pstore.service %buildroot%_unitdir/sysinit.target.wants
%endif

# create drop-in to prevent tty1 to be cleared
mkdir -p %buildroot%_unitdir/getty@tty1.service.d
cat > %buildroot%_unitdir/getty@tty1.service.d/noclear.conf << EOF
[Service]
# ensure tty1 isn't cleared
TTYVTDisallocate=no
EOF

# don't enable wall ask password service, it spams every console
rm -f %buildroot%_unitdir/multi-user.target.wants/systemd-ask-password-wall.path

# disable legacy services
ln -s /dev/null %buildroot%_unitdir/fbsetfont.service
ln -s /dev/null %buildroot%_unitdir/keytable.service
ln -s /dev/null %buildroot%_unitdir/killall.service
ln -s /dev/null %buildroot%_unitdir/single.service
ln -s /dev/null %buildroot%_unitdir/netfs.service

# create modules.conf as a symlink to /etc/modules
mkdir -p %buildroot/lib/modules-load.d
mkdir -p %buildroot%_sysconfdir/modules-load.d
ln -r -s %buildroot%_sysconfdir/modules %buildroot%_sysconfdir/modules-load.d/modules.conf

# create /etc/sysctl.d/99-sysctl.conf as a symlink to /etc/sysctl.conf
mkdir -p %buildroot%_sysconfdir/sysctl.d
ln -r -s %buildroot%_sysconfdir/sysctl.conf %buildroot%_sysconfdir/sysctl.d/99-sysctl.conf

# Make sure directories in /var exist
mkdir -p %buildroot%_localstatedir/lib/systemd/coredump
mkdir -p %buildroot%_localstatedir/lib/systemd/catalog
mkdir -p %buildroot%_localstatedir/lib/systemd/backlight
mkdir -p %buildroot%_localstatedir/lib/systemd/rfkill
mkdir -p %buildroot%_localstatedir/lib/systemd/linger
mkdir -p %buildroot%_localstatedir/lib/systemd/journal-upload
mkdir -p %buildroot%_localstatedir/lib/private/systemd/journal-upload
mkdir -p %buildroot%_logdir/private
mkdir -p %buildroot%_localstatedir/cache/private
mkdir -p %buildroot%_localstatedir/lib/systemd/timesync
mkdir -p %buildroot%_logdir/journal
touch %buildroot%_localstatedir/lib/systemd/catalog/database
touch %buildroot%_sysconfdir/udev/hwdb.bin
touch %buildroot%_localstatedir/lib/systemd/random-seed
touch %buildroot%_localstatedir/lib/systemd/timesync/clock

# Create new-style configuration files so that we can ghost-own them
touch %buildroot%_sysconfdir/hostname
touch %buildroot%_sysconfdir/vconsole.conf
touch %buildroot%_sysconfdir/locale.conf
touch %buildroot%_sysconfdir/machine-info

# fix pam.d/systemd-user for ALTLinux
install -m644 %SOURCE14 %buildroot%_sysconfdir/pam.d/systemd-user

# Install ALTLinux default preset policy
mkdir -p %buildroot/lib/systemd/system-preset
mkdir -p %buildroot%_sysconfdir/systemd/system-preset
mkdir -p %buildroot/lib/systemd/user-preset
mkdir -p %buildroot%_sysconfdir/systemd/user-preset
mkdir -p %buildroot%_prefix/lib/systemd/user-preset
install -m 0644 %SOURCE34 %buildroot/lib/systemd/system-preset/
install -m 0644 %SOURCE35 %buildroot/lib/systemd/system-preset/
install -m 0644 %SOURCE36 %buildroot/lib/systemd/system-preset/
install -m 0644 %SOURCE37 %buildroot/lib/systemd/system-preset/
install -m 0644 %SOURCE38 %buildroot/lib/systemd/system-preset/

# systemd-oomd default configuration
install -D -m 0644 -t %buildroot/lib/systemd/oomd.conf.d/ %SOURCE44
install -D -m 0644 -t %buildroot%_unitdir/-.slice.d/ %SOURCE45
install -D -m 0644 -t %buildroot%_unitdir/user@.service.d/ %SOURCE46

mkdir -p %buildroot%_sysconfdir/systemd/network

# The following services are currently installed by initscripts
#pushd %buildroot%_unitdir/graphical.target.wants && {
#	rm -f display-manager.service
#	rm -f dm.service
#popd
#}

# Set up the pager to make it generally more useful
mkdir -p %buildroot%_sysconfdir/profile.d
cat > %buildroot%_sysconfdir/profile.d/systemd.sh << EOF
export SYSTEMD_PAGER="/usr/bin/less -FR"
EOF
chmod 755 %buildroot%_sysconfdir/profile.d/systemd.sh

install -m644 %SOURCE30 %buildroot/lib/sysctl.d/49-coredump-disable.conf
# rpm posttrans filetriggers
install -pD -m755 %SOURCE71 %buildroot%_rpmlibdir/udev.filetrigger
install -pD -m755 %SOURCE72 %buildroot%_rpmlibdir/udev-hwdb.filetrigger
install -pD -m755 %SOURCE73 %buildroot%_rpmlibdir/systemd.filetrigger
install -pD -m755 %SOURCE74 %buildroot%_rpmlibdir/systemd-tmpfiles.filetrigger
install -pD -m755 %SOURCE75 %buildroot%_rpmlibdir/systemd-sysctl.filetrigger
install -pD -m755 %SOURCE76 %buildroot%_rpmlibdir/systemd-binfmt.filetrigger
install -pD -m755 %SOURCE77 %buildroot%_rpmlibdir/journal-catalog.filetrigger
install -pD -m755 %SOURCE78 %buildroot%_rpmlibdir/systemd-sysusers.filetrigger
install -pD -m755 %SOURCE79 %buildroot%_rpmlibdir/systemd-modules-load.filetrigger

cat >>%buildroot/lib/sysctl.d/50-mmap-min-addr.conf <<EOF
# Indicates the amount of address space which a user process will be
# restricted from mmaping.  Since kernel null dereference bugs could
# accidentally operate based on the information in the first couple of
# pages of memory userspace processes should not be allowed to write to
# them.  By default, this value in kernel is set to 0 and no protections
# will be enforced by the security module.  Setting this value to
# something >= 32k will allow the vast majority of applications to work
# correctly and provide defense in depth against future potential kernel
# bugs.  This value is somewhat architecture-dependent, though.
# Recommended default for x86_64 is 65536.
vm.mmap_min_addr = %mmap_min_addr
EOF

# define default PATH for system and user
mkdir -p %buildroot%_prefix/lib/systemd/user.conf.d
install -m 0644 %SOURCE11 %buildroot%_prefix/lib/systemd/user.conf.d/env-path.conf
#mkdir -p %buildroot%_prefix/systemd/system.conf.d
#install -m 0644 %SOURCE12 %buildroot%_prefix/systemd/system.conf.d/env-path.conf

#######
# UDEV
#######
mkdir -p %buildroot%_initdir
install -p -m755 %SOURCE19 %buildroot%_initdir/udevd

ln -s systemd-udevd.service %buildroot%_unitdir/udevd.service

# compatibility symlinks to udevd binary
ln -r -s %buildroot/lib/systemd/systemd-udevd %buildroot/lib/udev/udevd
ln -r -s %buildroot/lib/systemd/systemd-udevd %buildroot/sbin/udevd

install -p -m644 %SOURCE22 %buildroot%_sysconfdir/scsi_id.config

cat >>%buildroot%_sysconfdir/udev/udev.conf <<EOF
# Whether to mount a tmpfs filesystem to \$udev_root
udev_tmpfs="1"

# tmpfs options. Note that size shouldn't be less than several
# megabytes due to insane format of current udev database
# (in /dev/.udevdb)
tmpfs_options="size=5m"
EOF

# Install symlinks for rules which are needed in initramfs
mkdir -p %buildroot/lib/udev/initramfs-rules.d
for f in \
	50-udev-default.rules \
	60-persistent-storage.rules \
	80-drivers.rules
do
	ln -s ../rules.d/"$f" \
		%buildroot/lib/udev/initramfs-rules.d/
done
# Create ghost files
touch %buildroot%_sysconfdir/udev/hwdb.bin


echo ".so man8/systemd-udevd.8" > %buildroot%_man8dir/udevd.8

install -p -m644 %SOURCE31 %buildroot%_sysconfdir/udev/rules.d/

# https://bugzilla.redhat.com/show_bug.cgi?id=1378974
install -D -m644 -t %buildroot%_unitdir/systemd-udev-trigger.service.d/ %SOURCE10

%check
export LD_LIBRARY_PATH=$(pwd)/%{__builddir}/src/shared:$(pwd)/%{__builddir}
%meson_test

%pre
groupadd -r -f systemd-journal >/dev/null 2>&1 ||:
groupadd -r -f systemd-oom >/dev/null 2>&1 ||:
useradd -g systemd-omm -c 'systemd Userspace OOM Killer' \
    -d /var/empty -s /dev/null -r -l -M systemd-omm >/dev/null 2>&1 ||:

%post
# Move old stuff around in /var/lib
[ -d %_localstatedir/lib/systemd/random-seed ] && rm -rf %_localstatedir/lib/systemd/random-seed >/dev/null 2>&1 || :
[ -e %_localstatedir/lib/random-seed ] && mv %_localstatedir/lib/random-seed %_localstatedir/lib/systemd/random-seed >/dev/null 2>&1 || :
[ -e %_localstatedir/lib/backlight ] && mv %_localstatedir/lib/backlight %_localstatedir/lib/systemd/backlight >/dev/null 2>&1 || :

/lib/systemd/systemd-random-seed save >/dev/null 2>&1 || :

# rm symlinks for network.service
[ -L %_sysconfdir/systemd/system/network.target.wants/network.service ] && rm -f %_sysconfdir/systemd/system/network.target.wants/network.service  >/dev/null 2>&1 || :
[ -L %_sysconfdir/systemd/system/multi-user.target.wants/network.service ] && rm -f %_sysconfdir/systemd/system/multi-user.target.wants/network.service  >/dev/null 2>&1 || :

# rm symlinks for prefdm.service
[ -L %_sysconfdir/systemd/system/graphical.target.wants/prefdm.service ] && rm -f %_sysconfdir/systemd/system/graphical.target.wants/prefdm.service  >/dev/null 2>&1 || :

if [ $1 -eq 1 ] ; then
     # create /var/log/journal only on initial installation
     mkdir -p %_logdir/journal
fi

# Make sure new journal files will be owned by the "systemd-journal" group
chgrp systemd-journal /run/log/journal/ /run/log/journal/`cat /etc/machine-id 2> /dev/null` %_logdir/journal/ %_logdir/journal/`cat /etc/machine-id 2> /dev/null` >/dev/null 2>&1 || :
chmod g+s  /run/log/journal/ /run/log/journal/`cat /etc/machine-id 2> /dev/null` %_logdir/journal/ %_logdir/journal/`cat /etc/machine-id 2> /dev/null` >/dev/null 2>&1 || :

# Apply ACL to the journal directory
setfacl -Rnm g:wheel:rx,d:g:wheel:rx,g:adm:rx,d:g:adm:rx %_logdir/journal/ >/dev/null 2>&1 || :

# remove obsolete systemd-readahead file and services symlink
rm -f /.readahead > /dev/null 2>&1 || :
[ -L %_sysconfdir/systemd/system/default.target.wants/systemd-readahead-collect.service ] && rm -f %_sysconfdir/systemd/system/default.target.wants/systemd-readahead-collect.service
[ -L %_sysconfdir/systemd/system/default.target.wants/systemd-readahead-replay.service ] && rm -f %_sysconfdir/systemd/system/default.target.wants/systemd-readahead-replay.service
[ -L %_sysconfdir/systemd/system/system-update.target.wants/systemd-readahead-drop.service ] && rm -f %_sysconfdir/systemd/system/system-update.target.wants/systemd-readahead-drop.service


if [ $1 -eq 1 ] ; then
        # Enable the services we install by default
        systemctl preset-all >/dev/null 2>&1 || :
        systemctl --global preset-all >/dev/null 2>&1 || :
fi


# Migrate /etc/sysconfig/clock
SYSCONFIG_CLOCK=/etc/sysconfig/clock
if [ ! -L /etc/localtime -a -e "$SYSCONFIG_CLOCK" ] ; then
       . "$SYSCONFIG_CLOCK" >/dev/null 2>&1 || :
       if [ -n "$ZONE" -a -e "/usr/share/zoneinfo/$ZONE" ] ; then
              ln -sf "../usr/share/zoneinfo/$ZONE" /etc/localtime >/dev/null 2>&1 || :
       fi
fi
#rm -f "$SYSCONFIG_CLOCK" >/dev/null 2>&1 || :

# Migrate /etc/sysconfig/i18n
SYSCONFIG_I18N=/etc/sysconfig/i18n
if [ -e "$SYSCONFIG_I18N" -a ! -e /etc/locale.conf ]; then
        unset LANG
        unset LC_CTYPE
        unset LC_NUMERIC
        unset LC_TIME
        unset LC_COLLATE
        unset LC_MONETARY
        unset LC_MESSAGES
        unset LC_PAPER
        unset LC_NAME
        unset LC_ADDRESS
        unset LC_TELEPHONE
        unset LC_MEASUREMENT
        unset LC_IDENTIFICATION
        . "$SYSCONFIG_I18N" >/dev/null 2>&1 || :
        [ -n "$LANG" ] && echo LANG=$LANG > /etc/locale.conf 2>&1 || :
        [ -n "$LC_CTYPE" ] && echo LC_CTYPE=$LC_CTYPE >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_NUMERIC" ] && echo LC_NUMERIC=$LC_NUMERIC >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_TIME" ] && echo LC_TIME=$LC_TIME >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_COLLATE" ] && echo LC_COLLATE=$LC_COLLATE >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_MONETARY" ] && echo LC_MONETARY=$LC_MONETARY >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_MESSAGES" ] && echo LC_MESSAGES=$LC_MESSAGES >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_PAPER" ] && echo LC_PAPER=$LC_PAPER >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_NAME" ] && echo LC_NAME=$LC_NAME >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_ADDRESS" ] && echo LC_ADDRESS=$LC_ADDRESS >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_TELEPHONE" ] && echo LC_TELEPHONE=$LC_TELEPHONE >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_MEASUREMENT" ] && echo LC_MEASUREMENT=$LC_MEASUREMENT >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_IDENTIFICATION" ] && echo LC_IDENTIFICATION=$LC_IDENTIFICATION >> /etc/locale.conf 2>&1 || :
fi
#rm -f "$SYSCONFIG_I18N" >/dev/null 2>&1 || :

# Migrate /etc/sysconfig/keyboard and /etc/sysconfig/consolefont
SYSCONFIG_KEYBOARD=/etc/sysconfig/keyboard
SYSCONFIG_CONSOLEFONT=/etc/sysconfig/consolefont
if [ -e "$SYSCONFIG_KEYBOARD" -a -e "$SYSCONFIG_CONSOLEFONT" -a ! -e /etc/vconsole.conf ]; then
        unset SYSFONT
	unset SYSFONTACM
	unset UNIMAP
        unset KEYTABLE
        [ -e "$SYSCONFIG_KEYBOARD" ] && . "$SYSCONFIG_KEYBOARD" >/dev/null 2>&1 || :
        [ -e "$SYSCONFIG_CONSOLEFONT" ] && . "$SYSCONFIG_CONSOLEFONT" >/dev/null 2>&1 || :
        [ -n "$SYSFONT" ] && echo FONT=$SYSFONT > /etc/vconsole.conf 2>&1 || :
        [ -n "$SYSFONTACM" ] && echo FONT_MAP=$SYSFONTACM >> /etc/vconsole.conf 2>&1 || :
        [ -n "$UNIMAP" ] && echo FONT_UNIMAP=$UNIMAP >> /etc/vconsole.conf 2>&1 || :
        [ -n "$KEYTABLE" ] && echo KEYMAP=$KEYTABLE >> /etc/vconsole.conf 2>&1 || :
fi
#rm -f "$SYSCONFIG_KEYBOARD" >/dev/null 2>&1 || :
#rm -f "$SYSCONFIG_CONSOLEFONT" >/dev/null 2>&1 || :

# Migrate HOSTNAME= from /etc/sysconfig/network
SYSCONFIG_NETWORK=/etc/sysconfig/network
if [ -e "$SYSCONFIG_NETWORK" -a ! -e /etc/hostname ]; then
        unset HOSTNAME
        . "$SYSCONFIG_NETWORK" >/dev/null 2>&1 || :
        [ -n "$HOSTNAME" ] && echo $HOSTNAME > /etc/hostname 2>&1 || :
fi
#sed -i '/^HOSTNAME=/d' "$SYSCONFIG_NETWORK" >/dev/null 2>&1 || :

%preun
if [ $1 -eq 0 ] ; then
        systemctl disable --quiet \
                remote-fs.target \
                getty@.service \
                serial-getty@.service \
                console-getty.service \
                debug-shell.service \
                 >/dev/null 2>&1 || :

        rm -f /etc/systemd/system/default.target > /dev/null 2>&1 || :
fi

%post utils
systemd-machine-id-setup >/dev/null 2>&1 || :

%if_enabled networkd
%pre networkd
groupadd -r -f systemd-network >/dev/null 2>&1 ||:
useradd -g systemd-network -c 'systemd Network Management' \
    -d /var/empty -s /dev/null -r -l -M systemd-network >/dev/null 2>&1 ||:

groupadd -r -f systemd-resolve >/dev/null 2>&1 ||:
useradd -g systemd-resolve -c 'systemd Resolver' \
    -d /var/empty -s /dev/null -r -l -M systemd-resolve >/dev/null 2>&1 ||:

%post networkd
if [ $1 -eq 1 ] ; then
        # Enable the services we install by default
        systemctl preset \
                systemd-networkd.service \
                systemd-networkd-wait-online.service \
                systemd-resolved.service \
                 >/dev/null 2>&1 || :
fi

%preun networkd
if [ $1 -eq 0 ] ; then
        systemctl disable --quiet \
                systemd-networkd.service \
                systemd-networkd-wait-online.service \
                systemd-resolved.service \
                 >/dev/null 2>&1 || :
fi
%endif

%if_enabled coredump
%pre coredump
groupadd -r -f systemd-coredump >/dev/null 2>&1 ||:
useradd -g systemd-coredump -c 'systemd Core Dumper' \
    -d /var/empty -s /dev/null -r -l -M systemd-coredump >/dev/null 2>&1 ||:
%endif

%if_enabled timesyncd
%pre timesyncd
groupadd -r -f systemd-timesync >/dev/null 2>&1 ||:
useradd -g systemd-timesync -c 'systemd Time Synchronization' \
    -d /var/empty -s /dev/null -r -l -M systemd-timesync >/dev/null 2>&1 ||:


%post timesyncd
if [ -L %_localstatedir/lib/systemd/timesync ]; then
    rm %_localstatedir/lib/systemd/timesync
    mv %_localstatedir/lib/private/systemd/timesync %_localstatedir/lib/systemd/timesync
fi
if [ -f %_localstatedir/lib/systemd/clock ] ; then
    mkdir -p %_localstatedir/lib/systemd/timesync
    mv %_localstatedir/lib/systemd/clock %_localstatedir/lib/systemd/timesync/
fi

%post_service systemd-timesyncd.service

%preun timesyncd
%preun_service systemd-timesyncd.service

%endif

%post homed
%post_service systemd-homed.service

%preun homed
%preun_service systemd-homed.service

%post -n libnss-systemd
if [ -f /etc/nsswitch.conf ] ; then
            grep -E -q '^(passwd|group):.* systemd' /etc/nsswitch.conf ||
            sed -i.rpmorig -r -e '
                s/^(passwd|group):(.*)/\1:\2 systemd/
                ' /etc/nsswitch.conf >/dev/null 2>&1 || :
fi
update_chrooted all

%postun -n libnss-systemd
if [ "$1" = "0" ]; then
        if [ -f /etc/nsswitch.conf ] ; then
                sed -i.rpmorig -e '
                        /^(passwd|group):/ !b
                        s/[[:blank:]]\+systemd\>//
                        ' /etc/nsswitch.conf >/dev/null 2>&1 || :
        fi
fi
update_chrooted all

%post -n libnss-resolve
if [ -f /etc/nsswitch.conf ] ; then
        grep -E -q '^hosts:.* resolve' /etc/nsswitch.conf ||
        sed -i.rpmorig -r -e '
                s/^(hosts):(.*) files( mdns4_minimal .NOTFOUND=return.)? dns myhostname/\1:\2 resolve [!UNAVAIL=return] myhostname files\3 dns/
                ' /etc/nsswitch.conf >/dev/null 2>&1 || :
fi
update_chrooted all

%postun -n libnss-resolve
if [ "$1" = "0" ]; then
        if [ -f /etc/nsswitch.conf ] ; then
                sed -i.rpmorig -e '
                        /^hosts:/ !b
                        s/[[:blank:]]\+resolve\+[[:blank:]]*\[[^]]*\]*/      /
                        ' /etc/nsswitch.conf >/dev/null 2>&1 || :
        fi
fi
update_chrooted all

%post -n libnss-myhostname
if [ -f /etc/nsswitch.conf ] ; then
        grep -E -q '^hosts:.* myhostname' /etc/nsswitch.conf ||
        sed -i.rpmorig -e '
                /^hosts:/ !b
                /\<myhostname\>/ b
                s/[[:blank:]]*$/ myhostname/
                ' /etc/nsswitch.conf >/dev/null 2>&1 || :
fi
update_chrooted all

%postun -n libnss-myhostname
if [ "$1" = "0" ]; then
        if [ -f /etc/nsswitch.conf ] ; then
                sed -i.rpmorig -e '
                        /^hosts:/ !b
                        s/[[:blank:]]\+myhostname\>//
                        ' /etc/nsswitch.conf >/dev/null 2>&1 || :
        fi
fi
update_chrooted all

%post -n libnss-mymachines
if [ -f /etc/nsswitch.conf ] ; then
        grep -E -q '^hosts:.* mymachines' /etc/nsswitch.conf ||
        sed -i.rpmorig -e '
                /^hosts:/ !b
                /\<mymachines\>/ b
                s/[[:blank:]]*$/ mymachines/
                ' /etc/nsswitch.conf >/dev/null 2>&1 || :

# Cleanup. sinse v246 nss-mymachines: drop support for UID/GID resolving
        grep -v -E -q '^(passwd|group):.* mymachines' /etc/nsswitch.conf ||
        sed -i.rpmorig -e '
                /^(passwd|group):/ !b
                s/[[:blank:]]\+mymachines\>//
                ' /etc/nsswitch.conf >/dev/null 2>&1 || :
fi
update_chrooted all

%postun -n libnss-mymachines
if [ "$1" = "0" ]; then
        if [ -f /etc/nsswitch.conf ] ; then
                sed -i.rpmorig -e '
                        /^hosts:/ !b
                        s/[[:blank:]]\+mymachines\>//
                        ' /etc/nsswitch.conf >/dev/null 2>&1 || :

        fi
fi

update_chrooted all

%if_enabled microhttpd
%pre journal-remote
groupadd -r -f systemd-journal-remote ||:
useradd -g systemd-journal-remote -c 'Journal Remote' \
    -d %_logdir/journal/remote -s /dev/null -r -l systemd-journal-remote >/dev/null 2>&1 ||:

%post journal-remote
%post_service systemd-journal-gatewayd
%post_service systemd-journal-remote
%if_enabled libcurl
%post_service systemd-journal-upload
%endif

%preun journal-remote
%preun_service systemd-journal-gatewayd
%preun_service systemd-journal-remote
%if_enabled libcurl
%preun_service systemd-journal-upload
%endif

if [ $1 -eq 1 ] ; then
    if [ -f %_localstatedir/lib/systemd/journal-upload/state -a ! -L %_localstatedir/lib/systemd/journal-upload ] ; then
        mkdir -p %_localstatedir/lib/private/systemd/journal-upload
        mv %_localstatedir/lib/systemd/journal-upload/state %_localstatedir/lib/private/systemd/journal-upload/
        rmdir %_localstatedir/lib/systemd/journal-upload || :
     fi
fi
%endif

%pre -n udev
groupadd -r -f cdrom >/dev/null 2>&1 ||:
groupadd -r -f tape >/dev/null 2>&1 ||:
groupadd -r -f dialout >/dev/null 2>&1 ||:
groupadd -r -f input >/dev/null 2>&1 ||:
groupadd -r -f video >/dev/null 2>&1 ||:
groupadd -r -f render >/dev/null 2>&1 ||:
groupadd -r -f vmusers >/dev/null 2>&1 ||:

%post -n udev
udevadm hwdb --update &>/dev/null
%post_service udevd

%preun -n udev
%preun_service udevd

%files -f %name.lang
%dir %_sysconfdir/systemd/system
%dir %_sysconfdir/systemd/user

%_sysconfdir/profile.d/systemd.sh


%_tmpfilesdir/systemd-nologin.conf
%_tmpfilesdir/systemd.conf
%_tmpfilesdir/journal-nocow.conf

%_xdgconfigdir/%name
%_x11sysconfdir/xinit.d/50-systemd-user.sh

%config(noreplace) %_sysconfdir/systemd/journald.conf
%config(noreplace) %_sysconfdir/systemd/sleep.conf
%config(noreplace) %_sysconfdir/systemd/system.conf
%config(noreplace) %_sysconfdir/systemd/user.conf
%_datadir/dbus-1/system.d/org.freedesktop.systemd1.conf

%_rpmlibdir/systemd.filetrigger
/sbin/systemd
/sbin/systemd-ask-password
/bin/systemd-inhibit

/bin/systemd-notify
/sbin/systemd-tty-ask-password-agent

%if_enabled pstore
/etc/systemd/pstore.conf
/lib/systemd/systemd-pstore
%_man5dir/pstore.*
%_man8dir/systemd-pstore.*
%_tmpfilesdir/systemd-pstore.conf
%endif

%_bindir/busctl
%_bindir/systemd-socket-activate
%_bindir/systemd-cat
%_bindir/systemd-cgls
%_bindir/systemd-cgtop
%_bindir/systemd-delta
%_bindir/systemd-detect-virt
%_bindir/systemd-dissect
%_bindir/systemd-id128
%_bindir/systemd-mount
%_bindir/systemd-umount
%_bindir/systemd-path
/bin/systemd-repart
/bin/systemd-run
%_bindir/systemd-stdio-bridge
/lib/systemd/systemd
/lib/systemd/systemd-ac-power
/lib/systemd/systemd-cgroups-agent
%if_enabled libcryptsetup
/lib/systemd/systemd-cryptsetup
/lib/systemd/systemd-veritysetup
%_man5dir/crypttab*
%_mandir/*/*cryptsetup*
%_man8dir/systemd-veritysetup*
%endif
/lib/systemd/systemd-boot-check-no-failures
/lib/systemd/systemd-fsck
/lib/systemd/systemd-growfs
/lib/systemd/systemd-hibernate-resume
/lib/systemd/systemd-initctl
/lib/systemd/systemd-journald
/lib/systemd/systemd-makefs
/lib/systemd/systemd-quotacheck
/lib/systemd/systemd-random-seed
/lib/systemd/systemd-remount-fs
/lib/systemd/systemd-reply-password
/lib/systemd/systemd-rfkill
/lib/systemd/systemd-shutdown
/lib/systemd/systemd-sleep
/lib/systemd/systemd-socket-proxyd
/lib/systemd/systemd-update-done
/lib/systemd/systemd-update-utmp
/lib/systemd/systemd-user-runtime-dir
/lib/systemd/systemd-user-sessions
/lib/systemd/systemd-vconsole-setup
/lib/systemd/systemd-volatile-root
/lib/systemd/systemd-sysv-install
/lib/systemd/systemd-sulogin-shell
/lib/systemd/systemd-xdg-autostart-condition

%dir /lib/environment.d
/lib/environment.d/99-environment.conf
%_mandir/man[58]/*environment*
#%dir /lib/systemd/system.conf.d
#/lib/systemd/system.conf.d/env-path.conf

%dir %_unitdir
%_unitdir/*

%exclude %_unitdir/-.slice.d/10-oomd-root-slice-defaults.conf
%exclude %_unitdir/user@.service.d/10-oomd-user-service-defaults.conf

%if_enabled networkd
%exclude %_unitdir/*networkd*
%exclude %_unitdir/systemd-network-generator.service
%exclude %_unitdir/*resolv*
%exclude %_unitdir/*/*resolv*
%endif
%if_enabled timesyncd
%exclude %_unitdir/*timesyncd*
%exclude %_unitdir/*time-wait-sync*
%endif
%if_enabled microhttpd
%exclude %_unitdir/systemd-journal-gatewayd*
%exclude %_unitdir/systemd-journal-remote*
%endif
%if_enabled libcurl
%exclude %_unitdir/systemd-journal-upload*
%endif
%if_enabled efi
%exclude %_unitdir/systemd-boot-system-token.service
%exclude %_unitdir/*/systemd-boot-system-token.service
%exclude %_unitdir/systemd-bless-boot.service
%endif
%if_enabled coredump
%exclude %_unitdir/systemd-coredump*
%exclude %_unitdir/*/systemd-coredump*
%endif
%if_enabled homed
%exclude %_unitdir/systemd-homed*
%endif

%exclude %_unitdir/*udev*
%exclude %_unitdir/*/*udev*

%exclude %_unitdir/*.machine1.*
%exclude %_unitdir/*.import1.*
%exclude %_unitdir/*.portable1.*
%exclude %_unitdir/systemd-machined.service
%exclude %_unitdir/systemd-importd.service
%exclude %_unitdir/machine.slice
%exclude %_unitdir/machines.target
%exclude %_unitdir/*/machines.target
%exclude %_unitdir/var-lib-machines.mount
%exclude %_unitdir/*/var-lib-machines.mount
%exclude %_unitdir/systemd-nspawn@.service
%exclude %_unitdir/*/systemd-sysusers.service
%exclude %_unitdir/systemd-sysusers.service
%exclude %_unitdir/systemd-portabled.service

%_man1dir/busctl.*
%_mandir/*/systemd-ask-password*
%_man1dir/systemd-cat.*
%_man1dir/systemd-cgls.*
%_man1dir/systemd-cgtop.*
%_man1dir/systemd-delta.*
%_man1dir/systemd-detect-virt.*
%_man1dir/systemd-dissect.*
%_man1dir/systemd-inhibit.*
%_man1dir/systemd-id128.*
%_man1dir/systemd-mount.*
%_man1dir/systemd-umount.*
%_man1dir/systemd-notify.*
%_man1dir/systemd-path.*
%_man1dir/systemd-run.*
%_man1dir/systemd-socket-activate.*
%_mandir/*/systemd-tty-ask-password*
%_man1dir/systemd.*
%_mandir/*/*journald*
%_man5dir/localtime*
%_man5dir/*-release*
%_man5dir/*sleep.conf*
%_man5dir/*system.conf*
%_man5dir/*systemd1*
%_man5dir/*user*
%_man5dir/repart.d.*
%_man5dir/systemd.automount*
%_man5dir/systemd.exec*
%_man5dir/systemd.kill*
%_man5dir/systemd.mount*
%_man5dir/systemd.path*
%_man5dir/systemd.preset*
%_man5dir/systemd.resource-control*
%_man5dir/systemd.scope*
%_man5dir/systemd.service*
%_man5dir/systemd.slice*
%_man5dir/systemd.socket*
%_man5dir/systemd.swap*
%_man5dir/systemd.target*
%_man5dir/systemd.timer*
%_man5dir/systemd.unit*
%_mandir/*/*vconsole*

%_man7dir/*
%exclude %_man7dir/hwdb*
%exclude %_man7dir/udev*
%if_enabled efi
%exclude %_man7dir/systemd-boot*
%exclude %_man7dir/sd-boot*
%endif

%_man8dir/systemd-debug-generator*
%_man8dir/systemd-fsck*
%_man8dir/systemd-fstab-generator*
%_man8dir/systemd-getty-generator*
%_man8dir/systemd-gpt-auto-generator*
%_man8dir/systemd-growfs*
%_man8dir/systemd-sysv-generator*
%_man8dir/systemd-hibernate*
%_man8dir/*sleep*
%_man8dir/systemd-initctl*
%_man8dir/systemd-kexec*
%_man8dir/systemd-makefs*
%_man8dir/systemd-mkswap*
%_man8dir/systemd-quota*
%_man8dir/systemd-random-seed*
%_man8dir/systemd-rc-local-generator*
%_man8dir/rc-local.service*
%_man8dir/systemd-repart*
%_man8dir/systemd-remount*
%_man8dir/systemd-rfkill*
%_man8dir/systemd-run-generator*
%_man8dir/systemd-socket-proxyd*
%_man8dir/systemd-suspend*
%_man8dir/systemd-system-update-generator*
%_man8dir/systemd-update-utmp*
%_man8dir/systemd-user-sessions*
%_man8dir/systemd-update-done*
%_man8dir/systemd-halt*
%_man8dir/systemd-reboot*
%_man8dir/systemd-shutdown*
%_man8dir/systemd-poweroff*
%_man8dir/systemd-volatile-root*
%_man8dir/systemd-xdg-autostart-generator*

%exclude %_mandir/*/*sysusers*
%exclude %_datadir/factory
%exclude %_tmpfilesdir/etc.conf

%_prefix/lib/systemd
/lib/systemd/system-generators
%if_enabled efi
%exclude /lib/systemd/system-generators/systemd-bless-boot-generator
%if_enabled gnuefi
%exclude %_prefix/lib/systemd/boot
%endif
%endif

%dir /lib/systemd/system-preset
/lib/systemd/system-preset/85-display-manager.preset
/lib/systemd/system-preset/90-default.preset
/lib/systemd/system-preset/90-systemd.preset
/lib/systemd/system-preset/99-default-disable.preset

/lib/udev/rules.d/70-uaccess.rules
/lib/udev/rules.d/71-seat.rules
/lib/udev/rules.d/73-seat-late.rules
/lib/udev/rules.d/90-vconsole.rules
/lib/udev/rules.d/99-systemd.rules

%dir %_datadir/systemd
%_datadir/systemd/kbd-model-map
%_datadir/systemd/language-fallback-map
%_datadir/dbus-1/system-services/org.freedesktop.systemd1.service
%_datadir/dbus-1/services/org.freedesktop.systemd1.service

%if_enabled polkit
%_datadir/polkit-1/actions/org.freedesktop.systemd1.policy
%endif

%ghost %dir %attr(2755, root, systemd-journal) %verify(not mode) %_logdir/journal
%ghost %attr(0700,root,root) %dir %_logdir/private
%ghost %attr(0700,root,root) %dir %_localstatedir/cache/private
%ghost %attr(0700,root,root) %dir %_localstatedir/lib/private
%dir %_localstatedir/lib/systemd
%dir %_localstatedir/lib/systemd/catalog
%ghost %dir %_localstatedir/lib/private/systemd
%_rpmlibdir/journal-catalog.filetrigger
%ghost %_localstatedir/lib/systemd/catalog/database
%ghost %_localstatedir/lib/systemd/random-seed
%ghost %dir %_localstatedir/lib/systemd/linger

%_defaultdocdir/%name-%version
%_logdir/README
# may be need adapt for ALTLinux?
/sbin/kernel-install
%_man8dir/kernel-install.*
%dir %_sysconfdir/kernel
%dir %_sysconfdir/kernel/install.d
%dir %_prefix/lib/kernel
%dir %_prefix/lib/kernel/install.d
%_prefix/lib/kernel/install.d/*
%exclude %_prefix/lib/kernel/install.d/50-depmod.install

%files -n libsystemd
/%_lib/libsystemd.so.*

%files -n libsystemd-devel
/%_lib/*.so
%exclude /%_lib/*udev*.so
%_pkgconfigdir/*.pc
%exclude %_pkgconfigdir/*udev*.pc
%_datadir/pkgconfig/systemd.pc
%_includedir/systemd
%_man3dir/*
%exclude %_man3dir/udev*
%exclude %_man3dir/libudev*

%files -n libsystemd-devel-static
/%_lib/libsystemd.a

%files -n libnss-systemd
/%_lib/libnss_systemd.so.*
%_man8dir/*nss?systemd.*

%files -n libnss-myhostname
/%_lib/libnss_myhostname.so.*
%_man8dir/*myhostname.*

%files -n libnss-mymachines
/%_lib/libnss_mymachines.so.*
%_man8dir/*mymachines.*

%files -n libnss-resolve
/%_lib/libnss_resolve.so.*
%_man8dir/*nss*resolve*

%files -n pam_%name
%config %_sysconfdir/pam.d/systemd-user
/%_lib/security/pam_systemd.so
%_man8dir/pam_systemd.*

%if_enabled homed
%files -n pam_%{name}_home
/%_lib/security/pam_systemd_home.so
%_man8dir/pam_systemd_home.*

%files homed
%config(noreplace) %_sysconfdir/systemd/homed.conf
/bin/homectl
/lib/systemd/systemd-homed
/lib/systemd/systemd-homework
%_unitdir/systemd-homed*
%_datadir/dbus-1/system.d/org.freedesktop.home1.conf
%_datadir/dbus-1/system-services/org.freedesktop.home1.service
%if_enabled polkit
%_datadir/polkit-1/actions/org.freedesktop.home1.policy
%endif
%_man1dir/homectl.*
%_man5dir/*home*
%_man8dir/systemd-homed.*
%endif

%files sysvinit
/sbin/init
/sbin/reboot
/sbin/halt
/sbin/poweroff
/sbin/shutdown
/sbin/telinit
/sbin/runlevel
%_man1dir/init*
%_man8dir/halt*
%_man8dir/reboot*
%_man8dir/shutdown*
%_man8dir/poweroff*
%_man8dir/telinit*
%_man8dir/runlevel*
%_initdir/README

%files utils
%dir /lib/systemd
/lib/systemd/libsystemd-shared-%ver_major.so

/lib/modprobe.d/README
/lib/sysctl.d/README
/lib/sysusers.d/README
/lib/tmpfiles.d/README

/sbin/systemctl
/bin/systemctl
%_bindir/systemctl
%_man1dir/systemctl.*

/bin/journalctl
/sbin/journalctl
%_man1dir/journalctl.*

/bin/systemd-escape
%_mandir/*/*escape*

/sbin/systemd-tmpfiles
%_mandir/*/*tmpfiles*
%_rpmlibdir/systemd-tmpfiles.filetrigger
%_tmpfilesdir/legacy.conf
%_tmpfilesdir/x11.conf
%_tmpfilesdir/tmp.conf
%_tmpfilesdir/systemd-tmp.conf
%_tmpfilesdir/var.conf
%_tmpfilesdir/home.conf

/lib/systemd/systemd-binfmt
/sbin/systemd-binfmt
%_rpmlibdir/systemd-binfmt.filetrigger
%_mandir/*/*binfmt*

/lib/systemd/systemd-modules-load
%_sysconfdir/modules-load.d/modules.conf
/sbin/systemd-modules-load
%_rpmlibdir/systemd-modules-load.filetrigger
%_mandir/*/*modules-load*

/lib/systemd/systemd-sysctl
/sbin/systemd-sysctl
%_rpmlibdir/systemd-sysctl.filetrigger
%config(noreplace) %_sysconfdir/sysctl.d/99-sysctl.conf
/lib/sysctl.d/49-coredump-disable.conf
/lib/sysctl.d/50-default.conf
/lib/sysctl.d/50-net.conf
/lib/sysctl.d/50-mmap-min-addr.conf
%if %_lib == lib64
/lib/sysctl.d/50-pid-max.conf
%endif
%_mandir/*/*sysctl*

/lib/systemd/systemd-backlight
%_mandir/*/*backlight*
%ghost %dir %_localstatedir/lib/systemd/backlight

/sbin/systemd-machine-id-setup
%_man8dir/systemd-machine-id-*

/bin/systemd-sysext
%_man8dir/systemd-sysext.*

/usr/bin/systemd-cryptenroll
%_man1dir/systemd-cryptenroll.*
%_man5dir/veritytab.*

%if_enabled firstboot
/sbin/systemd-firstboot
%_man8dir/systemd-firstboot.*
%endif

%ghost %config(noreplace) %_sysconfdir/machine-info
%ghost %config(noreplace) %_sysconfdir/hostname
%ghost %config(noreplace) %_sysconfdir/vconsole.conf
%ghost %config(noreplace) %_sysconfdir/locale.conf

%files services
%dir %_sysconfdir/systemd
%config(noreplace) %_sysconfdir/systemd/logind.conf
%_datadir/dbus-1/system.d/org.freedesktop.*.conf
%exclude %_datadir/dbus-1/system.d/org.freedesktop.systemd1.conf
%exclude %_datadir/dbus-1/system.d/org.freedesktop.resolve1.conf
%exclude %_datadir/dbus-1/system.d/org.freedesktop.network1.conf
%exclude %_datadir/dbus-1/system.d/org.freedesktop.machine1.conf
%exclude %_datadir/dbus-1/system.d/org.freedesktop.import1.conf
%exclude %_datadir/dbus-1/system.d/org.freedesktop.timesync1.conf
%if_enabled homed
%exclude %_datadir/dbus-1/system.d/org.freedesktop.home1.conf
%endif
%_datadir/dbus-1/system-services/org.freedesktop.*.service
%exclude %_datadir/dbus-1/system-services/org.freedesktop.systemd1.service
%exclude %_datadir/dbus-1/system-services/org.freedesktop.resolve1.service
%exclude %_datadir/dbus-1/system-services/org.freedesktop.network1.service
%exclude %_datadir/dbus-1/system-services/org.freedesktop.machine1.service
%exclude %_datadir/dbus-1/system-services/org.freedesktop.import1.service
%exclude %_datadir/dbus-1/system-services/org.freedesktop.portable1.service
%exclude %_datadir/dbus-1/system-services/org.freedesktop.timesync1.service
%if_enabled homed
%exclude %_datadir/dbus-1/system-services/org.freedesktop.home1.service
%endif
%if_enabled polkit
%_datadir/polkit-1/actions/*.policy
%exclude %_datadir/polkit-1/actions/org.freedesktop.systemd1.policy
%exclude %_datadir/polkit-1/actions/org.freedesktop.resolve1.policy
%exclude %_datadir/polkit-1/actions/org.freedesktop.network1.policy
%exclude %_datadir/polkit-1/actions/org.freedesktop.machine1.policy
%exclude %_datadir/polkit-1/actions/org.freedesktop.import1.policy
%exclude %_datadir/polkit-1/actions/org.freedesktop.portable1.policy
%if_enabled homed
%exclude %_datadir/polkit-1/actions/org.freedesktop.home1.policy
%endif
%endif

/bin/loginctl
/lib/systemd/systemd-logind
/bin/userdbctl
/lib/systemd/systemd-userdbd
/lib/systemd/systemd-userwork
%_bindir/hostnamectl
/lib/systemd/systemd-hostnamed
%_bindir/localectl
/lib/systemd/systemd-localed
%_bindir/timedatectl
/lib/systemd/systemd-timedated
%dir /lib/systemd/ntp-units.d
%dir %_sysconfdir/systemd/ntp-units.d
/bin/oomctl
/lib/systemd/systemd-oomd
%config(noreplace) %_sysconfdir/systemd/oomd.conf

%_datadir/bash-completion/completions/*
%exclude %_datadir/bash-completion/completions/udevadm
%_datadir/zsh/site-functions/*
%exclude %_datadir/zsh/site-functions/_udevadm

%_mandir/*/*login*
%_mandir/*/*userdb*
%exclude %_man3dir/*
%_mandir/*/*hostname*
%exclude %_man8dir/*myhostname*
%exclude %_man8dir/*mymachines*
%_mandir/*/*locale*
%_mandir/*/*timedate*
%_man5dir/*LogControl1*
%_mandir/*/*oom*

%if_enabled networkd
%files networkd
/bin/networkctl
%dir %_sysconfdir/systemd/network
%config(noreplace) %_sysconfdir/systemd/networkd.conf
%config(noreplace) %_sysconfdir/systemd/resolved.conf
%_datadir/dbus-1/system.d/org.freedesktop.resolve1.conf
%_datadir/dbus-1/system.d/org.freedesktop.network1.conf
%_datadir/dbus-1/system-services/org.freedesktop.resolve1.service
%_datadir/dbus-1/system-services/org.freedesktop.network1.service
%if_enabled polkit
%_datadir/polkit-1/rules.d/systemd-networkd.rules
%_datadir/polkit-1/actions/org.freedesktop.network1.policy
%_datadir/polkit-1/actions/org.freedesktop.resolve1.policy
%endif
/lib/systemd/systemd-network-generator
/lib/systemd/system-preset/85-networkd.preset
/lib/systemd/systemd-networkd
/lib/systemd/systemd-networkd-wait-online
/lib/systemd/systemd-resolved
/lib/systemd/resolv.conf
/lib/modprobe.d/systemd.conf
%_bindir/resolvectl
%_bindir/systemd-resolve
# TODO: Provides: /sbin/resolvconf ?
%exclude /sbin/resolvconf
%_tmpfilesdir/systemd-network.conf
%_unitdir/*networkd*
%_unitdir/systemd-network-generator.service
%_unitdir/*resolv*
%_unitdir/*/*resolv*
/lib/systemd/network/80-container-host0.network
/lib/systemd/network/80-wifi-adhoc.network
/lib/systemd/network/80-wifi-ap.network.example
/lib/systemd/network/80-wifi-station.network.example
%_mandir/*/*networkd*
%_mandir/*/systemd-network-generator*
%_mandir/*/*netdev*
%_mandir/*/*resolved*
%_mandir/*/*resolve1*
%_mandir/*/*dnssd*
%_man1dir/networkctl.*
%_man1dir/resolvectl.*
%_man1dir/resolvconf.*
%_man5dir/dnssec-trust-anchors.d.*
%_man5dir/systemd.negative.*
%_man5dir/systemd.positive.*
%_man5dir/systemd.network.*
%endif

%files oomd-defaults
/lib/systemd/oomd.conf.d/10-oomd-defaults.conf
%_unitdir/-.slice.d/10-oomd-root-slice-defaults.conf
%_unitdir/user@.service.d/10-oomd-user-service-defaults.conf

%files container
%_datadir/dbus-1/system.d/org.freedesktop.machine1.conf
%_datadir/dbus-1/system.d/org.freedesktop.import1.conf
/bin/machinectl
%_bindir/systemd-nspawn
/lib/systemd/import-pubring.gpg
%_tmpfilesdir/systemd-nspawn.conf
%_unitdir/*.machine1.*
%_unitdir/*.import1.*
%_unitdir/systemd-machined.service
%_unitdir/systemd-importd.service
%_unitdir/machine.slice
%_unitdir/machines.target
%_unitdir/*/machines.target
%_unitdir/var-lib-machines.mount
%_unitdir/*/var-lib-machines.mount
%_unitdir/systemd-nspawn@.service
/lib/systemd/systemd-machined
/lib/systemd/systemd-export
/lib/systemd/systemd-import
/lib/systemd/systemd-import-fs
/lib/systemd/systemd-importd
/lib/systemd/systemd-pull
/lib/systemd/network/80-container-ve.network
/lib/systemd/network/80-container-vz.network
/lib/systemd/network/80-vm-vt.network
%_datadir/dbus-1/system-services/org.freedesktop.machine1.service
%_datadir/dbus-1/system-services/org.freedesktop.import1.service
%if_enabled polkit
%_datadir/polkit-1/actions/org.freedesktop.import1.policy
%_datadir/polkit-1/actions/org.freedesktop.machine1.policy
%endif
%_mandir/*/*nspawn*
%_mandir/*/*machine*
%_mandir/*/*import*
%exclude %_man3dir/*machine*
%exclude %_man8dir/*mymachines.*
%exclude %_man8dir/systemd-machine-id-*

%files portable
%_tmpfilesdir/portables.conf
%_unitdir/systemd-portabled.service
%_unitdir/*.portable1.*
%dir /lib/systemd/portable
%dir /lib/systemd/portable/profile
/lib/systemd/portable/profile/*
/bin/portablectl
/lib/systemd/systemd-portabled
%_datadir/dbus-1/system-services/org.freedesktop.portable1.service
%if_enabled polkit
%_datadir/polkit-1/actions/org.freedesktop.portable1.policy
%endif
%_mandir/*/*portable*

%if_enabled timesyncd
%files timesyncd
%config(noreplace) %_sysconfdir/systemd/timesyncd.conf
/lib/systemd/system-preset/85-timesyncd.preset
/lib/systemd/systemd-timesyncd
/lib/systemd/systemd-time-wait-sync
/lib/systemd/ntp-units.d/80-systemd-timesync.list
%_datadir/dbus-1/system.d/org.freedesktop.timesync1.conf
%_datadir/dbus-1/system-services/org.freedesktop.timesync1.service
%_unitdir/systemd-timesyncd.service
%_unitdir/systemd-time-wait-sync.service
%_mandir/*/*timesyncd*
%_mandir/*/*time-wait-sync*
%ghost %dir %_localstatedir/lib/systemd/timesync
%ghost %_localstatedir/lib/systemd/timesync/clock
%endif

%files analyze
%_bindir/systemd-analyze
%_man1dir/systemd-analyze.*

%if_enabled microhttpd
%files journal-remote
%dir %attr(2755,systemd-journal-remote,systemd-journal-remote) %_logdir/journal/remote
%config(noreplace) %_sysconfdir/systemd/journal-remote.conf
/lib/systemd/systemd-journal-gatewayd
/lib/systemd/systemd-journal-remote
%_unitdir/systemd-journal-gatewayd.*
%_unitdir/systemd-journal-remote*
%_datadir/systemd/gatewayd
%_man8dir/systemd-journal-gatewayd.*
%_man8dir/systemd-journal-remote.*
%_man5dir/journal-remote.conf.*
%_man5dir/journal-upload.conf.*

%if_enabled sysusers
/lib/sysusers.d/systemd-remote.conf
%endif

%if_enabled libcurl
%config(noreplace) %_sysconfdir/systemd/journal-upload.conf
%ghost %dir %_localstatedir/lib/systemd/journal-upload
%ghost %dir %_localstatedir/lib/private/systemd/journal-upload
/lib/systemd/systemd-journal-upload
%_unitdir/systemd-journal-upload.service
%_man8dir/systemd-journal-upload*
%endif
%endif

%if_enabled efi
%files boot-efi
%_bindir/bootctl
/lib/systemd/systemd-bless-boot
/lib/systemd/system-generators/systemd-bless-boot-generator
%_unitdir/systemd-boot-system-token.service
%_unitdir/sysinit.target.wants/systemd-boot-system-token.service
%_unitdir/systemd-bless-boot.service
%_man1dir/bootctl.*
%_man5dir/loader*
%_man7dir/systemd-boot*
%_man7dir/sd-boot*
%_man8dir/systemd-bless*
%_man8dir/systemd-boot*
%if_enabled gnuefi
%dir %_prefix/lib/systemd/boot
%dir %_prefix/lib/systemd/boot/efi
%_prefix/lib/systemd/boot/efi/*
%endif
%endif

%if_enabled coredump
%files coredump
%config(noreplace) %_sysconfdir/systemd/coredump.conf
/lib/systemd/systemd-coredump
%_bindir/*coredumpctl
/lib/sysctl.d/50-coredump.conf
%_unitdir/systemd-coredump*
%_unitdir/*/systemd-coredump*
%_man1dir/*coredumpctl.*
%_man5dir/coredump.conf.*
%_man8dir/systemd-coredump*
%dir %_localstatedir/lib/systemd/coredump
%endif

%if_enabled sysusers
%files stateless
/sbin/systemd-sysusers
%dir /lib/sysusers.d
%dir %_datadir/factory
%_datadir/factory/*
%_unitdir/systemd-sysusers.service
%_unitdir/sysinit.target.wants/systemd-sysusers.service
%_rpmlibdir/systemd-sysusers.filetrigger
/lib/sysusers.d/systemd.conf
/lib/sysusers.d/basic.conf
%_tmpfilesdir/etc.conf
%_mandir/*/*sysusers*

%if_enabled ldconfig
%_unitdir/ldconfig.service
%_unitdir/sysinit.target.wants/ldconfig.service
%endif #ldconfig
%endif #sysuser

%if_enabled standalone_binaries
%if_enabled sysusers
%files sysusers-standalone
/sbin/systemd-sysusers.standalone
%endif #sysuser

%files modules-load-standalone
/sbin/systemd-modules-load.standalone

%files sysctl-standalone
/sbin/systemd-sysctl.standalone

%files tmpfiles-standalone
/sbin/systemd-tmpfiles.standalone
%endif

%files -n libudev1
/%_lib/libudev.so.*

%files -n libudev-devel
%_includedir/libudev.h
/%_lib/libudev.so
%_pkgconfigdir/libudev.pc
%_datadir/pkgconfig/udev.pc
%_man3dir/udev*
%_man3dir/libudev*

%files -n libudev-devel-static
/%_lib/libudev.a

%files -n udev
%dir %_sysconfdir/udev
%dir %_sysconfdir/udev/rules.d
%dir %_sysconfdir/udev/hwdb.d
%config(noreplace) %_sysconfdir/udev/*.conf
%ghost %_sysconfdir/udev/hwdb.bin
%config(noreplace) %_sysconfdir/udev/rules.d/*
%config(noreplace) %_sysconfdir/scsi_id.config
%_initdir/udev*
%_unitdir/*udev*
%_unitdir/*/*udev*
%dir /lib/systemd/network
/lib/systemd/network/*.link
%_tmpfilesdir/static-nodes-permissions.conf
/lib/udev
/sbin/udevadm
/sbin/udevd
/sbin/systemd-hwdb
/lib/systemd/systemd-udevd
%_rpmlibdir/udev.filetrigger
%_rpmlibdir/udev-hwdb.filetrigger
%_mandir/*/*udev*
%_mandir/*/*hwdb*
%_mandir/*/*.link*
%_man5dir/systemd.device*
%exclude %_man3dir/*
%_datadir/bash-completion/completions/udevadm
%_datadir/zsh/site-functions/_udevadm

# systemd
%exclude /lib/udev/rules.d/70-uaccess.rules
%exclude /lib/udev/rules.d/71-seat.rules
%exclude /lib/udev/rules.d/73-seat-late.rules
%exclude /lib/udev/rules.d/90-vconsole.rules
%exclude /lib/udev/rules.d/99-systemd.rules

%changelog
* Fri Jul 09 2021 Alexey Shabalin <shaba@altlinux.org> 1:249-alt1
- 249
- Add rpm filetrigger for systemd-modules-load.
- Drop altlinux-clock-setup.service.
- Add condition for build with bpf-framework (disabled).
- Define SBAT options for ALT Linux.
- Define system user GID as in setup package.
- Add migrate /etc/sysconfig/ i18n, keyboard, consolefont, network files/variables to %%post.
- Enable default LLMNR mode for systemd-resolver.
- Disable build standalone utils.

* Wed Jul 07 2021 Dmitry V. Levin <ldv@altlinux.org> 1:248.3-alt3
- NMU.
- Reverted all changes introduced in the previous release due to regressions
  (closes: #40392).
- Update from the previous release has not been tested due to urgency,
  all users of 248.3-alt2 are advised to wait for the next release.

* Sat Jun 26 2021 Alexey Shabalin <shaba@altlinux.org> 1:248.3-alt2
- Add rpm filetrigger for systemd-modules-load.
- Add rpm filetriggers for standalone utils.
- Switch to systemd-tmpfiles.standalone in udevd.init SysV script.
- udev do not requires systemd-utils.
- Drop altlinux-clock-setup.service.
- Add Conflicts with startup.
- Merge services files to main systemd package.
- Merge utils files to main systemd package.
- Add migrate /etc/sysconfig/ i18n, keyboard, consolefont, network files/variables to %%post.

* Thu May 27 2021 Alexey Shabalin <shaba@altlinux.org> 1:248.3-alt1
- 248.3
- Create systemd-oomd-defaults subpackage to install unit drop-ins that will
  configure systemd-oomd to monitor and act.
- Build systemd-resolved with:
  + DNSSEC disabled by default
  + mDNS disabled by default
  + LLMNR support in resolve-only mode by default.
- Merge udev-rules and udev-hwdb to udev package.

* Fri May 07 2021 Alexey Shabalin <shaba@altlinux.org> 1:248.2-alt1
- 248.2

* Wed Feb 10 2021 Alexey Shabalin <shaba@altlinux.org> 1:247.3-alt2
- Add efi_pstore kernel module requires to systemd-pstore.service

* Wed Feb 03 2021 Alexey Shabalin <shaba@altlinux.org> 1:247.3-alt1
- 247.3
- Enable systemd-pstore.service by default.

* Wed Dec 16 2020 Alexey Shabalin <shaba@altlinux.org> 1:247.2-alt1
- 247.2
- Move 80-container-host0.network to networkd subpackage.
- Add separate packages for standalone binaries:
  + systemd-modules-load
  + systemd-sysctl
  + systemd-sysusers
  + systemd-tmpfiles

* Tue Dec 08 2020 Alexey Shabalin <shaba@altlinux.org> 1:247.1-alt1
- 247.1

* Tue Dec 08 2020 Stanislav Levin <slev@altlinux.org> 1:247-alt2
- Backported fix for systemd GH#17768.

* Fri Nov 27 2020 Alexey Shabalin <shaba@altlinux.org> 1:247-alt1
- 247

* Sun Nov 08 2020 Alexey Shabalin <shaba@altlinux.org> 1:246.6-alt5
- add cloud@altlinux.org key to import-pubring.gpg

* Mon Oct 19 2020 Alexey Shabalin <shaba@altlinux.org> 1:246.6-alt4
- revert kernelinstalldir path /usr/lib/kernel/install.d -> /lib/kernel/install.d
- build systemd-boot for arm

* Fri Oct 16 2020 Alexey Shabalin <shaba@altlinux.org> 1:246.6-alt3
- dhcp-server: offer router address as next-server (sbolshakov@)

* Sat Oct 03 2020 Alexey Shabalin <shaba@altlinux.org> 1:246.6-alt2
- kernelinstalldir path /usr/lib/kernel/install.d -> /lib/kernel/install.d
- install kernel-install script to /sbin
- move systemd-boot and bootctl utils to systemd-boot-efi package

* Mon Sep 21 2020 Alexey Shabalin <shaba@altlinux.org> 1:246.6-alt1
- 246.6

* Wed Sep 16 2020 Alexey Shabalin <shaba@altlinux.org> 1:246.5-alt1
- 246.5

* Tue Sep 08 2020 Alexey Shabalin <shaba@altlinux.org> 1:246.4-alt1
- 246.4

* Mon Aug 10 2020 Alexey Shabalin <shaba@altlinux.org> 1:246.1-alt1
- 246.1

* Mon Aug 03 2020 Alexey Shabalin <shaba@altlinux.org> 1:246-alt1
- 246

* Mon Jul 27 2020 Alexey Shabalin <shaba@altlinux.org> 1:245.7-alt1
- 245.7

* Tue Jul 07 2020 Nikita Ermakov <arei@altlinux.org> 1:245.6-alt2
- disable kexec-tools for riscv64

* Thu Jun 04 2020 Alexey Shabalin <shaba@altlinux.org> 1:245.6-alt1
- 245.6

* Thu Apr 30 2020 Alexey Shabalin <shaba@altlinux.org> 1:245.5-alt1
- 245.5

* Fri Apr 10 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1:245.4-alt2
- add resolve files, located at /run, to the list of tracked by altlinux-libresolv files

* Wed Apr 08 2020 Alexey Shabalin <shaba@altlinux.org> 1:245.4-alt1
- 245.4

* Mon Mar 30 2020 Alexey Shabalin <shaba@altlinux.org> 1:245.3-alt1
- 245.3 (v245-stable branch)
- drop altlinux-kmsg-loglevel.service and altlinux-save-dmesg.service

* Tue Mar 24 2020 Alexey Shabalin <shaba@altlinux.org> 1:245.2-alt1
- 245.2 (v245-stable branch)

* Fri Mar 13 2020 Alexey Shabalin <shaba@altlinux.org> 1:245-alt3
- disable p11kit support (before enable, need move libp11-kit and libffi to /lib)

* Wed Mar 11 2020 Alexey Shabalin <shaba@altlinux.org> 1:245-alt2
- v245-stable branch (084df9c616fdfbcbf3d7fbe7dc6b975f1fa359d2)

* Fri Mar 06 2020 Alexey Shabalin <shaba@altlinux.org> 1:245-alt1
- 245
- move org.freedesktop.timesync1.service from systemd-service to systemd-timesyncd
- move resolve1 and network1 polkit policy from systemd-services to systemd-networkd
- build with -Dlink-networkd-shared=false and -Dlink-timesyncd-shared=false
- fixed package network.target and network-online.target
- package userdb to systemd-services
- build systemd-homed

* Mon Feb 17 2020 Alexey Shabalin <shaba@altlinux.org> 1:244.3-alt2
- move systemd-network-generator.service to systemd-networkd package
- avoid requires quota package

* Sun Feb 16 2020 Alexey Shabalin <shaba@altlinux.org> 1:244.3-alt1
- 244.3 (Fixes: CVE-2020-1712)

* Thu Dec 19 2019 Alexey Shabalin <shaba@altlinux.org> 1:244.1-alt1
- 244.1 (v244-stable branch)

* Wed Dec 04 2019 Alexey Shabalin <shaba@altlinux.org> 1:244-alt1
- 244
- switch default-hierarchy to unified (cgroup-v2)
- drop udev-extras package

* Fri Nov 22 2019 Alexey Shabalin <shaba@altlinux.org> 1:243.4-alt1
- 243.4 from stable branch

* Tue Nov 05 2019 Alexey Shabalin <shaba@altlinux.org> 1:243-alt4
- move completions to systemd-services (ALT #37352)
- group add vmusers in pre for udev package (ALT #37200)

* Mon Oct 14 2019 Alexey Shabalin <shaba@altlinux.org> 1:243-alt3
- merge with v243-stable ef677436aa203c24816021dd698b57f219f0ff64
- add symlink /usr/bin/systemctl -> /bin/systemctl for compat with other distros
- merge bash and zsh completion packages to utils and udev

* Sun Sep 29 2019 Alexey Shabalin <shaba@altlinux.org> 1:243-alt2
- merge with v243-stable fab6f010ac6c3bc93a10868de722d7c8c3622eb9

* Tue Sep 03 2019 Alexey Shabalin <shaba@altlinux.org> 1:243-alt1
- 243

* Fri Aug 09 2019 Alexey Shabalin <shaba@altlinux.org> 1:242-alt11
- merge with v242-stable 07f0549ffe3413f0e78b656dd34d64681cbd8f00

* Thu Jul 18 2019 Dmitry Terekhin <jqt4@altlinux.org> 1:242-alt10.0.mips1
- build w/o lto on mipsel

* Wed Jul 17 2019 Alexey Shabalin <shaba@altlinux.org> 1:242-alt10
- merge with v242-stable 572385e13566f9ca442ee3b46742159b905b4712:
  + networkd: fix link_up()
  + conf-parser: fix continuation handling
- random-util: eat up bad RDRAND values seen on AMD CPUs

* Tue Jul 16 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:242-alt9
- udev: sysvinit-script:
  + do not use /dev mount options for /run;
  + add default for $tmpfs_options variable.

* Wed May 22 2019 Alexey Shabalin <shaba@altlinux.org> 1:242-alt8
- silent execute egrep in rpm filetrigger

* Tue May 21 2019 Alexey Shabalin <shaba@altlinux.org> 1:242-alt7
- add systemd-sysusers.filetrigger
- update rpm filetriggers
- add condition for run update resolv.conf

* Wed May 15 2019 Alexey Shabalin <shaba@altlinux.org> 1:242-alt6
- merge with v242-stable 298d13df7ef1097fa4801de573f668cef23a22b3
- units: add usb-gadget.target (sbolshakov@)
- dhcp-server: offer router address as next-server (sbolshakov@)

* Sat May 04 2019 Alexey Shabalin <shaba@altlinux.org> 1:242-alt5
- merge with v242-stable db2e367bfc3b119609f837eb973d915f6c550b2f

* Wed Apr 24 2019 Alexey Shabalin <shaba@altlinux.org> 1:242-alt4
- update rpm systemd.filetrigger

* Sat Apr 20 2019 Alexey Shabalin <shaba@altlinux.org> 1:242-alt3
- fix path in systemd.pc (ALT #36634)

* Fri Apr 19 2019 Alexey Shabalin <shaba@altlinux.org> 1:242-alt2
- update patch timezone detection(mrdrew@)

* Sat Apr 13 2019 Alexey Shabalin <shaba@altlinux.org> 1:242-alt1
- 242 (Fixes: CVE-2019-3842)
- move execute systemctl daemon-reexec from post-script to filetrigger
- add requires systemd to libnss-systemd package (ALT #36267)
- move LOCKFILE to /run/lock in udev init script (ALT #35888)

* Tue Apr 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:241-alt5
- this change includes the following (closes: #32346):
  + possibility to get the time zone from /etc/sysconfig/clock
  + set-timezone call adds the time zone to /etc/sysconfig/clock as well
  + user notification shown when two sources have different time zones
  + rollback of the change that had the file copied in case of separate /usr;
  now a symlink is created when calling set-timezone.

* Mon Apr 01 2019 Alexey Shabalin <shaba@altlinux.org> 1:241-alt4
- merge with v241-stable branch
- fixed error 'too many arguments' in rpm filetrigger (ALT #36461)

* Tue Feb 19 2019 Alexey Shabalin <shaba@altlinux.org> 1:241-alt3
- backport patches from master:
  + backlight: handle loading truncated file
  + udev-rules: update log messages about OWNER= or GROUP= settings on --resolve=names=never
    This also set lower log level for the messages. (fixes ALT#36135)
  + udev-rule, ethtool: several coding style cleanups

* Tue Feb 19 2019 Alexey Shabalin <shaba@altlinux.org> 1:241-alt2
- Fixes for the following security vulnerabilities:
  + CVE-2019-6454: systemd (PID1) crash with specially crafted D-Bus message

* Fri Feb 15 2019 Alexey Shabalin <shaba@altlinux.org> 1:241-alt1
- 241
- allow execute logind without systemd

* Fri Jan 11 2019 Alexey Shabalin <shaba@altlinux.org> 1:240-alt4
- merge with v240-stable branch
- udevadm: refuse to run trigger, control, settle and monitor commands in chroot
- sd-device: do not try SO_RCVBUF when setting receive buffer size
- sd-device: enable SO_PASSCRED again after fork()
- add build options -Dbump-proc-sys-fs-file-max=false and -Dbump-proc-sys-fs-nr-open=false
- build libsystemd as static and add libsystemd-devel-static package
- build libudev as static and add libudev-devel-static package

* Tue Jan 08 2019 Mikhail Efremov <sem@altlinux.org> 1:240-alt3
- journald: set a limit on the number of fields once more.
- Backported patches from upstream (fixes: CVE-2018-16864, CVE-2018-16865).

* Fri Jan 04 2019 Alexey Shabalin <shaba@altlinux.org> 1:240-alt2
- backport patches from upstream master (fixes ALT#35843, ALT#35840)

* Mon Dec 31 2018 Alexey Shabalin <shaba@altlinux.org> 1:240-alt1
- 240
- install systemd-run to /bin (for allow execute from udev rules for lvm2)
- install upstream completions for bash4

* Mon Oct 29 2018 Alexey Shabalin <shaba@altlinux.org> 1:239-alt3
- merge with v239-stable
- Fixes for the following security vulnerabilities:
  + CVE-2018-15688 dhcp6: make sure we have enough space for the DHCP6 option header
  + CVE-2018-15687 chown-recursive: rework the recursive logic to use O_PATH

* Mon Sep 17 2018 Alexey Shabalin <shaba@altlinux.org> 1:239-alt2
- merge with v239-stable
- build with libmicrohttpd-0.9.59

* Fri Jun 22 2018 Alexey Shabalin <shaba@altlinux.ru> 1:239-alt1
- 239
- backport some patches from master
- add portable package
- mount /run/user/500 with noexec
- static link systemd-udev and systemctl with libsystemd-shared
- build with gnu-efi suuport (systemd boot loader)
- Revert "Make hostnamed/localed/logind/machined/timedated D-Bus activatable"
- Revert "Start logind on demand via libpam-systemd"

* Wed May 16 2018 Alexey Shabalin <shaba@altlinux.ru> 1:238-alt8
- merge with v238-stable branch
- add "noexec" for /run/lock mount option

* Fri Apr 13 2018 Alexey Shabalin <shaba@altlinux.ru> 1:238-alt7
- merge with v238-stable branch

* Fri Apr 06 2018 Alexey Shabalin <shaba@altlinux.ru> 1:238-alt6
- move to systemd-utils package:
  + systemctl
  + journalctl
  + libsystemd-shared
- drop packages:
  + journalctl
  + libsystemd-shared
  + bash-completion-journalctl
  + zsh-completion-journalctl
- clenup Conflicts

* Tue Apr 03 2018 Alexey Shabalin <shaba@altlinux.ru> 1:238-alt5
- drop Conflicts in udev-rules (fixed update from p8)

* Fri Mar 30 2018 Alexey Shabalin <shaba@altlinux.ru> 1:238-alt4
- order all /*/sbin before /*/bin (thx imz@)
- add drop-in config with defined PATH for user
- split udev-rule-generator to separate package
- set default-kill-user-processes=true

* Thu Mar 29 2018 Alexey Shabalin <shaba@altlinux.ru> 1:238-alt3
- update Requires for allow update udev after systemd

* Sat Mar 24 2018 Alexey Shabalin <shaba@altlinux.ru> 1:238-alt2
- merge with v238-stable branch
- add group render

* Mon Mar 12 2018 Alexey Shabalin <shaba@altlinux.ru> 1:238-alt1
- 238
- fix build systemd.directive man
- move "journalctl --update-catalog" from %%post to filetrigger
- move "udevadm hwdb" from %%post to filetrigger
- add filetriggers for systemd-sysctl,systemd-binfmt

* Wed Feb 14 2018 Ivan Zakharyaschev <imz@altlinux.org> 1:237-alt3
- libsystemd doesn't obsolete the old split libs anymore (with
  different filenames), so that legacy binaries linked with them are
  not "obsoleted", too, whereas some new binaries can be installed.
  (That's in the spirit of shared libs policy.)
  (Note that the compat libraries are not packaged in any package now.)

* Tue Feb 13 2018 Alexey Shabalin <shaba@altlinux.ru> 1:237-alt2
- merge with v237-stable branch
- include additional directories in ProtectSystem
- let graphical-session-pre.target be manually started
- fix order in PATH (ALT #34527)
- add conflicts to ConsoleKit2 for logind

* Mon Jan 29 2018 Alexey Shabalin <shaba@altlinux.ru> 1:237-alt1
- 237
- build with libidn2

* Tue Jan 23 2018 Alexey Shabalin <shaba@altlinux.ru> 1:236-alt1
- 236

* Tue Nov 14 2017 Alexey Shabalin <shaba@altlinux.ru> 1:235-alt3
- fixed udevadm path in units

* Tue Nov 14 2017 Alexey Shabalin <shaba@altlinux.ru> 1:235-alt2
- fixed udevadm path in rules
- fixed man pages

* Wed Nov 08 2017 Alexey Shabalin <shaba@altlinux.ru> 1:235-alt1
- 235
- use default upstream path /bin (not /sbin) for binary
- enable sysusers and build stateless package

* Thu Oct 19 2017 Ivan Zakharyaschev <imz@altlinux.org> 1:234-alt4
- udevd.init (SysV): fix creating static device inodes (ALT: #34031).
  (Use an option introduced in v209 for "unsafe" tmpfiles actions,
  because the static devices are listed as such by kmod.)
- This also helps the unmounting of NFS when halting after having
  upgraded/reinstalled udev (& other) on a system with SysV init
  (ALT: #34019) by a lucky coincidence.

* Fri Aug 11 2017 Paul Wolneykien <manowar@altlinux.org> 1:234-alt3
- Fix: Make --root option really work (closes: 33749).

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 1:234-alt2
- merge with v234-stable branch
- avoid plymouth requires

* Thu Jul 13 2017 Alexey Shabalin <shaba@altlinux.ru> 1:234-alt1
- 234

* Thu Apr 27 2017 Anton Farygin <rider@altlinux.ru> 1:233-alt2
- added /lib/systemd/systemd-machined provides to systemd-container

* Thu Mar 02 2017 Alexey Shabalin <shaba@altlinux.ru> 1:233-alt1
- 233

* Mon Feb 13 2017 Alexey Shabalin <shaba@altlinux.ru> 1:232-alt3.git.486b3d0
- update conflicts

* Thu Feb 02 2017 Alexey Shabalin <shaba@altlinux.ru> 1:232-alt2.git.486b3d0
- upstream snapshot of master 486b3d08dbf6c6b0b20e2960990f864d5d95fd37

* Sun Nov 06 2016 Alexey Shabalin <shaba@altlinux.ru> 1:232-alt1
- 232
- split container support to systemd-container
- add libnss-systemd package

* Fri Sep 30 2016 Alexey Shabalin <shaba@altlinux.ru> 1:231-alt3
- build with libidn support
- backport upstream patches for networkd
- fix for the empty notify message
- build with option --without-kill-user-processes

* Fri Aug 05 2016 Alexey Shabalin <shaba@altlinux.ru> 1:231-alt2
- build without libidn support (ALT #32362)

* Wed Jul 27 2016 Alexey Shabalin <shaba@altlinux.ru> 1:231-alt1
- 231

* Mon May 23 2016 Alexey Shabalin <shaba@altlinux.ru> 1:230-alt1
- 230
- Drop libsystemd-{id128,daemon,login,journal}.so compat libs
- Remove systemd-bootchart

* Wed May 18 2016 Mikhail Efremov <sem@altlinux.org> 1:229-alt6
- Patch from upstream:
    + strbuf: set the proper character when creating new nodes
      (closes: #32060).

* Thu Apr 28 2016 Eugene Prokopiev <enp@altlinux.ru> 1:229-alt5
- fix alt-specific simpleresolv units

* Wed Apr 27 2016 Alexey Shabalin <shaba@altlinux.ru> 1:229-alt4
- fixed insecure core_pattern (ALT #32029)
- add enable kdm4 to preset (ALT #32027)

* Fri Apr 15 2016 Alexey Shabalin <shaba@altlinux.ru> 1:229-alt3
- Don't enable audit by default.
- drop support /lib/udev/devices.
- systemd-networkd-wait online times out with ipv6 disabled
- backport many patches from upstream master (see git log)

* Tue Apr 12 2016 Eugene Prokopiev <enp@altlinux.ru> 1:229-alt2
- add alt-specific simpleresolv units (closes: #31276)

* Fri Feb 19 2016 Alexey Shabalin <shaba@altlinux.ru> 1:229-alt1
- 229
- enable seccomp support
- useradd systemd-coredump to systemd-coredump package
- add alias tmpfiles.service for systemd-tmpfiles-setup.service
- return udevd-final service for copy generated rules to /etc/udev/rules.d/

* Tue Dec 08 2015 Alexey Shabalin <shaba@altlinux.ru> 1:228-alt2
- package dir /etc/systemd/network to systemd-networkd

* Wed Nov 18 2015 Alexey Shabalin <shaba@altlinux.ru> 1:228-alt1
- 228
- update altlinux-libresolv and altlinux-openresolv units
- disable use compiled-in list of DNS and NTP Google servers

* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 1:227-alt1
- 227

* Tue Sep 08 2015 Alexey Shabalin <shaba@altlinux.ru> 1:226-alt1
- 226

* Wed Sep 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1:225-alt2
- enable nss-mymachines in /etc/nsswitch.conf
- always install libnss-myhostname and libnss-mymachines

* Fri Aug 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1:225-alt1
- 225

* Mon Aug 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1:224-alt1
- 224
- drop python subpackages

* Thu Jul 23 2015 Alexey Shabalin <shaba@altlinux.ru> 1:222-alt2
- tmpfiles: downgrade errors when a file system does not support file attributes

* Wed Jul 15 2015 Alexey Shabalin <shaba@altlinux.ru> 1:222-alt1
- 222
- several patches from master

* Tue Jun 30 2015 Alexey Shabalin <shaba@altlinux.ru> 1:221-alt4
- backport patches from upstream master
- add systemd-firstboot to utils package
- autostart machines.target for multi-user.target

* Thu Jun 25 2015 Alexey Shabalin <shaba@altlinux.ru> 1:221-alt3
- backport patches from upstream master
- add --no-redirect for chkconfig in systemd-sysv-install

* Wed Jun 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1:221-alt2
- add add_findreq_skiplist %_x11sysconfdir/xinit.d/*

* Mon Jun 22 2015 Alexey Shabalin <shaba@altlinux.ru> 1:221-alt1
- 221

* Fri May 22 2015 Alexey Shabalin <shaba@altlinux.ru> 1:220-alt1
- 220
- add patches from master
- build with gcrypt support

* Wed Mar 04 2015 Alexey Shabalin <shaba@altlinux.ru> 1:219-alt2
- v219-stable snapshot 0436d5c5f4b39ba8177437fa92f082f8ef1830fb

* Tue Feb 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1:219-alt1
- 219
- drop systemd-devel package

* Wed Nov 19 2014 Alexey Shabalin <shaba@altlinux.ru> 1:217-alt3
- sync with v217-stable branch

* Wed Nov 12 2014 Alexey Shabalin <shaba@altlinux.ru> 1:217-alt2
- udev hwdb: Change error message regarding missing hwdb.bin back to debug.

* Wed Oct 29 2014 Alexey Shabalin <shaba@altlinux.ru> 1:217-alt1
- 217

* Tue Sep 23 2014 Alexey Shabalin <shaba@altlinux.ru> 1:216-alt4
- backport fixes for timesyncd from upstream master
- backport many fixes for mem leak from upstream master

* Mon Sep 15 2014 Alexey Shabalin <shaba@altlinux.ru> 1:216-alt3
- move systemd-machine-id-setup to systemd-utils
- move configs /etc/{machine-info,hostname,vconsole.conf,locale.conf} to systemd-utils
- move all units files frorm systemd-utils,systemd-services to systemd

* Mon Sep 15 2014 Alexey Shabalin <shaba@altlinux.ru> 1:216-alt2
- move systemd-{halt,poweroff,reboot,shutdown} man pages to systemd package

* Fri Sep 05 2014 Alexey Shabalin <shaba@altlinux.ru> 1:216-alt1
- 216
- drop use /proc/sys/kernel/hotplug in init script (ALT#30275)
- split zsh completions for systemd, journalctl, udev (ALT#29698)
- update altlinux-openresolv units
- run first_time before display-manager (ALT#29200)
- add systemd-logind shell wrapper
- revert allow copy to /etc/localtime (Debian patch)
- make hostnamed/localed/logind/machined/timedated D-Bus activatable (Debian patch)
- split systemd-network support from main tmpfiles.d/systemd.conf
- move hostnamed/localed/logind/machined/timedated and *ctl utils to systemd-service package
- split pam_systemd to separate package
- add libnss-mymachines, libnss-resolve packages

* Fri Aug 15 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt14
- add altlinux-openresolv unit to networkd package

* Fri Aug 15 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt13
- fixed networkd and timesyncd preset

* Thu Aug 14 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt12
- split networkd and timesyncd into a separate packages

* Tue Aug 05 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt11
- set default polling interval on removable devices as well
- sysv: order initscripts which provide $network before network.target
- sysv-generator: do not generate 'Wants' symlinks to generated service files that will be shadowed by a native unit
- altlinux-update_chrooted.service -> altlinux-libresolv.path

* Tue Jul 08 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt10
- backport patches for generator from upstream master
- fix preun journal-gateway
- drop detect and set default.target
- update presets services
- skip log_parse_environment for initrd

* Wed Jul 02 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt9
- add alias for halt and reboot services
- don't do automatic cleanup in $XDG_RUNTIME_DIR

* Tue Jul 01 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt8
- drop prefdm.service
- add preset for display managers

* Mon Jun 30 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt7
- update ALTLinux units

* Mon Jun 30 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt6
- units: networkd - don't order wait-online.service before network.target
- libudev: queue - watch entire directory to allow the re-use of the watch descriptor

* Sat Jun 28 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt5
- backport fixes from upstream master branch

* Fri Jun 27 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt3
- revert "add systemd-vconsole-setup@.service for another way localize ttyX"
- revert "start systemd-ask-password-wall.service after getty@tty1.service"
- revert "increase RestartSec to 5 sec for getty services"

* Fri Jun 27 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt2
- snapshot v214-stable branch
- fixed sysv generator
- don't create symlinks /var/run, /var/lock (ALT#30138)

* Mon Jun 23 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt1
- switch to v214-stable branch

* Thu May 08 2014 Alexey Shabalin <shaba@altlinux.ru> 1:210-alt8
- increase RestartSec to 5 sec for getty services (ALT#30061)

* Thu Apr 24 2014 Alexey Shabalin <shaba@altlinux.ru> 1:210-alt7
- v210-stable snapshot (1ba98e163ed872d8744ff644e3d255b4be171bc6)
- fixed typo, /lib/systemd/network should work fine
- revert patch "udev always rename network"
- start systemd-sysctl.service after systemd-module-load.service
- start systemd-ask-password-wall.service after getty@tty1.service
- drop default enabled getty.target.wants/getty@tty*.service
- add systemd-vconsole-setup@.service for another way localize ttyX
- add config with "TTYVTDisallocate=no" for getty@tty1.service
- apply 1003-udev-netlink-null-rules.patch from opensuse
- drop network.service unit - use sysvinit script
- rename 99-default.preset to 99-default-disable.preset
- add 90-default.preset

* Mon Apr 14 2014 Sergey V Turchin <zerg@altlinux.org> 1:210-alt4.2
- NMU: don't disable getty for tty1 because prefdm have conflict
- NMU: don't disable plymouth-quit for xdm-like

* Wed Apr 09 2014 Sergey V Turchin <zerg@altlinux.org> 1:210-alt4.1
- NMU: disable getty for tty1 by default (ALT#29959)
- NMU: don't run prefdm before plymouth-quit

* Thu Mar 20 2014 Alexey Shabalin <shaba@altlinux.ru> 1:210-alt4
- v210-stable snapshot (28be65e12016d365783ac9646bf588ec68352b75)

* Wed Mar 19 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:210-alt3
- systemd-tmpfiles.filetrigger:
 + Skip filetrigger if root is fake (e.g. in hasher) (ALT#29895).
 + Move to utils subpackage.

* Fri Mar 07 2014 Alexey Shabalin <shaba@altlinux.ru> 1:210-alt2
- snapshot of systemd-stable/v210-stable
- update bash3 completions
- new distribution-agnostic configs should be redefine old configs

* Tue Feb 25 2014 Alexey Shabalin <shaba@altlinux.ru> 1:210-alt1
- 210
- build systemd-networkd
- drop systemd-startup-nologin.conf tmpfile, used upstream systemd-nologin.conf
- add and define conditions for seccomp(disabled), IMA(disabled), selinux(enabled), apparmor(disabled)
- updated bash3 completions
- all systemd-* libraries moved to libsystemd package
- update %post
- renamed 80-net-name-slot.rules to 80-net-setup-link.rules
- give systemd-logind access to /proc when it's mounted with hidepid option
- /boot -> /boot/efi in efi-boot-generator
- return time zone setup from /etc/sysconfig/clock
- return hostname setup from /etc/sysconfig/network
- build python module
- build gtk-doc packages (libudev-devel-doc, libgudev-devel-doc)
- delete old dir /var/lib/systemd/random-seed

* Thu Jan  2 2014 Ivan Zakharyaschev <imz@altlinux.org> 1:208-alt4
- declare the file conflicts with systemd pkgs before the split of journalctl
  (Epoch 1 for the split pkg, so that the new split journalctl from Sisyphus
  or any branches conflicts with Epoch 0 old pkgs)
- declare shaba@ as the maintainer

* Thu Jan  2 2014 Ivan Zakharyaschev <imz@altlinux.org> 208-alt3
- split journalctl into a separate pkg
  (to be used for querying without systemd) (ALT#29674)

* Thu Oct 17 2013 Alexey Shabalin <shaba@altlinux.ru> 208-alt2
- update udev.init for create static inodes for SysV

* Wed Oct 02 2013 Alexey Shabalin <shaba@altlinux.ru> 208-alt1
- 208

* Tue Oct 01 2013 Alexey Shabalin <shaba@altlinux.ru> 207-alt3.git.a0f70805
- fixed post install (ALT#29411)

* Mon Sep 30 2013 Alexey Shabalin <shaba@altlinux.ru> 207-alt2.git.a0f70805
- fixed mount /usr (ALT#29407)
- default kernel.sysrq = 1 (ALT#29366)
- fixed error about /var/lib/systemd/random-seed

* Mon Sep 23 2013 Alexey Shabalin <shaba@altlinux.ru> 207-alt1.git.a0f70805
- upstream git snapshot a0f708053ba42c8289caed1107f498bbf332e204

* Wed Jul 24 2013 Alexey Shabalin <shaba@altlinux.ru> 206-alt1
- 206

* Fri Jul 05 2013 Alexey Shabalin <shaba@altlinux.ru> 205-alt1
- 205
- add udev.filetrigger for reload udev rules

* Thu Jun 13 2013 Sergey V Turchin <zerg@altlinux.org> 204-alt5
- turn off tmp.mount by default (ALT#29066)

* Wed May 29 2013 Alexey Shabalin <shaba@altlinux.ru> 204-alt4
- fix permition of /run/lock/serial (ALT#29032)
- move tmpfiles.d/{tmp.conf,x11.conf} to systemd-utils

* Mon May 27 2013 Alexey Shabalin <shaba@altlinux.ru> 204-alt3
- move /etc/modules-load.d/modules.conf from systemd to systemd-utils

* Fri May 17 2013 Alexey Shabalin <shaba@altlinux.ru> 204-alt2
- fix permitions for ALTLinux in /lib/tmpfiles.d/legacy.conf
- move sysctl  and tmpfiles configs to systemd-utils
- use /sbin/systemd-tmpfiles for create static inodes in SysV init script
- add systemd-coredump package

* Thu May 16 2013 Michael Shigorin <mike@altlinux.org> 204-alt1.1
- NMU: apply F18 patch to revert upstream breakage of ethX/ethY
  renaming, see also RH#896135, FDO#53837, FDO#56929

* Sun May 12 2013 Alexey Shabalin <shaba@altlinux.ru> 204-alt1
- 204
- add symlink /bin/systemctl -> /sbin/systemctl

* Wed May 08 2013 Alexey Shabalin <shaba@altlinux.ru> 203-alt1
- 203
- move root utils to /sbin
- split systemd-bash3 completion to several files
- disable build python module
- add systemd-utils package

* Tue Apr 09 2013 Alexey Shabalin <shaba@altlinux.ru> 201-alt1
- 201

* Mon Apr 08 2013 Alexey Shabalin <shaba@altlinux.ru> 200-alt3
- run systemd-vconsole-setup before getty.target

* Mon Apr 08 2013 Alexey Shabalin <shaba@altlinux.ru> 200-alt2
- fixed custom font in console
- remove conflict with hal for udev

* Fri Apr 05 2013 Alexey Shabalin <shaba@altlinux.ru> 200-alt1
- 200

* Tue Mar 12 2013 Alexey Shabalin <shaba@altlinux.ru> 198-alt1
- 198
- add systemd-journal-gateway package

* Tue Feb 12 2013 Alexey Shabalin <shaba@altlinux.ru> 197-alt6
- revert --action=add in systemd-udev-trigger.service

* Mon Feb 11 2013 Alexey Shabalin <shaba@altlinux.ru> 197-alt5
- mask 80-net-name-slot.rules in udev-rule-generator-net

* Thu Feb 07 2013 Alexey Shabalin <shaba@altlinux.ru> 197-alt4
- revert persistent net generator
- split package udev-rule-generator to udev-rule-generator-cdrom and udev-rule-generator-net
- add more preset dirs
- only enforce ALTLinux's disable-by-default policy

* Wed Feb 06 2013 Alexey Shabalin <shaba@altlinux.ru> 197-alt3
- move 75-net-description.rules and 75-tty-description.rules from udev-extras to udev-rules
- add default preset policy

* Tue Jan 29 2013 Alexey Shabalin <shaba@altlinux.ru> 197-alt2
- add --action=add to udevadm trigger in udevd.init
- add strict inter-package dependencies

* Wed Jan 16 2013 Alexey Shabalin <shaba@altlinux.ru> 197-alt1
- 197
- drop 75-persistent-net-generator.rules and write_net_rules
- revert support ALTLinux configuration files for console,locale,hostname
- build libnss-myhostname as separate package
- enable build bootchart
- fixed /etc/firsttime.d support

* Thu Nov 29 2012 Alexey Shabalin <shaba@altlinux.ru> 196-alt1
- 196
- move completion to separate noarch packages:
  bash-completion-systemd, bash-completion-udev, zsh-completion-systemd
- provide syslogd-daemon because the journal is fine as a syslog implementation
- add udev-hwdb package

* Thu Nov 22 2012 Alexey Shabalin <shaba@altlinux.ru> 195-alt3
- drop altlinux-storage-init.service,altlinux-wait-storage.service,altlinux-storage-init-late.service

* Thu Nov 22 2012 Alexey Shabalin <shaba@altlinux.ru> 195-alt2
- drop rtc.conf from modules-load.d

* Tue Oct 23 2012 Alexey Shabalin <shaba@altlinux.ru> 195-alt1
- 195

* Mon Oct 08 2012 Alexey Shabalin <shaba@altlinux.ru> 194-alt2
- add 60-raw.rules from util-linux

* Thu Oct 04 2012 Alexey Shabalin <shaba@altlinux.ru> 194-alt1
- 194

* Mon Oct 01 2012 Alexey Shabalin <shaba@altlinux.ru> 193-alt2
- drop altlinux-swap.service
- add /etc/profile.d/systemd.sh and export
  SYSTEMD_PAGER="/usr/bin/less -FR" (ALT#27784)

* Fri Sep 28 2012 Alexey Shabalin <shaba@altlinux.ru> 193-alt1
- 193
- add support build with microhttpd, but disable

* Thu Sep 27 2012 Alexey Shabalin <shaba@altlinux.ru> 192-alt1
- 192

* Fri Sep 21 2012 Alexey Shabalin <shaba@altlinux.ru> 190-alt1
- 190
- mask legacy services: halt, single, netfs
- fix load font on tty1-6 - add and autorun systemd-vconsole-setup@.service
- add package contains python binds for systemd APIs

* Tue Sep 18 2012 Alexey Shabalin <shaba@altlinux.ru> 189-alt4
- exclude run tmpfiles systemd-startup-nologin.conf from filetrigger
  for upgrade systemd. (ALT#27749)
- move create /run/nologin to separate file systemd-startup-nologin.conf.

* Fri Sep 14 2012 Alexey Shabalin <shaba@altlinux.ru> 189-alt3
- because initrd drop udev db, need full rebuild with udevadm trigger

* Wed Sep 12 2012 Alexey Shabalin <shaba@altlinux.ru> 189-alt2
- move libsystemd-journal,libsystemd-id128{-devel} to separate packages
- systemd-devel as noarch without any requires;
  many packages require pkgconfig/systemd.pc only

* Tue Aug 28 2012 Alexey Shabalin <shaba@altlinux.ru> 189-alt1
- snapshot fe1fed02c7637a2c18cd575f78be7fda27972148
- build without FSS (gcrypt and qrencode)

* Thu Aug 09 2012 Alexey Shabalin <shaba@altlinux.ru> 188-alt1
- 188
- update prefdm.service
- fix rule_generator.functions for udev > 185

* Wed Aug 08 2012 Alexey Shabalin <shaba@altlinux.ru> 187-alt5
- add rtc.conf to modules-load.d for load rtc kernel module at boot time
- drop altlinux-loadmodules.service
  add symlink /etc/modules-load.d/modules.conf -> /etc/modules
- add export SYSTEMD_LOG_TARGET=syslog in udev init script for don't log to kmsg (ALT#27610)

* Wed Aug 08 2012 Alexey Shabalin <shaba@altlinux.org> 187-alt4
- call multipath and kpartx with -u
- fix typo in altlinux-storage-init

* Wed Aug 08 2012 Alexey Shabalin <shaba@altlinux.org> 187-alt3
- run prefdm after getty.target
- add rpm filetrigger for create tmpfiles
- add Conflicts: DeviceKit (ALT#27612)
- add ploop devices to skip rules (ALT#27083)

* Wed Aug 01 2012 Alexey Shabalin <shaba@altlinux.ru> 187-alt2
- update network.service
- add a storage setup after cryptsetup.target
- cleanup spec
- update ALTLinux specific unit files
- add unit file for run scripts from /etc/firsttime.d after install distro
- add unit for update /etc/issue and /etc/issue.net files
- add systemd-rc-local-generator for ALTLinux
- add Conflicts: hal

* Fri Jul 20 2012 Alexey Shabalin <shaba@altlinux.ru> 187-alt1
- 187

* Mon Jul 16 2012 Alexey Shabalin <shaba@altlinux.ru> 186-alt1
- 186
- fix path to udev binary in init script (ALT#27471)
- change Obsoletes to Conflicts for libudev

* Wed Jun 20 2012 Alexey Shabalin <shaba@altlinux.ru> 185-alt3
- fix install - add Obsoletes: libudev < 185-alt3 (ALT#27472)

* Wed Jun 20 2012 Alexey Shabalin <shaba@altlinux.org> 185-alt2
- rename libudev to libudev1.
- return cd rule generator (ALT#26389).
- run setsysfont as ExecStartPre for getty instead of fbsetfont
  service.
- units: avoid redundant VT clearing by agetty (thx Michal Schmidt).
- ALTLinux support: Don't set LANG to "C" by default. (thx Mikhail Efremov) (ALT#27408).

* Tue Jun 05 2012 Alexey Shabalin <shaba@altlinux.ru> 185-alt1
- 185
- add udev subpackages
- drop gtk subpackage (move to systemd-ui)

* Fri Mar 16 2012 Alexey Shabalin <shaba@altlinux.ru> 44-alt1
- v44

* Mon Mar 05 2012 Alexey Shabalin <shaba@altlinux.ru> 43-alt2
- split libsystemd-daemon(-devel) and libsystemd-login(-devel) packages

* Wed Feb 22 2012 Alexey Shabalin <shaba@altlinux.ru> 43-alt1
- v43
- merge units into the main package

* Fri Jan 13 2012 Alexey Shabalin <shaba@altlinux.ru> 37-alt3
- adapt for filesystem-2.3.10-alt1

* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 37-alt2.1
- Rebuild with Python-2.7

* Tue Nov 01 2011 Alexey Shabalin <shaba@altlinux.ru> 37-alt2
- rebuild with libcryptsetup-1.4.0

* Wed Oct 12 2011 Alexey Shabalin <shaba@altlinux.ru> 37-alt1
- v37
- mask SYSV plymouth service

* Fri Sep 23 2011 Alexey Shabalin <shaba@altlinux.ru> 36-alt1
- v36

* Thu Sep 01 2011 Alexey Shabalin <shaba@altlinux.ru> 35-alt1
- v35

* Mon Aug 29 2011 Alexey Shabalin <shaba@altlinux.ru> 34-alt1
- v34

* Mon Aug 22 2011 Alexey Shabalin <shaba@altlinux.ru> 33-alt2.gite1915
- fix ABRT on service file reloading

* Mon Aug 08 2011 Alexey Shabalin <shaba@altlinux.ru> 33-alt1
- v33

* Thu Jul 28 2011 Alexey Shabalin <shaba@altlinux.ru> 31-alt1
- v31
- add devel package

* Thu Jun 16 2011 Alexey Shabalin <shaba@altlinux.ru> 29-alt1
- v29

* Fri Jun 10 2011 Alexey Shabalin <shaba@altlinux.ru> 28-alt3
- allow enable/disable symlinks for ALTLinux
- enable chkconfig support in systemctl for ALTLinux

* Sun Jun 05 2011 Alexey Shabalin <shaba@altlinux.ru> 28-alt2
- rebuild with new libnotify

* Sun May 29 2011 Alexey Shabalin <shaba@altlinux.ru> 28-alt1
- v28

* Sun May 22 2011 Alexey Shabalin <shaba@altlinux.ru> 27-alt2
- backported fixes from upstream

* Fri May 20 2011 Alexey Shabalin <shaba@altlinux.ru> 27-alt1
- v27
- mask /etc/init.d/killall
- add Requires: libnss-myhostname
- drop previus patch for pull rpcbind.target to multi-user.target,
  nfs services must requires rpcbind.target

* Sat May 14 2011 Alexey Shabalin <shaba@altlinux.ru> 26-alt3
- update network.service
- pull rpcbind.target to multi-user.target

* Sat May 07 2011 Alexey Shabalin <shaba@altlinux.ru> 26-alt2
- move systemd-analyze(python) tool to subpackage

* Wed May 04 2011 Alexey Shabalin <shaba@altlinux.ru> 26-alt1
- v26
- /var/lock and /var/run on tmpfs
- add altlinux-kmsg-loglevel.service
- add altlinux-save-dmesg.service

* Tue Mar 22 2011 Alexey Shabalin <shaba@altlinux.ru> 20-alt3
- disable legacy services: fbsetfont and keytable

* Mon Mar 21 2011 Alexey Shabalin <shaba@altlinux.ru> 20-alt2
- disable swap enable by systemd, use altlinux-swap.service
- disable "SysVConsole" legacy output to console

* Wed Mar 09 2011 Alexey Shabalin <shaba@altlinux.ru> 20-alt1
- v20

* Fri Mar 04 2011 Alexey Shabalin <shaba@altlinux.ru> 19-alt3.git20110301
- add workaround Conflicts: SysVinit < 2.86-alt2 in sysvinit-utils

* Wed Mar 02 2011 Alexey Shabalin <shaba@altlinux.ru> 19-alt2.git20110301
- upstream snapshot 20110301

* Tue Mar 01 2011 Alexey Shabalin <shaba@altlinux.ru> 19-alt1
- v19
- add condstop, condreload for compatibility with ALTLinux

* Mon Feb 28 2011 Alexey Shabalin <shaba@altlinux.ru> 18-alt2.git20110225
- upstream snapshot 20110225
- modify altlinux-clock for run only when /etc/adjtime is missing, and use hwclock-load
- add support mount /proc with gid=proc
- add network.service

* Thu Feb 17 2011 Alexey Shabalin <shaba@altlinux.ru> 18-alt1
- v18

* Tue Feb 15 2011 Alexey Shabalin <shaba@altlinux.ru> 17-alt9.20110213
- add one altlinux-storage-init service (with altlinux-storage-init script) instead of altlinux-lvm, altlinux-multipath, altlinux-raid services

* Tue Feb 15 2011 Alexey Shabalin <shaba@altlinux.ru> 17-alt8.20110213
- fix run clock service
- add altlinux-swap service
- add altlinux-lvm, altlinux-multipath, altlinux-raid services

* Mon Feb 14 2011 Alexey Shabalin <shaba@altlinux.ru> 17-alt7.20110213
- adapt completion for bash3; thx to iv@
- add altlinux-clock service
- fix work with plymoth
- package dir /etc/modules-load.d and add example
- add quota services to local-fs.target
- build with libcryptsetup support

* Wed Feb 09 2011 Alexey Shabalin <shaba@altlinux.ru> 17-alt6.20110209
- upstream snapshot
- plymouth support
- drop multipath and evms services

* Mon Feb 07 2011 Alexey Shabalin <shaba@altlinux.ru> 17-alt5
- add multipath service
- add update_chrooted service
- add idetune service
- add evms service to git (but not install)

* Fri Feb 04 2011 Alexey Shabalin <shaba@altlinux.ru> 17-alt4
- add load legacy module configuration from /etc/modules
- use hwclock-load.service instead init.d/clock
- use systemd-random-seed-load.service instead init.d/random

* Thu Feb 03 2011 Alexey Shabalin <shaba@altlinux.ru> 17-alt3
- don't use sysinit
- fix symlink path for rc-local

* Tue Feb 01 2011 Alexey Shabalin <shaba@altlinux.ru> 17-alt2
- add prefdm service
- fix syslog name service
- add Before=sysinit.target to sysinit.service
- use mingetty instead of agetty

* Tue Jan 25 2011 Alexey Shabalin <shaba@altlinux.ru> 17-alt1
- version 17

* Fri Jan 14 2011 Alexey Shabalin <shaba@altlinux.ru> 16-alt1
- version 16

* Fri Nov 19 2010 Alexey Shabalin <shaba@altlinux.ru> 13-alt1
- version 13

* Sun Sep 19 2010 Alexey Shabalin <shaba@altlinux.ru> 10-alt1
- version 10 + snapshot Sep 22 2010

* Thu Sep 09 2010 Alexey Shabalin <shaba@altlinux.ru> 9-alt1
- version 9

* Thu Aug 26 2010 Alexey Shabalin <shaba@altlinux.ru> 8-alt1
- version 8
- build with libaudit

* Wed Aug 25 2010 Alexey Shabalin <shaba@altlinux.ru> 7-alt1
- version 7
- build with selinux

* Fri Jul 09 2010 Alexey Shabalin <shaba@altlinux.ru> 2-alt1
- version 2

* Wed Jul 07 2010 Alexey Shabalin <shaba@altlinux.ru> 1-alt1
- initial build for ALTLinux
