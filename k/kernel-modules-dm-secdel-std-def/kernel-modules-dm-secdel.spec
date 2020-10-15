%define module_name     dm-secdel
%define module_version  1.0.7
%define module_release  alt5
%define flavour         std-def
%define karch %ix86 x86_64 aarch64 ppc64le armh e2k e2kv4 e2kv5 e2kv6

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

Summary: dm-linear with secure deletion on discard
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Epoch: 1
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
Url: https://github.com/vt-alt/dm-secdel/

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
Requires: dmsetup
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
Linear device-mapper target with secure deletion on discard.

%prep
rm -rf %module_name-%module_version
tar xf %kernel_src/kernel-source-%module_name-%module_version.tar*
%setup -D -T -n %module_name-%module_version

%build
make VERSION=%version-%release -C %_usrsrc/linux-%kversion-%flavour-%krelease M=$(pwd) modules

%install
install -d %buildroot/%module_dir
install -m644 -D dm-secdel.ko %buildroot/%module_dir/

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %epoch:%version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
