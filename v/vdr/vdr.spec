Name: vdr
Version: 2.2.0
Release: alt8

Summary: Digital satellite receiver box with advanced features
License: GPLv2
Group: Video
Url: http://www.tvdr.de

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ fontconfig-devel
BuildRequires: libalsa-devel libbluray-devel libcap-devel libncursesw-devel
BuildRequires: libfreetype-devel libjpeg-devel libssl-devel libudev-devel
BuildRequires: libGraphicsMagick-c++-devel libxine2-devel libzvbi-devel
BuildRequires: libGL-devel libGLU-devel libglut-devel libX11-devel libXext-devel
BuildRequires: libXinerama-devel libXrandr-devel libXrender-devel libXv-devel
BuildRequires: boost-devel libtntnet-devel libtntdb-devel libdbus-glib-devel perl-Date-Manip
BuildRequires: libcurl-devel libcxxtools-devel libpcrecpp-devel
# vaapidevice
BuildRequires: pkgconfig(libva) pkgconfig(libavcodec) pkgconfig(libswscale) pkgconfig(libswresample)
BuildRequires: pkgconfig(x11) pkgconfig(x11-xcb) pkgconfig(xcb) pkgconfig(xcb-icccm) pkgconfig(xcb-screensaver)
BuildRequires: pkgconfig(xcb-dpms)

%description
VDR, Video Disc Recorder, enables you to build a powerful set-top box on your own
using Linux and a DVB card. It incorporates basic features, such as watching TV,
recording and time-shifting, plus advanced features, including MP3/Ogg playback,
playback of all video formats supported by MPlayer and backup of the recorded
material to MPEG-4, video CD or DVD.

%package devel
Summary: Development part of VDR
Group: Development/C

%package plugin-sc
Summary: VDR softcam plugin
Group: Video
Requires: vdr = %version-%release

%package plugin-enigmang
Summary: VDR theme
Group: Video
Requires: vdr = %version-%release

%package plugin-epgsync
Summary: VDR EPG sync plugin
Group: Video
Requires: vdr = %version-%release

%package plugin-femon
Summary: VDR femon plugin
Group: Video
Requires: vdr = %version-%release

%package plugin-iptv
Summary: VDR IPTV plugin
Group: Video
Requires: vdr = %version-%release

%package plugin-live
Summary: VDR LIVE plugin
Group: Video
Requires: vdr = %version-%release

%package plugin-manager
Summary: VDR manager plugin
Group: Video
Requires: vdr = %version-%release

%package plugin-pvrinput
Summary: VDR pvrinput plugin
Group: Video
Requires: vdr = %version-%release

%package plugin-remoteosd
Summary: VDR remote OSD plugin
Group: Video
Requires: vdr = %version-%release

%package plugin-remotetimers
Summary: VDR remote timers plugin
Group: Video
Requires: vdr = %version-%release

%package plugin-vaapidevice
Summary: VDR HD-capable ffmpeg plugin
Group: Video
Requires: vdr = %version-%release

%package plugin-streamdev
Summary: VDR streamdev plugin
Group: Video
Requires: vdr = %version-%release

%package plugin-text2skin
Summary: VDR skin rendering plugin
Group: Video
Requires: vdr = %version-%release

%package plugin-ttxtsubs
Summary: VDR teletext subtitles plugin
Group: Video
Requires: vdr = %version-%release

%package plugin-vnsiserver
Summary: VDR Network StreamingInterface
Group: Video
Requires: vdr = %version-%release

%package plugin-wirbelscan
Summary: VDR wirbelscan plugin
Group: Video
Requires: vdr = %version-%release

%package plugin-xineliboutput
Summary: VDR X11 and framebuffer frontend
Group: Video
Requires: vdr = %version-%release

%package plugin-xine
Summary: Xine plugins for use with VDR frontends
Group: Video

%package fbfe
Summary: VDR framebuffer frontend
Group: Video
Requires: vdr-plugin-xine = %version-%release
 
%package sxfe
Summary: VDR X11 frontend
Group: Video
Requires: vdr-plugin-xine = %version-%release

%description devel
Header and pkgconfig files of VDR

%description plugin-sc
Softcam plugin  for the Video Disk Recorder (VDR).

%description plugin-enigmang
EnigmaNG standalone skin for the Video Disk Recorder (VDR).

%description plugin-epgsync
imports EPG data from remote VDR server

%description plugin-femon
DVB Frontend Status Monitor plugin for the Video Disk Recorder (VDR).

%description plugin-iptv
IPTV plugin for the Video Disk Recorder (VDR).

%description plugin-live
Live Interactive VDR Environment -- web inteface for the Video Disk Recorder (VDR).

%description plugin-manager
Manager plugin for the Video Disk Recorder (VDR).

%description plugin-pvrinput
Analog PVR-like cards (ivtv, cx18 etc) support for the Video Disk Recorder (VDR).

%description plugin-remoteosd
Remote OSD plugin for the Video Disk Recorder (VDR).

%description plugin-remotetimers
VDR timers manipulations across VDR instances

%description plugin-vaapidevice
HD-capable (VDPAU) softdevice plugin for the Video Disk Recorder (VDR).

%description plugin-streamdev
Streaming server and client plugins for the Video Disk Recorder (VDR).

%description plugin-text2skin
Plugin designed to load and interpret a set of files describing the
layout of the On Screen Display.

%description plugin-ttxtsubs
Teletext subtitles plugin for the Video Disk Recorder (VDR).

%description plugin-vnsiserver
Network streaming interface for the Video Disk Recorder (VDR).

%description plugin-wirbelscan
This plugin performs a channel scans for digital terrestrial and digital
cable TV and analog ivtv cards, satellite is also supported.

%description plugin-xineliboutput
X11 and Linux framebuffer front-end for VDR.
Plugin displays video and OSD in X/Xv/XvMC window or framebuffer.
Support for local and remote frontends.
Built-in image and media player supports playback of most known 
media files (avi/mp3/divx/jpeg/...), DVDs and radio/video streams
(http, rtsp, ...) directly from VDR.

%description fbfe
Linux framebuffer front-end for VDR.

%description sxfe
X11 front-end for VDR.

%description plugin-xine
Additional Xine plugins for use with VDR frontends.

%define docdir		%_defaultdocdir/%name-%version
%define	confdir		%_sysconfdir/vdr
%define	plugindir	%_libdir/vdr
%define	resdir		%_datadir/vdr
%define videodir	%_localstatedir/vdr

%prep
%setup
sed -e 's,^#PREFIX.\+$,PREFIX = %prefix,' \
    -e 's,^#BINDIR.\+$,BINDIR = %_bindir,' \
    -e 's,^#INCDIR.\+$,INCDIR = %_includedir,' \
    -e 's,^#LIBDIR.\+$,LIBDIR = %plugindir,' \
    -e 's,^#LOCDIR.\+$,LOCDIR = %_datadir/locale,g' \
    -e 's,^#MANDIR.\+$,MANDIR = %_mandir,' \
    -e 's,^#PCDIR.\+$,PCDIR = %_pkgconfigdir,' \
    -e 's,^#RESDIR.\+$,RESDIR = %resdir,g' \
    -e 's,^#VIDEODIR.\+$,VIDEODIR = %videodir,g' \
    -e 's,^#CONFDIR.\+$,CONFDIR = %confdir,g' \
    -e 's,^#CACHEDIR.\+$,CACHEDIR = %_cachedir/vdr,g' \
    -e 's,^\(CFLAGS[[:blank:]]\+[^[:blank:]]\+[[:blank:]]\+\)\(.\+$\),\1%optflags \2,' \
    -e 's,^\(CXXFLAGS[[:blank:]]\+[^[:blank:]]\+[[:blank:]]\+\)\(.\+$\),\1%optflags \2,' \
    < Make.config.template > Make.config

sed -i 's,^IMAGELIB.\+$,IMAGELIB = graphicsmagick,' PLUGINS/src/text2skin/Makefile

%build
(cd PLUGINS/src/xineliboutput && sh configure  --disable-opengl)

%make_build

%install
make install DESTDIR=%buildroot

mkdir -p %buildroot%docdir %buildroot%confdir/plugins %buildroot%confdir/themes
cp -p CONTRIBUTORS HISTORY INSTALL MANUAL PLUGINS.html README* UPDATE* %buildroot%docdir

mkdir -p %buildroot%docdir/sc %buildroot%confdir/plugins/sc
cp -p PLUGINS/src/sc/README* %buildroot%docdir/sc
cp -a PLUGINS/src/sc/examples %buildroot%docdir/sc

mkdir -p %buildroot%docdir/enigmang %buildroot%confdir/plugins/skinenigmang
cp -p PLUGINS/src/enigmang/README %buildroot%docdir/enigmang
cp -p PLUGINS/src/enigmang/themes/* %buildroot%confdir/themes/

mkdir -p %buildroot%docdir/epgsync
cp -p PLUGINS/src/epgsync/README %buildroot%docdir/epgsync

mkdir -p %buildroot%docdir/femon
cp -p PLUGINS/src/femon/README %buildroot%docdir/femon

mkdir -p %buildroot%docdir/iptv
cp -p PLUGINS/src/iptv/README %buildroot%docdir/iptv

mkdir -p %buildroot%docdir/live %buildroot%confdir/plugins/live
cp -p PLUGINS/src/live/README %buildroot%docdir/live
cp -a PLUGINS/src/live/live %buildroot%resdir/plugins

mkdir -p %buildroot%docdir/manager %buildroot%confdir/plugins/manager
cp -p PLUGINS/src/manager/README %buildroot%docdir/manager
touch %buildroot%confdir/plugins/manager/vdrmanager.conf

mkdir -p %buildroot%docdir/pvrinput
cp -p PLUGINS/src/pvrinput/{FAQ,HISTORY,README} %buildroot%docdir/pvrinput

mkdir -p %buildroot%docdir/remoteosd
cp -p PLUGINS/src/remoteosd/README %buildroot%docdir/remoteosd

mkdir -p %buildroot%docdir/svdrposd
cp -p PLUGINS/src/svdrposd/README %buildroot%docdir/svdrposd

mkdir -p %buildroot%docdir/svdrpservice
cp -p PLUGINS/src/svdrpservice/README %buildroot%docdir/svdrpservice

mkdir -p %buildroot%docdir/remoteosd
cp -p PLUGINS/src/remoteosd/README %buildroot%docdir/remoteosd

mkdir -p %buildroot%docdir/remotetimers
cp -p PLUGINS/src/remotetimers/README %buildroot%docdir/remotetimers

mkdir -p %buildroot%docdir/vaapidevice
cp -p PLUGINS/src/vaapidevice/README %buildroot%docdir/vaapidevice

mkdir -p %buildroot%docdir/streamdev
cp -p PLUGINS/src/streamdev/{README,PROTOCOL} %buildroot%docdir/streamdev
cp -a PLUGINS/src/streamdev/streamdev-server %buildroot%confdir/plugins

mkdir -p %buildroot%docdir/text2skin %buildroot%confdir/plugins/text2skin
cp -a PLUGINS/src/text2skin/{README,Docs} %buildroot%docdir/text2skin

mkdir -p %buildroot%docdir/ttxtsubs %buildroot%confdir/plugins/ttxtsubs
cp -p PLUGINS/src/ttxtsubs/{README,TROUBLESHOOTING} %buildroot%docdir/ttxtsubs

mkdir -p %buildroot%docdir/vnsiserver
cp -p PLUGINS/src/vnsiserver/README %buildroot%docdir/vnsiserver
cp -a PLUGINS/src/vnsiserver/vnsiserver %buildroot%confdir/plugins

mkdir -p %buildroot%docdir/wirbelscan
cp -p PLUGINS/src/wirbelscan/README %buildroot%docdir/wirbelscan

make install -C PLUGINS/src/xineliboutput DESTDIR=%buildroot
mkdir -p %buildroot%docdir/xineliboutput
cp -p PLUGINS/src/xineliboutput/{README,examples/remote.conf.example} %buildroot%docdir/xineliboutput

touch %buildroot%confdir/setup.conf
install -pD -m0755 vdr.init %buildroot%_initdir/vdr
install -pD -m0644 vdr.service %buildroot%_unitdir/vdr.service
install -pD -m0644 vdr.tmpfiles %buildroot%_tmpfilesdir/vdr.conf
install -pD -m0644 vdr.sysconfig %buildroot%_sysconfdir/sysconfig/vdr
install -pm0755 contrib/xmltv2vdr/xmltv2vdr.pl %buildroot%_bindir/xmltv2vdr
install -pm0644 contrib/xmltv2vdr/README %buildroot%docdir/README.xmltv2vdr

mkdir -p %buildroot%_iconsdir
cp -a icons/* %buildroot%_iconsdir
install -pm0644 -D vdr.desktop %buildroot%_desktopdir/vdr.desktop

mkdir -p %buildroot%_runtimedir/vdr %buildroot%_cachedir/vdr

%find_lang --output=VDR.lang --append vdr vdr-hello vdr-pictures vdr-skincurses vdr-dvbsddevice vdr-dvbhddevice
%find_lang --output=sc.lang vdr-sc
%find_lang --output=enigmang.lang vdr-skinenigmang
%find_lang --output=epgsync.lang vdr-epgsync
%find_lang --output=femon.lang vdr-femon
%find_lang --output=iptv.lang vdr-iptv
%find_lang --output=live.lang vdr-live
%find_lang --output=manager.lang vdr-manager
%find_lang --output=pvrinput.lang vdr-pvrinput
%find_lang --output=vaapidevice.lang vdr-vaapidevice
%find_lang --output=streamdev.lang --append vdr-streamdev-server vdr-streamdev-client
%find_lang --output=text2skin.lang vdr-text2skin
%find_lang --output=ttxtsubs.lang vdr-ttxtsubs
%find_lang --output=remoteosd.lang --append vdr-svdrpservice vdr-remoteosd
%find_lang --output=remotetimers.lang vdr-remotetimers
%find_lang --output=vnsiserver.lang vdr-vnsiserver
%find_lang --output=wirbelscan.lang vdr-wirbelscan
%find_lang --output=xineliboutput.lang vdr-xineliboutput

mkdir -p %buildroot%_libexecdir/rpm
cat << __EOF__ > %buildroot%_libexecdir/rpm/vdr.filetrigger
#!/bin/sh -e
grep -qs '^%plugindir/' || exit 0
service vdr condrestart
__EOF__

chmod 755 %buildroot%_libexecdir/rpm/vdr.filetrigger

%pre
%_sbindir/groupadd -r -f _vdr &> /dev/null
%_sbindir/useradd -r -g _vdr -G audio,radio,video \
    -d %videodir -s /dev/null -c 'VDR User' -n _vdr &> /dev/null ||:

%post
%post_service vdr

%preun
%preun_service vdr

%files -f VDR.lang
%dir %docdir
%docdir/CONTRIBUTORS
%docdir/HISTORY
%docdir/INSTALL
%docdir/MANUAL
%docdir/PLUGINS.html
%docdir/README
%docdir/README.i18n
%docdir/README.xmltv2vdr
%docdir/UPDATE*

%dir %attr(0770,root,_vdr) %confdir
%dir %attr(0750,root,_vdr) %confdir/plugins
%dir %attr(0770,root,_vdr) %confdir/themes

%config(noreplace) %attr(0600,_vdr,_vdr) %confdir/*.conf

%_initdir/vdr
%_unitdir/vdr.service
%_tmpfilesdir/vdr.conf
%config(noreplace) %_sysconfdir/sysconfig/vdr

%_bindir/vdr
%_bindir/svdrpsend
%_bindir/xmltv2vdr

%dir %plugindir
%plugindir/libvdr-dummydevice.so.%version
%plugindir/libvdr-dvbhddevice.so.%version
%plugindir/libvdr-dvbsddevice.so.%version
%plugindir/libvdr-hello.so.%version
%plugindir/libvdr-osddemo.so.%version
%plugindir/libvdr-pictures.so.%version
%plugindir/libvdr-skincurses.so.%version
%plugindir/libvdr-status.so.%version
%plugindir/libvdr-svccli.so.%version
%plugindir/libvdr-svcsvr.so.%version
%plugindir/libvdr-svdrpdemo.so.%version
%plugindir/libvdr-rcu.so.%version
%plugindir/libvdr-epgtableid0.so.%version

%dir %resdir
%dir %resdir/plugins

%_man1dir/vdr.1*
%_man1dir/svdrpsend.1*
%_man5dir/vdr.5*

%dir %attr(0770,root,_vdr) %videodir
%dir %attr(0770,root,_vdr) %_runtimedir/vdr
%dir %attr(0770,root,_vdr) %_cachedir/vdr

%_libexecdir/rpm/vdr.filetrigger

%files devel
%_includedir/libsi
%_includedir/vdr
%_pkgconfigdir/vdr.pc

%files plugin-sc -f sc.lang
%docdir/sc
%dir %attr(0770,root,_vdr) %confdir/plugins/sc
%plugindir/libsc-cardclient-*.so.%version
%plugindir/libsc-conax-*.so.%version
%plugindir/libsc-constcw-*.so.%version
%plugindir/libsc-cryptoworks-*.so.%version
%plugindir/libsc-irdeto-*.so.%version
%plugindir/libsc-nds-*.so.%version
%plugindir/libsc-sc_conax-*.so.%version
%plugindir/libsc-sc_cryptoworks-*.so.%version
%plugindir/libsc-sc_irdeto-*.so.%version
%plugindir/libsc-sc_seca-*.so.%version
%plugindir/libsc-sc_viaccess-*.so.%version
%plugindir/libsc-sc_videoguard2-*.so.%version
%plugindir/libsc-seca-*.so.%version
%plugindir/libsc-shl-*.so.%version
%plugindir/libsc-viaccess-*.so.%version
%plugindir/libsc-dvbhddevice-*.so.%version
%plugindir/libsc-dvbsddevice-*.so.%version
%plugindir/libvdr-sc.so.%version

%files plugin-enigmang -f enigmang.lang
%docdir/enigmang
%confdir/themes/EnigmaNG*.theme
%dir %attr(0770,root,_vdr) %confdir/plugins/skinenigmang
%plugindir/libvdr-skinenigmang.so.%version

%files plugin-epgsync -f epgsync.lang
%docdir/epgsync
%plugindir/libvdr-epgsync.so.%version

%files plugin-femon -f femon.lang
%docdir/femon
%plugindir/libvdr-femon.so.%version

%files plugin-iptv -f iptv.lang
%docdir/iptv
%plugindir/libvdr-iptv.so.%version
%resdir/plugins/iptv

%files plugin-live -f live.lang
%docdir/live
%dir %attr(0770,root,_vdr) %confdir/plugins/live
%plugindir/libvdr-live.so.%version
%resdir/plugins/live

%files plugin-manager -f manager.lang
%docdir/manager
%dir %attr(0770,root,_vdr) %confdir/plugins/manager
%config(noreplace) %attr(0600,_vdr,_vdr) %confdir/plugins/manager/*
%plugindir/libvdr-manager.so.%version

%files plugin-pvrinput -f pvrinput.lang
%docdir/pvrinput
%plugindir/libvdr-pvrinput.so.%version

%files plugin-remoteosd -f remoteosd.lang
%docdir/svdrposd
%docdir/remoteosd
%docdir/svdrpservice
%plugindir/libvdr-svdrposd.so.%version
%plugindir/libvdr-remoteosd.so.%version
%plugindir/libvdr-svdrpservice.so.%version

%files plugin-remotetimers -f remotetimers.lang
%docdir/remotetimers
%plugindir/libvdr-remotetimers.so.%version

%files plugin-vaapidevice -f vaapidevice.lang
%docdir/vaapidevice
%plugindir/libvdr-vaapidevice.so.%version

%files plugin-streamdev -f streamdev.lang
%docdir/streamdev
%dir %attr(0770,root,_vdr) %confdir/plugins/streamdev-server
%config(noreplace) %attr(0600,_vdr,_vdr) %confdir/plugins/streamdev-server/streamdevhosts.conf
%config(noreplace) %attr(0700,_vdr,_vdr) %confdir/plugins/streamdev-server/externremux.sh
%plugindir/libvdr-streamdev-server.so.%version
%plugindir/libvdr-streamdev-client.so.%version

%files plugin-text2skin -f text2skin.lang
%docdir/text2skin
%dir %attr(0770,root,_vdr) %confdir/plugins/text2skin
%plugindir/libvdr-text2skin.so.%version

%files plugin-ttxtsubs -f ttxtsubs.lang
%docdir/ttxtsubs
%dir %attr(0770,root,_vdr) %confdir/plugins/ttxtsubs
%plugindir/libvdr-ttxtsubs.so.%version

%files plugin-vnsiserver -f vnsiserver.lang
%docdir/vnsiserver
%dir %attr(0770,root,_vdr) %confdir/plugins/vnsiserver
%config(noreplace) %attr(0600,_vdr,_vdr) %confdir/plugins/vnsiserver/allowed_hosts.conf
%plugindir/libvdr-vnsiserver.so.%version

%files plugin-wirbelscan -f wirbelscan.lang
%docdir/wirbelscan
%plugindir/libvdr-wirbelscan.so.%version

%files plugin-xineliboutput -f xineliboutput.lang
%docdir/xineliboutput
%dir %attr(0770,root,_vdr) %confdir/plugins/xineliboutput
%config(noreplace) %attr(0600,_vdr,_vdr) %confdir/plugins/xineliboutput/allowed_hosts.conf
%confdir/plugins/xineliboutput/*.mpg
%plugindir/libvdr-xineliboutput.so.%version

%files fbfe
%_bindir/vdr-fbfe
%dir %plugindir
%plugindir/libxineliboutput-fbfe.so.%version

%files sxfe
%_bindir/vdr-sxfe
%dir %plugindir
%plugindir/libxineliboutput-sxfe.so.%version
%_iconsdir/hicolor/*/apps/vdr.png
%_desktopdir/vdr.desktop

%files plugin-xine
%_libdir/xine/plugins/*/post/xineplug_post_audiochannel.so
%_libdir/xine/plugins/*/post/xineplug_post_autocrop.so
%_libdir/xine/plugins/*/post/xineplug_post_swscale.so
%_libdir/xine/plugins/*/xineplug_inp_xvdr.so

%changelog
* Sun May 10 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt8
- drop unmaintained upnp plugin

* Wed Dec 11 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt7
- fix build with gcc9

* Sat Nov 24 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt6
- fix build with kernel headers >= 4.19

* Thu Nov 15 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt5
- rebuilt with recent GraphicsMagick

* Tue Nov 13 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt4
- iptv: made external utilities optional

* Mon Sep 24 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt3
- replaced softhddevice plugin with vaapidevice
- xineliboputput plugin resurrected
- live plugin updated to 2.3.1

* Tue Jul 11 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt2
- rebuilt without ffmpeg

* Sun Mar 06 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt1
- 2.2.0 released

* Tue Jun 23 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.0.7-alt1.2
- Reenabled FFdecsa testsuite on %%ix86.

* Wed Jun 17 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.0.7-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Fri Feb 20 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.7-alt1
- 2.0.7 released

* Fri Jan 02 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.6-alt3
- manager plugin added

* Sat May 10 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.6-alt2
- live plugin added
- plugins updated:
  + dummydevice 2.0.0
  + epgsync 1.0.1
  + femon 2.0.4
  + iptv 2.0.4
  + remotetimers 1.0.1
  + vnsiserver 1.0.1

* Sat Mar 22 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.6-alt1
- 2.0.6 released

* Tue Mar 18 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.4-alt2
- updated vnsi and streamdev plugins
- fixed sc plugin build on i586

* Tue Oct 29 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.4-alt1
- 2.0.4 released

* Fri Sep 13 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.3-alt1
- 2.0.3 released

* Fri May 24 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.2-alt2
- epgsync plugin added
- remotetimers plugin added
- softhddevice plugin added

* Tue May 21 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.2-alt1
- 2.0.2 released

* Sun Apr 14 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.1-alt1
- 2.0.1 released

* Sun Mar 31 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.0-alt1
- 2.0.0 released

* Sun Mar 24 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.42-alt1
- 1.7.42 released

* Wed Mar 13 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.39-alt1
- 1.7.39 released

* Sat Feb 23 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.38-alt1
- 1.7.38 released

* Tue Feb 12 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.37-alt1
- 1.7.37 released

* Mon Nov 19 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.32-alt1
- 1.7.32 released

* Sun Sep 30 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.31-alt1
- 1.7.31 released

* Mon Sep 17 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.30-alt2
- enigmang skin plugin added
- softdevice plugin resurrected
- vdr cachedir packaged

* Wed Sep 12 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.30-alt1
- 1.7.30 released

* Fri Dec 02 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.21-alt5
- xvdr plugin updated to 0.9.5
- xineliboutput plugin rebuilt with recent libbluray

* Tue Nov 15 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.21-alt4
- rebuilt with recent libxine

* Fri Nov 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.21-alt3
- rebuilt with recent libupnp

* Wed Oct 12 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.21-alt2
- reenabled dvbhddevice plugin

* Mon Oct 10 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.21-alt1
- 1.7.21 released

* Wed Aug 17 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.20-alt1
- 1.7.20 released

* Mon Jun 20 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.19-alt1
- 1.7.19 released

* Tue Apr 19 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.18-alt1
- 1.7.18 released

* Sun Nov 21 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.16-alt1
- 1.7.16 released
- upnp plugin added
- femon plugin updated to 1.7.8
- iptv plugin updated to 0.4.2
- pvrinput plugin updated to git.3a403a
- wirbelscan plugin updated to 0.0.5

* Thu Aug 19 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.14-alt6
- use GraphicsMagick for text2skin plugin

* Mon Aug 16 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.14-alt5
- vnsiserver plugin updated to svn rev.32590
- xineliboutput plugin updated to git.49b7ce
- text2skin plugin updated to 1.3.1

* Mon Aug 02 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.14-alt4
- vnsiserver plugin updated to svn rev.32024

* Sat May 29 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.14-alt3
- remove vdr req from frontends

* Sat May 29 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.14-alt2
- xineliboutput plugin splitted
- xbmc-related changes on streamdev plugin

* Mon May 24 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.14-alt1
- 1.7.14 released
- femon plugin added
- text2skin plugin added
- ttxtsubs plugin added
- vnsiserver plugin added
- wirbelscan plugin added
- xineliboutput plugin added

* Fri Jan 22 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.11-alt1
- 1.7.11 released

* Sat Jan  2 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.10-alt2
- pvrinput plugin added
- xmltv2vdr utility added

* Sun Nov 29 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.10-alt1
- 1.7.10 released

* Fri Nov 27 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.9-alt2
- sc snapshot added

* Sat Oct 10 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.9-alt1
- 1.7.9 released

* Sat Mar 22 2008 Vyacheslav Dikonov <slava@altlinux.ru> 1.4.7-alt1
- 1.4.7

* Tue Jan 02 2007 Vyacheslav Dikonov <slava@altlinux.ru> 1.4.4-alt2
- minor fixes

* Sat Nov 11 2006 Vyacheslav Dikonov <slava@altlinux.ru> 1.4.4-alt1
- patched 1.4.4 from ArVDR SVN

* Sat Mar 05 2005 Vyacheslav Dikonov <slava@altlinux.ru> 1.3.22-alt1
- 1.3.22

* Sun Feb 27 2005 Vyacheslav Dikonov <slava@altlinux.ru> 1.3.21-alt1
- 1.3.21

* Fri Nov 05 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.3.15-alt1
- 1.3.15

* Tue Oct 19 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.3.14-alt1
- 1.3.14 

* Sun Oct 17 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.3.12-alt2
- Rebuild

* Tue Oct 05 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.3.12-alt1
- 1.3.12

* Sun Apr 04 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.3.6-alt3
- techpatch substituted by femon module

* Mon Mar 22 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.3.6-alt2
- subtitles plugin support patch

* Sun Mar 21 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.3.6-alt1
- 1.3.6

* Wed Mar 17 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.3.5-alt2
- configdir patch and runvdr script update

* Wed Mar 17 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.3.5-alt1
- 1.3.5, ElchiAIO 4d

* Sat Feb 28 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.3.4-alt2
- ElchiAIO patch 4c

* Tue Feb 17 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.3.4-alt1
- 1.3.4, Translation update, tweaks and fixes

* Fri Jan 16 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.2.6-alt1
- Initial build
