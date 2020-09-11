#TODO: try bulding against OpenMPI only when version upgrade 2.1->3.1
%def_without openmpi
%def_with ffmpeg

%define mpiimpl openmpi-compat
%define mpidir %_libdir/%mpiimpl

%def_without shared_togl
%define togl_ver 2.1

%set_verify_elf_method unresolved=relaxed

Name: netgen
Version: 6.2.2004
Release: alt1
Summary: Automatic 3d tetrahedral mesh generator
License: LGPLv2
Group: Sciences/Mathematics
Url: https://github.com/NGSolve/netgen
#Git: https://github.com/NGSolve/netgen.git

Source: %name-%version.tar
Source1: netgen.png
Source2: netgen.desktop
Source3: netgen-parallel.desktop

# Rename shared libaries (the original names are often way too generic), add library version
Patch2: netgen-6.2-alt-libs-rename-and-versions.patch
# Set a default NETGENDIR appropriate for packaging
Patch3: netgen-6.2-alt-set-default-netgendir.patch
# Make some includes relative (needed for when headers are in -private subpackage)
Patch4: 0004-Make-some-includes-relative.patch
# Make bin, lib and python sitearch installation directories configurable
Patch5: 0005-Make-bin-lib-and-pysitearch-dirs-configurable.patch
# Unbundle togl (see also %%prep)
Patch6: netgen-6.2-alt-unbundle-togl.patch
# SuperBuild.cmake fails to propagate USE_JPEG
Patch7: 0007-Add-missing-USE_JPEG-propagation.patch
# Add missing -ldl
Patch8: 0008-Add-missing-ldl.patch
# Only include immintrin.h on x86 arches
Patch9: 0009-immintrin.patch
# Use system pybind11
Patch10: netgen-6.2-alt-unbundle-pybind11.patch

BuildRequires(pre): rpm-build-tcl
BuildRequires(pre): rpm-build-python3

# Automatically added by buildreq on Wed Jun 13 2018
# optimized out: OCE-foundation OCE-modeling OCE-ocaf OCE-visualization cmake cmake-modules fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdmcp-devel libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXres-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libavcodec-devel libavutil-devel libopencore-amrnb0 libopencore-amrwb0 libp11-kit libstdc++-devel libx265-130 libxkbfile-devel mpi-selector openmpi-compat perl pkg-config python-base python-modules python3 python3-base tcl tcl-devel tk tk-devel xorg-proto-devel xorg-xf86miscproto-devel
BuildRequires: gcc-c++
BuildRequires: ccmake
BuildRequires: OCE-devel
BuildRequires: libXmu-devel
BuildRequires: libavformat-devel
BuildRequires: libjpeg-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: pybind11-devel
BuildRequires: python3-dev
BuildRequires: zlib-devel
BuildRequires: desktop-file-utils
%if_with openmpi
BuildRequires: libmetis-devel
BuildRequires: %mpiimpl-devel
%endif
%if_with shared_togl
BuildRequires: tcl-togl-devel 
%endif

Requires: lib%name = %EVR tcl-tix

ExclusiveArch: x86_64

%add_findreq_skiplist %_datadir/%name/*
%add_findprov_lib_path %_libdir/%mpiimpl/lib %_tcllibdir

%define base_description \
"NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input \
from constructive solid geometry (CSG) or boundary representation (BRep) \
from STL file format. The connection to a geometry kernel allows the \
handling of IGES and STEP files. NETGEN contains modules for mesh \
optimization and hierarchical mesh refinement."

%description
%base_description

%package -n lib%name
Summary: Shared library of NETGEN
Group: System/Libraries

%description -n lib%name
%base_description

This package contains shared library of NETGEN.

%package -n python3-module-%name
Summary: Python bindings of NETGEN
Group: Development/Python3
Requires: lib%name = %EVR
Provides: python3(netgen.libngpy._NgOCC) python3(netgen.libngpy._csg) python3(netgen.libngpy._geom2d) python3(netgen.libngpy._meshing) python3(netgen.libngpy._stl)
Conflicts: python3-module-%name-openmpi

%description -n python3-module-%name
%base_description

This package contains Python bindings of NETGEN.

%package -n lib%name-devel
Summary: Development files of NETGEN
Group: Development/C++
#BuildArch: noarch
Requires: lib%name = %EVR

%description -n lib%name-devel
%base_description

This package contains development files of NETGEN.

%package doc
Summary: Documentation for NETGEN
Group: Documentation
BuildArch: noarch

%description doc
%base_description

This package contains documentation for NETGEN.

%package tutorials
Summary: Tutorials for NETGEN
Group: Documentation
BuildArch: noarch

%description tutorials
%base_description

This package contains tutorials for NETGEN.

%if_with openmpi
%package openmpi
Summary: Shared library of NETGEN built with %mpiimpl
Group: System/Libraries
%description openmpi
%base_description

%package -n lib%name-openmpi
Summary: Shared library of NETGEN
Group: System/Libraries

%description -n lib%name-openmpi
%base_description

This package contains shared library of NETGEN.

%package -n lib%name-openmpi-devel
Summary: Development files of NETGEN
Group: Development/C++
#BuildArch: noarch
Requires: lib%name-openmpi = %EVR

%description -n lib%name-openmpi-devel
%base_description

This package contains development files of NETGEN.

%package -n python3-module-%name-openmpi
Summary: Python bindings of NETGEN
Group: Development/Python3
Requires: lib%name-openmpi = %EVR
Provides: python3(netgen.libngpy._NgOCC) python3(netgen.libngpy._csg) python3(netgen.libngpy._geom2d) python3(netgen.libngpy._meshing) python3(netgen.libngpy._stl)
Conflicts: python3-module-%name

%description -n python3-module-%name-openmpi
%base_description

This package contains Python bindings of NETGEN.

%endif


%prep
%setup

#%%patch2 -p1
%patch3 -p1
%patch4 -p1
#%%patch5 -p1
%if_with shared_togl
%patch6 -p1
%endif
%patch7 -p1
#%%patch8 -p1
%patch9 -p1
%patch10 -p1

%if_with shared_togl
# Remove bundled togl
rm -rf ng/Togl-1.7
rm -rf ng/Togl2.1
rm -f ng/togl_1_7.h
%endif

%ifarch x86_64 aarch64
sed -i 's|@UINT64_C@|UL|' ng/ngpkg.cpp
%else
sed -i 's|@UINT64_C@|ULL|' ng/ngpkg.cpp
%endif

#repair default (R)PATHs
sed -i 's|NG_INSTALL_DIR_LIB_DEFAULT lib|NG_INSTALL_DIR_LIB_DEFAULT lib${LIB_SUFFIX}|' CMakeLists.txt
#TODO: uncomment and apply if no MPI version to be assembled in future
sed -i 's|NG_INSTALL_DIR_CMAKE_DEFAULT lib/cmake/${NG_INSTALL_SUFFIX}|NG_INSTALL_DIR_CMAKE_DEFAULT %_libdir/cmake/%name|' CMakeLists.txt
#sed -i 's|${NG_RPATH_TOKEN};${NG_RPATH_TOKEN}/${NETGEN_RPATH}|${NG_RPATH_TOKEN};${NG_RPATH_TOKEN}/${NETGEN_RPATH};%%mpidir/lib:%%_tcllibdir|' CMakeLists.txt
#sed -i 's|${NG_RPATH_TOKEN};${NG_RPATH_TOKEN}/${NETGEN_RPATH}|%%_tcllibdir|' CMakeLists.txt
#sed -i 's|${NG_RPATH_TOKEN}/../${NETGEN_PYTHON_RPATH}||' ng/CMakeLists.txt

%if_without shared_togl
sed -i 's|<tkInt.h>|<tk/generic/tkInt.h>|' ng/Togl2.1/togl.c
%endif

%build

###########################################################################
###################          SERIAL VER           #########################
  OPTFLAGS="%optflags"
  CFLAGS="$OPTFLAGS -fno-strict-aliasing" \
  CXXFLAGS="$OPTFLAGS -fno-strict-aliasing" \
  %cmake \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DNG_INSTALL_DIR_BIN=%_bindir \
    -DNG_INSTALL_DIR_INCLUDE=%_includedir/%name \
    -DUSE_JPEG=1 \
    -DUSE_OCC=1 \
    -DPYBIND_INCLUDE_DIR=%_includedir \
    -DNG_INSTALL_PYBIND=OFF \
    -DLIBTOGL=%_tcllibdir/libTogl%togl_ver.so \
    -Dng_install_dir_lib=%_libdir \
    -DCMAKE_SKIP_RPATH=OFF \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
    -DCMAKE_SKIP_BUILD_RPATH=OFF \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=OFF \
    -DCMAKE_INSTALL_RPATH_USE_LINK_PATH:BOOL=FALSE \
    -DCMAKE_INSTALL_RPATH="%_tcllibdir" \
    -DNETGEN_PYTHON_RPATH="%_libdir" \
    -DUSE_NATIVE_ARCH=OFF \
    -DUSE_GUI=ON \
    -DUSE_PYTHON=ON \
    -DUSE_MPI=OFF \
    -DUSE_OCC=ON \
    -DUSE_JPEG=ON \
%if_with ffmpeg
    -DUSE_MPEG=ON \
%else
    -DUSE_MPEG=OFF \
%endif

%cmake_build VERBOSE=1

############################################################################
############################      MPI ver ##################################

%if_with openmpi
mkdir -p %mpiimpl-BUILD
pushd %mpiimpl-BUILD
mpi-selector --yes --set %mpiimpl
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath, %mpidir/lib -L%mpidir/lib"
source %mpidir/bin/mpivars.sh
export MPIDIR=%mpidir

  OPTFLAGS="%optflags"
  CFLAGS="$OPTFLAGS -fno-strict-aliasing -DOMPI_IGNORE_CXX_SEEK" \
  CXXFLAGS="$OPTFLAGS -fno-strict-aliasing -DOMPI_IGNORE_CXX_SEEK" \
  %cmake \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DNG_INSTALL_DIR_BIN=%mpidir/bin \
    -DNG_INSTALL_DIR_LIB=%mpidir/lib \
    -DNG_INSTALL_DIR_INCLUDE=%mpidir/include/%name \
    -DNG_INSTALL_DIR_CMAKE=%mpidir/lib/cmake \
    -DMETIS_INCLUDE_DIR:PATH=%_includedir/metis \
    -DUSE_JPEG=1 \
    -DUSE_OCC=1 \
    -DPYBIND_INCLUDE_DIR=%_includedir \
    -DNG_INSTALL_PYBIND=OFF \
    -DLIBTOGL=%_tcllibdir/libTogl%togl_ver.so \
    -Dng_install_dir_lib=%_libdir \
    -DCMAKE_SKIP_RPATH=OFF \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
    -DCMAKE_SKIP_BUILD_RPATH=OFF \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=OFF \
    -DCMAKE_INSTALL_RPATH_USE_LINK_PATH:BOOL=FALSE \
    -DCMAKE_INSTALL_RPATH="%mpidir/lib:%_tcllibdir" \
    -DNETGEN_PYTHON_RPATH=%_libdir \
    -DUSE_NATIVE_ARCH=OFF \
    -DUSE_GUI=ON \
    -DUSE_PYTHON=ON \
    -DNG_INSTALL_DIR_PYTHON=%python3_sitelibdir \
    -DUSE_MPI=ON \
    -DUSE_OCC=ON \
    -DUSE_JPEG=ON \
%if_with ffmpeg
    -DUSE_MPEG=ON \
%else
    -DUSE_MPEG=OFF \
%endif 
    ../..

%cmake_build VERBOSE=1
popd
%endif #openmpi

%install

sed -i 's|file(INSTALL DESTINATION "%_prefix/include/netgen/pybind11" TYPE FILE FILES "/usr/include/../LICENSE")||' BUILD/netgen/cmake_install.cmake

#installing serial version
%cmakeinstall_std NETGENDIR=%_bindir TCLLIBDIR=%_tcllibdir LIBTOGL=%_tcllibdir/libTogl%togl_ver.so TOPDIR=$PWD
%add_findreq_skiplist %_datadir/%name/py_tutorials/*.py

# Install icon and desktop file
install -Dpm 0644 %SOURCE1 %buildroot%_iconsdir/hicolor/48x48/apps/%name.png
desktop-file-install --dir %buildroot%_datadir/applications/ %SOURCE2

%if_with openmpi
export MPIDIR=%mpidir
#installing OpenMPI version
pushd %mpiimpl-BUILD
%cmakeinstall_std NETGENDIR=%_bindir TCLLIBDIR=%_tcllibdir LIBTOGL=%_tcllibdir/libTogl%togl_ver.so TOPDIR=$PWD
popd

# Install parallel desktop file
desktop-file-install --dir %buildroot%_datadir/applications/ %SOURCE3
sed -i 's|Exec=mpirun|Exec=%mpidir/bin/mpirun|' %buildroot%_datadir/applications/netgen-parallel.desktop
%endif

rm -rf %buildroot%_includedir/netgen/pybind11
rm -rf %buildroot%_datadir/%name/doc

%files
%doc AUTHORS
%_datadir/icons/hicolor/48x48/apps/%name.png
%_datadir/applications/*.desktop
%_bindir/*

%files -n lib%name
%_libdir/*.so*

%files -n lib%name-devel
%_includedir/*
%_libdir/cmake/%name/*.cmake

%files doc
%doc doc/ng4.pdf

%files tutorials
%_datadir/%name

%files -n python3-module-%name
%python3_sitelibdir/*

%if_with openmpi
%files openmpi
%mpidir/bin/*

%files -n lib%name-openmpi
%mpidir/lib/*.so*

%files -n lib%name-openmpi-devel
%mpidir/lib/cmake/*.cmake

%files -n python3-module-%name-openmpi
%python3_sitelibdir/*
%endif #openmpi

%changelog
* Tue May 12 2020 Nikolai Kostrigin <nickel@altlinux.org> 6.2.2004-alt1
- New version

* Thu Jan 23 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.1910-alt1
- Updated to new version

* Fri Mar 15 2019 Nikolai Kostrigin <nickel@altlinux.org> 6.2.1810-alt1
- New version

* Mon Feb 11 2019 Nikolai Kostrigin <nickel@altlinux.org> 6.2.1808-alt2
- Fix build with gcc8 [-Werror=return-type]

* Mon Oct 08 2018 Nikolai Kostrigin <nickel@altlinux.org> 6.2.1808-alt1
- New version
- Remove %%ubt
- Change default *.cmake config files path to %%_libdir/cmake

* Fri Jun 08 2018 Nikolai Kostrigin <nickel@altlinux.org> 6.2-alt1.1804
- New version

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1-alt1.dev.git20150306.qa5.1
- NMU: rebuilt with boost-1.67.0

* Fri Apr 27 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 6.1-alt1.dev.git20150306.qa5
- Rebuilt against OCE

* Thu Jan 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1-alt1.dev.git20150306.qa4
- Fixed build.

* Fri Jul 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1-alt1.dev.git20150306.qa3
- Fixed build with new ffmpeg

* Thu Mar 23 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 6.1-alt1.dev.git20150306.qa2
- NMU: fixed build and rebuilt against Tcl/Tk 8.6.

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 6.1-alt1.dev.git20150306.qa1
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Mon Mar 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1-alt1.dev.git20150306
- Version 6.1-dev

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1.svn20140625
- New snapshot

* Thu Jun 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1.svn20140428
- Version 5.3

* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2-alt3.svn20130902
- Fixed build

* Wed Sep 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2-alt2.svn20130902
- Fixed build

* Thu Sep 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2-alt1.svn20130902
- Version 5.2

* Fri Jul 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt1.svn20130527
- New snapshot

* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt1.svn20130203
- Version 5.1

* Tue Aug 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0-alt1.svn20120820
- Version 5.0

* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt4.svn20120215
- Rebuilt with OpenMPI 1.6

* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt3.svn20120215
- Fixed build

* Thu Mar 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20120215
- New snapshot
- Built with OpenCASCADE

* Tue Dec 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20111201
- New snapshot
- Rebuilt with libparmetis instead of libparmetis0

* Fri Nov 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20111103
- New snapshot

* Wed Sep 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20110725.1
- Rebuilt with libparmetis0 instead of libparmetis

* Mon Aug 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20110725
- Version 4.9.14

* Sun May 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt2.svn20101017.4
- Built without OpenCASCADE (awaiting fix from upstream)

* Thu Mar 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt2.svn20101017.3
- Rebuilt for debuginfo

* Sat Feb 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt2.svn20101017.2
- Rebuilt with parmetis 3.1.1-alt10

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt2.svn20101017.1
- Rebuilt for soname set-versions

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt2.svn20101017
- New snapshot

* Tue Jul 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt2
- Rebuilt with reformed ParMetis

* Mon Jun 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt1
- Version 4.9.13
- Added demo

* Mon Mar 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.9-alt4
- Fixed build with modified OpenCascade headers

* Tue Dec 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.9-alt3
- Rebuilt with OpenCascade

* Mon Aug 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.9-alt2
- Rebuilt without OpenCascade

* Thu Aug 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.9-alt1
- Initial build for Sisyphus

