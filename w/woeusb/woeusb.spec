Name: woeusb
Version: 3.3.0
Release: alt1
Summary: Windows USB installation media creator
Summary(ru_RU.UTF-8): Утилита для создания установочного USB накопителя с Windows
Group: Archiving/Cd burning
License: GPLv3+
Url: https://github.com/slacka/WoeUSB
ExclusiveArch: %ix86 x86_64
Packager: Artyom Bystrov <arbars@altlinux.org>
Source0: %name-%version.tar.gz

BuildRequires: grub-pc
BuildRequires: gcc-c++
BuildRequires: libwxGTK-devel
BuildRequires: gettext-tools
BuildRequires: libpolkit1-devel

%description
This package contains two programs:

 o woeusb: A command-line utility that enables you to create your own bootable
Windows installation USB storage device from an existing Windows
Installation disc or disk image

 o woeusbgui: A GUI wrapper of woeusb based on WxWidgets

Supported images:

Windows Vista, Windows 7, Window 8.x, Windows 10. All languages and any version
(home, pro...) and Windows PE are supported.

Supported bootmodes:

Legacy/MBR-style/IBM PC compatible bootmode
Native UEFI booting is supported for Windows 7 and later images
(limited to the FAT filesystem as the target)


%description -l ru_RU.UTF-8
Этот пакет содержит две программы:

 o woeusb: Утилита командной строки, помогающая создавать загрузочный
накопитель для установки Windows из образа диска или непосредственно
установочного диска.

 o woeusbgui: Графическая обёртка для woeusb на базе WxWidgets

Поддерживаемые образы:

Windows Vista, Windows 7, Window 8.x, Windows 10. Поддерживаются все
языки и версии (home, pro...) и Windows PE.

Поддерживаемые режимы загрузки:

Legacy/MBR-стиль/IBM PC-совместимый
Нативный UEFI режим поддерживается для  Windows 7 и поздних систем
(с учётом ограничений файловой системы FAT)

%prep
%setup -n %name-%version

%build

%autoreconf
%configure

find ./* -type f -exec sed -i "s/@@WOEUSB_VERSION@@/%{version}/g" {} \+
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/%{name}gui
%_man1dir/%name.*
%_man1dir/%{name}gui.*
%_pixmapsdir/%{name}gui-icon.png
%_datadir/%name

%_desktopdir/%{name}gui.desktop

%changelog
* Mon Aug 26 2019 Artyom Bystrov <arbars@altlinux.org> 3.3.0-alt1
- initial build for ALT Sisyphus from Open Mandriva
