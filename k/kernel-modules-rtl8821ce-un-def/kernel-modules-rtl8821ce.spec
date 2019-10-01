%define module_name rtl8821ce
%define module_version 5.5.2
%define module_release alt1

%define flavour	un-def
%define karch %ix86 x86_64
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-un-def

%setup_kernel_module %flavour

%define _moduledir /lib/modules/%kversion-%flavour-%krelease

Name: kernel-modules-%module_name-%flavour
Group: System/Kernel and hardware
Summary: Module for Realtek RTL8821CE
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
These packages contain Realtek RTL8821CE module.

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
    USER_EXTRA_CFLAGS="-Wno-error=date-time -Wno-error=incompatible-pointer-types" \
    V=1

%install
install -D -m 644 %module_name.ko %buildroot%_moduledir/net/wireless/realtek/rtlwifi/%module_name.ko

%files
%dir %_moduledir/net
%dir %_moduledir/net/wireless
%dir %_moduledir/net/wireless/realtek
%dir %_moduledir/net/wireless/realtek/rtlwifi
%_moduledir/net/wireless/realtek/rtlwifi/*

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
