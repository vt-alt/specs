Name: SDL
Version: 1.2.14
Release: alt8

Summary: Simple DirectMedia Layer
License: LGPL
Group: System/Libraries

Url: http://www.libsdl.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libGLU-devel libXext-devel libXrandr-devel libalsa-devel libpulseaudio-devel libusb-compat-devel
%ifarch %ix86 x86_64
BuildRequires: nasm
%endif

%description
This is the Simple DirectMedia Layer, a generic API that provides low level
access to audio, keyboard, mouse, and display framebuffer across multiple
platforms.

%package -n lib%name
Summary: Simple DirectMedia Layer
Group: System/Libraries
Provides: SDL

%description -n lib%name
This is the Simple DirectMedia Layer, a generic API that provides low level
access to audio, keyboard, mouse, and display framebuffer across multiple
platforms.

This package provides shared libraries required to run %name-based applications.

%package -n lib%name-devel
Summary: Development environment for Simple DirectMedia Layer
Group: Development/C
Requires: lib%name = %version-%release libGLU-devel

%description -n lib%name-devel
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

This is the libraries, include files and other resources you can use
to develop %name applications.

%prep
%setup
%patch -p1

cat acinclude/* > aclocal.m4

%build
autoconf
%configure \
	--disable-nas \
	--disable-oss \
	--disable-esd \
	--disable-arts \
	--disable-alsa-shared \
	--disable-pulseaudio-shared \
	--disable-x11-shared \
	--disable-static
%make_build

%install
%makeinstall_std

%files -n lib%name
%doc BUGS CREDITS README README-%name.txt TODO WhatsNew
%_libdir/*.so.*

%files -n lib%name-devel
%doc docs.html docs/*html*
%_includedir/*
%_bindir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/aclocal/*
%_mandir/man?/*

# TODO: 1.2.15+

%changelog
* Tue Jun 18 2019 Michael Shigorin <mike@altlinux.org> 1.2.14-alt8
- fixed upstream bug #894 with upstream rev#4aa31b9207f2

* Fri Jan 06 2017 Michael Shigorin <mike@altlinux.org> 1.2.14-alt7
- fixed FTBFS (upstream bug #1111 / hg rev 32f0f603a0c8)
- minor spec cleanup

* Wed Mar 09 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.2.14-alt6
- rebuilt for debuginfo

* Mon Nov 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.14-alt5
- devel: added libGLU-devel requires

* Mon Nov 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.14-alt4
- updated build dependencies

* Sun Oct 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.14-alt3
- rebuild

* Sun Jan 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.14-alt2
- removed rpath from sdl.pc (closes: #22706)

* Tue Oct 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.14-alt1
- 1.2.14

* Fri Sep 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.13-alt8
- drop pa patches (closes: #19983)

* Sun Apr 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.13-alt7
- merged RH patches for pulseaudio

* Sat Dec 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.13-alt6
- enabled Xrender
- drop fullscreen toggle patch

* Mon Dec 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.13-alt5
- updated build dependencies

* Mon Nov 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.13-alt4
- disabled esd support

* Tue Nov 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.13-alt3
- disabled OSS support

* Tue Nov 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.13-alt2
- rebuild with gcc4.3

* Wed Jan 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.13-alt1
- 1.2.13
- disabled static by default

* Mon Sep 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.12-alt3
- require nasm for building only on %%ix86 and x86_64

* Fri Aug 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.12-alt2
- relocated development documentation (close #12581)

* Sun Jul 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.12-alt1
- 1.2.12

* Sat Jun 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.11-alt4
- added SDL-1.2.11-fullscreen-toggle.patch

* Mon Mar 26 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.11-alt3
- disable nas
- drop SDL-1.2.11-configure.patch

* Wed Jan 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.11-alt2
- fixed Provides/Obsoletes

* Wed Dec 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.2.11-alt1
- 1.2.11

* Mon May 22 2006 Anton Farygin <rider@altlinux.ru> 1.2.10-alt1
- new version

* Fri Oct 21 2005 Anton Farygin <rider@altlinux.ru> 1.2.9-alt1
- new version

* Sat Mar 26 2005 Anton D. Kachalov <mouse@altlinux.org> 1.2.8-alt2
- x86_64 support

* Mon Dec 27 2004 Anton Farygin <rider@altlinux.ru> 1.2.8-alt1
- new version
- added SDL provides (#4840)

* Tue Aug 03 2004 Anton Farygin <rider@altlinux.ru> 1.2.7-alt2
- x86_64 patch
- joistick fix from mdk (for kernel 2.6)

* Thu Mar 18 2004 Anton Farygin <rider@altlinux.ru> 1.2.7-alt1
- 1.2.7

* Mon Dec 15 2003 Anton Farygin <rider@altlinux.ru> 1.2.6-alt3
- added patch from Sir Raorn for correct 3DNow! detection (#3342)

* Mon Dec 01 2003 Rider <rider@altlinux.ru> 1.2.6-alt2
- rebuild without .la files 

* Mon Sep 01 2003 Rider <rider@altlinux.ru> 1.2.6-alt1
- new version

* Fri Aug 22 2003 Rider <rider@altlinux.ru> 1.2.5-alt2
- disable directfb and aa video support (#2668, #2670)

* Wed Oct 09 2002 Rider <rider@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Mon Sep 23 2002 Rider <rider@altlinux.ru> 1.2.4-alt2
- rebuild with new gcc

* Sat Apr 27 2002 Rider <rider@altlinux.ru> 1.2.4-alt1
- alsa9 patch from MDK
- new version

* Fri Feb 22 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.2.3-alt2
- Fixed buildrequires.

* Sun Dec 09 2001 Rider <rider@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Fri Jul 27 2001 Rider <rider@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Thu Apr  5 2001 Kostya Timoshenko <kt@altlinux.ru> 1.2.0-alt1
- version 1.2.0
- removed old 1.0.8
- adapted rpath patch.
- Moved static libraries to devel-static subpackage.

* Wed Feb 14 2001 Kostya Timoshenko <kt@petr.kz> 1.1.8-ipl1mdk
- 1.1.8

* Tue Feb 06 2001 Dmitry V. Levin <ldv@fandra.org> 1.1.7-ipl2mdk
- Build with --enable-video-aalib.
- Explicitly set strip methods.
- Libification.

* Tue Jan  9 2001 Kostya Timoshenko <kt@petr.kz>
- 1.1.7

* Tue Dec 26 2000 Kostya Timoshenko <kt@petr.kz>
- Rebuild for RE

* Wed Nov 29 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.1.6-2mdk
- follow new lib policy, split packages with current and old versions

* Tue Oct 24 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.1.6-1mdk
- 1.1.6
- include man pages
- include html help

* Thu Oct 19 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.1.4-8mdk
- rebuild to fix sdl-config to not provide some rpath

* Fri Sep 29 2000 Giuseppe GhibР <ghibo@mandrakesoft.com> 1.1.4-7mdk
- rebuild with latest XFree 4.0.1 from FredL.

* Fri Sep 15 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.1.4-6mdk
- rebuild against fixed XFree4 by fredl

* Tue Aug 29 2000 Giuseppe GhibР <ghibo@mandrakesoft.com> 1.1.4-5mdk
- rebuild without %%configure.

* Mon Aug 28 2000 Giuseppe GhibР <ghibo@mandrakesoft.com> 1.1.4-4mdk
- fixed a typo in changelog.

* Mon Aug 28 2000 Giuseppe GhibР <ghibo@mandrakesoft.com> 1.1.4-3mdk
- use of configure and other macros.

* Sat Aug 25 2000 Giuseppe GhibР <ghibo@mandrakesoft.com> 1.1.4-2mdk
- removed Mesa-devel from BuildRequires and other entries listed twice.
- updated URL.

* Fri Aug 25 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.1.4-1mdk
- 1.1.4 (which fixes a bug in KDE according to the README for xmms-smpeg).

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.1.3-4mdk
- automatically added BuildRequires.

* Thu Jun 28 2000 Giuseppe GhibР <ghibo@mandrakesoft.com> 1.1.3-3mdk
- added old 1.0.X version for backward compatibility.

* Sat Jun 24 2000 Giuseppe GhibР <ghibo@mandrakesoft.com> 1.1.3-2mdk
- added some Requires.

* Thu Jun 22 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.1.3-1mdk
- v1.1.3.

* Thu May 18 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.8-4mdk
- don't use nasm on non Intel archs.

* Tue Apr 11 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.8-3mdk
- fixed the few problems

* Fri Apr 07 2000 Giuseppe GhibР <ghibo@mandrakesoft.com>
- changed group.

* Sat Mar 18 2000 Giuseppe GhibР <ghibo@mandrakesoft.com>
- updated to version 1.0.8.

* Tue Feb 09 2000 Giuseppe GhibР <ghibo@mandrakesoft.com>
- updated to version 1.0.4.

* Sat Feb 05 2000 Giuseppe GhibР <ghibo@linux-mandrake.com>
- updated for version 1.0.3.
- added BuildPreReq.

* Wed Jan 19 2000 Sam Lantinga <slouken@devolution.com>
- Re-integrated spec file into SDL distribution
- 'name' and 'version' come from configure
- Some of the documentation is devel specific
- Removed SMP support from %build - it doesn't work with libtool anyway

* Tue Jan 18 2000 Hakan Tandogan <hakan@iconsult.com>
- Hacked Mandrake sdl spec to build 1.1

* Sun Dec 19 1999 John Buswell <johnb@mandrakesoft.com>
- Build Release

* Sat Dec 18 1999 John Buswell <johnb@mandrakesoft.com>
- Add symlink for libSDL-1.0.so.0 required by sdlbomber
- Added docs

* Thu Dec 09 1999 Lenny Cartier <lenny@mandrakesoft.com>
- v 1.0.0

* Mon Nov  1 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- First spec file for Mandrake distribution.
