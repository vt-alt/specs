%define set_disable() %{expand:%%force_disable %{1}} %{expand:%%undefine _enable_%{1}}
%define set_without() %{expand:%%force_without %{1}} %{expand:%%undefine _with_%{1}}

%define base_flavour ovz
%define sub_flavour el7
%define flavour %base_flavour-%sub_flavour

#     rh7-3.10.0-957.27.2.vz7.107.7
%define orelease 957.27.2.vz7.107.7

Name: kernel-image-%flavour
Version: 3.10.0
Release: alt1.%orelease
Epoch: 1

%define kernel_req %nil
%define kernel_prov %nil
%define kernel_branch %version
%define kernel_stable_version 32
%define kernel_extra_version %nil

%define krelease %release

%define kmandir %{_man9dir}l
# Build options
# You can change compiler version by editing this line:
%define kgcc_version %__gcc_version_base
%define nprocs 8

%def_disable verbose
%def_with src
%def_enable docs
%def_enable htmldocs
%def_enable man
%def_disable debug
%def_disable module_sig
%def_with firmware
%def_without perf

%def_enable debug_section_mismatch

%define strip_mod_opts --strip-unneeded -R .comment

## Don't edit below this line ##################################

%define kversion	%kernel_branch%kernel_extra_version
%define modules_dir	/lib/modules/%kversion-%flavour-%krelease
%define firmware_dir	/lib/firmware/%kversion-%flavour-%krelease

%define kheaders_dir	%_prefix/include/linux-%kernel_branch-%flavour
%define kbuild_dir	%_prefix/src/linux-%kversion-%flavour-%krelease
%define old_kbuild_dir	%_prefix/src/linux-%kversion-%flavour

Summary: The Linux kernel (the core of the Linux operating system)
License: GPL
Group: System/Kernel and hardware
Url: http://www.kernel.org/

Source0: rh7-%version.tar
Source1: %flavour.x86_64.config

ExclusiveOS: Linux
ExclusiveArch: x86_64
# ExclusiveArch: x86_64 aarch64 ppc64le

%ifarch x86_64 %ix86
%define kernel_arch x86
%else
%define kernel_arch %_target_cpu
%endif

%ifarch x86_64
%define base_arch x86_64
%endif
%ifarch %ix86
%define base_arch x86
%endif

%ifnarch x86_64 i586 i686
%set_disable docs
%set_without src
%endif

%if "%sub_flavour" != "def"
%set_disable docs
%set_without src
%endif

%if_disabled docs
%set_disable htmldocs
%set_disable man
%endif

%define perf_make_opts %{?_enable_verbose:V=1} prefix=%_prefix perfexecdir=%_libexecdir/perf WERROR=0 EXTRA_CFLAGS="%optflags %{?_disable_debug:-g0}" NO_GTK2=1

BuildPreReq: rpm-build-kernel
BuildRequires: dev86 flex
BuildRequires: libdb4-devel
BuildRequires: bc
%{?kgcc_version:BuildRequires: gcc%kgcc_version}
BuildRequires: module-init-tools >= 3.1
BuildRequires: patch >= 2.6.1-alt1
%{?_with_src:BuildRequires: pxz}

%{?_with_firmware:BuildRequires: hardlink}
%{?_enable_htmldocs:BuildRequires: xmlto transfig ghostscript}
%{?_enable_man:BuildRequires: xmlto}
%{?_with_perf:BuildRequires: binutils-devel libelf-devel asciidoc elfutils-devel >= 0.138 libnewt-devel perl-devel python-dev libunwind-devel libaudit-devel libnuma-devel}
%{?!_without_check:%{?!_disable_check:BuildRequires: qemu-system-x86-core glibc-devel-static}}

Requires: bootloader-utils >= 0.4.21
Requires: module-init-tools >= 3.1
Requires: mkinitrd >= 1:2.9.9-alt1
Requires: startup >= 0.9.8.24.1

Provides: kernel = %kversion
Provides: kernel-modules-md-%flavour = %version-%release

PreReq: coreutils
PreReq: module-init-tools >= 3.1
PreReq: mkinitrd >= 1:2.9.9-alt1
AutoProv: no, %kernel_prov
AutoReq: no, %kernel_req

%description
This package contains the Linux kernel that is used to boot and run
your system.
Most hardware drivers for this kernel are built as modules.  Some of
these drivers are built separately from the kernel; they are available
in separate packages (kernel-modules-*-%flavour).
The "el" variant of kernel packages is derived from sources freely provided
to the public by a prominent North American Enterprise Linux vendor.
This kernel has LTS and suitable for servers and workstations.


%package -n kernel-headers-modules-%flavour
Summary: Headers and other files needed for building kernel modules
Group: Development/Kernel
%{?kgcc_version:Requires: gcc%kgcc_version}
Provides: kernel-headers-modules-%flavour = %version-%release
Provides: kernel-devel-%flavour = %version-%release
%{?base_flavour:Provides: kernel-devel-%base_flavour = %version-%release}
Provides: kernel-devel = %version-%release
#Obsoletes: kernel-headers-modules-%flavour = %version
AutoProv: no

%description -n kernel-headers-modules-%flavour
This package contains header files, Makefiles and other parts of the
Linux kernel build system which are needed to build kernel modules for
the Linux kernel package %name-%version-%release.

If you need to compile a third-party kernel module for the Linux
kernel package %name-%version-%release, install this package
and specify %kbuild_dir as the kernel source directory.


%if_with firmware
%package -n firmware-kernel-%flavour
Summary: Firmware for drivers from %name
Group: System/Kernel and hardware
AutoProv: no
AutoReq: no

%description -n firmware-kernel-%flavour
Firmware for drivers from %name.
%endif


%if_with perf
%package -n perf
Summary: Performance analysis tools for Linux
Group: Development/Tools
AutoReq: yes,noperl,nopython
AutoProv: yes,noperl,nopython

%description -n perf
Performance counters for Linux are a new kernel-based subsystem that provide
a framework for all things performance analysis. It covers hardware level
(CPU/PMU, Performance Monitoring Unit) features and software features
(software counters, tracepoints) as well.
This package contains performance analysis tools for Linux
%endif


%package -n kernel-headers-%flavour
Summary: Header files for the Linux kernel
Group: Development/Kernel
Requires: kernel-headers-common >= 1.1.5
Provides: kernel-headers = %version
%{?base_flavour:Provides: kernel-headers-%base_flavour = %version}
Provides: kernel-headers-%flavour = %version-%release
#Obsoletes: kernel-headers-%flavour = %version
Provides: %kheaders_dir/include
AutoProv: no

%description -n kernel-headers-%flavour
This package makes Linux kernel headers corresponding to the Linux
kernel package %name-%version-%release available for building
userspace programs (if this version of headers is selected by
adjust_kernel_headers).


%if_enabled docs
%define kernel_doc_package_std_body() \
Group: Documentation \
%{?base_flavour:Provides: kernel-%{1}-%base_flavour = %version-%release} \
BuildArch: noarch \
AutoProv: no \
AutoReq: no

%package -n kernel-doc-%flavour
Summary: Linux kernel %kversion-%flavour documentation
%kernel_doc_package_std_body doc

%description -n kernel-doc-%flavour
This package contains documentation files for Linux kernel package
kernel-image-%flavour-%kversion-%krelease
The documentation files contained in this package may be different
from the similar files in upstream kernel distributions, because some
patches applied to the corresponding kernel packages may change things
in the kernel and update the documentation to reflect these changes.


%if_enabled htmldocs
%package -n kernel-docbook-%flavour
Summary: Linux kernel %kversion-%flavour HTML API documentation
%kernel_doc_package_std_body docbook

%description -n kernel-docbook-%flavour
This package contains API documentation HTML files for Linux kernel
package kernel-image-%flavour-%kversion-%krelease
The documentation files contained in this package may be different
from the similar files in upstream kernel distributions, because some
patches applied to the corresponding kernel packages may change things
in the kernel and update the documentation to reflect these changes.
%endif


%if_enabled man
%package -n kernel-man-%flavour
Summary: Linux kernel %kversion-%flavour man pages
%kernel_doc_package_std_body man

%description -n kernel-man-%flavour
This package contains man pages for Linux kernel package
kernel-image-%flavour-%kversion-%krelease
The man pages contained in this package may be different from the similar
files in upstream kernel distributions, because some patches applied to
the corresponding kernel packages may change things in the kernel and
update the documentation to reflect these changes.
%endif
%endif


%if_with src
%package -n kernel-src-%flavour
Summary: Linux kernel %kversion-%flavour sources
Group: Development/Kernel
%{?base_flavour:Provides: kernel-src-%base_flavour = %version-%release}
BuildArch: noarch
AutoProv: no
AutoReq: no

%description -n kernel-src-%flavour
This package contains sources for Linux kernel package
kernel-image-%flavour-%kversion-%krelease
%endif


%prep
%setup -c -n kernel-image-%flavour-%kversion-%krelease
cd rh7-%version

# get rid of unwanted files resulting from patch fuzz
#find . -name "*.orig" -delete -or -name "*~" -delete

# this file should be usable both with make and sh (for broken modules
# which do not use the kernel makefile system)
echo -n "export GCC_VERSION=" > gcc_version.inc
%ifdef kgcc_version
echo "%kgcc_version" \
%else
%__cc -dumpversion | cut -d. -f1-2 \
%endif
	>> gcc_version.inc

%if_with src
cd ..
find rh7-%kversion -type f -or -type l -not -name '*.orig' -not -name '*~' -not -name '.git*' > kernel-src-%flavour.list
cd -
%endif

install -m644 %SOURCE1 .


%build
[ "%__nprocs" -gt "%nprocs" ] || export NPROCS=%nprocs
cd rh7-%version
export ARCH=%base_arch

cp -vf \
	.gear/%flavour.%_target_cpu.config \
	.config

scripts/config \
	%{?_disable_debug_section_mismatch: -d debug_section_mismatch} \
	%{?_disable_debug:-d debug_info} \
	%{?_disable_module_sig:-d module_sig} \
	-d build_docsrc \
	-m reiserfs_fs \
		-E reiserfs_fs reiserfs_fs_security \
		-E reiserfs_fs reiserfs_fs_posix_acl \
		-E reiserfs_fs reiserfs_fs_xattr \
		-D reiserfs_fs reiserfs_proc_info \
		-D reiserfs_fs reiserfs_check \
	-m jfs_fs \
		-D jfs_fs jfs_statistics \
		-D jfs_fs jfs_debug \
		-E jfs_fs jfs_security \
		-E jfs_fs jfs_posix_acl \
	-m f2fs_fs \
		-E f2fs_fs f2fs_fs_posix_acl \
		-E f2fs_fs f2fs_fs_xattr \
		-E f2fs_fs f2fs_stat_fs \
	-m fb_uvesa \
	--set-str localversion -%flavour-%krelease

echo "Building kernel %kversion-%flavour-%krelease"

. ./gcc_version.inc
export CC=gcc-$GCC_VERSION
%make_build olddefconfig
%make_build kernelversion
%make_build kernelrelease
%make_build %{?_enable_verbose:V=1} CC=gcc-$GCC_VERSION bzImage
%make_build %{?_enable_verbose:V=1} CC=gcc-$GCC_VERSION modules

%{?_with_perf:%make_build -C tools/perf %{?_enable_verbose:V=1} %perf_make_opts all man}

echo "Kernel built %kversion-%flavour-%krelease"

# psdocs, pdfdocs don't work yet
%{?_enable_htmldocs:%def_enable builddocs}
%{?_enable_man:%def_enable builddocs}
%if_enabled builddocs
echo "Building kernel docs %kversion-%flavour-%krelease"
%{?_enable_htmldocs:%make_build htmldocs}
%{?_enable_man:%make_build mandocs 2>mandocs.err.log}
echo "Kernel docs built %kversion-%flavour-%krelease"
%endif


%install
export ARCH=%base_arch
cd rh7-%version

install -Dp -m644 System.map %buildroot/boot/System.map-%kversion-%flavour-%krelease
install -Dp -m644 arch/%base_arch/boot/bzImage %buildroot/boot/vmlinuz-%kversion-%flavour-%krelease
install -Dp -m644 .config %buildroot/boot/config-%kversion-%flavour-%krelease

%make_install \
	INSTALL_MOD_PATH=%buildroot \
	INSTALL_FW_PATH=%buildroot%firmware_dir \
	%{!?_enable_debug:%{?strip_mod_opts:INSTALL_MOD_STRIP="%strip_mod_opts"}} \
	modules_install

install -d -m 0755 %buildroot%kbuild_dir
cp -aL include %buildroot%kbuild_dir/
for t in f d; do
	find %buildroot%kbuild_dir/include/config -type $t -empty -delete
done
for d in arch/%kernel_arch/include; do
	a="$(dirname "$d")"
	install -d -m 0755 %buildroot%kbuild_dir/$a
	cp -a $d %buildroot%kbuild_dir/$a/
	install -p -m 0644 $a/Makefile* %buildroot%kbuild_dir/$a/
done
find %buildroot%kbuild_dir/{include,arch} -type f -name Kbuild -delete

%if 0
# drivers-headers install
install -d -m 0755 %buildroot%kbuild_dir/{drivers/{scsi,md,usb/core,net/wireless},net/mac80211,kernel,lib}
install -m 0644 drivers/scsi/scsi{{,_typedefs}.h,_module.c} %buildroot%kbuild_dir/drivers/scsi/
install -m 0644 drivers/md/dm*.h %buildroot%kbuild_dir/drivers/md/
install -m 0644 drivers/usb/core/*.h %buildroot%kbuild_dir/drivers/usb/core/
install -m 0644 drivers/net/wireless/Kconfig %buildroot%kbuild_dir/drivers/net/wireless/
install -m 0644 lib/hexdump.c %buildroot%kbuild_dir/lib/
install -m 0644 kernel/workqueue.c %buildroot%kbuild_dir/kernel/
install -m 0644 net/mac80211/{ieee80211_i,sta_info}.h %buildroot%kbuild_dir/net/mac80211/
%endif

# Install files required for building external modules (in addition to headers)
for f in \
	.config \
	Makefile \
	Module.symvers \
	scripts/Kbuild.include \
	scripts/Makefile{,.{build,clean,host,lib,mod*}} \
	scripts/bin2c \
	scripts/check{includes,version}.pl \
	scripts/conmakehash \
	scripts/depmod.sh \
	scripts/extract-ikconfig \
	scripts/gcc-*.sh \
	scripts/kallsyms \
	scripts/makelst \
	scripts/mk{compile_h,makefile,version} \
	scripts/module-common.lds \
	scripts/pnmtologo \
	scripts/recordmcount* \
	scripts/basic/fixdep \
	scripts/genksyms/genksyms \
	scripts/kconfig/conf \
	scripts/mod/{modpost,mk_elfconfig} \
	gcc_version.inc
do
	if [ -f "$f" ]; then
		[ -x "$f" ] && mode=0755 || mode=0644
		install -Dp -m $mode {,%buildroot%kbuild_dir/}$f
	fi
done

# Provide kbuild directory with old name (without %%krelease)
ln -s "$(relative %kbuild_dir %old_kbuild_dir)" %buildroot%old_kbuild_dir

# Provide kernel headers for userspace
make -j%__nprocs headers_install INSTALL_HDR_PATH=%buildroot%kheaders_dir
find %buildroot%kheaders_dir -type f -a \( -name .install -o -name ..install.cmd \) -delete

# Fix symlinks to kernel sources in /lib/modules
rm -f %buildroot%modules_dir/{build,source}
ln -s %kbuild_dir %buildroot%modules_dir/build

%if_with perf
%makeinstall_std -C tools/perf %perf_make_opts install-man
install -d -m 0755 %buildroot%_docdir/perf-%version
install -m 0644 tools/perf/{CREDITS,design.txt,Documentation/examples.txt} %buildroot%_docdir/perf-%version/
%endif

# install documentation
%if_enabled docs
install -d %buildroot%_docdir/kernel-doc-%flavour/
for I in Documentation/*; do
	case "$(basename "$I")" in
		DocBook)
%if_enabled htmldocs
			for J in "$I"/*.tmpl; do
				j=$(basename "$J" .tmpl)
				[ -d "$I/$j" ] || continue
				install -d -m 0755 %buildroot%_docdir/kernel-doc-%flavour/DocBook/"$j"
				install -m 0644 "$I/$j"/*.html %buildroot%_docdir/kernel-doc-%flavour/DocBook/"$j"/
				install -m 0644 "$I/$j.html" %buildroot%_docdir/kernel-doc-%flavour/DocBook/
			done
%endif
			;;
		[a-z][a-z]_[A-Z][A-Z]|Makefile|dontdiff) ;;
		*) cp -aL "$I" %buildroot%_docdir/kernel-doc-%flavour/ ;;
	esac
done
find %buildroot%_docdir/kernel-doc-%flavour -type f -name Makefile -delete
%if_enabled man
install -d %buildroot%kmandir
install -m 0644 Documentation/DocBook/man/* %buildroot%kmandir/
%endif
%endif

cd -

%if_with src
install -d -m 0755 %kernel_srcdir
t="%__nprocs"
[ $t -gt 1 ] && XZ="pxz -T$t" || XZ="xz"
tar	--transform='s/^\(linux-%kversion\)/\1-%flavour-%krelease/' \
	--owner=root --group=root --mode=u+w,go-w,go+rX \
	-T kernel-src-%flavour.list \
	-cf - | \
	$XZ -8e > %kernel_srcdir/linux-%kversion-%flavour-%krelease.tar.xz
%endif

%if_with firmware
hardlink -c %buildroot%firmware_dir
%ifdef brp_strip_none
%brp_strip_none %firmware_dir/*
%else
%add_strip_skiplist %firmware_dir/*
%endif
%add_verify_elf_skiplist %firmware_dir/*
%endif

%check
mkdir test
cd test
gcc -static -xc -o init - <<EOF
#include <unistd.h>
#include <stdio.h>
#include <err.h>
#include <sys/mount.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/reboot.h>
void main()
{
	if (mkdir("/proc", 0666))
		warn("mkdir /proc");
	else if (mount("proc", "/proc", "proc", 0, NULL))
		warn("mount /proc");
	else if (access("/proc/user_beancounters", R_OK))
		warn("access /proc/user_beancounters");
	else
		puts("Boot successful!");
	reboot(RB_POWER_OFF);
}
EOF
echo "init" | cpio -H newc -o | gzip > initrd.img
time -p \
timeout 600 qemu-system-x86_64 -bios bios.bin \
	-nographic -no-reboot -m 256M \
	-kernel %buildroot/boot/vmlinuz-%kversion-%flavour-%krelease \
	-initrd initrd.img \
	-append "console=ttyS0 panic=-1" > boot.log &&
grep -q "^Boot successful" boot.log &&
grep -qE '^(\[ *[0-9]+\.[0-9]+\] *)?(reboot: )?Power down' boot.log || {
	cat >&2 boot.log
	echo >&2 'Marker not found'
	exit 1
}
grep beancounter boot.log

%files
/boot/*
%dir %modules_dir
%modules_dir/modules.alias*
%modules_dir/modules.builtin
%modules_dir/modules.dep*
%modules_dir/modules.order
%modules_dir/modules.symbols*
%ghost %modules_dir/modules.builtin.bin
%ghost %modules_dir/modules.devname
%ghost %modules_dir/modules.softdep
%modules_dir/kernel


%files -n kernel-headers-%flavour
%kheaders_dir


%if_with firmware
%files -n firmware-kernel-%flavour
%dir /lib/firmware
%firmware_dir
%endif


%if_with perf
%files -n perf
%doc %_docdir/perf-%version
%_sysconfdir/bash_completion.d
%_bindir/perf
%_libexecdir/perf
%_man1dir/*
%endif


%files -n kernel-headers-modules-%flavour
%kbuild_dir
%old_kbuild_dir
%dir %modules_dir
%modules_dir/build


%if_enabled docs
%files -n kernel-doc-%flavour
%doc %_docdir/kernel-doc-%flavour
%{?_enable_htmldocs:%exclude %_docdir/kernel-doc-%flavour/DocBook}


%if_enabled htmldocs
%files -n kernel-docbook-%flavour
%doc %dir %_docdir/kernel-doc-%flavour
%doc %_docdir/kernel-doc-%flavour/DocBook
%endif


%if_enabled man
%files -n kernel-man-%flavour
%kmandir
%endif
%endif


%if_with src
%files -n kernel-src-%flavour
%_usrsrc/kernel
%endif


%changelog
* Wed Sep 18 2019 Andrew A. Vasilyev <andy@altlinux.org> 1:3.10.0-alt1.957.27.2.vz7.107.7
- Build 3.10.0-alt1.957.27.2.vz7.107.7

* Fri Sep 13 2019 Andrew A. Vasilyev <andy@altlinux.org> 1:3.10.0-alt1.957.27.2.vz7.107.6
- Build 3.10.0-alt1.957.27.2.vz7.107.6

* Wed Sep 11 2019 Andrew A. Vasilyev <andy@altlinux.org> 1:3.10.0-alt1.957.27.2.vz7.107.5
- Build 3.10.0-alt1.957.27.2.vz7.107.5

* Tue Sep 10 2019 Vitaly Chikunov <vt@altlinux.org> 1:3.10.0-alt1.957.27.2.vz7.107.4
- Build 3.10.0-alt1.957.27.2.vz7.107.4

* Sat Aug 24 2019 Vitaly Chikunov <vt@altlinux.org> 1:3.10.0-alt1.957.21.3.vz7.106.7
- Import rh7-3.10.0-957.21.3.vz7.106.7
- Fix qemu run after qemu package update.
- Update boot test.

* Thu Aug 01 2019 Vitaly Chikunov <vt@altlinux.org> 1:3.10.0-alt1.957.21.3.vz7.106.6
- Build 3.10.0-957.21.3.vz7.106.6

* Mon Mar 25 2019 Vitaly Chikunov <vt@altlinux.org> 1:3.10.0-alt1.957.5.1.vz7.84.2
- Build 3.10.0-alt1.957.5.1.vz7.84.2

* Tue Mar 19 2019 Vitaly Chikunov <vt@altlinux.org> 3.10.0-alt1.957.vz7.82.3
- Build 3.10.0-alt1.957.vz7.82.3

* Thu Apr  5 2018 Vitaly Chikunov <vt@altlinux.org> 3.10.0-alt1.693.17.1.vz7.45.7
- Second build (3.10.0-alt1.693.17.1.vz7.45.7)

* Mon Feb 12 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.10.0-alt1.693.11.6.vz7.42.2
- Initial build (rh7-3.10.0-693.11.6.vz7.42.2).
