Name: x11vnc
Version: 0.9.16
Release: alt1

%def_with avahi

Summary: VNC server for real X displays
License: GPL
Group: Networking/Remote access
Url: https://github.com/LibVNC/x11vnc

Source: %version.tar.gz

# Automatically added by buildreq on Wed Apr 27 2016
# optimized out: fontconfig libX11-devel libXext-devel libXfixes-devel libXi-devel libXrender-devel libcom_err-devel libgpg-error libkrb5-devel libp11-kit libwayland-client libwayland-server perl pkg-config python-base python-modules xorg-compositeproto-devel xorg-damageproto-devel xorg-fixesproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-randrproto-devel xorg-recordproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel zlib-devel
BuildRequires: imake libICE-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXinerama-devel libXrandr-devel libXtst-devel libavahi-devel libcairo-devel libssl-devel libvncserver-devel xorg-cf-files

%if_with avahi
BuildRequires: libavahi-devel
%endif

%description
x11vnc allows one to remotely view and interact with real X displays
(i.e. a display corresponding to a physical monitor, keyboard, and mouse)
with any VNC viewer. In this way it plays the role for Unix/X11 that
WinVNC plays for Windows.

%package scripts
License: GPL
Group: Networking/Remote access
BuildArch: noarch
Summary: Various x11vnc wrappers

%description scripts
%summary

In this directory you'll find a hodgepodge of wrapper scripts and
utility programs that have found some use with x11vnc.

Some are on the rough side and will need some customization for your use.

%prep
%setup

%build
%autoreconf
%configure --without-uinput
%make_build

%install
%makeinstall
install tkx11vnc %buildroot%_bindir/

%files
%_bindir/%name
%_man1dir/%name.*
%_desktopdir/*
%doc README NEWS

%files scripts
%_bindir/tkx11vnc
%doc misc/*
%exclude  %_bindir/Xdummy

%changelog
* Wed Aug 21 2019 Fr. Br. George <george@altlinux.ru> 0.9.16-alt1
- Autobuild version bump to 0.9.16

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.15-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 0.9.15-alt1
- Autobuild version bump to 0.9.15

* Wed Apr 27 2016 Fr. Br. George <george@altlinux.ru> 0.9.14-alt1
- Upstream migrated under libNVNC project
- Autobuild version bump to 0.9.14
- Introduce supplemental scripts

* Sun Mar 27 2011 Terechkov Evgenii <evg@altlinux.org> 0.9.12-alt3
- Fix build with sisyphus_check 0.8.20-alt1

* Sat Oct  2 2010 Terechkov Evgenii <evg@altlinux.org> 0.9.12-alt2
- Rebuild with libssl10

* Sun Sep 12 2010 Terechkov Evgenii <evg@altlinux.org> 0.9.12-alt1
- 0.9.12

* Wed Apr 07 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9.9-alt2
- fixed starting Xvfb 1.8

* Sat Mar 13 2010 Terechkov Evgenii <evg@altlinux.ru> 0.9.9-alt1
- Patch from upstream git to fix "will always overflow destination" on x86_64
- 0.9.9

* Fri Jun 05 2009 Ivanov Maxim <redbaron@altlinux.org> 0.9.8-alt1
- Bump to 0.9.8

* Wed Jul 11 2007 Alex V. Myltsev <avm@altlinux.ru> 0.9.2-alt1
- 0.9.1:
- - "-users sslpeer": authentication by unix username in SSL cert id
- - SSL connections in the Java viewer
- - misc bug fixes
- 0.9.2: supports building with external libvncserver (not used yet)

* Fri Apr 20 2007 Alex V. Myltsev <avm@altlinux.ru> 0.9-alt1
- 0.9: avahi advertising, ultravnc extensions, more minor features;
- TightVNC file transfer now off by default

* Mon Feb 19 2007 Alex V. Myltsev <avm@altlinux.ru> 0.8.4-alt1
- 0.8.4: VNC reflector, X session autocreation.

* Sat Nov 25 2006 Alex V. Myltsev <avm@altlinux.ru> 0.8.3-alt1
- 0.8.3: allows unixpw authentication, can rotate screen, etc.

* Thu Jul 20 2006 Alex V. Myltsev <avm@altlinux.ru> 0.8.2-alt1
- New version (display autosearch, kbd/mouse grabbing etc).
- Now built with OpenSSL.

* Tue Mar 28 2006 Alex V. Myltsev <avm@altlinux.ru> 0.8-alt1
- New version (file transfer support, some minor features, bug fixes).

* Mon Aug 29 2005 Alex V. Myltsev <avm@altlinux.ru> 0.7.2-alt1
- First build for ALT Linux.

