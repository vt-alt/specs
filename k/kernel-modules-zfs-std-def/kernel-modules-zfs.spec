%define module_name zfs
%define module_version 0.8.2
%define module_release alt2

%define flavour std-def
%define karch %ix86 x86_64 aarch64 ppc64le
BuildRequires(pre): kernel-headers-modules-std-def

%setup_kernel_module %flavour

%define strip_mod_opts --strip-unneeded -R .comment
%define module_dir /lib/modules/%kversion-%flavour-%krelease/fs

Summary: ZFS Linux modules
Name: kernel-modules-%module_name-%flavour
%define ksname %module_name
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: CDDL
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: http://zfsonlinux.org
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease

Provides: kernel-modules-spl-%flavour = %version-%release
Provides: kernel-modules-spl-%kversion-%flavour-%krelease = %version-%release

ExclusiveArch: %karch

%description
ZFS is an advanced file system and volume manager which was originally developed
for Solaris and is now maintained by the Illumos community.
ZFS on Linux, which is also known as ZoL, is currently feature complete.
It includes fully functional and stable SPA, DMU, ZVOL, and ZPL layers.
This package contains ZFS Linux kernel modules.

%prep
rm -rf %module_name-%module_version
tar xvf %kernel_src/%module_name-%module_version.tar.*
%setup -D -T -n %module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
export CC="gcc${GCC_VERSION:+-$GCC_VERSION}"
%configure --with-config=kernel --with-linux=%_usrsrc/linux-%kversion-%flavour
%make_build -C module

%install
%makeinstall_std -C module \
	INSTALL_MOD_DIR=$(basename %module_dir) \
	%{!?_enable_debug:%{?strip_mod_opts:INSTALL_MOD_STRIP="%strip_mod_opts"}}

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
