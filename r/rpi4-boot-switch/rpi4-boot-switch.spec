%define noub rpi4-boot-nouboot
%define ubfw rpi4-boot-uboot-fw
%define uboot rpi4-boot-uboot
%define ftrigger rpi4-boot-nouboot.filetrigger
%define ftrgrname rpi4-boot-nouboot-filetrigger
%define ftrigger2 rpi4-boot-uboot.filetrigger
%define ftrgrname2 rpi4-boot-uboot-filetrigger
%define firsttimename rpi4-uboot-directory-cleanup
%define vars rpi4-boot-vars

Name: rpi4-boot-switch
Version: 0.9
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
Source5: %ftrigger
Source6: %ftrigger2
Source7: %firsttimename
Source8: %vars

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

%package -n %ftrgrname
Summary: Do a kernel update on /mnt/FIRMPART
Group: System/Configuration/Other
Requires: %name

%description -n %ftrgrname
This filetrigger executes "rpi4-boot-nouboot --default"
to do a kernel update on /mnt/FIRMPART

%package -n %ftrgrname2
Summary: Do a u-boot update on files in directory /usr/share/u-boot/rpi_4/
Group: System/Configuration/Other
Requires: %name

%description -n %ftrgrname2
This filetrigger executes "rpi4-boot-uboot --update-uboot-only"
to do a u-boot update on files in directory /usr/share/u-boot/rpi_4/

%install
install -Dpm 0755 %SOURCE0 %buildroot%_sbindir/%noub
install -Dpm 0755 %SOURCE1 %buildroot%_sbindir/%ubfw
install -Dpm 0755 %SOURCE2 %buildroot%_sbindir/%uboot
install -m 644 %SOURCE3 ./
install -m 644 %SOURCE4 ./
install -Dpm 0755 %SOURCE5 %buildroot%_rpmlibdir/%ftrigger
install -Dpm 0755 %SOURCE6 %buildroot%_rpmlibdir/%ftrigger2
install -Dpm 0755 %SOURCE7 %buildroot%_sysconfdir/firsttime.d/%firsttimename
install -Dpm 0644 %SOURCE8 %buildroot%_sbindir/%vars

%files
%doc README.ru README.en
%_sysconfdir/firsttime.d/%firsttimename
%_sbindir/%noub
%_sbindir/%ubfw
%_sbindir/%uboot
%_sbindir/%vars

%files -n %ftrgrname
%_rpmlibdir/%ftrigger

%files -n %ftrgrname2
%_rpmlibdir/%ftrigger2

%changelog
* Tue Jun 09 2020 Dmitry Terekhin <jqt4@altlinux.org> 0.9-alt1
- rpi4-boot-nouboot: removed cma=192M option from kernel cmd line

* Thu Jun 04 2020 Dmitry Terekhin <jqt4@altlinux.org> 0.8-alt1
- Removed read-only remounting
- Changed copying kernel, initrd, dtb to FAT
- Added copying overlays along with dtb

* Sat May 23 2020 Dmitry Terekhin <jqt4@altlinux.org> 0.7-alt1
- Common file for variables
- Adapted for armh

* Sun Apr 05 2020 Dmitry Terekhin <jqt4@altlinux.org> 0.6-alt1
- rpi4-boot-uboot*: always edit file extlinux.conf

* Thu Apr 02 2020 Dmitry Terekhin <jqt4@altlinux.org> 0.5-alt1
- rpi4-boot-nouboot --bootstrap: backup dtb file

* Thu Apr 02 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.4-alt1
- Improve remount process
- rpi4-boot-uboot: add --update-uboot-only option and u-boot files filetrigger
- rpi4-boot-nouboot: add --bootstrap option with firsttime cleanup script

* Wed Apr 01 2020 Dmitry Terekhin <jqt4@altlinux.org> 0.3-alt1
- Gently remount /mnt/FIRMPART

* Wed Apr 01 2020 Dmitry Terekhin <jqt4@altlinux.org> 0.2-alt1
- rpi4-boot-nouboot: added --default option
- Added rpi4-boot-nouboot.filetrigger

* Fri Nov 22 2019 Dmitry Terekhin <jqt4@altlinux.org> 0.1-alt1
- Initial build
