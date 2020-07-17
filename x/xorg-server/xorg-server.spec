%define mesaversion 19.0
%define xorgversion 7.7.0

%define _libexecdir /usr/libexec
%define _modulesdir %_libdir/X11/modules
%define _fontsdir %_datadir/fonts
%define _deffontdir catalogue:%_sysconfdir/X11/fontpath.d

%def_enable glamor
%def_enable xwayland

%def_enable dmx
%def_enable xnest
%def_enable ipv6

%def_enable xephyr
%if_enabled xephyr
%def_enable kdrive
%else
%def_disable kdrive
%endif

%def_enable systemd

Name: xorg-server
Version: 1.20.8
Release: alt3
Epoch: 2
License: MIT/X11
Summary: Xserver - X Window System display server
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

# grep ABI_ hw/xfree86/common/xf86Module.h
Provides: XORG_ABI_VIDEODRV = 24.1
Provides: XORG_ABI_XINPUT = 24.1
Provides: XORG_ABI_EXTENSION = 10.0
Provides: xorg-x11-server = %epoch:%version-%release xorg-extensions-glx = %epoch:%version-%release
%if_enabled glamor
Provides: xorg-glamor = %epoch:%version-%release
Obsoletes: xorg-glamor < %epoch:%version-%release
%endif
PreReq: xorg-server-control >= 1.3-alt1 %name-common = %epoch:%version-%release xorg-dri-swrast >= %mesaversion
Requires: xset iceauth xdpyinfo xorg-drv-fbdev xorg-drv-evdev
%ifarch %ix86 x86_64
Requires: xorg-drv-vesa
%endif
Provides: xorg-drv-modesetting = %epoch:%version-%release
Obsoletes: xorg-drv-modesetting < %epoch:%version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: doxygen flex libGL-devel libXau-devel libXaw-devel libXdmcp-devel libXext-devel libXfixes-devel libXfont-devel libXmu-devel
BuildRequires: libXi-devel libXpm-devel libXrender-devel libXres-devel libXtst-devel libXv-devel libdmx-devel libudev-devel libSM-devel
BuildRequires: libpciaccess-devel libpixman-devel libssl-devel libxkbfile-devel xorg-proto-devel xorg-font-utils xorg-xtrans-devel xkbcomp
BuildRequires: xorg-util-macros libselinux-devel libaudit-devel xmlto xorg-sgml-doctools libxshmfence-devel libdrm-devel libXfont2-devel
%if_enabled glamor
BuildRequires: libEGL-devel libgbm-devel libepoxy-devel
%endif
%if_enabled xwayland
BuildRequires: libwayland-client-devel wayland-protocols
%endif
%if_enabled xephyr
BuildRequires: libxcbutil-devel libxcbutil-image-devel libxcbutil-icccm-devel libxcbutil-keysyms-devel libxcb-render-util-devel
%endif
%{?_enable_systemd:BuildRequires: libdbus-devel libudev-devel}

%description
X  is  the  generic name for the X Window System display server.  It is
frequently a link or a copy of the appropriate server binary for  driving
the most frequently used server on a given machine.

%package common
Summary: The X server common files
Group: System/X11
PreReq: startup >= 0.9.2-alt1
Requires: xorg-rgb xauth fonts-bitmap-misc >= 7.0.0-alt2
Requires: xkbcomp xkeyboard-config
Obsoletes: libXiconfig

%description common
%name-common is common files for X.Org

%package -n xorg-xvfb
Summary: A virtual framebuffer X Windows System server for X.Org
Group: System/X11
Requires: %name-common = %epoch:%version-%release xorg-dri-swrast >= %mesaversion
Provides: xorg-x11-xvfb = %epoch:%version-%release

%description -n xorg-xvfb
Xvfb (X Virtual Frame Buffer) is an X Windows System server
that is capable of running on machines with no display hardware and no
physical input devices.  Xvfb emulates a dumb framebuffer using virtual
memory.  Xvfb doesn't open any devices, but behaves otherwise as an X
display.  Xvfb is normally used for testing servers.  Using Xvfb, the mfb
or cfb code for any depth can be exercised without using real hardware
that supports the desired depths.  Xvfb has also been used to test X
clients against unusual depths and screen configurations, to do batch
processing with Xvfb as a background rendering engine, to do load testing,
to help with porting an X server to a new platform, and to provide an
unobtrusive way of running applications which really don't need an X
server but insist on having one.

If you need to test your X server or your X clients, you may want to
install Xvfb for that purpose.

%package -n xorg-xnest
Summary: A nested X.Org server
Group: System/X11
Requires: %name-common = %epoch:%version-%release xorg-dri-swrast >= %mesaversion
Provides: xorg-x11-xnest = %epoch:%version-%release

%description -n xorg-xnest
Xnest is an X Window System server which runs in an X window.
Xnest is a 'nested' window server, actually a client of the
real X server, which manages windows and graphics requests
for Xnest, while Xnest manages the windows and graphics
requests for its own clients.

You will need to install Xnest if you require an X server which
will run as a client of your real X server (perhaps for
testing purposes).

%package -n xorg-xephyr
Summary: A kdrive-based X server
Group: System/X11
Requires: %name = %epoch:%version-%release

%description -n xorg-xephyr
Xephyr is a kdrive based X Server which targets a window on
a host X Server as its framebuffer. Unlike Xnest it supports
modern X extensions (even if host server doesn't) such as Composite,
Damage, randr etc.

It uses SHM Images and shadow framebuffer updates to provide
good performance.
It also has a visual debugging mode for observing screen updates.

%package -n xorg-xdmx
Summary: Multi-head X server
Group: System/X11
Requires: %name = %epoch:%version-%release

%description -n xorg-xdmx
Xdmx  is  a proxy X server that uses one or more other X servers as its
display devices.  It provides multi-head X functionality  for  displays
that  might  be  located  on  different  machines.  Xdmx functions as a
front-end X server that acts as a proxy to a set of back-end X servers.
All  of  the  visible  rendering  is  passed to the back-end X servers.
Clients connect to the Xdmx front-end, and  everything  appears  as  it
would  in  a  regular multi-head configuration.  If Xinerama is enabled
(e.g., with +xinerama on the command line), the clients  see  a  single
large screen.

Xdmx communicates to the back-end X servers using the standard X11 pro-
tocol, and standard and/or commonly available X server extensions.

%package -n xorg-xwayland
Summary: Wayland X server
Group: System/X11
Requires: %name = %epoch:%version-%release

%description -n xorg-xwayland
Xwayland is an X server for running X clients under Wayland

%package -n xorg-sdk
Summary: SDK for X server driver module development
Group: Development/C
Requires: xorg-util-macros xorg-dri3proto-devel xorg-presentproto-devel
%if_enabled glamor
Provides: xorg-glamor-devel = %epoch:%version-%release
Obsoletes: xorg-glamor-devel < %epoch:%version-%release
%endif

%description -n xorg-sdk
The SDK package provides the developmental files which are necessary for
developing X server driver modules, and for compiling driver modules
outside of the standard X11 source code tree.  Developers writing video
drivers, input drivers, or other X modules should install this package.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-os-name="%(cat %_sysconfdir/altlinux-release)" \
	--with-os-vendor="%(uname -m)" \
	--with-builder-addr="%packager" \
	--with-serverconfig-path=%_datadir/X11 \
	--with-module-dir=%_modulesdir \
	--with-log-dir=%_logdir \
	--with-xkb-path=%_datadir/X11/xkb \
	--with-xkb-output=%_localstatedir/xkb \
	--with-default-font-path=%_deffontdir \
	--with-shared-memory-dir=/dev/shm \
%ifarch %ix86 x86_64
	--with-int10=x86emu \
%endif
	--enable-xcsecurity \
	--enable-xselinux \
	--enable-config-udev \
	--disable-config-hal \
	--disable-linux-apm \
	--disable-linux-acpi \
	--enable-record \
	%{subst_enable xwayland} \
	%{subst_enable glamor} \
	%{subst_enable dmx} \
	%{subst_enable xnest} \
	%{subst_enable xephyr} \
	%{subst_enable kdrive} \
	%{subst_enable ipv6} \
	--enable-docs \
	--disable-static \
	%{?_enable_systemd:--enable-systemd-logind}
%make_build

%install
%make DESTDIR=%buildroot install

find %buildroot%_modulesdir -name \*.la -delete

mkdir -p %buildroot%_modulesdir/{drivers,input}
mkdir -p %buildroot%_datadir/X11
mkdir -p %buildroot%_sysconfdir/X11/{app-defaults,xorg.conf.d}

touch %buildroot%_sysconfdir/X11/xorg.conf

install -pD -m644 xserver.pamd %buildroot%_sysconfdir/pam.d/xserver
mkdir -p %buildroot%_sysconfdir/security/console.apps
touch %buildroot%_sysconfdir/security/console.apps/xserver

# rpm macros
install -pD -m644 xorg-sdk.rpmmacros %buildroot%_rpmmacrosdir/xorg-sdk

%pre
%_sbindir/groupadd -r -f xgrp
%pre_control xorg-server

%post
%post_control xorg-server

%files
%config(noreplace) %_sysconfdir/pam.d/xserver
%config(missingok noreplace) %_sysconfdir/security/console.apps/xserver
%ghost %_sysconfdir/X11/xorg.conf
%_bindir/X
%attr(0700,root,root) %_bindir/Xorg
%_bindir/gtf
%_bindir/cvt
%dir %_modulesdir/drivers
%dir %_modulesdir/input
%dir %_modulesdir/extensions
%_modulesdir/extensions/libglx.so
%_modulesdir/*.so
%_man1dir/Xorg.1*
%_man1dir/gtf.1*
%_man1dir/cvt.1*
%_man1dir/Xserver.1*
%_man4dir/fbdevhw.4*
%_man4dir/exa.4*
%_man5dir/xorg.conf.5*
%_man5dir/xorg.conf.d.5*
%_modulesdir/drivers/modesetting_drv.so
%_man4dir/modesetting.4*

%files common
%dir %_sysconfdir/X11/app-defaults
%dir %_sysconfdir/X11/xorg.conf.d
%dir %_libdir/X11
%dir %_datadir/X11
%_datadir/X11/xorg.conf.d
%_datadir/X11/protocol.txt
%dir %_modulesdir
%_localstatedir/xkb

%files -n xorg-xvfb
%_bindir/Xvfb
%_man1dir/Xvfb.1*

%if_enabled xnest
%files -n xorg-xnest
%_bindir/Xnest
%_man1dir/Xnest.1*
%endif

%if_enabled xephyr
%files -n xorg-xephyr
%_bindir/Xephyr
%_man1dir/Xephyr.1*
%endif

%if_enabled dmx
%files -n xorg-xdmx
%_bindir/*dmx*
%_man1dir/*dmx*.1*
%endif

%if_enabled xwayland
%files -n xorg-xwayland
%_bindir/Xwayland
%endif

%files -n xorg-sdk
%_includedir/xorg
%_pkgconfigdir/*.pc
%_datadir/aclocal/*.m4
%_rpmmacrosdir/xorg-sdk

%changelog
* Wed Jul 15 2020 Sergey V Turchin <zerg@altlinux.org> 2:1.20.8-alt3
- autobind GPUs to the screen

* Tue May 05 2020 Yuri N. Sedunov <aris@altlinux.org> 2:1.20.8-alt2
- enabled systemd-logind integration

* Mon Mar 30 2020 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.8-alt1
- 1.20.8

* Thu Feb 20 2020 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.7-alt2
- fixed provides XORG_ABI_VIDEODRV

* Tue Jan 14 2020 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.7-alt1
- 1.20.7

* Mon Nov 25 2019 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.6-alt1
- 1.20.6

* Wed Oct 30 2019 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.5-alt3
- lower gl version to work with libglvnd

* Mon Sep 09 2019 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.5-alt2
- use intel ddx only on pre-gen4 hw, newer ones will fall back to modesetting

* Mon Jun 03 2019 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.5-alt1
- 1.20.5

* Fri Apr 12 2019 Sergey V Turchin <zerg@altlinux.org> 2:1.20.4-alt2
- use smallest monitor size to compute DPI

* Wed Feb 27 2019 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.4-alt1
- 1.20.4

* Fri Oct 26 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.3-alt1
- 1.20.3

* Tue Oct 16 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.2-alt1
- 1.20.2

* Wed Oct 10 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.1-alt1
- 1.20.1
- removed OpenGL libs switcher

* Wed Sep 05 2018 Grigory Ustinov <grenka@altlinux.org> 2:1.20.0-alt2.1
- NMU: rebuilt with current openssl.

* Thu Jun 14 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.0-alt2
- exa: Use PictureMatchFormat for source-only picture format description (closes: #34975)

* Wed May 30 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.0-alt1
- 1.20.0

* Tue May 29 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.19.6-alt3
- update build dependensies

* Tue May 29 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.19.6-alt2
- rebuild

* Thu Dec 21 2017 Valery Inozemtsev <shrek@altlinux.ru> 2:1.19.6-alt1
- 1.19.6

* Wed Nov 29 2017 Sergey V Turchin <zerg@altlinux.org> 2:1.19.5-alt2
- allow to disable OpenGL libs switcher via command line option

* Mon Oct 16 2017 Valery Inozemtsev <shrek@altlinux.ru> 2:1.19.5-alt1
- 1.19.5

* Fri Oct 06 2017 Valery Inozemtsev <shrek@altlinux.ru> 2:1.19.4-alt1
- 1.19.4

* Tue Jun 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 2:1.19.3-alt4
- use intel ddx only on pre-gen4 hw, newer ones will fall back to modesetting (closes: #33242)

* Thu Jun 01 2017 Valery Inozemtsev <shrek@altlinux.ru> 2:1.19.3-alt3
- use va_gl as vdpau_driver for Intel i965 GPUS (closes: #33517)

* Tue May 30 2017 Valery Inozemtsev <shrek@altlinux.ru> 2:1.19.3-alt2
- don't force 96dpi

* Thu Mar 16 2017 Valery Inozemtsev <shrek@altlinux.ru> 2:1.19.3-alt1
- 1.19.3

* Thu Jan 12 2017 Valery Inozemtsev <shrek@altlinux.ru> 2:1.19.1-alt1
- 1.19.1

* Thu Dec 15 2016 Valery Inozemtsev <shrek@altlinux.ru> 2:1.19.0-alt2
- git snapshot server-1.19-branch.d6da208

* Wed Nov 30 2016 Valery Inozemtsev <shrek@altlinux.ru> 2:1.19.0-alt1
- 1.19.0

* Tue Sep 27 2016 Valery Inozemtsev <shrek@altlinux.ru> 2:1.18.4-alt1.M80P.1
- backport to p8 branch

* Tue Sep 27 2016 Valery Inozemtsev <shrek@altlinux.ru> 2:1.18.4-alt2
- nvidia added to the list of drivers (closes: #24632)

* Tue Jul 19 2016 Valery Inozemtsev <shrek@altlinux.ru> 2:1.18.4-alt1
- 1.18.4

* Fri Apr 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 2:1.18.3-alt1
- 1.18.3

* Sat Mar 19 2016 Valery Inozemtsev <shrek@altlinux.ru> 2:1.18.2-alt1
- 1.18.2

* Tue Feb 09 2016 Valery Inozemtsev <shrek@altlinux.ru> 2:1.18.1-alt1
- 1.18.1

* Mon Nov 23 2015 Valery Inozemtsev <shrek@altlinux.ru> 2:1.18.0-alt1
- 1.18.0

* Mon Oct 26 2015 Valery Inozemtsev <shrek@altlinux.ru> 2:1.17.3-alt1
- 1.17.3

* Mon Oct 05 2015 Valery Inozemtsev <shrek@altlinux.ru> 2:1.17.2-alt1
- 1.17.2

* Mon Feb 16 2015 Valery Inozemtsev <shrek@altlinux.ru> 2:1.17.1-alt1
- 1.17.1

* Wed Feb 11 2015 Valery Inozemtsev <shrek@altlinux.ru> 2:1.16.4-alt1
- 1.16.4

* Wed Dec 10 2014 Valery Inozemtsev <shrek@altlinux.ru> 2:1.16.2.901-alt1
- 1.16.3 RC1

* Mon Nov 10 2014 Valery Inozemtsev <shrek@altlinux.ru> 2:1.16.2-alt1
- 1.16.2

* Sun Nov 02 2014 Valery Inozemtsev <shrek@altlinux.ru> 2:1.16.1.901-alt1
- 1.16.2 RC1

* Mon Sep 29 2014 Valery Inozemtsev <shrek@altlinux.ru> 2:1.16.1-alt1
- 1.16.1

* Tue Sep 16 2014 Valery Inozemtsev <shrek@altlinux.ru> 2:1.16.0.901-alt1
- 1.16.1 RC1

* Fri Jul 18 2014 Valery Inozemtsev <shrek@altlinux.ru> 2:1.16.0-alt1
- 1.16.0

* Fri Jun 27 2014 Valery Inozemtsev <shrek@altlinux.ru> 2:1.15.2-alt1
- 1.15.2

* Tue Jun 10 2014 Valery Inozemtsev <shrek@altlinux.ru> 2:1.15.1-alt2
- Report DRI3, Present as a built-in module

* Mon Apr 14 2014 Valery Inozemtsev <shrek@altlinux.ru> 2:1.15.1-alt1
- 1.15.1

* Sat Mar 22 2014 Valery Inozemtsev <shrek@altlinux.ru> 2:1.15.0.901-alt1
- 1.15.1 RC1

* Fri Jan 31 2014 Valery Inozemtsev <shrek@altlinux.ru> 2:1.15.0-alt2
- reenabled xephyr

* Thu Jan 30 2014 Valery Inozemtsev <shrek@altlinux.ru> 2:1.15.0-alt1
- 1.15.0

* Thu Jan 30 2014 Dmitry V. Levin <ldv@altlinux.org> 2:1.14.5-alt3
- NMU.
- Reverted to 1.14.5-alt1 due to regressions (closes: #29354, #29747).

* Tue Dec 24 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.14.5-alt2
- added patches to censored screenshots for selinux

* Fri Dec 13 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.14.5-alt1
- 1.14.5

* Sun Nov 24 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.14.4.901-alt1
- 1.14.5 RC1

* Fri Nov 01 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.14.4-alt1
- 1.14.4

* Wed Oct 30 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.14.3.901-alt1
- 1.14.4 RC1

* Fri Sep 13 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.14.3-alt1
- 1.14.3

* Fri Aug 23 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.14.2.902-alt1
- 1.14.3 RC2

* Fri Jul 26 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.14.2.901-alt1
- 1.14.3 RC1

* Wed Jun 26 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.14.2-alt1
- 1.14.2

* Sat Jun 15 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.14.1.902-alt1
- 1.14.2 RC2

* Fri May 31 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.14.1.901-alt1
- 1.14.2 RC1

* Thu May 02 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.14.1-alt2
- fixed uninitialized variable in glxdri.c (closes #28782)

* Wed Apr 17 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.14.1-alt1
- 1.14.1

* Wed Apr 10 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.14.0-alt2
- rebuild with enabled abstract socket

* Wed Mar 06 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.14.0-alt1
- 1.14.0

* Fri Mar 01 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.13.2.902-alt1
- 1.13.3 RC2

* Sat Feb 16 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.13.2.901-alt1
- 1.13.3 RC1

* Fri Jan 25 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.13.2-alt1
- 1.13.2

* Fri Jan 18 2013 Valery Inozemtsev <shrek@altlinux.ru> 2:1.13.1.901-alt1
- 1.13.2 RC1
- switch libEGL & libGLESv2 (closes: #27875)

* Wed Oct 03 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.12.4-alt2
- added modesetting driver to fallback list (closes: #27773)

* Mon Aug 27 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.12.4-alt1
- 1.12.4

* Mon Aug 20 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.12.3.902-alt1
- 1.12.4 RC2

* Sun Aug 05 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.12.3.901-alt1
- 1.12.4 RC1

* Mon Jul 09 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.12.3-alt1
- 1.12.3

* Mon Jul 02 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.12.2.902-alt1
- 1.12.3 RC2

* Fri Jun 15 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.12.2.901-alt1
- 1.12.3 RC1

* Wed May 30 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.12.2-alt1
- 1.12.2

* Mon May 21 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.12.1.902-alt1
- 1.12.2 RC2

* Tue May 08 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.12.1.901-alt1
- 1.12.2 RC1

* Sat Apr 14 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.12.1-alt1
- 1.12.1

* Tue Apr 10 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.12.0.902-alt1
- 1.12.1 RC2

* Sun Apr 01 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.12.0.901-alt1
- 1.12.1 RC1

* Mon Mar 05 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.12.0-alt1
- 1.12.0

* Sat Jan 28 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.11.4-alt1
- 1.11.4

* Mon Jan 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.11.3.902-alt1
- 1.11.4 RC2

* Sat Jan 07 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:1.11.3.901-alt1
- 1.11.4 RC1

* Sun Dec 18 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.11.3-alt1
- 1.11.3

* Mon Dec 12 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.11.2.902-alt1
- 1.11.3 RC2

* Mon Nov 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.11.2.901-alt1
- 1.11.3 RC1

* Sat Nov 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.11.2-alt1
- 1.11.2

* Sat Oct 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.11.1.902-alt1
- 1.11.2 RC2

* Mon Oct 17 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.11.1.901-alt1
- 1.11.2 RC1

* Tue Sep 27 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.11.1-alt1
- 1.11.1

* Thu Sep 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.11.0-alt2
- rename wfbTriangles and wfbTrapezoids

* Mon Aug 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.11.0-alt1
- 1.11.0

* Fri Aug 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.10.4-alt1
- 1.10.4

* Sun Aug 14 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.10.3.902-alt1
- 1.10.4 RC2

* Fri Jul 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.10.3.901-alt1
- 1.10.4 RC1

* Sat Jul 09 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.10.3-alt1
- 1.10.3

* Sat Jul 02 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.10.2.902-alt1
- 1.10.3 RC2

* Fri Jun 17 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.10.2.901-alt1
- 1.10.3 RC1

* Thu Jun 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.10.2-alt2
- enabled ipv6

* Sun May 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.10.2-alt1
- 1.10.2

* Sat May 21 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.10.1.902-alt1
- 1.10.2 RC2

* Sun May 15 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.10.1.901-alt1
- 1.10.2 RC1

* Thu May 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.10.1-alt2
- update to server-1.10-branch git.c52a93c

* Thu Apr 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.10.1-alt1
- 1.10.1
- enabled record extension (closes: #25515)

* Mon Apr 04 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.5-alt2
- updated to server-1.9-branch git.9095585

* Fri Mar 18 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.5-alt1
- 1.9.5 release

* Mon Mar 07 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.4.901-alt1
- 1.9.5 RC1

* Tue Mar 01 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.4-alt2
- updated to server-1.9-branch git.7b3b7ef

* Fri Feb 04 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.4-alt1
- 1.9.4 release

* Mon Jan 31 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.3.902-alt1
- 1.9.4 RC2

* Wed Jan 12 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.3.901-alt2
- build with gcc 4.3

* Sun Jan 09 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.3.901-alt1
- 1.9.4 RC1

* Wed Dec 29 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.3-alt2
- updated to server-1.9-branch git.295a893

* Tue Dec 14 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.3-alt1
- 1.9.3 release

* Sat Dec 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.2.902-alt1
- 1.9.3 RC2

* Fri Dec 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.2.901-alt3
- updated to server-1.9-branch git.806790b

* Wed Nov 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.2.901-alt2
- updated to server-1.9-branch git.2da9b72
- autoconf: added "nvidia" for NVIDIA GPUs (closes: #24632)

* Sun Nov 14 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.2.901-alt1
- 1.9.3 RC1

* Sun Nov 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.2-alt2
sdk: readded xorg-util-macros requires

* Mon Nov 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.2-alt1
- 1.9.2

* Sun Oct 31 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.1-alt2
- updated build dependencies

* Sun Oct 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.1-alt1
- 1.9.1 release

* Fri Oct 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.0.902-alt1
- 1.9.1 RC2

* Mon Oct 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.0.901-alt1
- 1.9.1 RC1

* Mon Aug 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.0-alt3
- fixed check SELinux mode on system

* Sat Aug 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.0-alt2
- enabled SELinux support

* Sat Aug 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.9.0-alt1
- 1.9.0 release

* Fri Aug 13 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.8.99.906-alt1
- 1.9.0 RC6

* Wed Jun 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.8.99.901-alt1
- 1.9.0 RC1

* Wed Jun 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.8.1.901-alt1
- 1.8.2 RC1

* Tue May 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.8.1-alt1
- 1.8.1

* Tue May 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.8.0.902-alt1
- 1.8.1 RC2

* Tue Apr 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.8.0.901-alt1
- 1.8.1 RC1

* Sat Apr 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.8.0-alt4
- rpmmacros: added %%get_xorg_abi_extension, %%_xorgmoduledir, %%_xorgsysconfigdir
- added provides XORG_ABI_EXTENSION = 3.0

* Thu Apr 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.8.0-alt3
- xfree86: Search for a system xorg.conf.d

* Mon Apr 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.8.0-alt2
- rebuild with fresh libpciaccess

* Fri Apr 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.8.0-alt1
- 1.8.0 release

* Mon Mar 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.7.99.902-alt1
- 1.8 RC2

* Sat Jan 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.7.4-alt1
- 1.7.4

* Thu Dec 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.7.3-alt1
- 1.7.3

* Fri Nov 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.7.2-alt1
- 1.7.2 release

* Sun Nov 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.7.1.902-alt1
- 1.7.2 RC2

* Fri Nov 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.7.1.901-alt1
- 1.7.2 RC1

* Wed Nov 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.7.1-alt2
- removed provides/obsoletes libxorgconfig

* Fri Oct 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.7.1-alt1
- 1.7.1 release

* Mon Oct 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.7.0.902-alt1
- 1.7.1 RC2

* Mon Oct 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.7.0.901-alt1
- 1.7.1 RC1

* Tue Oct 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.7.0-alt1
- 1.7.0

* Fri Oct 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.4-alt2
- Re-fix DGA removal

* Mon Sep 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.4-alt1
- 1.6.4 release

* Fri Sep 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.3.901-alt2
- Don't reset the lastDeviceEventTime when doing DPMS actions.
  This patch fixes gnome-power-manager and xfce-power-manager.

* Wed Aug 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.3.901-alt1
- 1.6.4 RC1

* Sat Aug 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.3-alt1
- 1.6.3

* Mon Jul 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.3-alt0.rc1
- 1.6.3 RC1

* Mon Jul 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.2-alt4
- xdmcp: Don't crash on X -query with more than 255 IP addresses

* Wed Jul 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.2-alt3
- 1.6.2 release

* Fri Jul 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.2-alt2.rc2
- dri: disabled DRI_TEX_BUFFER version 2 (closes: #20649 #20650 #20653)

* Tue Jun 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.2-alt1.rc2
- 1.6.2 RC2

* Fri May 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.2-alt1.rc1
- 1.6.2 RC1

* Fri Apr 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.1-alt3
- merged xorg-x11-server-1.5 branch

* Fri Apr 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.1-alt2
- security:
  + Grant untrusted windows remove access on all windows
  + Fix a crash caused by wrong ordering of format arguments
  + Revert behavior of extension access for compatibility

* Wed Apr 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.1-alt1
- 1.6.1

* Tue Apr 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.0-alt5
- Xext: set POINTER_SCREEN flag in XTestFakeInput if necessary

* Mon Apr 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.0-alt4
- fixed DRI2 memory leak
- correct access mode in call to dixLookupWindow() within RRSelectInput

* Sat Mar 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.0-alt3
- don't crash on key repeats in xinerama setups (close #19308)

* Tue Mar 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.0-alt2
- randr: fixed a thinko in output setup when only one head is attached

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.6.0-alt1
- 1.6.0

* Fri Feb 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.3-alt14
- xdrvswitch: added dri symlink
 
* Wed Feb 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.3-alt12.M50.1
- build for branch 5.0

* Mon Jan 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.3-alt13
- xdrvswitch: fixed created symlinks if start X server from user

* Sun Jan 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.3-alt12
- enabled Security extension

* Sat Jan 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.3-alt11
- xdrvswitch: used internal function

* Sat Jan 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.3-alt10
- Xorg: fixed segfault (close #18406)

* Wed Dec 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.3-alt9
- integrated x11setupdrv to X server

* Thu Dec 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.3-alt8
- xkb: removed soft repeat
- server-1.5-branch 2008-12-16

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.3-alt7
- autorepeat: delay = 350, rate = 34

* Mon Dec 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.3-alt6
- rebuild with libXi-1.1.4

* Thu Nov 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.3-alt5
- updated build dependencies

* Tue Nov 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.3-alt4
- updated build dependencies

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.3-alt3
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Nov 12 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.3-alt2
- config: don't removed keyboard if use driver kbd

* Thu Nov 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.3-alt1
- 1.5.3

* Tue Oct 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.2-alt3
- EDID: Catch even more cases of encoding aspect as size
- mieq: Backtrace when the queue overflows
- dri: don't set the dixPrivate key to NULL, as this is a staticly set variable

* Mon Oct 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.2-alt2
- config: don't add duplicate devices through HAL

* Sat Oct 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.2-alt1
- 1.5.2

* Thu Oct 09 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.1-alt3
- server-1.5-branch 2008-10-08

* Fri Sep 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.1-alt2
- disabled abstract socket support

* Tue Sep 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.1-alt1
- 1.5.1

* Thu Sep 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.0-alt6
- exa: disabled shared pixmaps
- XAA: enabled offscreen pixmaps by default
- libglx.so: fixed undefined symbols

* Sun Sep 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.0-alt5
- fixed create symlink to libGL.so.1 for x86_64 (close #17127)

* Fri Sep 12 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.0-alt4
- enabled AIGLX by default

* Tue Sep 09 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.0-alt3
- added requires xorg-dri-swrast for xorg-xnest, xorg-xvfb

* Fri Sep 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.0-alt2
- join xorg-server and xorg-extensions-glx

* Thu Sep 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.5.0-alt1
- Xorg-7.4.0 release

* Fri Aug 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.99.906-alt3
- disabled dri2, xtrap

* Fri Aug 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.99.906-alt2
- update libGL.so.1 and libglx.so links for both architectures (close #16195 #16227)

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.99.906-alt1
- 1.5 RC6

* Fri Aug 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.2-alt7
- server-1.4-branch 2008-07-29

* Mon Jun 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.2-alt6
- 10-x11-input.fdi: drop XkbRules & XkbModel, requires hal > 0.5.11-alt8

* Sat Jun 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.2-alt5
- cleanup 10-x11-input.fdi, requires hal >= 0.5.11-alt8

* Sat Jun 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.2-alt4
- build with hal, input-hotplug disable by default

* Fri Jun 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.2-alt3
- AllowEmptyInput, AllowMouseOpenFail, NoPM enable by defaults

* Mon Jun 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.2-alt2
- Mesa-7.0.4

* Wed Jun 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.2-alt1
- Xorg-7.3.2

* Tue Jun 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.1-alt2
- Xorg-7.3.1

* Mon Jun 09 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt23
- renamed xorg-x11-* to xorg-*
- CVE-2008-1377 - RECORD and Security extensions memory corruption
- CVE-2008-1379 - MIT-SHM arbitrary memory read
- CVE-2008-2360 - RENDER Extension heap buffer overflow
- CVE-2008-2361 - RENDER Extension crash
- CVE-2008-2362 - RENDER Extension memory corruption

* Mon Jun 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt21
- added rpm macros in xorg-x11-sdk:
  + %get_xorg_abi_videodrv return XORG_ABI_VIDEODRV
  + %get_xorg_abi_xinput return XORG_ABI_XINPUT
- added provides XORG_ABI_VIDEODRV = 2.0, XORG_ABI_XINPUT = 2.0

* Tue May 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt20
- server-1.4-branch 2008-05-17

* Thu May 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt19
- server-1.4-branch 2008-05-07

* Wed May 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt18
- enabled Composite extension by defaults
- load glx and dri modules by defaults
- AutoConfig: disable vga
- AutoConfig: add geode

* Thu Apr 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt17
- Xext: fixed memory corruption in ProcXResQueryClients()
- X86EMU: fixing X for GeodeLX (close #15300)

* Sat Apr 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt16
- Mesa-7.0.3 release
- fixed key gets stuck (close #13926)

* Fri Apr 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt15
- AutoConfig: replace via to openchrome
- libxf86config: fixed parse "Disable" parameters from Section Module (close #15242)

* Wed Apr 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt14
- Mesa-7.0.3-rc3

* Mon Mar 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt13
- disable legacy mono, color, advanced framebuffer

* Fri Mar 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt12
- disable load Record exstension by default
- fontpath.d updated documentation (close #14933)

* Wed Feb 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt11
- merged server-1.4-branch:
  + security: Fix for Bug #14480: untrusted access broken in 7.3
  + Fix rotation for multi-monitor situation
  + Don't break grab and focus state for a window when redirecting it
  + Fix context sharing between direct/indirect contexts
- dix: set dev->key to NULL after freeing it in CloseDevice
- fix %%bx in VBEGetPixelClock to match spec

* Fri Feb 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt10
- Mesa-7.0.3-rc2
- resize composite overlay window when the root window changes
- xfree86: fix plug memory leak

* Fri Feb 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt9
- merged server-1.4-branch:
  + xkb: don't update LEDs if they don't exist
  + xkb: when copying sections, make sure num_rows is set too
  + xfree86: don't call xalloc from signal handlers when posting events
  + xfree86: stick two more checks in for num_valuators < MAX_VALUATORS
  + dix: Always add valuator information if present
  + dix: Allow arbitrary value ranges in GetPointerEvents
  + dix: Add scaling of X and Y on the reported pointer-events
  + dix: Skip call to clipAxis for relative core-events
  + dix: Move motion history update until after screen crossing and clipping
  + X86EMU: handle CPUID instruction
  + xkb: when copying the keymap, make sure the structs default to 0/NULL
  + XkbCopyKeymap: Don't leak all the sections
  + dix: set the correct number of valuators in valuator events
  + Xephyr: Don't leak screen damage structure
  + Xephyr: One-time keyboard leak fix
  + OS: IO: Zero out client buffers
  + bgPixel (unsigned long) is 64-bit on x86_64, so -1 != 0xffffffff

* Tue Jan 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt8
- there is no such thing as /dev/cpu/mtrr
- fix AlwaysCore handling

* Mon Jan 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt7
- update last security patch

* Fri Jan 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt6
- CVE-2007-6429: Don't spuriously reject <8bpp shm pixmaps

* Thu Jan 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt5
- fixed CVE-2007-5760, CVE-2007-6427, CVE-2007-6428, CVE-2007-6429, CVE-2008-0006

* Wed Jan 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt4
- yet another Xv extension byte swapping fix

* Mon Jan 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt3
- Don't leak connection translation table on regeneration
- Don't reinit devices
- Fix potential crasher in xf86CrtcRotate()
- Xv extension not byte-swapping properly

* Tue Jan 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt2
- fixed requires (close #13808)
- never overwrite realInputProc with enqueueInputProc (close #13843)

* Sat Dec 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4.0.90-alt1
- 1.4.1 pre-release

* Mon Dec 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4-alt12
- fixed keyboard leds reflect modifier state (close #13024)

* Sat Dec 08 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4-alt11
- verify and reject obviously broken modes
- fixes memory corruption if a too small "Virtual" was specified in xorg.conf
  for the selected multi-monitor configuration
- make config file preferred mode override monitor preferred mode

* Sat Dec 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4-alt10
- fix a hang in OpenOffice.org when opening menus (close #13566)

* Sun Nov 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4-alt9
- Mesa-7.0.2-git-GLX_BIND_TO_MIPMAP_TEXTURE_EXT-bug9264.patch

* Sun Nov 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4-alt8
- Mesa-7.0.2

* Mon Nov 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4-alt7
- drop XKB patches (close #13298, reopen #13024)
- added Mesa-7.0.1-git-memleak-in-SSE.patch

* Tue Oct 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4-alt6
- fixed keyboard leds reflect modifier state (close #5712, #13024)

* Thu Oct 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4-alt5
- fixed vga driver crash
- disable optimization (introduced by ajax) due to a general vesa
  driver crash later in memcpy
- only issue XF86_APM_CAPABILITY_CHANGED for video change ACPI events
  (not e.g. brightness etc.)
- fixed key down test

* Sun Oct 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4-alt4
- rebuild

* Fri Sep 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4-alt3
- disable Composite exstension by default

* Sat Sep 08 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4-alt2
- disable dbus/hal
- fixed build Xdmx

* Thu Sep 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.4-alt1
- 1.4
- drop upstream patches

* Sat Sep 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt24
- rebuild with renderproto-0.9.3

* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt23
- drop %_sysconfdir/X11/xinit.d/xfonts, adieu chkfontpath

* Tue Aug 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt22
- xorg-x11-xtrans-devel to pull in abstract socket support
- set default font path to "catalogue:%_sysconfdir/X11/fontpath.d"
- requires libXfont >= 1.3.0, fonts-bitmap-misc >= 7.0.0-alt2

* Fri Aug 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt21
- get rid of the type1 font module
- added xorg-server-1.3.0.0-idletime.patch
- update offscreen pixmaps patch
- update patch for Mesa-7.0.1

* Thu Aug 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt20
- update pci.ids to 2007-08-15 snapshot

* Tue Aug 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt19
- Backported many randr 1.2 fixes and additions from xserver git

* Tue Aug 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt18
- drop obsolete "-scanpci" option (close #12544)

* Sat Aug 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt17
- Mesa-7.0.1

* Wed Aug 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt16
- added Mesa-7.0-git-function-call-bug11731.patch,
	Mesa-7.0-git-fragment-program-bug11733.patch,
	Mesa-7.0-git-glPointParameteriv-bug11754.patch,
	Mesa-7.0-git-failure-caused-by-undeclared-variable-bug11783.patch,
	Mesa-7.0-git-glGetAttribLocation-bug11774.patch

* Tue Jul 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt15
- update pci.ids to 2007-07-16 snapshot

* Mon Jul 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt14
- added xorg-server-1.3.0.0-git-domain-support-bug5000.patch,
	Mesa-7.0-git-depth-mix-up-bug11577.patch,
	Mesa-7.0-git-swizzle-related-bug11534.patch,
	Mesa-7.0-git-shader-info-bug11588.patch

* Tue Jul 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt13
- added xorg-server-1.3.0.0-git-xf86XVReputVideo.patch (close #12201),
	Mesa-7.0-git-image-bug11448.patch,
	Mesa-7.0-git-GL_DOT3_RGBA-bug11030.patch

* Mon Jun 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt12
- added xorg-server-1.3.0.0-git-DRIScreenPrivIndex-bug11340.patch:
  fixed Xorg crashes when last client disconnects and DRI is not available

* Sat Jun 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt11
- Mesa-7.0

* Thu Jun 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt10
- fixed XKEYBOARD extension for Xnest (close #12095)

* Sat Jun 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt9
- add libwfb.so module ownership for future compatibility

* Mon Jun 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt8
- added Mesa-6.5.3-git-GL_TEXTURE_LOD_BIAS-bug11049.patch,
	Mesa-6.5.3-git-point-attentuation-bug11042.patch,
	xserver-1.2.0-honor-displaysize.patch

* Tue May 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt7
- build GLX without USE_XCB

* Sat May 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt6
- added Mesa-6.5.3-git-STATE_HALF_VECTOR-bug10987.patch
- build GLX with USE_XCB

* Thu May 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt5
- added xorg-x11-server-Red-Hat-extramodes.patch

* Tue May 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt4
- build xephyr server
- added Mesa-6.5.3-git-glXGetArrayType-return-type-bug10938.patch

* Wed May 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt3
- rebuild with libX11 & Mesa with xcb

* Mon Apr 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt2
- Mesa-6.5.3
- fixed CVE-2007-1356

* Fri Apr 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.3.0.0-alt1
- Xorg-7.3 release
- drop upstream patches

* Wed Apr 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.2.99.905-alt4
- added xorg-server-1.2.99.905-git-optparsing-memleak.patch: Fix memory leak in option parsing

* Tue Apr 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.2.99.905-alt3
- added xorg-server-1.2.99.905-git-AIGLX-enterVT.patch: In AIGLX EnterVT processing,
  invoke driver EnterVT before resuming glx
- added xorg-server-1.2.99.905-git-parcer.patch: Don't write out empty sections from the parser
- added xorg-server-1.2.99.905-git-linuxPci-sysfs.patch: Look for the PCI ROM file elsewhere in sysfs

* Mon Apr 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.2.99.905-alt2
- fixed release-major

* Fri Apr 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.2.99.905-alt1
- Xorg-7.3RC5

* Fri Apr 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.2.99.904-alt1
- Xorg-7.3RC4

* Tue Apr 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.2.99.903-alt3
- fixed CVE-2007-1003: XC-MISC Extension ProcXCMiscGetXIDList() Memory Corruption

* Thu Mar 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.2.99.903-alt2
- added xorg-server-1.2.99.903-git-timer-rescheduling-bug10296.patch

* Tue Mar 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.2.99.903-alt1
- Xorg-7.3RC3
- set black background on startup

* Wed Mar 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.2.99.902-alt5
- added xorg-server-1.2.99.902-git-xf86_reload_cursors.patch,
	xorg-server-1.2.99.902-alt-loader-typo.patch
- spec cleanup

* Wed Mar 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.2.99.902-alt2
- added xorg-server-1.2.99.902-git-CRTC-based-cursor.patch

* Wed Mar 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.2.99.902-alt1
- Xorg-7.3RC2
- drop xorg-server-1.1.99.903-revert-int10.patch

* Tue Mar 13 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.2.99.901-alt1
- Xorg-7.3RC1
- added Mesa-6.5.2-git-n_dot_h-bug9977.patch

* Wed Feb 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.2.0-alt6
- added Mesa-6.5.2-git-tnl-bug9856.patch,
	xorg-server-1.2.0-git-8888x0565mmx-bug9682.patch,
	xorg-server-1.2.0-git-use-8888x0565mmx.patch,
	Mesa-6.5.2-git-fd-bug9684.patch,
	xorg-server-1.2.0-git-xf86_libc_h-typo.patch,
	xorg-server-1.2.0-git-client-privates-leak.patch,
	xorg-server-1.2.0-git-security-bug6988.patch,
	xorg-server-1.2.0-git-clientGone-XFixes-bug1753.patch

* Mon Feb 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.2.0-alt5
- added Mesa-6.5.2-git-main-mem-leak.patch,
	Mesa-6.5.2-git-glxext-mem-leak.patch

* Mon Feb 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.2.0-alt4
- added xorg-server-1.2.0-git-linuxPCIOpenFile-bug9692.patch,
	Mesa-6.5.2-git-CheckArrayBounds-bug9285.patch,
	Mesa-6.5.2-git-GetVertexAttribPointerv-bug9628.patch,
	xorg-server-1.2.0-git-length-limiting-bug9680.patch
- added requires iceauth for %name

* Thu Jan 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.2.0-alt3
- added xorg-server-1.2.0-git-EXA-bug7639.patch,
	xorg-server-1.2.0-git-plugmemoryleak.patch

* Wed Jan 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.2.0-alt2
- fixed typo in obsoletes xorg-x11-extensions-dri

* Tue Jan 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.2.0-alt1
- Xorg-7.2.0 release
- drop upstream patches

* Mon Jan 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.99.903-alt6.2
- added xorg-server-1.1.99.903-git-drmOpen-bug9275.patch,
	xorg-server-1.1.99.903-git-optimized-render-cases.patch,
	xorg-server-1.1.99.903-git-real-optimized-render-cases.patch,
	xorg-server-1.1.99.903-alt-libglx-link.patch

* Fri Jan 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.99.903-alt6
- update pci.ids to 2007-01-18 snapshot

* Tue Jan 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.99.903-alt5
- security fix CVE-2006-6101, CVE-2006-6102, CVE-2006-6103
- added Mesa-6.5.2-git-PolygonMode-bug9578.patch,
	xorg-server-1.1.99.901-glXDRIbindTexImage-target.patch,
	xorg-server-1.1.99.903-dont-backfill-bg-none.patch,
	xorg-server-1.1.99.903-offscreen-pixmaps.patch,
	xorg-server-1.1.99.903-no-move-damage.patch,
	xorg-server-1.1.99.903-git-ARGB-GLcore.patch,
	Mesa-6.5.2-git-VBO-state-bug9445.patch,
	Mesa-6.5.2-git-32bit-Z-buffer.patch

* Mon Jan 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.99.903-alt4
- added Mesa-6.5.2-git-swrast-bug9345.patch,
	xorg-server-1.1.99.903-git-exa-disable-SHM-pixmaps.patch,
	xorg-server-1.1.99.903-git-exa-dxdy.patch,
	xorg-server-1.1.99.903-git-exa-driver-limits.patch,
	xorg-server-1.1.99.903-git-fbdevhw.patch

* Thu Dec 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.99.903-alt3
- added xorg-server-1.1.99.903-revert-int10.patch, fixed i9xx problems
- added xorg-server-1.1.99.903-ignore-libdrm.patch to ignore requests
  for loading obsolete drm module
 
* Wed Dec 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.99.903-alt2.1
- added xorg-server-1.1.99.903-git-composite-viewable.patch,
	xorg-server-1.1.99.903-git-pci_ids.patch

* Sun Dec 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.99.903-alt2
- Mesa-6.5.2 release
- added xorg-server-1.1.99.903-render-size-overflow.patch

* Sat Dec 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.99.903-alt1
- Xorg-7.2RC3
- Mesa-6.5.2 CVS snapshot 2006-12-01
- removed xorg-x11-extensions-dri subpackage
- moved libglx-x11.so to %_libdir/X11/mesa_gl
- added xorg-server-1.1.99.902-git-xf86MapDomainMemory.patch,
	xorg-server-1.1.99.902-git-latest_gl_API.patch,
	xorg-server-1.1.99.902-xdmx-RENDER.patch,
	xorg-server-1.1.99.901-GetDrawableAttributes.patch

* Thu Nov 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.99.902-alt2
- fixed undefined symbol in libxf86config.so
- removed xorg-server-1.1.99.3-alt-extmod-fontcache.patch and disabled fontcache
- Mesa-6.5.2 CVS snapshot 2006-11-15

* Tue Nov 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.99.902-alt1
- Xorg-7.2RC2
- Mesa-6.5.2 CVS snapshot 2006-11-14
- removed xorg-x11-server-1.1.1-offscreen-pixmaps.patch

* Wed Oct 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.99.901-alt1
- Xorg-7.2RC1
- Mesa-6.5.2 CVS snapshot 2006-10-18

* Wed Oct 11 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.1-alt6
- build with --enable-glx-tls to enable TLS support.

* Wed Oct 04 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.1-alt5
- rebuild with glibc-2.5
- remove linux-libc-headers from build dependencies, build with glibc-kernheaders

* Thu Sep 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.1-alt4
- rollback to older GL API (xorg-server-1.1.1 2006-03-12, since 2006-08-31 broke fglrx)
- added %%_optlevel 3 and call me a gentooist

* Mon Sep 11 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.1-alt3
- fix AIGLX VT switching
- probe xorg-server-1.1.1-mdk-Blue-background-on-startup.patch

* Fri Sep 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.1-alt2
- fix problems with vertex program protocol

* Wed Aug 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.1-alt1.1
- Xorg-7.1.1
- Mesa-6.5.1
- build AIGLX, disabled by defaults
- build with APM/ACPI, PM support disabled by defaults

* Wed Aug 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.2-alt6
- xorg-server-1.1.0-setuid.patch
- removed x-cursor-theme-bluecurve
- fixed requires for %name

* Wed May 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.2-alt5
- xorg-x11-6.9.0-CVE-2006-1526.patch

* Sun Apr 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.2-alt4
- removed patch for support APM/ACPI (since not used)

* Sat Apr 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.2-alt3
- removed shadow patch

* Fri Mar 24 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.2-alt2
- added fonts loader script
- removed layer extension
- fixed build glx extension for x86_64

* Tue Mar 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.2-alt1
- 1.0.2 security bugfix
- updated shadow to 1.1.0 from CVS

* Tue Mar 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt15
- Xfixes Version 4.0
- Composite Version 0.3
- disabled RH die-ugly-pattern-die-die-die patch

* Sun Mar 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt14
- added render2swap patch from CVS
- added RRGetRotation patch from CVS
- added mesa-6.4.2-dix-config patch

* Fri Mar 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt13
- fixed update from XFree86
- added xkb maprules patch from CVS

* Tue Feb 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt12
- build with linux-libc-headers
- removed requires libmesa-%%mesaversion to xorg-x11-extensions-glx, requires libmesa

* Fri Feb 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt11
- Added xorg-server-1.0.1-SEGV-on-null-interface.patch which prevents a
  SEGV on null interfaces (#9023)

* Thu Feb 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt10
- rebuild with Mesa-6.4.2

* Fri Feb 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt9
- removed xkb script (#9012, #7787)
- added requires xorg-x11-xdm

* Tue Jan 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt8
- added randrstr.h to sdk subpackage

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt7
- fixed ACPI support

* Wed Jan 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt6
- fixed requires

* Thu Jan 12 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt5
- set drvdir to /usr/libexec/X11/drv.d
- fixed build FontCache extensions

* Sun Jan 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt4
- fixed conflicts version

* Thu Jan 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt3
- enabled APM/ACPI support

* Sun Jan 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt2
- fixed requires

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.99.4-alt1
- Xorg-7.0RC3

* Fri Nov 25 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:0.99.3-alt0.1
- 7.0-RC2
