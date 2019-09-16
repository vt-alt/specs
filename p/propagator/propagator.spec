%def_with cifs
%def_with shell
%def_with splash

Name: propagator
Version: 20190829
Release: alt1

Summary: 'Early userspace' set of binaries
License: GPL
Group: System/Kernel and hardware

Url: http://altlinux.org/propagator
Source: %name-%version-%release.tar

BuildRequires: libnewt-devel-static libslang2-devel-static

%description
%name is a set of binaries useful in 'early userspace' environment,
including init and various helpers for hw probing and bootstrapping.

%prep
%setup

%build
%make_build \
	%{?_with_cifs:WITH_CIFS=t} \
	%{?_with_shell:WITH_SHELL=t} \
	%{?_with_splash:WITH_SPLASH=t} \
	version=%version-%release \
	libdir=%_libdir

%install
%makeinstall_std libdir=%_libdir

%files
%_bindir/gencpio
%_bindir/mkmodpack
%_sbindir/propagator

%changelog
* Thu Aug 29 2019 Evgeny Sinelnikov <sin@altlinux.org> 20190829-alt1
- fix hangs until http socket not closed on server side (closes: #37150)
- tools.c: break reading cycle if we actually loaded program into memory
- url.c, network.c: disable keep-alive and close http socket after downloading

* Thu Apr 18 2019 Sergey V Turchin <zerg@altlinux.org> 20190418-alt1
- compile with _FILE_OFFSET_BITS=64

* Sat Nov 17 2018 Leonid Krivoshein <klark@altlinux.org> 20181117-alt1
- probing.c: added support for SD-cards when boot in LiveCD-mode

* Wed Aug 22 2018 Evgeny Sinelnikov <sin@altlinux.org> 20180822-alt1
- add support cifs install method
- replace HTTP request version from 1.0 to 1.1
- increase DHCP tries and timeouts for DISCOVER request

* Wed Jun 06 2018 Arseny Maslennikov <arseny@altlinux.org> 20180606-alt1
- dhcp.c: Remove temporary default route properly (altbug:#34347).
- dhcp.c: Provide DHCP vendor class identifier in requests (altbug:#34320).

* Mon Apr 23 2018 Leonid Krivoshein <klark@altlinux.org> 20180423-alt1
- New udev control logic imported from make-initrd scripts.
- Udev-trigger replaced to udev-settle() in hardware wait loops.
- All udev control code moved from init.c to new udev.c module.
- Lazy initialization mode support added for work in cooperate
  with make-initrd: this is experimental future, turned off by
  default, and also required patched make-initrd-propagator.
- disk.c, cdrom.c: 15 attempts with udev-settle() calls.
- network.c: bridge up algorithm reviewed, fixed memory leaks.
- network.c: 15 attempts to select and wait network interface;
- probing.c, probing.h, dhcp.c: small fixes, now black list used.
- modules_descr.h, stage1.c: deprecated header, unused code removed.
- dhcp.c: fix potentially destructive typo (closes: #34322),
  thanks to Arseny Maslennikov <arseny@altlinux.org>.
- Workaround race conditions during disks detection (closes: #30315).
- Workaround race conditions during bridging up network interfaces,
  see: https://bugzilla.altlinux.org/show_bug.cgi?id=34347 and
  https://lists.altlinux.org/pipermail/sysadmins/2018-April/date.html
  (about "No network Devices found" error message).
- Multiple small code improvements, fixes for avoid memory leaks
  and suppress compiler warnings.

* Fri Dec 08 2017 Mikhail Efremov <sem@altlinux.org> 20171208-alt1
- probing.c: added support for MMC devices when boot in LiveCD-mode
  (by Leonid Krivoshein).
- cdrom.c: fixed implicit declaration of function opendir warning
  (by Leonid Krivoshein).
- disk.c: Workaround race conditions during disks detection
  (closes: #30315).
- cdrom.c, network.c, tools.c: Fix memory leaks.
- tools.c: Don't do useless comparisons during cmdline processing.
- Use ramdisk_size from kernel cmdline.
- Check that RAM size is enough for ramdisk.

* Thu May 11 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 20170511-alt1
- Fixed errors found by cppcheck.

* Sat Mar 18 2017 Michael Shigorin <mike@altlinux.org> 20170318-alt1
- tools.c: why on Earth make *that* a nested function??

* Mon Dec 26 2016 Michael Shigorin <mike@altlinux.org> 20161226-alt1
- probing.c: bump max disk number from 50 to 250 (closes: #32934)

* Mon Oct 24 2016 Michael Shigorin <mike@altlinux.org> 20161024-alt2
- disk.c: retry uuid/label based autodetection upon a pause
  if the first attempt has failed (e.g. flash not ready yet)

* Mon Oct 24 2016 Michael Shigorin <mike@altlinux.org> 20161024-alt1
- probing.c: load uas module too

* Fri May 20 2016 Michael Shigorin <mike@altlinux.org> 20160516-alt1
- use spawn to run udevadm (legion@; see also #32068)

* Tue Nov 03 2015 Michael Shigorin <mike@altlinux.org> 20151103-alt1
- modules.c: silence modprobe (some could be compiled in at times)

* Tue Mar 10 2015 Michael Shigorin <mike@altlinux.org> 20150310-alt1
- cdrom.c, disk.c: poke lazy udev to do its job while waiting for disk
  (#30315 again)

* Fri Mar 06 2015 Michael Shigorin <mike@altlinux.org> 20150306-alt1
- cdrom.c: fix pointer arithmetics (ldv@)

* Fri Feb 27 2015 Michael Shigorin <mike@altlinux.org> 20150227-alt1
- cdrom.c: minor fixup for "1, 2, 1 seconds" visual effect
- disk.c: slightly better "help me find my media" message
- probing.c: ensure sd_mod along with usb_storage

* Wed Dec 17 2014 Michael Shigorin <mike@altlinux.org> 20141217-alt1
- ldv@'s workaround for media detection race condition (closes: #30315)

* Fri Aug 15 2014 Michael Shigorin <mike@altlinux.org> 20140815-alt1
- drop /proc/sys/kernel/hotplug check (OBSOLETE)

* Wed Apr 23 2014 Michael Shigorin <mike@altlinux.org> 20140423-alt1
- digest check refactoring (ldv@)

* Sat Apr 19 2014 Michael Shigorin <mike@altlinux.org> 20140419-alt1
- initial stage2 digest check

* Mon Apr 14 2014 Michael Shigorin <mike@altlinux.org> 20140414-alt1
- optimize filesystem probing order (iso9660 first, ntfs last)

* Wed Nov 06 2013 Michael Shigorin <mike@altlinux.org> 20130822-alt2
- rebuilt for Sisyphus

* Thu Aug 22 2013 Led <led@altlinux.ru> 20130822-alt1
- don't panic of mkdir(2) if directory already exist
- init: fix trying mount devtmpfs into /dev
- support build with MUSL

* Wed Aug 21 2013 Fr. Br. George <george@altlinux.ru> 20130821-alt1
- switch back to nfsmount (mount.nfs fails on NFSv3)

* Tue Jul 16 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130716-alt1
- ext4 support added

* Sat Mar 16 2013 Michael Shigorin <mike@altlinux.org> 20130316-alt1
- cdrom: probe sda1 before sda (see also #28289)

* Thu Feb 21 2013 Michael Shigorin <mike@altlinux.org> 20130315-alt1
- complete the /bin/plymouth existence check started in 20101130-alt6

* Thu Feb 14 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130314-alt1
- rewrite net devices probing

* Fri Nov 09 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20121109-alt1
- use /sbun/mount.nfs instead of /bin/nfsmount

* Mon Oct 15 2012 Michael Shigorin <mike@altlinux.org> 20101130-alt20
- kmod-10 still does, remade the workaround as a longer term one

* Tue Oct 02 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20121002-alt1
- no more initfs

* Mon Aug 13 2012 Michael Shigorin <mike@altlinux.org> 20101130-alt19
- modprobe suddenly wants modules.dep.bin to exist

* Fri Aug 10 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20101130-alt18
- modprobe --list changed to find

* Mon May 28 2012 Mikhail Efremov <sem@altlinux.org> 20101130-alt17
- init: Use devtmpfs for /dev if possible.

* Sat Mar 17 2012 Michael Shigorin <mike@altlinux.org> 20101130-alt16
- added an Url:
- minor spec cleanup

* Mon Mar 12 2012 Michael Shigorin <mike@altlinux.org> 20101130-alt15
- rebuilt for Sisyphus

* Fri Feb 10 2012 Mykola Grechukh <gns@altlinux.ru> 20101130-alt14.hybrid1
- simplifed handling of hybrid disk images

* Wed Feb 08 2012 Mykola Grechukh <gns@altlinux.ru> 20101130-alt14
- merged mkmodpack's .xz support

* Mon Dec 19 2011 Michael Shigorin <mike@altlinux.org> 20101130-alt13
- tweaked usb_storage wait to avoid the needlessly requisite one

* Fri Dec 16 2011 Michael Shigorin <mike@altlinux.org> 20101130-alt12
- fixed the fd leak introduced in previous release (thanks ldv@)

* Fri Dec 16 2011 Michael Shigorin <mike@altlinux.org> 20101130-alt11
- reworked usb_storage wait to use ten second intervals
  instead of a ten second one

* Fri Dec 16 2011 Michael Shigorin <mike@altlinux.org> 20101130-alt10
- tweaked cdrom support to allow for isohybrid usbflash images too
  (loosely based on mandriva svn's implementation by cfergeau)

* Fri Jun 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20101130-alt9
- completely broken memory calculation code deleted: we are lucky

* Wed Dec 22 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20101130-alt8
- run plymouth on tty5

* Tue Dec 21 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20101130-alt7
- tell plymouth to exit if automatic fails

* Fri Dec 10 2010 Anton Farygin <rider@altlinux.ru> 20101130-alt6
- check /bin/plymouth before exec in init

* Mon Dec 06 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 20101130-alt5
- disable plymouth if splash parameter not in cmdline (by rider@)

* Wed Dec 01 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20101130-alt4
- telling plymouth about rootfs change added
- run udevd with --resolve-names=never

* Wed Dec 01 2010 Anton Farygin <rider@altlinux.ru> 20101130-alt3
- add nosplash command for disable plymouth

* Wed Dec 01 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20101130-alt2
- spawning plymouth fixed

* Tue Nov 30 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20101130-alt1
- plymouth support added
- bootsplash support removed
- additionaly packaged init separatly from initfs

* Sat Nov 20 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20090301-alt14
- waiting for /dev/disk added, waiting ttys fixed

* Fri Nov 19 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20090301-alt13.1
- silly bug in waiting fixed

* Thu Nov 18 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20090301-alt13
- Wait for tty[23]. It seems that is also fixes drives detection on el-smp

* Wed Nov 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20090301-alt12
- support for using glob patterns in disk label added
  (like authomatic=method:disk,label:ALT*)

* Fri Sep 24 2010 Mykola Grechukh <gns@altlinux.ru> 20090301-alt11
- ext3 added

* Thu Jul  1 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 20090301-alt10
- ensure that /lib/firmware exists in resulting initramfs image

* Thu Jun  3 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 20090301-alt9
- recognize infiniband ifaces as network ones

* Wed May 26 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 20090301-alt8
- iso9660 filesystem support added (boyarsh@)

* Thu Apr  1 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 20090301-alt7
- mkmodpack: fixed firmware extraction resident in own directory

* Wed Sep  9 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 20090301-alt6
- workaround for (#21416)

* Wed Jul 29 2009 Nick S. Grechukh <gns@altlinux.org> 20090301-alt5
- build fixed

* Mon Jul  6 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 20090301-alt4
- run hooks, namely /sbin/init-{top,premount,bottom}, if exist
- use init= kernel cmdline parameter, if supplied (stanv@)

* Thu Jun 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 20090301-alt3
- add /lib/firmware/<kernel version> to fw search paths (#20583)

* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 20090301-alt2
- rebuilt against new newt library

* Fri Mar 13 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 20090301-alt1
- try all interfaces in turn, when no `interface' parm supplied (slazav@)

* Mon Dec 15 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 20080301-alt11
- replace busybox by /bin/sh from klibc in initramfs
- add [u]mount utilities from klibc in initramfs

* Wed Nov 12 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 20080301-alt10
- bring networking up, if requested by auto "network" param, regardless of method

* Mon Nov  3 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 20080301-alt9
- fixed build on recent toolchain

* Wed Sep  3 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 20080301-alt8
- adapted for recent udev

* Thu Jun 12 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 20080301-alt7
- rebuilt with recent udev

* Thu May 22 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 20080301-alt6
- unblock SIGIGN/SIGTSTP right before exec'ing secondary init (#15757)

* Thu May  8 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 20080301-alt5
- added ability to mount disk with 2nd stage by label or uuid (#15561)

* Wed Apr 16 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 20080301-alt4
- media scan delayed for devices, handled by usb-storage (#15348)
- add capability to boot directly from cd (folder with root fs) (stanv@)

* Tue Mar 18 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 20080301-alt3
- iso-on-nfs, iso-on-disk: stop trying to pass initial mountpoint
  with iso image to 2nd stage, there's no point for this

* Sun Mar 16 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 20080301-alt2
- fixed for x86_64

* Sat Mar  1 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 20080301-alt1
- use udev in 1st installer stage from now
- unchangeable part of initramfs prepared and packaged
- mkmodpack utility added

* Wed Aug  8 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 20070301-alt7
- do not show %name build date on tty1, closes \#12491

* Thu Aug  2 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 20070301-alt6
- use version string everywhere in user dialogs, closes \#12444
- added support for noload=module command line (boyarsh@)

* Wed Jul 18 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 20070301-alt5
- fixed crash when splashcount used, closes \#12365

* Fri May 25 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 20070301-alt4
- spawn animated splash, if possible

* Wed Apr 18 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 20070301-alt3
- do not warn user after insmod'ing already existing module, closes \#11549

* Thu Apr 12 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 20070301-alt2
- fixed env passing to 2nd stage

* Fri Mar 16 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 20070301-alt1
- switch to glibc, thanks to gns@
- redo block device probing, based on sysfs
- cleaned up

* Thu Nov 23 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 20061123-alt1
- added conditional shell spawning
- fixed probing of some RAID adaptors
- probe usbhid early
- one full-featured stage1 binary

* Tue Jan 24 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 20060124-alt1
- added tweaks for nForce nics

* Fri Oct 28 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 20051028-alt1
- modified init to pass given argv further

* Fri Aug 19 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 20050819-alt1
- modified IDE probing to use ide-generic if search in pcitable fails

* Thu Jul 07 2005 Anton D. Kachalov <mouse@altlinux.org> 20050707-alt1
- multilib support

* Tue Jul 05 2005 Anton Farygin <rider@altlinux.ru> 20050705-alt1
- export DNS_SERVER and DNS_SERVER2 for stage2

* Sat May 14 2005 Anton Farygin <rider@altlinux.ru> 20050514-alt1
- stage1 now may be used as modprobe (only modprobe -q -- <modulename> format supported)
- gencpio updated from 2.6.11 kernel with symlinks support

* Mon Apr 20 2005 Anton Farygin <rider@altlinux.ru> 20050420-alt1
- added splash update support

* Tue Apr 12 2005 Anton Farygin <rider@altlinux.ru> 20050412-alt1
- use squashfs for stage2 and live system

* Wed Mar 30 2005 Anton Farygin <rider@altlinux.ru> 20050330-alt1
- use ext2 filesystem for stage2

* Sat Mar  5 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 20050305-alt1
- usb cdrom/flash now supported
- ntfs added

* Wed Feb 16 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 20050216-alt1
- adopted for modularized IDE

* Tue Feb  8 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 20050208-alt1
- snapshot @ 20050208

* Fri Dec 17 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 20041215-alt0.2
- gencpio utility added

* Wed Dec 15 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 20041215-alt0.1
- snapshot @ 20041215

* Fri Nov 12 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 20041112-alt0.1
- Initial build.
