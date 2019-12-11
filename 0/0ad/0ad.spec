Name: 0ad
Epoch: 1
Version: 0.0.23b
Release: alt3

Group: Games/Strategy
Summary: Free, open-source realtime strategy game of ancient warfare
License: Various (all distributable)
Url: http://www.wildfiregames.com/0ad/
Requires: %name-data = %epoch:%version
Source: %name-%version.tar
Patch0: mozjs38-jit-none.patch
Patch1: 0ad-ppc64le.patch

BuildRequires: gcc-c++ python cmake
BuildRequires: boost-filesystem-devel boost-flyweight-devel boost-signals-devel
BuildRequires: libjpeg-devel libpng-devel libvorbis-devel
BuildRequires: libopenal-devel libGL-devel libSDL2-devel libwxGTK3.0-devel libXcursor-devel
BuildRequires: libcurl-devel libxml2-devel libnspr-devel libicu-devel zlib-devel
BuildRequires: libenet-devel libminiupnpc-devel libgloox-devel libsodium-devel
BuildRequires: python-devel python-module-json

# premake5 requires /proc/self/exe
BuildRequires: /proc

%description
0 A.D. (pronounced "zero ey-dee") is a free, open-source, cross-platform
real-time strategy (RTS) game of ancient warfare. In short, it is a
historically-based war/economy game that allows players to relive or
rewrite the history of Western civilizations, focusing on the years
between 500 B.C. and 500 A.D. The project is highly ambitious, involving
state-of-the-art 3D graphics, detailed artwork, sound, and a flexible
and powerful custom-built game engine.

The game has been in development by Wildfire Games (WFG), a group of
volunteer, hobbyist game developers, since 2001. The code and data are
available under the GPL license, and the art, sound and documentation
are available under CC-BY-SA. In short, we consider 0 A.D. an an
educational celebration of game development and ancient history.

%prep
%setup
cp -p %{P:0} libraries/source/spidermonkey/FixJitNone.diff
echo "patch -p0 <../FixJitNone.diff" >>libraries/source/spidermonkey/patch.sh
%patch1 -p1

%build
mkdir -p libraries/source/fcollada/src/output/debug/FCollada
export CFLAGS="%optflags"
export CPPFLAGS="%optflags"
export SHELL=/bin/sh
[ -n "$NPROCS" ] || NPROCS=%__nprocs
build/workspaces/update-workspaces.sh \
	--bindir=%_bindir \
	--datadir=%_datadir/%name \
	--libdir=%_libdir/%name \
	-j$NPROCS
%make_build -C build/workspaces/gcc verbose=1

%install
install -Dm 0755 binaries/system/pyrogenesis %buildroot%_bindir/pyrogenesis
install -Dm 0755 binaries/system/libCollada.so %buildroot%_libdir/%name/libCollada.so
install -Dm 0755 binaries/system/libAtlasUI.so %buildroot%_libdir/%name/libAtlasUI.so
install -Dm 0755 binaries/system/libmozjs*-ps-release.so %buildroot%_libdir/%name/
install -Dm 0755 binaries/system/libnvcore.so %buildroot%_libdir/%name/libnvcore.so
install -Dm 0755 binaries/system/libnvimage.so %buildroot%_libdir/%name/libnvimage.so
install -Dm 0755 binaries/system/libnvmath.so %buildroot%_libdir/%name/libnvmath.so
install -Dm 0755 binaries/system/libnvtt.so %buildroot%_libdir/%name/libnvtt.so

install -Dm 0644 build/resources/0ad.desktop %buildroot%_desktopdir/%name.desktop
install -Dm 0644 build/resources/0ad.png %buildroot%_pixmapsdir/%name.png
ln -s pyrogenesis %buildroot%_bindir/0ad
mkdir -p %buildroot%_datadir/0ad
cp -a binaries/data/* %buildroot%_datadir/0ad/

%files
%doc README.txt
%_bindir/0ad
%_bindir/pyrogenesis
%_libdir/%name/*.so
%_pixmapsdir/%name.png
%_desktopdir/%name.desktop
%dir %_libdir/%name
%_datadir/0ad/*

%changelog
* Thu Aug 29 2019 Alexey Tourbin <at@altlinux.ru> 1:0.0.23b-alt3
- ppc64le.patch from wiki.raptorcs.com/wiki/Porting/0ad

* Wed Aug 28 2019 Alexey Tourbin <at@altlinux.ru> 1:0.0.23b-alt2
- build with bundled mozjs38 again, should cure sporadic segfaults
- backported a fix for mozjs38 on non-JIT architectures

* Mon Dec 24 2018 Alexey Tourbin <at@altlinux.ru> 1:0.0.23b-alt1
- official re-release of Alpha 23

* Tue Jun 26 2018 Alexey Tourbin <at@altlinux.ru> 1:0.0.23-alt2
- bundled mozjs won't build on aarch64, trying --with-system-mozjs38

* Wed Jun 06 2018 Alexey Tourbin <at@altlinux.ru> 1:0.0.23-alt1
- 0.0.22 -> 0.0.23
- updated build dependencies (wxGTK 2.8 -> 3.0, added libsodium)

* Sun Nov 05 2017 Alexey Tourbin <at@altlinux.ru> 1:0.0.22-alt1
- 0.0.21 -> 0.0.22

* Mon Jan 16 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:0.0.21-alt1
- Updated to 0.0.21.

* Mon Apr 04 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:0.0.20-alt1
- 0.0.20

* Sun Feb 28 2016 Andrey Cherepanov <cas@altlinux.org> 1:0.0.19.alpha-alt1.1
- Rebuild with new icu

* Mon Nov 30 2015 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:0.0.19.alpha-alt1
- 0.0.19

* Sun Jun 14 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:0.0.18.alpha-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Sat Mar 14 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.18.alpha-alt1
- 0.0.18

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 1:0.0.17.alpha-alt1.1
- rebuild with boost 1.57.0

* Tue Oct 14 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.17.alpha-alt1
- 0.0.17

* Mon May 19 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.16.alpha-alt1
- 0.0.16

* Wed Dec 25 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.15.alpha-alt1
- 0.0.15

* Fri Sep 06 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.14.alpha-alt1
- 0.0.14

* Wed Apr 03 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.13.alpha-alt1
- 0.0.13

* Thu Mar 28 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.12.alpha-alt1.1
- rebuild with boost 1.53

* Tue Dec 18 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.12.alpha-alt1
- 0.0.12
- don't relay on -data release

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.0.11.alpha-alt1.2
- Rebuilt with Boost 1.52.0

* Wed Oct 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.0.11.alpha-alt1.1
- Rebuilt with libpng15

* Wed Sep 12 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1:0.0.11.alpha-alt1
- build 0.0.11 from scratch

