%define module_name promethean

Name: activdriver
Version: 5.18.19
Release: alt1

Summary: Driver for Promethean ActivBoard and ActivHub
License: GPL-2.0
Group: Development/Kernel
URL: https://support.prometheanworld.com/product/activdriver

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kernel

%description
%{summary}.

%package -n kernel-source-%module_name
Summary: The kernel mode drivers for Promethean ActivBoard and ActivHub
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%module_name
%{summary}.

%prep
%setup -c
rm -f kernal/*.ko

%build
make KERN_INC=.. BUILD=release -C activlc

%install
install -Dpm0755 activlc/release/activlc %buildroot%_bindir/activlc
mkdir -p %kernel_srcdir
mkdir kernel-source-%module_name-%version
cp -a inc kernel kernel-source-%module_name-%version
tar -cjf %kernel_srcdir/kernel-source-%module_name-%version.tar.bz2 kernel-source-%module_name-%version

%files
%_bindir/activlc

%files -n kernel-source-%module_name
%attr(0644,root,root) %kernel_src/kernel-source-%module_name-%version.tar.bz2

%changelog
* Thu Mar 11 2021 Andrey Cherepanov <cas@altlinux.org> 5.18.19-alt1
- Initial build for Sisyphus.
