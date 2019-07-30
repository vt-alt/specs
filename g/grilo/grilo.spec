%define ver_major 0.3
%define api_ver %ver_major
%def_enable gtk_doc
%def_disable check

Name: grilo
Version: %ver_major.9
Release: alt1

Summary: Content discovery framework
Group: Sound
License: LGPLv2+
Url: https://wiki.gnome.org/Projects/Grilo

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define __python %nil

BuildRequires(pre): meson rpm-build-python3 rpm-build-gir
BuildRequires: gnome-common intltool >= 0.40.0
BuildRequires: libgio-devel >= 2.44
BuildRequires: libxml2-devel
BuildRequires: libgtk+3-devel >= 3.0
BuildRequires: libsoup-devel >= 2.41.3 libsoup-gir-devel
BuildRequires: liboauth-devel
BuildRequires: vala-tools >= 0.27 libvala-devel
BuildRequires: gtk-doc >= 1.10
BuildRequires: gobject-introspection-devel >= 0.9.0
BuildRequires: libtotem-pl-parser-devel >= 3.4.1
BuildRequires: gstreamer1.0-devel

%description
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains the core library and elements.

%package -n lib%name
Summary: Libraries files for Grilo framework
Group: System/Libraries

%description -n lib%name
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains the core library.

%package -n lib%name-devel
Summary: Development files for Grilo framework
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains the core library and elements, as well as
general and API documentation.

%package devel-doc
Summary: Development documentation for %name
Group: Development/GNOME and GTK+
Conflicts: lib%name < %version-%release
BuildArch: noarch

%description devel-doc
This package provides development documentation for %name.

%package -n lib%name-gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the %name library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %name library

%package tools
Summary: Tools for the %name library
Group: Sound
Requires: lib%name = %version-%release

%description tools
Tools for the %name library

%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup

%build
%meson \
	-Denable-vala=true \
	-Denable-gtk-doc=true \
	-Denable-introspection=true \
	-Denable-grl-net=true \
	-Denable-grl-pls=true \
	-Denable-test-ui=true

%meson_build

%install
%meson_install
mkdir -p %buildroot%_libdir/grilo-%ver_major %buildroot%_datadir/grilo-%ver_major/plugins

%find_lang %name

# Remove files that will not be packaged
#rm -f %buildroot%_bindir/grilo-simple-playlist

%check
# grilo-plugins should be installed for check
%meson_test

%files tools
%doc AUTHORS COPYING NEWS README* TODO
%_bindir/grl-inspect-%api_ver
%_bindir/grl-launch-%api_ver
%_bindir/grilo-test-ui-%api_ver
%_man1dir/*

%files -n lib%name -f %name.lang
%_libdir/*.so.*
%dir %_libdir/grilo-%ver_major
%dir %_datadir/grilo-%ver_major/plugins

%files -n lib%name-devel
%_includedir/%name-%api_ver/
%_libdir/*.so
%_pkgconfigdir/*-%api_ver.pc
%_vapidir/*

%files -n lib%name-gir
%_typelibdir/Grl-%api_ver.typelib
%_typelibdir/GrlNet-%api_ver.typelib
%_typelibdir/GrlPls-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Grl-%api_ver.gir
%_girdir/GrlNet-%api_ver.gir
%_girdir/GrlPls-%api_ver.gir

%if_enabled gtk_doc
%files devel-doc
%_gtk_docdir/%name/
%endif

%changelog
* Wed Jul 17 2019 Yuri N. Sedunov <aris@altlinux.org> 0.3.9-alt1
- 0.3.9

* Mon Jul 15 2019 Yuri N. Sedunov <aris@altlinux.org> 0.3.8-alt1
- 0.3.8

* Mon Nov 19 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.7-alt1
- 0.3.7

* Fri Jul 27 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- 0.3.6

* Tue Jul 17 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt1
- 0.3.5

* Thu Aug 24 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- 0.3.4

* Tue Feb 14 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Sat Sep 10 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Fri Jun 17 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Wed Feb 03 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Sat Dec 19 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.15-alt1
- 0.2.15

* Sat Sep 12 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.14-alt1
- 0.2.14

* Mon Sep 07 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.13-alt1
- 0.2.13

* Tue Feb 17 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.12-alt1
- 0.2.12

* Wed Aug 27 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.11-alt1
- 0.2.11

* Wed Mar 19 2014 Alexey Shabalin <shaba@altlinux.ru> 0.2.10-alt1
- 0.2.10

* Wed Feb 19 2014 Alexey Shabalin <shaba@altlinux.ru> 0.2.9-alt1
- 0.2.9

* Tue Oct 01 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.7-alt2
- fixed build with vala-0.22

* Thu Sep 19 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.7-alt1
- 0.2.7

* Thu May 16 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.6-alt1
- 0.2.6

* Mon Apr 08 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.5-alt1
- 0.2.5

* Tue Dec 04 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Mon Nov 12 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.3-alt1
- 0.2.3

* Mon Oct 08 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.2-alt1
- 0.2.2

* Wed Sep 19 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Fri May 25 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.19-alt1
- 0.1.19

* Thu Mar 29 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.18-alt2
- rebuild with vala-0.16

* Tue Jan 10 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.18-alt1
- 0.1.18

* Wed Oct 26 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.17-alt2
- rebuild with vala-0.14

* Wed Sep 14 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.17-alt1
- 0.1.17

* Tue Jul 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.16-alt1
- 0.1.16

* Mon May 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.15-alt1
- initial build for ALT Linux Sisyphus
