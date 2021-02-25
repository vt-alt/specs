Name: alsa-plugins
Version: 1.2.2
Release: alt2
Epoch: 1

Summary: Advanced Linux Sound Architecture (ALSA) plugins
License: LGPLv2.1+
Group: System/Libraries

Url: http://www.alsa-project.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ libalsa-devel libavcodec-devel libdbus-devel
BuildRequires: libpulseaudio-devel libsamplerate-devel libspeex-devel libspeexdsp-devel

%define _unpackaged_files_terminate_build 1

Summary(ru_RU.UTF-8): Плагины ALSA
Summary(uk_UA.UTF-8): Плагіни ALSA

%description
Advanced Linux Sound Architecture (ALSA) plugins.

%description -l ru_RU.UTF-8
Этот пакет содержит плагины ALSA.

%description -l uk_UA.UTF-8
Цей пакунок містить плагіни ALSA.

%package pulse
Summary: ALSA pulseaudio plugin
Group: Sound
Requires: libalsa >= 1.0.21a
Requires: pulseaudio-daemon

%description pulse
ALSA pulseaudio plugin

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

# drop unneeded files
find %buildroot%_libdir/alsa-lib/ -name '*.la' -delete

# install configs from Debian
install -D pulse-alsa.conf %buildroot%_datadir/alsa/pulse-alsa.conf
install -D pulse.conf %buildroot%_datadir/alsa/alsa.conf.d/99-pulse.conf

# turn symlinks into relative ones
find %buildroot%_sysconfdir/alsa/conf.d/ -type l -delete
for i in %buildroot%_datadir/alsa/alsa.conf.d/*.conf; do
	ln -sr "$i" %buildroot%_sysconfdir/alsa/conf.d/
done

%files
# I know of README-pulse, too much hassle with merging docdirs
%doc doc/*.txt doc/README-*
%config(noreplace) %_sysconfdir/alsa/conf.d/*.conf
%exclude %_sysconfdir/alsa/conf.d/*pulse*.conf
%_datadir/alsa/alsa.conf.d/*.conf
%exclude %_datadir/alsa/alsa.conf.d/*pulse*.conf
%_libdir/alsa-lib/*.so
%exclude %_libdir/alsa-lib/*pulse*.so

%files pulse
%_libdir/alsa-lib/*pulse*.so
%_sysconfdir/alsa/conf.d/99-pulseaudio-default.conf.example
%_sysconfdir/alsa/conf.d/50-pulseaudio.conf
%_sysconfdir/alsa/conf.d/99-pulse.conf
%_datadir/alsa/pulse-alsa.conf
%_datadir/alsa/alsa.conf.d/50-pulseaudio.conf
%_datadir/alsa/alsa.conf.d/99-pulse.conf

%changelog
* Mon Feb 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.2.2-alt2
- Imported config files from Debian for alsa-plugins-pulse.
  Upstream config 50-pulseaudio.conf alone sometimes isn't enough.

* Thu Feb 20 2020 Michael Shigorin <mike@altlinux.org> 1:1.2.2-alt1
- 1.2.2

* Mon Nov 18 2019 Michael Shigorin <mike@altlinux.org> 1:1.2.1-alt1
- 1.2.1
- actually package plugin configuration files
- dropped pulse.conf in favour of upstream 50-pulseaudio.conf

* Mon May 13 2019 Michael Shigorin <mike@altlinux.org> 1:1.1.9-alt1
- 1.1.9

* Thu Jan 24 2019 Michael Shigorin <mike@altlinux.org> 1:1.1.8-alt1
- 1.1.8

* Wed Oct 17 2018 Michael Shigorin <mike@altlinux.org> 1:1.1.7-alt1
- 1.1.7

* Mon Jun 25 2018 Anton Farygin <rider@altlinux.ru> 1:1.1.6-alt2
- rebuilt for ffmpeg-4

* Wed Apr 04 2018 Michael Shigorin <mike@altlinux.org> 1:1.1.6-alt1
- 1.1.6

* Wed Nov 22 2017 Michael Shigorin <mike@altlinux.org> 1:1.1.5-alt1
- 1.1.5

* Sat Jun 03 2017 Anton Farygin <rider@altlinux.ru> 1:1.1.4-alt3
- rebuild with debuginfo-enabled ffmpeg

* Sat Jun 03 2017 Anton Farygin <rider@altlinux.ru> 1:1.1.4-alt2
- rebuild with ffmpeg-3.3.1

* Mon May 29 2017 Michael Shigorin <mike@altlinux.org> 1:1.1.4-alt1
- 1.1.4

* Mon Jun 20 2016 Michael Shigorin <mike@altlinux.org> 1:1.1.1-alt1
- 1.1.1

* Mon Nov 30 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.1.0-alt1.1
- NMU: added BR: libspeexdsp-devel

* Mon Nov 09 2015 Michael Shigorin <mike@altlinux.org> 1:1.1.0-alt1
- 1.1.0

* Fri Feb 27 2015 Michael Shigorin <mike@altlinux.org> 1:1.0.29-alt2
- added 50-pulseaudio.conf
- converted spec to UTF-8

* Fri Feb 27 2015 Michael Shigorin <mike@altlinux.org> 1:1.0.29-alt1
- 1.0.29

* Wed Jun 18 2014 Michael Shigorin <mike@altlinux.org> 1:1.0.28-alt1
- 1.0.28

* Fri May 30 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.0.27-alt3
- rebuilt with libav10

* Sat Apr 13 2013 Michael Shigorin <mike@altlinux.org> 1:1.0.27-alt2
- retag

* Sat Apr 13 2013 Michael Shigorin <mike@altlinux.org> 1:1.0.27-alt1
- 1.0.27

* Fri Sep 07 2012 Michael Shigorin <mike@altlinux.org> 1:1.0.26-alt2
- retag

* Thu Sep 06 2012 Michael Shigorin <mike@altlinux.org> 1:1.0.26-alt1
- 1.0.26
- moved pulse.conf:
  from %_datadir/alsa/pulse.conf
    to %_datadir/alsa/alsa.conf.d/pulse.conf

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.24-alt2.1
- Fixed build with new glibc

* Fri Sep 09 2011 Michael Shigorin <mike@altlinux.org> 1:1.0.24-alt2
- rebuilt against libva
- merged spec with my old 1.0.22-alt1

* Wed Feb 16 2011 Michael Shigorin <mike@altlinux.org> 1:1.0.24-alt1
- 1.0.24

* Sun Apr 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.23-alt1
- 1.0.23

* Thu Dec 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.22-alt1
- 1.0.22

* Tue Sep 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.21-alt1
- 1.0.21
- new subpackage %name-pulse (closes: #21534)

* Tue Jul 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.20-alt4
- rebuild with libavutil.so.50

* Mon Jul 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.20-alt3
- disabled jack plugin

* Sun May 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.20-alt2
- rebuild

* Thu May 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.20-alt1
- 1.0.20

* Thu Feb 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.19-alt2
- rebuild with libavcodec.so.52

* Mon Jan 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.19-alt1
- 1.0.19

* Wed Oct 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.18-alt1
- 1.0.18

* Wed Jul 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17-alt1
- 1.0.17

* Thu May 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.16-alt1
- 1.0.16

* Sun Jan 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.15-alt1
- 1.0.15
- spec cleanup
- update build dependencies

* Mon Jun 11 2007 Michael Shigorin <mike@altlinux.org> 1.0.14-alt1
- 1.0.14
- fixed install
- set _unpackaged_files_terminate_build

* Mon Oct 16 2006 Michael Shigorin <mike@altlinux.org> 1.0.13-alt1
- 1.0.13

* Tue Sep 05 2006 Igor Zubkov <icesik@altlinux.ru> 1.0.12-alt2
- NMU
- add PulseAudio support (polypaudio removed)

* Sun Sep 03 2006 Michael Shigorin <mike@altlinux.org> 1.0.12-alt1
- 1.0.12
- changed BuildPreReq: kernel-headers-std to linux-libc-headers
- fixed README-polyp being renamed

* Wed May 31 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt5
- rebuilt against libpolyp-0.9

* Sat Apr 29 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt4
- accepted changes by icesik@
- minor cleanup

* Fri Apr 28 2006 Igor Zubkov <icesik@altlinux.ru> 1.0.11-alt3
- NMU
- real fix #9447
- buildreq
- add packager tag
- add docs

* Thu Apr 27 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt2
- fix #9447 (polypaudio support), thanks icesik@
- remove (unpackaged) *.la

* Wed Apr 19 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt1
- 1.0.11

* Wed Apr 05 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt0.4
- 1.0.11rc4
- minor spec cleanup

* Wed Nov 16 2005 Michael Shigorin <mike@altlinux.org> 1.0.10-alt1
- 1.0.10

* Thu Jun 23 2005 Michael Shigorin <mike@altlinux.org> 1.0.9-alt1
- 1.0.9

* Thu Jun 09 2005 Michael Shigorin <mike@altlinux.ru> 1.0.9-alt0
- built for ALT Linux
