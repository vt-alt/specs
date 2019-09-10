Name: installer
Version: 1.10.0
Release: alt1

Summary: Installer common parts
License: GPLv2+
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer
Source: %name-%version.tar

BuildRequires: glibc-devel-static

%description
This package contains common installer parts.

%package common-stage2
Summary: Installer common stage2
Group: System/Configuration/Other
Provides: %name-stage2 = %version-%release
Obsoletes: %name-stage2 < %version-%release
# installer-preinstall.desktop
Requires: alterator-preinstall >= 0.7-alt1
# scripts/install2
Requires: alterator-wizardface alterator-backend-x11 >= 0.21-alt2 xinit xinitrc xorg-server xorg-drv-video
# scripts/postinstall
Requires: eject
# initinstall.d/10-vt.sh
Requires: bash console-vt-tools

Provides: installer-feature-autohostname
Obsoletes: installer-feature-autohostname
Provides: installer-feature-autohostname-stage2
Obsoletes: installer-feature-autohostname-stage2

Provides: installer-feature-cmdline-parameters-stage2
Obsoletes: installer-feature-cmdline-parameters-stage2

Provides: installer-feature-services
Obsoletes: installer-feature-services

Provides: installer-feature-copy-udev-rules-stage3
Obsoletes: installer-feature-copy-udev-rules-stage3
Requires: udev-rule-generator


Provides: installer-feature-systemd
Obsoletes: installer-feature-systemd

Provides: installer-feature-setup-network-stage2
Obsoletes: installer-feature-setup-network-stage2
Requires: hostinfo iproute2

Provides: installer-feature-setup-bootloader-stage2
Obsoletes: installer-feature-setup-bootloader-stage2

Requires: xorg-xvfb

# needed for lvm binary, see 11-remount.sh
Requires: libdevmapper-event

Conflicts: alterator-pkg < 1.2-alt1, alterator-sysconfig < 0.6-alt1, alterator-datetime < 4.3.0-alt1
# stage2 and stage3 are mutually exclusive
Conflicts: %name-common-stage3

%description common-stage2
This package contains common installer stage2 files and dependencies.

%package common-stage3
Summary: Installer common stage3
Group: System/Configuration/Other
BuildArch: noarch
Provides: %name-stage3 = %version-%release
Obsoletes: %name-stage3 < %version-%release
Requires: alterator-notes
# stage2 and stage3 are mutually exclusive
Conflicts: %name-common-stage2

Provides: installer-feature-eth-by-mac-stage3
Obsoletes: installer-feature-eth-by-mac-stage3

Provides: installer-feature-setup-network-stage3
Obsoletes: installer-feature-setup-network-stage3
Requires: alterator-net-eth chkconfig etcnet

%description common-stage3
This package contains common installer stage3 files and dependencies.

%prep
%setup

%build
%make_build

%install
%makeinstall
mkdir -p %buildroot%_sysconfdir/apt/apt.conf.d/
cat > %buildroot%_sysconfdir/apt/apt.conf.d/installer-cache-limit.conf <<@@@
APT::Cache-Limit "$((32*1024*1024))";
@@@

%files common-stage2
%_bindir/*
%_sbindir/*
%_datadir/install2
%_sysconfdir/apt/apt.conf.d/installer-cache-limit.conf
%exclude %_datadir/install2/preinstall.d/30-setup-network.sh

%files common-stage3
%_datadir/install2/preinstall.d/30-setup-network.sh

%changelog
* Fri Sep 06 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.10.0-alt1
- remove alterator-postinstall if not used
- run apt-get autoremove after removing installer

* Thu May 16 2019 Mikhail Efremov <sem@altlinux.org> 1.9.0-alt1
- preinstall: Drop options for mkinitrd.
- postinstall: Generate host key files.
- install2: Mount runfs to /run.
- initinstall: Start NTP client if present.
- install2: Use systemd-tmpfiles to create tmp files.

* Tue Apr  9 2019 Leonid Krivoshein <klark@altlinux.org> 1.8.48-alt1
- postinstall: fix for configurations without mdraid.

* Sat Apr  6 2019 Leonid Krivoshein <klark@altlinux.org> 1.8.47-alt1
- postinstall: wait MD-resync, mdsync_nowait turn OFF this feature.
- install2-init.c: execute swapoff and post-umount hook added.
- install2-post-umount: new script (installer hook) added.
- install2-action-functions: return codes fixup.

* Mon Feb 25 2019 Leonid Krivoshein <klark@altlinux.org> 1.8.46-alt1
- Xorg configuration fallback mechanism repaired and improved.

* Thu Dec 06 2018 Anton Farygin <rider@altlinux.ru> 1.8.45-alt1
- btrfs utils cleanup moved from installer to mkimage profile

* Mon Oct 15 2018 Leonid Krivoshein <klark@altlinux.org> 1.8.44-alt1
- Fix poweroff functionality (closes #35479)

* Fri Oct 05 2018 Michael Shigorin <mike@altlinux.org> 1.8.43-alt1
- Try harder to sync/umount rootfs before rebooting
- Ensure /proc is mounted before checking for "poweroff" keyword
- Avoid curl spam

* Fri Aug 17 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.8.42-alt1
- Copying .disk/info into destination added

* Sat Jun 09 2018 Sergey Bubnov <omg@altlinux.org> 1.8.41-alt2
- Fix for DHCP waiting loop

* Fri Jun 08 2018 Sergey Bubnov <omg@altlinux.org> 1.8.41-alt1
- Wait for DHCP responce when `curl=` is in kernel parameters
  (closes: #26813)

* Fri Dec 08 2017 Mikhail Efremov <sem@altlinux.org> 1.8.40-alt1
- Remove DRM modules if Xorg server is not present.
- Drop autofs4 from initrd.
- Drop systemd feature in the initrd.mk.

* Thu Nov 09 2017 Mikhail Efremov <sem@altlinux.org> 1.8.39-alt1
- 10-xorg.sh: Set correct default.targer.
- 10-xorg.sh: Add more DMs for check.

* Mon Jul 31 2017 Michael Shigorin <mike@altlinux.org> 1.8.38-alt1
- 90-date.sh: force distro birth date if system one reads "before"
  (closes: #33705)

* Tue Jun 27 2017 Michael Shigorin <mike@altlinux.org> 1.8.37-alt1
- 10-disk.sh: ignore sed exit code (see also #30239).

* Wed Mar 29 2017 Michael Shigorin <mike@altlinux.org> 1.8.36-alt1
- 40-autohostname.sh: Don't setup /etc/HOSTNAME.

* Mon Mar 20 2017 Michael Shigorin <mike@altlinux.org> 1.8.35-alt1
- vnc related improvements

* Tue Jan 31 2017 Michael Shigorin <mike@altlinux.org> 1.8.34-alt1
- *fixed* "headful" mode of installation over vnc

* Tue Jan 31 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.8.33-alt1
- headfull mode in vnc installation fixed

* Tue Jun 07 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.8.32-alt1
- don't require alterator-wizardface in stage3. There is no need
  for it, but it requires qt4

* Wed Feb 10 2016 Michael Shigorin <mike@altlinux.org> 1.8.31-alt1
- added 65-setup-control.sh (for m-p at least)

* Thu Nov 12 2015 Anton Farygin <rider@altlinux.ru> 1.8.30-alt1
- add mmbclk*boot* to evms exclude list

* Mon May 11 2015 Andrey Cherepanov <cas@altlinux.org> 1.8.29-alt1
- If there is 'poweroff' option in kernel command line then power off
  instead of reboot (useful for autoinstall)

* Tue Mar 31 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.8.28-alt1
- Added default APT::Cache-Limit=32M for installer.

* Thu Feb 26 2015 Michael Shigorin <mike@altlinux.org> 1.8.27-alt1
- ignore MMC RPMB
- silence efivars
- 45-setup-dhcp.sh: check whether ifacedir is there

* Thu Sep 11 2014 Michael Shigorin <mike@altlinux.org> 1.8.26-alt1
- 20-systemd.sh: update systemd check
  a la sd_booted from service-0.5.26-alt1

* Fri Jun 20 2014 Mikhail Efremov <sem@altlinux.org> 1.8.25-alt1
- 20-systemd.sh: Check for systemd-sysvinit installed.

* Sat Mar 22 2014 Michael Shigorin <mike@altlinux.org> 1.8.24-alt1
- survive missing locale(1)

* Sun Feb 09 2014 Michael Shigorin <mike@altlinux.org> 1.8.23-alt1
- fixed 65-setup-services.sh

* Sun Jan 12 2014 Evgeny Sinelnikov <sin@altlinux.ru> 1.8.22-alt1
- add support cifs install method

* Mon Dec 02 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.21-alt1
- set fallback lang to en_US from POSIX

* Fri Nov 29 2013 Mikhail Efremov <sem@altlinux.org> 1.8.20-alt1
- Fix 10-xorg.sh preinstall script.

* Wed Sep 25 2013 Michael Shigorin <mike@altlinux.org> 1.8.19-alt1
- Fix initinstall scripts (the noise was annoying enough already).

* Thu Mar 28 2013 Mikhail Efremov <sem@altlinux.org> 1.8.18-alt1
- Fix firsttime flag-file path.
- Use xorg-drv-video virtual package again.

* Mon Mar 11 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.17-alt1
- dependences on xorg video drivers added

* Thu Mar 07 2013 Michael Shigorin <mike@altlinux.org> 1.8.16-alt1
- fixed xorg dependencies (thx shrek@)

* Tue Feb 12 2013 Mikhail Efremov <sem@altlinux.org> 1.8.15-alt1
- cp-installer-logs: Don't copy wizard.log.
- cp-installer-logs: Fix removal passwords from install logs.

* Wed Jan 30 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.14-alt2
- 08-crypttab fixed

* Wed Jan 23 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.14-alt1
- add luks to initrd only if / on luks, otherwise create crypttab

* Sat Dec 29 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.13-alt1
- add luks to initrd only if threre are luks partitions

* Thu Dec 27 2012 Andrey Cherepanov <cas@altlinux.org> 1.8.12-alt2
- Fix retrieve alteratord.log
- Add wizard.log and remount.log (this fixes password cleanup)

* Thu Dec 27 2012 Timur Aitov <timonbl4@altlinux.org> 1.8.12-alt1
- 50-initrd.sh: always add luks in initrd

* Fri Dec 21 2012 Michael Shigorin <mike@altlinux.org> 1.8.11-alt1
- remount: split off as install2-remount-functions-stage2 package

* Thu Dec 20 2012 Michael Shigorin <mike@altlinux.org> 1.8.10-alt1
- steps: added luks.desktop

* Mon Dec 17 2012 Michael Shigorin <mike@altlinux.org> 1.8.9-alt1
- remount: luksOpen part (timonbl4@) (closes: #28200)

* Thu Dec 13 2012 Michael Shigorin <mike@altlinux.org> 1.8.8-alt1
- remount: "duplicate" turn_evms_off call

* Thu Dec 13 2012 Michael Shigorin <mike@altlinux.org> 1.8.7-alt1
- remount: initial LUKS support (deactivation part)
- remount: ignore swapon errors

* Thu Dec 13 2012 Michael Shigorin <mike@altlinux.org> 1.8.6-alt1
- remount: fixed variable scope thinko

* Tue Dec 11 2012 Michael Shigorin <mike@altlinux.org> 1.8.5-alt1
- 10-fstab script merged into install2-remount-functions either
- added an Url:

* Tue Dec 11 2012 Michael Shigorin <mike@altlinux.org> 1.8.4-alt1
- 11-remount script moved to become install2-remount-functions
  (to be included in alterator-preinstall and used just in time)

* Mon Dec 10 2012 Michael Shigorin <mike@altlinux.org> 1.8.3-alt1
- 11-remount script moved back to stage2 (no use of prepkg.d too)

* Mon Dec 10 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.2-alt1
- 11-remount script moved to stage3

* Fri Dec 07 2012 Michael Shigorin <mike@altlinux.org> 1.8.1-alt1
- 11-remount fixes (see #28181)

* Tue Dec 04 2012 Michael Shigorin <mike@altlinux.org> 1.8.0-alt1
- introduced volume remounting (closes: #28181)

* Fri Nov 30 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.7.11-alt1
- copy-udev-rules moved to preinstall

* Wed Nov 28 2012 Timur Aitov <timonbl4@altlinux.org> 1.7.10-alt1
- removed preinstall.d/08-crypttab.sh

* Thu Nov 15 2012 Michael Shigorin <mike@altlinux.org> 1.7.9-alt1
- fixed 08-crypttab.sh

* Wed Nov 14 2012 Michael Shigorin <mike@altlinux.org> 1.7.8-alt1
- added EFI support script

* Tue Nov 13 2012 Timur Aitov <timonbl4@altlinux.org> 1.7.7-alt3
- fixed search raid/lvm devices in preinstall.d/08-crypttab.sh

* Tue Nov 13 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.7.7-alt2
- mdm added to dms list

* Mon Oct 29 2012 Timur Aitov <timonbl4@altlinux.org> 1.7.7-alt1
- added preinstall.d/08-crypttab.sh

* Sat Oct 27 2012 Michael Shigorin <mike@altlinux.org> 1.7.6-alt1
- fixed wrong presumption in 10-xorg.sh (failed with current udev)

* Thu Oct 11 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.7.5-alt1
- 20-systemd and 65-setup services fixed

* Thu Oct 11 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.7.4-alt1
- added "40-autohostname.sh: re{li,ad}ability fixes" (mike@)

* Wed Sep 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.7.3-alt1
- set systemd default target if any dm present

* Fri Sep 14 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.7.2-alt1
- ability to work on writable aufs /

* Tue Sep 11 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.7.1-alt1
- copy xorg.conf to destdir if Driver set

* Fri Sep 07 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.7.0-alt1
- don't force 800x600 and use native resolution

* Fri Aug 17 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.2-alt1
- included installer features: cmdline-parameters, setup-bootloader,
  setup-network

* Thu Aug 16 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.1-alt1
- included installer feature: systemd
- additional provides/obsoletes added for features from prev release

* Tue Aug 07 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6-alt1
- included installer features: services, copy-udev-rules, autohostname,

* Fri Mar 16 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.5.1-alt1
- dont't copy xorg.conf to destdir

* Sun Mar 11 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.5.0-alt1
- don't set DPI to 80 if 800x600 failed

* Wed Sep 14 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.14-alt2
- btrfs added to expert-only FS

* Thu Sep 01 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.14-alt1
- 15-expert.sh fixed

* Tue Aug 16 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.13-alt1
- new cp-mwtadata from stanv@

* Mon Aug 15 2011 Andrey Cherepanov <cas@altlinux.org> 1.4.12-alt4
- Unset no globbing parameter -f to copy my mask

* Fri Aug 12 2011 Andrey Cherepanov <cas@altlinux.org> 1.4.12-alt3
- Fix path to alteratord.log

* Thu Aug 11 2011 Andrey Cherepanov <cas@altlinux.org> 1.4.12-alt2
- Set exception on copy of non existed log file

* Thu Aug 11 2011 Andrey Cherepanov <cas@altlinux.org> 1.4.12-alt1
- Copy pkg-install.log and alteratord.log to installed system

* Tue Jul 12 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.11-alt1
- added nodesign command line option for automatic testing

* Tue May 31 2011 Michael Shigorin <mike@altlinux.org> 1.4.10-alt1
- terminate countdown at a key press (closes: #17338)

* Fri May 20 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.9-alt1
- ignore return code of get_local_metadata when nfs

* Wed Feb 23 2011 Anton Farygin <rider@altlinux.ru> 1.4.8-alt1
- add workaround for aufs /etc/hosts bug
- Go away from HAL (Andrey Stepanov)

* Fri Dec 10 2010 Anton Farygin <rider@altlinux.ru> 1.4.7-alt1
- remove plymouth requires

* Tue Dec 07 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.6-alt5
- fixes from stanv@

* Fri Dec 03 2010 Anton Farygin <rider@altlinux.ru> 1.4.6-alt4
- ignore plymouth errors (fixed work without plymouth theme)

* Fri Dec 03 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.6-alt3
- stop plymouth before start X

* Thu Dec 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.6-alt2
- nfs installation fixed

* Thu Dec 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.6-alt1
- plymouth support

* Tue Nov 30 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.5-alt1
- fix for cp-metadata from stanv@

* Fri Oct 29 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.4-alt3
- direct vnc installation fixed

* Mon Oct 18 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.4-alt2
- step file for vm-ortodox added

* Thu Sep 23 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.4-alt1
- mounting /dev/pts added for -el kernel

* Tue Sep 21 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.3-alt1
- LVM / installation fixed by aspsk@

* Tue Jun 29 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.2-alt1
- next curl call improvements from stanv@

* Thu Jun 10 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.1-alt1
- curl call improvements from stanv@

* Wed Apr 07 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt2
- wait for network in VNC install

* Mon Mar 22 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt1
- installation via VNC support (boot parameters are similar with fedora)

* Wed Mar 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3.4-alt1
- step file for alterator-grub added

* Mon Mar 15 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3.3-alt1
- fix nfs installation

* Sun Dec 27 2009 Anton Farygin <rider@altlinux.ru> 1.3.2-alt1
- add --omit-ide-modules to installkernel hook

* Mon Dec 07 2009 Stanislav Ievlev <inger@altlinux.org> 1.3.1-alt1
- add support for noeject parameter (don't eject media)
- add cmdline_has_arg() function (check for existance of some parameter in kernel args)
- sbolshakov@:
    ensure that etc X11 exists;
    introduce new cmdline parameter for remote metadata.

* Tue Nov 10 2009 Stanislav Ievlev <inger@altlinux.org> 1.3-alt1
- expand data paths to avoid chroot operation

* Thu Nov 05 2009 Stanislav Ievlev <inger@altlinux.org> 1.2.14-alt2
- explicitly require alterator-wizardface at stage2 and stage3

* Wed Oct 21 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.14-alt1
- removed -e from /usr/sbin/alterator-install2, wrong killall or 
  'service stop' exit status should not break installation

* Thu Oct 15 2009 Stanislav Ievlev <inger@altlinux.org> 1.2.13-alt2
- fix false alarms

* Wed Sep 16 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.13-alt1
- check for already run scripts added to postinstall

* Wed Sep 09 2009 Anton Farygin <rider@altlinux.ru> 1.2.12-alt1
- remove hal and dbus from stage3 requires
- run haldaemon and message bus if theirs was installed to stage3

* Thu Aug 27 2009 Stanislav Ievlev <inger@altlinux.org> 1.2.11-alt1
- run postinstall.d hooks only if system was marked as a new

* Thu Aug 20 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.10-alt1
- added handling 'expertmode' in command line

* Fri Apr 10 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.9-alt2
- Cleaned up manual dependencies.
- install2-action-functions: Append timestamp if not in color mode.

* Fri Apr 10 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.9-alt1
- scripts/alterator-install2: Updated from image-scripts.d/01xorg.
- scripts/install2: Parametrized xserver args, added -nolisten tcp by default.

* Mon Mar 30 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.8-alt2
- Added conflicts for mutually exclusive subpackages.

* Thu Mar 26 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.8-alt1
- Updated steps.

* Thu Mar 19 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.7-alt1
- 50-removable reverted

* Thu Mar 19 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.6-alt1
- fixed initrd generation in installer/preinstall.d/50-initrd.sh

* Tue Mar 17 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.5-alt1
- Removed obsolete hooks:
  initinstall.d/50-removable
  preinstall.d/60-nfs.sh
  preinstall.d/99-ldconfig.sh

* Tue Mar 17 2009 Stanislav Ievlev <inger@altlinux.org> 1.2.4-alt1
- Moved preinstall stage into separate package alterator-preinstall.
- Moved firsttime script from preinstall into postinstall.

* Mon Mar 16 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.3-alt1
- Fix from ldv@ for 99-cdrom.sh

* Fri Mar 13 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.2-alt1
- install2-init-functions (exec_chroot): Forward DURING_INSTALL variable.
- install2-init-functions: Deprecated run_chroot(), made it an alias to exec_chroot().
- preinstall.d/*: Replaced run_chroot() with exec_chroot().

* Fri Mar 13 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt1
- Removed obsolete backend2/deadline (Stanislav Ievlev).
- Updated BuildRequires.
- Added "common-" prefix to subpackages.
- Cleaned up makefiles and scripts/*.
- install2-init: Changed to list filesystems which remains mounted only once.

* Wed Mar 11 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- install2-init: Fixed loop_change_fd (Michail Yakushin).

* Fri Feb 06 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1-alt2
- switch to aufs usage. You should resurrect fs/exportfs.ko in your
  profiles/install2/image-scripts.d/999system

* Mon Feb 02 2009 Stanislav Ievlev <inger@altlinux.org> 1.1-alt1
- join datetime and tzone steps

* Mon Jan 26 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt2
- run postinstall scripts from $destdir/$postinstall_dir and $postinstall_dir

* Wed Jan 21 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt1
- move basesystem installation to alterator-pkg package

* Thu Jan 15 2009 Stanislav Ievlev <inger@altlinux.org> 0.9-alt2
- add step for sysconfig-base

* Thu Nov 06 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt1
- fix build with gcc-4.3
- add new native backend

* Thu Oct 16 2008 Stanislav Ievlev <inger@altlinux.org> 0.8-alt1
- use alterator-sh-functions instead of backend3.sh

* Thu Oct 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt30
- add XORG_CONF definition to install2

* Thu Oct 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt29
- fix Requires: alterator-backend-x11

* Thu Oct 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt28
- add fallback to all drivers returned by vcscan

* Wed Sep 24 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt27
- preinstall.d/10-xorg.sh: fix breackage of InputDevice section

* Fri Sep 19 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt26
- fixed creating xorg.conf for nvidia

* Fri Sep 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt25
- change fbdev and vesa fallbacks in install2

* Thu Sep 18 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt24
- fixed remove-if-removable scripts with mike@

* Thu Sep 18 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt23
- add steps/sysconfig.desktop

* Thu Sep 18 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt22
- fixed error from grep when CDROM installation

* Fri Sep 12 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt21
- update step files translations

* Thu Sep 11 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt20
- starting HAL after basesystem installation

* Wed Sep 10 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt19
- starting hal before x11_autosetup

* Wed Sep 10 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt18
- use new x11_autosetup options for setting xdriver and xres

* Wed Sep 03 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt17
- added sources.installer list when installing from removable devices

* Tue Sep 02 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt16
- really skip devices ;)

* Fri Aug 29 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt15
- fix bug in previous feature

* Thu Aug 28 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt14
- skip removable devices  from destination fstab

* Wed Aug 20 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt13
- fixed excluding usb media

* Fri Aug 15 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt12
- changeble fonts in stage2

* Thu Aug 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt11
- move icons to steps subdir

* Tue Jul 29 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt10
- move creation of xorg.conf from install2 to initinstall.d/30-xorg.sh
- fix problem with xdriver=auto

* Tue Jul 29 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt9
- add sleep 1 at the end of alterator-install2 (see #16450)

* Fri Jul 25 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt8
- add Requires: hal dbus to stage2

* Tue Jul 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt7
- modify preinstall.d/10-xorg.sh: create new xorg.conf for system,
  do not copy installer's xorg.conf

* Tue Jul 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt6
- kill console-kit-daemon too (by rider)

* Tue Jul 01 2008 Anton Farygin <rider@altlinux.ru> 0.7-alt5
- stop hal and dbus before alterator-wizard

* Mon Jun 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt4
- set 800x600 resolution for X

* Mon Jun 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt3
- fix scripts/install2, modify Requires

* Mon Jun 30 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt2
- fix scripts/install2

* Fri Jun 27 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt1
- remove initinstall.d/30-xorg.sh (configuration of xorg.conf)
- configure xorg.conf in scripts/install2 using x11_autosetup from new alterator-x11
- add preinstall.d/10-xorg.sh for copying xorg.conf to destination system

* Thu Jun 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt5
- modify for new alterator-x11 (require hal, dbus)

* Tue Jun 17 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt4
- update documentation

* Sat Jun 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt3
- document:replace -> frame:replace

* Wed May 28 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt2
- first run preinstall scripts from installed system

* Wed May 28 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- drop unionfs usage by sbolshakov@

* Mon May 26 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt3
- remove rest of dependencies on alterator-autoinstall package

* Fri May 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt2
- move logfile copying to postinstall scripts
- improve splash support

* Thu May 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- step files: use help files from modules
- remove autoinstall backend usage
- basesystem,preinstall: use colspan, remove inmplicit text attributes for labels, add help
- remove unused .scm files

* Wed May 14 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt17
- splash support
- exclude SCSI cdrom devices

* Wed Apr 30 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt16
- move preinstall.d to new alterator-net-eth
- update url of the installer-network step

* Thu Apr 24 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt15
- updated for new alterator-net-eth

* Wed Apr 16 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt14
- yet another merge (ldv@, sin@)
- fix reexec

* Mon Apr 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt13
- merge code improvements from @ldv and @sin
- move preinstall.d/pkg-groups to alterator-pkg

* Wed Apr 09 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt12
- add support for nonanonymous ftp servers (#14697)
- fix work with empty DNS_SERVER (#14966)

* Tue Apr 08 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt11
- @ldv: install2-init.c (killall): Do some sleep after sending SIGKILL

* Mon Apr 07 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt10
- fix install2-init abnormal exit (by ldv@, sin@)
- use control to switch portmap status

* Thu Mar 13 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt9
- use ALTERATOR_DATADIR

* Thu Mar 06 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt8
- added kernels sorting
- run installkernel in normal mode (without DURING_INSTALL)

* Mon Mar 03 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt7
- replace installer-finish with release-notes

* Fri Feb 29 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt6
- build to Sisyphus

* Thu Feb 28 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt5.1
- exclude a whole boot device

* Wed Feb 27 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt5
- fix typo

* Fri Feb 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt4
- kill before loop_change_fd

* Thu Feb 21 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt3
- move last loop_change_fd into init

* Tue Feb 19 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- ignore eject failure
- improve sources layout
- improve install2-init:
  sleep between sigterm and sigkill
  more messages during kill process
  fix typo in messages

* Tue Feb 12 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- fix /mnt/destination umount in multidisk installation

* Wed Jan 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt9
- fix help refs in users-root and users-add steps

* Tue Jan 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt8
- global DURING_INSTALL export

* Thu Jan 10 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt7
- update docs
- patch from boyarsh: added -f option to openvt to avoid 'vt is already in use' bug

* Fri Dec 07 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt6
- xorg tuning: add mouse_autosetup call (need to use serial mices)

* Mon Nov 12 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt5
- common find-free-partition utility
- common CDROMDEV variable
- new preinstall script: try to free cdrom device

* Mon Nov 12 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt4
- build system improvements (split C-sources and shell scripts)
- move main global variables to install2-sh-functions
- move unionfs code to common place
- add losetup-mv utility

* Tue Nov 06 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt3
- add missing requires to stage3
- add support for multiple xdriver= (to allow xdriver defaults tuning)

* Tue Oct 30 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- fix firsttime script
- move openvt start to initinstall.d script

* Fri Oct 26 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- update documentation

* Wed Oct 24 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt5
- replace get-manifest with common cp-metadata utility
- add support for pkg-groups profile
- move old apt-profile.scm copying into preinstall script
- add initinstall.d feature (tuning before installator start)

* Thu Oct 18 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- fix icon names

* Mon Oct 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- backports from desktop branch
- turn off splash at the end of install

* Fri Oct 12 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- add default finish step (installer-finish)

* Fri Oct 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- new profile system

* Mon Sep 24 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- improve nfs support
- move finish step to distribution specific package

* Thu Sep 20 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- move language step and i18n preinstall hack into common sysconfig package

* Wed Sep 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- move license step into separate package

* Fri Sep 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- remove conflict between stages

* Tue Aug 28 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- rename to installer

* Thu Mar 08 2007 Alexey Gladkov <legion@altlinux.ru> 0.2-alt7
- Rewrite Date/Time step.

* Wed Feb 21 2007 Alexey Gladkov <legion@altlinux.ru> 0.2-alt6
- Fix network settings.

* Mon Feb 12 2007 Alexey Gladkov <legion@altlinux.ru> 0.2-alt5
- UI optimazations.
- Change bootloader stage.
- Broke autoinstall.
- Remove net-tcp stage.

* Thu Feb 08 2007 Alexey Gladkov <legion@altlinux.ru> 0.2-alt4
- Add 'ai' parameter.
- Fix package for new udev-105.
- Fix autoinstall.
- Fix cdrom method.

* Fri Jan 12 2007 Alexey Gladkov <legion@altlinux.ru> 0.2-alt3
- Add autoinstall.
- Add ftp/http install methods.
- Avoid using libhw-tools.
- Use swap.
- UI optimizations.

* Wed Jan 10 2007 Alexey Gladkov <legion@altlinux.ru> 0.2-alt2
- Marge install2 and install3 stages.
- Remove useless UI step.
- UI optimizations.

* Fri Nov 17 2006 Alexey Gladkov <legion@altlinux.ru> 0.0.1-alt4
- Initial revision.
