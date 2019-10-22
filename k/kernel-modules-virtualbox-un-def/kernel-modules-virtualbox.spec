%define module_name	virtualbox
%define module_version	5.2.34

%define module_release	alt1

%define drv_module_name	vboxdrv
%define pci_module_name	vboxpci
%define net_module_name	vboxnetflt
%define net_module_adaptor_name	vboxnetadp

%define flavour		un-def
%define karch %ix86 x86_64
BuildRequires(pre): rpm-build-kernel >= 0.100-alt1
BuildRequires(pre): kernel-headers-modules-un-def

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

Summary: VirtualBox modules
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPL
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: http://www.virtualbox.org/

BuildPreReq: gcc-c++
BuildRequires: perl
BuildRequires: rpm >= 4.0.2-75
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%drv_module_name = %module_version
BuildRequires: kernel-source-%pci_module_name = %module_version
BuildRequires: kernel-source-%net_module_name = %module_version
BuildRequires: kernel-source-%net_module_adaptor_name = %module_version

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

Requires: %module_name-common

%description
This package contains VirtualBox modules (vboxdrv) that are needed
for VirtualBox to run. Note that you have to compile these modules on the
system with your VirtualBox version installed or you will have to specify
your VirtualBox version as `version' parameter when loading these modules
or in your /etc/modules.conf file.

%prep
%setup -T -c -n kernel-source-%module_name-%module_version
tar jxvf %kernel_src/kernel-source-%drv_module_name-%module_version.tar.bz2
pushd kernel-source-%drv_module_name-%module_version
popd
tar jxvf %kernel_src/kernel-source-%pci_module_name-%module_version.tar.bz2
tar jxvf %kernel_src/kernel-source-%net_module_name-%module_version.tar.bz2
tar jxvf %kernel_src/kernel-source-%net_module_adaptor_name-%module_version.tar.bz2

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make -C kernel-source-%drv_module_name-%module_version \
    KERN_DIR=%_usrsrc/linux-%kversion-%flavour/ KERN_VER=%kversion
cp kernel-source-%drv_module_name-%module_version/Module.symvers \
    kernel-source-%pci_module_name-%module_version
%make -C kernel-source-%pci_module_name-%module_version \
    KERN_DIR=%_usrsrc/linux-%kversion-%flavour/ KERN_VER=%kversion
cp kernel-source-%drv_module_name-%module_version/Module.symvers \
    kernel-source-%net_module_name-%module_version
%make -C kernel-source-%net_module_name-%module_version \
    KERN_DIR=%_usrsrc/linux-%kversion-%flavour/ KERN_VER=%kversion
cp kernel-source-%drv_module_name-%module_version/Module.symvers \
    kernel-source-%net_module_adaptor_name-%module_version
%make -C kernel-source-%net_module_adaptor_name-%module_version \
    KERN_DIR=%_usrsrc/linux-%kversion-%flavour/ KERN_VER=%kversion

%install
mkdir -p %buildroot/%module_dir
install -pD -m644 kernel-source-%drv_module_name-%module_version/vboxdrv.ko \
    %buildroot%module_dir/
install -pD -m644 kernel-source-%pci_module_name-%module_version/vboxpci.ko \
    %buildroot%module_dir/
install -pD -m644 kernel-source-%net_module_name-%module_version/vboxnetflt.ko \
    %buildroot%module_dir/
install -pD -m644 kernel-source-%net_module_adaptor_name-%module_version/vboxnetadp.ko \
    %buildroot%module_dir/

%files
%defattr(644,root,root,755)
%module_dir

%changelog
* %(LC_TIME=C date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Mon Oct 21 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.34-alt1
- Updated template for virtualbox 5.2.34

* Wed Aug 14 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.2.30-alt2
- Build only on %%ix86 and x86_64.

* Tue Jun 09 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.30-alt1
- Updated template for virtualbox 5.2.30

* Fri Feb 08 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.26-alt1
- Updated template for virtualbox 5.2.26

* Wed Jan 16 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.24-alt1
- Updated template for virtualbox 5.2.24

* Fri Oct 19 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.22-alt1
- Updated template for virtualbox 5.2.22

* Fri Oct 19 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.20-alt1
- Updated template for virtualbox 5.2.20

* Mon Oct 15 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.18-alt1
- Updated template for virtualbox 5.2.18

* Thu Jul 19 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.16-alt1
- Updated template for virtualbox 5.2.16

* Thu May 24 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.12-alt1
- Updated template for virtualbox 5.2.12

* Tue Dec 26 2017 Denis Medvedev <nbr@altlinux.org> 5.1.30-alt2
- updated for correct building on un-def

* Tue Nov 14 2017 Denis Medvedev <nbr@altlinux.org> 5.1.30-alt1
- Updated template for virtualbox 5.1.30

* Thu Jul 20 2017 Denis Medvedev <nbr@altlinux.org> 5.1.24-alt1
- Updated template for virtualbox 5.1.24

* Thu Mar 16 2017 Denis Medvedev <nbr@altlinux.org> 5.1.18-alt1
- Updated template for virtualbox 5.1.18

* Thu Mar 16 2017 Denis Medvedev <nbr@altlinux.org> 5.1.16-alt1
- Updated template for virtualbox 5.1.16

* Wed Jan 25 2017 Denis Medvedev <nbr@altlinux.org> 5.1.14-alt1
- Updated template for virtualbox 5.1.14

* Tue Nov 22 2016 Denis Medvedev <nbr@altlinux.org> 5.1.10-alt1
- Updated template for virtualbox 5.1.10

* Thu Jul 28 2016 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.1.2-alt1
- Updated template for virtualbox 5.1.2

* Wed May 11 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.0.20-alt1
- Updated template for virtualbox 5.0.20.

* Tue Feb 16 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.0.14-alt1
- Updated template for virtualbox 5.0.14.

* Thu Nov 12 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.3.30-alt3
- build with kernel 4.3 fixed

* Fri Oct  9 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.3.30-alt2
- work with kernel 4.2 fixed

* Mon Aug 31 2015 Aleksey Avdeev <solo@altlinux.org> 4.3.30-alt1
- Update template for virtualbox 4.3.30.

* Wed Jan 28 2015 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.20-alt1
- Update template for virtualbox 4.3.20.

* Wed Sep 03 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.3.14-alt1
- Update template for virtualbox 4.3.14.

* Mon Mar 18 2013 Evgeny Sinelnikov <sin@altlinux.ru> 4.2.10-alt1
- Update to new release
- Support specsubst for kflavour

* Mon Dec 17 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.2.4-alt2
- new template

* Tue Nov 27 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.2.4-alt1
- 4.2.4

* Wed Aug 29 2012 Anton Protopopov <aspsk@altlinux.org> 4.1.20-alt2
- technical

* Wed Aug 22 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.20-alt1
- Update to new release

* Sun Jul 29 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.18-alt1
- 4.1.18

* Sat Jul 28 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.18-alt1
- Update to new release

* Fri Apr 06 2012 Anton Protopopov <aspsk@altlinux.org> 4.1.12-alt2
- Technical

* Tue Apr 03 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.12-alt1
- Update to new release

* Sun Apr 01 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.10-alt1
- Update to new release with 3.2 kernel support

* Sat Jan 14 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.6-alt2
- fix to build with 3.2 kernel

* Fri Dec 02 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.6-alt1
- Update to new release

* Sun Oct 30 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.4-alt1
- Update to new release

* Wed Sep 21 2011 Anton Protopopov <aspsk@altlinux.org> 4.0.12-alt2
- Technical

* Mon Jul 25 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.12-alt1
- 4.0.12

* Sun Feb 20 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.4-alt1
- Update to new release

* Sun Feb 06 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.2-alt1
- Update to new release

* Thu Jan 06 2011 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.12-alt1
- Update to new release

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 3.2.4-alt3
- technical

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 3.2.4-alt2
- technical

* Thu Jun 10 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.4-alt1
- Update to new release

* Tue May 11 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.1.8-alt1
- Update to new release

* Sun Apr 04 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.1.6-alt1
- Update to new release

* Wed Mar 10 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.1.4-alt1
- Update to new release

* Tue Nov 03 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.10-alt1
- Updated to new release

* Wed Oct 07 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.8-alt1
- Updated to new release

* Sun Sep 20 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.6-alt1
- Updated to new release

* Tue Aug 11 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.4-alt1
- Updated to new release

* Thu Jul 23 2009 Anton Protopopov <aspsk@altlinux.org> 3.0.2-alt2
- Merge with sin@ to enforce inheritance

* Mon Jul 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.2-alt1
- Updated to new release

* Sun Jul 12 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.0-alt2
- Add vboxnetadp building

* Wed Jul 08 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.0-alt1
- Updated to new release

* Sat Jun 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.2.4-alt1
- Updated to new release

* Tue May 12 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.2.2-alt1
- Updated to new release

* Wed Feb 25 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.4-alt1
- Updated to new release

* Fri Dec 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.0-alt1
- Updated to new release
- Built new netfilter module with vboxdrv Module.symvers

* Sat Nov 08 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.0.4-alt1
- Updated to new release

* Thu Sep 04 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.6-alt1
- Updated to last release

* Sun Aug 31 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.4-alt1
- Updated to last release

* Sun Jun 08 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.2-alt1
- Updated to last release

* Fri Apr 18 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.5.6-alt2
- Added requires for common package

* Fri Mar 28 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.5.6-alt1
- Initial virtualbox modules build

