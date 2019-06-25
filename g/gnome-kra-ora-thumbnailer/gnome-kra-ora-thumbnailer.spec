%define ver_major 1.4
%define _libexecdir %_prefix/libexec

Name: gnome-kra-ora-thumbnailer
Version: %ver_major
Release: alt1

Summary: Thumbnailer for Krita and MyPaint images
License: LGPLv2+
Group: Graphical desktop/GNOME
Url: https://live.gnome.org

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildRequires: libgio-devel libgdk-pixbuf-devel libxml2-devel libarchive-devel >= 3.1

%description
This package provides a thumbnailer for Krita and MyPaint images.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/gnome-openraster-thumbnailer
%_bindir/gnome-kra-thumbnailer
%_datadir/thumbnailers/gnome-openraster-thumbnailer.thumbnailer
%_datadir/thumbnailers/gnome-kra-thumbnailer.thumbnailer
%doc README AUTHORS NEWS

%changelog
* Thu Jun 20 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt1
- 1.4

* Thu Dec 19 2013 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt1
- first build for Sisyphus


