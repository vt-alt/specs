%define noub rpi4-boot-nouboot
%define ubfw rpi4-boot-uboot-fw
%define uboot rpi4-boot-uboot

Name: rpi4-boot-switch
Version: 0.1
Release: alt1
Summary: Switch of boot mode for Raspberry Pi 4
License: GPLv2+
Group: System/Configuration/Other
Packager: Dmitry Terekhin <jqt4@altlinux.org>
Url: https://git.altlinux.org/people/jqt4/packages/rpi4-boot-switch.git
BuildArch: noarch
Source0: %noub
Source1: %ubfw
Source2: %uboot
Source3: README.ru
Source4: README.en

%description
Switch of boot mode for Raspberry Pi 4
In Alt, it is customary to load the kernel, dtb and initrd
using u-boot and configuration in extlinux.conf.
Firmware Raspberry Pi 4 loads and modifies dtb
according to config.txt configuration.
U-boot doesn't.
The scripts in this package allow you to switch boot modes:
Firmware loads the kernel, dtb, and initrd. U-boot is not used.
Firmware loads dtb. U-boot loads the kernel and initrd.
U-boot loads the kernel, dtb, and initrd.

%description -l ru_RU.UTF-8
Переключатель режимов загрузки для Raspberry Pi 4
В Альт принято загружать ядро, dtb и initrd
с помошью u-boot используя конфигурацию в extlinux.conf.
Firmware Raspberry Pi 4 загружает и модифицирует dtb
в соответсвии с конфигурацией config.txt.
U-boot так не умеет.
Скрипты в этом пакете позволяют переключать режимы загрузки:
Firmware загружает ядро, dtb и initrd. U-boot не используется.
Firmware загружает dtb. U-boot загружает ядро и initrd.
U-boot загружает ядро, dtb и initrd.

%install
install -Dpm 0755 %SOURCE0 %buildroot%_sbindir/%noub
install -Dpm 0755 %SOURCE1 %buildroot%_sbindir/%ubfw
install -Dpm 0755 %SOURCE2 %buildroot%_sbindir/%uboot
install -m 644 %SOURCE3 ./
install -m 644 %SOURCE4 ./

%files
%doc README.ru README.en
%_sbindir/%noub
%_sbindir/%ubfw
%_sbindir/%uboot

%changelog
* Fri Nov 22 2019 Dmitry Terekhin <jqt4@altlinux.org> 0.1-alt1
- Initial build
