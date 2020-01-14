%define module_name	wireguard
%define module_version	0.0.20191219
%define module_release	alt1

%define flavour		std-def
%define karch %ix86 x86_64 aarch64 ppc64le
BuildRequires(pre): kernel-headers-modules-std-def
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: Wireguard is a fast, modern, secure VPN tunnel module for Linux kernel
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
URL: https://www.wireguard.com/
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch 

%description
WireGuard kernel module.
WireGuard is an extremely simple yet fast and modern VPN that utilizes
state-of-the-art cryptography. It aims to be faster, simpler, leaner, and more
useful than IPSec, while avoiding the massive headache. It intends to be
considerably more performant than OpenVPN. WireGuard is designed as a general
purpose VPN for running on embedded interfaces and super computers alike, fit
for many different circumstances. Initially released for the Linux kernel, it
plans to be cross-platform and widely deployable. It is currently under heavy
development, but already it might be regarded as the most secure, easiest to
use, and simplest VPN solution in the industry.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version/src

%build
%make_build -C %_usrsrc/linux-%kversion-%flavour M=`pwd` modules

%install
install -d %buildroot%module_dir
install wireguard.ko %buildroot%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Mon Dec 23 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20191219-alt1
- New version 0.0.20191219

* Thu Dec 12 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20191212-alt1
- New version 0.0.20191212

* Sun Dec 08 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20191206-alt1
- New version 0.0.20191206

* Thu Dec 05 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20191205-alt1
- New version 0.0.20191205

* Thu Nov 28 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20191127-alt1
- New version 0.0.20191127

* Sun Oct 13 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20191012-alt1
- New version 0.0.20191012

* Mon Sep 30 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20190913-alt1
- New version 0.0.20190913

* Fri Sep 06 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20190905-alt1
- New version 0.0.20190905
- Fix build with upcoming kernel 5.3

* Thu Jul 04 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20190702-alt1
- New version 0.0.20190702

* Sun Jun 02 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20190601-alt1
- New version 0.0.20190601
- Add missing previous changelog item

* Sat May 04 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.20190406-alt2
- build fixed

* Tue Apr 23 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20190406-alt1
- New version 0.0.20190406

* Mon Mar 04 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20190227-alt1
- New version 0.0.20190227

* Wed Dec 31 2018 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20181218-alt1
- New version 0.0.20181218

* Wed Sep 12 2018 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20180910-alt1
- New version 0.0.20180910

* Wed Jul 04 2018 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20180625-alt1
- New version 0.0.20180625

* Fri Jun 15 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.0.20180625-alt1.k
- Add karch specsubst

* Tue Apr 17 2018 Nikolai Kostrigin <nickel@altlinux.org> 0.0.20180413-alt1
- Initial build

