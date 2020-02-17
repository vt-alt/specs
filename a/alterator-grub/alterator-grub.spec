%define _altdata_dir %_datadir/alterator

Name: alterator-grub
Version: 0.14
Release: alt1

Summary: alterator module to setup grub bootloader
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Alterator
Source: %name-%version.tar

Requires: alterator >= 4.7-alt5
Requires: alterator-l10n >= 2.9-alt10
Requires: alterator-sh-functions >= 0.6-alt1
Requires: alterator-hw-functions >= 0.7.7-alt1
Conflicts: guile-evms < 0.4-alt13

BuildPreReq: alterator >= 4.7-alt5
BuildRequires: grub >= 2.00-alt7
BuildRequires: libdevmapper-devel

%ifarch %ix86 x86_64
Requires: grub-pc > 2.00-alt20
%endif
%ifarch aarch64 x86_64
Requires: grub-efi >= 2.00-alt12
%endif
%ifarch ppc64le
Requires: grub-ieee1275
Requires: powerpc-utils
%endif

%description
alterator module to setup grub bootloader

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*/
%_altdata_dir/steps/*
%_alterator_backend3dir/*
%dir %_libexecdir/alterator/hooks/grub.d
%_bindir/*

%changelog
* Fri Feb 07 2020 Anton Midyukov <antohami@altlinux.org> 0.14-alt1
- backend: added variant removable device for EFI (needed Secure Boot disabled)

* Thu Jan 23 2020 Nikolai Kostrigin <nickel@altlinux.org> 0.13-alt2
- fix grub bootloader installation failure if a LUKS encryption
  is chosen for root partition (closes: #28225)

* Tue Jul 16 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.13-alt1
- Added ppc64le support.

* Sat Jun 08 2019 Leonid Krivoshein <klark@altlinux.org> 0.12-alt4
- backend: add workarounds to avoid UEFI/NVRAM hardware problems
- bin/grub-disk and backend: more friendly for l10n translations

* Thu Jun 06 2019 Leonid Krivoshein <klark@altlinux.org> 0.12-alt3
- list devices and set/reset password in web-ui fixed (closes: #34208)

* Mon May 21 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12-alt2
- do not require grub-pc on non-pc

* Wed Mar 21 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.12-alt1
- added display of the default username (closes: #33098, #34249)
- disabled web-ui (until solved #34208)
- update requires (grub2 -> grub)

* Fri Jun 10 2016 Michael Shigorin <mike@altlinux.org> 0.11-alt1
- added test to exclude hybrid installation media
  (usually USB Flash drive with ISO written onto it)
  from bootloader installation targets

* Wed Dec 02 2015 Michael Shigorin <mike@altlinux.org> 0.10-alt1
- added GRUB2 hashed password support
- NB: depends on fixes made after grub-2.00-alt20 to *not* require
      boot password given default boot options for a menuentry

* Tue Sep 02 2014 Michael Shigorin <mike@altlinux.org> 0.9.10-alt1
- care for efivars

* Wed Jun 11 2014 Michael Shigorin <mike@altlinux.org> 0.9.9-alt1
- convert GRUB_AUTOUPDATE_DEVICE members to stable symlinks (closes: #29546)

* Thu Jan 23 2014 Michael Shigorin <mike@altlinux.org> 0.9.8-alt1
- force shim installation even if SecureBoot is not there
  during install (so that the bootloader doesn't turn into
  a pumpkin when SB is suddenly turned on or the disk is
  moved into another system)

* Mon Mar 04 2013 Michael Shigorin <mike@altlinux.org> 0.9.7-alt1
- do not force ESP subdir name onto grub-install;
  thus it's changed from "ALT Linux" to "altlinux"
  given the fixes in grub2-2.00-alt12

* Wed Feb 27 2013 Michael Shigorin <mike@altlinux.org> 0.9.6-alt1
- fixed install-to-partition by working around i18n (see also #28600)

* Thu Feb 07 2013 Michael Shigorin <mike@altlinux.org> 0.9.5-alt1
- backend: use LANG variable

* Fri Feb 01 2013 Michael Shigorin <mike@altlinux.org> 0.9.4-alt1
- fix adding BIOS boot targets in EFI mode

* Thu Jan 31 2013 Michael Shigorin <mike@altlinux.org> 0.9.3-alt1
- make temporary file in proper location (thanks sem@

* Wed Jan 30 2013 Michael Shigorin <mike@altlinux.org> 0.9.2-alt1
- filter out boot device

* Tue Jan 29 2013 Michael Shigorin <mike@altlinux.org> 0.9.1-alt1
- add BIOS boot targets even in EFI case

* Tue Dec 18 2012 Michael Shigorin <mike@altlinux.org> 0.9-alt2
- added arch-specific grub2-efi dependency

* Thu Dec 06 2012 Michael Shigorin <mike@altlinux.org> 0.9-alt1
- dropped EVMS specific hacks (see also #28181)

* Wed Nov 21 2012 Michael Shigorin <mike@altlinux.org> 0.8.1-alt1
- amended EFI support (closes: #27972)

* Thu Nov 15 2012 Michael Shigorin <mike@altlinux.org> 0.8-alt1
- added initial EFI support

* Thu Nov 08 2012 Michael Shigorin <mike@altlinux.org> 0.7-alt5
- replace symlink with bindmount for grub 2.00

* Wed Nov 07 2012 Timur Aitov <timonbl4@altlinux.org> 0.7-alt4
- add hack for luks devices

* Thu Jun 16 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt3
- mike@: set default input focus to the combobox

* Mon Jun 06 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt2
- fix grub install into partition (ALT #25628)

* Mon May 30 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt1
- add /dev/emvs/md hackaround

* Tue Feb 15 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt2
- rebuild with new libdevmapper versioning

* Mon Jan 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt1
- install into partition in installer fixed (ALT #24617)

* Wed Oct 27 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt4
- fisttime script moved to the grub2 package

* Wed Oct 27 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt3
- "one time system" effect fixed

* Tue Oct 26 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt2
- typo fixed

* Mon Oct 25 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt1
- firttime script added

* Sun Oct 24 2010 Andrey Cherepanov <cas@altlinux.org> 0.4-alt2
- localize backend scripts

* Mon Oct 04 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt1
- allow grub install on partition using blocklists (ALT #24197)
- set GRUB_AUTOUPDATE_DEVICE and GRUB_AUTOUPDATE_FORCE options

* Tue Sep 21 2010 Anton Protopopov <aspsk@altlinux.org> 0.3-alt7
- Add dirty hack to install grub2 on lvm

* Mon Jun 28 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt6
- do not try to install bootloader on floppy (ALT #23687)

* Tue Jun 01 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt5
- do not try to install bootloader on cd/dvdrom

* Fri Apr 23 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt4
- include removable devices in proposed locations

* Mon Mar 29 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt3
- avoid conflict with alterator-lilo

* Fri Mar 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt2
- reuse devmap_name from alterator-lilo

* Fri Mar 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1
- "skip bootloader install" added
- fix 'set bootable'
- fix typo

* Thu Mar 25 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt8
- simplify raid handling

* Wed Mar 24 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt7
- another fox for raid install
- more verbose error handling

* Wed Mar 24 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt6
- fix raid install

* Tue Mar 23 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt5
- fix grub-install fail on some devices

* Fri Mar 19 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt4
- just another possible installer fix

* Thu Mar 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt3
- possible installer fix

* Tue Mar 16 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2
- step file packaged

* Mon Mar 15 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- step file added

* Fri Mar 12 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1
- Initial
