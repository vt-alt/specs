Name: kernel-image-un-def
Release: alt1
epoch:1 
%define kernel_base_version	5.2
%define kernel_sublevel .9
%define kernel_extra_version	%nil
Version: %kernel_base_version%kernel_sublevel%kernel_extra_version
# Numeric extra version scheme developed by Alexander Bokovoy:
# 0.0.X -- preX
# 0.X.0 -- rcX
# 1.0.0 -- release
%define kernel_extra_version_numeric 1.0.0

%define krelease	%release

%define flavour		%( s='%name'; printf %%s "${s#kernel-image-}" )
%define base_flavour	%( s='%flavour'; printf %%s "${s%%%%-*}" )
%define sub_flavour	%( s='%flavour'; printf %%s "${s#*-}" )

# Build options
# You can change compiler version by editing this line:
%define kgcc_version	%__gcc_version_base

# Enable/disable SGML docs formatting
%if "%sub_flavour" == "def" && %kgcc_version > 5
%def_enable docs
%else
%def_disable docs
%endif

%ifarch %ix86 x86_64
%def_enable domU
%else
%def_disable domU
%endif

#Remove oss
%def_disable oss
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
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

Patch0: %name-%version-%release.patch

%if "%sub_flavour" == "pae"
ExclusiveArch: i586
%else
ExclusiveArch: i586 x86_64 ppc64le
%endif

%define make_target bzImage
%ifarch ppc64le
%define make_target vmlinux
%endif

%define image_path arch/%base_arch/boot/%make_target
%ifarch ppc64le
%define image_path %make_target
%endif

%define kvm_modules_dir arch/x86/kvm
%ifarch ppc64le
%define kvm_modules_dir arch/powerpc/kvm
%endif

%define qemu_pkg %_arch
%ifarch %ix86 x86_64
%define qemu_pkg x86
%endif
%ifarch ppc64le
%define qemu_pkg ppc
%endif

ExclusiveOS: Linux

BuildRequires(pre): rpm-build-kernel
%ifarch %ix86 x86_64
BuildRequires: dev86
%endif
BuildRequires: flex
BuildRequires: libdb4-devel
BuildRequires: gcc%kgcc_version gcc%kgcc_version-c++
BuildRequires: gcc%kgcc_version-plugin-devel libgmp-devel libmpc-devel
BuildRequires: kernel-source-%kernel_base_version = %kernel_extra_version_numeric
BuildRequires: module-init-tools >= 3.16
BuildRequires: lzma-utils
BuildRequires: libelf-devel
BuildRequires: bc
BuildRequires: openssl-devel 
# for check
%{?!_without_check:%{?!_disable_check:BuildRequires: qemu-system-%qemu_pkg-core glibc-devel-static}}
Provides: kernel-modules-eeepc-%flavour = %version-%release
Provides: kernel-modules-drbd83-%flavour = %version-%release
Provides: kernel-modules-igb-%flavour = %version-%release
Provides:  kernel-modules-alsa = %version-%release


%if_enabled docs
BuildRequires: python-module-sphinx perl-Pod-Usage 
%endif

%if_enabled ccache
BuildRequires: ccache
%endif

%ifdef use_ccache
BuildRequires: ccache
%endif

Requires: bootloader-utils >= 0.4.24-alt1
Requires: module-init-tools >= 3.1
Requires: mkinitrd >= 1:2.9.9-alt1
Requires: startup >= 0.8.3-alt1

Provides: kernel = %kversion

Prereq: coreutils
Prereq: module-init-tools >= 3.1
Prereq: mkinitrd >= 1:2.9.9-alt1

%description
This package contains the Linux kernel that is used to boot and run
your system.

Most hardware drivers for this kernel are built as modules.  Some of
these drivers are built separately from the kernel; they are available
in separate packages (kernel-modules-*-%flavour).

There are some kernel variants in ALT systems:
* std-def: standard longterm kernel without preemption;
* std-pae: variant of std-def kernel for i686 with 64G memory support;
* std-debug: variant of std-def kernel kernel with some DEBUG options enabled;
* un-def: more modern then std-def and with voluntary (on ppc64le) and
  forced (on x86) preemption enabled.

%package -n kernel-image-domU-%flavour
Summary: Uncompressed linux kernel for XEN domU boot 
Group: System/Kernel and hardware
Prereq: coreutils
Prereq: module-init-tools >= 3.1

%description -n kernel-image-domU-%flavour
Most XEN virtualization system versions can not boot lzma-compressed
kernel images. This is an optional package with uncompressed linux
kernel image for this special case. If you do not know what is it XEN
it seems that you do not need this package.


%package -n kernel-modules-drm-%flavour
Summary: The Direct Rendering Infrastructure modules
Group: System/Kernel and hardware
Provides:  kernel-modules-drm-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-drm-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-drm-%kversion-%flavour-%krelease > %version-%release
Prereq: coreutils
Prereq: module-init-tools >= 3.1
Prereq: %name = %epoch:%version-%release
Requires(postun): %name = %epoch:%version-%release

%description -n kernel-modules-drm-%flavour
The Direct Rendering Infrastructure, also known as the DRI, is a framework
for allowing direct access to graphics hardware in a safe and efficient
manner.  It includes changes to the X server, to several client libraries,
and to the kernel.  The first major use for the DRI is to create fast
OpenGL implementations.

These are modules for your ALT Linux system

%package -n kernel-modules-drm-ancient-%flavour
Summary: The Direct Rendering modules for ancient cards
Group: System/Kernel and hardware
Provides:  kernel-modules-drm-ancient-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-drm-ancient-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-drm-ancient-%kversion-%flavour-%krelease > %version-%release
Prereq: coreutils
Prereq: %name = %epoch:%version-%release
Requires(postun): %name = %epoch:%version-%release

%description -n kernel-modules-drm-ancient-%flavour
The Direct Rendering Modules for ancient cards: mgag200.ko,
sis.ko, tdfx.ko, savage.ko, r128.ko, mga.ko, via.ko

These are modules for your ALT Linux system

%package -n kernel-modules-drm-nouveau-%flavour
Summary: The Direct Rendering Infrastructure modules for NVIDIA cards
Group: System/Kernel and hardware
Provides:  kernel-modules-drm-nouveau-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-drm-nouveau-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-drm-nouveau-%kversion-%flavour-%krelease > %version-%release
Requires: kernel-modules-drm-%kversion-%flavour-%krelease = %version-%release
Prereq: coreutils
Prereq: module-init-tools >= 3.1
Prereq: %name = %epoch:%version-%release
Requires(postun): %name = %epoch:%version-%release

%description -n kernel-modules-drm-nouveau-%flavour
The Direct Rendering Infrastructure, also known as the DRI, is a framework
for allowing direct access to graphics hardware in a safe and efficient
manner.  It includes changes to the X server, to several client libraries,
and to the kernel.  The first major use for the DRI is to create fast
OpenGL implementations.

These are modules for your ALT Linux system

%package -n kernel-modules-drm-radeon-%flavour
Summary: The Direct Rendering Infrastructure modules for ATI cards
Group: System/Kernel and hardware
Provides:  kernel-modules-drm-radeon-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-drm-radeon-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-drm-radeon-%kversion-%flavour-%krelease > %version-%release
Requires: kernel-modules-drm-%kversion-%flavour-%krelease = %version-%release
Prereq: coreutils
Prereq: module-init-tools >= 3.1
Prereq: %name = %epoch:%version-%release
Requires(postun): %name = %epoch:%version-%release

%description -n kernel-modules-drm-radeon-%flavour
The Direct Rendering Infrastructure, also known as the DRI, is a framework
for allowing direct access to graphics hardware in a safe and efficient
manner.  It includes changes to the X server, to several client libraries,
and to the kernel.  The first major use for the DRI is to create fast
OpenGL implementations.

These are modules for your ALT Linux system

%package -n kernel-modules-ide-%flavour
Summary: IDE  driver modules (obsolete by PATA)
Group: System/Kernel and hardware
Provides:  kernel-modules-ide-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-ide-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-ide-%kversion-%flavour-%krelease > %version-%release
Prereq: coreutils
Prereq: module-init-tools >= 3.1
Prereq: %name = %epoch:%version-%release
Requires(postun): %name = %epoch:%version-%release

%description -n kernel-modules-ide-%flavour
This package contains  IDE driver modules for the Linux kernel
package %name-%version-%release.

These drivers are declared obsolete by the kernel maintainers; PATA
drivers should be used instead.  However, the older IDE drivers may be
still useful for some hardware, if the corresponding PATA drivers do
not work well.

Install this package only if you really need it.

%package -n kernel-modules-kvm-%flavour
Summary: Linux KVM (Kernel Virtual Machine) modules
Group: System/Kernel and hardware
Provides:  kernel-modules-kvm-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-kvm-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-kvm-%kversion-%flavour-%krelease > %version-%release
Prereq: coreutils
Prereq: module-init-tools >= 3.1
Prereq: %name = %epoch:%version-%release
Requires(postun): %name = %epoch:%version-%release

%description -n kernel-modules-kvm-%flavour
Linux kernel module for Kernel Virtual Machine virtualization
environment.


%package -n kernel-modules-v4l-%flavour
Summary: Video4Linux driver modules (obsolete)
Group: System/Kernel and hardware
Provides:  kernel-modules-v4l-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-v4l-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-v4l-%kversion-%flavour-%krelease > %version-%release
Provides:  kernel-modules-uvcvideo-%kversion-%flavour-%krelease = %version-%release
Provides:  kernel-modules-gspca-%kversion-%flavour-%krelease = %version-%release
Provides:  kernel-modules-lirc-%kversion-%flavour-%krelease = %version-%release
Provides:  kernel-modules-lirc-%flavour = %version-%release
Prereq: coreutils
Prereq: module-init-tools >= 3.1
Prereq: %name = %epoch:%version-%release
Requires(postun): %name = %epoch:%version-%release

%description -n kernel-modules-v4l-%flavour
Video for linux drivers

%package -n kernel-modules-staging-%flavour
Summary:  Kernel modules under development
Group: System/Kernel and hardware
Provides:  kernel-modules-staging-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-staging-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-staging-%kversion-%flavour-%krelease > %version-%release
Requires: kernel-modules-drm-%kversion-%flavour-%krelease = %version-%release
Requires: kernel-modules-v4l-%kversion-%flavour-%krelease = %version-%release
Prereq: coreutils
Prereq: module-init-tools >= 3.1
Prereq: %name = %epoch:%version-%release
Requires(postun): %name = %epoch:%version-%release

%description -n kernel-modules-staging-%flavour
Drivers and filesystems that are not ready to be merged into the main
portion of the Linux kernel tree at this point in time for various
technical reasons.

%package -n kernel-headers-%flavour
Summary: Header files for the Linux kernel
Group: Development/Kernel
Requires: kernel-headers-common >= 1.1.5
Provides: kernel-headers = %version
#Provides: kernel-headers-%base_flavour = %version-%release

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
Requires: libelf-devel

%description -n kernel-headers-modules-%flavour
This package contains header files, Makefiles and other parts of the
Linux kernel build system which are needed to build kernel modules for
the Linux kernel package %name-%version-%release.

If you need to compile a third-party kernel module for the Linux
kernel package %name-%version-%release, install this package
and specify %kbuild_dir as the kernel source
directory.

%package -n kernel-doc-%base_flavour
Summary: Linux kernel %kversion-%base_flavour documentation
Group: System/Kernel and hardware
BuildArch: noarch

%description -n kernel-doc-%base_flavour
This package contains documentation files for ALT Linux kernel packages:
 * kernel-image-%base_flavour-up-%kversion-%krelease
 * kernel-image-%base_flavour-smp-%kversion-%krelease

The documentation files contained in this package may be different
from the similar files in upstream kernel distributions, because some
patches applied to the corresponding kernel packages may change things
in the kernel and update the documentation to reflect these changes.

%prep
%setup -cT -n kernel-image-%flavour-%kversion-%krelease
rm -rf kernel-source-%kernel_base_version
tar -xf %kernel_src/kernel-source-%kernel_base_version.tar
%setup -D -T -n kernel-image-%flavour-%kversion-%krelease/kernel-source-%kernel_base_version
%patch0 -p1


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


#configuration construction

CONFIGS="config config-%_target_cpu"

%if "%base_flavour" == "std"
CONFIGS="$CONFIGS config-std"
%endif

%if "%sub_flavour" == "pae"
CONFIGS="$CONFIGS config-pae"
%endif

%if "%sub_flavour" == "debug"
CONFIGS="$CONFIGS config-debug"
%endif

scripts/kconfig/merge_config.sh -m $CONFIGS

%make_build oldconfig
#%make_build include/linux/version.h
%make_build %make_target
%make_build modules

echo "Kernel built $KernelVer"

%if_enabled docs
# psdocs, pdfdocs don't work yet
%make_build htmldocs
%endif

%install
export ARCH=%base_arch
KernelVer=%kversion-%flavour-%krelease

install -Dp -m644 System.map %buildroot/boot/System.map-$KernelVer
install -Dp -m644 %image_path \
	%buildroot/boot/vmlinuz-$KernelVer
%if_enabled domU
install -Dp -m644 vmlinux %buildroot/boot/vmlinux-$KernelVer
%endif
install -Dp -m644 .config %buildroot/boot/config-$KernelVer

make modules_install INSTALL_MOD_PATH=%buildroot
find %buildroot -name '*.ko' | xargs gzip

mkdir -p %buildroot%kbuild_dir/arch/x86
install -d %buildroot%kbuild_dir
cp -a include %buildroot%kbuild_dir/include
cp -a arch/x86/include %buildroot%kbuild_dir/arch/x86


# drivers-headers install
install -d %buildroot%kbuild_dir/drivers/scsi
install -d %buildroot%kbuild_dir/drivers/md
install -d %buildroot%kbuild_dir/drivers/usb/core
install -d %buildroot%kbuild_dir/drivers/net/wireless
install -d %buildroot%kbuild_dir/net/mac80211
install -d %buildroot%kbuild_dir/kernel
install -d %buildroot%kbuild_dir/lib
cp -a drivers/scsi/scsi.h \
	%buildroot%kbuild_dir/drivers/scsi/
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
%ifarch %ix86 x86_64
	arch/x86/Makefile
	arch/x86/Makefile_32
	arch/x86/Makefile_32.cpu
%ifarch x86_64
	arch/x86/Makefile_64
%endif
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

# Provide kbuild directory with old name (without %%krelease)
ln -s "$(relative %kbuild_dir %old_kbuild_dir)" %buildroot%old_kbuild_dir

# Provide kernel headers for userspace
make headers_install INSTALL_HDR_PATH=%buildroot%kheaders_dir

#provide symlink to autoconf.h for back compat
pushd %buildroot%old_kbuild_dir/include/linux
ln -s ../generated/autoconf.h
ln -s ../generated/utsrelease.h
ln -s ../generated/uapi/linux/version.h
popd

# remove *.bin files
rm -f %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin
touch %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin

# install documentation
%if_enabled docs
install -d %buildroot%_docdir/kernel-doc-%base_flavour-%version/
cp -a Documentation/* %buildroot%_docdir/kernel-doc-%base_flavour-%version/
%endif # if_enabled docs

# On some architectures (at least ppc64le) kernel image is ELF and
# eu-findtextrel will fail if it is not a DSO or PIE.
%add_verify_elf_skiplist /boot/vmlinuz-*


%check
KernelVer=%kversion-%flavour-%krelease
mkdir -p test
cd test
msg='Booted successfully'
%__cc %optflags -s -static -xc -o init - <<__EOF__
#include <unistd.h>
#include <sys/reboot.h>
int main()
{
	static const char msg[] = "$msg\n";
	write(2, msg, sizeof(msg) - 1);
	reboot(RB_POWER_OFF);
	pause();
}
__EOF__
echo init | cpio -H newc -o | gzip -9n > initrd.img
qemu_arch=%_arch
console=ttyS0
%ifarch %ix86
qemu_arch=i386
%endif
%ifarch ppc64le
qemu_arch=ppc64
console=hvc0
%endif
timeout --foreground 600 qemu-system-"$qemu_arch" -kernel %buildroot/boot/vmlinuz-$KernelVer -nographic -append console="$console" -initrd initrd.img > boot.log &&
grep -q "^$msg" boot.log &&
grep -qE '^(\[ *[0-9]+\.[0-9]+\] *)?reboot: Power down' boot.log || {
	cat >&2 boot.log
	echo >&2 'Marker not found'
	exit 1
}

%files
/boot/vmlinuz-%kversion-%flavour-%krelease
/boot/System.map-%kversion-%flavour-%krelease
/boot/config-%kversion-%flavour-%krelease
%dir %modules_dir/
%defattr(0600,root,root,0700)
%modules_dir/*
%exclude %modules_dir/build
%exclude %modules_dir/kernel/drivers/media/
%exclude %modules_dir/kernel/drivers/staging/
%exclude %modules_dir/kernel/drivers/gpu/drm
%exclude %modules_dir/kernel/drivers/ide/
%exclude %modules_dir/kernel/%kvm_modules_dir
%ghost %modules_dir/modules.alias.bin
%ghost %modules_dir/modules.dep.bin
%ghost %modules_dir/modules.symbols.bin
%ghost %modules_dir/modules.builtin.bin

%if_enabled domU
%files -n kernel-image-domU-%flavour
/boot/vmlinux-%kversion-%flavour-%krelease
%endif

%files -n kernel-headers-%flavour
%kheaders_dir

%files -n kernel-headers-modules-%flavour
%kbuild_dir
%old_kbuild_dir
%dir %modules_dir/
%modules_dir/build

%if_enabled docs
%files -n kernel-doc-%base_flavour
%doc %_docdir/kernel-doc-%base_flavour-%version
%endif

%files -n kernel-modules-drm-%flavour
%modules_dir/kernel/drivers/gpu/drm
%exclude %modules_dir/kernel/drivers/gpu/drm/nouveau
%exclude %modules_dir/kernel/drivers/gpu/drm/radeon
%exclude %modules_dir/kernel/drivers/gpu/drm/mgag200
%exclude %modules_dir/kernel/drivers/gpu/drm/sis
%exclude %modules_dir/kernel/drivers/gpu/drm/savage
%exclude %modules_dir/kernel/drivers/gpu/drm/tdfx
%exclude %modules_dir/kernel/drivers/gpu/drm/r128
%exclude %modules_dir/kernel/drivers/gpu/drm/mga
%exclude %modules_dir/kernel/drivers/gpu/drm/via

%files -n kernel-modules-drm-ancient-%flavour
%modules_dir/kernel/drivers/gpu/drm/mgag200
%modules_dir/kernel/drivers/gpu/drm/sis
%modules_dir/kernel/drivers/gpu/drm/savage
%modules_dir/kernel/drivers/gpu/drm/tdfx
%modules_dir/kernel/drivers/gpu/drm/r128
%modules_dir/kernel/drivers/gpu/drm/mga
%modules_dir/kernel/drivers/gpu/drm/via

%files -n kernel-modules-drm-nouveau-%flavour
%modules_dir/kernel/drivers/gpu/drm/nouveau

%files -n kernel-modules-drm-radeon-%flavour
%modules_dir/kernel/drivers/gpu/drm/radeon

%files -n kernel-modules-ide-%flavour
%modules_dir/kernel/drivers/ide/

%files -n kernel-modules-kvm-%flavour
%modules_dir/kernel/%kvm_modules_dir

%files -n kernel-modules-v4l-%flavour
%modules_dir/kernel/drivers/media/
%dir %modules_dir/kernel/drivers/staging/media

%files -n kernel-modules-staging-%flavour
%modules_dir/kernel/drivers/staging/

%changelog
* Fri Aug 16 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.2.9-alt1
- v5.2.9

* Sun Aug 11 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.2.8-alt1
- v5.2.8

* Tue Aug 06 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.1.21-alt1
- v5.1.21  (Fixes: CVE-2019-11478)

* Tue Aug 06 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.2.7-alt1
- v5.2.7

* Mon Aug 05 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.2.6-alt1
- v5.2.6  (Fixes: CVE-2019-10207, CVE-2019-11478, CVE-2019-13648)

* Thu Jul 18 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.2.1-alt1
- v5.2.1

* Tue Jul 16 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.1.18-alt1
- v5.1.18  (Fixes: CVE-2019-3846)

* Fri Jul 12 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.1.17-alt1
- v5.1.17

* Thu Jul 04 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:5.1.16-alt2
- Added ppc64le support.

* Wed Jul 03 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.1.16-alt1
- v5.1.16

* Tue Jun 25 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.1.15-alt1
- v5.1.15

* Mon Jun 24 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.1.14-alt1
- v5.1.14

* Thu Jun 20 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.1.12-alt1
- v5.1.12 (Fixes: CVE-2019-11477, CVE-2019-11478, CVE-2019-11479)

* Mon Jun 17 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.21-alt2
- multiple kernel remote denial of service issues fixed

* Mon Jun 03 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.1.9-alt1
- v5.1.9

* Sat May 11 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.15-alt1
- v5.0.15  (Fixes: CVE-2011-1079)

* Wed May 08 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.14-alt1
- v5.0.14

* Sun May 05 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.13-alt1
- v5.0.13

* Sat May 04 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.12-alt1
- v5.0.12  (Fixes: CVE-2019-3882)

* Mon Apr 22 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.9-alt1
- v5.0.9

* Wed Apr 17 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.8-alt2
- AltHa LSM added

* Wed Apr 17 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.8-alt1
- v5.0.8  (Fixes: CVE-2019-3887)

* Mon Apr 08 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.7-alt1
- v5.0.7

* Wed Apr 03 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.6-alt1
- v5.0.6

* Sat Mar 30 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.5-alt1
- v5.0.5

* Tue Mar 19 2019 Kernel Bot <kernelbot@altlinux.org> 1:5.0.1-alt1
- v5.0.1

* Tue Mar 19 2019 Kernel Bot <kernelbot@altlinux.org> 1:4.20.17-alt1
- v4.20.17

* Wed Mar 13 2019 Kernel Bot <kernelbot@altlinux.org> 1:4.20.15-alt1
- v4.20.15

* Wed Mar 06 2019 Kernel Bot <kernelbot@altlinux.org> 1:4.20.14-alt1
- 4.20.14

* Thu Feb 28 2019 Kernel Bot <kernelbot@altlinux.org> 1:4.19.26-alt1
- v4.19.26

* Tue Feb 26 2019 Kernel Bot <kernelbot@altlinux.org> 1:4.19.25-alt2
- SCSI_SMARTPQI set to m

* Tue Feb 26 2019 Kernel Bot <kernelbot@altlinux.org> 1:4.20.12-alt1
- 4.20.12

* Thu Feb 07 2019 Kernel Bot <kernelbot@altlinux.org> 1:4.20.7-alt1
- 4.20.7

* Fri Jan 11 2019 Kernel Bot <kernelbot@altlinux.org> 1:4.20.1-alt1
- 4.20.1

* Mon Dec 24 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.20.0-alt1
- 4.20

* Sat Dec 22 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.12-alt1
- v4.19.12

* Mon Dec 17 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.10-alt1
- v4.19.10

* Thu Dec 13 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.9-alt1
- v4.19.9  (Fixes: CVE-2018-14625)

* Tue Dec 11 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.8-alt1
- v4.19.8

* Thu Dec 06 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.7-alt1
- v4.19.7

* Sun Dec 02 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.6-alt1
- v4.19.6

* Fri Nov 30 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.5-alt2
- build iin old branches fixed

* Tue Nov 27 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.5-alt1
- v4.19.5

* Fri Nov 23 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.4-alt1
- v4.19.4

* Thu Nov 22 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.3-alt1
- v4.19.3  (Fixes: CVE-2018-10940, CVE-2018-16658)

* Wed Nov 14 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.2-alt1
- v4.19.2  (Fixes: CVE-2018-18955)

* Fri Nov 09 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.1-alt1
- v4.19.1

* Mon Nov 05 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.17-alt1
- v4.18.17

* Mon Oct 29 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.19.0-alt1
- v4.19

* Sat Oct 20 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.16-alt1
- v4.18.16

* Thu Oct 18 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.15-alt1
- v4.18.15

* Mon Oct 15 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.14-alt1
- v4.18.14  (Fixes: CVE-2018-15471)

* Thu Oct 04 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.12-alt1
- v4.18.12  (Fixes: CVE-2018-7755)

* Mon Oct 01 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.11-alt1
- v4.18.11  (Fixes: CVE-2018-14633)

* Wed Sep 26 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.10-alt0.M80C.1
- v4.18.10

* Wed Sep 26 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.10-alt1
- v4.18.10

* Thu Sep 20 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.9-alt1
- v4.18.9

* Mon Sep 17 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.8-alt1
- v4.18.8

* Mon Sep 10 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.7-alt1
- v4.18.7

* Wed Sep 05 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.6-alt1
- v4.18.6

* Wed Aug 29 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.5-alt1
- v4.18.5

* Wed Aug 22 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.4-alt1
- v4.18.4

* Tue Aug 21 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.3-alt1
- v4.18.3  (Fixes: CVE-2018-9363)

* Fri Aug 17 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.18.1-alt1
- 4.18.1

* Thu Aug 16 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.15-alt1
- v4.17.15  (Fixes: CVE-2018-3620)

* Thu Aug 09 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.14-alt1
- v4.17.14

* Tue Aug 07 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.13-alt1
- v4.17.13

* Sat Aug 04 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.12-alt1
- v4.17.12

* Sun Jul 22 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.9-alt1
- v4.17.9

* Wed Jul 18 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.8-alt1
- v4.17.8

* Tue Jul 17 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.7-alt1
- v4.17.7

* Wed Jul 11 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.6-alt1
- v4.17.6  (Fixes: CVE-2018-10876, CVE-2018-10877, CVE-2018-10879, CVE-2018-10880,
  CVE-2018-10881, CVE-2018-10882, CVE-2018-10883)

* Mon Jul 09 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.5-alt1
- v4.17.5

* Tue Jul 03 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.4-alt1
- v4.17.4

* Tue Jun 26 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.18-alt1
- v4.16.18  (Fixes: CVE-2018-10840, CVE-2018-1118, CVE-2018-11412)

* Mon Jun 04 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.17.0-alt1
- v4.17

* Wed May 30 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.13-alt1
- v4.16.13

* Mon May 28 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.12-alt1
- v4.16.12
- external modules build fixed
- experimantal AltHa LSM added

* Wed May 23 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.11-alt1
- v4.16.11

* Mon May 21 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.10-alt1
- v4.16.10  (Fixes: CVE-2018-1120)

* Wed May 16 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.9-alt1
- v4.16.9  (Fixes: CVE-2018-1000200)

* Wed May 09 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.8-alt1
- v4.16.8

* Sun May 06 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.7-alt1
- v4.16.7  (Fixes: CVE-2018-1093, CVE-2018-1108)

* Thu Apr 26 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.5-alt1
- v4.16.5

* Tue Apr 24 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.4-alt1
- v4.16.4  (Fixes: CVE-2018-1092, CVE-2018-1094, CVE-2018-1095, CVE-2018-1108)

* Thu Apr 19 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.3-alt1
- v4.16.3

* Thu Apr 12 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.2-alt1
- v4.16.2

* Mon Apr 09 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.1-alt1
- v4.16.1

* Tue Apr 03 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.16.0-alt1
- v4.16.0

* Sun Apr 01 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.14.32-alt1
- v4.14.32  (Fixes: CVE-2017-8824)

* Mon Feb 19 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.15.4-alt1
- v4.15.4

* Mon Feb 05 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.14.17-alt1
- v4.14.17

* Wed Jan 31 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.14.16-alt1
- v4.14.16  (Fixes: CVE-2017-5715)

* Wed Jan 24 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.14.15-alt1
- v4.14.15

* Wed Jan 17 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.14.14-alt1
- v4.14.14  (Fixes: CVE-2017-1000410, CVE-2017-17741, CVE-2017-5753)

* Wed Jan 10 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.14.13-alt1
- v4.14.13

* Tue Jan 09 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.9.75-alt0.M80C.1
- v4.9.75

* Tue Jan 09 2018 Kernel Bot <kernelbot@altlinux.org> 1:4.14.12-alt1
- v4.14.12

* Fri Dec 29 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.14.10-alt1
- v4.14.10

* Mon Dec 25 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.14.9-alt1
- v4.14.9  (Fixes: CVE-2017-16995, CVE-2017-16996)

* Mon Dec 25 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.14.8-alt1.1
- SMACK enabled
- kernel.unprivileged_bpf_disabled set by default  (Fixes: CVE-2017-16995, CVE-2017-16996)

* Wed Dec 20 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.14.8-alt1
- v4.14.8

* Sun Dec 17 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.14.7-alt1
- v4.14.7

* Fri Dec 15 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.14.6-alt1
- v4.14.6   (Fixes: CVE-2017-0861, CVE-2017-1000407)

* Mon Dec 11 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.14.5-alt1
- v4.14.5

* Wed Dec 06 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.14.4-alt1
- v4.14.4   (Fixes: CVE-2011-1161, CVE-2017-8824)

* Tue Dec 05 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.16-alt1.1
- temporary fix for HugeDirtyCowPOC (fixes CVE-2017-1000405)

* Mon Nov 13 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.14.0-alt1
- v4.14.0

* Wed Nov 08 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.12-alt1
- v4.13.12

* Thu Nov 02 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.11-alt1
- v4.13.11   (Fixes: CVE-2017-12193)

* Fri Oct 27 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.10-alt1.1
- v4.13.10

* Sun Oct 22 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.9-alt1.1
- v4.13.9

* Wed Oct 18 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.8-alt1.1
- v4.13.8   (Fixes: CVE-2017-12188, CVE-2017-15265)

* Tue Oct 17 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.7-alt1.1
- Local root in alsa fixed (Fixes: CVE-2017-15265)

* Sun Oct 15 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.7-alt1
- v4.13.7   (Fixes: CVE-2017-5123)

* Fri Oct 13 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.6-alt1
- v4.13.6   (Fixes: CVE-2017-0786, CVE-2017-1000255)

* Thu Oct 05 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.5-alt1
- v4.13.5   (Fixes: CVE-2017-1000252, CVE-2017-12153, CVE-2017-12154)

* Wed Sep 27 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.4-alt1
- v4.13.4 

* Wed Sep 20 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.3-alt1
- v4.13.3

* Thu Sep 14 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.2-alt1
- v4.13.2

* Thu Sep 14 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.13.0-alt1
- v4.13.0

* Tue Sep 12 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.12.12-alt1
- v4.12.12

* Wed Aug 30 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.12.10-alt1
- v4.12.10

* Fri Aug 25 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.12.9-alt1
- v4.12.9

* Wed Aug 16 2017 Dmitry V. Levin <ldv@altlinux.org> 1:4.12.8-alt1
- v4.12.7 -> v4.12.8.
- Synced %%check with std-def.
- Changed kernel-doc to a noarch subpackage.
- Restricted access to %%modules_dir/ (see #5969).

* Sun Aug 13 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.12.7-alt1
- v4.12.7

* Sat Aug 12 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.12.6-alt1
- v4.12.6

* Sun Aug 06 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.12.5-alt1
- v4.12.5

* Thu Jul 27 2017 Dmitry V. Levin <ldv@altlinux.org> 1:4.12.4-alt1
- v4.12.2 -> v4.12.4.

* Sat Jul 15 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.12.2-alt1
- v4.12.2

* Thu Jul 13 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.12.1-alt1
- v4.12.1

* Tue Jul 04 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.12.0-alt1
- v4.12

* Thu Jun 22 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.11.6-alt1
- 4.11.6

* Wed May 24 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.11.2-alt1
- v4.11.2

* Mon May 22 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.11.1-alt1
- v4.11.1

* Mon May 22 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.10.17-alt1
- v4.10.17

* Mon May 15 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.10.16-alt1
- v4.10.16

* Wed May 10 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.10.15-alt1
- v4.10.15

* Sat Apr 22 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.10.12-alt1
- v4.10.12

* Wed Apr 19 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.10.11-alt1
- v4.10.11

* Thu Apr 13 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.10.10-alt1
- v4.10.10

* Sun Apr 09 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.10.9-alt1
- v4.10.9

* Fri Mar 31 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.10.8-alt1
- v4.10.8

* Sun Mar 26 2017 Kernel Bot <kernelbot@altlinux.org> 1:4.10.6-alt1
- v4.10.6

* Wed Mar 22 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.10.5-alt1
- v4.10.5

* Sun Mar 19 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.10.4-alt1
- v4.10.4

* Fri Mar 17 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.10.3-alt1
- 4.10.3
- in-kernel ipset returned

* Sun Mar 12 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.10.2-alt1
- 4.10.2

* Sun Mar 12 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.14-alt1
- v4.9.14

* Mon Feb 27 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.10.1-alt1
- 4.10.1

* Mon Feb 27 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.13-alt1
- v4.9.13

* Fri Feb 24 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.12-alt1
- v4.9.12

* Mon Feb 20 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.11-alt1
- v4.9.11

* Wed Feb 15 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.10-alt1
- v4.9.10

* Thu Feb 09 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.9-alt1
- v4.9.9

* Sun Feb 05 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.8-alt1
- v4.9.8

* Wed Feb 01 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.7-alt1
- v4.9.7

* Thu Jan 26 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.6-alt1
- v4.9.6

* Fri Jan 20 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.5-alt1
- v4.9.5

* Wed Jan 18 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.4-alt1
- v4.9.4

* Thu Jan 12 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.9.3-alt1
- v4.9.3

* Tue Jan 10 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.17-alt1
- v4.8.17

* Sat Jan 07 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.16-alt1
- v4.8.16

* Fri Dec 16 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.15-alt1
- v4.8.15

* Sun Dec 11 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.14-alt1
- v4.8.14

* Fri Dec 09 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.13-alt1
- v4.8.13

* Fri Dec 02 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.12-alt1
- v4.8.12

* Sat Nov 26 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.11-alt1
- v4.8.11

* Mon Nov 21 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.10-alt1
- v4.8.10

* Sun Nov 20 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.9-alt1
- v4.8.9

* Tue Nov 15 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.8-alt1
- v4.8.8

* Thu Nov 10 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.7-alt1
- v4.8.7

* Tue Nov 01 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.6-alt1
- v4.8.6

* Fri Oct 28 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.5-alt1
- v4.8.5
- secured /proc/interrupts

* Tue Oct 25 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.4-alt1
- v4.8.4

* Sat Oct 22 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.7.10-alt1
- v4.7.10

* Mon Oct 10 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.1-alt1
- v4.8.1

* Thu Oct 06 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.8.0-alt1
- v4.8
- gcc5 as kgcc
- gcc plugin activated (uses gcc-c++, libgmp-devel, mpc-devel)

* Fri Sep 30 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.7.6-alt1
- v4.7.6

* Sat Sep 24 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.7.5-alt1
- v4.7.5

* Thu Sep 15 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.7.4-alt1
- v4.7.4

* Wed Sep 07 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.7.3-alt1
- v4.7.3

* Sat Aug 20 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.7.2-alt1
- v4.7.2

* Thu Aug 18 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.7.1-alt1
- v4.7.1

* Wed Aug 17 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.6.7-alt1
- v4.6.7

* Mon Jul 25 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.7.0-alt1
- v4.7

* Mon Jul 11 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.6.4-alt1
- v4.6.4

* Sat Jun 25 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.6.3-alt1
- v4.6.3

* Fri Jun 10 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.6.2-alt1
- 4.6.2

* Wed Jun 08 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.5.7-alt1
- v4.5.7

* Thu May 19 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.6.0-alt1
- 4.6.0

* Thu May 12 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.5.4-alt1
- 4.5.4

* Fri May 06 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.5.3-alt1
- 4.5.3

* Wed Apr 20 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.5.2-alt1
- 4.5.2

* Wed Apr 13 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.5.1-alt1
- 4.5.1

* Tue Mar 15 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.5.0-alt1
- 4.5

* Thu Mar 10 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.4.5-alt1
- 4.4.5

* Fri Mar 04 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.4.4-alt1
- 4.4.4

* Fri Feb 26 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.4.3-alt1
- 4.4.3

* Thu Feb 18 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.4.2-alt1
- 4.4.2

* Tue Feb 02 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.4.1-alt1
- 4.4.1

* Tue Jan 19 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.4.0-alt2
- CVE-2016-0728 fixed

* Mon Jan 11 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.4.0-alt1
- 4.4.0

* Tue Dec 15 2015 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.3.3-alt1
- 4.3.3

* Fri Dec 11 2015 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.3.2-alt1
- 4.3.2

* Thu Dec 10 2015 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.3.1-alt1
- 4.3.1

* Tue Nov 17 2015 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.3.0-alt1
- 4.3.0

* Tue Nov 10 2015 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:4.2.6-alt1
- 4.2.6

* Tue Oct 27 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.2.5-alt1
- 4.2.5

* Fri Oct 23 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.2.4-alt1
- 4.2.4

* Thu Oct 08 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.2.3-alt2
- CONFIG_NO_HZ_FULL disabled (closes: #31342)

* Mon Oct 05 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.2.3-alt1
- 4.2.3

* Tue Sep 29 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.2.1-alt1
- 4.2.1

* Tue Sep 08 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.2.0-alt1
- 4.2

* Mon Aug 17 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.1.6-alt1
- 4.1.6

* Tue Aug 11 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.1.5-alt1
- 4.1.5

* Wed Aug 05 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.1.4-alt1
- 4.1.4

* Tue Aug 04 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.0.9-alt1
- 4.0.9

* Mon Jul 13 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.0.8-alt1
- 4.0.8

* Tue Jun 23 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.0.6-alt1
- 4.0.6
- dependence on bootloader-utils upgraded

* Tue Jun 09 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.0.5-alt1
- 4.0.5

* Thu May 21 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.0.4-alt1
- 4.0.4

* Mon May 18 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.0.3-alt1
- 4.0.3

* Tue May 12 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.19.8-alt1
- 3.19.8

* Mon Apr 27 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:4.0.0-alt1
- 4.0.0

* Mon Apr 20 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.19.5-alt1
- 3.19.5

* Mon Apr 13 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.19.4-alt1
- 3.19.4

* Thu Mar 26 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.19.3-alt1
- 3.19.3

* Wed Mar 18 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.19.2-alt1
- 3.19.2

* Sun Mar 08 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.19.1-alt1
- 3.19.1

* Tue Feb 17 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.19.0-alt1
- 3.19

* Wed Feb 11 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.18.7-alt1
- 3.18.7
- adjtimex on 32-bit fixed
- in-kernel ipset excluded
- netlabel patch updated

* Sat Feb 07 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.18.6-alt1
- 3.18.6

* Fri Jan 30 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.18.5-alt1
- 3.18.5

* Wed Jan 28 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.18.4-alt1
- 3.18.4

* Sat Jan 17 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.18.3-alt1
- 3.18.3

* Fri Jan 09 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.18.2-alt1
- 3.18.2

* Wed Dec 17 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.18.1-alt1
- 3.18.1

* Mon Dec 08 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.18.0-alt1
- 3.18.0

* Mon Dec 08 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.17.6-alt1
- 3.17.6

* Sun Dec 07 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.17.5-alt1
- 3.17.5

* Sat Nov 22 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.17.4-alt1
- 3.17.4
- set HZ=1000 on x86_64

* Sun Nov 16 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.17.3-alt1
- 3.17.3

* Fri Oct 31 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.17.2-alt1
- 3.17.2

* Fri Oct 17 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.17.1-alt1
- 3.17.1

* Wed Oct 15 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.16.6-alt1
- 3.16.6

* Fri Oct 10 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.16.5-alt1
- 3.16.5

* Mon Oct 06 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.16.4-alt1
- 3.16.4

* Thu Oct 02 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.16.3-alt2
- ldv and sem patches added

* Thu Sep 18 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.16.3-alt1
- 3.16.3

* Mon Sep 08 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.16.2-alt1
- 3.16.2

* Wed Aug 20 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.16.1-alt1
- 3.16.1

* Mon Aug 18 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.16.0-alt1
- 3.16.0

* Mon Aug 18 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.15.10-alt1
- 3.15.10

* Fri Aug 01 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.15.8-alt1
- 3.15.8

* Thu Jul 31 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.15.7-alt1
- 3.15.7

* Wed Jul 16 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.15.5-alt2
- EFI_MIXED enabled

* Wed Jul 09 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.15.5-alt1
- 3.15.5

* Mon Jul 07 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.15.4-alt1
- 3.15.4

* Tue Jul 01 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.15.3-alt1
- 3.15.3

* Fri Jun 27 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.15.2-alt1
- 3.15.2
- LEGACY_PTYS disabled
- AUFS added

* Tue Jun 17 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.15.1-alt1
- 3.15.1

* Tue Jun 17 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.8-alt1
- 3.14.7

* Thu Jun 12 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.7-alt1
- 3.14.7

* Sun Jun 08 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.6-alt1
- 3.14.6

* Thu Jun 05 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.5-alt2
- Fixes CVE-2014-3153

* Sun Jun 01 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.5-alt1
- 3.14.5

* Wed May 14 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.4-alt1
- 3.14.4

* Wed May 07 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.3-alt1
- 3.14.3

* Mon Apr 28 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.2-alt1
- 3.14.2

* Wed Apr 23 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.11-alt1
- 3.13.11

* Tue Apr 15 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.1-alt1
- 3.14.1

* Mon Apr 14 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.14.0-alt1
- 3.14

* Fri Apr 04 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.9-alt1
- 3.13.9

* Tue Apr 01 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.8-alt1
- 3.13.8
- "usb: ehci: fix deadlock when threadirqs option is use" reverted

* Mon Mar 24 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.7-alt1
- 3.13.7

* Thu Mar 20 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.6-alt2
- CVE-2014-2523 fixed

* Tue Mar 11 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.6-alt1
- 3.13.6

* Mon Feb 24 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.5-alt1
- 3.13.5

* Fri Feb 21 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.4-alt1
- 3.13.4

* Fri Feb 14 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.3-alt1
- 3.13.3

* Fri Feb 07 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.2-alt1
- 3.13.2

* Thu Jan 30 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.1-alt1
- 3.13.1

* Wed Jan 22 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.13.0-alt1
- 3.13.0

* Thu Jan 16 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.12.8-alt1
- 3.12.8

* Fri Jan 10 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.12.7-alt1
- 3.12.7
- "drm/radeon: 0x9649 is SUMO2 not SUMO" patch applied

* Fri Dec 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.12.6-alt1
- 3.12.6

* Thu Dec 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.12.5-alt1
- 3.12.5

* Mon Dec 09 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.12.4-alt1
- 3.12.4

* Thu Dec 05 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.12.3-alt1
- 3.12.3

* Tue Dec 03 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.12.2-alt1
- 3.12.2

* Fri Nov 22 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.12.1-alt1
- 3.12.1

* Thu Nov 21 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.9-alt1
- 3.11.9

* Wed Nov 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.12.0-alt1
- 3.12.0

* Wed Nov 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.8-alt1
- 3.11.8

* Mon Nov 04 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.7-alt1
- 3.11.7

* Sat Oct 19 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.6-alt1
- 3.11.6

* Mon Oct 14 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.5-alt1
- 3.11.5

* Sun Oct 06 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.4-alt1
- 3.11.4

* Tue Oct 01 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.3-alt1
- 3.11.3

* Fri Sep 27 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.2-alt1
- 3.11.2

* Wed Sep 18 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.1-alt2
- CONFIG_DEBUG_ATOMIC_SLEEP disabled
- aufs fixed

* Sun Sep 15 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.1-alt1
- 3.11.1

* Fri Sep 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.11.0-alt1
- 3.11

* Tue Sep 10 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.10.11-alt1
- 3.10.11

* Thu Aug 29 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.10.10-alt1
- 3.10.10

* Tue Aug 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.10.8-alt1
- 3.10.8

* Fri Aug 16 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.10.7-alt1.1
- bpp hack from Ulf Winkelvos in hope to fix #29219
- memory sanitizing patch added
- exfat driver from Samsung added

* Thu Aug 15 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.10.7-alt1
- 3.10.7

* Mon Aug 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.10.6-alt1
- 3.10.6
- CONFIG_GOLDFISH_* disabled (mike@)

* Wed Aug 07 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.10.5-alt2
- "Add mark s0 flag for NetLabel subsystem" patch from stanv@ added

* Mon Aug 05 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.10.5-alt1
- 3.10.5

* Mon Jul 29 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.10.4-alt1
- 3.10.4

* Fri Jul 26 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.10.3-alt1
- 3.10.3

* Mon Jul 22 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.10.2-alt1
- 3.10.2

* Tue Jul 16 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.10.1-alt1
- 3.10.1

* Sun Jul 14 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.10-alt1
- 3.9.10

* Thu Jun 27 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.8-alt1
- 3.9.8
- ipset disabled for separate module

* Fri Jun 21 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.7-alt1
- 3.9.7
- SWIOTLB on i586 set to y (closes #28911)

* Fri Jun 14 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.6-alt1
- 3.9.6

* Mon Jun 10 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.5-alt1
- 3.9.5

* Tue Jun 04 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.4-alt2
- CVE-2013-2850 fixed

* Sat May 25 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.4-alt1
- 3.9.4

* Mon May 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.3-alt1
- 3.9.3

* Sun May 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.2-alt1
- 3.9.2

* Sun May 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.13-alt1
- 3.8.13

* Wed May 08 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.1-alt1
- 3.9.1

* Mon May 06 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.9.0-alt1
- 3.9.0

* Sun May 05 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.11-alt1
- 3.8.11

* Mon Apr 29 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.10-alt1
- 3.8.10

* Fri Apr 26 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.9-alt1
- 3.8.9

* Mon Apr 22 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.8-alt2
- EFI_VARS set back to m

* Wed Apr 17 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.8-alt1
- 3.8.8
- EFI_VARS set to y

* Tue Apr 16 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.7-alt2
- uefi boot record instalation fixed (closes #28827)

* Fri Apr 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.7-alt1
- 3.8.7

* Fri Apr 05 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.6-alt1
- 3.8.6
- evbug disabled

* Fri Mar 29 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.5-alt1
- 3.8.5
- RTC_CMOS changed ot y (closes #28513)

* Thu Mar 21 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.4-alt1
- 3.8.4

* Fri Mar 15 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.3-alt1
- 3.8.3
- obsoleted postinstall scripts calls removed

* Thu Mar 14 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.2-alt3
- Don't allow CLONE_NEWUSER | CLONE_FS (local root fixed)
- CVE-2013-1828 fixed

* Wed Mar 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.2-alt2
- lost rtl8192ce enabled on i586
- default bpp on cirrus/qemu set to 16

* Mon Mar 04 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.2-alt1
- 3.8.2

* Thu Feb 28 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.1-alt1
- 3.8.1

* Thu Feb 28 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.10-alt1
- 3.7.10

* Mon Feb 25 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.0-alt2
- CVE-2013-1763 fixed

* Tue Feb 19 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.8.0-alt1
- 3.8.0

* Mon Feb 18 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.9-alt1
- 3.7.9
- patches for correct /proc permissions from ldv@ applied

* Fri Feb 15 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.8-alt1
- 3.7.8

* Wed Feb 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.7-alt1.1
- REGULATOR_DUMMY disabled (closes #27798)

* Mon Feb 11 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.7-alt1
- 3.7.7

* Wed Feb 06 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.6-alt1.1
- no OSS and some other config changes (closes: #28358) (closes: #28359)

* Mon Feb 04 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.6-alt1
- 3.7.6

* Tue Jan 29 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.5-alt1
- 3.7.5
- FANOTIFY and MMC_RICOH_MMC enabled

* Tue Jan 22 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.4-alt1
- 3.7.4

* Thu Jan 17 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.3-alt1
- 3.7.3

* Mon Jan 14 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.2-alt1.2
- conditional docs building

* Mon Jan 14 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.2-alt1.1
- changelog entries for std-def and std-pae added (hackaround)

* Mon Jan 14 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.2-alt1
- std-def, std-pae and un-def from one tree via specsubst
- 3.7.2
- gcc 4.7

* Sat Dec 29 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.1-alt2.1
- really do as written below

* Fri Dec 28 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.1-alt2
- make sha256 module on i586

* Thu Dec 20 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.6.11-alt1
- 3.6.11 (closes: 28138)
- Build using std-def config with config diff from 3.5.7.

* Tue Dec 18 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.1-alt1
- 3.7.1

* Tue Dec 18 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.11-alt1
- 3.6.11

* Tue Dec 11 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.0-alt1
- 3.7 release

* Tue Dec 04 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.0-alt0.8
- 3.7-rc8

* Tue Nov 27 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.7.0-alt0.7
- 3.7-rc7

* Tue Nov 27 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.8-alt1
- 3.6.8

* Wed Nov 21 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.7-alt2
- 32 bpp framebuffer on kvm's cirrus disabled back
- link-vmlinux.sh packaged (closes: #28016)

* Mon Nov 19 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.7-alt1
- 3.6.7

* Thu Nov 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.6-alt2
- some cirrus-related patches applied, 32 bpp mode enabled

* Tue Nov 06 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.6-alt1
- 3.6.6

* Thu Nov 01 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.5-alt1
- 3.6.5
- FB_EFI enabled

* Mon Oct 29 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.4-alt2
- 3.6.4

* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.3-alt2
- fixed possible ex4 corruption (https://lkml.org/lkml/2012/10/23/690)
- ldv@ patchs to mountinfo added
- CONFIG_DEBUG_PREEMPT disabled

* Mon Oct 22 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.3-alt1
- 3.6.3
- Borislav Petkovs test fix fo boot crash on nvidia ide

* Sat Oct 13 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.2-alt1
- 3.6.2

* Thu Oct 11 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.1-alt2.1
- POWER_AVS disabled

* Mon Oct 08 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.1-alt2
- 3.6.1

* Thu Oct 04 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.0-alt2
- wrong default hostname on x86_64 fixed
- drm-vgem driver added
- some config changes from std-def

* Mon Oct 01 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.6.0-alt1
- 3.6

* Sat Sep 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.5.4-alt1
- 3.5.4

* Sun Aug 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.5.3-alt1
- 3.5.3
- kmod: pass -b option to /sbin/modprobe (by ldv@)

* Wed Aug 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.5.2-alt1
- 3.5.2
- Applyed: fs: push rcu_barrier() from deactivate_locked_super()

* Fri Aug 10 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.5.1-alt1
- 3.5.1

* Thu Aug 02 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.5.0-alt2
- rebuild with right kernel-source

* Thu Jul 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.5.0-alt1
- 3.5

* Fri Jul 20 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.4.6-alt1
- 3.4.6

* Tue Jul 17 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.4.5-alt1
- 3.4.5

* Mon Jun 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.4.4-alt1
- 3.4.4

* Mon Jun 18 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.4.3-alt1
- 3.4.3

* Fri Jun 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.4.2-alt1
- 3.4.2

* Thu May 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.4.0-alt1
- 3.4

* Tue May 22 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.3.7-alt1
- 3.3.7

* Mon May 14 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.3.6-alt1
- 3.3.6

* Thu May 10 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.3.5-alt1
- 3.3.5

* Wed May 02 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.3.4-alt1
- 3.3.4

* Mon Apr 23 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.3.3-alt1
- 3.3.3

* Mon Apr 16 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.3.2-alt1
- 3.3.2

* Fri Apr 13 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.3.1-alt2
- kgcc set to 4.5
- AUDIT_LOGINUID_IMMUTABLE disabled

* Tue Apr 03 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.3.1-alt1
- 3.3.1

* Tue Mar 20 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.3.0-alt1
- 3.3

* Tue Mar 13 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.2.10-alt1
- 3.2.10

* Mon Mar 05 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.2.9-alt2
- HID_MULTITOUCH enabled for i586

* Thu Mar 01 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.2.9-alt1
- 3.2.9

* Wed Feb 29 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.2.8-alt1
- 3.2.8

* Tue Feb 21 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.2.7-alt1
- 3.2.7

* Tue Feb 14 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.2.6-alt1
- 3.2.6

* Tue Feb 07 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.2.5-alt1
- 3.2.5

* Mon Feb 06 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.2.4-alt1
- 3.2.4

* Thu Jan 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.2.2-alt1
- 3.2.2

* Thu Jan 19 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.2.1-alt2
- CVE-2012-0056 fixed

* Fri Jan 13 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.2.1-alt1
- 3.2.1

* Wed Jan 11 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.2.0-alt1
- 3.2

* Tue Jan 10 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.1.8-alt1
- 3.1.8

* Mon Dec 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.1.6-alt1
- 3.1.6

* Mon Dec 12 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.1.5-alt1
- 3.1.5

* Wed Nov 30 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.1.4-alt1
- 3.1.4

* Mon Nov 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.1.3-alt1
- 3.1.3

* Wed Nov 23 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.1.2-alt1
- 3.1.2

* Sat Nov 12 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.1.1-alt1
- 3.1.1

* Thu Oct 27 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.1.0-alt1
- 3.1

* Wed Oct 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.0.8-alt1
- 3.0.8
- *bin files are %%ghost now (aspsk@)
- feat-pegatron (silicium@)

* Wed Oct 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.0.7-alt1
- 3.0.7
- dependence on module-init-tools updated

* Fri Oct 07 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.0.6-alt2
- NULL dereference in nouveau fixed (cherry-pick from 3.1-rc4)

* Tue Oct 04 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.0.6-alt1
- 3.0.6

* Tue Aug 30 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.0.4-alt1
- 3.0.4

* Fri Aug 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.0.3-alt1
- 3.0.3

* Fri Aug 05 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.0.1-alt1
- 3.0.1
- modules provides fixed

* Wed Jul 27 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.0.0-alt2
- dependence on bootloader-utils 0.4.13 added

* Fri Jul 22 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:3.0.0-alt1
- 3.0.0

* Mon Jul 11 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.39-alt3
- 2.6.39.3

* Fri Jun 17 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.39-alt2
- 2.6.39.2
- xz squashfs compression enabled on i586
- usb gadget disabled

* Wed Jun 01 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.39-alt1
- 2.6.39.1

* Mon May 30 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.39-alt0.2
- cirrus kms enabled
- possible fix for scsi workqueue

* Tue May 24 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.39-alt0.1
- 2.6.39

* Sun May 22 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.38-alt7
- 2.6.38.7
- cirrus kms limited to 1024x768

* Tue May 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.38-alt6
- 2.6.38.6
- KMS on kvm emulated cirrus fixed

* Fri May 06 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.38-alt5.1
- KMS for kvm emulated cirrus

* Tue May 03 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.38-alt5
- 2.6.38.5
- epoch added to modules requires

* Fri Apr 22 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.38-alt4
- 2.6.38.4

* Fri Apr 15 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.38-alt3
- 2.6.38.3

* Wed Mar 30 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.38-alt2
- 2.6.38.2

* Fri Mar 25 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.38-alt1
- 2.6.38.1

* Tue Mar 15 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.37-alt4
- 2.6.37.4
- scripts/gcc-goto.sh packed into headers-modules

* Mon Mar 14 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.37-alt3
- 2.6.37.3

* Sun Feb 27 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.37-alt2
- 2.6.37.2
- in-kernel HDAPS enabled (#25127)
- igb and drbd provides fixed

* Thu Feb 17 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.37-alt1
- new version (2.6.37.1)

* Wed Feb 02 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.36-alt3.2
- r8712u added
- nvidia backlight added

* Tue Jan 25 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.36-alt3.1
- fix boot on i586

* Tue Jan 11 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.36-alt3
- 2.6.36.3

* Fri Dec 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.36-alt2
- 2.6.36.2

* Tue Nov 23 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.35-alt9
- 2.6.35.9
- default io sched set to deadline

* Fri Oct 29 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.35-alt8
- 2.6.35.8

* Tue Oct 12 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.35-alt7.1
- CVE-2010-2962 fixed
- netflow added (closes #24244)

* Tue Oct 05 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.35-alt7
- 2.6.35.7
- aufs2 really included (closes #24137)

* Mon Sep 27 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.35-alt6
- 2.6.35.6
- aufs2 included
- CONFIG_DEVTMPFS enabled
- legacy BSD ptys turned off

* Tue Sep 21 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.35-alt5
- 2.6.35.5

* Thu Sep 16 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.35-alt4.2
- CVE-2010-3301
- mountpoint for cgroup in /sys

* Tue Sep 14 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.35-alt4.1
- obsoleted RAMZSWAP changed to ZRAM from 2.6.36

* Thu Sep 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.35-alt4
- 2.6.35.4

* Thu Aug 26 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.35-alt3
- 2.6.35.3: run, rabbit, run!

* Sat Aug 21 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt20
- 2.6.32.20
- should fix local root

* Thu Aug 05 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt17
- 2.6.32.17

* Tue Jul 06 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt16
- 2.6.32.16
- Resume on intel should be fixed:
  see https://bugzilla.kernel.org/show_bug.cgi?id=13811

* Tue Jun 01 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt15
- 2.6.32.15

* Thu May 27 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt14
- 2.6.32.14

* Thu May 13 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt13
- 2.6.32.13

* Mon Apr 26 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt12
- 2.6.32.12

* Fri Apr 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt11
- 2.6.32.11

* Mon Mar 15 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt10
- 2.6.32.10
- drm-next merged

* Tue Feb 23 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt9
- 2.6.32.9
- NETFLOW activated

* Tue Feb 16 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt8.1
- kms enabled by default
- radeon and nouveau drm separated to subpackages
- netfilter: add NETFLOW target

* Tue Feb 09 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt8
- 2.6.32.8
- ide separated to subpackage
- additional -domU package with uncompressed vmlinux
- CONFIG_CGROUP_MEM_RES_CTLR enabled

* Thu Jan 28 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt7
- 2.6.32.7
- OSS disabled
- preemption enabled

* Mon Jan 25 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt6
- 2.6.32.6
- move aufs to module
- merge feat-gpu-drm-intel-kms-overlay from shrek@
- staging modules are separated to subpackage
- paravirtualization enabled

* Thu Jan 21 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt5
- aufs updated

* Fri Jan 15 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt4
- bootsplash patch added

* Wed Jan 13 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt3
- kvm enabled
- aufs enabled

* Tue Jan 12 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt2
- 2.6.32.3

* Fri Dec 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:2.6.32-alt1
- try to run before of locomotive

* Tue Oct 06 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.30-alt14
- 2.6.30.9

* Mon Sep 28 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.30-alt13
- 2.6.30.8

* Thu Sep 17 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.30-alt12
- 2.6.30.7

* Fri Sep 11 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.30-alt11
- 2.6.30.6 
- Echo canceler module moved to zaptel package
- Add CUSE support

* Mon Aug 17 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.30-alt10
- 2.6.30.5 

* Mon Aug 17 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.30-alt9
- [SECURITY] Fix CVE-2009-2692

* Wed Aug 12 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.30-alt8
- Add Samsung SWC-U200 WiMax dongle support.

* Fri Jul 31 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.30-alt7
- 2.6.30.4
- add wacom intuos4 support (tnx shrek@)
- fix pulseaudio support (tnx shrek@)

* Wed Jul 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.6.30-alt6
- drm/intel: merged Intel 2009Q2

* Mon Jul 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.6.30-alt5
- 2.6.30.2

* Tue Jul 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.6.30-alt4
- CVE-2009-1895: personality: fix PER_CLEAR_ON_SETID

* Fri Jul 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:2.6.30-alt3
- 2.6.30.1
- drm/radeon: added support RV740/RV790

* Thu Jun 25 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.30-alt2
- add perfcounter support

* Tue Jun 16 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.30-alt1
- 2.6.30 
- missed perfcounter patch
- vanilla ALSA
- missed DSDT from initrd patch.
- Infiniband support from kernel source

* Sun Jun 07 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.29-alt3
- fix i915 support(shrek@) (closes #20239):
	+disable GEM on i8xx 
	+disable KMS by default
	+allow tiled front buffers on 965+
- add Usb-serial driver for Moxa NP1240/1220/1220I
- update aufs patch. Replaced by aufs-standalone (closes: #20344)

* Thu May 28 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.29-alt2
- add missed bootsplash patch 

* Mon Apr 27 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.29-alt1
- 2.6.29.4

* Wed Apr 01 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.27-alt16
- alsa: alsa 1.0.19 repleaced by vanilla alsa with patches
- alsa: turn off pcspeeker support (closes: 19653)
- v4l: add AverMedia CardBus Plus  support (tnx week@) 
- udf: add dmode and mode mount options (tnx mutab0r@)

* Tue Mar 24 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.27-alt15
- 2.6.27.21
- disable GEM on Intel 8xx 

* Tue Mar 17 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.27-alt14
- 2.6.27.20

* Tue Feb 24 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.27-alt13
- 2.6.27.19 

* Thu Jan 29 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.27-alt12
- 2.6.27.14
- move eeepc modules to kernel  

* Sun Jan 25 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.27-alt11
- 2.6.27.13 
- alsa 1.0.19
- replaced unionfs by aufs

* Thu Jan 15 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.27-alt10
- 2.6.27.12 
- add eeepc rfkill support
- config:
+	turn on PRINTK_TIME
+	build-in kernel config
+	turn off CONFIG_USB_OHCI_HCD_SSB

* Sun Jan 11 2009 Michail Yakushin <silicium@altlinux.ru> 1:2.6.27-alt9
- add GEM support
- update config on x86_64: turn off CONFIG_SYSFS_DEPRECATED 
- fix thinkpad and prism54 aliases
- add conntrack RTSP support
- add AUFS

* Thu Dec 18 2008 Michail Yakushin <silicium@altlinux.ru> 1:2.6.27-alt8
- 2.6.27.10 
- update v4l to snapshot 2008-12-19
- config: Turn off WAN_ROUTER. 

* Tue Dec 16 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.27-alt7
- 2.6.27.9
- turn on SND_HDA_POWER_SAVE on x86_64 
* Mon Dec 08 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.27-alt6
- 2.6.27.8 
- fix rtc-cmos autoloading

* Thu Dec 04 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.27-alt5
- Build in MD raid support. Fix boot from MD. 

* Tue Dec 02 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.27-alt4
- Add elantech touchpad dirver
- Add missing evms-nodm patch
- Move KVM modules to separated package 
- USB: update unusual dev: (thank to vsu@)
	- add Nokia 6270, 5300, 6300, 7610 Supernova, 5310
	- add Nikon D300
	- add Kyocera / Contax SL300R T*
	- add Mio moov 330 gps
- Update r8169 driver (thank to vsu@)
- config changes:
    + Builded as module, what before was compiled in:
    	- IKCONFIG - /proc/config.gz  - How need it, can load it.
    	- IOSCHED_DEADLINE IOSCHED_DEADLINE - not default IO schedulers
    	- BLK_DEV_MD - SoftRAID support aka MD. (MAY BREAK BOOT ON MD,  TESTING NEEDED)
    	- FIREWIRE - new experemental firewire stack. Need testing.
    	- ULTRA32 - ISA network card.
    	- CRYPTO_HASH, CRYPTO_MANAGER, CRYPTO_HMAC, CRYPTO_DES(x86_64), CRYPTO_DEV_HIFN_795X(x86_64 )
    
    +Builded as module, what before was not build:
    	- LTPC ,COPS, COPS_DAYNA, COPS_TANGENT - some additional network features.
    	- NET_TCPPROBE - TCP network probber
    	- MTD_OOPS - save kernel oops to MTD
    	- SCSI_SRP - SCSI RDMA Protocol helper library
    	- ISDN_DRV_AVMB1_B1ISA, ISDN_DRV_AVMB1_T1ISA - Missed ISDN cards
    	- INPUT_WISTRON_BTNS - x86 Wistron laptop button interface -
    	- HP_WATCHDOG - HP Proliant watchdog driver
    	- SCx200_WDT - National Semiconductor SCx200 Watchdog
    	- VIDEO_SAA7134_DVB -  DVB on SAA7134 support
    	- RADIO_CADET, RADIO_RTRACK, RADIO_RTRACK2,CONFIG_RADIO_AZTECH,
    	 RADIO_GEMTEK,RADIO_GEMTEK_PCI,RADIO_MAXIRADIO, RADIO_MAESTRO, RADIO_SF16FMI, CONFIG_RADIO_SF16FMR2,
    	 CONFIG_RADIO_TERRATEC, RADIO_TRUST,RADIO_TYPHOON,
    	 RADIO_ZOLTRIX, USB_DSBR, USB_SI470X - missed radio drives
    	- MDA_CONSOLE - Monochrome console support
    	- USB_SERIAL_DEBUG - USB serial debug support
    	- USB_MIDI_GADGET -
    	- BACKTRACE_SELF_TEST, LKDTM, DEBUG_NX_TEST  - for debug perpouse
    
* Thu Nov 13 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.27-alt3
- 2.6.27.7
- Add custom DSDT support.
- Add to v4l subpackage gspca and uvcvideo provides

* Fri Nov 07 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.27-alt2
- 2.6.27.5
- turn on KVM
- rollback alsa to 2.6.27

* Fri Oct 24 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.27-alt1
- 2.6.27.4
- alsa 1.0.18
- Cramfs and ROMFS builded as module
- Alsa, V4l and DRM moved to subpackages
* Wed Sep 17 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.25-alt10
- 2.6.25.18
- add alsa 1.0.17 to this package
- add v4l 20081001 to tihs package
- turn on network flow classifer(CONFIG_NET_CLS_FLOW)
- turn off kvm. It is in separated package now.
- update to squashfs 3.4
- turn on CONFIG_LATENCYTOP

* Mon Sep 08 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.25-alt9
- 2.6.25.17
- add atl1e network card support (stanv@)
- Allow recursion in binfmt_script and binfmt_misc. (kas@)
- merge kernel-modules-e1000 into kernel-image

* Thu Jul 25 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.25-alt8
- 2.6.25.16
- add Intel AMT support 
- revert squashfs lzma patch, it`s full of bugs
- update unionfs

* Mon Jul 07 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.25-alt7
-2.6.25.11:
	+x86: fix ldt limit for 64 bit
- add lzma support to squashfs (stanv@)
- compile-in cramfs support (#9019)
- Merged changes from FC:
	+ add atl2 support
	+ add at76 support
	+ add e1000e network card on ich9 chipset support
	+ update wireless support
	+ fix tehuti driver
	+ fix eeepc sata driver (now it must should faster)
	+ fix rt2x00
	+ fix libata sleep mode
	+ fix serial port support
	+ add verbosity (print sizeof main structs at startup)
	+ fix ehci (now it respects nousb)
	+ fix MS wireless receiver support


* Thu Jul 03 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.25-alt6
- 2.6.25.10
- moved e1000 drivers to kernel-image-e1000

* Fri Jun 27 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.25-alt5
- 2.6.25.9 

* Mon Jun 23 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.25-alt4
- Security related fixes:
	+ l2tp: Fix potential memory corruption in pppol2tp_recvmsg()
	+ Reinstate ZERO_PAGE optimization in 'get_user_pages()' and fix XIP
	+ sctp: Make sure N * sizeof(union sctp_addr) does not overflow.
- 2.6.25.8
- intel_agp: Add support for Intel 4 series chipsets
- config-i586:
  + turn off Voluntary Preemption
  + turn on EISA and EISA drivers for hardware
  + flat memory model
  + some cleanups

* Mon Jun 16 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.25-alt3
- 2.6.25.7
- 2.6.25.6 

* Sat Jun 07 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.25-alt2
- 2.6.25.5:
  - fix CVE-2008-1673

* Wed May 07 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.25-alt1
- 2.6.25.4
- 2.6.25.2
  + CVE-2008-1669: fix SMP ordering hole in fcntl_setlk()
  + CVE-2008-1375: fix dnotify/close race

* Mon Mar 31 2008 Michail Yanushin <silicium@altlinux.ru> 2.6.24-alt7
-turn off v4l (moved to separate package)
-turn on many partition table support(i.e mac partion and amiga patition (bug #1599))
-turn off support ucb1400_ts to turn off ac97_bus.ko
-exclude alsa headers from kernel-headers-modules

* Mon Mar 24 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.24-alt6
- 2.6.24.4
- fixes support prism wifi cards
- add support of Atmel at76c503/at76c505/at76c505a
- add support of Realtek 8180/8185 PCI
- add bootsplash support
- turn on USB_DEVICE_CLASS(adds /dev/usb devices, fix bug  #15053)

* Mon Mar 17 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.24-alt5
-fix bug 14843
-add support for some Apple hardware
-turn on NUMA support on x86_64
-add some missed drives
-config cleanups

* Wed Feb 27 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.24-alt4
- 2.6.24.3
- add unionfs

* Mon Feb 11 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.24-alt3
- fix CVE-2008-0009/10

* Tue Feb 05 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.24-alt2
- added sqashfs patch
- added evms-nodm patch
- added altlinux init patch
- added some bugfix patches
- config fixup

* Thu Jan 31 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.24-alt1
- 2.6.24 fixes for sisyphus


* Fri Jan 18 2008 Michail Yakushin <silicium@altlinux.ru> 2.6.23-alt0
- 2.6.23

* Mon Jan 14 2008 Sergey Vlasov <vsu@altlinux.ru> 2.6.18-alt11
- Security-related changes:
  + CVE-2008-0001: fix access mode check for directories and RO filesystems

- x86-specific changes:
  + i386: retrieve CLFLUSH size from CPUID (needed for new drm modules)
- Header changes: 
  + <linux/kernel.h>: add upper_32_bits macro (needed for new drm modules)
- Filesystem updates:
  + squashfs: Updated to version 3.3.
- Network driver updates:
  + e1000e: New driver for Intel PCI Express network controllers; currently
    supports ICH9 LOM (8086:{10C0,10C2,10C3,10BD,294C}); backported from
    2.6.24-rc5.
  + forcedeth: fix long boot delay due to management unit handshake
    (lakostis@).
- Hardware monitor driver updates:
  + coretemp: New driver for builtin temperature sensors of Intel Core CPUs
    (backported from 2.6.24-rc1)
  + abituguru3: New driver for Abit uGuru revision 3 chips (found on recent
    Abit motherboards; uGuru revision 1 and 2 are handled by the older
    abituguru driver); backported from 2.6.24-rc3.
  + abituguru3: add AUX4 fan input for Abit IP35 Pro

* Wed Dec 12 2007 Sergey Vlasov <vsu@altlinux.ru> 2.6.18-alt10
- AGP driver changes:
  + *-agp: fix unbalanced ioremap/iounmap calls
  + agpgart: remove unnecessary flushes when inserting and removing pages
  + agpgart: add compat ioctl support
  + agpgart: const'ify the agpgart driver version
  + agpgart: don't lock pages
  + agpgart, *-agp: allow drm-populated agp memory types
  + ali-agp: add missing calls to global_flush_tlb()
  + amd-k7-agp: fix use after free in amd create gatt pages
  + amd64-agp, x86_64: fix off-by-two errors in aperture size checking
  + ati-agp: fix "use after free" / "double free" bug
  + efficeon-agp: fix 'struct agp_bridge_data' leaks in error paths
  + intel-agp: fix detection of aperture size versus GTT size on G965
  + intel-agp: fix PCI-posting flush typo
  + intel-agp: fix G965 GTT size detect
  + intel-agp: fix __free_pages() calls and error path handling
  + intel-agp: cleanup private data
  + intel-agp: use table for device probe
  + intel-agp: add support for 965GME/GLE (8086:2a12)
  + intel-agp: add support for 945GME (8086:27ae)
  + intel-agp: add support for G33, Q33 and Q35 (8086:29[bcd][02])
  + intel-agp: fix device probe for non-integrated video and multiple submodels
  + intel-agp: don't load if no IGD and AGP port
  + intel-agp: fix GTT map size on G33
  + intel-agp: fix i830 mask variable that changed with G33 support
  + sis-agp, amd64-agp: fix probe collisions due to overlapping PCI IDs
  + via-agp: fix wrong PCI ID for CX700/VT3324 (1106:0324)
  + via-agp: add support for P4M900 (VT3364) (1106:0364)
- Input driver fixes:
  + i8042: fix AUX port detection with some chips (fixes builtin touchpad
    detection on HP500/HP510 notebooks) (lakostis@)
- SD/MMC driver updates (lakostis@):
  + sdhci: high speed support
  + sdhci: change SDHCI iomem error to a warning
  + sdhci: power quirk for ENE controllers
  + sdhci: fix ENE CB712/4 card readers support
- SATA driver updates:
  + libata core:
    + blacklisted lots of drives with broken NCQ (backport from 2.6.24-rc2):
      - HDT722516DLA380 / V43OA96A
      - HITACHI HDS7225SBSUN250G* (all firmware versions)
      - HITACHI HDS7250SASUN500G* (all firmware versions)
      - Hitachi HTS542525K9SA00 / BBFOC31P
      - Maxtor * / BANC* (wildcard match for lots of buggy devices)
      - Maxtor 7V300F0 / VA111630
      - Maxtor 7V300F0 / VA111900
      - SAMSUNG HD401LJ / ZZ100-15
      - ST3160812AS / 3.ADJ
      - ST380817AS / 3.42
      - ST9120822AS / 3.CLF
      - ST9160821AS / 3.ALD
      - ST9160821AS / 3.CCD
      - ST9160821AS / 3.CLF
      - ST980813AS / 3.ADB
      - WDC WD3200AAJS-00RYA0 / 12.01B01
    + libata: prevent devices with blank model names from being DMA blacklisted
    + libata: fix reported task file values in sense data
    + passthru: update protocol numbers for new spec
    + passthru: map the ATA passthru UDMA protocols to ATA_PROT_DMA
  + ahci: add ATI SB700 support in AHCI/RAID modes (1002:{4391,4392,4393})
  + ahci: add ATI SB800 support (1002:{4394,4395})
  + ahci: add Intel Tolapai support (8086:{502a,502b})
  + ahci: add nVidia MCP79 support (10de:0ab[89a-f])
  + ata_piix: update map 10b for ich8m
  + pata_marvell: add more device ids (11ab:{6121,6123})
  + sata_mv: add Hightpoint RocketRaid 1740/1742 support (1103:{1740,1742})
  + sata_promise: mark FastTrack TX4200 as a second-generation chip
  + sata_sil24: fix IRQ clearing race when PCIX_IRQ_WOC is used
  + sata_sis: use correct S/G table size
- Network subsystem updates:
  + netpoll: fix UDP checksum issue in net poll rx
  + fix race condition in network device name allocation (lakostis@)
- Network driver updates:
  + forcedeth: backported changes from 2.6.23-rc2 (lakostis@):
    + bugfixes (including MAC address fixes for some boards)
    + added MCP67, MCP73 chip support
    + added NAPI support
  + forcedeth: backported changes from 2.6.24-rc2:
    + bugfixes
    + added MCP77 chip support
  + r8169: backported changes from 2.6.23
  + skge: backported bugfixes from 2.6.22-rc1 (lakostis@)
  + tg3: backported bugfixes from 2.6.23 (lakostis@)
- Config updates:
  + enabled NAPI support in forcedeth driver (CONFIG_FORCEDETH_NAPI=y)
  + disabled NTFS write support (CONFIG_NTFS_RW) due to reported hangs during
    mount (this write support was very limited anyway; use ntfs-3g instead)
  + enabled RTC IRQ emulation through HPET (CONFIG_HPET_EMULATE_RTC=y) - fixes
    periodic RTC IRQ when HPET is enabled on recent motherboards (tested on
    Gigabyte GA-P35-DS3R, ASUS P5B Plus); this also requires non-modular RTC
    driver (CONFIG_RTC=y).  If the RTC IRQ is still broken, try the "nohpet"
    boot option on x86_64, or the "hpet=disable" boot option on i586.

* Sat Nov 24 2007 Sergey Vlasov <vsu@altlinux.ru> 2.6.18-alt9
- Security-related changes:
  + CVE-2006-6058: minix: limit printks on corrupted dir i_size
  + CVE-2007-2875: cpuset: fix information leak through /dev/cpuset/tasks
  + CVE-2007-2878: vfat: fix compat ioctls memory corruption on 64-bit systems
  + CVE-2007-3105: random: fix bound check ordering
  + CVE-2007-3513: usblcd: limit memory consumption during write
  + CVE-2007-3731 [1/2]: ptrace: handle bogus %%cs in single-step decoding
  + CVE-2007-3731 [2/2]: i386: fix TRACE_IRQS_ON without proper segment setup
  + CVE-2007-3740: cifs: respect umask when unix extensions are enabled
  + CVE-2007-3843: cifs: fail mount if signing is requested but not supported
  + CVE-2007-3848: reset current->pdeath_signal on SUID binary execution
  + CVE-2007-4133: don't allow the stack to grow into hugetlb reserved regions
  + CVE-2007-4133: hugetlbfs: fix prio_tree unit
  + CVE-2007-4308: aacraid: require CAP_SYS_ADMIN for configuration ioctls
  + CVE-2007-4997: ieee80211: avoid integer underflow for runt rx frames
  + CVE-2007-5500: wait_task_stopped: Check p->exit_state, not TASK_TRACED

- Filesystem fixes:
  + locks: fix possible infinite loop in posix deadlock detection

- Updated BuildRequires (kernel-build-tools changed to rpm-build-kernel).
- Added BuildRequires(pre): rpm-build-kernel to get clean build in hasher.

* Sun Sep 23 2007 Sergey Vlasov <vsu@altlinux.ru> 2.6.18-alt8
- CVE-2007-4573 (x86_64 only): Zero extend all registers after ptrace in 32bit
  entry path.

* Thu Aug 02 2007 Sergey Vlasov <vsu@altlinux.ru> 2.6.18-alt7
- Security-related changes:
  + CVE-2007-1353: bluetooth: fix L2CAP and HCI setsockopt() information leaks
  + CVE-2007-1496: netfilter: nfnetlink_log: fix NULL pointer dereferences
  + CVE-2007-2453: random: fix error in entropy extraction, fix seeding with
    zero entropy
  + CVE-2007-2525: pppoe: fix leak when socket is closed before PPPIOCGCHAN
  + CVE-2007-2876: netfilter: {ip,nf}_conntrack_sctp: fix remotely triggerable
    NULL ptr dereference
  + CVE-2007-3642: netfilter: nf_conntrack_h323: check range of choices' index
    values

- Added internal USB core header files to kernel-headers-modules (needed to
  compile external USB host controller drivers) (#12451).
- Added aic94xx driver (v1.0.2, from RHEL5 kernel-2.6.18-8.1.6.el5) for
  Adaptec SAS/SATA AIC94xx chip based host adapters (no HostRAID support).

- Core fixes:
  + audit/accounting: fix tty locking
  + audit: do not accept arch filter lists with < or >
  + audit: fix PPID filtering
  + audit: fix name_count array overrun
  + audit: fix kstrdup() error check
  + audit: fix audit_filter_user_rules() initialization bug
  + audit: fix deadlock in audit_log_task_context()
  + audit: fix oops removing watch if audit disabled
- Character driver fixes:
  + random: fix error in entropy extraction (CVE-2007-2453 1/2)
  + random: fix seeding with zero entropy (CVE-2007-2453 2/2)
- IDE driver updates:
  + amd74xx: add NVIDIA MCP73/MCP77 support (10de:{056c,0759})
  + atiixp: add ATI SB700 support (1002:439c)
  + ide-cd: remove ugly messages when opening CD drive without media
  + ide-core: unregister idepnp driver on unload
  + ide-core: update DMA blacklist (sync with v2.6.22-rc3)
  + ide-cs: add new device ids (sync with v2.6.22-rc1)
  + piix, ide-core: clear bmdma status in ide_intr() for Intel ICHx controllers
  + serverworks: fix corruption/timeouts with MegaIDE
  + sis5513: add support for SiS966 in IDE emulation mode (1039:1180)
  + via82cxxx: add VIA CX700 and VT8237S support (1106:{8324,3372})
  + via82cxxx: add support for VIA SATA in EIDE mode (1106:5324)
- SATA driver updates:
  + libata core fixes:
    + clear TF before IDENTIFY (fixes problems with some weird devices)
    + fix decoding of 6-byte SCSI commands
    + fix upper LBA bits copying in HDIO_DRIVE_TASK
    + improve handling of diagnostic fail
    + passthru: always enforce correct DEV bit
    + update device blacklist (sync with v2.6.22 and later updates)
  + ahci: add ATI SB700 support (1002:4390)
  + ahci: add NVIDIA MCP73/MCP77 support (10de:{07f[0-9ab],0ad[0-9ab]})
  + ahci: add another PCI ID for Intel ICH9M in RAID mode (8086:292c)
  + ahci: add another VIA PCI ID (1106:6287)
  + ahci: disable 64bit DMA on ATI SB600 (also affects SB700)
  + ahci: remove nonexistent PCI ID for SB600 (1002:4381)
  + ata_piix: kill incorrect invalid map value warning
  + sata_mv: add Adaptec 1430SA support (9005:0243)
  + sata_mv: add PCI ID for Marvell 7042 (11ab:7042)
  + sata_nv: remove wildcard IDs for all NVIDIA chips with IDE and RAID class
    (newer chips are AHCI-based and not compatible with sata_nv)
  + sata_promise: add TX2plus PATA channel support (backport from v2.6.20-rc1)
  + sata_promise: chip setup fixes backported from v2.6.20-rc1
  + sata_sil24: add Adaptec 1220SA support (1095:0242)
  + sata_via: add more PCI IDs (1106:{5287,5372,7372})
- Network driver fixes:
  + e1000: fix watchdog timeout panics
  + pppoe: fix leak when socket is closed before PPPIOCGCHAN (CVE-2007-2525)
  + ppp: fix "osize too small" errors when decoding mppe (#12081)
- Network subsystem fixes:
  + bluetooth: fix L2CAP and HCI setsockopt() information leaks (CVE-2007-1353)
  + netfilter: nf_conntrack_ipv6: fix incorrect classification of IPv6
    fragments as ESTABLISHED (CVE-2007-1497)
  + netfilter: nfnetlink_log: fix NULL pointer dereferences on multiple packets
    per netlink message (CVE-2007-1496 1/3)
  + netfilter: nfnetlink_log: fix possible NULL pointer dereferences in
    nfulnl_recv_config() (CVE-2007-1496 2/3)
  + netfilter: nfnetlink_log: fix crash on bridged packet (CVE-2007-1496 3/3)
  + netfilter: nf_conntrack_h323: check range of choices' index values
    (CVE-2007-3642)
  + netfilter: {ip,nf}_conntrack_sctp: fix remotely triggerable NULL ptr
    dereference (CVE-2007-2876)
  + tipc: add missing unlock in port timeout code
  + tipc: fix NULL dereference in tipc_publish()
  + tipc: fix infinite loop in netlink handler
- PCI subsystem fixes:
  + disable MSI on ATI RS400-200 and RS480, Serverworks HT1000, VIA VT3351
- Filesystem fixes:
  + ext3: fix inode number overflows
  + ext3: fix block number overflows on 16 TB filesystems
  + ext3: jbd: journal_dirty_data re-check for unmapped buffers
  + ext3: return ENOENT from ext3_link when racing with unlink
  + ext3: fix lost brelse in ext3_read_inode()

* Sat Apr 28 2007 Sergey Vlasov <vsu@altlinux.ru> 2.6.18-alt6
- Added a separate IDE driver module "jmicron" for JMicron IDE controllers
  (backported from 2.6.21-rc1, partially by lakostis@).  In previous releases
  these devices were supported by the "generic" module; be careful during
  upgrade if you have such controllers.
- Added bootsplash support (from SUSE 10.2 kernel-source-2.6.18.8-0.1).
- Removed framebuffer console rotation support due to incompatibility with
  bootsplash.
- Increased number of supported processors to 32 for i586 kernels and to 64
  for x86_64 kernels (#11068).
- Added dvb-core, cx88 and saa7134 headers to kernel-headers-modules (#10626).

- Security-related changes:
  + CVE-2007-0005: cm4040_cs: fix buffer overflow
  + CVE-2007-1357: appletalk: fix a remotely triggerable crash
  + CVE-2007-1388: ipv6: fix ipv6_setsockopt NULL dereference
  + CVE-2007-1592: ipv6: avoid ipv6_fl_socklist sharing
  + CVE-2007-1861: ipv4: Fix infinite recursion in nl_fib_lookup()
  + ipv6: disallow source routing by default (can be enabled again with the
    net.ipv6.accept_source_route sysctl, or with per-interface settings).

- Core fixes:
  + x86_64: swsusp: avoid memory holes and reserved memory regions
  + x86_64: fix page align in e820 allocator
  + fix reboot on Dell OptiPlex 745
  + x86: restore i8259A eoi status on resume
  + apm: default to "power_off" when SMP kernel is used on single CPU machines
  + swiotlb: fix panic on sg list sync (affected Intel EM64T with > 3G RAM)
  + cpu-hotplug: release workqueue_mutex properly on CPU hot-remove
  + cpu-hotplug: fix locking races
  + mm: fix wrong pgsteal counters in /proc/vmstat
  + mm: hugetlb: fix absurd HugePages_Rsvd
  + mm: reject corrupt swapfiles earlier
  + mm: catch swap write failure instead of losing page data
  + mm: fix possible madvise(MADV_REMOVE) infinite loop
- ACPI fixes:
  + acpi-pnp: fix DMA resource allocation
  + processor: fix bounds checking from the value returned from _PPC method
  + processor: delete some spurious ACPI messages
  + processor: do not query _PPC at startup (fixes missing frequencies in
    acpi-cpufreq on some laptops)
  + processor: fix not waking up from C2 for Banias and Dothan Pentium M
- Block driver fixes:
  + cciss: bugfixes from RHEL5/CentOS kernel-2.6.18-8.1.1.el5:
     + fix "fifo full" errors on E200 family controllers
     + fix subsystem ID for E500
     + disable DMA prefetch on P600 due to hardware bug
     + don't try to start a queue on a disk which is configuring
     + cciss_interrupt_mode() cleanup
     + remove pci_disable_device() (fixes reloading after rmmod)
  + cciss: fixes for previously applied >= 2TB volume support patch
  + cpqarray: add pci_set_master() to fix detection failure on some systems
- Character driver changes:
  + agpgart: fix up misprogrammed bridges with incorrect AGPv2 rates
  + agpgart: amd-k7-agp: Prevent memory leak in amd_create_gatt_pages()
  + agpgart: amd64-agp: add VIA VT3336 support
  + agpgart: intel-agp: fix Intel 965 AGP memory mapping function
  + agpgart: intel-agp: restore graphics device's pci space early in resume
  + agpgart: intel-agp: don't try to remap i810 registers on resume
  + agpgart: intel-agp: add Intel 965GM chipset support
  + agpgart: via-agp: add CX700, VT3336, P4M890 support
  + cm4000_cs: fix return value check in init
  + cm4040_cs: fix buffer overflow (CVE-2007-0005)
- EDAC driver fixes:
  + i82875p_edac: fix /proc/bus/pci/devices mismatch with the rest of
    /proc/bus/pci/* tree (from RHEL5/CentOS kernel-2.6.18-8.1.1.el5)
  + edac_mc: fix error handling during init
  + e752x_edac: fix fatal vs. non-fatal error mask
  + e752x_edac: use byte access for DRA registers instead of dword
  + e752x_edac: read error offset properly
- IDE driver fixes:
  + ide-floppy: fix crash on unformatted media
- Infiniband driver fixes:
  + IB/mthca: fix off-by-one in FMR handling on memfree
- MD driver fixes:
  + linear: fix read past end of array
- DVB driver fixes:
  + dvb-core: fix illegal reuse of file_operations struct
  + dvb-core: fix locking problems
- Network driver fixes:
  + 3c589_cs: fix SMP bugs
  + 8139too: fix netpoll deadlock
  + atm drivers: fix wrong __init usage and error handling
  + e1000: sync with RHEL5/CentOS kernel-2.6.18-8.1.1.el5:
     + add support for Intel Kirkwood adapters: 8086:{10a4,10bc}
     + add support for newer ICH8 LOM devices: 8086:{10c4,10c5}
     + fix TSO hangs on 82544 chips
  + ppp: fix possible sk_buff leak on interface destruction
  + ppp: fix skbuff.c:BUG() on garbage input
  + sis190: fix MAC address reading from EEPROM
  + sis190: fix RTNL and flush_scheduled_work deadlock
  + sis190: add Broadcom PHY AC131 support (WinFast 761GXK8MB-RS motherboard)
  + r8169: revert bogus BMCR reset
  + r8169: fix a race between PCI probe and dev_open
- PCI subsystem fixes:
  + fix JMicron PCI quirk handling (should fix IDE/AHCI subdevice confusion on
    some controllers leading to double disk detection)
- SCSI subsystem fixes:
  + don't add scsi_device for devices that return PQ=1, PDT=0x1f
- SCSI driver fixes:
  + sym53c8xx: fix PCI ID conflict with cpqarray
- SATA driver fixes:
  + ahci: ignore SERR_INTERNAL on ATI SB600 (lakostis@)
  + ahci: use PCI class matching for JMicron devices
  + ahci: remove JMicron fixup (now performed by the PCI quirk code)
- USB driver fixes:
  + rtl8150: new device ID (1557:8150)
  + rtl8150: fix write_mii_word()
- Filesystem fixes:
  + xfs: fix sub-block zeroing for buffered writes into unwritten extents
- Network subsystem fixes:
  + appletalk: fix potential OOPS in atalk_sendmsg()
  + appletalk: fix a remotely triggerable crash (CVE-2007-1357)
  + bluetooth: fix endian swapping for L2CAP socket list
  + bluetooth: fix wrong put_user() in HIDP compat ioctl handling
  + bluetooth: fix socket locking in hci_sock_dev_event()
  + copy mac_len in skb_clone()
  + ifb: fix packet double-counting
  + ifb: fix crash on input device removal
  + cls_basic: fix NULL pointer dereference
  + cls_basic: fix memory leak in basic_destroy
  + decnet: handle neigh_parms_alloc() failure
  + decnet: fib: Fix out of bound access of dn_fib_props[]
  + ipv4/ipv6 multicast: check add_grhead() return value
  + ip: fix twcal_jiffie size
  + tcp: fix freeing of used skb when using IPV6_RECVPKTINFO
  + tcp: fix sorting of SACK blocks
  + tcp: don't apply FIN exception to full TSO segments
  + tcp: prevent pseudo garbage in SYN's advertized window
  + udp: reread uh pointer after pskb_trim
  + tcp: fix minisock tcp_create_openreq_child() typo
  + ipv4: fib: Fix out of bound access of fib_props[]
  + ipv4: fib: Fix infinite recursion in nl_fib_lookup() (CVE-2007-1861)
  + ipv6: fix anycast address refcounting
  + ipv6: fix /proc/net/anycast6 unbalanced inet6_dev refcnt
  + ipv6: fix ipv6_setsockopt NULL dereference (CVE-2007-1388)
  + ipv6: fix ipv6_getsockopt_sticky copy_to_user leak
  + ipv6: avoid ipv6_fl_socklist sharing (CVE-2007-1592)
  + ipv6: use appropriate seed for calculating ehash index
  + ipv6: fix incorrect length check in rawv6_sendmsg()
  + ipv6: disallow source routing by default
  + packet: check device down state before hard header callbacks

* Fri Mar 09 2007 Sergey Vlasov <vsu@altlinux.ru> 2.6.18-alt5
- Security-related fixes:
  + CVE-2007-0006: security: keys: fix key serial number collision handling
  + CVE-2007-0772: knfsd: fix a free-wrong-pointer bug in nfs/acl server
  + CVE-2007-1000: ipv6: handle np->opt being NULL in ipv6_getsockopt_sticky()
- Applied changes from 2.6.18.7 and 2.6.18.8 stable releases:
  + bcm43xx: Fix for oops on resume
  + bcm43xx: Fix for oops on ampdu status
  + IB/mad: Fix race between cancel and receive completion
  + dvb-core: fix bug in CRC-32 checking on 64-bit systems
  + v4l: fix cx2341x audio_properties
  + v4l: cx88: Fix leadtek_eeprom tagging
  + v4l: fix quickcam communicator driver for big endian architectures
  + v4l: fix ks0127 status flags
  + v4l: tveeprom: autodetect LG TAPC G701D as tuner type 37
  + v4l: video-buf: fix videobuf_queue->stream corruption and lockup
  + x86_64: fix 2.6.18 regression - PTRACE_OLDSETOPTIONS should be accepted
  + mm: fix msync error on unmapped area
  + ext2, ext3: fix umask when noACL kernel meets extN tuned for ACLs
- PCI driver changes:
  + pcieport-driver: remove wrong warning message about invalid IRQ (lakostis)
- SCSI driver changes:
  + pata_marvell: New driver for Marvell 88SE6101/88SE6145 ATA in legacy mode
    (lakostis; backport from 2.6.21-rc1)
- Network driver changes:
  + r8169: updated to version from 2.6.16-rc1 (lakostis)
- EDAC driver changes:
  + EDAC: turn off debug messages by default
- USB driver changes:
  + rndis_host: fix bind failure handling bugs leading to oopses (#9996)
- Filesystem changes:
  + knfsd: ratelimit some nfsd messages that are triggered by external events

* Fri Feb 16 2007 Sergey Vlasov <vsu@altlinux.ru> 2.6.18-alt4
- Security-related fixes:
  + CVE-2004-1073: do not dump core for unreadable binaries via PT_INTERP
  + CVE-2006-4814: fix incorrect user space access locking in mincore()
  + CVE-2006-5749: ISDN: call init_timer() for ISDN PPP CCP reset state timer
  + CVE-2006-5753: fix memory corruption due to wrong bad_inode method types
  + CVE-2006-6054: ext2: skip pages past number of blocks in ext2_find_entry
  + CVE-2006-4572: netfilter: fix ip6_tables protocol bypass bug
  + CVE-2006-4572: netfilter: fix ip6_tables extension header bypass bug
- Core MM fixes:
  + fix BUG_ON() in shmem_truncate_range()
  + fix locking bug in read_zero_pagealigned()
- PCI subsystem changes:
  + add ICH9 IRQ router support
- Block layer changes:
  + Reenabled bd_claim() check between whole devices and partitions.
    Disabling this check is too dangerous - e.g., it allows simultaneous
    mounting of a whole device and a partition on some bootable USB-Flash
    drives.  Support for EVMS coexistence with the in-kernel partitioning
    code is now provided by a patch to the device mapper driver.
- Crypto subsystem changes:
  + sha512: fix sha384 block size
- CD-ROM driver changes:
  + cdrom: set default timeout to 7 seconds
- Character driver fixes:
  + rio: fix typo in bitwise AND expression
- I2C driver changes:
  + ds1337: fix broken initialization
  + i2c-i801: add Intel ICH9 SMBus support
  + i2c-i801: enable PEC support on ICH6, ICH7, ICH8, ICH9 and ESB2
- IDE driver changes:
  + atiixp: fix hang on error handling due to wrong ide_lock usage
  + atiixp: SB600 IDE/PATA controller has only one channel
  + atiixp: add cable detection support for ATI IDE (guess from BIOS modes)
- Device mapper changes:
  + dm: allow DM to use whole devices even when some partitions are in use
    (allows EVMS coexistence with the in-kernel partitioning code without
    allowing other types of concurrent usage)
  + dm: fix alloc_dev error path (free minor on blk_alloc_queue() failure)
  + dm snapshot: fix invalidation ENOMEM
  + dm snapshot: fix metadata writing when suspending
  + dm raid1: remove trailing space from 'dmsetup table' output
  + dm: add uevent change event on resume
  + dm: fix find_device race
  + dm suspend: fix error path
  + dm raid1: fix waiting for I/O on suspend
- MD driver changes:
  + send "change" uevent on array start
  + pass down BIO_RW_SYNC in raid{1,10} (fixes large latency in some cases)
  + make 'repair' actually work for raid1
  + make sure the events count in an md array never returns to zero
- DVB driver changes:
  + dvb-core: fix uninitialised variable in dvb_frontend_swzigzag
  + flexcop-usb: fix debug printk
- MTD driver changes:
  + mtd_dataflash: DataFlash is not bit writable
  + mtd_dataflash: prevent oops when MISO has a pulldown instead of pullup
- Network driver changes:
  + tg3: update version from 3.65 to 3.72 (as included in 2.6.20)
  + tg3: avoid an expensive divide in tg3_poll()
  + tulip: disable support for Davicom cards by default (the driver claims
    to support them, but does not really work; the dmfe driver should be
    used with these cards)
- SCSI driver changes:
  + advansys: add PCI ID table for module autoloading
  + gdth: fix && typos
  + qla1280: fix command timeout setting
  + qla1280: fix bus reset
  + qla1280: set residual correctly
  + qla2xxx: add MODULE_FIRMWARE tags for use by mkinitrd
- SATA driver changes:
  + (ahci) PCI quirk: switch ATI SB600 SATA from IDE to AHCI mode
  + ahci: ignore PORT_IRQ_IF_ERR on JMB and ULi M5288 controllers
  + ahci: match PCI class code for AHCI
  + ahci: preserve PORTS_IMPL over host resets
  + ahci: do not mangle saved HOST_CAP while resetting controller
  + ahci: use 0x80 as wait stat value instead of 0xff
  + ahci, sata_nv: move NVIDIA MCP65/67 PCI IDs from sata_nv to ahci
  + sata_mv: add HighPoint 2310 support (88SX7042)
  + sata_nv: SRST sometimes fails after hotplug, use hard reset to resume
  + sata_svw: disable ATAPI DMA on current boards (errata workaround)
  + sata_via: add PCI ID 1106:5337 (VT8237 in IDE mode)
- USB driver changes:
  + ati_remote: fix wrong buffer freeing on disconnect
  + usb-storage: unusual_devs list update:
     + 0421:0433 (Nokia E70): IGNORE_RESIDUE, FIX_CAPACITY
     + 0421:0492 (Nokia 6233): MAX_SECTORS_64
     + 046b:ff40 (AMI Virtual Floppy): NO_WP_DETECT
     + 054c:002c (Sony USB Floppy Drive)
     + 05ac:1204 (Apple iPod): +NOT_LOCKABLE (was FIX_CAPACITY)
     + 08ca:3103 (Aiptek USB Keychain MP3 Player): IGNORE_RESIDUE
     + 0fce:e030 (Sony Ericsson P990i): +IGNORE_RESIDUE (was FIX_CAPACITY)
     + 1019:0c55 (Desknote UCR-61S2B): extend to bcdDevice 0.00 to 1.10
     + 1210:0003 (DigiTech Mass Storage [GNX4]): IGNORE_RESIDUE
     + 12d1:1003 (HUAWEI E220 USB-UMTS Install): IGNORE_DEVICE
     + 14cd:6600 (Super Top IDE DEVICE): IGNORE_RESIDUE
     + 1652:6600 (Teac HD-35PUK-B): IGNORE_RESIDUE
- Filesystem changes:
  + adfs: fix handling of filenames with 8-bit characters
  + ext2: fix error behavior (errors=... options and default stored in SB)
  + ext2: protect ioctl modifying append_only immutable etc with i_mutex
  + ext3: fix wrong error behavior
  + fuse: backported updates from 2.6.20 (adds fuseblk support required
    for recent ntfs-3g versions)
  + nfs: fix SUNRPC wakeup/execute race condition
  + reiserfs: make fsync only use barriers when they are enabled
  + reiserfs: fix missing parameter in warning message
  + reiserfs: fix bad path release panic
  + squashfs: updated to version 3.2 (important bugfixes, NFS export support)
- Network subsystem changes:
  + Bluetooth:
     + handle command complete event for exit periodic inquiry
     + return EINPROGRESS for non-blocking socket calls
     + fix compat ioctl for BNEP, CMTP and HIDP
     + add locking for bt_proto array manipulation
     + check if RFCOMM session is still attached to the TTY
     + more checks if DLC is still attached to the TTY
     + fix uninitialized return value for RFCOMM sendmsg()
  + ipv4/ipv6: fix inet{,6} device initialization order
  + ipv4: IGMP: fix IGMPV3_EXP() normalization bit shift value
  + ipx: fix IPX checksum calculation (0xffff means checksum disabled)
  + ipx: fix NULL pointer dereference on ipx unload
  + netfilter: ebtables: don't compute gap before checking struct type
- Config updates:
  - disabled hdaps driver (CONFIG_SENSORS_HDAPS): #10734 (full version will
    be built in a separate kernel-modules-tp_smapi-* package)

* Fri Dec 22 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.18-alt3
- Applied remaining changes from 2.6.18.5 stable release:
  + bluetooth: Fix unaligned access in hci_send_to_sock.
  + ia64: bte_unaligned_copy() transfers one extra cache line.
  + alpha: Fix ALPHA_EV56 dependencies typo
  + v4l: Do not enable VIDEO_V4L2 unconditionally
  + netfilter: xt_CONNSECMARK: fix Kconfig dependencies
  + netfilter: Kconfig: fix xt_physdev dependencies
  (the rest of 2.6.18.5 changes were already applied earlier)
- Applied changes from 2.6.18.6 stable release:
  + x86_64: Mark rdtsc as sync only for netburst, not for core2
  + bluetooth: Add packet size checks for CAPI messages (CVE-2006-6106)
  + forcedeth: Disable INTx when enabling MSI in forcedeth
  + m32r: Make userspace headers platform-independent
  + softirq: Remove BUG_ONs which can incorrectly trigger
  + mount: skip data conversion in compat_sys_mount when data_page is NULL
  + ARM: Add sys_*at syscalls
  + ieee1394: ohci1394: Add PPC_PMAC platform code to driver probe
  + v4l: Fix broken TUNER_LG_NTSC_TAPE radio support
  + dvb: lgdt330x: Fix signal/lock status detection bug
  + bonding: Fix incorrect bonding state reported via ioctl
  + irda: Fix incorrect TTP header reservation
  + ipsec: Fix inetpeer leak in ipv4 xfrm dst entries.
  + dm snapshot: Fix freeing pending exception
  + xfrm: Use output device disable_xfrm for forwarded packets
  + sunhme: Fix for sunhme failures on x86
  + pkt_sched: act_gact: Fix division by zero
  + netfilter: ip_tables: Revision support for compat code
  + dm crypt: Fix data corruption with dm-crypt over RAID5
  + net_sched: policer: Restore compatibility with old iproute binaries
  + ebtables: Prevent wraparounds in checks for entry components' sizes.
  + ebtables: Deal with the worst-case behaviour in loop checks.
  + ebtables: Verify that ebt_entries have zero ->distinguisher.
  + ebtables: Fix wraparounds in ebt_entries verification.
  + ieee80211: softmac: Remove netif_tx_disable when scanning
- SCSI subsystem fixes:
  + Add missing cdb clearing in scsi_execute()
- Infiniband driver fixes:
  + IB/srp: Fix FMR mapping for 32-bit kernels and addresses above 4G
- Network driver fixes:
  + bonding: Fixes from 2.6.20-rc1:
     + Fix oops when slave device does not provide get_stats
     + Add lockdep annotation
     + Fix deadlock on high loads in bond_alb_monitor()
     + Update version number
     + Fix primary selection error at enslavement time
     + Don't mangle LACPDUs
     + Validate probe replies in ARP monitor
     + Don't release slaves when master is admin down
     + Add priv_flag to avoid event mishandling (fixes oops when bonding is
       used together with VLANs: #10410)
     + Handle large hard_header_len
     + Remove unneeded NULL test
     + Format fix in seq_printf call
     + Convert delay value from s16 to int
     + Allow bonding to enslave a 10 Gig adapter
- SATA driver changes:
  + libata: Use new PCI_VDEVICE() macro to dramatically shorten ID lists
  + ahci, sata_nv: Reformat PCI ID table to match upstream
  + ata_piix: Add Intel ICH9 support (IDE mode)
  + ahci: Add Intel ICH9 support (enhanced AHCI/RAID mode)
  + libata: Use kmap_atomic(KM_IRQ0) in SCSI simulator
- PCI subsystem changes:
  + MSI: Cleanup existing MSI quirks
  + MSI: Factorize common code in pci_msi_supported()
  + MSI: Export the PCI_BUS_FLAGS_NO_MSI flag in sysfs
  + MSI: Rename PCI_CAP_ID_HT_IRQCONF into PCI_CAP_ID_HT
  + MSI: Blacklist PCI-E chipsets depending on Hypertransport MSI capability
  + PCIE: Restore PCI Express capability registers after PM event
  + quirks: Switch quirks code offender to use pci_get API
- Enabled build of the kernel-doc-%%base_flavour subpackage (it was lost when
  moving from 2.6.16 to 2.6.18, because the documentation was built only with
  the -up subflavour, which was removed).
- Removed duplicate provides from the kernel-headers-%%flavour subpackage.
- Fixed mkinitrd version requirements (2.9.9 is needed for swsusp support).
- Replaced modutils with module-init-tools in package dependencies.

* Thu Nov 30 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.18-alt2
- Applied changes from 2.6.18.4 stable release:
  + bridge: fix possible overflow in get_fdb_entries (CVE-2006-5751)
- x86-specific fixes:
  + x86 microcode: don't check the size (fixes problems with some microcode
    updates which are less than 2048 bytes)
- Character driver fixes:
  + agpgart: Allocate AGP pages with GFP_DMA32 by default
- Network driver fixes:
  + tg3: Add missing unlock in tg3_open() error path
  + r8169: Fix iteration variable sign
- Network subsystem fixes:
  + ieee80211 softmac: fix slab corruption in WEP restricted key association
  + ipv4: UDP: Make udp_encap_rcv use pskb_may_pull
  + ipv6: Fix address/interface handling in UDP and DCCP
  + netfilter fixes:
     + add missing check for CAP_NET_ADMIN in iptables compat layer
     + ip_tables: fix error handling in compat code
     + ip_tables: fix module refcount leaks in compat error paths
     + {arp,ip,ip6}_tables: fix missed and reordered checks
     + arp_tables: fix missing unregistration on module unload
     + honour source routing for LVS-NAT
     + H.323 conntrack: fix crash with CONFIG_IP_NF_CT_ACCT
- PCMCIA driver fixes:
  + pcmcia: fix 'rmmod pcmcia' with unbound devices
- SCSI driver fixes:
  + clear garbage after CDBs on SG_IO (fixes problems with ATAPI devices)
- Filesystem fixes:
  + fuse: fix Oops in lookup

* Sun Nov 26 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.18-alt1
- Version 2.6.18.
- Renamed kernel variant from std26 to std.
- Spec file reworked for use with gear (removed macros from Name, Version,
  Release fields, now using %%name, %%version, %%release values to define other
  macros instead).
- Moved to git - removed everything related to separate patch packages; now
  src.rpm contains only a single combined patch between the vanilla release and
  the packaged version.
- Removed %%set_kernel_arches and %%get_kernel_config macros - config files are
  now included in the combined patch instead of separate source files.
- Switched to gcc 4.1.
- Updated %%install for new location of internal bttv headers (some files were
  moved from drivers/media/video/ to drivers/media/video/bt8xx/).
- Removed audio.ko and usb-midi.ko modules from kernel-modules-oss-%%flavour
  (these OSS drivers were declared obsolete and removed from the kernel).
- Removed all %%__* macro abuse from spec.
- Reworked kernel-headers-%%flavour subpackage: now it contains headers
  sanitized for userspace (by "make headers_install") instead of raw kernel
  headers which were there in previous releases.
- Moved kernel header files to /usr/src instead of symlinking include directory
  from /usr/include (should fix problems with broken build systems of
  proprietary modules).
- Moved kernel sources to /usr/src/linux-%%kversion-%%flavour-%%krelease
  instead of /usr/src/linux-%%kversion-%%flavour; old directory name is still
  available as symlink.
- Added information about SMP alternatives to %%description.
- i586: Switched from CONFIG_HIGHMEM64G to CONFIG_HIGMMEM4G to avoid PAE
  requirement; a separate kernel variant with CONFIG_HIGHMEM64G will be made.
  Added notes about PAE and maximum addressable RAM to %%description.
- Applied changes from 2.6.18.3 stable release:
  + cifs: fix POSIX locking return code when server does not have support
  + cifs: report rename failure when target file is locked by Windows
  + cciss: fix iostat
  + cpqarray: fix iostat
  + Char: isicom, fix close bug
  + block: Fix bad data direction in SG_IO
  + pci: don't try to remove sysfs files before they are setup.
  + Patch for nvidia divide by zero error for 7600 pci-express card
  + CPUFREQ: Make acpi-cpufreq unsticky again.
  + security/seclvl.c: fix time wrap (CVE-2005-4352)
  + fix via586 irq routing for pirq 5
  + NET: Set truesize in pskb_copy
  + TCP: Don't use highmem in tcp hash size calculation.
  + correct keymapping on Powerbook built-in USB ISO keyboards
  + x86_64: Fix FPU corruption
  + Input: psmouse - fix attribute access on 64-bit systems
  + NET: __alloc_pages() failures reported due to fragmentation
  + e1000: Fix regression: garbled stats and irq allocation during swsusp
  + usbtouchscreen: use endpoint address from endpoint descriptor
  + USB: failure in usblp's error path
  + init_reap_node() initialization fix
  + ipmi_si_intf.c sets bad class_mask with PCI_DEVICE_CLASS
  + fix UFS superblock alignment issues
  + SPARC: Fix missed bump of NR_SYSCALLS.
  + Fix sys_move_pages when a NULL node list is passed.
  + SPARC64: Fix futex_atomic_cmpxchg_inatomic implementation.
  + POWERPC: Make alignment exception always check exception table
  + S390: user readable uninitialised kernel memory, take 2.
  + usbfs: private mutex for open, release, and remove
  + md: check bio address after mapping through partitions.
  + IPV6: fix lockup via /proc/net/ip6_flowlabel [CVE-2006-5619]
  + tcp: cubic scaling error
  + JMB 368 PATA detection
  + fill_tgid: fix task_struct leak and possible oops
  + Use min of two prio settings in calculating distress for reclaim
  + vmscan: Fix temp_priority race
  + NFS: nfs_lookup - don't hash dentry when optimising away the lookup
  + Reintroduce NODES_SPAN_OTHER_NODES for powerpc
  + PCI: Remove quirk_via_abnormal_poweroff
  + SPARC64: Fix PCI memory space root resource on Hummingbird.
  + ISDN: fix drivers, by handling errors thrown by ->readstat()
  + ISDN: check for userspace copy faults
  + rtc-max6902: month conversion fix
  + posix-cpu-timers: prevent signal delivery starvation
  + fix Intel RNG detection
  + Watchdog: sc1200wdt - fix missing pnp_unregister_driver()
  + ALSA: snd_rtctimer: handle RTC interrupts with a tasklet
  + uml: remove warnings added by previous -stable patch
  + uml: make Uml compile on FC6 kernel headers
  + x86-64: Fix C3 timer test
  + SCTP: Always linearise packet on input
  + NET: Fix skb_segment() handling of fully linear SKBs
  + fix missing ifdefs in syscall classes hookup for generic targets
  + SCSI: aic7xxx: pause sequencer before touching SBLKCTL
  + sky2: 88E803X transmit lockup (2.6.18)
  + Fix potential interrupts during alternative patching
  + fuse: fix hang on SMP
  + IB/mthca: Use mmiowb after doorbell ring
  + IPoIB: Rejoin all multicast groups after a port event
  + SCSI: aic7xxx: avoid checking SBLKCTL register for certain cards
  + knfsd: Fix race that can disable NFS server.
  + md: Fix calculation of ->degraded for multipath and raid10
  + md: Fix bug where spares don't always get rebuilt properly when they become
    live.
  + ALSA: Fix re-use of va_list
  + DVB: fix dvb_pll_attach for mt352/zl10353 in cx88-dvb, and nxt200x
  + bcm43xx: fix watchdog timeouts.
  + SPARC64: Fix memory corruption in pci_4u_free_consistent().
  + SPARC64: Fix central/FHC bus handling on Ex000 systems.
  + JFS: pageno needs to be long
  + Bluetooth: Check if DLC is still attached to the TTY
  + SERIAL: Fix oops when removing suspended serial port
  + SERIAL: Fix resume handling bug
  + Fix uninitialised spinlock in via-pmu-backlight code.
  + SCSI: DAC960: PCI id table fixup
  + uml: fix processor selection to exclude unsupported processors and features
  + sky2: GMAC pause frame
  + sky2: accept multicast pause frames
  + ALSA: Repair snd-usb-usx2y for usb 2.6.18
  + ALSA: Fix bug in snd-usb-usx2y's usX2Y_pcms_lock_check()
  + ALSA: Dereference after free in snd_hwdep_release()
  + sound/pci/au88x0/au88x0.c: ioremap balanced with iounmap
  + ALSA: powermac - Fix Oops when conflicting with aoa driver
  + ALSA: emu10k1: Fix outl() in snd_emu10k1_resume_regs()
  + sky2: turn off PHY IRQ on shutdown
  + sky2: pause parameter adjustment
  + sky2: MSI test race and message
  + mm: fix a race condition under SMC + COW
  + __div64_32 for 31 bit.
  + splice: fix pipe_to_file() ->prepare_write() error path
  + Fix sfuzz hanging on 2.6.18
  + add utsrelease.h to the dontdiff file
  + V4L: copy-paste bug in videodev.c
  + block layer: elv_iosched_show should get elv_list_lock
  + NETFILTER: NAT: fix NOTRACK checksum handling
  + bcm43xx: fix regressions in 2.6.18
  + x86-64: Calgary IOMMU: Fix off by one when calculating register space
    location
  + ide-generic: jmicron fix
  + scx200_hrt: fix precedence bug manifesting as 27x clock in 1 MHz mode
  + invalidate_inode_pages2(): ignore page refcounts
  + rtc driver rtc-pcf8563 century bit inversed
  + fbdev: correct buffer size limit in fbmem_read_proc()
  + mm: bug in set_page_dirty_buffers
  + TCP: Fix and simplify microsecond rtt sampling
  + MD: Fix problem where hot-added drives are not resynced.
  + IPV6: Disable SG for GSO unless we have checksum
  + PKT_SCHED: cls_basic: Use unsigned int when generating handle
  + sata_mv: fix oops
  + SPARC64: Fix sparc64 ramdisk handling
  + IPV6: bh_lock_sock_nested on tcp_v6_rcv
  + CPUFREQ: Fix some more CPU hotplug locking.
  + SPARC64: Fix serious bug in sched_clock() on sparc64
  + Fix VIDIOC_ENUMSTD bug
  + load_module: no BUG if module_subsys uninitialized
  + i386: fix flat mode numa on a real numa system
  + cpu to node relationship fixup: map cpu to node
  + cpu to node relationship fixup: acpi_map_cpu2node
  + backlight: fix oops in __mutex_lock_slowpath during head
    /sys/class/graphics/fb0/*
  + do not free non slab allocated per_cpu_pageset
  + rtc: lockdep fix/workaround
  + i386 bootioremap / kexec fix
  + powerpc: Fix ohare IDE irq workaround on old powermacs
  + sysfs: remove duplicated dput in sysfs_update_file
  + powerpc: fix building gdb against asm/ptrace.h
  + Remove offsetof() from user-visible <linux/stddef.h>
  + Clean up exported headers on CRIS
  + Fix v850 exported headers
  + Don't advertise (or allow) headers_{install,check} where inappropriate.
  + Remove UML header export
  + Remove ARM26 header export.
  + Fix H8300 exported headers.
  + Fix m68knommu exported headers
  + Fix exported headers for SPARC, SPARC64
  + Fix 'make headers_check' on m32r
  + Fix 'make headers_check' on sh64
  + Fix 'make headers_check' on sh
  + Fix ARM 'make headers_check'
  + One line per header in Kbuild files to reduce conflicts
  + sky2 network driver device ids
  + sky2: tx pause bug fix
  + netdrvr: lp486e: fix typo
  + mv643xx_eth: fix obvious typo, which caused build breakage
  + zone_reclaim: dynamic slab reclaim
  + Fix longstanding load balancing bug in the scheduler
  + jbd: fix commit of ordered data buffers
  + ALSA: Fix initiailization of user-space controls
  + USB: Allow compile in g_ether, fix typo
  + IB/mthca: Fix lid used for sending traps
  + S390: user readable uninitialised kernel memory (CVE-2006-5174)
  + zd1211rw: ZD1211B ASIC/FWT, not jointly decoder
  + V4L: pvrusb2: Limit hor res for 24xxx devices
  + V4L: pvrusb2: Suppress compiler warning
  + V4L: pvrusb2: improve 24XXX config option description
  + V4L: pvrusb2: Solve mutex deadlock
  + DVB: cx24123: fix PLL divisor setup
  + V4L: Fix msp343xG handling regression
  + UML: Fix UML build failure
  + uml: use DEFCONFIG_LIST to avoid reading host's config
  + uml: allow using again x86/x86_64 crypto code
  + NET_SCHED: Fix fallout from dev->qdisc RCU change
- Other security-related fixes:
  + moxa: sanity check dltmp.len size before all copy_from_user() calls
  + x86_64: fix local DoS due to NT/AC flags leak through sysenter
- Build fixes:
  + add and use in-kernel unifdef utility for "make headers_install"
- Core changes:
  + run_init_process: Print init program name before trying to run it
  + Change list of executables which the kernel tries to run as init
  + sys_syslog: check open permission for reading and getting unread count
  + security: allow reads from an open /proc/kmsg fd by unprivileged processes
  + add ServerWorks LE chipset to the PM timer graylist
  + make dev_printk usable from non-GPL modules again
  + x86: Add acpi_user_timer_override option for Asus boards (workaround for
    ALT bug #9888)
  + x86_64: stack unwinder crash fix
  + i386/x86_64: ACPI cpu_idle_wait() fix
- ACPI changes:
  + Add support for DSDT override through initramfs; patch from
    http://gaugusch.at/kernel.shtml
  + Show device attributes in sysfs under /sys/firmware/acpi/namespace
  + i386 blacklist: IBM ThinkPad 600E needs acpi=noirq
  + fix oops on processor module unload when ACPI is disabled
  + fix incorrect handling of PCI Express Root Bridge _HID
  + remove deferred execution from global lock acquire wakeup path
  + fix potential oops in power driver
  + fix acpi_pci_link_set() using GFP_KERNEL with interrupts off during resume
  + fix printk format warnings
  + asus_acpi: add W3000 (W3V) support
  + asus_acpi: fix proc files parsing
  + asus_acpi: don't printk on writing garbage to proc files
  + battery: check battery status on resume for un/plug events during sleep
  + sbs: check for NULL device pointer
- Block driver changes:
  + block/scsi_ioctl.c: fix bad data direction in SG_IO
  + cciss: add support for >2TB logical volumes
  + cciss: remove unneeded spaces in output for attached volumes
  + cciss: fix warnings (and bug on 1TB discs)
- Bluetooth driver changes:
  + hci_usb: add support for Canyon CN-BTU1 dongle
  + hci_usb: add support for newer ANYCOM USB dongles (USB-200 and USB-250)
  + dtl1_cs: add missing entry for Nokia DTL-4 PCMCIA card
- Character driver changes:
  + ipmi: clean up the waiting message queue properly on unload
  + ipmi: retry messages on certain error returns
  + ipmi_si_intf: fix uninitialized data bug
  + ipmi_si_intf: fix return codes in failure case
  + ipmi_si_intf: fix "&& 0xff" typos
  + AGPGART changes:
    + Intel 965 Express support
    + Rework AGPv3 modesetting fallback
    + Apply errata workarounds in all cases
- Hardware monitor driver fixes:
  + atxp1: Signed/unsigned char bug fix
  + hdaps: Handle errors from input_register_device
  + hdaps: support Lenovo ThinkPad T60
  + i2c-isa: Restore driver owner
  + smsc47m1: List the SMSC LPC47M112 as supported
  + smsc47m1: dev_warn fix
- Hardware monitor driver updates:
  + it87: Add support for the IT8716F
  + it87: Add support for the IT8718F
  + it87: No sysfs files for disabled fans
  + it87: Prevent overflow on fan clock divider write
  + it87: in8 has no limit registers
  + it87: Overwrite broken default limits
  + k8temp: New driver for builtin temperature sensors of AMD K8 CPUs
  + vt1211: New driver for the VIA VT1211 Super-IO chip (an older version of
    this driver was available in kernel-modules-vt1211-* packages)
- I2C driver changes:
  + i2c-viapro: add support for VT8237A and VT8251
- IDE driver changes:
  + amd74xx: Add NVIDIA MCP67 support (10de:0560)
  + generic: Allow ide_generic_all to be used modular and built in
  + ide-cs: Add new device IDs
  + ide-io: IDE error handling fixes
- MD driver fixes:
  + md: fix up maintenance of ->degraded in multipath
  + md: fix /proc/mdstat refcounting
  + md: make messages about resync/recovery etc more specific
- MMC/SD driver fixes:
  + mmc: use own work queue
  + mmc: fix MMIO vs memory races in sdhci
  + mmc: avoid some resets without card
- MMC/SD driver updates:
  + tifm: New driver for TI Flash Media card readers (although these readers
    support multiple card types, this driver supports only MMC/SD cards)
- Networking changes:
  + ieee80211: Update to version 1.2.15 from ieee80211.sf.net (mostly the same
    code as included in 2.6.19-rc1)
  + ieee80211: don't flood log with errors from buggy APs
- Network driver fixes:
  + PPP MPPE: do not accept unsupported MPPE options
  + PPPOE: Advertise PPPoE MTU
  + bcm43xx: Drain TX status before starting IRQs
- Network driver updates:
  + r8169: updated to the newer version from 2.16.19-rc5 (adds support for new
    devices and fixes several bugs, including hang with PCMCIA cards)
- Network config changes:
  + sk98lin: no longer built together with the kernel (the in-kernel version is
    obsolete); use skge/sky2, or install a separately built
    kernel-modules-sk98lin-* package with the vendor driver
- PCI subsystem changes:
  + Add 'unhide_smbus' boot option to unhide SMBus controllers
  + VIA IRQ quirk behaviour change (should fix regression since 2.6.16.17)
  + reset pci device state to unknown state for resume
  + add ICH7/8 ACPI/GPIO io resource quirks
- SATA driver changes:
  + ide/libata: fix SCSI_SATA_INTEL_COMBINED setting with modular IDE
  + ahci: add SiS PCI IDs (1039:{1184,1185,0186})
  + sata_sil: remove unaffected drives from m15w blacklist
  + Fix libata resource conflict for legacy mode
  + libata: return sense data in HDIO_DRIVE_CMD ioctl
  + sata_promise: add PCI ID (105a:3577)
  + libata: refuse to register IRQless ports
  + libata: Print out Status register, if a BSY-sleep takes too long
  + libata: turn off NCQ if queue depth is adjusted to 1
  + ata_piix: use correct map_db values for ICH8
  + ata_piix: allow 01b MAP for both ICH6M and ICH7M
  + ahci: fix status register check in ahci_softreset
  + sata_nv: Add PCI IDs for MCP67 (10de:{0550,0551,0552,0553)
  + ahci: Add support for AHCI controllers of MCP67 (10de:{0554-055b})
  + sata_via: fix broken test for ATA_PFLAG_LOADING
  + libata: fix double-completion on error
- SCSI driver changes:
  + add new devices to the quirk list:
     + EMC Invista (supports sparse LUNs and large LUNs)
     + Tornado F4 (disable report LUN support)
     + NEC iStorage (support the report LUNs opcode)
     + several HP and Hitachi devices which support sparse LUNs and large LUNs
  + megaraid_mbox: add support for change_queue_depth
  + megaraid_mbox, megaraid_mm: 64-bit DMA capability fix
- SCSI/RAID driver updates:
  + 3w-9xxx: Updated driver to version 2.26.02.008:
     + free irq handler in __twa_shutdown()
     + serialize reset code
     + add support for 9650SE controllers
  + arcmsr: New driver for Areca SATA RAID controllers (version 1.20.00.13);
    previously this driver was available in kernel-modules-areca-* packages
  + stex: New driver for Promise SuperTrak EX8350/8300/16350/16300 controllers
- USB driver fixes:
  + usb: deal with broken config descriptors
  + usb-storage: unusual_devs entry for Lacie DVD+-RW
  + usb-storage: unusual_dev entry for Sony P990i
  + usb-storage: add rio karma eject support
  + usb-storage: fix for UFI LUN detection
  + usb-storage: unusual-devs entry for Nokia E60
  + usb-storage: unusual_devs entry for Nokia 6131
  + usb-storage: Mitsumi USB FDD 061M: UNUSUAL_DEV multilun fix
  + usb-storage: unusual_devs entry for Nokia 6234
  + usb-storage: fix unusual_devs entry for Cowon iAUDIO M5
- Filesystem changes:
  + fs/buffer.c: fix grow_buffers() infinite loop on out-of-range block number
  + cifs: support deep tree mounts (e.g. mounts to //server/share/path)
  + cifs: fix readdir breakage when blocksize set too small
  + cifs: allow null user connections with "username="
  + cifs: avoid flood of "close with pending write" messages
  + cifs: fix mount failure when domain not specified
  + cramfs: add a sanity check to avoid oops on corrupted filesystem
  + cramfs: fix error checking during initialization
  + ext3: handle directory corruption better (fix log spew and infinite loop)
  + hfs: fix oops on attempt to mount a corrupted filesystem
- Block layer changes:
  + Disable bd_claim check between whole devices and partitions (for using EVMS
    together with the kernel partition support)
- Added SquashFS 3.1 filesystem support.
- Added Unionfs 1.4 filesystem support.

* Wed Oct 25 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.16-alt13
- Patches updated up to 2.6.16.30-rc1.
- Updated kernel-fix-build:
  + add -fno-stack-protector for new gcc
  + build vDSO with -Wl,--hash-style=sysv for compatibility with older glibc
- Updated kernel-fix-core:
  + textsearch: ts_bm: fix initialization bug
- Updated kernel-fix-drivers-i2c:
  + i2c: fix 'ignore' module parameter handling
- Updated kernel-fix-drivers-ide:
  + amd74xx: AMD756 does not support host side cable detection
  + amd74xx: add NVIDIA MCP61 IDE support: 10de:03ec
  + amd74xx: add NVIDIA MCP65 IDE support: 10de:0448
  + atiixp: add ATI SB600 IDE support: 1002:438c
  + generic: add all_generic_ide module parameter
  + ide-cd: quiet down GPCMD_READ_CDVD_CAPACITY failure
  + ide: fix /proc/ide/*/media reporting for optical (MO) devices
  + ide: if the id fields looks screwy, disable DMA
  + ide_cs: add IBM microdrive to known IDs
  + ide_cs: add new device IDs
  + it821x: fix ATAPI DMA problem
  + it821x: only enable DMA for a valid speed setting
  + sis5513: add SiS 966 and 968 IDE support: 1039:{0966,0968}
  + sis5513: add SiS5517 ATA16 chipset support: 1039:5517
  + sis5513: fix broken timing setup
- Updated kernel-fix-drivers-media:
  + added drivers/media patches from 2.6.16.30-rc1:
    + Backport the budget driver DISEQC instability fix
    + Backport fix to artec USB DVB devices
    + Fix budget-av frontend detection
    + TDA8290 update
    + TDA10046 Driver update
    + Add drivers/media/video/saa7134/saa7134-input.c:flydvb_codes
    + Added support for the new Lifeview hybrid cardbus modules
    + Corrected CVBS input for the AVERMEDIA 777 DVB-T
    + Added PCI IDs of 2 LifeView Cards
    + Saa7134: select FW_LOADER
    + Medion 7134: Autodetect second bridge chip
    + Saa7134: make unsupported secondary decoder message generic
    + Saa7134: add support for AVerMedia A169 Dual Analog tuner card
    + Saa7134: document that there's also a 220RF from KWorld
    + ELSA EX-VISION 700TV: fix incorrect PCI subsystem ID
    + Kworld ATSC110: initialize the tuner for analog mode on module load
    + Kworld ATSC110: cleanups
    + Kworld ATSC110: enable composite and svideo inputs
    + KWorld ATSC110: implement set_pll_input
    + Add support for Kworld ATSC110
    + Add saa713x card: ELSA EX-VISION 700TV (saa7130)
    + Added support for the Tevion DVB-T 220RF card
    + Added support for the ADS Instant TV DUO Cardbus PTV331
    + Added support for the LifeView FlyDVB-T LR301 card
    + Add support for the Avermedia 777 DVB-T card
- Added kernel-fix-drivers-mmc:
  + mmc_block: always use a sector size of 512 bytes even for cards >= 2G
- Updated kernel-fix-drivers-net:
  + winbond-840: fix bad calls to pci_map_single (#10177)
  + via-velocity: fix link detection
  + via-velocity: fix speed and link status reported by ethtool
  + sky2: use dev_alloc_skb for receive buffers
  + sky2: fix fiber support
  + pppoe: advertise correct MTU for PPP channel
- Updated kernel-fix-drivers-scsi:
  + megaraid_{mm,mbox}: fix a bug in reset handler
  + megaraid_mbox: fix section mismatch warnings
  + megaraid_{mm,mbox}: 64-bit DMA capability checker
  + megaraid_{mm,mbox}: fix INQUIRY with EVPD
  + megaraid_mbox: sdd support for change_queue_depth
  + megaraid_{mm,mbox}: 64-bit DMA capability fix
  + ahci: add ATI SB600 support: 1002:{4380,4381}
  + ahci: add NVIDIA MCP65 support: 10de:{044c,044d,044e,044f}
  + ahci: add SiS 966 and 968 support: 1039:{1184,1185,0186}
  + ahci: add VIA VT8251 support (restore lost patch from 2.6.14): 1106:3349
  + sata_nv: add NVIDIA MCP61 support: 10de:{03e7,03f6,03f7}
  + sata_nv: add more PCI IDs: 10de:{045c,045d,045e,045f}
  + sata_promise: add FastTrak TX4300/TX4310 (PDC40719) support: 105a:3515
  + sata_sil24: add PCI ID for another SiI3124 variant: 8086:3124
  + sata_via: add VIA VT8237A support: 1106:0591
- Updated kernel-fix-drivers-usb:
  + yealink: fix unload oops and memory leak
  + usbhid: ignore Yealink devices which should be handled by the yealink
    driver
- Updated kernel-fix-drivers-video:
  + fbdev: add modeline for 1680x1050@60
- Updated kernel-fix-fs:
  + fix fdset leakage due to freeing fdsets of wrong size
  + cifs: fix possible NULL dereference
  + cifs: fix unlink oops in rename error path
  + cifs: add another NULL check in the unlink path
  + cifs: allow cifsd to suspend if connection is lost
- Updated kernel-fix-net:
  + pfkeyv2: fix inconsistent typing in struct sadb_x_kmprivate
  + ipv6: Sum real space for RTAs (fixes RTNLGRP_IPV6_IFINFO netlink
    notifications)
  + pkt_sched: cls_basic: use unsigned int when generating handle
- Updated kernel-fix-security:
  + CVE-2006-4623: dvb-core: handle ULE SNDU length of 0 properly
  + CVE-2006-4997: atm: clip: fix use-after-free in clip_mkip()

* Tue Oct 10 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.16-alt12
- Updated kernel-fix-security:
  + fixed broken eflags-save-restore patch for x86_64

* Sun Oct 08 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.16-alt11
- Updated kernel-fix-acpi:
  + blacklist IBM ThinkPad 600E which needs acpi=noirq (#9859)
- Updated kernel-fix-core:
  + idr: convert internal locking to _irqsave variant
  + fix race in usermodehelper
  - removed old (2.6.9) headers-fix patch which actually was breaking use of
    kernel headers for userspace compilation (ldv, see #5409)
- Updated kernel-fix-drivers-char:
  + n_tty: update tty->receive_room _before_ calling the driver unthrottle
    routine that prevents stalling PPP connections over ptys (lakostis)
  + via-agp: add VIA PT880 Ultra support
- Updated kernel-fix-drivers-net:
  + update e1000 driver to the version from linux-2.6.17 (#10053, adds
    631xESB/632xESB (ESB2) support)
- Updated kernel-fix-security:
  + x86, x86_64: fix local DoS due to NT flag leak through sysenter
- kernel-headers-%%flavour: add provides for compatibility with old
  kernel-headers-std-* packages (ldv).
- Add "export ARCH=%%base_arch" to %%build and %%install (#9808).

* Tue Sep 12 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.16-alt10
- Patches updated up to 2.6.16.29-rc2.
- Updated kernel-fix-core:
  + pdflush: handle resume wakeups
  + futex: fix misoptimization in unqueue_me()
  + idr: fix race in idr code
- Updated kernel-fix-drivers-block:
  + block: fix bounce limit address check (fixes some OOMs on 64-bit systems)
- Updated kernel-fix-drivers-char:
  + tty: serialize flush_to_ldisc() to fix buffer list corruption on SMP
  + amd64-agp: fix nforce3 suspend/resume on amd64
  + intel-agp: add support for Intel 946GZ, 965G, 965Q
  + intel-agp: fix number of aperture sizes in 830 gart structs
- Updated kernel-fix-drivers-ide:
  + ide-io: increase timeout value to allow for slave wakeup
  + pci_ids.h: add some VIA IDE identifiers
  + via82cxxx: add VT8237A support
  + alim15x3: add ULI M5229 (rev c8) support
- Updated kernel-fix-drivers-ieee1394:
  + ohci1394: fix broken suspend/resume
  + sbp2: enable auto spin-up for Maxtor disks
- Added kernel-fix-drivers-infiniband:
  + IB/mthca: restore missing PCI registers after reset
- Updated kernel-fix-drivers-md:
  + md: raid1: fix a potential NULL dereference
- Updated kernel-fix-drivers-scsi
  + aic79xx: use BIOS settings
- Updated kernel-fix-fs:
  + fix missing ret assignment in __bio_map_user() error path
  + debugfs: fix inode leak
  + fs/namei.c: fix struct file leak due to unreleased open intent data
- Updated kernel-fix-net:
  + ipv6: fix source address selection
  + ipv6 addrconf: fix default source address selection without
    CONFIG_IPV6_PRIVACY
  + sctp: reject packets with broadcast addresses
  + sctp: fix persistent slowdown when a gap ack consumes rx buffer
  + sctp: limit association max_retrans setting in setsockopt
  + sctp: reset rtt_in_progress for the chunk when processing its sack
  + sctp: send only 1 window update SACK per message
  + ulog: fix panic on SMP kernels
  + ip_tables: fix locking in ipt_do_table
  + ethtool: fix ETHTOOL_GUFO typo
  + ethtool: fix oops in ethtool_set_pauseparam()
  + ipv6: fix kernel oops when setting sticky socket options
  + pktgen: fix oops when used with balance-tlb bonding due to uninitialized
    skb->{nh,h}
  + pktgen: make sure skb->{nh,h} are initialized in fill_packet_ipv6() too
- Updated kernel-fix-security:
  + CVE-2006-2936: USB serial ftdi_sio: prevent userspace DoS
  + CVE-2006-2935: cdrom: fix bad cgc.buflen assignment
  + CVE-2006-4145: udf: fix possible deadlock and memory corruption.  Warning:
    the fix will limit maximum size of files written to UDF filesystems to 1GB;
    existing files bigger than 1GB still can be read.
  + CVE-2006-3745: sctp: fix privilege elevation through abort handling
  + CVE-2006-3745: sctp: fix bug in the previous patch
  + CVE-2006-3468: ext3: avoid triggering ext3_error on bad NFS file handle
  + CVE-2006-3468: ext3: reject file handles with bad inode numbers early
  + ext2: reject file handles with bad inode numbers early (like CVE-2006-3468,
    but for ext2)

* Sun Jul 16 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.16-alt9
- Patches updated up to 2.6.16.26.
- Updated kernel-fix-security:
  + CVE-2006-3626: fix local privilege escalation through /proc race

* Fri Jul 07 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.16-alt8
- Patches updated up to 2.6.16.24.
- Updated kernel-fix-core:
  + check_process_timers: fix possible lockup
- Updated kernel-fix-drivers-scsi:
  + scsi_lib.c: properly count the number of pages in scsi_req_map_sg()
  + I2O: bugfixes to get I2O working again
- Updated kernel-fix-drivers-usb:
  + whiteheat: fix firmware spurious errors
- Updated kernel-fix-fs:
  + add missing error checking for intent's filp in open_namei()
  + fix call to file_permission() under a spinlock in do_lookup_path()
  + jfs: fix multiple errors in metapage_releasepage
- Updated kernel-fix-security:
  + CVE-2006-2445: run_posix_cpu_timers: remove a bogus BUG_ON()
  + CVE-2006-3085: netfilter: xt_sctp: fix endless loop caused by 0 chunk
    length
  + CVE-2006-2934: netfilter: sctp conntrack: fix crash triggered by packet
    without chunks
  + CVE-2006-2451: fix prctl privilege escalation and suid_dumpable

* Sun Jun 18 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.16-alt7
- Patches updated up to 2.6.16.20.
- Moved kernel-fix-security to the start of patch list.
- Updated kernel-feat-net-ieee80211:
  + fix wrong value for 802.11a channel count
- Updated kernel-fix-acpi:
  + processor: work around oops on powernow-k8 unload
- Updated kernel-fix-core:
  + fix swsusp resume triggered from old-style initrd
  + cpuset: might sleep checking zones allowed fix
  + x86_64: add crashdump trigger points
  + x86_64: don't do syscall exit tracing twice
- Added kernel-fix-drivers-input:
  + psmouse: fix new device detection logic
- Updated kernel-fix-drivers-ieee1394:
  + ohci1394, sbp2: fix "scsi_add_device failed" with PL-3507 based devices
  + sbp2: backport read_capacity workaround for iPod
  + sbp2: fix check of return value of hpsb_allocate_and_register_addrspace
- Updated kernel-fix-drivers-net:
  + b44: initialize the chip earlier, so that changing the MAC address before
    the interface is up will work (bug #9672)
  + b44: check that the MAC address from EEPROM or user input is valid
  + b44: disable tx pause frame support by default due to hardware bug
  + b44: x86_64: check for bad dma address in 1GB DMA workaround
- Updated kernel-fix-drivers-pci:
  - removed broken VIA IRQ fixup patches
- Updated kernel-fix-drivers-scsi:
  + fix libata resume lockup on some machines
- Updated kernel-fix-fs:
  + tmpfs: time granularity fix for inode times going backwards
- Updated kernel-fix-security:
  + CVE-2006-1343: netfilter: fix small information leak in SO_ORIGINAL_DST

* Fri May 26 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.16-alt6
- Patches updated up to 2.6.16.18.
- Updated kernel-fix-security:
  + CVE-2006-1858: SCTP: respect the real chunk length when walking parameters
  + CVE-2006-1857: SCTP: validate the parameter length in HB-ACK chunk
  + CVE-2006-2444: netfilter: SNMP NAT: fix memory corruption

* Sat May 20 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.16-alt5
- Patches updated up to 2.6.16.16 + 2.6.16-stable queue.
- Updated kernel-fix-core:
  + make vm86 call audit_syscall_exit()
  + clean up broken asm in vm86 syscall audit code
  + remove cond_resched in gather_stats()
  + add migratepage address space op to shmem
  + page migration: fix fallback behavior for dirty pages
  + fix ptrace_attach()/ptrace_traceme()/de_thread() race
  + ptrace_attach: fix possible deadlock schenario with irqs
- Updated kernel-fix-drivers-block:
  + ub: fix oops in block_uevent()
  + block layer: limit request_fn recursion
- Updated kernel-fix-drivers-char:
  + tipar: fix oops when compiled into the kernel
- Updated kernel-fix-drivers-i2c:
  + scx200_acb: fix resource name use after free
- Updated kernel-fix-drivers-md:
  + md: avoid oops when attempting to fix read errors on raid10
- Updated kernel-fix-drivers-net:
  + via-rhine: zero pad short packets on Rhine I ethernet cards
  + tg3: fix ethtool always reporting port is TP
- Updated kernel-fix-drivers-pci:
  + PCI quirk: do not unhide Intel SMBus controller if ACPI suspend is enabled
    (unhiding SMBus kills thermal management after suspend on many laptops)
  + PCI quirk: run VIA IRQ fixup only for VIA southbridges
  + PCI quirk: fix the previous VIA IRQ fixup fix (add VIA 82C586 PCI IDs)
  + PCI ACPI: correctly allocate return buffers for _OSC calls
  + PCI quirk: add 'unhide_smbus' boot option to unhide SMBus controllers
    disabled by BIOS
- Updated kernel-fix-drivers-pcmcia:
  + cardman 40x0: fix udev device creation
- Updated kernel-fix-fs:
  + fix sys_flock() race which could result in double free
  + tmpfs: decrement i_nlink correctly in shmem_rmdir()
  + smbfs: fix slab corruption in samba error path
  + fix typo in compat_sys_ppoll()
- Updated kernel-fix-security:
  + CVE-2006-1527: netfilter: sctp conntrack: fix infinite loop
  + CVE-2006-1864: smbfs: fix chroot issue
  + CVE-2006-2272: SCTP: fix panic when receiving fragmented SCTP control
    chunks
  + CVE-2006-2271: SCTP: fix state table entries for chunks received in CLOSED
    state
  + CVE-2006-2275: SCTP: allow spillover of receive buffer to avoid deadlock
  + CVE-2006-2274: SCTP: prevent possible infinite recursion with multiple
    bundled DATA
  + CVE-2006-1860: fs/locks.c: fix lease_init
  + CVE-2006-0039: netfilter: fix do_add_counters race

* Sun Apr 30 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.16-alt4
- Patches updated up to 2.6.16.11 + 2.6.16-stable queue.
- Added kernel-feat-net-ieee80211: update IEEE 802.11 subsystem to version
  1.1.13 (required for newer version of Intel wireless drivers).
- Updated kernel-fix-core:
  + x86_64: pass -32 to the assembler when compiling the 32bit vsyscall pages
  + x86_64: fix a race in the free_iommu path
  + backport for_each_possible_cpu() into 2.6.16
  + x86/PAE: fix pte_clear for the >4GB RAM case
- Updated kernel-fix-drivers-char:
  + cs5535_gpio: call cdev_del() during module_exit
  + sonypi: correct detection of new ICH7-based laptops
- Updated kernel-fix-drivers-md:
  + dm snapshot: fix kcopyd destructor
  + dm: fix dm_suspend() cancellation
- Updated kernel-fix-drivers-media:
  + get_dvb_firmware: download nxt2002 firmware from new driver location
  + fix saa7129 support in saa7127 module for pvr350 tv out
  + cxusb-bluebird: power down corrupts frontend
- Updated kernel-fix-drivers-net:
  + e1000: update truesize with the length of the packet for packet split
- Updated kernel-fix-drivers-usb:
  + fix array overrun in drivers/usb/serial/option.c
- Updated kernel-fix-fs:
  + simplify /proc/devices and fix early termination regression
  + reiserfs: fix acl-related deadlock
  + LSM: add missing hook to do_compat_readv_writev()
- Updated kernel-fix-security:
  + CVE-2006-1863: cifs: don't allow a backslash in a path component
  + fix FP exception handling broken by the CVE-2006-1056 fix

* Sun Apr 23 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.16-alt3
- Patches updated up to 2.6.16.9 + 2.6.16-stable queue.
- Updated kernel-fix-core:
  + fix buddy list race that could lead to page lru list corruptions
  + RLIMIT_CPU: fix handling of a zero limit
  + fix suspend with traced tasks
  + fix non-leader exec under ptrace
  + ipc: fix access to unmapped vmalloc area in grow_ary()
  + apm: fix the "apm: set display: Interface not engaged" error on Armada
    laptops again
  + add more prevent_tail_call() to fix userspace register corruption
- Updated kernel-fix-drivers-block:
  + cciss: fix crash when running hpacucli
- Updated kernel-fix-drivers-char
  + efficeon-agp: add missing memory mask
  + ipmi: fix buffer overflow in BT code
- Updated kernel-fix-drivers-i2c:
  + i2c-i801: fix resume when PEC is used
  + m41t00: fix bitmasks when writing to chip
- Updated kernel-fix-drivers-ide:
  + alim15x3: fix ULI M1573 southbridge support
- Added kernel-fix-drivers-mtd:
  + MTD_NAND_SHARPSL and MTD_NAND_NANDSIM should be tristate's
- Updated kernel-fix-drivers-scsi:
  + 3w-xxxx: disable local IRQs around kmap_atomic() calls
  + 3w-9xxx: disable local IRQs around kmap_atomic() calls
- Updated kernel-fix-drivers-usb:
  + remove __init from usb_console_setup
- Updated kernel-fix-drivers-video:
  + fbdev: fix return error of fb_write
- Updated kernel-fix-fs:
  + fuse: fix oops in fuse_send_readpages()
  + fix block device symlink name for devices with a '/' in their name
  + ext3: fix missed mutex unlock in error path
  + xfs: fix utime(2) in the case that no times parameter was passed in
  + cifs: fix incorrect signature sent on SMB Read (Samba bug 3621, kernel.org
    bug 6147)
  + x86: don't allow tail-calls in sys_ftruncate[64]() to avoid userspace
    register corruption
  + x86: be careful about tailcall breakage for sys_open[at] too
  + fix file lookup without ref
- Updated kernel-fix-net:
  + atm: clip causes unregister hang
  + tcp: fix truesize underflow with TSO
  + ipv6: ensure to have hop-by-hop options in our header of sk_buff
  + ipv6: xfrm: don't use old copy of pointer after pskb_may_pull()
  + ipv6: xfrm: fix decoding session with preceding extension header(s)
- Updated kernel-fix-security:
  + CVE-2006-0744: x86_64: always call IRET in execve; when user could have
    changed RIP always force IRET
  + shmat: stop mprotect from giving write permission to a readonly attachment
  + CVE-2006-1524: check file and mmap protections for MADV_REMOVE
  + CVE-2006-1525: ipv4: ip_route_input panic fix
  + CVE-2006-1056: i386/x86-64: fix x87 information leak between processes
  + selinux: fix MLS compatibility off-by-one bug

* Wed Apr 12 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.16-alt2
- Patches updated up to 2.6.16.4.
- Updated kernel-fix-core:
  + fix wrong error path in dup_fd() leading to oopses in RCU
  + cpufreq: mark longhaul driver as broken
  + cpufreq: fix the p4-clockmod N60 errata workaround
  + fix module refcount leak in __set_personality()
  + fix NULL pointer dereference in node_read_numastat()
- Updated kernel-fix-drivers-char:
  + isicom must select FW_LOADER
  + tlclk: fix sysfs permissions
- Added kernel-fix-drivers-ieee1394:
  + sbp2: fix spinlock recursion
- Updated kernel-fix-drivers-media:
  + saa7134: fix oops with disable_ir=1
- Updated kernel-fix-drivers-net:
  + PCMCIA_SPECTRUM must select FW_LOADER
  + ipw2200: fix an array overrun
  + AIRO and AIRO_CS must select CRYPTO
  + hostap: fix EAPOL frame encryption
  + sky2: fix oops on dual port cards
  + PPP MPPE: do not accept unsupported MPPE options
- Added kernel-fix-drivers-pcmcia:
  + pcmcia: permit single-character-identifiers
- Updated kernel-fix-drivers-usb:
  + EHCI full speed ISO bugfixes
  + usbcore: usb_set_configuration oops (NULL ptr dereference)
  + isd200: limit to BLK_DEV_IDE
- Updated kernel-fix-drivers-video:
  + fbcon: fix big-endian bogosity in slow_imageblit()
- Updated kernel-fix-fs:
  + knfsd: correct reserved reply space for read requests
  + kdump proc vmcore size overflow fix
- Updated kernel-fix-net:
  + {ip,nf}_conntrack_netlink: fix expectation notifier unregistration
  + fib_trie.c node freeing fix
  + netfilter: fix fragmentation issues with bridge netfilter
  + fix hotplug race during device registration
- Updated kernel-fix-security:
  + CVE-2006-1055: sysfs: zero terminate sysfs write buffers
  + CVE-2006-1522: keys: fix oops when adding key to non-keyring
  + CVE-2006-1523: __group_complete_signal: remove bogus BUG_ON

* Thu Mar 30 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.16-alt1
- 2.6.16 (patches from 2.6.16.1 included).
- Added more files to kernel-headers-modules-%%flavour subpackage:
  + arch/%%base_arch/Makefile.cpu
  + scripts/mkmakefile
  + .kernelrelease
- Added kernel-fix-security-altsec - hardening patch for Linux 2.6.
- Updated kernel-feat-drivers-net-sk98lin:
  + updated sk98lin driver to 8.31
  + added patch to fix compilation with 2.6.16
- Updated kernel-fix-build:
  + fix kbuild compatibility with make-3.81rc1
  + fix <linux/rtc.h> changes which broke strace builds
- Updated kernel-fix-core:
  + sysfs: sysfs_remove_dir() needs to invalidate the dentry (fixes USB cdc-acm
    oops on disconnect)
  + firmware: fix BUG: in fw_realloc_buffer
  + fix get_cpu_sysdev() parameter type
  + sysfs: fix a kobject leak in sysfs_add_link on the error path
  + fix scheduler deadlock
  + DMI: fix DMI onboard device discovery
  + speedstep-smi: fix assembly bug in speedstep_smi_ownership
  + unshare: error if passed unsupported flags
- Updated kernel-fix-drivers-block:
  + cciss: fix use-after-free in cciss_init_one
- Updated kernel-fix-drivers-char:
  + tlclk: fix handling of device major
  + agpgart: add ATI RS350 support
  + agpgart: fix wrong PCI ID for ALI M1695 AGP bridge
- Updated kernel-fix-drivers-i2c:
  + i2c-piix4: add Broadcom HT-1000 support
  + i2c-ixp4xx: add hwmon class
- Updated kernel-fix-drivers-md:
  + dm: bio split bvec fix
  + raid1: fix bug: BIO_RW_BARRIER requests to md/raid1 hang
- Updated kernel-fix-drivers-media:
  + V4L/DVB: fix Samsung NTSC tuner frequency ranges
  + VIDEO_DECODER must select FW_LOADER
- Updated kernel-fix-drivers-scsi:
  + sata_mv: fix irq port status usage
  + sata_mv: fix off by one bug in processing of the EDMA response queue
- Updated kernel-fix-drivers-usb:
  + irda-usb: fix use-after-free bug in irda_usb_receive()
- Updated kernel-fix-drivers-video:
  + i810fb_cursor(): use GFP_ATOMIC
- Updated kernel-fix-fs:
  + fix duplicated line in /proc/devices
  + xfs: avoid writeout of clean data
  + v9fs: assign dentry ops to negative dentries
- Updated kernel-fix-net:
  + ensure device name passed to SO_BINDTODEVICE is NULL terminated
- Updated kernel-fix-security:
  + CVE-2006-1242: TCP: do not use inet->id of global tcp_socket when sending
    RST
- Updated kernel-fix-acpi, kernel-fix-core, kernel-fix-drivers-block,
  kernel-fix-drivers-char, kernel-fix-drivers-i2c, kernel-fix-drivers-ide,
  kernel-fix-drivers-media, kernel-fix-drivers-net, kernel-fix-drivers-scsi,
  kernel-fix-drivers-usb, kernel-fix-fs, kernel-fix-net, kernel-fix-security:
  - disabled obsolete patches when applying to kernel 2.6.16
- Removed kernel-fix-core-skbuff, kernel-fix-drivers-hwmon,
  kernel-fix-drivers-input, kernel-fix-drivers-pcmcia,
  kernel-feat-net-ieee80211, kernel-feat-net-ppp-mppe (obsolete patches)
- Important configuration changes:
  + i586 smp: enabled CONFIG_HIGHMEM64G to support more than 4GB RAM (#8865)
  + i586: enabled CONFIG_REGPARM
  + x86_64 smp: enabled NUMA support
  + changed default IO scheduler to CFQ
  + enabled traffic control actions support (CONFIG_NET_CLS_ACT)
  + usb-storage: enabled ub driver in addition to usb-storage, enabled libusual
    module to select between ub and usb-storage
  + enabled kernel-fix-security-altsec features:
    + CONFIG_ALT_SECURE_PROC: tighten permissions for some things in /proc
      (similar to the Openwall patch for kernels 2.4.x)
    + CONFIG_ALT_SECURE_SHM: immediately destroy unused SysV shared memory
      segments (configurable through the kernel.shm_destroy_unused sysctl)

* Thu Feb 09 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.14-alt5
- Updated kernel-fix-drivers-ide:
  + via82cxxx: add VIA VT8251 IDE controller support
- Added kernel-fix-drivers-input:
  + mousedev: fix memory leak
  + iforce: fix detection of USB devices
- Updated kernel-fix-drivers-scsi:
  + ahci: add VIA VT8251 SATA controller support
- Updated kernel-fix-fs:
  + fix NFS inode leak when d_instantiate_unique finds aliased dentry
- Updated kernel-fix-net:
  + ppp: fix hardware RX checksum handling
- Updated kernel-fix-security:
  + CVE-2006-0095: dm-crypt: zero key before freeing it
  + seclvl: do not crash on settime() with a NULL timeval
  + fix keyctl usage of strnlen_user()

* Tue Feb 07 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.14-alt4
- Updated kernel-fix-core:
  + fix setting irq affinity with MSI enabled
- Updated kernel-fix-drivers-scsi:
  + i2o_scsi: fix oops on command abort
- Updated kernel-fix-fs:
  + ufs: fix oops on mount
  + reiserfs: fix mount options parsing
- Updated kernel-fix-net:
  + ebtables: don't match tcp/udp source/destination port for IP fragments
  + netlink: fix oops on socket creation failure
  + fix /sys/class/net/<if>/wireless without dev->get_wireless_stats
  + make second arg to skb_reserve() signed (fixes PPP on 64-bit archs)
- Updated kernel-fix-security:
  + moxa: require CAP_SYS_RAWIO for firmware loading ioctls
  + CVE-2006-0036: netfilter: fix crash in ip_nat_pptp
  + CVE-2006-0037: netfilter: fix another crash in ip_nat_pptp
  + CVE-2005-3356: fix refcounting on failure exits in sys_mq_open()
  + CVE-2006-0454: icmp: fix extra dst release when ip_options_echo() fails

* Fri Jan 20 2006 LAKostis <lakostis at altlinux.ru> 2.6.14-alt3.1
- add missing bt{848,cx-risc} headers for lirc compiling.

* Sat Jan 07 2006 Sergey Vlasov <vsu@altlinux.ru> 2.6.14-alt3
- Updated kernel-fix-core:
  + add try_to_freeze to kauditd to fix suspend failure
  + kernel/params.c: fix sysfs access with CONFIG_MODULES=n
- Updated kernel-fix-drivers-block:
  + cciss: bug fix for hpacucli
  + cciss: bug fix for BIG_PASS_THRU
- Updated kernel-fix-drivers-char:
  + agpgart: fix serverworks TLB flush
  + i8k: fix /proc reporting of blank service tags
- Updated kernel-fix-drivers-ide:
  + ide-floppy: fix software eject with LS-120 drive
- Added kernel-fix-drivers-media:
  + dvb: BUDGET CI card depends on STV0297 demodulator
  + dvb: fix tuner init for Pinnacle PCTV Stereo
  + dvb: fix analog NTSC for Thomson DTT 761X hybrid tuner (pcHDTV 3000,
    FusionHDTV3 Gold-T)
  + dvb: dst: fix possible buffer overflow
- Updated kernel-fix-drivers-net:
  + sungem: gem_remove_one mustn't be __devexit
- Added kernel-fix-drivers-pcmcia:
  + i82365: release all resources if no devices are found
- Updated kernel-fix-drivers-scsi:
  + libata: separate controller-wide spinlock from Scsi_Host lock
  + dpt_i2o fix for deadlock condition
  + fix transfer direction in sd (kernel panic when ejecting iPod)
  + fix transfer direction in scsi_lib and st
- Updated kernel-fix-drivers-usb:
  + adapt microtek driver to new scsi features
  + usbhid: fix oops when connecting simulation devices generating unknown
    simulation events
  + pl2303: add IDs for Siemens SX1 and x75 mobiles
  + pl2303: fix data length check in pl2303_update_line_status
- Updated kernel-fix-fs:
  + fix listxattr() for generic security attributes
  + ufs: inode->i_sem is not released in error path
- Updated kernel-fix-net:
  + fix processing of fib_lookup netlink messages
  + bonding: fix feature consolidation
  + bridge: recompute features when adding a new device
  + netfilter: fix CTA_PROTO_NUM attribute size in ctnetlink
  + netfilter: fix unbalanced read_unlock_bh in ctnetlink
  + ip_gre: fix hardware checksum modification
  + vlan: fix hardware rx csum errors
  + netfilter: fix NAT init order
  + netfilter: fix incorrect dependency for IP6_NF_TARGET_NFQUEUE
  + rtnetlink: fix RTNLGRP definitions in rtnetlink.h
  + bridge-nf: fix ipv6 length check
  + ipv6: fix route lifetime
  + ipsec: perform SA switchover immediately
  + IEEE80211_CRYPT_TKIP depends on NET_RADIO
- Updated kernel-fix-security:
  + updated CVE-2005-3257 fix patch:
    - require CAP_SYS_TTY_CONFIG for KDSKBENT in addition to KDSKBSENT
    - allow normal users to read current settings
  + CVE-2005-3623: nfsd: do not allow setting ACLs on readonly mounted NFS
    filesystems
  + CVE-2005-4605: insanity avoidance in /proc
  + sysctl: don't overflow the user-supplied buffer with '\0'
  + sysctl: make sure to terminate strings with a NUL

* Sun Dec 04 2005 Sergey Vlasov <vsu@altlinux.ru> 2.6.14-alt2
- Restored x86_64 support; updated kernel config for x86_64.
- Updated kernel-fix-acpi:
  + fix HP nx8220 boot hang regression due to change in acpi_bus_find_driver()
  + prefer _CST over FADT for C-state capabilities (as written in the ACPI
    standard)
  + support FADT P_LVL2_UP flag (C2 is valid for UP only)
  + properly detect pmtimer on ASUS A8V
  + fix null pointer deref in video/lcd/brightness
  + fix boot hang on HT boxes with broken BIOS reporting wrong ACPI IDs
  + allow return to active cooling mode once passive mode is entered
- Updated kernel-fix-drivers-ide:
  + via82cxxx: add VT6410 controller support
- Updated kernel-fix-fs:
  + xfs: fix umount/xfslogd deadlock
- Updated kernel-fix-security:
  + CVE-2005-3257: require root privileges for loading key mappings
  + CVE-2005-3857: remove time_out_leases() printk that's easily triggered by
    users
  + CVE-2005-3808: fix 32bit integer overflow in invalidate_inode_pages2()

* Wed Nov 30 2005 Sergey Vlasov <vsu@altlinux.ru> 2.6.14-alt1
- 2.6.14.
- Temporarily removed x86_64 support (to be restored by arch maintainers).
- Removed kernel-fix-drivers-ieee1394, kernel-fix-drivers-input,
  kernel-fix-drivers-media, kernel-feat-drivers-input (obsolete).
- Removed kernel-feat-drivers-video-splash (does not work currently).
- Removed kernel-feat-drivers-lirc (the patch is unmaintained, some drivers no
  longer compile at all, others refer to symbols which no longer exist in the
  kernel).
- Added kernel-fix-drivers-hwmon - fixes to hardware monitoring drivers:
  + it87: fix missing fan div init
  + lm78: fix VID conversion
  + w83627hf: fix missing boundary check when setting in0 limits
- Added kernel-feat-net-ieee80211 - IEEE 802.11 subsystem update (needed for
  newer versions of ipw2x00 drivers; cannot be built separately, because now
  there are some in-kernel drivers which use it).
- Added drivers/md/dm*.h headers to kernel-headers-modules-%%flavour (#8443).
- Added drivers/media/video/bttv.h, drivers/media/video/bttvp.h to
  kernel-headers-modules-%%flavour (needed for separate compilation of lirc
  modules).
- Updated kernel-fix-acpi:
  + updated the dsdt-initrd patch to version 0.7e for kernel 2.6.14
  + fix oops on processor module unload when ACPI is disabled
- Updated kernel-fix-build:
  + fix Kconfig dependencies (selecting NFSD_V4 forced CRYPTO_MD5 to be
    builtin, even if NFSD was modular)
- Updated kernel-fix-core:
  + fix de_thread() vs send_group_sigqueue() race
  + fix ptrace self-attach rule
  + fix signal->live leak in copy_process()
  + ptrace: don't auto-reap traced children
  + x86_64/i386: Compute correct MTRR mask on early Noconas
  + fix crash when ptrace poking hugepage areas
- Updated kernel-fix-drivers-block:
  + fix oops on suspend after on-the-fly switch to anticipatory i/o scheduler
  + pktcdvd: fix possible oops in pkt_count_states() due to array overrun
- Updated kernel-fix-drivers-char:
  + fix soft lockup with ALSA rtc-timer due to the wrong irq handling in
    rtc_control()
- Updated kernel-fix-drivers-net:
  + airo.c/airo_cs.c: correct prototypes
  + prism54: fix frame length setting bug which might result in information
    leak
  + drivers/isdn/hardware/eicon/os_4bri.c: correct the xdiLoadFile() signature
  + generic HDLC WAN drivers: disable netif_carrier_off()
  + infiniband: fix a use-after-free
- Updated kernel-fix-drivers-scsi:
  + updated patch for old megaraid driver:
    + removed controllers which are supported by the new driver (megaraid_mbox)
      from the table of supported devices
    + changed PCI driver name to megaraid_legacy to avoid conflict with the
      newer driver
  + dpt_i2o: fix use-after-free
  + i2o_pci: fix use-after-free
  + fix SCSI_SATA_INTEL_COMBINED setting with modular IDE
  + add boot option to control Intel combined mode behavior (to allow DMA in
    combined mode configs)
- Updated kernel-fix-drivers-usb:
  + USB: always export interface information for modalias
- Updated kernel-fix-fs:
  + VFS: fix memory leak with file leases
  + fix XFS_QUOTA for modular XFS
- Updated kernel-fix-net:
  + fix zero-size datagram reception
  + ipvs: fix connection leak if expire_nodest_conn=1
  + tcp: fix too large BIC max increment
  + ctnetlink: check if protoinfo is present
  + ctnetlink: fix oops when no ICMP ID info in message
  + ipv6: fix calculation of AH length during filling ancillary data
  + ipv6: fix memory management error during setting up new advapi sockopts
  + ipv6: fix sending extension headers before and including routing header
  + ip_conntrack: fix ftp/irc/tftp helpers on ports >= 32768
  + ip_conntrack TCP: Accept SYN+PUSH like SYN
  + NAT: fix module refcount dropping too far
  + nf_queue: fix Ooops when no queue handler registered
  + PPTP helper: fix endianness bug in GRE key / CallID NAT
  + PPTP helper: fix PNS-PAC expectation call id
  + fix refcount leak of proto when ctnetlink dumping tuple
- Updated kernel-fix-security:
  + fix syctls unregistration oops (CVE-2005-2709)

* Sun Aug 14 2005 Sergey Vlasov <vsu@altlinux.ru> 2.6.12-alt4
- Updated kernel-fix-acpi:
  - removed suspend-setup-leave patch (#6785, #7539)
- Updated kernel-fix-core:
  + do not BUG() when module per-cpu alignment cannot be met
  + fix powernow oops on dual-core Athlon
  + clear the returned argument in sys_get_thread_area()
  + check if mode < 0 in sys_set_mempolicy()
  + x86_64: fix memleak from malicious 32bit elf program
  + x86_64: fixing smpboot timing problem
  + x86_64: fix SRAT for non dual-core AMD systems
- Updated kernel-fix-drivers-char:
  + rocket: fix ldisc ref count handling
  + moxa: fix tty driver name which was conflicting with the BSD-style pty
    driver, therefore some ports were inaccessible when using udev
- Updated kernel-fix-drivers-scsi:
  + qla2xxx: correct handling of fc_remote_port_add() failure case
- Updated kernel-fix-fs:
  + fix BIO cloning bug which could result in data corruption with some MD
    setups
  + check input buffer size in zisofs
- Updated kernel-fix-net:
  + fix early vlan adding leads to not functional device
  + xfrm: fix possible overflow of sock->sk_policy
  + fix potential memory corruption in NAT code
  + fix deadlock in ip6_queue
  + wait until all references to ip_conntrack_untracked are dropped on unload
  + fix signedness issues in net/core/filter.c
- Updated kernel-fix-security:
  + fix keyring handling bugs (CAN-2005-2098, CAN-2005-2099)
- Updated kernel-feat-drivers-net-sk98lin:
  + version 8.23
- Rebuild with new kernel-feat-fs-squashfs.

* Mon Jul 25 2005 Sergey Vlasov <vsu@altlinux.ru> 2.6.12-alt3
- Fixed kernel-fix-core-skbuff so that it does nothing for 32-bit architectures
  and enabled it for all architectures to avoid arch-specific BuildRequires.
- Updated kernel-fix-acpi:
  + if ACPI doesn't find an irq listed, don't accept 0 as a valid PCI irq
  + fix PNPACPI resource parser (#7392)
- Updated kernel-fix-drivers-char:
  + fix tpm driver initialization which was messing up other devices
  + add missing NULL checks in tty ioctl code
- Updated kernel-fix-drivers-media:
  + cx88: set hue offset to 128 to correct behavior in cx88 cards
- Updated kernel-fix-drivers-net:
  + fix locking in the shaper driver
- Updated kernel-fix-fs:
  + fix locking in __unregister_chrdev_region()
- Updated kernel-fix-net:
  + revert the nf_reset change completely (previous fix was not enough); drop
    conntrack references manually before packets are queued to packet sockets
- Added kernel-fix-drivers-input:
  + fix problem with trackpoint attached to synaptics passthrough port

* Thu Jul 14 2005 Anton D. Kachalov <mouse@altlinux.org> 2.6.12-alt2
- Per-arch configuration
- Added kernel-fix-core-skbuff for x86_64 only

* Sat Jul 02 2005 Sergey Vlasov <vsu@altlinux.ru> 2.6.12-alt1
- 2.6.12.
- Updated kernel-fix-build, kernel-fix-core, kernel-fix-drivers-char,
  kernel-fix-drivers-ide, kernel-fix-drivers-media, kernel-fix-drivers-net,
  kernel-fix-drivers-pci, kernel-fix-drivers-scsi, kernel-fix-drivers-usb,
  kernel-fix-drivers-video, kernel-fix-fs, kernel-fix-net, kernel-fix-security:
  - removed obsolete patches
- Updated kernel-fix-acpi:
  + updated acpi-attrs and suspend-setup-leave patches for 2.6.12
  + call acpi_register_gsi() even for default PCI interrupt assignment (needed
    to set PCI interrupts to level/low properly)
- Updated kernel-fix-core:
  + round size in remap_pfn_range() up to a page boundary
  + add "memory" clobbers to string.h functions to avoid memory access
    reordering by gcc
- Updated kernel-fix-drivers-media:
  + updated Manli and BeholdTV remote control support patch for 2.6.12
- Updated kernel-fix-drivers-net:
  + e1000: fix spinlock bug
- Updated kernel-fix-drivers-pci:
  + fix typo in drv->driver.shutdown setting for PCI drivers that might result
    in not setting drv->driver.owner
- Updated kernel-fix-drivers-scsi:
  + fix qla2xxx initialization problems
- Updated kernel-fix-drivers-usb:
  + updated old_scheme_first patch for 2.6.12
- Updated kernel-fix-net:
  + fix connection tracking on bridges
  + fix socket hashing bugs in netlink
- Updated kernel-fix-security:
  + CAN-2005-1913
- Updated kernel-feat-drivers-input:
  + updated trackpoint support patch:
    - warning: module parameters for trackpoint device configuration are no
      longer available - use sysfs for configuration;
    - support for scroll emulation in the driver was removed - use the
      appropriate Xorg options
- Updated kernel-feat-drivers-lirc, kernel-feat-drivers-sk98lin:
  + fix compilation with 2.6.12
- Updated kernel-feat-drivers-video-splash:
  + updated splash patch for kernel 2.6.12

* Mon Jun 13 2005 Sergey Vlasov <vsu@altlinux.ru> 2.6.11-alt11
- Updated kernel-fix-core:
  + fix get_unmapped_area() sanity tests
  + fix try_to_unmap_cluster() passing out-of-bounds pte to pte_unmap()
- Updated kernel-fix-drivers-char:
  + fix mxser receive problem (#6615)
- Updated kernel-fix-drivers-media:
  + bttv: make video capture work on Leadtek WinFast VC100 XP cards
  + saa7134: add support for remote control as used with Manli MuchTV
    M-TV00[12] boards; add BeholdTV 401 and BeholdTV 403 FM card names to the
    Manli entries (#6917)
  + bttv: fix oops on i2c registration failure
- Updated kernel-fix-fs:
  + ext3: fix possible false assertion failure in log_do_checkpoint()
  + hfs, hfsplus: fix leaks and oops in hfsplus
- Updated kernel-fix-net:
  + bridge: avoid poisoning of the bridge forwarding table by frames that have
    been dropped by filtering
  + netem: avoid infinite loop in qdisc_run() when using duplication
  + fix deadlock with ip_queue and tcp local input path
- Modified configuration:
  + (CONFIG_PREEMPT was already disabled in std26-smp)
  + disabled CONFIG_ACPI_DEBUG (workaround for #6304)
  + enabled CONFIG_LOGO_LINUX_CLUT224 (#6975)
  + enabled CONFIG_LOGO_LINUX_MONO (just in case)
- Moved OSS modules for USB audio devices (audio and usb-midi) to the
  kernel-modules-oss-%%flavour subpackage (the snd-usb-audio module from ALSA
  is preferred).

* Sun May 15 2005 Sergey Vlasov <vsu@altlinux.ru> 2.6.11-alt10
- Updated kernel-fix-security:
  + fix user pointer validation in raw and pktcdvd drivers

* Fri May 13 2005 Sergey Vlasov <vsu@altlinux.ru> 2.6.11-alt9
- Updated kernel-fix-acpi:
  + show some ACPI device attributes in sysfs (currently hardware_id,
    compatible_ids, bus_address, unique_id)
- Updated kernel-fix-core:
  + remove bogus BUG() in kernel/exit.c
  + fix driver_detach in case the release handler itself calls
    device_release_driver() for the next device (could cause hangs with some
    USB drivers like cdc-acm which bind to more than one interface)
- Updated kernel-fix-drivers-net:
  + 3c59x: only put the device into D3 when we're actually using WOL (some
    devices have trouble with D3 on warm boot)
- Added kernel-fix-drivers-scsi:
  + aacraid: fix oops on management device open for nonexistent controller
  + fix queue lock allocation for SCSI devices (fixes problems with hot
    unplugging, especially with the CFQ scheduler)
    https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=155472
  +  require CAP_ADMIN for SG_IO to tape drives (sending SCSI commands to the
    drive behind the back of the st driver may cause the device state to be
    inconsistent with the internal driver state and cause problems)
  + enable both old and new megaraid drivers (the new megaraid_mbox driver does
    not support some devices which are supported by the old driver)
  + blacklist some broken SCSI scanners which respond to all LUNs
- Updated kernel-fix-drivers-usb:
  + fix bug in visor driver with throttle/unthrottle causing oopses
- Added kernel-fix-drivers-video:
  + fix bad PCI driver name in intelfb
  + fix oops in intelfb due to __initdata marking of module parameters
- Updated kernel-fix-fs:
  + fix race between ext3 make block reservation and reservation window discard
- Updated kernel-fix-net:
  + ebtables: fix smp race under heavy load
  + rose: verify ndigis in rose_rt_ioctl()
- Removed kernel-feat-drivers-drm (switched from in-kernel DRM drivers to the
  DRM CVS).
- Modified configuration:
  + enabled old megaraid driver in addition to the new one
  + disabled intel-mch-agp (it contains a copy of the intel-agp code for Intel
    82865 and 82875 chips intended for the x86_64 architecture; these chips are
    supported by the intel-agp module on i386)
  + disabled DRM support for buildind external DRM modules from DRI CVS;
    removed corresponding Provides from the package
- Reverted kernel-headers-%%flavour and kernel-headers-modules-%%flavour layout
  modification from 2.6.11-alt7 (causes problems when upgrading old packages).

* Wed May 11 2005 Sergey Vlasov <vsu@altlinux.ru> 2.6.11-alt8
- Updated kernel-fix-security:
  + fix ELF core dump issue (CAN-2005-1263)

* Tue May 10 2005 Sergey Vlasov <vsu@altlinux.ru> 2.6.11-alt7
- Added kernel-feat-drivers-net-sk98lin:
  + updated sk98lin driver to 8.16 from vendor
- Updated kernel-fix-acpi:
  + call ACPI suspend preparation methods in proper places with respect to PCI
    devices suspend/resume (#6785)
- Updated kernel-fix-core:
  + make rwsems use interrupt disabling spinlocks (fixes deadlock in
    dio_complete())
  + fix syscall table for UML
  + fix SMP crash in security/keys/key.c
- Added kernel-fix-drivers-i2c:
  + fix oops in the eeprom driver
  + fix sysfs permissions in it87 and via686a drivers (could cause oops if
    write is attempted)
  + fix multiple bugs in i2c-ali1563 driver
- Updated kernel-fix-drivers-media:
  + fix freeze on loading bttv in some configurations
- Updated kernel-fix-drivers-net:
  + fix irda-usb "badness" problem and sysfs support
- Updated kernel-fix-drivers-usb:
  + enable "old_scheme_first" and "use_both_schemes" parameters of usbcore by
    default (#6728)
- Updated kernel-fix-fs:
  + fix race in jbd code which could give oopses
- Updated kernel-fix-net:
  + fix deadlock in IPsec when sending ICMP "fragmentation needed" packet
  + fix binary search in the BIC congestion control algorithm
- Modified configuration:
  + enlarged kernel message buffer to 128 KB (#6366)
  + disabled software suspend support (does not work with modular drivers)
  + disabled buggy MTD drivers (#5994)
  + enabled NAPI support in starfire, r8169, ixgb, s2io drivers
  + enabled ISDN4Linux support
  + enabled OSS sound drivers (#6521)
  + disabled HID Boot Protocol drivers (usbkbd, usbmouse)
  + enabled EFI partition table support
- Build OSS sound drivers as a separate module package
  (kernel-modules-oss-%%flavour) (#6521).
- Fixed kernel-headers-%%flavour file list (some headers were missing).
- Fixed passing of config file to the kernel build system.
- Moved kernel-headers-%%flavour files to /usr/src/linux-%version-%flavour,
  leaving a symlink in /usr/include (fixes problems with third-party modules
  which don't like symlinks in the kernel source tree).
- Spec file cleanup, rewritten package descriptions.

* Tue Mar 29 2005 Sergey Vlasov <vsu@altlinux.ru> 2.6.11-alt6
- Updated kernel-fix-security:
  + fixed isofs corrupted filesystem handling (CAN-2005-0815)
  + fixed bluetooth range checking bug (CAN-2005-0750)
  + fixed ext2 information leak (CAN-2005-0400)
  + fixed binfmt_elf DoS (CAN-2005-0749)
- Updated kernel-fix-core:
  + fixed tasklist locking bug which caused hangs instead of reboot on SMP
- Updated kernel-fix-drivers-net:
  + fixed missing free_irq in error path in amd8111e and via-rhine drivers
  + fixed check for underflow in the tun driver
  + fixed kernel panic on receive in the hd6457x driver
- Updated kernel-fix-net:
  + fixed deadlock in NetROM
  + fixed crash when reading /proc/net/route
  + fixed bug in IPSEC support (__xfrm_find_acq_byseq)
- Fixed passing config file to the kernel build system (replacing defconfig was
  a broken way which worked before for some unknown reason).
- Removed hack which copied .config back to source.

* Wed Mar 16 2005 Sergey Vlasov <vsu@altlinux.ru> 2.6.11-alt5
- Updated kernel-fix-security:
  + fix ppp_async issue (CAN-2005-0384)
  + fix information leak through get_task_comm()

* Mon Mar 14 2005 Sergey Vlasov <vsu@altlinux.ru> 2.6.11-alt4
- 2.6.11 (really kernel-fix-* packages contain relevant patches from 2.6.11.3).
- Updated kernel-fix-security:
  + epoll: return proper error on overflow condition
- Updated kernel-fix-acpi, kernel-fix-core, kernel-fix-drivers-block,
  kernel-fix-drivers-md, kernel-fix-drivers-sound:
  - removed obsolete patches
- Updated kernel-fix-build:
  + fix "make htmldocs" failure
- Updated kernel-fix-drivers-ide:
  + fix no_lba48_dma flag handling in ide-disk (fixes DMA timeouts on old
    ALI15x3 controllers with a large disk)
- Updated kernel-fix-drivers-input:
  + make ACPI detection of i8042 controllers ia64-only (many x86 PCs have
    broken BIOS tables)
- Updated kernel-fix-drivers-net:
  + fix receive descriptor length setting in r8169
  + fix sis900 oops with preempt/SMP
  + fix via-rhine oops on shutdown with old chips without WOL support
- Updated kernel-fix-drivers-pci:
  + fix double free in the pciehp module
- Updated kernel-fix-drivers-usb:
  + fix cdc-acm oopses on disconnect
- Updated kernel-fix-fs:
  + fix stat for device nodes on cramfs
- Updated kernel-fix-net:
  + export tcp_timer_bug_msg for modular ipv6 build
- Updated kernel-feat-drivers-input:
  + updated trackpoint patch
  - removed alps patch (included in 2.6.11)
- Updated kernel-feat-drivers-video-splash:
  + new bootsplash patch for 2.6.11
- Added kernel-fix-drivers-char:
  + fix bug in drm setversion ioctl which could crash the X server
  + fix chip type for Radeon Yi ES1000 RN50
- Added kernel-fix-drivers-media:
  + fix saa7110 oops on modprobe
  + fix i2c message flags in video drivers
- Added kernel-feat-drivers-drm:
  + add VIA Unichrome driver (version 2.3.3)
- Removed kernel-fix-drivers-atm, kernel-fix-drivers-i2c,
  kernel-fix-drivers-serial, kernel-fix-drivers-parport (obsolete for 2.6.11).
- Modified configuration:
  + enabled all DRM modules (DRM sources from xorg-x11 6.8.2 no longer compile
    with kernel 2.6.11, but modules shipped with the kernel are new enough)
- Added Provides: kernel-modules-drm-%%flavour for compatibility.

* Wed Feb 09 2005 Sergey Vlasov <vsu@altlinux.ru> 2.6.10-alt3
- Build with gcc-3.4.
- Added kernel-fix-drivers-atm, kernel-fix-drivers-block,
  kernel-fix-drivers-i2c, kernel-fix-drivers-input, kernel-fix-drivers-md,
  kernel-fix-drivers-pci, kernel-fix-drivers-serial; updated kernel-fix-acpi,
  kernel-fix-core, kernel-fix-drivers-char, kernel-fix-drivers-ide,
  kernel-fix-drivers-scsi, kernel-fix-drivers-sound, kernel-fix-drivers-usb:
    + sync with 2.6.10-as3 patchset
- Modified configuration:
  + moved IDE support to modules
  + moved ext2 filesystem support to modules
  + disabled ALSA drivers (in-kernel version is too old, use separate
    kernel-modules-alsa-* packages which are updated)
- Changed /lib/modules/%%version-%%flavour-%%krelease/build symlink to point to
  %%_usrsrc/linux-%%version-%%flavour/ and moved it to the
  kernel-headers-modules-%%flavour subpackage.
- Added version to Provides: kernel-headers (#5872).
- Updated kernel-fix-drivers-ide:
  + added patch to fix endless partition rescan on PCMCIA flash (#5853).

* Sat Jan 08 2005 Sergey Vlasov <vsu@altlinux.ru> 2.6.10-alt2
- Removed broken symlink /lib/modules/%%version-%%flavour-%%krelease/source.
- Updated kernel-fix-security:
  + fix uselib() issue (CAN-2004-1235)
  + fix expand_stack issue (CAN-2005-0001)
  + fix integer signedness issues in moxa, random, scsi drivers
  + fix RLIMIT_MEMLOCK enforcement

* Wed Dec 29 2004 Sergey Vlasov <vsu@altlinux.ru> 2.6.10-alt1
- 2.6.10
- Added ccache support (was lost because of CC=gcc3.3 in the kernel
  makefile).
- Updated kernel-fix-build, kernel-fix-drivers-net, kernel-fix-net,
  kernel-feat-drivers-pktcdvd:
  - removed obsolete patches
- Updated kernel-fix-drivers-parport:
  + fixed parport_pc module parameters
- Updated kernel-feat-drivers-video-splash:
  + new bootsplash patch for 2.6.10
- Updated kernel-feat-net-ppp-mppe:
  + updated patch to version 1.2 (fixes CryptoAPI-related bug)
- Added kernel-fix-drivers-ieee1394:
  + remove broken MODULE_ALIAS_CHARDEV entries from ieee1394 modules (#3873)
- Removed kernel-fix-drivers-serial (obsolete).
- Modified configuration:
  + CONFIG_EDD is not set (causes boot problems, #5511)
  + CONFIG_APM_IGNORE_USER_SUSPEND is not set (apparently this option was set
    accidentally a long time ago and then forgotten)
  + CONFIG_GEN_RTC is not set (conflicts with the real RTC support)
  + CONFIG_FB_RADEON_OLD is not set (conflicts with the new radeonfb driver)
  + CONFIG_USB_DYNAMIC_MINORS is not set (#5484)
  + lots of new drivers enabled (too many to list here)

* Thu Oct 28 2004 Anton Farygin <rider@altlinux.ru> 2.6.9-alt11
- fixed iptables
- fixed kernel-headers for using with userspace programms (#5409)
- added kernel-feat-evms-nodm patch
- ppp fixed: terminate connection on hangup

* Wed Oct 20 2004 Anton Farygin <rider@altlinux.ru> 2.6.9-alt10
- new version

* Wed Aug 18 2004 Sergey Vlasov <vsu@altlinux.ru> 2.6.8-alt9
- Added missing scripts/gcc-version.sh to kernel-headers-modules.
- Removed libkconfig.so shared library to avoid extra dependencies in packages.

* Mon Aug 16 2004 Anton Farygin <rider@altlinux.ru> 2.6.8-alt8
- 2.6.8
- added patch for fix typo in nfs code (2.6.8.1)
- updated acpi subsystem to last stable release (20040717)
- updated bootsplash

* Thu Aug 05 2004 Anton Farygin <rider@altlinux.ru> 2.6.7-alt8
- Updated kernel-fix-security:
    + fix ppos races (CAN-2004-0415)

* Thu Jun 17 2004 Anton Farygin <rider@altlinux.ru> 2.6.7-alt7
- 2.6.7
- updated bootsplash patch
- added kernel-fix-drivers-net:
  + 2.6_50_eql-check-null.patch: add NULL checks to the eql driver
  + 2.6_51_airo-proc-fix.patch: fix airo /proc write breakage
- added kernel-fix-drivers-usb:
  + 2.6_51_phidgetservo-fixes.patch: fix use of freed memory in PhidgetServo
    driver
  + 2.6_52_storage-jumpshot-fix.patch: fix size reporting in the Lexar Jumpshot
    CF driver; avoid "unneeded entry" message with some devices
- added kernel-fix-drivers-scsi:
  + 2.6_50_sata_sil-mod15write.patch: fix Seagate+SiI3112 mod15write bug
    workaround broken by the LBA48 optimizations

* Tue Jun 15 2004 Anton Farygin <rider@altlinux.ru> 2.6.6-alt6
- kernel-fix-security added:
  + 2.6_50_fpu-exception.patch: fix FPU exception handling DoS

* Fri May 21 2004 Anton Farygin <rider@altlinux.ru> 2.6.6-alt5
- updated to last kernel-fix-ide and kernel-fix-fs patches:
  + 2.6_55_reiserfs-i_size-race.patch: fix reiserfs inode size update race
    which could lead to file corruption
  + 2.6_52_no-suspend-on-reboot.patch: replaced with better fix (flush drive
    cache on reboot)
  + 2.6_51_dquot_release-oops.patch: fix dquot_release oops with quota_v1
  + 2.6_52_quota-recursion.patch: fixes quota recursion into filesystem
  + 2.6_53_quota-recursion-fix.patch: fix the recursion fix
  + 2.6_54_quota-v2-corruption.diff: fix possible quota_v2 files corruption
    when root did not have any inodes&space allocated
- added kernel-feat-pktcdvd

* Mon May 17 2004 Anton Farygin <rider@altlinux.ru> 2.6.6-alt4
- config tuning:
    CONFIG_BLK_DEV_ATIIXP=y
    CONFIG_IP_NF_MATCH_IPRANGE=m
    CONFIG_IP_NF_MATCH_PHYSDEV=m
    * disabled debug on i2c
    * enabled ebtables
    * disabled CONFIG_FONT_MINI_4x6
    * moved CONFIG_X86_MCE_NONFATAL to modules
    * disabled CONFIG_IDEDMA_IVB
- added kernel-fix-drivers-ide (Sergey Vlasov) with:
  + 2.6_50_wcache-fixes.patch: fix write cache handling problems:
    + fix drive->wcache setting
    + send CACHE FLUSH (EXT) only if the drive claims to support it
    + fix for Maxtor disks falsely claiming CACHE FLUSH EXT support
  + 2.6_51_system_state.patch: differentiate between halt/poweroff/reboot
  + 2.6_52_no-suspend-on-reboot.patch: avoid drive spindown on reboot
    
* Tue May 11 2004 Anton Farygin <rider@altlinux.ru> 2.6.6-alt3
- 2.6.6
- fixed depends (kernel-headers-modules)
- added kernel-fix-acpi with:
    fixes IRQ12 sharing
- Added kernel-feat-drivers-console-unicode by Ivan Zakharyaschev <imz@altlinux.ru>:
  fixes the imperfectness of Linux VT/console Unicode support 
  (involves a change of the kernel interface used by loadkeys, 
  but mainly is compatible with old loadkeys).

* Mon Apr 05 2004 Anton Farygin <rider@altlinux.ru> 2.6.5-alt1
- update to 2.6.5
- updated patches and config from std26-up-2.6.5-alt1 kernel

* Thu Mar 22 2004 Anton Farygin <rider@altlinux.ru> 2.6.4-alt4
- first build for Sisyphus, based on kernel-image-std26-up with changes:
    enabled CONFIG_HIGHMEM64G
    enabled CONFIG_X86_SMP (CONFIG_NR_CPUS=8)
    enabled CONFIG_X86_HT
    enabled CONFIG_IRQBALANCE
    enabled CONFIG_MPENTIUM4
    
