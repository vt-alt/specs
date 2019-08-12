%define ver_major 0.5
%define gst_api_ver 1.0

Name: gnome-video-effects
Version: %ver_major.0
Release: alt1

Summary: A collection of GStreamer video effects
License: GPLv2
Group: Video
Url: https://wiki.gnome.org/Projects/GnomeVideoEffects

BuildArch: noarch

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
Requires: frei0r-plugins

BuildRequires(pre): meson

%description
A collection of GStreamer video effects to be used in different GNOME Modules.

%package devel
Summary: Development files for %name
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
This package provides .pc file needed to build apllications using %name.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%dir %_datadir/gnome-video-effects
%_datadir/gnome-video-effects/*.effect
%doc AUTHORS README NEWS

%files devel
%_datadir/pkgconfig/%name.pc

%changelog
* Tue Aug 06 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Thu Feb 09 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Mon Mar 10 2014 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Tue Nov 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt2
- frei0r-plugins are required for some effects

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Thu Mar 10 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Wed Jan 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus
