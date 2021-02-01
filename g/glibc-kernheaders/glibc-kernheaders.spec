%define kernel_base_version 5.5
%define kernel_source kernel-source-%kernel_base_version

Name: glibc-kernheaders
Version: %kernel_base_version
Release: alt1

Summary: Linux kernel C header files for use by glibc and other userspace software
# grep -Fhwr SPDX-License-Identifier: /usr/include/linux-default/include |sort |uniq -c |sort -n
#   1 /* SPDX-License-Identifier: ((GPL-2.0 WITH Linux-syscall-note) AND MIT) */
#   1 /* SPDX-License-Identifier: (GPL-2.0 WITH Linux-syscall-note) */
#   1 /* SPDX-License-Identifier: (GPL-2.0 WITH Linux-syscall-note) OR BSD-3-Clause */
#   1 /* SPDX-License-Identifier: (GPL-2.0 WITH Linux-syscall-note) OR MIT */
#   1 /* SPDX-License-Identifier: (GPL-2.0 WITH Linux-syscall-note) or BSD-3-Clause */
#   1 /* SPDX-License-Identifier: GPL-2.0 WITH Linux-syscall-note
#   1 /* SPDX-License-Identifier: GPL-2.0-or-later WITH Linux-syscall-note */
#   2 /* SPDX-License-Identifier: ((GPL-2.0 WITH Linux-syscall-note) OR CDDL-1.0) */
#   2 /* SPDX-License-Identifier: BSD-3-Clause */
#   3 /* SPDX-License-Identifier: ((GPL-2.0 WITH Linux-syscall-note) OR MIT) */
#   3 /* SPDX-License-Identifier: LGPL-2.1 WITH Linux-syscall-note */
#   3 /* SPDX-License-Identifier: MIT */
#   4 /* SPDX-License-Identifier: ((GPL-2.0+ WITH Linux-syscall-note) OR BSD-3-Clause) */
#   4 /* SPDX-License-Identifier: LGPL-2.0+ WITH Linux-syscall-note */
#   5 /* SPDX-License-Identifier: ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-3-Clause) */
#   5 /* SPDX-License-Identifier: GPL-2.0-only WITH Linux-syscall-note */
#   6 /* SPDX-License-Identifier: ((GPL-2.0 WITH Linux-syscall-note) OR BSD-2-Clause) */
#  12 /* SPDX-License-Identifier: GPL-1.0+ WITH Linux-syscall-note */
#  15 /* SPDX-License-Identifier: LGPL-2.1+ WITH Linux-syscall-note */
#  17 /* SPDX-License-Identifier: ((GPL-2.0 WITH Linux-syscall-note) OR BSD-3-Clause) */
#  17 /* SPDX-License-Identifier: ((GPL-2.0 WITH Linux-syscall-note) OR Linux-OpenIB) */
# 118 /* SPDX-License-Identifier: GPL-2.0+ WITH Linux-syscall-note */
# 569 /* SPDX-License-Identifier: GPL-2.0 WITH Linux-syscall-note */
License: GPL-2.0-only with Linux-syscall-note
Group: Development/Kernel
Url: http://www.kernel.org/

# git://git.altlinux.org/gears/g/%name.git
#Patch: %name-%version-%release.patch

Patch1: 0001-uapi-fix-linux-sysctl.h-userspace-compilation-errors.patch
Patch2: 0002-uapi-move-struct-reiserfs_security_handle-out-from-l.patch
Patch3: 0003-uapi-fix-linux-nfc.h-userspace-compilation-errors.patch
Patch4: 0004-uapi-fix-linux-vm_sockets.h-userspace-compilation-er.patch
Patch5: 0005-uapi-fix-linux-sctp.h-userspace-compilation-errors.patch
Patch6: 0006-uapi-fix-asm-shmbuf.h-userspace-compilation-errors.patch
Patch7: 0007-uapi-fix-another-asm-shmbuf.h-userspace-compilation-.patch
Patch8: 0008-uapi-fix-asm-signal.h-userspace-compilation-errors.patch
Patch9: 0009-uapi-introduce-__kernel_uapi_size_t.patch
Patch10: 0010-x86-uapi-fix-asm-signal.h-userspace-compilation-erro.patch
Patch11: 0011-uapi-fix-linux-kexec.h-userspace-compilation-errors.patch
Patch12: 0012-uapi-fix-linux-omapfb.h-userspace-compilation-error.patch
Patch13: 0013-uapi-fix-linux-fsmap.h-userspace-compilation-error.patch
Patch14: 0014-uapi-fix-linux-usb-audio.h-userspace-compilation-err.patch
Patch15: 0015-uapi-fix-linux-sysctl.h-Obsolete-types-detected-warn.patch

BuildRequires: rpm-build-kernel rsync
BuildRequires: %kernel_source = 1.0.0

%if 0%{!?mips:1}
%define mips mips mipsn32 mips64 mipsel mipsn32el mips64el
%endif

%ifarch %ix86 x86_32 x86_64 x32
%define base_arch x86
%endif
%ifarch %arm
%define base_arch arm
%endif
%ifarch aarch64
%define base_arch arm64
%endif
%ifarch ppc ppc64 ppc64le
%define base_arch powerpc
%endif
%ifarch riscv riscv64
%define base_arch riscv
%endif
%ifarch s390 s390x
%define base_arch s390
%endif
%ifarch %mips
%define base_arch mips
%endif
%if 0%{!?base_arch}
%{error:%_target_cpu is not supported}
%endif

Requires: %name-%base_arch = %EVR
Provides: kernel-headers = %EVR
Provides: linux-libc-headers = %EVR
Obsoletes: linux-libc-headers < %version

%description
This package includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.
The header files define structures and constants that are needed for
building most standard programs and are also needed to build glibc.

%package generic
Summary: Generic Linux kernel C header files
Group: Development/Kernel
BuildArch: noarch
Conflicts: %name < %version
AutoReq: nocpp

%description generic
This package contains generic C header files that specify the interface
between the Linux kernel and userspace libraries and programs.
The header files define structures and constants that are needed for
building most standard programs and are also needed to build glibc.

%global kernel_arches %nil

%global do_package() \
%if 0%{2} \
%package %{1} \
Summary: %{1}-specific Linux kernel C header files \
Group: Development/Kernel \
BuildArch: noarch \
Requires: %name-generic = %EVR \
AutoReq: nocpp \
%description %{1} \
This package contains %{1}-specific C header files that specify \
the interface between the Linux kernel and userspace libraries and programs. \
The header files define structures and constants that are needed for \
building most standard programs and are also needed to build glibc. \
%endif

# In the kernel tree:
# ls arch/*/include/uapi/asm/Kbuild | sed -n 's|^arch/\([^/ ]\+\)/.*|\1|p' | sort | xargs echo %%define kernel_arches
%define kernel_arches alpha arc arm arm64 c6x csky h8300 hexagon ia64 m68k microblaze mips nds32 nios2 openrisc parisc powerpc riscv s390 sh sparc unicore32 x86 xtensa

# ls arch/*/include/uapi/asm/Kbuild | sed -n 's|^arch/\([^/ ]\+\)/.*|%%do_package \1 1|p' | sort
%do_package alpha 1
%do_package arc 1
%do_package arm 1
%do_package arm64 1
%do_package c6x 1
%do_package csky 1
%do_package h8300 1
%do_package hexagon 1
%do_package ia64 1
%do_package m68k 1
%do_package microblaze 1
%do_package mips 1
%do_package nds32 1
%do_package nios2 1
%do_package openrisc 1
%do_package parisc 1
%do_package powerpc 1
%do_package riscv 1
%do_package s390 1
%do_package sh 1
%do_package sparc 1
%do_package unicore32 1
%do_package x86 1
%do_package xtensa 1

%package all
Summary: All Linux kernel C header files
Group: Development/Kernel
BuildArch: noarch
Requires: %(for a in %kernel_arches; do printf '%%s = %%s ' %name-$a %EVR; done)

%description all
This package pulls in all other %name-* packages.

%prep
%setup -cT
tar -xf %kernel_src/%kernel_source.tar
cd %kernel_source
#%%patch -p1

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

# No exceptions, please!
sed -i 's/^no-export-headers/#&/' include/uapi/Kbuild

%build
mkdir -p headers
base_done=
for hdr_arch in %kernel_arches; do
	mkdir -p headers/"$hdr_arch"
	[ "$hdr_arch" != %base_arch ] || base_done=1
	make -C %kernel_source headers_install \
		ARCH="$hdr_arch" INSTALL_HDR_PATH="$PWD"/headers/"$hdr_arch" \
		&& rc= || rc=$?
	[ -z "$rc" ] || exit $rc
	find headers/"$hdr_arch"/include -name "*.install*" -delete
	mv headers/"$hdr_arch"/include/asm{,-"$hdr_arch"}
	(cd headers/"$hdr_arch"/include && find -type f -exec sha1sum {} +) |
		LC_COLLATE=C sort > "$hdr_arch".list
	if [ -s generic.list ]; then
		comm -12 generic.list "$hdr_arch".list > generic.list+
		mv generic.list+ generic.list
	else
		cp "$hdr_arch".list generic.list
	fi
done

for hdr_arch in %kernel_arches; do
	comm -23 "$hdr_arch".list generic.list > "$hdr_arch"-specific.list
done

sort -u *-specific.list |
	sed 's/.* //' |
	sort |
	uniq -d > dups.list
if [ -s dups.list ]; then
	cat >&2 dups.list
	exit 1
fi

[ -n "$base_done" ] || {
	echo >&2 "headers for %base_arch has not been generated"
	exit 1
}

ln -s generic.list generic-specific.list

%install
%define hdr_dir %_includedir/linux-default

gen_files()
{
	a="$1"; shift

	while read h file; do
		for dir in headers/*/include; do
			[ -f "$dir/$file" ] || continue
			install -pD -m644 "$dir/$file" \
				"%buildroot%hdr_dir/include/$file"
			echo "%hdr_dir/include${file#.}"
			break
		done
	done < "$a"-specific.list > package-"$a".files

	sed -n 's|^\(/.\+/\)[^/]\+$|%dir \1|p' < package-"$a".files |
		sort -u > dir-"$a".files

	cat >> package-"$a".files <<-@@@
	%%dir %hdr_dir/
	%%dir %hdr_dir/include/
	@@@
	cat dir-"$a".files >> package-"$a".files
}

for hdr_arch in generic %kernel_arches; do
	gen_files "$hdr_arch"
done

ln -s asm-%base_arch %buildroot%hdr_dir/include/asm

%check
set +x
d="$PWD"
cd %buildroot%hdr_dir/include
find asm/ [^a]* -type f -name '*.h' |sort |while read f; do
	%__cc -D_GNU_SOURCE %optflags \
		-S -o/dev/null -xc /dev/null -I. -include "$f" ||
		echo "$f"
done > "$d"/fail.list
if [ -s "$d"/fail.list ]; then
	echo "Compilation check failed for $(grep -Fc .h -- "$d"/fail.list) files:"
	cat -- "$d"/fail.list
fi
cd - > /dev/null

%define _unpackaged_files_terminate_build 1

%global do_files() \
%if 0%{2} \
%files %{1} -f package-%{1}.files \
%endif

# ls arch/*/include/uapi/asm/Kbuild | sed -n 's|^arch/\([^/ ]\+\)/.*|%%do_files \1 1|p' | sort
%do_files alpha 1
%do_files arc 1
%do_files arm 1
%do_files arm64 1
%do_files c6x 1
%do_files csky 1
%do_files h8300 1
%do_files hexagon 1
%do_files ia64 1
%do_files m68k 1
%do_files microblaze 1
%do_files mips 1
%do_files nds32 1
%do_files nios2 1
%do_files openrisc 1
%do_files parisc 1
%do_files powerpc 1
%do_files riscv 1
%do_files s390 1
%do_files sh 1
%do_files sparc 1
%do_files unicore32 1
%do_files x86 1
%do_files xtensa 1

%files generic -f package-generic.files

%files all

%files
%dir %hdr_dir/
%dir %hdr_dir/include/
%hdr_dir/include/asm

%changelog
* Mon Jan 27 2020 Dmitry V. Levin <ldv@altlinux.org> 5.5-alt1
- v5.4 -> v5.5.

* Mon Nov 25 2019 Dmitry V. Levin <ldv@altlinux.org> 5.4-alt1
- v5.3 -> v5.4.

* Sun Sep 15 2019 Dmitry V. Levin <ldv@altlinux.org> 5.3-alt1
- v5.2 -> v5.3.

* Sun Jul 07 2019 Dmitry V. Levin <ldv@altlinux.org> 5.2-alt1
- v5.1 -> v5.2.

* Mon May 06 2019 Dmitry V. Levin <ldv@altlinux.org> 5.1-alt1
- v5.0 -> v5.1.

* Thu Mar 14 2019 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt2
- Fixed linux/sysctl.h "Obsolete types detected" warning
  reported by confused glibc misc/check-installed-headers-c test.
- Updated license information.

* Sun Mar 03 2019 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt1
- v4.20 -> v5.0.

* Mon Dec 17 2018 Dmitry V. Levin <ldv@altlinux.org> 4.20-alt1
- v4.19 -> v4.20.

* Fri Nov 23 2018 Dmitry V. Levin <ldv@altlinux.org> 4.19-alt2
- Added subpackages with header files for all architectures
  supported by the kernel (by glebfm@ and me).

* Mon Oct 22 2018 Dmitry V. Levin <ldv@altlinux.org> 4.19-alt1
- v4.18 -> v4.19.

* Mon Aug 13 2018 Dmitry V. Levin <ldv@altlinux.org> 4.18-alt1
- v4.17 -> v4.18.

* Thu Jun 07 2018 Dmitry V. Levin <ldv@altlinux.org> 4.17-alt1
- v4.16 -> v4.17.

* Thu Apr 05 2018 Dmitry V. Levin <ldv@altlinux.org> 4.16-alt1
- v4.15 -> v4.16.

* Tue Jan 30 2018 Dmitry V. Levin <ldv@altlinux.org> 4.15-alt1
- v4.14 -> v4.15.

* Sun Nov 12 2017 Dmitry V. Levin <ldv@altlinux.org> 4.14-alt1
- v4.13 -> v4.14.

* Sun Sep 03 2017 Dmitry V. Levin <ldv@altlinux.org> 4.13-alt1
- v4.12 -> v4.13.

* Wed Jul 05 2017 Dmitry V. Levin <ldv@altlinux.org> 4.12-alt2
- Fixed compilation errors in 5 header files.

* Wed Jul 05 2017 Dmitry V. Levin <ldv@altlinux.org> 4.12-alt1
- v4.11-rc7 -> v4.12.
- Split out -generic and -%base_arch noarch subpackages:
  moved arch-independent files to -generic noarch subpackage,
  asm-* directory to -%base_arch noarch subpackage,
  the only thing that remains in the main package
  (which is no longer noarch) is the asm symlink.

* Sun Apr 16 2017 Dmitry V. Levin <ldv@altlinux.org> 4.11-alt0.rc7
- v4.10 -> v4.11-rc7.
- Dropped %hdr_dir/include/asm-%_target_cpu symlink.
- BuildArch: noarch.

* Fri Mar 03 2017 Dmitry V. Levin <ldv@altlinux.org> 4.10-alt2
- Fixed compilation errors in 27 header files.

* Sun Feb 19 2017 Dmitry V. Levin <ldv@altlinux.org> 4.10-alt1
- v4.10-rc8-42-g558e8e2 -> v4.10.

* Thu Feb 16 2017 Dmitry V. Levin <ldv@altlinux.org> 4.10-alt0.rc8.42.g558e8e2
- v4.10-rc8 -> v4.10-rc8-42-g558e8e2.
- Fixed compilation errors in 8 header files.

* Tue Feb 14 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.10-alt0.rc8
- v4.9 -> v4.10-rc8.

* Sun Dec 11 2016 Dmitry V. Levin <ldv@altlinux.org> 4.9-alt1
- v4.8 -> v4.9.

* Sun Oct 02 2016 Dmitry V. Levin <ldv@altlinux.org> 4.8-alt1
- v4.7 -> v4.8.

* Mon Jul 25 2016 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt1
- v4.6 -> v4.7.

* Mon May 23 2016 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt1
- Updated to v4.6.

* Wed Jan 13 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.4-alt1
- Updated to v4.4.

* Wed Sep 09 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.2-alt1
- Updated to v4.2.
- Added aarch64 support.

* Mon Jul 27 2015 Dmitry V. Levin <ldv@altlinux.org> 4.1.3-alt1
- Updated to v4.1.3.

* Fri Jan 30 2015 Dmitry V. Levin <ldv@altlinux.org> 3.18.5-alt1
- Updated to v3.18.5.

* Mon Mar 31 2014 Dmitry V. Levin <ldv@altlinux.org> 3.12.16-alt1
- Updated to v3.12.16.

* Wed May 29 2013 Dmitry V. Levin <ldv@altlinux.org> 3.9.4-alt1
- Updated to v3.9.4.

* Thu Mar 21 2013 Dmitry V. Levin <ldv@altlinux.org> 3.8.4-alt1
- Updated to v3.8.4.

* Sun Sep 30 2012 Dmitry V. Levin <ldv@altlinux.org> 3.5.4-alt1
- Updated to v3.5.4.

* Fri Jun 08 2012 Dmitry V. Levin <ldv@altlinux.org> 3.3.8-alt1
- Updated to v3.3.8.

* Mon May 14 2012 Dmitry V. Levin <ldv@altlinux.org> 3.3.6-alt1
- Updated to v3.3.6.

* Sat May 12 2012 Dmitry V. Levin <ldv@altlinux.org> 3.3.5-alt2
- Added %%check.
- Added a workaround for
  https://bugzilla.altlinux.org/show_bug.cgi?id=27320#c3

* Fri May 11 2012 Dmitry V. Levin <ldv@altlinux.org> 3.3.5-alt1
- Updated to v3.3.5.
- Dropped upgrade trigger.
- Packaged /usr/include/linux-default/include/asm-%%_target_cpu symlink
  to make packages always different on different architectures.

* Fri Dec 03 2010 Dmitry V. Levin <ldv@altlinux.org> 2.6.36-alt5
- linux/netlink.h: fixed gcc -Wconversion compilation warning.

* Fri Oct 29 2010 Kirill A. Shutemov <kas@altlinux.org> 2.6.36-alt4
- Restore kvm.h, kvm_para.h an a.out (regression after 2.6.36-alt2).

* Fri Oct 22 2010 Dmitry V. Levin <ldv@altlinux.org> 2.6.36-alt3
- Fixed upgrade from earlier releases where %%asmdir
  was a directory.
- Dropped unsupported architectures.

* Fri Oct 22 2010 Kirill A. Shutemov <kas@altlinux.org> 2.6.36-alt2
- Make package noarch:
  + package headers for all architectures
  + setup asm symlink on %%post

* Fri Oct 15 2010 Kirill A. Shutemov <kas@altlinux.org> 2.6.36-alt1
- Updated to v2.6.36
- Drop useless fail.log

* Fri Mar 26 2010 Kirill A. Shutemov <kas@altlinux.org> 2.6.33-alt1
- Updated to v2.6.33

* Tue Oct 27 2009 Kirill A. Shutemov <kas@altlinux.org> 2.6.32-alt1
- Updated to v2.6.32-rc5

* Tue May 12 2009 Kirill A. Shutemov <kas@altlinux.ru> 2.6.29-alt3
- Updated to v2.6.29.3
- Use "powerpc" base arch on ppc and ppc64
- Delete .install and ..install.cmd files

* Tue Feb 24 2009 Kirill A. Shutemov <kas@altlinux.ru> 2.6.29-alt2
- Updated to v2.6.29-rc6

* Sun Feb 22 2009 Kirill A. Shutemov <kas@altlinux.ru> 2.6.29-alt1
- Updated to v2.6.29-rc5
- Reexport <linux/ext2_fs.h> and <linux/inotify.h> since changes
  is not approved by upstream

* Wed Sep 17 2008 Kirill A. Shutemov <kas@altlinux.ru> 2.6.27-alt3
- Unexport <linux/ext2_fs.h> and <linux/inotify.h>

* Tue Sep 16 2008 Kirill A. Shutemov <kas@altlinux.ru> 2.6.27-alt2
- linux/inotify.h: do not include <linux/fcntl.h> in userspace
- linux/smb.h: do not include <linux/time.h> in userspace

* Wed Sep 10 2008 Kirill A. Shutemov <kas@altlinux.ru> 2.6.27-alt1
- Update to v2.6.27-rc6
- There is no kernel-source-2.6.27 in Sisyphus, so pack whole tree

* Wed Sep 03 2008 Kirill A. Shutemov <kas@altlinux.ru> 2.6.24-alt5
- Use rpm-build-kernel instead kernel-build-tools in Buildrequires

* Sat Mar 29 2008 Kirill A. Shutemov <kas@altlinux.ru> 2.6.24-alt4
- Export aligned_u64, aligned_be64 and aligned_le64 to userspece

* Tue Mar 25 2008 Kirill A. Shutemov <kas@altlinux.ru> 2.6.24-alt3
- Sync with kernel-image-std-def-2.6.24-alt5
- Include <linux/fs.h> into linux/ext2_fs.h for FS_IOC* defines

* Fri Mar 21 2008 Kirill A. Shutemov <kas@altlinux.ru> 2.6.24-alt2
- Make linux/wireless.h be able to compile
- Include <linux/types.h> into linux/if_arp.h for __u* typedef
- Include <linux/types.h> into linux/atmmpc.h for __be32 typedef
- Wrap 'struct termios' into ifdef __KERNEL_ to avoid conflict with glibc

* Tue Mar 04 2008 Kirill A. Shutemov <kas@altlinux.ru> 2.6.24-alt1
- Based on kernel-image-std-def-2.6.24-alt5
- Dropped _syscallX macros

* Sat Feb 09 2008 Dmitry V. Levin <ldv@altlinux.org> 2.6.18-alt4
- Merged with kernel-image-std-smp-2.6.18-alt11.
- asm-powerpc/unistd.h: Fixed a leftover from a merge (Wartan Hachaturow).
- Unexported asm/page.h, asm/elf.h, asm/user.h and linux/user.h (Kirill A. Shutemov).

* Thu Nov 29 2007 Dmitry V. Levin <ldv@altlinux.org> 2.6.18-alt3
- Reenabled AutoReqProv.

* Sun Nov 04 2007 Sergey Vlasov <vsu@altlinux.ru> 2.6.18-alt2
- Fix package upgrade (%_includedir/linux-default/include/asm was a symlink
  before moving to "make headers_install", but now it is a real directory).

* Tue Oct 30 2007 Dmitry V. Levin <ldv@altlinux.org> 2.6.18-alt1
- Specfile cleanup.

* Tue Oct 23 2007 Kirill A. Shutemov <kas@altlinux.ru> 2.6.18-alt0.9
- Use kernel's "make headers_install" to generate userspace headers
- Based on kernel-image-std-smp-2.6.18-alt8
- Headers fixes:
  + Fix noise in futex.h
  + V4L/DVB (5867): videodev2.h: add missing <sys/time.h> for userspace
  + Restore macros _syscallX
  + linux/types.h related fixes:
    + use __u8/__u32 in userspace ioctl defines for I2O
    + linux/audit.h needs linux/types.h
    + replace u8 and u32 with __u8 and __u32 in scsi.h for user space
    + include <linux/types.h> into linux/if_fddi.h for __be16 typedef
    + include <linux/types.h> into linux/nbd.h for __be32 and __be64 typedefs
    + include <linux/types.h> into linux/ethtool.h for __u32 typedef
- Export linux/serial_reg.h and asm/unaligned.h to userspace

* Sun Sep 23 2007 Dmitry V. Levin <ldv@altlinux.org> 2.6.17-alt7
- Made linux/sem.h and linux/videodev2.h compilable in userspace.
- Provides/Obsoletes linux-libc-headers.

* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 2.6.17-alt6
- Updated linux/futex.h (Kirill A. Shutemov):
  + Backported FUTEX_* constants.
  + Fixed linux/futex.h compilation.

* Thu Jan 25 2007 Dmitry V. Levin <ldv@altlinux.org> 2.6.17-alt5
- Disabled sanitization of compiler*.h.

* Thu Jan 25 2007 Dmitry V. Levin <ldv@altlinux.org> 2.6.17-alt4
- Sanitize headers (#10634).

* Sun Oct 08 2006 Dmitry V. Levin <ldv@altlinux.org> 2.6.17-alt3
- linux/joystick.h: Include <linux/types.h> instead of <asm/types.h>.
- asm-i386/system.h: Replace u(8|16|32) types with __u(8|16|32).

* Fri Oct 06 2006 Dmitry V. Levin <ldv@altlinux.org> 2.6.17-alt2
- Removed improper kernheaders-2.6.9-alt-byteorder.patch, see
  https://bugzilla.altlinux.org/show_bug.cgi?id=5409#c5 for details.
- linux/types.h:
  + Include <sys/types.h>;
  + Hide "struct ustat" definition from userspace.
- linux/cciss_ioctl.h: Include <linux/compiler.h>.

* Mon Oct 02 2006 Dmitry V. Levin <ldv@altlinux.org> 2.6.17-alt1
- Updated to linux-2.6.17.
- Applied patch from SuSE to make headers more ready for userspace.
- Backported byteorder and MAX_NESTED_LINKS fixes from std26 headers.

* Tue Oct 04 2005 Dmitry V. Levin <ldv@altlinux.org> 2.4.29-alt2
- Fixed linux/if_fddi.h (see #8122).

* Tue Aug 09 2005 Anton D. Kachalov <mouse@altlinux.org> 2.4.29-alt1
- Updated headers to 2.4.29.
- Updated asm/unistd.h to linux-2.6.12.
- Added headers for x86_64 architecture.
- Added URL.

* Tue May 10 2005 Dmitry V. Levin <ldv@altlinux.org> 2.4.25-alt2
- Updated asm/termbits.h to linux-2.6.11.
- Updated asm/unistd.h to linux-2.6.11.
- Updated linux/prctl.h to linux-2.6.11.

* Sat Apr 10 2004 Dmitry V. Levin <ldv@altlinux.org> 2.4.25-alt1
- Updated to linux-2.4.25.
- Updated linux/prctl.h to linux-2.6.5.
- Updated asm/unistd.h to linux-2.6.5.

* Fri Jun 20 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.21-alt1
- Updated to linux-2.4.21.

* Mon Jun 09 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4-alt4
- Relocated to proper place, %_includedir/linux-default/include/.

* Tue Jun 03 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4-alt3
- Tarball and specfile cleanup.

* Wed May 28 2003 Peter Novodvorsky <nidd@altlinux.com> 2.4-alt2
- Removed all requires.

* Tue May 27 2003 Peter Novodvorsky <nidd@altlinux.com> 2.4-alt1
- Rebuilt with ALTLinux adaptations for new kernel policy.

* Sun Apr 13 2003 Ajran van de Ven <arjanv@redhat.com> 2.4-8.13
- remove more kernel private files

* Fri Apr 11 2003 Jakub Jelinek <jakub@redhat.com> 2.4-8.12
- update <linux/prctl.h> header
- remove i386 <asm/io.h>, replace it with a warning and <sys/io.h> include
  (Arjan van de Ven)

* Mon Feb 10 2003 Jakub Jelinek <jakub@redhat.com> 2.4-8.11
- update syscall numbers for all arches from 2.5.64 headers

* Fri Feb  7 2003 Bill Nottingham <notting@redhat.com> 2.4-8.10
- update more wireless headers

* Wed Feb  5 2003 Bill Nottingham <notting@redhat.com> 2.4-8.9
- update wireless headers

* Thu Jan 30 2003 Jakub Jelinek <jakub@redhat.com> 2.4-8.7
- make /usr/include/asm during build if it doesn't exist

* Thu Jan 30 2003 Jakub Jelinek <jakub@redhat.com> 2.4-8.6
- remove unpackaged file

* Thu Jan 30 2003 Bill Nottingham <notting@redhat.com>
- update netfilter headers

* Thu Jan 30 2003 Jakub Jelinek <jakub@redhat.com> 2.4-8.5
- don't include <linux/types.h> etc. in <asm-s390*/ptrace.h>

* Thu Jan 16 2003 Jakub Jelinek <jakub@redhat.com> 2.4-8.4
- updated s390 headers, added s390x headers
- HTB in <linux/pkt_sched.h>
- no -debuginfo subpackage

* Thu Dec 12 2002 Jakub Jelinek <jakub@redhat.com> 2.4-8.3
- update version.h from kernel-2.4.20-0.pp.6

* Tue Nov 26 2002 Jakub Jelinek <jakub@redhat.com> 2.4-8.2
- update unistd.h from kernel-2.4.19-0.pp.19

* Thu Oct 10 2002 Jakub Jelinek <jakub@redhat.com>
- generate stubs automatically
- remove /usr/include/scsi from file list

* Thu Oct 10 2002 Arjan van de Ven <arjanv@redhat.com
- added support for mixed 32/64 headers

* Thu Mar 21 2002 Arjan van de Ven <arjanv@redhat.com
- update ethtool and other network ioctls

* Sun Feb 10 2002 Arjan van de Ven <arjanv@redhat.com
- removed autoconf.h content

* Sun Feb 10 2002 Arjan van de Ven <arjanv@redhat.com
- fix missing include that broke quota.h

* Mon Jan 07 2002 Arjan van de Ven <arjanv@redhat.com
- fix rhconfig.h include file to not care about /boot/kernel.h

* Wed Jan 02 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- fix #warning in <asm-i386/rwlock.h> and <asm-i386/spinlock.h>

* Thu Dec 6 2001 Arjan van de Ven <arjanv@redhat.com>
- fix misplaced #endif

* Tue Dec 4 2001 Arjan van de Ven <arjanv@redhat.com>
- fix version.h to not include /boot/kernel.h

* Wed Oct 31 2001 Arjan van de Ven <arjanv@redhat.com>
- Initial packaging
