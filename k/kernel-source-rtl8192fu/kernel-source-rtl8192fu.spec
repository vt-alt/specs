Name: kernel-source-rtl8192fu
Version: 5.8.6.2
Release: alt1

Summary: RTL8192FU driver for Linux kernel
License: GPL-2.0
Group: Development/Kernel
URL: https://github.com/kelebek333/rtl8192fu-dkms
Packager: Andrey Cherepanov <cas@altlinux.org>

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-kernel

%description
RTL8192FU driver for Linux kernel.

%prep
%setup -q -c

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Fri Apr 09 2021 Andrey Cherepanov <cas@altlinux.org> 5.8.6.2-alt1
- Initial build for Sisyphus.
