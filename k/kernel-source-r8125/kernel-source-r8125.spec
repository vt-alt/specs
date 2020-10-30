Name: kernel-source-r8125
Version: 9.003.05
Release: alt1
Summary: Source for the r8125 driver
License: GPL
Group: Development/Kernel
URL: https://www.realtek.com/en/component/zoo/category/network-interface-controllers-10-100-1000m-gigabit-ethernet-pci-express-software
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source: r8125-9.003.05.tar.bz2

BuildArch: noarch
BuildPreReq: kernel-build-tools

%description
2.5G Ethernet LINUX driver r8125

%prep
%setup -c

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 r8125-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Mon Oct 19 2020 Valery Inozemtsev <shrek@altlinux.ru> 9.003.05-alt1
- initial release

