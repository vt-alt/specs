%define module_name	ipset
%define module_version	7.3
%define module_release	alt3

%define flavour		std-pae
%define karch %ix86
BuildRequires(pre): kernel-headers-modules-std-pae
%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/%module_name

Summary: ipset kernel modules
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL
Group: System/Kernel and hardware
ExclusiveArch: %ix86

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
URL: http://ipset.netfilter.org/
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version
BuildRequires: libmnl-devel

Provides:  kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: coreutils
PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease

%description
ipset kernel modules.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
autoreconf -fisv
%configure --with-kbuild=%_usrsrc/linux-%kversion-%flavour --with-ksource=%_usrsrc/linux-%kversion-%flavour
make modules

%install
install -d %buildroot%module_dir
install -p -m644 kernel/net/netfilter/ipset/*.ko %buildroot%module_dir
install -p -m644 kernel/net/netfilter/*.ko %buildroot%module_dir


%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Thu Aug  8 2019 Anton Farygin <rider@altlinux.ru> 7.3-alt1
- 7.1 -> 7.3

* Tue Jan 22 2019 Anton Farygin <rider@altlinux.ru> 7.1-alt1
- 7.0 -> 7.1

* Wed Nov 14 2018 Anton Farygin <rider@altlinux.ru> 7.0-alt1
- 6.29 -> 7.0

* Tue Jul 26 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 6.29-alt2
- build with 4.7 kernel fixed

* Tue Jun 28 2016 Anton Farygin <rider@altlinux.ru> 6.29-alt1
- new version

* Tue Sep 29 2015 Anton V. Boyarshinov <boyarsh@altlinux.org> 6.26-alt1
- new version

* Wed Feb 11 2015 Anton Farygin <rider@altlinux.ru> 6.24-alt1
- new version

* Wed Sep 24 2014 Anton Farygin <rider@altlinux.ru> 6.23-alt1
- new version

* Mon Mar 24 2014 Anton V. Boyarshinov <boyarsh@altlinux.org> 6.21-alt1
- new version

* Fri Nov 15 2013 Anton Farygin <rider@altlinux.ru> 6.20.1-alt1
- new version

* Fri Jun 28 2013 Anton V. Boyarshinov <boyarsh@altlinux.org> 6.19-alt1
- new version

* Wed Oct 13 2010 Anton Farygin <rider@altlinux.ru> 4.4-alt1
- new version

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 4.3-alt1
- new version 

* Mon Jan 25 2010 Anton Farygin <rider@altlinux.ru> 4.1-alt1
- fisrt build for Sisyphus, specfile from Igor Zubkov
