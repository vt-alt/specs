Name: installer-feature-bootloader-grub
Version: 0.1.0
Release: alt1

Summary: Installer bootlader step for stage 3 (alterator-grub)
License: GPL-2.0-or-later
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

ExclusiveArch: %ix86 x86_64 aarch64 ppc64le riscv64
BuildArch: noarch

Requires: alterator-grub

%description
This used in mkimage-profiles (feature bootloader),
to explicitly not install the alterator-grub package.

%files

%changelog
* Fri Jun 05 2020 Anton Midyukov <antohami@altlinux.org> 0.1.0-alt1
- Initial build
