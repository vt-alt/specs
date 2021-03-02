%define module_name             ixgbe
%define module_version          5.10.2
%define module_release          alt1

%define flavour		std-def
%define karch	x86_64 aarch64 ppc64le

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
Patch1: allow-all-sfp.patch

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
%patch1 -p1

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
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Mon Feb 08 2021 Alexei Takaseev <taf@altlinux.org> 5.10.2-alt1
- 5.10.2
- Allow all vendors sfp+

* Thu Oct 01 2020 Alexei Takaseev <taf@altlinux.org> 5.9.4-alt1
- 5.9.4

* Wed Aug 19 2020 Alexei Takaseev <taf@altlinux.org> 5.8.1-alt1
- 5.8.1
- Build 64bit-only

* Thu May 21 2020 Alexei Takaseev <taf@altlinux.org> 5.7.1-alt1
- 5.7.1
- Added support for 5.6 kernel version

* Wed May 13 2020 Alexei Takaseev <taf@altlinux.org> 5.6.4-alt1
- 5.6.4
- Fix build with kernel >= 5.4

* Sat Nov 16 2019 Alexei Takaseev <taf@altlinux.org> 5.6.3-alt1
- initial build
