Name: klibc
Version: 2.0.8
Release: alt2
Summary: A minimal libc subset for use with initramfs
License: BSD/GPL
Group: System/Libraries
URL: http://www.zytor.com/mailman/listinfo/%name
# git://git.kernel.org/pub/scm/libs/klibc/klibc
Source0: %name-%version.tar
Source1: %name-find-provides
Source2: %name-find-requires

Patch: %name-%version-%release.patch

# due to %%base_arch
BuildPreReq: rpm-build-kernel

# Some architectures do not match arch naming in kernel.
%ifarch riscv64
%global base_arch riscv64
%endif
%ifarch ppc64le
%global base_arch ppc64
%endif

%define klibcdir  %_libdir/%name
%define libdocdir %_docdir/%name-%version-%release
%define bindocdir %_docdir/%name-utils-%version-%release

# Use special scripts to find dependencies on klibc-*.so (default RPM scripts
# do not pick up these dependencies).
%global __find_provides %_builddir/%name-%version/%name-find-provides %__find_provides
%global __find_requires %_builddir/%name-%version/%name-find-requires %__find_requires

%description
%name is intended to be a minimalistic libc subset for use with initramfs.
It is deliberately written for small size, minimal entanglement, and portability,
not speed.


%package devel
Summary: Libraries and tools needed to compile applications against klibc
Group: Development/C
Requires: %name = %version-%release
AutoReq: nocpp
Provides: klcc = %version-%release
Provides: %name-devel-static = %version-%release

%description devel
This package contains the link libraries, header files, and gcc wrapper scripts
needed to compile applications against klibc.


%package utils
Summary: Small utilities built with klibc
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description utils
This package contains a collection of programs that are linked against klibc.
These duplicate some of the functionality of a regular Linux toolset, but are
typically much smaller than their full-function counterparts. They are intended
for inclusion in initramfs images and embedded systems.

%prep
%setup
%patch -p1
# Install fixed scsi headers
install -d -m 0755 usr/include/scsi
for f in %_includedir/scsi/*; do
	sed '/^#[[:blank:]]*include/s|features.h|sys/stat.h|' "$f" > usr/include/scsi/$(basename "$f")
done

install -p -m 0755 %{S:1} ./%name-find-provides
install -p -m 0755 %{S:2} ./%name-find-requires

cat > defconfig <<__EOF__
CONFIG_KLIBC=y
# CONFIG_KLIBC_ERRLIST is not set
# CONFIG_KLIBC_ZLIB is not set
# CONFIG_KLIB_ZIP is not set
# CONFIG_KINIT_LOAD_INITRD is not set
# i386 option
CONFIG_REGPARM=y
# ARM options
CONFIG_AEABI=y
# CONFIG_KLIBC_THUMB is not set
__EOF__

%build
%define optflags_debug %nil
%make_build \
	KLIBCARCH=%base_arch prefix=%prefix bindir=%_bindir \
	KLIBCKERNELSRC=$(readlink -ev %_includedir/linux/../..) \
	SHLIBDIR=/%_lib \
	INSTALLDIR=%klibcdir mandir=%_mandir INSTALLROOT=%buildroot \
	V=1


%install
%make_install \
	KLIBCARCH=%base_arch prefix=%prefix bindir=%_bindir \
	KLIBCKERNELSRC=$(readlink -ev %_includedir/linux/../..) \
	SHLIBDIR=/%_lib \
	INSTALLDIR=%klibcdir mandir=%_mandir INSTALLROOT=%buildroot \
	install
rm -f %buildroot%klibcdir/include/Kbuild

install -p -m 0755 %name-find-requires %buildroot%klibcdir/

# Install the docs
install -d -m 0755 %buildroot{%bindocdir,%libdocdir}
install -p -m 0644 README usr/%name/{,arch/}README.%{name}* %buildroot%libdocdir/
for f in usr/{gzip/{COPYING,README},kinit{,/ipconfig}/README*}; do
	install -p -m 0644 $f %buildroot%bindocdir/$(basename $f).$(basename $(dirname $f))
done

Symlinks()
{
	local src=$1 dir=$2
	shift 2
	while [ -n "$1" ]; do
		ln -sf $src %buildroot$dir/$1
		shift
	done
}

Symlinks gzip %klibcdir/bin gunzip zcat
for d in %klibcdir/bin; do
	Symlinks halt $d poweroff reboot
done

# This file must have normal symbols - they are used for linking
# (klibc does not use the dynamic symbol table).
strip -g %buildroot%klibcdir/lib/libc.so
%ifdef brp_strip_none
%brp_strip_none %klibcdir/lib/libc.so
%else
%add_strip_skiplist %klibcdir/lib/libc.so
%endif


%files
/%_lib/%name-*.so


%files devel
%klibcdir
%exclude %klibcdir/bin
%klibcdir/%name-find-requires
%_bindir/klcc
%_man1dir/*
%doc %libdocdir


%files utils
%dir %klibcdir
%klibcdir/bin
%doc %bindocdir

%changelog
* Wed Nov 11 2020 Nikita Ermakov <arei@altlinux.org> 2.0.8-alt2
- Fix build in p9.

* Fri Aug 21 2020 Nikita Ermakov <arei@altlinux.org> 2.0.8-alt1
- Updated to 2.0.8.

* Wed Oct 23 2019 Nikita Ermakov <arei@altlinux.org> 2.0.7-alt1
- Updated to 2.0.7.

* Wed May 08 2019 Nikita Ermakov <arei@altlinux.org> 2.0.6-alt1
- Updated to 2.0.6.
- Added ppc64le support (by Gleb F-Malinovskiy).

* Tue Dec 4 2018 Nikita Ermakov <arei@altlinux.org> 2.0.4-alt2
- Added RISC-V (rv64) support.

* Tue Nov 27 2018 Nikita Ermakov <arei@altlinux.org> 2.0.4-alt1
- Updated to 2.0.4.
- Removed klibc-utils-initramfs.

* Fri Apr 25 2014 Led <led@altlinux.ru> 2.0.3-alt4
- ln: fixed

* Thu Apr 24 2014 Led <led@altlinux.ru> 2.0.3-alt3
- upstream optimizations

* Fri Apr 11 2014 Led <led@altlinux.ru> 2.0.3-alt2
- upstream fixes

* Thu Dec 19 2013 Led <led@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Fri Nov 22 2013 Led <led@altlinux.ru> 2.0.2-alt5
- removed unneeded 'false', 'true', 'kill' utils from utils-initramfs subpackage
  (already sh builtin)

* Mon Nov 18 2013 Led <led@altlinux.ru> 2.0.2-alt4
- upstream fixes
- removed unneeded 'readlink' from utils-initramfs subpackage

* Fri Jan 04 2013 Led <led@altlinux.ru> 2.0.2-alt3
- klibc: added popen() and pclose()
- cleaned up spec

* Sat Dec 15 2012 Led <led@altlinux.ru> 2.0.2-alt2
- kinit: make initrd support optional
- cleaned up spec
- updated defconfig
- disabled:
  + CONFIG_KLIBC_ERRLIST
  + CONFIG_KLIBC_ZLIB
  + CONFIG_KINIT_LOAD_INITRD

* Fri Nov 23 2012 Led <led@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Wed Nov 21 2012 Led <led@altlinux.ru> 1.5.25-alt1
- 1.5.25 with bakported fixes and features from 2.0.2
- cleaned up spec

* Sun Nov 18 2012 Led <led@altlinux.ru> 1.5.18-alt3
- nfsmount: use UDP by default
- ipconfig: add support infiniband
- ipconfig: exits by timeout with code 110
- fixed a bug where all files are rebuild each time we invoke make
- cleaned up spec

* Mon Oct 15 2012 Led <led@altlinux.ru> 1.5.18-alt2
- fixed build with make 3.82
- fixed build with kernel >= 3.5

* Mon Mar 12 2012 Michael Shigorin <mike@altlinux.org> 1.5.18-alt1.1
- tested and rebuilt for Sisyphus
  + NB: misses boyarsh@'s -alt2 changes

* Thu May 20 2010 Dmitry V. Levin <ldv@altlinux.org> 1.5.18-alt1
- Updated to 1.5.18.
- Fixed include/arch/i386/klibc/archsignal.h (closes: #23514).

* Fri Apr 02 2010 Dmitry V. Levin <ldv@altlinux.org> 1.5.17-alt2
- Build this package without optimizations based on strict aliasing rules.
- Fixed build with fresh glibc-kernheaders.
- Enhanced sys/socket.h to make it usable for building udev.

* Sat Mar 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.5.17-alt1
- 1.5.17

* Sun Mar 14 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.5.16-alt1
- 1.5.16

* Tue Nov 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.5.15-alt4
- build with kernel-headers-std-def

* Tue Jul 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.5.15-alt3
- implementing signalfd()
- fixed faccessat(), linkat(), fchmodat(), unlinkat()

* Fri Jul 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.5.15-alt2
- rebuild

* Sun Jan 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.5.15-alt1
- 1.5.15

* Thu Nov 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.5.14-alt2
- rebuild

* Thu Sep 11 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.5.14-alt1.2
- Enable EABI support on ARM

* Tue Sep 09 2008 Kirill A. Shutemov <kas@altlinux.ru> 1.5.14-alt1.1
- NMU:
  + build with glibc-kernheaders
  + replace kernel-build-tools with rpm-build-kernel to reduce build
    dependents

* Sat Aug 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.5.14-alt1
- 1.5.14

* Tue Jul 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.5.12-alt1
- 1.5.12

* Mon Jun 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.5.11-alt1
- 1.5.11

* Wed Jun 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.5.10-alt1
- 1.5.10

* Thu Mar 29 2007 Sergey Vlasov <vsu@altlinux.ru> 1.5-alt1
- Version 1.5.

* Mon Feb 19 2007 Sergey Vlasov <vsu@altlinux.ru> 1.4.34-alt1
- Version 1.4.34.
- Fixed broken shared library build on x86_64 with binutils versions having
  max-page-size=0x200000 (caused immediate segfault on kernels with the
  exec-shield patch applied).

* Thu Feb 08 2007 Sergey Vlasov <vsu@altlinux.ru> 1.4.32-alt1
- First build for ALT Linux.
- Version 1.4.32.
- Spec file cleanup according to ALT conventions.
- Use kernel-headers-std >= 2.6.18 headers for build.
- Move klibc-*.so from /lib to /%%_lib (which is /lib64 on x86_64).
- Move other klibc files to %%_libdir instead of %%_prefix/lib.
- Move libc.so and interp.o to the devel subpackage (RPM dependencies should
  prevent mismatches between runtime and devel packages).
- Do not strip libc.so (klibc uses normal symbols for linking).
- Add klibc-find-provides and klibc-find-requires scripts to generate proper
  dependencies on /%%_lib/klibc-*.so (klibc-find-provides is used privately,
  klibc-find-requires is available in the devel subpackage for use by other
  packages which link with klibc).
- Add klibc-utils-initramfs subpackage which contains the subset of
  utilities used by mkinitrd-generated initramfs images; these files are
  installed under /lib/mkinitrd to make them available even without /usr.
- Add md_run utility to handle old-style RAID startup separate from kinit.
- umount: Add -l option for lazy unmount.

* Tue Mar 1 2005 H. Peter Anvin <hpa@zytor.com>
- New "make install" scheme, klcc

* Tue Jul 6 2004 H. Peter Anvin <hpa@zytor.com>
- Update to use kernel-source RPM for the kernel symlink.

* Sat Nov 29 2003 Bryan O'Sullivan <bos@serpentine.com> -
- Initial build.
