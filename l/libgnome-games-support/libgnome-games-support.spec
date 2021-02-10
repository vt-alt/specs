%define ver_major 1.8
%define api_ver 1

Name: libgnome-games-support
Version: %ver_major.0
Release: alt1

Summary: Shared library for GNOME games
Group: System/Libraries
License: LGPL-3.0

Url: https://wiki.gnome.org/Apps/Games
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.40
%define gtk_ver 3.20.0
%define vala_ver 0.39.6

BuildRequires(pre): meson
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libgee0.8-devel vala-tools >= %vala_ver

%description
%name provides code that's useful for different GNOME games.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Requires: libgee0.8-devel

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%_libdir/%name-%api_ver.so.*
%doc README NEWS

%files devel
%_includedir/gnome-games-support-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%_vapidir/%name-%api_ver.vapi


%changelog
* Sat Sep 12 2020 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Fri Mar 27 2020 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Fri Mar 06 2020 Yuri N. Sedunov <aris@altlinux.org> 1.6.0.1-alt1
- 1.6.0.1 (ported to Meson build system)

* Tue Sep 03 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.4-alt1
- 1.4.4

* Fri Dec 21 2018 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Mon Aug 13 2018 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Thu Mar 22 2018 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Sat Mar 10 2018 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Sat Sep 09 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Fri Jun 16 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Tue Oct 25 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0 (renamed to libgnome-games-support)

* Sat May 07 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Fri Apr 08 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0

* Wed Mar 09 2016 Yuri N. Sedunov <aris@altlinux.org> 0.91-alt1
- 0.91

* Fri Sep 25 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt1
- first build for Sisyphus

