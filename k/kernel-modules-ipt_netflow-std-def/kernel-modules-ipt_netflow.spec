%define module_name	ipt_netflow
%define module_version	2.5

%define module_release alt1.k

%define flavour		std-def
%define karch %ix86 x86_64 aarch64 ppc64le
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

Summary: Netflow iptables module for Linux kernel 
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: http://sourceforge.net/projects/ipt-netflow/
BuildRequires(pre): rpm-build-kernel
BuildRequires: iptables-devel
BuildRequires: rpm >= 4.0.2-75
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
Ipt-netflow is very fast and effective Netflow exporting module for
Linux kernel. Designed for Linux router with heavy network load.
This is netfilter/iptables module adding support for NETFLOW target.

%prep
rm -rf %module_name-%{module_version}*
tar xf %kernel_src/%module_name-%module_version.tar.*
%setup -D -T -n %module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
./configure --kdir=%_usrsrc/linux-%kversion-%flavour-%krelease
make KDIR=%_usrsrc/linux-%kversion-%flavour-%krelease

%install
mkdir -p %buildroot/%module_dir
install ipt_NETFLOW.ko %buildroot/%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Tue Feb 10 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru>  2.1-alt1
- new version

* Wed Oct 22 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru>  2.0.1-alt1
- new version

* Fri Sep  6 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru>  1.8-alt3
- Build with 3.11 fixed

* Wed Jul 17 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru>  1.8-alt2
- Build with 3.10 fixed
