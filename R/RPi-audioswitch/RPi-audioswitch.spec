Name: RPi-audioswitch
Version: 1.2
Release: alt1

License: CC-BY-4.0
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
# icon source: https://www.svgrepo.com/svg/108499/switch
install -D -m0644 icons/%name.svg %buildroot%_iconsdir/hicolor/scalabale/apps/%name.svg
install -D -m0644 icons/%name-1024x1024.png %buildroot%_iconsdir/hicolor/1024x1024/apps/%name.png
install -D -m0644 icons/%name-512x512.png %buildroot%_iconsdir/hicolor/512x512/apps/%name.png
install -D -m0644 icons/%name-384x384.png %buildroot%_iconsdir/hicolor/384x384/apps/%name.png
install -D -m0644 icons/%name-256x256.png %buildroot%_iconsdir/hicolor/256x256/apps/%name.png
install -D -m0644 icons/%name-128x128.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png
install -D -m0644 icons/%name-96x96.png %buildroot%_iconsdir/hicolor/96x96/apps/%name.png
install -D -m0644 icons/%name-72x72.png %buildroot%_iconsdir/hicolor/72x72/apps/%name.png
install -D -m0644 icons/%name-64x64.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
install -D -m0644 icons/%name-48x48.png %buildroot%_iconsdir/hicolor/48x48/apps/%name.png
install -D -m0644 icons/%name-36x36.png %buildroot%_iconsdir/hicolor/36x36/apps/%name.png
install -D -m0644 icons/%name-32x32.png %buildroot%_iconsdir/hicolor/32x32/apps/%name.png
install -D -m0644 icons/%name-24x24.png %buildroot%_iconsdir/hicolor/24x24/apps/%name.png
install -D -m0644 icons/%name-22x22.png %buildroot%_iconsdir/hicolor/22x22/apps/%name.png
install -D -m0644 icons/%name-16x16.png %buildroot%_iconsdir/hicolor/16x16/apps/%name.png

%files
%attr(0755, root, root) %_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Mon Nov 25 2019 Pavel Isopenko <pauli@altlinux.org> 1.2-alt1
- add icons
- fix License: tag

* Wed Nov 20 2019 Pavel Isopenko <pauli@altlinux.org> 1.1-alt1
- initial build for Sisyphus

