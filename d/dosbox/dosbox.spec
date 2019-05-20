%define docbook_man %_datadir/xml/docbook/xsl-stylesheets/manpages/docbook.xsl

Name: dosbox
Epoch: 1
Version: 0.74.2
Release: alt1

Summary: i8086/DOS/VGA software emulator for running old games
Summary(ru_RU.UTF8): Программный эмулятор i8086/DOS/VGA для запуска старых игр

License: GPLv2+
Group: Emulators

Url: http://dosbox.com

Packager: Anton Chernyshov <ach@altlinux.org>

Source0: %name-%version.tar.gz
Source1: DOSBox-russian-lang.zip

# additional scripts and man
Source2: %name-wrapper
Source3: %name-install
Source4: %name-install.xml

# icons and desktop file
Source5: %name.xpm
Source6: %name.desktop

# fix #24306 bug
Source7: %name-0.74-2.conf
Source8: README_ru.ALT

Patch: fix_werror_return_type.patch

Requires: shadow-utils unarj unzip unrar

Conflicts: dosbox-russian

BuildPreReq: docbook-dtds
BuildPreReq: docbook-style-xsl
BuildPreReq: gcc-c++
BuildPreReq: libalsa-devel
BuildPreReq: libGL-devel
BuildPreReq: libGLU-devel
BuildPreReq: libpng-devel
BuildPreReq: libSDL-devel
BuildPreReq: libSDL_net-devel
BuildPreReq: libSDL_sound-devel
BuildPreReq: libX11-devel
BuildPreReq: xsltproc
BuildPreReq: unzip

# Automatically added by buildreq on Sat Jul 12 2014
# optimized out: gnu-config libGL-devel libGLU-devel libSDL-devel libX11-devel libcloog-isl4 libstdc++-devel libtinfo-devel xorg-kbproto-devel xorg-xproto-devel zlib-devel
BuildRequires: gcc-c++ libSDL_net-devel libSDL_sound-devel libalsa-devel libncurses-devel libpng-devel

%description
DOSBox is graphical application that provides rich programming emulation
of Intel 8086 real-mode, SVGA and DOS with XMS/EMS (but no DPMI!).

This is very useful for running old good DOS games written for PC/XT/AT
that's impossible directly on modern Pentiums, SUN's, PowerPC & etc.
At least PII 400MHz is required for comfortable running.

Full list of tested games successfully supported by DOSBox
is published on the http://dosbox.sourceforge.net site.

Run it as following:
  * dosbox /path/to/game.exe
  * dosbox /path/to/gamedir
Examples:
  * dosbox /tmp/old-games/ugh.exe
    ...maps given directory to drive C: and start given EXE/COM/BAT-file
  * dosbox /usr/local/games
    ...maps given directory to drive C: and start built-in COMMAND.COM

%description -l ru_RU.UTF8
DOSBox - это графическое приложение, программно эмулирующее
процессор Intel 8086, графический адаптер SVGA
и операционную систему DOS с поддержкой XMS и EMS, но без DPMI.

DOSBox позволяет запускать на современном компьютере старые игры,
созданные для XT и AT, и не работающие на более новых системах.
Для комфортной работы требуется PII 400MHz или сравнимый с ним
по скорости процессор любой архитектуры (SUN, PowerPC и т.д.).

Полный список протестированных игр (Tower, Wings of Fury, Dune, ...)
находится на официальном сайте программы: http://dosbox.sourceforge.net.

Запуск эмулятора производится следующим образом:
  * dosbox /путь/к/игре/game.exe
  * dosbox /путь/к/игре
Примеры:
  * dosbox /tmp/old-games/ugh.exe
    ...отобразит каталог игры на диск C: и запустит указанный EXE/COM/BAT-файл
  * dosbox /usr/local/games
    ...отобразит указанный каталог на диск C: и запустит встроенный COMMAND.COM

%prep
%setup
%patch -p2

# Create script dosbox-set-lang (#24306)

cat > %name-set-lang << EOF
#!/bin/bash
#
# This script is distributed under terms of GPLv2 or later
# Copyright (C) Anton Chernyshov <ach@altlinux.org>
#
# Encoding in this file is UTF-8
#
# This is a simple script that set default DOSBox language
# to English or Russian language.
# It requires setting one parameter: en or ru,
# which would set needed language.
#
# Это простой скрипт, переключающий используемый DOSBox
# язык на указанный пользователем.
# Скрипту необходимо указать один параметр: en или ru,
# который и установит нужный язык.
#

if [ -e ~/.%name/%name-%version.conf ]; then
	echo "File exist. GOOD!";
else
	echo "File doesn't exist. Creating!"
	cp %_defaultdocdir/%name-%version/%name-%version.conf ~/.%name/
fi

case \$1 in
ru)
    echo "Set DOSBox language to Russian"
    sed -i -e 's/^language=$/language=\/usr\/share\/doc\/%name-%version\/DOSBox-russian-lang\/russian.txt/' \
	   -e 's/^keyboardlayout=auto/keyboardlayout=RU/' \
	~/.%name/%name-%version.conf
	;;
en)
    echo "Set DOSBox language to English"
    sed -i -e 's/language=\/usr\/share\/doc\/%name-%version\/DOSBox-russian-lang\/russian.txt/language=/' \
	   -e 's/^keyboardlayout=RU/keyboardlayout=auto/' \
	~/.%name/%name-%version.conf
	;;
*)
    echo "Please set correct options: en or ru";
esac
EOF

%build
%configure \
	--enable-debug=heavy \
	--enable-core-inline \
	--disable-fpu-x86

%make_build
cp -a src/dosbox src/dosbox-debug

make distclean
%configure \
	--enable-core-inline \
	--disable-fpu-x86

%make_build
xsltproc %docbook_man %{SOURCE4}

%install
%makeinstall_std

# install dosbox debugger
install src/%name-debug %buildroot%_bindir/%name-debug

# install additional scripts
install -D -p %{SOURCE2} %buildroot/%_bindir/%name-install
install -D -p %{SOURCE3} %buildroot/%_bindir/%name-wrapper

# install dosbox-install manual
install -D dosbox-install.1 %buildroot/%_man1dir/dosbox-install.1

# install DOSBox-russian-docs
mkdir -p %buildroot/%_defaultdocdir/%name-%version/
unzip %{SOURCE1} -d %buildroot/%_defaultdocdir/%name-%version/

# install upstream docs
cp AUTHORS ChangeLog NEWS README THANKS %buildroot/%_defaultdocdir/%name-%version
cp docs/{README.video,PORTING} %buildroot/%_defaultdocdir/%name-%version

# create directory for data files and for placing games
mkdir -p %buildroot{%_datadir/%name,%_gamesbindir/%name}

# install icons and desktop file
install -D -m 0644 %{SOURCE5} %buildroot/%_iconsdir/%name.xpm
install -D -m 0644 %{SOURCE6} %buildroot/%_desktopdir/%name.desktop

# fix #24306 bug
install -D -m755 %name-set-lang %buildroot%_bindir/%name-set-lang
cp %{SOURCE7} %{SOURCE8} %buildroot/%_defaultdocdir/%name-%version

%files
%_bindir/*
%dir %_datadir/%name
%_man1dir/%{name}*
%doc %_defaultdocdir/*
%_iconsdir/*
%_desktopdir/*

%changelog
* Wed May 15 2019 Grigory Ustinov <grenka@altlinux.org> 1:0.74.2-alt1
- Build new version (Closes: #36653).

* Wed May 04 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.74.r3852-alt1
- svn snapshot, fpu problems on x86_64 should be fixed

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.74-alt4.qa1
- Rebuilt for gcc5 C++11 ABI.

* Thu Oct 09 2014 Mikhail Kolchin <mvk@altlinux.org> 0.74-alt4
- fix %install section

* Sat Jul 12 2014 Fr. Br. George <george@altlinux.ru> 0.74-alt3
- add debugger-enabled binary

* Fri Jul 11 2014 Mikhail Kolchin <mvk@altlinux.org> 0.74-alt2.4
- fixed script dosbox-set-lang (ALT#24306)

* Thu Apr 18 2013 Sergey V Turchin <zerg@altlinux.org> 0.74-alt2.3
- fix requires (ALT#28864)

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.74-alt2.2
- Rebuilt with libpng15

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.74-alt2.1
- Fixed build

* Mon Nov 8 2010 Anton Chernyshov <ach@altlinux.org> 0.74-alt2
- closes #24306 bug (completely):
  + add to package script dosbox-set-lang to help users set language
    that he/she needed
- add new build dependency libGLU-devel

* Sat Nov 6 2010 Anton Chernyshov <ach@altlinux.org> 0.74-alt1.1
- fix #24306 bug:
  + add dosbox-0.74.conf with support russian language
  + add README_ru.ALT file with problem resolv method

* Sat Nov 6 2010 Anton Chernyshov <ach@altlinux.org> 0.74-alt1
- new upstream release 0.74
- slightly spec file modifications
- convert russian DOSBox docs to UTF-8
- add new ./configure options

* Tue Jul 21 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.73-alt2
- do not package %%_gamesbindir/%%name

* Thu May 28 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.73-alt1
- 0.73
- disable dosbox-0.65-loadfont-base.patch

* Sat May 09 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.72-alt9
- fix build with gcc 4.4 (RH)

* Tue Apr 07 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.72-alt8
- fix keyboard mappings when using evdev X11 driver (closes: #19488; RH)

* Sun Nov 23 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.72-alt7
- remove alternatives trigger

* Mon Nov 17 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.72-alt6
- remove update_*/clean_* invocations

* Sun Oct 26 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.72-alt5
- fix build

* Tue May 27 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.72-alt4
- desktop file improvements (closes: #15726; cas@)

* Thu Apr 17 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.72-alt3
- remove alternatives support, add Conflicts on dosbox-russian
- remove English lang file, sample config and tools for their generation
- fix desktop file
- move 32x32 icon from iconsdir to niconsdir
- add http://www.dosbox.com/tools/DOSBox-russian-lang-072-2.zip (Russian readme
  and config)

* Fri Oct 19 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.72-alt2
- add requires on shadow-utils (#13136)

* Tue Aug 28 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.72-alt1
- 0.72

* Thu Aug 02 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.71-alt1
- 0.71

* Sat Mar 03 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.70-alt1
- 0.70

* Sun Sep 17 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.65-alt1
- 0.65
- massive spec cleanup

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.63-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue Dec 21 2004 Ilya Evseev <evseev@altlinux.ru> 0.63-alt1
- updated to version 0.63 containing multiple bugfixes
- bugfix: /usr/share/dosbox was not owned by package
- new alternatives scheme used in ALTLinux 2.4

* Mon Oct 17 2004 Ilya Evseev <evseev@altlinux.ru> 0.62-alt5
- fixed spec bug with macro man1dir -> _man1dir

* Mon Oct  4 2004 Ilya Evseev <evseev@altlinux.ru> 0.62-alt4
- official 0.62 release
- added 'BuildPreReq: gcc-c++' for building in ALTLinux hasher environment
- added --no-main switch to wrapper for running it as subroutines container only
- /usr/bin/dosbox is managed by alternatives, by default is assigned to wrapper
- small spec cleanups

* Fri Jul 23 2004 Ilya Evseev <evseev@altlinux.ru> 0.62-alt3
- russian support is completely moved to separate spec-file
- conform to ALTLinux Specfile conventions
- simplify "%prep" and "%install" sections
- add support of /etc/dosbox/runargs directory to wrapper and spec

* Mon Jun  7 2004 Ilya Evseev <ilya_evseev@mail.ru> 0.62-1
- updated to version 0.62 from CVS
- added dosbox-install script
- added support of loadable fonts
- add dosbox-russian package with manuals, cyrillic fonts,
  configuration and language file
- added dosbox-apps package

* Mon Apr 26 2004 Ilya Evseev <ilya_evseev@mail.ru> 0.61-2
- fixed bug with creating group on installation stage,
  split installation: create group before, update menus after
- removed Packager record from spec-file
- added patch for loading user-defined fonts to Video-BIOS ROM on startup
- article removed from packaged stuff and will be managed separately

* Fri Feb 15 2004 Ilya Evseev <ilya_evseev@mail.ru> 0.61-1
- updated to version 0.61
- manpage and langfile are translated to Russian
- added script for running binary with global/localized settings
- added introduction article (in Russian)
- added menu item and icons for X, taken from DosEmu package
- added script for downloading/extracting/menu adding DOS executables

* Wed Oct 08 2003 Ilya Evseev <ilya_evseev@mail.ru> 0.58-1
- initial RPM build, rpmbuild -ba --target i586 dosbox.spec
