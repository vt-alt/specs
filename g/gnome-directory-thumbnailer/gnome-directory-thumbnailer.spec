%define ver_major 0.1
%define _libexecdir %_prefix/libexec

Name: gnome-directory-thumbnailer
Version: %ver_major.11
Release: alt1

Summary: GNOME thumbnailer to generate thumbnails for directories
License: LGPLv2.1+
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Projects/GnomeDirectoryThumbnailer

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildRequires: intltool libgio-devel >= 2.36.0 libgtk+3-devel >= 3.0 libgnome-desktop3-devel

%description
This package provides a GNOME thumbnailer utility which will generate a
thumbnail for a directory.
It is intended to be called by gnome-desktops thumbnailer code, but
can be called manually as well.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_datadir/thumbnailers/%name.thumbnailer
%doc README AUTHORS NEWS

%changelog
* Tue Sep 03 2019 Yuri N. Sedunov <aris@altlinux.org> 0.1.11-alt1
- 0.1.11

* Sun Feb 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.10-alt2
- rebuilt against libgnome-desktop-3.so.17

* Thu Jan 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.10-alt1
- 0.1.10

* Sun Apr 30 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.9-alt1
- 0.1.9

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 0.1.8-alt1
- 0.1.8

* Fri Feb 05 2016 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt1
- 0.1.7

* Thu Sep 24 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt2
- rebuilt against libgnome-desktop-3.so.12

* Tue Jun 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- 0.1.6

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- 0.1.5

* Sun Jan 25 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- 0.1.4

* Wed May 28 2014 Yuri N. Sedunov <aris@altlinux.org> 0.1.3-alt1
- 0.1.3

* Fri Mar 21 2014 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt2
- rebuilt against libgnome-desktop-3.so.10

* Mon Feb 24 2014 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- first build for Sisyphus



