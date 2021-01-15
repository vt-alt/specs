%define module_name     vhba
%define module_version  20200106
%define module_release alt1.k

%define flavour         std-def
%define karch %ix86 x86_64
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/extra

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: VHBA virtual host bus adapter module
License: GPLv2
Group: System/Kernel and hardware

Url: http://cdemu.sourceforge.net/
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel
BuildPreReq: rpm-build-ubt

BuildRequires: module-init-tools
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %EVR
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %EVR

Requires(pre): kernel-image-%flavour = %kepoch%kversion-%krelease

Requires: vhba-udev-rules
ExclusiveArch: %karch

%description
VHBA kernel module, a virtual SCSI host bus adapter used by CDEmu daemon from
userspace-cdemu suite.

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make_build KDIR=%_usrsrc/linux-%kversion-%flavour

%install
install -d %buildroot/%module_dir
cp -a %module_name.ko %buildroot/%module_dir/

%files
%dir %module_dir
%module_dir/%module_name.ko

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Mon Nov 02 2020 Nazarov Denis <nenderus@altlinux.org> 20200106-alt1
- Version 20200106

* Mon Jun 17 2019 Nazarov Denis <nenderus@altlinux.org> 20190410-alt1
- Version 20190410

* Mon Jul 31 2017 Nazarov Denis <nenderus@altlinux.org> 20170610-alt1
- Version 20170610

* Tue Jul 11 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 20161009-alt2
- fixed build with kernel 4.12

* Thu Oct 13 2016 Nazarov Denis <nenderus@altlinux.org> 20161009-alt1
- Version 20161009

* Tue Oct 07 2014 Nazarov Denis <nenderus@altlinux.org> 20140928-alt1
- Version 20140928

* Tue Jul 15 2014 Nazarov Denis <nenderus@altlinux.org> 20140629-alt3
- Move init script to cdemu-daemon

* Fri Jul 04 2014 Nazarov Denis <nenderus@altlinux.org> 20140629-alt1.M70T.1
- Build for branch t7

* Thu Jul 03 2014 Nazarov Denis <nenderus@altlinux.org> 20140629-alt2
- Fix correct unload vhba module when CDemu daemon is running

* Wed Jul 02 2014 Nazarov Denis <nenderus@altlinux.org> 20140629-alt1
- Version 20140629

* Wed Jul 02 2014 Nazarov Denis <nenderus@altlinux.org> 20140629-alt1
- Version 20140629

* Sun Jun 09 2013 Nazarov Denis <nenderus@altlinux.org> 20130607-alt1
- Version 20130607

* Mon Dec 17 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 20120422-alt2
- new template

* Wed Apr 25 2012 Nazarov Denis <nenderus@altlinux.org> 20120422-alt1
- Version 20120422

* Tue Oct 11 2011 Anton Protopopov <aspsk@altlinux.org> 20110915-alt4
- Don't pack 60-vhba.rules, use vhba-udev-rules package (ALT 26335)

* Tue Sep 20 2011 Anton Protopopov <aspsk@altlinux.org> 20110915-alt3
- Technical

* Tue Sep 20 2011 Nazarov Denis <nenderus@altlinux.org> 20110915-alt2
- Add init script

* Sun Sep 18 2011 Nazarov Denis <nenderus@altlinux.org> 20110915-alt1
- Version 20110915

* Thu Jun 09 2011 Nazarov Denis <nenderus@altlinux.org> 1.2.1.20110416-alt1
- Version 1.2.1.20110416

* Sat Nov 20 2010 Nazarov Denis <nenderus@altlinux.org> 1.2.1.20100822-alt1
- Initial build for ALT Linux
