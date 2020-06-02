%def_disable snapshot

Name: mypaint
Version: 2.0.1
Release: alt0.1.p9

Summary: A simple paint program
Group: Graphics
License: GPL-2.0-or-later and ISC and Public-domain
Url: http://mypaint.org/

%if_disabled snapshot
Source: https://github.com/%name/%name/releases/download/v%version/%name-%version.tar.xz
%else
# VCS: https://github.com/mypaint/mypaint
Source: %name-%version.tar
%endif

%define mypaintlib_ver 1.6

Requires: %name-data = %version-%release
Requires: mypaint-brushes >= 2.0
Requires: typelib(MyPaint) = 1.6

%add_python3_path %_datadir/%name %_libdir/%name

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: lib%name-devel >= %mypaintlib_ver
BuildRequires: gcc-c++ libgomp-devel swig libgtk+3-devel
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-numpy libnumpy-py3-devel
BuildRequires: libpng-devel libjson-c-devel liblcms2-devel
BuildRequires: gobject-introspection-devel python3-module-pygobject3-devel
BuildRequires: pkgconfig(mypaint-brushes-2.0)
BuildRequires: libnumpy-devel

%description
MyPaint is a simple drawing and painting program that works well with
Wacom-style graphics tablets. Its main features are a highly configurable
brush engine, speed, and a fullscreen mode which allows artists to fully
immerse themselves in their work.

%package data
Summary: A simple paint program
Group: Graphics
BuildArch: noarch

%description data
Mypaint is a fast and easy/simple painter program. It comes with a large
brush collection including charcoal and ink to emulate real media, but the
highly configurable brush engine allows you to experiment with your own
brushes and with not-quite-natural painting.

This package contains the data files needed for the program.

%package -n lib%name-devel-static
Summary: Static mypaint brush library
Group: Development/C

%description -n lib%name-devel-static
Mypaint is a fast and easy/simple painter program. It comes with a large
brush collection including charcoal and ink to emulate real media, but the
highly configurable brush engine allows you to experiment with your own
brushes and with not-quite-natural painting.

This package provides files needed for development applications statically linked
with mypaint brush library.

%add_python_lib_path %_datadir/%name

%prep
%setup
# fix libdir
subst "s|prefix, 'lib'|prefix, '%_lib'|" mypaint.py

%build
%python3_build

%install
%python3_install --install-lib=%_libdir/%name
%find_lang --output=%name.lang %name

%files -f %name.lang
%_bindir/*
%_libdir/%name/

%files data
%_datadir/%name/
%_datadir/thumbnailers/%name-ora.thumbnailer
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/*
%_datadir/metainfo/mypaint.appdata.xml
%doc README.md Changelog.md Licenses.md

%changelog
* Sat May 30 2020 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt0.1.p9
- Backport new versioon to p9 branch.

* Fri May 29 2020 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Tue Mar 17 2020 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Tue May 15 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt2
- updated to v1.2.1-4-g498cb3f
- removed libmypaint.mo to avoid conflict with standalone libmypaint used by gimp-2.10 now

* Fri Feb 10 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Sun Aug 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt2
- fixed https://github.com/mypaint/mypaint/issues/634 (ALT #32415)

* Sat Jan 16 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Fri Jan 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Sun Apr 15 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt2
- rebuilt to remove libpython2.7 dependency

* Thu Nov 24 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.1-alt3.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt3
- replaced obsolete python-module-json by python-modules-json

* Mon May 02 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt2
- rebuild against current numpy

* Sat Mar 05 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Tue Jan 04 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt2
- explicitly requires python-module-json

* Sun Dec 19 2010 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- 0.9.0 (ALT #24610)

* Mon Jul 26 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt2
- rebuild against current numpy (closes #23769)

* Mon Mar 01 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2

* Mon Feb 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- new version

* Fri Feb 19 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt2
- %%_bindir/mypaint moved to main arch dependent package

* Sun Jan 31 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Fri Jan 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- first build for Sisyphus

