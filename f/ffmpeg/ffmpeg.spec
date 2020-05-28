# defined macro based on Sergey Bolshakov <sbolshakov@altlinux.org> libav spec

# Macros
%define set_disable() %{expand:%%force_disable %{1}} %{expand:%%undefine _enable_%{1}}
%define set_enable() %{expand:%%force_enable %{1}} %{expand:%%undefine _disable_%{1}}
%define subst_enable_with() %{expand:%%{?_enable_%{1}:--enable-%{2}} } %{expand:%%{?_disable_%{1}:--disable-%{2}} }


# Enable/Disable stuff
%def_enable doc
%def_disable nonfree
%def_enable gpl
%def_enable version3
%def_enable ffplay
%def_enable ffprobe
%def_enable gpl
%def_enable pthreads
%def_enable shared
%def_disable static
%ifarch %ix86 x86_64
%def_enable mmx
%else
%def_disable mmx
%endif
%def_enable debug
# External library support
%def_disable avisynth
%def_enable bzlib
%def_disable frei0r
%def_enable gnutls
%def_enable libaom
%def_enable libass
%def_enable libbluray
%def_enable libbs2b
%def_enable libcaca
%def_enable libcdio
# need libcelt >= 0.11.0
%def_disable libcelt
%def_enable libcodec2
%def_enable libdav1d
%def_enable libdc1394
%def_enable libdrm
%def_enable libflite
%def_enable libfontconfig
%def_enable libfreetype
%def_enable libfribidi
%def_enable libgme
%def_enable libgsm
%def_enable libjack
%def_enable libmp3lame

%{?_enable_version3:%def_enable libopencore_amrnb}
%{?_enable_version3:%def_enable libopencore_amrwb}
%def_enable libopenjpeg
%def_enable libopus
%def_enable libpulse
%def_enable librsvg
%def_enable librubberband
%def_disable librtmp
%def_enable libsnappy
%def_enable libsoxr
%def_enable libssh
%def_enable libspeex
%def_enable libtheora
%def_enable libtwolame
%def_enable libv4l2
%def_enable libvidstab
%def_enable libvorbis
%def_enable libvpx
%def_enable libwavpack
%def_enable libwebp
%def_enable libx264
%def_enable libx265
%def_enable libxvid
%def_enable libzmq
%def_enable libzvbi
%def_enable lv2
%def_enable openal
%def_enable opengl
%def_enable vaapi
%def_enable vdpau
%def_enable zlib

%if_enabled mmx
%set_verify_elf_method textrel=relaxed
%endif

%ifarch %arm
%set_verify_elf_method textrel=relaxed
%endif
#soversion

%define avdevicever 58
%define avformatver 58
%define avfilterver 7
%define avcodecver 58
%define postprocver 55
%define swresamplever 3
%define avresamplever 4
%define swscalever 5
%define avutilver 56

Name:		ffmpeg
Epoch:		2
Version:	4.2.3
Release:	alt1

Summary:	A command line toolbox to manipulate, convert and stream multimedia content
License:	GPLv3
Group:		Video

Url:		http://ffmpeg.org

# https://git.ffmpeg.org/ffmpeg.git
Source:		%name-%version.tar
Patch:		%name-%version-%release.patch
BuildRequires:	libX11-devel libXext-devel libXvMC-devel libXfixes-devel
BuildRequires:	libalsa-devel
%ifarch %ix86 x86_64
BuildRequires:	yasm
%endif

%{?_enable_doc:BuildRequires: perl-podlators texi2html}
%{?_enable_ffplay:BuildRequires: libSDL2-devel}
%{?_enable_bzlib:BuildRequires: bzlib-devel}
%{?_enable_frei0r:BuildRequires: frei0r-devel}
%{?_enable_gnutls:BuildRequires: libgnutls-devel}
%{?_enable_libaom:BuildRequires: libaom-devel >= 1.0.0}
%{?_enable_libass:BuildRequires: libass-devel}
%{?_enable_libbluray:BuildRequires: libbluray-devel}
%{?_enable_libbs2b:BuildRequires: libbs2b-devel}
%{?_enable_libcaca:BuildRequires: libcaca-devel}
%{?_enable_libcdio:BuildRequires: libcdio-devel libcdio-paranoia-devel}
%{?_enable_libcelt:BuildRequires: libcelt-devel}
%{?_enable_libcodec2:BuildRequires: libcodec2-devel}
%{?_enable_libdav1d:BuildRequires: libdav1d-devel}
%{?_enable_libdc1394:BuildRequires: libdc1394-devel libraw1394-devel}
%{?_enable_libdrm:BuildRequires: libdrm-devel}
%{?_enable_libfreetype:BuildRequires: libfreetype-devel}
%{?_enable_libflite:BuildRequires: flite-devel}
%{?_enable_libfontconfig:BuildRequires: fontconfig-devel}
%{?_enable_libfribidi:BuildRequires: libfribidi-devel}
%{?_enable_libgme:BuildRequires: libgme-devel}
%{?_enable_libgsm:BuildRequires: libgsm-devel}
%{?_enable_libjack:BuildRequires: libjack-devel}
%{?_enable_libmp3lame:BuildRequires: liblame-devel}
%{?_enable_libopencore_amrnb:BuildRequires: libopencore-amrnb-devel}
%{?_enable_libopencore_amrwb:BuildRequires: libopencore-amrwb-devel}
%{?_enable_libopenjpeg:BuildRequires: libopenjpeg2.0-devel}
%{?_enable_libopus:BuildRequires: libopus-devel}
%{?_enable_libpulse:BuildRequires: libpulseaudio-devel}
%{?_enable_librsvg:BuildRequires: librsvg-devel}
%{?_enable_librubberband:BuildRequires: librubberband-devel libstdc++-devel}
%{?_enable_librtmp:BuildRequires: librtmp-devel}
%{?_enable_libsnappy:BuildRequires: libsnappy-devel}
%{?_enable_libsoxr:BuildRequires: libsoxr-devel}
%{?_enable_libssh:BuildRequires: libssh-devel}
%{?_enable_libspeex:BuildRequires: libspeex-devel}
%{?_enable_libtheora:BuildRequires: libtheora-devel}
%{?_enable_libtwolame:BuildRequires: libtwolame-devel}
%{?_enable_libv4l2:BuildRequires: libv4l-devel}
%{?_enable_libvidstab:BuildRequires: libvidstab-devel}
%{?_enable_libvorbis:BuildRequires: libvorbis-devel}
%{?_enable_libvpx:BuildRequires: libvpx-devel}
%{?_enable_libwavpack:BuildRequires: libwavpack-devel}
%{?_enable_libwebp:BuildRequires: libwebp-devel}
%{?_enable_libx264:BuildRequires: libx264-devel >= 118}
%{?_enable_libx265:BuildRequires: libx265-devel}
%{?_enable_libxvid:BuildRequires: libxvid-devel}
%{?_enable_libzmq:BuildRequires: libzeromq-devel}
%{?_enable_libzvbi:BuildRequires: libzvbi-devel}
%{?_enable_lv2:BuildRequires: liblilv-devel lv2-devel}
%{?_enable_openal:BuildRequires: libopenal-devel}
%{?_enable_opengl:BuildRequires: libGL-devel}
%{?_enable_vaapi:BuildRequires: libva-devel}
%{?_enable_vdpau:BuildRequires: libvdpau-devel}

%define common_descr \
FFmpeg is a collection of libraries and tools to process multimedia content\
such as audio, video, subtitles and related metadata.

%description
%common_descr

The ffmpeg is a command line toolbox to manipulate, convert and stream
multimedia content.


%package	doc
Summary:	FFmpeg documentation
Group:		Documentation
BuildArch:	noarch

%description	doc
%common_descr

This package contains documentation for FFmpeg.

%package -n	ffplay
Summary:	A minimalistic multimedia player
Group:		Video
Obsoletes:	avplay
Provides:	avplay

%description -n	ffplay
%common_descr

This package contains a minimalistic multimedia player.

%package -n	ffplay-doc
Summary:	Documentation for ffplay
Group:		Documentation
BuildArch:	noarch

%description -n	ffplay-doc
%common_descr

This package contains documentation for ffplay.

%package -n	ffprobe
Summary:	A simple analysis tool to inspect multimedia content
Group:		Video
Obsoletes:	avprobe
Provides:	avprobe

%description -n	ffprobe
%common_descr

This package contains ffprobe, a simple analysis tool to inspect
multimedia content.

%package -n	ffprobe-doc
Summary:	Documentation for ffprobe
Group:		Documentation
BuildArch:	noarch

%description -n	ffprobe-doc
%common_descr

This package contains documentation for ffprobe.

%package -n	ffserver
Summary:	A multimedia streaming server for live broadcasts
Group:		Video

%description -n ffserver
%common_descr

This package contains a multimedia streaming server for live broadcasts.


%package -n	ffserver-doc
Summary:	Documentation for ffserver
Group:		Documentation
BuildArch:	noarch

%description -n ffserver-doc
%common_descr

This package contains documentation for ffserver.


%package -n	libavcodec%avcodecver
Summary:	provides implementation of a wider range of codecs
Group:		System/Libraries

%description -n libavcodec%avcodecver
%common_descr

The libavcodec library provides implementation of a wider range of
codecs.

%package -n libavcodec-devel
Summary: Development files for libavcodec
Group: Development/C
Requires: libavcodec%avcodecver = %EVR
Requires: libavutil-devel = %EVR

%description -n libavcodec-devel
This package contains development files for libavcodec.

%package -n libavcodec-devel-static
Summary: Static development files for libavcodec
Group: Development/C
Requires: libavcodec-devel = %EVR


%description -n libavcodec-devel-static
This package contains static development files for libavcodec.


%package -n	libavdevice%avdevicever
Summary:	FFmpeg device handling library
Group:		System/Libraries

%description -n libavdevice%avdevicever
%common_descr

The libavdevice library provides a generic framework for grabbing from
and rendering to many common multimedia input/output devices, and
supports several input and output devices, including Video4Linux2, VfW,
DShow, and ALSA.

%package -n libavdevice-devel
Summary: Development files for libavdevice
Group: Development/C
Requires: libavdevice%avdevicever = %EVR

%description -n libavdevice-devel
This package contains development files for libavdevice.

%package -n libavdevice-devel-static
Summary: Static development files for libavdevice
Group: Development/C
Requires: libavdevice-devel = %EVR

%description -n libavdevice-devel-static
This package contains static development files for libavdevice.

%package -n	libavfilter%avfilterver
Summary:	FFmpeg filter layer library
Group:		System/Libraries

%description -n libavfilter%avfilterver
%common_descr

The libavfilter library provides a mean to alter decoded Audio and Video
through chain of filters.

%package -n libavfilter-devel
Summary: Development files for libavfilter
Group: Development/C
Requires: libavfilter%avfilterver = %EVR

%description -n libavfilter-devel
This package contains development files for libavfilter.

%package -n libavfilter-devel-static
Summary: Static development files for libavfilter
Group: Development/C
Requires: libavfilter-devel = %EVR

%description -n libavfilter-devel-static
This package contains static development files for libavfilter.

%package -n	libavformat%avformatver
Summary:	FFmpeg audio, video and subtitle streams (de)multiplexing library
Group:		System/Libraries

%description -n libavformat%avformatver
%common_descr

The libavformat library implements streaming protocols, container
formats and basic I/O access.

%package -n libavformat-devel
Summary: Development files for libavcodec
Group: Development/C
Requires: libavformat%avformatver = %EVR
Requires: libavcodec-devel = %EVR

%description -n libavformat-devel
This package contains development files for libavformat.


%package -n libavformat-devel-static
Summary: Static development files for libavformat
Group: Development/C
Requires: libavformat-devel = %EVR

%description -n libavformat-devel-static
This package contains static development files for libavformat.

%package -n	libavutil%avutilver
Summary:	Utility library to aid portable multimedia programming
Group:		System/Libraries

%description -n libavutil%avutilver
%common_descr

The libavutil library includes hashers, decompressors and miscellaneous
utility functions.

%package -n libavutil-devel
Summary: Development files for libavutil
Group: Development/C
Requires: libavutil%avutilver = %EVR

%description -n libavutil-devel
This package contains development files for libavutil.

%package -n libavutil-devel-static
Summary: Static development files for libavutil
Group: Development/C
Requires: libavutil-devel = %EVR

%description -n libavutil-devel-static
This package contains static development files for libavutil.

%package -n	libpostproc%postprocver
Summary:	FFmpeg postprocessing library
Group:		System/Libraries

%description -n libpostproc%postprocver
%common_descr

The libpostproc library implements video postprocessing routines.

%package -n libpostproc-devel
Summary: Development files for libpostproc
Group: Development/C
Requires: libpostproc%postprocver = %EVR
Requires: libavutil-devel = %EVR

%description -n libpostproc-devel
This package contains development files for libpostproc.

%package -n libpostproc-devel-static
Summary: Static development files for libpostproc
Group: Development/C
Requires: libpostproc-devel = %EVR

%description -n libpostproc-devel-static
This package contains static development files for libpostproc.

%package -n	libswresample%swresamplever
Summary:	FFmpeg audio resampling, rematrixing and sample format conversion library
Group:		System/Libraries

%description -n libswresample%swresamplever
%common_descr

The libswresample library implements audio mixing and resampling
routines.

%package -n libswresample-devel
Summary: Development files for libswresample
Group: Development/C
Requires: libswresample%swresamplever = %EVR
Requires: libavutil-devel = %EVR

%description -n libswresample-devel
This package contains development files for libswresample.

%package -n libswresample-devel-static
Summary: Static development files for libswresample
Group: Development/C
Requires: libswresample-devel = %EVR

%description -n libswresample-devel-static
This package contains static development files for libswresample.

%package -n	libavresample%avresamplever
Summary:	FFmpeg video postprocessing library
Group:		System/Libraries

%description -n libavresample%avresamplever
%common_descr
This package contains libavresample, the ffmpeg project video postprocessing library.

%package -n libavresample-devel
Summary: Development files for libswresample
Group: Development/C
Requires: libavresample%avresamplever = %EVR
Requires: libavutil-devel = %EVR

%description -n libavresample-devel
This package contains development files for libavresample.

%package -n libavresample-devel-static
Summary: Static development files for libavresample
Group: Development/C
Requires: libavresample-devel = %EVR

%description -n libavresample-devel-static
This package contains static development files for libavresample.



%package -n	libswscale%swscalever
Summary:	FFmpeg image scaling and colorspace and pixel format conversion library
Group:		System/Libraries

%description -n libswscale%swscalever
%common_descr

The libswscale library implements color conversion and scaling routines.

%package -n libswscale-devel
Summary: Development files for libswscale
Group: Development/C
Requires: libswscale%swscalever = %EVR
Requires: libavutil-devel = %EVR

%description -n libswscale-devel
This package contains development files for libswscale.

%package -n libswscale-devel-static
Summary: Static development files for libswscale
Group: Development/C
Requires: libswscale-devel = %EVR

%description -n libswscale-devel-static
This package contains static development files for libswscale.

%prep
%setup
%patch -p1

%build
xz Changelog
%ifarch x86_64
%add_optflags %optflags_shared
%else
%ifarch %ix86
%add_optflags %{?_enable_mmx:-DRUNTIME_CPUDETECT}
%endif
%endif
./configure \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--shlibdir=%_libdir \
	--mandir=%_mandir \
	--docdir=%_docdir/%name-%version \
	--disable-rpath \
%ifarch mips mipsel mips64 mips64el
	--disable-mipsdsp \
	--disable-mipsdspr2 \
	--disable-loongson2 \
	--disable-loongson3 \
	--disable-mmi \
	--disable-mips32r5 \
	--disable-mips32r6 \
	--disable-mips64r6 \
	--disable-msa \
%endif
%ifarch mips mipsel
	--disable-mipsfpu \
%endif
	%{subst_enable gpl} \
	%{subst_enable version3} \
	%{subst_enable pthreads} \
	%{subst_enable shared} \
	%{subst_enable static} \
	%{subst_enable mmx} \
	%{subst_enable nonfree} \
	%{subst_enable ffplay} \
	%{subst_enable ffprobe} \
	--enable-avfilter \
	--enable-avresample \
	%{subst_enable avisynth} \
	%{subst_enable bzlib} \
	%{subst_enable frei0r} \
	%{subst_enable gnutls} \
	%{subst_enable libaom} \
	%{subst_enable libass} \
	%{subst_enable libbluray} \
	%{subst_enable libbs2b} \
	%{subst_enable libcaca} \
	%{subst_enable libcdio} \
	%{subst_enable libcelt} \
	%{subst_enable libcodec2} \
	%{subst_enable libdav1d} \
	%{subst_enable libdc1394} \
	%{subst_enable libdrm} \
	%{subst_enable libflite} \
	%{subst_enable libfontconfig} \
	%{subst_enable libfreetype} \
	%{subst_enable libfribidi} \
	%{subst_enable libgme} \
	%{subst_enable libgsm} \
	%{subst_enable libjack} \
	%{subst_enable libmp3lame} \
	%{subst_enable_with libopencore_amrnb libopencore-amrnb} \
	%{subst_enable_with libopencore_amrwb libopencore-amrwb} \
	%{subst_enable libopenjpeg} \
	%{subst_enable libopus} \
	%{subst_enable libpulse} \
	%{subst_enable librsvg} \
	%{subst_enable librubberband} \
	%{subst_enable librtmp} \
	%{subst_enable libsnappy} \
	%{subst_enable libsoxr} \
	%{subst_enable libssh} \
	%{subst_enable libspeex} \
	%{subst_enable libtheora} \
	%{subst_enable libtwolame} \
	%{subst_enable libv4l2} \
	%{subst_enable libvidstab} \
	%{subst_enable libvorbis} \
	%{subst_enable libvpx} \
	%{subst_enable libwavpack} \
	%{subst_enable libwebp} \
	%{subst_enable libx264} \
	%{subst_enable libx265} \
	%{subst_enable libxvid} \
	%{subst_enable libzmq} \
	%{subst_enable libzvbi} \
	%{subst_enable lv2} \
	%{subst_enable openal} \
	%{subst_enable opengl} \
	%{subst_enable vaapi} \
	%{subst_enable vdpau} \
	%{subst_enable zlib} \
	--enable-hardcoded-tables \
	--enable-runtime-cpudetect \
%if_enabled debug
	--enable-debug \
%else
	--disable-debug \
%endif
	--disable-stripping \
	--enable-pic \
	--extra-cflags="%optflags" \
	--extra-version='%release' \
	#
%make_build

%install
%makeinstall_std

%files
%doc README.md
%doc MAINTAINERS
%doc Changelog*
%doc LICENSE.md
%_bindir/ffmpeg
%{?_enable_doc:%_man1dir/ffmpeg*}
%_datadir/ffmpeg
%exclude %_datadir/ffmpeg/examples

%if_enabled doc
%files doc
%doc doc/ffmpeg*.html
%doc doc/faq.html
%doc doc/fate.html
%doc doc/general.html
%doc doc/git-howto.html
%doc doc/lib*.html
%doc doc/nut.html
%doc doc/platform.html
%_man3dir/*
%endif

%if_enabled ffplay
%files -n ffplay
%_bindir/ffplay
%{?_enable_doc:%_man1dir/ffplay*}

%if_enabled doc
%files -n ffplay-doc
%doc doc/ffplay*.html
%endif
%endif

%if_enabled ffprobe
%files -n ffprobe
%_bindir/ffprobe
%{?_enable_doc:%_man1dir/ffprobe*}

%if_enabled doc
%files -n ffprobe-doc
%doc doc/ffprobe*.html
%endif
%endif

%if_enabled ffserver
%files -n ffserver
%_bindir/ffserver
%{?_enable_doc:%_man1dir/ffserver*}
%endif

%if_enabled doc
%files -n ffserver-doc
%{?_enable_ffserver:%doc doc/ffserver*.html}
%endif

%files -n libavcodec%avcodecver
%_libdir/libavcodec.so.%{avcodecver}*

%files -n libavcodec-devel
%_includedir/libavcodec
%_libdir/libavcodec.so
%_pkgconfigdir/libavcodec.pc

%files -n libavdevice%avdevicever
%_libdir/libavdevice.so.%{avdevicever}*

%files -n libavdevice-devel
%_includedir/libavdevice
%_libdir/libavdevice.so
%_pkgconfigdir/libavdevice.pc

%files -n libavfilter%avfilterver
%_libdir/libavfilter.so.%{avfilterver}*

%files -n libavfilter-devel
%_includedir/libavfilter
%_libdir/libavfilter.so
%_pkgconfigdir/libavfilter.pc

%files -n libavformat%avformatver
%_libdir/libavformat.so.%{avformatver}*

%files -n libavformat-devel
%_includedir/libavformat
%_pkgconfigdir/libavformat.pc
%_libdir/libavformat.so

%files -n libavutil%avutilver
%_libdir/libavutil.so.%{avutilver}*

%files -n libavutil-devel
%_includedir/libavutil
%_libdir/libavutil.so
%_pkgconfigdir/libavutil.pc

%files -n libpostproc%postprocver
%_libdir/libpostproc.so.%{postprocver}*

%files -n libpostproc-devel
%_includedir/libpostproc
%_libdir/libpostproc.so
%_pkgconfigdir/libpostproc.pc

%files -n libswresample%swresamplever
%_libdir/libswresample.so.%{swresamplever}*

%files -n libswresample-devel
%_includedir/libswresample
%_libdir/libswresample.so
%_pkgconfigdir/libswresample.pc

%files -n libavresample%avresamplever
%_libdir/libavresample.so.%{avresamplever}*

%files -n libavresample-devel
%_pkgconfigdir/libavresample.pc
%_includedir/libavresample
%_libdir/libavresample.so


%files -n libswscale%swscalever
%_libdir/libswscale.so.%{swscalever}*

%files -n libswscale-devel
%_includedir/libswscale
%_libdir/libswscale.so
%_pkgconfigdir/libswscale.pc

%if_enabled static
%files -n libavformat-devel-static
%_libdir/libavformat.a

%files -n libavcodec-devel-static
%_libdir/libavcodec.a

%files -n libavutil-devel-static
%_libdir/libavutil.a

%files -n libswresample-devel-static
%_libdir/libswresample.a

%files -n libavresample-devel-static
%_libdir/libavresample.a

%files -n libswscale-devel-static
%_libdir/libswscale.a

%files -n libavdevice-devel-static
%_libdir/libavdevice.a

%files -n libavfilter-devel-static
%_libdir/libavfilter.a

%files -n libpostproc-devel-static
%_libdir/libpostproc.a

%endif

%changelog
* Mon May 25 2020 Anton Farygin <rider@altlinux.ru> 2:4.2.3-alt1
- 4.2.3 (Fixes: CVE-2019-13312,CVE-2020-12284)

* Thu Apr 30 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 2:4.2.2-alt2
- Built against libdav1d.

* Thu Jan 09 2020 Anton Farygin <rider@altlinux.ru> 2:4.2.2-alt1
- 4.2.2

* Wed Sep 11 2019 Anton Farygin <rider@altlinux.ru> 2:4.2.1-alt1
- 4.2.1 (Fixes: CVE-2019-15942)

* Sat Aug 10 2019 Anton Farygin <rider@altlinux.ru> 2:4.2-alt1
- 4.1.4 -> 4.2

* Wed Jul 31 2019 Nikita Ermakov <arei@altlinux.org> 2:4.1.4-alt2
- NMU: Remove duplicates of libbluray-devel and libass-devel from BR.

* Tue Jul 23 2019 Anton Farygin <rider@altlinux.ru> 2:4.1.4-alt1
- 4.1.4 (fixes: CVE-2019-12730)

* Sun May 26 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 2:4.1.3-alt3
- Built with support of:
  + libaom and HAP codecs;
  + bs2b, flite, livl, rubberband and vidstab filters;
  + Direct Rendering Manager;
  + Game Music Emu format;
  + SFTP protocol.

* Fri Apr 19 2019 Michael Shigorin <mike@altlinux.org> 2:4.1.3-alt2
- fixed doc knob (former docs one, renamed for consistency)

* Thu Apr 04 2019 Anton Farygin <rider@altlinux.ru> 2:4.1.3-alt1
- 4.1.3

* Mon Mar 25 2019 Anton Farygin <rider@altlinux.ru> 2:4.1.2-alt1
- 4.1.2 (fixes: CVE-2019-9718, CVE-2019-9721)

* Tue Feb 26 2019 Anton Farygin <rider@altlinux.ru> 2:4.1.1-alt2
- added provides and obsoletes for avplay and avprobe packages (closes: #36109)

* Thu Feb 21 2019 Anton Farygin <rider@altlinux.ru> 2:4.1.1-alt1
- 4.1.1

* Thu Nov 08 2018 Anton Farygin <rider@altlinux.ru> 2:4.1-alt1
- 4.1

* Mon Nov 05 2018 Anton Farygin <rider@altlinux.ru> 2:4.0.3-alt1
- 4.0.3 (fixes: CVE-2018-15822)

* Sat Sep 01 2018 Anton Farygin <rider@altlinux.ru> 2:4.0.2-alt4
- disabled build with librtmp (this library is not supported by anyone)

* Mon Aug 13 2018 Anton Farygin <rider@altlinux.ru> 2:4.0.2-alt3
- fixed build with disabled glpv3 codecs

* Sun Aug 12 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 2:4.0.2-alt2
- built with new external libraries:
  + libcodec2
  + libjack
  + librsvg
- return changes that were accidentally dropped by one of previous builds:
  + built with new de/encoder: libopus
  + built with new encoders:
    - libass
    - libbluray
    - libcaca
    - libfontconfig
    - libfribidi
    - libopenjpeg
    - libsoxr
    - libzmq
    - libzvbi
    - openal
    - opengl
  + disabled some optimizations on MIPS arch family (by glebfm@)
  + disabled devel-static subpackage build

* Sat Jul 21 2018 Anton Farygin <rider@altlinux.ru> 2:4.0.2-alt1
- 4.0.2

* Mon Jun 25 2018 Anton Farygin <rider@altlinux.ru> 2:4.0.1-alt2
- enabled documentation build

* Fri Jun 22 2018 Anton Farygin <rider@altlinux.ru> 2:4.0.1-alt1
- 4.0 -> 4.0.1

* Thu May 31 2018 Anton Farygin <rider@altlinux.ru> 2:4.0-alt1
- 4.0 

* Wed May 30 2018 Anton Farygin <rider@altlinux.ru> 2:3.3.6-alt3
- rebuilt in new environment

* Thu Mar 15 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 2:3.3.6-alt2
- built with new de/encoder: libopus
- built with new encoders:
  + libtwolame
  + libwavpack
  + libwebp
- built with new external libraries:
  + libass
  + libbluray
  + libcaca
  + libfontconfig
  + libfribidi
  + libopenjpeg
  + librubberband
  + libsnappy
  + libsoxr
  + libzmq
  + libzvbi
  + openal
  + opengl
- disabled some optimizations on MIPS arch family (by glebfm@)
- disabled devel-static subpackage build

* Tue Jan 23 2018 Anton Farygin <rider@altlinux.ru> 2:3.3.6-alt1
- new version

* Sun Jan 14 2018 Yuri N. Sedunov <aris@altlinux.org> 2:3.3.5-alt1.1
- rebuild against libcdio.so.18

* Sat Oct 28 2017 Anton Farygin <rider@altlinux.ru> 2:3.3.5-alt1
- 3.3.4
- fixes:
   * CVE-2017-15186 double free when ffmpeg parsing an craft AVI file to MKV file using ffvhuff decoder.

* Fri Oct 06 2017 Anton Farygin <rider@altlinux.ru> 2:3.3.4-alt3
- rebuild for libx265 2.5

* Tue Oct 03 2017 Anton Farygin <rider@altlinux.ru> 2:3.3.4-alt2
- rebuild for recent libvpx4 1.6.1

* Mon Sep 18 2017 Anton Farygin <rider@altlinux.ru> 2:3.3.4-alt1
- 3.3.4 with fixes for multiple vilnerabilities (CVE-2017-14054, CVE-2017-14055,
	CVE-2017-14059, CVE-2017-14058, CVE-2017-14057, CVE-2017-14225, CVE-2017-14170,
	CVE-2017-14056, CVE-2017-14222, CVE-2017-14169, CVE-2017-14223, CVE-2017-14171)

* Tue Aug 01 2017 Anton Farygin <rider@altlinux.ru> 2:3.3.3-alt1
- 3.3.3 with fixes for following vulnerabilities:
	* CVE-2017-11399 remote DoS via crafted APE file
	* CVE-2017-11665 remote DoS via crafted RTMP stream
	* CVE-2017-11719 remote DoS via crafted crafted DNxHD file

* Wed Jun 14 2017 Anton Farygin <rider@altlinux.ru> 2:3.3.2-alt1
- 3.3.2

* Sat Jun 03 2017 Anton Farygin <rider@altlinux.ru> 2:3.3.1-alt2
- enabled debuginfo

* Thu May 25 2017 Anton Farygin <rider@altlinux.ru> 2:3.3.1-alt1
- updated to 3.3.1
- cleanup spec

* Sun Aug 21 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:3.1.2-alt1
- Reintroduce to Sisyphus

