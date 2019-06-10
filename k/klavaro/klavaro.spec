Name: klavaro
Version: 3.07
Release: alt1

Summary: Yet another touch typing tutor
License: GPLv3+
Group: Education

Url: http://klavaro.sourceforge.net/en/
Source: http://downloads.sourceforge.net/klavaro/klavaro-%version.tar.bz2

BuildRequires: libgtk+3-devel >= 3.8.0
BuildRequires: libcurl-devel intltool libappstream-glib-devel

%description
Klavaro is just another free touch typing tutor program. It intends to
be keyboard and language independent, saving memory and time.

%prep
%setup
subst 's#/usr/share/icons/hicolor/24x24/apps/klavaro.png#klavaro#' data/klavaro.desktop.in
subst 's/Education/Education;Science;ComputerScience/' data/klavaro.desktop.in

%build
%add_optflags -D_FILE_OFFSET_BITS=64
export DATADIRNAME=share
%autoreconf
%configure --disable-shared \
	LIBS=%(pkg-config --libs cairo)
%make_build

%install
%makeinstall_std DATADIRNAME=share appdatadir=%_datadir/metainfo
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_man1dir/%name.1*
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/metainfo/%name.appdata.xml

%exclude %_includedir
%exclude %_libdir/libgtkdataboks.a

%changelog
* Tue Jun 04 2019 Yuri N. Sedunov <aris@altlinux.org> 3.07-alt1
- 3.07

* Tue Mar 19 2019 Yuri N. Sedunov <aris@altlinux.org> 3.05-alt1
- 3.05

* Tue Feb 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.04-alt1
- 3.04

* Thu Apr 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.03-alt2
- fixed PACKAGE_LOCALE_DIR (ALT #34798)
- fixed appdatadir

* Mon Jul 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.03-alt1
- 3.03

* Fri Dec 16 2016 Yuri N. Sedunov <aris@altlinux.org> 3.02-alt1
- 3.02

* Fri Jun 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.01-alt1
- 3.01

* Thu Jan 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.00-alt1
- 3.0.0

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 2.00-alt1
- 2.0.0

* Tue Dec 04 2012 Yuri N. Sedunov <aris@altlinux.org> 1.9.6-alt1
- 1.9.6
- built against libgtkdatabox-0.9.2.so.0

* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.3-alt3.1
- Fixed build

* Mon Aug 15 2011 Andrey Cherepanov <cas@altlinux.org> 1.9.3-alt3
- Update Russian translation (closes: #26055)

* Sun Jul 17 2011 Victor Forsiuk <force@altlinux.org> 1.9.3-alt2
- Rebuild with new libgtkdatabox.

* Sun Jul 10 2011 Victor Forsiuk <force@altlinux.org> 1.9.3-alt1
- 1.9.3

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 1.9.2-alt1
- 1.9.2

* Sun Apr 17 2011 Victor Forsiuk <force@altlinux.org> 1.9.1-alt1
- 1.9.1

* Tue Mar 29 2011 Victor Forsiuk <force@altlinux.org> 1.9.0-alt1
- 1.9.0

* Wed Feb 23 2011 Victor Forsiuk <force@altlinux.org> 1.8.1-alt1
- 1.8.1

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 1.7.5-alt1
- 1.7.5

* Mon Dec 20 2010 Victor Forsiuk <force@altlinux.org> 1.7.4-alt1
- 1.7.4

* Fri Nov 26 2010 Victor Forsiuk <force@altlinux.org> 1.7.3-alt1
- 1.7.3

* Mon Sep 27 2010 Victor Forsiuk <force@altlinux.org> 1.7.2-alt1
- 1.7.2

* Thu Aug 26 2010 Victor Forsiuk <force@altlinux.org> 1.7.1-alt1
- 1.7.1

* Tue Aug 17 2010 Victor Forsiuk <force@altlinux.org> 1.6.0-alt1
- 1.6.0

* Mon Mar 01 2010 Victor Forsiuk <force@altlinux.org> 1.5.0-alt1
- 1.5.0

* Mon Dec 28 2009 Victor Forsyuk <force@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Dec 14 2009 Victor Forsyuk <force@altlinux.org> 1.4.0-alt1
- 1.4.0

* Tue Sep 08 2009 Victor Forsyuk <force@altlinux.org> 1.3.0-alt1
- 1.3.0

* Wed Jul 29 2009 Victor Forsyuk <force@altlinux.org> 1.2.1-alt1
- 1.2.1

* Sat Jan 26 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.0.7-alt1
- first build
