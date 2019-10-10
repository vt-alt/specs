
%define sover 1
%define libqmmp libqmmp%sover
%define libqmmpui libqmmpui%sover

%define rname qmmp
Name: qmmp1
Version: 1.3.4
Release: alt1

Group: Sound
Summary: Qmmp - Qt-based multimedia player
Summary(ru_RU.UTF8): Qmmp - мультимедиа проигрыватель на базе Qt
Summary(uk_UA.UTF8): Qmmp - мультимедіа програвач на базі Qt
Url: http://qmmp.ylsoftware.com/
License: GPLv2

Provides: qmmp = %version-%release
Conflicts: qmmp < 1:0.12.0-alt0.M80P.svn8288.1
Conflicts: qmmp-docs < 1:0.12.0-alt0.M80P.svn8288.1 qmmp-qsui < 1:0.12.0-alt0.M80P.svn8288.1

Requires: unzip winamplike-skins

Source: %rname-%version.tar
Patch2: alt-def-plugins.patch
Patch3: alt-def-statusicon.patch
Patch4: alt-hide-on-close.patch
Patch5: alt-def-id3v1-encoding.patch

# Automatically added by buildreq on Tue Apr 26 2016 (-bi)
# optimized out: cmake-modules elfutils gcc-c++ glib2-devel libEGL-devel libGL-devel libX11-devel libavcodec-devel libavutil-devel libcdio-devel libcdio-paranoia libgpg-error libjson-c libogg-devel libopencore-amrnb0 libopencore-amrwb0 libopus-devel libp11-kit libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-widgets libqt5-x11extras libqt5-xml libsndfile-devel libstdc++-devel perl pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-tools rpm-build-python3 ruby ruby-stdlibs xorg-kbproto-devel xorg-xproto-devel
#BuildRequires: cmake doxygen libalsa-devel libavformat-devel libbs2b-devel libcddb-devel libcdio-paranoia-devel libcurl-devel libenca-devel libfaad-devel libflac-devel libgme-devel libjack-devel libmad-devel libmms-devel libmodplug-devel libmpcdec-devel libopusfile-devel libprojectM-devel libpulseaudio-devel libsamplerate-devel libsidplayfp-devel libtag-devel libvorbis-devel libwavpack-devel libwildmidi-devel python-module-google python3-dev qt5-tools-devel qt5-x11extras-devel rpm-build-ruby
BuildRequires(pre): kde-common-devel rpm-build-ubt rpm-build-wlskins
BuildRequires: cmake doxygen qt5-tools-devel qt5-x11extras-devel
BuildRequires: libmms-devel libprojectM-devel libtag-devel
BuildRequires: libalsa-devel libjack-devel libpulseaudio-devel qt5-multimedia-devel
BuildRequires: libbs2b-devel libcddb-devel libcdio-paranoia-devel libcurl-devel libenca-devel
BuildRequires: libavformat-devel libwildmidi-devel
BuildRequires: libfaad-devel libflac-devel libgme-devel libopusfile-devel libsamplerate-devel libsoxr-devel
BuildRequires: libmad-devel libmpg123-devel
BuildRequires: libmodplug-devel libmpcdec-devel libvorbis-devel libwavpack-devel
#BuildRequires: libshout2-devel
#BuildRequires: libarchive-devel
#BuildRequires: libsidplayfp-devel

%description
Qmmp is an audio-player, written with help of Qt library.
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

%package devel
Summary: Qmmp header files
Group: Development/C++
Provides: qmmp-devel = %version-%release libqmmp-devel = %version-%release
Conflicts: qmmp-devel < 1:0.12.0-alt0.M80P.svn8288.1 libqmmp-devel < 1:0.12.0-alt0.M80P.svn8288.1
%description devel
%name-devel contains the header files needed to develop
programs which make use of Qmmp.

%package -n %libqmmp
Summary: Qmmp library
Group: System/Libraries
%description -n %libqmmp
Qmmp Shared library

%package -n %libqmmpui
Summary: Qmmp library
Group: System/Libraries
%description -n %libqmmpui
Qmmp Shared library

%prep
%setup -qn %rname-%version
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%Kbuild \
    -DQMMP_DEFAULT_OUTPUT=pulse \
    -DQMMP_DEFAULT_UI=qsui \
    #
cd doc && doxygen Doxyfile

%install
%Kinstall

mkdir -p %buildroot/%_datadir/%rname
ln -s `relative %_wlskindir %_datadir/%rname/skins` %buildroot/%_datadir/%rname/skins

%files
%doc AUTHORS ChangeLog* README* doc/html
%_bindir/%{rname}*
%_libdir/%{rname}-?.*/
%_desktopdir/%{rname}*.desktop
%_datadir/%rname/
%_iconsdir/hicolor/*/apps/%{rname}*.*
%_datadir/metainfo/*qmmp*.appdata.xml

%files -n %libqmmp
%_libdir/libqmmp.so.%sover
%_libdir/libqmmp.so.%sover.*

%files -n %libqmmpui
%_libdir/libqmmpui.so.%sover
%_libdir/libqmmpui.so.%sover.*

%files devel
%_includedir/%{rname}*
%_pkgconfigdir/%{rname}*.pc
%_libdir/lib*.so

%changelog
* Wed Oct 09 2019 Sergey V Turchin <zerg@altlinux.org> 1.3.4-alt1
- new version

* Fri Jul 12 2019 Sergey V Turchin <zerg@altlinux.org> 1.3.3-alt1
- new version

* Thu Jan 10 2019 Sergey V Turchin <zerg@altlinux.org> 1.2.6-alt1
- new version

* Tue Nov 13 2018 Sergey V Turchin <zerg@altlinux.org> 1.2.4-alt1
- new version

* Fri Sep 21 2018 Sergey V Turchin <zerg@altlinux.org> 1.2.3-alt2%ubt
- resolve conflicts with current qmmp

* Wed Sep 19 2018 Sergey V Turchin <zerg@altlinux.org> 1.2.3-alt1%ubt
- new version

* Fri Jun 15 2018 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt1%ubt
- new version

* Fri Jan 12 2018 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt2%ubt
- rebuild with new libcdio

* Mon Nov 27 2017 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt1%ubt
- new version

* Thu Oct 26 2017 Sergey V Turchin <zerg@altlinux.org> 1.1.12-alt1%ubt
- new version

* Tue Sep 19 2017 Sergey V Turchin <zerg@altlinux.org> 1.1.10-alt2%ubt
- build without libsidplayfp

* Mon Sep 18 2017 Sergey V Turchin <zerg@altlinux.org> 1.1.10-alt1%ubt
- new version

* Tue Jun 06 2017 Sergey V Turchin <zerg@altlinux.org> 1.1.9-alt1%ubt
- new version

* Mon Feb 13 2017 Sergey V Turchin <zerg@altlinux.org> 1.1.7-alt1%ubt
- new version

* Fri Jan 27 2017 Sergey V Turchin <zerg@altlinux.org> 1.1.6-alt1%ubt
- new version

* Tue Oct 04 2016 Sergey V Turchin <zerg@altlinux.org> 1.1.4-alt1
- new version

* Wed Sep 07 2016 Sergey V Turchin <zerg@altlinux.org> 1.1.3-alt1
- new version

* Thu Jul 28 2016 Sergey V Turchin <zerg@altlinux.org> 1.1.2-alt1
- new version

* Fri Jul 22 2016 Sergey V Turchin <zerg@altlinux.org> 1.1.1-alt1
- new version

* Tue Jun 28 2016 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt1
- new version

* Fri May 20 2016 Sergey V Turchin <zerg@altlinux.org> 1.0.9-alt2
- hide to tray on close by default
- use standart icons for statusicon

* Mon May 16 2016 Sergey V Turchin <zerg@altlinux.org> 1.0.9-alt1
- new version

* Tue Apr 26 2016 Sergey V Turchin <zerg@altlinux.org> 1.0.7-alt1
- initial build
