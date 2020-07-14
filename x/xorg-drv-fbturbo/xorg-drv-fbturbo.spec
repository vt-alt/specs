Name: xorg-drv-fbturbo
Version: 0.5.1
Release: alt6

Summary: ARM-optimized fbdev video driver
License: MIT/X11
Group: System/X11

ExclusiveArch: armh

Requires: XORG_ABI_VIDEODRV = %get_xorg_abi_videodrv

Source: %name-%version-%release.tar

BuildRequires(Pre): xorg-sdk xorg-util-macros
BuildRequires: xorg-scrnsaverproto-devel xorg-resourceproto-devel xorg-xf86dgaproto-devel
BuildRequires: pkgconfig(libUMP)

%description
%name is an modified Xorg fbdev driver with optimizations for ARM boards.

%prep
%setup

%build
%autoreconf
%configure --with-xorg-module-dir=%_x11modulesdir --with-drm-module=vpout-drm
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_x11modulesdir/drivers/*.so
%_man4dir/fbturbo.4*

%changelog
* Thu Jul 18 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.1-alt6
- rebuilt with xorg-server 1.20

* Wed Dec 14 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.1-alt4
- rebuilt with xorg-server 1.19

* Sun Nov 29 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.1-alt3
- rebuilt with xorg-server 1.18

* Fri Oct 24 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.1-alt2
- rebuild with xorg-server 1.16.1

* Fri Feb 07 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.1-alt1
- rebuild with xorg-server 1.15.0

* Mon Dec 16 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.1-alt1
- 0.3.1 released
- renamed to fbturbo

* Wed Jul 31 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt2
- requires XORG_ABI_VIDEODRV = 14.1

* Fri Jun 14 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt1
- initial
