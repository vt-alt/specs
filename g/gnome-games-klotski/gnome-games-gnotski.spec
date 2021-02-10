%define _unpackaged_files_terminate_build 1

%define _name klotski
%define xdg_name org.gnome.Klotski
%define __name gnome-%_name
%define ver_major 3.38
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.2
Release: alt1

Summary: Derivative game from Klotski
Group: Games/Boards
License: GPLv3+
Url: https://wiki.gnome.org/Apps/Klotski

Source: ftp://ftp.gnome.org/pub/gnome/sources/%__name/%ver_major/%__name-%version.tar.xz

Provides:  %__name = %version-%release
Obsoletes: gnome-games-gnotski
Provides:  gnome-games-gnotski = %version-%release

%define glib_ver 2.40.0
%define gtk_ver 3.22.0

BuildRequires(pre): meson
BuildRequires: vala-tools
BuildRequires: yelp-tools libappstream-glib-devel desktop-file-utils
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libgee0.8-devel libgnome-games-support-devel
BuildRequires: librsvg-devel

%description
Gnome Klotski is a small game for GNOME. The idea is originally
from a game called "Klotski".

%prep
%setup -n %__name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %__name

%files -f gnome-%_name.lang
%attr(2711,root,games) %_bindir/%__name
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/%{xdg_name}*.*
%_man6dir/%__name.*
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml


%changelog
* Sun Nov 22 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Sat Oct 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Sat Sep 12 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Sun May 31 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.3-alt1
- 3.36.3

* Sat Apr 25 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Tue Mar 10 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Fri Feb 14 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.4-alt1
- 3.34.4

* Mon Jan 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.3-alt1
- 3.34.3

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Sat Mar 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Sat Sep 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Tue Nov 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sat May 07 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Fri Apr 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Thu Oct 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon Sep 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Thu Mar 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Fri Oct 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Sun Sep 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Sat Oct 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- first build for people/gnome



