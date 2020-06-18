Name: livecd-install
Version: 0.9.14
Release: alt1

Summary: Permanently install Live system
License: GPLv2
Group: System/Configuration/Other

Source: %name-%version.tar
Source1: %name.pam
Source2: %name.apps

Url: http://www.altlinux.org/Alterator
Packager: Andriy Stepanov <stanv@altlinux.ru>

BuildArch: noarch
BuildRequires(pre): rpm-macros-alternatives
Requires: alterator-wizardface
Requires: alterator-livecd >= 0.5-alt1
Requires: alterator-vm alterator-users >= 10.2-alt1 alterator-root >= 0.9-alt1 alterator-datetime >= 2.6 alterator-notes
Requires: alterator-service-functions
Requires: installer-scripts-remount-stage2 >= 0.3-alt1
Requires: livecd-evms
#Requires: make-initrd-plymouth
Requires: consolehelper

# Alterator-vm always allow to create an encrypted partition.
# So always install alterator-luks.
Requires: alterator-luks >= 0.2.1-alt1
Requires: make-initrd-luks

Requires(post): chkconfig
Requires(preun): chkconfig

# There was 'removable' initinstall hook
Conflicts: installer-feature-simply-livecd < 0.8.4-alt1

%description
%summary

%prep
%setup

%install
%makeinstall
install -D -p -m 0644 %{S:1} %buildroot%_sysconfdir/pam.d/%name
install -D -p -m 0644 %{S:2} %buildroot%_sysconfdir/security/console.apps/%name
install -d -m 0755 %buildroot%_bindir
ln -s %_libexecdir/consolehelper/helper %buildroot%_bindir/%name
mkdir -p %buildroot%_x11sysconfdir/profile.d
install -m 0755 zdg-user-dirs-install.sh %buildroot%_x11sysconfdir/profile.d/

%files
%config(noreplace) %_sysconfdir/%name
%_altdir/livecd-install.steps
%_bindir/%name
%_sbindir/%name
%config(noreplace) %_sysconfdir/pam.d/%name
%config(noreplace) %_sysconfdir/security/console.apps/%name
%_datadir/alterator/steps/*
%_libexecdir/alterator/hooks/livecd-*.d/*
%_desktopdir/*.desktop
%_x11sysconfdir/profile.d/*

%changelog
* Wed Mar 18 2020 Anton Midyukov <antohami@altlinux.org> 0.9.14-alt1
- Restore all kernels

* Sun Jan 12 2020 Anton Midyukov <antohami@altlinux.org> 0.9.13-alt1
- 50-restore-kernel.sh: copy kernel from EFI/BOOT

* Mon Jan 06 2020 Anton Midyukov <antohami@altlinux.org> 0.9.12-alt1
- copy kernel from /images/boot if not in /images/sylinux/alt0

* Tue Apr 23 2019 Anton Midyukov <antohami@altlinux.org> 0.9.11-alt1
- Not restart systemd-logind

* Mon Oct 01 2018 Michael Shigorin <mike@altlinux.org> 0.9.10-alt5
- avoid R: make-initrd-plymouth, should be added in the profile
  if needed (closes: #35461)

* Thu Aug 09 2018 Michael Shigorin <mike@altlinux.org> 0.9.10-alt4
- BR(pre): rpm-macros-alternatives (thx ldv@)

* Tue Jan 23 2018 Paul Wolneykien <manowar@altlinux.org> 0.9.10-alt3
- Fix: Depend on alterator-notes.

* Tue Jan 16 2018 Paul Wolneykien <manowar@altlinux.org> 0.9.10-alt2
- Adapt for the multi-arch build: do not require alterator-grub any more.

* Thu Aug 17 2017 Paul Wolneykien <manowar@altlinux.org> 0.9.10-alt1
- Use /etc/alternatives for the installer steps configuration.

* Tue Aug 08 2017 Michael Shigorin <mike@altlinux.org> 0.9.9-alt1
- Umount any udisks-mounted filesystems (as we ask anyways).

* Fri Mar 31 2017 Mikhail Efremov <sem@altlinux.org> 0.9.8-alt1
- 40-autohostname.sh: Don't setup /etc/HOSTNAME.

* Thu Dec 15 2016 Michael Shigorin <mike@altlinux.org> 0.9.7-alt1
- Update for rpm 4.13 (harden against missing packages to be removed).

* Tue Nov 22 2016 Michael Shigorin <mike@altlinux.org> 0.9.6-alt1
- Revert the change made in 0.9.2-alt1 (closes: #32777).

* Tue Nov 15 2016 Michael Shigorin <mike@altlinux.org> 0.9.5-alt1
- Deactivate EVMS if a previous run has got down to
  disk partitioning but not through (closes: #31582).
- Update the icon in desktop file. :)

* Fri Apr 08 2016 Michael Shigorin <mike@altlinux.org> 0.9.4-alt1
- Drop dconf hook (thanks shaba@).
  + NB: incompatible with p7/t7!

* Tue Jun 16 2015 Michael Shigorin <mike@altlinux.org> 0.9.3-alt1
- Security fix: purge LiveCD's sudoers (closes: #31071).

* Fri Apr 24 2015 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt1
- Use alterator-service-functions.
- Setup and save /etc/adjtime.

* Wed Jun 11 2014 Michael Shigorin <mike@altlinux.org> 0.9.1-alt1
- Added 45-mdadm.sh from installer.

* Fri Apr 25 2014 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- Care to transfer NM/connman and runtime /etc/net configurations too.

* Tue Mar 18 2014 Michael Shigorin <mike@altlinux.org> 0.8.11-alt1
- Remove autologin and nodm packages too.

* Thu Sep 26 2013 Michael Shigorin <mike@altlinux.org> 0.8.10-alt1
- Remove 'altlinux' group too.

* Wed Sep 18 2013 Michael Shigorin <mike@altlinux.org> 0.8.9-alt1
- Handle dconf and localectl configuration (see #28991).

* Fri Jun 07 2013 Michael Shigorin <mike@altlinux.org> 0.8.8-alt1
- Add Ukrainian translation to desktop file.

* Wed May 29 2013 Mikhail Efremov <sem@altlinux.org> 0.8.7-alt1
- Add disable-efivars postinstall hook.

* Mon May 27 2013 Mikhail Efremov <sem@altlinux.org> 0.8.6-alt1
- Add 'removable' initinstall hook.

* Thu Apr 18 2013 Mikhail Efremov <sem@altlinux.org> 0.8.5-alt1
- setup-plymouth: Disable plymouth if root on luks only.

* Thu Mar 28 2013 Mikhail Efremov <sem@altlinux.org> 0.8.4-alt1
- Fix firsttime flag-file path.

* Mon Mar 04 2013 Michael Shigorin <mike@altlinux.org> 0.8.3-alt1
- Fixed plymouth setup script to be more careful
  ("splash" FP was ruining GRUB_WALLPAPER path).

* Thu Feb 21 2013 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt1
- Turn off autologin in case of lightdm too.

* Tue Feb 12 2013 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1
- Added cp-installer-logs postinstall hook (closes: #28537).
- remove-livecd-pkgs: Remove alterator-luks.

* Fri Feb 08 2013 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- Replace bootsplash hook with setup-plymouth hooks.
- Added make-initrd-luks to requires.
- Added crypttab preinstall hook.

* Wed Feb 06 2013 Mikhail Efremov <sem@altlinux.org> 0.7.3-alt1
- Added alterator-luks to requires.
- Added disable-privatetmp initinstall hook.

* Mon Feb 04 2013 Mikhail Efremov <sem@altlinux.org> 0.7.2-alt1
- Drop steps/luks.desktop.

* Wed Jan 30 2013 Michael Shigorin <mike@altlinux.org> 0.7.1-alt1
- destination /etc/fstab is being cared for by i-s-remount

* Thu Jan 10 2013 Mikhail Efremov <sem@altlinux.org> 0.7-alt1
- Added setup-network and autohostnameh preinstall hooks.

* Thu Dec 27 2012 Michael Shigorin <mike@altlinux.org> 0.6-alt11
- added luks.desktop as well

* Wed Dec 26 2012 Michael Shigorin <mike@altlinux.org> 0.6-alt10
- added luks to steps (but not to deps)
- minor spec cleanup
- added an Url:

* Wed Dec 19 2012 Michael Shigorin <mike@altlinux.org> 0.6-alt9
- added alterator-datetime to Requires: (as it's in steps)

* Wed Jun 27 2012 Mikhail Efremov <sem@altlinux.org> 0.6-alt8
- preinstall hooks: Add rm-issue.

* Thu Sep 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt7
- remove alterator-wisardf*, not only alterator-wisardface

* Thu Jun 30 2011 Mikhail Efremov <sem@altlinux.org> 0.6-alt6
- remove-livecd-pkgs: Remove branding-*-slideshow.

* Tue Jun 28 2011 Mikhail Efremov <sem@altlinux.org> 0.6-alt5
- Add License install step.

* Thu Jun 16 2011 Mikhail Efremov <sem@altlinux.org> 0.6-alt4
- remove-livecd-pkgs: preinstall -> postinstall stage.
- remove-livecd-pkgs: remove more packages.

* Fri Jun 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt3
- put livecd-install.desktop only if UID==500

* Mon Jun 06 2011 Mikhail Efremov <sem@altlinux.org> 0.6-alt2
- Add postinstall firsttime hook.
- preinstall hooks: Use digital prefix.

* Thu Jun 02 2011 Mikhail Efremov <sem@altlinux.org> 0.6-alt1
- livecd-postinstall.d -> livecd-preinstall.d.
- Drop hal.sh hook.

* Mon Apr 25 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt1
- put install icon on desktop

* Tue Apr 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt3
- plymouth setup added

* Wed Apr 13 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt2
- turn GdM autologin off

* Tue Apr 12 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- use grub instead lilo

* Mon Aug 10 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- fix application name (closes: #20601)
- improve some livecd-postinstall.d scripts
- don't umount partitions with newly installed system
- move profile specific data from general framework package

* Fri Jun 19 2009 Andriy Stepanov <stanv@altlinux.ru> 0.2-alt1
- Adjust date time at running Live, then copy settings.
  Export $ALTERATOR_DESTDIR

* Wed Jun 17 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt8
- Use consolehelper

* Tue Jun 16 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt7
- umount bind over bind

* Tue Jun 16 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt6
- after installation umount all FS at $target_dir

* Tue Jun 09 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt5
- Correct .desktop file

* Thu Jun 04 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt4
- Add step: ditetime

* Thu Jun 04 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt3
- Add steps: root, users

* Fri May 29 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt2
- Add dependency to lived-evms

* Fri May 29 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt1
- Initial build
