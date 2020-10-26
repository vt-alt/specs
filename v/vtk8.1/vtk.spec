%define _unpackaged_files_terminate_build 1

%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname vtk
%define ver 8.1
Name: %oname%ver
Version: %ver.1
Release: alt4
Summary: The Visualization Toolkit, an Object-Oriented Approach to 3D Graphics
License: BSD-like
Group: Development/Tools
Url: https://www.vtk.org/

# https://gitlab.kitware.com/vtk/vtk.git
Source: %name-%version.tar
# https://gitlab.kitware.com/vtk/vtk-m.git
Source1: vtkm-%version.tar

Patch0: %oname-%version-alt-armh.patch
Patch1: %oname-%version-alt-build.patch
Patch2: alt-qt5.15.patch

Requires: lib%name = %EVR

BuildRequires(pre): rpm-build-tcl rpm-build-python /proc
BuildRequires(pre): rpm-macros-qt5
BuildRequires: gcc-c++ tcl-devel tk-devel cmake libGLU-devel libXt-devel
BuildRequires: libmysqlclient-devel postgresql-devel
BuildRequires: boost-devel boost-filesystem-devel python-module-matplotlib
BuildRequires: boost-graph-parallel-devel
BuildRequires: vtk-data%ver
BuildRequires: libfreetype-devel libjpeg-devel
BuildRequires: libxml2-devel libexpat-devel libftgl220-devel libpng-devel
BuildRequires: libtiff-devel zlib-devel libhdf5-devel libsqlite3-devel
BuildRequires: doxygen graphviz libgsl-devel
BuildRequires: libbfd-devel libnumpy-devel libopenmotif-devel
BuildRequires: libgl2ps-devel
BuildRequires: python-devel libXxf86misc-devel libimlxx-devel
BuildRequires: libdc1394-devel libtheora-devel
BuildRequires: libgsm-devel libvorbis-devel libtag-devel
BuildRequires: gnuplot
BuildRequires: libcgns-seq-devel
BuildRequires: inkscape texlive-latex-base
BuildRequires: texlive-latex-extra texlive-science
BuildRequires: libavformat-devel libpostproc-devel libswscale-devel
BuildRequires: libavdevice-devel libavfilter-devel
BuildRequires: liblz4-devel
BuildRequires: libnetcdf-devel libnetcdf_c++-devel
BuildRequires: jsoncpp-devel
BuildRequires: qt5-base-devel qt5-x11extras-devel qt5-tools-devel
BuildRequires: python-module-PyQt5-devel
BuildRequires: phonon-devel python-module-sip-devel
BuildRequires: libharu-devel
BuildRequires: libgdal-devel

Conflicts: vtk vtk6.1 vtk6.2

%description
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

%package -n lib%name
Summary: Shared libraries of The Visualization Toolkit (VTK)
Group: System/Libraries

%description -n lib%name
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains shared libraries of VTK.

%package -n lib%name-utils
Summary: Util libraries for The Visualization Toolkit (VTK)
Group: System/Libraries
Conflicts: lib%name-devel < %EVR
Conflicts: lib%name < %EVR
Requires: lib%name = %EVR

%description -n lib%name-utils
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains util libraries for VTK.

%package -n lib%name-devel
Summary: Development files of The Visualization Toolkit (VTK)
Group: Development/C++
Requires: %name = %EVR
Requires: %name-tcl = %EVR
Requires: lib%name = %EVR
Requires: qt5-base-devel
Requires: libfreetype-devel
Conflicts: libvtk-devel libvtk6.1-devel libvtk6.2-devel

%description -n lib%name-devel
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains development files of VTK.

%package qt5-designer-plugin
Summary: The Visualization Toolkit (VTK) plugin for Qt5
Group: Development/KDE and QT
Requires: lib%name = %EVR
Requires: qt5-designer

%description qt5-designer-plugin
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains VTK plugin for Qt5 Designer.

%package doc
Summary: Documentation for The Visualization Toolkit (VTK)
Group: Development/Documentation
BuildArch: noarch

%description doc
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains documentation for VTK.

%package tcl
Summary: The Visualization Toolkit (VTK) TCL bindings
Group: Development/Tcl
Requires: %name = %EVR
Requires: lib%name = %EVR
Requires: lib%name-tcl = %EVR
%add_tcl_lib_path %_libexecdir/tcltk/%oname-%ver
Conflicts: vtk-tcl vtk6.1-tcl vtk6.2-tcl

%description tcl
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package provides TCL bindings to VTK.

%package -n lib%name-tcl
Summary: Shared libraries of VTK-TCL bindings
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-tcl
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains shared libraries for TCL bindings to VTK.

%package -n lib%name-tcl-devel
Summary: Development files of VTK-TCL bindings
Group: Development/Tcl
Requires: lib%name-devel = %EVR
Requires: lib%name-tcl = %EVR
Conflicts: libvtk-tcl-devel libvtk6.1-tcl-devel libvtk6.2-tcl-devel

%description -n lib%name-tcl-devel
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains development files for TCL bindings to VTK.

%package python
Summary: The Visualization Toolkit (VTK) Python bindings
Group: Development/Python
Requires: %name = %EVR
Requires: lib%name = %EVR
Requires: lib%name-python = %EVR
Requires: python-module-%name = %EVR
Conflicts: vtk-python vtk6.1-python vtk6.2-python

%description python
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package provides Python bindings to VTK.

%package -n lib%name-python
Summary: The Visualization Toolkit (VTK) Python shared libraries
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-python
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains Python shared libraries of VTK.

%package -n lib%name-python-devel
Summary: The Visualization Toolkit (VTK) Python development files
Group: Development/Python
Requires: lib%name-python = %EVR
Conflicts: libvtk-python-devel libvtk6.1-python-devel libvtk6.2-python-devel

%description -n lib%name-python-devel
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains Python development files of VTK.

%package -n python-module-%name
Summary: The Visualization Toolkit (VTK) Python bindings
Group: Development/Python
Requires: lib%name-python = %EVR
Requires: python-module-pygtkglext
%add_python_req_skip GDK gtkgl vtkParallelPython
%py_requires gtk
Conflicts: python-module-vtk python-module-vtk6.1 python-module-vtk6.2
Provides: python-module-vtk = %EVR

%description -n python-module-%name
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package provides Python bindings to VTK.

%package -n python-module-%name-tests
Summary: Tests for The Visualization Toolkit (VTK) Python bindings
Group: Development/Python
Requires: python-module-%name = %EVR
Conflicts: python-module-vtk-tests python-module-vtk6.1-tests python-module-vtk6.2-tests

%description -n python-module-%name-tests
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains tests for Python bindings to VTK.

%package examples
Summary: The Visualization Toolkit (VTK) examples
Group: Development/Tools
Requires: %name = %EVR
Requires: %name-tcl = %EVR
Requires: %name-data = %EVR
%add_python_req_skip numeric
Conflicts: vtk-examples vtk6.1-examples vtk6.2-examples

%description examples
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains VTK examples. For correct work of all examples and tests
You need set environment variable VTK_DATA_ROOT=/usr/share/vtk-%ver.

%package data
Summary: The Visualization Toolkit (VTK) data
Group: Development/Tools
#BuildArch: noarch

%description data
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains VTK data files for tests/examples.

%package tests
Summary: The Visualization Toolkit (VTK) tests
Group: Development/Tools
Requires: %name-data = %EVR

%description tests
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains VTK tests For correct work of all examples and tests
You need set environment variable VTK_DATA_ROOT=/usr/share/vtk-%ver.

%prep
%setup
%ifarch armh
%patch0 -p1
%endif
%patch1 -p1
%patch2 -p1

cp -rv %_datadir/vtk-%ver/.ExternalData/* ./.ExternalData/

# remove bundled libraries
for x in constantly expat freetype hdf5 hyperlink gl2ps incremental jpeg jsoncpp libharu libxml2 lz4 netcdf oggtheora png tiff Twisted txaio zlib ZopeInterface ; do
	rm -rf ThirdParty/${x}/vtk${x}
done

rm -rf \
	ThirdParty/AutobahnPython/vtkAutobahn

# Save an unbuilt copy of the Example's sources for %%doc
mkdir vtk-examples
cp -a Examples vtk-examples

%build
PATH=$PATH:%_qt5_bindir

export VTK_DATA_ROOT=%_datadir/%oname-%ver
%add_optflags -I%_includedir/gsl
%add_optflags -DHAVE_SYS_TIME_H -DHAVE_SYS_TYPES_H -DHAVE_SYS_SOCKET_H
%add_optflags -D__USE_LARGEFILE64 -DH5_HAVE_SIGSETJMP -D__USE_POSIX
%add_optflags -DH5_HAVE_SETJMP_H

%cmake_insource \
	-DBUILD_SHARED_LIBS=ON \
	-DVTK_USE_SYSTEM_AUTOBAHN=ON \
	-DVTK_USE_SYSTEM_EXPAT=ON \
	-DVTK_USE_SYSTEM_FREETYPE=ON \
	-DVTK_USE_SYSTEM_FreeType=ON \
	-DVTK_USE_SYSTEM_HDF5=ON \
	-DVTK_USE_SYSTEM_JPEG=ON \
	-DVTK_USE_SYSTEM_LIBXML2=ON \
	-DVTK_USE_SYSTEM_LibXml2=ON \
	-DVTK_USE_SYSTEM_NETCDF=ON \
	-DVTK_USE_SYSTEM_OGGTHEORA=ON \
	-DVTK_USE_SYSTEM_PNG=ON \
	-DVTK_USE_SYSTEM_TIFF=ON \
	-DVTK_USE_SYSTEM_TWISTED=ON \
	-DVTK_USE_SYSTEM_ZLIB=ON \
	-DVTK_USE_SYSTEM_ZOPE=ON \
	-DVTK_USE_SYSTEM_LIBRARIES=ON \
	-DVTK_USE_SYSTEM_LIBPROJ4=OFF \
	-DVTK_USE_GL2PS=ON \
	-DVTK_USE_PARALLEL=ON \
	-DVTK_EXTRA_COMPILER_WARNINGS=ON \
	-DVTK_Group_StandAlone=ON \
	-DBUILD_DOCUMENTATION=ON \
	-DBUILD_EXAMPLES=ON \
	-DBUILD_VTK_BUILD_ALL_MODULES_FOR_TESTS=OFF \
	-DVTK_Group_Imaging=ON \
	-DVTK_Group_Rendering=ON \
	-DVTK_Group_Tk=ON \
	-DVTK_Group_Views=ON \
	-DVTK_WRAP_PYTHON=ON \
	-DVTK_WRAP_PYTHON_SIP=ON \
	-DVTK_WRAP_TCL=ON \
	-DVTK_USE_BOOST=ON \
	-DUSE_VTK_USE_BOOST=ON \
	-DModule_vtkInfovisBoost=ON \
	-DModule_vtkInfovisBoostGraphAlgorithms=ON \
	-DVTK_USE_OGGTHEORA_ENCODER=ON \
	-DVTK_USE_X=ON \
	-DVTK_USE_FFMPEG_ENCODER=ON \
	-DModule_vtkIOGDAL=ON \
	-DModule_vtkIOGeoJSON=ON \
	-DBUILD_TESTING=ON \
	-DVTK_SMP_IMPLEMENTATION_TYPE="Sequential" \
	-DVTK_INSTALL_PYTHON_MODULE_DIR="%python_sitelibdir" \
	-DPYTHON_INCLUDE_DIR=%python_includedir \
	-DVTK_PYTHON_INCLUDE_DIR=%python_includedir \
	-DVTK_USE_SYSTEM_SIX=ON \
	-DSIP_INCLUDE_DIR:PATH=%python_includedir \
	-DVTK_USE_QVTK=ON \
	-DVTK_USE_QVTK_OPENGL=ON \
	-DVTK_USE_QVTK_QTOPENGL=ON \
	-DQT_WRAP_CPP=ON \
	-DQT_WRAP_UI=ON \
	-DVTK_INSTALL_QT_DIR:PATH=%_qt5_plugindir/designer \
	-DVTK_INSTALL_QT_PLUGIN_DIR:PATH=%_qt5_plugindir/designer \
	-DDESIRED_QT_VERSION=5 \
	-DVTK_QT_VERSION=5 \
	-DQT_MOC_EXECUTABLE="%_qt5_bindir/moc" \
	-DQT_UIC_EXECUTABLE="%_qt5_bindir/uic" \
	-DQT_INCLUDE_DIR="%_includedir/qt5" \
	-DQT_QMAKE_EXECUTABLE="%_qt5_bindir/qmake" \
	-DVTK_Group_Qt:BOOL=ON \
	-DNETCDF_DIR=%_libdir/hdf5-seq \
	-DVTK_INSTALL_LIBRARY_DIR=%_lib \
	-DVTK_INSTALL_ARCHIVE_DIR=%_lib \
	-DVTK_INSTALL_PACKAGE_DIR=%_lib/cmake/vtk-%ver

export LD_LIBRARY_PATH=$PWD/lib
%make_build
%make DoxygenDoc

%install
export VTK_DATA_ROOT=%_datadir/%oname-%ver
%makeinstall_std

# List of executable examples
cat > examples.list << EOF
HierarchicalBoxPipeline
MultiBlock
Arrays
Cube
RGrid
SGrid
Medical1
Medical2
Medical3
finance
AmbientSpheres
Cylinder
DiffuseSpheres
SpecularSpheres
Cone
Cone2
Cone3
Cone4
Cone5
Cone6
EOF

# Install examples
for file in $(cat examples.list); do
	install -p bin/$file %buildroot%_bindir/vtkExample$file
	echo %_bindir/vtkExample$file >> examples.fixed.list
done

# List of executable test binaries
find bin \( -name \*Tests -o -name Test\* -o -name VTKBenchMark \) \
         -printf '%f\n' > testing.list

for file in $(cat testing.list); do
	install -p bin/$file %buildroot%_bindir/$file
done

# Fix up filelist paths
perl -pi -e's,^,%_bindir/,' testing.list

#Install data
mkdir -p %buildroot%_datadir/%oname-%ver
cp -alL ExternalData/* %buildroot%_datadir/%oname-%ver

%files
%doc Copyright.txt README.md
%_bindir/vtk
%_bindir/vtkEncodeString-%ver
%_bindir/vtkHashSource-%ver
%_bindir/vtkParseJava-%ver
%_bindir/vtkWrapHierarchy-%ver
%_bindir/vtkWrapJava-%ver

%files -n lib%name
%_libdir/*.so.*
%exclude %_libdir/*TCL-%ver.so.*
%exclude %_libdir/*Python*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_libdir/*.a
%exclude %_libdir/*TCL-%ver.so
%exclude %_libdir/*Python*.so
%_includedir/%oname-%ver
%exclude %_includedir/%oname-%ver/*Tcl*
%exclude %_includedir/%oname-%ver/*Python*
%_libdir/cmake/%oname-%ver
%exclude %_libdir/cmake/%oname-%ver/*TCL*
%exclude %_libdir/cmake/%oname-%ver/*Tcl*
%exclude %_libdir/cmake/%oname-%ver/*Python*

%files doc
%_docdir/%oname-%ver

%files tcl
%_bindir/*Tcl*
%_libexecdir/tcltk/%oname-%ver

%files -n lib%name-tcl
%_libdir/*TCL-%ver.so.*

%files -n lib%name-tcl-devel
%_libdir/*TCL-%ver.so
%_libdir/cmake/%oname-%ver/*TCL*
%_libdir/cmake/%oname-%ver/*Tcl*
%_includedir/%oname-%ver/*Tcl*

%files examples -f examples.fixed.list
%doc vtk-examples/Examples

%files qt5-designer-plugin
%_qt5_plugindir/designer/*

%files python
%_bindir/*python*
%_bindir/*Python*

%files -n lib%name-python
%_libdir/*Python*.so.*
%_libdir/libvtkRenderingPythonTkWidgets-8.1.so

%files -n lib%name-python-devel
%_libdir/*Python*.so
%exclude %_libdir/libvtkRenderingPythonTkWidgets-8.1.so
%_includedir/%oname-%ver/*Python*
%_libdir/cmake/%oname-%ver/*Python*

%files -n python-module-%name
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/test

%files -n python-module-%name-tests
%python_sitelibdir/%oname/test

%files data
%_datadir/%oname-%ver

%files tests -f testing.list

%changelog
* Thu Oct 22 2020 Sergey V Turchin <zerg@altlinux.org> 8.1.1-alt4
- fix compile with Qt-5.15

* Thu Oct 11 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.1.1-alt3
- fixed build on armh

* Wed Oct 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 8.1.1-alt2
- Updated build dependencies.

* Mon Sep 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 8.1.1-alt1
- Updated to upstream version 8.1.1.

* Wed Aug 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.0-alt4
- Rebuilt without openpdt.

* Sun Jun 24 2018 Anton Midyukov <antohami@altlinux.org> 6.2.0-alt3
- Rebuilt for aarch64
- Fix FTBFS

* Fri Mar 24 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 6.2.0-alt2.qa1
- NMU: rebuilt against Tcl/Tk 8.6

* Thu Mar 23 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 6.2.0-alt2
- NMU: fixed build

* Fri Mar 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.2.0-alt1
- Version 6.2.0

* Tue May 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1.0-alt1
- Version 6.1.0

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.0-alt2
- Fixed cmake files

* Fri Dec 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.0-alt1
- Version 6.0.0

* Wed Nov 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt6
- Rebuilt with new python-module-sip

* Tue Jul 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt5
- Fixed build

* Thu Jun 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt4
- Rebuilt with new libhdf5

* Fri Apr 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt3
- Rebuilt without MPI

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt2
- Rebuilt with Boost 1.53.0

* Fri Feb 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt1
- Version 5.10.1

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt7
- Rebuilt with new qscintilla2

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt6
- Rebuilt with Boost 1.52.0

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt5
- Rebuilt with libpng15

* Wed Sep 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt4
- Rebuilt with Boost 1.51.0 (thnx iv@)

* Wed Jun 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt3
- Rebuilt with OpenMPI 1.6

* Sun Jun 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt2
- Set soname version for libvtkQtPythonD.so

* Sat Jun 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt1
- Version 5.10.0

* Fri Apr 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt12
- Fixed utils subpackage
- Set soname version for libvtkNetCDF_cxx.so
- Restored qt4-designer-plugin subpackage

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt11
- Fixed build with boost 1.49.0 (thnx iv@)

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt10
- Rebuilt with python-module-sip 4.13.2

* Wed Feb 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt9
- Built without OSMesa

* Mon Feb 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt8
- Fixed build with libav 0.8

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt7
- Rebuilt with python-module-sip 4.13.1

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt6
- Fixed file name: VTKTargets-reswithdebinfo.cmake ->
  VTKTargets-relwithdebinfo.cmake

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt5
- Fixed VTKTargets-reswithdebinfo.cmake (ALT #26650)

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt4
- Added necessary headers
- Fixed VTK_LIBRARY_DIRS (ALT #26650)

* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt3
- Rebuilt with Boost 1.48.0

* Sat Nov 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt2
- Set directories of data files

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.8.0-alt1.1
- Rebuild with Python-2.7

* Fri Sep 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt1
- Version 5.8.0

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.1-alt2
- Rebuilt with libnetcdf7-mpi

* Thu Apr 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.1-alt1
- Version 5.6.1

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt10
- Rebuilt with Boost 1.46.1

* Fri Mar 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt9
- Rebuilt with openmotif
- Added needed requirements

* Tue Mar 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt8
- Rebuilt for debuginfo

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt7
- Rebuilt with PostgreSQL 9.0

* Tue Nov 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt6
- Rebuilt for soname set-versions

* Fri Oct 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt5
- Fixed underlinking of libraries

* Wed Sep 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt4
- Do not use off screen calls (avoid segfault)

* Wed Sep 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt3
- Rebuilt with libmysqlclient.so.16

* Mon Aug 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt2
- Removed paths to buildroot

* Tue Jul 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt1
- Version 5.6.0

* Mon Mar 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt9
- Rebuilt with postgresql 8.4

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt8
- Changed requirement for python-module-%name: pygtkglext -> pygtkglext_git

* Wed Mar 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt7
- Rebuilt with new Boost (changed position of property_maps)
- Added some functionals (interfaces with addition packages)

* Sat Jan 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt6
- Rebuilt without python-module-Numeric

* Wed Jul 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt5
- Rebuild with python 2.6

* Thu Jul 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt4
- Enabled Python module

* Tue Jun 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt3
- Rebuild with changed libpng12

* Fri Jun 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt2
- Fixed directory layout for TCL wrappers

* Thu Jun 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt1
- Initial build for Sisyphus

