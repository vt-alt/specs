%def_enable qt5

Name: qsynth
Version: 0.5.7
Release: alt1

Summary: QSynth is a GUI front-end for FluidSynth
Summary(ru_RU.UTF-8): QSynth - это графическая надстройка над FluidSynth
Group: Sound
License: GPL
Url: http://%name.sourceforge.net

Packager: Yuri N. Sedunov <aris@altlinux.ru>

Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar.gz

Requires: fluidsynth

BuildRequires: gcc-c++ ladspa_sdk libfluidsynth-devel libXext-devel
%if_enabled qt5
BuildRequires: qt5-tools qt5-x11extras-devel
%else
BuildRequires: libqt4-devel
%endif

%description
QSynth is a fluidsynth GUI front-end application. Eventually it may
evolve into a softsynth management application allowing the user to
control and manage a variety of command line softsynth but for the
moment it wraps the excellent Fluidsynth. Fluidsynth is a command line
software synthesiser based on the Soundfont specification.

%description -l ru_RU.UTF-8
QSynth -- это графическая надстройка над FluidSynth. В будущем
программа может превратиться в универсальный фронт-энд для многих
других синтезаторов, работающих из командной строки, но пока
используется только FluidSynth. FluidSynth же, в свою очередь,
является программным синтезатором на основе спецификаций SoundFont 2.

%define qtdir %_libdir/qt4

%prep
%setup

%build
%if_disabled qt5
export QTDIR=%qtdir
export PATH=%qtdir/bin:$PATH
%endif
%configure --localedir=%_datadir/%name/locale

# SMP-incompatible build
%make_build

%install
%makeinstall_std

%find_lang --with-qt %name

%files -f %name.lang
%_bindir/%name
%_datadir/applications/*
%_iconsdir/hicolor/*/*/*.png
%dir %_datadir/%name
%dir %_datadir/%name/translations
%_datadir/metainfo/%name.appdata.xml
%_man1dir/%name.1.*
%doc AUTHORS ChangeLog README TODO

%changelog
* Sat Jul 13 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.7-alt1
- 0.5.7

* Thu Apr 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.6-alt1
- 0.5.6

* Wed Mar 13 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.5-alt1
- 0.5.5

* Thu Jan 17 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt2
- rebuilt against libfluidsynth.so.2

* Fri Dec 28 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4

* Thu Oct 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- 0.5.3

* Mon Jul 23 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- 0.5.2

* Mon May 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Tue Dec 26 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Thu Apr 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- 0.4.4

* Mon Nov 14 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Thu Sep 15 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Tue Apr 05 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1 with qt5

* Wed Sep 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Sat Mar 28 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.9-alt1
- 0.3.9

* Tue Dec 31 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.8-alt1
- 0.3.8

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.7-alt1
- 0.3.7

* Fri Aug 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- 0.3.6

* Sat May 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt1
- 0.3.5

* Tue Apr 06 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- new version

* Tue Dec 02 2008 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3
- updated buildreqs

* Mon May 15 2006 Mikhail Yakshin <greycat@altlinux.org> 0.2.5-alt1
- 0.2.5

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.2.1-alt0.5.1
- Rebuilt with libstdc++.so.6.

* Mon Sep 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.1-alt0.5
- 0.2.1

* Tue Feb 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.2-alt0.5
- 0.1.2

* Mon Jan 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.0-alt0.5
- 0.1.0

* Mon Dec 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.3-alt0.5
- 0.0.3

* Fri Nov 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.2-alt0.5
- new version.

* Sun Nov 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.1-alt0.5
- First build for Sisyphus.
- summary, description by avp.
