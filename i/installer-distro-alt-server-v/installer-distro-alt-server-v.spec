%define distro alt-server-v

Name: installer-distro-%distro
Version: 9.0.1
Release: alt1

Summary: Installer configuration (Server V)
License: GPLv2
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer
Source: %name-%version.tar
BuildArch: noarch

%description
This package contains installer configuration hopefully suitable
for an ALT Linux based server distribution.

It is derived from installer-distro-altlinux-generic.

%package stage2
Summary: Installer configuration and scripts (stage2 part)
License: GPLv2
Group: System/Configuration/Other
Provides: installer-%distro-stage2 = %version
Requires: installer-stage2
# modules
Requires: alterator-sysconfig
Requires: alterator-datetime
Requires: alterator-pkg
Requires: alterator-vm
Requires: alterator-notes

%description stage2
This package contains installer configuration hopefully suitable
for an ALT Linux based server distribution.

The stage2 part is included into live installer system.

%package stage3
Summary: Installer configuration and scripts (stage3 part)
License: GPLv2
Group: System/Configuration/Other
Provides: installer-%distro-stage3 = %version
# modules
Requires: alterator-users
Requires: alterator-root
Requires: alterator-luks
Requires: alterator-net-eth dhcpcd
Requires: alterator-net-bond alterator-net-bridge
Requires: alterator-net-general
Requires: installer-stage3
Requires: installer-feature-create-vmbr-stage3
Requires: installer-feature-sudo-enable-by-default-stage3
Requires: installer-feature-online-repo
Requires: installer-feature-nfs-server-stage3
Requires: installer-feature-powerbutton-stage3

%description stage3
This package contains installer configuration hopefully suitable
for an ALT Linux based server distribution.

The stage3 part is installed onto the new system's root
and executed off there during installation process.

%prep
%setup

%install
%define install2dir %_datadir/install2
mkdir -p %buildroot%install2dir
cp -a * %buildroot%install2dir/

%files stage2
%install2dir/*.d/*
%install2dir/alterator-menu
%install2dir/installer-steps

%files stage3

%changelog
* Mon Jul 06 2020 Alexey Shabalin <shaba@altlinux.org> 9.0.1-alt1
- update title for /var/lib/vz (ALT #38193)
- drop Generic server (large /srv) profile in vm
- switch from alterator-grub to installer-feature-bootloader in m-p

* Thu Feb 13 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.0-alt3
- add vmbr creation for PVE

* Thu Sep 26 2019 Alexey Shabalin <shaba@altlinux.org> 9.0.0-alt2
- add support vd* disks in vm profile
- rename /var/lib/libvirt/images -> /var/lib/libvirt

* Wed Sep 25 2019 Alexey Shabalin <shaba@altlinux.org> 9.0.0-alt1
- add OpenVZ server (large /var/lib/vz)
- add Podman server (large /var/lib/containers)
- update alterator-menu lists

* Wed Aug 21 2019 Alexey Shabalin <shaba@altlinux.org> 7.0.6-alt1
- vm -> vm-ortodox
- add preinstall and postinstall scripts
- update Requires and Provides

* Wed Aug 21 2019 Alexey Shabalin <shaba@altlinux.org> 7.0.5-alt1
- update title in vm-profile

* Thu Jul 11 2019 Alexey Shabalin <shaba@altlinux.org> 7.0.4-alt1
- /var/lib/libvirt ->  /var/lib/libvirt/images
- add LXD HN server (large /var/lib/lxd)

* Fri Jun 14 2019 Alexey Shabalin <shaba@altlinux.org> 7.0.3-alt1
- package as name alt-server-v for Server Virtualization
- update vm profile for server-v

* Fri Mar 11 2016 Michael Shigorin <mike@altlinux.org> 7.0.2-alt1
- tweaked disk partitioning profiles towards capping the size
  of partitions differing from the "main" one (otherwise it's
  prone to e.g. three largish partitions of which two will be
  likely mostly empty forever)
- changed profile order so that "generic server" comes first

* Mon Oct 28 2013 Michael Shigorin <mike@altlinux.org> 7.0.1-alt1
- added a few more disk partitioning profiles (closes: #29483)
- fixed silly typo in steps file (non-root user *is* added now)

* Mon Jul 15 2013 Michael Shigorin <mike@altlinux.org> 7.0.0-alt1
- initial release based on installer-distro-altlinux-generic 7.0.1-alt1
- get things back somewhat closer to a useful (not test) distribution
