%define kernel_base_version	4.9
%define kernel_sublevel        .140
%define kernel_extra_version	%nil

Name: kernel-image-tegra
Version: %kernel_base_version%kernel_sublevel%kernel_extra_version
Release: alt2

%define kernel_extra_version_numeric 1.0.0

%define krelease	%release

%define flavour		%( s='%name'; printf %%s "${s#kernel-image-}" )
%define base_flavour	%( s='%flavour'; printf %%s "${s%%%%-*}" )
%define sub_flavour	%( s='%flavour'; printf %%s "${s#*-}" )

# Build options
# You can change compiler version by editing this line:
%define kgcc_version	8

## Don't edit below this line ##################################

%define kversion	%kernel_base_version%kernel_sublevel%kernel_extra_version
%define modules_dir	/lib/modules/%kversion-%flavour-%krelease

%define kheaders_dir	%_prefix/include/linux-%kversion-%flavour
%define kbuild_dir	%_prefix/src/linux-%kversion-%flavour-%krelease
%define old_kbuild_dir	%_prefix/src/linux-%kversion-%flavour

%brp_strip_none /boot/*

Summary: The Linux kernel (the core of the Linux operating system)
License: GPL
Group: System/Kernel and hardware
Url: http://www.kernel.org/

Source1: kernel-nvidia-4.9.tar
Patch0: %name-%version.patch
Patch1: %name-%version-gcc-werror.patch
Patch2: kernel-image-tegra-config.patch

Patch10: 0001-Bluetooth-hidp-fix-buffer-overflow.patch
Patch11: 0001-can-gw-ensure-DLC-boundaries-after-CAN-frame-modific.patch
Patch12: 0001-ext4-zero-out-the-unused-memory-region-in-the-extent.patch
Patch13: 0001-HID-debug-fix-the-ring-buffer-implementation.patch
Patch14: 0001-kvm-fix-kvm_ioctl_create_device-reference-counting-C.patch
Patch15: 0001-KVM-x86-work-around-leak-of-uninitialized-stack-cont.patch
Patch16: 0001-tcp-enforce-tcp_min_snd_mss-in-tcp_mtu_probing.patch
Patch17: 0001-tcp-limit-payload-size-of-sacked-skbs.patch
Patch19: 0002-KVM-nVMX-unconditionally-cancel-preemption-timer-in-.patch
Patch20: 0002-tcp-tcp_fragment-should-apply-sane-memory-limits.patch
Patch22: 0003-tcp-add-tcp_min_snd_mss-sysctl.patch

ExclusiveArch: aarch64

ExclusiveOS: Linux

BuildRequires(pre): rpm-build-kernel
BuildRequires: bc flex lzma-utils
BuildRequires: libdb4-devel
BuildRequires: gcc%kgcc_version
BuildRequires: kernel-source-%kernel_base_version = %kernel_extra_version_numeric
BuildRequires: libssl-devel xxd

%if_enabled ccache
BuildRequires: ccache
%endif

%ifdef use_ccache
BuildRequires: ccache
%endif

Requires: bootloader-utils >= 0.5.2-alt3
Provides: kernel = %kversion

%define Image Image

%description
This package contains the Linux kernel that is used to boot and run
your system and supports most recent arm machines.

%package -n kernel-headers-%flavour
Summary: Header files for the Linux kernel
Group: Development/Kernel
Requires: kernel-headers-common >= 1.1.5
Provides: kernel-headers = %version

%description -n kernel-headers-%flavour
This package makes Linux kernel headers corresponding to the Linux
kernel package %name-%version-%release available for building
userspace programs (if this version of headers is selected by
adjust_kernel_headers).

Since Linux 2.6.18 the kernel build system supports creation of
sanitized kernel headers for use in userspace (by deleting headers
which are not usable in userspace and removing #ifdef __KERNEL__
blocks from installed headers).  This package contains sanitized
headers instead of raw kernel headers which were present in some
previous versions of similar packages.

If possible, try to use glibc-kernheaders instead of this package.

%package -n kernel-headers-modules-%flavour
Summary: Headers and other files needed for building kernel modules
Group: Development/Kernel
Requires: gcc%kgcc_version

%description -n kernel-headers-modules-%flavour
This package contains header files, Makefiles and other parts of the
Linux kernel build system which are needed to build kernel modules for
the Linux kernel package %name-%version-%release.

If you need to compile a third-party kernel module for the Linux
kernel package %name-%version-%release, install this package
and specify %kbuild_dir as the kernel source
directory.

%prep
%setup -cT -n kernel-image-%flavour-%kversion-%krelease -a1
rm -rf kernel-source-%kernel_base_version
tar -xf %kernel_src/kernel-source-%kernel_base_version.tar
%setup -D -T -n kernel-image-%flavour-%kversion-%krelease/kernel-source-%kernel_base_version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch19 -p1
%patch20 -p1
%patch22 -p1

# this file should be usable both with make and sh (for broken modules
# which do not use the kernel makefile system)
echo 'export GCC_VERSION=%kgcc_version' > gcc_version.inc

subst 's/EXTRAVERSION[[:space:]]*=.*/EXTRAVERSION = %kernel_extra_version-%flavour-%krelease/g' Makefile
subst 's/CC.*$(CROSS_COMPILE)gcc/CC         := $(shell echo $${GCC_USE_CCACHE:+ccache}) gcc-%kgcc_version/g' Makefile

# get rid of unwanted files resulting from patch fuzz
find . -name "*.orig" -delete -or -name "*~" -delete

%build
export ARCH=%base_arch
KernelVer=%kversion-%flavour-%krelease

echo "Building Kernel $KernelVer"

%make_build mrproper

cp -vf config-%_target_cpu .config

%make_build oldconfig
%make_build %Image modules

%install
export ARCH=%base_arch
KernelVer=%kversion-%flavour-%krelease

install -Dp -m644 System.map %buildroot/boot/System.map-$KernelVer
install -Dp -m644 arch/%base_arch/boot/%Image %buildroot/boot/vmlinuz-$KernelVer
install -Dp -m644 .config %buildroot/boot/config-$KernelVer
make modules_install INSTALL_MOD_PATH=%buildroot

mkdir -p %buildroot/lib/devicetree/$KernelVer
#find arch/%base_arch/boot/dts -type f -name \*.dtb |xargs -iz install -pm0644 z %buildroot/lib/devicetree/$KernelVer

mkdir -p %buildroot%kbuild_dir/arch/%base_arch
cp -a include %buildroot%kbuild_dir/include
cp -a arch/%base_arch/include %buildroot%kbuild_dir/arch/%base_arch

# drivers-headers install
install -d %buildroot%kbuild_dir/drivers/md
install -d %buildroot%kbuild_dir/drivers/usb/core
install -d %buildroot%kbuild_dir/drivers/net/wireless
install -d %buildroot%kbuild_dir/net/mac80211
install -d %buildroot%kbuild_dir/kernel
install -d %buildroot%kbuild_dir/lib
cp -a drivers/md/dm*.h \
	%buildroot%kbuild_dir/drivers/md/
cp -a drivers/usb/core/*.h \
	%buildroot%kbuild_dir/drivers/usb/core/
cp -a drivers/net/wireless/Kconfig \
	%buildroot%kbuild_dir/drivers/net/wireless/
cp -a lib/hexdump.c %buildroot%kbuild_dir/lib/
cp -a kernel/workqueue.c %buildroot%kbuild_dir/kernel/
cp -a net/mac80211/ieee80211_i.h \
	%buildroot%kbuild_dir/net/mac80211/
cp -a net/mac80211/sta_info.h \
	%buildroot%kbuild_dir/net/mac80211/

# Install files required for building external modules (in addition to headers)
KbuildFiles="
	Makefile
	Module.symvers
	arch/%base_arch/Makefile
	scripts/pnmtologo
	scripts/mod/modpost
	scripts/mkmakefile
	scripts/mkversion
	scripts/mod/mk_elfconfig
	scripts/kconfig/conf
	scripts/mkcompile_h
	scripts/makelst
	scripts/Makefile.modpost
	scripts/Makefile.modinst
	scripts/Makefile.lib
	scripts/Makefile.host
	scripts/Makefile.clean
	scripts/Makefile.build
	scripts/Makefile.extrawarn
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
	scripts/recordmcount.pl
	scripts/gcc-version.sh
	scripts/gcc-goto.sh
	scripts/module-common.lds
	scripts/depmod.sh
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

# Provide kbuild directory with old name (without %%krelease)
ln -s "$(relative %kbuild_dir %old_kbuild_dir)" %buildroot%old_kbuild_dir

# Provide kernel headers for userspace
make headers_install INSTALL_HDR_PATH=%buildroot%kheaders_dir

# remove *.bin files
rm -f %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin
touch %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin
touch %buildroot%modules_dir/modules.{alias,dep,devname,softdep,symbols}

%set_verify_elf_method none

%files
/boot/vmlinuz-%kversion-%flavour-%krelease
/boot/System.map-%kversion-%flavour-%krelease
/boot/config-%kversion-%flavour-%krelease
/lib/devicetree/%kversion-%flavour-%krelease
%modules_dir/kernel
%ghost %modules_dir/modules.alias
%ghost %modules_dir/modules.dep
%ghost %modules_dir/modules.devname
%modules_dir/modules.order
%ghost %modules_dir/modules.softdep
%ghost %modules_dir/modules.symbols
%modules_dir/modules.builtin
%ghost %modules_dir/modules.alias.bin
%ghost %modules_dir/modules.dep.bin
%ghost %modules_dir/modules.symbols.bin
%ghost %modules_dir/modules.builtin.bin

%files -n kernel-headers-%flavour
%kheaders_dir

%files -n kernel-headers-modules-%flavour
%kbuild_dir
%old_kbuild_dir
%dir %modules_dir
%modules_dir/build

%changelog
* Tue Jun 18 2019 Valery Inozemtsev <shrek@altlinux.ru> 4.9.140-alt2
- fixed CVE-2019-11478, CVE-2019-11477, CVE-2019-11833, CVE-2019-3882, CVE-2019-3819, CVE-2019-7222, CVE-2019-3701, CVE-2018-19985

* Mon Jun 03 2019 Valery Inozemtsev <shrek@altlinux.ru> 4.9.140-alt1
- initial build for Jetson Nano

