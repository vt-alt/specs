Name:    coin3d
Version: 4.0.0
Release: alt1
Summary: OpenGL-based, 3D graphics library
License: BSD-3-Clause
Group:   System/Libraries
Url:     https://github.com/coin3d/coin
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

Patch1: 0002-Added-c-suffix-to-SO_VERSION.patch
Patch2: 0003-Drop-use-of-cpack.patch
Patch3: 01_convert_old_patches.patch

Requires: lib%name = %version-%release
Requires: %name-common = %version-%release

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: boost-devel
BuildRequires: bzlib-devel
BuildRequires: fontconfig-devel
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: libexpat-devel
BuildRequires: libfreetype-devel
BuildRequires: zlib-devel

%description
Coin is an OpenGL-based, 3D graphics library that has its roots in the
Open Inventor 2.1 API, which Coin still is compatible with.

If you are not familiar with Open Inventor, it is a scene-graph based,
retain-mode, rendering and model manipulation, C++ class library,
originally designed by SGI.  It quickly became the de facto standard
graphics library for 3D visualization and visual simulation software
in the scientific and engineering community after its release.  It
also became the basis for the VRML1 file format standard.

%package -n lib%name
Summary: Shared libraries of Coin3D
Group: System/Libraries
Conflicts: %name < %version-%release

%description -n lib%name
Coin is an OpenGL-based, 3D graphics library that has its roots in the
Open Inventor 2.1 API, which Coin still is compatible with.

If you are not familiar with Open Inventor, it is a scene-graph based,
retain-mode, rendering and model manipulation, C++ class library,
originally designed by SGI.  It quickly became the de facto standard
graphics library for 3D visualization and visual simulation software
in the scientific and engineering community after its release.  It
also became the basis for the VRML1 file format standard.

This package contains shared libraries of Coin3D.

%package -n lib%name-devel
Summary: Development files for Coin3D
Group: Development/C++
Requires: lib%name = %version-%release
Requires: %name-common = %version-%release
Conflicts: %name < %version-%release
Conflicts: libInventor-devel

%description -n lib%name-devel
Coin is an OpenGL-based, 3D graphics library that has its roots in the
Open Inventor 2.1 API, which Coin still is compatible with.

If you are not familiar with Open Inventor, it is a scene-graph based,
retain-mode, rendering and model manipulation, C++ class library,
originally designed by SGI.  It quickly became the de facto standard
graphics library for 3D visualization and visual simulation software
in the scientific and engineering community after its release.  It
also became the basis for the VRML1 file format standard.

This package contains development files for Coin3D.

%package -n lib%name-devel-doc
Summary: Documentation for Coin3D
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-doc
Coin is an OpenGL-based, 3D graphics library that has its roots in the
Open Inventor 2.1 API, which Coin still is compatible with.

If you are not familiar with Open Inventor, it is a scene-graph based,
retain-mode, rendering and model manipulation, C++ class library,
originally designed by SGI.  It quickly became the de facto standard
graphics library for 3D visualization and visual simulation software
in the scientific and engineering community after its release.  It
also became the basis for the VRML1 file format standard.

This package contains development documentation for Coin3D.

%package common
Summary: Architecture independent files of Coin3D
Group: Development/Documentation
BuildArch: noarch

%description common
Coin is an OpenGL-based, 3D graphics library that has its roots in the
Open Inventor 2.1 API, which Coin still is compatible with.

If you are not familiar with Open Inventor, it is a scene-graph based,
retain-mode, rendering and model manipulation, C++ class library,
originally designed by SGI.  It quickly became the de facto standard
graphics library for 3D visualization and visual simulation software
in the scientific and engineering community after its release.  It
also became the basis for the VRML1 file format standard.

This package contains architecture independent files of Coin3D.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%cmake -GNinja \
       -DCOIN_BUILD_DOCUMENTATION=TRUE \
       -DCOIN_BUILD_DOCUMENTATION_MAN=TRUE \
       -DHAVE_MULTIPLE_VERSION=TRUE \
       -DUSE_EXTERNAL_EXPAT=TRUE
%ninja_build -C BUILD

%install
%ninja_install -C BUILD

%files -n lib%name
%doc AUTHORS ChangeLog README{,.UNIX} THANKS FAQ*
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/*
%_libdir/*.so
%_pkgconfigdir/*
%_libdir/cmake/*
%_includedir/*

%files -n lib%name-devel-doc
%doc docs/*
%doc %_defaultdocdir/Coin4
%_man3dir/*
%exclude %_man3dir/details.3*

%files common
%_datadir/Coin4

%changelog
* Thu Sep 17 2020 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- New version.

* Tue Dec 08 2015 Andrey Cherepanov <cas@altlinux.org> 3.1.3-alt10
- Add debugerror.h include in base include file (for freecad build)

* Thu Feb 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt9
- Fixed build with gcc 4.8

* Tue Oct 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt8
- Fixed build with gcc 4.7

* Sun Feb 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt7
- libcoin3d-devel-doc: avoid conflict with libtrilinos10-devel-doc

* Fri Feb 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt6
- Built without OSMesa

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt5
- Removed %name package (ALT #25523)

* Sat Feb 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt4
- Rebuilt for debuginfo

* Mon Jan 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt3
- Moved devel man pages into devel-doc package

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt2
- Rebuilt for soname set-versions

* Wed Mar 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt1
- Version 3.1.3

* Wed Feb 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt3
- Renamed coin.m4 -> coin3d.m4

* Mon Jan 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt2
- Removed %_man3dir/deprecated.3*

* Fri Jan 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1
- Version 3.1.2

* Tue May 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt3
- lib%name-devel: explicit conflict with libInventor-devel

* Sun May 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1.M50.1
- Port for Branch 5.0

* Sun May 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt2.2
- Move default config file into package %name

* Sat May 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt2.1
- Fix pkgconfig file for x86_64

* Sat May 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt2
- Fix for x86_64

* Sat May 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt0.M50.1
- Port for Branch 5.0

* Sat May 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus

