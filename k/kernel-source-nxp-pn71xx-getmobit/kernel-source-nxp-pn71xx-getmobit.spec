%define _unpackaged_files_terminate_build 1

Name: kernel-source-nxp-pn71xx-getmobit

Version: 1.4
Release: alt3

Summary: NXP's NFC Open Source Kernel mode driver optimized for GM-box
License: GPLv2
Group: Development/Kernel
BuildArch: noarch
Url: https://www.getmobit.ru

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-kernel

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
* Thu Mar 12 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.4-alt3
- Spec: remove unnecessary BR: libmnl-devel inherited from spec template

* Wed Feb 05 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.4-alt2
- Fix build for kernels after 5.5
  + "pr_warning" was renamed to "pr_warn"

* Fri Jun 07 2019 Nikolai Kostrigin <nickel@altlinux.org> 1.4-alt1
- Initial build for OS ALT
