%define branch 0.12
%define svn svn9218

%define rel alt1

%if "%rel" == "alt0.M51"
%define PLUG_DISABLE "UDISKS2_PLUGIN OPUS_PLUGIN WITH_NEW_JACK WITH_QSUI ARCHIVE_PLUGIN"
%define PLUG_ENABLE "FFMPEG_LEGACY UDISKS_PLUGIN JACK_PLUGIN"
%endif

%if "%rel" == "alt0.M60T"
%define PLUG_DISABLE "UDISKS2_PLUGIN ARCHIVE_PLUGIN"
%define PLUG_ENABLE "UDISKS_PLUGIN WITH_NEW_JACK"
%endif

%if "%rel" == "alt0.M70T"
%define PLUG_DISABLE "UDISKS_PLUGIN ARCHIVE_PLUGIN"
%define PLUG_ENABLE "UDISKS2_PLUGIN WITH_NEW_JACK"
%endif

%if "%rel" == "alt0.M80P"
%define PLUG_DISABLE "UDISKS_PLUGIN"
%define PLUG_ENABLE "UDISKS2_PLUGIN WITH_NEW_JACK ARCHIVE_PLUGIN"
%endif

%if "%rel" == "alt1"
%define PLUG_DISABLE "UDISKS_PLUGIN"
%define PLUG_ENABLE "UDISKS2_PLUGIN WITH_NEW_JACK ARCHIVE_PLUGIN"
%endif

Version: %branch.7
Epoch: 1
Name: qmmp
Release: %rel.%svn
Summary: QMMP - Qt-based multimedia player
Summary(ru_RU.UTF8): Qmmp - мультимедиа проигрыватель на базе Qt
Summary(uk_UA.UTF8): Qmmp - мультимедіа програвач на базі Qt
License: GPLv2
Group: Sound
Packager: Motsyo Gennadi <drool@altlinux.ru>
Url: http://qmmp.ylsoftware.com/
Source0: %name-%branch.tar.bz2

Requires: unzip winamplike-skins lib%name = %version-%release %name-out-pulseaudio = %version-%release

BuildPreReq: rpm-build-wlskins doxygen

BuildRequires: gcc-c++ libavformat-devel libmad-devel
BuildRequires: libcurl-devel libfaad-devel libmpg123-devel libmodplug-devel
BuildRequires: libmpcdec-devel libpulseaudio-devel >= 0.9.15 libqt4-devel
BuildRequires: libsoxr-devel libtag-devel >= 1.6 libvorbis-devel
BuildRequires: libwavpack-devel libalsa-devel libflac-devel libbs2b-devel >= 3.0
BuildRequires: libprojectM-devel >= 2.0.1 jackit-devel xorg-xf86miscproto-devel
BuildRequires: libenca-devel libcddb-devel libmms-devel >= 0.4 libwildmidi-devel >= 0.2.3.4
BuildRequires: libgme-devel libGLU-devel libsidplayfp-devel >= 1.0.3 libshout2-devel

# for ALT >= 8 only
%define alt_over_8 libcdio-devel
%if "%rel" == "alt1"
%define alt_over_8 libcdio-paranoia-devel libarchive-devel
%endif
%if "%rel" == "alt0.M80P"
%define alt_over_8 libcdio-paranoia-devel libarchive-devel
%endif
BuildRequires: %alt_over_8

%if "%rel" != "alt0.M51"
# disable for 5.1
BuildRequires: libopusfile-devel
%endif

%description
QMMP is an audio-player, written with help of Qt library.
The user interface is similar to winamp or xmms.

Supported formats:
- MPEG1 layer 2/3
- Ogg Vorbis
- Opus
- Native FLAC, Ogg FLAC
- Musepack
- WavePack
- tracker modules (mod, s3m, it, xm, etc)
- ADTS AAC
- CD Audio
- WMA, Monkey's Audio (and other formats provided by FFmpeg library)
- PCM WAVE (and other formats provided by libsndfile library)
- midi
- chiptune formats (AY, GBS, GYM, HES, KSS, NSF, NSFE, SAP, SPC, VGM, VGZ, VTX)

DSP effects:
- BS2B effect
- sample rate converter
- LADSPA effects
- extra stereo
- crossfade (Experimental)

Visual effects:
- projectM visualization
- spectrum analyzer

Output system support:
- OSS
- ALSA (Linux)
- Pulse Audio
- JACK
- WaveOut (Win32)

Other features:
- XMMS and Winamp 2.x skins support
- 10-band equalizer
- MP3, Vorbis, AAC, AAC+ streams support
- mms support
- MPRIS (1.0 and 2.0)
- removable device detection (via HAL or UDisks)
- video playback via Mplayer
- lyrics (using lyrics.wikia.com)
- cover art support
- CUE sheet support
- embedded CUE support (for FLAC and WavPack)
- multiple playlists
- automatic charset detection for cue files and ShoutCast metadata
- playlist formats: m3u, pls, xspf
- ReplayGain support
- Last.fm/Libre.fm scrobbler
- CDDB support

%description -l ru_RU.UTF8
Программа является аудио-плеером, написанным с использованием библиотеки Qt.
Пользовательский интерфейс сходный с winamp или xmms.

Поддерживаемые форматы:
- MPEG1 layer 2/3
- Ogg Vorbis
- Opus
- Native FLAC, Ogg FLAC
- Musepack
- WavePack
- трекерные форматы (mod, s3m, it, xm и т.д.)
- ADTS AAC
- CD Audio
- WMA, Monkey's Audio (и др. форматы библиотеки FFmpeg)
- PCM WAVE (и др. форматы библиотеки libsndfile)
- midi
- форматы звука игровых консолей (AY, GBS, GYM, HES, KSS, NSF, NSFE, SAP, SPC, VGM, VGZ, VTX)

Аудио-эффекты:
- эффект BS2B
- Передискретизация
- эффекты LADSPA
- расширение стереобазы
- плавный переход между треками (экспериментальный)

Визуальные эффекты:
- визуализация projectM
- анализатор спектра

Системы вывода звука:
- OSS
- ALSA (Linux)
- Pulse Audio
- JACK
- WaveOut (Win32)

Другие возможности:
- поддержка обложек XMMS и Winamp 2.x
- 10-полосный эквалайзер
- поддержка потоков MP3, Vorbis, AAC, AAC+
- поддержка протокола MMS
- MPRIS (1.0 и 2.0)
- автоопределение съёмных устройств (с помощью HAL или UDisks)
- воспроизведение видео с помощью Mplayer-а
- получение текстов песен с lyrics.wikia.com
- просмотр обложек
- поддержка CUE
- поддержка "встроенного" CUE (для файлов FLAC и WavPack)
- возможность использовать несколько списков воспроизведения
- автоматической определение кодировки для cue-файлов и ShoutCast-метаданных
- поддерживаемые форматы списков воспроизведения: m3u, pls, xspf
- поддержка ReplayGain
- скробблер Last.fm/Libre.fm
- поддержка CDDB

%description -l uk_UA.UTF8
Програма є аудіо-плеєром, написаним з використанням бібліотеки Qt.
Інтерфейс користувача подібний до winamp чи xmms.

Підтримувані формати:
- MPEG1 layer 2/3
- Ogg Vorbis
- Opus
- Native FLAC, Ogg FLAC
- Musepack
- WavePack
- трекерные форматы (mod, s3m, it, xm и т.д.)
- ADTS AAC
- CD Audio
- WMA, Monkey's Audio (та інші формати бібліотеки FFmpeg)
- PCM WAVE (та інші формати бібліотеки libsndfile)
- midi
- формати звуку ігрових консолей (AY, GBS, GYM, HES, KSS, NSF, NSFE, SAP, SPC, VGM, VGZ, VTX)

Аудіо-ефекти:
- Ефект BS2B
- Передискретизація
- Ефекти LADSPA
- розширення стереобази
- плавний перехід між треками (експериментально)

Візуальні ефекти:
- Візуалізація projectM
- Аналізатор спектру

Системы вывода звукаСистеми виведення звуку:
- OSS
- ALSA (Linux)
- Pulse Audio
- JACK
- WaveOut (Win32)

Інші можливості:
- Підтримка обкладинок Xmms і Winamp 2.x
- 10-смуговий еквалайзер
- Підтримка потоків MP3, Vorbis, AAC, AAC +
- Підтримка протоколу MMS (експериментальна)
- MPRIS
- Автовизначення знімних пристроїв (за допомогою HAL або UDisks)
- Відтворення відео за допомогою MPlayer-а
- Отримання текстів пісень з lyricsplugin.com
- Перегляд обкладинок
- Підтримка CUE
- Підтримка "вбудованого" CUE (для файлів FLAC і WavPack)
- Можливість використовувати декілька списків відтворення
- Автоматичне визначення кодування для cue-файлів і ShoutCast-метаданих
- Підтримувані формати списків відтворення: m3u, pls, xspf
- Підтримка ReplayGain
- Скробблер Last.fm/Libre.fm
- Підтримка CDDB

%package -n %name-docs
Summary: Documentation for Qmmp
Group: Documentation
BuildArch: noarch

%description -n %name-docs
Documentation for Qmmp

%package -n lib%name
Summary: Shared libraries for Qmmp
Group: System/Libraries

%description -n lib%name
Shared libraries for Qmmp

# Output plugins
%package -n %name-out-pulseaudio
Summary: Qmmp PulseAudio Output Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-out-pulseaudio
Qmmp PulseAudio Output Plugin

%package -n %name-out-oss
Summary: Qmmp OSS Output Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-out-oss
Qmmp OSS Output Plugin

%package -n %name-out-jack
Summary: Qmmp Jack Output Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-out-jack
Qmmp Jack Output Plugin

%package -n %name-out-qtmultimedia
Summary: Qmmp Qt Multimedia Output Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-out-qtmultimedia
Qmmp Qt Multimedia Output Plugin

%package -n %name-out-null
Summary: Qmmp Null Output Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-out-null
Qmmp Null Output Plugin

%package -n %name-out-icecast
Summary: Qmmp Icecast Output Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-out-icecast
Qmmp Icecast Output Plugin

# Input plugins
%package -n %name-in-ffmpeg
Summary: Qmmp FFMPEG Audio Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-in-ffmpeg
Qmmp FFMPEG Audio Plugin

%package -n %name-in-flac
Summary: Qmmp FLAC Audio Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-in-flac
Qmmp FLAC Audio Plugin

%package -n %name-in-musepack
Summary: Qmmp Musepack Audio Plugin
Group: Sound
Requires: qmmp = %version-%release libtag >= 1.6

%description -n %name-in-musepack
Qmmp Musepack Audio Plugin

%package -n %name-in-sndfile
Summary: Qmmp Sndfile Audio Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-in-sndfile
Qmmp Sndfile Audio Plugin

%package -n %name-in-wavpack
Summary: Qmmp WavPack Audio Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-in-wavpack
Qmmp WavPack Audio Plugin

%package -n %name-in-modplug
Summary: Qmmp ModPlug Audio Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-in-modplug
Qmmp ModPlug Audio Plugin

%package -n %name-in-cue
Summary: Qmmp Cue Audio Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-in-cue
Qmmp Cue Audio Plugin

%package -n %name-in-aac
Summary: Qmmp AAC Audio Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-in-aac
Qmmp AAC Audio Plugin

%package -n %name-in-mplayer
Summary: Qmmp MPlayer Plugin
Group: Video
Requires: qmmp = %version-%release mplayer

%description -n %name-in-mplayer
Qmmp MPlayer Plugin

%package -n %name-in-cdaudio
Summary: Qmmp CDAudio Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-in-cdaudio
Qmmp CDAudio Plugin

%package -n %name-in-midi
Summary: Qmmp Midi Plugin
Group: Sound
Requires: qmmp = %version-%release
Requires: libwildmidi

%description -n %name-in-midi
Qmmp Midi Plugin, used WildMidi

%package -n %name-in-gme
Summary: Qmmp GME Audio Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-in-gme
Qmmp GME Audio Plugin

%package -n %name-in-opus
Summary: Qmmp Opus Audio Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-in-opus
Qmmp Opus Audio Plugin

%package -n %name-in-sid
Summary: Qmmp SID Audio Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-in-sid
This plugin plays Commodore 64 music files using libsidplayfp library

%package -n %name-in-archive
Summary: Qmmp Archive Reader Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-in-archive
Qmmp Archive Reader Plugin

# Visualization plugins
%package -n %name-vis-analyzer
Summary: Qmmp Analyzer Visual Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-vis-analyzer
Qmmp Analyzer Visual Plugin

%package -n %name-vis-projectm
Summary: Qmmp ProjectM Visual Plugin
Group: Sound
Requires: qmmp = %version-%release libprojectM >= 2.0.1

%description -n %name-vis-projectm
Qmmp ProjectM Visual Plugin

# Effects plugins
%package -n %name-eff-soxr
Summary: Qmmp SoX Resampler Plugin
Group: Sound
Requires: qmmp = %version-%release
Provides: %name-eff-srconverter
Obsoletes: %name-eff-srconverter

%description -n %name-eff-soxr
Qmmp SoX Resampler Plugin

%package -n %name-eff-bs2b
Summary: Qmmp BS2B Effect Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-eff-bs2b
Qmmp BS2B Effect Plugin

%package -n %name-eff-ladspa
Summary: Qmmp LADSPA Effect Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-eff-ladspa
Qmmp LADSPA Effect Plugin

%package -n %name-eff-crossfade
Summary: Qmmp Crossfade Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-eff-crossfade
Qmmp Crossfade Plugin

%package -n %name-eff-extrastereo
Summary: Qmmp Extra Stereo Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-eff-extrastereo
Qmmp Extra Stereo Plugin

%package -n %name-eff-monotostereo
Summary: Qmmp Mono to Stereo Converter Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-eff-monotostereo
Qmmp Mono to Stereo Converter Plugin

%package -n %name-eff-filewriter
Summary: File Writer Plugin for Qmmp
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-eff-filewriter
File Writer Plugin for Qmmp

# Transports plugins
%package -n %name-http
Summary: Qmmp HTTP Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-http
Qmmp HTTP Plugin

%package -n %name-mms
Summary: Qmmp MMS Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-mms
Qmmp Plugin for MMS stream protocol support

# Interface plugins
%package -n %name-qsui
Summary: Qmmp Simple Ui - simple user interface based on standard widgets set
Summary(ru_RU.UTF8): Qmmp Simple Ui - простой пользовательский интерфейс с использованием стандартных элементов
Summary(uk_UA.UTF8): Qmmp Simple Ui - простий інтерфейс користувача з використанням стандартних елементів
Group: Sound
Requires: qmmp >= %version-%release
Provides: qmmp-plugin-pack-qsui
Obsoletes: qmmp-plugin-pack-qsui

%description -n %name-qsui
Qmmp Simple Ui - simple user interface based on standard widgets set for Qmmp.

%description -l ru_RU.UTF8 -n %name-qsui
Qmmp Simple Ui - простой пользовательский интерфейс с использованием стандартных элементов для Qmmp.

%description -l uk_UA.UTF8 -n %name-qsui
Qmmp Simple Ui - простий інтерфейс користувача з використанням стандартних елементів для Qmmp.


# General plugins
%package -n %name-converter
Summary: Qmmp Converter Plugin
Group: Sound
Requires: qmmp = %version-%release
Requires: /usr/bin/oggenc lame flac wavpack

%description -n %name-converter
Qmmp Converter Plugin. This plugin converts supported audio
files to other file formats using external command-line encoders.

%package -n %name-mpris
Summary: Qmmp MPRIS Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-mpris
Qmmp MPRIS Plugin

%package -n %name-notifier
Summary: Qmmp Notifier Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-notifier
Qmmp Notifier Plugin

%package -n %name-kdenotify
Summary: Qmmp notification plugin for KDE4
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-kdenotify
Qmmp notification plugin for KDE4

%package -n %name-scrobbler
Summary: Qmmp AudioScrobbler Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-scrobbler
Qmmp AudioScrobbler Plugin

%package -n %name-statusicon
Summary: Qmmp Status Icon Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-statusicon
Qmmp Status Icon Plugin

%package -n %name-lyrics
Summary: Qmmp Lyrics Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-lyrics
Qmmp Lyrics Plugin

%package -n %name-hal
Summary: Qmmp HAL Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-hal
Qmmp HAL Plugin

%package -n %name-hotkey
Summary: Qmmp Global Hotkey Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-hotkey
Qmmp Global Hotkey Plugin. This plugin adds support
for multimedia keys or global key combinations

%package -n %name-gnomehotkey
Summary: Qmmp Gnome Hotkey Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-gnomehotkey
Qmmp Gnome Hotkey Plugin. This plugin adds
support of the GNOME/Cinnamon hotkeys

%package -n %name-fileops
Summary: Qmmp file operations Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-fileops
Qmmp file operations Plugin

%package -n %name-covermanager
Summary: Qmmp cover manager Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-covermanager
Qmmp cover manager Plugin

%package -n %name-udisks
Summary: Qmmp UDisks Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-udisks
Qmmp UDisks Plugin

%package -n %name-streambrowser
Summary: Qmmp Stream Browser Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-streambrowser
This Qmmp plugin allows to add stream from IceCast stream directory

%package -n %name-copypaste
Summary: Qmmp Copy/Paste Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-copypaste
This plugin allows to copy selected tracks from one playlist to another

%package -n %name-trackchange
Summary: Qmmp Track Change Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-trackchange
This plugin executes external command when current track is changed

%package -n %name-rgscan
Summary: ReplayGain Scanner Plugin for Qmmp
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-rgscan
This plugin scans audio files and gives information for volume normalization

%package -n %name-history
Summary: Qmmp Listening History Plugin
Group: Sound
Requires: qmmp = %version-%release

%description -n %name-history
This plugin collects information about listened tracks

%package -n lib%name-devel
Summary: Qmmp header files
Group: Development/C++
Requires: lib%name = %version-%release
Provides: %name-devel
Obsoletes: %name-devel

%description -n lib%name-devel
%name-devel contains the header files needed to develop
programs which make use of Qmmp.

%package -n %name-full
Summary: QMMP - Qt-based multimedia player
Group: Sound
BuildArch: noarch
Requires: qmmp qmmp-in-wavpack qmmp-mpris qmmp-notifier
Requires: qmmp-eff-soxr qmmp-in-ffmpeg qmmp-in-mplayer
Requires: qmmp-in-flac qmmp-out-pulseaudio qmmp-in-modplug qmmp-in-midi
Requires: qmmp-in-musepack qmmp-statusicon qmmp-in-sndfile qmmp-in-cue
Requires: qmmp-vis-analyzer qmmp-scrobbler qmmp-hal qmmp-hotkey qmmp-gnomehotkey
Requires: qmmp-eff-bs2b qmmp-vis-projectm qmmp-fileops qmmp-converter
Requires: qmmp-out-jack qmmp-out-oss qmmp-out-null qmmp-http qmmp-mms
Requires: qmmp-kdenotify qmmp-eff-ladspa qmmp-covermanager qmmp-rgscan
Requires: qmmp-eff-crossfade qmmp-udisks qmmp-in-gme qmmp-in-sid qmmp-history
Requires: qmmp-streambrowser qmmp-trackchange qmmp-copypaste qmmp-eff-extrastereo
Requires: qmmp-out-qtmultimedia qmmp-out-icecast qmmp-eff-filewriter qmmp-eff-monotostereo

%if "%rel" != "alt0.M51"
# disable for 5.1
Requires: qmmp-in-opus qmmp-qsui
%endif

%if "%alt_over_8" != "libcdio-devel"
# ALT >= 8 only
Requires: qmmp-in-archive
%endif

%description -n %name-full
Virtual package for full installation Qmmp (exclude %name-devel).

%prep
%setup -q -n %name-%branch-svn

%build
# # with CMake
# # cmake \
# # 	-DCMAKE_INSTALL_PREFIX=%prefix \
# # 	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
# # 	-DCMAKE_C_FLAGS:STRING="%optflags" \
# # 	-DLIB_DIR:STRING=%_lib \
# # 	-DUSE_OSS:BOOL=TRUE

# # with QMake
export PATH=$PATH:%_qt4dir/bin
qmake	"QMAKE_CFLAGS+=%optflags" \
	"QMAKE_CXXFLAGS+=%optflags" \
	LIB_DIR=%_libdir \
	'DISABLED_PLUGINS=OSS4_PLUGIN %PLUG_DISABLE' \
	'CONFIG+=%PLUG_ENABLE QMMP_DEFAULT_OUTPUT=pulse' \
	%name.pro
%make_build VERBOSE=1

cd doc && doxygen Doxyfile

%install
# # with CMake
# # %make DESTDIR=%buildroot install

# # with QMake
%make INSTALL_ROOT=%buildroot install

mkdir -p %buildroot%_datadir/%name-0
ln -s %_wlskindir %buildroot%_datadir/%name-0/skins
mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}

%files
%dir %_libdir/%name-%branch
%dir %_libdir/%name-%branch/Input
%dir %_libdir/%name-%branch/Ui
%dir %_libdir/%name-%branch/Output
%dir %_libdir/%name-%branch/Engines
%dir %_libdir/%name-%branch/Transports
%dir %_libdir/%name-%branch/PlayListFormats
%dir %_libdir/%name-%branch/CommandLineOptions
%dir %_libdir/%name-%branch/FileDialogs
%dir %_libdir/%name-%branch/Effect
%dir %_libdir/%name-%branch/General
%dir %_libdir/%name-%branch/Visual
%_bindir/*
%_desktopdir/*
%_libdir/%name-%branch/Input/libmpeg*
%_libdir/%name-%branch/Input/libvorbis*
%_libdir/%name-%branch/Ui/libskinned*
%_libdir/%name-%branch/Output/libalsa*
%_libdir/%name-%branch/PlayListFormats/*.so
%_libdir/%name-%branch/CommandLineOptions/*.so
%_libdir/%name-%branch/FileDialogs/*.so
%_datadir/%name-0/
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/scalable/apps/*
%_datadir/metainfo/*.xml

%files -n lib%name
%_libdir/*.so.0
%_libdir/*.so.0.12*

# Output plugins
%files -n %name-out-pulseaudio
%_libdir/%name-%branch/Output/libpulseaudio*

%files -n %name-out-oss
%_libdir/%name-%branch/Output/liboss*

%files -n %name-out-jack
%_libdir/%name-%branch/Output/libjack*

%files -n %name-out-qtmultimedia
%_libdir/%name-%branch/Output/libqtmultimedia*

%files -n %name-out-null
%_libdir/%name-%branch/Output/libnull*

%files -n %name-out-icecast
%_libdir/%name-%branch/Output/libshout*

# Input plugins
%files -n %name-in-ffmpeg
%_libdir/%name-%branch/Input/libffmpeg*

%files -n %name-in-flac
%_libdir/%name-%branch/Input/libflac*

%files -n %name-in-musepack
%_libdir/%name-%branch/Input/libmpc*

%files -n %name-in-sndfile
%_libdir/%name-%branch/Input/libsndfile*

%files -n %name-in-wavpack
%_libdir/%name-%branch/Input/libwavpack*

%files -n %name-in-cue
%_libdir/%name-%branch/Input/libcue*

%files -n %name-in-aac
%_libdir/%name-%branch/Input/libaac*

%files -n %name-in-modplug
%_libdir/%name-%branch/Input/libmodplug*

%files -n %name-in-mplayer
%_libdir/%name-%branch/Engines/libmplayer*

%files -n %name-in-cdaudio
%_libdir/%name-%branch/Input/libcdaudio*

%files -n %name-in-midi
%_libdir/%name-%branch/Input/libwildmidi*

%files -n %name-in-gme
%_libdir/%name-%branch/Input/libgme*

%files -n %name-in-sid
%_libdir/%name-%branch/Input/libsid*

%if "%alt_over_8" != "libcdio-devel"
# ALT >= 8 only
%files -n %name-in-archive
%_libdir/%name-%branch/Input/libarchive*
%endif

%if "%rel" != "alt0.M51"
# disable for 5.1
%files -n %name-in-opus
%_libdir/%name-%branch/Input/libopus*
%endif

# Visualization plugins
%files -n %name-vis-analyzer
%_libdir/%name-%branch/Visual/libanalyzer*

%files -n %name-vis-projectm
%_libdir/%name-%branch/Visual/libprojectm*

# Effects plugins
%files -n %name-eff-soxr
%_libdir/%name-%branch/Effect/libsoxr*

%files -n %name-eff-bs2b
%_libdir/%name-%branch/Effect/libbs2b*

%files -n %name-eff-ladspa
%_libdir/%name-%branch/Effect/libladspa*

%files -n %name-eff-crossfade
%_libdir/%name-%branch/Effect/libcrossfade*

%files -n %name-eff-extrastereo
%_libdir/%name-%branch/Effect/libstereo*

%files -n %name-eff-monotostereo
%_libdir/%name-%branch/Effect/libmonotostereo*

%files -n %name-eff-filewriter
%_libdir/%name-%branch/Effect/libfilewriter*

# Transports plugins
%files -n %name-http
%_libdir/%name-%branch/Transports/libhttp*

%files -n %name-mms
%_libdir/%name-%branch/Transports/libmms*

# Interface plugins
%if "%rel" != "alt0.M51"
%files -n %name-qsui
%_libdir/%name-%branch/Ui/libqsui*
%endif

# General plugins
%files -n %name-converter
%_libdir/%name-%branch/General/libconverter*

%files -n %name-mpris
%_libdir/%name-%branch/General/libmpris*

%files -n %name-notifier
%_libdir/%name-%branch/General/libnotifier*

%files -n %name-kdenotify
%_libdir/%name-%branch/General/libkdenotify*

%files -n %name-scrobbler
%_libdir/%name-%branch/General/libscrobbler*

%files -n %name-statusicon
%_libdir/%name-%branch/General/libstatusicon*

%files -n %name-lyrics
%_libdir/%name-%branch/General/liblyrics*

%files -n %name-hal
%_libdir/%name-%branch/General/libhal*

%files -n %name-hotkey
%_libdir/%name-%branch/General/libhotkey*

%files -n %name-gnomehotkey
%_libdir/%name-%branch/General/libgnomehotkey*

%files -n %name-fileops
%_libdir/%name-%branch/General/libfileops*

%files -n %name-covermanager
%_libdir/%name-%branch/General/libcovermanager*

%files -n %name-udisks
%_libdir/%name-%branch/General/libudisks*

%files -n %name-streambrowser
%_libdir/%name-%branch/General/libstreambrowser*

%files -n %name-trackchange
%_libdir/%name-%branch/General/libtrackchange*

%files -n %name-copypaste
%_libdir/%name-%branch/General/libcopypaste*

%files -n %name-history
%_libdir/%name-%branch/General/libhistory*

%files -n %name-rgscan
%_libdir/%name-%branch/General/librgscan*

%files -n lib%name-devel
%dir %_includedir/%name-0
%dir %_includedir/%name-0/qmmp
%dir %_includedir/%name-0/qmmpui
%_pkgconfigdir/*.pc
%_includedir/%name-0/%name/*.h
%_includedir/%name-0/%{name}ui/*.h
%_libdir/*.so

%files -n %name-docs
%doc AUTHORS ChangeLog* README* doc/html

%files -n %name-full

%changelog
* Sun Jan 26 2020 Motsyo Gennadi <drool@altlinux.ru> 1:0.12.7-alt1.svn9218
- 0.12.7 svn9218 version

* Sun Jul 21 2019 Motsyo Gennadi <drool@altlinux.ru> 1:0.12.3-alt1.svn9010
- 0.12.3 svn9010 version

* Sat Jul 20 2019 Motsyo Gennadi <drool@altlinux.ru> 1:0.12.3-alt1.svn9005
- 0.12.3 svn9005 version

* Sat Jan 26 2019 Motsyo Gennadi <drool@altlinux.ru> 1:0.12.0-alt1.svn8656
- 0.12.0 svn8656 version

* Fri Sep 14 2018 Motsyo Gennadi <drool@altlinux.ru> 1:0.12.0-alt1.svn8288.1
- fix subdirectories packaging violation

* Fri Sep 14 2018 Motsyo Gennadi <drool@altlinux.ru> 1:0.12.0-alt1.svn8288
- 0.12.0 svn8288 version

* Tue Sep 11 2018 Motsyo Gennadi <drool@altlinux.ru> 1:0.12.0-alt1.svn8283
- 0.12.0 svn8283 version

* Tue Jun 05 2018 Motsyo Gennadi <drool@altlinux.ru> 1:0.12.0-alt1.svn7877.1
- build with new libva

* Sat Mar 17 2018 Motsyo Gennadi <drool@altlinux.ru> 1:0.12.0-alt1.svn7877
- 0.12.0 svn7877 version

* Sun Jan 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1:0.11.0-alt1.svn7463.1
- rebuild against libcdio.so.18

* Tue Sep 12 2017 Motsyo Gennadi <drool@altlinux.ru> 1:0.11.0-alt1.svn7463
- 0.11.0 svn7463 version

* Fri Aug 25 2017 Motsyo Gennadi <drool@altlinux.ru> 1:0.11.0-alt1.svn7388
- 0.11.0 svn7388 version

* Sun Jul 02 2017 Motsyo Gennadi <drool@altlinux.ru> 1:0.11.0-alt1.svn7284
- 0.11.0 svn7284 version

* Mon Apr 17 2017 Motsyo Gennadi <drool@altlinux.ru> 1:0.11.0-alt1.svn7121
- 0.11.0 svn7121 version

* Sat Jan 07 2017 Motsyo Gennadi <drool@altlinux.ru> 1:0.11.0-alt1.svn6953
- 0.11.0 svn6953 version

* Fri Aug 19 2016 Motsyo Gennadi <drool@altlinux.ru> 1:0.11.0-alt1.svn6682
- 0.11.0 svn6682 version

* Fri Aug 12 2016 Motsyo Gennadi <drool@altlinux.ru> 1:0.11.0-alt1.svn6670
- 0.11.0 svn6670 version

* Sat Jun 25 2016 Motsyo Gennadi <drool@altlinux.ru> 1:0.11.0-alt1.svn6521
- 0.11.0 svn6521 version

* Mon May 09 2016 Motsyo Gennadi <drool@altlinux.ru> 1:0.10.0-alt1.svn6342
- 0.10.0 svn6342 version

* Wed Apr 20 2016 Motsyo Gennadi <drool@altlinux.ru> 1:0.10.0-alt1.svn6253
- 0.10.0 svn6253 version

* Fri Apr 01 2016 Motsyo Gennadi <drool@altlinux.ru> 1:0.10.0-alt1.svn6214
- 0.10.0 svn6214 version

* Wed Mar 30 2016 Motsyo Gennadi <drool@altlinux.ru> 1:0.10.0-alt1.svn6202
- 0.10.0 svn6202 version

* Mon Mar 28 2016 Motsyo Gennadi <drool@altlinux.ru> 1:0.10.0-alt1.svn6201
- 0.10.0 svn6201 version

* Sun Mar 27 2016 Motsyo Gennadi <drool@altlinux.ru> 1:0.10.0-alt1.svn6199
- 0.10.0 svn6199 version

* Sat Mar 26 2016 Motsyo Gennadi <drool@altlinux.ru> 1:0.10.0-alt1.svn6198
- 0.10.0 svn6198 version

* Wed Feb 10 2016 Motsyo Gennadi <drool@altlinux.ru> 1:0.10.0-alt1.svn6129
- 0.10.0 svn6129 version

* Wed Feb 10 2016 Motsyo Gennadi <drool@altlinux.ru> 1:0.10.0-alt1.svn6126
- 0.10.0 svn6126 version

* Fri Nov 13 2015 Motsyo Gennadi <drool@altlinux.ru> 1:0.10.0-alt1.svn5769
- 0.10.0 svn5769 version

* Tue Nov 03 2015 Motsyo Gennadi <drool@altlinux.ru> 1:0.10.0-alt1.svn5734
- 0.10.0 svn5734 version

* Sat Sep 26 2015 Motsyo Gennadi <drool@altlinux.ru> 1:0.10.0-alt1.svn5598
- 0.10.0 svn5598 version
- bump version

* Sun Sep 06 2015 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn5545
- 0.9.0 svn5545 version

* Thu Aug 06 2015 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn5329
- 0.9.0 svn5329 version
- rebuild with libcdio-paranoia

* Sun Jul 26 2015 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn5273
- 0.9.0 svn5273 version

* Tue Jun 16 2015 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn5161
- 0.9.0 svn5161 version

* Tue Jun 16 2015 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn5157.1
- fix build

* Tue Jun 16 2015 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn5157
- 0.9.0 svn5157 version

* Sun Jun 14 2015 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn5138
- 0.9.0 svn5138 version

* Sat Jun 13 2015 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn5136
- 0.9.0 svn5136 version

* Sun May 03 2015 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn4802
- 0.9.0 svn4802 version

* Thu Dec 25 2014 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn4636
- 0.9.0 svn4636 version
- build with cmake

* Tue Dec 23 2014 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn4634
- 0.9.0 svn4634 version
- build with qmake

* Wed Dec 10 2014 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn4630
- 0.9.0 svn4630 version

* Tue Oct 21 2014 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn4592
- 0.9.0 svn4592 version

* Tue Oct 21 2014 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn4590
- 0.9.0 svn4590 version

* Sun Oct 19 2014 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn4587
- 0.9.0 svn4587 version

* Fri Oct 17 2014 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn4582
- 0.9.0 svn4582 version

* Thu Oct 16 2014 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn4581
- 0.9.0 svn4581 version

* Thu Aug 07 2014 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn4425
- 0.9.0 svn4425 version

* Mon Aug 04 2014 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn4400
- 0.9.0 svn4400 version

* Sun Jul 06 2014 Motsyo Gennadi <drool@altlinux.ru> 1:0.9.0-alt1.svn4344
- 0.9.0 svn4344 version

* Wed Apr 23 2014 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0.1-alt2.svn4266
- 0.8.0 svn4266 version

* Fri Mar 21 2014 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0.1-alt2.svn4183
- 0.8.0 svn4183 version

* Fri Jan 17 2014 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0.1-alt2.svn4041
- 0.8.0 svn4041 version

* Wed Dec 25 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0.1-alt2.svn3984
- 0.8.0 svn3984 version

* Sat Dec 07 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0.1-alt2.svn3953
- 0.8.0 svn3953 version

* Sat Nov 23 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0.1-alt2.svn3924
- 0.8.0 svn3924 version

* Thu Nov 14 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0.1-alt2.svn3910
- 0.8.0 svn3910 version

* Wed Nov 13 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0.1-alt2.svn3902
- 0.8.0 svn3902 version

* Thu Nov 07 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3880
- 0.8.0 svn3880 version

* Fri Oct 18 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3815
- 0.8.0 svn3815 version

* Fri Oct 04 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3746
- 0.8.0 svn3746 version

* Fri Sep 06 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3686
- 0.8.0 svn3686 version

* Fri Sep 06 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3683
- 0.8.0 svn3683 version

* Wed Aug 28 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3671
- 0.8.0 svn3671 version

* Mon Aug 26 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3669
- 0.8.0 svn3669 version

* Thu Aug 22 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3647
- 0.8.0 svn3647 version

* Wed Aug 21 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3636
- 0.8.0 svn3636 version

* Tue Aug 20 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3630
- 0.8.0 svn3630 version

* Tue Jul 30 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3564
- 0.8.0 svn3564 version

* Wed Jul 17 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3555
- 0.8.0 svn3555 version

* Mon Jul 15 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3552
- 0.8.0 svn3552 version

* Mon Jul 01 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3528
- 0.8.0 svn3528 version

* Mon May 20 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3479
- 0.8.0 svn3479 version

* Mon May 20 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3478
- 0.8.0 svn3478 version

* Sun May 19 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3477
- 0.8.0 svn3477 version

* Wed May 01 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3440
- 0.8.0 svn3440 version

* Sun Apr 28 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.8.0-alt2.svn3431
- 0.8.0 svn3431 version

* Sun Apr 07 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn3381
- 0.7.0 svn3381 version

* Thu Apr 04 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn3379
- 0.7.0 svn3379 version

* Thu Mar 21 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn3337
- 0.7.0 svn3337 version (fixed opus codec sample rate)

* Mon Mar 18 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn3333
- 0.7.0 svn3333 version

* Sat Mar 16 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn3318
- 0.7.0 svn3318 version

* Fri Mar 01 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn3290
- 0.7.0 svn3290 version

* Thu Feb 14 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn3255
- 0.7.0 svn3255 version

* Tue Feb 12 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn3240
- 0.7.0 svn3240 version

* Wed Jan 16 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn3171
- 0.7.0 svn3171 version

* Tue Jan 15 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn3168
- 0.7.0 svn3168 version

* Thu Jan 03 2013 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn3126
- 0.7.0 svn3126 version

* Tue Dec 18 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn3077
- 0.7.0 svn3077 version

* Sat Dec 15 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn3067.1
- fix buildrequires

* Sat Dec 15 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn3067
- 0.7.0 svn3067 version

* Sun Oct 14 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn2957
- 0.7.0 svn2957 version

* Sun Sep 02 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn2928
- 0.7.0 svn2928 version

* Sat Sep 01 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn2915
- 0.7.0 svn2915 version

* Thu Aug 23 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn2896
- 0.7.0 svn2896 version

* Thu Aug 09 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn2872
- 0.7.0 svn2872 version

* Mon Jul 30 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn2842
- 0.7.0 svn2842 version

* Tue Jul 24 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.7.0-alt2.svn2827
- 0.7.0 svn2827 version

* Thu Jul 12 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt2.svn2793
- 0.6.0 svn2793 version

* Sat Jun 30 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt2
- 0.6.0 released (svn 2762)

* Mon Jun 04 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.4.svn2744
- 0.6.0 svn2744 version

* Mon May 28 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.4.svn2737
- 0.6.0 svn2737 version

* Sat Apr 14 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.4.svn2712
- 0.6.0 svn2712 version

* Sun Mar 18 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.4.svn2686
- 0.6.0 svn2686 version (fixed problem with invalid tracks, issue 528)

* Sat Mar 10 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.4.svn2685
- 0.6.0 svn2685 version

* Fri Feb 17 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.4.svn2613
- 0.6.0 svn2613 version

* Mon Feb 13 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.4.svn2601
- 0.6.0 svn2601 version

* Thu Jan 26 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.4.svn2565
- 0.6.0 svn2565 version

* Thu Jan 19 2012 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.4.svn2553
- 0.6.0 svn2553 version

* Fri Dec 09 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.4.svn2525
- 0.6.0 svn2525 version

* Sun Nov 20 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.4.svn2513
- 0.6.0 svn2513 version

* Thu Nov 10 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.4.svn2505
- 0.6.0 svn2505 version

* Thu Nov 03 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.4.svn2483
- 0.6.0 svn2483 version

* Fri Oct 28 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2455
- 0.6.0 svn2455 version

* Wed Oct 26 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2453
- 0.6.0 svn2453 version

* Sun Oct 23 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2432
- 0.6.0 svn2432 version

* Fri Oct 14 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2400
- 0.6.0 svn2400 version

* Thu Oct 13 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2392
- 0.6.0 svn2392 version

* Mon Oct 03 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2378
- 0.6.0 svn2378 version

* Sun Oct 02 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2369
- 0.6.0 svn2369 version

* Wed Sep 21 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2358
- 0.6.0 svn2358 version

* Sun Sep 18 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2356
- 0.6.0 svn2356 version

* Sat Sep 17 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2353
- 0.6.0 svn2353 version

* Fri Sep 16 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2352
- 0.6.0 svn2352 version

* Thu Sep 08 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2343
- 0.6.0 svn2343 version

* Fri Aug 26 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2318
- 0.6.0 svn2318 version

* Fri Aug 19 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2313
- 0.6.0 svn2313 version

* Thu Aug 04 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2292
- 0.6.0 svn2292 version

* Tue Jul 19 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2282
- 0.6.0 svn2282 version
- cleanup spec

* Tue Jun 28 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2248
- 0.6.0 svn2248 version
- cleanup spec

* Sun May 22 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2219
- 0.6.0 svn2219 version

* Sat May 14 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2198
- 0.6.0 svn2198 version

* Thu May 12 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2188
- 0.6.0 svn2188 version

* Mon May 09 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2181
- 0.6.0 svn2181 version

* Tue Apr 26 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2175
- 0.6.0 svn2175 version

* Sat Apr 16 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2167
- 0.6.0 svn2167 version

* Wed Apr 13 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2162
- 0.6.0 svn2162 version

* Sun Apr 03 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.6.0-alt0.2.svn2150
- 0.6.0 svn2150 version
- change version to 0.6 branch

* Sat Mar 26 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt2
- 0.5.0 release

* Sun Mar 13 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn2125
- 0.5.0 svn2125 version

* Fri Mar 11 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn2120
- 0.5.0 svn2120 version

* Thu Mar 03 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn2090
- 0.5.0 svn2090 version

* Wed Mar 02 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn2079
- 0.5.0 svn2079 version

* Wed Feb 16 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn2057
- 0.5.0 svn2057 version

* Mon Jan 31 2011 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn2029
- 0.5.0 svn2029 version

* Mon Dec 20 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn2016
- 0.5.0 svn2016 version

* Wed Dec 08 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1998
- 0.5.0 svn1998 version (fix build)

* Mon Dec 06 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1997
- 0.5.0 svn1997 version

* Sat Nov 27 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1992
- 0.5.0 svn1992 version

* Fri Nov 19 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1991
- 0.5.0 svn1991 version

* Tue Nov 09 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1985.1
- fix build (libGLU-devel)

* Mon Nov 08 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1985
- 0.5.0 svn1985 version

* Tue Oct 19 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1949
- 0.5.0 svn1949 version

* Wed Oct 13 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1938
- 0.5.0 svn1938 version

* Sat Oct 09 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1936
- 0.5.0 svn1936 version

* Mon Oct 04 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1927
- 0.5.0 svn1927 version

* Thu Sep 30 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1925
- 0.5.0 svn1925 version

* Thu Sep 23 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1909
- 0.5.0 svn1909 version

* Mon Sep 20 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1905
- 0.5.0 svn1905 version

* Fri Sep 17 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1890
- 0.5.0 svn1890 version

* Tue Sep 14 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1886
- 0.5.0 svn1886 version

* Tue Sep 07 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1881
- 0.5.0 svn1881 version

* Wed Aug 25 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1851
- 0.5.0 svn1851 version

* Thu Aug 19 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1834
- 0.5.0 svn1834 version

* Tue Aug 17 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1832
- 0.5.0 svn1832 version

* Fri Aug 13 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1827
- 0.5.0 svn1827 version

* Sat Aug 07 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1825
- 0.5.0 svn1825 version
- rebuild with libwildmidi-0.2.3.4

* Sat Aug 07 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1824
- 0.5.0 svn1824 version

* Fri Aug 06 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1820
- 0.5.0 svn1820 version
  + added MIDI support

* Mon Aug 02 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1817
- 0.5.0 svn1817 version

* Sun Jul 25 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1814
- 0.5.0 svn1814 version

* Thu Jul 22 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1802
- 0.5.0 svn1802 version

* Sun Jul 04 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1799
- 0.5.0 svn1799 version

* Sat Jun 26 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1791
- 0.5.0 svn1791 version

* Sun Jun 13 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.5.0-alt0.2.svn1778
- 0.5.0 svn1778 version
- change version to 0.5 branch

* Sat Jun 12 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.1-alt0.2.svn1775
- 0.4.1 svn1775 version

* Sun Jun 06 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.1-alt0.2.svn1767
- 0.4.1 svn1767 version

* Sat May 29 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.1-alt0.2.svn1754
- 0.4.1 svn1754 version
  + fixed problems with transparency settings (Closes issue 317)

* Sat May 22 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.1-alt0.2.svn1748
- 0.4.1 svn1748 version

* Tue May 18 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.1-alt0.2.svn1741
- 0.4.1 svn1740 version

* Sun May 16 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.1-alt0.2.svn1740
- 0.4.1 svn1740 version
  + added wm detection
  + added tint2/lxpanel support

* Mon May 10 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.1-alt0.2.svn1731
- 0.4.1 svn1731 version

* Sun May 09 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.1-alt0.2.svn1726
- 0.4.1 svn1726 version

* Fri May 07 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.1-alt0.2.svn1722
- 0.4.1 svn1722 version

* Thu May 06 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.1-alt0.2.svn1716
- 0.4.1 svn1716 version

* Sun May 02 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt2
- 0.4.0 released

* Tue Apr 27 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1697
- 0.4 svn1697 version

* Sun Apr 18 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1682
- 0.4 svn1682 version

* Sat Apr 17 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1674
- 0.4 svn1674 version

* Sun Apr 11 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1669
- 0.4 svn1669 version
  + kdenotify plugin: fixed kde 3.3 support (Artur Guzik)

* Fri Apr 09 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1665.1
- build with libprojectM 2.0.1

* Tue Apr 06 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1665
- 0.4 svn1665 version

* Sat Mar 27 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1655
- 0.4 svn1655 version

* Wed Mar 24 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1641
- 0.4 svn1641 version

* Sun Mar 21 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1638
- 0.4 svn1638 version

* Wed Mar 17 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1631
- 0.4 svn1630 version

* Tue Mar 16 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1630
- 0.4 svn1630 version

* Fri Mar 12 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1623
- 0.4 svn1623 version

* Fri Mar 05 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1601
- 0.4 svn1601 version

* Mon Mar 01 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1595
- 0.4 svn1595 version

* Sat Feb 27 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1591
- 0.4 svn1591 version

* Tue Feb 23 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1574
- 0.4 svn1574 version

* Mon Feb 22 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1568
- 0.4 svn1568 version

* Sat Feb 20 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1562
- 0.4 svn1562 version

* Wed Feb 17 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1561
- 0.4 svn1561 version

* Tue Feb 16 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1559
- 0.4 svn1559 version

* Mon Feb 08 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1555
- 0.4 svn1555 version

* Fri Feb 05 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1553
- 0.4 svn1553 version

* Tue Feb 02 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1542
- 0.4 svn1542 version

* Fri Jan 29 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1533
- 0.4 svn1533 version

* Wed Jan 27 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1530
- 0.4 svn1530 version

* Sun Jan 24 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1528
- 0.4 svn1528 version

* Fri Jan 22 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1523
- 0.4 svn1523 version

* Wed Jan 20 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1518
- 0.4 svn1518 version

* Sun Jan 17 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1508
- 0.4 svn1508 version

* Wed Jan 13 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1503
- 0.4 svn1503 version

* Sat Jan 09 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1491
- 0.4 svn1491 version

* Fri Jan 08 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1490
- 0.4 svn1490 version

* Thu Jan 07 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1488
- 0.4 svn1488 version

* Tue Jan 05 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1482
- 0.4 svn1482 version

* Mon Jan 04 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1481
- 0.4 svn1481 version

* Sun Jan 03 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1476
- 0.4 svn1476 version
  + fixed metadata regression

* Sat Jan 02 2010 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1475
- 0.4 svn1475 version

* Thu Dec 31 2009 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1462
- 0.4 svn1462 version

* Mon Dec 28 2009 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1459
- 0.4 svn1459 version

* Mon Dec 21 2009 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1452
- 0.4 svn1452 version

* Mon Dec 21 2009 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1451
- 0.4 svn1451 version
  + fixed track repeat regression

* Fri Dec 18 2009 Motsyo Gennadi <drool@altlinux.ru> 1:0.4.0-alt0.2.svn1449
- 0.4 svn1449 version

* Sun Dec 13 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.2.svn1446
- 0.4 svn1446 version

* Thu Dec 10 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.2.svn1438
- 0.4 svn1438 version

* Tue Dec 08 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.2.svn1430
- 0.4 svn1430 version

* Sun Dec 06 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.2.svn1425
- 0.4 svn1425 version

* Fri Dec 04 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.2.svn1417
- 0.4 svn1417 version

* Tue Dec 01 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.2.svn1414
- 0.4 svn1414 version

* Mon Nov 30 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.2.svn1413
- 0.4 svn1413 version

* Sat Nov 28 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.2.svn1411
- 0.4 svn1411 version

* Thu Nov 26 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.2.svn1410
- 0.4 svn1410 version

* Mon Nov 23 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.2.svn1403
- 0.4 svn1403 version

* Mon Nov 23 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.2.svn1397
- fixed required version libtag >= 1.6 for %name-in-musepack

* Sun Nov 22 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.1.svn1397
- 0.4 svn1397 version

* Sat Nov 21 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.1.svn1395
- 0.4 svn1395 version

* Fri Nov 20 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.1.svn1388
- 0.4 svn1388 version

* Tue Nov 17 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.1.svn1382.1
- rebuild with new libcdio

* Mon Nov 16 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.1.svn1382
- 0.4 svn1382 version

* Sat Nov 14 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.1.svn1372
- 0.4 svn1372 version

* Fri Nov 13 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.1.svn1366
- 0.4 svn1366 version

* Fri Nov 06 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.1.svn1360
- 0.4 svn1360 version

* Mon Nov 02 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.1.svn1353
- 0.4 svn1353 version

* Sat Oct 31 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.1.svn1348
- 0.4 svn1348 version

* Sat Oct 31 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.1.svn1340
- 0.4 svn1340 version

* Thu Oct 22 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.1.svn1335
- 0.4 svn1335 version

* Sat Oct 17 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.1.svn1324
- 0.4 svn1324 version

* Tue Oct 13 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.1.svn1312
- 0.4 svn1312 version
  + added new details dialog, disabled input plugins due api changes
  + notifier: fixed popup widget icon
  + updated Ukrainian translation
  + removed obsolete qt macros, updated Russian translation
  + removed unused files
  + added getcwd portability patch (Pino Toskano)
  + added SALSA/non-Linux compatibility patch (Pino Toskano)
  + fixed desktop file
  + prepare for gapless playback support
  + fixed memory leak
  + fixed some bugs, removed unused code
  + fixed button focus behavior (patch by erlk.ozlr AT gmail.com)
  + fixed cue bug
  + fixed tag refresh
  + fixed notifications
  + fixed regression
  + added transport api, moved http into plugin, fixed problems with cue metadata
  + text scroller: added scrolling with mouse (patch by Erik lsar)
  + removed noise between cue tracks
  + fixed problem with cue parser
  + fixed build
  + fixed cue parsing
  + fixed saving of track
  + fixed cue+flac regression (Fixes issue 169)
  + wavpack plugin: added file size
  + ported ffmpeg plugin (Closes issue 170)
  + some ffmpeg fixes
  + added bitmap text support (thanks to Erik lsar)
  + do not allow main window overlap (patch by majlos88 AT gmail.com)
  + some notifier plugin changes
  + fixed problem with slow visualization
  + added possibility to disable snd_pcm_pause function
  + fixed mp4 aac regression
  + fixed cue playing with '?' in its path
  + fixed locale detection
  + added engine api
  + updated Polish translation (Grzegorz Gibas)
  + clear next url if user presses stop
  + fixed problem with qt 4.6 (Closes issue 179)
  + fixed signal conflict
  + fixed popup widget attributes
  + added some optimizations, removed deprecated functions
  + fixed text scroller bugs
  + fixed build (Closes issue 181)
  + fixed problem with threads
  + fixed bug with calling XGrabKey with zero keycodes
  + notifier plugin: fixed popup widget
  + added APIC frame support, added some api functions
  + mpris plugin: added 'arturl' key
  + changed required taglib version from 1.4 to 1.6

* Thu Sep 10 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.1.svn1193
- 0.4 svn1193 version
  + fixed problems with lyricwiki (Fixes issue 158)
  + fixed uds data receiving
  + updated Lithuanian translation (Algirdas Butkus)
  + fixed desktop file
  + removed broken LyricWiki.org support, added lyricsplugin.com instead
  + fixed typo

* Wed Sep 02 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.0-alt0.1.svn1172
- 0.4 svn1172 version
  + change branch version
  + updated Czech translation (Karel Voln)
  + updated Italian translation (Gian Paolo Renello)
  + some updated Ukrainian translation
  + fixed build (Fixes issue 157)
  + fixed lyrics plugin

* Wed Aug 26 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.1-alt0.1.svn1160.1
- rebuild with libcdio-0.81

* Tue Aug 25 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.1-alt0.1.svn1160
- 0.3 svn1160 version
  + updated Polish translation (Gregorz Gibas)
  + updated German translation (Stefan Koelling)
  + updated German translation (Panagiotis Papadopoulos)
  + fixed translation strings (Panagiotis Papadopoulos)
  + updated Czech translation (Karel Voln)
  + updated Ukrainian translation
  + fixed freezes with jack
  + fixed cue parsing, fixed jack
  + fixed cue parsing
  + fixed translatble strings

* Mon Aug 17 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.1-alt0.1.svn1146
- 0.3 svn1146 version
  + fixed default font
  + notifier plugin: added font and cover size settings
  + fixed details dialog layout
  + updated Ukrainian translation

* Sat Aug 15 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.1-alt0.1.svn1140
- 0.3 svn1140 version
  + hide cover widget if cover pixmap is not available
  + notifier plugin: added cover support

* Wed Aug 12 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.1-alt0.1.svn1138
- 0.3 svn1138 version
  + fixed cover support
  + added cover support api
  + fixed seeking

* Sun Aug 09 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.1-alt0.1.svn1135
- 0.3 svn1135 version
  + added unified dialog api
  + updated Russian translation
  + added support for additional tags
  + fixed title format
  + changed details dialog layout
  + hotkey plugin: added volume control
  + mpeg plugin: added support for comment and disc number tags
  + flac plugin: added support for composer and disc number tags
  + flac plugin: fixed metadata reading
  + vorbis plugin: added support for composer and disc number tags
  + some details dialog fixes
  + ffmpeg plugin: added unified details dialog
  + wavpack plugin: added support for composer and disc number tags
  + mpc plugin: added composer tag support
  + fixed build
  + added partial cover support
  + hotkey plugin: fixed bug with capslock
  + updated and fixed Ukrainian translation

* Wed Aug 05 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.1-alt0.1.svn1110
- 0.3 svn1110 version
  + fixed problem with lyricwiki
  + updated *.ts files
  + updated Ukrainian translation

* Tue Aug 04 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.1-alt0.1.svn1105
- 0.3 svn1105 version
  + fixed problem with qt4.4
  + updated Turkish translation (Bilgesu Gngr)

* Sun Aug 02 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.1-alt0.1.svn1101
- 0.3 svn1101 version
  + updated German translation (Panagiotis Papadopoulos)
  + fixed typo
  + added Kazakh translation (Baurzhan Muftakhidinov)
  + fixed build
  + fixed cache scrobbling
  + status icon plugin: added standard icons support
  + updated Ukrainian translation
  + mpeg decoder: do not send empty metadata
  + some state handler fixes
  + new decoder api, disabled broken plugins
  + fixed installation
  + updated Russian translation
  + ported musepack plugin
  + fixed regression
  + added cygwin patches (yselkowitz AT gmail.com)
  + ported cue plugin
  + improved cue support (very unstable)
  + fixed sorting by name
  + fixed cue support
  + enabled flac plugin
  + enabled mplayer support, added mkv extension
  + added Home/End hotkeys
  + added 'show song numbers' option
  + updated Chinese Traditional and Chinese Simplified translations (lon)
  + mpeg plugin: fixed problem with small files
  + flac plugin: fixed cue support
  + removed unused code
  + enabled sndfile plugin
  + enabled wavpack plugin, fixed problem with slow seeking
  + enabled modplug plugin
  + added shift modifier for home/end hotkeys
  + enabled ffmpeg plugin
  + new ffmpeg support
  + ported aac plugin
  + ported cd audio plugin
  + mpeg plugin: show mpeg version
  + fixed build under debian(closes issue 135)
  + updated Turkish translation (author: Bilgesu Gngr)
  + added patch which allows to load plugins form a different location (Holger Schurig)
  + fixed previous patch
  + added Lithuanian translation (author: Algirdas Butkus)
  + updated translators list
  + updated *.ts files
  + alsa plugin: fixed settings dialog layout
  + mpeg plugin: fixed regression
  + added 'remove invalid files' action'
  + fixed playlist menu
  + mpeg plugin: changed detailes dialog
  + added partial cover support
  + some details dialog improvements
  + fixed problems with openbox (closes issue 141)
  + added openbox compatibility option
  + added form of the unified details dialog

* Sat Jul 04 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt1
- 0.3.0 release

* Mon Jun 29 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn987
- 0.3 svn987 version
  + some fileops plugin improvements
  + updated changelog

* Sun Jun 28 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn984
- 0.3 svn984 version
  + fixed fileops plugin
  + fileops plugin: do not convert spaces to '_'

* Sat Jun 27 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn982
- 0.3 svn982 version
  + fixed typo
  + ported oss plugin
  + fixed build with oss4
  + fixed pulse audio support
  + improved audio output
  + ported jack plugin

* Sun Jun 21 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn975
- 0.3 svn975 version
  + added library suffix autodetection

* Sat Jun 20 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn974
- 0.3 svn974 version
  + fixed audio skipping when using soft volume

* Tue Jun 16 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn973
- 0.3 svn973 version
  + added debug message
  + fixed skin parsing

* Sun Jun 14 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn971
- 0.3 svn971 version
  + fixed some debug messages
  + fixed audio distortion in the end of file

* Sat Jun 13 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn969
- 0.3 svn969 version
  + clear queue with playlist

* Thu Jun 11 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn968
- 0.3 svn968 version
  + scorbbler plugin: fixed problem with tags that contain the & sign
  + updated documentation
  + fixed typo

* Tue Jun 09 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn964
- 0.3 svn964 version
  + lyrics plugin: fixed window flags

* Mon Jun 08 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn963
- 0.3 svn963 version
  + fixed text scroller and window titles

* Sun Jun 07 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn962.1
- rebuild with libbs2b-3.1.0

* Sun May 31 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn962
- 0.3 svn962 version
  + updated German translation (Panagiotis Papadopoulos)
  + updated Polish translation (Gregorz Gibas)
  + fixed: adding streams from command line
  + notifier plugin: fixed notification window position

* Sat May 30 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn958
- 0.3 svn958 version
  + improved scrobbler plugin, fixed libre.fm support
  + fixed config dialog layout
  + updated Ukrainian translation

* Fri May 29 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn954
- 0.3 svn954 version
  + fixed language detection

* Mon May 18 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn953
- 0.3 svn953 version
  + libre.fm support
  + fixed translation list
  + fixed plugins page size in the config dialog (patch by Panagiotis Papadopoulos)
  + updated Ukrainian translation

* Fri May 15 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn949
- 0.3 svn949 version
  + removed dublicate files
  + fixed build

* Tue May 12 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn947
- 0.3 svn947 version
  + fixed segmentation fault when resume playback with empty playlist
  + added Italian translation (author: Gian Paolo)
  + wavpack plugin: improved total time calculation

* Tue May 12 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn944
- 0.3 svn944 version
  + lyrics plugin: added hotkey
  + enabled file operations plugin
  + file operations: fixed settings
  + fixed wavpack with embedded cue support
  + fixed Russian translation
  + fixed skin path
  + updated Ukrainian translation for fileops plugin
  + fixed build with Qt4.4

* Sun May 10 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn935
- 0.3 svn935 version
  + updated fileops plugin, fixed file dialog bugs

* Fri May 08 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn934
- 0.3 svn934 version
  + fixed m4a support with enabled aac plugin

* Fri May 08 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn933
- 0.3 svn933 version
  + fixed bs2b build

* Mon May 04 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn932
- 0.3 svn932 version
  + fixed about dialog layout (patch by Panagiotis Papadopoulos)
  + fixed m4a support

* Sun May 03 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn930
- 0.3 svn930 version
  + added cue with several files support
  + creating file operations plugin structure
  + fixed cue regression
  + fixed ffmpeg plugin bugs

* Sat May 02 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn926
- 0.3 svn926 version
  + fixed build
  + improved config dialog
  + pulse audio plugin: 32-bit samples support
  + fixed Russian translation
- fixed not owned by any package directoryes

* Thu Apr 30 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn922
- 0.3 svn922 version
  + fixed playing cue files with symbol '#' in the path
  + fixed documentation
- added russian description

* Wed Apr 29 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn920
- 0.3 svn920 version
  + fixed scrobbler plugin regression

* Wed Apr 29 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn918
- 0.3 svn918 version
  + scrobbler: added offline mode
  + increased uds data size

* Tue Apr 21 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn916
- 0.3 svn916 version
  + fixed gnome support

* Sun Apr 19 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn915
- 0.3 svn915 version
  + qmmp file dialog: fixed sorting
  + fixed build with Qt-4.3
  + fixed build
  + updated German translation (Panagiotis Papadopoulos)

* Wed Apr 15 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn911
- 0.3 svn911 version
  + added wave output plugin (only M$-Windows)
  + alsa plugin: show more debug info
  + fixed skin path for windows
  + fixed main window flags
  + fixed now-playing notification for flac and wavpack files with embeded cue
  + added waveout plugin translation
  + updated documentation
  + fixed build
  + fixed typo

* Fri Apr 10 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn901
- 0.3 svn901 version
  + partial mingw support
  + fixed build using cmake < 2.6.2

* Thu Apr 09 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn899
- 0.3 svn899 version
  + updated bs2b plugin, removed libbs2b-2.x support
  + some alsa fixes
  + fixed build
  + updated Ukrainian translation

* Tue Apr 07 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn894
- 0.3 svn894 version
  + prepare for ms windows support

* Sun Apr 05 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn893
- 0.3 svn893 version
  + libbs2b 3.0.0 support
  + scrobbler plugin: fixed now-playing notification

* Sat Apr 04 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn891
- 0.3 svn891 version
  + updated Polish translation (Grzegorz Gibas)
  + updated Russian translation
  + alsa plugin: added hard restart

* Wed Apr 01 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn887
- 0.3 svn887 version
  + some core fixes and improvements

* Sat Mar 28 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn886
- 0.3 svn886 version
  + fixed default font
  + fixed clicked item calculation
  + fixed selected item calculation

* Fri Mar 27 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn883
- 0.3 svn883 version
  + fixed command line regression

* Thu Mar 26 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn880
- 0.3 svn880 version
  + fixed desktop file
  + fixed alsa buffer underrun

* Tue Mar 24 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn878
- 0.3 svn878 version
  + added Ukrainian translation to qmmp_cue.desktop file
  + faster mp3 seeking

* Mon Mar 23 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn876
- 0.3 svn876 version
  + added qmmp_enqueue.desktop file, added 'inode/directory' mimetype
  + fixed directory adding bug
  + play cue in directories
  + removed unused code

* Sun Mar 22 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn870
- 0.3 svn870 version
  + some hotkey fixes
  + updated desktop file
  + moved phonon to qmmp plugin pack

* Sun Mar 22 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn865
- 0.3 svn865 version
  + musepack sv8 support

* Thu Mar 19 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn863
- 0.3 svn863 version
  + updated German translation (Panagiotis Papadopoulos)
  + fixed SRC plugin regression, increased buffer size
  + some api fixes

* Wed Mar 18 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn860
- 0.3 svn860 version
  + updated devel files list
  + fixed content type detection
  + fixed 'jumping windows' bug

* Mon Mar 16 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn857
- 0.3 svn857 version
  + fixed bug: qmmp continues current track instead of loading new one
  + fixed cue regression
  + fixed regression

* Sun Mar 15 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn854
- 0.3 svn854 version
  + aac plugin fixes, updated Russian translation
  + updated Ukrainian translation

* Sat Mar 14 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn852
- 0.3 svn852 version
  + PlayListModel class documentation
  + command line api documentation
  + file dialog plugin api documentation
  + general plugin api documentation
  + playlist format api documentation
  + decoder api documentation
  + effect plugin api documentation
  + output and visual api documentation
  + SoundCore class documentation, fixed other documentation
  + fixed build regression
  + fixed typo
  + some api fixes
- add docs package

* Wed Mar 11 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn839
- 0.3 svn839 version
  + added tooltips
  + updated Ukrainian translation
  + fixed Russian translation
  + mplayer plugin: added auto synchronization option

* Mon Mar 09 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn835
- 0.3 svn835 version
  + some api changes
  + fixed pulse audio bug

* Sun Mar 08 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn833
- 0.3 svn833 version
  + removed unused code
  + updated logo

* Sun Mar 08 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn832
- 0.3 svn832 version
  + improved seeking accuracy
  + fixed regression
  + fixed build

* Sat Mar 07 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn827
- 0.3 svn827 version
  + fixed version
- update BuildRequires

* Fri Mar 06 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn826
- 0.3 svn826 version
  + playlist api changes and optimizations
  + mplayer settings
  + fixed ffmpeg regression
  + updated Ukrainian translation

* Thu Mar 05 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn822
- 0.3 svn822 version
  + added item skip limit
  + fixed time indicator blinking

* Thu Mar 05 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn820
- 0.3 svn820 version
  + fixed typo (thanks to Sebastian Pipping)
  + updated Ukrainian translation

* Sun Mar 01 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn816
- 0.3 svn816 version
  + old ffmpeg support (Sergey Dryabzhinsky)
  + fixed bs2b plugin bug (thanks to Sebastian Pipping)

* Sun Mar 01 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn814
- 0.3 svn814 version
  + enapled projectM plugin
  + updated Ukrainian translation (projectM)

* Sat Feb 28 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn812
- 0.3 svn812 version
  + updated bs2b plugin. Now it uses updated bs2b library and enabled by default
  + updated Czech translation (Karel Voln)
  + updated Ukrainian translation (BS2B Plugin)

* Wed Feb 25 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn808
- 0.3 svn808 version
  + uploaded fixed oss plugin from branch
  + added projectm visual plugin (not ready yet)

* Tue Feb 24 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn805
- 0.3 svn805 version
  + fixed Czech translation (Tomas Chvatal), fixed build
  + updated German translation (Panagiotis Papadopoulos)
  + fixed Russian translation
  + fixed invalid file handling

* Thu Feb 19 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn799
- 0.3 svn799 version
  + removed useless option
  + fixed embedded cue encoding
  + improved lyrics plugin
  + updated Ukrainian translation

* Tue Feb 17 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn794
- 0.3 svn794 version
  + fixed proxy support, fixed xspf version
  + libqmmp: allow config path override
  + fixed regression
  + fixed url dialog bug

* Sat Feb 14 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn790
- 0.3 svn790 version
  + some qmmp launcher improvements (Sebastian Pipping)
  + qt-4.5 fixes
  + global hotkey support
  + mplayer plugin: 3gp and flv extensions
  + updated Ukrainian translation (Global Hotkey Plugin)

* Mon Feb 09 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn784
- 0.3 svn784 version
  + updated German translation (Panagiotis Papadopoulos)
  + fixed xspf format support (thanks to Sebastian Pipping)

* Sat Feb 07 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn781
- 0.3 svn781 version
  + wavpack embeded cue support (thanks to Dmitry Kostin)

* Fri Feb 06 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn779
- 0.3 svn779 version
  + fixed build
  + fixed aac build
  + aac plugin: debian support

* Thu Feb 05 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn776
- 0.3 svn776 version
  + fixed large playlist downloading

* Mon Feb 02 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn774
- 0.3 svn774 version
  + mad plugin: skip ID3v2 tag
  + fixed segmentation fault

* Sat Jan 31 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn770
- 0.3 svn770 version
  + fixed main window title
- removed prescripts for new skindir workaround (#18695)

* Fri Jan 30 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn769
- 0.3 svn769 version
  + some hal plugin improvements, updated Russian translation
  + updated readme files
  + fixed typo
  + updated Ukrainian translation
- updated description from README file

* Thu Jan 29 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn764
- 0.3 svn764 version
  + removable devices support
  + fixed Russian translation
  + updated Ukrainian translation

* Sat Jan 24 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn761
- 0.3 svn761 version
  + cd audio plugin: url syntax changes
  + hal support (experimental)
  + show genre for streams
  + some general api changes
  + fixed build with --as-needed linking flag
  + some skin fixes
  + updated Russian translation
  + updated and fixed Ukrainian translation

* Thu Jan 22 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn751
- 0.3 svn751 version
  + mp3 support by ffmpeg plugin (Csaba Hrushka)
  + updated Ukrainian translation
  + updated German translation (Panagiotis Papadopoulos)
  + fixed build with qt-4.3

* Thu Jan 15 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn747
- 0.3 svn747 version
  + lyrics plugin
  + updated Ukrainian translation (lyrics plugin)

* Wed Jan 14 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn745
- 0.3 svn745 version
  + fixed playlist actions
  + some menu improvements

* Tue Jan 13 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn743
- 0.3 svn743 version
  + fixed division by zero
  + menu support
  + updated Ukrainian translation

* Tue Jan 06 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn740
- 0.3 svn740 version
  + fixed bug in volume control

* Mon Jan 05 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn739
- 0.3 svn739 version
  + cd audio plugin
  + cda plugin: show metadata
  + updated Russian translation
  + updated and fixed Ukrainian translation
  + short command line keys
  + fixed xspf parsing

* Sun Jan 04 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn732
- 0.3 svn732 version
  + updated German translation (Panagiotis Papadopoulos)
  + fixed Ukrainian translation
  + fixed file filters
  + fixed scrobbler settings
  + fixed plugins short name

* Thu Jan 01 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn727
- 0.3 svn727 version
  + fixed list widget
  + added mplayer and phonon plugins
  + enabled mplayer support
  + mplayer plugin: added details dialog and Russsian translation
  + fixed mplayer plugin dialog title
  + updated Ukrainian translation (mplayer plugin)

* Mon Dec 29 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn721
- 0.3 svn721 version
  + settings dialog: fixed selection
  + added application name; removed unused debug message

* Sun Dec 28 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn719
- 0.3 svn719 version
  + notification plugin: volume change notification, transparency settings
  + added transparency options
  + updated Russian translation
  + updated Ukrainian translation
  + fixed typo
  + status icon: fixed state tracking; notifier plugin: show test message
  + fixed comments

* Fri Dec 26 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn712
- 0.3 svn712 version
  + show version with svn revision
  + mpris plugin: fixed player name
  + updated German translation (Panagiotis Papadopoulos)
  + scrobbler plugin: now-playing notification support, new api support
  + cue plugin: added Russian translation; ffmepg plugin: fixed widgets layout
  + fixed build with using qmake (--as-needed)
  + added Ukrainian translation for CUE plugin
  + fixed build
- fix conflicts folder vs symlink
- rename %name-devel to lib%name-devel
- moved *.so to new subpackage lib%name-devel

* Wed Dec 24 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn704
- 0.3 svn704 version
  + full mpris support; new options: "repeat track", "show protocol"
  + fixed sorting by track and year
  + updated Russian translation
  + updated Ukrainian translation
  + global config file path

* Sun Dec 21 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn698
- 0.3 svn698 version
  + more mpris methods support

* Sat Dec 20 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn697
- 0.3 svn697 version
  + ffmpeg fixes

* Fri Dec 19 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn696
- 0.3 svn696 version
  + more ffmpeg formats support (including ape); ffmpeg plugin settings
  + some ffmpeg plugin fixes
  + fixed ffmpeg plugin build
  + faster ape seeking
- removed patch for ape support (upstream now supported)

* Wed Dec 17 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn692
- 0.3 svn692 version
  + improved equalizer precision
  + using standard dialog buttons
  + fixed dialog layouts

* Tue Dec 16 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn688
- 0.3 svn688 version
  + equalizer: overwrite existing presets
  + added some mpris methods

* Mon Dec 15 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn685
- 0.3 svn685 version
  + fixed linker flags
  + mediplayer class, enabled all statusicon actions
  + removed unused debug messages
  + better mpris support
  + fixed regression

* Sun Dec 14 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn680
- 0.3 svn680 version
  + moved playlist model to libqmmpui
- ape support enabled (experimental)

* Fri Dec 12 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn679
- 0.3 svn679 version
  + fixed playlists load with --enqueue option
  + status icon plugin: mouse wheel volume control

* Thu Dec 11 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn677
- 0.3 svn677 version
  + skin installation dialog
  + --enqueue command line option

* Mon Dec 08 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn674
- 0.3 svn674 version
  + fixed some midi bugs
  + moved midi plugin to plugin pack

* Sun Dec 07 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn672
- fix allocation skinsdir for winamplike-skins
- 0.3 svn672 version
  + fixed qmake scripts
  + fixed effect plugin table
  + fixed typo
  + fixed sliders
  + updated changelog
  + updated Czech translation
  + fixed build
  + midi plugin

* Mon Dec 01 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn649
- 0.3 svn649 version
  + fixed shaded playlist title

* Sat Nov 29 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn647
- 0.3 svn647 version
  + fixed next/previous command in pause mode
  + fixed cue parsing
  + flac plugin: embeded cue support (using cuesheet xiph comment)
  + changed decoder api; fixed flac plugin
  + general api changes, removed unused code
  + removed unused code
- removed libqt3-devel from BuildRequires

* Wed Nov 26 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn640
- 0.3 svn640 version
  + some mpris plugin improvements
  + fixed Russian translation (MPRIS plugin)
  + fixed command line plugin
- refresh BuildRequires

* Wed Nov 26 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn637
- 0.3 svn637 version
  + fixed regression
  + partial mpris support, removed dbus plugin
  + added mpris plugin translations
  + fixed Ukrainian translation (MPRIS Plugin)
  + fix link (--as-needed) for notifier plugin

* Tue Nov 25 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn631
- 0.3 svn631 version
  + show notification for all files
  + notifier plugin: show duration of the cue tracks
  + fixed notification bug
  + general api cleanup

* Sun Nov 23 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn626
- 0.3 svn626 version
  + fixed possible freeze
  + fixed notifier duration bug
  + removed unused code

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn623
- 0.3 svn623 version
  + fixed build
  + output api changes
  + make visualization independent of the software volume level

* Mon Nov 17 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn619
- 0.3 svn619 version
  + added enter hotkey support in the jump dialog
- remove post/postun scripts (new rpm)

* Thu Nov 13 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn615
- 0.3 svn615 version
  + fixed shaded playlist title
  + fixed modplug defines

* Mon Nov 10 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn610
- 0.3 svn610 version
  + gcc-4.3 support

* Sat Nov 01 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn609
- 0.3 svn609 version
  + AAC plugin: added details dialog
  + fixed out-of-source build

* Fri Oct 31 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn606
- 0.3 svn606 version
  + enabled aac plugin
  + AAC plugin: fixed seeking; id3v2 tags support

* Sun Oct 26 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn604
- 0.3 svn604 version
  + fixed desktop file regression
  + fixed playlist parsing
  + some playlist fixes
  + fixed some event-handling bugs
  + fixed equalizer
  + cue plugin: equalizer support
  + send buffering state befor playing
  + fixed regression
  + aac plugin
  + clear visualization after stop, fixed possible flickering
  + removed unused debug message

* Sun Oct 19 2008 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt0.1.svn589
- initial build 0.3 branch for ALT Linux

* Sun Oct 19 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2.2.1-alt0.1.svn590
- 0.2 svn590 version
  + fixed program exit with enabled visualization
- fixed desktop file (repocop warning)

* Thu Oct 16 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2.2.1-alt0.1.svn586
- 0.2 svn586 version
  + fixed playlist loading when using drag and drop and command line
  + fixed build

* Fri Sep 26 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2.2.1-alt0.1.svn564
- 0.2 svn564 version
  + fixed russian translation
  + added French translation (author: Stanislas Zeller)
  + updated translators list
  + jack plugin: do not try to connect to MIDI ports (Adrian Knoth)
  + fixed memory leak

* Tue Sep 09 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2.2.1-alt0.1.svn545
- 0.2 svn545 version
  + kde4-like library suffix (Funda Wang)
  + new ffmpeg support
  + removed duplicate --next command line option (thanks to Adrian Knoth)
  + rebuilt translations

* Sat Aug 30 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2.2-alt1
- 0.2.2 release

* Sat Aug 30 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2.1.1-alt0.1.svn525
- 0.2 svn525 version
  + fixed UDS datagram encoding

* Tue Aug 26 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2.1.1-alt0.1.svn523
- 0.2 svn523 version
  + added Polish translation (author: Grzegorz Gibas)
  + fixed build
  + make alsa plugin optional
  + fixed compile warnings
  + some jack fixes
  + removed unused code
  + fixed Russian translation

* Sun Aug 17 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2.1-alt2
- fix Ukrainian translation

* Fri Aug 15 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2.1-alt1
- 0.2.1
  + fixed desktop file;
  + fixed build;
  + fixed bugs in the file dialog;
  + fixed margins;
  + updated Chezh translation;
  + middle mouse button click on the tray icon works as the play/pause command;
  + fixed memory leak;
  + fixed skin parsing;
  + increased file dialog speed;
  + improved accuracy of the mp3 duration calculation;
  + added preamp support in the the modplug plugin
- add %name-full package

* Tue Jul 22 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2.0-alt2
- 0.2.0 release
- updated description

* Tue Jul 22 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn469
- 0.2 svn469 version
  + devel files installation
  + fixed build
  + updated description
  + fixed changelog

* Mon Jul 21 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn462
- 0.2 svn462 version
  + 24-bit support
  + fixed and updated Russian translation

* Sat Jul 19 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn459
- 0.2 svn459 version
  + updated German translation (author: Stefan Koelling)
  + fixed memory leak
  + optimized alsa output

* Sat Jul 12 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn456
- 0.2 svn456 version
  + fixed build
  + fixed visualization

* Fri Jul 11 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn453
- 0.2 svn453 version
  + updated Chinese Simplified and Chinese Traditional translations (author: lon)
  + notifier: fixed popu message
  + some file dialog fixes

* Thu Jul 10 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn450
- 0.2 svn450 version
  + completed file dialog support
  + fixed translation
  + updated and fixed Ukrainian translation
  + updated Russian translation
  + fixed build
  + fixed bug in the file dialog

* Mon Jul 07 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn442
- 0.2 svn442 version
  + full proxy support
  + fixed software volume

* Sun Jul 06 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn440
- 0.2 svn440 version
  + fixed status icon message

* Sat Jul 05 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn439
- 0.2 svn439 version
  + updated Ukrainian translation

* Sat Jul 05 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn438
- 0.2 svn438 version
  + updated Ukrainian translation
  + updated Chinese Simplified and Chinese Traditional translations
  + fixed visualization disabling
  + improved text scroller
  + updated Russian translation
  + fixed text scroller string
  + fixed build

* Wed Jun 25 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn431
- 0.2 svn431 version
  + alsa plugin: mmap access support

* Sun Jun 22 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn430
- 0.2 svn430 version
  + fixed Russian translation

* Sat Jun 21 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn429
- 0.2 svn429 version
  + fixed qmmp file dialog

* Thu Jun 19 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn428
- 0.2 svn428 version
  + enabled qmmp file dialog

* Tue Jun 17 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn427
- 0.2 svn427 version
  + fixed build message
  + updated Chinese Traditional Translation (author: lon)
  + fixed critical bug which causes crash
  + added distclean target

* Mon Jun 16 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn423
- 0.2 svn423 version
  + added uninstall target for cmake
  + fixed Ukrainian translation
  + fixed build

* Sun Jun 15 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn420
- 0.2 svn420 version
  + generate *.qm files by build scripts
  + removed unused files

* Sun Jun 15 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn418
- 0.2 svn418 version
  + updated Ukrainian translation (in upstream)
  + updated Russian translation

* Sun Jun 15 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn416uk
- 0.2 svn416 version
  + fixed visualization blink
- updated Ukrainian translation (uk)

* Sat Jun 14 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn415
- 0.2 svn415 version
  + fixed qmake scripts
  + updated Russian translation
  + updated Chinese Simplified Translation (author: lon)
  + updated Chinese Traditional Translation (author: lon)
  + fixed build
  + fixed typo
  + updated Russian translation
  + fixed Russian translation

* Thu Jun 12 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn406
- 0.2 svn406 version
  + moved queue action
  + fixed typo
  + some settings dialog changes

* Thu Jun 12 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn403
- 0.2 svn403 version
  + show metadata for streams

* Wed Jun 11 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn402
- 0.2 svn402 version
  + fixed qmake scripts
  + some visualization fixes
  + enabled command line plugins support
  + updated translation
- remove libqt3-devel from BuildRequires

* Wed Jun 04 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn398
- 0.2 svn398 version
  + moved playlist formats support to plugins
  + fixed playlist dialog default path

* Mon Jun 02 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn396
- 0.2 svn396 version
  + fixed Alt+F4 closing

* Sun Jun 01 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn395
- 0.2 svn395 version
  + removed unused files
- run clear_cmake.sh script before building

* Sun Jun 01 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn394
- 0.2 svn394 version
  + added username to the socket name (thanks to Karel Volny)
  + changed socket error message
  + added PlayListItem class, removed MediaFile
  + more playlist options
  + visualization: transparent background option
  + fixed cmake build progress (thanks to Ken Martin)
  + fixed crash

* Mon May 26 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn385
- 0.2 svn385 version
  + stream reader: play stream buffer after disconnect
  + id3v2 support for streams
  + fixed build

* Thu May 22 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn382
- 0.2 svn382 version
  + some alsa fixes
  + fixed build (thanks to Karel Volny)
- enable verbose mode for building

* Tue May 20 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn380
- 0.2 svn380 version
  + fixed qmake scripts
  + clear text scroller before playing
  + updated German translation (author: Stefan Koelling)
  + fixed build

* Sun May 18 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn375
- 0.2 svn375 version
  + flac plugin: fixed cmake script

* Sun May 18 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn374
- 0.2 svn374 version
  + cmake 2.6 support

* Fri May 16 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn373
- 0.2 svn373 version
  + improved cmake scripts

* Thu May 15 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn372
- 0.2 svn372 version
  + fixed localization support
  + updated *.qm files
  + updated Chezh translation (author: Karel Volny)

* Tue May 13 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn369
- 0.2 svn369 version
  + modplug plugin: some settings dialog changes
  + modplug plugin: some ui fixes
- fixed unpackaged directory (new sisyphus_check)

* Fri May 09 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn367
- 0.2 svn367 version
  + added *.ts files

* Thu May 08 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn366
- 0.2 svn366 version
  + display buffering progress

* Tue May 06 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn365
- 0.2 svn365 version
  + fixed segmentation fault while changing visualization (qt 4.4 issue)
  + fixed pulse audio build message
  + FFMEG plugin: fixed build again

* Mon May 05 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn362
- 0.2 svn362 version
  + fixed possible segmentation fault

* Sun May 04 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn361
- 0.2 svn361 version
  + ffmpeg plugin: fixed build scripts (thanks to Stefan Koelling)
  + fixed skin parsing

* Thu May 01 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn357
- 0.2 svn357 version
  + some cmake cleanup
  + improved build scripts
  + fixed translators list

* Mon Apr 28 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn354
- 0.2 svn354 version
  + notifier plugin: fixed layout

* Wed Apr 23 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn352
- 0.2 svn352 version
  + play file if it was added from command line

* Tue Apr 22 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn350
- 0.2 svn350 version
  + modplug plugin: fixed it, mod, stm, s3m support

* Tue Apr 22 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn349
- 0.2 svn349 version
  + fixed modplug window title
  + added modplug support

* Sun Apr 20 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn347
- 0.2 svn347 version
  + fixed playlist format parsing
- separate various plugins to subpackage
- added unzip to requires (for zip packed skins support)

* Fri Apr 11 2008 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt0.1.svn338
- 0.2 svn338 version
  + mp3 wave support
  + Analyzer plugin: fixed build
  * required cmake >= 2.4.8

* Mon Apr 07 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Fri Apr 04 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1.5.1-alt5.svn329
- new svn version
  + grey out configuration button if a plugin has no settings
  + fixed regression
  + use qt translations
- refresh BuildRequires

* Wed Apr 02 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1.5.1-alt4.svn297
- fix desktop-mime-entry

* Fri Mar 28 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1.5.1-alt3.svn297
- new svn version
  + show more debug info
  + updated changelog
  + fixed typo
  + fixed loading playlists with double extensions
  + fixed scroller text color
  + some id3v1/v2 fixes
  + *.tar.bz2 skins support
  + fixed GPL violation

* Tue Mar 25 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1.5.1-alt2.svn226
- rebuild with new libqt4

* Sat Mar 08 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1.5.1-alt1.svn226
- rebuild with new libffmpeg

* Mon Feb 25 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1.5.1-alt0.svn226
- new svn version
  + fixed skin parsing

* Thu Jan 24 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1.5.1-alt0.svn223
- new svn version
  + added 'share/qmmp/skins' to skin search path

* Thu Jan 17 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1.5-alt2
- cleanup spec
- fix cmake build

* Sat Dec 08 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.5-alt1
- 0.1.5
- use cmake
- add icons

* Sat Sep 15 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.4-alt2
- fix deskciption - packed skins now supported

* Sun Sep 09 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.4-alt1
- new version

* Wed Aug 29 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.3.2-alt0.svn126.1
- fix categories in desktop file

* Fri Aug 24 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.3.2-alt0.svn126
- new svn version (special building for current song saving)

* Tue Jul 31 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.3.1-alt1
- hotfix version (bug with dir for libqmmp.so*)

* Mon Jul 30 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.3-alt1
- release
- fix patch0 for release

* Sun Jul 22 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.3-alt0.svn29.1
- fix for x86_64 (thanks Led for help)

* Sat Jul 21 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.3-alt0.svn29
- initial build for Sisyphus

* Mon Jul 16 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.3-alt0.svn29.M40.1
- new svn snapshot
- add desktop file
- trivial fix patch0

* Thu Jun 21 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.2-alt0.M40.1
- new version
- build for M40
- fix patch0 for 0.1.2
- fix optflags (thanx to Ilya <forkotov02 at hotmail dot ru>

* Sat Jun 02 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.1-alt0.M24.1
- 0.1.1

* Tue May 29 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt0.M24.1
- test build for ALM2.4
