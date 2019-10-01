Name: strawberry
Version: 0.6.5
Release: alt1
Summary: Audio player and music collection organizer

# Main program: GPLv3
# src/analyzer and src/engine/gstengine and src/engine/xineengine: GPLv2
# 3rdparty/taglib, src/widgets/fancytabwidget and src/widgets/stylehelper: LGPLv2
# 3rdparty/qocoa: MIT
# 3rdparty/singleapplication: MIT
# 3rdparty/utf8-cpp: Boost
# src/core/timeconstants.h and ext/libstrawberry-common/core/logging and ext/libstrawberry-common/core/messagehandler: ASL 2.0
# some icons in qocoa: CC-BY-SA
License: GPLv2 and GPLv3+ amd LGPLv2 and ASL 2.0 and MIT and Boost and CC-BY-SA
Group: Sound
Url: http://www.strawbs.org/
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: https://github.com/jonaski/strawberry/archive/%version/%name-%version.tar.gz

Patch: strawberry-udisks-headers.patch

BuildRequires: boost-program_options-devel ccache gcc-c++ gettext-tools glib2-devel gst-plugins1.0-devel gstreamer1.0-devel libalsa-devel libcdio-devel libchromaprint-devel libdbus-devel libfftw3-devel libgio-devel libgnutls-devel libgpod-devel libimobiledevice-devel libmtp-devel libplist-devel libprotobuf-devel libpulseaudio-devel libsqlite3-devel libtag-devel libusbmuxd-devel libvlc-devel libxine2-devel qt5-phonon-devel qt5-x11extras-devel
BuildRequires: cmake rpm-macros-cmake extra-cmake-modules desktop-file-utils libappstream-glib qt5-tools-devel protobuf-compiler
%ifnarch s390 s390x
BuildRequires: libgpod-devel
%endif

Requires: gst-plugins-good1.0 vlc-mini

Provides: bundled(qocoa)
Provides: bundled(utf8-cpp)
Provides: bundled(singleapplication)
Provides: bundled(singlecoreapplication)

%description
Strawberry is a audio player and music collection organizer.
It is a fork of Clementine. The name is inspired by the band Strawbs.

Features:
  * Play and organize music
  * Supports WAV, FLAC, WavPack, DSF, DSDIFF, Ogg Vorbis, Speex, MPC,
    TrueAudio, AIFF, MP4, MP3 and ASF
  * Audio CD playback
  * Native desktop notifications
  * Playlists in multiple formats
  * Advanced output and device options with support for bit perfect playback
    on Linux
  * Edit tags on music files
  * Fetch tags from MusicBrainz
  * Album cover art from Last.fm, Musicbrainz and Discogs
  * Song lyrics from AudD and API Seeds
  * Support for multiple backends
  * Audio analyzer
  * Equalizer
  * Transfer music to iPod, iPhone, MTP or mass-storage USB player
  * Integrated Tidal support
  * Scrobbler with support for Last.fm, Libre.fm and ListenBrainz

%prep
%setup
#patch -p1

# Remove most 3rdparty libraries
# Unbundle taglib next release:
# https://github.com/taglib/taglib/issues/837#issuecomment-428389347

mv 3rdparty/singleapplication/LICENSE 3rdparty/singleapplication/LICENSE-singleapplication
mv 3rdparty/taglib/COPYING 3rdparty/taglib/COPYING-taglib

%build
%cmake \
  -DBUILD_WERROR=OFF \
  -DUSE_SYSTEM_TAGLIB=ON

%make -C BUILD

%install
%cmakeinstall_std

%check
desktop-file-validate %buildroot%_desktopdir/org.strawberrymusicplayer.strawberry.desktop
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/org.strawberrymusicplayer.strawberry.appdata.xml

%files
%doc COPYING 3rdparty/taglib/COPYING-taglib 3rdparty/singleapplication/LICENSE-singleapplication
%doc Changelog
%_bindir/strawberry
%_bindir/strawberry-tagreader
%_datadir/metainfo/org.strawberrymusicplayer.strawberry.appdata.xml
%_desktopdir/org.strawberrymusicplayer.strawberry.desktop
%_iconsdir/hicolor/*/apps/strawberry.*
%_man1dir/strawberry.1.*
%_man1dir/strawberry-tagreader.1.*

%changelog
* Tue Oct 01 2019 Leontiy Volodin <lvol@altlinux.org> 0.6.5-alt1
- New version (0.6.5) with rpmgs script.

* Thu Sep 26 2019 Leontiy Volodin <lvol@altlinux.org> 0.6.4-alt1
- New version (0.6.4) with rpmgs script.

* Tue Aug 06 2019 Leontiy Volodin <lvol@altlinux.org> 0.6.3-alt1
- 0.6.3
- Fixed crash with vlc backend

* Mon Aug 05 2019 Leontiy Volodin <lvol@altlinux.org> 0.6.2-alt1
- 0.6.2

* Mon Jul 15 2019 Leontiy Volodin <lvol@altlinux.org> 0.5.5-alt2
- Added BR.

* Thu Jul 11 2019 Leontiy Volodin <lvol@altlinux.org> 0.5.5-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec)
