%define module_name	r8168
%define module_release	alt1.k
%define module_version	8.047.05

%define flavour		std-def
%define karch %ix86 x86_64

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/kernel/drivers/net

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: Linux driver for RealTek Ethernet controllers
License: GPLv2+
Group: System/Kernel and hardware

URL: http://www.realtek.com/
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
ExclusiveArch: %karch

BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def

BuildRequires: module-init-tools
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Requires(pre): kernel-image-%flavour = %kepoch%kversion-%krelease

Requires: r8168-blacklist
 
Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release kernel-modules-rtl8168-%flavour
Obsoletes: kernel-modules-rtl8168-%flavour
Conflicts: kernel-modules-rtl8168-%flavour

%description
RTL8168 is the Linux device driver released for RealTek RTL8168B/8111B,
RTL8168C/8111C, RTL8168CP/8111CP, RTL8168D/8111D, and RTL8168DP/8111DP
Gigabit Ethernet controllers with PCI-Express interface.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make_build KERNELDIR=%_usrsrc/linux-%kversion-%flavour modules

%install
install -Dp -m600 src/%module_name.ko %buildroot/%module_dir/%module_name.ko

%files
%module_dir/%module_name.ko

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Wed Nov 27 2019 Nazarov Denis <nenderus@altlinux.org> 8.047.05-alt1
- Version 8.047.05

* Fri Jun 14 2019 Nazarov Denis <nenderus@altlinux.org> 8.047.01-alt1
- Version 8.047.01

* Sun Nov 12 2017 Nazarov Denis <nenderus@altlinux.org> 8.045.08-alt1
- Version 8.045.08

* Thu Aug 17 2017 Dmitry V. Levin <ldv@altlinux.org> 8.044.02-alt4
- Unpackaged %%module_dir/.
- Restricted access to %%module_dir/%module_name.ko (see #5969).

* Tue Jul 11 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.042.00-alt3
- build with kernel 4.11 fixed

* Sun Mar 12 2017 Nazarov Denis <nenderus@altlinux.org> 8.044.02-alt1
- Version 8.044.02

* Fri Oct 14 2016 Nazarov Denis <nenderus@altlinux.org> 8.043.01-alt1
- Version 8.043.01

* Thu Aug 18 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.042.00-alt3
- build with kernel 4.7 fixed

* Tue Jul 19 2016 Nazarov Denis <nenderus@altlinux.org> 8.042.00-alt2
- build for kernel un-def

* Tue Jul 12 2016 Nazarov Denis <nenderus@altlinux.org> 8.042.00-alt1
- Version 8.042.00

* Wed Mar 16 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.041.01-alt2
- build with kernel 4.5 fixed

* Sat Jan 16 2016 Nazarov Denis <nenderus@altlinux.org> 8.041.01-alt1
- Version 8.041.01

* Tue Jun 23 2015 Nazarov Denis <nenderus@altlinux.org> 8.040.00-alt1
- Version 8.040.00

* Thu Sep 25 2014 Nazarov Denis <nenderus@altlinux.org> 8.039.00-alt1
- Version 8.039.00

* Wed Mar 19 2014 Nazarov Denis <nenderus@altlinux.org> 8.038.00-alt1
- Version 8.038.00

* Tue Oct 01 2013 Nazarov Denis <nenderus@altlinux.org> 8.037.00-alt1
- Version 8.037.00

* Wed Jul 17 2013 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.036.00-alt2
- build with kernel 3.10 fixed

* Sat Jun 15 2013 Nazarov Denis <nenderus@altlinux.org> 8.036.00-alt1
- Version 8.036.00

* Thu May 23 2013 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.035.00-alt4
- conflicts with other versions removed

* Wed Feb 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.035.00-alt3
- build with kernel 3.8 fixed

* Wed Jan 30 2013 Nazarov Denis <nenderus@altlinux.org> 8.035.00-alt2
- New template

* Tue Jan 29 2013 Nazarov Denis <nenderus@altlinux.org> 8.035.00-alt1
- Version 8.035.00

* Sat Dec 03 2011 Nazarov Denis <nenderus@altlinux.org> 8.027.00-alt2
- Add provides and obsoletes

* Fri Dec 02 2011 Nazarov Denis <nenderus@altlinux.org> 8.027.00-alt1
- Version 8.027.00

* Sat Oct 29 2011 Nazarov Denis <nenderus@altlinux.org> 8.026.00-alt1
- Version 8.026.00

* Fri Aug 26 2011 Nazarov Denis <nenderus@altlinux.org> 8.025.00-alt1
- Version 8.025.00

* Sun May 29 2011 Nazarov Denis <nenderus@altlinux.org> 8.024.00-alt1
- Version 8.024.00

* Sat Apr 23 2011 Nazarov Denis <nenderus@altlinux.org> 8.023.00-alt1
- Version 8.023.00

* Sun Mar 27 2011 Nazarov Denis <nenderus@altlinux.org> 8.022.00-alt1
- Version 8.022.00

* Tue Feb 01 2011 Nazarov Denis <nenderus@altlinux.org> 8.021.00-alt1
- Version 8.021.00

* Mon Jan 03 2011 Nazarov Denis <nenderus@altlinux.org> 8.020.00-alt1
- Initial build for ALT Linux
