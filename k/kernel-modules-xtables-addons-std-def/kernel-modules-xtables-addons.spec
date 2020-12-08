%define module_name	xtables-addons
%define module_version	3.13
%define module_release	alt1

%define flavour		std-def
%define karch %ix86 x86_64 aarch64 ppc64le
BuildRequires(pre): kernel-headers-modules-std-def
BuildRequires(pre): rpm-build-kernel
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name


Name:		kernel-modules-%module_name-%flavour
Version:	%module_version
Release:	%module_release.%kcode.%kbuildrelease

Packager:	Kernel Maintainer Team <kernel@packages.altlinux.org>

Group:		System/Kernel and hardware
Summary:	%module_name kernel module
URL:		http://xtables-addons.sourceforge.net/
License: GPLv2

ExclusiveOS:	Linux
BuildRequires: kernel-build-tools >= 0.7
BuildRequires: kernel-source-%module_name = %module_version
BuildRequires: rpm-build-licenses
ExclusiveArch: %karch

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Prereq:		coreutils
Prereq:         kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease

%description
Xtables-addons is the proclaimed successor to patch-o-matic(-ng). It
contains extensions that were not accepted in the main Xtables
package.

Xtables-addons is different from patch-o-matic in that you do not
have to patch or recompile either kernel or Xtables(iptables). But
please see the INSTALL file for the minimum requirements of this
package.

All code imported from patch-o-matic has been reviewed and all
apparent bugs like binary stability across multiarches, missing
sanity checks and incorrect endianess handling have been fixed,
simplified, and sped up.

%prep
rm -rf kernel-source-%module_name-%{module_version}*
tar xjf %kernel_src/kernel-source-%module_name-%module_version.tar.*
%setup -D -T -n kernel-source-%module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make -C %_usrsrc/linux-%kversion-%flavour TEMP_DIR=$(pwd) V=1 M=$(pwd) XA_ABSTOPSRCDIR=`pwd` modules

%install
mkdir -p %buildroot/%module_dir/
install -pD -m 0644 *.ko %buildroot/%module_dir/

#Remove not used modules
rm -f %buildroot/%module_dir/xt_TEE.ko

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Tue Nov 24 2020 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.13-alt1
- 3.11 -> 3.13

* Wed Sep 23 2020 Anton Farygin <rider@altlinux.ru> 3.11-alt1
- 3.10 -> 3.11

* Wed Sep 02 2020 Anton Farygin <rider@altlinux.ru> 3.10-alt1
- 3.9 -> 3.10

* Tue Mar 10 2020 Anton Farygin <rider@altlinux.ru> 3.9-alt1
- 3.7 -> 3.9

* Tue Dec  3 2019 Anton Farygin <rider@altlinux.ru> 3.7-alt1 
- 3.6 -> 3.7

* Wed Nov 27 2019 Anton Farygin <rider@altlinux.ru> 3.6-alt1
- 3.5 -> 3.6

* Wed Sep 11 2019 Anton Farygin <rider@altlinux.ru> 3.5-alt1
- 3.3 -> 3.5

* Mon Aug 19 2019 Nikolai Kostrigin <nickel@altlinux.org> 3.3-alt3
- fix build with upcoming kernel 5.3

* Tue Jun 18 2019 Anton Farygin <rider@altlinux.ru> 3.3-alt1
- new version

* Thu Mar 27 2014 Anton Farygin <rider@altlinux.ru> 2.4-alt1
- new version

* Fri Jan 13 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.39-alt3
- fix to build with 3.2 kernel

* Wed Oct 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.39-alt2
- 1.39

* Fri Apr 08 2011 Anton Protopopov <aspsk@altlinux.org> 1.33-alt2
- Use @kernelarch@

* Thu Feb 17 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.33-alt1
- 1.33

* Wed Oct 13 2010 Anton Farygin <rider@altlinux.ru> 1.30-alt1
- first build for Sisyphus

