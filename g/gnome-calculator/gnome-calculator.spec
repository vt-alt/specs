%def_disable snapshot
%define ver_major 3.32
%define xdg_name org.gnome.Calculator
%define _libexecdir %_prefix/libexec

Name: gnome-calculator
Version: %ver_major.2
Release: alt1

Summary: GTK+3 based desktop calculator
License: %gpl2plus
Group: Sciences/Mathematics
Url: https://wiki.gnome.org/Apps/Calculator

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

Obsoletes: gcalctool <= 6.6.2
Provides: gcalctool = 6.6.2

BuildRequires(pre): meson rpm-build-licenses rpm-build-gnome
BuildRequires: vala-tools >= 0.24
BuildRequires: yelp-tools libappstream-glib-devel desktop-file-utils
BuildRequires: libgtk+3-devel >= 3.20.0
BuildRequires: libgio-devel >= 2.48.0 libxml2-devel
BuildRequires: libmpfr-devel libgtksourceview4-devel >= 4.0.2
BuildRequires: libsoup-devel >= 2.42 libmpc-devel

%description
This package provides gcalctool, the calculator application that was
previously in the OpenWindows Deskset of the Solaris 8 operating system.

It incorporates a multiple precision arithmetic packages based on the work
of Professor Richard Brent.

A single graphics driver for GTK included with this package.

%prep
%setup
find ./ -name "*.stamp" -delete

%build
%meson
%meson_build

%install
%meson_install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_libexecdir/%name-search-provider
%_datadir/dbus-1/services/org.gnome.Calculator.SearchProvider.service
%_datadir/gnome-shell/search-providers/%xdg_name-search-provider.ini
%_desktopdir/%xdg_name.desktop
%_man1dir/%name.1.*
%_man1dir/gcalccmd.1.*
%config %_datadir/glib-2.0/schemas/org.gnome.calculator.gschema.xml
%_iconsdir/hicolor/*/*/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%doc NEWS


%changelog
* Wed Jun 26 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Sep 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Mon Jun 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Mon Feb 26 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt2
- rebuilt against libmpfr.so.6 (ALT #34582)

* Thu Nov 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Tue Sep 05 2017 Yuri N. Sedunov <aris@altlinux.org> 3.25.92-alt1
- 3.25.92

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Feb 14 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Tue Nov 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sun Aug 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt2
- use git snapshot with some *.ui that were missed in tarball

* Mon Aug 01 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Sat May 07 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Wed Jan 27 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Tue Nov 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed Jun 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Fri May 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Sun Oct 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon Sep 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.4-alt1
- 3.12.4

* Mon Jun 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.3-alt1
- 3.12.3

* Thu Apr 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Nov 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Sat Oct 19 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Sun Apr 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Feb 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.90-alt1
- gcalctool -> gnome-calculator

