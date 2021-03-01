Name: firmware-bcm4345
Version: 2.0
Release: alt1
Summary: This file is needed to bluetooth working on Paspberry Pi 4
License: LICENCE.cypress
Group: System/Configuration/Other
Packager: Dmitry Terekhin <jqt4@altlinux.org>
Url: https://github.com/RPi-Distro/bluez-firmware/raw/master/broadcom/BCM4345C0.hcd
BuildArch: noarch
Source0: BCM4345C0.hcd
Source1: LICENCE.cypress

%description
%summary

%install
%define bt_rpi4 /lib/firmware/brcm
%__install -d %buildroot%bt_rpi4
%__install -m644 %SOURCE0 %buildroot%bt_rpi4
%__install -d %buildroot/%_docdir/%name
%__install -m644 %SOURCE1 %buildroot/%_docdir/%name

%files
%bt_rpi4/BCM4345C0.hcd
%doc %_docdir/%name

%changelog
* Wed Feb 24 2021 Dmitry Terekhin <jqt4@altlinux.org> 2.0-alt1
- Firmware updated

* Fri Mar 27 2020 Dmitry Terekhin <jqt4@altlinux.org> 1.0-alt1
- Initial build
