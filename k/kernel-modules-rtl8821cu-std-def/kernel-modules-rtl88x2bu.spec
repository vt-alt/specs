%define module_name rtl8821cu
%define module_version 5.4.1
%define module_release alt3

%define flavour	std-def
%define karch %ix86 x86_64 aarch64
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/net/wireless/realtek/%module_name

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: Realtek RTL8811CU/RTL8821CU USB wifi adapter driver
Group: System/Kernel and hardware
License: GPL-2.0
URL: https://github.com/brektrou/rtl8821CU

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
ExclusiveArch: %karch

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
BuildRequires: bc

Patch0: rtl8821cu-no-float.patch

%description
%{summary}.

%prep
rm -rf kernel-source-%module_name-%module_version
tar xvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%patch0 -p0

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make_build \
    ARCH=%base_arch \
    CROSS_COMPILE= \
    KSRC=%_usrsrc/linux-%kversion-%flavour \
    modules \
    USER_EXTRA_CFLAGS="-Wno-error=date-time -Wno-error=incompatible-pointer-types"

%install
install -Dm0644 *.ko %buildroot/%module_dir/%module_name.ko

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
