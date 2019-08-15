%define module_name	xtables-addons
%define module_version	2.14
%define module_release	alt3

%define flavour		std-pae
%define karch %ix86
BuildRequires(pre): kernel-headers-modules-std-pae
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
License: GPL 

ExclusiveOS:	Linux
BuildRequires: kernel-build-tools >= 0.7
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
BuildRequires: rpm-build-licenses
ExclusiveArch: %karch

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Prereq:		coreutils
Prereq:         kernel-image-%flavour = %kepoch%kversion-%krelease

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
%make -C %_usrsrc/linux-%kversion-%flavour TEMP_DIR=$(pwd) V=1 SUBDIRS=$(pwd) XA_ABSTOPSRCDIR=`pwd` modules

%install
mkdir -p %buildroot/%module_dir/
install -pD -m 0644 *.ko %buildroot/%module_dir/

#Remove not used modules
rm -f %buildroot/%module_dir/xt_TEE.ko

%files
%module_dir/*

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

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

