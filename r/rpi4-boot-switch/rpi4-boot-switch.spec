%define noub rpi4-boot-nouboot
%define ubfw rpi4-boot-uboot-fw
%define uboot rpi4-boot-uboot
%define ftrigger rpi4-boot-nouboot.filetrigger
%define ftrgrname rpi4-boot-nouboot-filetrigger
%define ftrigger2 rpi4-boot-uboot.filetrigger
%define ftrgrname2 rpi4-boot-uboot-filetrigger
%define vars rpi4-boot-vars
%define rpicommon rpi4-boot-common
%define rpiconf config.txt
%define rpicmd cmdline.txt

Name: rpi4-boot-switch
Version: 0.12
Release: alt1
Summary: Switch of boot mode for Raspberry Pi 4
License: GPL-2.0-or-later
Group: System/Configuration/Other
Packager: Dmitry Terekhin <jqt4@altlinux.org>
Url: https://git.altlinux.org/people/jqt4/packages/rpi4-boot-switch.git
ExclusiveArch: %arm aarch64
Source0: %noub
Source1: %ubfw
Source2: %uboot
Source3: README.ru
Source4: README.en
Source5: %ftrigger
Source6: %ftrigger2
Source8: %vars
Source9: %rpicommon
Source10: %rpiconf
Source11: %rpicmd

%description
Switch of boot mode for Raspberry Pi 4
In Alt, it is customary to load the kernel, dtb and initrd
using u-boot and configuration in extlinux.conf,
or using grub.
Firmware Raspberry Pi 4 loads and modifies dtb
according to config.txt configuration.
U-boot and grub can't do that.
The scripts in this package allow you to switch boot modes:
- Firmware loads the kernel, dtb, and initrd. U-boot is not used.
armv7l (armh) 32-bit system only:
- Firmware loads dtb. U-boot loads the kernel and initrd.
- U-boot loads the kernel, dtb, and initrd.
aarch64 64-bit system only:
- U-boot loads grub, grub loads kernel, dtb and initrd.

%description -l ru_RU.UTF-8
Переключатель режимов загрузки для Raspberry Pi 4
В Альт принято загружать ядро, dtb и initrd
с помошью u-boot используя конфигурацию в extlinux.conf,
или с помощью grub.
Firmware Raspberry Pi 4 загружает и модифицирует dtb
в соответсвии с конфигурацией config.txt.
U-boot и grub так не умеют.
Скрипты в этом пакете позволяют переключать режимы загрузки:
- Firmware загружает ядро, dtb и initrd. U-boot не используется.
Только 32-битная система armv7l (armh):
- Firmware загружает dtb. U-boot загружает ядро и initrd.
- U-boot загружает ядро, dtb и initrd.
Только 64-битная система aarch64:
- U-boot загружает grub, grub загружает ядро, dtb и initrd.

%package -n %ftrgrname
Summary: Do a kernel update on /mnt/FIRMPART or /boot/efi
Group: System/Configuration/Other
Requires: %name

%description -n %ftrgrname
This filetrigger executes "rpi4-boot-nouboot --default"
to do a kernel update on /mnt/FIRMPART or /boot/efi

%package -n %ftrgrname2
Summary: Do a u-boot and firmware update on /mnt/FIRMPART or /boot/efi
Group: System/Configuration/Other
Requires: %name

%description -n %ftrgrname2
This filetrigger executes "rpi4-boot-uboot --update-uboot-only"
to do a u-boot and firmware update on files in directories
/usr/share/u-boot/rpi_3/ and /usr/share/u-boot/rpi_4/
armv7l (armh) 32-bit system only:
/usr/share/u-boot/rpi_3_32b/kernel7.img is rename to
uboot-rpi_3_32b.bin
/usr/share/u-boot/rpi_4_32b/kernel7.img is rename to
uboot-rpi_4_32b.bin
aarch64 64-bit system only:
/usr/share/u-boot/rpi_3/kernel8.img is rename to
uboot-rpi_3.bin
/usr/share/u-boot/rpi_4/kernel8.img is rename to
uboot-rpi_4.bin

%install
install -Dpm 0755 %SOURCE0 %buildroot%_sbindir/%noub
install -Dpm 0755 %SOURCE1 %buildroot%_sbindir/%ubfw
install -Dpm 0755 %SOURCE2 %buildroot%_sbindir/%uboot
install -m 644 %SOURCE3 ./
install -m 644 %SOURCE4 ./
install -Dpm 0755 %SOURCE5 %buildroot%_rpmlibdir/%ftrigger
install -Dpm 0755 %SOURCE6 %buildroot%_rpmlibdir/%ftrigger2
install -Dpm 0644 %SOURCE8 %buildroot%_sbindir/%vars
install -Dpm 0644 %SOURCE9 %buildroot%_sbindir/%rpicommon
mkdir -p %buildroot%_datadir/%name
install -Dpm 0644 %SOURCE10 %buildroot%_datadir/%name/%rpiconf
install -Dpm 0644 %SOURCE11 %buildroot%_datadir/%name/%rpicmd

%ifarch %arm
sed -i 's/^arm_64bit=/# arm_64bit=/ ; s/.bin/_32b.bin/g' \
	%buildroot%_datadir/%name/%rpiconf
%endif

%files
%doc README.ru README.en
%_sbindir/%noub
%_sbindir/%ubfw
%_sbindir/%uboot
%_sbindir/%vars
%_sbindir/%rpicommon
%_datadir/%name/
%_datadir/%name/%rpiconf
%_datadir/%name/%rpicmd

%files -n %ftrgrname
%_rpmlibdir/%ftrigger

%files -n %ftrgrname2
%_rpmlibdir/%ftrigger2

%changelog
* Sat Jan 09 2021 Dmitry Terekhin <jqt4@altlinux.org> 0.12-alt1
- Bugs fixed:
- rpi4-boot-common: the lack of overlays is normal
- rpi4-boot-nouboot: restore default config.txt

* Thu Oct 15 2020 Dmitry Terekhin <jqt4@altlinux.org> 0.11-alt1
- Added aarch64 ang GRUB-EFI support.
- Added experimental support for RPi3 booting in firmware
- and u-boot boot modes.
- Added experimental support for other RPi in firmware only
- boot mode.

* Sun Jun 28 2020 Anton Midyukov <antohami@altlinux.org> 0.10-alt1
- Initiate allocation of common code in rpi4-boot-common
- Copy dtb for RasPi3 also
- Do not add devicetree to config.txt
- Do not backup config.txt every time

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
