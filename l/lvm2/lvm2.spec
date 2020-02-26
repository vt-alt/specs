%define _unpackaged_files_terminate_build 1

%define lvm2version 2.03.8
%define dmversion 1.02.169

%define _sbindir /sbin
%define usrsbindir %_prefix/sbin
%define _runtimedir /run
%define _lockdir /run/lock
%def_enable static

%def_enable selinux
%def_enable lvmpolld
%def_enable lvmlockd
%def_enable blkid_wiping
%def_disable lvmdbusd
%def_enable dmfilemapd
%def_enable thin
%def_enable vdo
%def_enable writecache
%def_enable cmirrord
%def_enable cmdlib

%if_enabled lvmlockd
 %def_enable lvmlockd_sanlock
 %def_enable lvmlockd_dlm
%endif

Summary: Userland logical volume management tools
Name: lvm2
Version: %lvm2version
Release: alt1
License: GPLv2+ AND LGPL-2.1+

Group: System/Base
Url: http://sources.redhat.com/lvm2
Source: %name-%version.tar

Source3: lvm2-monitor.init
Source5: blk-availability.init
Source6: lvm2-lvmpolld.init

Patch: %name-%version-%release.patch

Conflicts: liblvm

Requires: dmsetup  >= %{dmversion}-%{release}
Requires: dmeventd >= %{dmversion}-%{release}
Requires: liblvm2  = %{lvm2version}-%{release}

BuildRequires: gcc-c++
BuildRequires: libreadline-devel libtinfo-devel libudev-devel CUnit-devel
BuildRequires: libaio-devel
# libudev-devel >= 205 required for udev-systemd-background-jobs
BuildRequires: libudev-devel >= 205
BuildRequires: systemd-devel
%if_enabled thin
BuildRequires: thin-provisioning-tools >= 0.7.0
%endif
BuildRequires: autoconf-archive
%{?_enable_thin:BuildRequires: thin-provisioning-tools >= 0.5.4}
BuildRequires(pre): rpm-build-python3
%{?_enable_lvmdbusd:BuildRequires: python3-devel python3-module-setuptools python3-module-dbus python3-module-pyudev}
%{?_enable_static:BuildRequires: libreadline-devel-static libtinfo-devel-static libaio-devel-static}
%{?_enable_selinux:BuildRequires: libselinux-devel libsepol-devel}
%{?_enable_blkid_wiping:BuildRequires: libblkid-devel >= 2.23}
%{?_enable_lvmlockd_sanlock:BuildRequires: sanlock-devel >= 3.3.0}
%{?_enable_lvmlockd_dlm:BuildRequires: libdlm-devel >= 4.0.9}
%{?_enable_cmirrord:BuildRequires: libcorosync-devel}

%description
LVM2 includes all of the support for handling read/write operations
on physical volumes (hard disks, RAID-Systems, magneto optical, etc.,
multiple devices (MD), see mdadd(8) or even loop devices, see losetup(8)),
creating volume groups (kind of virtual disks) from one or more physical
volumes and creating one or more logical volumes (kind of logical
partitions) in volume groups.

%package static
Summary: Statically linked userland logical volume management tool
Group: System/Base
Requires: %name = %lvm2version-%release

%description static
This package contains statically linked LVM2 tool.

### liblvm* subpackages go here.

%package -n liblvm2
Summary: LVM2 shared libraries
License: LGPLv2
Group: System/Libraries
Requires: libdevmapper = %dmversion-%release
Requires: libdevmapper-event = %dmversion-%release

%description -n liblvm2
This package contains shred lvm2 libraries for applications.

%package -n liblvm2-devel
Summary: LVM2 development libraries and headers
Group: System/Libraries
License: LGPLv2
Requires: lvm2 = %lvm2version-%release
Requires: liblvm2 = %lvm2version-%release
Requires: libdevmapper-devel = %dmversion-%release

%description -n liblvm2-devel
This package contains files needed to develop applications that use
the lvm2 libraries.

### device-mapper subpackages go here.

%package -n libdevmapper
Version: %dmversion
Summary: Library of routines for device-mapper management
Group: System/Libraries

%description -n libdevmapper
Library of routines for device-mapper management.

%package -n libdevmapper-devel
Version: %dmversion
Summary: Header file for libdevmapper
Group: System/Libraries
Requires: libdevmapper = %dmversion-%release

%description -n libdevmapper-devel
Header files for libdevmapper.

%package -n libdevmapper-devel-static
Version: %dmversion
Summary: Static version of libdevmapper
Group: System/Libraries
Requires: libdevmapper-devel = %dmversion-%release

%description -n libdevmapper-devel-static
Static version of libdevmapper.

%package -n dmsetup
Version: %dmversion
Summary: Utilities for low level logical volume management
Group: System/Kernel and hardware
Requires: libdevmapper = %dmversion-%release
Requires: lsblk udev >= 150-alt4

%description -n dmsetup
Utilities for low level logical volume management.

%package -n dmeventd
Version: %dmversion
Summary: Device-mapper event daemon
Group: System/Base
Requires: dmsetup = %dmversion-%release
Requires: libdevmapper-event = %dmversion-%release

%description -n dmeventd
This package contains the dmeventd daemon for monitoring the state
of device-mapper devices.

%package -n libdevmapper-event
Summary: Device-mapper event daemon shared library
Version: %dmversion
License: LGPLv2
Group: System/Libraries
Requires: liblvm2  = %lvm2version-%release
Requires: libdevmapper = %dmversion-%release

%description -n libdevmapper-event
This package contains the device-mapper event daemon shared library,
libdevmapper-event.

%package -n libdevmapper-event-devel
Summary: Development libraries and headers for the device-mapper event daemon
Version: %dmversion
License: LGPLv2
Group: System/Libraries
Requires: libdevmapper-event = %dmversion-%release
Requires: libdevmapper-devel = %dmversion-%release

%description -n libdevmapper-event-devel
This package contains files needed to develop applications that use
the device-mapper event library.

%package lockd
Summary: LVM locking daemon
Group: System/Base
Requires: %name = %lvm2version-%release
%{?_enable_lvmlockd_sanlock:Requires: sanlock}
%{?_enable_lvmlockd_dlm:Requires: dlm}

%description lockd
LVM commands use lvmlockd to coordinate access to shared storage.

%package cmirrord
Summary: Daemon for device-mapper-based clustered mirrors
Group: System/Base
Provides: cmirror = %lvm2version-%release
Provides: %name-cmirror = %lvm2version-%release
Requires: corosync >= 1.99.9
Requires: dmsetup = %dmversion-%release
Requires: resource-agents >= 3.9.5
 
%description cmirrord
Daemon providing device-mapper-based mirrors in a shared-storage cluster.

%package dbusd
Summary: LVM2 D-Bus daemon
License: GPLv2
Group: System/Base
Requires: %name = %lvm2version-%release
Requires: dbus

%description dbusd
Daemon for access to LVM2 functionality through a D-Bus interface.

%prep
%setup
%patch -p1
%ifarch %e2k
# as of lcc-1.21.24
sed -i '/-Wmissing-parameter-type/d' make.tmpl.in
%endif

%build
%autoreconf
export ac_cv_path_MODPROBE_CMD=%_sbindir/modprobe

%if_enabled static
%configure \
	--disable-readline \
	--disable-selinux \
	--disable-blkid_wiping \
	--disable-nls \
	--enable-static_link \
	ac_cv_lib_dl_dlopen=no \
	--with-optimisation="%optflags -Os" \
	--with-group= \
	--with-staticdir=%_sbindir \
	--with-user= \
	--disable-pkgconfig \
	--with-device-uid=0 \
	--with-device-gid=6 \
	--with-device-mode=0660 \
	--with-dmeventd-path="%_sbindir/dmeventd" \
	--with-default-pid-dir=%_runtimedir \
	--with-default-dm-run-dir=%_runtimedir \
	--with-default-run-dir=%_runtimedir/lvm \
	--with-default-locking-dir=%_lockdir/lvm \
	--disable-silent-rules

	#
%make_build libdm
%make_build lib
%make_build -C tools lvm.static
mv tools/lvm.static .
mv libdm/ioctl/libdevmapper.a .
%make clean
%endif # static

# dynamic

%configure \
	%{subst_enable selinux} \
	--disable-static_link \
	--enable-readline \
	--with-group= \
	--with-user= \
	--enable-pkgconfig \
	--with-device-uid=0 \
	--with-device-gid=6 \
	--with-device-mode=0660 \
	--enable-write_install \
	%{subst_enable cmdlib} \
	--with-usrlibdir=%_libdir \
	--with-usrsbindir=%usrsbindir \
	--enable-dmeventd \
	--with-udevdir=%_udevrulesdir \
	%{subst_enable lvmpolld} \
	%{subst_enable dmfilemapd} \
	%{subst_enable cmirrord} \
	--enable-udev_sync \
	%{subst_enable blkid_wiping} \
	%{?_enable_lvmlockd_dlm:--enable-lvmlockd-dlm --enable-lvmlockd-dlmcontrol} \
	%{?_enable_lvmlockd_sanlock:--enable-lvmlockd-sanlock} \
	%{?_enable_lvmdbusd:--enable-dbus-service} \
	%{?_enable_vdo:--with-vdo=internal --with-vdo-format=%_bindir/vdoformat} \
	%{?_enable_writecache:--with-writecache=internal} \
	--with-dmeventd-path="%_sbindir/dmeventd" \
	--with-systemdsystemunitdir=%_unitdir \
	--with-tmpfilesdir=%_tmpfilesdir \
	--with-default-pid-dir=%_runtimedir \
	--with-default-dm-run-dir=%_runtimedir \
	--with-default-run-dir=%_runtimedir/lvm \
	--with-default-locking-dir=%_lockdir/lvm \
	--disable-silent-rules

%make_build

%install
%makeinstall_std
%makeinstall_std install_system_dirs
%makeinstall_std install_systemd_units
%makeinstall_std install_systemd_generators
%makeinstall_std install_tmpfiles_configuration

chmod -R u+rwX %buildroot
%{?_enable_static:install -pm755 lvm.static %buildroot%_sbindir}

### device-mapper part

%{?_enable_static:install -pm755 libdevmapper.a %buildroot%_libdir/}

mkdir -p %buildroot/%_lib

# Relocate shared library from %_libdir/ to /%_lib/.
for f in `ls %buildroot%_libdir/libdevmapper.so`; do
	t=`objdump -p "$f" |awk '/SONAME/ {print $2}'`
	[ -n "$t" ]
	ln -sf ../../%_lib/"$t" "$f"
done

mv %buildroot%_libdir/libdevmapper.so.1.02 %buildroot/%_lib/
mv %buildroot%_libdir/libdevmapper-event.so.1.02 %buildroot/%_lib/

pushd %buildroot%_libdir
rm -f libdevmapper-event.so
ln -sf ../../%_lib/libdevmapper-event.so.1.02 ./libdevmapper-event.so
popd

# Fix pkgconfig file.
subst '/^Version:/ s/"\([^[:space:]]\+\)[^"]*"/\1/' %buildroot%_pkgconfigdir/*

# provide a symlink for devmapper.pc
ln -sf devmapper.pc %buildroot%_pkgconfigdir/libdevmapper.pc

### lvm2-monitor init script

mkdir -p %buildroot%_initdir
install -m 0755 %SOURCE3 %buildroot%_initdir/lvm2-monitor
install -m 0755 %SOURCE5 %buildroot%_initdir/blk-availability
install -m 0755 %SOURCE6 %buildroot%_initdir/lvm2-lvmpolld

%post
%if_enabled lvmpolld
%post_service lvm2-lvmpolld
%endif
%post_service blk-availability
%post_service lvm2-monitor

%preun
%preun_service lvm2-monitor
%if_enabled lvmpolld
%preun_service lvm2-lvmpolld
%endif
%preun_service blk-availability

%post lockd
%post_service lvmlockd

%preun lockd
%preun_service lvmlockd

%post dbusd
%post_service lvm2-lvmdbusd

%preun dbusd
%preun_service lvm2-lvmdbusd

%files
%doc README WHATS_NEW udev/12-dm-permissions.rules
%doc doc/*.txt
%_sbindir/*
%exclude %_sbindir/dmsetup
%exclude %_sbindir/dmstats
%exclude %_sbindir/blkdeactivate
%exclude %_sbindir/dmeventd
%{?_enable_static:%exclude %_sbindir/*.static}
%_mandir/man?/*
%exclude %_man8dir/dmsetup*
%exclude %_man8dir/dmstats*
%exclude %_man8dir/blkdeactivate*
%exclude %_man8dir/cmirrord*
%config(noreplace) %_sysconfdir/lvm/lvm.conf
%config(noreplace) %_sysconfdir/lvm/lvmlocal.conf
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/lvm/profile/*.profile
%_initdir/lvm2-monitor
%_unitdir/lvm2-monitor.service
%_unitdir/blk-availability.service
%_initdir/blk-availability
%_unitdir/lvm2-pvscan@.service
%_udevrulesdir/69-dm-lvm-metad.rules
%if_enabled lvmpolld
%_initdir/lvm2-lvmpolld
%_unitdir/lvm2-lvmpolld*
%endif
%if_enabled lvmlockd
%exclude %_sbindir/lvmlockd
%exclude %_sbindir/lvmlockctl
%exclude %_man8dir/lvmlockd*
%endif
/lib/systemd/system-generators/lvm2-activation-generator
%_tmpfilesdir/%name.conf
%dir %_sysconfdir/lvm
%dir %_sysconfdir/lvm/profile
%defattr(600,root,root,700)
%dir %_sysconfdir/lvm/backup
%dir %_sysconfdir/lvm/archive
%dir %_sysconfdir/lvm/cache
#%ghost %_lockdir/lvm
%ghost %_sysconfdir/lvm/cache/.cache

%if_enabled static
%files static
%_sbindir/*.static
%endif # static

%files -n liblvm2
%_libdir/liblvm2cmd.so.*

%files -n liblvm2-devel
%_libdir/liblvm2cmd.so
%_includedir/lvm2cmd.h

%files -n libdevmapper
/%_lib/libdevmapper.so.*

%files -n libdevmapper-devel
%_libdir/libdevmapper.so
%_includedir/libdevmapper.h
%_pkgconfigdir/*devmapper.*

%files -n libdevmapper-devel-static
%_libdir/libdevmapper.a

%files -n dmsetup
%doc WHATS_NEW_DM
%_sbindir/dmsetup
%_man8dir/dmsetup*
%_sbindir/blkdeactivate
%_man8dir/blkdeactivate*
%_sbindir/dmstats
%_man8dir/dmstats*
%_udevrulesdir/*
%exclude %_udevrulesdir/69-dm-lvm-metad.rules

%files -n dmeventd
%_sbindir/dmeventd
%_unitdir/dm-event.service
%_unitdir/dm-event.socket

%files -n libdevmapper-event
/%_lib/libdevmapper-event.so.*
%_libdir/libdevmapper-event-*.so*
%dir %_libdir/device-mapper
%_libdir/device-mapper/libdevmapper-event-*.so*

%files -n libdevmapper-event-devel
%_libdir/libdevmapper-event.so
%_includedir/libdevmapper-event.h
%_pkgconfigdir/devmapper-event.pc

%if_enabled lvmlockd
%files lockd
%_sbindir/lvmlockd
%_sbindir/lvmlockctl
%_man8dir/lvmlockd*
%_unitdir/lvmlock*
#%_initdir/lvmlock*
%endif

%if_enabled cmirrord
%files cmirrord
%usrsbindir/cmirrord
%_man8dir/cmirrord*
%_unitdir/lvm2-cmirrord.service
%endif

%if_enabled lvmdbusd
%files dbusd
%_sbindir/lvmdbusd
%_sysconfdir/dbus-1/system.d/com.redhat.lvmdbus1.conf
%_datadir/dbus-1/system-services/com.redhat.lvmdbus1.service
%_man8dir/lvmdbusd.*
%_unitdir/lvm2-lvmdbusd.service
%python3_sitelibdir/lvmdbusd
%endif

%changelog
* Thu Feb 20 2020 Alexey Shabalin <shaba@altlinux.org> 2.03.8-alt1
- 2.03.8

* Thu Dec 12 2019 Alexey Shabalin <shaba@altlinux.org> 2.03.7-alt1
- 2.03.7

* Fri Oct 25 2019 Alexey Shabalin <shaba@altlinux.org> 2.03.6-alt1
- 2.03.6

* Sat Aug 10 2019 Alexey Shabalin <shaba@altlinux.org> 2.03.5-alt1
- 2.03.5
- drop applib support
- drop python2 and python3 bindings
- drop cluster support
- drop lvmetad support
- add cmirrord support
- add writecache support
- add vdo support

* Mon Jun 03 2019 Alexey Shabalin <shaba@altlinux.org> 2.02.185-alt1
- 2.02.185
- filter zvols and PVE VG by default
- enable issue_discards by default in config

* Tue May 07 2019 Alexey Shabalin <shaba@altlinux.org> 2.02.185-alt0.1.9d7afaaa
- snapshot of stable-2.02 branch
- update udev rules for lvm metad

* Mon Apr 01 2019 Alexey Shabalin <shaba@altlinux.org> 2.02.184-alt1
- 2.02.184
- enable use lvmetad by default
- enable udev_systemd_background_jobs
- enable lvmlockd

* Mon Nov 26 2018 Alexey Shabalin <shaba@altlinux.org> 2.02.182-alt2
- shutdown lvmetad automatically after one hour of inactivity
- disable use lvmetad by default

* Fri Nov 23 2018 Alexey Shabalin <shaba@altlinux.org> 2.02.182-alt1
- 2.02.182
- fixed blkdeactivate script for bash3

* Mon Aug 13 2018 Alexey Shabalin <shaba@altlinux.org> 2.02.181-alt1
- 2.02.181

* Wed Jun 27 2018 Alexey Shabalin <shaba@altlinux.ru> 2.02.180-alt0.1
- 2.02.180(2)-git (2018-06-18)
- disable build python2 and python3 bindings based on deprecated liblvm2app

* Sat Apr 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.02.177-alt4
- (NMU) Rebuilt with python-3.6.4.

* Wed Apr 25 2018 Michael Shigorin <mike@altlinux.org> 2.02.177-alt3
- fix thin knob (was ignored when systemd is enabled)
- E2K: avoid lcc-unsupported option

* Sun Jan 28 2018 Alexey Shabalin <shaba@altlinux.ru> 2.02.177-alt2
- BOOTSTRAP: introduce systemd, thin knobs (on by default)
  + conditionally loosen BR: libudev-devel as 205+ isn't
    a strict requirement for a build without systemd support
- internal macros cleaned up
- add symlink /usr/sbin/clvmd -> /sbin/clvmd (fixed bug #33362)

* Wed Dec 20 2017 Alexey Shabalin <shaba@altlinux.ru> 2.02.177-alt1
- 2.02.177

* Fri Nov 10 2017 Alexey Shabalin <shaba@altlinux.ru> 2.02.176-alt1
- 2.02.176

* Fri Sep 29 2017 Alexey Shabalin <shaba@altlinux.ru> 2.02.174-alt1
- 2.02.174

* Thu Jul 13 2017 Alexey Shabalin <shaba@altlinux.ru> 2.02.172-alt1
- 2.02.172

* Wed Dec 07 2016 Alexey Shabalin <shaba@altlinux.ru> 2.02.168-alt1
- 2.02.168

* Tue Nov 08 2016 Alexey Shabalin <shaba@altlinux.ru> 2.02.167-alt1
- 2.02.167

* Thu Sep 22 2016 Alexey Shabalin <shaba@altlinux.ru> 2.02.165-alt1
- 2.02.165

* Mon Aug 01 2016 Alexey Shabalin <shaba@altlinux.ru> 2.02.162-alt1
- 2.02.162

* Tue Jul 05 2016 Alexey Shabalin <shaba@altlinux.ru> 2.02.158-alt1
- 2.02.158
- build with --enable-blkid_wiping
- build with --disable-udev-systemd-background-jobs; else need move systemd-run to rootbindir
- don't run pvscan in background
- define %_runtimedir as /run (need for systemd socket activation lvm2-lvmetad service without /var mounted) (fixed bug #32216)
- define %_lockdir as /run/lock

* Fri Jun 24 2016 Alexey Shabalin <shaba@altlinux.ru> 2.02.157-alt2
- 2.02.157

* Thu Jun 16 2016 Alexey Shabalin <shaba@altlinux.ru> 2.02.156-alt1
- 2.02.156

* Mon Apr 25 2016 Alexey Shabalin <shaba@altlinux.ru> 2.02.151-alt1
- 2.02.151
- update requires for lockd package
- add python3 package
- add dbusd package, but not buld now

* Mon Mar 28 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.02.137-alt2
- enabled cluster support

* Thu Dec 10 2015 Alexey Shabalin <shaba@altlinux.ru> 2.02.137-alt1
- 2.02.137

* Thu Sep 10 2015 Alexey Shabalin <shaba@altlinux.ru> 2.02.130-alt1
- 2.02.130

* Tue Aug 11 2015 Alexey Shabalin <shaba@altlinux.ru> 2.02.127-alt1
- 2.02.127

* Tue Jul 14 2015 Alexey Shabalin <shaba@altlinux.ru> 2.02.125-alt1
- 2.02.125
- move blkdeactivate to dmsetup package
- enable lvmpolld

* Tue May 12 2015 Alexey Shabalin <shaba@altlinux.ru> 2.02.119-alt1
- 2.02.119

* Fri Apr 10 2015 Alexey Shabalin <shaba@altlinux.ru> 2.02.118-alt1
- 2.02.118

* Wed Mar 04 2015 Alexey Shabalin <shaba@altlinux.ru> 2.02.116-alt1
- 2.02.116
- add package python-module-lvm

* Fri Oct 03 2014 Alexey Shabalin <shaba@altlinux.ru> 2.02.111-alt1
- 2.02.111
- enable lvmetad by default
- set default preferred_names in lvm.conf

* Tue Sep 02 2014 Alexey Shabalin <shaba@altlinux.ru> 2.02.110-alt1
- 2.02.110

* Wed Jun 25 2014 Alexey Shabalin <shaba@altlinux.ru> 2.02.107-alt1
- 2.02.107

* Wed Apr 23 2014 Alexey Shabalin <shaba@altlinux.ru> 2.02.106-alt1
- 2.02.106

* Sun Jan 19 2014 Alexey Shabalin <shaba@altlinux.ru> 2.02.104-alt1
- 2.02.104

* Mon Oct 07 2013 Alexey Shabalin <shaba@altlinux.ru> 2.02.103-alt1
- 2.02.103

* Mon Jul 29 2013 Alexey Shabalin <shaba@altlinux.ru> 2.02.99-alt1
- 2.02.99

* Mon Nov 19 2012 Alexey Shabalin <shaba@altlinux.ru> 2.02.98-alt1
- git snapshot 7a34db0c
- build with lvmetad support
- add lvm2-lvmetad and blk-availability services
- adapt blkdeactivate.sh for bash3 (tnx iv@)

* Sat Aug 18 2012 Alexey Shabalin <shaba@altlinux.ru> 2.02.97-alt1
- 2.02.97

* Wed Jun 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.96-alt1
- 2.02.96

* Tue Jun 05 2012 Alexey Shabalin <shaba@altlinux.ru> 2.02.95-alt2
- add systemd unit dm-event, but not enable by default.
- use systemd units from upstream.
- adapt systemd unit for ALTLinux.
- use pvscan --cache instead of vgscan in systemd units.
- add patch for build with libudev > 183.

* Mon Apr 02 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.95-alt1
- 2.02.95

* Tue Feb 07 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.90-alt1
- 2.02.90

* Tue Jan 31 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.89-alt1
- 2.02.89

* Tue Sep 13 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.88-alt1
- 2.02.88.

* Fri Aug 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.87-alt1
- 2.02.87.

* Wed Jul 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.86-alt1
- 2.02.86.

* Fri May 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.85-alt2
- shaba@:
    add lvm2-monitor.service

* Tue May 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.85-alt1
- 2.02.85.

* Tue Feb 15 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.84-alt1
- 2.02.84.
- shaba@:
    add libs-cleanup.patch from debian
    shared build with selinux

* Mon Feb 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.83-alt3
- 2.02.83.

* Tue Jan 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.82-alt2
- bump release to alt2 to avoid dm version conflict

* Tue Jan 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.82-alt1
- 2.02.82.

* Mon Jan 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.81-alt1
- 2.02.81.

* Sun Jan 16 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.80-alt1
- 2.02.80.

* Tue Dec 21 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.79-alt1
- 2.02.79.

* Mon Dec 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.78-alt1
- 2.02.78.

* Tue Nov 23 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.77-alt1
- 2.02.77.

* Mon Nov 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.76-alt1
- 2.02.76.
- fix 'executable' parameter processing

* Fri Nov 05 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.75-alt3
- build with proper dmeventd path (ALT #24499)

* Sun Oct 31 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.75-alt2
- move libdevmapper-event.so.1.00 to /lib[64] (ALT #24458)

* Tue Oct 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.75-alt1
- 2.02.75.

* Thu Aug 26 2010 Konstantin Pavlov <thresh@altlinux.org> 2.02.73-alt1
- 2.02.73.

* Mon Mar 15 2010 Kirill A. Shutemov <kas@altlinux.org> 2.02.61-alt3
- Drop lvm2-2.02.54-alt-udev-rules.patch. udev sets property STARTUP=1
  for coldplug now.

* Fri Mar 05 2010 Kirill A. Shutemov <kas@altlinux.org> 2.02.61-alt2
- Reapply lvm2-2.02.54-alt-udev-rules.patch

* Tue Mar 02 2010 Konstantin Pavlov <thresh@altlinux.org> 2.02.61-alt1
- 2.02.61 (closes: #22939).
- Remove translated descriptions (closes: #22131).

* Tue Feb 16 2010 Dmitry V. Levin <ldv@altlinux.org> 2.02.54-alt3
- dmsetup: Placed udev rules to valid location (closes: #22968).

* Thu Dec 03 2009 Kirill A. Shutemov <kas@altlinux.org> 2.02.54-alt2
- Reenable udev synchronisation.
- Fix and cleanup requires.

* Wed Nov 18 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.02.54-alt1
- 2.02.54.
- Disabled cluster support.

* Thu Oct 15 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.02.53-alt1
- 2.02.53.
- Disable udev synchronisation.

* Thu Sep 24 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.02.52-alt2
- Enable udev synchronisation code.
- Install default udev rules for dmsetup and lvm2.

* Thu Sep 24 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.02.52-alt1
- 2.02.52.
- Introducing new subpackages:
  + dmeventd,
  + libdevmapper-event
  + libdevmapper-event-devel.
- Relocate liblvm2*.so to /%%_lib/.
- Monitor LV mirrors by default (using dmeventd).

* Fri Aug 28 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.02.51-alt1
- 2.02.51.
- Add patches from fedora:
  + Fix pvcreate on a partition (2.02.51)
  + Fix global locking in PV reporting commands (2.02.49).
- Build with liblvm2app and liblvm2cmd.

* Thu Apr 16 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.02.45-alt1
- 2.02.45.
- libdevmapper merged into lvm subtree.
- Create device-mapper devices with 0660 root:disk permissions.
- Build clvm against cman.

* Sun Nov 16 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.02.43-alt1
- 2.02.43.

* Fri Jul 11 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.02.39-alt1
- 2.02.39.
- Stricted build requires for libdevmapper-devel >= 1.02.27-alt1.

* Mon Jan 28 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.02.31-alt1
- 2.02.31.
- Stricted build requires for libdevmapper-devel >= 1.02.24-alt1.

* Tue Aug 28 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.02.28-alt1
- 2.02.28.

* Wed Jul 25 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.02.27-alt1
- 2.02.27.

* Mon Jun 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.02.26-alt1
- 2.02.26.

* Wed May 02 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.02.25-alt1
- 2.02.25.
- Stricted build requires for libdevmapper-devel >= 1.02.19-alt1.

* Sun Mar 11 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.02.23-alt1
- 2.02.23.

* Wed Feb 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.02.22-alt1
- 2.02.22.

* Sun Jan 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.02.19-alt1
- 2.02.19.
- Stricted build requires for libdevmapper-devel >= 1.02.15-alt1.

* Fri Dec 15 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.02.17-alt1
- 2.02.17.

* Sat Nov 11 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.02.14-alt1
- 2.02.14.

* Thu Oct 19 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.02.12-alt1
- 2.02.12.
- Stricted build requires for libdevmapper-devel >= 1.02.12-alt1.

* Mon Feb 06 2006 Dmitry V. Levin <ldv@altlinux.org> 2.02.01-alt2
- Removed ncurses dependencies.
- Relocated utilities to /sbin/.
- Linked lvm.static without readline and packaged it
  in separate subpackage.
- Cleaned up specfile according to ALT packaging policy.

* Mon Jan 16 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.02.01-alt1
- NMU.
- New development version.
- Added buildrequires: libdevmapper-devel-static >= 1.02.02.
- Added packager field.

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.01.14-alt1.1
- Rebuilt with libreadline.so.5.

* Wed Sep 14 2005 Anton Farygin <rider@altlinux.ru> 2.01.14-alt1
- 2.01.14

* Fri Jul 15 2005 Anton Farygin <rider@altlinux.ru> 2.01.09-alt2
- requires updated for lvmcompat package

* Fri Jun 24 2005 Anton Farygin <rider@altlinux.ru> 2.01.09-alt1
- first build for sisyphus, based on specfile from fedora project
