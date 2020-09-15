Name: gpac
Epoch: 1
Version: 1.0.0
Release: alt1

Summary: GPAC is a multimedia framework covering MPEG-4, VRML/X3D and SVG.
License: LGPL-2.1+
Group: Video
Url: http://gpac.sourceforge.net/
Packager: Michael A. Kangin <prividen@altlinux.org>

Source: %name-%version.tar
Patch: gpac-1.0.0-not-deb.patch

Requires: lib%name = %EVR

# optimized out: fontconfig glibc-kernheaders-generic
# glibc-kernheaders-x86 libGLU-devel libX11-devel libXext-devel libavcodec-devel
# libavformat-devel libavutil-devel libcairo-gobject libcdio-paranoia libdc1394-22
# libfreetype-devel libgdk-pixbuf libglvnd-devel libgpg-error libogg-devel
# libopencore-amrnb0 libopencore-amrwb0 libp11-kit librabbitmq-c libraw1394-11
# libstdc++-devel libx265-192 pkg-config python2-base sh4 xorg-proto-devel
# zlib-devel
BuildRequires: gcc-c++ git-core libSDL-devel libXv-devel
BuildRequires: liba52-devel libalsa-devel libavdevice-devel libavfilter-devel
BuildRequires: libdirectfb-devel libfaad-devel libjack-devel libjpeg-devel
BuildRequires: libmad-devel libopenjpeg-devel libpng-devel libpulseaudio-devel
BuildRequires: libssl-devel libswresample-devel libswscale-devel libtheora-devel
BuildRequires: libvorbis-devel libxvid-devel
BuildRequires: chrpath

%description
GPAC is a multimedia framework for MPEG-4, VRML/X3D and SVG/SMIL.
GPAC is built upon an implementation of the MPEG-4 Systems
standard (ISO/IEC 14496-1) developed from scratch in C.

The main development goal is to provide a clean (a.k.a. readable by as
many people as possible), small and flexible alternative to the MPEG-4
Systems reference software (known as IM1 and distributed in ISO/IEC
14496-5). GPAC covers a very large part of the MPEG-4 standard, and
features what can probably be seen as the most advanced and robust 2D
MPEG-4 Player available worldwide, as well as a decent 3D MPEG-4/VRML
player.

The second development goal is to achieve integration of recent
multimedia standards for content playback (SVG/SMIL, VRML, X3D, SWF,
etc) and content delivery into a single framework.
GPAC features 2D and 3D multimedia playback, MPEG-4 Systems (BIFS and
LASeR) encoders, multiplexers and publishing tools for content
distribution, such as RTP streamers, MPEG-2 TS muxers, ISO Base Media
File (MP4 & 3GP a.k.a. ISO/IEC 14496-12) and MPEG DASH muxers.

GPAC is licensed under the GNU Lesser General Public License.

%package -n lib%name
Summary: GPAC library
Group: System/Libraries
Conflicts: %name < %version-%release
Conflicts: mp4box < %version-%release

%description -n lib%name
This is a base GPAC library


%package -n mp4box
Summary: The GPAC multimedia packager
Group: Video
Requires: lib%name = %EVR

%description -n mp4box
MP4Box can be used for performing many manipulations on multimedia files
like AVI, MPG, TS, but mostly on ISO media files (e.g. MP4, 3GP), e.g.:
- for encoding/decoding presentation languages like MPEG-4 XMT or W3C
  SVG into/from binary formats like MPEG-4 BIFS or LASeR,
- for manipulating ISO files like MP4, 3GP: adding, removing,
  multiplexing audio, video and presentation data (including subtitles)
  from different sources and in different formats,
- for performing encryption of streams,
- for attaching metadata to individual streams or to the whole ISO file
  to produce MPEG-21 compliant or hybrid MPEG-4/MPEG-21 files,
- and packaging and tagging the result for streaming, download and
  playback on different devices (e.g. phones, PDA) or for different
  software (e.g. iTunes).

%package -n lib%name-devel
Summary: Development headers and library for %name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Development headers and libraries for %name.

%prep
%setup -q
%patch -p1

%build
%configure --prefix="%_prefix" \
    --libdir="%_lib" \
    --mandir="%_mandir" \
    --enable-pic \
    --enable-depth \
    --use-js=no \
    --use-ffmpeg=system \
    --use-ogg=system \
    --use-openjpeg=system \
    --use-theora=system \
    --use-vorbis=system \
    --disable-amr-nb \
    --disable-amr-wb \
    --enable-jack \
    --enable-joystick \
    --enable-pulseaudio
%make_build

%install
%make_install install DESTDIR="%buildroot"

# Remove useless directories
rm -rf %buildroot/%_includedir/win32
rm -rf %buildroot/%_includedir/wince

chrpath -d %buildroot%_bindir/MP4Client
chrpath -d %buildroot%_bindir/MP4Box
chrpath -d %buildroot%_bindir/gpac

%files
%doc Changelog COPYING README.md
%_bindir/%name
%_bindir/MP4Client
%_man1dir/mp4client*
%_datadir/%name
%_libdir/%name
%_desktopdir/%name.desktop
# TODO: pacakage pixmapsdir (problem with symlinks)

%files -n lib%name
%doc Changelog COPYING README.md
%_libdir/lib%name.so*
%_man1dir/gpac*

%files -n mp4box
%_bindir/MP4Box
%_man1dir/mp4box*

%files -n lib%name-devel
%_includedir/%name

%changelog
* Tue Sep 01 2020 Grigory Ustinov <grenka@altlinux.org> 1:1.0.0-alt1
- Updated to 1.0.0.
- Fixed license.
- Added devel subpackage.
- Cleaned up BR's.

* Wed Dec 19 2018 Grigory Ustinov <grenka@altlinux.org> v0.7.1.0.284.gite64a7d229-alt1
- Build new version (with openssl1.1).

* Sun Jun 19 2016 Michael A. Kangin <prividen@altlinux.org> 0.6.1-alt1
- 0.6.1

* Sun Jun 19 2016 Michael A. Kangin <prividen@altlinux.org> 0.5.0-alt2
- Update build dependencies

* Wed Feb 13 2013 Michael A. Kangin <prividen@altlinux.org> 0.5.0-alt1
- 0.5.0

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt1.svn3744.2.1
- Rebuilt with libpng15

* Fri Feb 10 2012 Michael A. Kangin <prividen@altlinux.org> 0.4.5-alt1.svn3744.2
- Rebuild with all libav -devel packages

* Sun Nov 27 2011 Michael A. Kangin <prividen@altlinux.org> 0.4.5-alt1.svn3744.1
- Initial build for ALTLinux

