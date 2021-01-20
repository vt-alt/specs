%define module_name LiME
%define module_version 1.9.1
%define module_release	alt2

%define module_source	%module_name-%module_version.tar

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: %module_release
Provides: kernel-source-%module_name-%module_version
Summary: Linux %module_name modules sources for LiME.
License: GPLv2
Group: Development/Kernel
BuildArch: noarch

BuildRequires: kernel-build-tools

Source0: %module_source
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

%description
%module_name Linux Memory Extractor module sources for Linux kernel.

%prep
%setup -n %module_name-%module_version

%install
%__mkdir_p %kernel_srcdir
cd ..
%__mv %module_name-%module_version kernel-source-%module_name-%module_version
%__tar -c  kernel-source-%module_name-%module_version | %__bzip2 -c > \
	%kernel_srcdir/kernel-source-%module_name-%module_version.tar.bz2

%files
%_usrsrc/*

%changelog
* Wed Dec 16 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.9.1-alt2
- compat with kernel 5.10

* Tue Oct 06 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.9.1-alt1
- 1.9.1

* Wed Jun 19 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.8.1-alt1
- 1.8.1 (kernels 4.14+ support)

* Tue Jul 11 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.7.8-alt1
- 1.7.6

* Wed Aug 24 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.7.5-alt1
- 1.7.5

* Tue Jan 20 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1-alt1
- initial build

