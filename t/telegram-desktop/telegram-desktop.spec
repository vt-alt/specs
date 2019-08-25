# other variant: Debug
%define buildmode Release

%define ffmpeg_version 3.4
%def_without ffmpeg_static

# Precompiled supports only for gcc now
%def_without clang
%def_without libcxx

Name: telegram-desktop
Version: 1.8.2
Release: alt1

Summary: Telegram is a messaging app with a focus on speed and security

License: %gpl3only
Group: Networking/Instant messaging
Url: https://telegram.org/

# Source-url: https://github.com/telegramdesktop/tdesktop/archive/v%version.tar.gz
Source: %name-%version.tar

Source2: CMakeLists.txt
Source3: gen_source_list.sh

Patch1: 0001_add-cmake.patch
Patch3: 0003_qt-plugins.patch
Patch5: 0005_Downgrade-Qt-version.patch
Patch6: 0006_fix-static-qt-functions.patch
#Patch9: 0001-use-correct-executable-path.patch
Patch15: 0015-disable-resource-fonts.patch
Patch16: 0016-fix-lzma.patch
#Patch17: 0017-ligsl-microsoft-fix.patch
Patch18: 0018-fix-linking.patch

# ix86 disabled due to memory limits for linker
#ExclusiveArch: %ix86 x86_64
ExclusiveArch: aarch64 x86_64

BuildRequires(pre): rpm-build-licenses rpm-macros-qt5 rpm-macros-cmake
BuildRequires(pre): rpm-macros-kde-common-devel

BuildRequires(pre): rpm-build-compat >= 2.1.5
BuildRequires(pre): rpm-build-intro >= 2.1.5
# use no more than system_memory/3000 build procs (see https://bugzilla.altlinux.org/show_bug.cgi?id=35112)
%_tune_parallel_build_by_procsize 3000

BuildRequires: gcc-c++ libstdc++-devel gyp

# cmake 3.13 due to add_compiler_definitions
BuildRequires: cmake >= 3.13

BuildRequires: qt5-base-devel libqt5-core libqt5-network libqt5-gui qt5-imageformats
# needs for smiles and emojicons
Requires: qt5-imageformats

# for -lQt5PlatformSupport
BuildRequires: qt5-base-devel-static

# for autoupdater (included ever if disabled)
BuildRequires: liblzma-devel

# for SourceFiles/mtproto/connection.cpp
BuildRequires: libzip-devel

BuildRequires: zlib-devel >= 1.2.8

BuildRequires: libminizip-devel libpcre-devel libexpat-devel libssl-devel bison
#BuildRequires: libxkbcommon-devel libxkbcommon-x11-devel
#BuildRequires: libXi-devel libSM-devel libICE-devel libdbus-devel libXfixes-devel
BuildRequires: libX11-devel

# GTK 3.0 integration
BuildRequires: libgtk+3-devel libappindicator-gtk3-devel
# TODO:
# libdee-devel

BuildRequires: libopenal-devel >= 1.17.2
# libportaudio2-devel libxcb-devel 
# used by qt imageformats: libwebp-devel
BuildRequires: libva-devel libdrm-devel

# libs from Telegram project
BuildRequires: libtgvoip-devel >= 2.4.4
BuildRequires: libcrl-devel >= 0.9

BuildRequires: libxxhash-devel

BuildRequires: librlottie-devel >= 0.0.1
BuildRequires: liblz4-devel

# C++ sugar
BuildRequires: libmicrosoft-gsl-devel >= 20180615
BuildRequires: libvariant-devel
BuildRequires: librange-v3-devel >= 0.5.0

# FIXME: libva need only for linking, extra deps?

Provides: tdesktop = %version-%release
Obsoletes: tdesktop

%if_with ffmpeg_static
BuildRequires: libffmpeg-devel-static >= %ffmpeg_version
%else
BuildRequires: libavcodec-devel >= %ffmpeg_version
BuildRequires: libavformat-devel >= %ffmpeg_version
BuildRequires: libavutil-devel >= %ffmpeg_version
BuildRequires: libswscale-devel >= %ffmpeg_version
BuildRequires: libswresample-devel >= %ffmpeg_version
%endif

%if_with clang
BuildRequires: clang
%remove_optflags -frecord-gcc-switches
%endif
%if_with libcxx
%add_optflags -stdlib=libc++
%endif

Requires: dbus

# instead of internal fonts OpenSans
Requires: fonts-ttf-open-sans

# some problems with t_assert
%add_optflags -fpermissive

# disable some warnings
%add_optflags -Wno-strict-aliasing -Wno-unused-variable -Wno-sign-compare -Wno-switch

%description
Telegram is a messaging app with a focus on speed and security, it's super-fast, simple and free.
You can use Telegram on all your devices at the same time - your messages
sync seamlessly across any number of your phones, tablets or computers.

With Telegram, you can send messages, photos, videos and files of any type (doc, zip, mp3, etc),
as well as create groups for up to 1000 people or channels for broadcasting to unlimited audiences.
You can write to your phone contacts and find people by their usernames.
As a result, Telegram is like SMS and email combined - and can take care of all your personal
or business messaging needs.


%prep
%setup
%patch1 -p1
%patch3 -p1
#patch5 -p1
%patch6 -p1
#patch9 -p1
%patch15 -p1
#patch17 -p2
%patch18 -p2

cp %SOURCE2 Telegram/
cp %SOURCE3 .
./gen_source_list.sh
# MacOS things will conflicts with binary name, so delete Telegram dir
rm -rf Telegram/Telegram/
# remove fonts from resources
rm -rf Telegram/Resources/fonts/
%__subst "s|.*fonts/OpenSans.*||" Telegram/Resources/qrc/telegram.qrc

%build
%if_with ffmpeg_static
export PKG_CONFIG_PATH=%_libdir/ffmpeg-static/%_lib/pkgconfig/
%endif
cd Telegram
%if_with clang
export CC=clang
export CXX=clang++
%endif
%cmake_insource \
%if_with libcxx
    -DLLVM_ENABLE_LIBCXX=ON
%else
    %nil
%endif
# due precompiled headers
export CCACHE_SLOPPINESS=pch_defines,time_macros
%make_build

%install
# XDG files
install -m644 -D lib/xdg/telegramdesktop.desktop %buildroot%_desktopdir/%name.desktop
install -m644 -D lib/xdg/tg.protocol %buildroot%_Kservices/tg.protocol
install -m644 -D lib/xdg/telegramdesktop.appdata.xml %buildroot%_datadir/appdata/telegram-desktop.appdata.xml
for i in 16 32 48 64 128 256; do
    install -m644 -D Telegram/Resources/art/icon$i.png %buildroot%_iconsdir/hicolor/${i}x${i}/apps/telegram.png
done

#cd out/%buildmode
install -D Telegram/Telegram %buildroot%_bindir/%name
ln -s %name %buildroot%_bindir/Telegram
ln -s %name %buildroot%_bindir/telegram

%files
%_bindir/%name
%_bindir/Telegram
%_bindir/telegram
%_desktopdir/%name.desktop
%_Kservices/tg.protocol
%_datadir/appdata/%name.appdata.xml
%_iconsdir/hicolor/16x16/apps/telegram.png
%_iconsdir/hicolor/32x32/apps/telegram.png
%_iconsdir/hicolor/48x48/apps/telegram.png
%_iconsdir/hicolor/64x64/apps/telegram.png
%_iconsdir/hicolor/128x128/apps/telegram.png
%_iconsdir/hicolor/256x256/apps/telegram.png
#_man1dir/*
%doc README.md

%changelog
* Thu Aug 22 2019 Vitaly Lipatov <lav@altlinux.ru> 1.8.2-alt1
- new version 1.8.2 (with rpmrb script)

* Tue Aug 13 2019 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- new version 1.8.1 (with rpmrb script)

* Fri Aug 09 2019 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)

* Sat Jul 13 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.14-alt3
- use official fix: Use private Qt color API only in official build

* Thu Jul 11 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.14-alt2
- reenable GTK file chooser possibility:
  - drop TDESKTOP_DISABLE_GTK_INTEGRATION
  - add  TDESKTOP_FORCE_GTK_FILE_DIALOG

* Tue Jul 09 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.14-alt1
- new version (1.7.14) with rpmgs script
- fix build with current Qt (thanks, arseerfc@)

* Sun Jul 07 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.13-alt1
- new version 1.7.13 (with rpmrb script)
- use external librlottie instead of internal qtlottie

* Thu Jun 27 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.10-alt1
- new version 1.7.10 (with rpmrb script)

* Mon Jun 24 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.9-alt1
- new version 1.7.9 (with rpmrb script)

* Tue Jun 11 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.7-alt1
- new version 1.7.7 (with rpmrb script)

* Sun Jun 02 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.3-alt1
- new version 1.7.3 (with rpmrb script) (ALT bug 36838)

* Sun May 12 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- new version 1.7.0 (with rpmrb script)

* Thu Apr 18 2019 Vitaly Lipatov <lav@altlinux.ru> 1.6.7-alt1
- new version 1.6.7 (with rpmrb script)

* Wed Mar 27 2019 Vitaly Lipatov <lav@altlinux.ru> 1.6.3-alt1
- new version (1.6.3) with rpmgs script

* Sat Feb 23 2019 Vitaly Lipatov <lav@altlinux.ru> 1.5.15-alt1
- new version 1.5.15 (with rpmrb script)

* Tue Feb 05 2019 Vitaly Lipatov <lav@altlinux.ru> 1.5.11-alt1
- new version 1.5.11 (with rpmrb script)

* Fri Feb 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1.5.10-alt1
- new version 1.5.10 (with rpmrb script)

* Wed Jan 16 2019 Vitaly Lipatov <lav@altlinux.ru> 1.5.7-alt2
- enable build on aarch64
- add fonts-ttf-open-sans require and drop OpenSans from resources
- drop external locales patches

* Mon Jan 14 2019 Vitaly Lipatov <lav@altlinux.ru> 1.5.7-alt1
- new version 1.5.7 (with rpmrb script)

* Mon Dec 31 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5.6-alt1
- new version 1.5.6 (with rpmrb script)

* Tue Dec 25 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt2
- fix registration process (set correct api_id and api_hash)

* Mon Dec 24 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt1
- new version 1.5.4 (with rpmrb script)

* Sun Dec 16 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- new version 1.5.2 (with rpmrb script)

* Tue Dec 11 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- new version (1.5.1) with rpmgs script
- disable build on i586

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 1.4.8-alt1
- new version 1.4.8 (with rpmrb script)

* Sat Sep 29 2018 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version (1.4.0) with rpmgs script

* Sat Sep 08 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.16-alt1
- new version (1.3.16) with rpmgs script
 + Update libtgvoip, fix crash in calls.
 + Improved local caching for images and GIF animations.
 + Control how much disk space is used by the cache
   and for how long the cached files are stored.

* Tue Aug 28 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.14-alt1
- new version 1.3.14 (with rpmrb script)

* Thu Aug 23 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.12-alt1
- new version 1.3.12 (with rpmrb script)

* Sat Jul 14 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.10-alt1
- new version 1.3.10 (with rpmrb script)

* Sat Jul 14 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.9-alt2
- restrict __nprocs with _tune_parallel_build_by_procsize
- drop libpixman-devel buildreq

* Tue Jul 10 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.9-alt1
- new version 1.3.9 (with rpmrb script)

* Mon Jun 25 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.8-alt1
- new version 1.3.8 (with rpmrb script)

* Thu Jun 14 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.7-alt1
- new version 1.3.7 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.5-alt1
- new version 1.3.5 (with rpmrb script)

* Fri Jun 01 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Sat May 26 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2.23-alt1
- new version 1.2.23 (with rpmrb script)

* Thu Feb 22 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2.8-alt1
- new version (1.2.8) with rpmgs script

* Thu Dec 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Sun Dec 03 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.26-alt1
- new version 1.1.26 (with rpmrb script)

* Thu Nov 30 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.24-alt1
- new version 1.1.24 (with rpmrb script)
- build with librange-v3-include
- disable GTK integration (ALT bug 34182)

* Sat Oct 21 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.23-alt3
- fix old lang code in settings
- fix CVE-2016-10351: Insecure cWorkingDir permissions
- sync CMakeLists.txt with Gentoo, fix build with new Qt 5.9.2

* Fri Sep 29 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.23-alt2
- add support for build with static ffmpeg

* Sat Sep 23 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.23-alt1
- new version 1.1.23 (with rpmrb script)
- add qt5-imageformats (fixes missed smiles and emojicons)

* Wed Aug 02 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.19-alt1
- new version 1.1.19 (with rpmrb script)

* Sun Jul 30 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.18-alt1
- new version 1.1.18 (with rpmrb script)
- update translations

* Sun Jul 23 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt2
- cleanup build requires (drop opus, pulseaudio, webp, xcb, exif, X*)

* Fri Jul 21 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt1
- new version 1.1.14 (with rpmrb script)
- build with custom API ID
- update translations
- language list now downloading from cloud

* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.7-alt2
- use correct executable path (fix restart)
- open localized FAQ for ru/uk/be
- get initial language name and country name from QLocale
- fix crash in video player seeking (66662e02a)

* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.7-alt1
- new version (1.1.7) with rpmgs script

* Thu May 18 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.19-alt5
- add /usr/bin/telegram-desktop, fix icons name (ALT bug #33001)

* Fri Dec 23 2016 Vitaly Lipatov <lav@altlinux.ru> 0.10.19-alt4
- get language name and country name from QLocale
- disable user desktop file generation
- fix hack for restart via Updater, use direct /usr/bin path

* Wed Dec 21 2016 Vitaly Lipatov <lav@altlinux.ru> 0.10.19-alt3
- add Belarusian Russian Ukrainian French Turkish Czech languages

* Mon Dec 19 2016 Vitaly Lipatov <lav@altlinux.ru> 0.10.19-alt2
- add desktop file, icons
- cleanup spec

* Sat Dec 17 2016 Vitaly Lipatov <lav@altlinux.ru> 0.10.19-alt1
- new version 0.10.19 (with rpmrb script)

* Sun Dec 20 2015 Hihin Ruslan <ruslandh@altlinux.ru> 0.9.15-alt1
- initial build for ALT Linux Sisyphus
