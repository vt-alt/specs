Name: squashfs-tools
Version: 4.4
Release: alt1

Summary: squashfs support
License: GPL
Group: System/Kernel and hardware
Url: https://git.kernel.org/cgit/fs/squashfs/squashfs-tools.git/
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: zlib-devel liblzma-devel liblzo2-devel libzstd-devel
Provides: squashfsprogs = %version-%release
Obsoletes: squashfsprogs

%description
Squashfs is a compressed read-only filesystem for Linux. Squashfs is
intended for general read-only filesystem use, for archival use
(i.e. in cases where a .tar.gz file may be used), and in constrained
block device/memory systems (e.g. embedded systems) where low overhead
is needed.

This package contains the utilities to (un)compress squashfs images.

%prep
%setup
%patch0 -p1

%build
export CFLAGS="%optflags"
%make_build XZ_SUPPORT=1 LZO_SUPPORT=1 ZSTD_SUPPORT=1 COMP_DEFAULT=xz

%install
install -pDm755 mksquashfs %buildroot/sbin/mksquashfs
install -pDm755 unsquashfs %buildroot/%_bindir/unsquashfs
ln -sf mksquashfs %buildroot/sbin/mkfs.squashfs
ln -sf ../../sbin/mksquashfs %buildroot%_bindir/mksquashfs

%files
/sbin/*
%_bindir/*

%changelog
* Tue Nov 05 2019 Anton Farygin <rider@altlinux.ru> 4.4-alt1
- 4.4 (fixes: CVE-2015-4645, CVE-2015-4646)

* Wed Aug 28 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3-alt4.e38956b
- Fixed build flags and debuginfo.

* Wed Jan 09 2019 Lenar Shakirov <snejok@altlinux.ru> 4.3-alt3.e38956b
- Add zstd support (commit e38956b)
- libzstd-devel added to BuildRequires

* Tue Jun 17 2014 Anton Farygin <rider@altlinux.ru> 4.3-alt2
- upstream fix for 32bit memory calculation on 64bit (or pae) kernel (closes: #30103)
- upstream fix for working without -mem options and/or /proc
- cleanup spec

* Fri May 30 2014 Anton Farygin <rider@altlinux.ru> 4.3-alt1
- new release

* Sun Apr 27 2014 Anton Farygin <rider@altlinux.ru> 4.2-alt1.aae0aff4
- updated from upstream git (stable branch)
- renamed to upstream name - squashfs-tools

* Fri Apr 01 2011 Anton Farygin <rider@altlinux.ru> 4.2-alt1
- new version
- patch0 removed (included to mainstream)

* Thu May 28 2009 Anton Farygin <rider@altlinux.ru> 4.0-alt1
- new version

* Tue Sep 02 2008 Anton Farygin <rider@altlinux.ru> 3.4-alt1
- new version

* Tue Aug 05 2008 Anton Farygin <rider@altlinux.ru> 3.3-alt4
- removed lzma support

* Tue Nov 06 2007 Anton Farygin <rider@altlinux.ru> 3.3-alt1
- new version

* Tue Jan 16 2007 Anton Farygin <rider@altlinux.ru> 3.2-alt2
- unsquashfs moved to %_bindir
- fixed description

* Sun Jan 14 2007 Anton Farygin <rider@altlinux.ru> 3.2-alt1
- new version
- removed kernel-feat-squashfs subpackage

* Tue Nov 07 2006 Anton Farygin <rider@altlinux.ru> 3.1-alt2.r2
- unsquashfs added to package

* Mon Oct 30 2006 Anton Farygin <rider@altlinux.ru> 3.1-alt1.r2
- updated to 3.1-r2
- removed kernel 2.4 patch
- use patch for 2.6.18 kernel

* Wed Sep 14 2005 Anton Farygin <rider@altlinux.ru> 2.2-alt1.r2
- updated to 2.2-r2
- use patch for 2.6.13 kernel

* Wed Aug 03 2005 Anton Farygin <rider@altlinux.ru> 2.2-alt1
- updated to new version

* Thu Apr 14 2005 Anton Farygin <rider@altlinux.ru> 2.1-alt2.r2
- mksquashfs: fixed target file permissions

* Wed Feb 09 2005 Anton Farygin <rider@altlinux.ru> 2.1-alt1.r2
- new version

* Thu May 20 2004 Alexey Morozov <morozov@altlinux.org> 1.3r3-alt2
- Initial build.

* Mon Mar 29 2004 Anton Farygin <rider@altlinux.ru> 1.3-alt1
- first build
