Name: kernel-source-rtl8821ce
Version: 5.5.2
Release: alt5
Summary: Source for the rtl8821ce driver
License: GPLv2
Group: Development/Kernel
URL: https://github.com/tomaspinho/rtl8821ce.git
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source: %name-%version.tar

BuildArch: noarch
BuildPreReq: kernel-build-tools

%description
Linux rtl8821ce driver for Realtek's Wi-Fi cards

%prep
%setup -c

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Wed Dec 16 2020 Valery Inozemtsev <shrek@altlinux.ru> 5.5.2-alt5
- fixes for Linux 5.10

* Wed Sep 02 2020 Valery Inozemtsev <shrek@altlinux.ru> 5.5.2-alt4
- fixes for Linux 5.8

* Thu Apr 30 2020 Valery Inozemtsev <shrek@altlinux.ru> 5.5.2-alt3
- v5.5.2_34066.20200325_COEX20180712-3232

* Mon Nov 25 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.5.2-alt2
- fixes for Linux 5.3

* Mon Sep 30 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.5.2-alt1
- v5.5.2

* Fri Mar 29 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.2.5.1-alt1
- initial release

