Name: libmediainfo
Version: 19.09
Release: alt1

Group: System/Libraries
Summary: %name - Shared library for mediainfo
License: LGPL
Url: http://mediainfo.sourceforge.net

Source: https://mediaarea.net/download/source/%name/%version/%{name}_%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: dos2unix
BuildRequires: doxygen graphviz
BuildRequires: zlib-devel
BuildRequires: id3lib-devel
BuildRequires: libflac-devel
BuildRequires: libmatroska-devel
BuildRequires: libfaad-devel
BuildRequires: libzen-devel >= 0.4.37
BuildRequires: libcurl-devel
BuildRequires: libmms-devel
BuildRequires: libtinyxml2-devel

%package devel
Group: System/Libraries
Summary: Devel package for %name
Requires: %name = %version
Provides: %name.so

%description
MediaInfo supplies technical and tag information about a video or audio file.
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

This package includes the shared library

%description devel
This package includes the development support files of the libmediainfo

%prep
%setup -q -T -b 0 -n MediaInfoLib
dos2unix ReadMe.txt Project/GNU/Library/%name.pc.in

%build
pushd Source/Doc
doxygen Doxyfile
popd
pushd Project/GNU/Library
%autoreconf
%configure --enable-shared=yes \
    --enable-static=no \
    --disable-staticlibs \
    --with-libcurl=system \
    --with-libmms=system \
    --with-libtinyxml2=system
%make_build
popd

%install
pushd Project/GNU/Library
%makeinstall_std
popd

%files
%doc ReadMe.txt
%_libdir/%name.so.*

%files devel
%_includedir/MediaInfo/
%_includedir/MediaInfoDLL/
%_pkgconfigdir/%name.pc
%_libdir/%name.so

%changelog
* Thu Sep 12 2019 Yuri N. Sedunov <aris@altlinux.org> 19.09-alt1
- 19.09

* Wed Jul 17 2019 Yuri N. Sedunov <aris@altlinux.org> 19.07-alt1
- 19.07

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

* Sat Nov 04 2017 Yuri N. Sedunov <aris@altlinux.org> 17.10-alt1
- 17.10

* Mon Sep 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.99-alt1
- 0.7.99

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
- Add libmms test build support

* Sat Dec 03 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.51-alt1
- New version

* Thu Jul 21 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.47-alt1
- New version

* Sun Mar 06 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.42-alt1
- New version

* Mon Feb 28 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.41-alt1
- New version

* Mon Oct 18 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.35-alt1
- New version

* Tue Mar 02 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.28-alt4
- Rebuild

* Tue Mar 02 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.28-alt3
- Remove libmms support due to continious error in libmms

* Tue Mar 02 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.28-alt2
- Add libmms support

* Tue Mar 02 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.28-alt1
- New version

* Mon Nov 23 2009 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.25-alt1
- New version

* Thu Nov 12 2009 Sergei Epiphanov <serpiph@altlinux.ru> 0.7.24-alt1
- initial build
