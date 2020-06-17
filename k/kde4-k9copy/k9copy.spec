
%define rname k9copy
Name: kde4-%rname
Version: 2.3.8
Release: alt10

Group: Video
Summary: Copy, split and shrink DVDs
Summary(ru_RU.UTF8): Копирование, разделение и уменьшение DVD-дисков
License: GPL
Url: http://k9copy.sourceforge.net

Requires: dvdauthor dvd+rw-tools mencoder phonon-backend
Provides: %rname = %version-%release
Obsoletes: k9copy < %version-%release

Source: %rname-%version.tar
# Debian
Patch1: fix-deprecated-func.patch
Patch2: fix-ftbfs-kfreebsd.patch
Patch3: german-spelling-error.patch
Patch4: fix-desktop-files.patch
Patch5: link_libav_directly.patch
Patch6: link_libdvd_directly.patch
# ALT
Patch100: alt-libav9.patch
Patch101: alt-libav10.patch
Patch102: alt-findexe.patch
Patch103: alt-gcc6.patch
Patch104: alt-ffmpeg3.patch

# Automatically added by buildreq on Mon Jul 20 2009 (-bi)
#BuildRequires: gcc-c++ kde4libs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libavformat-devel libmpeg2-devel libqt3-devel libswscale-devel libxine-devel libxkbfile-devel xorg-xf86vidmodeproto-devel
BuildRequires: kde4libs-devel
BuildRequires: gcc-c++ libavformat-devel libmpeg2-devel libswscale-devel libxine2-devel libdvdread-devel libdvdnav-devel


%description
K9Copy is a small utility which allows the copy of DVD on Linux.
The DVD video stream is compressed by the program Vamps. 

Copy without menus :
 In this case, dvdauthor is used to create a new DVD structure.
 It is possible to choose the order in which the video sequences are played. 

Copy with menus :
 As dvdauthor does not make it possible to integrate the original menus,
 K9Copy reproduces the original structure of the DVD. The navigation packs
 as well as IFO files are modified to point on the compressed MPEG stream.

%description -l ru_RU.UTF8
K9Copy - маленькая программа для копирования DVD в Linux.
Видео поток DVD сжимается с помощью программы Vamps.

Копирование без меню:
 В этом случае dvdauthor используется для создания новой структуры DVD.
 Возможно выбирать порядок, в котором видео фрагменты будут воспроизводиться.

Копирование с меню:
 Посколько dvdauthor не позволяет интегрировать оригинальное меню,
 K9Copy воспроизводит оригинальную структуру DVD. Навигационные пакеты, так же как
 и IFO файлы модифицируются для указания мест в сжатом MPEG потоке.


%prep
%setup -q -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1

%build
%K4build


%install
%K4install
%K4find_lang --with-kde %rname

%files -f %rname.lang
%doc README
%_K4bindir/*
%_K4xdg_apps/*
%_K4iconsdir/hicolor/*/apps/%rname.*
%_K4apps/%rname
%_K4apps/solid/actions/%{rname}*.desktop


%changelog
* Wed Apr 22 2020 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt10
- fix requires

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 2.3.8-alt9
- NMU: remove %ubt from release

* Thu Jun 14 2018 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt8
- rebuild with new ffmpeg

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt7
- fix to build with ffmpeg

* Mon Jan 30 2017 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt6
- fix for gcc6

* Fri Apr 10 2015 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt5
- rebuild with new libav

* Tue May 27 2014 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt4
- built with libxine2

* Tue May 27 2014 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt3
- fix to build with libav10

* Thu Nov 28 2013 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt1.M70P.1
- built for M70P

* Tue Oct 08 2013 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt2
- fix to build with new libav
- sync patches with Debian

* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt0.M60P.1
- built for M60P

* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 2.3.8-alt1
- new version

* Tue Aug 09 2011 Sergey V Turchin <zerg@altlinux.org> 2.3.7-alt0.M60P.1
- built for M60P

* Tue Aug 09 2011 Sergey V Turchin <zerg@altlinux.org> 2.3.7-alt1
- new version
- fix to build with libav

* Tue Apr 05 2011 Sergey V Turchin <zerg@altlinux.org> 2.3.6-alt3
- move to standart place

* Mon Feb 21 2011 Sergey V Turchin <zerg@altlinux.org> 2.3.6-alt2
- fix to compile

* Thu Aug 26 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.6-alt0.M51.1
- built for M51

* Thu Aug 26 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.6-alt1
- new version

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.5-alt0.M51.1
- build for M51

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 2.3.5-alt1
- new version

* Thu Dec 10 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.4-alt0.M51.1
- built for M51

* Thu Dec 10 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.4-alt1
- new version

* Tue Aug 25 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.3-alt1
- new version

* Fri Aug 07 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.2-alt0.M50.1
- built for M50

* Mon Jul 20 2009 Sergey V Turchin <zerg@altlinux.org> 2.3.2-alt1
- initial specfile
