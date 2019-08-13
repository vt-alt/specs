%define module_name zfs
%define module_version 0.7.13
%define module_release alt2

%define flavour std-def
%define karch x86_64 i586
BuildRequires(pre): kernel-headers-modules-std-def

%setup_kernel_module %flavour

%define strip_mod_opts --strip-unneeded -R .comment
%define module_dir /lib/modules/%kversion-%flavour-%krelease/fs
%define splmod_dir /lib/modules/%kversion-%flavour-%krelease/lib

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
BuildRequires: kernel-source-spl = %module_version
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
%setup -cT
for i in spl %ksname; do
	tar -xf %kernel_src/$i-%module_version.tar*
done


%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
export CC="gcc${GCC_VERSION:+-$GCC_VERSION}"
cd spl*
%configure --with-config=kernel --with-linux=%_usrsrc/linux-%kversion-%flavour
%make_build -C module
SPL_SRC_DIR="$PWD"
cd ../%{ksname}*
%configure --with-config=kernel --with-linux=%_usrsrc/linux-%kversion-%flavour --with-spl="$SPL_SRC_DIR"
%make_build -C module


%install
Install()
{
	%makeinstall_std -C $1-%module_version/module \
		INSTALL_MOD_DIR="$(basename $2)" \
		%{!?_enable_debug:%{?strip_mod_opts:INSTALL_MOD_STRIP="%strip_mod_opts"}}
}

Install spl %splmod_dir
Install %ksname %module_dir
mv %buildroot%splmod_dir/{spl*/*.ko*,}
find %buildroot%splmod_dir -type d -empty -delete


%files
%splmod_dir
%module_dir


%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
