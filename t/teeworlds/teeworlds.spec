%define _unpackaged_files_terminate_build 1 

%define _pseudouser_user     _teeworlds
%define _pseudouser_group    _teeworlds
%define _pseudouser_home     %_localstatedir/teeworlds

%def_without instagib

Name: teeworlds
Version: 0.7.3.1
Release: alt1
Summary: Cute little buggers with guns
License: distributable
Group: Games/Arcade
Url: https://www.teeworlds.com

ExclusiveArch: %ix86 x86_64

# https://github.com/teeworlds/teeworlds.git
Source: %name-%version.tar

# git submodules
Source1: %name-languages-%version.tar
Source2: %name-maps-%version.tar

# additional files from ALT
Source3: altlinux.tar

BuildRequires: gcc-c++ cmake
BuildRequires: python-modules
BuildRequires: libGL-devel libGLU-devel libSDL2-devel libX11-devel zlib-devel
BuildRequires: libalsa-devel libfreetype-devel libwavpack-devel libpnglite-devel libpng-devel
BuildRequires: libssl-devel

Requires: %name-gamedata = %EVR

Obsoletes: teeworlds-alt < %EVR

%description
A retro multiplayer shooter.

Teeworlds is a free online multiplayer game, available for all major
operating systems. Battle with up to 16 players in a variety of game
modes, including Team Deathmatch and Capture The Flag. You can even
design your own maps!

%package gamedata
Summary: Game data for teeworlds
License: distributable
Group: Games/Arcade
BuildArch: noarch

%description gamedata
Game data for teeworlds 2D shooter.

%package server
Summary: Teeworlds dedicated server
Group: System/Servers
Requires: %name-gamedata = %EVR

%description server
Teeworlds dedicated server

%if_with instagib
%package server-instagib
Summary: Instagib initscripts and config for teeworlds server
Group: System/Servers
Requires: %name-server = %EVR

%description server-instagib
:: Features ::
* One-hit-kill
* Killing spree
* Rifle only
* No powerups
* DM/TDM/CTF-support
* Easy setup (this one really is true)
%endif

%prep
%setup -a3

pushd datasrc/languages ; tar xf %SOURCE1 --strip-components=1 ; popd
pushd datasrc/maps      ; tar xf %SOURCE2 --strip-components=1 ; popd

rm -rf src/engine/external/{wavpack,zlib,pnglite}

%build
%cmake
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

install -Dpm0644 -t %buildroot%_datadir/metainfo other/%{name}.appdata.xml
install -Dpm0644 -t %buildroot%_desktopdir other/%{name}.desktop

mkdir -p %buildroot%_unitdir/
install -m 0644 altlinux/teeworlds-server@.service %buildroot%_unitdir/teeworlds-server@.service

install -pm755 altlinux/teeworlds_srv_wrapper %buildroot%_bindir

install -pDm644 altlinux/teeworlds.png %buildroot%_liconsdir/teeworlds.png
install -pDm644 altlinux/teeworlds16.png %buildroot%_miconsdir/teeworlds.png
install -pDm644 altlinux/teeworlds32.png %buildroot%_niconsdir/teeworlds.png

install -d %buildroot%_var/run/%name
install -d %buildroot%_var/log/%name
install -d %buildroot%_localstatedir/%name

install -pDm644 altlinux/teeworlds.logrotate %buildroot%_sysconfdir/logrotate.d/%name

install -pDm755 altlinux/teeworlds-dm.init %buildroot%_initdir/teeworlds-dm
install -pDm755 altlinux/teeworlds-tdm.init %buildroot%_initdir/teeworlds-tdm
install -pDm755 altlinux/teeworlds-ctf.init %buildroot%_initdir/teeworlds-ctf

%if_with instagib
install -pDm755 altlinux/teeworlds-idm.init %buildroot%_initdir/teeworlds-idm
install -pDm755 altlinux/teeworlds-itdm.init %buildroot%_initdir/teeworlds-itdm
install -pDm755 altlinux/teeworlds-ictf.init %buildroot%_initdir/teeworlds-ictf
%endif

install -pDm644 altlinux/teeworlds-dm.sysconfig %buildroot%_sysconfdir/sysconfig/teeworlds-dm
install -pDm644 altlinux/teeworlds-tdm.sysconfig %buildroot%_sysconfdir/sysconfig/teeworlds-tdm
install -pDm644 altlinux/teeworlds-ctf.sysconfig %buildroot%_sysconfdir/sysconfig/teeworlds-ctf

%if_with instagib
install -pDm644 altlinux/teeworlds-idm.sysconfig %buildroot%_sysconfdir/sysconfig/teeworlds-idm
install -pDm644 altlinux/teeworlds-itdm.sysconfig %buildroot%_sysconfdir/sysconfig/teeworlds-itdm
install -pDm644 altlinux/teeworlds-ictf.sysconfig %buildroot%_sysconfdir/sysconfig/teeworlds-ictf
%endif

install -pDm644 altlinux/server-dm.cfg %buildroot%_sysconfdir/%name/server-dm.cfg
install -pDm644 altlinux/server-tdm.cfg %buildroot%_sysconfdir/%name/server-tdm.cfg
install -pDm644 altlinux/server-ctf.cfg %buildroot%_sysconfdir/%name/server-ctf.cfg

%if_with instagib
install -pDm644 altlinux/server-idm.cfg %buildroot%_sysconfdir/%name/server-idm.cfg
install -pDm644 altlinux/server-itdm.cfg %buildroot%_sysconfdir/%name/server-itdm.cfg
install -pDm644 altlinux/server-ictf.cfg %buildroot%_sysconfdir/%name/server-ictf.cfg
%endif

%pre server
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'The teeworlds daemon' \
        -d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%post server
%post_service teeworlds-dm
%post_service teeworlds-tdm
%post_service teeworlds-ctf

%if_with instagib
%post server-instagib
%post_service teeworlds-idm
%post_service teeworlds-itdm
%post_service teeworlds-ictf
%endif

%preun server
%preun_service teeworlds-dm
%preun_service teeworlds-tdm
%preun_service teeworlds-ctf

%if_with instagib
%preun server-instagib
%preun_service teeworlds-idm
%preun_service teeworlds-itdm
%preun_service teeworlds-ictf
%endif

%files
%_bindir/teeworlds
%_desktopdir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_datadir/metainfo/%{name}.appdata.xml

%files server
%_unitdir/teeworlds-server@.service
%_bindir/teeworlds_srv*
%_initdir/%name-dm
%_initdir/%name-tdm
%_initdir/%name-ctf
%config(noreplace) %_sysconfdir/sysconfig/%name-dm
%config(noreplace) %_sysconfdir/sysconfig/%name-tdm
%config(noreplace) %_sysconfdir/sysconfig/%name-ctf
%config(noreplace) %_sysconfdir/%name/server-dm.cfg
%config(noreplace) %_sysconfdir/%name/server-tdm.cfg
%config(noreplace) %_sysconfdir/%name/server-ctf.cfg
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/logrotate.d/%name
%dir %attr(0770,root,%_pseudouser_group) %_var/run/%name
%dir %attr(0770,root,%_pseudouser_group) %_var/log/%name
%dir %attr(0700,%_pseudouser_user,%_pseudouser_group) %_localstatedir/%name

%if_with instagib
%files server-instagib
%config(noreplace) %_sysconfdir/%name/server-i*
%config(noreplace) %_sysconfdir/sysconfig/teeworlds-i*
%_initdir/teeworlds-i*
%endif

%files gamedata
%_datadir/teeworlds

%changelog
* Fri May 24 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.3.1-alt1
- Updated to upstream version 0.7.3.1.

* Tue Feb 12 2019 Slava Aseev <ptrnine@altlinux.org> 0.7.2-alt1
- Updated to upstream version 0.7.2
- Switch on debug info

* Wed Dec 05 2018 Alexey Melyashinsky <bip@altlinux.org> 0.7.0-alt1
- Updated to upstream version 0.7.0

* Fri Nov 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.4-alt2
- Fixed build with new bam.

* Wed Sep 06 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.4-alt1
- Updated to upstream version 0.6.4.

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6.1-alt1.qa1
- NMU: rebuilt for updated dependencies.

* Tue Aug 09 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.6.1-alt1
- 0.6.1.
- No instagib.
- Rename back to teeworlds.
- Apply gentoo patches for build using system pnglite and wavpack libs.

* Tue Dec 08 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.2-alt2
- Apply 3 fixes by Tom Adams:
  + When someone accidentally uses id=16 in kick command the server will
    crash.
  + When someone accidentally uses id=16 in ban command the server might
    crash.
  + If an invalid (too small) connless packet got received, the server
    will crash.
- Show caller of kick vote.

* Mon Nov 23 2009 Victor Forsyuk <force@altlinux.org> 0.5.2-alt1
- 0.5.2

* Tue Oct 27 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.2-alt1
- 0.5.2
- Rename package to teeworlds-alt
- Apply instagib patch, see
  http://www.teeworlds.com/forum/viewtopic.php?id=3103
- Add server and server-instagib subpackages with configs and
  initscripts.

* Wed Sep 02 2009 Victor Forsyuk <force@altlinux.org> 0.5.1-alt1
- 0.5.1
- Add instagib patch.
- Build with external pnglite and wavpack libraries.


* Wed Jan 14 2009 Victor Forsyuk <force@altlinux.org> 0.5.0-alt1
- 0.5.0

* Tue Dec 02 2008 Victor Forsyuk <force@altlinux.org> 0.4.3-alt2
- Renew build requirements to fix FTBFS.

* Mon Sep 01 2008 Victor Forsyuk <force@altlinux.org> 0.4.3-alt1
- 0.4.3

* Fri Aug 08 2008 Victor Forsyuk <force@altlinux.org> 0.4.2-alt1
- Initial build.
