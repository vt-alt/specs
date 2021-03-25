%define _unpackaged_files_terminate_build 1

%define oname superlu
%define over 4.0
%define somver 4
%define sover %somver.2.0
Name: %oname%over
Version: 4.3
Release: alt9

Summary: A set of subroutines to solve a sparse linear system A*X=B
License: BSD-like
Group: Sciences/Mathematics

Url: http://acts.nersc.gov/superlu/
Source: %{oname}_%version.tar
Source1: http://www.netlib.org/clapack/what/testing/matgen/clatm1.c
Source2: http://www.netlib.org/clapack/what/testing/matgen/zlatm1.c
Source3: http://www.netlib.org/clapack/CLAPACK-3.1.1/TESTING/MATGEN/blaswrap.h

Provides: %oname = %version-%release
Requires: lib%name = %version-%release

BuildRequires: gcc-fortran gcc-c++ liblapack-devel
BuildRequires: csh doxygen graphviz ghostscript-utils
#BuildRequires: texlive-latex-recommended texlive-extra-utils

%description
SuperLU contains a set of subroutines to solve a sparse linear system
A*X=B. It uses Gaussian elimination with partial pivoting (GEPP).
The columns of A may be preordered before factorization; the
preordering for sparsity is completely separate from the factorization.
SuperLU provides functionality for both real and complex matrices, in both
single and double precision.

%package -n lib%name
Summary: Shared libraries of SuperLU
Group: System/Libraries
Provides: lib%oname = %version-%release

%description -n lib%name
SuperLU contains a set of subroutines to solve a sparse linear system
A*X=B. It uses Gaussian elimination with partial pivoting (GEPP).
The columns of A may be preordered before factorization; the
preordering for sparsity is completely separate from the factorization.
SuperLU provides functionality for both real and complex matrices, in both
single and double precision.

This package contains shared libraries of SuperLU.

%package -n lib%oname-devel
Summary: Development files of SuperLU
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%oname-devel
SuperLU contains a set of subroutines to solve a sparse linear system
A*X=B. It uses Gaussian elimination with partial pivoting (GEPP).
The columns of A may be preordered before factorization; the
preordering for sparsity is completely separate from the factorization.
SuperLU provides functionality for both real and complex matrices, in both
single and double precision.

This package contains development files of SuperLU.

%package -n lib%oname-devel-doc
Summary: Documentation for SuperLU
Group: Development/Documentation
BuildArch: noarch

%description -n lib%oname-devel-doc
SuperLU contains a set of subroutines to solve a sparse linear system
A*X=B. It uses Gaussian elimination with partial pivoting (GEPP).
The columns of A may be preordered before factorization; the
preordering for sparsity is completely separate from the factorization.
SuperLU provides functionality for both real and complex matrices, in both
single and double precision.

This package contains documentation for SuperLU.

%prep
%setup
install -m644 %SOURCE1 %SOURCE2 %SOURCE3 TESTING/MATGEN
mkdir lib

%build
sed -i "s|(HOME)|$PWD|" make.inc
sed -i "s|(LIBDIR)|%_libdir|" make.inc
%ifarch %e2k riscv64
sed -i "s|-lopenblas|-lblas|" make.inc
%define blas -lblas
%else
%define blas -lopenblas
%endif
%ifarch %e2k
sed -i "s|-lgfortran||" make.inc
%define gfortran %nil
%else
%define gfortran -lgfortran
%endif
%make install
%make lib
%make testing

pushd EXAMPLE
%make_build
popd

#pushd DOC/latex
#make_build
#popd

pushd TESTING
%make_build
popd

%install
install -d %buildroot%_bindir
install -d %buildroot%_datadir/%name/examples
install -d %buildroot%_libdir
install -d %buildroot%_includedir
install -d %buildroot%_docdir/%name/html
install -d %buildroot%_docdir/%name/pdf
install -m644 SRC/*.h %buildroot%_includedir
install -m644 lib/*.a TESTING/MATGEN/libtmglib.a %buildroot%_libdir
install -m644 DOC/*.pdf %buildroot%_docdir/%name/pdf
install -m644 DOC/html/* %buildroot%_docdir/%name/html

install -m755 TESTING/?test TESTING/?test.csh %buildroot%_bindir
pushd EXAMPLE
rm -f *.o Makefile
chmod -x cg20.cua
mv README cg20.cua *.c %buildroot%_datadir/%name/examples/
install -m755 * %buildroot%_bindir
popd

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i %name.$i
done
popd

# shared libraries
pushd %buildroot%_libdir
for i in libsuperlu_%over libtmglib; do
	if [ "$i" = "libtmglib" ]; then
		ADDLIB="-L. -lsuperlu_%over"
	fi
	ar x $i.a
	g++ -shared *.o $ADDLIB -llapack %blas %gfortran -lm \
		-Wl,-soname,$i.so.%somver -o $i.so.%sover
	ln -s $i.so.%sover $i.so.%somver
	ln -s $i.so.%somver $i.so
	rm -f *.o
done
ln -s libsuperlu_%over.so libsuperlu.so
popd

# remove unpackaged files
rm -f %buildroot%_libdir/*.a

%files
%doc README
%_bindir/*
%_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%oname-devel
%_libdir/*.so
%_includedir/*

%files -n lib%oname-devel-doc
%_docdir/%name

# TODO:
# - redo doc subpackage with tex?
# - install -p

%changelog
* Thu Jul 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3-alt9
- Added devel symlink libsuperlu.so -> libsuperlu_%%over.so.

* Thu Feb 14 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.3-alt8
- exclude %%arm from crippled arches

* Tue Feb 12 2019 Nikita Ermakov <arei@altlinux.org> 4.3-alt7
- liblapack is built with libblas.so on riscv64, not libopenblas.so
- Minor spec changes

* Sun Jun 10 2018 Michael Shigorin <mike@altlinux.org> 4.3-alt6
- support e2kv4 through %%e2k macro
- gear: avoid tarball compression
- minor spec cleanup

* Mon Nov 20 2017 Andrew Savchenko <bircoph@altlinux.org> 4.3-alt5
- Fix build on e2k.

* Thu Nov 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3-alt4
- Fixed build with gcc-6.

* Tue Mar 12 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.3-alt3
- on %arm liblapack is built with libblas, not libopenblas

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3-alt2
- Built with OpenBLAS instead of GotoBLAS2

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3-alt1
- Version 4.3

* Wed Oct 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1
- Version 4.2

* Tue May 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt1
- Version 4.1
- Disabled devel-static package

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt6
- Rebuilt with GotoBLAS2 1.13-alt3

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt5
- Built with GotoBLAS2 instead of ATLAS

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt4
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt3
- Rebuilt for debuginfo

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt2
- Fixed underlinking of libraries

* Mon Dec 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1
- Version 4.0 (soname changed)
- Rebuilt with texlive instead of tetex

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt7
- Added shared libraries and additional documentation

* Thu Jun 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt6
- Resolved conflicts with ctest and dapl*-utils

* Sun Jun 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt5
- Rebuild with PIC

* Fri Jun 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt4
- Added examples

* Tue May 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt3
- Resolve conflict with superlu_dist

* Tue May 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt2
- Added explicit conflict with superlu_dist

* Fri Apr 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt1
- Initial build for Sisyphus
