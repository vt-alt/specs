# TODO: install 64-bit binaries

# Etersoft (c) 2006, 2007, 2008, 2009, 2010, 2013, 2015, 2016
# Multiplatform spec for autobuild system Korinf

# For build install,
# 	kernel-headers-modules-XXXX for ALT Linux
# 	kernel-devel-XXXX for FCx / ASP Linux
# 	kernel-source-stripped-XXXX for Mandriva 2007
# 	linux-headers for Debian / Ubuntu
# 	kernel-source-XXXX for SuSe
# 	kernel-source-XXXX for Slackware / MOPSLinux

Name: haspd
Version: 7.90
Release: alt2

Summary: Hardware key protection drivers and license managers

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: Proprietary
Group: System/Kernel and hardware
Url: http://www.etersoft.ru

Source: ftp://updates.etersoft.ru/pub/Etersoft/HASP/unstable/sources/tarball/%name-%version.tar

# compat needs due distr_vendor using
BuildRequires(pre): rpm-build-intro rpm-build-compat
BuildRequires: kernel-build-tools libusb-devel libncurses-devel

%define module_dir /lib/modules

# disable Fedora's build-id
%global _missing_build_ids_terminate_build 0
# due Empty %files file .../haspd-7.90/debugsourcefiles.list
%global debug_package %{nil}

# forbid future stripping
# http://bugs.etersoft.ru/show_bug.cgi?id=10819
%global __strip /bin/true

Obsoletes: aksusbd
Provides: aksusbd
Obsoletes: aksparlnx
Provides: aksparlnx
Obsoletes: winehasp
Provides: winehasp

Obsoletes: aksusbd-redhat
Provides: aksusbd-redhat
Obsoletes: aksusbd-suse
Provides: aksusbd-suse

#
#ifarch x86_64
#BuildPreReq: i586-glibc-core i586-glibc-pthread
# we need 32bit glibc in any caseOC
BuildRequires: ld-linux.so.2 libpthread.so.0
#else
Provides: sntl-sud = 7.3.0-0
#endif

# due propritary library packed
%set_verify_elf_method skip
# https://bugzilla.altlinux.org/show_bug.cgi?id=31207
# find-requires: ERROR: /usr/lib/rpm/lib.req failed
%add_findreq_skiplist /usr/lib/sentinel/*
# find-requires: ERROR: /usr/lib/rpm/lib.req failed
# ldd: ERROR: /tmp/.private/lav/haspd-buildroot/usr/sbin/aksusbd: trace failed
# ldd: exited with unknown exit code (132)
%add_findreq_skiplist /usr/sbin/aksusbd
%add_findreq_skiplist /usr/sbin/*

# disable make debuginfo (due the same ldd problem)
%define __find_debuginfo_files %nil

ExclusiveOS: Linux
%if %_vendor == "alt"
# have no idea how to build package with 32-bit binaries in the hasher
ExclusiveArch:  %ix86
%else
ExclusiveArch: %ix86 x86_64
%endif

%description
HASP - Hardware Against Software Piracy

The RPM package contains
* The required software for accessing HASP and Hardlock keys from Aladdin

  Supports parallel HASP keys, Hardlock keys, USB HASP keys.
  It contains kernel module which required when using parallel port keys and
  USB daemon which is general required to access the HASP/Hardlock key.

* The Smartkey key server for Linux (Smartkey 3 USB/LPT keys) from Eutron

* The SafeNet USB key server and license server for keys from SafeNet Sentinel

The RPM package prepared in Etersoft for WINE@Etersoft project.
Please send any comments to hasp@etersoft.ru

Copyright 1985-2008 Aladdin Knowledge Systems http://www.aladdin.com
Copyright 2006-2007 Eutron SPA http://www.smartkey.eutron.com
Copyright 2006-2006 SafeNet Sentinel http://www.safenet-inc.com
Copyright 2015-2016 SafeNet http://safenet-sentinel.ru/
Copyright 2017 Gemalto http://www.gemalto.com

%package modules
Summary: Linux kernel modules for HASP LPT keys
Summary(ru_RU.UTF-8): Модули ядра Linux для LPT-ключей HASP
Group: System/Kernel and hardware
Requires: %name >= %version

%if %_vendor == "suse"
# due kernel dependencies
AutoReq: no
%endif

%description modules
Linux kernel modules for HASP LPT keys

%prep
%setup -q
patch -p0 <etersoft/aksparpub.c.patch
patch -p0 <etersoft/aksparpub.h.patch
# Cleanup deprecated compatibility rules
%__subst '/Compatibility/,$d' aksusbd/udev/rules.d/80-hasp.rules

%build

%install
#export KBUILD_VERBOSE=1
MODULEVERSION=%version MAN_DIR=%buildroot%_mandir/ INIT_DIR=%buildroot%_initdir/ \
    SBIN_DIR=%buildroot%_sbindir/ INSTALL_MOD_PATH=%buildroot%module_dir \
    LIB_DIR=%buildroot%_libdir/ \
        etersoft/build.sh %_lib
# Install udev rules
install -m0644 -D aksusbd/udev/rules.d/80-hasp.rules %buildroot%_udevrulesdir/80-hasp.rules

%if %_vendor == "alt"
# Make symlink to /lib/libusb-1.0.so.0 for require i586-libusb in ALT Linux arepo
mkdir -p %buildroot/lib/%name
ln -s /lib/libusb-1.0.so.0 %buildroot/lib/%name/libusb-1.0.so.0
%endif

%post
%post_service %name
%start_service %name

%preun
%preun_service %name

%post modules
%post_service %name

%files
%_initdir/%name
%_initdir/haspd.outformat
%if %_vendor == "alt"
/lib/%name/libusb-1*
%endif

# Aladdin
%_sbindir/aksusbd
%_sbindir/winehasp
%_sbindir/hasplm

%_sbindir/hasplmd

#%_sbindir/haspdemo
#%_sbindir/nethaspdemo
%_sbindir/usbkeytest
%dir %_sysconfdir/haspd/
%_sysconfdir/haspd/hasplm.conf

%_udevrulesdir/80-hasp.rules

%doc winehasp/readme.txt
%doc aksparlnx/README.html aksparlnx/INSTALL hasplm/hasplm.txt
%doc doc/NETHASP.INI.example LICENSE.UTF-8.txt doc/README.UTF-8.txt
%doc smartkey-server-11.5/README.smartkey sentinel/licenseagreement.txt sentinel/sntlconfig.xml sentinel/readme.pdf

# Eutron
%_sysconfdir/skeyd.conf
%_sbindir/skeyd
%_sbindir/skeymon
#%_sbindir/smartdem-x86
#%_sbindir/smartdem-amd64

%ifarch x86_64
# TODO
%else
# Sentinel
%_libdir/sentinel/
%endif

%_man1dir/*
%_man5dir/*

%files modules
%_usrsrc/aksparlnx-%version/
#dir %module_dir/haspd/
#ghost %module_dir/haspd/aksparlnx.*
#module_dir/haspd/*.sh
#module_dir/2*

%changelog
* Thu Jul 11 2019 Vitaly Lipatov <lav@altlinux.ru> 7.90-alt2
- disable Fedora's build-id

* Fri Apr 12 2019 Vitaly Lipatov <lav@altlinux.ru> 7.90-alt1
- update binaries for Sentinel^(R) LDK and Sentinel HASP^(R) v 7.90

* Wed Nov 15 2017 Vitaly Lipatov <lav@altlinux.ru> 7.60-alt2
- add comment about usbkeytest

* Thu Jul 20 2017 Vitaly Lipatov <lav@altlinux.ru> 7.60-alt1
- update binaries for Sentinel^(R) LDK and Sentinel HASP^(R) v 7.60 (July, 2017)

* Fri Nov 25 2016 Vitaly Lipatov <lav@altlinux.ru> 7.40-alt10
- require i586-libusb in ALT Linux arepo (ALT bug 32808) (thanks, cas@)

* Fri Nov 25 2016 Andrey Cherepanov <cas@altlinux.org> 7.40-alt4.1
- require i586-libusb in ALT Linux arepo

* Tue Apr 05 2016 Konstantin Artyushkin <akv@altlinux.org> 7.40-alt9
- fix KERNELVERSION at DEPMODULEPATH

* Wed Mar 16 2016 Konstantin Artyushkin <akv@altlinux.org> 7.40-alt8
- aksparlnx/build.sh: added support for kernels > 3.15

* Tue Mar 15 2016 Konstantin Artyushkin <akv@altlinux.org> 7.40-alt7
- add support for kervel > 3.15

* Wed Feb 03 2016 Vitaly Lipatov <lav@altlinux.ru> 7.40-alt6
- skip prebuilt binary stripping again (eterbug #10819)

* Wed Feb 03 2016 Vitaly Lipatov <lav@altlinux.ru> 7.40-alt5
- skip prebuilt binary stripping (eterbug #10819)

* Fri Dec 04 2015 Vitaly Lipatov <lav@altlinux.ru> 7.40-alt4
- allow override with KERNELVERSION

* Fri Oct 23 2015 Vitaly Lipatov <lav@altlinux.ru> 7.40-alt3
- usbkeytest: fix build (thanks to Alexander R)

* Thu Oct 22 2015 Vitaly Lipatov <lav@altlinux.ru> 7.40-alt2
- fix aksparlnx source dir version

* Mon Sep 14 2015 Vitaly Lipatov <lav@altlinux.ru> 7.40-alt1
- update binaries for Sentinel^(R) LDK and Sentinel HASP^(R) v 7.40 (August, 2015)

* Tue Aug 25 2015 Vitaly Lipatov <lav@altlinux.ru> 7.32-alt1
- update binaries for Sentinel^(R) LDK and Sentinel HASP^(R) v 7.32 (April, 2015)

* Mon Aug 24 2015 Vitaly Lipatov <lav@altlinux.ru> 4.0-alt1
- update binaries for Sentinel^(R) LDK and Sentinel HASP^(R) v 2.0 (2012)
- do not pack haspdemo and nethaspdemo

* Sat Aug 22 2015 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt10
- fix udev rule replacement

* Wed Aug 19 2015 Andrey Cherepanov <cas@altlinux.org> 3.3-alt9
- Cleanup deprecated compatibility rules to prevent fail on daemon
  startup

* Tue Aug 18 2015 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt8
- haspd.init: run all service if usbkeytest is not compiled
- note about not compiled usbkeytest

* Fri Nov 29 2013 Andrey Cherepanov <cas@altlinux.org> 3.3-alt7
- Add udev rules to use 1C hasp key if plugged without haspd restart
  (see eterbug #9425)

* Thu Nov 28 2013 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt6
- build for ALT Linux Sisyphus

* Thu Feb 21 2013 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt5
- fix ExclusiveArch for i686 build

* Mon Sep 17 2012 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt4
- add mount debugfs to /sys/kernel/debug if needed (eterbug #513)
- update rules to new udev (SYSFS->ATTRS) (see eterbug #513)

* Wed Jul 25 2012 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt3
- fix install libdir

* Wed Jan 18 2012 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt2
- haspd.init: add sbin to PATH, fix dir version (3.3) (eterbug #7943)

* Fri Dec 09 2011 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt1
- fix build.sh to use for v3.x kernels
- replace the BLK with a local lock for kernels >= v2.6.39 (eterbug #7691)

* Tue Dec 06 2011 Vitaly Lipatov <lav@altlinux.ru> 3.2-alt10
- more correct fix for kernel version checking (eterbug #7813)
- buildreq 32 bit glibc in any arch
- do not pack source to tar.bz2

* Tue Dec 06 2011 Vitaly Lipatov <lav@altlinux.ru> 3.2-alt9
- haspd.init: drop out kernel version checking (eterbug #7813)
- print major and minor number for a device in /dev/bus/usb

* Tue Oct 18 2011 Vitaly Lipatov <lav@altlinux.ru> 3.2-alt8
- drop set_strip_method (unsupported on ALT)

* Fri Sep 02 2011 Vitaly Lipatov <lav@altlinux.ru> 3.2-alt7
- fix building on old kernels (eterbug #7563)

* Wed Jun 08 2011 Vitaly Lipatov <lav@altlinux.ru> 3.2-alt6
- fix build on v2.6.38 kernel (eterbug #7313)

* Wed Oct 13 2010 Vitaly Lipatov <lav@altlinux.ru> 3.2-alt5
- and rpm-build-intro buildrequires

* Wed Jun 02 2010 Vitaly Lipatov <lav@altlinux.ru> 3.2-alt3
- small fixes in status output

* Sat May 22 2010 Vitaly Lipatov <lav@altlinux.ru> 3.2-alt2
- add build requires for build on x86_64

* Tue Apr 06 2010 Vitaly Lipatov <lav@altlinux.ru> 3.2-alt1
- enable workaround for disabled CONFIG_USB_DEVICEFS (eterbug #513)
- fix init script according to LSB (eterbug #4850)

* Mon Mar 08 2010 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt1
- new build for public repo
- move repo to UTF-8

* Fri Mar 05 2010 Yuri Fil <yurifil@altlinux.org> 3.0-alt5.1
- add hasplmd for Mandriva

* Wed Nov 25 2009 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt5
- fix build with kernel 2.6.31
- build from git

* Sun Jul 26 2009 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt4
- small fixes for build

* Fri May 29 2009 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt3
- add personal libusb for usbsentinel driver

* Thu Apr 30 2009 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt2
- usbkeytest: fix build with libusb 1.0

* Sat Feb 28 2009 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt1
- update aksusbd and add hasplmd to HASP SRM 3.50
- make package build with x86_64

* Mon Nov 03 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt12.1
- fix LPT port checking, fix messages about aksparlnx kernel module

* Thu Oct 30 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt12
- add libncurses-devel requires
- do not check build and do not pack binary modules
- add /etc/haspd/hasplm.conf config file

* Fri Oct 17 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt11
- some fixes
- fix build on Ubuntu, more verbose build
- fix some bashism

* Tue Mar 25 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt10
- rename usbdaemon to usbsentinel
- add usbtestkey using for USB key detection (old libusb is supported)
- run Eutron or Sentinel drivers only if the key is detected

* Thu Feb 28 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt9
- dkms adopted, use modprobe only for module loading

* Tue Jan 22 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt8
- cleanup spec
- use start_service for initial start (it checks DURING_INSTALL)

* Mon Dec 03 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt7
- move setnethasp to wine package

* Tue Nov 13 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt6
- fix spec for Korinf build
- add setnethasp
- add support modprobe loading

* Mon Nov 05 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt5
- restore kernel 2.4 support
- disable smartkey, sentinel packing for Special
- fix install/restart issues

* Sun Jul 01 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt4
- kernel module loading order changed like in linux-cifs
- fixes for aksd module stopping
- add smartdem-x86 and smartdem-amd64 for SmartKey testing

* Mon Jun 11 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt3
- merged with aksparlnx 1.7 version
- add 'service haspd build' command for build kernel module
- small fixes in scripts
- add requires libusb for build and after install
- fix conflict with repeat build

* Sat Apr 21 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt2
- move kernel modules to standalone package

* Tue Mar 20 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- change numeration to own
- add Sentinel USB key drivers (Sentinel Key, Sentinel Dual Hardware Key, UltraPro Key, SuperPro Key)
- add Sentinel Keys Server

* Tue Mar 20 2007 Vitaly Lipatov <lav@altlinux.ru> 1.6e-alt4
- add detect for usbfs and CONFIG_USB_DEVICEFS
- restore broken binary aksusbd in repository

* Fri Mar 16 2007 Vitaly Lipatov <lav@altlinux.ru> 1.6e-alt3
- add detect appropriate kernel module

* Thu Mar 01 2007 Vitaly Lipatov <lav@altlinux.ru> 1.6e-alt2
- fix service script
- move depmod to preun section
- additional system support

* Wed Feb 21 2007 Vitaly Lipatov <lav@altlinux.ru> 1.6e-alt1
- new generation (build for all kernels)
- move all builds command to build.sh
- add SmarKey 3 keys (from Eutron)

* Mon Jan 08 2007 Vitaly Lipatov <lav@altlinux.ru> 1.6_2.6.12-alt8
- add buildroot if missed
- fix package version build
- get kernel version from current kernel if possible
- remove flavour define using

* Wed Nov 15 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6_2.6.12-alt7
- fix SMP checking in script
- fix selfconflicts (remove provides)

* Thu Sep 14 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6_2.6.16-alt6
- add patch for removed MODULE_PARM in newest kernel
  (thanks Alexandr Bondar <sasha(at)zm.kh.ua> for remind)

* Mon Jun 19 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6_2.6.16-alt5
- add NETHASP.INI example to doc
- add check for /proc/bus/usb present
- add hasptest program for hasp present checking

* Fri May 12 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6_2.6.16-alt4
- fix gcc compiler for kernel module
- disable version magic control for modules (for kernel update support)

* Wed May 03 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6_2.6.16-alt3
- update copyright
- rewrote init script, fix path to outformat
- add smp kernel support

* Mon Apr 10 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6_2.6.14-alt2
- use outformat for diagnose messages
- rebuild with new rpm-build-compat (fix chkconfig args)
- fix insmod params (-f instead --force)
- rebuild with normal post/preun macroses
- add wait for process killed during stopping
- fix already started logic

* Fri Apr 07 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6_2.6.14-alt1
- initial build for WINE@Etersoft project (based on Aladdin's builds)
- add patch against verify_area on newest kernels
- insert kernel version to package version
- fix init scripts (adopted to all Linux distro)
- add aksusbd and winehasp install
- improve spec
