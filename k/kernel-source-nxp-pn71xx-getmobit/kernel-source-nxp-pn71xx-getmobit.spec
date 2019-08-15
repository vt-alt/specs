%define _unpackaged_files_terminate_build 1

Name: kernel-source-nxp-pn71xx-getmobit

Version: 1.4
Release: alt1

Summary: NXP's NFC Open Source Kernel mode driver optimized for GM-box
License: GPLv2
Group: Development/Kernel
BuildArch: noarch
Url: https://www.getmobit.ru

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-kernel
BuildRequires: libmnl-devel

%description
Source package for NXP's NFC Open Source Kernel mode driver optimized for GM-box

%prep
%setup

%build

%install

tar xvf %SOURCE0
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Fri Jun 07 2019 Nikolai Kostrigin <nickel@altlinux.org> 1.4-alt1
- Initial build for OS ALT
