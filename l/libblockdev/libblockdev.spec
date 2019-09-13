%def_disable snapshot

%define _name blockdev
%define ver_major 2.23
%define rev 1

%ifnarch %ix86 x86_64
%def_without vdo
%else
%def_without vdo
%endif

%def_without python2
%def_without dmraid
%def_with tools
%def_enable check

Name: lib%_name
Version: %ver_major
Release: alt1

Summary: A library for low-level manipulation with block devices
Group: System/Libraries
License: LGPLv2+
Url: https://github.com/storaged-project/%name

%if_disabled snapshot
#VCS: https://github.com/rhinstaller/libblockdev.git
Source: %url/releases/download/%ver_major-%rev/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

BuildRequires(pre): rpm-build-python3
%{?_with_python2:BuildRequires(pre): rpm-build-python}
BuildRequires: python3-devel
%{?_with_python2:BuildRequires: python-devel}
BuildRequires: gtk-doc
BuildRequires: libgio-devel gobject-introspection-devel
BuildRequires: libcryptsetup-devel libdevmapper-devel
BuildRequires: systemd-devel libudev-devel libmount-devel
BuildRequires: libvolume_key-devel >= 0.3.9
BuildRequires: libnss-devel
BuildRequires: libkmod-devel
BuildRequires: libparted-devel
BuildRequires: libblkid-devel
BuildRequires: libbytesize-devel
BuildRequires: libuuid-devel
BuildRequires: libndctl-devel
%{?_with_dmraid:BuildRequires: dmraid-devel}
%{?_with_vdo:BuildRequires: libyaml-devel}
%{?_enable_check:BuildRequires: python3-module-pylint python3-module-pygobject3}

%ifarch s390 s390x
BuildRequires: s390utils-devel
%endif

%description
The libblockdev is a C library with GObject introspection support that can be
used for doing low-level operations with block devices like setting up LVM,
BTRFS, LUKS or MD RAID. The library uses plugins (LVM, BTRFS,...) and serves as
a thin wrapper around its plugins' functionality. All the plugins, however, can
be used as standalone libraries. One of the core principles of libblockdev is
that it is stateless from the storage configuration's perspective (e.g. it has
no information about VGs when creating an LV).

%package devel
Summary: Development files for libblockdev
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains header files and pkg-config files needed for development
with the libblockdev library.

%package -n python-module-blockdev
Summary: Python2 gobject-introspection bindings for libblockdev
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-blockdev
This package contains enhancements to the gobject-introspection bindings
for libblockdev in Python2.

%package -n python3-module-blockdev
Summary: Python3 gobject-introspection bindings for libblockdev
Group: Development/Python3
Requires: %name = %version-%release

%description -n python3-module-blockdev
This package contains enhancements to the gobject-introspection bindings for
libblockdev in Python3.

%package utils
Summary: A library with utility functions for the libblockdev library
Group: System/Libraries

%description utils
The libblockdev-utils is a library providing utility functions used by the
libblockdev library and its plugins.

%package utils-devel
Summary: Development files for libblockdev-utils
Group: Development/C
Requires: %name-utils = %version-%release

%description utils-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-utils library.

%package btrfs
Summary: The BTRFS plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %version-%release
Requires: btrfs-progs

%description btrfs
The libblockdev library plugin (and in the same time a standalone library)
providing the BTRFS-related functionality.

%package btrfs-devel
Summary: Development files for the libblockdev-btrfs plugin/library
Group: Development/C
Requires: %name-btrfs = %version-%release
Requires: %name-utils-devel = %version-%release

%description btrfs-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-btrfs plugin/library.

%package crypto
Summary: The crypto plugin for the libblockdev library
Group: System/Libraries

%description crypto
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to encrypted devices (LUKS).

%package crypto-devel
Group: Development/C
Summary: Development files for the libblockdev-crypto plugin/library
Requires: %name-crypto = %version-%release

%description crypto-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-crypto plugin/library.

%package dm
Summary: The Device Mapper plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %version-%release
Requires: dmsetup
%{?_with_dmraid:Requires: dmraid}

%description dm
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to Device Mapper.

%package dm-devel
Summary: Development files for the libblockdev-dm plugin/library
Group: Development/C
Requires: %name-dm = %version-%release
Requires: %name-utils-devel = %version-%release

%description dm-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-dm plugin/library.

%package fs
Summary: The FS plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %version-%release
Requires: multipath-tools

%description fs
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to operations with file systems.

%package fs-devel
Summary: Development files for the libblockdev-fs plugin/library
Group: Development/C
Requires: %name-fs = %version-%release
Requires: %name-utils-devel = %version-%release


%description fs-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-fs plugin/library.

%package kbd
Summary: The KBD plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %version-%release
Requires: bcache-status bcache-tools

%description kbd
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to kernel block devices (namely zRAM and
Bcache).

%package kbd-devel
Summary: Development files for the libblockdev-kbd plugin/library
Group: Development/C
Requires: %name-kbd = %version-%release
Requires: %name-utils-devel = %version-%release

%description kbd-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-kbd plugin/library.

%package loop
Summary: The loop plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %version-%release
Requires: agetty cfdisk coreutils eject fdisk getopt hwclock login look losetup
Requires: lsblk mount msulogin schedutils setarch sfdisk su sysvinit-utils util-linux

%description loop
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to loop devices.

%package loop-devel
Summary: Development files for the libblockdev-loop plugin/library
Group: Development/C
Requires: %name-loop = %version-%release
Requires: %name-utils-devel = %version-%release

%description loop-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-loop plugin/library.

%package lvm
Summary: The LVM plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %version-%release
Requires: lvm2

%description lvm
The libblockdev library plugin (and in the same time a standalone library)
providing the LVM-related functionality.

%package lvm-devel
Summary: Development files for the libblockdev-lvm plugin/library
Group: Development/C
Requires: %name-lvm = %version-%release
Requires: %name-utils-devel = %version-%release

%description lvm-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-lvm plugin/library.

%package lvm-dbus
Summary: The LVM plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %version-%release
Requires: lvm2

%description lvm-dbus
The libblockdev library plugin (and in the same time a standalone library)
providing the LVM-related functionality utilizing the LVM DBus API.

%package lvm-dbus-devel
Summary: Development files for the libblockdev-lvm-dbus plugin/library
Group: Development/C
Requires: %name-lvm-dbus = %version-%release
Requires: %name-utils-devel = %version-%release

%description lvm-dbus-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-lvm-dbus plugin/library.

%package mdraid
Summary: The MD RAID plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %version-%release
Requires: mdadm

%description mdraid
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to MD RAID.

%package mdraid-devel
Summary: Development files for the libblockdev-mdraid plugin/library
Group: Development/C
Requires: %name-mdraid = %version-%release
Requires: %name-utils-devel = %version-%release

%description mdraid-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-mdraid plugin/library.

%package mpath
Summary: The multipath plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %version-%release
Requires: multipath-tools

%description mpath
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to multipath devices.

%package mpath-devel
Summary: Development files for the libblockdev-mpath plugin/library
Group: Development/C
Requires: %name-mpath = %version-%release
Requires: %name-utils-devel = %version-%release

%description mpath-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-mpath plugin/library.

%package part
Summary: The partitioning plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %version-%release
Requires: multipath-tools
Requires: cgdisk fixparts gdisk

%description part
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to partitioning.

%package part-devel
Summary: Development files for the libblockdev-part plugin/library
Group: Development/C
Requires: %name-part = %version-%release
Requires: %name-utils-devel = %version-%release

%description part-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-part plugin/library.

%package swap
Summary: The swap plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %version-%release
Requires: agetty cfdisk coreutils eject fdisk getopt hwclock login look losetup lsblk
Requires: mount msulogin schedutils setarch sfdisk su sysvinit-utils util-linux

%description swap
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to swap devices.

%package swap-devel
Summary: Development files for the libblockdev-swap plugin/library
Group: Development/C
Requires: %name-swap = %version-%release
Requires: %name-utils-devel = %version-%release

%description swap-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-swap plugin/library.

%package nvdimm
Summary: The ndctl plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils = %version-%release
Requires: ndctl daxctl

%description nvdimm
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to NVDIMM devices.

%package nvdimm-devel
Summary: Development files for the libblockdev-nvdimm plugin/library
Group: Development/C
Requires: %name-nvdimm = %version-%release
Requires: %name-utils-devel = %version-%release

%description nvdimm-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-nvdimm plugin/library.

%package s390
Summary: The s390 plugin for the libblockdev library
Group: System/Libraries
Requires: s390utils

%description s390
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to s390 devices.

%package s390-devel
Summary: Development files for the libblockdev-s390 plugin/library
Group: Development/C
Requires: %name-s390 = %version-%release
Requires: %name-utils-devel = %version-%release

%description s390-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-s390 plugin/library.

%package vdo
Summary: The vdo plugin for the libblockdev library
Group: System/Libraries
Requires: %name-utils >= %version-%release
# https://github.com/dm-vdo/vdo
# https://github.com/dm-vdo/kvdo
Requires: vdo kmod-kvdo

%description vdo
The libblockdev library plugin providing the functionality related to VDO devices.

%package vdo-devel
Summary: Development files for the libblockdev-vdo plugin/library
Group: Development/C
Requires: %name-vdo = %version-%release
Requires: %name-utils-devel = %version-%release

%description vdo-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-vdo plugin/library.

%package plugins
Summary: Meta-package that pulls all the libblockdev plugins as dependencies
Group: System/Libraries
BuildArch: noarch
Requires: %name-btrfs = %version-%release
Requires: %name-crypto = %version-%release
Requires: %name-dm = %version-%release
Requires: %name-fs = %version-%release
Requires: %name-kbd = %version-%release
Requires: %name-loop = %version-%release
Requires: %name-lvm = %version-%release
Requires: %name-mdraid = %version-%release
Requires: %name-mpath = %version-%release
Requires: %name-part = %version-%release
Requires: %name-swap = %version-%release
Requires: %name-nvdimm = %version-%release
%{?_with_vdo:Requires: %name-vdo = %version-%release}
%ifarch s390 s390x
Requires: %name-s390 = %version-%release
%endif

%description plugins
A meta-package that pulls all the libblockdev plugins as dependencies.

%package tools
Summary: Tools from libblockdev package
Group: System/Kernel and hardware
Requires: %name-lvm = %version-%release

%description tools
This package contains cli libblockdev tools.
vm-cache-stats -- for displaying stats for LVM cache devices.

%prep
%setup -n %name-%version
sed -i 's/mkfs\.vfat/mkfs.fat/g
	s/fsck\.vfat/fsck.fat/g' src/plugins/fs.c src/lib/plugin_apis/fs.api tests/fs_test.py

sed -i 's/\(pylint\)-3/\1.py3/' Makefile.*

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%autoreconf
%configure \
	%{subst_with vdo} \
	%{subst_with dmraid} \
	%{subst_with tools} \
	%{subst_with python2}
%make_build

%install
%makeinstall_std
find %buildroot -type f -name "*.la" -print0| xargs -r0 rm -f --

%check
%make check

%files
%_libdir/libblockdev.so.*
%_typelibdir/BlockDev*.typelib
%config %_sysconfdir/libblockdev/conf.d/00-default.cfg
%doc *.rst LICENSE

%files devel
%_libdir/libblockdev.so
%dir %_includedir/blockdev
%_includedir/blockdev/blockdev.h
%_includedir/blockdev/dev_utils.h
%_includedir/blockdev/extra_arg.h
%_includedir/blockdev/plugins.h
%_pkgconfigdir/blockdev.pc
%_datadir/gtk-doc/html/libblockdev
%_girdir/BlockDev*.gir
%doc features.rst specs.rst

%if_with python2
%files -n python-module-blockdev
%python_sitelibdir/gi/overrides/*
%endif

%files -n python3-module-blockdev
%python3_sitelibdir/gi/overrides/BlockDev*
%python3_sitelibdir/gi/overrides/__pycache__/BlockDev*

%files utils
%_libdir/libbd_utils.so.*

%files utils-devel
%_libdir/libbd_utils.so
%dir %_includedir/blockdev
%_includedir/blockdev/utils.h
%_includedir/blockdev/sizes.h
%_includedir/blockdev/exec.h
%_includedir/blockdev/module.h
%_includedir/blockdev/dbus.h
%_pkgconfigdir/blockdev-utils.pc

%files btrfs
%_libdir/libbd_btrfs.so.*

%files btrfs-devel
%_libdir/libbd_btrfs.so
%dir %_includedir/blockdev
%_includedir/blockdev/btrfs.h

%files crypto
%_libdir/libbd_crypto.so.*

%files crypto-devel
%_libdir/libbd_crypto.so
%dir %_includedir/blockdev
%_includedir/blockdev/crypto.h

%files dm
%_libdir/libbd_dm.so.*

%files dm-devel
%_libdir/libbd_dm.so
%dir %_includedir/blockdev
%_includedir/blockdev/dm.h

%files fs
%_libdir/libbd_fs.so.*

%files fs-devel
%_libdir/libbd_fs.so
%dir %_includedir/blockdev
%_includedir/blockdev/fs.h
%_includedir/blockdev/fs/

%files kbd
%_libdir/libbd_kbd.so.*

%files kbd-devel
%_libdir/libbd_kbd.so
%dir %_includedir/blockdev
%_includedir/blockdev/kbd.h

%files loop
%_libdir/libbd_loop.so.*

%files loop-devel
%_libdir/libbd_loop.so
%dir %_includedir/blockdev
%_includedir/blockdev/loop.h

%files lvm
%_libdir/libbd_lvm.so.*

%files lvm-devel
%_libdir/libbd_lvm.so
%dir %_includedir/blockdev
%_includedir/blockdev/lvm.h

%files lvm-dbus
%_libdir/libbd_lvm-dbus.so.*
%config %_sysconfdir/libblockdev/conf.d/10-lvm-dbus.cfg

%files lvm-dbus-devel
%_libdir/libbd_lvm-dbus.so
%dir %_includedir/blockdev
#%_includedir/blockdev/lvm.h

%files mdraid
%_libdir/libbd_mdraid.so.*

%files mdraid-devel
%_libdir/libbd_mdraid.so
%dir %_includedir/blockdev
%_includedir/blockdev/mdraid.h

%files mpath
%_libdir/libbd_mpath.so.*

%files mpath-devel
%_libdir/libbd_mpath.so
%dir %_includedir/blockdev
%_includedir/blockdev/mpath.h

%files part
%_libdir/libbd_part.so.*
%_libdir/libbd_part_err.so.*

%files part-devel
%_libdir/libbd_part.so
%_libdir/libbd_part_err.so
%dir %_includedir/blockdev
%_includedir/blockdev/part.h

%files swap
%_libdir/libbd_swap.so.*

%files swap-devel
%_libdir/libbd_swap.so
%dir %_includedir/blockdev
%_includedir/blockdev/swap.h

%files nvdimm
%_libdir/libbd_nvdimm.so.*

%files nvdimm-devel
%_libdir/libbd_nvdimm.so
%dir %_includedir/blockdev
%_includedir/blockdev/nvdimm.h


%ifarch s390 s390x
%files s390
%_libdir/libbd_s390.so.*

%files s390-devel
%_libdir/libbd_s390.so
%dir %_includedir/blockdev
%_includedir/blockdev/s390.h
%endif

%if_with vdo
%files vdo
%_libdir/libbd_vdo.so.*

%files vdo-devel
%_libdir/libbd_vdo.so
%dir %_includedir/blockdev
%_includedir/blockdev/vdo.h
%endif

%files plugins

%if_with tools
%files tools
%_bindir/lvm-cache-stats
%endif

%changelog
* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 2.23-alt1
- 2.23

* Thu Jun 13 2019 Yuri N. Sedunov <aris@altlinux.org> 2.22-alt1
- 2.22

* Fri Feb 22 2019 Yuri N. Sedunov <aris@altlinux.org> 2.21-alt1
- 2.21
- new tools subpackage

* Sat Sep 29 2018 Yuri N. Sedunov <aris@altlinux.org> 2.20-alt1
- 2.20

* Sat Aug 11 2018 Yuri N. Sedunov <aris@altlinux.org> 2.19-alt1
- 2.19

* Thu Jun 21 2018 Yuri N. Sedunov <aris@altlinux.org> 2.18-alt1
- 2.18 with
- prepared optional vdo* subpackages (vdo and kvdo required)
- added conditionals for dmraid support

* Fri May 11 2018 Yuri N. Sedunov <aris@altlinux.org> 2.17-alt1
- 2.17 with new nvdimm* subpackages

* Fri Feb 09 2018 Yuri N. Sedunov <aris@altlinux.org> 2.16-alt1
- 2.16

* Mon Jan 29 2018 Yuri N. Sedunov <aris@altlinux.org> 2.15-alt2
- rebuilt against libcryptsetup.so.12

* Wed Dec 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.15-alt1
- 2.15

* Thu Nov 02 2017 Yuri N. Sedunov <aris@altlinux.org> 2.14-alt1
- 2.14

* Fri Oct 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.13-alt1
- 2.13

* Thu Sep 07 2017 Yuri N. Sedunov <aris@altlinux.org> 2.12.1-alt1
- 2.12.1

* Mon Aug 14 2017 Yuri N. Sedunov <aris@altlinux.org> 2.11.1-alt1
- 2.11-1

* Sat Jul 08 2017 Yuri N. Sedunov <aris@altlinux.org> 2.10.1-alt1
- 2.10-1

* Tue Jun 13 2017 Yuri N. Sedunov <aris@altlinux.org> 2.9.1-alt1
- first build for Sisyphus



