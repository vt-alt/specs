%define rname qemu
%define _group vmusers
%define rulenum 90
%define _libexecdir /usr/libexec
%define _localstatedir /var

Name: pve-%rname
Version: 3.0.1
Release: alt5
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

Patch0: qemu-alt.patch
Patch100: qemu-3.0.1-uuid.patch

Patch10: 0001-PVE-Config-block-file-change-locking-default-to-off.patch
Patch11: 0002-PVE-Config-Adjust-network-script-path-to-etc-kvm.patch
Patch12: 0003-PVE-Config-use-kvm-by-default.patch
Patch13: 0004-PVE-Config-set-the-CPU-model-to-kvm64-32-instead-of-.patch
Patch14: 0005-PVE-Config-ui-spice-default-to-pve-certificates.patch
Patch15: 0006-PVE-Config-smm_available-false.patch
Patch16: 0007-PVE-Config-glusterfs-no-default-logfile-if-daemonize.patch
Patch17: 0008-PVE-Config-rbd-block-rbd-disable-rbd_cache_writethro.patch
Patch18: 0009-PVE-Up-qmp-add-get_link_status.patch
Patch19: 0010-PVE-Up-glusterfs-allow-partial-reads.patch
Patch20: 0011-PVE-Up-qemu-img-return-success-on-info-without-snaps.patch
Patch21: 0012-PVE-Up-qemu-img-dd-add-osize-and-read-from-to-stdin-.patch
Patch22: 0013-PVE-Up-qemu-img-dd-add-isize-parameter.patch
Patch23: 0014-PVE-Up-qemu-img-dd-add-n-skip_create.patch
Patch24: 0015-PVE-virtio-balloon-improve-query-balloon.patch
Patch25: 0016-PVE-qapi-modify-query-machines.patch
Patch26: 0017-PVE-qapi-modify-spice-query.patch
Patch27: 0018-PVE-internal-snapshot-async.patch
Patch28: 0019-PVE-block-add-the-zeroinit-block-driver-filter.patch
Patch29: 0020-PVE-backup-modify-job-api.patch
Patch30: 0021-PVE-backup-introduce-vma-archive-format.patch
Patch31: 0022-PVE-Deprecated-adding-old-vma-files.patch
Patch32: 0023-PVE-vma-add-throttling-options-to-drive-mapping-fifo.patch
Patch33: 0024-PVE-vma-add-cache-option-to-device-map.patch
Patch34: 0025-PVE-vma-remove-forced-NO_FLUSH-option.patch
Patch35: 0026-PVE-Add-dummy-id-command-line-parameter.patch
Patch36: 0027-PVE-Config-Revert-target-i386-disable-LINT0-after-re.patch
Patch37: 0028-PVE-Up-Config-file-posix-make-locking-optiono-on-cre.patch
Patch38: 0001-monitor-guard-iothread-access-by-mon-use_io_thread.patch
Patch39: 0002-monitor-delay-monitor-iothread-creation.patch
Patch40: 0003-kvm-Add-support-to-KVM_GET_MSR_FEATURE_INDEX_LIST-an.patch
Patch41: 0004-i386-Add-CPUID-bit-and-feature-words-for-IA32_ARCH_C.patch
Patch42: 0005-i386-Add-new-MSR-indices-for-IA32_PRED_CMD-and-IA32_.patch
Patch43: 0006-x86-Data-structure-changes-to-support-MSR-based-feat.patch
Patch44: 0007-x86-define-a-new-MSR-based-feature-word-FEATURE_WORD.patch
Patch45: 0008-target-i386-add-MDS-NO-feature.patch
Patch46: 0009-target-i386-define-md-clear-bit.patch

ExclusiveArch: x86_64
BuildRequires: acpica bzlib-devel glib2-devel flex libaio-devel libalsa-devel libbluez-devel libcap-devel
BuildRequires: libcap-ng-devel libcurl-devel libfdt-devel libgnutls-devel libiscsi-devel libjemalloc-devel libjpeg-devel
BuildRequires: liblzo2-devel libncurses-devel libnettle-devel libnuma-devel libpixman-devel libpng-devel ceph-devel
BuildRequires: libsasl2-devel libseccomp-devel libspice-server-devel libssh2-devel libusbredir-devel libxfs-devel
BuildRequires: makeinfo perl-Pod-Usage python-modules-compiler
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
Requires: %name-aux = %version-%release
Conflicts: %rname-img

%description img
This package provides a command line tool for manipulating disk images

%package aux
Summary: QEMU auxiliary package
Group: Emulators
BuildArch: noarch
Conflicts: %rname-aux

%description aux
QEMU is a generic and open source processor emulator which achieves
good emulation speed by using dynamic translation.

This is an auxiliary package.

%set_verify_elf_method fhs=relaxed

%prep
%setup -n %rname-%version
%patch0 -p1

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

%patch100 -p1

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
        --disable-sdl \
        --audio-drv-list="alsa" \
        --enable-bluez  \
        --enable-vnc  \
        --enable-spice  \
        --enable-curl \
        --enable-kvm \
        --enable-tpm  \
        --enable-vhost-net \
        --enable-vhost-scsi  \
        --enable-linux-aio \
        --enable-libusb  \
        --enable-usb-redir \
        --enable-seccomp  \
        --enable-libiscsi  \
        --enable-rbd  \
        --enable-gnutls  \
        --enable-numa  \
        --enable-jemalloc  \
        --enable-pie \
        --enable-xfsctl \
        --enable-virtfs \
        --disable-strip \
        --disable-xen \
        --disable-smartcard \
        --disable-libnfs \
        --disable-glusterfs \
        --disable-libxml2 \
        --disable-guest-agent \
        --disable-guest-agent-msi \
	--disable-rdma

%make_build V=1

sed -i 's/@GROUP@/%_group/g' qemu-kvm.control.in

%install
%makeinstall_std

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
%_datadir/qemu
%_datadir/pve-edk2-firmware
%_sysconfdir/udev/rules.d/%rulenum-%rname-kvm.rules
%_controldir/*
%if_enabled vnc_sasl
%config(noreplace) %_sysconfdir/sasl2/%rname.conf
%endif

%files system -f %rname.lang
%_bindir/qemu
%_bindir/qemu-kvm
%_bindir/kvm
%_bindir/qemu*system*
%_bindir/vma
%_bindir/qemu-pr-helper
%_libexecdir/qemu-bridge-helper

%files img
%_bindir/qemu-img
%_bindir/qemu-io
%_bindir/qemu-nbd
%_bindir/virtfs-proxy-helper

%files aux
%dir %docdir/
%docdir/LICENSE

%changelog
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
