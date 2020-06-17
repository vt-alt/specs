%def_disable freerdp
%def_disable goom
%def_enable firewire
%def_enable visualization
%def_enable wayland

Name: vlc
Version: 3.0.10
Release: alt1

Summary: VLC media player
License: GPLv2
Group: Video

Url: http://www.videolan.org
Source: vlc-%version.tar
Patch: vlc-3.0.6-alt-e2k-lcc123.patch
Patch1: 0001-configure-fix-linking-on-RISC-V-ISA.patch

BuildRequires: gcc-c++
BuildRequires: freetype2-devel glib2-devel flex
BuildRequires: libdvdcss-devel libavcodec-devel libnotify-devel
BuildRequires: libavutil-devel libpostproc-devel libavformat-devel
BuildRequires: libswscale-devel libmpeg2-devel libebml-devel >= 1.3.5-alt1
BuildRequires: libmatroska-devel libcddb-devel liblive-devel aalib-devel
BuildRequires: libtwolame-devel libssh2-devel liba52-devel libalsa-devel
BuildRequires: libcdio-devel libdvbpsi-devel libdvdnav-devel >= 6.1.0
BuildRequires: libdvdread-devel >= 6.1.0 libflac-devel libgcrypt-devel librsvg-devel
BuildRequires: libgnutls-devel libgpg-error-devel libjpeg-devel liblirc-devel
BuildRequires: libmad-devel libmodplug-devel libspeex-devel libspeexdsp-devel libmpcdec-devel
BuildRequires: libncurses-devel libncursesw-devel libogg-devel libpng-devel
BuildRequires: libstdc++-devel libtheora-devel libtiff-devel libtinfo-devel
BuildRequires: libvcd-devel libvorbis-devel libxml2-devel
BuildRequires: libpulseaudio-devel libx264-devel vim-devel
BuildRequires: jackit-devel liblame-devel zlib-devel libavahi-devel dbus
BuildRequires: libtag-devel libfluidsynth-devel libdbus-devel
BuildRequires: libzvbi-devel libfribidi-devel
BuildRequires: libass-devel libbluray-devel libpcre-devel libopus-devel
BuildRequires: libkate-devel libv4l-devel libmtp-devel libshout2-devel
BuildRequires: libtar-devel libva-devel libvpx-devel libx265-devel
BuildRequires: libxcb-devel libxcbutil-devel libxcbutil-keysyms-devel
BuildRequires: libEGL-devel libGL-devel libGLES-devel
BuildRequires: libschroedinger-devel libsmbclient-devel
BuildRequires: libupnp-devel liblua5-devel lua5
BuildRequires: libtiger-devel libudev-devel libsqlite3-devel
BuildRequires: libgtk+3-devel libXpm-devel libXt-devel libminizip-devel
BuildRequires: libchromaprint-devel libvncserver-devel
BuildRequires: qt5-x11extras-devel libsecret-devel libgtk+2-devel libsoxr-devel libmpg123-devel qt5-svg-devel
BuildRequires: libnfs-devel libdca-devel libarchive-devel libprotobuf-lite-devel protobuf-compiler 
BuildRequires: libaom-devel libsamplerate-devel libsidplay2-devel
%{?_enable_freerdp:BuildRequires: libfreerdp-devel}
%{?_enable_goom:BuildRequires: libgoom-devel}
%{?_enable_firewire:BuildRequires: libdc1394-devel libraw1394-devel libavc1394-devel}
%{?_enable_visualization:BuildRequires: libprojectM-devel}
%{?_enable_wayland:BuildRequires: libwayland-egl-devel wayland-protocols}
BuildRequires: fortune-mod >= 1.0-ipl33mdk

%define allplugins aa ass audiocd bluray chromaprint dbus %{?_enable_firewire:dv} dvdnav dvdread ffmpeg flac framebuffer fluidsynth freetype globalhotkeys gnutls h264 h265 jack linsys live555 matroska modplug mpeg2 mtp musepack notify ogg opus png podcast pulseaudio realrtsp schroedinger shout smb speex svg taglib theora twolame upnp v4l videocd vpx xcb xml %{?_enable_goom:goom} %{?_enable_visualization:projectm}
%define baseplugins ass bluray dbus dvdnav dvdread ffmpeg freetype globalhotkeys live555 matroska mpeg2 ogg pulseaudio taglib v4l xcb xml
%define restplugins %(echo %allplugins %baseplugins |tr '[[:space:]]' '\\n'|sort |uniq -u|tr '\\n' ' ')
%define mergedplugins alsa dvb ts

%define vlcrequires() %(for p in %{*}; do printf 'Requires: vlc-plugin-%%s = %%s\\n' $p %version-%release; done)
%define vlcobsolete() %(for p in %{*}; do printf 'Provides: vlc-plugin-%%s = %%s\\nObsoletes: vlc-plugin-%%s\\n' $p %version-%release $p;done)

Requires: vlc-mini = %EVR
Requires: vlc-interface-qt = %EVR
%vlcrequires %baseplugins

Provides: %name-common = %EVR
Obsoletes: %name-common < %EVR
Provides: %name-normal = %EVR
Obsoletes: %name-normal < %EVR
Provides: %name-kde4 = %EVR
Obsoletes: %name-kde4
Obsoletes: %name-mad

%package mini
Summary: Minimalist version of VLC media player
Group: Video
Requires: lib%name = %EVR
%vlcobsolete %mergedplugins

%package maxi
Summary: Maxi package for VLC media player
Group: Video
Requires: vlc
Requires: vlc-interface-ncurses
Requires: vlc-interface-skins2
Requires: vlc-interface-lirc
Requires: vim-plugin-vlc-syntax
%vlcrequires %restplugins
BuildArch: noarch

%package interface-lirc
Summary: Lirc inteface plugin for VLC media player
Group: Video
Requires: lib%name = %EVR
Provides: vlc-plugin-lirc = %EVR
Obsoletes: vlc-plugin-lirc

%package interface-ncurses
Summary: ncurses plugin for VLC media player
Group: Video
Requires: lib%name = %EVR
Provides: %name-plugin-ncurses = %EVR

%package interface-skins2
Summary: Skins2 plugin for VLC media player
Group: Video
Requires: lib%name = %EVR
Requires: vlc-interface-qt = %EVR

%package interface-qt
Summary: QT interface plugin for VLC media player
Group: Video
Requires: lib%name = %EVR
Provides: %name-plugin-qt4 = %EVR
Obsoletes: %name-interface-qt4 < %EVR
Provides: %name-interface-qt4 = %EVR
Obsoletes: vlc-interface-wxwidgets

%package -n lib%name
Summary: VLC media player library
Group: System/Libraries
License: LGPLv2
Conflicts: %name-mini < %EVR

%package -n lib%name-devel
Summary: Development files for VLC media player
Group: Development/C
License: LGPLv2
Requires: lib%name = %EVR

%package plugin-aa
Summary: ASCII art video output plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-ass
Summary: ASS codec (subtitles) plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-audiocd
Summary: AudioCD access plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-bluray
Summary: Bluray access plugin for VLC media player
Group: Video
Requires: lib%name = %EVR
Requires: libaacs

%package plugin-chromaprint
Summary: Audio fingerprinting plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-dbus
Summary: DBUS plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-dv
Summary: DC1394/DV (firewire) plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-dvdnav
Summary: DVDNav input plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-dvdread
Summary: DVDRead input (DVD without a menu) plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-ffmpeg
Summary: FFMPeg plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-flac
Summary: FLAC codec plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-framebuffer
Summary: Framebuffer output plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-fluidsynth
Summary: Fluidsynth codec plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-freetype
Summary: FreeType OSD plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-globalhotkeys
Summary: Global Hotkeys control plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-gnutls
Summary: GNU TLS plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-goom
Summary: GOOM plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-h264
Summary: h264 output plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-h265
Summary: h265 output plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-jack
Summary: Jack audio output plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-live555
Summary: LiveMedia (RTSP) demuxing support for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-linsys
Summary: Linear Systems access module for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-matroska
Summary: Matroska Video demuxer plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-modplug
Summary: modplug demuxer plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-mpeg2
Summary: MPEG1/2 codec plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-mtp
Summary: MTP Service Discovery plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-musepack
Summary: Musepack demuxer plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-notify
Summary: Notify SDP plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-ogg
Summary: OGG/Vorbis/Kate codec plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-opus
Summary: OPUS codec plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-png
Summary: PNG plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-podcast
Summary: Podcast SDP plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-projectm
Summary: ProjectM visualisation plugin for VLC media player
Group: Video
Requires: lib%name = %EVR
Requires: /usr/share/fonts/ttf/dejavu/DejaVuSans.ttf
Requires: /usr/share/fonts/ttf/dejavu/DejaVuSansMono.ttf

%package plugin-pulseaudio
Summary: PulseAudio output plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%if_enabled freerdp
%package plugin-rdp
Summary: RDP and VNC access plugin for VLC media player
Group: Video
Requires: lib%name = %EVR
%endif

%package plugin-realrtsp
Summary: REAL RTSP access plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-schroedinger
Summary: Dirac codec (via libschroedinger) plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-shout
Summary: SHOUT access output plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-smb
Summary: SMB access plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-snapshot
Summary: Snapshot video output plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-speex
Summary: speex codec support plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-svg
Summary: SVG plugin plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-taglib
Summary: Taglib meta engine plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-theora
Summary: Theora codec plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-twolame
Summary: TwoLAME encoding plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-upnp
Summary: Intel UPNP Service Discovery plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-v4l
Summary: Video4Linux input plugin for VLC media player
Group: Video
Provides: vlc-plugin-v4l2 = %EVR
Requires: lib%name = %EVR

%package plugin-videocd
Summary: VideoCD input plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-vpx
Summary: VP8 output plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-xcb
Summary: X11 output / Service Discovery plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package plugin-xml
Summary: XML plugin for VLC media player
Group: Video
Requires: lib%name = %EVR

%package -n vim-plugin-vlc-syntax
Summary: VIm syntax for VLC media player
Group: Video
BuildArch: noarch

%package -n fortunes-vlc
Summary: VLC fortunes
Group: Video
PreReq: fortune-mod >= 1.0-ipl33mdk
BuildArch: noarch

# {{{ descriptions

%description
VLC media player is a free network-aware MPEG1, MPEG2, MPEG4 (aka DivX),
DVD and many-many-more-player-and-streamer.

The VLC media player allows to play MPEG2 Transport Streams from the
network or from a file, as well as direct DVD playback.

This version includes MPEG1 support, direct DVD support, DVD decryption,
arbitrary, seeking in the stream, pause, fast forward and slow motion,
hardware YUV acceleration and a few new interface features including
drag'n'drop... and more more more. :)

%description mini
VLC media player is a free network-aware MPEG1, MPEG2, MPEG4 (aka DivX),
DVD and many-many-more-player-and-streamer.

The VLC media player allows to play MPEG2 Transport Streams from the
network or from a file, as well as direct DVD playback.

This version includes MPEG1 support, direct DVD support, DVD decryption,
arbitrary, seeking in the stream, pause, fast forward and slow motion,
hardware YUV acceleration and a few new interface features including
drag'n'drop... and more more more. :)

You probably should install vlc package instead of this one.

%description maxi
This is a virtual package with every plugin or feature of VLC media player.

%description -n lib%name
This is a base VLC library.

%description -n lib%name-devel
This package provides files needed to develop plugins for VLC media player.

%description interface-lirc
This package is an infrared lirc interface for VLC media player.
To activate it, use the `--intf lirc' flag.

%description interface-ncurses
This package is an ncurses interface for VLC media player.

%description interface-skins2
This package is an skins2 interface for VLC media player.

%description interface-qt
This package is an QT interface for VLC media player.

%description plugin-aa
This is an ASCII art video output plugin for VLC media player.
To activate it, use the `--vout aa' flag or select the `aa'
vout plugin from the preferences menu.

%description plugin-ass
This package contains ASS subtitles support plugin for VLC media player.

%description plugin-audiocd
This package contains AudioCD access plugin for VLC media player.

%description plugin-bluray
This package contains Bluray disc access plugin for VLC media player.

%description plugin-chromaprint
This package contains client-side audio fingerprinting plugin,
based on AcoustID project chromaprint library.

%description plugin-dbus
This package contains DBUS control plugin for VLC media player.

%description plugin-dv
This package contains DC1394/DV (firewire) access plugin for VLC media player.

%description plugin-dvdnav
This package adds capability of DVDNav (DVD w/ menu) input to VLC media player.

%description plugin-dvdread
This package adds support of DVDRead (DVD w/o menu) input to VLC media player.

%description plugin-ffmpeg
This package adds support for ffmpeg decoders, encoders and demuxers
in VLC media player.

%description plugin-framebuffer
This package adds support for framebuffer video output in VLC media player.

%description plugin-flac
This package contains FLAC codec plugin for VLC media player.

%description plugin-fluidsynth
This package contains fluidsynth codec plugin for VLC media player.

%description plugin-freetype
This package contains freetype subtitles and OSD text output plugin 
to VLC media player.

%description plugin-globalhotkeys
This package contains Global Hotkeys control plugin for VLC media player.

%description plugin-gnutls
This package contains GNU TLS plugin for VLC media player.

%description plugin-goom
This package contains GOOM visualization plugin for VLC media player.

%description plugin-h264
This package contains h264 coder/packetizer plugin for VLC media player.

%description plugin-h265
This package contains h265 coder/packetizer plugin for VLC media player.

%description plugin-jack
This package contains Jack audio output plugin for VLC media player.

%description plugin-live555
This package contains LiveMedia (RTSP) demuxer support for VLC media player.

%description plugin-linsys
This package contains Linear Systems access plugins for VLC media player.

%description plugin-matroska
This package contains Matroska Video demuxing plugin for VLC media player.

%description plugin-modplug
This package contains modplug demuxing plugin for VLC media player.

%description plugin-mpeg2
This package contains MPEG1/2 decoder plugin for VLC media player.

%description plugin-mtp
This package contains MTP Service Discovery plugin for VLC media player.

%description plugin-musepack
This package contains musepack demuxer plugin for VLC media player.

%description plugin-notify
This package contains notify plugin for VLC media player.

%description plugin-ogg
This package contains OGG codec and Vorbis muxer/demuxer
plugin for VLC media player.

%description plugin-opus
This package contains OPUS codec plugin for VLC media player.

%description plugin-png
This package contains PNG codec plugin for VLC media player.

%description plugin-podcast
This package contains podcast discovery plugin for VLC media player.

%description plugin-projectm
This package contains ProjectM visualisation plugin for VLC media player.

%description plugin-pulseaudio
This package containts PulseAudio output plugin for VLC media player.

%description plugin-realrtsp
This package contains REAL RTSP access plugin for VLC media player.

%if_enabled freerdp
%description plugin-rdp
This package contains RDP and VNC access plugins for VLC media player.
%endif

%description plugin-schroedinger
This package contains dirac codec (via libschroedinger) plugin for VLC media
player.

%description plugin-shout
This package adds support for SHOUT output access/services discovery
to VLC media player.

%description plugin-smb
This package contains SMB access plugin to VLC media player.

%description plugin-snapshot
This package contains snapshot video output plugin to VLC media player.

%description plugin-speex
This package contains SPEEX plugin for VLC media player.

%description plugin-svg
This package contains SVG plugin for VLC media player.

%description plugin-taglib
This package contains taglib meta engine support for VLC media player.

%description plugin-theora
This package contains Theora codec support for VLC media player.

%description plugin-twolame
This package contains TwoLAME mpeg2 encoder plugin for VLC media player.

%description plugin-upnp
This package contains Intel UPNP Service Discovery plugin for VLC media player.

%description plugin-v4l
This package adds support for Video4Linux and Video4Linux2 to VLC media player.

%description plugin-videocd
This package contains VideoCD access plugin for VLC media player.

%description plugin-vpx
This package contains VP8 coder/packetizer plugin for VLC media player.

%description plugin-xcb
This package adds support for XCB video output and Service Discovery to VLC
media player.

%description plugin-xml
This package contains XML plugin to VLC media player.

%description -n vim-plugin-vlc-syntax
This package contains VIm syntax for VLC media player.

%description -n fortunes-vlc
This package contains fortunes from VLC media player.

# }}}

%define vlc_libdir %_libdir/%name
%define vlc_plugindir %vlc_libdir/plugins

%prep
%setup
echo %version-%release > src/revision.txt
%ifarch %e2k
# lcc 1.23 isn't quite gcc5 regarding builtins as well
%patch -p1
# EDG frontend bug
sed -i 's,const ATTR_USED,const,' modules/video_filter/deinterlace/yadif.h
# modules/demux/adaptive/PlaylistManager.cpp:638: undefined reference to `__pthread_register_cancel' ...
%add_optflags -pthread
%endif
%patch1 -p1

%build
%add_optflags -I%_includedir/samba-4.0
export BUILDCC=gcc

./bootstrap

%configure \
	%{subst_enable debug} \
	--disable-rpath \
	--disable-static \
	--enable-a52 \
	--enable-aa \
	--enable-alsa \
	--enable-avcodec \
	--enable-avformat \
	--enable-dca \
	--enable-dvbpsi \
	--enable-dvdnav \
	--enable-dvdread \
	--enable-egl \
	--enable-flac \
	--enable-freetype \
	--enable-fribidi \
	--enable-gles2 \
	--enable-gnutls \
	%{subst_enable goom} \
	--enable-httpd \
	--enable-jack \
	--enable-kate \
	--enable-libass \
	--enable-libcddb \
	--enable-libmpeg2 \
	--enable-libxml2 \
	--enable-lirc \
	--enable-live555 \
	--enable-mad \
	--enable-mkv \
	--enable-mod \
	--enable-mpc \
	--enable-ncurses \
	--enable-notify \
	--enable-ogg \
	--enable-omxil \
	--enable-omxil-vout \
	--enable-opus \
	--enable-png \
	--enable-postproc \
	--enable-pulse \
	--enable-realrtsp \
	--enable-schroedinger \
	--enable-sftp \
	--enable-shout \
	--enable-skins2 \
	--enable-smbclient \
	--enable-speex \
	--enable-svg \
	--enable-swscale \
	--enable-theora \
	--enable-twolame \
	--enable-upnp \
	--enable-vcd \
	--enable-vcdx \
	--enable-vlm \
	--enable-vorbis \
	--enable-x264 \
	--enable-xcb \
	--enable-wayland \
	%{subst_enable freerdp} \
%if_enabled firewire
	--enable-dc1394 \
	--enable-dv1394 \
%endif
%if_enabled visualization
	--enable-projectm \
%endif
	--disable-oss \
	--disable-quicktime \
	--disable-sdl \
	--with-kde-solid=%_datadir/kf5/solid/actions \
	--without-contrib \
        --with-default-font=/usr/share/fonts/ttf/dejavu/DejaVuSerif-Bold.ttf \
        --with-default-monospace-font=/usr/share/fonts/ttf/dejavu/DejaVuSansMono.ttf \
	--with-default-font-family="Sans Serif" \
	--with-default-monospace-font-family="Monospace" \
	#

%make_build

%install

mkdir -p %buildroot%_libdir
%make_install DESTDIR="%buildroot" install

install -pD -m644 doc/vlc.1 %buildroot/%_man1dir/vlc.1

# freedesktop menu
mkdir -p %buildroot%_datadir/applications 
install -pm644 share/vlc.desktop %buildroot%_datadir/applications/vlc.desktop

# remove non-packaged files
rm -rf %buildroot%_docdir/%name
find %buildroot -type f -name "*.la" -print -delete

# vim stuff
mkdir -p %buildroot%vim_syntax_dir
cp extras/analyser/vlc.vim %buildroot%vim_syntax_dir/

# fortunes stuff
mkdir -p %buildroot%_gamesdatadir/fortune
cp doc/fortunes.txt %buildroot%_gamesdatadir/fortune/vlc
strfile %buildroot%_gamesdatadir/fortune/vlc %buildroot%_gamesdatadir/fortune/vlc.dat

# vlc filetrigger to regenerate cache
mkdir -p %buildroot%_libexecdir/rpm

cat << __EOF__ > %buildroot%_libexecdir/rpm/vlc.filetrigger
#!/bin/sh -e
grep -qs '^%vlc_plugindir/.*\.so\$' || exit 0
%vlc_libdir/vlc-cache-gen %vlc_plugindir ||:
__EOF__

chmod 755 %buildroot%_libexecdir/rpm/vlc.filetrigger

%find_lang --output=%name.files %name

%files mini -f %name.files
%_bindir/vlc
%_bindir/cvlc
%_bindir/rvlc
%_bindir/vlc-wrapper
%vlc_libdir/vlc-cache-gen
%_libexecdir/rpm/vlc.filetrigger
%dir %vlc_libdir
%dir %vlc_plugindir
%exclude %_datadir/%name/skins2
%_datadir/%name
%dir %_datadir/metainfo
%_datadir/metainfo/vlc.appdata.xml
%_man1dir/*

%_iconsdir/hicolor/*/apps/vlc*.png
%_iconsdir/hicolor/*/apps/vlc*.xpm

%dir %vlc_plugindir/access
%vlc_plugindir/access/libaccess_alsa_plugin.so
%vlc_plugindir/access/libaccess_concat_plugin.so
%vlc_plugindir/access/libaccess_imem_plugin.so
%vlc_plugindir/access/libaccess_mms_plugin.so
%vlc_plugindir/access/libattachment_plugin.so
%vlc_plugindir/access/libdtv_plugin.so
%vlc_plugindir/access/libdvb_plugin.so
%vlc_plugindir/access/libfilesystem_plugin.so
%vlc_plugindir/access/libftp_plugin.so
%vlc_plugindir/access/libhttp_plugin.so
%vlc_plugindir/access/libhttps_plugin.so
%vlc_plugindir/access/libidummy_plugin.so
%vlc_plugindir/access/libimem_plugin.so
%vlc_plugindir/access/libnfs_plugin.so
%vlc_plugindir/access/librtp_plugin.so
%vlc_plugindir/access/libsatip_plugin.so
%vlc_plugindir/access/libsdp_plugin.so
%vlc_plugindir/access/libsftp_plugin.so
%vlc_plugindir/access/libshm_plugin.so
%vlc_plugindir/access/libtcp_plugin.so
%vlc_plugindir/access/libtimecode_plugin.so
%vlc_plugindir/access/libudp_plugin.so
%vlc_plugindir/access/libvdr_plugin.so
%vlc_plugindir/access/libvnc_plugin.so

%dir %vlc_plugindir/access_output
%vlc_plugindir/access_output/libaccess_output_dummy_plugin.so
%vlc_plugindir/access_output/libaccess_output_file_plugin.so
%vlc_plugindir/access_output/libaccess_output_http_plugin.so
%vlc_plugindir/access_output/libaccess_output_udp_plugin.so
%vlc_plugindir/access_output/libaccess_output_livehttp_plugin.so

%dir %vlc_plugindir/audio_filter
%vlc_plugindir/audio_filter/libscaletempo_pitch_plugin.so
%vlc_plugindir/audio_filter/libdolby_surround_decoder_plugin.so
%vlc_plugindir/audio_filter/libheadphone_channel_mixer_plugin.so
%vlc_plugindir/audio_filter/libtrivial_channel_mixer_plugin.so
%vlc_plugindir/audio_filter/libugly_resampler_plugin.so
%vlc_plugindir/audio_filter/libaudio_format_plugin.so
%vlc_plugindir/audio_filter/libequalizer_plugin.so
%vlc_plugindir/audio_filter/libnormvol_plugin.so
%vlc_plugindir/audio_filter/libsamplerate_plugin.so
%vlc_plugindir/audio_filter/libsimple_channel_mixer_plugin.so
%vlc_plugindir/audio_filter/libparam_eq_plugin.so
%vlc_plugindir/audio_filter/libmad_plugin.so
%vlc_plugindir/audio_filter/libmono_plugin.so
%vlc_plugindir/audio_filter/libscaletempo_plugin.so
%vlc_plugindir/audio_filter/libspatializer_plugin.so
%vlc_plugindir/audio_filter/libaudiobargraph_a_plugin.so
%vlc_plugindir/audio_filter/libchorus_flanger_plugin.so
%vlc_plugindir/audio_filter/libcompressor_plugin.so
%vlc_plugindir/audio_filter/libkaraoke_plugin.so
%vlc_plugindir/audio_filter/libgain_plugin.so
%vlc_plugindir/audio_filter/libremap_plugin.so
%vlc_plugindir/audio_filter/libsoxr_plugin.so
%vlc_plugindir/audio_filter/libstereo_widen_plugin.so
%vlc_plugindir/audio_filter/libtospdif_plugin.so

%dir %vlc_plugindir/audio_mixer
%vlc_plugindir/audio_mixer/libfloat_mixer_plugin.so
%vlc_plugindir/audio_mixer/libinteger_mixer_plugin.so

%dir %vlc_plugindir/audio_output
%vlc_plugindir/audio_output/libalsa_plugin.so
%vlc_plugindir/audio_output/libafile_plugin.so
%vlc_plugindir/audio_output/libadummy_plugin.so
%vlc_plugindir/audio_output/libamem_plugin.so

%dir %vlc_plugindir/codec
%vlc_plugindir/codec/liba52_plugin.so
%vlc_plugindir/codec/libadpcm_plugin.so
%vlc_plugindir/codec/libaes3_plugin.so
%vlc_plugindir/codec/libaom_plugin.so
%vlc_plugindir/codec/libaraw_plugin.so
%vlc_plugindir/codec/libcc_plugin.so
%vlc_plugindir/codec/libcdg_plugin.so
%vlc_plugindir/codec/libcvdsub_plugin.so
%vlc_plugindir/codec/libddummy_plugin.so
%vlc_plugindir/codec/libdca_plugin.so
%vlc_plugindir/codec/libdvbsub_plugin.so
%vlc_plugindir/codec/libedummy_plugin.so
%vlc_plugindir/codec/libg711_plugin.so
%vlc_plugindir/codec/libjpeg_plugin.so
%vlc_plugindir/codec/liblpcm_plugin.so
%vlc_plugindir/codec/libmpg123_plugin.so
%vlc_plugindir/codec/liboggspots_plugin.so
%vlc_plugindir/codec/libomxil_plugin.so
%vlc_plugindir/codec/libomxil_vout_plugin.so
%vlc_plugindir/codec/librawvideo_plugin.so
%vlc_plugindir/codec/librtpvideo_plugin.so
%vlc_plugindir/codec/libscte18_plugin.so
%vlc_plugindir/codec/libscte27_plugin.so
%vlc_plugindir/codec/libspdif_plugin.so
%vlc_plugindir/codec/libspudec_plugin.so
%vlc_plugindir/codec/libstl_plugin.so
%vlc_plugindir/codec/libsubsdec_plugin.so
%vlc_plugindir/codec/libsubstx3g_plugin.so
%vlc_plugindir/codec/libsubsusf_plugin.so
%vlc_plugindir/codec/libt140_plugin.so
%vlc_plugindir/codec/libtelx_plugin.so
%vlc_plugindir/codec/libtextst_plugin.so
%vlc_plugindir/codec/libttml_plugin.so
%vlc_plugindir/codec/libuleaddvaudio_plugin.so
%vlc_plugindir/codec/libvaapi_plugin.so
%vlc_plugindir/codec/libwebvtt_plugin.so
%vlc_plugindir/codec/libxwd_plugin.so

%dir %vlc_plugindir/control
%vlc_plugindir/control/liboldrc_plugin.so
%vlc_plugindir/control/libgestures_plugin.so
%vlc_plugindir/control/libhotkeys_plugin.so
%vlc_plugindir/control/libmotion_plugin.so
%vlc_plugindir/control/libnetsync_plugin.so
%vlc_plugindir/control/libdummy_plugin.so

%dir %vlc_plugindir/demux
%vlc_plugindir/demux/libadaptive_plugin.so
%vlc_plugindir/demux/libaiff_plugin.so
%vlc_plugindir/demux/libasf_plugin.so
%vlc_plugindir/demux/libau_plugin.so
%vlc_plugindir/demux/libavi_plugin.so
%vlc_plugindir/demux/libcaf_plugin.so
%vlc_plugindir/demux/libdemux_cdg_plugin.so
%vlc_plugindir/demux/libdemux_chromecast_plugin.so
%vlc_plugindir/demux/libdemux_stl_plugin.so
%vlc_plugindir/demux/libdemuxdump_plugin.so
%vlc_plugindir/demux/libdiracsys_plugin.so
%vlc_plugindir/demux/libdirectory_demux_plugin.so
%vlc_plugindir/demux/libes_plugin.so
%vlc_plugindir/demux/libh26x_plugin.so
%vlc_plugindir/demux/libimage_plugin.so
%vlc_plugindir/demux/libmjpeg_plugin.so
%vlc_plugindir/demux/libmp4_plugin.so
%vlc_plugindir/demux/libmpgv_plugin.so
%vlc_plugindir/demux/libnoseek_plugin.so
%vlc_plugindir/demux/libnsc_plugin.so
%vlc_plugindir/demux/libnsv_plugin.so
%vlc_plugindir/demux/libnuv_plugin.so
%vlc_plugindir/demux/libplaylist_plugin.so
%vlc_plugindir/demux/libps_plugin.so
%vlc_plugindir/demux/libpva_plugin.so
%vlc_plugindir/demux/librawaud_plugin.so
%vlc_plugindir/demux/librawdv_plugin.so
%vlc_plugindir/demux/librawvid_plugin.so
%vlc_plugindir/demux/libreal_plugin.so
%vlc_plugindir/demux/libsmf_plugin.so
%vlc_plugindir/demux/libsid_plugin.so
%vlc_plugindir/demux/libsubtitle_plugin.so
%vlc_plugindir/demux/libts_plugin.so
%vlc_plugindir/demux/libtta_plugin.so
%vlc_plugindir/demux/libty_plugin.so
%vlc_plugindir/demux/libvc1_plugin.so
%vlc_plugindir/demux/libvobsub_plugin.so
%vlc_plugindir/demux/libvoc_plugin.so
%vlc_plugindir/demux/libwav_plugin.so
%vlc_plugindir/demux/libxa_plugin.so

%dir %vlc_plugindir/gui

%dir %vlc_plugindir/keystore
%vlc_plugindir/keystore/libfile_keystore_plugin.so
%vlc_plugindir/keystore/libkwallet_plugin.so
%vlc_plugindir/keystore/libmemory_keystore_plugin.so
%vlc_plugindir/keystore/libsecret_plugin.so

%dir %vlc_plugindir/logger
%vlc_plugindir/logger/libconsole_logger_plugin.so
%vlc_plugindir/logger/libfile_logger_plugin.so
%vlc_plugindir/logger/libsyslog_plugin.so

%dir %vlc_plugindir/misc
%vlc_plugindir/misc/liblogger_plugin.so
%vlc_plugindir/misc/libvod_rtsp_plugin.so
%vlc_plugindir/misc/libexport_plugin.so
%vlc_plugindir/misc/libaudioscrobbler_plugin.so
%vlc_plugindir/misc/libstats_plugin.so
%vlc_plugindir/misc/libfingerprinter_plugin.so
%vlc_plugindir/misc/libxdg_screensaver_plugin.so
%vlc_plugindir/misc/libaddonsfsstorage_plugin.so
%vlc_plugindir/misc/libaddonsvorepository_plugin.so

%ifarch ppc ppc64
%dir %vlc_plugindir/altivec
%vlc_plugindir/altivec/libmemcpyaltivec_plugin.so
%vlc_plugindir/altivec/libi420_yuy2_altivec_plugin.so
%endif

%dir %vlc_plugindir/video_splitter
%vlc_plugindir/video_splitter/libclone_plugin.so
%vlc_plugindir/video_splitter/libwall_plugin.so

%dir %vlc_plugindir/services_discovery
%vlc_plugindir/services_discovery/libavahi_plugin.so
%vlc_plugindir/services_discovery/libmediadirs_plugin.so
%vlc_plugindir/services_discovery/libsap_plugin.so
%vlc_plugindir/services_discovery/libudev_plugin.so

%dir %vlc_plugindir/mux
%vlc_plugindir/mux/libmux_asf_plugin.so
%vlc_plugindir/mux/libmux_avi_plugin.so
%vlc_plugindir/mux/libmux_dummy_plugin.so
%vlc_plugindir/mux/libmux_mp4_plugin.so
%vlc_plugindir/mux/libmux_mpjpeg_plugin.so
%vlc_plugindir/mux/libmux_ps_plugin.so
%vlc_plugindir/mux/libmux_ts_plugin.so
%vlc_plugindir/mux/libmux_wav_plugin.so

%dir %vlc_plugindir/packetizer
%vlc_plugindir/packetizer/libpacketizer_a52_plugin.so
%vlc_plugindir/packetizer/libpacketizer_copy_plugin.so
%vlc_plugindir/packetizer/libpacketizer_dts_plugin.so
%vlc_plugindir/packetizer/libpacketizer_hevc_plugin.so
%vlc_plugindir/packetizer/libpacketizer_av1_plugin.so
%vlc_plugindir/packetizer/libpacketizer_mpeg4audio_plugin.so
%vlc_plugindir/packetizer/libpacketizer_mpeg4video_plugin.so
%vlc_plugindir/packetizer/libpacketizer_mpegaudio_plugin.so
%vlc_plugindir/packetizer/libpacketizer_mpegvideo_plugin.so
%vlc_plugindir/packetizer/libpacketizer_vc1_plugin.so
%vlc_plugindir/packetizer/libpacketizer_mlp_plugin.so
%vlc_plugindir/packetizer/libpacketizer_dirac_plugin.so
%vlc_plugindir/packetizer/libpacketizer_flac_plugin.so

%dir %vlc_plugindir/spu
%vlc_plugindir/spu/libaudiobargraph_v_plugin.so
%vlc_plugindir/spu/libdynamicoverlay_plugin.so
%vlc_plugindir/spu/liblogo_plugin.so
%vlc_plugindir/spu/libmarq_plugin.so
%vlc_plugindir/spu/libmosaic_plugin.so
%vlc_plugindir/spu/libremoteosd_plugin.so
%vlc_plugindir/spu/librss_plugin.so
%vlc_plugindir/spu/libsubsdelay_plugin.so

%dir %vlc_plugindir/stream_extractor
%vlc_plugindir/stream_extractor/libarchive_plugin.so

%dir %vlc_plugindir/stream_out
%vlc_plugindir/stream_out/libstream_out_chromecast_plugin.so
%vlc_plugindir/stream_out/libstream_out_display_plugin.so
%vlc_plugindir/stream_out/libstream_out_dummy_plugin.so
%vlc_plugindir/stream_out/libstream_out_duplicate_plugin.so
%vlc_plugindir/stream_out/libstream_out_es_plugin.so
%vlc_plugindir/stream_out/libstream_out_standard_plugin.so
%vlc_plugindir/stream_out/libstream_out_bridge_plugin.so
%vlc_plugindir/stream_out/libstream_out_cycle_plugin.so
%vlc_plugindir/stream_out/libstream_out_description_plugin.so
%vlc_plugindir/stream_out/libstream_out_gather_plugin.so
%vlc_plugindir/stream_out/libstream_out_mosaic_bridge_plugin.so
%vlc_plugindir/stream_out/libstream_out_rtp_plugin.so
%vlc_plugindir/stream_out/libstream_out_stats_plugin.so
%vlc_plugindir/stream_out/libstream_out_transcode_plugin.so
%vlc_plugindir/stream_out/libstream_out_autodel_plugin.so
%vlc_plugindir/stream_out/libstream_out_record_plugin.so
%vlc_plugindir/stream_out/libstream_out_smem_plugin.so
%vlc_plugindir/stream_out/libstream_out_delay_plugin.so
%vlc_plugindir/stream_out/libstream_out_setid_plugin.so

%dir %vlc_plugindir/stream_filter
%vlc_plugindir/stream_filter/libdecomp_plugin.so
%vlc_plugindir/stream_filter/librecord_plugin.so
%vlc_plugindir/stream_filter/libadf_plugin.so
%vlc_plugindir/stream_filter/libcache_block_plugin.so
%vlc_plugindir/stream_filter/libcache_read_plugin.so
%vlc_plugindir/stream_filter/libhds_plugin.so
%vlc_plugindir/stream_filter/libinflate_plugin.so
%vlc_plugindir/stream_filter/libprefetch_plugin.so
%vlc_plugindir/stream_filter/libskiptags_plugin.so

%dir %vlc_plugindir/text_renderer
%vlc_plugindir/text_renderer/libtdummy_plugin.so

%dir %vlc_plugindir/video_chroma
%vlc_plugindir/video_chroma/libchain_plugin.so
%vlc_plugindir/video_chroma/libi420_10_p010_plugin.so
%vlc_plugindir/video_chroma/libi420_nv12_plugin.so
%vlc_plugindir/video_chroma/libi420_rgb_plugin.so
%vlc_plugindir/video_chroma/libi420_yuy2_plugin.so
%vlc_plugindir/video_chroma/libi422_yuy2_plugin.so
%vlc_plugindir/video_chroma/libgrey_yuv_plugin.so
%vlc_plugindir/video_chroma/libi422_i420_plugin.so
%vlc_plugindir/video_chroma/libyuy2_i420_plugin.so
%vlc_plugindir/video_chroma/libyuy2_i422_plugin.so
%vlc_plugindir/video_chroma/libyuvp_plugin.so
%vlc_plugindir/video_chroma/librv32_plugin.so
%ifarch %ix86 x86_64
%vlc_plugindir/video_chroma/libi420_rgb_mmx_plugin.so
%vlc_plugindir/video_chroma/libi420_yuy2_mmx_plugin.so
%vlc_plugindir/video_chroma/libi422_yuy2_mmx_plugin.so
%vlc_plugindir/video_chroma/libi420_rgb_sse2_plugin.so
%vlc_plugindir/video_chroma/libi420_yuy2_sse2_plugin.so
%vlc_plugindir/video_chroma/libi422_yuy2_sse2_plugin.so
%endif

%dir %vlc_plugindir/video_filter
%vlc_plugindir/video_filter/libadjust_plugin.so
%vlc_plugindir/video_filter/libalphamask_plugin.so
%vlc_plugindir/video_filter/libantiflicker_plugin.so
%vlc_plugindir/video_filter/libball_plugin.so
%vlc_plugindir/video_filter/libblend_plugin.so
%vlc_plugindir/video_filter/libblendbench_plugin.so
%vlc_plugindir/video_filter/libbluescreen_plugin.so
%vlc_plugindir/video_filter/libcanvas_plugin.so
%vlc_plugindir/video_filter/libcolorthres_plugin.so
%vlc_plugindir/video_filter/libcroppadd_plugin.so
%vlc_plugindir/video_filter/libdeinterlace_plugin.so
%vlc_plugindir/video_filter/libedgedetection_plugin.so
%vlc_plugindir/video_filter/liberase_plugin.so
%vlc_plugindir/video_filter/libextract_plugin.so
%vlc_plugindir/video_filter/libfps_plugin.so
%vlc_plugindir/video_filter/libfreeze_plugin.so
%vlc_plugindir/video_filter/libgaussianblur_plugin.so
%vlc_plugindir/video_filter/libgradfun_plugin.so
%vlc_plugindir/video_filter/libgradient_plugin.so
%vlc_plugindir/video_filter/libgrain_plugin.so
%vlc_plugindir/video_filter/libhqdn3d_plugin.so
%vlc_plugindir/video_filter/libinvert_plugin.so
%vlc_plugindir/video_filter/libmagnify_plugin.so
%vlc_plugindir/video_filter/libmirror_plugin.so
%vlc_plugindir/video_filter/libmotionblur_plugin.so
%vlc_plugindir/video_filter/libmotiondetect_plugin.so
%vlc_plugindir/video_filter/liboldmovie_plugin.so
%vlc_plugindir/video_filter/libposterize_plugin.so
%vlc_plugindir/video_filter/libpsychedelic_plugin.so
%vlc_plugindir/video_filter/libpuzzle_plugin.so
%vlc_plugindir/video_filter/libripple_plugin.so
%vlc_plugindir/video_filter/librotate_plugin.so
%vlc_plugindir/video_filter/libscale_plugin.so
%vlc_plugindir/video_filter/libscene_plugin.so
%vlc_plugindir/video_filter/libsepia_plugin.so
%vlc_plugindir/video_filter/libsharpen_plugin.so
%vlc_plugindir/video_filter/libtransform_plugin.so
%vlc_plugindir/video_filter/libwave_plugin.so
%vlc_plugindir/video_filter/libvhs_plugin.so

%dir %vlc_plugindir/video_output
%vlc_plugindir/video_output/libglconv_vaapi_drm_plugin.so
%vlc_plugindir/video_output/libglconv_vaapi_wl_plugin.so
%vlc_plugindir/video_output/libglconv_vaapi_x11_plugin.so
%vlc_plugindir/video_output/libglconv_vdpau_plugin.so
%vlc_plugindir/video_output/libvdummy_plugin.so
%vlc_plugindir/video_output/libvmem_plugin.so
%vlc_plugindir/video_output/libyuv_plugin.so
%vlc_plugindir/video_output/libegl_wl_plugin.so
%vlc_plugindir/video_output/libflaschen_plugin.so
%vlc_plugindir/video_output/libwl_shell_plugin.so
%vlc_plugindir/video_output/libwl_shm_plugin.so
%vlc_plugindir/video_output/libxdg_shell_plugin.so

%dir %vlc_plugindir/visualization
%vlc_plugindir/visualization/libvisual_plugin.so

%dir %vlc_plugindir/meta_engine
%vlc_plugindir/meta_engine/libfolder_plugin.so

%vlc_plugindir/lua
%vlc_libdir/lua


%doc AUTHORS README NEWS THANKS

%files interface-ncurses
%_bindir/nvlc
%vlc_plugindir/gui/libncurses_plugin.so

%files interface-skins2
%_bindir/svlc
%vlc_plugindir/gui/libskins2_plugin.so
%_datadir/%name/skins2

%files interface-lirc
%vlc_plugindir/control/liblirc_plugin.so

%files interface-qt
%_bindir/qvlc
%vlc_plugindir/gui/libqt_plugin.so
%_datadir/applications/vlc.desktop

%files plugin-schroedinger
%vlc_plugindir/codec/libschroedinger_plugin.so

%files plugin-jack
%vlc_plugindir/audio_output/libjack_plugin.so
%vlc_plugindir/access/libaccess_jack_plugin.so

%files plugin-bluray
%vlc_plugindir/access/liblibbluray_plugin.so

%files plugin-linsys
%vlc_plugindir/access/liblinsys_sdi_plugin.so
%vlc_plugindir/access/liblinsys_hdsdi_plugin.so

%if_enabled goom
%files plugin-goom
%vlc_plugindir/visualization/libgoom_plugin.so
%endif

%files plugin-v4l
%vlc_plugindir/access/libv4l2_plugin.so

%files plugin-live555
%vlc_plugindir/access/liblive555_plugin.so

%files plugin-matroska
%vlc_plugindir/demux/libmkv_plugin.so

%files plugin-modplug
%vlc_plugindir/demux/libmod_plugin.so

%files plugin-mpeg2
%vlc_plugindir/codec/liblibmpeg2_plugin.so
%vlc_plugindir/codec/libzvbi_plugin.so

%files plugin-mtp
%vlc_plugindir/access/libaccess_mtp_plugin.so
%vlc_plugindir/services_discovery/libmtp_plugin.so

%files plugin-musepack
%vlc_plugindir/demux/libmpc_plugin.so

%files plugin-notify
%vlc_plugindir/notify/libnotify_plugin.so

%files plugin-speex
%vlc_plugindir/codec/libspeex_plugin.so
%vlc_plugindir/audio_filter/libspeex_resampler_plugin.so

%files plugin-ogg
%vlc_plugindir/mux/libmux_ogg_plugin.so
%vlc_plugindir/demux/libogg_plugin.so
%vlc_plugindir/codec/libvorbis_plugin.so
%vlc_plugindir/codec/libkate_plugin.so

%files plugin-opus
%vlc_plugindir/codec/libopus_plugin.so

%files plugin-flac
%vlc_plugindir/demux/libflacsys_plugin.so
%vlc_plugindir/codec/libflac_plugin.so

%files plugin-fluidsynth
%vlc_plugindir/codec/libfluidsynth_plugin.so

%files plugin-h264
%vlc_plugindir/codec/libx264_plugin.so
%vlc_plugindir/packetizer/libpacketizer_h264_plugin.so

%files plugin-h265
%vlc_plugindir/codec/libx265_plugin.so

%files plugin-vpx
%vlc_plugindir/codec/libvpx_plugin.so

%files plugin-aa
%vlc_plugindir/video_output/libaa_plugin.so

%files plugin-chromaprint
%vlc_plugindir/stream_out/libstream_out_chromaprint_plugin.so

%files plugin-taglib
%vlc_plugindir/meta_engine/libtaglib_plugin.so

%files plugin-theora
%vlc_plugindir/codec/libtheora_plugin.so

%files plugin-globalhotkeys
#vlc_plugindir/control/libglobalhotkeys_plugin.so

%files plugin-ffmpeg
%vlc_plugindir/access/libavio_plugin.so
%vlc_plugindir/codec/libavcodec_plugin.so
%vlc_plugindir/demux/libavformat_plugin.so
%vlc_plugindir/video_chroma/libswscale_plugin.so
%vlc_plugindir/video_filter/libpostproc_plugin.so
%vlc_plugindir/packetizer/libpacketizer_avparser_plugin.so

%files plugin-framebuffer
%vlc_plugindir/video_output/libfb_plugin.so

%files plugin-shout
%vlc_plugindir/access_output/libaccess_output_shout_plugin.so

%if_enabled freerdp
%files plugin-rdp
%vlc_plugindir/access/libvnc_plugin.so
%vlc_plugindir/access/librdp_plugin.so
%endif

%files plugin-xcb
%dir %vlc_plugindir/vdpau
%dir %vlc_plugindir/vaapi
%_libdir/vlc/libvlc_vdpau.so*
%vlc_plugindir/access/libxcb_screen_plugin.so
%vlc_plugindir/codec/libvaapi_drm_plugin.so
%vlc_plugindir/control/libxcb_hotkeys_plugin.so
%vlc_plugindir/services_discovery/libxcb_apps_plugin.so
%vlc_plugindir/vdpau/libvdpau_sharpen_plugin.so
%vlc_plugindir/vdpau/libvdpau_display_plugin.so
%vlc_plugindir/vdpau/libvdpau_deinterlace_plugin.so
%vlc_plugindir/vdpau/libvdpau_avcodec_plugin.so
%vlc_plugindir/vdpau/libvdpau_adjust_plugin.so
%vlc_plugindir/vdpau/libvdpau_chroma_plugin.so
%vlc_plugindir/vaapi/libvaapi_filters_plugin.so
%vlc_plugindir/video_output/libxcb_window_plugin.so
%vlc_plugindir/video_output/libxcb_x11_plugin.so
%vlc_plugindir/video_output/libxcb_xv_plugin.so
%vlc_plugindir/video_output/libegl_x11_plugin.so
%vlc_plugindir/video_output/libgl_plugin.so
%vlc_plugindir/video_output/libgles2_plugin.so
%vlc_plugindir/video_output/libglx_plugin.so
%vlc_plugindir/video_filter/libanaglyph_plugin.so
%vlc_plugindir/video_splitter/libpanoramix_plugin.so
%vlc_plugindir/visualization/libglspectrum_plugin.so

%files plugin-xml
%vlc_plugindir/misc/libxml_plugin.so

%files plugin-png
%vlc_plugindir/codec/libpng_plugin.so

%files plugin-podcast
%vlc_plugindir/services_discovery/libpodcast_plugin.so

%files plugin-pulseaudio
%vlc_plugindir/audio_output/libpulse_plugin.so
%vlc_plugindir/services_discovery/libpulselist_plugin.so
%vlc_plugindir/access/libpulsesrc_plugin.so

%files plugin-upnp
%vlc_plugindir/services_discovery/libupnp_plugin.so

%files plugin-realrtsp
%vlc_plugindir/access/libaccess_realrtsp_plugin.so

%files plugin-dbus
%vlc_plugindir/control/libdbus_plugin.so
%vlc_plugindir/misc/libdbus_screensaver_plugin.so

%if_enabled firewire
%files plugin-dv
%vlc_plugindir/access/libdc1394_plugin.so
%vlc_plugindir/access/libdv1394_plugin.so
%endif

%files plugin-twolame
%vlc_plugindir/codec/libtwolame_plugin.so

%files plugin-dvdnav
%vlc_plugindir/access/libdvdnav_plugin.so

%files plugin-dvdread
%vlc_plugindir/access/libdvdread_plugin.so

%files plugin-freetype
%vlc_plugindir/text_renderer/libfreetype_plugin.so

%files plugin-gnutls
%vlc_plugindir/misc/libgnutls_plugin.so

%files plugin-smb
%vlc_plugindir/access/libsmb_plugin.so

%files plugin-svg
%vlc_plugindir/codec/libsvgdec_plugin.so
%vlc_plugindir/text_renderer/libsvg_plugin.so

%files plugin-videocd
%vlc_plugindir/access/libvcd_plugin.so
%vlc_plugindir/codec/libsvcdsub_plugin.so

%files plugin-audiocd
%vlc_plugindir/access/libcdda_plugin.so

%files plugin-ass
%vlc_plugindir/codec/liblibass_plugin.so

%if_enabled visualization
%files plugin-projectm
%vlc_plugindir/visualization/libprojectm_plugin.so
%endif

%files -n lib%name
%_libdir/libvlccore.so.*
%_libdir/libvlc.so.*
%_libdir/vlc/libvlc_pulse.so.*
%_libdir/vlc/libvlc_xcb_events.so.*

%files -n lib%name-devel
%_pkgconfigdir/*.pc
%_includedir/*
%_libdir/vlc/libcompat.a
%_libdir/libvlccore.so
%_libdir/libvlc.so
%_libdir/vlc/libvlc_pulse.so
%_libdir/vlc/libvlc_xcb_events.so

%files -n vim-plugin-vlc-syntax
%vim_syntax_dir/vlc.vim

%files -n fortunes-vlc
%_gamesdatadir/fortune/vlc*

%files
%_datadir/kf5/solid/actions/vlc-openbd.desktop
%_datadir/kf5/solid/actions/vlc-opencda.desktop
%_datadir/kf5/solid/actions/vlc-opendvd.desktop
%_datadir/kf5/solid/actions/vlc-openvcd.desktop

%files maxi

%changelog
* Thu Apr 30 2020 Anton Farygin <rider@altlinux.ru> 3.0.10-alt1
- 3.0.10

* Sun Apr 12 2020 Anton Farygin <rider@altlinux.ru> 3.0.9.2-alt1
- 3.0.9.2

* Thu Mar 19 2020 Anton Farygin <rider@altlinux.ru> 3.0.8-alt3
- disabled libcaca support

* Tue Mar 03 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.0.8-alt2
- Fixed build on riscv64.

* Thu Aug 15 2019 Anton Farygin <rider@altlinux.ru> 3.0.8-alt1
- 3.0.8

* Sat Jun 15 2019 Anton Farygin <rider@altlinux.ru> 3.0.7.1-alt1
- 3.0.7.1

* Sun Jun 09 2019 Anton Farygin <rider@altlinux.ru> 3.0.7-alt1
- 3.0.7

* Sun May 05 2019 Michael Shigorin <mike@altlinux.org> 3.0.6-alt7
- fixed build on E2K
- fixed firewire knob

* Sun Apr 07 2019 Michael Shigorin <mike@altlinux.org> 3.0.6-alt6
- introduced firewire, visualization, wayland knobs (on by default)

* Mon Mar 25 2019 Alexey Shabalin <shaba@altlinux.org> 3.0.6-alt5
- fixed build with libssh2-1.8.1

* Sun Mar 10 2019 Anton Farygin <rider@altlinux.ru> 3.0.6-alt4
- fixed FTBFS by removing build requires of the old libsidplay package

* Thu Mar 07 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.0.6-alt3
- Added goom knob (disable by default to get rid of libgoom ->
  libxmms -> glib in Sisyphus).

* Thu Feb 21 2019 Anton Farygin <rider@altlinux.ru> 3.0.6-alt2
- added upstream path for build with libvpx-1.8.0

* Sat Jan 19 2019 Anton Farygin <rider@altlinux.ru> 3.0.6-alt1
- 3.0.6

* Sat Dec 29 2018 Anton Farygin <rider@altlinux.ru> 3.0.5.1-alt1
- 3.0.5-1

* Mon Dec 10 2018 Anton Farygin <rider@altlinux.ru> 3.0.5-alt0.git.bedc72800
- up to git bedc72800

* Thu Nov 08 2018 Anton Farygin <rider@altlinux.ru> 3.0.4-alt2
- built with libaom-devel libsamplerate-devel libsidplay2-devel
- changed solid actions path to kf5 defaults
- added chromecast plugin
- removed font-dejavu requires in freetype plugin (closes: #23213)

* Sun Sep 09 2018 Anton Farygin <rider@altlinux.ru> 3.0.4-alt1
- 3.0.4

* Mon Jul 09 2018 Anton Farygin <rider@altlinux.ru> 3.0.3.1-alt2
- rebuilt for libnfs-3.0

* Wed Jun 13 2018 Anton Farygin <rider@altlinux.ru> 3.0.3.1-alt1
- 3.0.3-1

* Fri Mar 02 2018 Anton Farygin <rider@altlinux.ru> 3.0.1-alt1
- 3.0.1

* Mon Feb 26 2018 Anton Farygin <rider@altlinux.ru> 3.0.0.2-alt1
- 3.0.0.2
- added ignore errors in filetrigger (closes: #34588)

* Fri Feb 09 2018 Anton Farygin <rider@altlinux.ru> 3.0.0.1-alt1
- 3.0.0.1 release

* Tue Jan 23 2018 Anton Farygin <rider@altlinux.ru> 3.0.0-alt10.rc7
- up to 3.0.0-rc7

* Sun Dec 10 2017 Anton Farygin <rider@altlinux.ru> 3.0.0-alt9.git8b54e4a
- up to 8b54e4a (3.0.0-rc) 

* Tue Nov 07 2017 Anton Farygin <rider@altlinux.ru> 3.0.0-alt8.gitf30c715
- up to f30c715

* Sat Oct 28 2017 Anton Farygin <rider@altlinux.ru> 3.0.0-alt7.git3767a33
- up to 3767a33

* Tue Oct 10 2017 Anton Farygin <rider@altlinux.ru> 3.0.0-alt6.git8cacc98
- up to 8cacc98

* Mon Jul 03 2017 Anton Farygin <rider@altlinux.ru> 3.0.0-alt5.git39e0d63
- up to 39e0d63

* Thu Jun 29 2017 Anton Farygin <rider@altlinux.ru> 3.0.0-alt4.git67dcb71
- up to 67dcb71

* Wed Jun 28 2017 Anton Farygin <rider@altlinux.ru> 3.0.0-alt3.git236b4f3
- 5149ccb -> 236b4f3

* Sat Jun 03 2017 Anton Farygin <rider@altlinux.ru> 3.0.0-alt2.git5149ccb
- move forward to git 5149ccb

* Wed May 31 2017 Anton Farygin <rider@altlinux.ru> 3.0.0-alt1.git7b57ce6
- updated to 7b57ce6 git snapshot
- build libarchive plugin

* Sat May 27 2017 Anton Farygin <rider@altlinux.ru> 3.0.0-alt0.git05262017.1
- updated to upstream 3.0.0 from git

* Thu May 25 2017 Anton Farygin <rider@altlinux.ru> 2.2.6-alt1
- 2.2.6 released
- disabled freerdp build, because vlc does not support the freerdp-2.0 API

* Thu Jul 07 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.4-alt1
- 2.2.4 released

* Wed Apr 27 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.3-alt1
- 2.2.3 released

* Thu Apr 07 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.2-alt2
- rebuilt with recent freerdp

* Thu Mar 10 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.2-alt1
- 2.2.2 released

* Mon Nov 30 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt3.1
- fixed build - added BR: libspeexdsp-devel

* Tue Aug 04 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt3
- rebuilt with recent libdvbpsi, libcdio, live555 and x265

* Wed Jul 15 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt2
- rebuilt with gcc5

* Mon Apr 13 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt1
- 2.2.1 released

* Sat Mar 07 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt2
- rebuilt with recent freerdp

* Wed Mar 04 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt1
- 2.2.0 released

* Tue Aug 05 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.5-alt1
- 2.1.5 released

* Mon May 12 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.4-alt1
- 2.1.4 released

* Thu Feb 06 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.3-alt2
- filetrigger fixed (closes: #29810)

* Thu Jan 30 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.3-alt1
- 2.1.3 released

* Mon Dec 09 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.2-alt1
- 2.1.2 released

* Tue Nov 12 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.1-alt1
- 2.1.1 released

* Fri Sep 20 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.0-alt1
- 2.1.0 released

* Thu Sep 12 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.8-alt3
- rebuilt with recent libav/libx264

* Fri Jul 26 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.8-alt2
- segfault in ffmpeg plugin fixed (closes: #29230)

* Thu Jul 25 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.8-alt1
- 2.0.8 released

* Wed Jun 19 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.7-alt1
- 2.0.7 released

* Mon Apr 08 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.6-alt1
- 2.0.6 released

* Mon Mar 11 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.5-alt2
- fixed build with smbclient from samba4
- built omxil plugin

* Fri Dec 21 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.5-alt1
- 2.0.5 released

* Mon Dec 10 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.4-alt2
- rebuilt with recent libmatroska

* Tue Oct 16 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.4-alt1
- 2.0.4 released

* Thu Sep  6 2012 Terechkov Evgenii <evg@altlinux.org> 2.0.3-alt2
- Rebuild with new libxcbutil

* Thu Jul 19 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.3-alt1
- 2.0.3 released

* Wed Jun 27 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.2-alt1
- 2.0.2 released

* Tue May 29 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.1-alt2
- treat m3u playlist with BOM at start as utf8-encoded (closes: #27373)

* Fri Mar 16 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.1-alt1
- 2.0.1 released

* Wed Feb 22 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0-alt3
- access_smb plugin fixed

* Sat Feb 18 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0-alt2
- line up with all-platforms 2.0.0 release

* Mon Feb 13 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0-alt1
- 2.0.0 released

* Mon Jan 30 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0-alt0.2
- rebuild vith recent libav/x264

* Wed Jan 25 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0-alt0.1
- 2.0-rc1 released

* Mon Jan 09 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt0.6
- 1.2.0-pre4 released

* Wed Dec 28 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt0.5
- 1.2.0-pre3 released

* Fri Dec 02 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt0.4
- rebuilt with recent libbluray due soname change
- updated from git c76783a0

* Mon Nov 28 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt0.3
- 1.2.0-pre2

* Fri Nov 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt0.2
- rebuild with recent libupnp

* Thu Nov 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt0.1
- 1.2 preview

* Thu Oct 13 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.12-alt2
- rebuilt with recent matroska

* Fri Oct 07 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.12-alt1
- 1.1.12 released

* Wed Aug 31 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.11-alt4
- fixed segfault when projectm visualization used (#24212)

* Fri Aug 19 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.11-alt3
- rebuilt with new fluidsynth

* Mon Aug 01 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.11-alt2
- rebuilt with recent libav/x264

* Thu Jul 14 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.11-alt1
- 1.1.11 release.
- CVE-2011-2587 and CVE-2011-2588 fixed

* Mon Jun  6 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.10-alt1
- 1.1.10 release.

* Tue Apr 26 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.9-alt2
- add explicit buildreq to Xpm and Xt

* Tue Apr 12 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.9-alt1
- 1.1.9 release.

* Wed Mar 23 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.8-alt1
- 1.1.8 release.

* Mon Jan 31 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.7-alt1
- 1.1.7 release.

* Mon Jan 24 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.6-alt1
- 1.1.6 release.

* Tue Nov 16 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.5-alt1
- 1.1.5 release.

* Fri Aug 27 2010 Konstantin Pavlov <thresh@altlinux.org> 1.1.4-alt1
- 1.1.4 release.

* Wed Aug 25 2010 Konstantin Pavlov <thresh@altlinux.org> 1.1.3-alt2
- Rebuild with new libva.

* Thu Aug 19 2010 Konstantin Pavlov <thresh@altlinux.org> 1.1.3-alt1
- 1.1.3 release (fixes CVE-2010-2937).

* Thu Aug 12 2010 Konstantin Pavlov <thresh@altlinux.org> 1.1.2-alt2
- almost 1.1.3 release.

* Thu Jul 29 2010 Konstantin Pavlov <thresh@altlinux.org> 1.1.2-alt1
- 1.1.2 release.

* Tue Jul 20 2010 Konstantin Pavlov <thresh@altlinux.org> 1.1.1-alt1
- 1.1.1 release.

* Mon Jun 21 2010 Konstantin Pavlov <thresh@altlinux.org> 1.1.0-alt6
- 1.1.0 release (fixes #23636).
- Require fonts-ttf-core instead of fonts-ttf-dejavu (fixes #23213).
- H264 encoding unbroken (fixes #23249).

* Tue May 25 2010 Konstantin Pavlov <thresh@altlinux.org> 1.1.0-alt5.rc
- 1.1.0 RC.

* Thu May 06 2010 Konstantin Pavlov <thresh@altlinux.org> 1.1.0-alt4.pre3
- 1.1.0 pre3 + some fixes from 1.1 branch.

* Tue Apr 13 2010 Konstantin Pavlov <thresh@altlinux.org> 1.1.0-alt3.pre1
- 1.1.0 pre1.

* Tue Mar 30 2010 Konstantin Pavlov <thresh@altlinux.org> 1.1-alt2.git22d2ded4
- 1.1 build from master branch (git revision 22d2ded4).

* Tue Mar 16 2010 Konstantin Pavlov <thresh@altlinux.org> 1.1-alt1.git846c422c.1
- 1.1 build from master branch (git revision 846c422c).

* Mon Mar 01 2010 Konstantin Pavlov <thresh@altlinux.org> 1.1-alt0.git892f3b5a.1
- 1.1 build from master branch (git revision 892f3b5a).

* Fri Feb 26 2010 Konstantin Pavlov <thresh@altlinux.org> 1.1-alt0.git6a0d4bdd.1
- 1.1 build from master branch (git revision 6a0d4bdd).

* Wed Feb 24 2010 Konstantin Pavlov <thresh@altlinux.org> 1.1-alt0.1
- 1.1 build from master branch.

* Wed Feb 03 2010 Afanasov Dmitry <ender@altlinux.org> 1.0.5-alt2
- Fix mozilla plugin build.
- Rebuild with libx264.so.85.

* Thu Jan 28 2010 Konstantin Pavlov <thresh@altlinux.org> 1.0.5-alt1
- 1.0.5 release.

* Wed Jan 27 2010 Konstantin Pavlov <thresh@altlinux.org> 1.0.4-alt2
- Rebuild with new libva1.

* Sat Dec 19 2009 Konstantin Pavlov <thresh@altlinux.org> 1.0.4-alt1
- 1.0.4 release.

* Mon Nov 16 2009 Konstantin Pavlov <thresh@altlinux.org> 1.0.3-alt3
- Rebuild with new libcdio.

* Sun Nov 15 2009 Konstantin Pavlov <thresh@altlinux.org> 1.0.3-alt2
- Rebuild with new libass.

* Thu Nov 12 2009 Konstantin Pavlov <thresh@altlinux.org> 1.0.3-alt1
- 1.0.3 release plus some fixes from 1.0-bugfix branch:
 + df1e199e: avformat: remove NOFILE hack, fix MXF seeking.
 + cbc88c38: Qt4: fix V4L1 device node specification.
 + a128f739: Ukrainian update.
 + 65824031: m3u.c: use input_item_SetTitle.
 + e34b79a7: dvb: set demux=ts only if we didn't do scan.

* Wed Sep 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt3.2
- rebuild with browser-plugins-npapi-2.0

* Sat Sep 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt3.1
- rebuild with libdvdread.so.4

* Wed Aug 26 2009 Konstantin Pavlov <thresh@altlinux.org> 1.0.1-alt3
- Rebuild with new libcdio.

* Wed Jul 29 2009 Konstantin Pavlov <thresh@altlinux.org> 1.0.1-alt2
- Backported VAAPI support from trunk, use --ffmpeg-hw to enable it.

* Tue Jul 28 2009 Konstantin Pavlov <thresh@altlinux.org> 1.0.1-alt1
- 1.0.1 release.

* Thu Jul 09 2009 Konstantin Pavlov <thresh@altlinux.org> 1.0.0-alt1
- 1.0 release plus some bugfixes from 1.0-bugfix branch:
  + ffbf27c0: Qt: avoid a crash with plugins dialog.
  + df8d92aa: Fix an infinite loop if we redirect from http to https (or contrary).
  + 0e4d1695: X11: I don't want random local users accessing my videos!
- Disabled dc1394 input plugin.

* Thu Jun 18 2009 Konstantin Pavlov <thresh@altlinux.org> 1.0.0-alt0.rc4
- 1.0 rc4 plus some changes from 1.0-bugfix branch: e75f9665.

* Thu May 28 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.0.0-alt0.rc2
- 1.0 rc2.

* Tue May 12 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.0.0-alt0.rc1.8766feda
- 1.0 post-rc1: git commit 8766feda.

* Sat Apr 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt0.pre2.1
- NMU: rebuild with libxcb-keysyms.so.1

* Tue Apr 21 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.0.0-alt0.pre2
- 1.0.0 pre2.

* Thu Mar 19 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.0.0-alt0.pre1
- 1.0.0 pre1.
- Fixes #19176, #17936.

* Thu Mar 12 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.0.0-alt0.git1
- 1.0.0 build, git rev ac14ce27a1a646787dfe1daf67c4ac3c586bfeaa.

* Tue Feb 17 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.0.0-alt0.git
- 1.0.0 build.

* Tue Feb 17 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.9.9-alt0.afterrc
- Build from 0.9-bugfix tree, some time after 0.9.9-rc (776c240).

* Wed Dec 10 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.9.8a-alt1
- 0.9.8a release.
- Fixes VideoLAN-SA-0811 (real media buffer overflow).

* Tue Nov 11 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.9.6-alt1
- 0.9.6 release.
- Fixes VideoLAN-SA-0810.

* Sun Oct 26 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.9.5-alt1
- 0.9.5 release, fixes CVE-2008-4654, CVE-2008-4686 aka VideoLAN-SA-0809.
- Added libv4l2 support to video4linux2 plugin.

* Wed Oct 15 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.9.4-alt1
- 0.9.4 release.
- Added kate support.

* Fri Sep 26 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.9.3.1-alt1
- 0.9.3.1 release.

* Mon Sep 15 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.9.2-alt1
- 0.9.2 release.

* Wed Sep 03 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.9.1-alt2
- Enable SSE on every ix86 arch.

* Tue Aug 26 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.9.1-alt1
- 0.9.1 release.
- Fix #16871.

* Mon Aug 25 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.9.0-alt1
- 0.9.0 release.

* Tue Aug 19 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.9.0-alt0.test3_477_g2e1a5af
- g2e1a5af commit.

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.9.0-alt0.test3_358_gbb36708
- gbb36708 commit.

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.9.0-alt0.test3
- test3 prerelease.

* Mon Jul 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.9.0-alt0.test2
- test2 prerelease.

* Thu Jul 03 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.9.0-alt0.test1
- test1 prerelease.

* Tue Jun 10 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6h-alt1
- 0.8.6h bugfix release.

* Sun Apr 06 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6f-alt1
- 0.8.6f bugfix release.

* Fri Feb 22 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6e-alt1
- 0.8.6e bugfix release.
- Security updates:
 * Subtitle demuxers overflow (CVE-2007-6681)
 * HTTP listener format string injection (CVE-2007-6682)
 * Fixed buffer overflow in the SDL_image library (CVE-2006-4484)
 * Real RTSP overflows (CVE-2008-0295, CVE-2008-0296, VideoLAN-SA-0801)
 * Arbitrary memory overwrite in the MP4 demuxer
   (CORE-2008-0130, VideoLAN-SA-0802, CVE-2008-0984).
 Note that some of those were already fixed in 0.8.6d-alt5.
- Backported pulseaudio output plugin from trunk.

* Wed Dec 26 2007 Michael Shigorin <mike@altlinux.org> 0.8.6d-alt5
- NMU: major security fixes:
  + changeset 23854: fix for a format string error
    in the web interface
  + changeset 23855: fixes for boundary errors in the
    "ParseMicroDvd()", "ParseSSA()", and "ParseVplayer()"
    functions
  + for details see http://secunia.com/advisories/28233/
    (CVE-2007-unknown-yet)

* Sun Dec 16 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6d-alt4
- Backport a fix from trunk to prevent audio hiccups using alsa.

* Fri Nov 30 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6d-alt3
- 0.8.6d release.
- Added mpeg2 / matroska / ogg / v4l / faad plugins to vlc package.

* Mon Oct 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6d-alt2
- Sync with 0.8.6-bugfix branch.
- Rebuild with new libdvbpsi.
- Build with libdirac-0.8.0, tuned BuildRequires.

* Mon Jul 30 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6d-alt1
- Sync with 0.8.6-bugfix branch.
- Fixed AAC-in-AVI decoding with files created by ffmpeg/mencoder:
  http://trac.videolan.org/vlc/changeset/20913 (closes our #12414).

* Wed Jul 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6c-alt4
- Renamed vlc-normal subpackage to vlc.
- Renamed vlc package to vlc-mini.
- Added vlc-plugin-opengl to vlc subpackage.

* Wed Jul 04 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6c-alt3
- Add Xinerama support.
- Synced with 0.8.6-bugfix branch again.

* Sat Jun 16 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6c-alt2
- You won't believe it, but it's a 0.8.6c release too.

* Wed Jun 13 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6c-alt1
- 0.8.6c release.
- Various bugfixes, notably:
  * Windows Vista compatibility
  * Cropping in Direct3D
  * Fullscreen change crash on Mac OS X
  * RSS filter string overflow
  * Few memory leaks
  * Embedded subtitles (GAB2 format) in AVI
  * MKV demuxer crash (related to seeking)

- CDDA / Vorbis / Theora / SAP plugins:
  * Security updates (VideoLAN-SA-0702)

* Fri Jun 08 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6b-alt3
- Merged fixes from 0.8.6-bugfix branch.

* Tue May 15 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6b-alt2
- Fix mozilloids plugin installation.
- Backport ffmpeg.c from trunk: lots of new fourccs.
- Backport fix seeking in mkv from trunk.
- Backport atrac support in rm files from trunk.
- Some tweaks to WX interface.
- Backport RSS fixes from trunk.
- Build with dirac = 0.7

* Thu Apr 19 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6b-alt1
- 0.8.6b release.

* Fri Mar 30 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6a-alt5
- Backported dirac 0.6 support from trunk.
- Applied numerous fixes from 0.8.6-bugfix branch.

* Fri Mar 23 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6a-alt4
- Revert patch for build with wxgtk-2.8. It sucks.

* Wed Feb 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6a-alt3
- Added strict requires for libavcodec >= 0.5.0-alt1.svn8045
  to ffmpeg plugin due to dirac DE support.
- Removed dirac plugin.
- Added a patch fixing build with libflac8.
- Added a patch fixing build with wxgtk-2.8, BR changed accordingly.
- Fixed BuildRequires a bit.
- Added vlc-plugin-xml to vlc-normal subpackage (apparently, vlc stores
  playlist in xml-based format...).
- Made plugins require libvlc instead of vlc package - this could help
  using libvlc+plugins with bindings without vlc package. Even interface
  plugins now require libvlc, though i have no idea if you could use them
  via bindings. :)

* Sun Jan 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6a-alt2
- Spec cleanup, we're VLC media player, not VideoLAN Client.
- Moved h264 demuxer to main vlc package.
- Made vlc package own %%_libdir/vlc/gui directory.
- Proper packaging of libvlc/libvlc-devel.
- Use glibc-kernheaders instead of linux-libc-headers.

* Sat Jan 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6a-alt1
- 0.8.6a bugfix release (well i fixed the bug in -alt3, but anyway...).

* Wed Jan 03 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt3
- Added fix for udp format string vulnerability (affects VCD/CDDAX modules)

* Wed Dec 27 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt2
- Rebuild with new dbus.

* Tue Dec 12 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt1
- 0.8.6 release.

* Fri Dec 01 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.18182
- 0.8.6-rc1.

* Thu Nov 30 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.18168
- 18168, yeah, it's almost test3, i swear!
- gnomevfs -> def_disable, it doesn't work at all.
- New plugin : dv/dc1394.

* Wed Nov 29 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.18153
- 18153, almost test3.

* Thu Nov 16 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.17817
- 17817 revision.

* Thu Nov 16 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.17797
- 17797 revision.
- 0.8.6-test2.

* Tue Nov 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.17528
- 17528 revision.

* Tue Oct 31 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.17389
- 17389 revision.

* Wed Oct 18 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.17132
- 17132, almost -test1.

* Thu Oct 05 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.16948
- 16948 revision.

* Tue Sep 26 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.16876
- 16876 revision.

* Mon Sep 18 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.16724
- 16724 revision of 0.8.6 stable branch.

* Sun Sep 03 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.16525
- 16525 revision.
- Removed patch10, patch13 as they moved upstream (theora, mux_ts -> plugins).
- Get rid of sed (ffmpeg was fixed).

* Fri Aug 25 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.16345
- 16345 revision.
- Moved FreeDesktop menu file to separate %%SOURCE1, modified it a bit.

* Mon Aug 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.16235
- 16235 revision.
- Added libtwolame-devel to BuildRequires.
- New plugin: twolame.
- Removed demux/ts from main vlc package.

* Sat Aug 05 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.16209
- 16209 revision.
- Use switch to on/off dirac plugin (now it's on).
- Stricted libdirac version to use (now it's 0.5.4-alt1).
- Stricted faad version to use (now it's 2.0-alt2.20040923).
- Stricted ffmpeg version to use (now it's 0.5.0-alt1.svn5790).
- probe_hal plugin goes to plugin-hal package.
- motion plugin -- punch your notebook to navigate thru playlist
  (only supported on some Thinkpad models, don't forget to modprobe hdaps).
- Made %%summary'ies for plugins more descriptive.
- Made %%summary'ies and %%description's for packages unified.
- Cleaned up %%description's.
- Enablind smb plugin.

* Tue Jun 20 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.15926
- 15926 revision.
- BuildRequires changes:
  + Added libnotify-devel, libdbus-glib-devel, libupnp-devel.
  + XOrg7ification.
- Not building upnp plugin due to current trunk playlist changes.
- Added Requires: vlc-interfaces-wxwidgets to vlc-interface-skins2.
- Added java bindings toggle, disabling by default, it is not ready yet.
- Added working python mediacontrol bindings toggle, disabling it by default.
- Live555 version bump.
- Live555 moved to plugins, added to -normal virtual package.
- Temporarily disabled smb plugin.

* Fri Jun 02 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.15786
- Unified provides system for interfaces plugins:
  each interface plugin now provides vlc-interface.
  each interface plugin now provides vlc-plugin-%%name.
- Added fortunes-vlc package.
- s/vlc-plugin-qt4/vlc-interface-qt4/ in maxi requires (thx legion@).
- Patch15 (qt4 fix) merged upstream, removing it.
- More requires/obsoletes in vlc-normal package.
- Added THANKS file to documentation.

* Tue May 30 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.15765
- 15765.
- Added libqt4-devel to buildreq, enabling by default, goes to separate 
  interface package, added patch to build qt4 interface.
- Lightened buildreq dependancy to liblive-devel.

* Sat May 06 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.15548
- 15548 (post 0.8.5-test4).
- Removed patch14 (mozilla paths) as it merged upstream.
- Removed patch5 (svg build) as it was fixed in upstream.
- Trying to build mozilla plugin without nspr4 xpcom etc stuff (patch15,
  merged upstream).
- Mosaic plugin linked with -lm (same fix in upstream).
- Moved ts_plugin from vlc package to plugin-ts with mux_ts, added
  plugin-ts to the list of the essential packages to run vlc on desktop.
- Renamed vlc-common to vlc-normal.
- Moved stream_out_switcher to ffmpeg plugin.
- Some spec cleanup.

* Fri Apr 28 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.15395
- 15395.

* Wed Apr 26 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.15364
- 15364.
- fixed mozilla plugin build.

* Sat Apr 22 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.6-alt0.15299
- 0.8.6 trunk.
- 15299 revision.
- Some spec cleanup.
- Renamed some patches.
- Removing kludgy *FLAGS.
- Enabling DAAP support thru libdaap, goes to separate plugin.
- Built with libdts -- enables DTS decoding, goes to separate plugin.
- Matroska, dts, bonjour (avahi), theora, mux_ts goes to plugins.
- Moving telnet and http interface to plugins.
- Fixed some unresolved symbols in some plugins (patch moved to upstream).
- Improved Xorg7 detection under ia32 (patch moved to upstream).
- added fonts-ttf-dejavu to freetype plugin requires as it uses hardcoded
font from dejavu by default (suggestions on default font are welcome).

* Tue Apr 04 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.15087
- 15087 (post test2).

* Sat Mar 25 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14911
- 14911.
- updated mozilla and wxnoupdates patches.
- to sisyphus.
- mmx memcpy and stuff moved to plugins from builtins and goes into main package.
- textrel = relaxed, unresolved = relaxed.

* Sun Mar 05 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14640
- 14640.
- compiling with linux-libc-headers.

* Sat Mar 04 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14613
- 14613.

* Sat Mar 04 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14602
- 14602
- same thing with svg, disabled it until fixed in upstream.

* Tue Feb 28 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14534
- 14534.
- added def_disable ggi and ifdeffed everything around it.

* Mon Feb 27 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14521
- 14521.

* Sun Feb 26 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14512
- 14512.
- added liblame devel to buildreq.

* Wed Feb 22 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14462
- 14462.
- enabling debug.

* Tue Feb 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14446
- 14446.

* Tue Feb 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14430
- 14430.

* Mon Feb 20 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14421
- 14421.

* Sun Feb 19 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14378
- 14378.
- fixed maxi/common packages.

* Fri Feb 17 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14350
- Added -maxi and -common packages for installation ease.

* Fri Feb 17 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14349
- 14349.
- deffed python bindings build. currently disabled it because of upstream changes.

* Thu Feb 16 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14333
- 14333.
- python patch edited.

* Mon Feb 06 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14182
- 14182.
- added ugly hack (tm) to enable building on 32bit systems.
- enabling quicktime and dmo only for 32bit.

* Fri Feb 03 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14148
- 14148.
- added jack plugin.
- added snapshot plugin.

* Fri Feb 03 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14146
- 14146.
- removed debian menu.

* Thu Feb 02 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14139
- 14139.
- skipping verify_elf.

* Tue Jan 31 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14090
- 14090
- added vim-plugin-vlc-syntax package.
- let's try to link with x264.
- removed --disable-rpath.
- added ./toolbox.

* Thu Jan 26 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14014
- 14014.
- removing configure patch.

* Tue Jan 24 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14009
- 14009.
- vcdx plugin.

* Mon Jan 23 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.14004
- svg fix build.

* Thu Jan 19 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.13949
- removed fix for xorg7, cause 13949 revision should check for xlibs better. ;)
- moved mpc to plugin-musepack.
- moved dvdread to plugin-dvdread.
- moved dvdnav to plugin-dvdnav.
- moved ffmpeg to plugin-ffmpeg.
- moved mpeg2 to plugin-mpeg2.
- moved modplug to plugin-modplug.
- moved ogg muxer to plugin-ogg.

* Thu Jan 19 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.13948
- revision 13948.
- fixed build with xorg7.0.

* Sat Jan 14 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8.5-alt0.13911
- svn trunk.
- new versioning.
- added wxnoupdates patch and osdmenu patch.
- moved all interface plugins to interface-* packets.
- added provides vlc-interface to all those packets.
- added .desktop file.
- removed broken documentation.
- Hopefully fixed xvideo on x86_64.
- Add requires libx264-devel-static.
- fixed mozilla plugin build (hello, new world with new mozilla-devel & co!).
- added goom plugin.
- removed java bindings as they doesn't even install. :(
- enabling python bindings.
- added podcast module.
- sed-i'ng modules path.
- using ./bootstrap.

* Tue Dec 13 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.8.4a-alt0.8
- 0.8.4a release.
- altered buildreqs.
- enabled hal.

* Sat Dec 10 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.8.4-alt0.77
- altered ffmpeg buildreq.
- remove vlc requires in mozilla-plugin-vlc package.

* Sat Dec 10 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.8.4-alt0.76
- buildreqs cleanup.

* Sat Dec 10 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.8.4-alt0.75
- Added LIVE555.com (formerly live.com, blame MS!) support for VLC to support RTSP.
- hal doesn't build on x86, let's %def_disable it.

* Thu Dec 08 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.8.4-alt0.71
- added librsvg2-devel to buildreqs.

* Wed Dec 07 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.8.4-alt0.6
- 0.6 version of spec.
- all the plugins are packaged, some of them (~40) are in the separate packages.
- xvideo plugin doesn't build on x86_64.

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.7.2-alt0.5.1.1
- Rebuilt with libstdc++.so.6.

* Tue Oct 05 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.7.2-alt0.5.1
- Rebuilt with libdvdread.so.3.

* Mon May 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.7.2-alt0.5
- 0.7.2

* Thu Apr 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.7.1-alt0.2
- 0.7.1

* Mon Jan 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.7.0-alt0.2
- 0.7.0

* Thu Apr 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5.3-alt0.5
- 0.5.3

* Tue Feb 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5.0-alt0.5
- 0.5.0

* Sat Nov 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.6-alt0.5
- 0.4.6

* Fri Nov 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.5-alt0.5
- 0.4.5

* Fri Sep 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.4-alt0.5
- 0.4.4

* Sat Jul 27 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.3-alt0.5
- 0.4.3

* Thu Jul 11 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.2-alt0.5
- 0.4.2
- built with libffmpeg-0.4.6-alt0.2cvs20020721

* Wed Jun 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.1-alt0.5
- 0.4.1
- built with libffmpeg-0.4.6-alt0.1cvs20020605
- configure.in patch removed.

* Fri May 24 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4-alt0.5
- Adopted for Sisyphus.

* Thu May 23 2002 Yves Duret <yduret@mandrakesoft.com> 0.4.0-1mdk
- version 0.4.0 with MPEG4 (DivX) support thx ffmpeg.
  thus s/MPEG, MPEG2 and DVD/multimedia/g
- sync %%description with debian ones.
- vlc now requires a vlc-gui (gtk, gnome or qt).
- removed gcc3.1 patches since merged upstream.

* Mon May 13 2002 Yves Duret <yduret@mandrakesoft.com> 0.3.1-4mdk
- removed xmga plugin (currently broken).
- manual rebuild in gcc3.1 environment aka added Patch0 & Patch1
- various summary/description changes.

* Fri May 03 2002 Yves Duret <yduret@mandrakesoft.com> 0.3.1-3mdk
- added vlc-lirc intf plugin rpm.

* Tue Apr 30 2002 Yves Duret <yduret@mandrakesoft.com> 0.3.1-2mdk
- rebuild against libalsa2 (vlc-sdl)

* Fri Apr 19 2002 Yves Duret <yduret@mandrakesoft.com> 0.3.1-1mdk
- version 0.3.1.
- removed patch0 merged upstream.
- removed old %%ifarch ppc
- added missing libmad-devel buldrequires

* Wed Apr 17 2002 Yves Duret <yduret@mandrakesoft.com> 0.3.0-4mdk
- added liba52 support (buildrequires).
- added vlc-alsa audio plugin.
- mad is a codec (audio) plugin. corrected description and summary.

* Wed Apr 10 2002 Yves Duret <yduret@mandrakesoft.com> 0.3.0-3mdk
- added patch0 from CVS: fix crashing GTK popup menus thx Michal Bukovjan <bukovjan@mbox.dkm.cz>

* Wed Apr 10 2002 Yves Duret <yduret@mandrakesoft.com> 0.3.0-2mdk
- added vlc-arts rpm plugin thx blindauer Emmanuel <manu@agat.net>
- better summary for plugin
- add packager tag to myself

* Sun Apr 07 2002 Yves Duret <yduret@mandrakesoft.com> 0.3.0-1mdk
- version 0.3.0
- added aa (Asci Art) plugin in vlc-aa rpm
- merged with sam's one:
  * using his plugins list into %%files
  * removed libdvdcss from the whole tarball.
  * removed the workaround for VLC's bad /dev/dsp detection.
- few spell corrections in all %%description
- added buildrequires on SDL-devel

* Tue Mar 05 2002 Yves Duret <yduret@mandrakesoft.com> 0.2.93-0.1mdk
- new cvs snapshot
- fix requires

* Mon Mar 04 2002 Yves Duret <yduret@mandrakesoft.com> 0.2.92-5mdk
- cvs snapshot

* Sat Jan 26 2002 Yves Duret <yduret@mandrakesoft.com> 0.2.92-4mdk
- mad plugin in vlc-mad rpm

* Mon Jan 21 2002 Yves Duret <yduret@mandrakesoft.com> 0.2.92-3mdk
- synced with main cvs specfile wich "fixed a few minor inaccuracies"

* Thu Jan 17 2002 Yves Duret <yduret@mandrakesoft.com> 0.2.92-2mdk
- readded libdvdcss rpm in specfile. use %%define css 1 with correct sources
  to build libdvdcss rpm.

* Wed Jan 09 2002 Yves Duret <yduret@mandrakesoft.com> 0.2.92-1mdk
- version 0.2.92
- %%makeinstall_std
- splitted again, added vlc-sdl vlc-esd vlc-ggi
- bring back some missing plugins
- fixed buildrequires
- added menu entries and icons (from cvs)

* Tue Oct 23 2001 Yves Duret <yduret@mandrakesoft.com> 0.2.83-2mdk
- rebuild against libpng3
- added some doc for sir rpmlint
- #5583: option -g

* Thu Aug 23 2001 Yves Duret <yduret@mandrakesoft.com> 0.2.83-1mdk
- version 0.2.83 :
  * Activated subtitles in overlay mode (far from perfect, but this
    was an often requested feature).

* Fri Aug 10 2001 Yves Duret <yduret@mandrakesoft.com> 0.2.82-1mdk
- version 0.2.82

* Mon Jul 30 2001 Yves Duret <yduret@mandrakesoft.com> 0.2.81-1mdk
- version 0.2.81
- added vlc-ncurses

* Wed Jun 20 2001 Yves Duret <yduret@mandrakesoft.com> 0.2.81-0.20010619-1mdk
- cvs snapshot
- added libdvdcss

* Wed Jun 13 2001 Yves Duret <yduret@mandrakesoft.com> 0.2.80-2mdk
- fix build on ppc (c) dadou

* Mon Jun 11 2001 Yves Duret <yduret@mandrakesoft.com> 0.2.80-1mdk
- version 0.2.80 : bug fixes and bug fixes and bug fixes and small
  improvements of the gtk interface.
- corrected Summary in vlc-qt

* Wed May 23 2001 Yves Duret <yduret@mandrakesoft.com> 0.2.73-2mdk
- added qt2 plugin (vlc-qt)

* Wed May 16 2001 Yves Duret <yduret@mandrakesoft.com> 0.2.73-1mdk
- version 0.2.73
- you can now get decss threw a plugin
- rewritte srcipt to build vlc (decss plugin)
- rebuild with SDL 1.2

* Thu Apr 26 2001 Yves Duret <yduret@mandrakesoft.com> 0.2.72-2mdk
- true 0.2.72

* Mon Apr 16 2001 Yves Duret <yduret@mandrakesoft.com> 0.2.72-1mdk
- version 0.2.72
- package split into vlc, vlc-gnome, vlc-gtk

* Fri Apr 13 2001 Yves Duret <yduret@mandrakesoft.com> 0.2.71-1mdk
- version 0.2.71 :
  * Fixed segfaults when compiled with gcc 3.0pre and versions of gcc
    shipped with the latest RedHat distributions.
  * Fixed the BeOS CSS decryption.
  * Fixed a few issues in IFO parsing.
  * Fixed XVideo video output.
  * Updated icons under Linux, BeOS, MacOS X.

* Wed Apr 11 2001 Yves Duret <yduret@mandrakesoft.com> 0.2.70-1mdk
- version 0.2.70

* Thu Mar 22 2001 Yves Duret <yduret@mandrakesoft.com> 0.2.63-1mdk
- version 0.2.63 : Bugfixes, bugfixes, and bugfixes again, a Gtk+
  interface for Gnome-impaired, an even better DVD support

* Fri Feb 16 2001 Yves Duret <yduret@mandrakesoft.com> 0.2.61-1mdk
- new version for all the DVD fans (add MPEG1 support, direct DVD support,
  DVD decryption, arbitrary, seeking in the stream, pause, fast forward
  and slow motion, hardware YUV acceleration enhanced CSS support and a few
  new interface features including drag'n'drop.
- first *real* public release (now under the GPL)

* Sat Jan 06 2001 David BAUDENS <baudens@mandrakesoft.com> 0.1.99i-2mdk
- Fix build and use right optimizations on PPC
- Enable SDL support
- Spec clean up

* Fri Jan  5 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.1.99i-1mdk
- 0.1.99i, rebuild

* Fri Aug 25 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.1.99h-1mdk
- 0.1.99h

* Mon Jul 10 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.1.99c-1mdk

- first Mandrake package with help of Sam
