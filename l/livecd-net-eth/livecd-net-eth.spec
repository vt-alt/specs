Name: livecd-net-eth
Version: 0.4.3
Release: alt1

Summary: Try to autoconfigure ethernet interfaces
License: GPL
Group: System/Configuration/Networking

Url: http://www.altlinux.org/etcnet
Source0: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%description
This package might be useful for livecd images or virtual machines
when it's required to autoconfigure ethernet interfaces via DHCP.

%prep
%setup

%build

%install
install -pDm755 %name.init %buildroot%_initdir/%name
install -pDm644 %name.service %buildroot%_unitdir/%name.service

%files
%_initdir/%name
%_unitdir/%name.service

%changelog
* Sat Feb 15 2020 Anton Midyukov <antohami@altlinux.org> 0.4.3-alt1
- Do not configure wlan interfaces

* Thu Sep 15 2016 Michael Shigorin <mike@altlinux.org> 0.4.2-alt1
- increase DHCP timeout from 3 to 7 seconds (closes: #32397)

* Mon Jun 01 2015 Michael Shigorin <mike@altlinux.org> 0.4.1-alt1
- added the missing space (cosmetic fix)

* Fri Apr 25 2014 Michael Shigorin <mike@altlinux.org> 0.4-alt1
- do not touch:
  + networking configuration resulting from propagator/netboot;
  + packaged default/options-eth configuration file

* Sat Feb 01 2014 Michael Shigorin <mike@altlinux.org> 0.3-alt1
- DHCP timeout set to 3 seconds (thanks msp@ for the question)

* Mon Feb 11 2013 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- resolv.conf (aufs) related workaround

* Fri Feb 08 2013 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on livecd-online-repo, livecd-setlocale)

