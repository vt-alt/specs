Name:    installer-distro-education
Version: 9.0
Release: alt1

Summary: Installer common files for ALT Education
License: GPL
Group: System/Configuration/Other
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: alterator rpm-devel

%define feature installer-feature-simply-linux

%description
Installer common files for ALT Education.

%package stage2
Summary: Installer stage2
License: GPL
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: installer-stage2
#modules
Requires: alterator-sysconfig
Requires: alterator-license
#Requires: alterator-auth
Requires: alterator-datetime
Requires: alterator-vm
Requires: alterator-pkg
Requires: alterator-luks
Requires: x-cursor-theme-jimmac
Requires: bc
#features
Requires: installer-feature-local-clock
Requires: installer-feature-autohostname-stage2
Requires: installer-feature-samba-usershares-stage2
Requires: installer-feature-desktop-other-fs-stage2
Requires: installer-feature-desktop-suspend-stage2
Requires: installer-feature-hwtweaks-stage2
Requires: installer-feature-set-tz
Requires: installer-feature-runlevel5-stage2
Requires: installer-feature-xdg-user-dirs
Requires: installer-feature-services

%description stage2
Installer stage2


%package stage3
Summary: Installer stage3
License: GPL
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
Requires: installer-feature-nfs-client-stage3
Requires: installer-feature-setup-network-stage3
Requires: installer-feature-online-repo
Requires: installer-feature-bell-off-stage3
Requires: installer-feature-symlinks-from-sbin
Requires: installer-feature-efi-stage3

%description stage3
Installer stage3

%prep
%setup -q

%install
%makeinstall

%find_lang alterator-simply-linux

%files -f alterator-simply-linux.lang
%_datadir/install2/help/*

%files stage2
%_datadir/install2/installer-steps
%_datadir/install2/*.d/*
%_datadir/install2/steps/*
%_datadir/install2/alterator-menu
%_datadir/install2/systemd-enabled
%_datadir/install2/systemd-disabled

%files stage3
%_datadir/alterator/ui/simply-linux

%changelog
* Fri Jun 07 2019 Andrey Cherepanov <cas@altlinux.org> 9.0-alt1
- Create new installer based on installer-distro-junior.
- Make autopatrition script from volumes-profile-lite.
- Increase size of / to 28G.
