# -*- mode: rpm-spec; coding: utf-8 -*-
%define realname icewm

Name: %realname
Version: 2.5.0
Release: alt1
Epoch:3

Summary: X11 Window Manager
Group: Graphical desktop/Icewm
License: LGPLv2
Url: https://ice-wm.org
Packager: Dmitriy Khanzhin <jinn@altlinux.org>

Provides: %realname-githubmod = %version-%release
Provides: %realname-light = %version-%release
Requires: design-%realname >= 1.0-alt6
Obsoletes: %realname-githubmod < %version-%release
Obsoletes: %realname-light < %version-%release

Source0: %name.tar
Source2: %realname.menu-method
Source3: %realname-16.png
Source4: %realname-32.png
Source5: %realname-48.png
Source6: start%realname
Source7: IceWM.xpm
Source8: %realname.wmsession
Source9: README.ALT
Source11: restart
Source12: icewm-old-changelog.bz2

Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake

# Automatically added by buildreq on Sun Jun 27 2021
BuildRequires: asciidoctor cmake gcc-c++ imlib2-devel libSM-devel
BuildRequires: libXcomposite-devel libXdamage-devel libXft-devel libXinerama-devel
BuildRequires: libXpm-devel libXrandr-devel libalsa-devel librsvg-devel
BuildRequires: libsndfile-devel perl-Pod-Usage perl-devel

%description
 Window Manager for X Window System. Can emulate the look of Windows'95, OS/2
Warp 3,4, Motif or the Java Metal GUI. Tries to take the best features of the
above systems. Features multiple workspaces, opaque move/resize, task bar,
window list, mailbox status, digital clock. Fast and small.
 This release is based on alternative source, based on a community fork
maintained on Github https://github.com/bbidulock/icewm

Recommends: iftop, mutt

%prep
%setup -n %name
%patch0 -p1
%ifarch armh
sed -i 's@-Wl,--as-needed @&-Wl,--allow-shlib-undefined@' src/CMakeLists.txt
%endif

%build
%cmake	-DPREFIX=%_prefix \
	-DCFGDIR=%_sysconfdir/X11/%realname \
	-DLIBDIR=%_x11x11dir/%realname \
	-DDOCDIR=%_datadir/doc/%name-%version \
	-DCONFIG_IMLIB2=on \
	-DCONFIG_LIBRSVG=on \
	-DCONFIG_GUIEVENTS=on \
	-DICESOUND="ALSA,OSS" \
	-DENABLE_LTO=on \
	-DXTERMCMD=xvt
%cmake_build

%install
# This step seems to be necessary for some reason. Executables have to be
# relinked before installation into buildroot; cmake --install alone does not
# invoke the re-link step.
DESTDIR=%buildroot %cmake_build -t install
%cmake_install

mkdir -p %buildroot%_sysconfdir/menu-methods
install -m 755 %SOURCE2 %buildroot%_sysconfdir/menu-methods/%realname

install -pD -m644 %SOURCE3 %buildroot%_miconsdir/%realname.png
install -pD -m644 %SOURCE4 %buildroot%_niconsdir/%realname.png
install -pD -m644 %SOURCE5 %buildroot%_liconsdir/%realname.png
install -pD -m644 %SOURCE7 %buildroot%_pixmapsdir/IceWM.xpm
install -pD -m644 %SOURCE8 %buildroot%_sysconfdir/X11/wmsession.d/04IceWM
install -m644 %SOURCE9 README.ALT
install -m644 %SOURCE12 icewm-old-changelog.bz2

mkdir -p %buildroot%_sysconfdir/X11/%realname

install -m 755 %SOURCE6 %buildroot%_bindir/start%realname
install -m 755 %SOURCE11 %buildroot%_sysconfdir/X11/%realname/restart

%find_lang  %realname

# remove unpackaged files
rm -f %buildroot/%_bindir/%realname-set-gnomewm
mv %buildroot/%_x11x11dir/%realname/themes/default ./Default
rm -rf %buildroot/%_x11x11dir/%realname/themes/*
mv ./Default %buildroot/%_x11x11dir/%realname/themes/
rm -f %buildroot/%_datadir/xsessions/%realname.desktop

%files -f %realname.lang
%dir %_sysconfdir/X11/%realname
%config(noreplace) %_sysconfdir/X11/%realname/restart
%config(noreplace) %_sysconfdir/menu-methods/*
%_sysconfdir/X11/wmsession.d/*
%_bindir/*
%dir %_x11x11dir/%realname
%_x11x11dir/%realname/*
%_niconsdir/*
%_miconsdir/*
%_liconsdir/*
%_pixmapsdir/*
%_man1dir/*
%_man5dir/*
%_datadir/xsessions/*.desktop

%doc AUTHORS NEWS README.ALT README.md %_cmake__builddir/*.html %_cmake__builddir/man/*.html icewm-old-changelog.bz2

%changelog
* Sun Jun 27 2021 Dmitriy Khanzhin <jinn@altlinux.org> 3:2.5.0-alt1
- 2.5.0
- buildreq
- fixed build in upstream and installed html documentation (ALT #35451)

* Thu May 13 2021 Arseny Maslennikov <arseny@altlinux.org> 3:2.3.4-alt1.1
- NMU: spec: adapted to new cmake macros.

* Fri May 07 2021 Dmitriy Khanzhin <jinn@altlinux.org> 3:2.3.4-alt1
- 2.3.4

* Sun May 02 2021 Dmitriy Khanzhin <jinn@altlinux.org> 3:2.3.3-alt1
- 2.3.3

* Sun Apr 04 2021 Dmitriy Khanzhin <jinn@altlinux.org> 3:2.3.1-alt1
- 2.3.1

* Sat Apr 03 2021 Dmitriy Khanzhin <jinn@altlinux.org> 3:2.3.0-alt1
- 2.3.0

* Thu Mar 25 2021 Dmitriy Khanzhin <jinn@altlinux.org> 3:2.2.1-alt1
- 2.2.1
- fixed build with LTO

* Wed Feb 10 2021 Dmitriy Khanzhin <jinn@altlinux.org> 3:2.1.2-alt1
- 2.1.2

* Fri Jan 29 2021 Dmitriy Khanzhin <jinn@altlinux.org> 3:2.1.1-alt1
- 2.1.1

* Thu Jan 07 2021 Dmitriy Khanzhin <jinn@altlinux.org> 3:2.0.1-alt1
- 2.0.1

* Fri Dec 18 2020 Dmitriy Khanzhin <jinn@altlinux.org> 3:2.0.0-alt1
- 2.0.0
- built with imlib2 as libgdk_pixbuf_xlib is deprecated

* Thu Nov 12 2020 Dmitriy Khanzhin <jinn@altlinux.org> 3:1.9.2-alt1
- 1.9.2

* Mon Nov 09 2020 Dmitriy Khanzhin <jinn@altlinux.org> 3:1.9.1-alt1
- 1.9.1

* Sat Oct 31 2020 Dmitriy Khanzhin <jinn@altlinux.org> 3:1.9.0-alt1
- 1.9.0

* Sat Sep 19 2020 Dmitriy Khanzhin <jinn@altlinux.org> 3:1.8.3-alt2
- fixed build on armh, thanks to sbolshakov@

* Sat Sep 19 2020 Dmitriy Khanzhin <jinn@altlinux.org> 3:1.8.3-alt1
- 1.8.3

* Sat Sep 12 2020 Dmitriy Khanzhin <jinn@altlinux.org> 3:1.8.2-alt1
- 1.8.2

* Sun Sep 06 2020 Dmitriy Khanzhin <jinn@altlinux.org> 3:1.8.1-alt1
- 1.8.1

* Sat Jul 18 2020 Dmitriy Khanzhin <jinn@altlinux.org> 3:1.7.0-alt1
- 1.7.0

* Fri Jun 05 2020 Dmitriy Khanzhin <jinn@altlinux.org> 3:1.6.6-alt1
- 1.6.6

* Fri Mar 20 2020 Dmitriy Khanzhin <jinn@altlinux.org> 3:1.6.5-alt1
- 1.6.5

* Mon Jan 27 2020 Dmitriy Khanzhin <jinn@altlinux.org> 3:1.6.4.0.2.397480d-alt1
- 1.6.4
- built with enabled LTO

* Wed Dec 25 2019 Dmitriy Khanzhin <jinn@altlinux.org> 3:1.6.3-alt1
- 1.6.3

* Thu Oct 03 2019 Dmitriy Khanzhin <jinn@altlinux.org> 3:1.6.2-alt1
- 1.6.2
- asciidoc replaced to asciidoctor
- buildreq

* Thu Aug 29 2019 Dmitriy Khanzhin <jinn@altlinux.org> 3:1.6.1-alt1
- 1.6.1 (ALT #37127)
- buildreq

* Thu Jan 03 2019 Dmitriy Khanzhin <jinn@altlinux.org> 3:1.4.2-alt4.git569bbe7
- git snapshot 569bbe7

* Tue Oct 02 2018 Dmitriy Khanzhin <jinn@altlinux.org> 3:1.4.2-alt3.git0ac7580
- git snapshot 0ac7580
- built with libgdk-pixbuf-xlib and librsvg support

* Sat Sep 15 2018 Dmitriy Khanzhin <jinn@altlinux.org> 3:1.4.2-alt2.git47ff050
- git snapshot 47ff050
- changed package name back to icewm
- added Epoch
- altconf: src/bindkey.h: key bindings back to default settings
- changed Url
- build without esound
- buildreq
- fixed documentation

* Sun Jul 30 2017 Dmitriy Khanzhin <jinn@altlinux.org> 1.4.2-alt1
- 1.4.2 release
- builreq

* Sat Mar 25 2017 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.12.195-alt2.git3cd87d6
- git snapshot 3cd87d6

* Thu Mar 09 2017 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.12.195-alt1.gitf199d1b
- git snapshot f199d1b

* Sun Mar 05 2017 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.12.56-alt5.gitedf8c50
- fixed icons search path
- added icons

* Mon Jan 16 2017 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.12.56-alt4.gitedf8c50
- git snapshot edf8c50
- fixed documentation place
- adapted logouticon patch, thx to YYY at altlinux forum

* Tue Dec 13 2016 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.12.56-alt3.gitcbb3423
- packaged desktop file for xsession

* Sun Nov 13 2016 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.12.56-alt2.gitcbb3423
- don't install debian-menu file, also desktop file
- packaged theme "Default"

* Tue Oct 04 2016 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.12.56-alt1.gitcbb3423
- git snapshot cbb3423 (ALT #32034, fixed in upstream)
- added support chromium and palemoon in toolbar (ALT #32504)

* Sun Mar 20 2016 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.12-alt2.gitb60d6d4
- git snapshot b60d6d4

* Sun Dec 20 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.12-alt1
- 1.3.12 release

* Mon Oct 05 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.11-alt2
- added Obsoletes
- added README.ALT
- fixed Url

* Tue Sep 22 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.11-alt1
- 1.3.11 release

* Sun Jul 05 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.10-alt1
- 1.3.10 release
- updated reboot/shutdown commands for use with systemd and sysvinit
- extended strong control of startup sequence in icewm-session

* Mon May 04 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.9-alt4.git960629d
- added forgotten requires to design-icewm

* Thu Apr 30 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.9-alt3.git960629d
- git snapshot 960629d
- old changelog cut off to separate file
- added conflict to icewm-light

* Tue Apr 14 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.9-alt2.gite97394f
- added support fd.o-style icons

* Tue Apr 14 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.9-alt1.gite97394f
- initial build for altlinux
