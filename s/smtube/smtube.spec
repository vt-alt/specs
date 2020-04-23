Name:		smtube
Version:	20.1
Release:	alt1
Summary:	Youtube Browser for SMPlayer
Summary(ru_RU.UTF8):	Браузер YouTube для SMPlayer
Summary(uk_UA.UTF8):	Переглядач YouTube для SMPlayer
Summary(de):	Youtube Browser für SMPlayer
Packager:	Motsyo Gennadi <drool@altlinux.ru>
License:	GPLv2+
Group:		Video
Url:		http://smtube.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/smtube/SMTube/%version/%name-%version.tar.bz2

Patch0:		smtube-fixed-trash-in-the-title-of-the-mpv-ON-SCREEN-CONTROLLER.patch

BuildRequires:	gcc-c++ libqt4-devel

%description
SMTube is a tool for searching and downloading videos from YouTube.
It supports SMPlayer, VLC and some other players.

%description -l de
Dies ist ein Youtube-Browser für den SMPayer.
Es unterstützt das Durchsuchen von Ordnern, allgemeine Suche, sowie das Downloaden
und Abspielen von Youtube Videos. Die Videos werden derzeit in SMPlayer
abgespielt.

%description -l ru_RU.UTF8
SMTube является утилитой для поиска и скачивания видео с YouTube.
Поддерживается SMPlayer, VLC и некоторые другие проигрыватели.

%description -l uk_UA.UTF8
SMTube є утилітою для пошуку та завантаження відео з YouTube.
Підтримується SMPlayer, VLC та деякі інші програвачі.

%prep
%setup -n %name-%version
%patch0 -p1

%build
subst 's|share/doc/smtube|share/doc/smtube-%version|g' Makefile
export PATH=$PATH:%_qt4dir/bin
lrelease ./src/translations/*.ts
cd ./src && qmake "QMAKE_CXXFLAGS+=%optflags -DTRANSLATION_PATH=%_datadir/%name/translations" PREFIX=%_prefix *.pro && cd ../
%make_build PREFIX=%_prefix

%install
%makeinstall_std PREFIX=%_prefix

%files
%dir %_datadir/%name/translations
%dir %_datadir/%name
%dir %_docdir/%name-%version
%_docdir/%name-%version/*
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/%name/translations/*.qm

%changelog
* Tue Apr 21 2020 Motsyo Gennadi <drool@altlinux.ru> 20.1-alt1
- 20.1

* Sat Jan 20 2018 Motsyo Gennadi <drool@altlinux.ru> 18.1.0-alt1
- 18.1.0 (#34436)

* Sat Jun 17 2017 Motsyo Gennadi <drool@altlinux.ru> 17.5.0-alt2
- (#33552) fixed trash in the title of the mpv ON SCREEN CONTROLLER

* Sat Jun 03 2017 Motsyo Gennadi <drool@altlinux.ru> 17.5.0-alt0.M51.1
- build for M51

* Sat Jun 03 2017 Motsyo Gennadi <drool@altlinux.ru> 17.5.0-alt1
- 17.5.0 (#33505)

* Mon Feb 20 2017 Motsyo Gennadi <drool@altlinux.ru> 17.1.0-alt1
- 17.1.0 (#33114)

* Fri Aug 12 2016 Motsyo Gennadi <drool@altlinux.ru> 16.7.2-alt1
- 16.7.2

* Sat Feb 06 2016 Motsyo Gennadi <drool@altlinux.ru> 16.1.0-alt1
- 16.1.0

* Sat Oct 10 2015 Motsyo Gennadi <drool@altlinux.ru> 15.9.0-alt1
- 15.9.0

* Sat Sep 05 2015 Motsyo Gennadi <drool@altlinux.ru> 15.8.0-alt1
- 15.8.0

* Fri Jun 12 2015 Motsyo Gennadi <drool@altlinux.ru> 15.5.17-alt1
- 15.5.17

* Thu May 14 2015 Motsyo Gennadi <drool@altlinux.ru> 15.5.10-alt1
- 15.5.10

* Fri May 08 2015 Motsyo Gennadi <drool@altlinux.ru> 15.5.7-alt1
- new beta versia (writen from scratch)

* Fri May 08 2015 Motsyo Gennadi <drool@altlinux.ru> 15.1.26-alt1
- 15.1.26

* Sat Apr 05 2014 Motsyo Gennadi <drool@altlinux.ru> 2.1-alt1
- 2.1 version

* Wed Oct 09 2013 Motsyo Gennadi <drool@altlinux.ru> 1.8-alt1
- initial build for ALT Linux (alt bug #29438)
