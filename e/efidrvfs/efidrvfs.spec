#% EFIFS source directory name
%define efifs 6e00f7ebe3472446a705b7ae706fff83e448fa0d

Name: efidrvfs
Version: 1.3.0.7.g6e00
Release: alt1
Summary: EFI drivers for certain filesystems
License: GPL-3.0
Group: System/Configuration/Boot and Init
URL: https://github.com/pbatard/efifs
Packager: Dmitry Terekhin <jqt4@altlinux.org>
Source0: https://github.com/pbatard/efifs/archive/6e00f7ebe3472446a705b7ae706fff83e448fa0d.zip
Source1: https://sourceforge.net/projects/gnu-efi/files/gnu-efi-3.0.11.tar.bz2
Source2: http://git.savannah.gnu.org/cgit/grub.git/snapshot/grub-2.04.tar.gz
Patch0: 0000-GRUB-fixes.patch
ExclusiveArch: aarch64

BuildRequires(pre): unzip

%description
%summary

%package -n efidrvext234
Summary: EFI driver for filesystems ext2, ext3, ext4
Group: System/Configuration/Boot and Init

%description -n efidrvext234
%summary

%prep
%setup -n %efifs
%setup -n %efifs -D -T -a 1
%setup -n %efifs -D -T -a 2
mv grub-2.04 grub
mv gnu-efi-3.0.11 gnu-efi
cd grub
%patch0 -p 1

%build
make ARCH=aa64 CROSS_COMPILE=''

%install
mkdir -p %buildroot/boot/efi/efi/drivers
cp -a %_builddir/%efifs/src/*.efi %buildroot/boot/efi/efi/drivers/

%files
/boot/efi/efi/drivers/*
%exclude /boot/efi/efi/drivers/ext2_aa64.efi

%files -n efidrvext234
/boot/efi/efi/drivers/ext2_aa64.efi

%changelog
* Thu Jan 16 2020 Dmitry Terekhin <jqt4@altlinux.org> 1.3.0.7.g6e00-alt1
- Initial build.
