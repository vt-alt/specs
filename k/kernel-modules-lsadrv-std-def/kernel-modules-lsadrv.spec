%define module_name             lsadrv
%define module_version          1.2.3
%define module_release alt4

%define flavour		std-def
%define karch		%ix86 x86_64
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Name: kernel-modules-%module_name-%flavour
Epoch: 1
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: Linux Kernel drivers supporting Hitachi StarBoard interactive whiteboard
License: GPL-3.0+
Group: System/Kernel and hardware
Url: http://www.charmexdocs.com/int/software/SBS0962_LINUX.zip

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name-%module_version

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
%module_name kernel driver for Linux.
This is usable for Hitachi StarBoard interactive whiteboard.
    FX-63/77(G)/82(WG) Wired
    FX-DUO-63/77/88W Wired
    FX-TRIO-77/77(S)/88W

This is module for your ALT Linux system.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make KERNEL_SRC=%_usrsrc/linux-%kversion-%flavour-%krelease \
    KERNELRELEASE=%kversion-%flavour-%krelease \
    %kversion-%flavour-%krelease/%module_name.ko

%install
install -d %buildroot/%module_dir
cp -a %kversion-%flavour-%krelease/%module_name.ko %buildroot/%module_dir/

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %epoch:%version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Thu Oct 27 2016 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:1.2.3-alt2
- disabled all /proc related code

* Wed Feb 24 2016 Andrey Cherepanov <cas@altlinux.org> 1:1.2.3-alt1
- new version
- change project homepage

* Wed Jul 17 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.0.1-alt3
- build with kernel 3.10 fixed

* Mon Dec 17 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.0.1-alt2
- new template

* Fri Feb 4 2011 Rinat Bikov <becase@altlinux.ru> 2.0.1-alt1
- intial build for altlinux
