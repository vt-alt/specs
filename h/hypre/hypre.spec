%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 0
%define sover %somver.2.15
Name: hypre
Version: 2.15.1
Release: alt2
Summary: Scalable algorithms for solving linear systems of equations
License: LGPL v2.1
Group: Sciences/Mathematics
Url: http://www.llnl.gov/casc/hypre/

# https://github.com/LLNL/hypre.git
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

Requires: lib%name-devel = %version-%release

BuildRequires(pre): rpm-build-python rpm-build-java /proc
BuildRequires: gcc-fortran gcc-c++ %mpiimpl-devel emacs-nox
BuildRequires: liblapack-devel netpbm
BuildRequires: libsuperlu-devel babel cmake texlive-base-bin
BuildRequires: java-devel-default python-devel
BuildRequires: libnumpy-devel libxml2-devel python-module-libxml2
BuildRequires: libltdl-devel ghostscript-classic

%description
The goal of the Scalable Linear Solvers project is to develop scalable
algorithms and software for solving large, sparse linear systems of equations on
parallel computers. The primary software product is Hypre, a library of high
performance preconditioners that features parallel multigrid methods for both
structured and unstructured grid problems. The problems of interest arise in the
simulation codes being developed at LLNL and elsewhere to study physical
phenomena in the defense, environmental, energy, and biological sciences.

%package -n lib%name
Summary: Shared libraries of Hypre
Group: System/Libraries

%description -n lib%name
The goal of the Scalable Linear Solvers project is to develop scalable
algorithms and software for solving large, sparse linear systems of equations on
parallel computers. The primary software product is Hypre, a library of high
performance preconditioners that features parallel multigrid methods for both
structured and unstructured grid problems. The problems of interest arise in the
simulation codes being developed at LLNL and elsewhere to study physical
phenomena in the defense, environmental, energy, and biological sciences.

This package contains shared libraries of Hypre.

%package -n lib%name-devel
Summary: Development files of Hypre
Group: Development/Other
Requires: libbabel-devel libltdl7-devel libsuperlu-devel
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
The goal of the Scalable Linear Solvers project is to develop scalable
algorithms and software for solving large, sparse linear systems of equations on
parallel computers. The primary software product is Hypre, a library of high
performance preconditioners that features parallel multigrid methods for both
structured and unstructured grid problems. The problems of interest arise in the
simulation codes being developed at LLNL and elsewhere to study physical
phenomena in the defense, environmental, energy, and biological sciences.

This package contains development files of Hypre.

%package -n lib%name-devel-doc
Summary: Development documentation for Hypre
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
The goal of the Scalable Linear Solvers project is to develop scalable
algorithms and software for solving large, sparse linear systems of equations on
parallel computers. The primary software product is Hypre, a library of high
performance preconditioners that features parallel multigrid methods for both
structured and unstructured grid problems. The problems of interest arise in the
simulation codes being developed at LLNL and elsewhere to study physical
phenomena in the defense, environmental, energy, and biological sciences.

This package contains development documentation for Hepre.

%prep
%setup
%patch1 -p1

%build
mpi-selector --set %mpiimpl
source /etc/profile.d/mpi-selector.sh
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

export includedir=%_includedir
export JNI_INCLUDES="%_libexecdir/jvm/java/include"
export MPIDIR=%mpidir
cd src

%add_optflags %optflags %optflags_shared -I%_includedir/numpy

%cmake \
	-DHYPRE_SHARED:BOOL=ON \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DHYPRE_INSTALL_PREFIX:PATH=%buildroot%prefix \
	-DMPIDIR=%mpidir \
	-DSOMVER=%somver \
	-DSOVER=%sover \
	-DHYPRE_SHARED:BOOL=ON \
	-DHYPRE_USING_HYPRE_BLAS:BOOL=OFF \
	-DHYPRE_USING_HYPRE_LAPACK:BOOL=OFF \
	..

%cmake_build

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

pushd src/BUILD

%make install

install -d %buildroot%_includedir/%name
mv %buildroot%_includedir/*.h %buildroot%_includedir/%name/

install -d %buildroot%_docdir/lib%name-devel-doc
cp -fR ../../docs/* %buildroot%_docdir/lib%name-devel-doc/
rm -f %buildroot%_libdir/libsidl*
popd

%files
%doc CHANGELOG COPYING.LESSER COPYRIGHT

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-doc
%_docdir/lib%name-devel-doc

%changelog
* Mon Apr 27 2020 Anton Midyukov <antohami@altlinux.org> 2.15.1-alt2
- clean buidrequires doc++

* Fri Feb 22 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.15.1-alt1
- Update to latest release

* Fri Jul 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.13.0-alt2
- Updated build dependencies.

* Mon Jan 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.13.0-alt1
- Updated to upstream version 2.13.0.

* Thu Feb 21 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.0b-alt1
- Version 2.9.0b

* Sat Aug 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0b-alt5
- Built with OpenBLAS instead of GotoBLAS2

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0b-alt4
- Rebuilt with emacs 24.1

* Sun Jun 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0b-alt3
- Rebuilt with OpenMPI 1.6

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0b-alt2
- Fixed build

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0b-alt1
- Version 2.8.0b

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0b-alt3
- Rebuilt with GotoBLAS2 1.13-alt3

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0b-alt2
- Rebuilt with GotoBLAS2 instead of ATLAS

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0b-alt1
- Version 2.7.0b
- Disabled static package

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0b-alt6
- Added -g into compiler flags

* Thu Feb 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0b-alt5
- Rebuilt for debuginfo

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0b-alt4
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0b-alt3
- Fixed overlinking of libraries

* Mon Aug 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0b-alt2
- Rebuilt without python-module-Numeric

* Tue Jun 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0b-alt1
- Version 2.6.0b

* Tue Dec 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt9
- Rebuilt with SuperLU 4.0 and emacs23

* Sun Nov 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt8
- Removed unnecessary headers

* Tue Sep 1 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt7
- Added shared libraries

* Sun Jul 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt6
- Fixed MPI check

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt5
- Rebuild with PIC

* Tue May 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt4
- Rebuild with OpenMPI

* Wed Apr 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt3
- Move headers into hypre subdirectory

* Tue Apr 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt2
- Remove files owned by other packages

* Sat Apr 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0b-alt1
- Initial build for Sisyphus

