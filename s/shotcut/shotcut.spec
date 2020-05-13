# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define _vstring %(echo %{version} |tr -d ".")

Name: shotcut
Version: 20.02.02
Release: alt1
Summary: A free, open source, cross-platform video editor
Summary(ru_RU.UTF-8): Свободный кросс-платфоорменный видеоредактор
License: GPL-3.0+
Group: Video
Url: http://www.shotcut.org/
Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar
# Melt patch /usr/bin/melt
Patch: mlt_path.patch

BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5Core) >= 5.9.1
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5OpenGL)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5WebKitWidgets)
BuildRequires: pkgconfig(Qt5WebSockets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: qt5-linguist
BuildRequires: pkgconfig(mlt++)
BuildRequires: pkgconfig(mlt-framework)
BuildRequires: libx264-devel
BuildRequires: pkgconfig(sdl2)
BuildRequires: ImageMagick-tools

Requires: %name-data = %version
Requires: mlt-utils
Requires: gst-plugins-bad1.0
Requires: frei0r-plugins
Requires: ladspa_sdk
Requires: lame
Requires: ffmpeg ffprobe ffplay
Requires: libSDL2
# see bug 34876
Requires: qt5-quickcontrols
# see bug 34877
Requires: qt5-graphicaleffects

%description
These are all currently implemented features:
 * supports oodles of audio and video formats and codecs;
 * supports many image formats as image sequences;
 * no import required - native editing;
 * frame-accurate seeking for many formats;
 * multi-format timeline;
 * screen capture (Linux only) including background capture;
 * webcam capture (Linux only);
 * audio capture (Linux only; PulseAudio, JACK, or ALSA);
 * network stream playback (HTTP, HLS, RTMP, RTSP, MMS, UDP);
 * frei0r video generator plugins (e.g. color bars and plasma);
 * Blackmagic Design SDI and HDMI for input and preview monitoring;
 * JACK transport sync;
 * deinterlacing;
 * detailed media properties panel;
 * recent files panel with search;
 * drag-n-drop files from file manager;
 * save and load trimmed clip as MLT XML file;
 * load and play complex MLT XML file as a clip;
 * audio signal level meter;
 * volume control;
 * scrubbing and transport control;
 * flexible UI through dock-able panels;
 * encode/transcode to a variety of formats and codecs;
 * capture (record);
 * stream (encode to IP) files and any capture source;
 * batch encoding with job control;
 * MLT XML playlists;
 * unlimited undo and redo for playlist edits;
 * connect to Melted servers over MVCP TCP protocol;
 * control the transport playback of Melted units;
 * edit Melted playlists including support for undo/redo;
 * OpenGL GPU-based image processing;
 * multi-core parallel image processing when not using GPU;
 * video filters;
 * audio filters;
 * 3-way color wheels for color correction and grading;
 * eye dropper tool to pick neutral color for white balancing;
 * HTML5 (sans audio and video) as video source and filters;
 * Leap Motion for jog/shuttle control;
 * DeckLink SDI keyer output - internal or external;
 * UI themes/skins: native-OS look and custom dark and light;
 * control video zoom in the player.

%package data
Summary: Data files for %name
Group: Video
BuildArch: noarch

%description data
Data files for %name

%prep
%setup
%patch -p0

# Create version.json from current version
echo "{" > version.json
echo " \"version_number\": %{_vstring}02," >> version.json
echo " \"version_string\": \"%{version}.02\"," >> version.json
echo " \"url\": \"https://shotcut.org/blog/new-release-%{_vstring}/\"" >> version.json
echo "}" >> version.json
echo "" >> version.json

# Postmortem debugging tools for MinGW.
rm -rf drmingw

%build
lrelease-qt5 translations/*.ts
export _VSTRING="%{version}.02"
%qmake_qt5 \
    QMAKE_CXXFLAGS=-DSHOTCUT_NOUPGRADE \
    _VSTRING="%{version}.02" \
    PREFIX=%buildroot%_prefix

%make_build

%install
%makeinstall_std
chmod a+x %buildroot/%_datadir/shotcut/qml/export-edl/rebuild.sh

for i in 16 32 48; do
    mkdir -p %buildroot/%_iconsdir/hicolor/"$i"x"$i"/apps
    convert icons/%name-logo-64.png -resize "$i"x"$i" \
    %buildroot/%_iconsdir/hicolor/"$i"x"$i"/apps/org.shotcut.Shotcut.png
done

%files
%_bindir/%name
%_desktopdir/org.shotcut.Shotcut.desktop
%doc COPYING README.md
%_iconsdir/hicolor/*/apps/org.shotcut.Shotcut.png
%_datadir/metainfo/org.shotcut.Shotcut.appdata.xml
%_datadir/mime/packages/org.shotcut.Shotcut.xml
%_man1dir/*

%files data
%_datadir/%name

%changelog
* Mon Feb 17 2020 Fr. Br. George <george@altlinux.ru> 20.02.02-alt1
- new version 20.02.02

* Wed Oct 03 2018 Fr. Br. George <george@altlinux.ru> 18.10.01-alt1
- new version 18.10.01

* Tue Jul 03 2018 Anton Midyukov <antohami@altlinux.org> 18.06.02-alt1
- new version 18.07
- unpackaged files in buildroot should terminate build
- update from git
- disabled autoupdate check

* Sat May 05 2018 Anton Midyukov <antohami@altlinux.org> 18.04-alt3
- Added missing requires qt5-quickcontrols
- Added missing requires qt5-graphicaleffects

* Fri Apr 20 2018 Anton Midyukov <antohami@altlinux.org> 18.04-alt2
- Update buildrequires and requires
- Added shotcut.appdata.xml

* Sat Apr 07 2018 Cronbuild Service <cronbuild@altlinux.org> 18.04-alt1
- repocop cronbuild 20180407. At your service.

* Mon Mar 19 2018 Fr. Br. George <george@altlinux.ru> 18.03-alt2
- Patch "/bin/nice" location
- Use native .desktop
- Added missing requires ff* and melt binaries

* Sun Mar 04 2018 Cronbuild Service <cronbuild@altlinux.org> 18.03-alt1
- new version (18.03) with rpmgs script

* Tue Feb 13 2018 Cronbuild Service <cronbuild@altlinux.org> 18.02-alt1
- repocop cronbuild 20180213. At your service.

* Sun Jan 28 2018 Anton Midyukov <antohami@altlinux.org> 18.01-alt2
- Added missing requires libSDL2
- Fix make install

* Tue Jan 02 2018 Cronbuild Service <cronbuild@altlinux.org> 18.01-alt1
- new version (18.01) with rpmgs script

* Wed Dec 06 2017 Cronbuild Service <cronbuild@altlinux.org> 17.12-alt1
- new version (17.12) with rpmgs script

* Tue Nov 07 2017 Cronbuild Service <cronbuild@altlinux.org> 17.11-alt1
- repocop cronbuild 20171107. At your service.

* Sat Oct 07 2017 Cronbuild Service <cronbuild@altlinux.org> 17.10-alt1
- repocop cronbuild 20171007. At your service.

* Fri Sep 01 2017 Cronbuild Service <cronbuild@altlinux.org> 17.09-alt1
- repocop cronbuild 20170901. At your service.

* Sat Aug 05 2017 Cronbuild Service <cronbuild@altlinux.org> 17.08-alt1
- new version (17.08) with rpmgs script

* Sat Jul 08 2017 Cronbuild Service <cronbuild@altlinux.org> 17.07-alt1
- repocop cronbuild 20170708. At your service.

* Sat Jun 03 2017 Cronbuild Service <cronbuild@altlinux.org> 17.06-alt1
- new version (17.06) with rpmgs script

* Sat May 06 2017 Cronbuild Service <cronbuild@altlinux.org> 17.05-alt1
- new version (17.05) with rpmgs script

* Sat Apr 01 2017 Cronbuild Service <cronbuild@altlinux.org> 17.04-alt1
- repocop cronbuild 20170401. At your service.

* Sat Mar 04 2017 Cronbuild Service <cronbuild@altlinux.org> 17.03-alt1
- new version (17.03) with rpmgs script

* Fri Feb 17 2017 Anton Midyukov <antohami@altlinux.org> 17.02-alt1
- new version (17.02) with rpmgs script

* Thu Jan 05 2017 Anton Midyukov <antohami@altlinux.org> 17.01-alt1
- new version (17.01) with rpmgs script

* Wed Dec 07 2016 Anton Midyukov <antohami@altlinux.org> 16.12-alt1
- new version (16.12) with rpmgs script

* Thu Nov 10 2016 Anton Midyukov <antohami@altlinux.org> 16.11-alt1
- new version (16.11) with rpmgs script

* Sat Sep 17 2016 Anton Midyukov <antohami@altlinux.org> 16.09-alt1
- New version 16.09

* Sat Jul 02 2016 Anton Midyukov <antohami@altlinux.org> 16.07-alt1
- New version 16.07-alt1

* Sun Jun 12 2016 Anton Midyukov <antohami@altlinux.org> 16.06-alt1
- New version.

* Wed Mar 02 2016 Anton Midyukov <antohami@altlinux.org> 16.03-alt1
- New version.

* Fri Jan 08 2016 Anton Midyukov <antohami@altlinux.org> 16.01-alt1
- Initial build for ALT Linux Sisyphus
