Name: startup-rescue
Version: 0.32
Release: alt4

Summary: The system startup scripts for rescue disk
License: GPL
Group: System/Base

Url: http://en.altlinux.org/rescue
Source: rescue-%version.tar
Packager: Anton V. Boyarshinov <boyarsh@altlinux.ru>

Requires(post): %post_service
Requires(preun): %preun_service
Requires: sfdisk console-vt-tools libshell system-report

# Weird kludge
Provides: /sbin/find-fstab

# Optional requires
%ifarch %ix86 x86_64
Requires: dmidecode ddcprobe
%endif
Requires: altquire
Requires: agetty

# /sbin/rescue-launcher is optional too
%filter_from_requires /rescue\-launcher/d

Conflicts: startup-school-rescue startup-nanolive

%description
This package contains scripts used to boot your system from rescue disk.

%prep
%setup -n rescue-%version

%install
mkdir -p -- %buildroot{%_bindir,/sbin,%_initdir}

install -pm755 rescue-shell %buildroot%_bindir/
%ifarch %ix86 x86_64
install -pm755 fixmbr %buildroot/sbin/
%endif
install -pm755 find-fstab %buildroot/sbin/
install -pm755 mount-fstab mount-system %buildroot/sbin/
install -pm644 inittab.rescue mdadm-ro.conf %buildroot/etc/
install -pm755 rc.sysinit.rescue %buildroot/etc/rc.d/
install -pm755 sysreport.init %buildroot%_initdir/sysreport
install -pm755 rescue-remote.init %buildroot%_initdir/rescue-remote

%post
%post_service rescue-remote

%preun
%preun_service rescue-remote

%files
/sbin/*
%_bindir/*
/etc/mdadm-ro.conf
/etc/inittab.rescue
/etc/rc.d/rc.sysinit.rescue
%_initdir/sysreport
%_initdir/rescue-remote

%changelog
* Sat Feb 15 2020 Anton Midyukov <antohami@altlinux.org> 0.32-alt4
- Fixed DHCP timeout (closes: 38089)

* Mon Nov 18 2019 Alexey Gladkov <legion@altlinux.ru> 0.32-alt3
- Make idetune optional.

* Tue Jul 09 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.32-alt2
- Package find-fstab script regardless of architecture.

* Sun Jan 06 2019 Anton Midyukov <antohami@altlinux.org> 0.32-alt1
- support tmpfiles.d

* Tue Dec 04 2018 Leonid Krivoshein <klark@altlinux.org> 0.31-alt1
- optional feature added: autorun on the first terminal

* Mon Oct 15 2018 Michael Shigorin <mike@altlinux.org> 0.30-alt1
- support overlayfs too

* Mon Jul 16 2018 Anton Midyukov <antohami@altlinux.org> 0.29-alt2
- package not noarch

* Mon May 21 2018 Michael Shigorin <mike@altlinux.org> 0.29-alt1
- restrict dmidecode, ddcprobe and fixmbr to x86
- hackaround for suddenly "missing" /sbin/find-fstab self-dependency

* Tue Jan 24 2017 Michael Shigorin <mike@altlinux.org> 0.28-alt1
- stop plymouth

* Thu Sep 08 2016 Michael Shigorin <mike@altlinux.org> 0.27-alt1
- decouple LVM/MDRAID handling

* Tue Sep 06 2016 Michael Shigorin <mike@altlinux.org> 0.26-alt1
- disable MDRAID/LVM-related udev rules in forensics mode

* Tue Nov 10 2015 Michael Shigorin <mike@altlinux.org> 0.25-alt1
- bump DHCP timeout to 35 so STP isn't a problem

* Mon Jun 01 2015 Michael Shigorin <mike@altlinux.org> 0.24-alt1
- added rescue-remote initscript
- eliminated mdadm.conf spam (shows up during multiple live_rw boots)

* Mon May 12 2014 Michael Shigorin <mike@altlinux.org> 0.23-alt1
- moved *-forensic into a standalone package

* Mon May 12 2014 Michael Shigorin <mike@altlinux.org> 0.22-alt1
- mount-forensic: minor fixes

* Wed May 07 2014 Michael Shigorin <mike@altlinux.org> 0.21-alt1
- added lvm2-forensic, raid-forensic scripts to help deal with
  guaranteed read-only LVM2/MDRAID setups (blockdev --setro
  might be not enough in some cases); thanks Maxim Suhanov again
- added Conflicts:

* Sat Apr 19 2014 Michael Shigorin <mike@altlinux.org> 0.20-alt1
- mount-fstab: do not skip /boot/efi
- added mount-forensic script by Maxim Suhanov

* Wed Apr 16 2014 Michael Shigorin <mike@altlinux.org> 0.19-alt1
- rescue-shell: propose read-only mdraid assembly
- added an Url:

* Tue Apr 15 2014 Michael Shigorin <mike@altlinux.org> 0.18-alt1
- find-fstab: *fix* forensic mode support (invert condition)
- improve user interaction too

* Mon Apr 14 2014 Michael Shigorin <mike@altlinux.org> 0.17-alt1
- forensic mode support:
  + boot process will not auto-assemble mdraid
    or auto-activate discovered swap partitions
  + mount-system will mount filesystems as "ro,loop"
  + rescue-shell tips adjusted appropriately

* Sun Apr 13 2014 Michael Shigorin <mike@altlinux.org> 0.16-alt1
- extended user advice

* Tue Nov 26 2013 Michael Shigorin <mike@altlinux.org> 0.15-alt1
- avoid remounting sysfs
- try activating lvm volumes before mounting filesystems (closes: #28631)

* Wed Oct 17 2012 Michael Shigorin <mike@altlinux.org> 0.14-alt1
- avoid aufs-over-aufs

* Fri Dec 24 2010 Anton Protopopov <aspsk@altlinux.org> 0.13-alt1
- add --grub option, use it by default

* Thu Dec 23 2010 Anton Protopopov <aspsk@altlinux.org> 0.12-alt1
- lilo support; totally rewrite algorithm

* Tue Nov 09 2010 Anton Farygin <rider@altlinux.ru> 0.11-alt1
- fixmbr:
    - do not use evms
    - display errors from mount-system only in verbose mode
    - reinstall grub only on block devices

* Mon Nov 08 2010 Anton Farygin <rider@altlinux.ru> 0.10-alt1
- do not start evms and system-report on boot
- do not use evms for mount-system
- fixed system search bug in fixmbr

* Wed Oct 27 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9-alt1
- fixmbr rewriten to work with grub (but lilo support dropped)

* Wed Jun 03 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt1
- fix from cas@ to fixmbr

* Thu Apr 09 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt1
- using aufs instead unionfs 

* Mon Nov 17 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- fixmbr fixed to work better with new alterator-lilo 

* Tue Sep 16 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt2
- inittab fixed (openvt is in /bin/ now) 

* Mon Aug 25 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt1
- fixmbr totally rewritten 

* Thu May 22 2008 Andrey Cherepanov <cas@altlinux.ru> 0.4.2-alt2.5.S40.2
- fix prompt (text and highlighting)

* Mon May 19 2008 Andrey Cherepanov <cas@altlinux.ru> 0.4.2-alt2.5.S40.1
- fix prompt

* Mon May 19 2008 Andrey Cherepanov <cas@altlinux.ru> 0.4.2-alt2.5.S40.0
- new version of mbrresc
- mbrresc is renamed to `fixmbr'

* Thu May 15 2008 Hihin Ruslan <ruslandh@altlinux.ru> 0.4.2-alt2.4
- fix mbrresc

* Fri May 02 2008 Hihin Ruslan <ruslandh@altlinux.ru> 0.4.2-alt2.3
- new version

* Mon Apr 28 2008 Hihin Ruslan <ruslandh@altlinux.ru> 0.4.2-alt2.2
- add rescue-0.4.2-mbrresc.diff

* Mon Mar 10 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.4.2-alt2.eter1
- Merged with stanv@ lilo restore feature

* Tue Jan 29 2008 Alexey Gladkov <legion@altlinux.ru> 0.4.2-alt2
- Use system sysreport utility.
- Fix for kbd-1.13*.
- Minimize requires.

* Wed Dec 12 2007 Andriy Stepanov <stanv@altlinux.ru> 0.4.2-alt1.2
- No LVM activation (EVMS fixed)
  fix lilo restore

* Thu Dec 06 2007 Andriy Stepanov <stanv@altlinux.ru> 0.4.2-alt1.1
- Added:
  + LVM activation at boot time
  + mbrresc utility (say `mbrresc' at command before kernel loading)

* Thu Aug 09 2007 Alexey Gladkov <legion@altlinux.ru> 0.4.2-alt1
- Added:
  + Report information about x86 hardware as described in
    the system BIOS according to the SMBIOS/DMI standard.
  + Report information from Display Data Channel (DDC).
- Added requires dmidecode and ddcprobe.
- mount-fstab: Fix for new libshell.

* Thu May 03 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4.1-alt1
- Added rescue-shell.

* Wed May 02 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4-alt1
- rc.sysinit.rescue: Mounted /mnt to overlay.
- inittab.rescue: Added runlevel scripts execution.
- inittab.rescue: Added shell execution to vc5 and vc6.
- rc.sysinit.rescue: Removed developer-report execution.
- Renamed developer-report to system-report.
- Added sysreport service.

* Sat Apr 28 2007 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- rc.sysinit.rescue: Added necessary $USEMODULES initialization.

* Mon Apr 23 2007 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- inittab.rescue: Run bash with -l option.

* Fri Mar 30 2007 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Updated sysreport email address.

* Wed Feb 28 2007 Alexey Gladkov <legion@altlinux.ru> 0.0.1-alt1
- First build for ALT Linux.
