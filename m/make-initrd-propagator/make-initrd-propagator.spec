Name: make-initrd-propagator
Version: 0.44
Release: alt1

Summary: Put propagator into make-initrd generated image

License: GPLv2+
Group: System/Base
URL: https://www.altlinux.org/Make-initrd-propagator

Source0: %name-%version.tar

Requires: console-vt-tools fdisk /sbin/addpart grep
Requires: sysvinit-utils net-tools
Requires: sed procps psmisc findutils nfs-utils
Requires: make-initrd
Requires: e2fsprogs time
Requires: udev-rules udev-extras

# For new put-file utility
Requires: make-initrd >= 2.0.3-alt1

BuildArch: noarch
AutoReq: noshell, noshebang


%description
make-initrd feature to make hybrid propagator/make-initrd image

%prep
%setup

%install
mkdir -p %buildroot%_datadir/make-initrd/features/
cp -a propagator %buildroot%_datadir/make-initrd/features/
mkdir -p %buildroot%_datadir/make-initrd/features/propagator/data/image

%files
%_datadir/make-initrd/features/propagator

%changelog
* Tue Jan 05 2021 Anton Midyukov <antohami@altlinux.org> 0.44-alt1
- init-bottom: Always create alt-live-storage

* Sun Dec 27 2020 Anton Midyukov <antohami@altlinux.org> 0.43-alt1
- init-bottom: Do not calculate starting sector for alt-live-storage
- Fix License Tag

* Tue Jun 25 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.42-alt1
- config.mk: removed copy of *-net-name-slot.rules udev rule (copying
  of absent file is going to be error in upcoming release of make-initrd).

* Thu Jun 20 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.41-alt3
- mount.aufs removed from config.mk (Closes: 36930)

* Wed Jun 19 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.41-alt2
- unneede dependence on aufs2-util removed

* Wed Jan 23 2019 Arseny Maslennikov <arseny@altlinux.org> 0.41-alt1
- Network overlays:
  + Overlays with a name of *.squashfs are now also taken into consideration.
  + Support for overlay sets of an unspecified profile is restored; see
    commit message for elaborate reasoning.

* Tue Aug 28 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.40-alt1
- switch from aufs to overlayfs

* Wed Jul 11 2018 Anton Midyukov <antohami@altlinux.org> 0.33-alt2
- Fix ACL access for livecd (Closes: 34793)

* Thu Jul 05 2018 Arseny Maslennikov <arseny@altlinux.org> 0.33-alt1
- netboot: Fixed busybox support.

* Sun Jan 21 2018 Arseny Maslennikov <arseny@altlinux.org> 0.32-alt1
- netboot: Allowed use of different overlay storage locations.
- netboot: Forbade mounting overlays with unspecified profile.
  To continue using overlays stored without a profile name:
  + pick a profile name;
  + put them into a subdirectory of the same name;
  + add `profile=$name' to kernel command line.

* Sun Apr 02 2017 Alexey Gladkov <legion@altlinux.ru> 0.31-alt3
- Enforce use system sed.

* Tue Mar 21 2017 Alexey Gladkov <legion@altlinux.ru> 0.31-alt2
- Port to make-initrd >= 2.0.3

* Mon Oct 17 2016 Michael Shigorin <mike@altlinux.org> 0.31-alt1
- improve RW slice operation (closes: #32476, #32562):
  only create/use it when there's enough space (1Gb or more), and
  it's been either
  + explicitly asked for (BIOS mode), or
  + fast enough (UEFI mode; otherwise the filesystem
    will be marked "alt-slow-storage")
- add mkfs/mount options for faster operation
- extend debug support

* Tue Sep 06 2016 Michael Shigorin <mike@altlinux.org> 0.30-alt1
- only mount rw slice when live_rw is specified explicitly
  due to severe I/O penalty coming with it (closes: #32476)
- slightly better package description

* Mon May 30 2016 Michael Shigorin <mike@altlinux.org> 0.29-alt1
- fix mount options (broke live_rw functionality)

* Tue Nov 03 2015 Michael Shigorin <mike@altlinux.org> 0.28-alt1
- remove superfluous rules duplicating propagator's functionality
  (closes: #31069)

* Tue Mar 10 2015 Michael Shigorin <mike@altlinux.org> 0.27-alt1
- init-bottom: explicitly handle rescue for rw overlays

* Mon Mar 09 2015 Michael Shigorin <mike@altlinux.org> 0.26-alt1
- trigger -c add (see also #30315)

* Fri Feb 27 2015 Michael Shigorin <mike@altlinux.org> 0.25-alt1
- init-bottom:
  + ensure compatibility with newer fdisk
  + make the output more concise

* Thu Feb 26 2015 Michael Shigorin <mike@altlinux.org> 0.24-alt1
- call udevadm trigger (see also #30315)

* Thu Jan 23 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.23-alt1
- partition size calculation fixed again

* Wed Dec 25 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.22-alt2
- partition size calculation fixed

* Tue Dec 24 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.22-alt1
- resurrect rw live on x86_64

* Mon Oct 14 2013 Fr. Br. George <george@altlinux.ru> 0.21-alt2
- Use subdirectory when mounting profiled .iso patches

* Mon Sep 30 2013 Fr. Br. George <george@altlinux.ru> 0.21-alt1
- Fix non-posix invalid redirection
- Show mounted overlays and mount status

* Thu Apr 11 2013 Michael Shigorin <mike@altlinux.org> 0.20-alt1
- fixed a typo, thanks Andrey Liakhovets

* Thu Mar 21 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.19-alt1
- use disk and nfs slices only if stagenage=live

* Tue Mar 19 2013 Michael Shigorin <mike@altlinux.org> 0.18-alt1
- init-bottom (see also the subsequent discussion in #28289):
  + require "live_rw" keyword for "cdrom" method to create rw slice
  + create ext4 w/o journal instead of ext3
  + tweaked rw slice mount options

* Sat Mar 16 2013 Michael Shigorin <mike@altlinux.org> 0.17-alt1
- accept cdrom for rw disk_slice on isohybrid media (closes: #28289)

* Thu Feb 21 2013 Michael Shigorin <mike@altlinux.org> 0.16-alt1
- reenable rw slice if it's not GPT (thus MBR)
- fixed annoying /etc/mtab related message

* Sun Feb 10 2013 Michael Shigorin <mike@altlinux.org> 0.15-alt1
- add name-slot-rules conditionally (see also #28484)
- fix a typo

* Thu Jan 31 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.14-alt1
- add name-slot-rules

* Fri Dec 28 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.13-alt2
- creating aufs slice on hybrid rw media temporary disabled

* Fri Nov 09 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.13-alt1
- mount.nfs added

* Mon Sep 17 2012 Fr. Br. George <george@altlinux.ru> 0.12-alt1
- Provide /proc/cmdline parser
- Add overlays profiling support

* Wed Sep 12 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.11-alt1
- put-file usage fix from sin@ (closes #27725)

* Wed Sep 05 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.10-alt1
- added --numeric-ports option to netstat (dans@), (closes: #27698)

* Thu May 10 2012 Michael Shigorin <mike@altlinux.org> 0.9-alt1
- NMU: merged legion@'s update for current make-initrd

* Thu Mar 22 2012 Andriy Stepanov <stanv@altlinux.ru> 0.8-alt1.2
- Works independent from propagator

* Wed Sep 14 2011 Michael Shigorin <mike@altlinux.org> 0.8-alt1.1
- NMU: add Requires: make-initrd (closes: #26133)
- trivial spec cleanup

* Tue Aug 23 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt1
- nfs live overlays order fixed

* Tue Jun 14 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt4
- nfs live overlays fixed

* Thu Jun 09 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt3
- head added to initramfs for nfs livecd overlays

* Tue Jun 07 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt2
- udba=notify deleted for compatibility with 2.6.32

* Wed Jun 01 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt1
- remount root for live to aufs

* Wed Dec 22 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- create /image in rootfs (fixes http and ftp methods)

* Fri Dec 10 2010 Anton Farygin <rider@altlinux.ru> 0.5-alt1
- do not copy plymouth files if plymouth not installed

* Wed Dec 08 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- creating /lib/firmware in rootfs

* Tue Dec 07 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- hack 60-persistent-storage-rules to not link sd[a-z] to disk/by-label

* Wed Dec 01 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- boot-duration copying added

* Tue Nov 30 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build



