# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%add_python3_path %_libdir/obs-scripting/
%add_python3_path %_datadir/obs/obs-plugins/frontend-tools/scripts/

Name: obs-studio
Summary: Free and open source software for video recording and live streaming
Summary(ru_RU.UTF-8): Свободная программа для записи и трансляции видеопотока
Version: 26.1.0
Release: alt1
License: GPLv2+
Group: Video
Url: https://github.com/jp9000/obs-studio.git
Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-luajit
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: libjansson-devel
BuildRequires: cmake gcc-c++
BuildRequires: libGL-devel libGLU-devel
BuildRequires: libX11-devel libxcb-devel
BuildRequires: libalsa-devel
BuildRequires: libjack-devel
BuildRequires: libpulseaudio-devel 
BuildRequires: qt5-base-devel qt5-x11extras-devel
BuildRequires: qt5-svg-devel
BuildRequires: pkgconfig(MagickCore)
BuildRequires: texlive-latex-base
BuildRequires: zlib-devel
BuildRequires: libcurl-devel
BuildRequires: libx264-devel
BuildRequires: libv4l-devel
BuildRequires: libswscale-devel libswresample-devel libavresample-devel
BuildRequires: libavutil-devel libavformat-devel libavdevice-devel libavfilter-devel libavcodec-devel
BuildRequires: libvlc-devel
BuildRequires: libpostproc-devel
BuildRequires: fontconfig-devel libfreetype-devel libpng-devel libexpat-devel
BuildRequires: systemd-devel libudev-devel
BuildRequires: pkgconfig(dbus-1)
BuildRequires: swig
BuildRequires: libspeexdsp-devel
%ifarch %luajit_arches
BuildRequires: libluajit-devel
%endif

Requires: %name-base = %EVR
Requires: %name-plugin-pulseaudio = %EVR
Requires: %name-plugin-jack = %EVR

Obsoletes: %name-plugin-frontend-tools <= 0.26.0
Obsoletes: %name-plugin-image-source <= 0.26.0
Obsoletes: %name-plugin-alsa <= 0.26.0
Obsoletes: %name-plugin-capture <= 0.26.0
Obsoletes: %name-plugin-decklink <= 0.26.0
Obsoletes: %name-plugin-v4l2 <= 0.26.0
Obsoletes: %name-plugin-ffmpeg <= 0.26.0
Obsoletes: %name-plugin-filters <= 0.26.0
Obsoletes: %name-plugin-outputs <= 0.26.0
Obsoletes: %name-plugin-transitions <= 0.26.0
Obsoletes: %name-plugin-rtmp-services <= 0.26.0
Obsoletes: %name-plugin-freetype2 <= 0.26.0
Obsoletes: %name-plugin-vlc-video <= 0.26.0
Obsoletes: %name-plugin-x264 <= 0.26.0

%description
Free and open source software for video recording and live streaming.

%description -l ru_RU.UTF-8
Свободная программа для записи и трансляции видеопотока.

%package base
Summary: Free and open source software for video recording and live streaming
Summary(ru_RU.UTF-8): Свободная программа для записи и трансляции видеопотока
Group: Video
Requires: libobs = %EVR
%add_python3_req_skip obspython

%description base
Free and open source software for video recording and live streaming.
Base application without plugins. Some of the plugins are required to run.

%description base -l ru_RU.UTF-8
Свободная программа для записи и трансляции видеопотока.
Базовое приложение без плагинов. Для запуска потребуются некоторые из плагинов.

%package -n libobs
Summary: Open Broadcaster Software Studio libraries
Group: Video

%description -n libobs
Library files for Open Broadcaster Software.

%package -n libobs-devel
Summary: Development files for %name
Group: Development/C
Requires: libobs = %EVR

%description -n libobs-devel
Development files for %name

%package plugin-jack
Summary: JACK plugin for Open Broadcaster Software.
Group: Video
Requires: %name-base = %EVR

%description plugin-jack
JACK plugin for Open Broadcaster Software.

%package plugin-pulseaudio
Summary: PulseAudio plugin for Open Broadcaster Software.
Group: Video
Requires: %name-base = %EVR

%description plugin-pulseaudio
PulseAudio plugin for Open Broadcaster Software.

%prep
%setup

# rpmlint reports E: hardcoded-library-path
# replace OBS_MULTIARCH_SUFFIX by LIB_SUFFIX
sed -i 's|OBS_MULTIARCH_SUFFIX|LIB_SUFFIX|g' cmake/Modules/ObsHelpers.cmake

%build
%cmake \
    -DOBS_VERSION_OVERRIDE=%version \
    -DUNIX_STRUCTURE=1

%cmake_build

%install
%cmakeinstall_std

%files
%_datadir/metainfo/*

%files base
%doc COPYING README.rst
%_bindir/*
%_datadir/obs/*
%exclude %_datadir/obs/libobs/
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_libdir/obs-scripting/
%_libdir/obs-plugins
%exclude %_libdir/obs-plugins/linux-jack.so
%exclude %_datadir/obs/obs-plugins/linux-jack/
%exclude %_libdir/obs-plugins/linux-pulseaudio.so
%exclude %_datadir/obs/obs-plugins/linux-pulseaudio/

%files -n libobs
%dir %_datadir/obs
%_datadir/obs/libobs/
%_libdir/*.so.*
%_libdir/libobs-scripting.so

%files -n libobs-devel
%_includedir/obs/
%_libdir/*.so
%exclude %_libdir/libobs-scripting.so
%_libdir/cmake/LibObs/
%_libdir/pkgconfig/libobs.pc

%files plugin-jack
%_libdir/obs-plugins/linux-jack.so
%_datadir/obs/obs-plugins/linux-jack/

%files plugin-pulseaudio
%_libdir/obs-plugins/linux-pulseaudio.so
%_datadir/obs/obs-plugins/linux-pulseaudio/

%changelog
* Tue Dec 15 2020 Anton Midyukov <antohami@altlinux.org> 26.1.0-alt1
- new version 26.1.0

* Sat Oct 10 2020 Anton Midyukov <antohami@altlinux.org> 26.0.2-alt1
- new version 26.0.2

* Fri Oct 02 2020 Anton Midyukov <antohami@altlinux.org> 26.0.0-alt1
- new version 26.0.0
- basic plugins included in the package obs-studio-base
- allowed for all architectures
- avoid luajit where unavailable

* Sat Nov 10 2018 Anton Midyukov <antohami@altlinux.org> 22.0.2-alt1
- new version 22.0.2

* Tue Sep 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 21.1.1-alt2
- NMU: fixed build with Qt-5.11.

* Fri Jul 06 2018 Anton Midyukov <antohami@altlinux.org> 21.1.1-alt1
- new version 21.1.1

* Fri Oct 06 2017 Anton Midyukov <antohami@altlinux.org> 20.0.1-alt1
- new version 20.0.1

* Wed Jul 12 2017 Anton Midyukov <antohami@altlinux.org> 19.0.3-alt1
- Initial build for ALT Linux Sisyphus (Closes: 30989).
