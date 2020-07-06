Name:    installer-distro-education
Version: 9.1
Release: alt2.1.p9

Summary: Installer common files for ALT Education
License: GPL-2.0
Group: System/Configuration/Other
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: alterator rpm-devel

%define feature installer-feature-simply-linux

%description
Installer common files for ALT Education.

%package stage2
Summary: Installer stage2
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: installer-common-stage2
# volumes profile
Requires: volumes-profile-education
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
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: installer-stage3
#modules
%ifnarch armh
Requires: alterator-grub
%endif
Requires: alterator-users
Requires: alterator-root
Requires: alterator-net-eth dhcpcd
Requires: alterator-luks
#Requires: alterator-x11
Requires: installer-feature-nfs-client-stage3
Requires: installer-feature-setup-network-stage3
Requires: installer-feature-online-repo
Requires: installer-feature-bell-off-stage3
Requires: installer-feature-efi-stage3

%description stage3
Installer stage3

%package -n volumes-profile-education
Summary: Volumes profile for ALT Education
Group: System/Configuration/Other

%description -n volumes-profile-education
Volumes profile for ALT Education.

%prep
%setup -q

%install
%makeinstall
rm -rf %buildroot%_datadir/alterator/help/ru_RU \
       %buildroot%_datadir/alterator/help/ru_UA \
       %buildroot%_datadir/alterator/steps
%find_lang alterator-simply-linux

%files -f alterator-simply-linux.lang
%_datadir/install2/help/*

%files stage2
%_datadir/install2/installer-steps
%_datadir/install2/*.d/*
%exclude %_datadir/install2/initinstall.d/10-vm-profile.sh
%_datadir/install2/steps/*
%_datadir/install2/alterator-menu
%_datadir/install2/systemd-enabled
%_datadir/install2/systemd-disabled

%files stage3
%_datadir/alterator/ui/simply-linux

%files -n volumes-profile-education
%_datadir/install2/initinstall.d/10-vm-profile.sh

%changelog
* Sat Jul 04 2020 Andrey Cherepanov <cas@altlinux.org> 9.1-alt2.1.p9
- Build package as noarch.

* Sat Jul 04 2020 Andrey Cherepanov <cas@altlinux.org> 9.1-alt3
- Exclude armh from build architectures.
- Remove autreq of installer-stage2.
- Fix License according to SPDX.
- Remove unpackaged files.
- Package volumes-profile-education as separate package.

* Fri Jul 03 2020 Andrey Cherepanov <cas@altlinux.org> 9.1-alt2
- Do not use deprecated installer-feature-symlinks-from-sbin.

* Thu Jun 04 2020 Andrey Cherepanov <cas@altlinux.org> 9.1-alt1
- Enable cups-browsed service.

* Fri Jun 07 2019 Andrey Cherepanov <cas@altlinux.org> 9.0-alt1
- Create new installer based on installer-distro-junior.
- Make autopatrition script from volumes-profile-lite.
- Increase size of / to 28G.
