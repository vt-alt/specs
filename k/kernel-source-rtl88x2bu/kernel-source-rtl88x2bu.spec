%define module_name     rtl88x2bu
%define module_version  35809.20191129

Name: kernel-source-rtl88x2bu
Version: 5.8.7.1
Release: alt1

Summary: Linux %module_name for Realtek DWA-182 Wireless AC Dual Band USB Adapter
URL: https://support.dlink.ca/ProductInfo.aspx?m=DWA-182
Group: Development/Kernel
License: GPL-2.0

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
BuildArch: noarch

# Got from ftp://ftp.dlink.ca/PRODUCTS/DWA-182/DWA-182_REVD_DRIVERS_v5.8.7.1_LINUX.ZIP
Source: %name-%version.tar

BuildRequires(pre): rpm-build-kernel

%description
%{summary}.

%prep
%setup -c

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Sat Oct 24 2020 Andrey Cherepanov <cas@altlinux.org> 5.8.7.1-alt1
- Initial build for Sisyphus.
