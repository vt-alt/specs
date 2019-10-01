%def_disable kde4

Name: mediainfo
Version: 19.09
Release: alt1

Group: File tools
Summary: MediaInfo supplies information about a video or audio file
License: LGPL
Url: http://mediainfo.sourceforge.net

Source: https://mediaarea.net/download/source/%name/%version/%{name}_%{version}.tar.xz

Requires: lib%name >= %version

%{?_enable_kde4:BuildRequires(pre): rpm-macros-kde-common-devel}
BuildRequires(pre): rpm-build-kf5

BuildRequires: gcc-c++
BuildRequires: dos2unix
BuildRequires: zlib-devel
BuildRequires: libpango-devel
BuildRequires: libzen-devel >= 0.4.37
BuildRequires: libmediainfo-devel >= %version
BuildRequires: libwxGTK-devel
BuildRequires: sgml-common

%description
MediaInfo supplies technical and tag information about a video or audio file

What information can I get from MediaInfo?
General: title, author, director, album, track number, date, duration...
Video: codec, aspect, fps, bitrate...
Audio: codec, sample rate, channels, language, bitrate...
Text: language of subtitle
Chapters: number of chapters, list of chapters

What format (container) does MediaInfo support?
Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1, MPEG-2,
       MPEG-4, DVD (VOB)...
(Codecs: DivX, XviD, MSMPEG4, ASP, H.264, AVC...)
Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF...
Subtitles: SRT, SSA, ASS, SAMI...

This package includes the command line interface

%package gui
Group: File tools
Summary: MediaInfo supplies information about a video or audio file
Requires: lib%name >= %version

%description gui
MediaInfo supplies technical and tag information about a video or audio file

What information can I get from MediaInfo?
General: title, author, director, album, track number, date, duration...
Video: codec, aspect, fps, bitrate...
Audio: codec, sample rate, channels, language, bitrate...
Text: language of subtitle
Chapters: number of chapters, list of chapters

What format (container) does MediaInfo support?
Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1, MPEG-2,
       MPEG-4, DVD (VOB)...
(Codecs: DivX, XviD, MSMPEG4, ASP, H.264, AVC...)
Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF...
Subtitles: SRT, SSA, ASS, SAMI...

This package contains the graphical user interface.

%if_enabled kde4
%package gui-KDE4
Group: File tools
Summary: KDE4 related MediaInfo files
BuildArch: noarch
Requires: %name-gui = %version-%release
Requires: kde4libs

%description gui-KDE4
This package contains KDE4 related MediaInfo files for konqueror
%endif

%package gui-KDE5
Group: File tools
Summary: KDE5 related MediaInfo files
BuildArch: noarch
Requires: %name-gui = %version-%release

%description gui-KDE5
This package contains KDE5 related MediaInfo files

%prep
%setup -q -T -b 0 -n MediaInfo

%build
pushd Project/GNU/CLI
%autoreconf
%configure --disable-staticlibs --with-dll
%make_build
popd
pushd Project/GNU/GUI
%autoreconf
%configure --disable-staticlibs --with-dll
%make_build
popd

%install
pushd Project/GNU/CLI
%makeinstall_std
popd
pushd Project/GNU/GUI
%makeinstall_std
popd
# Add here commands to install the package
cp Release/ReadMe_CLI_Linux.txt .
cp Release/ReadMe_GUI_Linux.txt .

install -m 644 Source/Resource/Image/MediaInfo.png %buildroot%_pixmapsdir/mediainfo.png
install -dm 755 %buildroot%_liconsdir
install -m 644 Source/Resource/Image/MediaInfo.png %buildroot%_liconsdir/mediainfo.png

%if_enabled kde4
install -dm 755 %buildroot%_K4srv/ServiceMenus/
grep -v '^Encoding=' Project/GNU/GUI/mediainfo-gui.kde4.desktop >%buildroot%_K4srv/ServiceMenus/mediainfo-gui.desktop
%else
rm -f %buildroot%_datadir/kde4/services/ServiceMenus/mediainfo-gui.desktop
%endif

%files
%doc ReadMe_CLI_Linux.txt
%_bindir/%name

%files gui
%doc ReadMe_GUI_Linux.txt
%_bindir/%name-gui
%_desktopdir/%name-gui.desktop
%_datadir/metainfo/%name-gui.metainfo.xml
%_datadir/apps/konqueror/servicemenus/%name-gui.desktop
%_iconsdir/hicolor/*x*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_pixmapsdir/%name.xpm
%_pixmapsdir/%name.png

%if_enabled kde4
%files gui-KDE4
%_K4srv/ServiceMenus/%name-gui.desktop
%endif

%files gui-KDE5
%_K5srv/ServiceMenus/%name-gui.desktop

%changelog
* Thu Sep 12 2019 Yuri N. Sedunov <aris@altlinux.org> 19.09-alt1
- 19.09

* Wed Jul 17 2019 Yuri N. Sedunov <aris@altlinux.org> 19.07-alt1
- 19.07

* Thu Apr 25 2019 Yuri N. Sedunov <aris@altlinux.org> 19.04-alt1.1
- enabled SMP build
- disabled gui-KDE4 subpackage by default

* Wed Apr 24 2019 Yuri N. Sedunov <aris@altlinux.org> 19.04-alt1
- 19.04

* Sun Dec 23 2018 Yuri N. Sedunov <aris@altlinux.org> 18.12-alt1
- 18.12

* Sat Sep 15 2018 Yuri N. Sedunov <aris@altlinux.org> 18.08.1-alt1
- 18.08.1

* Sun Sep 02 2018 Yuri N. Sedunov <aris@altlinux.org> 18.08-alt1
- 18.08

* Fri May 11 2018 Yuri N. Sedunov <aris@altlinux.org> 18.05-alt1
- 18.05

* Tue Mar 27 2018 Yuri N. Sedunov <aris@altlinux.org> 18.03.1-alt1
- 18.03.1

* Tue Mar 20 2018 Yuri N. Sedunov <aris@altlinux.org> 18.03-alt1
- 18.03

* Thu Dec 28 2017 Yuri N. Sedunov <aris@altlinux.org> 17.12-alt1
- 17.12
- new gui-KDE5 subpackage

* Sat Nov 04 2017 Yuri N. Sedunov <aris@altlinux.org> 17.10-alt1
- 17.10

* Wed Sep 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.99-alt2
- removed obsolete gui-KDE3 subpackage

* Mon Sep 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.99-alt1
- 0.7.99

* Fri Sep 01 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.98-alt2
- fixed dependencies (ALT #33839)

* Tue Aug 22 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.98-alt1
- 0.7.98

* Sat Jul 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.97-alt1
- 0.7.97

* Sun Jun 04 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.96-alt1
- 0.7.96

* Sun May 07 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.95-alt1
- 0.7.95

* Tue Apr 04 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.94-alt1
- 0.7.94

* Tue Aug 25 2015 Motsyo Gennadi <drool@altlinux.ru> 0.7.76-alt1
- 0.7.76

* Wed Oct 01 2014 Motsyo Gennadi <drool@altlinux.ru> 0.7.70-alt1
- 0.7.70

* Sat Feb 18 2012 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.53-alt1
- New version

* Sun Dec 04 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.51-alt2
- Fix build spec

* Sun Dec 04 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.51-alt1
- New version

* Thu Jul 21 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.47-alt1
- New version

* Mon Mar 07 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.42-alt2
- Update spec with noarch and K3/K4 macros

* Sun Mar 06 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.42-alt1
- New version

* Mon Feb 28 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.41-alt1
- New version

* Mon Oct 18 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.35-alt1
- New version

* Tue Mar 02 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.28-alt1
- New version

* Wed Feb 17 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.27-alt2
- Rebuild with libwxGTK
- Fix .destop files due to repocop info

* Wed Feb 10 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.27-alt1
- New version

* Mon Nov 23 2009 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.25-alt1
- New version
- create KDE3 and KDE4 subpackages from mediainfo-gui

* Thu Nov 12 2009 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.24-alt1
- initial build
