%define module_name	bcmwl
%define module_version	6.30.223.248
%define module_release alt18

%define flavour		un-def
%define karch %ix86 x86_64
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-un-def

%setup_kernel_module %flavour

%define norm_version	%kversion

%define module_dir /lib/modules/%kversion-%flavour-%krelease/net

Summary: Modules for Broadcom-based WiFi .11a/b/g adapters
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: Proprietary
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: http://www.broadcom.com/support/802.11/linux_sta.php
Patch1: bcmwl-build-kernel3.15.patch
Patch2: bcmwl-build-kernel3.17.patch
Patch3: bcmwl-build-kernel3.18.patch
Patch4: bcmwl-build-kernel4.0.patch
Patch5: bcmwl-fix.patch
Patch6: bcmwl-build-4.2.patch
Patch7: bcmwl-build-kernel4.3.patch
Patch8: bcmwl-build-kernel4.7.patch
Patch9: bcmwl-build-kernel4.8.patch
Patch11: bcmwl-build-kernel4.11.patch
Patch12: bcmwl-build-kernel4.12.patch
Patch15: bcmwl-build-kernel4.15.patch
Patch51: bcmwl-build-kernel5.1.patch
Patch56: bwcmwl-arch-build-kernel5.6.patch
BuildRequires: perl sharutils
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-source-%module_name = %module_version
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
These packages contain Broadcom's IEEE 802.11a/b/g/n hybrid Linux device
driver for use with Broadcom's BCM4311-, BCM431i2-,
BCM4321-, and BCM4322-based hardware.

NOTE: You must read the LICENSE.TXT file in the lib directory before
using this software.
%prep
rm -rf kernel-source-%module_name-%module_version

tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2

%setup -D -T -n kernel-source-%module_name-%module_version
pushd bcmwl
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p2
%patch7 -p0
%patch8 -p0
%patch9 -p1
%patch11 -p1
%patch12 -p1
%patch15 -p1
%patch51 -p1
%patch56 -p1
popd

%build
cd bcmwl
mkdir lib
if [ "$(arch)" = "x86_64" ] ; then
   cp src/lib/wlc_hybrid.o_shipped_x86_64 lib/wlc_hybrid.o_shipped
else
   cp src/lib/wlc_hybrid.o_shipped_i386 lib/wlc_hybrid.o_shipped
fi
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
make -C %_usrsrc/linux-%kversion-%flavour M=`pwd` modules

%install
mkdir -p $RPM_BUILD_ROOT%module_dir/

cd bcmwl
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
make -C %_usrsrc/linux-%kversion-%flavour INSTALL_MOD_PATH=%buildroot INSTALL_MOD_DIR=net M=`pwd`  modules_install

# blacklist several modules (see ALT bugs #26265, #26250)
mkdir -p %buildroot/%_sysconfdir/modprobe.d
cat > %buildroot/%_sysconfdir/modprobe.d/blacklist-bcm.conf << __EOF__
blacklist bcm43xx
blacklist ssb
blacklist b43
__EOF__
cat > %buildroot/%_sysconfdir/modprobe.d/blacklist-bcm2.conf << __EOF__
blacklist b44
blacklist b43legacy
blacklist bcma
blacklist brcmsmac
blacklist bcma-pci-bridge
__EOF__

%files
%module_dir
%config(noreplace) %_sysconfdir/modprobe.d/blacklist-bcm.conf
%config(noreplace) %_sysconfdir/modprobe.d/blacklist-bcm2.conf

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Fri Sep 06 2019 Nikolai Kostrigin <nickel@altlinux.org> 6.30.223.248-alt17
- build with kernel 5.3 fixed
- add .gear/km-karch: prevent build for aarch64 and ppc64le

* Mon Oct  5 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.248-alt9
- build with kernel 4.2 fixed

* Mon Sep 28 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.248-alt8
- #30807 fixed

* Thu May 28 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.248-alt7
- build with kernel 4.0 fixed

* Fri Dec 12 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.248-alt6
- build with kernel 3.18 fixed

* Fri Nov 14 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.248-alt5
- blacklist split

* Tue Oct 21 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.248-alt4
- build with kernel 3.17 fixed
- increased blacklist

* Mon Sep  8 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.248-alt3
- new version

* Tue Jun 24 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.30-alt3
- add support for kernel 3.15

* Tue Feb 18 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.30-alt2
- fixed version

* Mon Feb 17 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.30-alt1
- new version

* Wed Aug  7 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.30.223.30-alt1
- new version

* Wed Jul 17 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.100.82.112-alt5
- add support for kernel 3.10

* Mon Dec 17 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.100.82.112-alt4
- new template

* Mon Jun 11 2012 Anton Protopopov <aspsk@altlinux.org> 5.100.82.112-alt3
- fix to build with kernel 3.4

* Thu Jan 12 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.100.82.112-alt2
- fix to build with kernel 3.2

* Thu Jan 12 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.100.82.112-alt1
- 5.100.82.112

* Thu Sep 15 2011 Anton Protopopov <aspsk@altlinux.org> 5.60.48.36-alt6
- Add 'conf' extension to modprobe configuration file

* Wed Sep 14 2011 Anton Protopopov <aspsk@altlinux.org> 5.60.48.36-alt5
- Blacklist several modules (ALT 26265)

* Thu Feb 17 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.60.48.36-alt4
- 2.6.35 patch extended to infinity

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 5.60.48.36-alt3
- technical

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 5.60.48.36-alt2
- technical

* Wed Nov 10 2010 Anton Protopopov <aspsk@altlinux.org> 5.60.48.36-alt1
- 5.60.48.36

* Wed Jan 13 2010 Anton Protopopov <aspsk@altlinux.org> 5.10.91.9.3-alt1
- 5.10.91.9.3

* Tue May 26 2009 Michail Yakushin <silicium@altlinux.ru> 5.10.91.9-alt1
- 5.10.91.9

* Tue Apr 21 2009 Michail Yakushin <silicium@altlinux.ru> 5.10.79.10-alt2
- Fix module position (closes: 19603)

* Wed Mar 25 2009 Michail Yakushin <silicium@altlinux.ru> 5.10.79.10-alt1
- initial build

