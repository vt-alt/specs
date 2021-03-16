%define module_name     hifc
%define module_version  3.5.0.11
%define module_release  alt1
%define flavour         un-def
%define karch x86_64 aarch64

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

Summary: Huawei Hifc PCI Express Linux driver
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL-2.0-only
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
Url: https://openeuler.org/en/

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-un-def
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Requires(pre): kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
Huawei Hifc PCI Express Linux driver.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -xf %kernel_src/kernel-source-%module_name-%module_version.tar*
%setup -D -T -n kernel-source-%module_name-%module_version

%build
#sed -i s/SUBDIRS=/M=/g Makefile
make -C /lib/modules/*/build  M=$PWD/drivers/scsi/huawei/%module_name modules CONFIG_SCSI_FC_HIFC=m -j

%install
install -d %buildroot/%module_dir
install -m644 -D drivers/scsi/huawei/%module_name/%module_name.ko %buildroot/%module_dir/%module_name.ko

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
