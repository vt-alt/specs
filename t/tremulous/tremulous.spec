#define gver 4.7
#set_gcc_version %%gver

ExclusiveArch: %ix86 x86_64 aarch64 ppc64le %e2k

%define _user _tremulous
%define _group _tremulous
%define _home %_localstatedir/%name

%ifarch x86_64
%define __arch x86_64
%endif
%ifarch %ix86
%define __arch x86
%endif
%ifarch ppc
%define __arch ppc
%endif
%ifarch ppc64le
%define __arch ppc64le
%endif
%ifarch aarch64
%define __arch aarch64
%endif
%ifarch %e2k
%define __arch e2k
%endif

Name: tremulous
Version: 1.2.0
Release: alt2

Summary: Tremulous - 3D FPS Strategic Shooter
License: GPL
Group: Games/Arcade
Url: http://tremulous.net

Source: tremulous-%version-src.tar
Source1: tremulous-client.desktop
Source2: tremulous.xpm
Source3: tremulous.init

#	fix for #14027
Patch0: tremulous-alt-mmap.patch
Patch1: tremulous-alt-debuginfo-2.patch
Patch2: tremulous-alt-e2k.patch

# fedora patches
Patch10: tremulous-1.2.0-dll-overwrite.patch
Patch11: tremulous-getstatus-dos.patch
Patch12: tremulous-aarch64.patch
Patch13: tremulous-i686.patch

Requires: %name-server = %version-%release
Requires: %name-client = %version-%release

# Automatically added by buildreq on Wed Jun 25 2008
BuildRequires: esound libX11-devel libXext-devel libopenal-devel libSDL-devel

# instead of bundled ones
BuildRequires: libcurl-devel
BuildRequires: libjpeg-devel
BuildRequires: libvorbis-devel
BuildRequires: libspeex-devel
BuildRequires: libspeexdsp-devel
BuildRequires: zlib-devel

BuildPreReq: libGL-devel libGLU-devel

%description
Tremulous is a free, open source game that blends a team based FPS with elements
of an RTS. Players can choose from 2 unique races, aliens and humans. Players on
both teams are able to build working structures in-game like an RTS. These
structures provide many functions, the most important being spawning. The
designated builders must ensure there are spawn structures or other players will
not be able to rejoin the game after death. Other structures provide automated
base defense (to some degree), healing functions and much more...

Player advancement is different depending on which team you are on. As a human,
players are rewarded with credits for each alien kill. These credits may be used
to purchase new weapons and upgrades from the "Armoury". The alien team advances
quite differently. Upon killing a human foe, the alien is able to evolve into a
new class. The more kills gained the more powerful the classes available.

The overall objective behind Tremulous is to eliminate the opposing team. This
is achieved by not only killing the opposing players but also removing their
ability to respawn by destroying their spawn structures.

This is a virtual package to install tremulous client and dedicated server.

%package common
Group: Games/Arcade
Summary: Common files for Tremulous

%description common
Tremulous is a free, open source game that blends a team based FPS with elements
of an RTS. Players can choose from 2 unique races, aliens and humans. Players on
both teams are able to build working structures in-game like an RTS. These
structures provide many functions, the most important being spawning. The
designated builders must ensure there are spawn structures or other players will
not be able to rejoin the game after death. Other structures provide automated
base defense (to some degree), healing functions and much more...

This package contains common files.

%package client
Group: Games/Arcade
Summary: Tremulous client
Requires: %name-common = %version-%release
Provides: %name-client = %version-%release
Requires: %name-data = %version

%description client
Tremulous is a free, open source game that blends a team based FPS with elements
of an RTS. Players can choose from 2 unique races, aliens and humans. Players on
both teams are able to build working structures in-game like an RTS. These
structures provide many functions, the most important being spawning. The
designated builders must ensure there are spawn structures or other players will
not be able to rejoin the game after death. Other structures provide automated
base defense (to some degree), healing functions and much more...

Tremulous client.

%package server
Group: Games/Arcade
Summary: Tremulous dedicated server package
Requires: %name-common = %version-%release
Requires: %name-data = %version

%description server
Tremulous is a free, open source game that blends a team based FPS with elements
of an RTS. Players can choose from 2 unique races, aliens and humans. Players on
both teams are able to build working structures in-game like an RTS. These
structures provide many functions, the most important being spawning. The
designated builders must ensure there are spawn structures or other players will
not be able to rejoin the game after death. Other structures provide automated
base defense (to some degree), healing functions and much more...

Dedicated server.

%prep
%setup
sed -i 's,-Werror,,g' src/tools/asm/Makefile
%patch0 -p0 
%patch1 -p2
%ifarch %e2k
%patch2 -p2
%endif

%patch10 -p1 -b .dll-overwrite
%patch11 -p1 -b .getstatus-dos
%ifarch aarch64
%patch12 -p1 -b .aarch64
%endif
%patch13 -p1 -b .i686

# Rip out the bundled libraries and use the
# system versions instead
rm -r src/SDL12 src/AL src/libcurl src/libspeex src/libs

%build
%add_optflags -fno-strict-aliasing -ffast-math
# the CROSS_COMPILING=1 is a hack to not build q3cc and qvm files
# since we've stripped out q3cc as this is not Free Software.
%make_build release \
	OPTIMIZE="%optflags" \
	CROSS_COMPILING=1 \
	USE_CODEC_VORBIS=1 \
	USE_LOCAL_HEADERS=0 \
	BUILD_GAME_SO=0 \
	GENERATE_DEPENDENCIES=0 \
	USE_INTERNAL_SPEEX=0 \
	USE_INTERNAL_ZLIB=0

%install
install -p -D -m644 %SOURCE1 %buildroot%_desktopdir/%name-client.desktop
install -D -p -m 0644 %SOURCE2 %buildroot%_liconsdir/tremulous.xpm

install -pD -m 0755 build/release-linux-%__arch/tremulous.%__arch %buildroot%_gamesbindir/tremulous.%__arch
install -pD -m 0755 build/release-linux-%__arch/tremded.%__arch %buildroot%_gamesbindir/tremded.%__arch

mkdir -p %buildroot%_bindir

cat << __EOF__ > %buildroot%_bindir/tremulous
#!/bin/sh

%_gamesbindir/tremulous.%__arch +set sv_pure 0 +set vm_cgame 0 +set vm_game 0 +set vm_ui 0 +set fs_basepath %_gamesdatadir/%name $@
__EOF__
chmod 0755  %buildroot%_bindir/tremulous

ln -sf %_gamesbindir/tremded.%__arch %buildroot%_bindir/tremded

# initscript for dedicated server:
install -pDm0755 %SOURCE3 %buildroot%_initdir/%name

mkdir -p %buildroot%_sysconfdir/sysconfig/

cat << __EOF__ > %buildroot%_sysconfdir/sysconfig/%name
OPTIONS="+set sv_strictauth 0 +set sv_pure 0 +map atcs +set fs_basepath %_gamesdatadir/%name"
__EOF__

install -pDm0644 ChangeLog %buildroot%_docdir/%name/ChangeLog
install -pDm0644 COPYING %buildroot%_docdir/%name/COPYING
install -pDm0644 CC %buildroot%_docdir/%name/CC
install -pDm0644 GPL %buildroot%_docdir/%name/GPL

install -d %buildroot%_home

%pre server
/usr/sbin/groupadd -r -f %_group ||:
/usr/sbin/useradd -g %_group -c 'The tremulous user' \
        -d %_home -s /dev/null -r %_user >/dev/null 2>&1 ||:

%post server
%post_service %name

%preun server
%preun_service %name

%files

%files common
%doc %_docdir/%name

%files client
%_bindir/%name
%_gamesbindir/tremulous.%__arch
%_liconsdir/tremulous.xpm
%_desktopdir/tremulous-client.desktop

%files server
%_bindir/tremded
%_gamesbindir/tremded.%__arch
%config(noreplace) %_sysconfdir/sysconfig/*
%_initdir/*
%attr(775,root,%_group) %dir %_home

%changelog
* Sat Oct 05 2019 Michael Shigorin <mike@altlinux.org> 1.2.0-alt2
- Build on %%e2k and aarch64 as well (try building on ppc64le either)
- Pull fedora patches and some spec bits in

* Wed Sep 12 2018 Pavel Moseev <mars@altlinux.org> 1.2.0-alt1
- Updated to upstream version 1.2.0-beta

* Tue Mar 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt4.2
- Built with gcc 4.7

* Thu Apr 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt4.1
- Fixed build

* Thu Jul 16 2009 Timur Batyrshin <erthad@altlinux.org> 1.1.0-alt4
- fixed repocop warnings

* Mon Mar 02 2009 Timur Batyrshin <erthad@altlinux.org> 1.1.0-alt3
- spec fixed for ppc build

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt2.1
- NMU:
  * updated build dependencies

* Wed Nov 05 2008 Timur Batyrshin <erthad@altlinux.org> 1.1.0-alt2
- fixed repocop freedesktop warnings

* Wed Sep 10 2008 Timur Batyrshin <erthad@altlinux.org> 1.1.0-alt1
- Initial build for ALT Linux


