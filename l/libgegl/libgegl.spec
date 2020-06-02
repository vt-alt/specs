%define rname gegl
%define api_ver 0.4

Name: lib%rname
Version: %api_ver.22
Release: alt1
Summary: A graph based image processing framework
License: %gpllgpl3plus
Group: System/Libraries
Url: http://www.gimp.org

Source: %rname-%version.tar
Patch: %rname-%version-alt.patch

BuildRequires(pre): rpm-build-licenses meson
BuildRequires: asciidoc enscript gcc-c++ graphviz gtk-doc libSDL-devel libavformat-devel libbabl-devel libexiv2-devel
BuildRequires: libgexiv2-devel libgomp-devel libgtk+3-devel libjasper-devel libjpeg-devel libjson-glib-devel
BuildRequires: libpoly2tri-c-devel libraw-devel librsvg-devel libspiro-devel libsuitesparse-devel libswscale-devel
BuildRequires: libtiff-devel libv4l-devel libwebp-devel openexr-devel ruby vala-tools gobject-introspection-devel w3m
BuildRequires: python-module-pygobject3-common-devel libpoppler-glib-devel libspiro-devel liblua-devel libSDL2-devel
%ifarch %arm aarch64 %ix86 x86_64
BuildRequires: libluajit-devel
%endif

%description
GEGL (Generic Graphics Library) is a graph based image processing framework.
GEGLs original design was made to scratch GIMPs itches for a new
compositing and processing core. This core is being designed to have
minimal dependencies. and a simple well defined API.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: %name = %version-%release
Provides: %name-gir-devel = %version-%release
Obsoletes: %name-gir-devel < %version-%release

%description devel
This package contains the libraries and header files needed for
developing with %name.

%package gir
Summary: GObject introspection data for the GEGL
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GEGL library.

%prep
%setup -n %rname-%version
%patch -p1

%build
%meson \
	-Ddocs=false
%meson_build -v

%install
%meson_install

rm -f %buildroot%_libdir/%rname-%api_ver/*.la

%find_lang %rname-%api_ver

%files -f %rname-%api_ver.lang
%_bindir/%rname
%_bindir/%rname-imgcmp
%_libdir/%name-%api_ver.so.*
%_libdir/%name-sc-%api_ver.so
%_libdir/%name-npd-%api_ver.so
%dir %_libdir/%rname-%api_ver
%_libdir/%rname-%api_ver/*.so
%_libdir/%rname-%api_ver/grey2.json
%ifarch %arm aarch64 %ix86 x86_64
%_datadir/%rname-%api_ver
%endif

%files devel
%_includedir/%rname-%api_ver
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%rname-%api_ver.pc
%_pkgconfigdir/%rname-sc-%api_ver.pc
%_vapidir/%rname-%api_ver.deps
%_vapidir/%rname-%api_ver.vapi
%_girdir/Gegl-%api_ver.gir

%files gir
%_typelibdir/Gegl-%api_ver.typelib

%changelog
* Mon Mar 02 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.4.22-alt1
- 0.4.22

* Mon Mar 02 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.4.20-alt1
- 0.4.20

* Fri Nov 01 2019 Valery Inozemtsev <shrek@altlinux.ru> 0.4.18-alt1
- 0.4.18

* Thu Jun 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 0.4.16-alt1
- 0.4.16

* Mon Apr 08 2019 Valery Inozemtsev <shrek@altlinux.ru> 0.4.14-alt1
- 0.4.14

* Mon Nov 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.4.12-alt1
- 0.4.12

* Fri Sep 14 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.4.8-alt2
- rebuild with libraw 0.19

* Fri Aug 31 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.4.8-alt1.S1
- 0.4.8

* Thu Jul 05 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.4.4-alt1.S1
- 0.4.4

* Tue Jun 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.4.2-alt1.S1
- rebuild with libva 2.1.0

* Wed Jun 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Tue May 08 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Mon Jun 05 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt5
- rebuild with ffmpeg 3.3.1

* Mon Jan 23 2017 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt4
- rebuild with libopenraw 0.1.0

* Mon Nov 23 2015 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt3
- rebuilt for gcc5 C++11 ABI

* Wed Jun 04 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt2
- rebuilt with libav10

* Wed Apr 04 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Tue Aug 02 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.1.6-alt2
- disabled ffmpeg

* Tue Feb 15 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Tue Oct 19 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.2-alt2
- updated build dependencies

* Wed Mar 31 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.2-alt1
- 0.1.2

* Mon Jan 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.0-alt2
- updated build dependencies

* Mon Oct 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1.0-alt1
- 0.1.0

* Mon Jul 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.0.22-alt4
- fixed build with fresh gcc

* Mon Jul 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.0.22-alt3
- disabled docs

* Tue Jun 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.0.22-alt2
- rebuild with libpng12 1.2.37-alt2

* Mon Apr 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.0.22-alt0.M50.1
- build for branch 5.0

* Mon Feb 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.0.22-alt1
- 0.0.22

* Thu Feb 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.0.20-alt4
- rebuild with libavcodec.so.52

* Thu Jan 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.0.20-alt3
- drop fill plugin

* Fri Nov 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.20-alt2
- rebuild

* Fri Oct 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.20-alt1
- 0.0.20

* Thu Oct 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.18-alt2
- disabled workshop operations
- build docs

* Wed Oct 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.18-alt1
- initial release

