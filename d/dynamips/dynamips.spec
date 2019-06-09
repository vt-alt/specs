# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: dynamips
Version: 0.2.20
Release: alt1

Summary: Cisco 7200 Simulator
License: GPLv2
Group: Emulators

Url: https://github.com/GNS3/dynamips
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake cmake 
BuildRequires: libelf-devel libpcap-devel libuuid-devel

%description
A project to emulate a Cisco 7200 on a traditionnal PC.
The emulator currently supports the following platforms:
 - Cisco 7200 (NPE-100 to NPE-400)
 - Cisco 3600 (3620, 3640 and 3660)
 - Cisco 2691
 - Cisco 3725
 - Cisco 3745
 - Cisco 2600 (2610 to 2650XM)
 - Cisco 1700 (1710 to 1760)

The goals of this emulator are mainly:
    * To be used as a training platform, with software used in real world. It
      would allow people to become more familiar with Cisco devices, Cisco
      being the world leader in networking technologies ;
    * Test and experiment the numerous and powerful features of Cisco IOS ;
    * Check quickly configurations to be deployed later on real routers.

%prep
%setup
%ifarch %e2k
sed -i 's,(__ia64__),& || defined (__e2k__),' common/dynamips_common.h
%endif

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
install -d %buildroot%_localstatedir/%name/{labs,images}
rm -fR %buildroot%_docdir/%name

%files
%doc COPYING README* TODO ChangeLog RELEASE-NOTES
%_man1dir/*
%_man7dir/hypervisor_mode.7*
%_bindir/*
%dir %_localstatedir/%name
%dir %_localstatedir/%name/images
%dir %_localstatedir/%name/labs

%changelog
* Sun Jun 09 2019 Anton Midyukov <antohami@altlinux.org> 0.2.20-alt1
- new version 0.2.20

* Wed Jun 05 2019 Michael Shigorin <mike@altlinux.org> 0.2.18-alt2
- E2K: initial architecture support

* Fri Jul 06 2018 Anton Midyukov <antohami@altlinux.org> 0.2.18-alt1.1
- rebuilt for aarch64

* Wed Apr 11 2018 Anton Midyukov <antohami@altlinux.org> 0.2.18-alt1
- new version 0.2.18

* Wed Jan 24 2018 Anton Midyukov <antohami@altlinux.org> 0.2.17-alt1
- 0.2.17

* Sun Aug 07 2016 Anton Midyukov <antohami@altlinux.org> 0.2.16-alt1
- 0.2.16

* Sun Dec 01 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2.10-alt1
- 0.2.10

* Sun Sep 23 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2.8-alt2RC3
- 0.2.8-RC3-community
- Update patch and spec

* Sat Mar 22 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.2.8-alt1rc2
- 0.2.8-RC2
- add hypervisor_mode man page

* Thu Jul 05 2007 Michael Shigorin <mike@altlinux.org> 0.2.7-alt1
- initial build for ALT Linux Sisyphus (spec based on 
  PLD 0.2.5-0.1 rev 1.5 and Mandriva Contribs 0.2.7-1mdv2008.0)
- use mdv makefile patch

