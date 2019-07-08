%define _unpackaged_files_terminate_build 1
%def_disable arpack

%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 4
%define sover %somver.10.0
Name: mumps
Version: 4.10.0
Release: alt10
Summary: MUltifrontal Massively Parallel sparse direct Solver
License: Free
Group: Sciences/Mathematics
Url: http://mumps.enseeiht.fr/

Source: MUMPS_%version.tar
Source1: Makefile.inc
Source2: Makefile.inc.seq

BuildRequires: %mpiimpl-devel libopenblas-devel
BuildRequires: libscotch-devel libparmetis-devel
BuildRequires: libscalapack-devel libblacs-devel
%if_enabled arpack
# circular build deps with scalapack
BuildRequires: libarpack-devel
%endif

%description
MUMPS solves a sparse system of linear equations A x = b
using Gaussian elimination. Please read the README file and
the documentation for a complete list of functionalities.
Documentation and publications related to
MUMPS can also be found at http://mumps.enseeiht.fr/
or at http://graal.ens-lyon.fr/MUMPS

%package -n lib%name-headers
Summary: Headers for MUMPS
Group: Development/Other
BuildArch: noarch

%description -n lib%name-headers
MUMPS solves a sparse system of linear equations A x = b
using Gaussian elimination.

This package contains headers for MUMPS.

%package -n lib%name-devel-doc
Summary: Documentation for MUMPS
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
MUMPS solves a sparse system of linear equations A x = b
using Gaussian elimination.

This package contains development documentation for MUMPS.

%package -n lib%name
Summary: Shared libraries of MUMPS
Group: System/Libraries

%description -n lib%name
MUMPS solves a sparse system of linear equations A x = b
using Gaussian elimination.

This package contains shared libraries of MUMPS.

%package -n lib%name-devel
Summary: Development files of MUMPS
Group: Development/Other
Requires: lib%name-headers = %EVR
Requires: lib%name = %EVR
Conflicts: lib%name-devel < %EVR
Obsoletes: lib%name-devel < %EVR

%description -n lib%name-devel
MUMPS solves a sparse system of linear equations A x = b
using Gaussian elimination.

This package contains development files of MUMPS.

%package -n lib%name-devel-static
Summary: Static libraries of MUMPS
Group: Development/Other
Requires: lib%name-headers = %EVR
Requires: lib%name-devel = %EVR
Conflicts: lib%name-devel < %EVR

%description -n lib%name-devel-static
MUMPS solves a sparse system of linear equations A x = b
using Gaussian elimination.

This package contains static libraries of MUMPS.

%package -n lib%name-seq
Summary: Shared libraries of MUMPS (sequential version)
Group: System/Libraries

%description -n lib%name-seq
MUMPS solves a sparse system of linear equations A x = b
using Gaussian elimination.

This package contains shared libraries of MUMPS (sequential version).

%package -n lib%name-seq-devel
Summary: Development files of MUMPS (sequential version)
Group: Development/Other
Requires: lib%name-headers = %EVR
Requires: lib%name = %EVR
Conflicts: lib%name-devel < %EVR
Obsoletes: lib%name-devel < %EVR

%description -n lib%name-seq-devel
MUMPS solves a sparse system of linear equations A x = b
using Gaussian elimination.

This package contains development files of MUMPS (sequential version).

%package -n lib%name-seq-devel-static
Summary: Static libraries of MUMPS (sequential version)
Group: Development/Other
Requires: libfakempi-devel = %EVR
Requires: lib%name-headers = %EVR
Requires: lib%name-devel = %EVR
Conflicts: lib%name-devel < %EVR

%description -n lib%name-seq-devel-static
MUMPS solves a sparse system of linear equations A x = b
using Gaussian elimination.

This package contains static libraries of MUMPS (sequential version).

%package -n libfakempi-devel
Summary: Sequential MPI static library
Group: Development/Other

%description -n libfakempi-devel
This is sequential MPI static library, dummy MPI implementation for
uniprocessor machines only, no parallel.

%prep
%setup
install -m644 %SOURCE1 %SOURCE2 .
sed -i "s|@TOPDIR@|$PWD|" Makefile.inc*
sed -i 's|\-lmetis|-lparmetis|g' Make.inc/Makefile.*
%if_disabled arpack
sed -i '/^SCALAP/s/-larpack_LINUX//' Makefile.inc
%endif


%build
mpi-selector --yes --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir

function buildIt() {
	for i in clean all; do
		%make \
			LIBDIR=%_libdir \
			LIBEXECDIR=%_libdir \
			MPIDIR=%mpidir \
			TOPDIR=$PWD $i \
			LIBEXT=.a \
			LIBOTHERS="-lscalapack -lscotchmetis -lblacs -lmpi -lpthread" \
			INCS="-I%mpidir/include"
	done
}

mkdir lib
buildIt

mkdir -p par/lib
cp PORD/lib/*.a par/lib
rm -f lib/libpord.a
cp lib/* par/lib
mkdir -p par/bin
cp examples/c_example examples/?simpletest par/bin

cp -f Makefile.inc.seq Makefile.inc
#sed -i -e '15s/c_example//' examples/Makefile
buildIt

pushd examples
for i in s d c z; do
	mv ${i}simpletest ${i}simpletest_seq
done
mv c_example c_example_seq
popd
pushd lib
for i in $(ls|sed 's/\.a//'); do
	mv $i.a ${i}_seq.a
done
popd

mv libseq/libmpiseq.a libseq/libmpi.a

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_includedir/PORD
install -d %buildroot%_docdir/lib%name-devel
install -d %buildroot%_libdir/fakempi/lib
install -d %buildroot%_libdir/fakempi/include

install -m755 par/bin/* examples/*_seq %buildroot%_bindir
install -m644 par/lib/* lib/* %buildroot%_libdir
install -p -m644 include/* src/*.h %buildroot%_includedir
install -p -m644 PORD/include/*.h %buildroot%_includedir/PORD
install -p -m644 doc/* %buildroot%_docdir/lib%name-devel
install -p -m644 libseq/*.a %buildroot%_libdir/fakempi/lib
install -p -m644 libseq/*.h %buildroot%_libdir/fakempi/include

# shared libraries

function makeShared() {
	if [ "$2" = "" ]; then
		LIBS="$ADDLIB"
	else
		LIBS="$ADDLIB_SEQ"
	fi
	if [ "$1" = "libdmumps" -o "$1" = "libsmumps" ]; then
		FINLIB=-lopenblas
	elif [ "$1" = "libmumps_common" ]; then
		FINLIB=-lpthread
	else
		FINLIB=
	fi
	ar x ../$1$2.a
	mpif77 -shared * -L.. $LIBS \
		-lscotchmetis -lesmumps -lscalapack -lblacs \
%if_enabled arpack
		-larpack_LINUX \
%endif
		-Wl,-R%mpidir/lib \
		$FINLIB \
		-Wl,-soname,$1$2.so.%somver -o ../$1$2.so.%sover
	ln -s $1$2.so.%sover ../$1$2.so.%somver
	ln -s $1$2.so.%somver ../$1$2.so
	rm -f *
}

pushd %buildroot%_libdir
mkdir tmp
pushd tmp
for i in pord mumps_common cmumps dmumps smumps zmumps
do
	makeShared lib$i
	makeShared lib$i _seq
	ADDLIB="-l$i $ADDLIB"
	ADDLIB_SEQ="-l${i}_seq $ADDLIB_SEQ"
done
popd
rmdir tmp
popd

%files
%doc ChangeLog LICENSE README
%_bindir/*

%files -n lib%name-headers
%_includedir/*

%files -n lib%name
%_libdir/*.so.*
%exclude %_libdir/*_seq.so.*

%files -n lib%name-devel
%_libdir/*.so
%exclude %_libdir/*_seq.so

%files -n lib%name-devel-static
%_libdir/*.a
%exclude %_libdir/*_seq.a

%files -n lib%name-seq
%_libdir/*_seq.so.*

%files -n lib%name-seq-devel
%_libdir/*_seq.so

%files -n lib%name-seq-devel-static
%_libdir/*_seq.a

%files -n libfakempi-devel
%_libdir/fakempi

%files -n lib%name-devel-doc
%_docdir/lib%name-devel

%changelog
* Fri Jul 05 2019 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt10
- build without arpack

* Thu Dec 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.10.0-alt9
- Updated interpackage dependencies and build architectures.

* Mon Nov 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.10.0-alt8
- Fixed build.

* Tue Jul 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.0-alt7
- Fixed build

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.0-alt6
- Built with OpenBLAS instead of GotoBLAS2

* Sun Jun 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.0-alt5
- Rebuilt with OpenMPI 1.6

* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.0-alt4
- Fixed build

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.0-alt3
- Fixed RPATH

* Tue Sep 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.0-alt2
- Rebuilt with parmetis 4.0

* Fri Sep 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.0-alt1
- Version 4.10.0

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.2-alt7
- Rebuilt with GotoBLAS2 1.13-alt3

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.2-alt6
- Built with GotoBLAS instead of ATLAS

* Sat Feb 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.2-alt5
- Rebuilt with parmetis 3.1.1-alt10

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.2-alt4
- Rebuilt for debuginfo

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.2-alt3
- Fixed overlinking of libraries

* Tue Jul 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.2-alt2
- Rebuilt with reformed ParMetis

* Thu Jun 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.2-alt1
- Version 4.9.2

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8.4-alt3
- Added shared libraries

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8.4-alt2
- Rebuild with PIC

* Wed May 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8.4-alt1
- Initial build for Sisyphus

