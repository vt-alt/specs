Name: mpb
Version: 1.5
Release: alt4
Summary: MIT Photonic Bands
License: GPLv2+
Group: Sciences/Physics
Url: http://ab-initio.mit.edu/wiki/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: /proc
# Automatically added by buildreq on Sun Dec 10 2017
# optimized out: glibc-kernheaders-generic guile18 guile18-devel indent libgfortran-devel libgmp-devel libhdf5-8-seq libltdl7-devel libopenblas-devel libquadmath-devel perl python-base zlib-devel
BuildRequires: gcc-fortran libctl-devel libfftw3-devel libhdf5-devel
BuildRequires: liblapack-devel libnlopt-devel guile-devel

Requires: lib%name = %EVR

%description
The MIT Photonic-Bands (MPB) package is a free program for computing the
band structures (dispersion relations) and electromagnetic modes of
periodic dielectric structures, on both serial and parallel computers.
It was developed by Steven G. Johnson at MIT along with the Joannopoulos
Ab Initio Physics group.

This program computes definite-frequency eigenstates (harmonic modes) of
Maxwell's equations in periodic dielectric structures for arbitrary
wavevectors, using fully-vectorial and three-dimensional methods. It is
especially designed for the study of photonic crystals (a.k.a. photonic
band-gap materials), but is also applicable to many other problems in
optics, such as waveguides and resonator systems. (For example, it can
solve for the modes of waveguides with arbitrary cross-sections.)

%package -n lib%name
Summary: Shared libraries of MIT Photonic Bands (MPB)
Group: System/Libraries

%description -n lib%name
The MIT Photonic-Bands (MPB) package is a free program for computing the
band structures (dispersion relations) and electromagnetic modes of
periodic dielectric structures, on both serial and parallel computers.
It was developed by Steven G. Johnson at MIT along with the Joannopoulos
Ab Initio Physics group.

This package contains shared libraries of MIT Photonic Bands (MPB).

%package -n lib%name-devel
Summary: Development files of MIT Photonic Bands (MPB)
Group: Development/C++
Requires: lib%name = %EVR
Requires: %name = %EVR

%description -n lib%name-devel
The MIT Photonic-Bands (MPB) package is a free program for computing the
band structures (dispersion relations) and electromagnetic modes of
periodic dielectric structures, on both serial and parallel computers.
It was developed by Steven G. Johnson at MIT along with the Joannopoulos
Ab Initio Physics group.

This package contains development files of MIT Photonic Bands (MPB).

%prep
%setup

rm -fR autom4te.cache

%build
%autoreconf

%add_optflags -I%_includedir/ctl -I%_libdir/hdf5-seq/include
export CPPFLAGS="%optflags"

%configure \
	--enable-shared \
	--enable-static=no \
	--with-blas=-lopenblas \
	--with-lapack=-llapack \
	--with-inv-symmetry \
	--with-hermitian-eps \
	--with-libctl
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING COPYRIGHT NEWS.md README* TODO
%_bindir/*
%_man1dir/*
%_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Sat Mar 28 2020 Grigory Ustinov <grenka@altlinux.org> 1.5-alt4
- Build new version.

* Mon Dec 03 2018 Grigory Ustinov <grenka@altlinux.org> 1.5-alt3
- Rebuilt with guile22.

* Sun Dec 10 2017 Dmitry V. Levin <ldv@altlinux.org> 1.5-alt2
- Rebuilt with fftw3.

* Thu Jun 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1
- Version 1.5

* Tue Jul 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt4
- Rebuilt with new libhdf5

* Tue Oct 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt3
- Rebuilt with libctl 3.2.1
- Built with support of HDF5

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt2
- Built with OpenBLAS instead of GotoBLAS2

* Thu Mar 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus

