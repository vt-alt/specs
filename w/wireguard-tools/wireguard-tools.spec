%define _unpackaged_files_terminate_build 1

Name: wireguard-tools

Version: 1.0.20200513
Release: alt2

Summary: Tools for WireGuard: fast, modern, secure VPN tunnel
Summary(ru_RU.UTF-8): Утилиты для WireGuard, быстрого, современного, защищенного VPN-туннеля
License: GPLv2
Group: System/Servers
Url: https://www.wireguard.com/
#Git: https://git.zx2c4.com/wireguard-tools/

Source0: %name-%version.tar
Patch1: wireguard-tools-1.0.20200513-completion-exit-early-with-bash-less-than-4.patch

Obsoletes: bash-completion-wireguard < %EVR
Conflicts: bash-completion-wireguard < %EVR
Conflicts: wg-quick < %EVR

%package wg-quick
Summary: Tools' extension for WireGuard: fast, modern, secure VPN tunnel
Summary(ru_RU.UTF-8): Дополнительные утилиты для WireGuard, быстрого, современного, защищенного VPN-туннеля
License: GPLv2
Group: Networking/Remote access
Requires: %name = %EVR
Provides: wg-quick = %EVR
Obsoletes: wg-quick < %EVR
Conflicts: bash-completion-wireguard < %EVR
BuildArch: noarch

%package examples
Summary: Example scripts for WireGuard: fast, modern, secure VPN tunnel
Summary(ru_RU.UTF-8): Скрипты-примеры для WireGuard, быстрого, современного, защищенного VPN-туннеля
License: GPLv2
Group: Networking/Remote access
BuildArch: noarch

%description
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

%description wg-quick
Utilities extension package for WireGuard.
WireGuard is an extremely simple yet fast and modern VPN that utilizes
state-of-the-art cryptography.

%description examples
Example scripts package for WireGuard.
WireGuard is an extremely simple yet fast and modern VPN that utilizes
state-of-the-art cryptography.

%prep
%setup
%patch1 -p1
sed -i 's|%_bindir|%_sbindir|g' src/systemd/wg-quick@.service

%build
pushd src
%make_build
popd

%install
pushd src
%makeinstall \
	WITH_WGQUICK="yes" \
	WITH_BASHCOMPLETION="yes" \
	WITH_SYSTEMDUNITS="yes" \
	SYSTEMDUNITDIR=%_unitdir \
	DESTDIR=%buildroot \
	BINDIR=%_sbindir \
	MANDIR=%_mandir \
	RUNSTATEDIR=/run
popd

%files
%doc README.md COPYING
%_man8dir/wg.8*
%_sbindir/wg
%_datadir/bash-completion/completions/wg

%files wg-quick
%_man8dir/wg-quick.8*
%_sbindir/wg-quick
%_unitdir/wg-quick@.service
%_unitdir/wg-quick.target
%_datadir/bash-completion/completions/wg-quick

%files examples
%doc contrib/*

%changelog
* Fri Jun 26 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0.20200513-alt2
- Avoid completion scripts report errors on terminal start when bash version
  is less than 4

* Thu May 14 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0.20200513-alt1
- New version
  + add upstream wg-quick.target to package

* Tue May 12 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0.20200510-alt1
- New version

* Mon Mar 30 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0.20200319-alt2
- Spec: add Provides: for wg-quick

* Fri Mar 27 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0.20200319-alt1
- New version

* Thu Mar 12 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0.20200206-alt1
- New version
  + wireguard-tools becomes a separate repository in upstream
  + out-of-tree kernel module src code is transfered to wireguard-linux-compat
    repo for kernels before 5.6 (since 5.6 wireguard becomes in-tree module)
  + bash completions for wg and wg-quick are provided along with corresponding
    executables
  + examples are now provided as a separate package
- Fix path to wg-quick in a systemd unit file (closes: #37573)
- Spec: remove libmnl-devel from BR:, refer to upstream commit ef117a9

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
