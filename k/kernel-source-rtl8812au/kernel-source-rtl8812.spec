# -*- rpm-spec -*-
%define module_name	rtl8812au
%define module_version  7502.20200205

#### MODULE SOURCES ####
Name: kernel-source-rtl8812au
Version: %module_version
Release: alt1
Provides: kernel-source-%module_name-%module_version
Summary: Linux %module_name Realtek 8812 WiFi chipset series module sources
License: GPLv2
Group: Development/Kernel
URL: https://github.com/gnab/rtl8812au
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
BuildArch: noarch

Source: %name-%module_version.tar
#Patch:  rtl8812au-tpl-archiver.patch

BuildArch: noarch
BuildPreReq: rpm-build-kernel

%description
This is a fork of the Realtek 802.11ac (rtl8812au) v4.2.2 (7502.20130507)
driver altered to build on Linux kernel version >= 3.10.

%module_name module sources for Linux kernel.

%prep
%setup -c
cd %name-%module_version
#%patch -p1

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Wed Feb 05 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 7502.20200205-alt1
- updated from git
- build with kernel >=5.4 fixed

* Fri Nov  8 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 7502.20191011-alt1
- resurrect in sisyphus
- updated from git

* Mon Mar 27 2017 Hihin Ruslan <ruslandh@altlinux.ru> 7502.20130507-alt1
- first build for Sisyphus
