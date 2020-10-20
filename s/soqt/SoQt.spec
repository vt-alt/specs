Name: soqt
Version: 1.6.0
Release: alt2
Summary: Qt GUI component toolkit library for Coin
License: BSD-3-Clause
Group: Development/Tools
Url: https://github.com/coin3d/soqt
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: cpack-src.tar
Source2: soanydata-src.tar
Source3: sogui-src.tar
Patch1:  SoQt-1.6.0-cmake.patch

Provides: SoQt = %EVR
Obsoletes: SoQt < %EVR
Requires: lib%name = %version-%release

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires(pre): qt5-base-devel
BuildRequires: gcc-c++
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: doxygen
BuildRequires: libX11-devel
BuildRequires: libcoin3d-devel

%description
SoQt is a Qt GUI component toolkit library for Coin.  It is also compatible
with SGI and TGS Open Inventor, and the API is based on the API of the
InventorXt GUI component toolkit.

%package -n lib%name
Summary: Shared libraries of SoQt
Group: System/Libraries
Requires: libcoin3d
Provides: libSoQt = %EVR
Obsoletes: libSoQt < %EVR

%description -n lib%name
SoQt is a Qt GUI component toolkit library for Coin.  It is also compatible
with SGI and TGS Open Inventor, and the API is based on the API of the
InventorXt GUI component toolkit.

This package contains shared libraries of SoQt.

%package -n lib%name-devel
Summary: Development files for SoQt
Group: Development/C++
Requires: lib%name = %version-%release
Requires: libcoin3d-devel
Provides: libSoQt-devel = %EVR
Obsoletes: libSoQt-devel < %EVR

%description -n lib%name-devel
SoQt is a Qt GUI component toolkit library for Coin.  It is also compatible
with SGI and TGS Open Inventor, and the API is based on the API of the
InventorXt GUI component toolkit.

This package contains development files for SoQt.

%package -n lib%name-devel-doc
Summary: Documentation for SoQt
Group: Development/Documentation
BuildArch: noarch
Provides: libSoQt-devel-doc = %EVR
Obsoletes: libSoQt-devel-doc < %EVR

%description -n lib%name-devel-doc
SoQt is a Qt GUI component toolkit library for Coin.  It is also compatible
with SGI and TGS Open Inventor, and the API is based on the API of the
InventorXt GUI component toolkit.

This package contains development documentation for SoQt.

%prep
%setup
%patch1 -p1
tar xf %SOURCE1
tar xf %SOURCE2
tar xf %SOURCE3

%build
%cmake -GNinja \
       -DSOQT_BUILD_DOCUMENTATION=TRUE \
       -DSOQT_BUILD_DOC_MAN=TRUE
%ninja_build -C BUILD

%install
%ninja_install -C BUILD
mv %buildroot%_includedir/Inventor %buildroot%_includedir/Coin4/
rm -rf %buildroot%_infodir
rm -rf %buildroot%_man3dir/misc.3*

%files

%files -n lib%name
%doc AUTHORS BUGS.txt FAQ NEWS README
%_libdir/*.so.*

%files -n lib%name-devel
%_datadir/SoQt
%_libdir/*.so
%_includedir/*
%_man3dir/*
%_pkgconfigdir/*
%_libdir/cmake/*

%files -n lib%name-devel-doc
%doc docs/*
%doc %_defaultdocdir/SoQt

%changelog
* Fri Oct 16 2020 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt2
- Remove /usr/share/man/man3/misc.3.xz conflicting with xinetd-devel.

* Fri Sep 18 2020 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- New version.
- Fix License tag, project URL and maintainer.

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt6
- Rebuilt with coin3d 3.1.3-alt5

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt5
- Added -g into compiler flags

* Sat Feb 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt4
- Rebuilt for debuginfo

* Mon Oct 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt3
- Rebuilt with set-versioned libXi

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2
- Rebuilt for soname set-versions

* Wed Mar 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1
- Version 1.5.0

* Mon Jan 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt4
- Rebuilt without libcoin3d-devel-static

* Mon May 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt3
- Rebuild for Qt4

* Wed May 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.M50.1
- Port for Branch 5.0

* Wed May 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt2
- lib%name-devel: added explicit conflict with xinetd-devel

* Sun May 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt0.M50.1
- Port for Branch 5.0

* Sun May 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.2
- Remove common package

* Sat May 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.1
- Disable static library
- Fix for x86_64

* Sat May 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus
