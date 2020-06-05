Name: libGLU
Version: 9.0.1
Release: alt1
Epoch: 4
License: MIT
Summary: Mesa libGLU runtime library
Group: System/Libraries
Url: http://www.mesa3d.org

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ libGL-devel

%description
Mesa %name runtime library

%package devel
Summary: Mesa %name development package
Group: Development/C
Requires: %name = %epoch:%version-%release

%description devel
Mesa libGLU development package

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/%name.so.*

%files devel
%_includedir/GL/glu.h
%_includedir/GL/glu_mangle.h
%_libdir/%name.so
%_pkgconfigdir/glu.pc

%changelog
* Mon Mar 30 2020 Valery Inozemtsev <shrek@altlinux.ru> 4:9.0.1-alt1
- 9.0.1

* Mon Sep 10 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:9.0.0-alt1
- 9.0.0

