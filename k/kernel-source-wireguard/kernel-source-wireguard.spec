%define _unpackaged_files_terminate_build 1

Name: kernel-source-wireguard

Version: 1.0.20200712
Release: alt1

Summary: Source for WireGuard: fast, modern, secure VPN tunnel
Summary(ru_RU.UTF-8): Исходный код WireGuard, быстрого, современного, защищенного VPN туннеля
License: GPLv2
Group: Development/Kernel
Url: https://www.wireguard.com/
#Git: https://git.zx2c4.com/wireguard-linux-compat
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-kernel

%description
Src package for WireGuard.
WireGuard is an extremely simple yet fast and modern VPN that utilizes
state-of-the-art cryptography.

WireGuard was merged into the Linux kernel for 5.6. This package contains source
code of backport of WireGuard for kernels 3.10 to 5.5, as an out of tree module.

%prep
%setup

%build

%install
tar xvf %SOURCE0
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Tue Jul 14 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0.20200712-alt1
- New version

* Fri Jun 26 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0.20200623-alt1
- New version

* Sat Jun 13 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0.20200611-alt1
- New version

* Fri May 22 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0.20200520-alt1
- New version

* Thu May 07 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0.20200506-alt1
- New version

* Thu Apr 30 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0.20200429-alt1
- New version

* Mon Apr 27 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0.20200426-alt1
- New version

* Tue Apr 14 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0.20200413-alt1
- New version

* Mon Apr 06 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0.20200401-alt1
- New version

* Tue Mar 31 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0.20200330-alt1
- New version
  + source code is in sync with kernel 5.6 released on 2020.03.29

* Fri Mar 27 2020 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20200318-alt1
- New version

* Thu Mar 12 2020 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20200215-alt1
- New version
  + provides only source files package for kernel-module-wireguard from
  wireguard-linux-compat git repo (out-of-tree kernel module)

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
