%define module_name e1000e
%define module_version 3.8.7
%define module_release alt1

%define module_source %module_name.tar

#### MODULE SOURCES ####
Name: kernel-source-%module_name
Version: %module_version
Release: %module_release
Summary: Linux %module_name modules sources for e1000 Intel(R) Ethernet adapter
License: GPLv2
Group: Development/Kernel
URL: https://sourceforge.net/projects/e1000
BuildArch: noarch

BuildRequires: kernel-build-tools

Source0: %module_source
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

%description
This %module_name contains the Linux kernel drivers for e1000 Intel(R) Ethernet
adapter. To learn more about Intel Ethernet visit
http://communities.intel.com/community/tech/wired

%prep
%setup -c -q
cd %module_name

find . -name '*.orig' -print -delete
cd ..
%__mv %module_name kernel-source-%module_name-%module_version

%install
%__mkdir_p %kernel_srcdir
%__tar -c  kernel-source-%module_name-%module_version | %__bzip2 -c > \
%kernel_srcdir/kernel-source-%module_name-%module_version.tar.bz2

%files
%_usrsrc/*

%changelog
* Tue Oct 27 2020 Andrey Cherepanov <cas@altlinux.org> 3.8.7-alt1
- New version.

* Thu Feb 06 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 3.4.2.1-alt2
- build with kernel 5.4 fixed

* Fri Oct 19 2018 Pavel Skrylev <majioa@altlinux.org> 3.4.2.1-alt1
- Bump to 3.4.2.1.

* Wed Nov 16 2011 Anton Protopopov <aspsk@altlinux.org> 1.6.3-alt1
- New version

* Mon Feb 21 2011 Anton Protopopov <aspsk@altlinux.org> 1.2.20-alt1
- Build for sisyphus
