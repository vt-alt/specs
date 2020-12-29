# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: simplescreenrecorder
Version: 0.4.3
Release: alt1

Summary: Simple Screen Recording with OpenGL capture
License: GPL-3.0 and ISC and GPL-3.0+ and Zlib
Group: Video

Url: https://www.maartenbaert.be/simplescreenrecorder/
Source: https://github.com/MaartenBaert/ssr/archive/%version/ssr-%version.tar.gz

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libavformat-devel
BuildRequires: libswscale-devel
BuildRequires: libswresample-devel
BuildRequires: pkgconfig(Qt5) >= 5.7.0
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(xi)
BuildRequires: qt5-linguist
BuildRequires: libappstream-glib
BuildRequires: libXinerama-devel
BuildRequires: libv4l-devel
BuildRequires: qt5-tools-devel

Obsoletes: simplescreenrecording

%description
%summary

%prep
%setup -n ssr-%version
f="data/simplescreenrecorder.desktop"
for s in "GenericName=Simple screen recorder" \
	"GenericName[ru]=Запись видео с экрана" \
	"Comment[ru]=Программа записи видео с экрана" ; do
	fgrep -q "${s%%=}" "$f" || echo "$s" >> "$f"
done
# XXX waiting for support for channels
##sed -i '/#define SSR_USE_AVFRAME_CHANNELS/s/TEST_AV_VERSION.*/TEST_AV_VERSION(LIBAVCODEC, 57, 0, 57, 0)/' src/Global.h

%ifarch %e2k
sed -i 's,^#ifdef __x86_64__,#if defined (__x86_64__) || defined (__e2k__),' \
	glinject/elfhacks.h
%endif

%build
%cmake \
    -GNinja \
%ifnarch %ix86 x86_64
    -DENABLE_X86_ASM=FALSE \
%endif
%ifarch %arm aarch64
    -DWITH_GLINJECT=FALSE \
%endif
%ifarch ppc64le
    -DWITH_GLINJECT=FALSE \
%endif
    -DCMAKE_BUILD_TYPE=Release \
    -DWITH_QT5=TRUE
%ninja_build -C BUILD

%install
%ninja_install -C BUILD
rm -f %buildroot%_libdir/*.la

%files
%_bindir/*
%ifnarch %arm aarch64 ppc64le
%_libdir/lib*
%endif
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_man1dir/*.1.*
%_datadir/%name
%_datadir/metainfo/*

%changelog
* Mon Dec 28 2020 Leontiy Volodin <lvol@altlinux.org> 0.4.3-alt1
- 0.4.3
- Updated source link.
- Built with ninja instead make.
- Features:
    + Added V4L2 support (most webcams and capture cards).
    + Added option to mark recorded area on screen during recording.
    + Added JACK metadata.
    + Optionally support XDG config directory (~/.config/simplescreenrecorder) instead of home directory (~/.ssr).
    + Bugfixes.

* Tue May 19 2020 Leontiy Volodin <lvol@altlinux.org> 0.4.2-alt1
- 0.4.2

* Fri May 01 2020 Leontiy Volodin <lvol@altlinux.org> 0.4.1-alt1
- 0.4.1

* Mon Apr 13 2020 Leontiy Volodin <lvol@altlinux.org> 0.4.0-alt1
- 0.4.0

* Fri Oct 18 2019 Leontiy Volodin <lvol@altlinux.org> 0.3.11-alt4.gitb200b97
- update from git
- update buildrequires
- fixed russian translation

* Thu May 09 2019 Michael Shigorin <mike@altlinux.org> 0.3.11-alt3
- fixed build on e2k
- minor spec cleanup

* Sun Feb 17 2019 Anton Midyukov <antohami@altlinux.org> 0.3.11-alt2
- not ExclusiveArch
- build with qt5
- update buildrequires

* Tue Jun 26 2018 Fr. Br. George <george@altlinux.ru> 0.3.11-alt1
- Autobuild version bump to 0.3.11
- Exclusive x86 build

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 0.3.9-alt1
- Autobuild version bump to 0.3.9

* Mon Nov 20 2017 Andrey Cherepanov <cas@altlinux.org> 0.3.8-alt4
- Fix menu localization by add missing original GenericName

* Wed Nov 15 2017 Andrey Cherepanov <cas@altlinux.org> 0.3.8-alt3
- Add Russian localization to desktop file.

* Tue Jun 13 2017 Anton Farygin <rider@altlinux.ru> 0.3.8-alt2
- rebuilt with ffmpeg
- added man pages

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 0.3.8-alt1
- Autobuild version bump to 0.3.8

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 0.3.7-alt1
- Autobuild version bump to 0.3.7

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 0.3.6-alt1
- Autobuild version bump to 0.3.6

* Mon Feb 02 2015 Fr. Br. George <george@altlinux.ru> 0.3.3-alt1
- Autobuild version bump to 0.3.3
- Libavformat has no channels support still

* Mon Oct 06 2014 Fr. Br. George <george@altlinux.ru> 0.3.1-alt1
- Autobuild version bump to 0.3.1
- Obsolete simplescreenrecording

* Mon Oct 06 2014 Fr. Br. George <george@altlinux.ru> 0.3.0-alt1
- New version

* Wed Sep 04 2013 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux Sisyphus
