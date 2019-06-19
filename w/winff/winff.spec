Name: winff
Version: 1.5.5
Release: alt3.20171210
Summary: A cross platform batch GUI for FFmpeg
Summary(ru_RU.UTF-8): Кроссплатформенный графический интерфейс для FFmpeg
License: GPLv3
Group: Video
Url: http://winff.org
Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar
Source1: winff.desktop
BuildRequires: lazarus desktop-file-utils dos2unix
Requires: ffmpeg
Requires: ffplay
Requires: xterm

# Lazarus not allowed for aarch64
ExcludeArch: aarch64

%description
WinFF is a GUI for the command line video converter FFMPEG or fork Libav.
It will convert most any video file that FFmpeg or fork Libav will convert.
WinFF does multiple files in multiple formats at one time.
You can for example convert mpeg's, flv's, and mov's
all into avi's all at once.

%description -l ru_RU.UTF-8
WinFF представляет собой графический интерфейс для консольного видео-конвертора
FFMPEG или его форк LibAV. Позволяет конвертивровать видео во все форматы, в
которые поддерживает FFMPEG или его форк LibAV.
WinFF может одновременно конвертировать видео в разные форматы.

%prep
%setup
dos2unix *.txt
chmod 644 *.txt docs/*.pdf docs/*.odg docs/*.odt docs/*.txt winff-icons/*.txt

%build
lazbuild \
	--lazarusdir=%_libdir/lazarus \
	--widgetset=gtk2 \
	-B winff.lpr

%install
install -D -m755 winff %buildroot/%_bindir/winff
install -D -m644 %SOURCE1 %buildroot/%_desktopdir/winff.desktop
install -D -m644 presets.xml %buildroot/%_datadir/winff/presets.xml
install -d -m755 %buildroot%_datadir/winff/languages/
install -m644 languages/*.po %buildroot/%_datadir/winff/languages/
install -d -m755 %buildroot/%_mandir/man1/
install -m644 winff.1 %buildroot/%_mandir/man1/
install -d -m755 %buildroot/%_iconsdir/hicolor
for i in 16 24 32 48; do
  install -d -m755 %buildroot/%_iconsdir/hicolor/"$i"x"$i"/apps
  install -m644 winff-icons/"$i"x"$i"/*.png %buildroot/%_iconsdir/hicolor/"$i"x"$i"/apps
done
mkdir -p %buildroot/%_docdir/%name
install -m644 -t %buildroot/%_docdir/%name AUTHORS *.txt docs/*.pdf docs/*.odg docs/*.odt docs/*.txt winff-icons/*.txt

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/%name
%_mandir/man1/*
%_docdir/%name

%changelog
* Wed Jun 19 2019 Anton Midyukov <antohami@altlinux.org> 1.5.5-alt3.20171210
- Cleanup ubt
- exclude aarch64

* Fri Jan 19 2018 Anton Midyukov <antohami@altlinux.org> 1.5.5-alt2.20171210%ubt
- New snapshot

* Tue Jun 06 2017 Anton Midyukov <antohami@altlinux.org> 1.5.5-alt1
- Remove requires avplay, avconv. Added requires ffmpeg, xterm.
- Remove patch's.

* Mon Jun 20 2016 Anton Midyukov <antohami@altlinux.org> 1.5.3-alt2
- Fixed select the target architecture

* Sun Jun 05 2016 Anton Midyukov <antohami@altlinux.org> 1.5.3-alt1
- New version 1.5.3
- Disable winff-presets.patch.

* Mon Aug 24 2015 Anton Midyukov <antohami@altlinux.org> 1.5.2-alt1
- Initial build for ALT Linux Sisyphus (Closes: 31217).
