Name: audacity
Version: 2.3.2
Release: alt3
Summary: Cross-platform audio editor
Summary(ru_RU.UTF-8): Кроссплатформенный звуковой редактор
License: GPL
Group: Sound

Url: http://audacity.sourceforge.net/
# Source0: https://github.com/audacity/audacity/archive/Audacity-%{version}.tar.gz
# https://www.fosshub.com/Audacity.html/audacity-manual-%{version}.zip
Source0: %name-minsrc-%version.tar
Source2: %name-48x48.xpm
Source3: %name-32x32.xpm
Source4: %name-16x16.xpm
Source6: %name-%version-help-en.tar

Patch1: 0001-Fix-building-with-wxWidgets-3.1.2.patch
Patch2: 0002-Fix-Ru-translation-of-signed-and-float.patch

# Debian patches are from https://salsa.debian.org/multimedia-team/audacity/tree/master/debian/patches
# NetBSD patches are from http://ftp.netbsd.org/pub/pkgsrc/current/pkgsrc/audio/audacity/patches/
# openSUSE patches are from https://build.opensuse.org/package/show/openSUSE:Leap:15.0/audacity
# ROSA patches are from https://abf.io/import/audacity/tree/rosa2016.1
Patch20: Debian-0004-desktop.patch
Patch50: NetBSD-ALT-Session-directory-in-home.patch
Patch60: ALT-system-sbsms.patch
# maybe useful when backporting to p8
Patch130: NetBSD-ffmpeg3.patch
Patch140: Fedora-libmp3lame-default.patch
Patch170: ALT-Remove-warning-about-alpha-version.patch

# Patents on mp3 (liblame) expired in April 2017
BuildRequires: gcc-c++ libportaudio2-devel libstdc++-devel-static libfftw3-devel gettext-devel libjpeg-devel ladspa_sdk liblame-devel
BuildRequires: libflac++-devel >= 1.3.1
BuildRequires: libflac-devel >= 1.3.1
# pkconfig BuildRequires are based on ROSA's spec: https://abf.io/import/audacity/blob/rosa2016.1/audacity.spec
# and OpenSUSE's spec: https://build.opensuse.org/package/view_file/openSUSE:Leap:15.0/audacity/audacity.spec
BuildRequires: desktop-file-utils shared-mime-info
BuildRequires: libopencore-amrnb0 libopencore-amrwb0
BuildRequires: ImageMagick zip
# For Audacity 2.2.2, we need wxWidgets 3.0, built without STL, either gtk3 or gtk2
BuildRequires: libwxGTK3.1-devel >= 3.1.1-alt2
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(flac++)
BuildRequires: pkgconfig(id3tag)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(mad)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(soundtouch)
BuildRequires: pkgconfig(soxr)
BuildRequires: pkgconfig(speex)
BuildRequires: pkgconfig(suil-0)
BuildRequires: pkgconfig(twolame)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(vamp-hostsdk)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(vorbisenc)
BuildRequires: pkgconfig(vorbisfile)
BuildRequires: pkgconfig(zlib)
BuildRequires: libsbsms-devel >= 2.0.2-alt2

%description
Audacity is a program that lets you manipulate digital audio waveforms.
It imports many sound file formats, including WAV, AIFF, AU, IRCAM,
MP3, and Ogg Vorbis. It supports all common editing operations such
as Cut, Copy, and Paste, plus it will mix tracks and let you apply
plug-in effects to any part of a sound.

%description -l ru_RU.UTF-8
Audacity - программа, которая дает возможность обрабатывать звукозаписи
в цифровом виде. Она может импортировать множество аудиоформатов, в т.ч.
WAV, AIFF, AU, IRCAM, MP3, Ogg Vorbis, и поддерживает все основные
операции редактирования, такие как Вырезать, Скопировать, Вставить,
а также возможность микширования дорожек и применения эффектов,
предоставляемых подключаемыми модулями, к любой части звука.

%package manual
Summary: Audacity manual (offline install)
Group: Documentation
BuildArch: noarch

%description manual
Audacity Manual can be installed locally if preferred, or accessed
on-line if internet connection is available.

For the most up to date manual content, use the on-line manual.

%prep
%setup -n %name-src-%version

%patch1 -p1
%patch2 -p1

%patch20 -p1
%patch50 -p1
%patch60 -p1
%patch130 -p0
%patch140 -p1
%patch170 -p1

grep -Irl "libmp3lame.so" . | xargs sed -i "s/libmp3lame.so/libmp3lame.so.0/" || true
sed -i -e 's,/usr/lib/ladspa,%{_libdir}/ladspa,g' src/effects/ladspa/LadspaEffect.cpp

%build
# src/RevisionIdent.h is in src/.gitignore and may be missing, what leads to build errors, but it's empty in release tarballs
[ ! -f src/RevisionIdent.h ] && echo ' ' > src/RevisionIdent.h

%global optflags %{optflags} -fno-strict-aliasing
%ifarch mips mipsel mips32 mips64
export LDFLAGS="${LDFLAGS} -latomic"
%endif

aclocal -I m4
%autoreconf

# From SUSE's spec about PortAudio:
# 'This [using system PortAudio] would require to patch our portaudio package with "PortMixer"... an extra API that never got integrated in PortAudio'
%configure \
	--enable-sse \
	--enable-dynamic-loading=no \
	--disable-dynamic-loading \
	--enable-nyquist \
	--enable-ladspa \
	--enable-vst \
	--with-expat=system \
	--with-ffmpeg=system \
	--with-lame=system \
	--with-libflac=system \
	--with-libid3tag=system \
	--with-libmad=system \
	--with-sbsms=system \
	--with-libsndfile=system \
	--with-soundtouch=system \
	--with-libsoxr=system \
	--with-libtwolame=system \
	--with-libvamp=system \
	--with-libvorbis=system \
	--with-lv2=system \
	--with-portaudio=local \
	--with-midi=local \
	--without-xaudio \
	--with-widgetextra=local \
%ifnarch %ix86 x86_64 %e2k
	--disable-sse
%else
	--enable-sse
%endif

%make_build

%install
%makeinstall_std
[ ! -f %buildroot%_liconsdir/%name.xpm ] && install -pDm644 %SOURCE2 %buildroot%_liconsdir/%name.xpm
[ ! -f %buildroot%_niconsdir/%name.xpm ] && install -pDm644 %SOURCE3 %buildroot%_niconsdir/%name.xpm
[ ! -f %buildroot%_miconsdir/%name.xpm ] && install -pDm644 %SOURCE4 %buildroot%_miconsdir/%name.xpm
tar -xf %SOURCE6 -C %buildroot%_datadir/%name
rm -rf %buildroot%_defaultdocdir/%name
%find_lang %name

%files -f %name.lang
%doc CHANGELOG.txt CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.txt todo.txt
%_bindir/*
%_mandir/man?/*
%_iconsdir/*/*/apps/%name.*
%_liconsdir/*
%_niconsdir/*
%_miconsdir/*
%dir %_datadir/%name
%exclude %_datadir/%name/help
%_datadir/%name/*
%_datadir/applications/%name.desktop
%_datadir/mime/packages/%name.xml
%_datadir/appdata/%name.appdata.xml
%_datadir/icons/hicolor/*/apps/%name.*
%_pixmapsdir/*.xpm

%files manual
%dir %_datadir/%name
%_datadir/%name/help

%changelog
* Fri Oct 04 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.3.2-alt3
- Fix Russian translation of 'signed' and 'float' (Closes: 37238)
  PRed to upstream: https://github.com/audacity/audacity/pull/381

* Mon Aug 19 2019 Anton Midyukov <antohami@altlinux.org> 2.3.2-alt2
- fix build with wxGTK 3.1.2 (Thanks Mikhail Novosyolov)

* Thu May 14 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.3.2-alt1
- Version 2.3.2
- Fixed NetBSD-ALT-Session-directory-in-home.patch:
  this patch worked incorrectly, fixed it to really move session
  directory from /var/tmp/audacity-$USER to $HOME/.audacity-tmp
  to ensure session data consistency across reboots and after crashes;
  this directory may be overriden with AUDACITY_TMPDIR variable
- Use AUDACITY_TMPDIR env instead of TMPDIR to override session
  directory because TMPDIR is set by default to tmpfs in many cases
  what may lead to data loss
- Removed Fedora-libdir.patch, instead using sed to fix ladspa directory
- Dropped explicit -std=gnu++11 (build scripts set it by themselves)
- Set LDFLAGS as env on mipsel instead of conditional patching
  to not worry that the mipsel patch will become unappliable
  (removed ALT-link-with-libatomic.patch)

* Fri Apr 26 2019 Ivan A. Melnikov <iv@altlinux.org> 2.3.1-alt2
- Fix build on mipsel.

* Fri Apr 26 2019 Grigory Ustinov <grenka@altlinux.org> 2.3.1-alt1
- Build new version (no major changes, but (closes: #36354)).
- Cleanup changelog.

* Mon Feb 18 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.3.0-alt2.git20190217.2345
- Git master from 17.02.2019 23:45 UTC+0300 (commit e609a9d)
- Patch: remove warning that it's an alpha version from the welcome screen
  and don't recommend to install an "official" build

* Fri Jan 25 2019 Ivan A. Melnikov <iv@altlinux.org> 2.3.0-alt1.git20181205.2140.0.mips1
- Link with latomic to fix build on mipsel

* Wed Dec 05 2018 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.3.0-alt1.git20181205.2140
- New version 2.3.0 + git master from 05.12.2018 21:40 UTC+0300 (release 2.3.0 is officially buggy on Linux, so took git master)
- Now Russian translation is better than in previous versions
- Switched to no-STL wxGTK3.1 and GTK+3
- Reworked and extended build flags (now Audacity supports working with more formats) (Closes: 31852)
- Enable ffmpeg/avconv (Closes: 35366)
- Build with system libsbsms (packaged it seperately, moved audacity-2.2.2-alt-e2k-fft.patch from Audacity to libsbsms)
- Patched to move temporary files from tmpfs /tmp/.private/ to persistend storage in HOME
- Added built-in icons to RPM files list
- Install ALT's icons only if there are no upstream ones
- Install more docs & don't install docs for bundled statically linked libraries

* Fri Nov 23 2018 Grigory Ustinov <grenka@altlinux.org> 2.1.1-alt4
- Fixed packaging documentation (Closes: #34427).
- disable SSE for non-x86 and e2k arches.

* Sun Mar 18 2018 Andrew Savchenko <bircoph@altlinux.org> 2.1.1-alt3
- Fix SSE issue on E2K properly, revert SSE removal for non-x86.

* Sat Mar 17 2018 Michael Shigorin <mike@altlinux.org> 2.1.1-alt2
- disable SSE for non-x86
- enable parallel build

* Fri Jun 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.1-alt1.2
- Updated build to support gcc-6

* Sat Feb 20 2016 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1.1
- rebuilt against libSoundTouch.so.1

* Fri Oct 09 2015 Michael Shigorin <mike@altlinux.org> 2.1.1-alt1
- 2.1.1
- manual moved to a separate subpackage (not unlike fedora)

* Fri Oct 09 2015 Michael Shigorin <mike@altlinux.org> 2.1.0-alt1
- 2.1.0 (closes: #31343)
- buildreq for libsoxr-devel

* Thu Jun 11 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.0.5-alt4.1
- Rebuilt for gcc5 C++11 ABI.

* Thu Apr 24 2014 Michael Shigorin <mike@altlinux.org> 2.0.5-alt4
- try to recover MP3 processing capability (debian configure options)
- tweaked icons installation

* Tue Jan 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt3
- Restored in Sisyphus

* Tue Jan 07 2014 Michael Shigorin <mike@altlinux.org> 2.0.5-alt2
- build without ffmpeg support (latest one is unsupported so far)

* Tue Jan 07 2014 Michael Shigorin <mike@altlinux.org> 2.0.5-alt1
- 2.0.5
- spec cleanup according to ALT Packaging HOWTO
- converted Summary: in Russian from CP1251 to UTF-8
- added description in Russian

* Wed Jan 23 2013 Alex Karpov <karpov@altlinux.ru> 2.0.3-alt1
- new version
    + no more fullsrc package.

* Sun Sep 02 2012 Alex Karpov <karpov@altlinux.ru> 2.0.2-alt1
- new version

* Thu Mar 15 2012 Alex Karpov <karpov@altlinux.ru> 2.0.0-alt1
- new version. At last - not beta anymore!

* Tue Jan 31 2012 Alex Karpov <karpov@altlinux.ru> 1.3.14-alt1.3
- russian translation updated

* Sun Jan 22 2012 Alex Karpov <karpov@altlinux.ru> 1.3.14-alt1.2
- added new russian translation (bug #26841)

* Wed Jan 18 2012 Alex Karpov <karpov@altlinux.ru> 1.3.14-alt1.1
- export with libav* now works

* Tue Dec 13 2011 Alex Karpov <karpov@altlinux.ru> 1.3.14-alt1
- new version

* Wed Nov 09 2011 Alex Karpov <karpov@altlinux.ru> 1.3.13-alt2.1
- rebuild with new libav*

* Thu Aug 25 2011 Alex Karpov <karpov@altlinux.ru> 1.3.13-alt2
- fixed build (patch from Debian by Reinhard Tartler)

* Wed Apr 13 2011 Alex Karpov <karpov@altlinux.ru> 1.3.13-alt1
- new version

* Tue Nov 23 2010 Alex Karpov <karpov@altlinux.ru> 1.3.12-alt1.1
- disable portmixer for a while (build workaround)

* Fri Apr 02 2010 Alex Karpov <karpov@altlinux.ru> 1.3.12-alt1
- new version

* Tue Mar 23 2010 Alex Karpov <karpov@altlinux.ru> 1.3.11-alt1
- new version

* Thu Dec 10 2009 Alex Karpov <karpov@altlinux.ru> 1.3.10-alt1
- new version

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.3.9-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for audacity
  * postclean-05-filetriggers for spec file

* Mon Nov 02 2009 Alex Karpov <karpov@altlinux.ru> 1.3.9-alt1.1
- GSocket declaration conflict fixed

* Wed Sep 02 2009 Alex Karpov <karpov@altlinux.ru> 1.3.9-alt1
- new version
    + build from fullsrc tarball

* Mon Aug 24 2009 Alex Karpov <karpov@altlinux.ru> 1.3.8-alt2.1
- minor spec cleanup

* Mon Aug 24 2009 Alex Karpov <karpov@altlinux.ru> 1.3.8-alt2
- added actual help files

* Fri Aug 14 2009 Alex Karpov <karpov@altlinux.ru> 1.3.8-alt1.1
- updated build requirements
    + spec cleanup

* Thu Aug 13 2009 Alex Karpov <karpov@altlinux.ru> 1.3.8-alt1
- new version

* Tue Aug 11 2009 Alex Karpov <karpov@altlinux.ru> 1.3.7-alt1.1
- rebuild with new libs

* Fri Feb 27 2009 Alex Karpov <karpov@altlinux.ru> 1.3.7-alt1
- now it's stable enough for alt1 release

* Thu Jan 29 2009 Alex Karpov <karpov@altlinux.ru> 1.3.7-alt0.1
- 1.3.7

* Wed Jan 28 2009 Alex Karpov <karpov@altlinux.ru> 1.3.6-alt0.1
- 1.3.6
    + removed obsoleted %post and %postun stuff

* Thu Sep 25 2008 Alex Karpov <karpov@altlinux.ru> 1.3.5-alt0.1
- 1.3.5
    + updated build requirements

* Mon Apr 07 2008 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.9.2
- added update_menus

* Thu Mar 27 2008 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.9.1
- added desktopdb macros with new build requirements

* Mon Mar 24 2008 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.9
- added mimedb macros

* Sat Dec 15 2007 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.M40.7
- build for branch 4.0 with libtwolame

* Fri Dec 14 2007 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.6.1
- build for branch 4.0 (#13689 fix)

* Wed Nov 14 2007 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.6.1
- Vamp disabled for x86_64 build

* Wed Nov 14 2007 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.6
- 1.3.4 release

* Tue Oct 30 2007 Alex Karpov <karpov@altlinux.ru> 1.3.4-alt0.1
- new 1.3.4 unofficial beta
  + required wxGTK2u-2.6.4 (#13068 and probably #11880 fix)
  + removed desktop-file patch.

* Thu Sep 20 2007 Alex Karpov <karpov@altlinux.ru> 1.3.3-alt0.3
- audacity.desktop categories fixed (#12843)

* Tue Jun 05 2007 Alex Karpov <karpov@altlinux.ru> 1.3.3-alt0.2
- updated build requirements (now we can find a sound device)

* Wed May 30 2007 Alex Karpov <karpov@altlinux.ru> 1.3.3-alt0.1
- 1.3.3

* Tue Feb 20 2007 Alex Karpov <karpov@altlinux.ru> 1.3.2-alt0.4
- patch for flac-1.1.3 support by Led <led@> (bug #10868) 

* Thu Dec 14 2006 Alex Karpov <karpov@altlinux.ru> 1.3.2-alt0.3
- fixed bug 10420

* Sat Nov 11 2006 Alex Karpov <karpov@altlinux.ru> 1.3.2-alt0.2
- initial build of 1.3.x branch for Sisyphus

* Thu Dec 01 2005 Vladimir Lettiev <crux@altlinux.ru> 1.3.0-alt0.1
- 1.3.0 beta ( audacity-1_3_0-branch from cvs )

* Tue Feb 22 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.3-alt1.1.1
- Rebuilt with libflac-1.1.2-alt1

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.3-alt1.1
- Rebuilt with libstdc++.so.6.

* Sun Nov 21 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Thu Sep 02 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Fri Jun 25 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.1-alt2
- Updated patch from help file location.

* Wed May 12 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Tue Apr 13 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt2
- Updated russian translation.
- Added russian help.
- Fixed build with SoundTouch for gcc 3.3.3.

* Wed Mar 10 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sat Feb 14 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt0.9
- 1.2.0-pre4

* Fri Nov 14 2003 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt0.8
- 1.2.0-pre3
- Fixed build on SMP systems.

* Tue Oct 07 2003 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt0.7
- 1.2.0-pre2

* Sun Sep 28 2003 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt0.6
- 1.2.0-pre2 testing tarball.

* Sun Sep 14 2003 Andrey Astafiev <andrei@altlinux.ru> 1.2.0-alt0.3
- 1.2.0-pre1

* Wed Jun 25 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.3-alt3
- Fixed unmet: now requires wxGTK >= 2.4.1.

* Fri Jun 20 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.3-alt2
- Rebuilt with new wxGTK.

* Fri Mar 21 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Sun Mar 16 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.3-alt0.4
- Rebuilt with libid3tag package.

* Fri Mar 07 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.3-alt0.2
- Developers branch snapshot (CVS 20030306).
- Temprorary without libsamplerate.

* Wed Mar 05 2003 Andrey Astafiev <andrei@altlinux.ru> 1.0.0-alt6
- Rebuild with wxGTK-2.4.0

* Fri Feb 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt5
- Rebuild with new id3lib (3.8.2)

* Fri Nov 15 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt4
- Rebuild with new id3lib (3.8.1)

* Wed Nov 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt3
- Rebuild, system id3lib used.

* Wed Jul 31 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0.0-alt2.1
- rebuild with new vorbis

* Mon Jun 24 2002 Andrey Astafiev <andrei@altlinux.ru> 1.0.0-alt2
- Fixed intersection with basesystem.

* Fri Jun 7 2002 Andrey Astafiev <andrei@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Mon May 27 2002 Andrey Astafiev <andrei@altlinux.ru> 1.1-alt0.1.cvs
- cvs snapshot 20020527 of 1.1.x unstable branch especially for Daedalus.

* Wed Feb 13 2002 Andrey Astafiev <andrei@altlinux.ru> 0.99-alt0.1.pre1
- cvs snapshot 20020213 with several bugfixes.
- relocated help.

* Tue Feb 12 2002 Andrey Astafiev <andrei@altlinux.ru> 0.98-alt2
- rebuild with wxGTK 2.2.x branch.

* Fri Feb 01 2002 Andrey Astafiev <andrei@altlinux.ru> 0.98-alt1
- 0.98.

* Tue Jan 08 2002 Andrey Astafiev <andrei@altlinux.ru> 0.97-alt2
- Fixed group tag.

* Thu Oct 11 2001 Andrey Astafiev <andrei@altlinux.ru> 0.97-alt1
- First version of RPM package.l
