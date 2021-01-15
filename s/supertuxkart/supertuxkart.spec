Name: supertuxkart
Version: 1.2
Release: alt1

License: GPL-2.0-or-later and GPL-3.0-or-later and CC-BY-SA-3.0
Url: http://supertuxkart.sourceforge.net
Summary: SuperTuxKart is a kart racing game
Group: Games/Arcade
Packager: Ilya Mashkin <oddity@altlinux.ru>

# https://github.com/supertuxkart/stk-code
Source: %name-%version-src.tar.gz
#Patch: supertuxkart-0.9.3-debian-irrlicht.patch

BuildRequires(pre): rpm-build-ninja
# for aarch64 support
BuildRequires(pre): libGLES
# Automatically added by buildreq on Thu Jan 30 2020 (-bi)
# optimized out: bash4 bashrc cmake-modules elfutils glibc-kernheaders-generic glibc-kernheaders-x86 libGLU-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXrender-devel libcrypt-devel libglvnd-devel libharfbuzz-devel libogg-devel libsasl2-3 libstdc++-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-egl pkg-config python-modules python2-base python3 python3-base rpm-build-gir sh4 tzdata wayland-devel xorg-proto-devel xorg-xf86miscproto-devel zlib-devel
BuildRequires: bzlib-devel cmake gcc-c++ libGLEW-devel libXi-devel libXrandr-devel libXt-devel libXxf86misc-devel libXxf86vm-devel libcurl-devel libfreetype-devel libfribidi-devel libjpeg-devel libmcpp-devel libopenal-devel libpng-devel libsqlite3-devel libssl-devel libvorbis-devel libwayland-cursor-devel libwayland-egl-devel libxkbcommon-devel libxkbfile-devel poppler python-modules-compiler rpm-build-python3 libSDL2-devel
# use system libraries instead build-in
BuildRequires: libwiiuse-devel libraqm-devel

Requires: %name-data >= %version

%description
SuperTuxCart is a kart racing game

%prep
%setup -n %name-%version

%build
%cmake -GNinja -DCMAKE_BUILD_TYPE=Debug -DUSE_SYSTEM_ANGELSCRIPT=OFF -DBUILD_RECORDER=OFF -DCHECK_ASSETS=OFF
%ninja_build -C BUILD

%install
#install -d %%buildroot%%_niconsdir
%ninja_install -C BUILD

# The package contains a CVS/.svn/.git/.hg/.bzr/_MTN directory of revision control system.
# It was most likely included by accident since CVS/.svn/.hg/... etc. directories
# usually don't belong in releases.
# When packaging a CVS/SVN snapshot, export from CVS/SVN rather than use a checkout.
find %buildroot -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:
# the find below is useful in case those CVS/.svn/.git/.hg/.bzr/_MTN directory is added as %%doc
find . -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:

%files
#doc README.md CHANGELOG.md NETWORKING.md
%_bindir/*
%_desktopdir/%name.desktop
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/metainfo/*
%_pixmapsdir/*
%_iconsdir/hicolor/16x16/apps/*
%_iconsdir/hicolor/32x32/apps/*
%_iconsdir/hicolor/48x48/apps/*
%_iconsdir/hicolor/64x64/apps/*
%_iconsdir/hicolor/128x128/apps/*
%_iconsdir/hicolor/256x256/apps/*
%_iconsdir/hicolor/512x512/apps/*
%_iconsdir/hicolor/1024x1024/apps/*
# built in separate libwiiuse-devel
%exclude %_includedir/wiiuse.h
%exclude %_libdir/libwiiuse.a

%changelog
* Sat Aug 29 2020 Leontiy Volodin <lvol@altlinux.org> 1.2-alt1
- 1.2

* Tue Aug 11 2020 Leontiy Volodin <lvol@altlinux.org> 1.2-alt0.1.rc1
- Update to release candidate 1
- Build with ninja instead make

* Fri Jan 31 2020 Leontiy Volodin <lvol@altlinux.org> 1.1-alt2
- Move wiiuse into separate package (ALT #37832)
- Clean buildrequires

* Thu Jan 09 2020 Leontiy Volodin <lvol@altlinux.org> 1.1-alt1
- Update to upstream version 1.1

* Mon Apr 22 2019 Leontiy Volodin <lvol@altlinux.org> 1.0-alt1
- Update to upstream version 1.0

* Thu Feb 28 2019 Leontiy Volodin <lvol@altlinux.org> 0.10-alt0.1.beta1
- Update to beta1
- Added wayland support

* Mon Dec 17 2018 Leontiy Volodin <lvol@altlinux.org> 0.9.3git20181210-alt1
- Update to unreleased version (from git)

* Fri Jul 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.2-alt1
- Update to upstream version 0.9.2
- Move data into separate package

* Thu Aug 20 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt0.M70P.1
- Backport new version to p7 branch (ALT #31218)

* Wed Mar 26 2014 Ilya Mashkin <oddity@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Mon Dec 24 2012 Alex Karpov <karpov@altlinux.ru> 0.8-alt1
- at last - new version
    + libirrlicht dependency removed (there's included one)
    + build requirements revisited

* Thu Apr 05 2012 Alex Karpov <karpov@altlinux.ru> 0.7-alt2.2
- rebuild with new blender

* Sun Dec 26 2010 Alex Karpov <karpov@altlinux.ru> 0.7-alt2
- new release

* Mon Dec 20 2010 Alex Karpov <karpov@altlinux.ru> 0.7-alt1.rc2
- new release candidate

* Fri Dec 03 2010 Alex Karpov <karpov@altlinux.ru> 0.7-alt1.rc1
- mostly playable release candidate
    + updated build requirements

* Thu May 20 2010 Alex Karpov <karpov@altlinux.ru> 0.6.2-alt2
- fixed path for main executable in desktop-file (#23511)

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.6.2-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pkg-contains-cvs-or-svn-control-dir for supertuxkart
  * postclean-05-filetriggers for spec file

* Thu Aug 20 2009 Alex Karpov <karpov@altlinux.ru> 0.6.2-alt1
- new version

* Fri Aug 07 2009 Alex Karpov <karpov@altlinux.ru> 0.6.1a-alt1.2
- fixed buffer overflow error

* Wed Jul 01 2009 Alex Karpov <karpov@altlinux.ru> 0.6.1a-alt1.1
- fixed libs

* Fri May 08 2009 Alex Karpov <karpov@altlinux.ru> 0.6.1a-alt1
- 0.6.1 bugfix release

* Sun Jan 25 2009 Alex Karpov <karpov@altlinux.ru> 0.6-alt1
- 0.6 release

* Sun Jan 18 2009 Alex Karpov <karpov@altlinux.ru> 0.6-alt0.rc1
- new version
    + minor spec cleanup

* Tue Jun 10 2008 Alex Karpov <karpov@altlinux.ru> 0.5-alt0.1
- new version

* Thu Mar 27 2008 Alex Karpov <karpov@altlinux.ru> 0.4-alt0.1
- new version
    + updated build requirements
    + added menu macros

* Thu Nov 08 2007 Alex Karpov <karpov@altlinux.ru> 0.3-alt1
- rebuild for keyboard problem fix

* Mon Jul 30 2007 Alex Karpov <karpov@altlinux.ru> 0.3-alt0.5
- buildreq update

* Wed Jul 25 2007 Alex Karpov <karpov@altlinux.ru> 0.3-alt0.1
- initial build for Sisyphus

* Wed Jul 25 2007 Alexey Novikov <shader@yandex.ru> 0.3-alt0.M40.1
- first build

