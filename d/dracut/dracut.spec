# SPDX-License-Identifier: GPL-2.0-or-later

%define _unpackaged_files_terminate_build 1
%define dracutlibdir %prefix/lib/dracut
%def_enable documentation

# We ship a .pc file but don't want to have a dep on pkg-config. We
# strip the automatically generated dep here and instead co-own the
# directory.
%filter_from_requires /pkg-config/d
%filter_from_requires /^\/usr\/share\/pkgconfig/d

Name: dracut
Version: 051
Release: alt1

Summary: Initramfs generator using udev
Group: System/Base

# The entire source code is GPLv2+
# except install/* which is LGPLv2+
License: GPLv2+ and LGPLv2+

Vcs: https://github.com/dracutdevs/dracut.git
Url: https://dracut.wiki.kernel.org/

Source: %name-%version.tar

BuildRequires: bash >= 4
BuildRequires: git
BuildRequires: pkgconfig(libkmod) >= 23

BuildRequires: systemd-devel
BuildRequires: bash-completion

%if_enabled documentation
BuildRequires: docbook-style-xsl docbook-dtds xsltproc
BuildRequires: asciidoc xsltproc
%endif

Requires: bash >= 4
Requires: coreutils
Requires: cpio
Requires: filesystem
Requires: findutils
Requires: grep
Requires: kmod
Requires: sed
Requires: xz
Requires: gzip
Requires: pigz

Requires: util-linux >= 2.21
Requires: udev >= 219
Requires: hardlink
Requires: kpartx
Requires: procps
AutoReq: noshell, noshebang

%description
dracut contains tools to create bootable initramfses for the Linux
kernel. Unlike previous implementations, dracut hard-codes as little
as possible into the initramfs. dracut contains various modules which
are driven by the event-based udev. Having root on MD, DM, LVM2, LUKS
is supported as well as NFS, iSCSI, NBD, FCoE with the dracut-network
package.

%package network
Summary: Dracut modules to build a dracut initramfs with network support
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
Requires: iputils
Requires: iproute
Requires: NetworkManager
AutoReq: noshell, noshebang

%description network
This package requires everything which is needed to build a generic
all purpose initramfs with network support with dracut.

%package caps
Summary: Dracut modules to build a dracut initramfs which drops capabilities
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
Requires: libcap-utils
AutoReq: noshell, noshebang

%description caps
This package requires everything which is needed to build an
initramfs with dracut, which drops capabilities.

%package live
Summary: Dracut modules to build a dracut initramfs with live image capabilities
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
Requires: %name-network = %EVR
Requires: tar gzip coreutils bash dmsetup curl
Requires: fuse ntfs-3g
AutoReq: noshell, noshebang

%description live
This package requires everything which is needed to build an
initramfs with dracut, with live image capabilities, like Live CDs.

%package config-generic
Summary: Dracut configuration to turn off hostonly image generation
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
AutoReq: noshell, noshebang

%description config-generic
This package provides the configuration to turn off the host specific initramfs
generation with dracut and generates a generic image by default.

%package config-rescue
Summary: Dracut configuration to turn on rescue image generation
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
AutoReq: noshell, noshebang

%description config-rescue
This package provides the configuration to turn on the rescue initramfs
generation with dracut.

%package tools
Summary: Dracut tools to build the local initramfs
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
AutoReq: noshell, noshebang

%description tools
This package contains tools to assemble the local initrd and host configuration.

%package squash
Summary: Dracut module to build an initramfs with most files in a squashfs image
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
Requires: squashfs-tools
AutoReq: noshell, noshebang

%description squash
This package provides a dracut module to build an initramfs, but store most files
in a squashfs image, result in a smaller initramfs size and reduce runtime memory
usage.

%package fips
Summary: Dracut modules to build a dracut initramfs with an integrity check
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
Requires: libkcapi-fipscheck
Requires: libkcapi-hmaccalc
AutoReq: noshell, noshebang

%description fips
This package requires everything which is needed to build an
initramfs with dracut, which does an integrity check of the kernel
and its cryptography during startup.

%package ima
Summary: Dracut modules to build a dracut initramfs with IMA
Group: System/Base
BuildArch: noarch
Requires: %name = %EVR
#Requires: evmctl
Requires: keyutils
AutoReq: noshell, noshebang

%description ima
This package requires everything which is needed to build an
initramfs (using dracut) which tries to load an IMA policy during startup.

%prep
%setup
echo "DRACUT_VERSION=%version" > dracut-version.sh

%build
%configure \
	--systemdsystemunitdir=%_unitdir \
	--bashcompletiondir=$(pkg-config --variable=completionsdir bash-completion) \
	--libdir=%prefix/lib \
	%{subst_enable documentation}

%make_build

%install
%makeinstall_std \
     libdir=%prefix/lib

echo "DRACUT_VERSION=%version-%release" > %buildroot%dracutlibdir/dracut-version.sh

# compatibility symlinks
mkdir -p %buildroot/sbin
ln -r -s %buildroot%_sbindir/mkinitrd %buildroot/sbin/mkinitrd

# Cleanup
rm -fr -- %buildroot%dracutlibdir/modules.d/01fips

# for systemd, better use systemd-bootchart
rm -fr -- %buildroot%dracutlibdir/modules.d/00bootchart

# we do not support dash in the initramfs
rm -fr -- %buildroot%dracutlibdir/modules.d/00dash

# we do not support mksh in the initramfs
rm -fr -- %buildroot%dracutlibdir/modules.d/00mksh

# remove gentoo specific modules
rm -fr -- %buildroot%dracutlibdir/modules.d/50gensplash

# with systemd IMA and selinux modules do not make sense
rm -fr -- %buildroot%dracutlibdir/modules.d/96securityfs
rm -fr -- %buildroot%dracutlibdir/modules.d/97masterkey
rm -fr -- %buildroot%dracutlibdir/modules.d/98integrity

%ifnarch s390 s390x
# remove architecture specific modules
rm -fr -- %buildroot%dracutlibdir/modules.d/80cms
rm -fr -- %buildroot%dracutlibdir/modules.d/81cio_ignore
rm -fr -- %buildroot%dracutlibdir/modules.d/91zipl
rm -fr -- %buildroot%dracutlibdir/modules.d/95dasd
rm -fr -- %buildroot%dracutlibdir/modules.d/95dasd_mod
rm -fr -- %buildroot%dracutlibdir/modules.d/95dasd_rules
rm -fr -- %buildroot%dracutlibdir/modules.d/95dcssblk
rm -fr -- %buildroot%dracutlibdir/modules.d/95qeth_rules
rm -fr -- %buildroot%dracutlibdir/modules.d/95zfcp
rm -fr -- %buildroot%dracutlibdir/modules.d/95zfcp_rules
rm -fr -- %buildroot%dracutlibdir/modules.d/95znet
%else
rm -fr -- %buildroot%dracutlibdir/modules.d/00warpclock
%endif
%ifnarch ppc ppc64
rm -fr -- %buildroot%dracutlibdir/modules.d/90ppcmac
%endif
# remove gentoo specific modules
rm -fr -- %buildroot%dracutlibdir/modules.d/50gensplash

mkdir -p %buildroot/boot/dracut
mkdir -p %buildroot/%_var/lib/dracut/overlay
mkdir -p %buildroot%_logdir
touch %buildroot%_logdir/dracut.log
mkdir -p %buildroot%_sharedstatedir/initramfs

install -m 0644 dracut.conf.d/alt.conf.example %buildroot%dracutlibdir/dracut.conf.d/01-dist.conf
rm -f %buildroot%_mandir/man?/*suse*

echo 'hostonly="no"' > %buildroot%dracutlibdir/dracut.conf.d/02-generic-image.conf
echo 'dracut_rescue_image="yes"' > %buildroot%dracutlibdir/dracut.conf.d/02-rescue.conf

%files
%if_enabled documentation
%doc README.md HACKING TODO AUTHORS NEWS dracut.html dracut.png dracut.svg
%endif
%doc COPYING
%_sbindir/dracut
%_datadir/bash-completion/completions/dracut
%_datadir/bash-completion/completions/lsinitrd
%_sbindir/mkinitrd
/sbin/mkinitrd
%_bindir/lsinitrd
%dir %dracutlibdir
%dir %dracutlibdir/modules.d
%dracutlibdir/dracut-functions.sh
%dracutlibdir/dracut-init.sh
%dracutlibdir/dracut-functions
%dracutlibdir/dracut-version.sh
%dracutlibdir/dracut-logger.sh
%dracutlibdir/dracut-initramfs-restore
%dracutlibdir/dracut-install
%dracutlibdir/skipcpio
%config(noreplace) %_sysconfdir/dracut.conf
%dracutlibdir/dracut.conf.d/01-dist.conf
%dir %_sysconfdir/dracut.conf.d
%dir %dracutlibdir/dracut.conf.d
%_datadir/pkgconfig/dracut.pc

%if_enabled documentation
%_mandir/man8/dracut.8*
%_mandir/man8/*service.8*
%_mandir/man8/mkinitrd.8*
%_mandir/man1/lsinitrd.1*
%_mandir/man7/dracut.kernel.7*
%_mandir/man7/dracut.cmdline.7*
%_mandir/man7/dracut.modules.7*
%_mandir/man7/dracut.bootup.7*
%_mandir/man5/dracut.conf.5*
%endif

%dracutlibdir/modules.d/00bash
%dracutlibdir/modules.d/00systemd
%ifnarch s390 s390x
%dracutlibdir/modules.d/00warpclock
%endif
#%dracutlibdir/modules.d/01fips
%dracutlibdir/modules.d/01systemd-initrd
%dracutlibdir/modules.d/03modsign
%dracutlibdir/modules.d/03rescue
%dracutlibdir/modules.d/04watchdog
%dracutlibdir/modules.d/04watchdog-modules
%dracutlibdir/modules.d/05busybox
%dracutlibdir/modules.d/06dbus
%dracutlibdir/modules.d/06rngd
%dracutlibdir/modules.d/10i18n
%dracutlibdir/modules.d/30convertfs
%dracutlibdir/modules.d/45url-lib
%dracutlibdir/modules.d/50drm
%dracutlibdir/modules.d/50plymouth
%dracutlibdir/modules.d/80lvmmerge
%dracutlibdir/modules.d/90btrfs
%dracutlibdir/modules.d/90crypt
%dracutlibdir/modules.d/90dm
%dracutlibdir/modules.d/90dmraid
%dracutlibdir/modules.d/90kernel-modules
%dracutlibdir/modules.d/90kernel-modules-extra
%dracutlibdir/modules.d/90lvm
%dracutlibdir/modules.d/90mdraid
%dracutlibdir/modules.d/90multipath
%dracutlibdir/modules.d/90nvdimm
%ifarch ppc ppc64
%dracutlibdir/modules.d/90ppcmac
%endif
%dracutlibdir/modules.d/90qemu
%dracutlibdir/modules.d/91crypt-gpg
%dracutlibdir/modules.d/91crypt-loop
%dracutlibdir/modules.d/95debug
%dracutlibdir/modules.d/95fstab-sys
%dracutlibdir/modules.d/95lunmask
%dracutlibdir/modules.d/95nvmf
%dracutlibdir/modules.d/95resume
%dracutlibdir/modules.d/95rootfs-block
%dracutlibdir/modules.d/95terminfo
%dracutlibdir/modules.d/95udev-rules
%dracutlibdir/modules.d/95virtfs
%ifarch s390 s390x
%dracutlibdir/modules.d/80cms
%dracutlibdir/modules.d/81cio_ignore
%dracutlibdir/modules.d/91zipl
%dracutlibdir/modules.d/95dasd
%dracutlibdir/modules.d/95dasd_mod
%dracutlibdir/modules.d/95dasd_rules
%dracutlibdir/modules.d/95dcssblk
%dracutlibdir/modules.d/95qeth_rules
%dracutlibdir/modules.d/95zfcp
%dracutlibdir/modules.d/95zfcp_rules
%endif
#%dracutlibdir/modules.d/96securityfs
#%dracutlibdir/modules.d/97masterkey
#%dracutlibdir/modules.d/98integrity
%dracutlibdir/modules.d/97biosdevname
%dracutlibdir/modules.d/98dracut-systemd
%dracutlibdir/modules.d/98ecryptfs
%dracutlibdir/modules.d/98pollcdrom
%dracutlibdir/modules.d/98selinux
%dracutlibdir/modules.d/98syslog
%dracutlibdir/modules.d/98usrmount
%dracutlibdir/modules.d/99base
%dracutlibdir/modules.d/99memstrack
%dracutlibdir/modules.d/99fs-lib
%dracutlibdir/modules.d/99shutdown
%attr(0644,root,root) %ghost %config(missingok,noreplace) %_logdir/dracut.log
%dir %_sharedstatedir/initramfs
%_unitdir/dracut-shutdown.service
%_unitdir/sysinit.target.wants/dracut-shutdown.service
%_unitdir/dracut-cmdline.service
%_unitdir/dracut-initqueue.service
%_unitdir/dracut-mount.service
%_unitdir/dracut-pre-mount.service
%_unitdir/dracut-pre-pivot.service
%_unitdir/dracut-pre-trigger.service
%_unitdir/dracut-pre-udev.service
%_unitdir/initrd.target.wants/dracut-cmdline.service
%_unitdir/initrd.target.wants/dracut-initqueue.service
%_unitdir/initrd.target.wants/dracut-mount.service
%_unitdir/initrd.target.wants/dracut-pre-mount.service
%_unitdir/initrd.target.wants/dracut-pre-pivot.service
%_unitdir/initrd.target.wants/dracut-pre-trigger.service
%_unitdir/initrd.target.wants/dracut-pre-udev.service
%prefix/lib/kernel/install.d/50-dracut.install

%files network
%dracutlibdir/modules.d/02systemd-networkd
%dracutlibdir/modules.d/35network-manager
%dracutlibdir/modules.d/35network-legacy
%dracutlibdir/modules.d/35network-wicked
%dracutlibdir/modules.d/40network
%dracutlibdir/modules.d/45ifcfg
%dracutlibdir/modules.d/90kernel-network-modules
%dracutlibdir/modules.d/90qemu-net
%dracutlibdir/modules.d/95cifs
%dracutlibdir/modules.d/95fcoe
%dracutlibdir/modules.d/95fcoe-uefi
%dracutlibdir/modules.d/95iscsi
%dracutlibdir/modules.d/95nbd
%dracutlibdir/modules.d/95nfs
%dracutlibdir/modules.d/95ssh-client
%ifarch s390 s390x
%dracutlibdir/modules.d/95znet
%endif
%dracutlibdir/modules.d/99uefi-lib

%files caps
%dracutlibdir/modules.d/02caps

%files live
%dracutlibdir/modules.d/99img-lib
%dracutlibdir/modules.d/90dmsquash-live
%dracutlibdir/modules.d/90dmsquash-live-ntfs
%dracutlibdir/modules.d/90livenet

%files tools
%if_enabled documentation
%doc %_man8dir/dracut-catimages.8*
%endif

%_sbindir/dracut-catimages
%dir /boot/dracut
%dir %_var/lib/dracut
%dir %_var/lib/dracut/overlay

%files squash
%dracutlibdir/modules.d/99squash

%files config-generic
%dracutlibdir/dracut.conf.d/02-generic-image.conf

%files config-rescue
%dracutlibdir/dracut.conf.d/02-rescue.conf
%prefix/lib/kernel/install.d/51-dracut-rescue.install

#%files fips
#%config %_sysconfdir/dracut.conf.d/40-fips.conf
#%dracutlibdir/modules.d/01fips

#%files ima
#%config %_sysconfdir/dracut.conf.d/40-ima.conf
#%dracutlibdir/modules.d/96securityfs
#%dracutlibdir/modules.d/97masterkey
#%dracutlibdir/modules.d/98integrity

%changelog
* Fri Dec 18 2020 Alexey Shabalin <shaba@altlinux.org> 051-alt1
- 051

* Sun Nov 08 2020 Alexey Shabalin <shaba@altlinux.org> 050-alt4.git.831e31
- Fixed path /usr/lib/udev -> /lib/udev

* Sat Nov 07 2020 Alexey Shabalin <shaba@altlinux.org> 050-alt3.git.831e31
- Install dracut, dracut-catimages, mkinitrd to sbindir
- Delete requires to systemd

* Sat Nov 07 2020 Alexey Shabalin <shaba@altlinux.org> 050-alt2.git.831e31
- Update to upstream master snapshot
- Update spec
- Disable autoreq for shell scripts

* Wed Mar 18 2020 Vitaly Chikunov <vt@altlinux.org> 050-alt1
- Initial import into ALT.
- Based on dracut native spec.
