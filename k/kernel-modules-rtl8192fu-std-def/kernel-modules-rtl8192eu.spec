%define module_name	rtl8192fu
%define module_version	5.8.6.2
%define module_release	alt1

%define flavour		std-def
%define karch		%ix86 x86_64
BuildRequires(pre): kernel-headers-modules-std-def
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Patch: error-date-time.patch

Summary: RTL8192FU driver for Linux kernel
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL-2.0
Group: System/Kernel and hardware

Packager: Andrey Cherepanov <cas@altlinux.org>

ExclusiveOS: Linux
URL: https://github.com/kelebek333/rtl8192fu-dkms
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kversion-%krelease
Requires(postun): kernel-image-%flavour = %kversion-%krelease
ExclusiveArch: %karch

%description
RTL8192FU driver for Linux kernel.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version
%patch

%build
%make_build KSRC=%_usrsrc/linux-%kversion-%flavour

%install
install -d %buildroot%module_dir
install 8192fu.ko %buildroot%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Fri Apr 09 2021 Andrey Cherepanov <cas@altlinux.org> 5.8.6.2-alt1
- Initial build
