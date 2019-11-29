Name: RPi-audioswitch
Version: 1.1
Release: alt1

License: GPLv3
Group: System/Configuration/Hardware
Url: http://packages.altlinux.org

Packager: Pavel Isopenko <pauli@altlinux.org>
Summary: RPi simply audio switch
Summary(ru_RU.UTF-8): Простой переключатель аудиовыхода для Raspberry Pi
Source: %name-%version.tar
BuildArch: noarch

%description
Raspberry Pi 3/4 simply TUI switch between HDMI and 3,5mm headphone jack audio output

%description -l ru_RU.UTF-8
Простой консольный переключатель между HDMI и 3,5мм аудиовыходом для Raspberry Pi 3 и 4

%prep
%setup

%build

%install
install -D -m0755 %name %buildroot%_bindir/%name
install -D -m0644 %name.desktop %buildroot%_desktopdir/%name.desktop

%files
%attr(0755, root, root) %_bindir/%name
%_desktopdir/%name.desktop

%changelog
* Wed Nov 20 2019 Pavel Isopenko <pauli@altlinux.org> 1.1-alt1
- initial build for Sisyphus

