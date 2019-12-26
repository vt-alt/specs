%define module_name             ixgbe
%define module_version          5.6.3
%define module_release          alt1

%define flavour		std-def
%define karch	%ix86 x86_64 aarch64 ppc64le

BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/ixgbe

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: Intel(R) 10GbE PCI Express Linux Network Driver
License: GPLv2
Group: System/Kernel and hardware
Url: http://www.intel.com/network/connectivity/products/server_adapters.htm

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name

Patch0: ixgbe-rename.patch

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Requires(pre): kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
%module_name contains the Intel(R) 10GbE PCI Express Linux Network Driver.

%prep
rm -rf %module_name-%module_version
tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version
%patch0 -p1

%build
pushd src
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make_build KSRC=%_usrsrc/linux-%kversion-%flavour
popd

%install
install -Dp -m600 src/%module_name.ko %buildroot/%module_dir/%module_name-ext.ko
install -d %buildroot/etc/modprobe.d
echo "blacklist %module_name" > %buildroot/etc/modprobe.d/blacklist-%module_name.conf

%files
/etc/modprobe.d/*
%module_dir/*

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Sat Nov 16 2019 Alexei Takaseev <taf@altlinux.org> 5.6.3-alt1
- initial build
