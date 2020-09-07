# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define _libexecdir %_prefix/libexec

Name: lmms
Version: 1.2.2
Release: alt2

Summary: Linux MultiMedia Studio
License: GPL-2.0-or-later
Group: Sound

Url: http://lmms.sourceforge.net
# https://github.com/LMMS/lmms.git
Source: %name-%version.tar
Source4: %name-16x16.png
Source5: %name-32x32.png
Source6: %name-48x48.png
Patch1: %name-1.2.0-no_werror.patch
Patch2: %name-1.2.0-vst-nowine.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-lmms libfltk-devel 
BuildRequires: gcc-c++ cmake

BuildRequires: desktop-file-utils
BuildRequires: libfluidsynth-devel
%ifnarch %e2k riscv64
BuildRequires: libsoundio-devel
%endif
BuildRequires: qt5-base-devel
BuildRequires: liblame-devel
BuildRequires: qt5-tools-devel
BuildRequires: libstk-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5UiTools)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fftw3f) >= 3.0.0
BuildRequires: pkgconfig(fluidsynth) >= 1.0.7
BuildRequires: pkgconfig(jack) >= 0.77
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: pkgconfig(samplerate) >= 0.1.8
BuildRequires: pkgconfig(sdl)
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: pkgconfig(sndfile) >= 1.0.11
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(vorbisenc)
BuildRequires: pkgconfig(vorbisfile)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(zlib)

%add_verify_elf_skiplist %_libdir/%name/*

%description
LMMS aims to be a free alternative to popular (but commercial and closed-
source) programs like FruityLoops, Cubase and Logic giving you the ability of
producing music with your computer by creating/synthesizing sounds, arranging
samples, using effects, playing live with keyboard and much more...

%package devel
Summary:	Development package for %name
Group:		Development/C
Requires: %name = %EVR

%description devel
Development files and headers for %name

%prep
%setup
%patch1 -p1
mv qt5-x11embed/* src/3rdparty/qt5-x11embed
mv rpmalloc/* src/3rdparty/rpmalloc/rpmalloc/
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -name '*.cpp' | xargs -r sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%cmake \
    -DWANT_QT5=ON \
    -DCMAKE_INSTALL_LIBDIR=%_lib \
%ifarch %ix86
    -DWANT_VST:BOOL=ON \
%else
    -DWANT_VST:BOOL=OFF \
%endif
    -DWANT_SDL:BOOL=ON \
    -DWANT_PORTAUDIO:BOOL=ON \
    -DWANT_CAPS:BOOL=ON \
    -DWANT_TAP:BOOL=ON \
    -DWANT_SWH:BOOL=ON \
    -DWANT_CALF:BOOL=ON \
    -DWANT_VST_NOWINE:BOOL=ON \
    -DWANT_CARLA:BOOL=OFF

%cmake_build VERBOSE=1

%install
%cmakeinstall_std

rm -fr %buildroot%_datadir/bash-completion/completions/lmms

# remove static library
rm -f %buildroot%_libdir/*.a

%find_lang %name

%files -f %name.lang
%doc README.md LICENSE.txt doc/AUTHORS
%_bindir/*
%_libdir/%name/
%_datadir/%name/
%_man1dir/*
%_iconsdir/hicolor/*/apps/*
%_iconsdir/hicolor/*/mimetypes/*
%_desktopdir/*
%_datadir/mime/packages/*

%files devel
%_includedir/%name

%changelog
* Fri Jul 17 2020 Anton Midyukov <antohami@altlinux.org> 1.2.2-alt2
- Build without libsoundio on e2k, riscv64

* Thu Jul 16 2020 Anton Midyukov <antohami@altlinux.org> 1.2.2-alt1
- Version 1.2.2

* Mon Nov 18 2019 Anton Midyukov <antohami@altlinux.org> 1.2.1-alt1
- Version 1.2.1

* Sun Jul 28 2019 Michael Shigorin <mike@altlinux.org> 1.2.0-alt3.20190117
- E2K: strip UTF-8 BOM for lcc < 1.24

* Fri Jan 18 2019 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt2.20190117
- new snapshot
- build with qt5
- build with fluidsynth-2

* Tue Feb 21 2017 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1.rc2.1
- new snapshot 1.2.0-rc2

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.95-alt2.git20140910.1
- (AUTO) subst_x86_64.

* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.95-alt2.git20140910
- Rebuilt with new stk

* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.95-alt1.git20140910
- Version 1.0.95

* Sun Sep 15 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.15-alt1
- 0.4.15

* Mon Jul 29 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.14-alt1
- 0.4.14

* Sat Feb 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.13-alt1
- 0.4.13

* Wed Oct 19 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.12-alt1
- 0.4.12

* Thu Jun 23 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.11-alt1
- 0.4.11
- Fix repocop warnings

* Sun Mar 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.10-alt1
- 0.4.10
- Fix BuildRequires

* Sun Dec 19 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.9-alt1
- 0.4.9

* Mon Oct 11 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.8-alt1
- 0.4.8

* Fri Aug 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.7-alt1
- 0.4.7

* Sat Jan 16 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.6-alt1
- 0.4.6

* Wed Aug 26 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.4.5-alt1
- 0.4.5
- Switch off system ladspa
- Remove all patches

* Mon Mar 09 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.3-alt1
- 0.4.3
- Add Patch1: lmms-0.4.2-literal.patch from lmms-0.4.3-1mdv2009.1
- Add subpackage %name-devel
- Switch to system ladspa
- Add Requires: ladspa-caps ladspa-mcp-plugins ladspa-tap-plugins ladspa-swh-plugins ladspa-rev-plugins ladspa-vco-plugins

* Wed Dec 17 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.0-alt2
- Fix build in x86_64.

* Mon Dec 15 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.0-alt1
- 0.4.0
- Fix repocop tests: iconsdir, shared-mime-info, update_menus, freedesktop-categories et ctr.
- Update spec

* Thu Sep 11 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.3.2-alt2
- Fix for repocop solution
- Update BuildRequires

* Wed Jun 25 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.3.2-alt1
- 0.3.2

* Tue Dec 11 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.3.1-alt3
- Fix build in x86_64.
- Remove BuildPreReq: libwine-devel
- Add BuildPreReq: rpm-build-lmms

* Fri Dec 07 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.3.1-alt2
- Fix build in x86_64.
- Remove BuildPreReq: libwine-devel for x86_64

* Mon Nov 19 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.3.1-alt1
- 0.3.1
- update spec

* Tue Sep 11 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.3.0-alt1
- 0.3.0
- update spec

* Mon Jun 11 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2.1-alt1
- 0.2.1
- update spec

* Fri Jul 21 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.2.0-alt0
- 0.2.0
- Removed ALT menu file

* Thu Mar 23 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.1.4-alt2
- Removed BuildRequires: libqt4-core

* Tue Mar 21 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.1.4-alt1
- Removed BuildPreReq: wine

* Fri Feb 17 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.1.4-alt0
- initial build
