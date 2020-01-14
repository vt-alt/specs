%define _unpackaged_files_terminate_build 1

Name: wireguard

Version: 0.0.20191219
Release: alt1

Summary: Wireguard is a fast, modern, secure VPN tunnel module for Linux kernel
License: GPLv2
Group: System/Servers
Url: https://www.wireguard.com/
#Git: https://git.zx2c4.com/WireGuard/

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-kernel
BuildRequires: libmnl-devel

%package -n %name-tools 
Summary: Tools for WireGuard: fast, modern, secure VPN tunnel
Summary(ru_RU.UTF-8): Утилиты для WireGuard, быстрого, современного, защищенного VPN-туннеля
License: GPLv2
Group: Networking/Remote access

%package -n wg-quick
Summary: Tools' extension for WireGuard: fast, modern, secure VPN tunnel
Summary(ru_RU.UTF-8): Дополнительные утилиты для WireGuard, быстрого, современного, защищенного VPN-туннеля
License: GPLv2
Group: Networking/Remote access
BuildArch: noarch

%package -n bash-completion-%name 
Summary:  Bash_completion scripts for WireGuard: fast, modern, secure VPN tunnel
Summary(ru_RU.UTF-8): Скрипты bash-completion для WireGuard, быстрого, современного, защищенного VPN-туннеля
License: GPLv2
Group: Networking/Remote access
BuildArch: noarch

%package -n kernel-source-%name
Summary: Source for WireGuard: fast, modern, secure VPN tunnel
Summary(ru_RU.UTF-8): Исходный код WireGuard, быстрого, современного, защищенного VPN туннеля
License: GPLv2
Group: Development/Kernel
BuildArch: noarch

%description -n %name
WireGuard is an extremely simple yet fast and modern VPN that utilizes
state-of-the-art cryptography.

%description -n %name-tools
Utilities package for WireGuard.
WireGuard is an extremely simple yet fast and modern VPN that utilizes
state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more
useful than IPSec, while avoiding the massive headache. It intends to be
considerably more performant than OpenVPN. WireGuard is designed as a general
purpose VPN for running on embedded interfaces and super computers alike, fit
for many different circumstances. Initially released for the Linux kernel, it
plans to be cross-platform and widely deployable. It is currently under heavy
development, but already it might be regarded as the most secure, easiest to
use, and simplest VPN solution in the industry.

%description -n wg-quick
Utilities extension package for WireGuard.
WireGuard is an extremely simple yet fast and modern VPN that utilizes
state-of-the-art cryptography.

%description -n bash-completion-%name
Bash_completion scripts package for WireGuard.
WireGuard is an extremely simple yet fast and modern VPN that utilizes
state-of-the-art cryptography.

%description -n kernel-source-%name
Src package for WireGuard.
WireGuard is an extremely simple yet fast and modern VPN that utilizes
state-of-the-art cryptography.

%prep
%setup

%build
cd src
%make_build tools

%install
cd src/tools
%makeinstall WITH_WGQUICK="yes" WITH_BASHCOMPLETION="yes" WITH_SYSTEMDUNITS="yes" \
SYSTEMDUNITDIR=%_unitdir DESTDIR=%buildroot BINDIR=%_sbindir MANDIR=%_mandir \
RUNSTATEDIR=/run
   
tar xvf %SOURCE0
mv %name-%version kernel-source-%name-%version
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/kernel-source-%name-%version.tar.bz2 kernel-source-%name-%version

%files -n %name-tools
%doc README.md COPYING contrib/examples
%_man8dir/wg.8*
%_sbindir/wg

%files -n wg-quick
%_man8dir/wg-quick.8*
%_sbindir/wg-quick
%_unitdir/wg-quick@.service

%files -n bash-completion-%name
%_datadir/bash-completion/completions/wg
%_datadir/bash-completion/completions/wg-quick

%files -n kernel-source-%name
%attr(0644,root,root) %kernel_src/kernel-source-%name-%version.tar.bz2

%changelog
* Mon Dec 23 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20191219-alt1
- New version

* Thu Dec 12 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20191212-alt1
- New version

* Sun Dec 08 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20191206-alt1
- New version

* Thu Dec 05 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20191205-alt1
- New version

* Thu Nov 28 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20191127-alt1
- New version

* Sun Oct 13 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20191012-alt1
- New version

* Mon Sep 30 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20190913-alt1
- New version

* Fri Sep 06 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20190905-alt1
- New version

* Thu Jul 04 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20190702-alt1
- New version

* Sun Jun 02 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20190601-alt1
- New version

* Tue Apr 23 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20190406-alt1
- New version

* Mon Mar 04 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20190227-alt1
- New version

* Mon Dec 31 2018 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20181218-alt1
- New version
  + remove ubt

* Wed Sep 12 2018 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20180910-alt1
- New version

* Tue Jul 03 2018 Alexey Shabalin <shaba@altlinux.ru> 0.0.20180625-alt1
- 0.0.20180625

* Thu May 03 2018 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20180413-alt2
- Rebuild to provide wg-quick as a separate package

* Tue Apr 17 2018 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20180413-alt1
- Initial build
