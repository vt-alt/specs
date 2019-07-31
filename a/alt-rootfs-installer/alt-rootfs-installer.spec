Name: alt-rootfs-installer
Version: 0.2.4
Release: alt1
Summary: Installer rootfs archive to any specified block device
License: GPLv2+
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

