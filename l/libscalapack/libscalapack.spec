%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl
%define origname scalapack

%def_enable bootstrap

%define somver 1
%define sover %somver.8.0
Name: lib%origname
Version: 1.8.0
Release: alt19
Summary: Scalable LAPACK library
License: LGPL
Group: Sciences/Mathematics
Url: http://www.netlib.org/scalapack/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %origname-%version.tar.gz
Source1: SLmake.inc
Source2: manpages.tar.gz

BuildPreReq: liblapack-devel gcc-fortran
BuildPreReq: %mpiimpl-devel
BuildPreReq: libblacs-devel chrpath
%if_disabled bootstrap
# circular build deps with arpack
BuildRequires: libarpack-devel
%endif

%description
The ScaLAPACK (or Scalable LAPACK) library includes a subset of LAPACK routines
redesigned for distributed memory MIMD parallel computers. It is currently
written in a Single-Program-Multiple-Data style using explicit message passing
for interprocessor communication. It assumes matrices are laid out in a
two-dimensional block cyclic decomposition.

ScaLAPACK is designed for heterogeneous computing and is portable on any 
computer that supports MPI or PVM.

Like LAPACK, the ScaLAPACK routines are based on block-partitioned algorithms in
order to minimize the frequency of data movement between different levels of the
memory hierarchy. (For such machines, the memory hierarchy includes the
off-processor memory of other processors, in addition to the hierarchy of
registers, cache, and local memory on each processor.) The fundamental building
blocks of the ScaLAPACK library are distributed memory versions (PBLAS) of the
Level 1, 2 and 3 BLAS, and a set of Basic Linear Algebra Communication
Subprograms (BLACS) for communication tasks that arise frequently in parallel
linear algebra computations. In the ScaLAPACK routines, all interprocessor
communication occurs within the PBLAS and the BLACS. One of the design goals of
ScaLAPACK was to have the ScaLAPACK routines resemble their LAPACK equivalents
as much as possible.

If You need man pages, install libscalapack-manpages.

%package debug
Summary: Debug version of ScaLAPACK
Group: Sciences/Mathematics
%if_disabled bootstrap
Requires: libarpack-devel
%endif
Requires: libblacs-devel-debug

%description debug
Debug version of ScaLAPACK.

If You need man pages, install libscalapack-manpages.

%package devel
Summary: Development files of ScaLAPACK
Group: Development/Other
Requires: libblacs-devel %mpiimpl-devel
%if_disabled bootstrap
Requires: libarpack-devel
%endif
Requires: %name = %version-%release
Conflicts: %name < %version-%release
Obsoletes: %name < %version-%release
Conflicts: %name-devel < %version-%release
Obsoletes: %name-devel < %version-%release

%description devel
Development files of ScaLAPACK.

%package devel-static
Summary: Static library of ScaLAPACK
Group: Development/Other
Requires: %name-devel = %version-%release
Conflicts: %name < %version-%release
Conflicts: %name-devel < %version-%release

%description devel-static
Static library of ScaLAPACK.

%package -n pblas-tests
Summary: Tests for PBLAS
Group: Sciences/Mathematics

%description -n pblas-tests
Tests for PBLAS.

%package -n pblas-tests-data
Summary: Test data for PBLAS
Group: Sciences/Mathematics
BuildArch: noarch
Requires: pblas-tests = %version-%release

%description -n pblas-tests-data
Test data for PBLAS.

%package -n pblas-timing
Summary: PBLAS timing
Group: Sciences/Mathematics

%description -n pblas-timing
PBLAS timing.

%package -n pblas-timing-data
Summary: Data for PBLAS timing
Group: Sciences/Mathematics
BuildArch: noarch
Requires: pblas-timing = %version-%release

%description -n pblas-timing-data
Data for PBLAS timing.

%package -n pblas-devel
Summary: Headers for PBLAS
Group: Sciences/Mathematics
BuildArch: noarch
Requires: %name = %version-%release

%description -n pblas-devel
Headers for PBLAS.

%package -n %origname-redist
Summary: Tests for ScaLAPACK redist
Group: Sciences/Mathematics

%description -n %origname-redist
Tests for ScaLAPACK redist.

%package -n %origname-redist-data
Summary: Test data for ScaLAPACK redist
Group: Sciences/Mathematics
BuildArch: noarch
Requires: %origname-redist = %version-%release

%description -n %origname-redist-data
Test data for ScaLAPACK redist.

%package -n %origname-tests
Summary: Tests for ScaLAPACK
Group: Sciences/Mathematics

%description -n %origname-tests
Tests for ScaLAPACK.

%package -n %origname-tests-data
Summary: Test data for ScaLAPACK
Group: Sciences/Mathematics
BuildArch: noarch
Requires: %origname-tests = %version-%release

%description -n %origname-tests-data
Test data for ScaLAPACK.

%package -n %origname-example
Summary: Example for ScaLAPACK
Group: Sciences/Mathematics

%description -n %origname-example
Example for ScaLAPACK.

%package -n %origname-example-data
Summary: Example data for ScaLAPACK
Group: Sciences/Mathematics
BuildArch: noarch
Requires: %origname-example = %version-%release

%description -n %origname-example-data
Example data for ScaLAPACK.

%package manpages
Summary: Man pages of ScaLAPACK
Group: Sciences/Mathematics
BuildArch: noarch

%description manpages
Man pages of ScaLAPACK.

%package full
Summary: All in one ScaLAPACK shared libraries
Group: System/Libraries

%description full
All in one ScaLAPACK shared libraries.

%package full-devel
Summary: All in one ScaLAPACK development files
Group: Development/Other
Requires: %name-full = %version-%release

%description full-devel
All in one ScaLAPACK development files.


%prep
%setup
install -p -m644 %SOURCE1 ./
tar -xzvf %SOURCE2

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

BUILDDIR=`pwd`
sed -i 's|(LIBEXECDIR)|%_libdir|g' SLmake.inc
sed -i 's|(LIBDIR)|%_libdir|g' SLmake.inc
sed -i "s|(HOME)|$BUILDDIR|g" SLmake.inc
sed -i -e 's/(OPTFLAGS)/%optflags %optflags_shared -fno-strict-aliasing/g' \
	SLmake.inc
mkdir -pv TESTING0
cp -f TESTING/*.dat TESTING0/
make lib
mkdir -pv LIB0
mv *.a LIB0/
sed -i -e 's/^\(BLACSDBGLVL\).*/\1  = 1/' SLmake.inc
make lib what=clean
for i in pblaslib pblasexe toolslib redistlib redistexe scalapacklib \
	scalapackexe example
do
	make $i
# for know, what package have executables
#	pushd TESTING
#	ls x* > ../$i.list
#	mv x* %buildroot%_bindir
#	popd
done

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

mkdir -pv %buildroot%_bindir
mkdir -pv %buildroot%_libdir
mkdir -pv %buildroot%_includedir
mkdir -pv %buildroot%_datadir/%origname/tests
mkdir -pv %buildroot%_datadir/%origname/pblas-tests
mkdir -pv %buildroot%_datadir/%origname/pblas-timing
mkdir -pv %buildroot%_datadir/%origname/redist
mkdir -pv %buildroot%_datadir/%origname/example
mkdir -pv %buildroot%_mandir
rm -f SRC/pblas.h
cp -ar TESTING/x* %buildroot%_bindir/
cp -ar libscalapack*.a %buildroot%_libdir/
cp -ar LIB0/libscalapack*.a %buildroot%_libdir/
cp -ar PBLAS/SRC/*.h %buildroot%_includedir/
cp -ar REDIST/SRC/*.h %buildroot%_includedir/
cp -ar SRC/*.h %buildroot%_includedir/
cp -ar TESTING0/*.dat %buildroot%_datadir/%origname/tests/
cp -ar PBLAS/TESTING/*.dat %buildroot%_datadir/%origname/pblas-tests/
cp -ar PBLAS/TIMING/*.dat %buildroot%_datadir/%origname/pblas-timing/
cp -ar REDIST/TESTING/*.dat %buildroot%_datadir/%origname/redist/
cp -ar EXAMPLE/*.dat %buildroot%_datadir/%origname/example/
cp -ar MANPAGES/man/manl %buildroot%_mandir/

# all in one library

function createScalapack() {
	LNAME=%name$2-full.so
	mkdir tmp
	pushd tmp
	for i in blacs${1}init blacs arpack_LINUX
	do
		ar x %_libdir/lib$i.a
	done
	ar x %buildroot%_libdir/libscalapack_LINUX-0.a
	for i in $(ls *.C); do
		mv $i $i.o
	done
	mpif77 -shared -o ../$LNAME.0 * \
		-Wl,-soname,$LNAME.0 \
		-Wl,-R%mpidir/lib -lmpi_f77 -lmpi \
		-llapack -lopenblas
	popd
	rm -fR tmp
	ln -s $LNAME.0 $LNAME
	install -m644 $LNAME* %buildroot%_libdir
}

#createScalapack F77
#createScalapack C c
#install -d %buildroot%_includedir/%origname
#install -p -m644 %buildroot%_includedir/*.h \
#	$(rpm -ql libblacs-devel|grep '\.h') \
#	$(rpm -ql libarpack-devel|grep '\.h') \
#	%buildroot%_includedir/%origname

# simple shared library

pushd %buildroot%_libdir
mkdir tmp
pushd tmp
LIB=%{name}_LINUX-0
ar x ../$LIB.a
mpif77 -shared -o ../%name.so.%sover * \
	-Wl,-soname,%name.so.%somver \
	-Wl,-R%mpidir/lib -lblacs \
%if_disabled bootstrap
	-larpack_LINUX \
%endif
	-llapack -lopenblas
ln -s %name.so.%sover ../%name.so.%somver
ln -s %name.so.%somver ../%name.so
ln -s %name.so ../$LIB.so
chrpath -r %mpidir/lib ../$LIB.so
rm -f *
popd
rmdir tmp
popd

%files
%doc README
%_libdir/*.so.*
#exclude %_libdir/%{name}*-full.so.*
%_datadir/%origname
%exclude %_datadir/%origname/tests
%exclude %_datadir/%origname/pblas-tests
%exclude %_datadir/%origname/pblas-timing
%exclude %_datadir/%origname/redist
%exclude %_datadir/%origname/example

#files debug
#doc README
#_libdir/*-1.a

%files devel
%_libdir/*.so
#exclude %_libdir/%{name}*-full.so
%_includedir/redist.h
%_includedir/tools.h
%_includedir/pxsyevx.h

#files devel-static
#_libdir/*-0.a

%files -n pblas-tests
%_bindir/x?pblas?tst

%files -n pblas-tests-data
%_datadir/%origname/pblas-tests

%files -n pblas-timing
%_bindir/x?pblas?tim

%files -n pblas-timing-data
%_datadir/%origname/pblas-timing

%files -n pblas-devel
%_includedir/pblas.h
%_includedir/PB*.h

%files -n %origname-redist
%_bindir/x???mr

%files -n %origname-redist-data
%_datadir/%origname/redist

%files -n %origname-tests
%_bindir/*
%exclude %_bindir/x?pblas*
%exclude %_bindir/x???mr
%exclude %_bindir/x?scaex

%files -n %origname-tests-data 
%_datadir/%origname/tests

%files -n %origname-example
%_bindir/x?scaex

%files -n %origname-example-data
%_datadir/%origname/example

%files manpages
%_mandir/manl/*

#files full
#_libdir/%{name}*-full.so.*

#files full-devel
#_libdir/%{name}*-full.so
#_includedir/%origname

%changelog
* Mon Jul 08 2019 Sergey V Turchin <zerg@altlinux.org> 1.8.0-alt19
- build without arpack

* Thu Jul 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.0-alt18
- Rebuilt with new mpi and toolchain

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt17
- Built with OpenBLAS instead of GotoBLAS2

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt16
- Rebuilt with OpenMPI 1.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt15
- Fixed RPATH

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt14
- Rebuilt with GotoBLAS2 1.13-alt3

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt13
- Rebuilt with GotoBLAS2 instead of ATLAS
- Disabled static and *-full packages

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt12
- Rebuilt for debuginfo

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt11
- Rebuilt

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt10
- Rebuilt for soname set-versions

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt9
- Fixed overlinking of libraries

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt8
- Rebuilt without udapl support

* Mon Aug 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt7
- Added missing requirements for devel package

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt6
- Added simple shared library
- Disabled strict aliasing rules

* Sat Aug 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt5
- Added all-in-one shared library

* Thu Jun 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt4
- Rebuild with PIC

* Mon Jun 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt3
- Add requirement on libblacs-devel

* Tue May 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt2
- Rebuild with OpenMPI

* Sun Feb 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus

