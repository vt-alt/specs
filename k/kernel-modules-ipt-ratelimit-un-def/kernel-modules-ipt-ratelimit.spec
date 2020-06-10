%define module_name             ipt-ratelimit
%define module_version          0.3.1
%define module_release 		alt1

%define flavour		un-def
%define karch %ix86 x86_64 aarch64 ppc64le
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-un-def

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/kernel/net/netfilter

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: Linux kernel module for ipt-ratelimit
License: GPLv2
Group: System/Kernel and hardware
Url: https://github.com/aabc/ipt-ratelimit

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel cmake
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-iptables-ratelimit

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
%module_name kernel module for ipt-ratelimit

%prep
rm -rf iptables-ratelimit-%module_version
tar -jxvf %kernel_src/iptables-ratelimit-%module_version.tar.bz2
%setup -D -T -n iptables-ratelimit-%module_version

%build
chmod +x version.sh
make KDIR=%_usrsrc/linux-%kversion-%flavour xt_ratelimit.ko

%install
install -pD -m600 xt_ratelimit.ko %buildroot%module_dir/xt_ratelimit.ko

%files
%module_dir/xt_ratelimit.ko

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Thu Aug 17 2017 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt2
- Unpackaged %%module_dir/.
- Restricted access to %%module_dir/xt_ratelimit.ko (see #5969).

* Tue May 23 2017 Alexei Takaseev <taf@altlinux.org> 0.3-alt1
- 0.3

* Mon Nov 16 2015 Alexei Takaseev <taf@altlinux.org> 0.2-alt1
- 0.2

* Thu Oct 29 2015 Alexei Takaseev <taf@altlinux.org> 0.1-alt3
- Fix URL

* Sun Sep 27 2015 Alexei Takaseev <taf@altlinux.org> 0.1-alt2
- fix compilation for kernels > 3.18

* Fri Sep 25 2015 Alexei Takaseev <taf@altlinux.org> 0.1-alt1
- Initial RPM release
