%define uname xf86-video-vmware

Name: xorg-drv-vmware
Version: 13.3.0
Release: alt2
Epoch: 1

Summary: VMware SVGA Device video driver
License: MIT/X11
Group: System/X11

Url: http://cgit.freedesktop.org/xorg/driver/xf86-video-vmware
Source: %name-%version.tar
Patch: %name-%version-%release.patch

ExclusiveArch: x86_64 %ix86

PreReq: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

BuildRequires(Pre): xorg-sdk xorg-util-macros
BuildRequires: libXext-devel xorg-proto-devel libxatracker-devel libudev-devel

%description
%summary

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--with-xorg-module-dir=%_x11modulesdir \
	--disable-static

%make_build

%install
%makeinstall_std

%files
%dir %_x11modulesdir/drivers
%_x11modulesdir/drivers/*.so
%_man4dir/*

%changelog
* Thu Jun 13 2019 Michael Shigorin <mike@altlinux.org> 1:13.3.0-alt2
- added ExclusiveArch:
- minor spec cleanup

* Thu May 31 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:13.3.0-alt1
- 13.3.0

* Mon Dec 12 2016 Valery Inozemtsev <shrek@altlinux.ru> 1:13.2.1-alt1
- 13.2.1

* Fri Nov 27 2015 Valery Inozemtsev <shrek@altlinux.ru> 1:13.1.0-alt2
- rebuild for XORG_ABI_VIDEODRV = 20.0

* Wed Feb 04 2015 Fr. Br. George <george@altlinux.ru> 1:13.1.0-alt1
- Autobuild version bump to 13.1.0

* Thu Oct 23 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:13.0.2-alt2
- Rebuilt with new Xorg.

* Mon Apr 21 2014 Fr. Br. George <george@altlinux.ru> 1:13.0.2-alt1
- Autobuild version bump to 13.0.2

* Tue Feb 04 2014 Fr. Br. George <george@altlinux.ru> 1:13.0.1-alt2
- Rebuild for XORG_ABI_VIDEODRV=15.0

* Wed Jun 05 2013 Fr. Br. George <george@altlinux.ru> 1:13.0.1-alt1
- Autobuild version bump to 13.0.1
- Remove applied patch

* Thu Mar 07 2013 Fr. Br. George <george@altlinux.ru> 1:13.0.0-alt2
- Apply upstream changes as patch
- Rebuild woth Xorg 14.0

* Tue Feb 05 2013 Fr. Br. George <george@altlinux.ru> 1:13.0.0-alt1
- Autobuild version bump to 13.0.0

* Tue Feb 05 2013 Fr. Br. George <george@altlinux.ru> 0.0.0-alt1
- Initial zero version build

