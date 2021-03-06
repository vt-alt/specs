%define module_name     hinic
%define module_version  2.3.2.17
%define module_release  alt2
%define flavour         std-def
%define karch x86_64 aarch64

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/updates

Summary: Huawei(R) Intelligent Network Interface Card Driver
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL-2.0-only
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
Url: https://openeuler.org/en/

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Requires(pre): kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
Huawei(R) Intelligent Network Interface Card Driver

%prep
rm -rf kernel-source-%module_name-%module_version
tar -xf %kernel_src/kernel-source-%module_name-%module_version.tar*
%setup -D -T -n kernel-source-%module_name-%module_version

%build
make -C /lib/modules/*/build M=$PWD/drivers/net/ethernet/huawei/hinic modules CONFIG_HINIC=m -j

%install
install -d %buildroot/%module_dir
install -m644 -D drivers/net/ethernet/huawei/hinic/hinic.ko %buildroot/%module_dir/hinic.ko

%files
%module_dir/*.ko

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
