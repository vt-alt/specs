%def_disable snapshot

%define _name udisks
%define api_ver 2.0
%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

%def_enable introspection
%def_enable acl
# since 2.1.5 it is possible to configure udisks to mount devices
# in /media instead of /run/media but we use own control-based mechanism,
# so this option should never be enabled
%def_disable fhs_media
%def_enable lvm2
%def_enable lvmcache
%def_disable iscsi
%def_enable btrfs
%def_enable zram
%def_disable lsm
%def_enable bcache
%ifarch %ix86
%def_disable vdo
%else
%def_disable vdo
%endif

Name: %{_name}2
Version: 2.8.4
Release: alt1

Summary: Disk Management Service (Second Edition)
License: GPLv2+
Group: System/Servers
Url: https://github.com/storaged-project/udisks

%if_disabled snapshot
Source: https://github.com/storaged-project/%_name/releases/download/%_name-%version/%_name-%version.tar.bz2
%else
Source: %_name-%version.tar
%endif
Source1: %name.control

Obsoletes: %_name

%define glib_ver 2.50
%define gi_ver 1.30.0
%define polkit_ver 0.101
%define udev_ver 165
%define libatasmart_ver 0.17
%define dbus_ver 1.4.0
%define blockdev_ver 2.19
%define libmount_ver 2.30

Requires(pre): control
Requires: lib%name = %version-%release
Requires: /lib/udev/rules.d
Requires: /usr/sbin/cryptsetup
Requires: dbus >= %dbus_ver dbus-tools-gui
Requires: mdadm ntfsprogs parted gdisk dosfstools xfsprogs
%{?_enable_acl:Requires: acl}

Requires: libblockdev-fs
Requires: libblockdev-crypto
Requires: libblockdev-loop
Requires: libblockdev-mdraid
Requires: libblockdev-part
Requires: libblockdev-swap

BuildRequires: gtk-doc
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libpolkit-devel >= %polkit_ver
BuildRequires: libatasmart-devel >= %libatasmart_ver
BuildRequires: libudev-devel libgudev-devel >= %udev_ver
BuildRequires: pkgconfig(systemd) libmount-devel >= %libmount_ver
BuildRequires: libblockdev-devel >= %blockdev_ver libblockdev-loop-devel
BuildRequires: libblockdev-mdraid-devel libblockdev-fs-devel libblockdev-crypto-devel
BuildRequires: libblockdev-kbd-devel libblockdev-part-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= %gi_ver}
%{?_enable_acl:BuildRequires: libacl-devel}
%{?_enable_lvm2:BuildRequires: libdevmapper-devel liblvm2-devel libblockdev-lvm-devel}
%{?_enable_iscsi:BuildRequires: iscsi-initiator-utils-devel}
%{?_enable_btrfs:BuildRequires: libblockdev-btrfs-devel}
%{?_enable_zram:BuildRequires: libblockdev-kbd-devel libblockdev-swap-devel}
%{?_enable_lsm:BuildRequires: libstoragemgmt-devel libconfig-devel}
%{?_enable_vdo:BuildRequires: libblockdev-vdo-devel}

%description
The udisks project provides a daemon, tools and libraries to access
and manipulate disks and storage devices.

%package -n lib%name
Summary: Dynamic library to access the udisks daemon (Second Edition)
Group: System/Libraries

%description -n lib%name
The udisks project provides a daemon, tools and libraries to access
and manipulate disks and storage devices.

This package contains the dynamic %name library, which provides
access to the udisks daemon.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the development files for the library lib%name.

%package -n lib%name-gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the %name library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %name library

%package -n lib%name-devel-doc
Summary: Development documentation for lib%name
Group: Development/Documentation
Conflicts: %name < %version
BuildArch: noarch

%description -n lib%name-devel-doc
This package contains development documentation for lib%name.

%package module-lvm2
Summary: UDisks module for LVM2
Group: System/Servers
Requires: %name = %version-%release
Requires: libblockdev-lvm

%description module-lvm2
This package contains UDisks module for LVM2 configuration.

%package module-zram
Summary: UDisks module for Zram
Group: System/Servers
Requires: %name = %version-%release
Requires: libblockdev-kbd

%description module-zram
This package contains UDisks module for Zram configuration.

%package module-bcache
Summary: UDisks module for Bcache
Group: System/Servers
Requires: %name = %version-%release
Requires: libblockdev-kbd

%description module-bcache
This package contains UDisks module for Bcache configuration.

%package module-btrfs
Summary: UDisks module for BTRFS
Group: System/Servers
Requires: %name = %version-%release
Requires: libblockdev-btrfs

%description module-btrfs
This package contains UDisks module for BTRFS configuration.

%package module-lsm
Summary: UDisks module for LSM
Group: System/Servers
Requires: %name = %version-%release
Requires: libstoragemgmt

%description module-lsm
This package contains UDisks module for LibStorageMgmt configuration.

%package module-iscsi
Summary: UDisks module for iSCSI
Group: System/Servers
Requires: %name = %version-%release
Requires: iscsi-initiator-utils

%description module-iscsi
This package contains UDisks module for iSCSI configuration.

%package module-vdo
Summary: UDisks module for VDO
Group: System/Servers
Requires: %name = %version-%release
Requires: libblockdev-vdo

%description module-vdo
This package contains UDisks module for VDO management.


%prep
%setup -n %_name-%version
subst 's/mkfs\.vfat/mkfs.fat/
       s/dosfslabel/fatlabel/' src/udiskslinuxfsinfo.c

%build
%autoreconf
%configure --disable-static \
	--enable-gtk-doc \
	%{subst_enable acl} \
	%{?_enable_fhs_media:--enable-fhs-media} \
	%{subst_enable lvm2} \
	%{subst_enable lvmcache} \
	%{subst_enable iscsi} \
	%{subst_enable btrfs} \
	%{subst_enable zram} \
	%{subst_enable lsm} \
	%{subst_enable bcache} \
	%{subst_enable vdo}

%make_build

%install
%makeinstall_std

#mkdir -p %buildroot%_localstatedir/run/%name
touch %buildroot%_localstatedir/lib/%name/mtab

# use /media for mounting by default
mkdir -p %buildroot%_sysconfdir/udev/rules.d
cat > %buildroot%_sysconfdir/udev/rules.d/99-alt-%name-media-mount-point.rules <<_EOF_
ENV{ID_FS_USAGE}=="filesystem|other|crypto", ENV{UDISKS_FILESYSTEM_SHARED}="0"
_EOF_

# control support
install -pD -m755 %SOURCE1 %buildroot%_controldir/%name

%find_lang %name

%check
%make check

%pre
if [ -f %_controldir/%name ]; then
%pre_control %name
fi

%post
%post_control -s default %name

%files -f %name.lang
%_sbindir/umount.%name
%_bindir/udisksctl
/lib/udev/rules.d/80-%name.rules
%config(noreplace) %_sysconfdir/%name/%name.conf
%_sysconfdir/udev/rules.d/99-alt-%name-media-mount-point.rules
%dir %_libexecdir/%name
%_libexecdir/%name/udisksd
%dir %_libdir/%name
%dir %_libdir/%name/modules
%_datadir/polkit-1/actions/org.freedesktop.UDisks2.policy
%_datadir/dbus-1/system.d/org.freedesktop.UDisks2.conf
%_datadir/dbus-1/system-services/org.freedesktop.UDisks2.service
%_datadir/bash-completion/completions/udisksctl
%_man1dir/*
%_man5dir/%name.conf.5.*
%_man8dir/*
%attr(0700,root,root) %dir %_localstatedir/lib/%name
%ghost %_localstatedir/lib/%name/mtab
#%attr(0700,root,root) %dir %_localstatedir/run/%name
%config %systemd_unitdir/udisks2.service
%config %systemd_unitdir/clean-mount-point@.service
%_tmpfilesdir/%name.conf
%config %_controldir/%name
%doc README.md AUTHORS NEWS HACKING

%files -n libudisks2
%_libdir/libudisks2.so.*

%files -n libudisks2-devel
%_libdir/lib%name.so
%_includedir/%name/
%_libdir/pkgconfig/%name.pc

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/udisks2/*

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/UDisks-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/UDisks-%api_ver.gir
%endif

%if_enabled lvm2
%files module-lvm2
%_libdir/%name/modules/lib%{name}_lvm2.so
%_datadir/polkit-1/actions/org.freedesktop.UDisks2.lvm2.policy
%endif

%if_enabled zram
%files module-zram
%_libdir/%name/modules/lib%{name}_zram.so
%_datadir/polkit-1/actions/org.freedesktop.UDisks2.zram.policy
%_unitdir/zram-setup@.service
%endif

%if_enabled bcache
%files module-bcache
%_libdir/%name/modules/lib%{name}_bcache.so
%_datadir/polkit-1/actions/org.freedesktop.UDisks2.bcache.policy
%endif

%if_enabled btrfs
%files module-btrfs
%_libdir/%name/modules/lib%{name}_btrfs.so
%_datadir/polkit-1/actions/org.freedesktop.UDisks2.btrfs.policy
%endif

%if_enabled lsm
%files module-lsm
%_libdir/%name/modules/lib%{name}_lsm.so
%_datadir/polkit-1/actions/org.freedesktop.UDisks2.lsm.policy
%endif

%if_enabled iscsi
%files module-iscsi
%_libdir/%name/modules/lib%{name}_iscsi.so
%_datadir/polkit-1/actions/org.freedesktop.UDisks2.iscsi.policy
%endif

%if_enabled vdo
%files module-vdo
%_libdir/%name/modules/lib%{name}_vdo.so
%_datadir/polkit-1/actions/org.freedesktop.UDisks2.vdo.policy
%endif

%exclude %_libdir/%name/modules/*.la

%changelog
* Tue Jul 23 2019 Yuri N. Sedunov <aris@altlinux.org> 2.8.4-alt1
- 2.8.4

* Mon Jun 17 2019 Yuri N. Sedunov <aris@altlinux.org> 2.8.3-alt1
- 2.8.3

* Tue Mar 05 2019 Yuri N. Sedunov <aris@altlinux.org> 2.8.2-alt1
- 2.8.2

* Wed Sep 26 2018 Yuri N. Sedunov <aris@altlinux.org> 2.8.1-alt1
- 2.8.1

* Wed Aug 15 2018 Yuri N. Sedunov <aris@altlinux.org> 2.8.0-alt1
- 2.8.0

* Mon Jul 09 2018 Yuri N. Sedunov <aris@altlinux.org> 2.7.7-alt1
- 2.7.7

* Fri Feb 09 2018 Yuri N. Sedunov <aris@altlinux.org> 2.7.6-alt1
- 2.7.6

* Sat Dec 23 2017 Yuri N. Sedunov <aris@altlinux.org> 2.7.5-alt1
- 2.7.5

* Thu Nov 02 2017 Yuri N. Sedunov <aris@altlinux.org> 2.7.4-alt1
- 2.7.4

* Thu Sep 07 2017 Yuri N. Sedunov <aris@altlinux.org> 2.7.3-alt1
- 2.7.3

* Mon Aug 14 2017 Yuri N. Sedunov <aris@altlinux.org> 2.7.2-alt1
- 2.7.2

* Sat Jul 08 2017 Yuri N. Sedunov <aris@altlinux.org> 2.7.1-alt1
- 2.7.1
- reqs: xfsprogs (ALT #33608)

* Thu Jun 15 2017 Yuri N. Sedunov <aris@altlinux.org> 2.7.0-alt2
- updated dependencies

* Tue Jun 13 2017 Yuri N. Sedunov <aris@altlinux.org> 2.7.0-alt1
- updated to 2.7.0-13-ga26424b
- new *-module-{lvm2,bcache,zram,btrfs} subpackages

* Fri May 19 2017 Yuri N. Sedunov <aris@altlinux.org> 2.6.5-alt1
- 2.6.5

* Mon Apr 10 2017 Yuri N. Sedunov <aris@altlinux.org> 2.6.4-alt3
- data/Makefile.am fixed bad substitution (ALT #33346)

* Tue Mar 28 2017 Yuri N. Sedunov <aris@altlinux.org> 2.6.4-alt2
- 80-udisks2.rules: fixed ALT #33180

* Tue Mar 28 2017 Yuri N. Sedunov <aris@altlinux.org> 2.6.4-alt1
- updated to 2.6.4-14-ga556a64

* Sun Dec 11 2016 Yuri N. Sedunov <aris@altlinux.org> 2.1.9-alt0.1
- updated to 2.1.8-3-g054d9c4

* Wed Jul 27 2016 Yuri N. Sedunov <aris@altlinux.org> 2.1.8-alt0.1
- updated to 2.1.7-5-ga05e89d
- used mkfs.fat instead of old mkfs.vfat

* Tue Mar 01 2016 Yuri N. Sedunov <aris@altlinux.org> 2.1.7-alt1
- 2.1.7

* Tue Jun 30 2015 Yuri N. Sedunov <aris@altlinux.org> 2.1.6-alt1
- 2.1.6 release
- removed upstreamed udisks-1.92.0-alt-udiskd_dir.patch

* Fri Mar 27 2015 Yuri N. Sedunov <aris@altlinux.org> 2.1.6-alt0.1
- 2.1.6 snaphot

* Thu Jan 15 2015 Yuri N. Sedunov <aris@altlinux.org> 2.1.5-alt0.1
- 2.1.5 snapshot (fixed FDO #77134)

* Fri Jan 09 2015 Yuri N. Sedunov <aris@altlinux.org> 2.1.4-alt1
- 2.1.4

* Tue Mar 11 2014 Yuri N. Sedunov <aris@altlinux.org> 2.1.3-alt1
- 2.1.3 release

* Mon Jan 27 2014 Yuri N. Sedunov <aris@altlinux.org> 2.1.3-alt0.2
- fixed https://bugs.freedesktop.org/show_bug.cgi?id=71802

* Tue Jan 21 2014 Yuri N. Sedunov <aris@altlinux.org> 2.1.3-alt0.1
- 2.1.3 snapshot (4ce586f)

* Fri Aug 23 2013 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1 release

* Mon Jul 08 2013 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt0.1
- 2.1.1 snapshot (0a150d2)
- udisks2.control: use is_builtin_mode

* Sat Jul 06 2013 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt2.1
- 99-alt-udisks2-media-mount-point.rules: fixed syntax

* Thu Jul 04 2013 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt2
- 99-alt-udisks2-media-mount-point.rules: /media used for mounting
  Control support to switch mount points for removable media (ALT #27256, #29138)

* Mon Mar 18 2013 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0

* Sat Mar 16 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.92-alt2
- Added dependency on dbus-tools-gui (ALT #28692)

* Tue Feb 19 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.92-alt1
- 2.0.92

* Thu Dec 20 2012 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt2
- a time to obsolete old udisks

* Wed Dec 19 2012 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- after 2.0.1 snapshot (d2a937d3)

* Wed Oct 03 2012 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0 release

* Thu Sep 20 2012 Yuri N. Sedunov <aris@altlinux.org> 1.100.0-alt0.1
- 1.100.0 snapshot

* Fri Jul 27 2012 Yuri N. Sedunov <aris@altlinux.org> 1.99.0-alt1
- 1.99.0 release

* Wed Jul 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.99.0-alt0.1
- 1.99.0 snapshot

* Mon Jun 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.98.0-alt1
- 1.98.0

* Thu May 10 2012 Yuri N. Sedunov <aris@altlinux.org> 1.97.0-alt1
- 1.97.0

* Mon May 07 2012 Yuri N. Sedunov <aris@altlinux.org> 1.96.0-alt1
- 1.96.0

* Wed Apr 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.94.0-alt1.1
- 1.94.0 release

* Tue Apr 10 2012 Yuri N. Sedunov <aris@altlinux.org> 1.94.0-alt1
- 1.94.0 snapshot (ALT #27198)

* Thu Mar 22 2012 Yuri N. Sedunov <aris@altlinux.org> 1.93.0-alt2
- fixed udisksdprivdir accordingly with %%_libexecdir

* Tue Mar 06 2012 Yuri N. Sedunov <aris@altlinux.org> 1.93.0-alt1
- 1.93.0

* Wed Feb 29 2012 Yuri N. Sedunov <aris@altlinux.org> 1.92.0-alt1
- 1.92.0

* Wed Feb 08 2012 Yuri N. Sedunov <aris@altlinux.org> 1.91.0-alt1
- first build for Sisyphus
