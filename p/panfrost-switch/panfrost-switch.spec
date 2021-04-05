%define psw panfrost-switch

Name: panfrost-switch
Version: 0.1
Release: alt1
Summary: Switch panfrost use on Baikal-M
License: GPL-2.0-or-later
Group: System/Configuration/Other
Packager: Dmitry Terekhin <jqt4@altlinux.org>
Url: https://git.altlinux.org/people/jqt4/packages/panfrost-switch.git
BuildArch: noarch
Source0: %psw
Source1: README.ru
Source2: README.en

%description
Configuration switch for the panfrost driver
on a system with a Baikal-M processor

Creates or removes configuration files:

/etc/modprobe.d/panfrost_enable.conf
allows loading the panfrost driver

/etc/X11/xorg.conf.d/50-baikal-vdu.conf
allows panfrost to be used in Xorg

After changing the configuration,
you must reboot the system
for the changes to take effect.

%description -l ru_RU.UTF-8
Переключатель конфигурации для драйвера panfrost
на системе с процессором Байкал-М

Создаёт или удаляет конфигурационные файлы:

/etc/modprobe.d/panfrost_enable.conf
разрешает загрузку драйвера panfrost

/etc/X11/xorg.conf.d/50-baikal-vdu.conf
позволяет использовать panfrost в Xorg

Для встаупления в силу изменений конфигурации
нужно перезагрузить систему.

%install
install -Dpm 0755 %SOURCE0 %buildroot%_sbindir/%psw
install -m 644 %SOURCE1 ./
install -m 644 %SOURCE2 ./

%files
%doc README.ru README.en
%_sbindir/%psw

%changelog
* Tue Mar 30 2021 Dmitry Terekhin <jqt4@altlinux.org> 0.1-alt1
- Initial build
