%define kernel_base_version	4.4
%define kernel_sublevel 	.189
%define kernel_extra_version	.9

Name: kernel-image-mcom02
Version: %kernel_base_version%kernel_sublevel%kernel_extra_version
Release: alt7

Provides: kernel-modules-dm-secdel-mcom02 = %version-%release

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

Patch0: mainline-%version.patch
Patch1: mcom-%version.patch

ExclusiveArch: armh

ExclusiveOS: Linux

BuildRequires(pre): rpm-build-kernel
BuildRequires: bc flex kmod lzma-utils
BuildRequires: libdb4-devel
BuildRequires: gcc%kgcc_version
BuildRequires: kernel-source-%kernel_base_version = %kernel_extra_version_numeric

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
your system and supports ELVEES MCom-02 SoC.

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
%setup -cT -n kernel-image-%flavour-%kversion-%krelease
rm -rf kernel-source-%kernel_base_version
tar -xf %kernel_src/kernel-source-%kernel_base_version.tar
%setup -D -T -n kernel-image-%flavour-%kversion-%krelease/kernel-source-%kernel_base_version
%patch0 -p1
%patch1 -p1

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
%make_build zImage modules

%install
export ARCH=%base_arch
KernelVer=%kversion-%flavour-%krelease

install -Dp -m644 System.map %buildroot/boot/System.map-$KernelVer
install -Dp -m644 arch/%base_arch/boot/zImage %buildroot/boot/vmlinuz-$KernelVer
install -Dp -m644 .config %buildroot/boot/config-$KernelVer
make modules_install INSTALL_MOD_PATH=%buildroot INSTALL_FW_PATH=%buildroot/lib/firmware/$KernelVer

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
	arch/%base_arch/kernel/module.lds
	scripts/Kbuild.include
	scripts/Makefile
	scripts/Makefile.*
	scripts/basic/fixdep
	scripts/basic/hash
	scripts/bin2c
	scripts/checkconfig.pl
	scripts/checkincludes.pl
	scripts/checkversion.pl
	scripts/conmakehash
	scripts/depmod.sh
	scripts/extract-ikconfig
	scripts/gcc-goto.sh
	scripts/gcc-plugins/*.so
	scripts/gcc-version.sh
	scripts/genksyms/genksyms
	scripts/kallsyms
	scripts/kconfig/conf
	scripts/ld-version.sh
	scripts/link-vmlinux.sh
	scripts/makelst
	scripts/mkcompile_h
	scripts/mkmakefile
	scripts/mkversion
	scripts/mod/mk_elfconfig
	scripts/mod/modpost
	scripts/module-common.lds
	scripts/pnmtologo
	scripts/recordmcount
	scripts/recordmcount.c
	scripts/recordmcount.h
	scripts/recordmcount.pl
	scripts/subarch.include
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

# Provide kbuild directory with old name (without %%krelease)
ln -s "$(relative %kbuild_dir %old_kbuild_dir)" %buildroot%old_kbuild_dir

# Provide kernel headers for userspace
make headers_install INSTALL_HDR_PATH=%buildroot%kheaders_dir

# remove *.bin files
rm -f %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin
touch %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin

%set_verify_elf_method none
%add_debuginfo_skiplist /boot %modules_dir

%files
/boot/vmlinuz-%kversion-%flavour-%krelease
/boot/System.map-%kversion-%flavour-%krelease
/boot/config-%kversion-%flavour-%krelease
/lib/firmware/%kversion-%flavour-%krelease
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

%changelog
* Tue Nov 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.189.9-alt7
- CONFIG_CRYPTO_CRC32C=m

* Mon Nov 16 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.189.9-alt6
- fix netlabel userspace compatibility issue

* Wed Oct 28 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.189.9-alt5
- LiME 1.9.1
- nDPI 2.6

* Wed Oct 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.189.9-alt4
- rebuilt with AUDITSYSCALL=y

* Tue Oct 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.189.9-alt3
- netlabel: skip marking packets from s0

* Wed Oct 07 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.189.9-alt2
- rebuilt with SECURITY_SELINUX_DEVELOP=y

* Mon Sep 28 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.189.9-alt1
- Update for release v4.4.189.9

* Thu Jul 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.189.1-alt1
- Update for release v4.4.189.1

* Sat Jun 29 2019 RnD Center ELVEES <rnd_elvees@altlinux.org> 4.4.178.2-alt1
- Update for release v4.4.178.2

* Mon Dec 10 2018 RnD Center ELVEES <rnd_elvees@altlinux.org> 4.4.111.8-alt1
- Update for release v4.4.111.8

* Mon Apr 16 2018 Dmitriy Zagrebin <dzagrebin@altlinux.org> 4.4.111.3-alt1
- Initial build for ALT
