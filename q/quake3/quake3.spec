%define _user _q3
%define _group _q3
%define _home %_localstatedir/%name

%define revision 2349

%define __arch %_arch
%ifarch %ix86
%define __arch i386
%endif

Name: quake3
Version: 1.36
Release: alt3.svn%revision

Summary: Quake 3: Arena by ID Software
License: GPL
Group: Games/Arcade
Url: http://ioquake3.org

Source0: ioquake3-r%revision.tar.bz2

Source1: quake3.desktop
Source2: quake3.png

Source10: quake3.init
Source11: quake3.sysconfig
Source12: quake3-ctf.init
Source13: quake3-ctf.sysconfig

Patch0: quake3-alt-aarch64.patch

Packager: Igor Zubkov <icesik@altlinux.org>

Requires: %name-server = %version-%release
Requires: %name-common = %version-%release

# Automatically added by buildreq on Tue Nov 27 2012
# optimized out: libGL-devel libGLU-devel libogg-devel pkg-config
BuildRequires: libSDL-devel libcurl-devel libopenal-devel libspeex-devel libvorbis-devel zlib-devel libspeexdsp-devel

Obsoletes: quake3-client-up
Provides: quake3-client-up = %version-%release

Obsoletes: quake3-client-smp
Provides: quake3-client-smp = %version-%release

Obsoletes: quake3-client
Provides: quake3-client = %version-%release

%description
Quake 3: Arena by ID Software.

%description -l ru_RU.UTF-8
Quake 3: Arena by ID Software.
Превосходная 3D-стрелялка.

%package common
Group: Games/Arcade
Summary: Common files for Quake 3: Arena

%description common
Quake 3: Arena by ID Software.
This package contains common files.

%description common -l ru_RU.UTF-8
Quake 3: Arena by ID Software.
Этот пакет содержит общие файлы, используемые в других пакетах quake3.

%package server
Group: Games/Arcade
Summary: Quake 3: Arena dedicated server package
Requires: %name-common = %version-%release

%description server
Quake 3: Arena by ID Software.
Dedicated server.

%description server -l ru_RU.UTF-8
Quake 3: Arena by ID Software.
Выделенный сервер.

%prep
%setup -q -n ioquake3
%patch -p2

#rm -rf code/zlib code/libspeex

rm -rf `find -name .svn` code/AL code/SDL12 code/libcurl code/libs
rm -rf code/zlib code/libspeex

# rm -rf code/jpeg-8c code/tools/lcc

%build
%make_build release V=1 \
    BUILD_CLIENT_SMP=1 \
    USE_LOCAL_HEADERS=0 \
    USE_CODEC_VORBIS=1 \
    USE_INTERNAL_SPEEX=0 \
    USE_INTERNAL_ZLIB=0

%install
mkdir -p %buildroot%_bindir/

install -p -D -m644 %SOURCE1 %buildroot%_datadir/applications/%name.desktop

cat << __EOF__ > %buildroot%_bindir/quake3
#!/bin/sh

%_libdir/quake3/ioquake3.%__arch +set sv_pure 0 +set vm_cgame 0 +set vm_game 0 +set vm_ui 0 $@
__EOF__

chmod +x %buildroot%_bindir/quake3
ln -sf %_libdir/quake3/ioq3ded.%__arch %buildroot%_bindir/q3ded

install -D -p -m 0644 %SOURCE2 %buildroot%_miconsdir/quake3.png

mkdir -p %buildroot%_libdir/quake3/baseq3/
make copyfiles COPYDIR="%buildroot%_libdir/quake3" V=1 \
    BUILD_CLIENT_SMP=1 \
    USE_LOCAL_HEADERS=0 \
    USE_CODEC_VORBIS=1 \
    USE_INTERNAL_SPEEX=0 \
    USE_INTERNAL_ZLIB=0

cat > README.ALT <<EOF
In order to actually play the game, you will need pak-files from original game
CD (pak0.pk3) plus pak-files from latest quake3 point release! Put them into
%_libdir/quake3/baseq3/!
EOF

# initscript for dedicated server
install -pDm0755 %SOURCE10 %buildroot%_initdir/%name
install -pDm0755 %SOURCE12 %buildroot%_initdir/%name-ctf
install -pDm0644 %SOURCE11 %buildroot%_sysconfdir/sysconfig/%name
install -pDm0644 %SOURCE13 %buildroot%_sysconfdir/sysconfig/%name-ctf

install -dm1700 %buildroot%_home/

%pre server
/usr/sbin/groupadd -r -f %_group ||:
/usr/sbin/useradd -g %_group -c 'The quake3 user' \
        -d %_home -s /dev/null -r %_user >/dev/null 2>&1 ||:

%post
echo "In order to actually play the game, you'll need pak-files from original game CD (pak0.pk3) plus pak-files from latest quake3 point release! Put them into %_libdir/quake3/baseq3/ or ~/.q3a/baseq3/ ! "

%post server
%post_service %name
%post_service %name-ctf
echo "In order to actually play the game, you'll need pak-files from original game CD (pak0.pk3) plus pak-files from latest quake3 point release! Put them into %_libdir/quake3/baseq3/ or ~/.q3a/baseq3/ ! "

%preun server
%preun_service %name
%preun_service %name-ctf

%files
%doc BUGS ChangeLog NOTTODO README README.ALT TODO id-readme.txt md4-readme.txt rend2-readme.txt voip-readme.txt
%_bindir/%name
%_libdir/quake3/ioquake3.%__arch
%_libdir/quake3/renderer_opengl1_%__arch.so
%_libdir/quake3/renderer_opengl1_smp_%__arch.so
%_libdir/quake3/renderer_rend2_%__arch.so
%_datadir/applications/quake3.desktop
%_miconsdir/*.png

%files common
%dir %_libdir/quake3/
%dir %_libdir/quake3/baseq3/
%_libdir/quake3/baseq3/cgame%__arch.so
%_libdir/quake3/baseq3/qagame%__arch.so
%_libdir/quake3/baseq3/ui%__arch.so
%dir %_libdir/quake3/missionpack/
%_libdir/quake3/missionpack/cgame%__arch.so
%_libdir/quake3/missionpack/qagame%__arch.so
%_libdir/quake3/missionpack/ui%__arch.so

%files server
%doc BUGS ChangeLog NOTTODO README README.ALT TODO id-readme.txt md4-readme.txt rend2-readme.txt voip-readme.txt
%_initdir/*
%_bindir/q3ded
%_libdir/quake3/ioq3ded.%__arch
%config(noreplace) %_sysconfdir/sysconfig/*
%dir %attr(1770,root,%_group) %_home

%changelog
* Sat Sep 28 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.36-alt3.svn2349
- Fixed build on ppc64le and aarch64 architectures.

* Mon Nov 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.36-alt2.svn2349
- NMU: added BR: libspeexdsp-devel

* Thu Jan 17 2013 Igor Zubkov <icesik@altlinux.org> 1.36-alt1.svn2349
- Bump version

* Sun Nov 25 2012 Igor Zubkov <icesik@altlinux.org> 1.34-alt12.svn2349
- Remove quake3-alt-bug14027.patch
- Move %%_libdir/games/quake3/ -> %%_libdir/quake3/
- Build and link with system zlib
- Build and link with system libspeex
- Build with Ogg Vorbis support

* Sun Nov 25 2012 Igor Zubkov <icesik@altlinux.org> 1.34-alt11.svn2349
- svn1114 -> 2349
- Merge quake3-client-up and quake3-client-smp to quake3

* Wed Oct 31 2012 Igor Zubkov <icesik@altlinux.org> 1.34-alt10.svn1114
- convert spec to UTF-8
- buildreq

* Sun Apr 10 2011 Lenar Shakirov <snejok@altlinux.ru> 1.34-alt9.svn1114
- Fixed build: BuildReqs: libmesa-devel -> libGL-devel
- Desktop file fixed and cleaned: thanks to repocop!

* Sun Nov 08 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.34-alt8.svn1114.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for quake3-client-smp
  * pixmap-in-deprecated-location for quake3
  * update_menus for quake3-client-up
  * postclean-05-filetriggers for spec file

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt8.svn1114
- Fix #16247, thanks vvk@.

* Mon Jan 28 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt7.svn1114
- Fix #14027.

* Tue Dec 04 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt6.svn1114
- Merged vvk@'s initscripts for server side.

* Mon Jul 16 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt5.svn1114
- 1114 revision.
- Fixed launching.

* Tue Apr 10 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt4.svn1062
- Modified smp-desktop file to be able to launch SMP version.

* Tue Apr 10 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt3.svn1062
- 1062 revision.

* Thu Feb 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt3.svn1046
- Added requires: client-*, server to quake3 package.

* Sun Feb 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt2.svn1046
- 1046 svn revision.
- Fixed symlinks.

* Mon Jan 29 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt2.svn1037
- 1037 svn revision.
- Gearified package.
- Added freedesktop menu files.
- Fixed Requires for common package.
- Fixed Provides for -client-smp package.
- Rewrote descriptions and summaries.
- Make common package own directories in %%_libdir/games/.
- Minor spec cleanup.
- Removed xorg-x11-devel from BuildRequires,
  Added libXt-devel and libmesa-devel to BuildRequires instead.
- Added icon.
- Added README.ALT concerning running the program.
- Removed gcc3.4 build-dependancy.
- Fixed URL.
- Rewrote install section using quake3 own Makefile directives.
- Moved binaries to %%_libdir/games/quake3.

* Wed Nov 01 2006 Igor Zubkov <icesik@altlinux.org> 1.34-alt1.svn956
- new version (#10073)
- rename quake3-client to quake3-client-up (#7811)
- add provides quake3-client to quake3-client-up and quake3-client-smp (#7811)
- add docs (#7810)
- use gcc 3.4 for build

* Tue Oct 31 2006 Alexey Shabalin <shaba@altlinux.ru> 1.34-alt0.1svn956
- svn 956
- fix spec for build x86_64
- move clients and server to %_bindir
- fix menu files

* Thu Oct 19 2006 Afanasov Dmitry <ender@atrus.ru> svn916-alt1
- svn rebuild

* Fri Aug 26 2005 Igor Zubkov <icesik@altlinux.ru> 1.32b-alt1
- Initial build for Sisyphus

