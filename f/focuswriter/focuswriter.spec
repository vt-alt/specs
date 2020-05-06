Name:		focuswriter
Version:	1.7.6
Release:	alt1
Summary:	FocusWriter is a fullscreen, distraction-free word processor
License:	GPLv3
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Group:		Text tools
Url:		http://gottcode.org/focuswriter/
Source0:	http://gottcode.org/focuswriter/%name-%version-src.tar.bz2

BuildRequires:	libhunspell-devel qt5-multimedia-devel qt5-tools zlib-devel gcc-c++

%description
FocusWriter is a fullscreen, distraction-free word processor
designed to immerse you as much as possible in your work.
The program autosaves your progress, and reloads the last files
you had open to make it easy to jump back in during your next
writing session, and has many other features that make it such
that only one thing matters: your writing.

%prep
%setup
%ifarch %e2k
# lcc 1.23.12 doesn't grok u'’' by default
%add_optflags -finput-charset=utf8
%endif

%build
sed -i 's|DATADIR/metainfo/|DATADIR/appdata/|g' %name.pro
qmake-qt5 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" PREFIX=%prefix
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install
# http://altlinux.org/Icon_Paths_Policy
rm -f %buildroot%_pixmapsdir/*.xpm

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_datadir/appdata/%name.*
%_man1dir/%name.*
%_iconsdir/hicolor/*/apps/*

%changelog
* Fri May 01 2020 Motsyo Gennadi <drool@altlinux.ru> 1.7.6-alt1
- 1.7.6

* Tue Jun 18 2019 Michael Shigorin <mike@altlinux.org> 1.6.16-alt3
- E2K: better fix (see also mcst#3940)

* Tue Jun 18 2019 Michael Shigorin <mike@altlinux.org> 1.6.16-alt2
- E2K: ftbfs workaround

* Wed Oct 03 2018 Michael Shigorin <mike@altlinux.org> 1.6.16-alt1
- 1.6.16
- minor spec cleanup

* Fri Jan 26 2018 Motsyo Gennadi <drool@altlinux.ru> 1.6.8-alt1
- 1.6.8

* Mon Mar 13 2017 Motsyo Gennadi <drool@altlinux.ru> 1.6.4-alt1
- 1.6.4

* Wed Oct 05 2016 Motsyo Gennadi <drool@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Sat Aug 27 2016 Motsyo Gennadi <drool@altlinux.ru> 1.6.0-alt2
- fix BuildRequires for Qt5

* Sat Aug 27 2016 Motsyo Gennadi <drool@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Sat Jun 25 2016 Motsyo Gennadi <drool@altlinux.ru> 1.5.6-alt1
- 1.5.6

* Sun Sep 06 2015 Motsyo Gennadi <drool@altlinux.ru> 1.5.5-alt1
- 1.5.5

* Sun Jun 14 2015 Motsyo Gennadi <drool@altlinux.ru> 1.5.4-alt1
- 1.5.4

* Sun Jun 29 2014 Motsyo Gennadi <drool@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Sun Apr 13 2014 Motsyo Gennadi <drool@altlinux.ru> 1.4.6-alt1
- 1.4.6

* Fri Mar 28 2014 Motsyo Gennadi <drool@altlinux.ru> 1.4.5-alt1
- 1.4.5

* Fri May 31 2013 Motsyo Gennadi <drool@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Mon Apr 08 2013 Motsyo Gennadi <drool@altlinux.ru> 1.4.3-alt1
- 1.4.3

* Thu Mar 28 2013 Motsyo Gennadi <drool@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Thu Nov 29 2012 Motsyo Gennadi <drool@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Sun Sep 23 2012 Motsyo Gennadi <drool@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Sun Jun 17 2012 Motsyo Gennadi <drool@altlinux.ru> 1.3.6-alt1
- 1.3.6

* Fri Dec 09 2011 Motsyo Gennadi <drool@altlinux.ru> 1.3.5.1-alt1
- 1.3.5.1

* Sat Nov 05 2011 Motsyo Gennadi <drool@altlinux.ru> 1.3.4.1-alt1
- 1.3.4.1

* Tue Mar 22 2011 Motsyo Gennadi <drool@altlinux.ru> 1.3.2.1-alt1
- initial build for ALT Linux
