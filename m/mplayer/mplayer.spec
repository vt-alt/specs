%define set_disable() %{expand:%%force_disable %{1}} %{expand:%%undefine _enable_%{1}}
%define set_enable() %{expand:%%force_enable %{1}} %{expand:%%undefine _disable_%{1}}
%define set_without() %{expand:%%force_without %{1}} %{expand:%%undefine _with_%{1}}
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}
%define subst_o() %{expand:%%{?_enable_%{1}:%{1},}}
%define subst_o_pre() %{expand:%%{?_enable_%{2}:%{1}%{2},}}
%define subst_o_post() %{expand:%%{?_enable_%{1}:%{1}%{2},}}

%define prerel %nil
#define svnrev 32772
%define lname mplayer
%define gname g%lname
%define Name MPlayer
%define subrel %nil

#---------------------- BEGIN OF PARAMETERS -------------------------------------

# Optional features:
%def_enable mplayer
%def_enable mencoder
%def_enable xss
%def_enable lame
%def_disable lame_lavc
%def_enable gui
%def_enable termcap
%def_enable termios
%def_enable iconv
%def_enable shm
%def_enable langinfo
%def_enable lirc
%def_disable lircc
%def_enable joystick
%def_enable apple_ir
%def_enable xf86keysym
%def_enable tv
%def_disable tv_v4l1
%def_enable tv_v4l2
%def_enable v4l2
%def_enable radio
%def_disable radio_v4l1
%def_enable radio_v4l2
%def_enable radio_capture
%def_enable pvr
%def_enable rtc
%def_enable network
%def_enable gnutls
%def_disable winsock2
%def_enable smb
%def_enable live
%def_enable vcd
%def_enable bluray
%def_enable dvdnav
%def_enable dvdread
%def_enable cdparanoia
%def_enable bitmap_font
%def_enable freetype
%def_enable fontconfig
%def_enable unrarexec
%def_enable osdmenu
%def_enable sortsub
%def_enable fribidi
%def_enable enca
%def_enable inet6
%def_disable sctp
%def_enable ftp
%def_disable vstream
%def_enable pthreads
%def_enable ass
%def_disable ass_int
%def_disable rpath
%def_enable cddb
%def_disable librtmp
%def_disable nemesi

# Codecs:
%def_enable mng
%def_enable gif
%def_enable png
%def_enable jpeg
%def_enable openjpeg
%def_enable libcdio
%def_disable libgtop
%def_enable lzo
%def_enable win32
%def_enable qtx
%def_enable xanim
%def_enable real
%def_enable xvid
%def_enable xvid_lavc
%def_enable x264
%def_disable x264_lavc
%def_enable ffmpeg
%def_enable shared_ffmpeg
%def_enable postproc
%def_disable vf_lavfi
%def_disable libavcodec_mpegaudio_hp
%def_enable faad
%def_disable tremor
%def_enable vorbis
%def_enable speex
%def_enable theora
%def_disable faac
%def_enable ladspa
%def_enable bs2b
%def_enable dca
%def_enable libdv
%def_disable crystalhd
%def_enable mad
%def_disable toolame
%def_disable twolame
%def_disable xmms
%def_enable liba52
%def_enable libmpeg2
%def_disable libmpeg2_int
%def_enable musepack
%def_disable nut
%def_enable libgsm
%def_enable amrnb
%def_enable amrwb
%def_enable libvpx_lavc
%def_enable libopus
%def_enable libdca

# Video output:
%def_disable vidix
%def_enable gl
%def_disable dga1
%def_disable dga2
%def_disable vesa
%def_disable svga
%def_enable sdl
%def_enable aa
%def_enable caca
%def_disable ggi
%def_disable ggiwmh
%def_disable directx
%def_disable dxr2
%def_disable dxr3
%def_disable ivtv
%def_enable dvb
%def_disable mga
%def_disable xmga
%def_enable xv
%def_disable xvmc
%define xvmclib XvMCW
%def_enable vm
%def_enable xinerama
%def_enable x11
%def_enable xshape
%def_enable fbdev
%def_disable mlib
%def_disable 3dfx
%def_disable tdfxfb
%def_disable s3fb
%def_disable directfb
%def_disable zr
%def_disable bl
%def_disable tdfxvid
%def_disable tga
%def_enable pnm
%def_enable md5sum
%def_enable vdpau
%def_disable matrixview
%def_enable mpg123
%def_enable yuv4mpeg
%def_disable xvr100

# Audio output:
%def_enable alsa
%def_enable oss
%def_disable arts
%def_disable esd
%def_enable pulse
%def_enable jack
%def_disable openal
%def_disable nas
%def_disable sgiaudio
%def_disable sunaudio
%def_disable waveout
%def_enable select
%def_disable dart
%def_disable kai
%def_disable kva

# Miscellaneous options:
%def_enable cpu_detection
%def_enable yasm
#define asm as
%define charset UTF-8
%define language all

# Advanced options:
%ifarch %ix86 x86_64
%def_enable mmx
%def_enable mmxext
%def_enable 3dnow
%def_enable 3dnowext
%def_enable sse
%def_enable sse2
%def_enable ssse3
%def_disable altivec
%endif
%def_enable fastmemcpy
%def_disable debug
%def_disable profile
%def_enable sighandler
%def_disable gdb
%def_enable dynamic_plugins

%define termcaplib tinfo

# Other parameters
%def_enable nls
%def_with htmldocs
%def_with tools
%define default_vo %{subst_o xv}%{subst_o sdl}%{subst_o gl2}%{subst_o gl}%{subst_o x11}%{subst_o_pre x vidix}%{subst_o mga}%{subst_o dfbmga}%{subst_o tdfxfb}%{subst_o 3dfx}%{subst_o s3fb}%{subst_o_pre c vidix}%{subst_o_post fbdev 2}%{subst_o vesa}%{subst_o caca}%{subst_o aa}null
%define default_ao %{subst_o alsa}%{subst_o oss}%{subst_o openal}%{subst_o sdl}%{subst_o pulse}%{subst_o nas}null

# ARM
#%%def_disable armv5te
#%%def_disable armv6
#%%def_disable armv6t2
#%%def_disable armvfp
#%%def_disable iwmmxt
#%%def_disable neon

#---------------------- END OF PARAMETERS ---------------------------------------

%{?_disable_mencoder:%set_disable lame}

%if_disabled tv
%set_disable v4l1
%set_disable v4l2
%set_disable pvr
%endif

%if_disabled network
%set_disable live
%set_disable ftp
%endif

%{?_enable_shared_ffmpeg:%set_disable zr}

%if_enabled nls
%define awk gawk
%set_enable iconv
%{!?charset:%define charset UTF-8}
#%%undefine language
#%%define language en
%else
%define awk awk
%endif

%{?_disable_ffmpeg:%set_disable shared_ffmpeg}
%{?_disable_iconv:%set_disable freetype}
%{?_disable_freetype:%set_disable fontconfig}

%ifnarch %ix86 x86_64
%set_disable yasm
%set_disable vidix
%set_disable cpu_detection
%endif

%{?_enable_tremor:%set_disable tremor_low}

%ifnarch %ix86
%set_disable win32
%endif

%ifnarch ppc
%set_disable altivec
%endif

%define win32_libdir %_libdir/w32codec
%define xanim_libdir %_libdir/xanim
%define real_libdir %_libdir/real

%{?_disable_win32:%set_disable qtx}

%if_disabled x11
%set_disable xv
%set_disable xvmc
%set_disable xinerama
%set_disable xf86keysym
%set_disable vm
%set_disable vdpau
%set_disable dga1
%set_disable dga2
%endif

%if_disabled mplayer
%set_without tools
%set_disable gui
%endif


Name: %lname
Version: 1.4
Release: alt1.1.p9
%ifdef svnrev
%define pkgver svn-r%svnrev
%else
%define pkgver %version%prerel
%endif
Summary: Media player
Summary(uk_UA.UTF-8): Медіаплейер
Summary(ru_RU.UTF-8): Медиаплейер
License: GPLv2+
Group: Video
URL: http://www.mplayerhq.hu
Packager: Afanasov Dmitry <ender@altlinux.org>
%if %name != %Name
Provides: %Name = %version-%release
Obsoletes: %Name
%endif
%if_enabled freetype
%{?_disable_fontconfig:Requires: fonts-type1-urw}
Conflicts: %Name-fonts < 1.0-alt28
Conflicts: %name-i18n < 1.0-35.22229.1
Obsoletes: %Name-fonts
%else
Requires: %name-fonts
%endif
# repacked http://www.mplayerhq.hu/MPlayer/releases/MPlayer-%pkgver.tar.gz
Source0: %Name-%pkgver.tar
# register console mplayer as mime handler
Source2: %lname.desktop
Source4: standard-1.9.tar
Source5: %lname.conf.in
# git://git.altlinux.org/gears/m/mplayer.git
Patch0: %name-%version-%release.patch

%if_enabled gui
Provides: %name-gui = %version-%release
Obsoletes: %name-gui
Provides: %gname = %version-%release
Obsoletes: %Name-skin-default
%if %name != %Name
Provides: %Name-gui = %version-%release
Obsoletes: %Name-gui
%endif
%endif

BuildRequires: %awk libncurses-devel libslang-devel zlib-devel
BuildRequires: cpp >= 3.3 gcc >= 3.3 gcc-c++ >= 3.3
%{?svnrev:%{?_with_htmldocs:BuildRequires: docbook-style-xsl xsltproc sgml-common docbook-dtds}}

%{?_enable_mencoder:%{?_enable_lame:BuildRequires: liblame-devel}}
%{?_enable_termcap:BuildRequires: libtinfo-devel}
%{?_enable_smb:BuildRequires: libsmbclient-devel >= 3.0.3}
%{?_enable_live:BuildRequires: liblive555-devel >= 0.0.0-alt0.2006.03.03}
%{?_enable_bluray:BuildRequires: libbluray-devel}
%{?_enable_dvdnav:BuildRequires: libdvdnav-devel >= 0.1.10-alt4}
%{?_enable_dvdread:BuildRequires: libdvdread-devel}
%{?_enable_cdparanoia:BuildRequires: libcdparanoia-devel}
%{?_enable_vstream:BuildRequires: libvstream-client-devel}
%{?_enable_sctp:BuildRequires: libsctp-devel}
%if_enabled mplayer
%{?_enable_lirc:BuildRequires: liblirc-devel}
%{?_enable_lircc:BuildRequires: lirccd-devel}
%{?_enable_freetype:BuildRequires: libfreetype-devel >= 2.0.9}
%{?_enable_fontconfig:BuildRequires: fontconfig-devel}
%{?_enable_fribidi:BuildRequires: libfribidi-devel}
%{?_enable_enca:BuildRequires: libenca-devel}
%{?_enable_gnutls:BuildRequires: libgnutls-devel}
%endif

%{?_enable_vdpau:BuildRequires: libvdpau-devel}
%{?_enable_gif:BuildRequires: libungif-devel}
%{?_enable_mng:BuildRequires: libmng-devel}
%{?_enable_png:BuildRequires: libpng-devel}
%{?_enable_jpeg:BuildRequires: libjpeg-devel}
%{?_enable_openjpeg:BuildRequires: libopenjpeg-devel}
%{?_enable_libcdio:BuildRequires: libcdio-devel libcdio-paranoia-devel}
%{?_enable_libgtop:BuildRequires: pkgkonfig(libgtop-2.0)}
%{?_enable_lzo:BuildRequires: liblzo2-devel}
%{?_enable_xvid:BuildRequires: libxvid-devel}
%{?_enable_x264:BuildRequires: libx264-devel}
%{?_enable_shared_ffmpeg:BuildRequires: libavcodec-devel libavformat-devel libavutil-devel libswresample-devel libswscale-devel}
%{?_enable_tremor:BuildRequires: libtremor-devel}
%{?_enable_vorbis:BuildRequires: libvorbis-devel}
%{?_enable_speex:BuildRequires: libspeex-devel >= 1.1}
%{?_enable_theora:BuildRequires: libtheora-devel}
%{?_enable_faad:BuildRequires: libfaad-devel}
%{?_enable_faac:BuildRequires: libfaac-devel}
%{?_enable_ladspa:BuildRequires: ladspa_sdk}
%{?_enable_bs2b:BuildRequires: libbs2b-devel}
%{?_enable_libdv:BuildRequires: libdv-devel}
%{?_enable_crystalhd:BuildRequires: libcrystalhd-devel}
%{?_enable_mad:BuildRequires: libmad-devel}
%{?_enable_xmms:BuildRequires: libxmms-devel}
%{?_enable_liba52:BuildRequires: liba52-devel}
%{?_enable_libmpeg2:BuildRequires: libmpeg2-devel}
%{?_enable_musepack:BuildRequires: libmpcdec-devel >= 1.2.1}
%{?_enable_nut:BuildRequires: libnut-devel >= 0.0-alt0.272}
%{?_enable_amrnb:BuildRequires: libopencore-amrnb-devel}
%{?_enable_amrwb:BuildRequires: libopencore-amrwb-devel}
%{?_enable_dca:BuildRequires: libdca-devel}
%{?_enable_libgsm:BuildRequires: libgsm-devel}
%{?_enable_libvpx_lavc:BuildRequires: libvpx-devel}
%{?_enable_libopus:BuildRequires: libopus-devel}
%{?_enable_libdca:BuildRequires: libdca-devel}
%{?_enable_librtmp:BuildRequires: librtmp-devel}
%{?_enable_nemesi:BuildRequires: libnemesi-devel}
%{?_enable_mpg123:BuildRequires: libmpg123-devel}
%{?_enable_ass:BuildRequires: libass-devel}

%{?_enable_xvmc:BuildRequires: libXvMC-devel}
%if_enabled mplayer
%{?_enable_xss:BuildRequires: libXScrnSaver-devel}
%{?_enable_xshape:BuildRequires: libXext-devel}
%{?_enable_gl:BuildRequires: libGL-devel}
%{?_enable_vesa:BuildRequires: libvbe-devel}
%{?_enable_svga:BuildRequires: svgalib-devel}
%{?_enable_sdl:BuildRequires: libSDL-devel >= 1.1.7 libSDL_mixer-devel}
%{?_enable_aa:BuildRequires: aalib-devel libgpm-devel libslang-devel libX11-devel}
%{?_enable_caca:BuildRequires: libcaca-devel libslang-devel libX11-devel}
%{?_enable_ggi:BuildRequires: libggi-devel}
%{?_enable_dxr3:BuildRequires: libdxr3-devel}
%{?_enable_xv:BuildRequires: libXv-devel}
%{?_enable_vm:BuildRequires: libXxf86vm-devel}
%{?_enable_xinerama:BuildRequires: libXinerama-devel}
%{?_enable_x11:BuildRequires: libXt-devel xorg-xextproto-devel}
%{?_enable_dga1:BuildRequires: libXxf86dga-devel}
%{?_enable_dga2:BuildRequires: libXxf86dga-devel}
%{?_enable_directfb:BuildRequires: libdirectfb-devel}
%{?_enable_pnm:BuildRequires: libnetpbm-devel}

%{?_enable_alsa:BuildRequires: libalsa-devel}
%{?_enable_arts:BuildRequires: libarts-devel}
%{?_enable_esd:BuildRequires: esound-devel}
%{?_enable_pulse:BuildRequires: libpulseaudio-devel >= 0.9}
%{?_enable_jack:BuildRequires: jackit-devel}
%{?_enable_openal:BuildRequires: libopenal-devel}
%{?_enable_nas:BuildRequires: libaudio-devel}

%{?_enable_gui:BuildRequires: ImageMagick-tools desktop-file-utils gtk+2-devel}
%endif

%{?_enable_nls:BuildRequires: gettext-tools}

%{?_with_tools:BuildRequires: perl-libwww perl-Math-BigInt libSDL_image-devel normalize termutils vcdimager}

%{?_enable_yasm:BuildRequires: yasm}

%description
%Name is a movie and animation player that supports a wide range of file
formats, including AVI, MPEG, and Quicktime. It has many MMX/SSE/3DNow! etc.
optimized native audio and video codecs, but allows using XAnim's and
RealPlayer's binary codec plugins, and Win32 codec DLLs. It has basic VCD/DVD
playback functionality, including DVD subtitles, but supports many text-based
subtitle formats too.
For video and audio output, nearly every existing interface is supported
including some low-level card-specific drivers (for Matrox, Nvidia, 3Dfx and
Radeon, Mach64, Permedia3), hardware AC3 decoding and few hardware MPEG decoding
boards such as DVB and DXR3/Hollywood+.
It also supports video grabbing from V4L devices.

%description -l ru_RU.UTF-8
%Name - это видеопроигрыватель, который поддерживает широкий спектр форматов
файлов, в том числе AVI, MPEG и Quicktime. В него включено множество аудио- и
видеокодеков, оптимизированных для MMX, SSE, 3DNow! и.т.п. Кроме этого, имеется
возможность использования внешних кодеков: XAnim, RealPlayer и Win32. Реализованы
основные функции для проигрывания VCD/DVD, включая субтитры DVD, а также
множества других текстовых форматов субтитров.
Поддерживаются практически все способы вывода изображения и звука в
юниксоподобных системах. Имеются низкоуровневые специализированные драйвера для
некоторых видеокарт: Matrox, Nvidia, 3Dfx, Radeon, Mach64, Permedia3, аппаратного
декодирования AC3, а также нескольких плат, аппаратно декодирующих MPEG, таких
как DVB и DXR3/Hollywood+.
Кроме этого, %Name способен захватывать сигнал с устройств V4L.


%if_enabled mencoder
%package -n mencoder
Group: Video
Summary: Movie encoder for Unix.
Summary(ru_RU.UTF-8): Кодировщик фильмов для Unix.
Provides: MEncoder = %version-%release
Conflicts: %Name < 1.0-alt28

%description -n mencoder
MEncoder a movie encoder for Unix and is a part of the %name package.
%endif


%if_with tools
%package tools
Group: Video
Summary: %Name/MEncoder tools
%if_enabled mencoder
Provides: mencoder-tools = %version-%release
Requires: mencoder
%endif
Requires: %name


%description tools
Nice scripts and code that makes using %Name and MEncoder easier, for example
scripts for DVD track encoding in three pass mode or creating SVCDs from a movie.
%endif


%if_with htmldocs
%package docs
Group: Documentation
Summary: %Name all docs
BuildArch: noarch
Requires: %name-doc-tech
Requires: %name-doc-en
Requires: %name-doc-world
Requires: %name-doc-ru
%if %name != %Name
Provides: %Name-docs
Obsoletes: %Name-docs
%endif

%description docs
%Name all docs.


%package doc-tech
Group: Documentation
Summary: %Name Tech docs
BuildArch: noarch

%description doc-tech
%Name Tech docs.


%package doc-en
Group: Documentation
Summary: %Name English docs
BuildArch: noarch
Obsoletes: %Name-doc
Provides: %Name-doc
%if %name != %Name
Provides: %Name-doc-en = %version-%release
Obsoletes: %Name-doc-en
%endif

%description doc-en
%Name English docs.


%package doc-world
Group: Documentation
Summary: %Name docs
BuildArch: noarch
Conflicts: %name-doc-cs %name-doc-de %name-doc-es %name-doc-fr
Conflicts: %name-doc-hu %name-doc-it %name-doc-pl %name-doc-zh_CN

%description doc-world
%Name docs (exept English and Russian.


%package doc-ru
Group: Documentation
Summary: %Name Russian docs
BuildArch: noarch
%if %name != %Name
Provides: %Name-doc-ru = %version-%release
Obsoletes: %Name-doc-ru
%endif

%description doc-ru
%Name Russian docs.
%endif


%package i18n
Group: Video
Summary: Languages support for %Name
BuildArch: noarch
%{?_enable_mencoder:Provides: mencoder-i18n = %version-%release}
Requires: %name-i18n-world = %version-%release
Requires: %name-i18n-ru = %version-%release
%{?_enable_nls:Requires: %name-i18n-uk = %version-%release}

%description i18n
Languages support for %Name.


%package i18n-world
Group: Video
Summary: Languages support for %Name
BuildArch: noarch
Conflicts: %name-i18n < 1.0-35.22229.1
%{?_enable_mencoder:Provides: mencoder-i18n-world = %version-%release}

%description i18n-world
Languages support for %Name (except ru%{?_enable_nls: and uk}).


%package i18n-ru
Group: Video
Summary: Russian language support for %Name
BuildArch: noarch
Conflicts: %name-i18n < 1.0-35.22229.1
%{?_enable_mencoder:Provides: mencoder-i18n-ru = %version-%release}

%description i18n-ru
Russian language support for %Name.


%if_enabled nls
%package i18n-uk
Group: Video
Summary: Ukrainian language support for %Name
BuildArch: noarch
Conflicts: %name-i18n < 1.0-35.22229.1
%{?_enable_mencoder:Provides: mencoder-i18n-uk = %version-%release}

%description i18n-uk
Ukrainian language support for %Name.
%endif


%prep
%setup -q -n %Name-%pkgver
%patch0 -p1

%{?svnrev:subst 's/UNKNOWN/%svnrev/' version.sh}

subst 's|\\/\\/|//|g' help/help_mp-zh_??.h
sed -i '/\(VP8E_UPD_ENTROPY\|VP8E_UPD_REFERENCE\|VP8E_USE_REFERENCE\)/d' ffmpeg/libavcodec/libvpxenc.c
ls DOCS/man/*/%lname.1 | grep -v '^DOCS/man/en/' | xargs sed -i '1i.\\" -*- mode: troff; coding: utf-8 -*-'
echo "NotShowIn=KDE;" >> etc/%lname.desktop

%build
%define _optlevel 3
%add_optflags -Wno-switch-enum -Wno-switch
%ifarch armh
%add_optflags -Wa,-mimplicit-it=thumb
%endif
export CFLAGS="%optflags"
./configure \
	--target=%_target \
	--prefix=%_prefix \
	--bindir=%_bindir \
	--mandir=%_mandir \
	--libdir=%_libdir \
	--datadir=%_datadir/%name \
	--confdir=%_sysconfdir/%name \
%ifarch i586
	--disable-relocatable \
%endif
	--extra-cflags="%optflags %{?_enable_smb:$(pkg-config --cflags smbclient)}" \
	%{subst_enable mplayer} \
	--extra-libs-mplayer="-lvorbisenc" \
	%{subst_enable mencoder} \
	--extra-libs-mencoder="-lvorbisenc" \
	%{subst_enable xss} \
	%{subst_enable_to lame mp3lame} \
	%{subst_enable_to lame mp3lame-lavc} \
	%{subst_enable gui} \
	%{subst_enable termcap} \
	%{subst_enable termios} \
	%{subst_enable iconv} \
	%{subst_enable shm} \
	%{subst_enable langinfo} \
	%{subst_enable lirc} \
	%{subst_enable lircc} \
	%{subst_enable joystick} \
	%{subst_enable_to apple_ir apple-ir} \
	%{subst_enable xf86keysym} \
	%{subst_enable tv} \
	%{subst_enable_to tv_v4l1 tv-v4l1} \
	%{subst_enable_to tv_v4l2 tv-v4l2} \
	%{subst_enable radio} \
	%{subst_enable_to radio_v4l1 radio-v4l} \
	%{subst_enable_to radio_v4l2 radio-v4l2} \
	%{subst_enable_to radio_capture radio-capture} \
	%{subst_enable pvr} \
	%{subst_enable rtc} \
	%{subst_enable_to network networking} \
	%{subst_enable gnutls} \
	%{subst_enable winsock2}_h \
	%{subst_enable smb} \
	%{subst_enable live} \
	%{subst_enable dvdnav} \
	%{subst_enable dvdread} \
	%{subst_enable vdpau} \
	%{subst_enable xrender} \
	%{subst_enable_to dvdread_int dvdread-internal} \
	%{subst_enable cdparanoia} \
	%{subst_enable_to bitmap_font bitmap-font} \
	%{subst_enable freetype} \
	%{subst_enable fontconfig} \
	%{subst_enable unrarexec} \
	%{subst_enable_to osdmenu menu} \
	%{subst_enable sortsub} \
	%{subst_enable fribidi} \
	%{subst_enable enca} \
	%{subst_enable inet6} \
	%{subst_enable ftp} \
	%{subst_enable vstream} \
	%{subst_enable pthreads} \
	%{subst_enable ass} \
	%{subst_enable_to ass_int ass-internal} \
	%{subst_enable rpath} \
	%{subst_enable bluray} \
	%{subst_enable cddb} \
	%{subst_enable librtmp} \
	%{subst_enable nemesi} \
	%{subst_enable mng} \
	%{subst_enable gif} \
	%{subst_enable png} \
	%{subst_enable jpeg} \
	%{subst_enable_to openjpeg libopenjpeg} \
	%{subst_enable libcdio} \
	%{subst_enable_to lzo liblzo} \
	%{subst_enable_to win32 win32dll} \
	%{?_enable_win32:--codecsdir=%win32_libdir} \
	%{subst_enable qtx} \
	%{subst_enable xanim} \
	%{subst_enable real} \
	%{subst_enable xvid} \
	%{subst_enable_to xvid_lavc xvid-lavc} \
	%{subst_enable x264} \
	%{subst_enable_to x264_lavc x264-lavc} \
%if_enabled ffmpeg
%if_enabled shared_ffmpeg
	--disable-ffmpeg_a \
	--enable-ffmpeg_so \
%else
	--disable-ffmpeg_so \
	--enable-ffmpeg_a \
%endif
%else
	--disable-ffmpeg_a \
	--disable-ffmpeg_so \
%endif
	%{subst_enable postproc} \
	%{subst_enable_to vf_lavfi vf-lavfi} \
	%{subst_enable libavcodec_mpegaudio_hp} \
	%{subst_enable tremor} \
	%{subst_enable_to vorbis libvorbis} \
	%{subst_enable speex} \
	%{subst_enable theora} \
	%{subst_enable faad} \
	%{subst_enable faac} \
	%{subst_enable ladspa} \
	%{subst_enable_to bs2b libbs2b} \
	%{subst_enable_to dca libdca} \
	%{subst_enable libdv} \
	%{subst_enable crystalhd} \
	%{subst_enable mad} \
	%{subst_enable toolame} \
	%{subst_enable twolame} \
	%{subst_enable xmms} \
	%{subst_enable liba52} \
	%{subst_enable libmpeg2} \
	%{subst_enable_to libmpeg2_int libmpeg2-internal} \
	%{subst_enable musepack} \
	%{subst_enable_to nut libnut} \
	%{subst_enable libgsm} \
	%{subst_enable_to amrnb libopencore_amrnb} \
	%{subst_enable_to amrwb libopencore_amrwb} \
	%{subst_enable_to libvpx_lavc libvpx-lavc} \
	%{subst_enable libopus} \
	%{subst_enable libdca} \
	%{subst_enable vidix} \
	%{subst_enable gl} \
	%{subst_enable dga1} \
	%{subst_enable dga2} \
	%{subst_enable vesa} \
	%{subst_enable svga} \
	%{subst_enable sdl} \
	%{subst_enable aa} \
	%{subst_enable caca} \
	%{subst_enable ggi} \
	%{subst_enable ggiwmh} \
	%{subst_enable directx} \
	%{subst_enable dxr2} \
	%{subst_enable dxr3} \
	%{subst_enable ivtv} \
	%{subst_enable dvb} \
	%{subst_enable mga} \
	%{subst_enable xmga} \
	%{subst_enable xv} \
	%{subst_enable xvmc} \
	%{?_enable_xvmc:%{?xvmclib:--with-xvmclib=%xvmclib}} \
	%{subst_enable vm} \
	%{subst_enable xinerama} \
	%{subst_enable x11} \
	%{subst_enable xshape} \
	%{subst_enable fbdev} \
	%{subst_enable mlib} \
	%{subst_enable 3dfx} \
	%{subst_enable tdfxfb} \
	%{subst_enable s3fb} \
	%{subst_enable directfb} \
	%{subst_enable zr} \
	%{subst_enable bl} \
	%{subst_enable tdfxvid} \
	%{subst_enable tga} \
	%{subst_enable pnm} \
	%{subst_enable md5sum} \
	%{subst_enable matrixview} \
	%{subst_enable mpg123} \
	%{subst_enable yuv4mpeg} \
	%{subst_enable xvr100} \
	%{subst_enable alsa} \
	%{subst_enable_to oss ossaudio} \
	%{subst_enable arts} \
	%{subst_enable esd} \
	%{subst_enable pulse} \
	%{subst_enable jack} \
	%{subst_enable openal} \
	%{subst_enable nas} \
	%{subst_enable sgiaudio} \
	%{subst_enable sunaudio} \
	%{subst_enable_to waveout win32waveout} \
	%{subst_enable select} \
	%{subst_enable dart} \
	%{subst_enable kai} \
	%{subst_enable kva} \
	%{subst_enable select} \
	%{subst_enable_to cpu_detection runtime-cpudetection} \
	--cc=%__cc \
	%{?asm:--as=%asm} \
	--charset=%{?charset:%charset}%{!?charset:UTF-8} \
	--language=%{?language:"%language"}%{!?language:all} \
	%{subst_enable mmx} \
	%{subst_enable mmxext} \
	%{subst_enable 3dnow} \
	%{subst_enable 3dnowext} \
	%{subst_enable sse} \
	%{subst_enable sse2} \
	%{subst_enable ssse3} \
	%{subst_enable altivec} \
	%{subst_enable fastmemcpy} \
	%{subst_enable profile} \
	%{subst_enable sighandler} \
	%{subst_enable_to gdb crash-debug} \
	%{subst_enable_to dynamic_plugins dynamic-plugins} \
%if_enabled debug
	--enable-debug=3
%else
	--disable-debug
%endif

%make_build

%{?_enable_nls:%make_build -C po}

# make conf file
sed	-e 's/^@VO@/vo = %default_vo/' \
	-e 's/^@AO@/ao = %default_ao/' \
	-e 's|@CONF_FILE@|%_sysconfdir/%name/%lname.conf|g' \
	-e 's|@SKINS_DIR@|%_datadir/%name/skins|g' \
	%SOURCE5 > etc/%lname.conf
echo "fontconfig = %{?_enable_fontconfig:yes}%{?_disable_fontconfig:no}" >> etc/%lname.conf

%{?_with_tools:%make_build tools}

# build HTML documentation from XML files
%{?_with_htmldocs:%{?svnrev:%make_build -C DOCS/xml html-chunked}}

%if_enabled gui
for s in 128 96 72 64 48 36 32 24 22 16; do
	S=${s}x$s
	[ -e etc/%{lname}$S.png ] || convert -resize $S etc/%{lname}{256x256,$S}.png
done
%endif

gzip -9c Changelog > Changelog.gz


%install
%makeinstall_std

%if_enabled mplayer
install -d -m 0755 %buildroot%_docdir/%name-%version
install -p -m 0644 README AUTHORS Changelog.* %buildroot%_docdir/%name-%version/
install -p -m 0644 etc/{codecs,input,%lname}.conf %buildroot%_sysconfdir/%name/
%if_enabled gui
install -d -m 0755 %buildroot%_datadir/%name/skins
tar -C %buildroot%_datadir/%name/skins -xf %SOURCE4
ln -s standard %buildroot%_datadir/%name/skins/default
install -d -m 0755 %buildroot%_datadir/%name/skins/0
convert -size 8x1 xc:black -define png:format=png24 %buildroot%_datadir/%name/skins/0/0.png
cat >> %buildroot%_datadir/%name/skins/0/skin <<__EOF__
section = movieplayer
  window = main
    decoration = disable
    base = 0, 0, 0
  end
  window = video
    base = 0, -1, -1, 640, 480
    background = 0, 0, 0
  end
end
__EOF__
%endif
%{?_enable_freetype:%{?_disable_fontconfig:ln -s ../fonts/type1/urw/n019003l.pfb %buildroot%_datadir/%name/subfont.ttf}}
%{?_enable_osdmenu:install -p -m 0644 etc/menu.conf %buildroot%_sysconfdir/%name/}
%{?_enable_dvb:install -p -m 0644 etc/dvb-menu.conf %buildroot%_sysconfdir/%name/}

%if_with tools
install -p -m 0755 TOOLS/{alaw-gen,asfinfo,avi-fix,avisubdump,dump_mp4,movinfo,netstream,subrip,vivodump} %buildroot/%_bindir/
for f in vobshift; do
	install -p -m 0755 TOOLS/$f.py %buildroot/%_bindir/$f
done
for f in calcbpp countquant plotpsnr subedit wma2ogg %{?_enable_mencoder:dvd2divxscript}; do
	install -p -m 0755 TOOLS/$f.pl %buildroot/%_bindir/$f
done
%ifarch %ix86
install -p -m 0755 TOOLS/w32codec_dl.pl %buildroot/%_bindir/w32codec_dl
%endif
for f in aconvert divx2svcd mencvcd midentify mpconsole mplmult psnr-video subsearch %{?_enable_mencoder:qepdvcd}; do
	install -p -m 0755 TOOLS/$f.sh %buildroot/%_bindir/$f
done
install -pD -m 0644 {TOOLS,%buildroot%_docdir/%name-tools-%version}/README
%endif
%endif

# docs
for l in $(ls DOCS/man | grep -v '^en$'); do
%if_enabled mplayer
	install -pD -m 0644 DOCS/man/$l/%lname.1 %buildroot%_mandir/$l/man1/%lname.1
	%{?_enable_mencoder:ln -sf %lname.1 %buildroot%_mandir/$l/man1/mencoder.1}
%else
	%{?_enable_mencoder:install -pD -m 0644 DOCS/man/$l/mencoder.1 %buildroot%_mandir/$l/man1/mencoder.1}
%endif
done
rm -f %buildroot%_man1dir/mencoder.1
%{?_enable_mencoder:install -p -m 0644 DOCS/man/en/%lname.1 %buildroot%_man1dir/mencoder.1}
%if_with htmldocs
for l in cs de en es fr hu it pl ru zh_CN; do
	install -d %buildroot%_docdir/%name-%version/$l
	install -p -m 0644 DOCS/HTML/$l/{*.html,*.css} %buildroot%_docdir/%name-%version/$l/
done
%endif
install -d %buildroot%_docdir/%name-%version/tech/realcodecs
install -p -m 0644 DOCS/tech/{MAINTAINERS,TODO,*.txt,mpsub.sub,playtree,wishlist} %buildroot%_docdir/%name-%version/tech/
install -p -m 0644 DOCS/tech/realcodecs/{TODO,*.txt} %buildroot%_docdir/%name-%version/tech/realcodecs/
%find_lang --with-man %lname %lname-man

%if_enabled nls
for l in po/*.gmo; do
	install -pD -m 0644 $l %buildroot%_datadir/locale/$(basename $l .gmo)/LC_MESSAGES/%name.mo
done
%find_lang %lname
%endif

%if_enabled gui
for s in 256 128 96 72 64 48 36 32 24 22 16; do
	S=${s}x$s
	install -pD -m 0644 {etc/%lname$S,%buildroot%_iconsdir/hicolor/$S/apps/%lname}.png
done
install -pD -m 0644 {etc/%lname,%buildroot%_desktopdir/%gname}.desktop
%endif

%{?_enable_mplayer:install -pD -m 0644 %SOURCE2 %buildroot/%_desktopdir/%lname.desktop}

%{?_enable_mplayer:%{?_enable_vidix:%add_verify_elf_skiplist %_libdir/%lname/vidix/*}}


%if_enabled mplayer
%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/README
%doc %_docdir/%name-%version/AUTHORS
%_bindir/%lname
%_man1dir/%lname.*
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/codecs.conf
%config(noreplace) %verify(not size mtime md5) %_sysconfdir/%name/%lname.conf
%config(noreplace) %verify(not size mtime md5) %_sysconfdir/%name/input.conf
%{?_enable_osdmenu:%config(noreplace) %verify(not size mtime md5) %_sysconfdir/%name/menu.conf}
%{?_enable_dvb:%config(noreplace) %verify(not size mtime md5) %_sysconfdir/%name/dvb-menu.conf}
%dir %_datadir/%name
%_desktopdir/%lname.desktop
%if_disabled fontconfig
%if_enabled freetype
%config(missingok,noreplace) %verify(not link size mtime md5) %_datadir/%name/subfont.ttf
%else
%_datadir/%name/font
%endif
%endif
%if_enabled gui
%_bindir/%gname
%_desktopdir/%gname.desktop
#%%_datadir/pixmaps/*
%_iconsdir/hicolor/*/apps/*
%_datadir/%name/skins
%endif


%if_enabled mencoder
%files -n mencoder
%_bindir/mencoder
%_man1dir/mencoder.*
%if_disabled mplayer
%doc README AUTHORS Changelog.*
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/codecs.conf
%endif
%endif


%if_with tools
%files tools
%_docdir/%name-tools-%version
%_bindir/*
%{?_enable_mplayer:%exclude %_bindir/%lname}
%{?_enable_mencoder:%exclude %_bindir/mencoder}
%{?_enable_gui:%exclude %_bindir/%gname}
%endif


%files docs


%files doc-world
%dir %_docdir/%name-%version
%lang(cs) %_docdir/%name-%version/cs
%lang(de) %_docdir/%name-%version/de
%lang(es) %_docdir/%name-%version/es
%lang(fr) %_docdir/%name-%version/fr
%lang(hu) %_docdir/%name-%version/hu
%lang(it) %_docdir/%name-%version/it
%lang(pl) %_docdir/%name-%version/pl
%lang(zh_CN) %_docdir/%name-%version/zh_CN


%files doc-tech
%dir %_docdir/%name-%version
%_docdir/%name-%version/tech
%_docdir/%name-%version/Changelog.*


%files doc-en
%dir %_docdir/%name-%version
%_docdir/%name-%version/en


%files doc-ru
%dir %_docdir/%name-%version
%_docdir/%name-%version/ru
%endif


%files i18n


%files i18n-ru
%_mandir/ru
%{?_enable_nls:%_datadir/locale/ru/LC_MESSAGES/*}


%if_enabled nls
%files i18n-uk
%_datadir/locale/uk/LC_MESSAGES/*
%endif


%files i18n-world
%lang(cs) %_mandir/cs
%lang(de) %_mandir/de
%lang(es) %_mandir/es
%lang(fr) %_mandir/fr
%lang(hu) %_mandir/hu
%lang(it) %_mandir/it
%lang(pl) %_mandir/pl
%lang(zh_CN) %_mandir/zh_CN
%if_enabled nls
%lang(bg) %_datadir/locale/bg/LC_MESSAGES/*
%lang(cs) %_datadir/locale/cs/LC_MESSAGES/*
%lang(de) %_datadir/locale/da/LC_MESSAGES/*
%lang(de) %_datadir/locale/de/LC_MESSAGES/*
%lang(el) %_datadir/locale/el/LC_MESSAGES/*
%lang(es) %_datadir/locale/es/LC_MESSAGES/*
%lang(fr) %_datadir/locale/fr/LC_MESSAGES/*
%lang(hu) %_datadir/locale/hu/LC_MESSAGES/*
%lang(it) %_datadir/locale/it/LC_MESSAGES/*
%lang(ja) %_datadir/locale/ja/LC_MESSAGES/*
%lang(ko) %_datadir/locale/ko/LC_MESSAGES/*
%lang(mk) %_datadir/locale/mk/LC_MESSAGES/*
%lang(nb) %_datadir/locale/nb/LC_MESSAGES/*
%lang(nl) %_datadir/locale/nl/LC_MESSAGES/*
%lang(pl) %_datadir/locale/pl/LC_MESSAGES/*
%lang(pt) %_datadir/locale/pt_BR/LC_MESSAGES/*
%lang(ro) %_datadir/locale/ro/LC_MESSAGES/*
%lang(sk) %_datadir/locale/sk/LC_MESSAGES/*
%lang(sv) %_datadir/locale/sv/LC_MESSAGES/*
%lang(tr) %_datadir/locale/tr/LC_MESSAGES/*
%lang(zh_CN) %_datadir/locale/zh_CN/LC_MESSAGES/*
%lang(zh_TW) %_datadir/locale/zh_TW/LC_MESSAGES/*
%endif


%changelog
* Thu Jun 04 2020 Andrey Cherepanov <cas@altlinux.org> 1.4-alt1.1.p9
- Rebuild with libdvdnav-6.1.0.

* Sat Apr 20 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4-alt1
- 1.4 (ALT#36638).
- built with system FFmpeg (ALT#35031).
- built with gnutls, libopus and libdca support.

* Thu Apr 11 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.3.0-alt5
- Fixed build on ppc64le architecture.

* Thu Feb 21 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.3.0-alt4
- fixed FTBFS with new Samba

* Wed Jan 09 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.3.0-alt3
- rebuilt without librtmp

* Wed Jun 20 2018 Anton Farygin <rider@altlinux.ru> 1.3.0-alt2
- rebuilt with libbluray.so.1
- disabled crystalhd support
- fixed build on aarch64

* Sun Jan 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1.1
- rebuild against libcdio.so.18

* Fri Mar 17 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.3.0-alt1
- 1.3.0 (ALT#32975)
- rebuilt with live555 (ALT#30778)
- dropped non-upstream vaapi support
- converted all the descriptions from CP1251 to UTF-8

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 1.1.1-alt16
- hide menu items from KDE (ALT#31522)

* Wed Mar 09 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.1-alt15
- rebuilt with recent libx264

* Fri Aug 21 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.1-alt14
- rebuilt with recent libcdio

* Sat Dec 27 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.1-alt13
- rebuilt without live555

* Mon May 12 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.1-alt12
- rebuilt with recent libx264

* Tue Feb 04 2014 Led <led@altlinux.ru> 1.1.1-alt11
- fixed for new (0.34.0) VA API

* Mon Sep 16 2013 Led <led@altlinux.ru> 1.1.1-alt10
- remove gmplayer subpackage

* Thu Sep 12 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.1-alt9
- rebuilt with recent libx264

* Tue Jun 04 2013 Led <led@altlinux.ru> 1.1.1-alt8
- added empty skin (named '0') without control panel

* Mon Jun 03 2013 Led <led@altlinux.ru> 1.1.1-alt7
- mp_msg2po.awk: fix po generation
- mp_help2msg.awk: fixed
- fixed ru translation
- updated uk translation

* Fri May 31 2013 Led <led@altlinux.ru> 1.1.1-alt6
- updated ru translation
- updated uk translation
- fixed and cleaned up mp_*.awk scripts
- more verbose mp_msg2po.awk script
- fixed nls support
- added to %%name-tools subpackage
  + netstream
  + subrip
  + vivodump

* Tue May 28 2013 Led <led@altlinux.ru> 1.1.1-alt5
- upstream fixes
- fixed License
- cleaned up BuildRequires
- cleaned up spec
- fixed subfont.ttf symlink
- added VA-API support
- enabled:
  + vaapi
  + xrender

* Mon May 27 2013 Led <led@altlinux.ru> 1.1.1-alt4
- fixed encoding of manpages

* Mon May 27 2013 Led <led@altlinux.ru> 1.1.1-alt3
- set encoding of manpages

* Mon May 27 2013 Led <led@altlinux.ru> 1.1.1-alt2
- removed unneeded %%name-i18n-ru subpackage requires

* Sat May 24 2013 Led <led@altlinux.ru> 1.1.1-alt1
- 1.1.1 (ALT#28546)
- cleaned up spec
- enabled
  + apple_ir
  + bs2b
  + crystalhd
  + fribidi
  + inet6
  + libvpx_lavc
  + openjpeg
  + pvr
  + shm
  + vcd
- disabled:
  + tga
- build with optlevel 3
- parallel build
- removed patches:
  + MPlayer-1.0pre4-alt-explicit_gif.patch
  + mplayer-svn-r23722-VIDM-win32-codec.patch

* Fri Feb 22 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt35.32772.11
- tweak build parameters for arm

* Sun Feb 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt35.32772.10
- NMU: dropped StartupNotify=true from mplayer-svn-r32603-desktop.patch
  as this is not implemented in current gmplayer.
  Thanks to Alexei V. Mezin.

* Tue Nov 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt35.32772.9
- added mplayer-console.desktop - a mime handler for the console mplayer.
  Nowadays even mc use mime to launch applications ;) (closes: 27953)

* Tue Oct 16 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt35.32772.8
- rebuilt with recent live555

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt35.32772.7
- Rebuilt with libpng15

* Mon Jun 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt35.32772.6
- Fixed build

* Mon Jan 30 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt35.32772.5
- rebuilt with recent x264

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt35.32772.4.1
- Rebuild with Python-2.7

* Tue Nov 01 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt35.32772.4
- rebuilt with recent livemedia

* Mon Aug 01 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt35.32772.3
- rebuilt with recent x264

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt35.32772.2
- Rebuilt for debuginfo

* Sun Jan 09 2011 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.32772.1
- new SVN snapshot (revision 32772)
  + some AAC playback fixes;
  + drop internal faad.
- update opengl buildreq.
- fix gl video output.

* Fri Dec 24 2010 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.32728.1
- new SVN snapshot (revision 32728).

* Sun Nov 14 2010 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.32624.1
- new SVN snapshot (revision 32624). closes #24513.

* Mon Nov 08 2010 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.32603.1
- new SVN snapshot (revision 32603).
- fix track selection for lavf demuxer (since r30485 reimar has changed this
  mechanizm, for aviheader troubles still here).
- add buildreq for bluray.

* Sat Nov 06 2010 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.32566.3
- fix ass build.

* Sat Nov 06 2010 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.32566.2
- disable old features:
  + esd, arts, nas (old, subst'ed with pulse);
  + openal (openal uses oss);
  + dirac (rapid upstream), nut (not used with anyone);
  + nemesi (dup code from librtmp);
  + vidix, svga, mga, xmga, xvmc and other old vo's.

* Sat Oct 30 2010 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.32566.1
- new SVN snapshot (revision 32566).
- fix CVE-2010-3429 (closes: #24299).
- features:
  + enable new codecs: libgsm, dca, coreaudio, corevideo, amr, openjpeg;
  + enable ssse3 optimization;
  + enable bluray, cddb, librtmp support;
  + remove devfs support (removed from upstream);
  + remove dvdhead (removed from upstream);
  + remove dpms opt (it was already named as xshape);
  + xanim and real codecsdir (options was removed in upstream).
- patches:
  + update vbe and subreader patches;
  + remove builddoc patch
- fix aalib /dev/vcsa detection (closes: #17636).

* Mon Mar 01 2010 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.30485.4
- build with libopenal1

* Wed Feb 10 2010 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.30485.3
- disable XMMS input plugins (peoples does not want required by xmms gtk+).

* Tue Feb 02 2010 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.30485.2
- rebuild with libx264.so.85.

* Tue Feb 02 2010 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.30485.1
- new SVN snapshot (revision 30485).
- patches:
  + vaapi: remove (ffmpeg has own vaapi code);
  + subreader: update.
- features:
  + fribidi: disable (it does not build on x86_64);
  + tv-teletext: remove (it is not supported now);
  + yasm: first add;
  + directfb: disable (configure failes when try to detect it);
  + xss, dpms: first add.

* Tue Feb 02 2010 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29766.2
- rebuild with libva 0.31.

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real@altlinux.org> 1.0-alt35.29766.1.1
- Rebuilt with python 2.6

* Fri Oct 09 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29766.1
- new SVN snapshot (revision 29766).
- update patches:
  + vaapi: apply mplayer-vaapi-20090914
  + alt-changes: minor fix x86_64 detection
  + update dirac patch

* Sun Sep 27 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29579.5
- disable faac (closes: #21720)

* Fri Sep 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt35.29579.4
- rebuild with libdvdread.so.4

* Sat Sep 19 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29579.3
- rebuild with new libdvdread

* Thu Sep 03 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29579.2
- enable svga build back.

* Mon Aug 31 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29579.1
- new SVN snapshot (revision 29579).
- update patches:
  + desktop patch;
  + vaapi: apply mplayer-vaapi-20090828.
- split alt-changes patch into separate alt-changes, vaapi and nls patches.

* Wed Aug 26 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29350.4
- disable svga build (svga is orphaned)

* Tue Jun 23 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29350.3
- rebuild with libpng12-1.2.37-al2

* Tue Jun 16 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29350.2
- change global optimization level (fast fix mkv playing on x86_64)

* Fri Jun 05 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29350.1
- new SVN snapshot (revision 29350) with ffmpeg revision 19117.

* Sun May 31 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29330.1
- new SVN snapshot (revision 29330) with ffmpeg revision 19062.

* Thu May 28 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29325.2
- new SVN snapshot (revision 29325) with ffmpeg revision 18971.

* Fri May 22 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29318.2
- new SVN snapshot (revision 29318)
  + Set XVR100 make variable. Fixes compilation when support for xvr100 was
    detected (r29315)
  + Make SwScaler recognize RGB48 BE/LE colourspaces (not support though)
    (r29316)
  + Let SwScaler know that RGB48 BE/LE is 16-bits per component format (r29317)
- remove artsc-ldflags patch - merge into alt-changes

* Sun May 17 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29311.2
- touch to rebuild with alsa

* Sat May 16 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29311.1
- new SVN snapshot (revision 29311)
- remove ffmpeg patches (including amr) untill it will be fixed.
- merge vaapi-nls and nls patches into alt-changes patch.
- remove bmovl-test due to build failure on x86_64.

* Sat May 16 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29310.1
- new SVN snapshot (revision 29310)

* Tue May 12 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29298.1
- new SVN snapshot (revision 29298)

* Thu Apr 30 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29241.2
- new SVN snapshot (revision 29241)

* Mon Apr 27 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29238.2
- add %lname-svn-r29238-vaapi-nls.patch and enable build with vaapi. patch
  requires nls patch to be applied first.

* Sun Apr 26 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29238.1
- new SVN snapshot (revision 29238)
- enable vdpau video output
- updated patches:
  + ffmpeg-svn-r18694-amr.patch (refreshed and enabled back)

* Fri Apr 24 2009 Afanasov Dmitry <ender@altlinux.org> 1.0-alt35.29229.3
- new SVN snapshot (revision 29229)
- disable 3dfx video output (requires dga's to enable)
- add cumulative alt-changes patch (see git for details):
  + merge %lname-svn-r29229-configure.patch
  + merge %lname-svn-r27654-ext_ffmpeg.patch
  + fix libnut.h types (demux_nut.c)
  + fix live555 detection (configure)
  + fix dirac detection (configure)
  + fix faac and faad detection (configure)
  + append bmovl-test to tools list (Makefile)
- updated patches:
  + %lname-r29229-alt-artsc_ldflags.patch
  + %lname-svn-r29229-nls.patch
- removed patches:
  + %lname-svn-r29229-configure.patch (merge into alt-changes)
  + %lname-svn-r27654-ext_ffmpeg.patch (merge into alt-changes)
  + ffmpeg-svn-r15375-x264-65.patch (x264 code is rewritten)
  + %lname-svn-r27482-gui_nls.patch (merged into %lname-svn-r29229-nls.patch)
- disabled pathes
  + %lname-uni-svn26991.patch

* Sat Jan 10 2009 Led <led@altlinux.ru> 1.0-alt35.27654.3
- build with external libfaad (#6638)

* Sun Dec 14 2008 Led <led@altlinux.ru> 1.0-alt35.27654.2
- cleaned up spec
- fixed build with libx264.so.65
- updated BuildRequires

* Mon Sep 22 2008 Led <led@altlinux.ru> 1.0-alt35.27654.1
- new SVN snapshot (revision 27654)
- updated %lname-svn-r27654-configure.patch
- cleaned up %lname-svn-r27654-ext_ffmpeg.patch
  (partially fixed in upstream)

* Sun Aug 31 2008 Led <led@altlinux.ru> 1.0-alt35.27498.2
- updated:
  + ffmpeg-svn-r14967-xvmc-vld.patch
  + ffmpeg-svn-r14967-amr.patch
  + %lname-svn-r27498-ext_ffmpeg.patch
- build without shared ffmpeg

* Sat Aug 30 2008 Led <led@altlinux.ru> 1.0-alt35.27498.1
- new SVN snapshot (revision 27498)
- removed %lname-svn-r27482-dvdread.patch (fixed in upstream)
- cleaned up BuildRequires

* Tue Aug 26 2008 Led <led@altlinux.ru> 1.0-alt35.27482.1
- new SVN snapshot (revision 27482):
  + MLP decoder via lavc
  + use lavc ADPCM codecs by default
- updated:
  + %lname-svn-r27482-dirac.patch
  + %lname-svn-r27482-dvdread.patch
  + %lname-svn-r27482-nls.patch
  + %lname-svn-r27482-gui_nls.patch
  + %lname-svn-r27482-configure.patch
- added %lname-svn-r27482-desktop.patch

* Mon Jul 21 2008 Led <led@altlinux.ru> 1.0-alt35.27330.1
- new SVN snapshot (revision 27330):
  + video game codecs:
    Playstation MDEC video,
    ADPCM XA audio,
    EA Maxis XA ADPCM audio,
    RL2 video,
    Beam Software SIFF video,
    V.Flash PTX video
  + image decoders:
    Sun rasterfile,
    PCX image
  + support for chapters in lavf demuxer
- updated:
  + %lname-svn-r27330-configure.patch
  + %lname-svn-r27330-ext_ffmpeg.patch
- removed:
  + %lname-svn-r25454-vo_vidix.patch

* Wed Jun 18 2008 Led <led@altlinux.ru> 1.0-alt35.27097.1
- new SVN snapshot (revision 27097):
  + prefer lavf musepack demuxer over libmpdemux
  + prefer lavf MOV demuxer over libmpdemux
  + support -slang in lavf demuxer
  + support nosound switching in lavf demuxer
  + support libass in lavf demuxer
  + support VOBsub in lavf demuxer
  + support MOV subtitle format
  + support for attachments in lavf demuxer
  + allow specifying the TV standard for each channel
  + add force-pbo suboption for faster output in vo_gl
- updated %lname-svn-r27097-configure.patch

* Thu Jun 05 2008 Led <led@altlinux.ru> 1.0-alt35.26991.2
- updated %{lname}svn_trunk_revision_26980-dirac-0.10.x.patch

* Wed Jun 04 2008 Led <led@altlinux.ru> 1.0-alt35.26991.1
- new SVN snapshot (revision 26991)
- updated:
  + %lname-svn-r26991-dirac-0.9.1.patch
  + %lname-svn-r26992-gui_nls.patch
  + %lname-uni-svn26991.patch
-added %lname-svn-r26991-dvdread.patch

* Tue May 27 2008 Led <led@altlinux.ru> 1.0-alt35.26909.1
- new SVN snapshot (revision 26909)
- updated:
  + %lname-uni-svn26909.patch
  + %lname-svn-r26909-gui_nls.patch
  + %lname-svn-r26909-configure.patch

* Thu May 15 2008 Led <led@altlinux.ru> 1.0-alt35.26783.1
- new SVN snapshot (revision 26783)

* Wed May 14 2008 Led <led@altlinux.ru> 1.0-alt35.26763.1
- new SVN snapshot (revision 26763)

* Sat May 10 2008 Led <led@altlinux.ru> 1.0-alt35.26708.1
- new SVN snapshot (revision 26708):
  + BFI video decoder
- removed ffmpeg-svn-r12807-dirac-0.9.x.patch (added in upstream)
- updated:
  + %lname-svn-r26706-ext_ffmpeg.patch (partially fixed in upstream)
  + %lname-svn-r26706-dirac-0.9.1.patch
  + %lname-uni-svn26706.patch
  + %lname-svn-r26708-configure.patch
  + ffmpeg-svn-r13104-amr.patch

* Sat Apr 19 2008 Led <led@altlinux.ru> 1.0-alt35.26470.2
- build with external ffmpeg

* Sat Apr 19 2008 Led <led@altlinux.ru> 1.0-alt35.26470.1
- new SVN snapshot (revision 26470)
- updated %lname-svn-r26470-dirac-0.9.1.patch

* Wed Apr 16 2008 Led <led@altlinux.ru> 1.0-alt35.26454.2
- build with external ffmpeg

* Tue Apr 15 2008 Led <led@altlinux.ru> 1.0-alt35.26454.1
- new SVN snapshot (revision 26454)
- removed %lname-svn-r26454-mencoder.patch (fixed in upstream)
- cleaned up %lname-svn-r26454-ext_ffmpeg.patch
- build with internal ffmpeg

* Tue Apr 15 2008 Led <led@altlinux.ru> 1.0-alt35.26450.1
- new SVN snapshot (revision 26450)
- updated:
  + %lname-svn-r26450-dirac-0.9.1.patch
  + %lname-svn-r26450-gui.patch
  + %lname-svn-r26450-gui_nls.patch
  + %lname-svn-r26450-configure.patch
  + %lname-svn-r26450-ext_ffmpeg.patch
  + %lname-svn-r26450-builddocs.patch
  + ffmpeg-svn-r12807-dirac-0.9.x.patch
  + ffmpeg-svn-r12807-amr.patch
- added %lname-svn-r26450-mencoder.patch
- replaced ffmpeg-uni-svn-r10644.patch with
  ffmpeg-svn-r12807-xvmc-vld.patch

* Fri Apr 04 2008 Led <led@altlinux.ru> 1.0-alt35.25957.5
- fixes desktop-mime-entry

* Tue Mar 04 2008 Led <led@altlinux.ru> 1.0-alt35.25957.4
- fixed typo in spec (#14746)

* Sun Mar 02 2008 Led <led@altlinux.ru> 1.0-alt35.25957.3
- added icons
- fixed BuildRequires

* Wed Feb 27 2008 Led <led@altlinux.ru> 1.0-alt35.26107.1
- new SVN snapshot (revision 26107)
- updated:
  + %lname-svn-r25957-configure.patch
  + %lname-svn-r26107-gui.patch
  + %lname-svn-r26107-ext_ffmpeg.patch

* Wed Feb 27 2008 Led <led@altlinux.ru> 1.0-alt35.25957.2
- fixed ffmpeg-svn-r11246-dirac-0.9.x.patch
- updated %lname-svn-r25957-configure.patch (fixed #13791 again)

* Tue Feb 19 2008 Led <led@altlinux.ru> 1.0-alt35.26031.1
- new SVN snapshot (revision 26031)
- fixed ffmpeg-svn-r11246-dirac-0.9.x.patch

* Tue Feb 19 2008 Led <led@altlinux.ru> 1.0-alt35.26030.1
- new SVN snapshot (revision 26030)

* Tue Feb 12 2008 Led <led@altlinux.ru> 1.0-alt35.25987.1
- new SVN snapshot (revision 25987)
- updated %lname-svn-r25987-ext_ffmpeg.patch

* Wed Feb 06 2008 Led <led@altlinux.ru> 1.0-alt35.25957.1
- new SVN snapshot (revision 25957):
  + stack overflow in demuxer_audio.c fixed
  + buffer overflow in demuxer_mov.c fixed
- updated:
  + %lname-svn-r25895-ext_ffmpeg.patch
  + %lname-svn-r25957-dirac-0.9.1.patch
  + ffmpeg-svn-r11872-dirac-0.9.x.patch

* Sun Jan 27 2008 Led <led@altlinux.ru> 1.0-alt35.25873.2
- build with internal FAAD

* Sat Jan 26 2008 Led <led@altlinux.ru> 1.0-alt35.25873.1
- new SVN snapshot (revision 25873)
- updated %lname-svn-r25873-ext_ffmpeg.patch

* Thu Jan 24 2008 Led <led@altlinux.ru> 1.0-alt35.25844.1
- new SVN snapshot (revision 25844)
- updated ffmpeg-svn-r11604-dirac-0.9.x.patch
- updated %lname-svn-r25844-dirac-0.9.0.patch

* Mon Jan 21 2008 Led <led@altlinux.ru> 1.0-alt35.25826.1
- new SVN snapshot (revision 25826):
  + buffer overflow in url.c fixed
  + buffer overflow in stream_cddb.c fixed
- updated:
  + %lname-svn-r25826-dirac-0.8.x.patch
  + %lname-svn-r25826-configure.patch
  + %lname-svn-r25826-ext_ffmpeg.patch
- build with external libfaad

* Fri Jan 11 2008 Led <led@altlinux.ru> 1.0-alt35.25678.1
- new SVN snapshot (revision 25678)
- updated %lname-uni-svn25678.patch

* Fri Jan 11 2008 Led <led@altlinux.ru> 1.0-alt35.25669.1
- new SVN snapshot (revision 25669)
- updated:
  + %lname-svn-r25669-gui_nls.patch
  + %lname-svn-r25669-ext_ffmpeg.patch

* Tue Dec 25 2007 Led <led@altlinux.ru> 1.0-alt35.25498.1
- new SVN snapshot (revision 25498)
- removed %lname-svn-r25454-dvdnav.patch
- updated %lname-svn-r25505-configure.patch (fixed #13791)

* Sat Dec 22 2007 Led <led@altlinux.ru> 1.0-alt35.25487.1
- new SVN snapshot (revision 25487)
- updated:
  + ffmpeg-svn-r11263-dirac-0.8.x.patch
  + %lname-svn-r25454-dirac-0.8.x.patch
  + %lname-svn-r25454-vo_vidix.patch
  + %lname-svn-r25454-configure.patch
  + %lname-svn-r25487-ext_ffmpeg.patch
- added %lname-svn-r25454-dvdnav.patch

* Mon Nov 12 2007 Led <led@altlinux.ru> 1.0-alt35.25029.1
- new SVN snapshot (revision 25029)
- fixed %%changelog

* Sun Nov 11 2007 Led <led@altlinux.ru> 1.0-alt35.25023.1
- new SVN snapshot (revision 25023)
- updated ffmpeg-svn-r11000-dirac-0.8.x.patch

* Sun Nov 11 2007 Led <led@altlinux.ru> 1.0-alt35.25017.1
- new SVN snapshot (revision 25017):
  + support for wavpack in matroska
  + add vf_scaletempo
  + rewrite dec_audio to support more filters
  + Nellymoser audio decoding via lavc
  + Basic support for Closed Captioning Roll-up mode
- updated:
  + %lname-svn-r25014-dirac-0.8.x.patch
  + %lname-svn-r25014-ext_ffmpeg.patch
- removed:
  + %lname-svn-r19389-polyp0.8.patch
  + mplayer-svn-r21128-pulseaudio.patch

* Fri Oct 12 2007 Led <led@altlinux.ru> 1.0-alt35.24764.1
- new SVN snapshot (revision 24764)
- updated ffmpeg-svn-r10703-dirac-0.8.x.patch

* Wed Oct 03 2007 Led <led@altlinux.ru> 1.0-alt35.24688.1
- new SVN snapshot (revision 24688):
  + support H.263-2000 over RTSP
  + support AMR over RTSP
  + support H.264 over RTSP
  + channel scanner for tv://
  + fine tuning for tv://
  + driver autodetection for tv://
  + libnemesi RTSP/RTP support
- updated
  + %lname-svn-r24688-configure.patch
  + %lname-svn-r24688-ext_ffmpeg.patch
  + %lname-svn-r24688-dirac-0.8.x.patch
  + ffmpeg-svn-r10636-dirac-0.8.x.patch
  + ffmpeg-uni-svn-r10644.patch
  + ffmpeg-svn-r10644-amr.patch

* Mon Aug 27 2007 Led <led@altlinux.ru> 1.0-alt35.24247.1
- new SVN snapshot (revision 24247)
- updated %lname-svn-r24244-ext_ffmpeg.patch

* Mon Aug 27 2007 Led <led@altlinux.ru> 1.0-alt35.24127.1
- new SVN snapshot (revision 24127)
- updated %lname-svn-r24244-dirac-0.7.x.patch (fixed #12627)
- updated ffmpeg-svn-r10237-dirac-0.7.x.patch
- updated %lname-svn-r24127-ext_ffmpeg.patch

* Fri Aug 17 2007 Led <led@altlinux.ru> 1.0-alt35.24081.1
- new SVN snapshot (revision 24081)
- updated mplayer-svn-r24081-nls.patch
- updated %lname-svn-r24081-ext_ffmpeg.patch

* Mon Jul 23 2007 Led <led@altlinux.ru> 1.0-alt35.23844.1
- new SVN snapshot (revision 23844)
- updated %lname-svn-r23810-configure.patch
- updated %lname-svn-r23726-gui_nls.patch
- updated %lname-svn-r23726-ext_ffmpeg.patch
- added ffmpeg-svn-r9777-dirac-0.7.x.patch
- added ffmpeg-svn-r9777-amr.patch
- removed %lname-svn-r22092-dirac.patch
- added %lname-svn-r23840-dirac-0.7.x.patch

* Fri Jul 06 2007 Led <led@altlinux.ru> 1.0-alt35.23722.1
- new SVN snapshot (revision 23722)
- updated %lname-svn-r23664-ext_ffmpeg.patch
- updated BuildRequires
- added %lname-svn-r23722-VIDM-win32-codec.patch (by icesik@ FR #12211)

* Sat Jun 23 2007 Led <led@altlinux.ru> 1.0-alt35.23606.1
- new SVN snapshot (revision 23606)
- updated %lname-svn-r23600-ext_ffmpeg.patch
- updated %lname-svn-r23592-configure.patch
- added %lname-svn-r23606-desktop.patch
- fixed %lname.desktop

* Sat Jun 16 2007 Led <led@altlinux.ru> 1.0-alt35.23560.1
- new SVN snapshot (revision 23560)
- updated %lname-svn-r23560-configure.patch

* Wed Jun 13 2007 Led <led@altlinux.ru> 1.0-alt35.23550.1
- new SVN snapshot (revision 23550):
  + Teletext support for tv:// (v4l and v4l2 only)
- cleaned up spec
- cleaned up BuildRequires
- updated %lname-svn-r23545-ext_ffmpeg.patch
- updated %lname-svn-r23547-gui.patch
- updated %lname-svn-r23545-nls.patch
- added it docs

* Sat May 19 2007 Led <led@altlinux.ru> 1.0-alt35.23340.1
- new SVN snapshot (revision 23340)
- updated %lname-svn-r23340-configure.patch

* Fri May 18 2007 Led <led@altlinux.ru> 1.0-alt35.23331.1
- new SVN snapshot (revision 23331)
- updated %lname-svn-r23331-configure.patch
- updated %lname-svn-r23331-ext_ffmpeg.patch
- cleaned up spec

* Thu May 17 2007 Led <led@altlinux.ru> 1.0-alt35.23322.1
- new SVN snapshot (revision 23322)

* Mon May 14 2007 Led <led@altlinux.ru> 1.0-alt35.23311.1
- new SVN snapshot (revision 23311):
  + Renderware TeXture Dictionary video via lavc
- updated %lname-svn-r23304-ext_ffmpeg.patch
- updated %lname-svn-r23304-configure.patch
- updated ffmpeg-uni-svn-r8990.patch
- cleaned up spec

* Tue May 08 2007 Led <led@altlinux.ru> 1.0-alt35.23272.1
- new SVN snapshot (revision 23272):
  + support for channel navigation with PVR input
- updated %lname-svn-r23272-ext_ffmpeg.patch

* Mon May 07 2007 Led <led@altlinux.ru> 1.0-alt35.23241.1
- new SVN snapshot (revision 23241)

* Sun May 06 2007 Led <led@altlinux.ru> 1.0-alt35.23238.1
- new SVN snapshot (revision 23238)
- updated %lname-uni-svn23235.diff
- updated %lname-svn-r23235-ext_ffmpeg.patch
- updated %lname-svn-r23235-configure.patch
- fixed build with mainstream libdvdnav

* Thu Apr 26 2007 Led <led@altlinux.ru> 1.0-alt35.23114.1
- new SVN snapshot (revision 23114)
- updated %lname-svn-r23114-ext_ffmpeg.patch

* Wed Apr 25 2007 Led <led@altlinux.ru> 1.0-alt35.23104.1
- new SVN snapshot (revision 23104)

* Mon Apr 23 2007 Led <led@altlinux.ru> 1.0-alt35.23099.1
- new SVN snapshot (revision 23099)
- updated %lname-svn-r23099-gui.patch
- updated %lname-svn-r23099-gui_nls.patch
- updated %lname-svn-r23099-ext_ffmpeg.patch
- updated %lname-svn-r23099-configure.patch
- added %lname-svn-r23099-demux_nut.patch

* Thu Apr 19 2007 Led <led@altlinux.ru> 1.0-alt35.23023.1
- new SVN snapshot (revision 23023)

* Mon Apr 16 2007 Led <led@altlinux.ru> 1.0-alt35.23002.1
- new SVN snapshot (revision 23002):
  + THP audio and video via lavc
- fixed %%changelog

* Tue Apr 10 2007 Led <led@altlinux.ru> 1.0-alt35.22963.1
- new SVN snapshot (revision 22963):
  + AAC-LATM, H.263-2000, AMR, H.264 over RTSP
- removed %lname-svn-r22753-libdha.patch (due upstream)
- updated %lname-uni-svn22915.diff
- updated %lname-svn-r22963-ext_ffmpeg.patch
- removed %lname-svn-r22518-mwallp.patch (due upstream)
- updated %lname-svn-r22915-configure.patch
- removed %name-fontutils package (due upstream)
- added %lname-svn-r22963-gui.patch

* Tue Mar 20 2007 Led <led@altlinux.ru> 1.0-alt35.22753.1
- new SVN snapshot (revision 22753)
- updated %lname-svn-r22753-libdha.patch
- updated %lname-svn-r22753-ext_ffmpeg.patch
- updated %lname-svn-r22753-configure.patch

* Thu Mar 15 2007 Led <led@altlinux.ru> 1.0-alt35.22590.1
- new SVN snapshot (revision 22590)
- updated %lname-svn-r22590-libdha.patch

* Wed Mar 14 2007 Led <led@altlinux.ru> 1.0-alt35.22550.1
- new SVN snapshot (revision 22550)

* Mon Mar 12 2007 Led <led@altlinux.ru> 1.0-alt35.22535.1
- new SVN snapshot (revision 22535)
- updated %lname-svn-r22518-nls.patch
- updated %lname-svn-r22518-ext_ffmpeg.patch
- updated %lname-svn-r22518-configure.patch
- updated %lname-svn-r22518-builddocs.patch
- updated ffmpeg-uni-svn-r7650.patch
- updated %lname-svn-r22518-mwallp.patch

* Wed Feb 28 2007 Led <led@altlinux.ru> 1.0-alt35.22358.1
- new SVN snapshot (revision 22358)

* Fri Feb 23 2007 Led <led@altlinux.ru> 1.0-alt35.22324.1
- new SVN snapshot (revision 22324):
  + ffmpeg video decoder handles aspect ratio changes
  + smil playlist over Real RTSP
- updated %lname-svn-r22324-gui_nls.patch
- used liblzo2
- updated %lname-svn-r22324-ext_ffmpeg.patch

* Fri Feb 16 2007 Led <led@altlinux.ru> 1.0-alt35.22230.1
- new SVN snapshot (revision 22230)
- added subpackages %name-i18n-ru, %name-i18n-uk,
  %name-i18n-world, %name-doc-world, %name-docs
- fixed configure parameters (%%build section)
- %name-i18n-ru requires man-pages-ru (#10819)
- cleaned up BuildRequires

* Thu Feb 15 2007 Led <led@altlinux.ru> 1.0-alt35.22223.1
- new SVN snapshot (revision 22223)
- updated %lname-svn-r22217-configure.patch
- added mplayer-svn-r22221-subreader.patch (fixed #10844)
- fixed BuildRequires

* Mon Feb 12 2007 Led <led@altlinux.ru> 1.0-alt35.22210.1
- new SVN snapshot (revision 22210):
  + Russian man page translation finished
  + GIF demuxer improvement
  + support for VC1 in MPEG-TS and MPEG-PS files (bd,hd)-dvd
  + support for doubleclick as input event
  + select libavformat demuxer (-lavfdopts format=)
  + MEncoder support -ffourcc with -of lavf
- enabled Dirac
- removed %Name-svn-20060707_dirac-0.5.x.patch
- cleaned up spec

* Thu Feb 08 2007 Led <led@altlinux.ru> 1.0-alt35.22173.1
- new SVN snapshot (revision 22173)
- turned off joystick and LIRC support by default in %_sysconfdir/%lname.conf
- enabled LADSPA
- updated %lname-svn-r22173-ext_ffmpeg.patch

* Mon Feb 05 2007 Led <led@altlinux.ru> 1.0-alt35.22138.1
- new SVN snapshot (revision 22138)
- fixed %lname.conf (#10770)

* Mon Feb 05 2007 Led <led@altlinux.ru> 1.0-alt35.22092.2
- added %lname-svn-r22092-dirac.patch

* Wed Jan 31 2007 Led <led@altlinux.ru> 1.0-alt35.22092.1
- new SVN snapshot (revision 22092)
- removed %lname-svn-r22020-makefile.patch
- updated %lname-svn-r22092-libdha.patch
- updated %lname-svn-r22092-configure.patch

* Fri Jan 26 2007 Led <led@altlinux.ru> 1.0-alt35.22020.1
- new SVN snapshot (revision 22020)
- fixed %%changelog
- updated %lname-svn-r22020-makefile.patch
- removed %lname-svn-r22004-doc_hu.patch (fixed in upstream)

* Wed Jan 24 2007 Led <led@altlinux.ru> 1.0-alt35.22004.1
- new SVN snapshot (revision 22004)
- added %lname-svn-r22004-doc_hu.patch

* Wed Jan 24 2007 Led <led@altlinux.ru> 1.0-alt35.21995.1
- new SVN snapshot (revision 21995):
  + Russian documentation translation finished
- updated %lname-svn-r21995-makefile.patch
- updated %lname-svn-r21995-libdha.patch
- updated %lname-svn-r21995-ext_ffmpeg.patch

* Wed Jan 10 2007 Led <led@altlinux.ru> 1.0-alt35.21839.1
- new SVN snapshot (revision 21839)
- updated %lname-svn-r21839-ext_ffmpeg.patch
- updated %lname-svn-r21858-configure.patch
- fixed buffer overflow in realrtsp (upstream)

* Fri Dec 29 2006 Led <led@altlinux.ru> 1.0-alt35.21781.1
- new SVN snapshot (revision 21781)

* Fri Dec 29 2006 Led <led@altlinux.ru> 1.0-alt35.21766.2
- fixed x86_64 build:
  + fixed %lname-svn-r21766-configure.patch

* Mon Dec 25 2006 Led <led@altlinux.ru> 1.0-alt35.21766.1
- new SVN snapshot (revision 21766):
  + mencoder now can write to output streams file:// and smb://
- updated %lname-svn-r21765-configure.patch
- fixed BuildRequires
- fixed docs installing
- removed %name-doc-it, replaced %name-doc-zh with %name-doc-zh_CN

* Thu Dec 14 2006 Led <led@altlinux.ru> 1.0-alt35.21614.1
- new SVN snapshot (revision 21614)
- updated %lname-svn-r21611-ext_ffmpeg.patch
- removed %lname-svn-r20777-bmovl-test.patch

* Sat Dec 02 2006 Led <led@altlinux.ru> 1.0-alt35.21402.3
- added %lname-svn-r21402-gui_nls.patch

* Thu Nov 30 2006 Led <led@altlinux.ru> 1.0-alt35.21402.2
- fixed %lname-uni-svn21402.diff
- fixed BuildRequires
- added %lname-svn-r21402-makefile.patch
- fixed spec

* Thu Nov 30 2006 Led <led@altlinux.ru> 1.0-alt35.21402.1
- new SVN snapshot (revision 21402)

* Thu Nov 30 2006 Led <led@altlinux.ru> 1.0-alt35.21399.1
- new SVN snapshot (revision 21399)
- fixed %%changelog
- updated %lname-svn-r21398-ext_ffmpeg.patch
- removed %lname-svn-r20837-generic-x86_64.patch (fixed in upstream)

* Wed Nov 29 2006 Led <led@altlinux.ru> 1.0-alt35.21374.1
- new SVN snapshot (revision 21374)
- forced --enable-mplayer
- fixed BuildRequires
- updated %lname-svn-r21374-ext_ffmpeg.patch

* Tue Nov 28 2006 Led <led@altlinux.ru> 1.0-alt35.21357.1
- new SVN snapshot (revision 21352)
- updated %lname-svn-r21352-libdha.patch
- updated %lname-uni-svn21352.diff
- removed %lname-svn-r21352-xmmslibs_fix.patch
- updated %lname-svn-r21352-ext_ffmpeg.patch
- updated %lname-svn-r21357-configure.patch
- removed %Name-svn-20060607-vf_mcdeint.patch

* Mon Nov 20 2006 Led <led@altlinux.ru> 1.0-alt35.21093.1
- new SVN snapshot (revision 21093):
  + obsolete XviD 3 support removed
  + video stream switching
- updated %lname-uni-svn21093.diff
- updated %lname-svn-r21093-ext_ffmpeg.patch
- updated %lname-svn-r21093-configure.patch

* Mon Nov 13 2006 Led <led@altlinux.ru> 1.0-alt35.20885.1
- new SVN snapshot (revision 20885)

* Fri Nov 10 2006 Led <led@altlinux.ru> 1.0-alt35.20837.1
- new SVN snapshot (revision 20837)
- updated %lname-svn-r20837-pulseaudio.patch
- changed %lname-svn-r20837-generic-x86_64.patch
- updated %lname-svn-r20837-ext_ffmpeg.patch

* Thu Nov 09 2006 Led <led@altlinux.ru> 1.0-alt35.20777.1
- new SVN snapshot (revision 20777)
- removed %lname-1.0rc1-mp3lib-amd.patch (fixed in upstream)
- removed %Name-svn-20060710-alt-external_fame.patch (removed libfame
  support in upstream)
- updated %lname-svn-r20777-generic-x86_64.patch
- updated %lname-svn-r20777-nls.patch
- updated %lname-uni-svn20777.diff
- updated %lname-svn-r20777-pulseaudio.patch
- updated %lname-svn-r20777-bmovl-test.patch
- updated %lname-svn-r20777-configure.patch
- fixed %lname-svn-r20777-builddocs.patch
- cleaned up spec

* Tue Nov 07 2006 Led <led@altlinux.ru> 1.0-alt35
- build docs with xsltproc instead of openjade
  + updated %lname-svn-r20544-builddocs.patch
  + fixed BuildRequires
- added %name-tools package
- fixed %lname-1.0rc1-ext_ffmpeg.patch

* Tue Oct 31 2006 Led <led@altlinux.ru> 1.0-alt34
- fixed spec
- updated %lname-1.0rc1-ext_ffmpeg.patch
- added --enable-libswscale[_so] configure options
- added %lname-mwallp.patch
- added %lname-bmovl-test.patch
- fixed mp_msg2po.awk
- updated %lname-1.0rc1-configure.patch (fixed #4108)
- added %lname-1.0rc1-mp3lib-amd.patch (disabled broken asm-code)

* Mon Oct 30 2006 Led <led@altlinux.ru> 1.0-alt34.20523.1
- new SVN snapshot (revision 20523)
- fixed spec
- updated %lname-svn-r20448-ext_ffmpeg.patch
- added --enable-libswscale[_so] configure options
- added %lname-mwallp.patch
- added %lname-bmovl-test.patch
- fixed mp_msg2po.awk
- updated %lname-1.0rc1-configure.patch (fixed #4108)

* Mon Oct 23 2006 Led <led@altlinux.ru> 1.0-alt33
- 1.0rc1
- removed %Name-1.0pre8-udev.patch (fixed in upstream)
- cleaned up and fixed spec
- updated %lname-1.0rc1-configure.patch

* Thu Oct 19 2006 Led <led@altlinux.ru> 1.0-alt32.20300.1
- new SVN snapshot (revision 20300):
  + Russian documentation translation synced and almost finished
  + bicubic OpenGL scaling works with ATI cards
  + md5sum switched to use libavutil md5 implementation
  + support for libcaca 1.0 via compatibility layer
  + audio stream switching between streams with different codecs
  + fixed seeking to absolute and percent position for libavformat
    demuxer
  + NUT demuxer using libnut
  + Matroska SimpleBlock support
  + -correct-pts option
  + UTF-8 used for OSD and subtitles, some bitmap fonts will no longer
    work correctly and -subcp must be set for all non-UTF-8 subtitles
  + more audio-truncation fixes
  + libavutil mandatory for MPlayer compilation
  + more intuitive -edlout behaviour
  + -nortc is now default since -rtc has only disadvantages with recent
    kernels
  + MMX-optimizations for -vf yadif
  + MMX-optimizations for -vf zrmjpeg
  + GUI:
    drag-and-drop ignored last file
    save and load cache setting correctly
    working audio stream selection for Ogg and Matroska files
    xinerama fixes
- cleaned up spec
- fixed Provides for %lname-gui package
- enabled nut
- updated %lname-svn-r20300-configure.patch

* Fri Oct 13 2006 Led <led@altlinux.ru> 1.0-alt31.20190.1
- new SVN snapshot (revision 20190):
  + -endpos option for %lname

* Mon Oct 09 2006 Led <led@altlinux.ru> 1.0-alt31.20117.1
- new SVN snapshot (revision 20117)
- updated %lname-svn-r20117-ext_ffmpeg.patch
- returned %name's mans
- removed %lname-svn-r19982-doc-cs.patch (fixed in upstream)
- fixed %lname.conf (used default utf8 subtitles encoding)
- fixed spec

* Wed Oct 04 2006 Led <led@altlinux.ru> 1.0-alt30.20022.1
- new SVN snapshot (revision 20022)
- fixed console control:
  + updated %lname-svn-r20022-configure.patch
  + enabled termios

* Mon Oct 02 2006 Led <led@altlinux.ru> 1.0-alt29.20016.1
- new SVN snapshot (revision 20016)
- fixed Conflicts in mencoder package
- added %lname-svn-r19982-doc-cs.patch

* Mon Sep 25 2006 Led <led@altlinux.ru> 1.0-alt28.19912.1
- rebuild for Sisyphus

* Wed Sep 20 2006 Led <led@altlinux.ru> 1:1.0-alt1.19912.1
- new SVN snapshot (revision 19912)
- merged %lname-svn-r19389-ext_libswscale.patch to
  %lname-svn-r19912-ext_ffmpeg.patch
- cleaned up spec

* Fri Sep 15 2006 Led <led@altlinux.ru> 1:1.0-alt1.19838.1
- new SVN snapshot (revision 19838)
- fixed %%files section

* Thu Sep 14 2006 Led <led@altlinux.ru> 1:1.0-alt1.19833.1
- new SVN snapshot (revision 19833)

* Mon Sep 11 2006 Led <led@altlinux.ru> 1:1.0-alt1.19794.1
- new SVN snapshot (revision 19794)
- cleaned up spec

* Fri Sep 08 2006 Led <led@altlinux.ru> 1:1.0-alt1.19734.1
- new SVN snapshot (revision 19734)

* Fri Sep 08 2006 Led <led@altlinux.ru> 1:1.0-alt1.19700.2
- fixed BuildRequires
- fixed install mans

* Thu Sep 07 2006 Led <led@altlinux.ru> 1:1.0-alt1.19700.1
- new SVN snapshot (revision 19700)

* Tue Sep 05 2006 Led <led@altlinux.ru> 1:1.0-alt1.19671.2
- added %lname-svn-r19671-pulseaudio.patch (based on
  mplayer-pulse.patch from http://pulseaudio.org
- enabled pulse
- disabled polyp (obsoleted with pulse)

* Tue Sep 05 2006 Led <led@altlinux.ru> 1:1.0-alt1.19671.1
- new SVN snapshot (revision 19671)
- added NLS support: mp_help2msg.awk, mp_msg2po.awk,
  %lname-svn-r19595-nls.patch
- added %name-i18n package
- fixed spec

* Wed Aug 30 2006 Led <led@altlinux.ru> 1:1.0-alt1.19595.1
- new SVN snapshot (revision 19595):
  + Radio support (radio://)
- enabled radio

* Wed Aug 30 2006 Led <led@altlinux.ru> 1:1.0-alt1.19558.3
- rebuild with external vidix from MPlayer's SVN

* Tue Aug 29 2006 Led <led@altlinux.ru> 1:1.0-alt1.19558.2
- added %lname-svn-r19558-generic-x86_64.patch (thanks LAKostis)
- disabled win32 for x86_64
- enabled internal vidix
- fixed %%prep section
- forced internal vidix (if enabled) for non-ix86 arches

* Mon Aug 28 2006 Led <led@altlinux.ru> 1:1.0-alt1.19558.1
- new SVN snapshot (revision 19558)
- fixed configure parameters
- fixed spec
- removed %Name-1.0pre7try2-libdir_fix.patch
- updated %lname-uni-svn19558.diff
- cleaned up and fixed spec
- enabled samba

* Mon Aug 21 2006 Led <led@altlinux.ru> 1:1.0-alt1.19467.1
- new SVN snapshot (revision 19467)
  + support for chapters seeking in dvdnav:// stream
- updated %lname-svn-r19467-configure.patch
- fixed %lname.conf
- fixed %%changelog

* Sat Aug 19 2006 Led <led@altlinux.ru> 1:1.0-alt1.19447.2
- enabled: dvdnav, joystick, tga, xmms
- fixed Provides
- added %lname-svn-r19447-vo_vidix.patch

* Sat Aug 19 2006 Led <led@altlinux.ru> 1:1.0-alt1.19447.1
- new SVN snapshot (revision 19447)
  + support for chapters seeking in dvd:// stream
- fixed build with external vidix
- cleaned up spec
- removed:
  + %Name-svn-20060707-ext_vidix_drivers-0.9.9.1.patch,
  + vidix-0.9.9.1-pm3_vid.patch,
  + %Name-svn-20060630-vidix_ext_drivers.patch,
  + %Name-svn-20060630-vidix_0.9.9.1.patch
- updated %lname-svn-r19447-configure.patch
- added lname-svn-r19427-libdha.patch

* Thu Aug 17 2006 Led <led@altlinux.ru> 1:1.0-alt1.19416.1
- new SVN snapshot (revision 19416)
- fixed and updated %lname-svn-r19416-configure.patch
- fixed %%changelog
- cleaned up spec
- fixed BuildRequires

* Thu Aug 17 2006 Led <led@altlinux.ru> 1:1.0-alt1.19389.1
- new SVN snapshot (revision 19389)
- fixed spec
- fixed configure parameters (renaming and removed in upstream)
- new release numbering (therewith SVN revision)
- enabled external libswscale (libffmpeg)
- added %Name-1.0pre8-udev.patch
- fixed directfb ability
- added %lname-svn-r19389-ext_ffmpeg.patch

* Thu Jul 20 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060720.1
- new SVN snapshot (revision 19134)
- fixed lapses in %%changelog and %%description
- without soundwrapper
- making correct version.h
- removed %name-fonts
- added %name-fontutils

* Mon Jul 17 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060717.1
- new SVN snapshot (revision 19126)
- removed divx4linux and opendivx (upstream)

* Mon Jul 17 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060714.1
- new SVN snapshot (revision 19058)
- cleaned up spec
- changed base package name to %lname

* Thu Jul 13 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060713.1
- new SVN snapshot (revision 19047)
- cleaned up spec
- changed %%name to %lname

* Thu Jul 13 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060712.1
- new SVN snapshot (revision 19018)
- enabled fribidi
- fixed configure parameters

* Wed Jul 12 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060711.1
- new SVN snapshot (revision 19001)
- updated %Name-svn-20060711-configure.patch
- many changes in spec
- enabled libmpeg2, md5sum, 3dfx, tdfxfb
- disabled vesa

* Mon Jul 10 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060710.2
- added %lname-uni-20060710.diff

* Mon Jul 10 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060710.1
- new SVN snapshot (revision 18986)
- updated %Name-svn-20060710-alt-external_fame.patch
- enabled ass (internal SSA/ASS subtitles support)
- fixed spec

* Mon Jul 10 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060707.3
- replaced vidix-0.9.9.1.tar.bz2 with
  %Name-svn-20060707-ext_vidix_drivers-0.9.9.1.patch

* Sat Jul 08 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060707.2
- disabled dirac

* Fri Jul 07 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060707.1
- new SVN snapshot (revision 18929)
- fixed spec
- updated %Name-svn-20060707_dirac-0.5.x.patch

* Thu Jul 06 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060630.5
- enabled internal VIDIX
- disabled external VIDIX
- added vidix-0.9.9.1 with vidix-0.9.9.1-pm3_vid.patch
- added %Name-svn-20060630-vidix_0.9.9.1.patch
- added %Name-svn-20060630-vidix_ext_drivers.patch

* Thu Jul 06 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060630.4
- disabled internal VIDIX
- enabled external VIDIX

* Fri Jun 30 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060630.3
- don't include ffmpeg tarball if shared_ffmpeg enabled (default)
- updated %Name-dvd-ru patch
- cleaned up bogus patches
- fixed spec
- fixed libvo/vo_md5sum.c
- trying dvdmenu (disabled by deafult)
- some fixes from LAKostis (vidix prefixes, bogus BuildRequires)
- added %Name-svn-20060704_dirac-0.5.x.patch
- enabled dirac

* Fri Jun 30 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060630.1
- new SVN snapshot (revision 18853)
- enabled dvdnav
- fixed dvdnav detect

* Thu Jun 29 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060629.1
- new SVN snapshot (revision 18847)

* Mon Jun 26 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060626.1
- new SVN snapshot (revision 18821)
- removed %Name-cvs-20060506-docs.patch, used sed & iconv instead

* Fri Jun 23 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060623.1
- new SVN snapshot (revision 18791)

* Thu Jun 22 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060622.1
- new SVN snapshot (revision 18781)
- returned %name.sh (soundwrapper)
- cleaned up spec

* Wed Jun 21 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060621.1
- new SVN snapshot (revision 18766)
- added macroses
- enabled external tremor
- force enabled openal
- %Name-cvs-20060220-configure.patch merged with
  %Name-1.0pre7-aalib.patch and some additions to
  %Name-svn-20060621-configure.patch

* Tue Jun 20 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060620.1
- new SVN snapshot (revision 18760)
- fixed spec
- updated %Name-svn-20060620-alt-external_fame.patch
- fixed configure parameters
- cleaned up spec

* Tue Jun 13 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060613.1
- new SVN snapshot (revision 18698)
- removed additional icons
- fixed .desktop file
- removed %name.sh (soundwrapper)
- cleaned up spec

* Wed Jun 07 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060607.1
- 20060607 SVN snapshot
- fixed spec

* Fri Jun 02 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060519.4
- fixed fbdev support

* Wed May 31 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060519.3
- added menu file
- cleaned up spec

* Tue May 30 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060519.2
- cleaned up spec
- enabled polyp (thanx icesik and polypaudio's author)
- added %Name-cvs-20060519-polyp0.8.patch

* Thu May 25 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060519.1
- 20060519 CVS snapshot
- removed %lname-rpm-cvs.patch

* Thu May 25 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060515.5
- rebuild for libffmpeg

* Wed May 24 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060515.4
- disabled xmms
- enabled gtk+2.0 GUI
- added default (standard) skin to %name-gui package
- cleaned up spec

* Tue May 23 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060515.3
- enabled shared FFmpeg libs

* Mon May 15 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060515.2
- enabled live.com support

* Mon May 15 2006 Led <led@altlinux.ru> 1:1.0-alt0.20060515.1
- 20060515 CVS snapshot
- cleanup %name-cvs-20060506-docs.patch

* Wed May 03 2006 Led <led@altlinux.ru> 1.0-alt0.20060503.1
- 20060503 CVS snapshot
- fixed %%changelog
- fixed configure parameters in spec
- added %name-cvs-20060503-docs.patch
- enabled pl docs

* Wed Apr 26 2006 Led <led@altlinux.ru> 1.0-alt0.20060426.1
- 20060426 CVS snapshot
- disabled polyp because changes in it's API
- replaced mmx2 with mmxext and 3dnowex with 3dnowext in configure parameters
- fixed spec

* Thu Apr 20 2006 Led <led@altlinux.ru> 1.0-alt0.20060420.1
- 20060420 CVS snapshot
- fixed %%changelog
- added fr docs and de HTML docs
- splited docs to languages

* Wed Apr 19 2006 Led <led@altlinux.ru> 1.0-alt0.20060417.2
- enabled libdts

* Mon Apr 17 2006 Led <led@altlinux.ru> 1.0-alt0.20060417.1
- 20060417 CVS snapshot
- fixed spec

* Tue Apr 04 2006 Led <led@altlinux.ru> 1.0-alt0.20060331.2
- enabled musepack

* Fri Mar 31 2006 Led <led@altlinux.ru> 1.0-alt0.20060331.1
- CVS snapshot
- upgraded spec
- added configure and builddocs patches
- enabled svgalib, aalib, caca, png, speex, enca, polyp
- enabled x264 for mencoder

* Thu Jan 26 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.0-alt23.pre7try2
- Packaged skins separately.

* Fri Jan 13 2006 LAKostis <lakostis at altlinux.ru> 1.0-alt22.1.pre7try2
- NMU;
- x86_64 fixes;
- fix jackd builddep;
- fix unparseable macros;
- remove old menu files;
- remove kernel-headers-dvb deps, move to linux-libc-headers.

* Sat Nov 26 2005 Grigory Milev <week@altlinux.ru> 1.0-alt22.pre7try2
- update to bugfix version

* Tue Aug 30 2005 Eugene Ostapets <eostapets@altlinux.ru> 1.0-alt21.pre7
- fix CAN-2005-2718

* Thu Apr 21 2005 Grigory Milev <week@altlinux.ru> 1.0-alt20.pre7
- fixed build requires

* Mon Apr 18 2005 Grigory Milev <week@altlinux.ru> 1.0-alt19.pre7
- new version released
- build with v4l
- due compilation errors, temporary build with out aa lib

* Fri Apr 08 2005 Grigory Milev <week@altlinux.ru> 1.0-alt18.pre6a
- add theora support
- add jack support

* Fri Jan 28 2005 Grigory Milev <week@altlinux.ru> 1.0-alt17.pre6a
- new version released

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0-alt16.pre5.1
- Rebuilt with libstdc++.so.6.

* Fri Dec 17 2004 Grigory Milev <week@altlinux.ru> 1.0-alt16.pre5
- rebuild with new directfb

* Fri Dec 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.0-alt15.pre5.1
- Rebuilt with libdirectfb-0.9.so.21.

* Mon Nov 22 2004 Grigory Milev <week@altlinux.ru> 1.0-alt15.pre5
- temporary disable smb client support, due build troubles

* Tue Aug 17 2004 Grigory Milev <week@altlinux.ru> 1.0-alt14.pre5
- rebuild from A.Morozov spec

* Tue Aug 17 2004 Alexey Morozov <morozov@altlinux.org> 1.0-alt13.1.pre5
- release bump to shut up apt :-)

* Sun Aug  8 2004 Alexey Morozov <morozov@altlinux.org> 1.0-alt11.pre5
- new version (1.0pre5)
- some patches were adapted to the new version
- fbdev support is enabled by default

* Mon May 17 2004 Alexey Morozov <morozov@altlinux.org> 1.0-alt11.pre4
- Re-enabled samba support
- Dropped non-gui version because gui doesn't give us additional dependencies

* Tue May  4 2004 Alexey Morozov <morozov@altlinux.org> 1.0-alt10.pre4
- Incorporated patches and ideas for official RPMs of MPlayer
  Re-worked build scheme. Most options are configurable now.
- Handle most video formats from within MPlayer menu file
- Dropped MPlayer's own fonts in the default build (obsolete by
  fontconfig support)
- Preliminary spec-file translation
- smb, dvb and dxr3 support is temporarily disabled due to problems
  with corresponding packages. Brave souls can try to --enable them

* Mon Apr 12 2004 Grigory Milev <week@altlinux.ru> 1.0-alt8.pre3try2
- added dvb support
- rebuild with new libxvidcore

* Wed Mar 31 2004 Grigory Milev <week@altlinux.ru> 1.0-alt7.pre3try2
- remotely exploitable buffer overflow in the HTTP streaming code fixed

* Thu Mar 25 2004 Grigory Milev <week@altlinux.ru> 1.0-alt6.pre3
- rebuild with glib2

* Fri Jan 23 2004 Grigory Milev <week@altlinux.ru> 1.0-alt5.pre3
- added patch for multiplier dvd soudn tracs (thanx Kachalov Anton)

* Mon Jan 19 2004 Grigory Milev <week@altlinux.ru> 1.0-alt4.pre3
- next pre-release

* Tue Oct  7 2003 Grigory Milev <week@altlinux.ru> 1.0-alt3.pre2
- new version released

* Fri Sep 26 2003 Grigory Milev <week@altlinux.ru> 1.0-alt2.pre1.cvs20030926
- build cvs version with fixed "Exploitable remote buffer overflow vulnerability"
- move w32codec to separated package

* Fri Sep  5 2003 Grigory Milev <week@altlinux.ru> 1.0-alt1.pre1
- new version released

* Wed Aug 27 2003 Grigory Milev <week@altlinux.ru> 0.91-alt21
- rebuild with new xvid

* Fri Aug 22 2003 Grigory Milev <week@altlinux.ru> 0.91-alt20
- new version released
- updated default skin

* Tue Jul 29 2003 Grigory Milev <week@altlinux.ru> 0.90-alt20
- rebuild with nas support

* Wed Jun 11 2003 Grigory Milev <week@altlinux.ru> 0.90-alt19
- Rebuild with Lirc enabled

* Mon May 19 2003 Grigory Milev <week@altlinux.ru> 0.90-alt18
- fixed bug with mplayer bash alias, now don't close bash
  after mplayer exit
- can't build with libdvdnav (temporary removed)

* Thu Apr 24 2003 Grigory Milev <week@altlinux.ru> 0.90-alt17
- rebuild with new directfb
- rebuild with libdvdnav and libdvdread

* Mon Apr 14 2003 Grigory Milev <week@altlinux.ru> 0.90-alt16
- working with soundwrapper

* Wed Apr  9 2003 Grigory Milev <week@altlinux.ru> 0.90-alt15
- stable version released

* Wed Mar 19 2003 Grigory Milev <week@altlinux.ru> 0.90-alt14.rc5
- new version released

* Wed Feb 12 2003 Grigory Milev <week@altlinux.ru> 0.90-alt13.rc4
- new version released

* Thu Jan 30 2003 Grigory Milev <week@altlinux.ru> 0.90-alt12.rc3
- recompile with esound support

* Mon Jan 20 2003 Grigory Milev <week@altlinux.ru> 0.90-alt11.rc3
- new version released
- build with English menus, for compatible with non KOI8-R locales
- add --enable-runtime-cpudetection

* Wed Dec 11 2002 Grigory Milev <week@altlinux.ru> 0.90-alt10.rc1
- new version released

* Tue Dec  3 2002 Grigory Milev <week@altlinux.ru> 0.90-alt9.pre10
- rebuild with tinfo

* Fri Nov 15 2002 Grigory Milev <week@altlinux.ru> 0.90-alt8.pre10
- new version released

* Mon Nov  4 2002 Grigory Milev <week@altlinux.ru> 0.90-alt8.pre9
- new version released
- fixed vidix paths

* Wed Sep 25 2002 Grigory Milev <week@altlinux.ru> 0.90-alt8.pre8
- move w32codec, fons and gui to separated packages
- move skins to MPlayer-skins package, move default skin to MPlayer-gui

* Thu Sep 19 2002 Grigory Milev <week@altlinux.ru> 0.90-alt7.pre8
- fixed gui.conf reading
- new version released

* Wed Sep 18 2002 Stanislav Ievlev <inger@altlinux.ru> 0.90-alt6.pre7
- rebuild with new XFree86
- update buildreqs

* Fri Sep  6 2002 Grigory Milev <week@altlinux.ru> 0.90-alt5.pre7
- fix typo
- remove perl and ee from buildrequires

* Fri Sep  6 2002 Grigory Milev <week@altlinux.ru> 0.90-alt4.pre7
- new prerelease version released

* Wed Aug  7 2002 Grigory Milev <week@altlinux.ru> 0.90-alt3.pre6
- new version released

* Mon Jun 10 2002 Grigory Milev <week@altlinux.ru> 0.90pre5-alt2
- added build requires for libSDL
- (inger) hotfixes

* Mon Jun 10 2002 Grigory Milev <week@altlinux.ru> 0.90pre5-alt1
- new version released

* Fri May 17 2002 Grigory Milev <week@altlinux.ru> 0.90pre4-alt1
- new version released
- added options to spec: COMPAT_GCC, WITH_LIRC, WITH_DXR

* Tue May  7 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.90pre3-alt2.1
- tweaks

* Mon May  6 2002 Grigory Milev <week@altlinux.ru> 0.90pre3-alt0.1
- new version released

* Tue Apr 30 2002 Grigory Milev <week@altlinux.ru> 0.90pre2-alt1
- new version released

* Wed Apr 24 2002 Grigory Milev <week@altlinux.ru> 0.90pre1-alt1
- new version released

* Fri Apr 12 2002 Grigory Milev <week@altlinux.ru> 0.60-alt6.cvs20020412
- new cvs snapshot
- change fonts

* Tue Mar 26 2002 Grigory Milev <week@altlinux.ru> 0.60-alt5.cvs20020306
- added buildrequires, for compiling GUI
- added Menu

* Wed Mar 13 2002 Grigory Milev <week@altlinux.ru> 0.60-alt4.cvs20020306
- fix descriptions and summary

* Wed Mar  6 2002 Grigory Milev <week@altlinux.ru> 0.60-alt3.cvs20020306
- new cvs snapshot 2002/03/06
- added dxr3 patch, dxr3 now compiled and work
- added compiled with gui and fbdev
- include two skin for gui
- minor spec cleanup

* Sat Jan  5 2002 Grigory Milev <week@altlinux.ru> 0.60-alt2
- corrected build requires
- fixed error in font.desk from koi8-r-font for subtitles

* Thu Jan  3 2002 Grigory Milev <week@altlinux.ru> 0.60-alt1
- new version released

* Wed Dec 26 2001 Grigory Milev <week@altlinux.ru>  0.60pre1-alt1
- Initial build for ALT Linux distribution.
