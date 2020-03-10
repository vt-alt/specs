%define module_name     linux-gpib
%define module_version  4.3.0
%define module_release  alt3
%define flavour std-def
%define karch   %ix86 x86_64 aarch64 ppc64le

BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def
%setup_kernel_module %flavour
%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: %module_name kernel modules
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
URL: http://linux-gpib.sourceforge.net/
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Requires(pre,postun): coreutils
Requires(pre,postun): kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
%module_name kernel modules.

%prep
rm -rf %module_name-kernel-%module_version
tar -jxf %kernel_src/%module_name-%module_version.tar.bz2
%setup -D -T -n %module_name-kernel-%module_version
echo > ./configure
chmod 755 ./configure

%build
LINUX_SRCDIR=%_usrsrc/linux-%kversion-%flavour make

%install
install -d %buildroot%module_dir
install -p -m644 drivers/gpib/*/*.ko %buildroot%module_dir

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

