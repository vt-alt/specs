Name: xorg-drv-qxl
Version: 0.1.5
Release: alt2
Epoch: 2
Summary: QEMU QXL paravirt video
License: GPL
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk
BuildRequires: spice-protocol xorg-proto-devel libXext-devel
BuildRequires: libudev-devel pkgconfig(spice-server) libXfont2-devel

%description
Driver for QEMU QXL paravirt video

%package -n xorg-drv-spiceqxl
Summary: QXL video driver
Group: System/X11

%description -n xorg-drv-spiceqxl
xorg-drv-spiceqxl is both QXL video driver and SPICE server, intended for use without QEMU

%prep
%setup -q
%patch -p1

%build
export CFLAGS="-Wno-shadow -Wno-declaration-after-statement -Wno-unused-function -Wno-return-type"
%autoreconf
%configure \
	--with-xorg-module-dir=%_x11modulesdir \
	--enable-xspice \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_x11modulesdir/drivers/qxl_drv.so

%files -n xorg-drv-spiceqxl
%_x11modulesdir/drivers/spiceqxl_drv.so

%changelog
* Tue Jun 18 2019 Valery Inozemtsev <shrek@altlinux.ru> 2:0.1.5-alt2
- 0.1.5

* Thu May 31 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:0.1.4-alt6
- requires XORG_ABI_VIDEODRV = 24.0

* Wed Nov 30 2016 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.4-alt4
- requires XORG_ABI_VIDEODRV = 23.0

* Sun Oct 02 2016 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.4-alt3
- disabled KMS composite support

* Thu Jul 14 2016 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.4-alt2
- spiceqxl module packaged

* Fri Nov 27 2015 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.4-alt1
- 0.1.4

* Thu Oct 23 2014 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.2-alt1
- 0.1.2

* Thu Jun 19 2014 Alexey Shabalin <shaba@altlinux.ru> 1:0.1.1-alt2
- fix find libdrm headers for kms support
- build with libudev

* Fri Jan 31 2014 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.1-alt1
- 0.1.1

* Wed Mar 06 2013 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.0-alt2
- requires XORG_ABI_VIDEODRV = 14.1

* Fri Jan 18 2013 Valery Inozemtsev <shrek@altlinux.ru> 1:0.1.0-alt1
- 0.1.0

* Mon Aug 27 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:0.0.17-alt2
- requires XORG_ABI_VIDEODRV = 12.1

* Sun Mar 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:0.0.17-alt1
- 0.0.17

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.0.16-alt1
- 0.0.16

* Thu Apr 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.0.13-alt2
- requires XORG_ABI_VIDEODRV = 10.0

* Fri Mar 04 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.0.13-alt1
- 0.0.13

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.0.12-alt2
- requires XORG_ABI_VIDEODRV = 8.0

* Tue Feb 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.0.12-alt1
- 0.0.12

* Mon Jan 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.0.6-alt1
- initial release

