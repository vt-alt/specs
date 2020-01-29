%global myname make-initrd

Name: make-initrd
Version: 2.4.0
Release: alt1

Summary: Creates an initramfs image
License: GPL-3.0
Group: System/Base

Packager: Alexey Gladkov <legion@altlinux.ru>

BuildRequires: help2man
BuildRequires: libkmod-devel
BuildRequires: zlib-devel
BuildRequires: bzlib-devel
BuildRequires: liblzma-devel
BuildRequires: libzstd-devel
BuildRequires: libelf-devel

Provides: make-initrd(crc32c) = 1

Provides: mkinitrd = 2:%version-%release
Provides: make-initrd2 = %version-%release
Obsoletes: make-initrd2

Requires: sh libshell make sed module-init-tools coreutils findutils grep glibc-utils
Requires: chrooted-resolv service util-linux which file

# Feature qemu
Requires: pciutils

# setsid, timeout
Requires: make-initrd-busybox >= 1.24.2-alt2

# depinfo
Requires: libkmod >= 8-alt1

# make bug-report
Requires: tar

# ipconfig -q: kinit-utils-1.5.15-alt3
# run-init -e: kinit-utils-1.5.17-alt2
# ipconfig -D: kinit-utils-1.5.25-alt2
# halt, replace, showenv moved from kinit-utils-1.5.25-alt5
Requires: kinit-utils >= 1.5.25-alt5

# Move /dev from initrd to the real system.
# 167: udevadm info --run
Requires: udev >= 167-alt1

# installkernel
Requires: bootloader-utils >= 0.4.10-alt1

# blkid
Requires: util-linux >= 2.17.2-alt1

# This avoids getting a dependency on sh from "#!/bin/sh".
#AutoReq: yes, nopam, noperl, nopython, noshell, notcl
AutoReq: noshell, noshebang

Source0: %name-%version.tar

%description
make-initrd is a new, uevent-driven initramfs infrastructure based around udev.

%package devmapper
Summary: device-mapper module for %name
Group: System/Base
Requires: %name = %version-%release
Requires: dmsetup >= 1.02.44-alt3
AutoReq: noshell, noshebang

%description devmapper
device-mapper module for %name

%package lvm
Summary: LVM module for %name
Group: System/Base
Requires: %name = %version-%release
Requires: %name-devmapper = %version-%release
Requires: lvm2
AutoReq: noshell, noshebang

%description lvm
LVM module for %name

%package luks
Summary: LUKS module for %name
Group: System/Base
Requires: %name = %version-%release
Requires: %name-devmapper = %version-%release
Requires: cryptsetup
AutoReq: noshell, noshebang

%description luks
LUKS module for %name

%package nfs
Summary: NFS module for %name
Group: System/Base
AutoReq: noshell, noshebang

%description nfs
NFS module for %name

%package multipath
Summary: multipath module for %name
Group: System/Base
Requires: %name = %version-%release
Requires: %name-devmapper = %version-%release
Requires: multipath-tools
AutoReq: noshell, noshebang

%description multipath
Multipath module for %name

%package plymouth
Summary: plymouth module for %name
Group: System/Base
Requires: %name = %version-%release
Requires: plymouth
AutoReq: noshell, noshebang

%description plymouth
plymouth module for %name

%package mdadm
Summary: mdadm module for %name
Group: System/Base
Requires: %name = %version-%release
Requires: mdadm
AutoReq: noshell, noshebang

%description mdadm
Mdadm module for %name

%package ucode
Summary: CPU microcode module for %name
Group: System/Base
Requires: %name = %version-%release
Requires: iucode_tool, firmware-intel-ucode, linux-firmware
Requires: cpio
AutoReq: noshell, noshebang

%description ucode
CPU microcode autoloading module for %name

%prep
%setup -q

%build
%make_build

%install
%make_install DESTDIR=%buildroot install

%triggerin -- %name < 0.8.1-alt1
c="%_sysconfdir/initrd.mk"
if [ -s "$c" ] && ! grep -qs '^AUTODETECT[[:space:]]*=[[:space:]]*all[[:space:]]*' "$c"; then
	printf -- 'make-initrd: Migrating to new autodetect scheme ...\n' >&2
	sed -i -e 's/^\(AUTODETECT[[:space:]]*=.*\)$/# \1\nAUTODETECT = all/' "$c"
fi

%files
%dir %_sysconfdir/initrd.mk.d
%config(noreplace) %_sysconfdir/initrd.mk.d/*.mk.example
%config(noreplace) %_sysconfdir/initrd.mk
%_bindir/*
%_sbindir/*
%_datadir/%myname
%_man1dir/*
/lib/initrd
%exclude %_datadir/%myname/features/devmapper
%exclude %_datadir/%myname/features/lvm
%exclude %_datadir/%myname/features/luks
%exclude %_datadir/%myname/features/nfsroot
%exclude %_datadir/%myname/features/multipath
%exclude %_datadir/%myname/features/plymouth
%exclude %_datadir/%myname/features/mdadm
%exclude %_datadir/%myname/features/ucode
%doc docs/*.md

%files devmapper
%_datadir/%myname/features/devmapper

%files lvm
%_datadir/%myname/features/lvm

%files luks
%_datadir/%myname/features/luks

%files nfs
%_datadir/%myname/features/nfsroot

%files multipath
%_datadir/%myname/features/multipath

%files plymouth
%_datadir/%myname/features/plymouth

%files mdadm
%_datadir/%myname/features/mdadm

%ifarch %ix86 x86_64
%files ucode
%_datadir/%myname/features/ucode
%endif

%changelog
* Wed Jan 22 2020 Alexey Gladkov <legion@altlinux.ru> 2.4.0-alt1
- Feature changes:
  + luks: Add essiv for kernel >= 5.4.0
- Runtime changes:
  + Ignore subdirectories in the handlers directory
  + Remove obsolete debug rules
- Utilities:
  + initrd-cp: Use own helper instead of the file utility
  + depinfo: Add modules.builtin.modinfo support
- Misc:
  + Make kernel version check more human readable
  + Add helpers to compare kernel version
  + Add testsuite
  + add-module-pattern: Create tempdir in proper place

* Fri Nov 08 2019 Alexey Gladkov <legion@altlinux.ru> 2.3.0-alt1
- New feature:
  + network: New feature to configure network interfaces in initrd.
- Feature changes:
  + kbd: Configure console fonts if KMS is enabled
  + kbd: Use udev to setup font and keymap
  + kbd: Add guess-script
- Runtime changes:
  + Allow negative values in cmdline parameters
  + Rewrite network configuration
  + Allow to continue boot process after rdshell
  + Re-implement ueventd in shell
  + Allow more than one pre/post script for service
  + Allow run script before and after each service
- Utilities:
  + depinfo: Ignore files in current directory if the argument does
    not look like module name

* Thu Jul 25 2019 Alexey Gladkov <legion@altlinux.ru> 2.2.12-alt1
- Runtime changes:
  + Add /etc/sysconfig/init
  + Change activation of emergency console
  + rc.sysexec: Fix verbosity
  + simplify killall code
  + Do not print non-error messages if the 'quiet' parameter is
    specified
- Feature changes:
  + plymouth: Handle ImageDir
  + kbd: Rework feature
  + kbd: Add gzip/bzip2/xz if files are compressed

* Fri Jul 19 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.2.11-alt1
- Runtime changes:
  + Fix optional check for preloaded modules (thx Alexey Gladkov)
  + Run depmod if rd.depmod=y specified (thx Alexey Gladkov)
  + To generate fstab also read /etc/fstab.d/*.conf (thx Alexey Gladkov)
  + Fix panic=0 parameter (thx Alexey Gladkov)
  + Convert number parameter to number (thx Alexey Gladkov)
  + Do not stop process cmdline parameters on error (thx Alexey Gladkov)
  + Create /.initrd if necessary (thx Alexey Gladkov)
  + Do not umount /proc (thx Alexey Gladkov)
  + init waits for childs (thx Alexey Gladkov)
  + init do not use grep (thx Alexey Gladkov)
  + boolean variable with no value means it is set (thx Alexey Gladkov)
- Utilities:
  + initrd-cp: Ignore source file if file is already present in
    destination (thx Alexey Gladkov)
  + initrd-cp: parse ldd output more tolerant to the format (thx Alexey Gladkov)
- Feature changes:
  + multipath: Use patterns to add scsi_dh* modules (thx Alexey Gladkov)
  + plymouth: make drivers/char/agp module pattern optional
  + add-module: ignore missing module patterns too when --optional
    is passed
  + qemu: mark all added modules as optional
  + add-modules: add MODULES_TRY_ADD parameter for optional modules

* Sat Feb 16 2019 Alexey Gladkov <legion@altlinux.ru> 2.2.10-alt1
- New:
  + Add wrapper for udevd --version

* Thu Jan 31 2019 Alexey Gladkov <legion@altlinux.ru> 2.2.9-alt1
- Utilities:
  + Replace /sys by SYSFS_PATH
  + Allow to specify the modules or patterns in /lib/modules/KVER
    directory

* Thu Jan 24 2019 Alexey Gladkov <legion@altlinux.ru> 2.2.8-alt1
- Runtime changes:
  + Add service to handle x-mount-source mountpoints
- Utilities:
  + Builtin module may differ by name from the string being
    searched for.

* Tue Jan 22 2019 Alexey Gladkov <legion@altlinux.ru> 2.2.7-alt1
- Runtime changes:
  + Exclude some shell variables from the original environment
  + Allow mount anything as root from cmdline
  + Log network events
- Utilities:
  + depinfo: Add support for kernel builtins

* Fri Dec 21 2018 Alexey Gladkov <legion@altlinux.ru> 2.2.6-alt1
- Feature changes:
  + guestfs: Do not always turn off other features

* Thu Dec 20 2018 Alexey Gladkov <legion@altlinux.ru> 2.2.5-alt1
- Feature changes:
  + mdadm: Make /etc/mdadm.conf optional
  + guestfs: Show commmand before output
- New:
  + add guestfs feature (thx Alexey Shabalin)

* Mon Oct 08 2018 Alexey Gladkov <legion@altlinux.ru> 2.2.4-alt1
- Feature changes:
  + plymouth: Add uaccess and seat rules without logind calls

* Mon Oct 01 2018 Alexey Gladkov <legion@altlinux.ru> 2.2.3-alt1
- Utilities:
  + initrd-cp: Fix definition of filetype and reading the symlink

* Tue Sep 25 2018 Alexey Gladkov <legion@altlinux.ru> 2.2.2-alt1
- Feature changes:
  + plymouth: Plymouth requires udev
  + Revert "plymouth: Do not hardcode tty"

* Mon Sep 24 2018 Alexey Gladkov <legion@altlinux.ru> 2.2.1-alt1
- Add more requires
- Feature changes:
  + kbd: Fix path to consolefonts (ALT#35427)

* Tue Sep 18 2018 Alexey Gladkov <legion@altlinux.ru> 2.2.0-alt1
- Plymouth feature changes:
  + Do not hardcode tty
  + Fix service requires
- QEMU feature changes:
  + Add OF-based guess method (thx Sergey Bolshakov)
- Ucode feature changes:
  + Fix unbound function
- modules-nfs feature changes:
  + Fix pattern set
- Utilities:
  + initrd-cp: Speed up
  + make-initrd: Do not check uid if --no-check specified
  + Do not ignore error if no pattern is found
  + Add KERNEL_MODULES_DIR and remove hardcode value
  + Add /lib/udev/edd_id if exists
  + Do not hardcode LIBNAME, use getconf instead (thx Sergey Bolshakov)

* Fri Jul 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.2-alt1
- Improve compatibility with bash-4.4

* Thu May 17 2018 Alexey Gladkov <legion@altlinux.ru> 2.1.1-alt1
- Runtime changes:
  + Move functions that check real root existance into common place
  + Check and run /sbin/init-bin for backward compatibility
  + Always generate /etc/fstab

* Tue May 15 2018 Alexey Gladkov <legion@altlinux.ru> 2.1.0-alt1
- Runtime changes:
  + Remove sysvinit binary
  + Add service for emergency shell
  + Allow to customize mount options for /sys, /run
- New feature:
  + system-glibc to add additional glibc components
  + Add modules-crypto-user-api feature that contains userspace
    crypto API modules
- LUKS feature changes:
  + Fix luks2 configuration
- Ucode feature changes:
  + Make compress dependency optional
  + Remove debug
- Other fixes:
  + Fix module-* dependencies
- add-deps-ext4: Remove libcrc32c dependency
- Reduce the number of put-file calls

* Wed May 02 2018 Alexey Gladkov <legion@altlinux.ru> 2.0.10-alt2
- Remove build dependence, which was too heavy for not primary platforms.

* Tue May 01 2018 Alexey Gladkov <legion@altlinux.ru> 2.0.10-alt1
- Runtime changes:
  + Fix printf format string
- New feature:
  + Add modules-nfs feature that contains a set of NFS modules
  + Add modules-virtio feature that contains a set of virtio modules
- Ucode feature changes:
  + Fix syntax error
- New:
  + build: Add shell scripts verification using shellcheck
  + build: Move common targets on top level

* Mon Apr 30 2018 Alexey Gladkov <legion@altlinux.ru> 2.0.9-alt1
- Ucode feature changes:
  + Allow specify cpu vendor, cpu family and put all microcode
    into image
- Utilities:
  + depinfo: Fix firmware showing

* Sun Apr 29 2018 Alexey Gladkov <legion@altlinux.ru> 2.0.8-alt1
- Add wrapper to read modalias with and without new line at the end.
- Add new way to add kernel modules into initramfs.
- Add new way how to put programs into initrd.
- Add hidden ext4 dependency (ALT#34865).
- Output information about image size.
- Require kinit-utils >= 1.5.25-alt5 (ALT#34457).
- Runtime changes:
  + Add timeout after all events to avoid race conditions.
  + Allow parameter to have more than one name in /proc/cmdline.
  + Load kernel parameters from all system configuration files.
- LUKS feature changes:
  + Make luks-dev an array.
- Ucode feature changes:
  + Add optional dependency to compress feature.
- Utilities:
  + depinfo: Add softdeps to dependencies.
- Command arguments:
  + make-initrd: Check for unknown features in config.
  + bug-report: Improve bug report creation.
  + bug-report: Add kernel modules dependencies.
- New:
  + Add modules-filesystem feature.
  + Add modules-network feature.
- Old:
  + Remove lxc feature.

* Fri Jan 12 2018 Alexey Gladkov <legion@altlinux.ru> 2.0.7-alt1
- Add initrd-extract to split initramfs.
- Add feature to save information about generated initramfs.
- Feature make-initrd-ucode requires cpio (ALT#34270).
- LUKS feature changes:
  + Add luks-ignore option (thx Vladimir D. Seleznev).
  + Add luks-discard option (thx Vladimir D. Seleznev).
  + Add support for xts blockcipher (thx Vladimir D. Seleznev).
  + Add luks-key-format option.

* Wed Nov 29 2017 Alexey Gladkov <legion@altlinux.ru> 2.0.6-alt1
- Fix rootonly cmdline parameter.
- Fix handling of multiple mountpoints.
- sort-lsb: Add X-Start-Before support.
- luks:
  + Fix the password request (ALT#34257).

* Sat Nov 11 2017 Alexey Gladkov <legion@altlinux.ru> 2.0.5-alt1
- Replace parser of /proc/cmdline parameters (ALT#33712).
- Fix unbound variables cpu_vendor cpu_family (ALT#34117).

* Sat Apr 29 2017 Alexey Gladkov <legion@altlinux.ru> 2.0.4-alt3
- Move halt, replace and showenv from kinit-utils.
- luks:
  + Revert gpg support
  + Fix keyfile support

* Wed Apr 19 2017 Alexey Gladkov <legion@altlinux.ru> 2.0.4-alt2
- Fix permissions for /lib/uevent/filters/debug (ALT#33395)

* Wed Apr 19 2017 Alexey Gladkov <legion@altlinux.ru> 2.0.4-alt1
- initrd-cp:
  + Remove existing destination file before copy
- luks:
  + Add access to console
  + Add gpg encryption for keyfile
- initrd:
  + Do not mount /dev/pts (ALT#32068)

* Tue Mar 28 2017 Alexey Gladkov <legion@altlinux.ru> 2.0.3-alt3
- Change placement of initramfs helpers.

* Sun Mar 26 2017 Alexey Gladkov <legion@altlinux.ru> 2.0.3-alt2
- Rewrite ueventd.

* Tue Mar 21 2017 Alexey Gladkov <legion@altlinux.ru> 2.0.3-alt1
- Backport patches from make-initrd-0.8.14.
- Rename back to original name.

* Sun Mar 12 2017 Alexey Gladkov <legion@altlinux.ru> 2.0.2-alt1
- Add feature to control access to shell inside initrd.
- Replace put-file by standalone utility.
- ueventd process incoming events more quickly.

* Sun Jul 10 2016 Alexey Gladkov <legion@altlinux.ru> 2.0.1-alt2
- Fix install.

* Mon Jun 27 2016 Alexey Gladkov <legion@altlinux.ru> 2.0.1-alt1
- Add initrd-ls.
- Add ucode feature for early loading microcode.
- Add libnss_* only for target arch (closes: #32180).
- Add documentation (closes: #28967).
- Remove obsolete guess-kbd (closes: #29688).
- Fix compress detection for complex images.

* Mon May 02 2016 Alexey Gladkov <legion@altlinux.ru> 2.0.0-alt1
- New major release (2.0.0).
- Use sysv init in the initramfs.
- Use busybox by default.

* Fri Feb 06 2015 Anton Farygin <rider@altlinux.ru> 0.8.8-alt3
- fixed plymouth rules requires (closes: #30704)

* Fri Feb 06 2015 Anton Farygin <rider@altlinux.ru> 0.8.8-alt2
- removed `--quiet' option for `udevadm settle' (closes: #30156)

* Wed Mar 05 2014 Alexey Gladkov <legion@altlinux.ru> 0.8.8-alt1
- initrd: Remove /run size restriction.

* Tue Oct 08 2013 Alexey Gladkov <legion@altlinux.ru> 0.8.7-alt1
- Add support for mdadm >= 3.3.

* Sun Aug 18 2013 Alexey Gladkov <legion@altlinux.ru> 0.8.6-alt1
- initrd:
  + Do not remove udev database.

* Wed May 29 2013 Alexey Gladkov <legion@altlinux.ru> 0.8.5-alt1
- initrd:
  + Fix runtime message.
  + Remove lo interface before real init execution.

* Wed Mar 20 2013 Alexey Gladkov <legion@altlinux.ru> 0.8.4-alt1
- Add simple syntax check for /etc/os-release.
- Add /dev/{stdin,stdout,stderr,core,fd} to initrd.
- Add crc32c module for libcrc32c.
- depinfo: -D option.
- Fix race condition in plymouthd and plymouth show-splash (thx Anton V. Boyarshinov).

* Mon Feb 25 2013 Alexey Gladkov <legion@altlinux.ru> 0.8.3-alt1
- initrd: Add initrd-release/os-release support.
- guess: Ignore errors when resolve modalias.
- guess/keyboard: Remove obsolete code.

* Thu Feb 21 2013 Alexey Gladkov <legion@altlinux.ru> 0.8.2-alt1
- guess/net: Detect only if GUESS_NET_IFACE specified.

* Mon Feb 18 2013 Alexey Gladkov <legion@altlinux.ru> 0.8.1-alt1
- Rewrite guess modules.
- initrd: Export RD_TIMESTAMP.
- initrd: Fix root=HEX in cmdline (thx Sergey Vlasov and Alex Karpov).

* Fri Jan 25 2013 Alexey Gladkov <legion@altlinux.ru> 0.8.0-alt1
- Add possibility of do not set root=, if the booting on the same
  system as creation of initrd.
- Prevent luks activating on disassembled
  RAID components (thx Anton V. Boyarshinov).
- Add multi-mount implementation.
- Add keyboard feature.
- Add no_luks boot parameter.

* Fri Jul 20 2012 Alexey Gladkov <legion@altlinux.ru> 0.7.9-alt1
- Add qemu feature.
- Add support for udev >= 185.
- Create /run/systemd directory.
- README proofreading (thx Michael Shigorin).
- plymouth: Replace /dev/.systemd by /run/systemd.

* Mon May 14 2012 Alexey Gladkov <legion@altlinux.ru> 0.7.8-alt1
- Fix detection of builtin modules (ALT#27321).
- Add guess-modules option.
- Add --no-depmod option.

* Thu May 10 2012 Alexey Gladkov <legion@altlinux.ru> 0.7.7-alt1
- Fix behaviour in hasher environment (thx Michael Shigorin).

* Sun May 06 2012 Alexey Gladkov <legion@altlinux.ru> 0.7.6-alt1
- Rewrite put-file.
- Add support for libkmod >= 8.
- Add autodetection for raid modules (ALT#27248).
- Better handle builtin modules.

* Thu Apr 19 2012 Alexey Gladkov <legion@altlinux.ru> 0.7.5-alt1
- Ignore cachefile when running blkid (ALT#27229).

* Wed Apr 11 2012 Alexey Gladkov <legion@altlinux.org> 0.7.4-alt1
- Replay all events at system (ALT#27063).
- Add system groups/users to the image.
- Remove debug rule.

* Fri Apr 06 2012 Alexey Gladkov <legion@altlinux.ru> 0.7.3-alt1
- lvm: Fix glob in the event handler (ALT#27120) (thx Evgenii Terechkov, GalaxyMaster).
- raid, mdadm: Remove autodetection modules until it's unknown how to do it right.

* Tue Mar 06 2012 Alexey Gladkov <legion@altlinux.ru> 0.7.2-alt1
- Fix a race condition in queue processing.

* Tue Mar 06 2012 Alexey Gladkov <legion@altlinux.ru> 0.7.1-alt1
- Add initrd-diff utility (thx Evgenii Terechkov).
- Fix lvm and raid filters.

* Wed Feb 22 2012 Alexey Gladkov <legion@altlinux.ru> 0.7.0-alt1
- Add syslog feature.
- Add support for udev >= 180.
- Add the ability to handle multiple moountpoints.
- Add support for the key file in the LUKS module.
- Use /proc/mounts if rootfs not found in /etc/fstab.
- Use own utility to resolve modules, dependencies and firmware
  (don't use alt-specific modprobe option).
- Check builtin modules.
- Run depmod only once.
- initrd:
  + Use logger for messages.
  + Add libc Name Service Switch subsystem.
  + Clear and restore environ.
  + Kill all processes before the start of system init.
  + Simplify plymouth startup.
  + Always handle /run and export info real system.

* Wed Oct 26 2011 Alexey Gladkov <legion@altlinux.ru> 0.6.2-alt1
- Add support for udev >= 174.
- Run depmod before guess.
- Fix man page (ALT#25963).

* Wed Sep 14 2011 Michael Shigorin <mike@altlinux.org> 0.6.1-alt1.1
- NMU: add file to Requires: (ALT#26134).

* Sat Jun 25 2011 Alexey Gladkov <legion@altlinux.ru> 0.6.1-alt1
- Revert "Dont use alt-specific modprobe option"

* Fri Jun 24 2011 Alexey Gladkov <legion@altlinux.org> 0.6.0-alt1
- bug-report: Add proper kernel config.
- Dont use alt-specific modprobe option.
- initrd:
  + Remove hardcoded udev path.
- New:
  + Add mdadm feature.
  + Add DISABLE_FEATURES variable.
  + Add support for compressed kernel modules.

* Fri May 27 2011 Alexey Gladkov <legion@altlinux.ru> 0.5.0-alt1
- initrd:
  + Add the ability to export filesystems other than /dev.
  + Change modules order.
- plymouth:
  + Add systemd > v20 support.
- New:
  + Add systemd support.
  + Add btrfs support (ALT#25593).

* Tue Apr 26 2011 Alexey Gladkov <legion@altlinux.ru> 0.4.6-alt1
- scsi-mode: Add new feature (ALT#25388).
- Fix nfsroot boot scheme.

* Wed Mar 16 2011 Alexey Gladkov <legion@altlinux.ru> 0.4.5-alt3
- initrd: Fix events moving from udev_eventdir to handler_eventdir (ALT#25243).

* Wed Mar 16 2011 Alexey Gladkov <legion@altlinux.ru> 0.4.5-alt2
- udev: Create udev-eventdir befor udev start.
- plymouth: Fix plugin detection errors.

* Wed Mar 16 2011 Alexey Gladkov <legion@altlinux.ru> 0.4.5-alt1
- udev: Restart udev queue before running handlers (thx Kirill A. Shutemov).
- netdev: Initialize 'lo' interface only for network boot.
- Create /dev/kmsg.

* Thu Feb 24 2011 Alexey Gladkov <legion@altlinux.ru> 0.4.4-alt3
- plymouth: until plymouth does it itsself, touch /dev/.systemd/plymouth.

* Tue Feb 08 2011 Alexey Gladkov <legion@altlinux.ru> 0.4.4-alt2
- plymouth: Fix plugin detection errors.
- put-tree: Fix PUT_DIRS.

* Mon Dec 27 2010 Alexey Gladkov <legion@altlinux.ru> 0.4.4-alt1
- put-file: Fix recursion.
- make-initrd: Add --config option.
- bug-report: Add blkid output.

* Tue Dec 07 2010 Alexey Gladkov <legion@altlinux.ru> 0.4.3-alt2
- make-initrd: Fix help message.
- Move /etc/sysconfig/installkernel to bootloader-utils.

* Tue Nov 30 2010 Alexey Gladkov <legion@altlinux.ru> 0.4.3-alt1
- Move /dev into real system.
- Plymouth feature changes:
  + Check /dev/fb0 before creation.
  + Add search of the necessary modules.
  + Remove a file which creates unnecessary dependence.

* Sun Nov 14 2010 Alexey Gladkov <legion@altlinux.ru> 0.4.2-alt1
- More plymouth fixes (thx Anton V. Boyarshinov)
- Use /dev/.initramfs/root instad of /dev/root to avoid name
  collisions (ALT#24526) (thx Kirill A. Shutemov).

* Mon Nov 01 2010 Alexey Gladkov <legion@altlinux.ru> 0.4.1-alt1
- Drop devtmpfs support.
- Fix plymouth plugin detection.

* Thu Oct 28 2010 Alexey Gladkov <legion@altlinux.ru> 0.4.0-alt1
- Add devtmpfs support.
- Add plymouth support (thx Alexey Shabalin).
- Add hooks for rescue shell and for all /init stages.
- Allow to add kernel modules by pattern.
- Fix BLACKLIST_MODULES.
- luks: do not try to handle a device twice (thx Kirill A. Shutemov).

* Sun Sep 19 2010 Alexey Gladkov <legion@altlinux.ru> 0.3.9-alt1
- Search for device name in $DEVLINKS variable (ALT#24082)
- Add raid rules for udev >= 151 (ALT#23884)

* Sun Sep 05 2010 Alexey Gladkov <legion@altlinux.ru> 0.3.8-alt1
- Add multipath subpackage (ALT#24009).
- Fix typo in module name (ALT#24008).
- Fix udev rules for builtin kernel modules (ALT#23985).

* Sun Aug 29 2010 Alexey Gladkov <legion@altlinux.ru> 0.3.7-alt1
- Fix requires.
- Other fixes:
  + Fix guess-config (ALT#23956).

* Sat Aug 28 2010 Alexey Gladkov <legion@altlinux.ru> 0.3.6-alt1
- NFS feature changes:
  + preload modules only if feature enabled.
- LVM feature changes:
  + Disable udev synchronisation.
- New:
  + Add support for udev-161.
  + init: Add debug=1 option.
  + Add multipath support (untested).
  + Add possibility to check whether you need to load the kernel module.
  + Stop uevents processing while we handle arrived uevents to
    avoid race with new uevents generated by handlers.

* Tue Jun 29 2010 Alexey Gladkov <legion@altlinux.ru> 0.3.5-alt1
- bug-report: Add kernel config.
- Detect libusual.

* Fri May 28 2010 Alexey Gladkov <legion@altlinux.org> 0.3.4-alt1
- Show kernel modules list befor image creation.
- Add new features: usb, scsi-to-ide, ide-to-scsi.
- make-initrd: Add --no-checks option.
- allow user to add extra PUT_FILES and PUT_DIRS (thx Vitaly Kuznetsov).

* Fri May 07 2010 Alexey Gladkov <legion@altlinux.ru> 0.3.3-alt1
- init: Reset environment.
- Add config examples.

* Sun May 02 2010 Alexey Gladkov <legion@altlinux.ru> 0.3.2-alt1
- guess: add usb-storage and ub detection (ALT#23342).
- Add texinfo documentation.

* Fri Apr 16 2010 Alexey Gladkov <legion@altlinux.ru> 0.3.1-alt1
- Add protection from overlapping names of images (ALT#23334).
- guess: add module virtio_pci if virtio-pci detected.
- bug-report: store blkid output.
- bug-report: store more info from /proc.
- mkinitrd-make-initrd: Fix kernel version (ALT#23226).
- Fix MODULES_LOAD variable.
- Fix adding firmware.

* Wed Mar 31 2010 Alexey Gladkov <legion@altlinux.ru> 0.3.0-alt1
- Rewrite handling of udev events.
- Fix mounting the root before resume (ALT#23183).
- Fix races in the lvm activation (ALT#23077).

* Wed Mar 10 2010 Alexey Gladkov <legion@altlinux.ru> 0.2.3-alt1
- make-initrd:
  + Add INITRD_WORKDIR variable.
  + Check WORKDIR for 'noexec' mount option.
- guess-root: Ignore comments and empty strings in fstab.

* Mon Feb 22 2010 Alexey Gladkov <legion@altlinux.ru> 0.2.2-alt1
- Add wrapper to run the main program.
- Add check for AUTODETECT modules existence.
- Use mktemp for work directory.
- Fix manpage.

* Wed Feb 10 2010 Alexey Gladkov <legion@altlinux.ru> 0.2.1-alt1
- Fix user's parameters translation over environment.
- Increase verbosity.
- make-initrd:
  + Forbidden to call private goals.
  + Add help and version targets.

* Wed Feb 03 2010 Alexey Gladkov <legion@altlinux.ru> 0.2.0-alt1
- make-initrd: Add new arguments:
  + guess-config: guessing configuration;
  + bug-report: helps to generate an error report to developers.
- Introduce new flexible system for guessing configuration.
- Add BLACKLIST_MODULES variable.
- Add installkernel support.
- Fix firmware dirs (thx Valery Inozemtsev).
- Check /lib/udev/vol_id availability.
- Move make-initrd and mkinitrd-make-initrd to sbindir.

* Thu Dec 17 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.7-alt2
- Fix handling of ROOTFLAGS variable.

* Thu Dec 03 2009 Kirill A. Shutemov <kas@altlinux.org> 0.1.7-alt1
- Allow to pack few images by single make-initrd execution.
- Change boottime output and rename modules.
- Add support for /dev/disk/by-{uuid,label}/* devices.
- Fix device-mapper support.
- Rename feature 'device-mapper' to 'devmapper'.

* Mon Nov 16 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.6-alt3
- initrd.mk: Disable IMAGEFILE and use default value.
- autodetect: Fix AUTODETECT variable.
- Rename INITRD -> RUN_INITRD.
- Turn off job control for emergency shell.
- Allow ROOT=/dev/nfs.

* Fri Nov 13 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.6-alt2
- Add nfs subpackage.
- Add INITRD variable to identify initramfs.
- Minor bugfixes.

* Wed Nov 11 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.6-alt1
- Remove klibc support.

* Sun Oct 25 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.5-alt1
- Add simple RAID feature.
- Add simple NFS root support.
- Add simple network configuration.
- Add LUKS implemetation.
- Use udevsh in all udev helpers.
- device-mapper: Load dm_mod before udev.
- add-modules: Add preload-modules and load-modules stage.
- Allow to set more than one parameter with the same name.
- mkinitrd-like make-initrd wrapper (thx Alexey I. Froloff).
- RPM: Do not generate automatic requires from shebang.

* Fri Sep 04 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.4-alt2
- Fix ugly bug in cmdline parser.

* Thu Sep 03 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.4-alt1
- Fix requires;
- Fix deadlock;
- Fix parsing /proc/cmdline.
- Add docs/README.ru.

* Wed Aug 26 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.3-alt1
- Move klibc utilities from /lib/mkinitrd/klibc/bin/
  to /lib/mkinitrd/initramfs/bin/.
- Accept "3" as runlevel in command line (ALT#21103).
- Fix resume from disk (ALT#21102).

* Mon Aug 03 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.2-alt1
- Increase verbosity.
- WORKDIR is kernel-depended now.
- cleanup: Fix dependencies.

* Mon Aug 03 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.1-alt1
- Ignore modules options on copying (ALT #20936).

* Fri May 29 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.0-alt1
- First build.
