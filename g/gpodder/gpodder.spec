%def_disable snapshot
%def_enable check

Name: gpodder
Version: 3.10.10
Release: alt1

Summary: podcast receiver/catcher in PyGTK
License: GPLv3
Group: Sound
Url: http://gpodder.org

%if_disabled snapshot
Source: https://github.com/gpodder/gpodder/archive/%version/%name-%version.tar.gz
%else
# VCS: https://github.com/gpodder/gpodder.git
Source: %name-%version.tar
%endif

BuildArch: noarch

AutoReqProv: nopython
%define __python %nil
%add_python3_path %_datadir/%name

# M$ and ubuntu specific
%add_python3_req_skip comtypes pywintypes win32gui appindicator
%filter_from_requires /win32ctypes/d
%add_typelib_req_skiplist typelib(Unity)
# Optional dependencies
# https://github.com/SoCo/SoCo
%add_python3_req_skip soco
# https://github.com/freevo/kaa-metadata
# last commit in 2015
%add_python3_req_skip kaa.metadata

Requires: %_bindir/ffmpeg xdg-utils
Requires: python3-module-eyeD3

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-devel python3-module-mygpoclient
BuildRequires: python3-module-feedparser help2man intltool desktop-file-utils
%if_enabled check
BuildRequires: python3-module-podcastparser python3-modules-sqlite3
BuildRequires: python3-module-minimock python3-module-coverage
%endif

%description
gPodder enables you to subscribe to RSS feeds and download
podcast episodes from these feeds. gPodder can operate in
GUI mode and in CLI mode. Downloaded podcasts can either
be synchronized to portable MP3 players (including iPods)
or played back on the user's desktop.

%prep
%setup

%build
%make

%install
%makeinstall_std

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Tuner \
	%buildroot%_desktopdir/gpodder.desktop

%check
PYTHON=python3 %make unittest

%files -f %name.lang
%_bindir/*
%python3_sitelibdir/*
%_desktopdir/%name.desktop
%_desktopdir/%name-url-handler.desktop
%_datadir/dbus-1/services/org.gpodder.service
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.svg
%_iconsdir/hicolor/*/apps/%name.png
%_man1dir/*
%_datadir/metainfo/*.appdata.xml


%changelog
* Fri Sep 27 2019 Yuri N. Sedunov <aris@altlinux.org> 3.10.10-alt1
- 3.10.10

* Mon Jun 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.10.9-alt1
- 3.10.9

* Sat Apr 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.10.8-alt1
- 3.10.8

* Sat Feb 02 2019 Yuri N. Sedunov <aris@altlinux.org> 3.10.7-alt1
- 3.10.7

* Thu Jan 03 2019 Yuri N. Sedunov <aris@altlinux.org> 3.10.6-alt1
- updated to 3.10.6-5-g643b41e2

* Sun Sep 16 2018 Yuri N. Sedunov <aris@altlinux.org> 3.10.5-alt1
- 3.10.5 (ported to Python3, GTK+3)

* Thu Dec 28 2017 Yuri N. Sedunov <aris@altlinux.org> 3.9.5-alt1
- 3.9.5

* Sat Jan 07 2017 Yuri N. Sedunov <aris@altlinux.org> 3.9.3-alt1
- 3.9.3

* Thu Nov 17 2016 Yuri N. Sedunov <aris@altlinux.org> 3.9.1-alt1
- 3.9.1

* Wed Apr 13 2016 Yuri N. Sedunov <aris@altlinux.org> 3.9.0-alt1
- 3.9.0

* Thu Jan 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.8.5-alt1
- 3.8.5

* Fri May 29 2015 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Mon Nov 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Wed Oct 08 2014 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Jul 07 2014 Yuri N. Sedunov <aris@altlinux.org> 3.7.0-alt1
- 3.7.0

* Tue Jul 10 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.2-alt1
- 3.1.2

* Thu Jan 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.3-alt1
- 3.0.3

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3-alt1.qa1.1
- Rebuild with Python-2.7

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.3-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gpodder

* Sun Mar 28 2010 Yuri N. Sedunov <aris@altlinux.org> 2.3-alt1
- 2.3

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.2-alt1
- new version

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.1-alt1.qa1.1
- Rebuilt with python 2.6

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.12.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for gpodder
  * postclean-05-filetriggers for spec file

* Fri Jul 25 2008 Alexander Myltsev <avm@altlinux.ru> 0.12.1-alt1
- new version: bug fixes, usability enhancements.

* Tue Mar 11 2008 Alex V. Myltsev <avm@altlinux.ru> 0.11-alt1
- new version: systray icon, Bluetooth support, usability changes, bug fixes

* Fri Jan 18 2008 Alex V. Myltsev <avm@altlinux.ru> 0.10.3-alt1
- New version.

* Sun Nov 11 2007 Alex V. Myltsev <avm@altlinux.ru> 0.10.1-alt1
- Initial build for Sisyphus.
