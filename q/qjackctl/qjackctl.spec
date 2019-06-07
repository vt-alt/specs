%define cvsbuild 1
%undefine cvsbuild
%define cvsdate 20060910
%define prerel %nil

%def_enable qt5
# enable/disable JACK version support
%def_enable jack_version

Name: qjackctl
Version: 0.5.8
%ifdef cvsbuild
Release: alt0.cvs%cvsdate
%else
Release: alt1%prerel
%endif

Summary: Qjackctl is a programm to control the JACK sound server daemon
Summary(ru_RU.UTF-8): Qjackctl -- это программа для контроля над демоном JACK-сервера
Group: Sound
License: GPL
Url: http://%name.sourceforge.net

%ifdef cvsbuild
Source: %name-%cvsdate.tar
%else
Source: http://prdownloads.sourceforge.net/%name/%name-%version%prerel.tar.gz
%endif

%define jack_ver 0.118
Requires: jackd >= %jack_ver

BuildRequires(pre): jackit-devel >= %jack_ver
BuildRequires: gcc-c++ libalsa-devel libX11-devel libXext-devel
%if_enabled qt5
BuildRequires: qt5-base-devel qt5-x11extras-devel qt5-tools
%else
BuildRequires: libqt4-devel
%endif

%description
Qjackctl -- is an easy to use GUI to low-latency JACK audio server. You
can change options of starting JACK, assign scripts to be executed on
start/stop of the server, connect/disconnect loaded JACK clients and
route MIDI inputs'outputs.

%description -l ru_RU.UTF-8
Qjackctl -- это удобная программа с графическим интерфейсом для
управления звуковым сервером JACK. С её помощью можно изменять параметры
запуска сервера, указывать сценарии, запускаемые после старта сервера, а
также коммутировать звуковые и MIDI входы и выходы подключенных
JACK-клиентов.

%prep
%ifdef cvsbuild
%setup -n %name
%autoreconf
%else
%setup -n %name-%version%prerel
%endif

%build
%if_disabled qt5
export QTDIR=%_qt4dir
export PATH=%_qt4dir/bin:$PATH
%endif
%configure \
	--localedir=%_datadir/%name/locale \
	%{?_enable_jack_version:--enable-jack-version}
%make_build

%install
%makeinstall_std

%find_lang --with-qt --with-man %name

%files -f %name.lang
%_bindir/%name
%_datadir/applications/*
%dir %_datadir/%name
%dir %_datadir/%name/translations
%_iconsdir/hicolor/*/*/*.*
%_man1dir/*
%_datadir/metainfo/%name.appdata.xml
%doc AUTHORS ChangeLog README TODO

%changelog
* Mon May 27 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.8-alt1
- 0.5.8

* Thu Apr 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.7-alt1
- 0.5.7

* Wed Mar 13 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.6-alt1
- 0.5.6

* Mon Nov 26 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.5-alt1
- 0.5.5

* Thu Oct 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4

* Mon Jul 23 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- 0.5.3

* Sun May 27 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- 0.5.2

* Mon May 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Tue Dec 26 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Thu Apr 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.5-alt1
- 0.4.5

* Mon Nov 14 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- 0.4.4

* Thu Sep 15 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Tue May 31 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Mon Feb 22 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Wed Jul 15 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Mon Oct 20 2014 Yuri N. Sedunov <aris@altlinux.org> 0.3.12-alt1
- 0.3.12

* Fri Jan 17 2014 Yuri N. Sedunov <aris@altlinux.org> 0.3.11-alt1
- 0.3.11

* Mon Apr 01 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.10-alt1
- 0.3.10

* Mon May 28 2012 Yuri N. Sedunov <aris@altlinux.org> 0.3.9-alt1
- 0.3.9

* Fri Aug 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3.8-alt1
- 0.3.8

* Wed Mar 23 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3.7-alt1
- 0.3.7

* Tue Apr 06 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- 0.3.6

* Fri Oct 02 2009 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt1
- 0.3.5 (closes #21809)

* Sat Dec 13 2008 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- 0.3.4 release
- removed obsolete %%{update,clean}_menus
- updated {build,}reqs

* Sun Sep 10 2006 L.A. Kostis <lakostis@altlinux.ru> 0.2.20.17-alt0.cvs20060910
- CVS snapshot 2006-09-10.

* Mon Apr 04 2006 LAKostis <lakostis at altlinux.ru> 0.2.20-alt1
- 0.2.20.
- cleanup buildreq.

* Wed Aug 10 2005 LAKostis <lakostis at altlinux.ru> 0.2.18-alt1
- NMU.
- 0.2.18.

* Mon Feb 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.2.15-alt1
- 0.2.15.

* Mon Jan 24 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.2.14-alt1
- 0.2.14.

* Tue Nov 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.13-alt1
- 0.2.13

* Tue Sep 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.11-alt1
- 0.2.11

* Tue Jul 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.9-alt0.5
- 0.2.9

* Wed May 19 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.8-alt0.5
- 0.2.8

* Tue Feb 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.5-alt0.5
- 0.2.5

* Tue Jan 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.3-alt0.5a
- 0.2.3a

* Mon Jan 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.1-alt0.5
- 0.2.1

* Mon Dec 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.0-alt0.5
- 0.2.0

* Sun Nov 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.1.2-alt0.5
- 0.1.2

* Thu Oct 23 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.1.0-alt0.5
- 0.1.0

* Fri Sep 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.9-alt0.5
- 0.0.9

* Sat Sep 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.6-alt0.5
- 0.0.6

* Sat Sep 06 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.5-alt0.5
- 0.0.5

* Sat Aug 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.4-alt0.5
- 0.0.4

* Fri Aug 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.3-alt0.5
- First build for Sisyphus.
- russian summary, description by avp.
