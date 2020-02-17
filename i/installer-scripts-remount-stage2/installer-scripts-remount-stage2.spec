Name: installer-scripts-remount-stage2
Version: 0.5.16
Release: alt1

Summary: Shared installer scripts: remount
License: GPLv2+
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer
Source: %name-%version.tar
BuildArch: noarch
Requires: sfdisk

Conflicts: installer-common-stage2 < 1.8.11-alt1

%description
This package contains shared installer scripts,
namely a script to remount filesystems after
employing EVMS to partition and mkfs them
so that preinstall/postinstall scripts would
work in block device and devmapper environment
that's close to the target system's one.

%prep
%setup

%install
# a single script is not worth two makefiles yet
install -pDm755 scripts/install2-remount-functions \
	%buildroot%_sbindir/install2-remount-functions

install -pDm755 initinstall/stop-md-dm.sh \
	%buildroot%_datadir/install2/initinstall.d/80-stop-md-dm.sh

cat << __EOF__ > %buildroot%_datadir/install2/initinstall.d/85-start-multipath.sh
#!/bin/sh

. install2-remount-functions

start_multipath

:
__EOF__

%files
%_sbindir/*
%_datadir/install2/initinstall.d/80-stop-md-dm.sh
%attr(0755,root,root) %_datadir/install2/initinstall.d/85-start-multipath.sh

%changelog
* Mon Feb 03 2020 Oleg Solovyov <mcpain@altlinux.org> 0.5.16-alt1
- start_lvm: Activate all LVs when setting up LVM

* Fri Jul 19 2019 Michael Shigorin <mike@altlinux.org> 0.5.15-alt1
- silence harmless sfdisk's "re-reading the partition table failed"

* Fri Apr 07 2017 Michael Shigorin <mike@altlinux.org> 0.5.14-alt1
- ignore blkid cache as the script's goal is changing
  block device situation

* Tue Mar 21 2017 Michael Shigorin <mike@altlinux.org> 0.5.13-alt1
- ignore lvm exit code to hopefully avoid a few more unneeded
  "destination filesystem remount error" cases (closes: #33246)
- double-check before umounting /mnt/destination just in case

* Tue Jan 31 2017 Michael Shigorin <mike@altlinux.org> 0.5.12-alt1
- added /dev/md/* support to the existing /dev/md* one;
  thanks Vadim Zelenin for pointing this out (closes: #31286)

* Wed Dec 28 2016 Michael Shigorin <mike@altlinux.org> 0.5.11-alt1
- don't do "destination filesystem remount error"
  when it's just mdadm putting new arrays into PENDING state

* Mon Dec 05 2016 Michael Shigorin <mike@altlinux.org> 0.5.10-alt1
- fixed multipath support when multipathd is there
  but there are no multipath-capable devices available

* Thu Nov 24 2016 Michael Shigorin <mike@altlinux.org> 0.5.9-alt1
- *added* multipath support (shrek@)
  + stopping dm drops multipath setup, care for that too

* Wed Nov 16 2016 Michael Shigorin <mike@altlinux.org> 0.5.8-alt1
- added multipath support (shrek@)

* Thu Jun 09 2016 Michael Shigorin <mike@altlinux.org> 0.5.7-alt1
- ensure active partition(s) existence to workaround
  some intel/dell BIOS "smartness" resulting in boot refusal

* Mon Apr 04 2016 Michael Shigorin <mike@altlinux.org> 0.5.6-alt1
- defuse gvfs

* Tue Nov 03 2015 Michael Shigorin <mike@altlinux.org> 0.5.5-alt1
- /dev/md/imsm workaround (closes: #31286)

* Wed Oct 14 2015 Aleksey Avdeev <solo@altlinux.org> 0.5.4-alt1
- Fix unmount the root after copying

* Tue Oct 13 2015 Aleksey Avdeev <solo@altlinux.org> 0.5.3-alt1
- Use cp in the absence of installable system
  /usr/share/make-initrd/tools/put-file

* Tue Oct 13 2015 Aleksey Avdeev <solo@altlinux.org> 0.5.2-alt2
- Add copying the libraries necessary for binaries copied (ALT#31351).
  To copy using a script /usr/share/make-initrd/tools/put-file
  belonging to an installable distribution.

* Wed Jun 11 2014 Michael Shigorin <mike@altlinux.org> 0.5.1-alt1
- /run/udev support

* Thu Nov 14 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5-alt1
- Stop MD/DM devices in initinstall (ALT#29554).

* Wed May 22 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt1
- prepare data for installer-feature-desktop-other-fs >= 0.7-alt1
  (see also #29005)

* Wed Jan 30 2013 Michael Shigorin <mike@altlinux.org> 0.3-alt1
- reverted the change made in 0.2 since fstab manipulation
  is to be fixed in livecd-install

* Tue Jan 29 2013 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- tweaked populate_fstab() to support livecd-install case properly
  (fixes duplicated filesystem lines in target /etc/fstab)

* Fri Dec 21 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- split off installer-1.8.10-alt1 to use with livecd-install too
