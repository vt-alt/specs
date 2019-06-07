%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 3.32
%define _name org.gnome.MultiWriter

Name: gnome-multi-writer
Version: %ver_major.1
Release: alt1

Summary: Write an ISO file to multiple USB devices at once
Group: Archiving/Backup
License: GPLv2+
Url: https://wiki.gnome.org/Apps/MultiWriter

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

Requires: gnome-icon-theme-extras

%define gtk_ver 3.12.0
%define gusb_ver 0.2.7

BuildRequires(pre): meson
BuildRequires: libappstream-glib-devel docbook-utils yelp-tools
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libgusb-devel >= %gusb_ver
BuildRequires: libudisks2-devel libgudev-devel libcanberra-gtk3-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libpolkit-devel

%description
GNOME MultiWriter can be used to write an ISO file to multiple
USB devices simultaneously.

%prep
%setup

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%meson
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_libexecdir/%name-probe
%_desktopdir/%_name.desktop
%_datadir/glib-2.0/schemas/%_name.gschema.xml
%_datadir/polkit-1/actions/%_name.policy
%_iconsdir/hicolor/*/apps/*
%_man1dir/%name.1.*
%_datadir/metainfo/%_name.appdata.xml
%doc README.md AUTHORS RELEASE


%changelog
* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Fri Mar 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Wed Oct 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Fri Feb 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.90-alt1
- 3.15.90

* Mon Jan 19 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.4-alt1
- 3.15.4 release

* Mon Jan 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.3-alt0.1
- 3.15.3 snapshot

* Mon Jan 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.2-alt1
- first build for Sisyphus

