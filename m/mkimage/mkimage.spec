Name: mkimage
Version: 0.2.30
Release: alt1

Summary: Simple image creator
License: GPL3
Group: Development/Other

Packager: Alexey Gladkov <legion@altlinux.ru>
BuildArch: noarch

Requires: libshell >= 0.0.2
Requires: hasher >= 1.3.7-alt1

Url: http://altlinux.org/mkimage
Source: %name-%version.tar

%define sysctldir %_sysconfdir/sysctl.d
%define procfile /proc/sys/fs/protected_hardlinks

%description
mkimage is a tool for building ALT Linux distribution
ISO images out of a user-supplied set of configuration
files (called `templates').

%package preinstall
Summary: Security setup for mkimage to function properly
Group: Development/Other

%description preinstall
This package contains settings allowing mkimage to operate
as intended -- it relies on hardlinks to non-owned files to
spare space for copies within and outside chroots as well as
to save time and CPU cycles on actually performing those;
either free RAM, SSD wearing or HDD bandwidth are to be
spent with care too).

Please note that this subpackage disables an otherwise reasonable
security feature that's there for a reason but is almost completely
incompatible with important part of mkimage's design and security
model.  Changes take place upon the installation of this package
and are made persistent by a configuration file held within it.

Remove %name-preinstall subpackage and run this to re-enable:

  echo 1 > %procfile

(this will break mkimage though)

%prep
%setup

%build
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%sysctldir
echo "fs.protected_hardlinks = 0" > %buildroot%sysctldir/49-%name.conf
ln -s 49-%name.conf %buildroot%sysctldir/51-%name.conf	# *sigh*

%post
if grep -Fqsx 1 "%procfile"; then
	echo "warning: mkimage won't work, see %name-preinstall" >&2
fi

%post preinstall
if grep -Fqsx 1 "%procfile"; then
	echo "%name-preinstall: allowing to hardlink non-owned files..." >&2
	echo 0 > %procfile
fi

%files
%_bindir/*
%_datadir/%name
%doc examples doc/README.ru

%files preinstall
%config(noreplace) %sysctldir/??-%name.conf

# TODO:
# - consider %%postun preinstall to restore the variable value
# - maybe Require: %%name-preinstall in the main package sometime later

%changelog
* Tue Feb 25 2020 Anton Midyukov <antohami@altlinux.org> 0.2.30-alt1
- mki-copy-ieee1275boot: replaced alt0 to boot
- mki-copy-grubaa64boot, mki-pack-efionly-isoboot: replaced grub-efi
to EFI/BOOT

* Thu Nov 14 2019 Alexey Shabalin <shaba@altlinux.org> 0.2.29-alt1
- Added support grub-efi to efiboot

* Fri Sep 13 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.28-alt1
- Added support for aarch64 systems (grub-efi boot from ISO-9660)
  by klark@ and shaba@).
- Added hasher >= 1.4.0 support.

* Tue Jul 09 2019 Alexey Gladkov <legion@altlinux.ru> 0.2.27-alt1
- Add support for Open Firmware/OpenBoot/IEEE1275 firmware (glebfm@)

* Thu Jun 13 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.2.26-alt1
- mki-copy-pkgs: bisection improved

* Tue Mar 19 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.2.25-alt1
- mki-copy-efiboot: add support for signed shimia32 by default if available
  + clean up code
- fix a copy-pasted typo in an error message

* Wed Oct 03 2018 Nikolai Kostrigin <nickel@altlinux.org> 0.2.24-alt1
- mki-copy-efiboot: extract refind_ia32.efi config options into separate file

* Mon Sep 17 2018 Michael Shigorin <mike@altlinux.org> 0.2.23-alt1
- mki-pack-isodata: drop extra quotes that hurt (closes: #35229)

* Thu Sep 13 2018 Nikolai Kostrigin <nickel@altlinux.org> 0.2.22-alt1
- mki-copy-efiboot: reserve enough space for EFI fs(closes: #35270)

* Mon Aug 27 2018 Alexey Gladkov <legion@altlinux.ru> 0.2.21-alt1
- Sort packages list by default
- Add README.md and LICENSE

* Fri Jul 20 2018 Nikolai Kostrigin <nickel@altlinux.org> 0.2.20-alt1
- mki-copy-efiboot: add ia32 EFI boot support for x86_64 platforms

* Sun Dec 03 2017 Anton Farygin <rider@altlinux.ru> 0.2.19.2-alt1
- mki-copy-efiboot: adjusted for refind-0.11.2

* Wed Jan 11 2017 Michael Shigorin <mike@altlinux.org> 0.2.19.1-alt1
- preinstall:
  + added 51- to 49- to encircle 50-default regardless of order
  + dropped R: sysfsutils as irrelevant (thx snejok@)

* Wed Jan 11 2017 Michael Shigorin <mike@altlinux.org> 0.2.19-alt1
- preinstall: fixed sysctl file name, *thanks* snejok@ (closes: #30351)
- mki-copy-efiboot: adjusted for dosfstools-3.0 either

* Sat Jun 11 2016 Michael Shigorin <mike@altlinux.org> 0.2.18-alt1
- mki-copy-efiboot: adjusted for dosfstools-4.0

* Mon Mar 09 2015 Michael Shigorin <mike@altlinux.org> 0.2.17-alt1
- mki-copy-efiboot: added EFI_BOOTARGS support

* Fri Aug 15 2014 Michael Shigorin <mike@altlinux.org> 0.2.16-alt1
- mki-sh-functions: cope with umask 007 (thanks mithraen@)

* Mon Jun 02 2014 Michael Shigorin <mike@altlinux.org> 0.2.15-alt1
- added /proc support for mksquashfs 4.3

* Wed Apr 30 2014 Michael Shigorin <mike@altlinux.org> 0.2.14-alt1
- mki-copy-efiboot: minor enhancements

* Wed Apr 30 2014 Michael Shigorin <mike@altlinux.org> 0.2.13-alt1
- mki-copy-efiboot:
  + rescue: added forensic mode support
  + secondary refind switched to text mode

* Sat Mar 01 2014 Michael Shigorin <mike@altlinux.org> 0.2.12.2-alt1
- preinstall subpackage: added missing dependency (thanks Speccyfighter)

* Wed Dec 25 2013 Michael Shigorin <mike@altlinux.org> 0.2.12.1-alt1
- mki-copy-efiboot: rescue needs no bootsplash

* Sun Dec 22 2013 Michael Shigorin <mike@altlinux.org> 0.2.12-alt1
- mki-copy-efiboot: further refactoring and fixups
  + hardlink image contents
  + added efi-memtest86 support
  + reworked refind installation
- added Url:

* Wed Dec 18 2013 Michael Shigorin <mike@altlinux.org> 0.2.11-alt1
- mki-copy-efiboot: refactored EFI support
  + drop -signed subpackages as irrelevant
  + added multiple stage2, refind branding support

* Thu Nov 07 2013 Michael Shigorin <mike@altlinux.org> 0.2.10-alt1
- mki-image-prepare: fixed the change made in 0.2.9 (ldv@) (ALT#29558)

* Fri Oct 18 2013 Michael Shigorin <mike@altlinux.org> 0.2.9-alt3
- %%post scriptlet simplification (thx ldv@)

* Fri Oct 18 2013 Michael Shigorin <mike@altlinux.org> 0.2.9-alt2
- fixed eval-order-thinko in %%post scriptlet, sorry

* Wed Oct 16 2013 Michael Shigorin <mike@altlinux.org> 0.2.9-alt1
- added preinstall subpackage which is basically required
  to be installed since Linux 3.6

* Fri Feb 22 2013 Michael Shigorin <mike@altlinux.org> 0.2.8-alt1
- example{3,4}: updated for current make-initrd (see #28578)
- minor spec cleanup

* Thu Feb 21 2013 Michael Shigorin <mike@altlinux.org> 0.2.7-alt1
- mki-copy-efiboot: essentially rewritten again
  + avoid undefined EFI_CERT variable error
  + copy EFI shell if requested
  + complement refind with elilo (for UEFI SB case)
  + added locale submenu to refind
  + put certificate in itw own directory

* Tue Jan 15 2013 Alexey Gladkov <legion@altlinux.ru> 0.2.6-alt1
mki-print-uris: Guarantee newline at the end.
mki-pack-isoboot: make xorriso *read* the config (thx Michael Shigorin).
mki-pack-isoboot: introduced ISOHYBRID variable (thx Michael Shigorin).
mki-copy-efiboot: rewrite, extend and cleanup (thx Michael Shigorin).

* Sat Dec 15 2012 Michael Shigorin <mike@altlinux.org> 0.2.5-alt1
- Initial EFI bootloader support (including example4).

* Thu Dec 13 2012 Michael Shigorin <mike@altlinux.org> 0.2.4-alt1
- mki-pack-boot: made mki-build-propagator call conditional
- example3: added propagator explicitly (m-i-p no longer pulls it in)

* Sun Jul 22 2012 Alexey Gladkov <legion@altlinux.ru> 0.2.3-alt1
- mki-count-cpu: Get the number of processors in different ways (ALT#27136).
- mki-pack-squash: do not need no recovery info.
- mki-pack-ubifs: Allow ubifs image packing.

* Tue Jan 17 2012 Michael Shigorin <mike@altlinux.org> 0.2.2-alt1
- tools/mki-pack-{isodata,isoboot,yaboot}: added mkisofs -sort support

* Fri Dec 09 2011 Alexey Gladkov <legion@altlinux.ru> 0.2.1-alt1
- tools/mki-scripts: Allow symlinks (ALT#26487).
- example3: fixup for current Sisyphus (ALT#26591)

* Fri Sep 02 2011 Alexey Gladkov <legion@altlinux.org> 0.2.0-alt1
- conditionally set IMAGE_INIT_LIST (ALT#26135).
- example3: updated base/packages (thx Michael Shigorin).
- tools/mki-copy-pkgs: split processing of pkglists (thx Michael Shigorin).
- tools/mki-copy-isolinux: handle kernel absence (thx Michael Shigorin).

* Sun Apr 17 2011 Alexey Gladkov <legion@altlinux.ru> 0.1.9-alt1
- Add xz support.

* Sun Jan 23 2011 Alexey Gladkov <legion@altlinux.ru> 0.1.8-alt1
- mki-build-propagator: Fix for bootloader-utils-0.4.11-alt1 (ALT#24850).

* Thu Dec 16 2010 Alexey Gladkov <legion@altlinux.ru> 0.1.7-alt1
- Fix IMAGE_PACKAGES_* expansion (ALT#24669).
- mki-expand-pkgs: Fixed output with verbose enabled.

* Tue Oct 05 2010 Alexey Gladkov <legion@altlinux.ru> 0.1.6-alt1
- mki-pack-results: Fix MKI_IMAGESUBDIR (ALT#24120).
- Add example3 (thx Michael Shigorin).

* Fri Sep 03 2010 Alexey Gladkov <legion@altlinux.ru> 0.1.5-alt1
- mki-pack-tar: Fix syntax error.

* Fri Aug 20 2010 Alexey Gladkov <legion@altlinux.ru> 0.1.4-alt1
- Add gfxboot support for isolinux images (Sergey V Turchin)
- Add squashfsprogs-lzma support
- MKI_PACK_RESULTS: Add directory exclusion support
- Update documentation

* Mon Jun 08 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.3-alt1
- Make a configurable list of packages for each stage
- Workaround for stupid squashfsprogs
- Move propagator variables to standalone file
- Dont quote strings in .mkisofsrc
- Update README.ru

* Mon May 25 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.2-alt1
- mki-pack-custom: Fix execution (ALT#20093)
- Add examples/example2/.mki/.gitignore
- Add COPYING

* Fri Mar 27 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.1-alt1
- targets.mk: clean-current: remove .work symlink, if it's broken.
- Add TOPDIR and PREVDIR into config.mk.
- Add another example.
- Update README.ru.

* Tue Nov 11 2008 Alexey Gladkov <legion@altlinux.ru> 0.1.0-alt2
- Fix requires.

* Mon Nov 10 2008 Alexey Gladkov <legion@altlinux.ru> 0.1.0-alt1
- Targets:
  + Fix error handler for copy-packages and build-image.
  + Add rule for invalidate cache of defined targets.
- Add support for PPC bootable images (thx Sergey Bolshakov).
- Write stage result into outdir directly.
- Move all temp scripts into /.host directory.
- mki-build-propagator: Move /.image/syslinux/alt0/full.cz -> /boot/full.cz.
- mki-pack-cpio: Suppress EPERM messages.
- mki-pack-cpio: Fix compress methods.

* Wed Aug 13 2008 Alexey Gladkov <legion@altlinux.ru> 0.0.9-alt1
- mki-pack-squash: Add PACK_SQUASHFS_OPTS to be able to use the
  mksquashfs with additional options.
- targets.mk.in:
  + Add debug rule.
  + Disable command echoing.
  + New option GLOBAL_WORKROOT (legion, kas, #14502).
- examples/example1:
  + Do not overwrite OUTDIR (kas).
  + Update script 999-system and use target run-image-scripts
    instead of run-scripts (kas).
  + Update modules (kas).
  + Use std-def kernel instead of std-smp to fix building on Sisyphus (kas).

* Mon Jun 23 2008 Alexey Gladkov <legion@altlinux.ru> 0.0.8-alt1
- Increase verbosity.
- Update examples.
- Update documentation.
- Add IMAGE_INIT_LIST to change hasher init list.
- mki-build-propagator: Always follow symlinks in
  PROPAGATOR_MAR_MODULES and PROPAGATOR_INITFS.
- mki-scripts: Allow to read to scripts GLOBAL_* env variables.
- mki-cache-run-scripts: Check scriptdir existence.
- mki-pack-tar:
  + Fix compress options.
  + Add lzma compress method.
  + Install compess program into the chroot.
- mki-pack-data:
  + Ignore hasher directories.
  + Return error if MKI_IMAGESUBDIR not found.
- mki-pack-results: Allow MKI_PACK_RESULTS=data.

* Fri Mar 14 2008 Alexey Gladkov <legion@altlinux.ru> 0.0.7-alt3
- mki-build-propagator: adapted for both mkmar & mkmodpack.
- targets.mk: Fix typo.

* Sun Mar 02 2008 Alexey Gladkov <legion@altlinux.ru> 0.0.7-alt2
- mki-pack: Add 'cpio' pack method.
- mki-pack-boot: Add 'syslinux' boot method.
- mki-pack-data: Use MKI_OUTNAME variable.
- mki-copy-tree: Fix ownership at copying data from /.in to /.image.

* Sun Feb 24 2008 Alexey Gladkov <legion@altlinux.ru> 0.0.7-alt1
- New version (0.0.7).
- Allow stage remote build.
- Allow subdirectories in SUBDIRS.
- Add BOOT_LANG variable to able set default boot language.
- Split rules.mk into separate files: config.mk, tools.mk and targets.mk.
- Fix .fakedata check.
- Fix 'data' and 'custom' methods.
- Fix makefile hardcode.
- Fix NO_CACHE option.
- Update README.ru.

* Wed Jan 09 2008 Alexey Gladkov <legion@altlinux.ru> 0.0.6-alt2
- Fix requires.

* Mon Dec 17 2007 Alexey Gladkov <legion@altlinux.ru> 0.0.6-alt1
- New version (0.0.6).
- Add another method to describe 'pack-image' logic. Variables MKI_OUTNAME and
  MKI_PACKTYPE are obsoletes. Use MKI_PACK_RESULTS instead.
- Add 'split' target.
- Add package names expand methods for 'build-image' and 'copy-packages' targets.
- Rename mki-pack-tarbz2 -> tools/mki-pack-tar.

* Wed Oct 31 2007 Alexey Gladkov <legion@altlinux.ru> 0.0.5-alt2
- Fix REQUIRES variable parsing.

* Mon Oct 15 2007 Alexey Gladkov <legion@altlinux.ru> 0.0.5-alt1
- New version (0.0.5).
- Added qemu support (kas@).
- Rename GLOBAL_LANG to GLOBAL_HSH_LANG.
- Variable CLEANUP_OUTDIR is enabled by default.
- New method of conflicts resolution in packages list.
- Fix cache generation.

* Mon Oct 08 2007 Alexey Gladkov <legion@altlinux.ru> 0.0.4-alt1
- New version (0.0.4).
- Ignore scripts with '~', '.bak', '.rpmnew' and '.rpmsave' suffix.
- Packages list allow matches grouping.
- Add support for --install-langs (boyarsh@).
- Add creating console/tty/tty0 in chroots (boyarsh@).

* Mon Oct 01 2007 Alexey Gladkov <legion@altlinux.ru> 0.0.3-alt1
- New version (0.0.3).

* Fri Sep 21 2007 Alexey Gladkov <legion@altlinux.ru> 0.0.2-alt1
- New version (0.0.2).

* Thu Aug 30 2007 Alexey Gladkov <legion@altlinux.ru> 0.0.1-alt1
- First build for ALT Linux.
