# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%add_verify_elf_skiplist %modules_dir/*

%define flavour			xenomai
Name: kernel-image-%flavour

%define xenomai_version		3.1
%define ipipe_version		4.19.152-cip37-x86-15
%define kernel_base_version	4.19
%define kernel_sublevel		.152
%define kernel_extra_version	%nil
%define kernel_cip_release	cip37
%define kernel_ipipe_release	15

Version: %kernel_base_version%kernel_sublevel%kernel_extra_version
Release: alt1.%kernel_cip_release.%kernel_ipipe_release

# Numeric extra version scheme developed by Alexander Bokovoy:
# 0.0.X -- preX
# 0.X.0 -- rcX
# 1.0.0 -- release
%define kernel_extra_version_numeric 1.0.0

%define krelease	%release

# Build options
# You can change compiler version by editing this line:
%define kgcc_version	%__gcc_version_base

#Remove oss
%def_disable oss
## Don't edit below this line ##################################

%define kversion	%kernel_base_version%kernel_sublevel%kernel_extra_version
%define modules_dir	/lib/modules/%kversion-%flavour-%krelease

%define kheaders_dir	%_prefix/include/linux-%kversion-%flavour
%define kbuild_dir	%_prefix/src/linux-%kversion-%flavour-%krelease

%brp_strip_none /boot/*

Summary: The Linux kernel (I-pipe) %ipipe_version with Xenomai %xenomai_version real-time Cobalt core
License: GPL-2.0-only
Group: System/Kernel and hardware
Url: https://xenomai.org/
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

Patch0: %name-%version-%release.patch

ExclusiveArch: x86_64

ExclusiveOS: Linux

BuildRequires(pre): rpm-build-kernel
BuildRequires: dev86 flex
BuildRequires: libdb4-devel
BuildRequires: gcc%kgcc_version gcc%kgcc_version-c++
BuildRequires: gcc%kgcc_version-plugin-devel libgmp-devel libmpc-devel
BuildRequires: kernel-source-%kernel_base_version = %kernel_extra_version_numeric
BuildRequires: xenomai-kernel-source >= %xenomai_version
BuildRequires: module-init-tools >= 3.16
BuildRequires: lzma-utils
BuildRequires: libelf-devel
BuildRequires: bc
BuildRequires: openssl-devel 
# for check
%{?!_without_check:%{?!_disable_check:BuildRequires: rpm-build-vm-run}}

Requires: bootloader-utils >= 0.4.24-alt1
Requires: module-init-tools >= 3.1
Requires: mkinitrd >= 1:2.9.9-alt1
Requires: startup >= 0.8.3-alt1

Provides: kernel = %kversion

Requires(pre,postun): coreutils
Requires(pre,postun): module-init-tools >= 3.1
Requires(pre,postun): mkinitrd >= 1:2.9.9-alt1

%description
This package contains the Linux kernel %ipipe_version with Xenomai
real-time Cobalt and Interrupt pipeline (I-pipe) patches.

Xenomai brings POSIX and traditional RTOS APIs for porting time-critical
applications to Linux-based platforms. When the native Linux kernel cannot meet
the response time requirements of the application, Xenomai supplements it with
Cobalt, a small real-time infrastructure which schedules time-critical
activities independently from the main kernel logic.

The Cobalt real-time core depends on the Interrupt pipeline (I-pipe) patch to
the mainline Linux kernel, which introduces a separate, high-priority execution
stage for running out-of-band interrupt handlers immediately upon IRQ receipt,
which cannot be delayed by the regular kernel work.

CIP kernels are Super Long Term Service (SLTS) kernels maintained by the Civil
Infrastructure Platform (CIP) Project, which is open source project hosted by
The Linux Foundation.

%package -n kernel-headers-%flavour
Summary: Header files for the Linux kernel %name-%version-%release
Group: Development/Kernel
Requires: kernel-headers-common >= 1.1.5
Provides: kernel-headers = %version
AutoReqProv: nocpp

%description -n kernel-headers-%flavour
This package makes Linux kernel headers corresponding to the Linux
kernel package %name-%version-%release available for building
userspace programs (if this version of headers is selected by
adjust_kernel_headers).

%package -n kernel-headers-modules-%flavour
Summary: Files needed for building modules for Linux kernel %name-%version-%release
Group: Development/Kernel 
Requires: gcc%kgcc_version
Requires: libelf-devel
AutoReqProv: nocpp

%description -n kernel-headers-modules-%flavour
This package contains header files, Makefiles and other parts of the
Linux kernel build system which are needed to build kernel modules for
the Linux kernel package %name-%version-%release.

If you need to compile a third-party kernel module for the Linux
kernel package %name-%version-%release, install this package
and specify %kbuild_dir as the kernel source directory.

%prep
%setup -cT -n kernel-image-%flavour-%kversion-%krelease
rm -rf kernel-source-%kernel_base_version
tar -xf %kernel_src/kernel-source-%kernel_base_version.tar
%setup -D -T -n kernel-image-%flavour-%kversion-%krelease/kernel-source-%kernel_base_version
%patch0 -s -p1

# ALT glibc contains strlcpy, so we need disable it there:
sed -i /strlcpy/d tools/include/linux/string.h

# Undo -cip suffix
rm -f localversion-cip

/usr/src/xenomai-kernel-source/scripts/prepare-kernel.sh --arch=%_arch

# Fix symlinks into regular files to stop autoreq producing per-file
# dependency from kernel-headers-module-xenomai to kernel-source-xenomai.
find -type l -name '*.h' -lname '/usr/src/xenomai-kernel-source/*' -printf '%%l %%p\n' \
  | xargs -n2 cp --remove-destination --

# this file should be usable both with make and sh (for broken modules
# which do not use the kernel makefile system)
echo 'export GCC_VERSION=%kgcc_version' > gcc_version.inc

subst 's/EXTRAVERSION[[:space:]]*=.*/EXTRAVERSION = %kernel_extra_version-%flavour-%krelease/g' Makefile
subst 's/CC.*$(CROSS_COMPILE)gcc/CC         := $(shell echo $${GCC_USE_CCACHE:+ccache}) gcc-%kgcc_version/g' Makefile

# get rid of unwanted files resulting from patch fuzz
find . -name "*.orig" -delete -or -name "*~" -delete

chmod +x tools/objtool/sync-check.sh

%build
export ARCH=%base_arch
export NPROCS=%__nprocs
KernelVer=%kversion-%flavour-%krelease

echo "Building Kernel $KernelVer"

%make_build mrproper

# Configuration construction
%make_build defconfig
scripts/config -e IKCONFIG
scripts/config -e IKCONFIG_PROC

scripts/config -e IPIPE
scripts/config -e XENOMAI

# All options from Xenomai .travis.yml except DEBUG
scripts/config -e XENO_OPT_SCHED_CLASSES
scripts/config -e XENO_OPT_SCHED_WEAK
scripts/config -e XENO_OPT_SCHED_TP
scripts/config -e XENO_OPT_SCHED_SPORADIC
scripts/config -e XENO_OPT_SCHED_QUOTA
scripts/config -e XENO_OPT_SHIRQ
scripts/config -e XENO_OPT_SCALABLE_SCHED
scripts/config -e XENO_OPT_DEBUG
scripts/config -e XENO_OPT_DEBUG_LEGACY
scripts/config -e XENO_DRIVERS_16550A
scripts/config -e XENO_DRIVERS_16550A_ANY
scripts/config -e XENO_DRIVERS_16550A_PCI
scripts/config -e XENO_DRIVERS_16550A_PCI_MOXA
scripts/config -e XENO_DRIVERS_IMX_UART
scripts/config -e XENO_DRIVERS_RTDMTEST
scripts/config -e XENO_DRIVERS_CAN
scripts/config -e XENO_DRIVERS_CAN_LOOPBACK
scripts/config -e XENO_DRIVERS_CAN_VIRT
scripts/config -e XENO_DRIVERS_CAN_FLEXCAN
scripts/config -e XENO_DRIVERS_CAN_SJA1000
scripts/config -e XENO_DRIVERS_CAN_SJA1000_ISA
scripts/config -e XENO_DRIVERS_CAN_SJA1000_MEM
scripts/config -e XENO_DRIVERS_CAN_SJA1000_PEAK_PCI
scripts/config -e XENO_DRIVERS_CAN_SJA1000_IXXAT_PCI
scripts/config -e XENO_DRIVERS_CAN_SJA1000_ADV_PCI
scripts/config -e XENO_DRIVERS_CAN_SJA1000_PLX_PCI
scripts/config -e XENO_DRIVERS_CAN_SJA1000_EMS_PCI
scripts/config -e XENO_DRIVERS_CAN_SJA1000_ESD_PCI
scripts/config -e XENO_DRIVERS_CAN_SJA1000_PEAK_DNG
scripts/config -m XENO_DRIVERS_NET
scripts/config -e XENO_DRIVERS_RTNET_CHECKED
scripts/config -e XENO_DRIVERS_NET_ETH_P_ALL
scripts/config -e XENO_DRIVERS_NET_RTIPV4_NETROUTING
scripts/config -e XENO_DRIVERS_NET_RTIPV4_ROUTER
scripts/config -m XENO_DRIVERS_NET_RTIPV4_TCP
scripts/config -m XENO_DRIVERS_NET_NOMAC
scripts/config -m XENO_DRIVERS_NET_DRV_PCNET32
scripts/config -m XENO_DRIVERS_NET_DRV_TULIP
scripts/config -e XENO_DRIVERS_NET_DRV_EEPRO100_DBG
scripts/config -m XENO_DRIVERS_NET_DRV_E1000E
scripts/config -m XENO_DRIVERS_NET_DRV_NATSEMI
scripts/config -m XENO_DRIVERS_NET_DRV_VIA_RHINE
scripts/config -m XENO_DRIVERS_NET_DRV_IGB
scripts/config -m XENO_DRIVERS_NET_DRV_R8169
scripts/config -m XENO_DRIVERS_NET_DRV_SMC91111
scripts/config -e XENO_DRIVERS_NET_EXP_DRIVERS
scripts/config -m XENO_DRIVERS_NET_DRV_3C59X
scripts/config -m XENO_DRIVERS_NET_DRV_E1000_NEW
scripts/config -m XENO_DRIVERS_NET_DRV_RT2500
scripts/config -m XENO_DRIVERS_NET_ADDON_RTCAP
scripts/config -m XENO_DRIVERS_NET_ADDON_PROXY
scripts/config -e XENO_DRIVERS_NET_ADDON_PROXY_ARP
scripts/config -e XENO_DRIVERS_ANALOGY
scripts/config -e XENO_DRIVERS_ANALOGY_FAKE
scripts/config -e XENO_DRIVERS_ANALOGY_NI_PCIMIO
scripts/config -e XENO_DRIVERS_ANALOGY_S526
scripts/config -e XENO_DRIVERS_RTIPC
scripts/config -e XENO_DRIVERS_UDD
scripts/config -e XENO_DRIVERS_GPIO
scripts/config -e XENO_DRIVERS_GPIO_BCM2835
scripts/config -e XENO_DRIVERS_GPIO_MXC
scripts/config -e XENO_DRIVERS_GPIO_SUN8I_H3
scripts/config -e XENO_DRIVERS_GPIO_ZYNQ7000
scripts/config -e XENO_DRIVERS_GPIO_XILINX
scripts/config -e XENO_DRIVERS_GPIOPWM
scripts/config -e XENO_DRIVERS_SPI_BCM2835
scripts/config -e XENO_DRIVERS_SPI_SUN6I

# Enable EFI handover support
scripts/config -e EFI
scripts/config -e EFI_STUB

scripts/config -m ISO9660_FS
scripts/config -m UDF_FS
scripts/config -m VFAT_FS

# For test SM box
scripts/config -m IGB
scripts/config -m DRM_AST
scripts/config -m I2C_PIIX4
scripts/config -m SENSORS_K10TEMP
scripts/config -m DRM_RADEON
scripts/config -m FB_RADEON
scripts/config -m USB_XHCI_HCD
scripts/config -m SCSI_DH
scripts/config -m SCSI_DH_EMC
scripts/config -m SCSI_DH_RDAC
scripts/config -m SCSI_DH_ALUA

scripts/config -m IPMI_SI
scripts/config -m IPMI_DEVICE_INTERFACE
scripts/config -m IPMI_HANDLER
scripts/config -m IPMI_SSIF
scripts/config -m IPMI_WATCHDOG

# For livecd
scripts/config -e CONFIG_USER_NS
scripts/config -e CONFIG_SQUASHFS -e CONFIG_SQUASHFS_XZ
# For qemu & vm-run
scripts/config -e CONFIG_SCSI_VIRTIO -e CONFIG_SCSI_LOWLEVEL -m CONFIG_VIRTIO_PCI \
	       -e CONFIG_VIRTIO_BLK -e CONFIG_VIRTIO_NET -e CONFIG_VIRTIO_CONSOLE \
	       -e CONFIG_HW_RANDOM_VIRTIO -e CONFIG_VIRTIO_BALLOON \
	       -m CONFIG_NET_9P -m CONFIG_NET_9P_VIRTIO -m CONFIG_9P_FS \
	       -e CONFIG_CONFIGFS_FS

scripts/config -e CONFIG_DEBUG_INFO

# Disable what is recommended in
# https://gitlab.denx.de/Xenomai/xenomai/wikis/Configuring_For_X86_Based_Dual_Kernels
scripts/config -d CONFIG_CPU_FREQ
scripts/config -d CONFIG_CPU_IDLE
scripts/config -d CONFIG_APM
scripts/config -d CONFIG_ACPI_PROCESSOR -d X86_INTEL_PSTATE -d SCHED_MC_PRIO
scripts/config -d CONFIG_INTEL_IDLE
scripts/config -d CONFIG_INPUT_PCSPKR

scripts/config -m NLS_CODEPAGE_866
scripts/config -e I2C_CHARDEV
scripts/config -m DRM
scripts/config -m DRM_AMDGPU
scripts/config -e X86_AMD_PLATFORM_DEVICE
scripts/config -m PINCTRL_AMD
scripts/config -e GPIOLIB
scripts/config -e GPIO_ACPI
scripts/config -e GPIOLIB_IRQCHIP
scripts/config -e GPIO_SYSFS
scripts/config -d CONFIG_SERIAL_8250_EXAR
scripts/config -d CONFIG_GPIO_EXAR

%make_build olddefconfig
egrep 'IPIPE|XENO' .config

# Verify that bad options are still disabled
grep -w -e ^CONFIG_CPU_FREQ \
	-e ^CONFIG_CPU_IDLE \
	-e ^CONFIG_APM \
	-e ^CONFIG_ACPI_PROCESSOR \
	-e ^CONFIG_INTEL_IDLE \
	-e ^CONFIG_INPUT_PCSPKR .config && exit 1

%make_build bzImage
%make_build modules

%install
export ARCH=%base_arch
KernelVer=%kversion-%flavour-%krelease

install -Dp -m644 System.map %buildroot/boot/System.map-$KernelVer
install -Dp -m644 arch/%base_arch/boot/bzImage \
	%buildroot/boot/vmlinuz-$KernelVer
install -Dp -m644 .config %buildroot/boot/config-$KernelVer

make modules_install INSTALL_MOD_PATH=%buildroot

#
# Install kernel-headers-modules
#
mkdir -p %buildroot%kbuild_dir/arch/x86
cp -a include			   %buildroot%kbuild_dir/include
cp -a arch/x86/include		   %buildroot%kbuild_dir/arch/x86
cp -a arch/x86/xenomai/include/asm %buildroot%kbuild_dir/include/xenomai/asm

# drivers-headers install
install -d %buildroot%kbuild_dir/drivers/scsi
install -d %buildroot%kbuild_dir/drivers/md
install -d %buildroot%kbuild_dir/drivers/usb/core
install -d %buildroot%kbuild_dir/drivers/net/wireless
install -d %buildroot%kbuild_dir/net/mac80211
install -d %buildroot%kbuild_dir/kernel
install -d %buildroot%kbuild_dir/lib
cp -a drivers/scsi/scsi.h	 %buildroot%kbuild_dir/drivers/scsi/
cp -a drivers/md/dm*.h		 %buildroot%kbuild_dir/drivers/md/
cp -a drivers/usb/core/*.h	 %buildroot%kbuild_dir/drivers/usb/core/
cp -a lib/hexdump.c		 %buildroot%kbuild_dir/lib/
cp -a kernel/workqueue.c	 %buildroot%kbuild_dir/kernel/
cp -a net/mac80211/ieee80211_i.h %buildroot%kbuild_dir/net/mac80211/
cp -a net/mac80211/sta_info.h	 %buildroot%kbuild_dir/net/mac80211/

# Install files required for building external modules (in addition to headers)
KbuildFiles="
	Makefile
	Module.symvers
	arch/%base_arch/Makefile
%ifarch x86_64
	arch/x86/Makefile
	arch/x86/Makefile_32
	arch/x86/Makefile_32.cpu
	arch/x86/Makefile_64
%endif
	scripts/pnmtologo
	scripts/mod/modpost
	scripts/mkmakefile
	scripts/mkversion
	scripts/link-vmlinux.sh
	scripts/mod/mk_elfconfig
	scripts/kconfig/conf
	scripts/mkcompile_h
	scripts/makelst
	scripts/Makefile.*
	scripts/Makefile
	scripts/Kbuild.include
	scripts/kallsyms
	scripts/genksyms/genksyms
	scripts/basic/fixdep
	scripts/basic/hash
	scripts/extract-ikconfig
	scripts/conmakehash
	scripts/checkversion.pl
	scripts/checkincludes.pl
	scripts/checkconfig.pl
	scripts/bin2c
	scripts/gcc-version.sh
	scripts/gcc-goto.sh
	scripts/recordmcount.pl
	scripts/recordmcount.h
	scripts/recordmcount.c
	scripts/recordmcount
	scripts/gcc-x86_*-has-stack-protector.sh
	scripts/module-common.lds
	scripts/subarch.include
	scripts/depmod.sh
	scripts/gcc-plugins/*.so
	scripts/ld-version.sh
	tools/objtool/objtool

	.config
	.kernelrelease
	gcc_version.inc
	System.map
"
for f in $KbuildFiles; do
	[ -e "$f" ] || continue
	[ -x "$f" ] && mode=755 || mode=644
	install -Dp -m$mode "$f" %buildroot%kbuild_dir/"$f"
done

# Fix symlinks to kernel sources in /lib/modules
rm -f %buildroot%modules_dir/{build,source}
ln -s %kbuild_dir %buildroot%modules_dir/build

# Provide kernel headers for userspace
make headers_install INSTALL_HDR_PATH=%buildroot%kheaders_dir

find %buildroot%kheaders_dir -name ..install.cmd -delete

#provide symlink to autoconf.h for back compat
pushd %buildroot%kbuild_dir/include/linux
ln -s ../generated/autoconf.h
ln -s ../generated/utsrelease.h
ln -s ../generated/uapi/linux/version.h
popd

# For external modules.
mkdir -p %buildroot%modules_dir/extra

%check
vm-run "set -x
  head /proc/ipipe/version /proc/xenomai/version
  dmesg | grep -i -e 'I-pipe' -e 'Xenomai'
  dmesg | grep 'head domain Xenomai registered'
  dmesg | grep 'Cobalt v[0-9.]'
  ! dmesg | grep 'init failed'
  set +x"

%files
/boot/vmlinuz-%kversion-%flavour-%krelease
/boot/System.map-%kversion-%flavour-%krelease
/boot/config-%kversion-%flavour-%krelease
%modules_dir
%exclude %modules_dir/build

%files -n kernel-headers-%flavour
%kheaders_dir

%files -n kernel-headers-modules-%flavour
%kbuild_dir
%dir %modules_dir
%modules_dir/build

%changelog
* Thu Nov 12 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.152-alt1.cip37.15
- Update to ipipe-core-4.19.152-cip37-x86-15 (released 2020-11-09)

* Sat Sep 26 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.140-alt2.cip33.14
- Fix depmod (modules.*) indices packaging.

* Thu Sep 24 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.140-alt1.cip33.14
- Update to ipipe-core-4.19.140-cip33-x86-14 (2020-09-11).
- Config changes.
- spec: Use vm-run to boot test.

* Mon Jun 15 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.124-alt1.cip27.13
- Update to ipipe-core-4.19.124-cip27-x86-13.

* Sun Apr 19 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.114-alt1.cip24.12
- Major upgrade of xenomai kernels to Linux 4.19 branch and update to
  ipipe-core-4.19.114-cip24-x86-12 released at 2020-04-16.
- Xenomai patches are upgraded from 3.0 to 3.1 branch. Note that with this
  release Xenomai ABI Revision Level is changed from r16 to r17.

* Fri Nov 29 2019 Vitaly Chikunov <vt@altlinux.org> 4.14.134-alt3
- Enable kdb/kgdb/lkdtm on x86.

* Sun Nov 24 2019 Vitaly Chikunov <vt@altlinux.org> 4.14.134-alt2
- Actually disable ACPI_PROCESSOR, CPU_FREQ, and CPU_IDLE
- Add more options based on -rt kernel experience.
- Enable virtio for debugging.
- Fix license tag and other minor spec changes.

* Sat Aug 24 2019 Vitaly Chikunov <vt@altlinux.org> 4.14.134-alt1
- Update to ipipe-core-4.14.134-x86-8.
- Fix qemu run.

* Fri Jun 28 2019 Vitaly Chikunov <vt@altlinux.org> 4.14.128-alt4
- Clean up ..install.cmd files (reported by repocop).

* Wed Jun 26 2019 Vitaly Chikunov <vt@altlinux.org> 4.14.128-alt3
- Add filesystems required for fstab to finish system boot

* Tue Jun 25 2019 Vitaly Chikunov <vt@altlinux.org> 4.14.128-alt2
- Enable EFI handover support
- Enable igb and some other drivers useful for SM

* Fri Jun 21 2019 Vitaly Chikunov <vt@altlinux.org> 4.14.128-alt1
- v4.14.128 with spec based on kernel-image-std-def-4.14.104-alt1
- I-pipe 4.14.128 with Xenomai Cobalt
