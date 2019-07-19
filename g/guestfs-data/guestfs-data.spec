Name: guestfs-data
Version: 0.6
Release: alt1

Summary: Virtual machine needed for libguestfs
License: GPLv2+
Group: File tools

Provides: lib%name = %version-%release

BuildPreReq: rpm-build-guestfs
BuildRequires: /proc

%description
libguestfs needs for it's run a virtual machine image.
This package provides such an image, an initrd and a kernel.

%install
mkdir -p %buildroot%_libdir/guestfs
cp -a %_libdir/guestfs/* %buildroot%_libdir/guestfs/
chmod 644 %buildroot%_libdir/guestfs/*

# On some architectures (at least ppc64le) kernel image is ELF and
# eu-findtextrel will fail if it is not a DSO or PIE.
%add_verify_elf_skiplist %_libdir/guestfs/vmlinuz*
# ... debuginfo.req will fail if it has no .interp .
%brp_strip_none %_libdir/guestfs/vmlinuz*

%files
%dir %_libdir/guestfs/
%_libdir/guestfs/*

%changelog
* Fri Jul 19 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.6-alt1
- Fixed build on ppc64le.

* Wed Apr 03 2019 Alexey Shabalin <shaba@altlinux.org> 0.5-alt1
- rebuild with libguestfs-1.40.2-alt1

* Fri Dec 21 2018 Alexey Shabalin <shaba@altlinux.org> 0.4-alt2
- rebuild with make-initrd-2.2.6

* Mon Oct 15 2018 Alexey Shabalin <shaba@altlinux.org> 0.4-alt1
- rebuild with libguestfs-1.36.15-alt1
- build with new make-initrd v2

* Thu May 26 2016 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt6
- rebuld with libguestfs-1.32.4

* Mon Jan 11 2016 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt5
- rebuld with libguestfs-1.32.0

* Tue Oct 20 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt4
- rebuld with libguestfs-1.31.17

* Tue Sep 22 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt3
- rebuld with libguestfs-1.31.6

* Thu Jun 25 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt2
- rebuild

* Fri Feb 13 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt1
- update

* Wed Feb 11 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- initial build
