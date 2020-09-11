%def_without shared_togl
%def_without openmpi
%define mpiimpl openmpi-compat
%define mpidir %_libdir/%mpiimpl
%def_without unittests

Name: ngsolve
Version: 6.2.2004
Release: alt1
Summary: NGSolve Finite Element Library
License: GPL or LGPL
Group: Sciences/Mathematics
Url: https://github.com/NGSolve/ngsolve

#Git: https://github.com/NGSolve/ngsolve.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

# Automatically added by buildreq on Wed Jun 13 2018
# optimized out: OCE-foundation OCE-modeling OCE-ocaf OCE-visualization cmake cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libGL-devel libGLU-devel libX11-devel libavcodec-devel libavutil-devel libopenblas-devel libstdc++-devel openmpi-compat openssh-common python-base python-module-sphinx python-modules python3 python3-base tcl-devel tk-devel zlib-devel
BuildRequires: gcc-c++
BuildRequires: OCE-devel
BuildRequires: ccmake
BuildRequires: cvs
BuildRequires: doxygen
BuildRequires: git-core
BuildRequires: libXmu-devel
BuildRequires: libavformat-devel
BuildRequires: libjpeg-devel
BuildRequires: liblapack-devel
BuildRequires: libswscale-devel
BuildRequires: pybind11-devel
BuildRequires: python3-dev
BuildRequires: subversion
BuildRequires: libnetgen-devel
BuildRequires: netgen
%if_with shared_togl
BuildRequires: tcl-togl-devel
%endif
%if_with openmpi
BuildRequires: %mpiimpl-devel
BuildRequires: libnetgen-openmpi-devel
BuildRequires: netgen-openmpi
BuildRequires: libmetis-devel
%endif

ExclusiveArch: x86_64

%define base_description \
NGSolve is a general purpose Finite Element Library on top of Netgen. \
With the basic library one can solve heat flow equations, Maxwell \
equations, and solid mechanical problems. Several add-ons are available \
for particular application classes.

%description
%base_description

%package -n lib%name
Summary: Shared libraries of NGSolve
Group: System/Libraries
%py_provides ngslib

%description -n lib%name
%base_description

This package contains shared libraries of NGSolve.

%package -n lib%name-devel
Summary: Development files of NGSolve
Group: Development/C++
Requires: lib%name = %EVR
#BuildArch: noarch

%description -n lib%name-devel
%base_description

This package contains development files of NGSolve.

%package -n python3-module-%name
Summary: Python module of NGSolve
Group: Development/Python
Requires: lib%name = %EVR
Provides: python3(ngsolve.bla) python3(ngsolve.comp) python3(ngsolve.fem) python3(ngsolve.la) python3(ngsolve.ngstd) python3(ngsolve.solve)
Conflicts: python3-module-%name-openmpi

%description -n python3-module-%name
%base_description

This package contains Python module of NGSolve.

%package demos
Summary: Demos for NGSolve
Group: Development/Documentation
Requires: lib%name = %EVR
%add_python_req_skip fem

%description demos
%base_description

This package contains demos for NGSolve.

%package docs
Summary: Documentation for NGSolve
Group: Development/Documentation
BuildArch: noarch

%description docs
%base_description

This package contains development documentation for NGSolve.

%if_with openmpi
%package openmpi
Summary: NGSolve Finite Element Library
Group: Sciences/Mathematics

%description openmpi
%base_description

%package -n lib%name-openmpi
Summary: Shared libraries of NGSolve
Group: System/Libraries
%py_provides ngslib

%description -n lib%name-openmpi
%base_description

This package contains shared libraries of NGSolve.

%package -n lib%name-openmpi-devel
Summary: Development files of NGSolve
Group: Development/C++
Requires: lib%name-openmpi = %EVR
#BuildArch: noarch

%description -n lib%name-openmpi-devel
%base_description

This package contains development files of NGSolve.

%package -n python3-module-%name-openmpi
Summary: Python module of NGSolve
Group: Development/Python
Requires: lib%name-openmpi = %EVR
Provides: python3(ngsolve.bla) python3(ngsolve.comp) python3(ngsolve.fem) python3(ngsolve.la) python3(ngsolve.ngstd) python3(ngsolve.solve)
Conflicts: python3-module-%name

%description -n python3-module-%name-openmpi
%base_description

This package contains Python module of NGSolve.

%endif #openmpi

%prep
%setup

%build

########################## SERIAL VERSION BUILD  ######################

OPTFLAGS="%optflags"
CFLAGS="$OPTFLAGS -fno-strict-aliasing -Wno-sign-compare -Wno-maybe-uninitialized -Wno-literal-suffix"
CXXFLAGS="$OPTFLAGS -fno-strict-aliasing -Wno-sign-compare -Wno-maybe-uninitialized -Wno-literal-suffix"
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_C_FLAGS:STRING="$CFLAGS" \
    -DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS" \
%if_with unittests
    -DCMAKE_INSTALL_PREFIX=%_prefix \
%endif
    -DNGSOLVE_INSTALL_DIR_CMAKE=%_prefix \
    -DNetgen_DIR:PATH=%_prefix/lib/cmake/%name/ \
    -DUSE_SUPERBUILD=OFF \
    -DUSE_MPI=OFF \
    -DUSE_OCC=ON \
    -DUSE_PYTHON=ON \
    -DUSE_LAPACK=ON \
    -DUSE_VT=OFF \
    -DUSE_MKL=OFF \
    -DUSE_HYPRE=OFF \
    -DUSE_MUMPS=OFF \
    -DUSE_PARDISO=OFF \
    -DUSE_UMFPACK=OFF \
    -DBUILD_UMFPACK=OFF \
    -DINTEL_MIC=OFF \
    -DUSE_VTUNE=OFF \
    -DUSE_NUMA=OFF \
    -DUSE_CCACHE=OFF \
    -DINSTALL_DEPENDENCIES=OFF \
    -DUSE_NATIVE_ARCH=OFF \
%if_with unittests
    -DENABLE_UNIT_TESTS=ON \
%endif

%cmake_build VERBOSE=1

######################### OpenMPI VERSION BUILD  ######################

%if_with openmpi
mkdir -p %mpiimpl-BUILD
pushd %mpiimpl-BUILD
mpi-selector --yes --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

OPTFLAGS="%optflags"
CFLAGS="$OPTFLAGS -fno-strict-aliasing -DOMPI_IGNORE_CXX_SEEK -Wno-sign-compare -Wno-maybe-uninitialized -Wno-literal-suffix"
CXXFLAGS="$OPTFLAGS -fno-strict-aliasing -DOMPI_IGNORE_CXX_SEEK -Wno-sign-compare -Wno-maybe-uninitialized -Wno-literal-suffix"
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_C_FLAGS:STRING="$CFLAGS" \
    -DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS" \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DNGSOLVE_INSTALL_DIR_CMAKE=%mpidir \
    -DNetgen_DIR:PATH=%mpidir/lib/cmake/ \
    -DUSE_SUPERBUILD=OFF \
    -DUSE_MPI=ON \
    -DUSE_OCC=ON \
    -DUSE_PYTHON=ON \
    -DUSE_LAPACK=ON \
    -DUSE_VT=OFF \
    -DUSE_MKL=OFF \
    -DUSE_HYPRE=OFF \
    -DUSE_MUMPS=OFF \
    -DUSE_PARDISO=OFF \
    -DUSE_UMFPACK=OFF \
    -DBUILD_UMFPACK=OFF \
    -DINTEL_MIC=OFF \
    -DUSE_VTUNE=OFF \
    -DUSE_NUMA=OFF \
    -DUSE_CCACHE=OFF \
    -DINSTALL_DEPENDENCIES=OFF \
    -DUSE_NATIVE_ARCH=OFF \
%if_with unittests
    -DENABLE_UNIT_TESTS=ON \
%endif
    ../..

%cmake_build VERBOSE=1
popd
%endif #openmpi

%add_findreq_skiplist %_datadir/%name/py_tutorials/*.py
doxygen

%install

%cmakeinstall_std

%if_with openmpi
pushd %mpiimpl-BUILD
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir
%cmakeinstall_std
popd
%endif

%files
%_bindir/ngsolve.tcl
%_datadir/%name

%files -n lib%name
%_libdir/*.so

%files -n lib%name-devel
%_libdir/cmake/%name/*.cmake
%_includedir/*

%files demos
%_bindir/*
%exclude %_bindir/ngsolve.tcl

%files docs
%doc doxy/html

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
%endif


%changelog
* Tue May 12 2020 Nikolai Kostrigin <nickel@altlinux.org> 6.2.2004-alt1
- New version

* Thu Jan 23 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.1910-alt1
- Updated to new version (Closes: #37907)

* Fri Mar 15 2019 Nikolai Kostrigin <nickel@altlinux.org> 6.2.1810-alt1
- New version
  + Fix build with gcc8 [-Werror=return-type]

* Mon Oct 08 2018 Nikolai Kostrigin <nickel@altlinux.org> 6.2.1808-alt1
- New version
- Remove %%ubt
- Change default *.cmake config files path to %%_libdir/cmake

* Sat Jun 09 2018 Nikolai Kostrigin <nickel@altlinux.org> 6.2-alt1.1804
- New version

* Tue Jun 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1-alt1.dev.git20150323.qa1.3
- NMU: rebuilt with boost-1.67.0.

* Sat Mar 25 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 6.1-alt1.dev.git20150323.qa1.2
- Rebuilt against Tcl/Tk 8.6
- Fixed build:
  + BR: openmpi-devel -> openmpi-compat-devel
  + BR: + libnuma-devel

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 6.1-alt1.dev.git20150323.qa1.1
- (AUTO) subst_x86_64.

* Fri Apr 08 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 6.1-alt1.dev.git20150323.qa1
- NMU: rebuilt with rebuilt netgen.

* Fri Mar 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1-alt1.dev.git20150323
- Version 6.1-dev
- Added Python module

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1.svn20140704
- New snapshot

* Fri Jun 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1.svn20140618
- Version 5.3

* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt3
- Fixed build

* Thu Sep 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt2
- 5.1 released

* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt1.svn20130203
- Version 5.1

* Wed Aug 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0-alt1.svn20120821
- Version 5.0

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt5.svn20120228
- Built with OpenBLAS instead of GotoBLAS2

* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt4.svn20120228
- Rebuilt with OpenMPI 1.6

* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt3.svn20120228
- Fixed build

* Thu Mar 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20120228
- New snapshot

* Tue Dec 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20111116
- Moved non-versioned libraries from lib%name-devel into lib%name

* Tue Dec 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt1.svn20111116
- Initial build for Sisyphus

