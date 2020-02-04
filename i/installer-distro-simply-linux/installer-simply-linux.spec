Name: installer-distro-simply-linux
Version: 9.2.1
Release: alt1

Summary: Installer common files
Summary(ru_RU.UTF-8): Общие пакеты для установки дистрибутива "Simply linux"
License: GPLv2+
Group: System/Configuration/Other
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: alterator rpm-devel

%description
Installer common files

%description -l ru_RU.UTF-8
Виртуальный пакет содержащий зависимости на необходимые пакеты и настройки
для установки дистрибутива "Просто линукс" (Simply linux).

%package stage2
Summary: Installer stage2
Summary(ru_RU.UTF-8): Пакеты необходимые на втором этапе установки Simply linux
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: installer-stage2
#fonts
# Not needed, will be added by m-p profile itself
#Requires: fonts-ttf-google-droid-sans
#modules
Requires: alterator-sysconfig
Requires: alterator-license
#Requires: alterator-auth
Requires: alterator-datetime >= 4.0
Requires: chrony
Requires: alterator-vm
Requires: alterator-pkg
Requires: alterator-luks
Requires: x-cursor-theme-jimmac
#features
Requires: installer-feature-autohostname-stage2
Requires: installer-feature-desktop-disable-remote-stage2
Requires: installer-feature-desktop-other-fs-stage2
Requires: installer-feature-desktop-suspend-stage2
Requires: installer-feature-hwtweaks-stage2
Requires: installer-feature-local-clock
Requires: installer-feature-runlevel5-stage2
Requires: installer-feature-samba-usershares-stage2
Requires: installer-feature-slideshow
Requires: installer-feature-xdg-user-dirs

Provides: installer-lite-stage2
Provides: installer-simply-linux-stage2
Obsoletes: installer-simply-linux-stage2

%description stage2
Installer stage2

%description stage2 -l ru_RU.UTF-8
Данный виртуальный пакет зависит от пакетов необходимых на втором этапе
установки дистрибутива "Просто линукс" (Simply linux).

%package stage3
Summary: Installer stage3
Summary(ru_RU.UTF-8): Пакеты необходимые на третьем этапе установки Simply linux
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: installer-stage3
#modules
Requires: alterator-grub
Requires: alterator-users
Requires: alterator-root
Requires: alterator-net-eth dhcpcd
Requires: alterator-luks
#Requires: alterator-x11
#features
Requires: installer-feature-bell-off-stage3
Requires: installer-feature-lightdm-stage3
Requires: installer-feature-nfs-client-stage3
Requires: installer-feature-online-repo
Requires: installer-feature-repo-add
Requires: installer-feature-setup-network-stage3
Requires: installer-feature-sudo-enable-by-default-stage3

Provides: installer-lite-stage3
Provides: installer-simply-linux-stage3
Obsoletes: installer-simply-linux-stage3

%description stage3
Installer stage3

%description stage3 -l ru_RU.UTF-8
Данный виртуальный пакет зависит от пакетов необходимых на третьем этапе
установки дистрибутива "Просто линукс" (Simply linux).

%prep
%setup -q

%install
%makeinstall

%find_lang alterator-simply-linux

%files -f alterator-simply-linux.lang
%_datadir/alterator/steps/*

%files stage2
%_datadir/install2/installer-steps
%_datadir/install2/*.d/*
%_datadir/install2/steps/*
%_datadir/install2/alterator-menu

%files stage3

%changelog
* Mon Feb 03 2020 Michael Shigorin <mike@altlinux.org> 9.2.1-alt1
- 05-vm-profile.sh: fix "Setup 3 for workstation" case
  (alterator-vm would break given large enough disk
  when reading the broken autopartitioning scheme).

* Mon Dec 23 2019 Mikhail Efremov <sem@altlinux.org> 9.2.0-alt1
- stage3: Drop installer-feature-efi-stage3.
- cleanup: Drop unused define.
- stage3: Move installer step to installer-distro-simply-linux.
- cosmetic: Split long lines in description.
- all: Set license as GPLv2+.
- stage3: Drop services enabled/disabled lists.
- stage3: Drop installer-feature-symlinks-from-sbin.

* Thu Dec 05 2019 Michael Shigorin <mike@altlinux.org> 9.1.1-alt1
- initinstall: Add e2k support.

* Tue Dec 03 2019 Mikhail Efremov <sem@altlinux.org> 9.1-alt1
- postinstall: Drop lightdm hook.

* Tue Oct 08 2019 Mikhail Efremov <sem@altlinux.org> 9.0-alt1
- Change lightdm theme to ClassicLooks.
- stage3: Add installer-feature-lightdm-stage3.
- cleanup: Arrange installer-features in alphabet order.
- Replace openntpd -> chrony.

* Thu Jun 22 2017 Mikhail Efremov <sem@altlinux.org> 8.3-alt1
- initinstall: Force 96 DPI.

* Mon Jun 19 2017 Mikhail Efremov <sem@altlinux.org> 8.2-alt1
- vm-profile: New profile.
- Drop help.
- Drop files ui/simply-linux.
- Drop unused steps.
- Use custom luks step.
- stage2: Don't require fonts-ttf-google-droid-sans.

* Thu May 18 2017 Mikhail Efremov <sem@altlinux.org> 8.1-alt1
- stage2: Drop installer-feature-set-tz.

* Fri Mar 31 2017 Mikhail Efremov <sem@altlinux.org> 8.0-alt1
- Replace prefdm.service with lightdm.service.
- i-f-sudo-enable-by-default moved stage2 -> stage3.
- Enable NetworkManager-wait-online.service.
- stage2: Add fonts-ttf-google-droid-sans.
- stage2: Add installer-feature-slideshow.
- lightdm: Setup indicators.

* Tue Apr 14 2015 Mikhail Efremov <sem@altlinux.org> 7.0-alt12
- Set Xfce4 as default session to start.
- lightdm: Disable language selector.

* Thu Mar 06 2014 Mikhail Efremov <sem@altlinux.org> 7.0-alt11
- Add installer-feature-repo-add.

* Thu Feb 13 2014 Mikhail Efremov <sem@altlinux.org> 7.0-alt10
- Disable cups.socket.
- Disable haspd.service by default.

* Tue Dec 24 2013 Mikhail Efremov <sem@altlinux.org> 7.0-alt9
- Disbale clamd.service by default.

* Fri Jun 21 2013 Mikhail Efremov <sem@altlinux.org> 7.0-alt8
- Drop installer-feature-cpufreq-stage3.

* Fri May 31 2013 Mikhail Efremov <sem@altlinux.org> 7.0-alt7
- Add module-expert-list (by cas@).
- Add installer-feature-efi-stage3.

* Mon May 27 2013 Mikhail Efremov <sem@altlinux.org> 7.0-alt6
- Add installer-feature-symlinks-from-sbin.

* Mon May 13 2013 Mikhail Efremov <sem@altlinux.org> 7.0-alt5
- Disable NetworkManager-wait-online.service.

* Thu Apr 25 2013 Mikhail Efremov <sem@altlinux.org> 7.0-alt4
- Enable x11presetdrv.service.

* Tue Apr 16 2013 Mikhail Efremov <sem@altlinux.org> 7.0-alt3
- lightdm: Set icon theme SimpleSL.
- Enable bluetoothd.service.
- Drop alterator-menu/module-expert-list,*-order-list.
- Hide alterator-logs in the acc.
- Fix alterator-menu postinstall hook perms.

* Wed Mar 27 2013 Mikhail Efremov <sem@altlinux.org> 7.0-alt2
- Explicitly enable prefdm.service.
- Disable krb5kdc service.
- Change lightdm theme to Clearlooks-Phenix.
- Added setup-journald postinstall hook.
- Disable syslogd.service.
- Disable consolesaver.service.

* Thu Feb 28 2013 Mikhail Efremov <sem@altlinux.org> 7.0-alt1
- Enable ntpd.service.
- Use installer hook for setup services.
- Replace gdm-theme with lightdm-theme postinstall hook.

* Thu Feb 14 2013 Mikhail Efremov <sem@altlinux.org> 6.991-alt2
- Drop installer-feature-hdd-pm-disable-stage3.
- remove-installer-desktop-pkgs: Remove alterator-luks.
- stage3: Added alterator-luks.
- stage3: Drop alterator-net-general.

* Thu Feb 07 2013 Mikhail Efremov <sem@altlinux.org> 6.991-alt1
- Added alterator-luks.

* Fri Jun 29 2012 Mikhail Efremov <sem@altlinux.org> 6.990-alt1
- Use systemctl if systemd is present.
- Enable NetworkManger service.
- Drop disable-whatis hook.

* Fri Feb 03 2012 Mikhail Efremov <sem@altlinux.org> 6.0-alt12
- Don't try remove xscreensaver.

* Fri Dec 23 2011 Mikhail Efremov <sem@altlinux.org> 6.0-alt11
- Drop Packager from spec.
- Add disable-whatis hook.
- Drop updatedb.sh.

* Thu Nov 24 2011 Mikhail Efremov <sem@altlinux.org> 6.0-alt10
- Use installer-feature-hdd-pm-disable-stage3.

* Thu Nov 03 2011 Mikhail Efremov <sem@altlinux.org> 6.0-alt9
- Use installer-feature-cpufreq-stage3.

* Tue Nov 01 2011 Mikhail Efremov <sem@altlinux.org> 6.0-alt8
- Set dhcp for ethernet ifaces by default.
- Use installer-feature-local-clock.

* Wed Oct 19 2011 Mikhail Efremov <sem@altlinux.org> 6.0-alt7
- Use installer-feature-xdg-user-dirs.

* Thu Sep 08 2011 Mikhail Efremov <sem@altlinux.org> 6.0-alt6
- Use installer-feature-bell-off-stage3.
- gdm: Set SoundOnLogin=false.

* Wed Aug 31 2011 Mikhail Efremov <sem@altlinux.org> 6.0-alt5
- setup-user-groups hook: Add vboxusers group.
- gdm: Set Browser=true and drop unneeded menu items.

* Wed Aug 10 2011 Mikhail Efremov <sem@altlinux.org> 6.0-alt4
- Change gdm-theme: simple -> simply.
- Rename hook: gdm-simple -> gdm-theme.

* Fri Aug 05 2011 Mikhail Efremov <sem@altlinux.org> 6.0-alt3
- Return lost Requires: installer-feature-runlevel5-stage2.

* Thu Aug 04 2011 Mikhail Efremov <sem@altlinux.org> 6.0-alt2
- vm-profile hook: Drop settings for small HDD.
- Add updatedb and hostname-resolv hooks.
- setup-user-groups: Add 'video'.
- Drop unneded installer hooks.
- Installer-faetures consistent with livecd.

* Tue Apr 12 2011 Alexandra Panyukova <mex3@altlinux.ru> 6.0-alt1
- lilo step changed to grub step

* Thu Nov 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0-alt12
- Removed dependency to installer-feature-eth-by-mac
- GDM setup script moved to postinstall.d directory

* Tue Nov 03 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0-alt10.M51.1
- Backport to 5.1.

* Tue Nov 03 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0-alt11
- Version update for easy backport to 5.1.

* Mon Nov 02 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0-alt10
- Changed samba setup settings.

* Thu Oct 29 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0-alt9
- Xkb panel plugin keyboard layout setup added.

* Sun Oct 18 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0-alt8
- Added changes for gdm setup script.

* Sun Oct 18 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0-alt7
- Changes of spec and icons for steps.

* Sun Oct 18 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0-alt6
- Setup lilo script added.

* Sat Oct 17 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0-alt5
- GDM setup script changed (taken into account theme changes).

* Sun Oct 04 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0-alt4
- Remove lynx and lftp from packages list.

* Fri Aug 14 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0-alt3
- Added sonata settings. Now, mpd are completely configured.
- Added Synaptic settings.

* Wed Jul 08 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0-alt2
- Added samba setup settings.

* Tue Jun 30 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0-alt1
- Fork from installer-distro-desktop.

