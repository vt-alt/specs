%define _libexecdir %_prefix/libexec
%global _localstatedir %_var

Name: zfs
Version: 0.8.2
Release: alt1
Summary: ZFS on Linux
License: CDDL
Group: System/Kernel and hardware
URL: http://zfsonlinux.org/
Conflicts: fuse-zfs

Source0: %name-%version.tar
Patch1: zfs-0.7.13-import-by-disk-id.patch

BuildRequires: libblkid-devel libssl-devel libudev-devel libuuid-devel python3-devel zlib-devel rpm-build-kernel

%description
This package contains the ZFS command line utilities

%package utils
Summary: Native OpenZFS management utilities for Linux
Group: System/Kernel and hardware
Provides: spl-utils = %version-%release splat = %version-%release
Obsoletes: spl-utils < %version-%release

%description utils
This package provides the zpool and zfs commands that are used to
manage OpenZFS filesystems.

%package zed
Summary: OpenZFS Event Daemon
Group: System/Kernel and hardware

%description zed
This package adds OpenZFS to the system initramfs with a hook
for the initramfs-tools infrastructure.

%package -n lib%name
Summary: ZFS shared libraries
Group: System/Libraries

%description -n lib%name
This package contains ZFS shared libraries.

%package -n lib%name-devel
Summary: ZFS development files
Group: Development/C

%description -n lib%name-devel
This package contains ZFS development files.

%package -n kernel-source-%name
Summary: ZFS modules sources for Linux kernel
Group: Development/Kernel
BuildArch: noarch
Provides: kernel-src-%name = %version-%release

%description -n kernel-source-%name
This package contains ZFS modules sources for Linux kernel.

%prep
%setup -q
%patch1 -p1
sed -i 's|datarootdir|libdir|' lib/libzfs/Makefile.am

%build
%autoreconf
%configure \
	--sbindir=/sbin \
	--libexecdir=%_libexecdir \
	--with-config=user \
	--with-udevdir=/lib/udev \
	--with-udevruledir=%_udevrulesdir \
	--enable-systemd \
	--with-systemdunitdir=%_unitdir \
	--with-systemdpresetdir=%_unitdir-preset \
	--disable-sysvinit \
	--with-gnu-ld \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot pkgdatadir=%_datadir/doc/%name-utils-%version/examples modulesloaddir=%_sysconfdir/modules-load.d install
install -pDm0644 %SOURCE0 %kernel_srcdir/%name-%version.tar
gzip %kernel_srcdir/%name-%version.tar
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/lib*.so; do
	t=$(readlink "$f")
	ln -sf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/lib*.so.* %buildroot/%_lib/

install -m0644 COPYRIGHT LICENSE %buildroot%_datadir/doc/%name-utils-%version/

touch %buildroot%_sysconfdir/%name/zpool.cache
mkdir -p %buildroot%_sysconfdir/{modprobe.d,dfs}
touch %buildroot%_sysconfdir/dfs/sharetab
cat << __EOF__ > %buildroot%_sysconfdir/modprobe.d/zfs.conf
#options zfs zfs_autoimport_disable=0
__EOF__

rm -fr %buildroot%_datadir/zfs

%post utils
if [ $1 -eq 1 ] ; then
	/sbin/systemctl preset \
		zfs-import-cache.service \
		zfs-import-scan.service \
		zfs-mount.service \
		zfs-import.target \
		zfs.target \
		>/dev/null 2>&1 || :
fi

%preun utils
if [ $1 -eq 0 ] ; then
	/sbin/systemctl disable \
		zfs-import-cache.service \
		zfs-import-scan.service \
		zfs-mount.service \
		zfs-import.target \
		zfs.target \
		>/dev/null 2>&1 || :
fi

%post zed
if [ $1 -eq 1 ] ; then
	/sbin/systemctl preset \
		zfs-zed.service \
		>/dev/null 2>&1 || :
fi

%preun zed
if [ $1 -eq 0 ] ; then
	/sbin/systemctl disable \
		zfs-zed.service \
		>/dev/null 2>&1 || :
fi

%files utils
%_datadir/doc/%name-utils-%version
%dir %_sysconfdir/%name
%ghost %_sysconfdir/%name/zpool.cache
%dir %_sysconfdir/dfs
%ghost %_sysconfdir/dfs/sharetab
%exclude %_unitdir/zfs-zed.service
%config(noreplace) %_sysconfdir/modprobe.d/zfs.conf
%_sysconfdir/modules-load.d/%name.conf
%_unitdir/*.service
%_unitdir/*.target
%_unitdir-preset/50-zfs.preset
/lib/udev/*_id
%_udevrulesdir/*.rules
%exclude /sbin/zed
/sbin/*
%_bindir/*
%_man1dir/*.1*
%_man5dir/*.5*
%_man8dir/*.8*
%exclude %_man8dir/zed.8*

%files zed
%dir %_sysconfdir/%name/zed.d
%_sysconfdir/%name/zed.d/zed.rc
%_sysconfdir/%name/zed.d/zed-functions.sh
%_unitdir/zfs-zed.service
/sbin/zed
%_libexecdir/zfs
%_man8dir/zed.8*

%files -n lib%name
/%_lib/*.so.*

%files -n lib%name-devel
%_includedir/*
%_pkgconfigdir/*.pc
%_libdir/*.so

%files -n kernel-source-%name
%_usrsrc/kernel

%changelog
* Fri Sep 27 2019 Anton Farygin <rider@altlinux.ru> 0.8.2-alt1
- 0.8.2
- added conflicts with fuse-zfs

* Mon Jul 15 2019 Valery Inozemtsev <shrek@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Tue Mar 26 2019 Anton Farygin <rider@altlinux.ru> 0.7.13-alt2
- removed ALT glibc functions from libuutil, since  ALT build glibc has its own
  implementation of the strlcat, strlcpy and strnlen functions (closes: #36412)

* Thu Mar 14 2019 Anton Farygin <rider@altlinux.ru> 0.7.13-alt1
- 0.7.13

* Thu Dec 06 2018 Anton Farygin <rider@altlinux.ru> 0.7.12-alt3
- fixed buffer overflow during zfs replication (thanks shrek@) (closes: #35730)

* Tue Nov 20 2018 Anton Farygin <rider@altlinux.ru> 0.7.12-alt2
- changed the source code praparation scheme for kernel-modules-zfs

* Tue Nov 20 2018 Anton Farygin <rider@altlinux.ru> 0.7.12-alt1
- 0.7.12

* Thu Oct 04 2018 Anton Farygin <rider@altlinux.ru> 0.7.11-alt1
- 0.7.11

* Tue Jun 26 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.7.9-alt2
- fixed build kernel modules

* Mon Jun 25 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.7.9-alt1
- 0.7.9

* Wed Dec 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.7.5-alt2
- update preset service

* Tue Dec 19 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.7.5-alt1
- 0.7.5

* Sat Nov 18 2017 Anton Farygin <rider@altlinux.ru> 0.7.3-alt1
- 0.7.3

* Fri Sep 15 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.7.1-alt2
- fixed build kernel modules

* Thu Sep 14 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Mon Aug 07 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Thu Jul 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5.11-alt0.M80P.1
- backport to p8 branch

* Thu Jul 13 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5.11-alt1
- 0.6.5.11

* Thu Jun 15 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5.10-alt1
- 0.6.5.10

* Tue Feb 07 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5.9-alt0.M80P.1
- backport to p8 branch

* Mon Feb 06 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5.9-alt1
- 0.6.5.9

* Thu Oct 13 2016 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5.8-alt1.M80P.1
- backport to p8 branch

* Thu Oct 13 2016 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5.8-alt2
- moved libraries to /%_lib

* Tue Oct 11 2016 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5.8-alt0.M80P.1
- backport to p8 branch

* Mon Oct 10 2016 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5.8-alt1
- 0.6.5.8

* Wed Aug 27 2014 Led <led@altlinux.ru> 0.6.3-alt12
- upstream updates and fixes

* Sat Aug 16 2014 Led <led@altlinux.ru> 0.6.3-alt11
- upstream updates

* Thu Aug 14 2014 Led <led@altlinux.ru> 0.6.3-alt10
- upstream updates and fixes

* Sat Aug 09 2014 Led <led@altlinux.ru> 0.6.3-alt9
- upstream updates and fixes

* Sun Aug 03 2014 Led <led@altlinux.ru> 0.6.3-alt8
- upstream updates and fixes

* Wed Jul 30 2014 Led <led@altlinux.ru> 0.6.3-alt7
- upstream updates and fixes

* Sat Jul 26 2014 Led <led@altlinux.ru> 0.6.3-alt6
- upstream updates and fixes

* Thu Jul 03 2014 Led <led@altlinux.ru> 0.6.3-alt5
- upstream updates and fixes

* Tue Jul 01 2014 Led <led@altlinux.ru> 0.6.3-alt4
- upstream updates and fixes

* Mon Jun 16 2014 Led <led@altlinux.ru> 0.6.3-alt3
- module: replace stupidly defined spl's 'hz' with generic 'HZ'
- fixed Requires of kernel-source-zfs

* Sat Jun 14 2014 Led <led@altlinux.ru> 0.6.3-alt2
- Revert
  "sys/zfs_context: make ddi_time_* macros visible for build kernel- modules"

* Sat Jun 14 2014 Led <led@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Sat Jun 07 2014 Led <led@altlinux.ru> 0.6.2-alt50
- upstream updates and fixes

* Sun Jun 01 2014 Led <led@altlinux.ru> 0.6.2-alt49
- upstream updates

* Fri May 23 2014 Led <led@altlinux.ru> 0.6.2-alt48
- upstream updates

* Tue May 20 2014 Led <led@altlinux.ru> 0.6.2-alt47
- upstream updates and fixes

* Thu May 15 2014 Led <led@altlinux.ru> 0.6.2-alt46
- upstream updates

* Wed May 07 2014 Led <led@altlinux.ru> 0.6.2-alt45
- upstream updates and fixes

* Sat Apr 26 2014 Led <led@altlinux.ru> 0.6.2-alt44
- upstream updates

* Sat Apr 19 2014 Led <led@altlinux.ru> 0.6.2-alt43
- upstream fixes

* Tue Apr 15 2014 Led <led@altlinux.ru> 0.6.2-alt42
- upstream updates

* Sat Apr 12 2014 Led <led@altlinux.ru> 0.6.2-alt41
- upstream updates and fixes

* Thu Apr 10 2014 Led <led@altlinux.ru> 0.6.2-alt40
- upstream fixes

* Mon Apr 07 2014 Led <led@altlinux.ru> 0.6.2-alt39
- upstream updates and fixes

* Mon Mar 24 2014 Led <led@altlinux.ru> 0.6.2-alt38
- upstream updates and fixes

* Fri Mar 21 2014 Led <led@altlinux.ru> 0.6.2-alt37
- upstream updates and fixes

* Wed Mar 12 2014 Led <led@altlinux.ru> 0.6.2-alt36
- upstream fixes

* Mon Mar 10 2014 Led <led@altlinux.ru> 0.6.2-alt35
- upstream updates and fixes

* Sun Feb 23 2014 Led <led@altlinux.ru> 0.6.2-alt34
- upstream updates and fixes

* Wed Feb 12 2014 Led <led@altlinux.ru> 0.6.2-alt33
- upstream fixes

* Thu Feb 06 2014 Led <led@altlinux.ru> 0.6.2-alt32
- upstream fixes
- added systemd unit files for ZFS startup
- disabled sysvinit

* Tue Feb 04 2014 Led <led@altlinux.ru> 0.6.2-alt31
- upstream fixes

* Sat Feb 01 2014 Led <led@altlinux.ru> 0.6.2-alt30
- upstream updates and fixes

* Fri Jan 24 2014 Led <led@altlinux.ru> 0.6.2-alt29
- upstream updates and fixes

* Thu Jan 16 2014 Led <led@altlinux.ru> 0.6.2-alt28
- upstream updates and fixes

* Tue Jan 14 2014 Led <led@altlinux.ru> 0.6.2-alt27
- upstream updates and fixes

* Wed Jan 08 2014 Led <led@altlinux.ru> 0.6.2-alt26
- upstream updates and fixes

* Tue Dec 24 2013 Led <led@altlinux.ru> 0.6.2-alt25
- upstream fixes

* Sat Dec 21 2013 Led <led@altlinux.ru> 0.6.2-alt24
- upstream updates and fixes

* Thu Dec 19 2013 Led <led@altlinux.ru> 0.6.2-alt23
- upstream updates and fixes

* Fri Dec 13 2013 Led <led@altlinux.ru> 0.6.2-alt22
- upstream fixes

* Wed Dec 11 2013 Led <led@altlinux.ru> 0.6.2-alt21
- upstream fixes

* Mon Dec 09 2013 Led <led@altlinux.ru> 0.6.2-alt20
- upstream updates and fixes

* Tue Dec 03 2013 Led <led@altlinux.ru> 0.6.2-alt19
- upstream updates and fixes

* Sun Nov 24 2013 Led <led@altlinux.ru> 0.6.2-alt18
- upstream updates and fixes

* Sat Nov 16 2013 Led <led@altlinux.ru> 0.6.2-alt17
- upstream updates and fixes

* Tue Nov 12 2013 Led <led@altlinux.ru> 0.6.2-alt16
- Updated kernel-source-spl requires

* Tue Nov 12 2013 Led <led@altlinux.ru> 0.6.2-alt15
- kernel modules: added missed includes

* Tue Nov 12 2013 Led <led@altlinux.ru> 0.6.2-alt14
- upstream updates and fixes

* Tue Nov 05 2013 Led <led@altlinux.ru> 0.6.2-alt13
- upstream updates and fixes

* Sat Nov 02 2013 Led <led@altlinux.ru> 0.6.2-alt12
- upstream fixes

* Fri Nov 01 2013 Led <led@altlinux.ru> 0.6.2-alt11
- upstream updates and fixes

* Tue Oct 29 2013 Led <led@altlinux.ru> 0.6.2-alt10
- upstream updates and fixes

* Wed Oct 23 2013 Led <led@altlinux.ru> 0.6.2-alt9
- fixed udevdir

* Wed Oct 23 2013 Led <led@altlinux.ru> 0.6.2-alt8
- upstream fixes

* Sat Oct 19 2013 Led <led@altlinux.ru> 0.6.2-alt7
- upstream fixes

* Mon Oct 14 2013 Led <led@altlinux.ru> 0.6.2-alt6
- upstream updates and fixes

* Thu Oct 10 2013 Led <led@altlinux.ru> 0.6.2-alt5
- upstream updates and fixes

* Fri Sep 27 2013 Led <led@altlinux.ru> 0.6.2-alt4
- upstream updates and fixes

* Sat Sep 14 2013 Led <led@altlinux.ru> 0.6.2-alt3
- upstream fixes

* Sun Sep 08 2013 Led <led@altlinux.ru> 0.6.2-alt2
- upstream fixes

* Tue Aug 27 2013 Led <led@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Sun Aug 18 2013 Led <led@altlinux.ru> 0.6.1-alt12
- upstream updates and fixes

* Thu Aug 15 2013 Led <led@altlinux.ru> 0.6.1-alt11
- upstream updates

* Sun Aug 11 2013 Led <led@altlinux.ru> 0.6.1-alt10
- upstream updates and fixes

* Fri Aug 02 2013 Led <led@altlinux.ru> 0.6.1-alt9
- kernel modules: upstream updates

* Sat Jul 27 2013 Led <led@altlinux.ru> 0.6.1-alt8
- zpool: upstream fixes

* Thu Jul 18 2013 Led <led@altlinux.ru> 0.6.1-alt7
- upstream fixes

* Wed Jul 17 2013 Led <led@altlinux.ru> 0.6.1-alt6
- upstream fixes

* Fri Jul 12 2013 Led <led@altlinux.ru> 0.6.1-alt5
- upstream updates

* Sat Jul 06 2013 Led <led@altlinux.ru> 0.6.1-alt4
- kernel-source-%name: add config/missing

* Thu Jul 04 2013 Led <led@altlinux.ru> 0.6.1-alt3
- upstream fixes
- kernel-source-%%name requires kernel-source-spl

* Tue Jul 02 2013 Led <led@altlinux.ru> 0.6.1-alt2
- upstream fixes

* Tue Jun 18 2013 Led <led@altlinux.ru> 0.6.1-alt1
- initial build
