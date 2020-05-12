Name: vice
Version: 3.4
Release: alt2

Summary: Versatile Commodore Emulator
Summary(pl.UTF-8): Uniwersalny emulator Commodore
License: GPL-2.0-or-later
Group: Emulators

Url: https://netcologne.dl.sourceforge.net/project/vice-emu
Source0: https://netcologne.dl.sourceforge.net/project/vice-emu/releases/%name-%version.tar.gz
Source1: vice-c128.desktop
Source2: vice-c1541.desktop
Source3: vice-c64dtv.desktop
Source4: vice-c64sc.desktop
Source5: vice-cbm2.desktop
Source6: vice-cbm5x0.desktop
Source7: vice-pet.desktop
Source8: vice-plus4.desktop
Source9: vice-vic20.desktop
Source10: vice-vsid.desktop
Source11: vice-normalicons.tar.bz2
Source12: vice-largeicons.tar.bz2
Source13: vice-miniicons.tar.bz2
Patch0: vice-3.4-fix-build.patch
Patch1: vice-3.4-fix-destination-path.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: flex gcc-c++
BuildRequires: libGL-devel
BuildRequires: libSDL2-devel
BuildRequires: libXrandr-devel
BuildRequires: libesd-devel
BuildRequires: libjpeg-devel
BuildRequires: liblame-devel
BuildRequires: libreadline-devel
BuildRequires: libungif-devel
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: libX11-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libalsa-devel
BuildRequires: makeinfo
BuildRequires: xa
BuildRequires: libpulseaudio-devel
BuildRequires: libavcodec-devel libswresample-devel

%description
VICE is a Versatile Commodore Emulator, i.e. a program that runs on a
Unix, MS-DOS, Win95/NT, OS/2, RiscOS or BeOS machine and executes
programs intended for the old 8-bit Commodore computers. The current
version emulates the C64, the C128 (80 column screen is included now),
the VIC20, all the PET models (except the SuperPET 9000, which is out
of line anyway), CBM-II (aka C610) and the Plus4.

%description -l pl.UTF-8
VICE jest wszechstronnym emulatorem 8-bitowego komputera Commodore.
Aktualna wersja emuluje C64, C128 (wraz z trybem pracy 80 kolumnowym),
VIC20, wszystkie modele PET (poza SuperPET 9000, który zresztą nie
pasował do tej linii), CBM-II (C610) oraz Plus4.

%prep
%setup
%patch0 -p2
%patch1 -p2

%build
touch ABOUT-NLS config.rpath
%add_optflags -fno-strict-aliasing
%autoreconf
%configure \
	--enable-sdlui2 \
	--enable-external-ffmpeg

%make_build

%install
install -d %buildroot{%_desktopdir,%_pixmapsdir}

perl -i -pe 's/SUBDIRS = html\n//' doc/Makefile
%make_install install DESTDIR=%buildroot 

rm -f doc/html/{Makefile*,texi2html}
rm -rf %buildroot%_datadir/vice/doc

install -pm644 \
	%SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 \
	%SOURCE6 %SOURCE7 %SOURCE8 %SOURCE9 %SOURCE10 \
	%buildroot%_desktopdir

mkdir -p %buildroot%_iconsdir/hicolor/{16x16,32x32,48x48}/apps
tar xjf %SOURCE11 -C %buildroot%_iconsdir/hicolor/32x32/apps
tar xjf %SOURCE12 -C %buildroot%_iconsdir/hicolor/48x48/apps
tar xjf %SOURCE13 -C %buildroot%_iconsdir/hicolor/16x16/apps

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog FEEDBACK NEWS README
%doc doc/iec-bus.txt doc/html
%_bindir/*
%_prefix/lib/%name/
%_mandir/man?/*
%_infodir/*.info*
%_desktopdir/*.desktop
#_pixmapsdir/*
%_iconsdir/hicolor/*/*/*.png

%changelog
* Tue May 12 2020 Anton Midyukov <antohami@altlinux.org> 3.4-alt2
- Rebuild with xa

* Mon May 04 2020 Anton Midyukov <antohami@altlinux.org> 3.4-alt1
- New version 3.4

* Wed Feb 06 2019 Michael Shigorin <mike@altlinux.org> 2.1-alt9
- rebuilt against libreadline7

* Sat Feb 03 2018 Michael Shigorin <mike@altlinux.org> 2.1-alt8
- fixed build with current perl

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 2.1-alt7.3
- Fixed build with perl 522

* Wed Nov 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt7.2
- Fixed build with libpng15

* Tue Jun 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt7.1
- Fixed build

* Sun Mar 27 2011 Michael Shigorin <mike@altlinux.org> 2.1-alt7
- more missing BR: back

* Sun Mar 20 2011 Michael Shigorin <mike@altlinux.org> 2.1-alt6
- re-added lost BRs, thx at@

* Thu May 28 2009 Michael Shigorin <mike@altlinux.org> 2.1-alt5
- fixed the last problem with deeply broken mandriva desktop files
  (thanks viy@ who did better than desktop-file-validate)

* Tue May 26 2009 Michael Shigorin <mike@altlinux.org> 2.1-alt4
- fixed a couple of broken desktop files

* Sun May 24 2009 Michael Shigorin <mike@altlinux.org> 2.1-alt3
- rebuilt with libalsa-1.0.20-alt2

* Fri May 15 2009 Michael Shigorin <mike@altlinux.org> 2.1-alt2
- applied gentoo patch to fix FTBFS with gcc-4.4

* Tue Mar 17 2009 Michael Shigorin <mike@altlinux.org> 2.1-alt1
- built for ALT Linux (folks from Virtual Sky Solutions asked for it)
  + somewhat based on PLD 2.1-1, Mandriva 2.1-2mdk and DAG's
    specs, resources and patches
  + heavy cleanup/merge/adaptation
  + VICEDIR=/usr/lib/vice
- NB: no C64, no ROMs, so you guessed no maintainer ;-)
