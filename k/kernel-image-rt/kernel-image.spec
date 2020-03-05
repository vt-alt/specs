%define kflavour		rt
Name: kernel-image-%kflavour
%define kernel_base_version	4.19
%define kernel_sublevel		.103
%define kernel_rt_release	rt42
%define kernel_extra_version	%nil
Version: %kernel_base_version%kernel_sublevel%kernel_extra_version
Release: alt1.%kernel_rt_release
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

#Remove oss
%def_disable oss
## Don't edit below this line ##################################

%define kversion	%kernel_base_version%kernel_sublevel%kernel_extra_version
%define modules_dir	/lib/modules/%kversion-%flavour-%krelease

%define kheaders_dir	%_prefix/include/linux-%kversion-%flavour
%define kbuild_dir	%_prefix/src/linux-%kversion-%flavour-%krelease
%define old_kbuild_dir	%_prefix/src/linux-%kversion-%flavour

%brp_strip_none /boot/*

Summary: The Linux kernel with PREEMPT_RT patches (Real-Time Linux)
License: GPL-2.0-only
Group: System/Kernel and hardware
Url: https://wiki.linuxfoundation.org/realtime/
# git://git.kernel.org/pub/scm/linux/kernel/git/rt/linux-stable-rt.git
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

Patch0: %name-%version-%release.patch

ExclusiveArch: x86_64

%define make_target bzImage
%ifarch ppc64le
%define make_target vmlinux
%endif
%ifarch aarch64
%define make_target Image
%endif

%define image_path arch/%base_arch/boot/%make_target
%ifarch ppc64le
%define image_path %make_target
%endif

%define arch_dir %base_arch
%ifarch %ix86 x86_64
%define arch_dir x86
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
%{?!_without_check:%{?!_disable_check:BuildRequires: qemu-system-%qemu_pkg-core ipxe-roms-qemu glibc-devel-static}}
Provides: kernel-modules-eeepc-%flavour = %version-%release
Provides: kernel-modules-drbd83-%flavour = %version-%release
Provides: kernel-modules-igb-%flavour = %version-%release
Provides:  kernel-modules-alsa = %version-%release
%ifarch aarch64
Provides: kernel-modules-kvm-%flavour = %version-%release
Provides: kernel-modules-kvm-%kversion-%flavour-%krelease = %version-%release
%endif

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
This package contains the Linux kernel %kernel_base_version%kernel_sublevel \
with PREEMPT_RT patches (%kernel_extra_version).

This kernel uses most vanilla config as possible to achieve better stability.

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
%patch0 -p1 -s

# ALT glibc contains strlcpy, so we need disable it there:
sed -i /strlcpy/d tools/include/linux/string.h

# fix -rt suffix
rm -f localversion*

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
CONFIGS=config-x86_64
%if "%base_flavour" == "rt"
CONFIGS="$CONFIGS config-rt"
%endif

scripts/kconfig/merge_config.sh -m $CONFIGS

# Options not recommended by
# https://wiki.linuxfoundation.org/realtime/documentation/known_limitations
FORBID="TRANSPARENT_HUGEPAGE
	OPROFILE
	X86_POWERNOW_K8
	BCACHE
	RT_GROUP_SCHED
	CPUMASK_OFFSTACK"

# Clean up and settle everything
%make_build olddefconfig

# Panic if forbidden options are enabled
for opt in $FORBID; do
	grep CONFIG_$opt= .config && exit 1
done

%make_build %make_target
%make_build modules
%ifarch aarch64
%make_build dtbs
%endif

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

%ifarch aarch64
mkdir -p %buildroot/lib/devicetree/$KernelVer
find arch/%arch_dir/boot/dts -type f -name \*.dtb | xargs -iz install -pm0644 z %buildroot/lib/devicetree/$KernelVer
%endif

mkdir -p %buildroot%kbuild_dir/arch/%arch_dir
install -d %buildroot%kbuild_dir
cp -a include %buildroot%kbuild_dir/include
cp -a arch/%arch_dir/include %buildroot%kbuild_dir/arch/%arch_dir


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
	arch/%arch_dir/Makefile
%ifarch %ix86 x86_64
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
%ifarch aarch64 ppc64le
	arch/%arch_dir/kernel/module.lds
%endif
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

find %buildroot%kheaders_dir -name ..install.cmd -delete

#provide symlink to autoconf.h for back compat
pushd %buildroot%old_kbuild_dir/include/linux
ln -s ../generated/autoconf.h
ln -s ../generated/utsrelease.h
ln -s ../generated/uapi/linux/version.h
popd

# remove *.bin files
rm -f %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin
touch %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin
touch %buildroot%modules_dir/modules.{alias,dep,devname,softdep,symbols}

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
qemu_opts=""
console=ttyS0
%ifarch %ix86
qemu_arch=i386
%endif
%ifarch ppc64le
qemu_arch=ppc64
console=hvc0
%endif
%ifarch aarch64
qemu_opts="-machine accel=tcg,type=virt -cpu cortex-a57 -drive if=pflash,unit=0,format=raw,readonly,file=%_datadir/AAVMF/QEMU_EFI-pflash.raw"
%endif
timeout --foreground 600 qemu-system-"$qemu_arch" $qemu_opts -kernel %buildroot/boot/vmlinuz-$KernelVer -nographic -append console="$console" -initrd initrd.img > boot.log &&
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
%dir %modules_dir
%defattr(0600,root,root,0700)
%modules_dir/kernel
%modules_dir/modules.order
%modules_dir/modules.builtin*
%exclude %modules_dir/build
%ghost %modules_dir/modules.alias
%ghost %modules_dir/modules.dep
%ghost %modules_dir/modules.devname
%ghost %modules_dir/modules.softdep
%ghost %modules_dir/modules.symbols
%ghost %modules_dir/modules.alias.bin
%ghost %modules_dir/modules.dep.bin
%ghost %modules_dir/modules.symbols.bin
%ghost %modules_dir/modules.builtin.bin
%ifarch aarch64
/lib/devicetree/%kversion-%flavour-%krelease
%endif

%files -n kernel-headers-%flavour
%kheaders_dir

%files -n kernel-headers-modules-%flavour
%kbuild_dir
%old_kbuild_dir
%dir %modules_dir
%modules_dir/build

%if_enabled docs
%files -n kernel-doc-%base_flavour
%doc %_docdir/kernel-doc-%base_flavour-%version
%endif

%changelog
* Wed Feb 26 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.103-alt1.rt42
- Update to v4.19.103-rt42.
- Make ATA modules built-in (for qemu -hda).

* Tue Feb 11 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.100-alt1.rt41
- Update to v4.19.100-rt41.

* Thu Jan 09 2020 Vitaly Chikunov <vt@altlinux.org> 4.19.90-alt1.rt35
- Update to v4.19.90-rt35.

* Sun Nov 24 2019 Vitaly Chikunov <vt@altlinux.org> 4.19.59-alt8.rt24
- Add some more std-def =y options.

* Mon Nov 18 2019 Vitaly Chikunov <vt@altlinux.org> 4.19.59-alt7.rt24
- Add CONFIG_USER_NS=y.

* Mon Oct 14 2019 Vitaly Chikunov <vt@altlinux.org> 4.19.59-alt6.rt24
- Add xz support squashfs (for propagator).

* Thu Sep 19 2019 Vitaly Chikunov <vt@altlinux.org> 4.19.59-alt5.rt24
- Enable virtio_scsi module.

* Sun Sep 08 2019 Vitaly Chikunov <vt@altlinux.org> 4.19.59-alt4.rt24
- Add two OSADL patches for debug purposes:
  + tracing: Add latency histograms
  + Provide individual CPU usage measurement based on idle time
- Enable performance scaling governor by default and disable powersave.
- Disable multiple debug options.

* Sat Sep 07 2019 Vitaly Chikunov <vt@altlinux.org> 4.19.59-alt3.rt24
- Add more performance (disable NO HZ) and tracing options.

* Fri Sep 06 2019 Vitaly Chikunov <vt@altlinux.org> 4.19.59-alt2.rt24
- Enable EFI handover support.

* Thu Sep 05 2019 Vitaly Chikunov <vt@altlinux.org> 4.19.59-alt1.rt24
- Initial build of PREEMPT_RT kernel.
