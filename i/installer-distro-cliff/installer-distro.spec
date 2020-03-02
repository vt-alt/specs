%define distro cliff
Name: installer-distro-%distro
Version: 8.1
Release: alt2

Summary: Installer files for Cliff distro
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
BuildRequires: alterator-officer

Source: %name-%version.tar

%description
Installer files for Cliff distro.

%package stage2
Summary: Installer stage2
License: GPL
Group: System/Configuration/Other
Provides: installer-%distro-stage2 = %name-%version
Requires: installer-stage2
#modules
Requires: alterator-sysconfig
Requires: alterator-datetime
Requires: alterator-pkg
Requires: alterator-vm
Requires: alterator-notes
Requires: alterator-officer
Requires: x-cursor-theme-jimmac

%description stage2
Cliff Installer stage2.

%package stage3
Summary: Installer stage3
License: GPL
Group: System/Configuration/Other
Provides: installer-%distro-stage3 = %name-%version
Requires: installer-stage3
#modules
Requires: alterator-users
Requires: alterator-officer
Requires: alterator-root
Requires: alterator-net-eth dhcpcd
Requires: alterator-net-general
Requires: alterator-net-bond alterator-net-bridge
Requires: installer-feature-nfs-server-stage3
Requires: installer-feature-powerbutton-stage3
Requires: alterator-grub
Requires: alterator-luks

%description stage3
Cliff Installer stage3.

%prep
%setup

%install
%define install2dir %_datadir/install2
mkdir -p %buildroot%install2dir
mkdir -p %buildroot%install2dir/steps
cp -a * %buildroot%install2dir/
cp -a steps.d/* %buildroot%install2dir/steps 

%files stage2
%install2dir/alterator-menu
%install2dir/installer-steps
%install2dir/steps/*.desktop
%install2dir/services-*
%install2dir/systemd-*
%install2dir/*.d/*

%files stage3

%changelog
* Wed Feb 26 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.1-alt2
- build for sisyphus

* Wed Jul 17 2019 Denis Medvedev <nbr@altlinux.org> 8.1-alt1.M80C.7
- users-officer.desktop now lives here, not in alterator-officer.

* Sat Jun 29 2019 Denis Medvedev <nbr@altlinux.org> 8.1-alt1.M80C.6
- ipv6 is only when selinux is on

* Fri Jun 28 2019 Denis Medvedev <nbr@altlinux.org> 8.1-alt1.M80C.5
- allow officer to run its scripts by making them with right context.

* Wed Jun 26 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.1-alt1.M80C.4
- mount separate execable tmpfs into /tmp/.private/root

* Thu May 23 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.1-alt1.M80C.3
- changes from nbr@ merged

* Tue May 21 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.1-alt1.M80C.2
- add enviroment for officer

* Tue May 21 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.1-alt1.M80C.1
- delete wheel from default groups
- set /home and /tmp noexec

* Tue Apr 16 2019 Denis Medvedev <nbr@altlinux.org> 8.0-alt1.M80C.13
- fixed wheel group assignment for officer while selinux mode on.

* Tue Apr 16 2019 Denis Medvedev <nbr@altlinux.org> 8.0-alt1.M80C.12
- handling of selinux smem  and  ipv6.

* Wed Apr 10 2019 Mikhail Efremov <sem@altlinux.org> 8.0-alt1.M80C.11
- postinstall: Generate host key files.
- Add hack to bend Russian name for License step.

* Wed Mar 06 2019 Michael Shigorin <mike@altlinux.org> 8.0-alt1.M80C.10
- license step returned (reverts 8.0-alt1.M80C.1 change)

* Wed Jan 23 2019 Denis Medvedev <nbr@altlinux.org> 8.0-alt1.M80C.9
- remove alterator-officer after installation.

* Sun Jan 20 2019 Denis Medvedev <nbr@altlinux.org> 8.0-alt1.M80C.8
- fix bugs in scripts.

* Thu Jan 17 2019 Denis Medvedev <nbr@altlinux.org> 8.0-alt1.M80C.7
- adding officer to group wheel. Enable trusted mode for
python and perl.

* Wed Nov 21 2018 Denis Medvedev <nbr@altlinux.org> 8.0-alt1.M80C.6
- moved hider script to a proper place

* Tue Nov 20 2018 Denis Medvedev <nbr@altlinux.org> 8.0-alt1.M80C.5
- hide unused installer steps in some configs.

* Wed Oct 03 2018 Denis Medvedev <nbr@altlinux.org> 8.0-alt1.M80C.4
- Added alterator-officer

* Mon Apr 17 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.0-alt1.M80C.3
- no alterator-notes

* Mon Apr 17 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.0-alt1.M80C.2
- net-bond and net-bridge in stage3

* Tue Apr 04 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.0-alt1.M80C.1
- license step removed

* Fri Dec 02 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.0-alt0.M80P.1
- cliff version: vm/blonde used

* Wed Jun 08 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.0-alt2
- xinetd enabled in systemd installations

* Fri Jun 03 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.0-alt1
- sshd, ahttpd, alteratord enabled in systemd installations

* Fri Apr 04 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0-alt8
- 'users' group added to default group list

* Wed Jan 08 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0-alt7
- ModemManager enabled in systemd-enabled

* Tue Dec 17 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0-alt6
- dm changed to prefdm in systemd-enabled

* Sun Dec 01 2013 Andrey Cherepanov <cas@altlinux.org> 7.0-alt5
- Move rare modules to expert list, hide unusable modules trust
  and moodle-install

* Wed Sep 11 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0-alt4
- postfix enabled in systemd

* Fri Jul 19 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0-alt3
- removing alterator-luks added

* Wed Jul 17 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0-alt2
- NetworkManager-wait-online disabled by default

* Wed Jul 03 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0-alt1
- use cups.service instead cups.socket

* Tue Mar 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.9-alt7
- some sysVinit services disabled in systemd

* Fri Dec 21 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.9-alt6
- alterator-luks added

* Tue Dec 18 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.9-alt5
- grub2-efi on x86_64 added

* Wed Nov 28 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.9-alt4
- nscd and nslcd added to systemd-enabled

* Fri Nov 16 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.9-alt3
- nscd and nslcd temporary removed from services-on

* Wed Oct 10 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.9-alt2
- nm and avahi added to systemd-enables, nscd and nslcd to services-on

* Tue Sep 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.9-alt1
- bump version
- systemd-enabled file added

* Fri Aug 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0-alt14
- removed dependences on outdated installer features

* Thu Aug 25 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0-alt13
- fix 80-setup-user-groups

* Mon Aug 22 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0-alt12
- add first user to vboxusers

* Fri Aug 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0-alt11
- datetime-tcp activation added

* Fri Jul 15 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0-alt10
- installer-feature-copy-udev-rules-stage3 added

* Mon Mar 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0-alt9
- set server role to none

* Wed Mar 02 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0-alt8
- xdg-user-dirs: coupled Photos/Pictures and Movies/Videos

* Fri Feb 18 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0-alt7
- bacula-fd on by default

* Thu Feb 17 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0-alt6
- hide alterator-users only if a-ldap-users is installed
- unset xdg-user-dirs PUBLICSHARE

* Wed Feb 09 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0-alt5
- openntpd added to services-on

* Fri Feb 04 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0-alt4
- libvirtd, qemu-kvm-el and virtualbox added to services-on

* Tue Nov 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0-alt3
- trust moved to expert mode

* Tue Oct 26 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0-alt2
- net-iptables-manual moved to expert mode

* Fri Oct 22 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0-alt1
- more services off by default

* Mon Oct 18 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9-alt7
- slapd turned off by default
- vm changed to ortodox

* Tue Oct 05 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9-alt6
- vz off by default

* Fri Oct 01 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9-alt5
- server role setting added

* Wed Sep 29 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9-alt4
- alterator-users moded to expert mode list

* Tue Sep 28 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9-alt3
- alterator-{auth,services} moved from expert list

* Tue Apr 06 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9-alt2
- services, started by defaul set up

* Mon Mar 15 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9-alt1
- s/lilo/grub/

* Fri Feb 05 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt1
- first build based on server-light

* Tue Sep 08 2009 Anton Farygin <rider@altlinux.ru> 5.0-alt2
- disabled bind, alteratord and ntpd services by default
- specfile cleanup

* Thu May 07 2009 Anton Farygin <rider@altlinux.ru> 5.0-alt1
- initial build, based on Office Server

* Tue Apr 28 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt8
- Added installer-feature-net-br-stage2 to stage2.

* Fri Apr 10 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt7
- preinstall.d: Renamed 01-home -> 01-fs, added /srv support there.
- postinstall.d/03-button.sh: Replaced with installer-feature-powerbutton-stage3.
- initinstall.d/05-vm-profile-ofs: Replaced with installer-feature-vm-ofs-stage2.
- preinstall.d/01-fs: Replaced with installer-feature-vm-ofs-stage3.
- module-order-list: Added new modules.

* Thu Apr 02 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt6
- Updated alterator/menu/module-order-list from inger@.
- Renamed to installer-distro-office-server.

* Thu Apr 02 2009 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt5
- stage3: Added requirement on installer-feature-nfs-server-stage3.
- initinstall.d/05-vm-profile: Rewritten.
- postinstall.d/06-xinetd.sh: Removed.
- postinstall.d/10-alteratord.sh: s/run_chroot/exec_chroot/.
- preinstall.d/01-home: Rewritten.
- Added files for /etc/alterator/menu/.
- Updated BuildRequires.

* Thu Feb 26 2009 Stanislav Ievlev <inger@altlinux.org> 5.0-alt4
- remove unused files
- add postinstall.d script for alteratord

* Tue Feb 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt3
- root and ldap steps moved to firsttime 

* Mon Feb 09 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt2
- root and net steps changed to office-server 

* Wed Feb 04 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt1
- joined tzone and datetime 

* Fri Jan 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- updated for sisyphus installer state 

* Wed Nov 05 2008 Alexandra Panyukova <mex3@altlinux.ru> 0.2-alt5.M41
- Version for M41
- sysconfig step added

* Fri Dec 14 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt4
- Xinetd hook to disable localhost-only access.
- Check alterator-firewall backend presence before call.

* Mon Nov 19 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt3
- Alterator-ulogd hook.

* Mon Nov 19 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt2
- Use $destdir in postinstall hooks.

* Wed Oct 10 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt1
- Merge installer-hpc-0.2-alt2.
- Add translations.
- Alterator-iptables hook.
- Carry finish step (finish.scm).

* Sat Sep 08 2007 Grigory Batalov <bga@altlinux.ru> 0.1-alt1
- Initial build based on installer-hpc.
