%define module_name rtl88x2bu
%define module_version 5.8.7.1
%define module_release alt1

%define flavour	std-def
%define karch %ix86 x86_64
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/net/wireless/realtek/rtlwifi/%module_name

Name: kernel-modules-%module_name-%flavour
Group: System/Kernel and hardware
Summary: Module for Realtek RTL88x2bu
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
Url: https://github.com/tomaspinho/rtl8821ce.git
License: GPLv2

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
ExclusiveArch: %ix86 x86_64

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

%description
These packages contain Realtek RTL88x2bu module.

%prep
rm -rf kernel-source-%module_name-%module_version
tar xvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make_build \
    ARCH=%base_arch \
    CROSS_COMPILE= \
    KSRC=%_usrsrc/linux-%kversion-%flavour \
    modules \
    USER_EXTRA_CFLAGS="-Wno-error=date-time -Wno-error=incompatible-pointer-types"

%install
install -D -m 644 88x2bu.ko %buildroot/%module_dir/%module_name.ko

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
