%def_with nas
%def_with pulse
%def_with sdl

# list of audio output modules
%define mods alsa oss %{?_with_nas:nas} %{?_with_pulse:pulse} %{?_with_sdl:sdl}

Name: mpg123
Version: 1.25.12
Release: alt1

Summary: MPEG audio player
Group: Sound
License: LGPLv2.1
Url: http://www.%name.org

Source: http://downloads.sourceforge.net/%name/%name-%version.tar.bz2
Source1: mp3license

Requires: libmpg123 = %version-%release

%ifarch %ix86
%define wcpu i586
%else
%ifarch x86_64
%define wcpu x86-64
%else
%define wcpu generic
%endif
%endif

BuildRequires: libalsa-devel
%{?_with_nas:BuildRequires: libaudio-devel}
%{?_with_sdl:BuildRequires: libSDL_sound-devel libSDL-devel}
%{?_with_pulse:BuildRequires: libpulseaudio-devel}

%description
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
%url


%package -n libmpg123
Summary: mpg123 library
Group: System/Libraries
Provides: libmpg123

%description -n libmpg123
This package provides mpg123 library.

%package -n libmpg123-devel
Summary: mpg123 library headers
Group:  Development/C
Requires: libmpg123 = %version-%release

%description -n libmpg123-devel
This package provides mpg123 library headers


%prep
%setup
install -p -m644 %SOURCE1 .

%build
%autoreconf
%add_optflags %optflags_shared
%configure \
	--with-audio="%mods" \
	--with-optimization=0 \
	--enable-network=yes \
	--with-cpu=%{wcpu}
%make_build CFLAGS="%optflags -Wformat -Werror=format-security"

%install
%makeinstall_std
mkdir -p %buildroot%_defaultdocdir/%name-%version/
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README mp3license doc/

%_bindir/%name
%_bindir/%name-id3dump
%_bindir/%name-strip
%_bindir/out123
%_man1dir/%name.1.*
%_man1dir/out123.1.*
%dir %_libdir/%name
%_libdir/%name/*.so

%files -n libmpg123
%_libdir/libmpg123.so.*
%_libdir/libout123.so.*
%doc NEWS.lib%name

%files -n libmpg123-devel
%_libdir/libmpg123.so
%_libdir/libout123.so
%_pkgconfigdir/lib%name.pc
%_pkgconfigdir/libout123.pc
%_includedir/*.h


%changelog
* Sun Aug 25 2019 Yuri N. Sedunov <aris@altlinux.org> 1.25.12-alt1
- 1.25.12

* Thu Jul 18 2019 Yuri N. Sedunov <aris@altlinux.org> 1.25.11-alt1
- 1.25.11

* Thu Mar 01 2018 Yuri N. Sedunov <aris@altlinux.org> 1.25.10-alt1
- 1.25.10

* Wed Dec 06 2017 Yuri N. Sedunov <aris@altlinux.org> 1.25.8-alt1
- 1.25.8

* Thu Sep 28 2017 Yuri N. Sedunov <aris@altlinux.org> 1.25.7-alt1
- 1.25.7

* Wed Aug 16 2017 Yuri N. Sedunov <aris@altlinux.org> 1.25.6-alt1
- 1.25.6

* Fri Aug 04 2017 Yuri N. Sedunov <aris@altlinux.org> 1.25.4-alt2
- removed obsolete ExclusiveArch tag

* Tue Aug 01 2017 Yuri N. Sedunov <aris@altlinux.org> 1.25.4-alt1.2
- fixed license tag

* Tue Aug 01 2017 Michael Shigorin <mike@altlinux.org> 1.25.4-alt1.1
- BOOTSTRAP: introduce nas, pulse, sdl knobs (on by default)
- E2K: added to ExclusiveArch:

* Mon Jul 31 2017 Yuri N. Sedunov <aris@altlinux.org> 1.25.4-alt1
- 1.25.4

* Thu Jul 13 2017 Yuri N. Sedunov <aris@altlinux.org> 1.25.2-alt1
- 1.25.2 (fixed CVE-2017-11126)

* Sat Jul 08 2017 Yuri N. Sedunov <aris@altlinux.org> 1.25.1-alt1
- 1.25.1

* Wed May 31 2017 Yuri N. Sedunov <aris@altlinux.org> 1.25.0-alt1
- 1.25.0

* Wed Mar 08 2017 Yuri N. Sedunov <aris@altlinux.org> 1.24.0-alt1
- 1.24.0

* Wed Oct 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.23.8-alt1
- 1.23.8 (fixed CVE-2016-1000247)

* Thu Jul 28 2016 Yuri N. Sedunov <aris@altlinux.org> 1.23.6-alt1
- 1.23.6

* Tue May 31 2016 Yuri N. Sedunov <aris@altlinux.org> 1.23.4-alt1
- 1.23.4

* Thu Apr 07 2016 Yuri N. Sedunov <aris@altlinux.org> 1.23.3-alt1
- 1.23.3

* Wed Feb 10 2016 Yuri N. Sedunov <aris@altlinux.org> 1.23.0-alt1.1
- fixed %%files section

* Sun Feb 07 2016 Yuri N. Sedunov <aris@altlinux.org> 1.23.0-alt1
- 1.23.0
- disabled ESOUND support

* Sat Jul 11 2015 Yuri N. Sedunov <aris@altlinux.org> 1.22.2-alt1
- 1.22.2

* Wed Feb 11 2015 Yuri N. Sedunov <aris@altlinux.org> 1.21.0-alt1
- 1.21.0

* Sun Jul 27 2014 Yuri N. Sedunov <aris@altlinux.org> 1.20.1-alt1
- 1.20.1

* Mon Feb 17 2014 Yuri N. Sedunov <aris@altlinux.org> 1.18.1-alt1
- 1.18.1

* Sat Feb 01 2014 Yuri N. Sedunov <aris@altlinux.org> 1.18.0-alt1
- 1.18.0

* Fri Jan 17 2014 Yuri N. Sedunov <aris@altlinux.org> 1.17.0-alt1
- 1.17.0

* Thu Feb 14 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.13.4-alt2
- build for arm too

* Wed Dec 21 2011 Alexey Morsov <swi@altlinux.ru> 1.13.4-alt1
- new version

* Wed Mar 30 2011 Alexey Morsov <swi@altlinux.ru> 1.13.2-alt1
- new version

* Fri Oct 29 2010 Alexey Morsov <swi@altlinux.ru> 1.12.5-alt1
- new version
- build with pulse support

* Wed Jul 21 2010 Alexey Morsov <swi@altlinux.ru> 1.12.3-alt1
- new version

* Sun Jul 04 2010 Alexey Morsov <swi@altlinux.ru> 1.12.2-alt1
- new version

* Fri May 07 2010 Alexey Morsov <swi@altlinux.ru> 1.12.1-alt1
- new version

* Sun Dec 06 2009 Alexey Morsov <swi@altlinux.ru> 1.10-alt1
- new version

* Mon Sep 14 2009 Alexey Morsov <swi@altlinux.ru> 1.9.0-alt1
- new version

* Wed Jun 17 2009 Alexey Morsov <swi@altlinux.ru> 1.8.1-alt1
- new version

* Thu Apr 30 2009 Alexey Morsov <swi@altlinux.ru> 1.7.2-alt1
- remove conflict on kdemultimedia-arts

* Tue Apr 21 2009 Alexey Morsov <swi@altlinux.ru> 1.7.2-alt0.1
- new version
- fix spec (optimization is chosen depending on the architecture)

* Tue Mar 31 2009 Alexey Morsov <swi@altlinux.ru> 1.7.0-alt0.1
- new version
- remove local libltdl (use external)
- remove optimization
- set optimization to i386 (textrel)

* Wed Jan 14 2009 Alexey Morsov <swi@altlinux.ru> 1.6.4-alt0.1
- new version

* Thu Nov 06 2008 Alexey Morsov <swi@altlinux.ru> 1.6.0-alt0.1
- new version

* Sun Jan 06 2008 Alexey Morsov <swi@altlinux.ru> 1.0.1-alt1
- 1.0.1
- fixed bug with crash when current work directory name > 49 chars.

* Mon Dec 24 2007 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt0.1
- 1.0.0
- remove patch (no such file)
- adding a re-born decoder library to replace the old mpglib
  (libmpg123) and support for run-time audio .output selection

* Sat Jun 16 2007 Alexey Morsov <swi@altlinux.ru> 0.66-alt0.1
- version 0.66
- remove most of patches (allready in upstream)
- regenerate 1 patche (-8bit) for new source tree
- fix build and install section (now upstrean use configure)
- add BuildRequires for libaudio and libalsa

* Sat Mar 04 2006 Anton Farygin <rider@altlinux.ru> 0.59s-alt0.9
- NMU: fix build for x86_64

* Wed Sep 08 2004 Alexey Tourbin <at@altlinux.ru> 0.59s-alt0.8
- fixed buffer overflow in layer2 decoder (CAN-2004-0805)

* Thu Sep 25 2003 Alexey Tourbin <at@altlinux.ru> 0.59s-alt0.7
- security update (heap corruption in httpget.c)

* Tue Sep 23 2003 Alexey Tourbin <at@altlinux.ru> 0.59s-alt0.6
- build without esd by default (-a options works, #2981)

* Thu Aug 21 2003 Alexey Tourbin <at@altlinux.ru> 0.59s-alt0.5
- memory leak fixed (#0002810)
- esd support restored
- IPv6 support enabled

* Mon Aug 04 2003 Alexey Tourbin <at@altlinux.ru> 0.59s-alt0.4
- security update (CAN-2003-0577)

* Sun Jun 15 2003 Alexey Tourbin <at@altlinux.ru> 0.59s-alt0.3
- some PLD patches applied
- some heavy optimization options dropped
- some bugs disappeared, after all :-/

* Thu Oct 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.59s-alt0.2
- Rebuilt in new environment

* Fri Oct 12 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.59s-alt0.1
- pre059s
- Added some Arch-dependent optimizations

* Wed Feb 28 2001 Konstantin Volckov <goldhead@linux.ru.net> 0.59r-ipl2mdk
- Added 3dNOW patch by Takuhiro KIMURA
- Fixed esd building

* Thu Dec 14 2000 Dmitry V. Levin <ldv@fandra.org> 0.59r-ipl1mdk
- RE adaptions.

* Sat Nov 27 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Mon Nov 15 1999 Lenny Cartier <lenny@mandrakesoft.com>
- v0.59r

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Wed Apr 07 1999 Preston Brown <pbrown@redhat.com>
- removed debug output from audio_esd.c.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 5)

* Wed Mar 17 1999 Michael Fulbright <drmike@redhat.com>
- hacked to work with esd for 8 bit fallback

* Sat Mar  6 1999 Matt Wilson <msw@redhat.com>
- rebuilt against new libaudio and esd

* Mon Mar  1 1999 Matt Wilson <msw@redhat.com>
- rebuilt against new libaudio and esd

* Fri Feb 26 1999 Michael Maher <mike@redhat.com>
- update package

* Tue Jan 12 1999 Michael Maher <mike@redhat.com>
- allowed to ship ... finally.

* Wed Jan 21 1998 Otto Hammersmith <otto@redhat.com>
- more cleanup
