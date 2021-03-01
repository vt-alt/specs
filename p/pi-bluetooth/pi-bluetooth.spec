Name: pi-bluetooth
Version: 0.1.15
Release: alt1

Summary: Tool for setting up bluetooth on a Raspberry Pi.
License: BSD-3-Clause
Group: System/Base
URL: https://github.com/RPi-Distro/pi-bluetooth
BuildArch: noarch
Packager: Dmitry Terekhin <jqt4@altlinux.org>
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Requires: bluez

%description
The hciuart.service unit calls the btuart script,
which analyzes the system and calls hciattach
to set up bluetooth and serial communication.

%prep
%setup
%patch -p1

%install
install -D -m 755 usr/bin/btuart %buildroot/usr/bin/btuart
install -D -m 644 debian/pi-bluetooth.hciuart.service %buildroot/lib/systemd/system/hciuart.service
install -D -m 755 usr/bin/bthelper %buildroot/usr/bin/bthelper
install -D -m 644 debian/pi-bluetooth.bthelper@.service %buildroot/lib/systemd/system/bthelper@.service
install -D -m 644 lib/udev/rules.d/90-pi-bluetooth.rules %buildroot/lib/udev/rules.d/90-pi-bluetooth.rules

%files
/usr/bin/btuart
/lib/systemd/system/hciuart.service
/usr/bin/bthelper
/lib/systemd/system/bthelper@.service
/lib/udev/rules.d/90-pi-bluetooth.rules

%changelog
* Tue Feb 16 2021 Dmitry Terekhin <jqt4@altlinux.org> 0.1.15-alt1
- Initial build
