Name: egctl
Version: 0.1
Release: alt1

Summary: control EnerGenie programmable surge protector over LAN/WLAN
License: MIT
Group: Networking/Remote access

Url: http://github.com/unterwulf/egctl
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

%description
egctl is a program to control the state of EnerGenie Programmable
surge protector with LAN/WLAN interface. It uses native data exchange
protocol of the device, not HTTP.

Currently the following devices are supported:
- EG-PMS-LAN
- EG-PM2-LAN
- EG-PMS2-LAN
- EG-PMS-WLAN

See also sispmctl package for Gembird's USB PDU support.

%prep
%setup

%build
%make

%install
%makeinstall_std PREFIX=%_usr
install -pDm640 egtab %buildroot%_sysconfdir/egtab

%files
%_bindir/*
%_man1dir/*
%config(noreplace) %attr(0640,root,wheel) %_sysconfdir/egtab
%doc README

%changelog
* Wed Sep 16 2020 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (b525716 git commit)

