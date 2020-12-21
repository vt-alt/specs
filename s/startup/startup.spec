Name: startup
Version: 0.9.9.10
Release: alt1

Summary: The system startup scripts
License: GPL-2.0-or-later
Group: System/Base
BuildArch: noarch

Source: %name-%version.tar

Provides: /etc/firsttime.d
PreReq: chkconfig, gawk, grep, sed, coreutils
# due to sed -i
PreReq: sed >= 1:4.1.1
# Who could remind me where these dependencies came from?
Requires: findutils >= 0:4.0.33, mount >= 0:2.10q-ipl1mdk
Requires: procps >= 0:2.0.7-ipl5mdk, psmisc >= 0:19-ipl2mdk, util-linux >= 0:2.10q-ipl1mdk
# due to bootsplash functions
PreReq: service >= 0.5.8
# due to /sys
Requires: filesystem >= 0:2.1.7-alt1
# due to /bin/clock_unsynced
Requires: hwclock >= 1:2.14-alt1
# due to killall5 return code semantics and mountpoint utility (SysVinit >= 0:2.86-alt1)
Requires: sysvinit-utils
# due to fsck in rc.sysinit (ALT#22410)
Requires: /sbin/fsck
# due to systemd-sysctl, systemd-tmpfiles, and systemd-modules-load (see ALT#29537).
Requires: systemd-utils >= 209

# due to update_wms
Conflicts: xinitrc < 0:2.4.13-alt1
# due to gen_kernel_headers
Conflicts: kernel-headers-common < 0:1.1
# due to netfs
Conflicts: net-scripts < 0:0.5.4-alt1
# due to /sbin/setsysfont's package change
Conflicts: interactivesystem < 1:sisyphus-alt12
# due to vconfig
Conflicts: vlan-utils < 0:1.9
# due to kexec support in halt
Conflicts: sysvinit < 2.88-alt4

%description
This package contains scripts used to boot your system,
change runlevels, and shut the system down cleanly.

%prep
%setup

%install
mkdir -p %buildroot%_sysconfdir/rc.d/rc{0,1,2,3,4,5,6}.d
install -p -m644 inittab modules sysctl.conf %buildroot%_sysconfdir/
cp -a rc.d sysconfig %buildroot%_sysconfdir/

# these services do not support chkconfig:
# killall, halt, single local - Can't store symlinks in a CVS archive
ln -s ../init.d/killall %buildroot%_sysconfdir/rc.d/rc0.d/S00killall
ln -s ../init.d/killall %buildroot%_sysconfdir/rc.d/rc6.d/S00killall

ln -s ../init.d/halt %buildroot%_sysconfdir/rc.d/rc0.d/S01halt
ln -s ../init.d/halt %buildroot%_sysconfdir/rc.d/rc6.d/S01reboot

ln -s ../init.d/single %buildroot%_sysconfdir/rc.d/rc1.d/S00single

for i in `seq 2 5`; do
	ln -s ../init.d/local %buildroot%_sysconfdir/rc.d/rc$i.d/S99local
done

mkdir -p %buildroot/var/{log,run}
touch %buildroot{/etc/firsttime.flag,/var/{log/wtmp,run/utmp}}
touch %buildroot%_sysconfdir/sysconfig/{clock,i18n,system}
chmod -R +x %buildroot%_sysconfdir/rc.d
mkdir -p %buildroot%_sysconfdir/sysconfig/harddisk

mkdir -p %buildroot%_sysconfdir/firsttime.d
mkdir -p %buildroot%_localstatedir/rsbac

mkdir -p %buildroot%_localstatedir/random
touch %buildroot%_localstatedir/random/random-seed

%post
if [ $1 -eq 1 ]; then
	/sbin/chkconfig --add fbsetfont
	/sbin/chkconfig --add netfs
	/sbin/chkconfig --add random
	/sbin/chkconfig --add rawdevices
	touch /etc/firsttime.flag
fi

for f in /var/{log/wtmp,run/utmp}; do
	if [ ! -f "$f" ]; then
		:>>"$f"
		chown root:utmp "$f"
		chmod 664 "$f"
	fi
done

%preun
if [ $1 -eq 0 ]; then
	/sbin/chkconfig --del fbsetfont
	/sbin/chkconfig --del netfs
	/sbin/chkconfig --del random
	/sbin/chkconfig --del rawdevices
fi

%triggerpostun -- initscripts < 1:5.49.1-alt1
for f in %_sysconfdir/{inittab,modules,sysctl.conf,sysconfig/{clock,framebuffer,i18n,init,mouse,rawdevices,system}}; do
	if [ ! -f "$f" ]; then
	        if [ -f "$f".rpmsave ]; then
	                cp -pf "$f".rpmsave "$f"
	        elif [ -f "$f".rpmnew ]; then
	                cp -pf "$f".rpmnew "$f"
	        fi
	fi
done
/sbin/chkconfig --add fbsetfont
/sbin/chkconfig --add netfs
/sbin/chkconfig --add random
/sbin/chkconfig --add rawdevices

%triggerpostun -- startup < 0:0.2-alt1
/sbin/chkconfig --add fbsetfont

%triggerpostun -- startup < 0:0.9.3-alt1
/sbin/chkconfig --add netfs

%files
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/sysconfig/*
%config(noreplace) %_sysconfdir/inittab
%config(noreplace) %verify(not md5 size mtime) %_sysconfdir/modules
%config(noreplace) %_sysconfdir/sysctl.conf
%config(missingok) %_sysconfdir/rc.d/rc?.d/*
%dir    %_sysconfdir/rc.d/scripts
%config %_sysconfdir/rc.d/scripts/*
%config %_sysconfdir/rc.d/init.d/*
%config %_sysconfdir/rc.d/rc
%config %_sysconfdir/rc.d/rc.sysinit
%config %_sysconfdir/rc.d/rc.powerfail
%ghost %attr(664,root,utmp) /var/log/wtmp
%ghost %attr(664,root,utmp) /var/run/utmp
%ghost %config(missingok) /etc/firsttime.flag
%dir %_sysconfdir/firsttime.d
%dir %_localstatedir/rsbac
%dir %_localstatedir/random
%ghost %config(noreplace,missingok) %verify(not md5 mtime size) %attr(600,root,root) %_localstatedir/random/random-seed

%changelog
* Tue Dec 15 2020 Alexey Gladkov <legion@altlinux.ru> 0.9.9.10-alt1
- rc.sysinit:
  + Create /dev/{core,fd,stdin,stdout,stderr} symlinks if needed (ALT#39423).

* Thu Nov 28 2019 Alexey Gladkov <legion@altlinux.ru> 0.9.9.9-alt1
- rc.sysinit:
  + Remount procfs/sysfs even if these filesystems were not mounted.
  + Do not change group of /proc since it does not change anything.
- Remove creation of /etc/locale.conf.
- Remove the legacy code of migration /etc/localtime.
- Remove the legacy code of migration framebuffer_setfont.

* Wed Nov 20 2019 Alexey Gladkov <legion@altlinux.ru> 0.9.9.8-alt1
- rc.sysinit:
  + Fix regression with ignoring HOSTNAME.

* Sun Nov 17 2019 Alexey Gladkov <legion@altlinux.ru> 0.9.9.7-alt1
- rc.sysinit:
  + Add parameter for udev service.
  + Do not hardcode systemd-modules-load and optimize mount /proc.
  + Remove obsolete code that updates the /etc/mtab file.
  + Remove obsolete idetune.
  + Remove obsolete rsbac_autotune.
  + Refactor code.
- fbsetfont: Remove duplicate code

* Wed Oct 31 2018 Alexey Shabalin <shaba@altlinux.org> 0.9.9.6-alt1
- random: move random_seed from /var/run to /var/lib/random,
  because /var/run might be on tmpfs
- scripts/cleanup: run systemd-tmpfiles --create
  before touch /var/run/utmp and /var/run/utmpx

* Fri Apr 18 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.9.5-alt1.2
- inittab: don't run getty on tty1 only when runlevel 5 (closes: #29960)

* Wed Apr 09 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.9.5-alt1.1
- inittab: don't run getty on tty1

* Sun Mar 23 2014 Dmitry V. Levin <ldv@altlinux.org> 0.9.9.5-alt1
- scripts/cleanup: pass --boot to systemd-tmpfiles --remove --create
  (once more closes: #29537)

* Wed Mar 19 2014 Dmitry V. Levin <ldv@altlinux.org> 0.9.9.4-alt1
- rc.sysinit: remount /proc and /sys.

* Fri Jan 17 2014 Dmitry V. Levin <ldv@altlinux.org> 0.9.9.3-alt1
- rc.sysinit: determine selinuxfs mountpoint at runtime.
- init.d/netfs: added glusterfs support
  (by Danil Mikhailov; closes: #29304).

* Wed Nov 06 2013 Dmitry V. Levin <ldv@altlinux.org> 0.9.9.2-alt1
- scripts/cleanup: pass --remove --exclude-prefix=/dev
  to systemd-tmpfiles (closes: #29537).

* Wed May 29 2013 Dmitry V. Levin <ldv@altlinux.org> 0.9.9.1-alt1
- raidstop: skip root device in case of partitioned raid (closes: #29027).
- scripts/cleanup: do not create x11 directories, rely on
  tmpfiles.d/x11.conf instead.

* Mon May 27 2013 Dmitry V. Levin <ldv@altlinux.org> 0.9.9.0-alt1
- rc.sysinit:
  + added sysctl.d support using systemd-sysctl (closes: #20938);
  + added modules-load.d support using systemd-modules-load;
  + added tmpfiles.d support using systemd-tmpfiles.
- scripts/lang: added /etc/locale.conf support (closes: #28525).

* Wed Feb 06 2013 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.38-alt1
- rc.sysinit: hide plymouth when appropriate (closes: #28515).

* Wed Jan 09 2013 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.37-alt1
- Fixed /etc/firsttime.d support (closes: #28308).

* Thu Nov 01 2012 Timur Aitov <timonbl4@altlinux.org> 0.9.8.36-alt1
- rc.sysinit: activate encrypted block devices.
- init.d/halt: turn off encrypted block devices.

* Fri Jul 27 2012 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.35-alt1
- init.d/clock: changed to use tzupdate from tzdata >= 2012d-alt2.

* Tue Jun 19 2012 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.34-alt1
- scripts/first_time: cleaned up antediluvian mess.

* Wed Jun 13 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.8.33-alt1
- init.d/halt: pass -k to halt for kexec support

* Wed May 16 2012 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.32-alt1
- init.d/local: exit 0 in the end (by glebfm@).
- sysconfig/mouse: update device name (by glebfm@; closes: #25110).
- init.d/netfs (start): do not start without routing (closes: #27303).

* Wed Oct 05 2011 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.31-alt1
- rc.sysinit: do not check the root filesystem when it is already
  mounted in read-write mode.
- init.d/halt: added $INIT_HALT support (closes: #26391).
- init.d/halt: do not unmount devtmpfs (closes: #26416).
- Added /etc/sysconfig/halt file (closes: #25905).

* Tue Nov 09 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.30-alt1
- init.d/netfs: do not start portmap (closes: #24517).

* Tue Nov 02 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.29-alt1
- rc.sysinit: run setsysfont only once, at the point where everything
  mountable should be already mounted (closes: #24070).

* Fri Aug 27 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.28-alt1
- Added dependence on /sbin/fsck (closes: #22410).
- init.d/rawdevices: turned off by default
  (by Michael Shigorin; closes: #10906).
- rc.sysinit:
  + Disable update of /etc/mtab when the latter is a symlink
    (by Alexey I. Froloff; closes: #23133).
  + No longer try to mount already mounted /proc and /sys
    (closes: #23660).
  + Disable USEMODULES when /sbin/modprobe is not available,
    thus removed hard dependence on module-init-tools
    (closes: #11033).
  + Refactored automatic reboot.
  + Added SELinux support
    (by Mikhail Efremov and me).
- init.d/halt:
  + Made halt action configurable, default remains unchanged
    (by Sergey Y. Afonin and me; closes: #10326).
  + Reworked unmounting of virtual filesystems so that /proc, /sys,
    /dev and any usbfs inside /dev are nor longer unmounted
    (closes: #11888, #22118).

* Mon Nov 16 2009 Kirill A. Shutemov <kas@altlinux.org> 0.9.8.27-alt1
- sysctl.conf: Set "vm.mmap_min_addr = 32768" if arch isn't ia64 ppc64
  or x86
- startup package isn't noarch any more

* Wed Sep 30 2009 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.26-alt1
- rc.sysinit: Removed creation of /mnt/cdrom and /mnt/floppy (Led).
- scripts/lvm_start: Pass --mknodes to vgscan (Eugene Ostapets; closes: ALT#21492)

* Wed Sep 30 2009 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.25-alt1
- rc.sysinit: Detect USEMODULES by /proc/modules only (Led; closes: #21738).

* Fri Sep 25 2009 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.24-alt1
- scripts/multipath_stop: Made output less noisy (Konstantin Pavlov).

* Thu Sep 03 2009 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.23-alt1
- Added multipath devices support (Konstantin Pavlov; closes: #21385).

* Mon Aug 17 2009 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.22-alt1
- rc.d/init.d/clock, sysconfig/clock: Introduced
  HWCLOCK_SET_TIME_AT_START (closes: #19787).
- sysctl.conf: Added "vm.mmap_min_addr = 65536".

* Mon Dec 29 2008 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.21-alt1
- scripts/cleanup: Fixed /var cleanup (closes: #16647).
- rc.sysinit: Turned /etc/HOSTNAME into symlink to /proc/sys/kernel/hostname.

* Sun Aug 03 2008 Alexey Gladkov <legion@altlinux.ru> 0.9.8.20-alt1
- Remove "FAST" parameter since hwclock from util-linux
  does not have --fast option.

* Thu Apr 24 2008 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.19-alt1
- rc.sysinit:
  + Unlink /dev/mapper/control iff it is going to be re-created right away.
- init.d/halt:
  + Pass -f option to halt.
- Require sysvinit-utils instead of versioned SysVinit.

* Tue Feb 05 2008 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.18-alt1
- init.d/clock:
  + Added "FAST" parameter (solo, #13633).
- rc.sysinit:
  + Added support for custom hostname resolver (inger).
- sysconfig/init:
  + Documented REMOUNT_ROOTFS_RW_COMMAND and RESOLVE_HOSTNAME_COMMAND (inger).

* Thu Aug 09 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.17-alt1
- rc.sysinit: Added cifs to network fs list (#12140).

* Tue May 22 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.16-alt1
- rc.sysinit: Moved bootsplash activation after udevd start (zerg, #11866).

* Mon May 21 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.15-alt1
- rc.sysinit: Parametrized remounting root filesystem (#11806).

* Sun Apr 22 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.14-alt1
- init.d/netfs: Added nfs4 support (#11593).

* Wed Apr 11 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.13-alt1
- lvm_stop: Do not execute vgchange if /proc/partitions contains no dm devices.

* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.12-alt1
- rc.sysinit: Load modules before udevd start (legion, #11085).

* Wed Mar 14 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.11-alt1
- init.d/rawdevices:
  Changed to exit not only when /etc/sysconfig/rawdevices is
  missing or empty but also when it does not contain data.
- inittab: Added --noclear option to "mingetty tty1".

* Tue Feb 20 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.10-alt1
- rc.sysinit:
  + Do not set kernel.{modprobe,hotplug} if udevd is running (vsu@).
  + Add /dev/shm to mtab if it was mounted early (vsu@).

* Fri Feb 16 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.9-alt1
- rc.sysinit:
  + Dropped ISA PNP support
  + Dropped devfs support.
  + Implemented udev early startup (legion@).
- init.d/halt:
  + Dropped devfs support.
  + Chaged unmount sequence to unmount /dev late.

* Thu Feb 01 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.8-alt1
- rc.sysinit: Removed st module loading support.
- /etc/rc.d/scripts/vconfig-update: Removed.

* Tue Jan 16 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.7-alt1
- init.d/halt: Make shutdown up to 5 seconds faster.

* Mon Dec 04 2006 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.6-alt1
- init.d/halt: Pass "off" argument to accton (#10063).
- raidstop: Fix /proc/mdstat check.
- rc.sysinit: If sysfs is mounted, add /sys to mtab.
- rc.sysinit: Add "-O no_netdev" to "mount -a" invocations (#10349).
- raidstop: Skip root device (#6614).
- rc.sysinit: Add proper /proc/bus/usb entry to mtab when usbfs is mounted.
- Move LVM support code to separate scripts (#6526, #6614, #7399, #10117).
- raidstart: Fix /etc/mdadm.conf and /etc/raidtab checks.
- raidstart: Cleanup.

* Fri Aug 11 2006 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.5-alt1
- rc.sysinit:
  + Make sysfs mount logic based on /proc/filesystems.
  + Enhanced RAID-related failures handling,
    based on patch from Ilya Evseev (#9488).
- sysctl.conf:
  + Set "kernel.core_pattern = /dev/null" by default,
    suggested by Michael Shigorin (#9780).
- init.d/clock:
  + Add status parameter, suggested by Vitaly Lipatov (#8718).
- init.d/halt, scripts/raidstop:
  + Use new scripts/raidstop file to stop RAID using mdadm
    or raidtools, based on patch from Ilya Evseev (#7768).

* Thu Dec 08 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.4-alt1
- init.d/halt:
  + Unmount non-/dev tmpfs filesystems before deactivating swap.
- scripts/cleanup:
  + Shutup /tmp cleanup script.

* Fri Oct 07 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.3-alt1
- rc.sysinit: Do not run depmod in fastboot mode (#8130).

* Sat Jun 11 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.2-alt1
- init.d/clock:
  + in "stop" mode, do not set hwclock if clock is in synced mode.

* Fri May 27 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.8.1-alt1
- rc.sysinit: Ignore unfilled /etc/mdadm.conf and /etc/raidtab.

* Tue May 24 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.8-alt1
- rc.d/scripts/raidstart: new file.
- rc.sysinit: added mdadm support (#6397).
- sysconfig/mouse: added default settings.

* Mon Apr  4 2005 Ivan Zakharyaschev <imz@altlinux.ru> 0.9.7-alt1
- Moved console-related files to console-common-scripts package:
  /sbin/setsysfont, %_sysconfdir/sysconfig/console/setterm, 
  %_sysconfdir/sysconfig/keyboard
  (no extra dependency on console-common-scripts required, it belongs 
  to interactivesystem).

* Sun Apr 03 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.6.1-alt1
- rc.sysinit: reverted previous change.

* Fri Apr 01 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.6-alt1
- rc.sysinit: do not pass "-a" option to fsck(8), "-y" is enough.

* Tue Mar 22 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.5.1-alt1
- Additional bootsplash tweaks (#6299, #6300).

* Mon Mar 21 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.5-alt1
- Initial bootsplash support, based on patch from Rider (#6274).

* Thu Mar 17 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.4-alt1
- inittab: added runlevel for install3.

* Wed Mar 09 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.3-alt1
- vconfig-update: do not produce dangling symlink (closes #6146).
- rc.sysinit:
  + do not create /mnt/disk (closes #6166);
  + extended list of non-local filesystems (closes #3403).
- sysconfig/clock: set UTC=true by default.
- init.d/netfs: moved from net-scripts back to this package (closes #5857).
- sysctl.conf: moved net.ipv4 options to separate config file (closes #5857).
- inittab: commented out execution of /sbin/update.

* Sun Oct 03 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.2-alt1
- rc.sysinit:
  + enhanced LVM support, based on patch from Vladimir Kholmanov.
- scripts/cleanup:
  + recreate some directories in /tmp/ with proper permissions.

* Mon Aug 09 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.1-alt1
- scripts/vconfig-update: do nothing if /etc/alternatives
  directory doesn't exist.

* Wed May 26 2004 Dmitry V. Levin <ldv@altlinux.org> 0.9.0-alt1
- Removed scripts: init.d/ieee1394, init.d/usb.

* Wed May 26 2004 Dmitry V. Levin <ldv@altlinux.org> 0.8.4-alt1
- init.d/fbsetfont: fixed (#3120).
- sysconfig/clock: added missing desriptions (#3496).

* Sat Feb 07 2004 Dmitry V. Levin <ldv@altlinux.org> 0.8.3-alt1
- Requires: filesystem >= 0:2.1.7-alt1 (due to /sys).
- rc.d/rc.sysinit:
  + mount /sys where appropriate;
  + use "swapon -a -e" to activate swap partitions (#3781);
  + removed support for obsolete /lib/modules/default;
  + removed support for obsolete /boot/System.map;
  + added evms support (#3647).
- init.d/halt:
  + added nut support (#3701).
- sysctl.conf:
  + removed net.ipv4.ip_always_defrag key.

* Thu Jan 29 2004 Dmitry V. Levin <ldv@altlinux.org> 0.8.2-alt1
- rc.d/rc.sysinit: do not initialize console powersaver so early.
- setsysfont: source /etc/sysconfig/consolefont.

* Sun Jan 18 2004 Dmitry V. Levin <ldv@altlinux.org> 0.8.1-alt1
- sysctl.conf: fixed comment for net.ipv4.tcp_timestamps,
  thanks to Solar for the hint.
- Packaged as noarch (#3407).

* Wed Dec 24 2003 Dmitry V. Levin <ldv@altlinux.org> 0.8-alt1
- rc.sysinit:
  + removed old bits of linuxconf support;
  + enhanced USEMODULES support.

* Sun Oct 26 2003 Dmitry V. Levin <ldv@altlinux.org> 0.7-alt1
- %_sysconfdir/adjtime: relocated to hwclock package.
- scripts/indexhtml_update: relocated to indexhtml package.
- scripts/first_time:
  + moved menu support to menu package;
  + moved index.html support to indexhtml package;
  + moved aumix support to aumix-minimal package;
  + moved mozilla support to mozilla packages.
- init.d/clock:
  + check for /etc/localtime before 'clock start';
  + try to set timezone if not set.
  + new mode: tzset.
- rc.d/rc.sysinit:
  When /etc/adjtime is present and non-empty, run
  "clock start" after root filesystem is mounted read-write.

* Thu Oct 16 2003 Dmitry V. Levin <ldv@altlinux.org> 0.6-alt1
- init.d/ieee1394: new script (rider).
- scripts/first_time: removed kudzu call (rider).

* Tue Jun 03 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5-alt1
- init.d/*: fixed lockfiles handling.
- init.d/killall: if first argument is not "start", exit.

* Wed May 28 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4-alt1
- Added firsttime.d support (#0002287).

* Sun May 25 2003 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- init.d/fbsetfont: fixed tty initialization.

* Wed May 21 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Relocated scripts/framebuffer_setfont -> init.d/fbsetfont.
- Removed framebuffer_setfont entry from inittab.
- Dropped gen_kernel_headers in favour of adjust_kernel_headers.
- Removed update_wms and gen_kernel_headers calls from rc.sysinit.

* Mon May 12 2003 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- rc.sysinit:
  + removed (never used) devfs initialization code;
  + fixed ROOTFSTYPE initialization.
- init.d/halt: call poweroff in halt mode by default.
- scripts/indexhtml_update: use subst instead of perl.
- setsysfont: use absolute() to find path.
- scripts/lang: rewritten.
- everywhere:
  + use new functions from service package;
  + set WITHOUT_RC_COMPAT=1 .

* Wed Apr 23 2003 Dmitry V. Levin <ldv@altlinux.org> 0.0.2-alt1
- Relocated %_sysconfdir/rc?.d and %_sysconfdir/rc.d/rc?.d
  from this package to service package.

* Mon Apr 21 2003 Dmitry V. Levin <ldv@altlinux.org> 0.0.1-alt1
- Removed all service and networking code and packaged them separately.
- Renamed to startup.

* Sat Apr 19 2003 Dmitry V. Levin <ldv@altlinux.org> 5.49-ipl54mdk
- %_initdir/sound: don't sort aliases in LoadModule (#0001802).
- %_initdir/clock: test $HWCLOCK_ADJUST also for "true" value (#0002351).
- %_initdir/functions:
  + fixed check logic in daemon() a bit (#0002407).
  + fixed return code in killproc() (#0002412).
- %_initdir/outformat: check argumnets being passed to tput (#0002450).
- /etc/sysctl.conf:
  + set "net.ipv4.icmp_echo_ignore_broadcasts = 1" by default (#0002472);
  + added comments from Owl's sysctl.conf file.
- usernetctl: support variable definitions quoted with single quotes.
