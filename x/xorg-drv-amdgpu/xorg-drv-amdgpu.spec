Name: xorg-drv-amdgpu
Version: 19.1.0
Release: alt3
Summary: AMD GPU video driver for the Xorg X server
License: MIT/X11
Group: System/X11
Url: http://cgit.freedesktop.org/xorg/driver/xf86-video-amdgpu

PreReq: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv
Requires: xorg-dri-radeon

Source: %name-%version.tar
Patch: %name-%version-%release.patch

ExclusiveArch: %ix86 x86_64 aarch64 ppc64le %e2k
BuildRequires(Pre): xorg-sdk xorg-util-macros
BuildRequires: libGL-devel libgbm-devel libudev-devel xorg-proto-devel

%description
%summary

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-xorg-module-dir=%_x11modulesdir \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%dir %_x11modulesdir/drivers
%_xorgsysconfigdir/*
%_x11modulesdir/drivers/*.so
%_man4dir/*

%changelog
* Fri Apr 09 2021 Michael Shigorin <mike@altlinux.org> 19.1.0-alt3
- ExclusiveArch += %%e2k (works fine there)

* Thu Apr 08 2021 Valery Inozemtsev <shrek@altlinux.ru> 19.1.0-alt2
- cherry-pick upstream build fix for GCC 10

* Mon Oct 14 2019 Valery Inozemtsev <shrek@altlinux.ru> 19.1.0-alt1
- 19.1.0

* Wed Mar 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 19.0.1-alt1
- 19.0.1

* Wed Mar 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 19.0.0-alt1
- 19.0.0

* Mon Sep 17 2018 Valery Inozemtsev <shrek@altlinux.ru> 18.1.0-alt1
- 18.1.0

* Mon May 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 18.0.1-alt1
- 18.0.1

* Mon Oct 23 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt0.M80P.1
- backport to p8 branch

* Mon Oct 23 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Thu Mar 16 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Thu Dec 01 2016 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Thu Oct 13 2016 Fr. Br. George <george@altlinux.ru> 1.1.2-alt1
- Autobuild version bump to 1.1.2

* Mon Apr 18 2016 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Initial build for ALT

* Mon Apr 18 2016 Fr. Br. George <george@altlinux.ru> 1:1.1.0-alt1
- Autobuild version bump to 1.1.0

