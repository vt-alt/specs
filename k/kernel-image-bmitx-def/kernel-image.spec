%define kernel_base_version	4.9
%define kernel_sublevel        .227
%define kernel_extra_version	%nil

Name: kernel-image-bmitx-def
Version: %kernel_base_version%kernel_sublevel%kernel_extra_version
Release: alt1

%define kernel_extra_version_numeric 1.0.0

%define krelease	%release

%define flavour		%( s='%name'; printf %%s "${s#kernel-image-}" )
%define base_flavour	%( s='%flavour'; printf %%s "${s%%%%-*}" )
%define sub_flavour	%( s='%flavour'; printf %%s "${s#*-}" )

# Build options
# You can change compiler version by editing this line:
%define kgcc_version	7

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

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

ExclusiveArch: aarch64

ExclusiveOS: Linux

BuildRequires(pre): rpm-build-kernel
BuildRequires: bc flex kmod lzma-utils
BuildRequires: libdb4-devel
BuildRequires: gcc%kgcc_version
BuildRequires: libssl-devel

%if_enabled ccache
BuildRequires: ccache
%endif

%ifdef use_ccache
BuildRequires: ccache
%endif

Requires: bootloader-utils >= 0.5.2-alt3
Provides: kernel = %kversion

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
%setup
%patch0 -p1

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
%make_build Image modules dtbs

%install
export ARCH=%base_arch
KernelVer=%kversion-%flavour-%krelease

install -Dp -m644 System.map %buildroot/boot/System.map-$KernelVer
install -Dp -m644 arch/%base_arch/boot/Image %buildroot/boot/vmlinuz-$KernelVer
install -Dp -m644 .config %buildroot/boot/config-$KernelVer
make modules_install INSTALL_MOD_PATH=%buildroot

mkdir -p %buildroot/lib/devicetree/$KernelVer
find arch/%base_arch/boot/dts -type f -name \*.dtb |xargs -iz install -pm0644 z %buildroot/lib/devicetree/$KernelVer

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

%set_verify_elf_method none

%files
/boot/vmlinuz-%kversion-%flavour-%krelease
/boot/System.map-%kversion-%flavour-%krelease
/boot/config-%kversion-%flavour-%krelease
/lib/devicetree/%kversion-%flavour-%krelease
%modules_dir
%exclude %modules_dir/build
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

%post
rm -f /boot/dtb
ln -s /lib/devicetree/%kversion-%flavour-%krelease /boot/dtb

%changelog
* Mon Jun 15 2020 Alexey Sheplyakov <asheplyakov@altlinux.org> 4.9.227-alt1
- Merged with the latest linux-stable/v4.9.227
- Enabled more WiFi drivers

* Sat May 23 2020 Alexey Sheplyakov <asheplyakov@altlinux.org> 4.9.216-alt2
- Fixed monitor wakeup from the idle state and switching between virtual
  consoles. Mali drivers still breaks power management.

* Mon Apr 13 2020 Alexey Sheplyakov <asheplyakov@altlinux.org> 4.9.216-alt1
- Updates from Baikal SDK-M-4.2
  WARNING: the kernel depends on firmware from the same version of SDK.
- Merged with linux-stable v4.9.216
- Build preemptible kernel
- Enabled more drivers (GPUs, web cameras, virtio, HD audio, etc)

* Sun Apr 12 2020 Alexey Sheplyakov <asheplyakov@altlinux.org> 4.9.208-alt3
- Merged with linux-stable v4.9.208 to make tracking changes (by Baikal
  Electronics) easier

* Tue Mar 03 2020 Dmitry Terekhin <jqt4@altlinux.org> 4.9.208-alt2
- build the module mali_kbase.ko
- this is kernel part for graphical acceleration on Mali T628

* Mon Feb 17 2020 Dmitry Terekhin <jqt4@altlinux.org> 4.9.208-alt1
- updated from https://share.baikalelectronics.ru/index.php/s/FPrYNPEAebKzCLC

* Tue Feb 11 2020 Dmitry Terekhin <jqt4@altlinux.org> 4.9.205-alt1
- updated from SDK-M-4.1

* Tue Oct 22 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.9.190-alt1
- initial

