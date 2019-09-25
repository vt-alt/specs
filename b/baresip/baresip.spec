Name: baresip
Version: 0.6.1
Release: alt2

Summary: Baresip is a portable and modular SIP User-Agent with audio and video support
License: BSD
Group: Communications

Url: http://www.creytiv.com/baresip.html
Source: http://www.creytiv.com/pub/baresip-%version.tar

BuildRequires: libSDL-devel libXext-devel libalsa-devel
BuildRequires: libavdevice-devel libavformat-devel libswscale-devel
BuildRequires: libgsm-devel libmpg123-devel libopus-devel
BuildRequires: libre-devel >= 0.5.3 librem-devel >= 0.4.7
BuildRequires: libpulseaudio-devel
BuildRequires: libsndfile-devel libspandsp-devel libspeex-devel libspeexdsp-devel
BuildRequires: libssl-devel libuuid-devel libv4l-devel
BuildRequires: libvpx-devel libx264-devel

%description
baresip is a bare-bones SIP user agent. It supports SIP, SDP, RTP/RTCP,
and STUN/TURN/ICE, and IPv4 and IPv6, and is RFC-compliant and has
portable C89 and C99 source code. A modular plugin architecture provides
stdio, cons, and evdev user interfaces, celt, g711, g722, gsm, ilbc, l16,
and speex audio codecs, alsa, coreaudio, gst, portaudio, oss, winwav,
and mda audio drivers, speex_pp, speex_aec, speex_resamp, and sndfile
audio filters, the avcodec video codec, avformat, quicktime, qtcapture,
v4l, and v4l2 video sources, sdl, opengl, and x11 video display drivers,
and srtp media encoding.

%prep
%setup

%build
%make_build RELEASE=1 MOD_AUTODETECT=1 PREFIX=%_prefix MOD_PATH=%_libdir/baresip/modules

%install
%makeinstall_std RELEASE=1 MOD_AUTODETECT=1 LIBDIR=%_libdir

%files
%doc docs/*
%_bindir/%name
%_libdir/%name
%_datadir/%name

%changelog
* Fri Jul 12 2019 Michael Shigorin <mike@altlinux.org> 0.6.1-alt2
- fix modpath properly

* Tue May 14 2019 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version 0.6.1 (with rpmrb script)

* Fri Dec 14 2018 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

* Fri Oct 12 2018 Vitaly Lipatov <lav@altlinux.ru> 0.5.11-alt1
- new version 0.5.11 (with rpmrb script)

* Thu Sep 13 2018 Vitaly Lipatov <lav@altlinux.ru> 0.5.10-alt1
- new version 0.5.10 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 0.5.9-alt2
- rebuild with ffmpeg 4.0

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 0.5.9-alt1
- new version 0.5.9 (with rpmrb script)

* Wed Feb 07 2018 Vitaly Lipatov <lav@altlinux.ru> 0.5.7-alt1
- new version 0.5.7 (with rpmrb script)

* Fri Nov 10 2017 Vitaly Lipatov <lav@altlinux.ru> 0.5.6-alt1
- new version 0.5.6 (with rpmrb script)

* Thu Jun 08 2017 Konstantin Kondratyuk <kondratyuk@altlinux.org> 0.5.3-alt1
- new version 0.5.3 (with rpmrb script)

* Fri Nov 18 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.20-alt1
- 0.4.20

* Thu Nov 17 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.12-alt2.qa1
- Fixed build with glibc >= 2.24.

* Wed Mar 09 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.12-alt2
- rebuilt with recent libx264

* Mon Nov 30 2015 Igor Vlasenko <viy@altlinux.ru> 0.4.12-alt1.1
- NMU: added BR: libspeexdsp-devel

* Fri Jan 02 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.12-alt1
- 0.4.12

* Mon May 26 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.10-alt1
- 0.4.10

* Tue May 13 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.2-alt5
- rebuilt with recent x264, again

* Tue Sep 10 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.2-alt4
- rebuilt with recent libx264

* Tue Mar 26 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.2-alt3
- fixed build with recent glibc

* Mon Oct 01 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.2-alt2
- revisit buildreqs and modules
- fixed module path

* Mon Sep 17 2012 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt1
- initial build for ALT Linux Sisyphus
