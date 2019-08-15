%define module_name     kvdo
%define module_version  6.2.1.138
%define module_release  alt2
%define flavour         un-def
# Note: This project can only be built on x86_64, ppc, and aarch64.
%define karch           x86_64

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

Summary: Kernel Modules for Virtual Data Optimizer
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2+
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
Url: http://github.com/dm-vdo/kvdo

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-un-def
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release
PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExcludeArch: i586
ExclusiveArch: %karch

%description
Virtual Data Optimizer (VDO) is a device mapper target that delivers
block-level deduplication, compression, and thin provisioning.

%prep
rm -rf %module_name-%module_version
tar xf %kernel_src/kernel-source-%module_name-%module_version.tar*
%setup -D -T -n %module_name-%module_version

%build
make -C %_usrsrc/linux-%kversion-%flavour-%krelease M=$(pwd) modules KCFLAGS=-Wno-vla

%install
install -d %buildroot/%module_dir
install -m644 -D vdo/kvdo.ko %buildroot/%module_dir/
install -m644 -D uds/uds.ko %buildroot/%module_dir/

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
