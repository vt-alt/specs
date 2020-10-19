%global __find_debuginfo_files %nil

%define rname qemu
%define _group vmusers
%define rulenum 90
%define _libexecdir /usr/libexec
%define _localstatedir /var

Name: pve-%rname
Version: 5.1.0
Release: alt2
Epoch: 1
Summary: QEMU CPU Emulator
License: GPL/LGPL/BSD
Group: Emulators
Requires: %name-system = %version-%release %name-user = %version-%release
Conflicts: %rname
URL: http://www.nongnu.org/qemu/

Source0: qemu-%version.tar.xz
Source2: qemu-kvm.control.in
Source4: qemu-kvm.rules
# qemu-kvm back compat wrapper
Source5: qemu-kvm.sh

Source100: Logo.bmp
Source101: libproxmox_backup_qemu.so.x86_64-linux
Source102: libproxmox_backup_qemu.so.aarch64-linux
Source103: proxmox-backup-qemu.h

Patch100: qemu-3.0.1-uuid.patch
Patch101: qemu-pbs-link.patch
Patch10: 0001-block-block-copy-always-align-copied-region-to-clust.patch
Patch11: 0002-Revert-qemu-img-convert-Don-t-pre-zero-images.patch
Patch12: 0003-usb-fix-setup_len-init-CVE-2020-14364.patch
Patch13: 0001-PVE-Config-block-file-change-locking-default-to-off.patch
Patch14: 0002-PVE-Config-Adjust-network-script-path-to-etc-kvm.patch
Patch15: 0003-PVE-Config-set-the-CPU-model-to-kvm64-32-instead-of-.patch
Patch16: 0004-PVE-Config-ui-spice-default-to-pve-certificates.patch
Patch17: 0005-PVE-Config-smm_available-false.patch
Patch18: 0006-PVE-Config-glusterfs-no-default-logfile-if-daemonize.patch
Patch19: 0007-PVE-Config-rbd-block-rbd-disable-rbd_cache_writethro.patch
Patch20: 0008-PVE-Up-qmp-add-get_link_status.patch
Patch21: 0009-PVE-Up-glusterfs-allow-partial-reads.patch
Patch22: 0010-PVE-Up-qemu-img-return-success-on-info-without-snaps.patch
Patch23: 0011-PVE-Up-qemu-img-dd-add-osize-and-read-from-to-stdin-.patch
Patch24: 0012-PVE-Up-qemu-img-dd-add-isize-parameter.patch
Patch25: 0013-PVE-Up-qemu-img-dd-add-n-skip_create.patch
Patch26: 0014-PVE-virtio-balloon-improve-query-balloon.patch
Patch27: 0015-PVE-qapi-modify-query-machines.patch
Patch28: 0016-PVE-qapi-modify-spice-query.patch
Patch29: 0017-PVE-internal-snapshot-async.patch
Patch30: 0018-add-optional-buffer-size-to-QEMUFile.patch
Patch31: 0019-PVE-block-add-the-zeroinit-block-driver-filter.patch
Patch32: 0020-PVE-Add-dummy-id-command-line-parameter.patch
Patch33: 0021-PVE-Config-Revert-target-i386-disable-LINT0-after-re.patch
Patch34: 0022-PVE-Up-Config-file-posix-make-locking-optiono-on-cre.patch
Patch35: 0023-PVE-monitor-disable-oob-capability.patch
Patch36: 0024-PVE-Compat-4.0-used-balloon-qemu-4-0-config-size-fal.patch
Patch37: 0025-PVE-Allow-version-code-in-machine-type.patch
Patch38: 0026-PVE-Backup-add-vma-backup-format-code.patch
Patch39: 0027-PVE-Backup-add-backup-dump-block-driver.patch
Patch40: 0028-PVE-Backup-proxmox-backup-patches-for-qemu.patch
Patch41: 0029-PVE-Backup-pbs-restore-new-command-to-restore-from-p.patch
Patch42: 0030-PVE-Backup-avoid-coroutines-to-fix-AIO-freeze-cleanu.patch
Patch43: 0031-drive-mirror-add-support-for-sync-bitmap-mode-never.patch
Patch44: 0032-drive-mirror-add-support-for-conditional-and-always-.patch
Patch45: 0033-mirror-add-check-for-bitmap-mode-without-bitmap.patch
Patch46: 0034-mirror-switch-to-bdrv_dirty_bitmap_merge_internal.patch
Patch47: 0035-iotests-add-test-for-bitmap-mirror.patch
Patch48: 0036-mirror-move-some-checks-to-qmp.patch
Patch49: 0037-PVE-Backup-Add-dirty-bitmap-tracking-for-incremental.patch
Patch50: 0038-PVE-backup-rename-incremental-to-use-dirty-bitmap.patch
Patch51: 0039-PVE-fixup-pbs-restore-API.patch
Patch52: 0040-PVE-always-set-dirty-counter-for-non-incremental-bac.patch
Patch53: 0041-PVE-use-proxmox_backup_check_incremental.patch
Patch54: 0042-PVE-fixup-pbs-backup-add-compress-and-encrypt-option.patch
Patch55: 0043-PVE-Add-PBS-block-driver-to-map-backup-archives-into.patch
Patch56: 0044-PVE-add-query_proxmox_support-QMP-command.patch
Patch57: 0045-pbs-fix-missing-crypt-and-compress-parameters.patch
Patch58: 0046-PVE-handle-PBS-write-callback-with-big-blocks-correc.patch
Patch59: 0047-PVE-add-zero-block-handling-to-PBS-dump-callback.patch
Patch60: 0048-PVE-add-query-pbs-bitmap-info-QMP-call.patch
Patch61: 0049-PVE-redirect-stderr-to-journal-when-daemonized.patch
Patch62: 0050-PVE-Add-sequential-job-transaction-support.patch
Patch63: 0051-PVE-Backup-Use-a-transaction-to-synchronize-job-stat.patch
Patch64: 0052-PVE-Backup-Use-more-coroutines-and-don-t-block-on-fi.patch

ExclusiveArch: x86_64 aarch64
BuildRequires: acpica bzlib-devel glib2-devel flex libaio-devel libalsa-devel libcap-devel
BuildRequires: libcap-ng-devel libcurl-devel libfdt-devel libgnutls-devel libiscsi-devel libjemalloc-devel libjpeg-devel
BuildRequires: liblzo2-devel libncurses-devel libnettle-devel libnuma-devel libpixman-devel libpng-devel ceph-devel
BuildRequires: libsasl2-devel libseccomp-devel libspice-server-devel libssh2-devel libusbredir-devel libxfs-devel
BuildRequires: makeinfo perl-Pod-Usage python-modules-compiler pkgconfig(glusterfs-api) pkgconfig(virglrenderer)
BuildRequires: libsystemd-devel libfuse3-devel
# librdmacm-devel libibverbs-devel libibumad-devel
BuildRequires: ipxe-roms-qemu seavgabios seabios

%description
QEMU is a fast processor emulator using dynamic translation to achieve
good emulation speed.  QEMU has two operating modes:

* Full system emulation.  In this mode, QEMU emulates a full system
  (for example a PC), including a processor and various peripherials.
  It can be used to launch different Operating Systems without rebooting
  the PC or to debug system code.

* User mode emulation.  In this mode, QEMU can launch Linux processes
  compiled for one CPU on another CPU.  It can be used to launch the
  Wine Windows API emulator or to ease cross-compilation and
  cross-debugging.

As QEMU requires no host kernel patches to run, it is very safe and easy
to use.

%package common
Summary: QEMU CPU Emulator - common files
Group: Emulators
Requires(pre): control >= 0.7.2
Requires(pre): shadow-utils sysvinit-utils
Requires: seavgabios
Requires: seabios
Requires: ipxe-roms-qemu >= 1.0.0-alt4.git93acb5d
Requires: %name-img = %version-%release
Requires: edk2-ovmf edk2-aarch64
Conflicts: %rname-common
Obsoletes: %name-aux < %version-%release

%description common
QEMU is a fast processor emulator using dynamic translation to achieve
good emulation speed.
This package contains common files for qemu.

%package system
Summary: QEMU CPU Emulator - full system emulation
Group: Emulators
Requires: %name-common = %version-%release
Conflicts: %rname-system

%description system
Full system emulation.  In this mode, QEMU emulates a full system
(for example a PC), including a processor and various peripherials.
It can be used to launch different Operating Systems without rebooting
the PC or to debug system code.

%package img
Summary: QEMU command line tool for manipulating disk images
Group: Emulators
Conflicts: %rname-img

%description img
This package provides a command line tool for manipulating disk images

%package -n ivshmem-tools
Summary: Client and server for QEMU ivshmem device
Group: Emulators

%description -n ivshmem-tools
This package provides client and server tools for QEMU's ivshmem device

%set_verify_elf_method fhs=relaxed

%prep
%setup -n %rname-%version

%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1

%patch100 -p1
%patch101 -p1 -b .-lpbs

%ifarch aarch64
install -m644 %SOURCE102 libproxmox_backup_qemu.so.0
%else
install -m644 %SOURCE101 libproxmox_backup_qemu.so.0
%endif
ln -s libproxmox_backup_qemu.so.0 libproxmox_backup_qemu.so
install -m644 %SOURCE103 proxmox-backup-qemu.h

cp -f %SOURCE2 qemu-kvm.control.in

%build
export CFLAGS="%optflags"
# non-GNU configure
./configure \
	--target-list=x86_64-softmmu,aarch64-softmmu \
	--prefix=%_prefix \
	--sysconfdir=%_sysconfdir \
	--libdir=%_libdir \
	--mandir=%_mandir \
	--libexecdir=%_libexecdir \
	--localstatedir=%_localstatedir \
	--extra-cflags="%optflags" \
	--disable-werror \
        --audio-drv-list="alsa" \
        --disable-capstone \
        --disable-gtk \
        --disable-guest-agent \
        --disable-guest-agent-msi \
        --disable-libnfs \
        --disable-libxml2 \
        --disable-sdl \
        --disable-smartcard \
        --disable-strip \
        --disable-xen \
        --enable-virglrenderer \
        --enable-curl \
        --enable-glusterfs \
        --enable-gnutls \
        --enable-jemalloc \
        --enable-libiscsi \
        --enable-libusb \
        --enable-linux-aio \
        --enable-numa \
        --enable-rbd \
        --enable-seccomp \
        --enable-spice \
        --enable-usb-redir \
        --enable-virtfs \
        --enable-xfsctl

sed -i 's|^QEMU_CFLAGS=|QEMU_CFLAGS=-I$(SRC_PATH) |' config-host.mak

%make_build V=1

sed -i 's/@GROUP@/%_group/g' qemu-kvm.control.in

%install
%makeinstall_std
install -pD -m644 libproxmox_backup_qemu.so.0 %buildroot%_libdir/libproxmox_backup_qemu.so.0

%define docdir %_docdir/%name-%version
#mv %buildroot%_docdir/qemu 
mkdir -p %buildroot%docdir
install -m644 LICENSE MAINTAINERS %buildroot%docdir/

install -m 0755 %SOURCE5 %buildroot%_bindir/qemu-kvm
ln -r -s %buildroot%_bindir/qemu-kvm %buildroot%_bindir/kvm
ln -r -s %buildroot%_bindir/qemu-kvm %buildroot%_bindir/qemu

install -m 0755 vma %buildroot%_bindir/vma

rm -f %buildroot%_bindir/check-*
rm -f %buildroot%_sysconfdir/udev/rules.d/*

install -D -m 0644 %SOURCE4 %buildroot%_sysconfdir/udev/rules.d/%rulenum-%rname-kvm.rules
install -D -m 0755 %rname-kvm.control.in %buildroot%_controldir/kvm

%if_enabled vnc_sasl
install -D -p -m 0644 qemu.sasl %buildroot%_sysconfdir/sasl2/%rname.conf
%endif

%find_lang %rname

rm -f %buildroot%_datadir/%rname/pxe*rom
rm -f %buildroot%_datadir/%rname/efi*rom
rm -f %buildroot%_datadir/%rname/vgabios*bin
rm -f %buildroot%_datadir/%rname/bios.bin
rm -f %buildroot%_datadir/%rname/bios-256k.bin
rm -f %buildroot%_datadir/%rname/s390-*.img
rm -f %buildroot%_datadir/%rname/openbios*
rm -f %buildroot%_datadir/%rname/u-boot*

for rom in e1000 ne2k_pci pcnet rtl8139 virtio eepro100 e1000e vmxnet3 ; do
  ln -r -s %buildroot%_datadir/ipxe/pxe-${rom}.rom %buildroot%_datadir/%rname/pxe-${rom}.rom
  ln -r -s %buildroot%_datadir/ipxe.efi/efi-${rom}.rom %buildroot%_datadir/%rname/efi-${rom}.rom
done

for bios in vgabios vgabios-cirrus vgabios-qxl vgabios-stdvga vgabios-vmware vgabios-virtio ; do
  ln -r -s %buildroot%_datadir/seavgabios/${bios}.bin %buildroot%_datadir/%rname/${bios}.bin
done

ln -r -s %buildroot%_datadir/seabios/{bios,bios-256k}.bin %buildroot%_datadir/%rname/

mkdir -p %buildroot%_datadir/pve-edk2-firmware
ln -sf ../OVMF/OVMF_CODE.fd %buildroot%_datadir/pve-edk2-firmware/OVMF_CODE.fd
ln -sf ../OVMF/OVMF_VARS.fd %buildroot%_datadir/pve-edk2-firmware/OVMF_VARS.fd
ln -sf ../AAVMF/QEMU_EFI-pflash.raw %buildroot%_datadir/pve-edk2-firmware/AAVMF_CODE.fd
ln -sf ../AAVMF/vars-template-pflash.raw %buildroot%_datadir/pve-edk2-firmware/AAVMF_VARS.fd


%check
# Disabled on aarch64 where it fails with several errors.  Will
# investigate and fix when we have access to real hardware
#ifnarch aarch64
#make V=1 check
#endif

%pre common
%_sbindir/groupadd -r -f %_group
if [ -f %_controldir/qemu-kvm ];then
%pre_control qemu-kvm
mv -f /var/run/control/qemu-kvm /var/run/control/kvm
else
%pre_control kvm
fi

%post common
%post_control -s vmusers kvm

%files common
%dir %docdir/
%docdir/LICENSE
%_libdir/libproxmox_backup_qemu.so.0
%_datadir/qemu
%_datadir/pve-edk2-firmware
%_sysconfdir/udev/rules.d/%rulenum-%rname-kvm.rules
%_controldir/*
%if_enabled vnc_sasl
%config(noreplace) %_sysconfdir/sasl2/%rname.conf
%endif

%files system -f %rname.lang
%_bindir/elf2dmp
%_bindir/qemu*system*
%_bindir/vma
%_bindir/qemu-edid
%_bindir/qemu-storage-daemon
%_libexecdir/qemu-bridge-helper
%_libexecdir/qemu-pr-helper

%files img
%_bindir/qemu-img
%_bindir/qemu-io
%_bindir/qemu-nbd
%_libexecdir/virtfs-proxy-helper
%_libexecdir/virtiofsd

#%files -n ivshmem-tools
#%_bindir/ivshmem-client
#%_bindir/ivshmem-server

%changelog
* Sat Oct 10 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:5.1.0-alt2
- 5.1.0-3 (fix CVE-2020-14364)

* Tue Sep 01 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:5.1.0-alt1
- 5.1.0-1

* Wed Mar 11 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:4.1.1-alt4
- 4.1.1-4 (fix CVE-2020-8608)

* Fri Mar 06 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:4.1.1-alt3
- 4.1.1-3 (fix CVE-2019-20382)

* Wed Jan 22 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:4.1.1-alt2
- 4.1.1-2

* Mon Nov 25 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:4.1.1-alt1
- 4.1.1-1

* Wed Nov 13 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:4.0.1-alt3
- 4.0.1-5

* Wed Oct 23 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:4.0.1-alt2
- 4.0.1-2

* Wed Oct 02 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:4.0.0-alt2
- 4.0.0-6

* Tue Aug 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:4.0.0-alt1
- 4.0.0-5

* Tue Jun 25 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:3.0.1-alt5
- 3.0.1-62

* Mon Jun 17 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:3.0.1-alt4
- 3.0.1-4

* Mon May 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:2.12.1-alt3
- 2.12.1-3

* Mon Oct 22 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:2.12.1-alt1
- 2.12.1-1

* Fri Sep 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 3.0.0-alt2
- fixed efi roms path

* Mon Sep 17 2018 Valery Inozemtsev <shrek@altlinux.ru> 3.0.0-alt1.S1
- 3.0.0-1

* Thu Sep 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.11.2-alt2.S1
- disable vde support

* Tue Sep 04 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.11.2-alt1.S1
- 2.11.2-1

* Mon Jul 16 2018 Igor Vlasenko <viy@altlinux.ru> 2.11.1-alt5.S1.1.qa2
- reverted repocop patch (closes: #35115)

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 2.11.1-alt5.S1.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * udev-files-in-etc for pve-qemu-common

* Thu May 17 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.11.1-alt5.S1.1
- remove problematic 'evdev 86' key from en-us keymap (closes: #34856)

* Mon Apr 09 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.11.1-alt5.S1
- 2.11.1-5

* Fri Mar 23 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.11.1-alt4.S1
- 2.11.1-4

* Tue Feb 20 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.9.1-alt9.S1
- 2.9.1-9

* Wed Jan 17 2018 Valery Inozemtsev <shrek@altlinux.ru> 2.9.1-alt6.S1
- 2.9.1-6

* Fri Dec 22 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.1-alt4.1
- rebuild with libiscsi 1.18

* Thu Dec 07 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.1-alt0.M80P.4
- backport to p8 branch

* Thu Dec 07 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.1-alt4
- fixes:
 + CVE-2017-17381 fix and backup race condition fix

* Mon Sep 25 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.1-alt0.M80C.1
- backport to c8 branch

* Fri Sep 08 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.1-alt0.M80P.1
- backport to p8 branch

* Fri Sep 08 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.1-alt1
- 2.9.1-1

* Mon Aug 07 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.0-alt0.M80P.3
- backport to p8 branch

* Mon Aug 07 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.0-alt3
- fix CVE-2017-7539, CVE-2017-11434, CVE-2017-11334, CVE-2017-10806, CVE-2017-10664, CVE-2017-9524, CVE-2017-9503

* Fri Jun 16 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.0-alt0.M80P.2
- backport to p8 branch

* Fri Jun 16 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.0-alt2
- merge various stable fixes

* Thu May 11 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.0-alt0.M80P.1
- backport to p8 branch

* Thu May 11 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.9.0-alt1
- 2.9.0-1

* Wed Apr 05 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt3.M80P.1
- backport to p8 branch

* Wed Apr 05 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt4
- 2.7.1-4

* Thu Feb 02 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt1.M80P.1
- backport to p8 branch

* Thu Feb 02 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt2
- various fixes

* Mon Jan 16 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt0.M80P.1
- backport to p8 branch

* Mon Jan 16 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Tue Dec 13 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt9.M80P.1
- backport to p8 branch

* Tue Dec 13 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt10
- 2.7.0-10

* Mon Dec 05 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt8.M80P.1
- backport to p8 branch

* Mon Dec 05 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt9
- 2.7.0-9

* Tue Nov 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt7.M80P.1
- backport to p8 branch

* Tue Nov 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt8
- 2.7.0-8

* Sun Oct 23 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt2.M80P.1
- backport to p8 branch

* Sun Oct 23 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt3
- various fixes

* Mon Oct 17 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt1.M80P.1
- backport to p8 branch

* Mon Oct 17 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.0-alt2
- 2.7.0-2

* Sun Oct 09 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.2-alt1.M80P.1
- backport to p8 branch

* Fri Oct 07 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.2-alt2
- 2.6.2-2

* Mon Oct 03 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.1-alt5.M80P.1
- backport to p8 branch

* Mon Oct 03 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.1-alt6
- various CVE fixes

* Tue Sep 20 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.1-alt4.M80P.1
- backport to p8 branch

* Mon Sep 19 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.1-alt5
- various CVE fixes

* Thu Aug 25 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.1-alt2
- added in some stable hotfixes

* Mon Aug 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Tue Aug 02 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.0-alt2
- fixed CVE-2016-6490, CVE-2016-2391, CVE-2016-5126

* Sun Jul 10 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Wed Jun 01 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.5.1.1-alt1
- 2.5.1.1

* Tue Feb 09 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.5.0-alt1
- proxmox version
