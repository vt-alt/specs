Name: alt-rootfs-installer
Version: 0.3.3
Release: alt1
Summary: Installer rootfs archive to any specified block device
License: GPL-2.0-or-later
Group: System/Configuration/Other
Url:  https://git.altlinux.org/people/antohami/packages/alt-rootfs-installer.git
BuildArch: noarch
Source0: %name-%version.tar

Provides: arm-rootfs-installer = %EVR
Obsoletes: arm-rootfs-installer < 0.2

%description
Allows one to first select a source rootfs archive installer. The rootfs must be
containing File Systems with u-boot for target board.
This fork arm-image-installer.

%prep
%setup

%install
install -d %buildroot%_datadir/%name
install -d %buildroot%_datadir/%name/socs.d
cp -a socs.d/* %buildroot%_datadir/%name/socs.d/
install -d %buildroot%_datadir/%name/boards.d
cp -a boards.d/* %buildroot%_datadir/%name/boards.d/

install -d %buildroot%_bindir
install -pm 0755 %name %buildroot%_bindir/
ln -s %name %buildroot%_bindir/arm-rootfs-installer

install -d %buildroot%_docdir/%name
install -pm 644 AUTHORS COPYING README SUPPORTED-BOARDS \
        %buildroot%_docdir/%name

%files
%doc %_docdir/%name
%_bindir/*
%_datadir/%name/

%changelog
* Thu May 14 2020 Anton Midyukov <antohami@altlinux.org> 0.3.3-alt1
- Fix typo

* Mon Apr 13 2020 Anton Midyukov <antohami@altlinux.org> 0.3.2-alt1
- Added resize option
- Replace LABEL to UUID /usr/share/u-boot/rpi_4/cmdline.txt
- Update supported boards (u-boot 2020.01)

* Wed Nov 13 2019 Anton Midyukov <antohami@altlinux.org> 0.3.1.2-alt1
- Simplified check for Raspberry Pi devices targets
- Add u-boot 2019.10 support
- Fix bbl-riscv64 (Thanks arei@)

* Tue Oct 08 2019 Anton Midyukov <antohami@altlinux.org> 0.3.1.1-alt1
- hot-fix for Nvidia Jetson Nano (unmount device)

* Fri Oct 04 2019 Anton Midyukov <antohami@altlinux.org> 0.3.1-alt1
- 0.3.1
- make messages userfriendly more

* Wed Sep 11 2019 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- 0.3.0
- Add the ability create images from tarball
- Add the ability write image to media
- Add support u-boot-*-201907
- bug fixes and typos

* Fri Aug 02 2019 Anton Midyukov <antohami@altlinux.org> 0.2.4.1-alt1
- hot fix release
- change interpreter on /bin/bash

* Mon Jul 22 2019 Anton Midyukov <antohami@altlinux.org> 0.2.4-alt1
- 0.2.4
- Add support Nvidia Jetson Nano
- Add support u-boot-sunxi-201907

* Wed Jun 26 2019 Anton Midyukov <antohami@altlinux.org> 0.2.3-alt1
- 0.2.3
- Simplified code, improved portability (thanks sem@ and arei@)

* Thu Apr 18 2019 Anton Midyukov <antohami@altlinux.org> 0.2.1-alt1
- 0.2.1
- support u-boot-* 2019.04

* Fri Mar 29 2019 Anton Midyukov <antohami@altlinux.org> 0.2-alt0.1
- 0.2-beta
- Renamed package arm-rootfs-installer to alt-rootfs-installer
- Add support riscv64 (thanks arei@)
- Update URL

* Sun Feb 24 2019 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build

