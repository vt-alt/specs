%def_with bundled_libs
%def_with glvnd
%define oname freecad
%define ldir %_libdir/%oname
%ifndef build_parallel_jobs
%define build_parallel_jobs 7
%endif

%define vtkver 8.1

# Last number in version is computed by command:
# git rev-list --count remotes/upstream/releases/FreeCAD-0-17

Name:    freecad
Version: 0.18.4
Release: alt1.1.p9
Epoch:   1
Summary: OpenSource 3D CAD modeller
License: LGPL-2.0+
Group:   Graphics
Url:     http://free-cad.sourceforge.net/
# VCS:   https://github.com/FreeCAD/FreeCAD
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: freecad.1

%if_without bundled_libs
Patch1: %name-remove-3rdParty.patch
Patch2: %name-build-with-external-smesh.patch
%endif

# branch releases/FreeCAD-0-17
#Patch3: upstream.patch
Patch4: %name-desktop-ru.patch

Provides:  free-cad = %version-%release
Obsoletes: free-cad < %version-%release

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-xdg
BuildRequires(pre): rpm-build-ninja
BuildRequires: qt5-base-devel
BuildRequires: qt5-assistant
BuildRequires: qt5-designer
BuildRequires: qt5-sql-sqlite3
BuildRequires: qt5-svg-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-tools-devel-static
BuildRequires: qt5-webkit-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-phonon-devel
BuildRequires: python-module-PySide2
BuildRequires: pyside2-tools-python2
BuildRequires: python-module-shiboken2-devel
%define qmake %qmake_qt5
%define qtbindir %_qt5_bindir
BuildRequires: python-devel swig gcc-fortran libf2c-ng-devel chrpath
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-geometry-devel
BuildRequires: boost-polygon-devel
BuildRequires: boost-program_options-devel
BuildRequires: boost-python-devel
BuildRequires: boost-signals-devel
BuildRequires: libcoin3d-devel
#BuildRequires: libSoQt-devel
BuildRequires: zlib-devel
BuildRequires: libopencv2-devel libxerces-c-devel gcc-c++
BuildRequires: java-devel-default
BuildRequires: libXxf86misc-devel
BuildRequires: OCE-devel libgts-devel
BuildRequires: libode-devel libann-devel
BuildRequires: doxygen graphviz
BuildRequires: eigen3
#BuildRequires: python-module-pivy
BuildRequires: libnumpy-devel
BuildRequires: boost-interprocess-devel
BuildRequires: gdb
BuildRequires: libvtk%{vtkver}-devel vtk%{vtkver}-examples vtk%{vtkver}-python
BuildRequires: libhdf5-devel libhdf5-mpi-devel
BuildRequires: libmed-devel libspnav-devel
BuildRequires: python-module-matplotlib
BuildRequires: libkdtree++-devel
%if_without bundled_libs
BuildRequires: libsmesh-devel libnetgen-devel
%endif
%if_with glvnd
BuildRequires: libglvnd-devel
%else
Requires: libEGL-devel libGLU-devel
%endif
#BuildRequires: texlive-extra-utils

%py_requires pivy
%py_provides Fem FreeCAD FreeCADGui Mesh Part MeshPart Drawing ImportGui
%py_provides PartGui Sketcher TestSketcherApp Robot RobotGui SketcherGui
%py_provides ImageGui PartDesignGui _PartDesign
%add_python_req_skip pyopencl IfcImport Units
%add_findreq_skiplist %ldir/Mod/*

%description
FreeCAD will be a general purpose 3D CAD modeler. FreeCAD is aimed directly at
mechanical engineering and product design but also fits in a wider range of uses
around engineering, such as architecture or other engineering specialties.

FreeCAD features tools similar to Catia, SolidWorks or Solid Edge, and therefore
also falls into the category of MCAD, PLM, CAx and CAE. It will be a feature
based parametric modeler with a modular software architecture which makes it
easy to provide additional functionality without modifying the core system.

%package docs
Summary: Documentation for FreeCAD
Group: Documentation
#BuildArch: noarch
Provides:  free-cad-docs = %version-%release
Obsoletes: free-cad-docs < %version-%release
Requires: qt5-assistant

%description docs
FreeCAD will be a general purpose 3D CAD modeler. FreeCAD is aimed directly at
mechanical engineering and product design but also fits in a wider range of uses
around engineering, such as architecture or other engineering specialties.

FreeCAD features tools similar to Catia, SolidWorks or Solid Edge, and therefore
also falls into the category of MCAD, PLM, CAx and CAE. It will be a feature
based parametric modeler with a modular software architecture which makes it
easy to provide additional functionality without modifying the core system.

This package contains documentation for FreeCAD.

%prep
%setup
%if_without bundled_libs
# Removed bundled libraries
%patch1 -p1
%patch2 -p1
rm -rf src/3rdParty
%endif

#patch3 -p1
%patch4 -p1

%build
export PATH=$PATH:%_qt5_bindir
%add_optflags -Wl,-rpath,%ldir/lib
%cmake_insource -GNinja \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_DATADIR=%ldir \
	-DCMAKE_INSTALL_DOCDIR=%ldir/doc \
	-DCMAKE_INSTALL_LIBDIR=%ldir/lib \
	-DOPENMPI_INCLUDE_DIRS=%_libdir/openmpi/include \
	-DFREECAD_LIBPACK_USEPYSIDE=OFF \
	-DBUILD_QT5=ON \
%if_without bundled_libs
	-DFREECAD_USE_EXTERNAL_SMESH=ON \
	-DSMESH_DIR=%_libdir \
	-DSMESH_INCLUDE_DIR=%_includedir/smesh \
	-DSMESH_VERSION_MAJOR=7 \
%endif
%if_with glvnd
	-DOpenGL_GL_PREFERENCE=GLVND \
%endif
	-DFREECAD_USE_EXTERNAL_PIVY=ON 

# Fix Unknown release and repository URL
sed -i 's,FCRevision      \"Unknown\",FCRevision      \"%{release} (Git)\",' src/Build/Version.h
sed -i 's,FCRepositoryURL \"Unknown\",FCRepositoryURL \"git://github.com/FreeCAD/FreeCAD.git master\",' src/Build/Version.h

export NPROCS=%build_parallel_jobs
%ninja_build

%install
%ninja_install

# binaries
mkdir -p %buildroot%ldir/bin
mv %buildroot%_bindir/* %buildroot%ldir/bin
ln -s ../%_lib/%name/bin/FreeCAD %buildroot%_bindir/freecad
ln -s ../%_lib/%name/bin/FreeCADCmd %buildroot%_bindir/freecadcmd
ln -s ../%_lib/%name/bin/FreeCAD %buildroot%_bindir/FreeCAD
ln -s ../%_lib/%name/bin/FreeCADCmd %buildroot%_bindir/FreeCADCmd

# icons
for size in 16 32 48 64
do
  install -Dm0644 %buildroot%ldir/%name-icon-${size}.png %buildroot%_iconsdir/hicolor/${size}x${size}/apps/%name.png
done
install -Dm0644 %buildroot%ldir/%name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
install -Dm0644 %buildroot%ldir/%name.xpm %buildroot%_pixmapsdir/%name.xpm

# manpage
install -Dm0644 %SOURCE1 %buildroot%_man1dir/%name.1

# stuff
cp -af %buildroot%_prefix/Mod/* %buildroot%ldir/Mod
rm -rf %buildroot%_prefix/Mod
cp -af %buildroot%_prefix/Ext/ %buildroot%ldir/Ext
rm -rf %buildroot%_prefix/Ext

# l10n
%find_lang --with-kde %name

%files -f %name.lang
%doc ChangeLog.txt README.md
%doc %ldir/License.txt
%dir %ldir
%_bindir/*
%ldir/bin
%ldir/lib
%ldir/Gui
%ldir/Ext
%ldir/Mod
%ldir/examples
%ldir/*.png
%ldir/*.svg
%ldir/*.xpm
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_man1dir/*
%_xdgdatadir/mime/packages/*
%_pixmapsdir/%name.xpm
%_iconsdir/hicolor/scalable/apps/*.svg
%_datadir/metainfo/*.appdata.xml

%files docs
%ldir/doc

%changelog
* Wed May 27 2020 Andrey Cherepanov <cas@altlinux.org> 1:0.18.4-alt1.1.p9
- Backport to p9 branch.

* Mon May 25 2020 Andrey Cherepanov <cas@altlinux.org> 1:0.18.4-alt2
- Fix Unknown release and repository URL.
- Build with Qt5.
- Fix License tag according to upstream information and SPDX.
- Build using ninja-build.

* Tue Apr 14 2020 Andrey Cherepanov <cas@altlinux.org> 1:0.18.4-alt0.1.p9
- Backport new version to p9 branch.

* Sun Oct 27 2019 Andrey Cherepanov <cas@altlinux.org> 1:0.18.4-alt1
- New version.

* Thu Jul 18 2019 Andrey Cherepanov <cas@altlinux.org> 1:0.18.3-alt1
- New version.

* Fri May 24 2019 Slava Aseev <ptrnine@altlinux.org> 1:0.18.2-alt3
- Rebuild with vtk8.2

* Tue May 21 2019 Andrey Cherepanov <cas@altlinux.org> 1:0.18.2-alt2
- Use desktop file and mime data from upstream (ALT #36762).
- Add Russian localization of desktop file as patch.

* Sun May 12 2019 Andrey Cherepanov <cas@altlinux.org> 1:0.18.2-alt1
- New version.

* Fri Apr 05 2019 Andrey Cherepanov <cas@altlinux.org> 1:0.18.1-alt1
- New version (ALT #36524).

* Fri Mar 22 2019 Andrey Cherepanov <cas@altlinux.org> 1:0.18-alt1
- New version (ALT #36332).

* Thu Nov 22 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.17.13543-alt1
- Version 0.17 with changes from releases/FreeCAD-0-17.

* Tue Nov 06 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.17-alt7
- Build with libglvnd-devel.

* Wed Sep 26 2018 Anton Midyukov <antohami@altlinux.org> 1:0.17-alt6
- Fix segfault (Closes: 35002)

* Fri Sep 21 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.17-alt5
- NMU: rebuilt with vtk-8.1.

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.17-alt4.1
- NMU: rebuilt with boost-1.67.0

* Tue May 22 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.17-alt4
- Fix path in desktop file.

* Mon May 21 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.17-alt3
- Fix run from menu (add FreeCAD executable to %_bindir).

* Fri May 04 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.17-alt2
- Build with OCE instead of opencascade

* Mon Apr 09 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.17-alt1
- New version (ALT #34781).

* Mon Apr 11 2016 Andrey Cherepanov <cas@altlinux.org> 1:0.16-alt1
- New version
- Add boost-python-devel to build requirements

* Thu Dec 10 2015 Andrey Cherepanov <cas@altlinux.org> 1:0.15-alt1
- New version (ALT #31511)
- Rename free-cad to freecad

* Sun Dec 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.14.0-alt1.git20141214
- Version 0.14.0 (ALT #30563)

* Wed Jul 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.13.0-alt1.git20140701
- New snapshot

* Thu May 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.13.0-alt1.git20140521
- New snapshot

* Tue Nov 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.13.0-alt1.git20131111
- New snapshot

* Fri Sep 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.13.0-alt1.git20130912
- Version 0.13.0

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.12.2237-alt3.git20130123
- Rebuilt with Boost 1.53.0

* Thu Feb 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.12.2237-alt2.git20130123
- Rebuilt with OpenCASCADE 6.5.4

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.12.2237-alt1.git20130123
- Version 0.12.2237 (from git)

* Tue Dec 04 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.13.5443-alt5.svn20120331
- Rebuild with new libxerces-c

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.5443-alt4.svn20120331
- Rebuilt with Boost 1.52.0

* Tue Oct 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.5443-alt3.svn20120331
- Fixed build with gcc 4.7

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.5443-alt2.svn20120331
- Rebuilt with Boost 1.51.0

* Wed Aug 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.5443-alt1.svn20120331
- Version 0.13.5443

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.5438-alt3.svn20120226
- Rebuilt with Boost 1.49.0

* Tue Mar 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.5438-alt2.svn20120226
- Built with Eigen3

* Thu Mar 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.5438-alt1.svn20120226
- Version 0.13.5438

* Wed Jan 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.5214-alt2.svn20111203
- Fixed build with new Mesa

* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.5214-alt1.svn20111203
- Version 0.13.5214

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.2237-alt1.svn20110830.1.1
- Rebuild with Python-2.7

* Thu Sep 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.2237-alt1.svn20110830.1
- Rebuilt with OpenCASCADE 6.5.1

* Thu Sep 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.2237-alt1.svn20110830
- New snapshot

* Wed Jul 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.2237-alt1.svn20110501.1
- Rebuilt with Boost 1.47.0

* Tue May 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.2237-alt1.svn20110501
- Version 0.12.2237

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.3752-alt1.svn20101120.5
- Rebuilt with Boost 1.46.1

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.3752-alt1.svn20101120.4
- Really rebuilt for debuginfo

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.3752-alt1.svn20101120.3
- Rebuilt with debuginfo
- Fixed build with Boost 1.46.0

* Thu Jan 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.3752-alt1.svn20101120.2
- Extracted freecad-thumbnailer into separate package

* Thu Nov 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.3752-alt1.svn20101120.1
- Rebuilt with set-versioned libxerces-c

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.3752-alt1.svn20101120
- Version 0.11.3752

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.3340-alt1.svn20100725.1
- Rebuilt for soname set-versions

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.3340-alt1.svn20100725
- Version 0.10.3340

* Fri Mar 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3017-alt1.svn20100308.1
- Built with libopencv4

* Wed Mar 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3017-alt1.svn20100308
- Version 0.9.3017

* Fri Jan 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2237-alt1.svn20091224
- Initial build for Sisyphus
