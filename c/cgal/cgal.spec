%define _unpackaged_files_terminate_build 1

Name: cgal
Version: 5.0.2
Release: alt1.1
Summary: Easy access to efficient and reliable geometric algorithms
License: Free for non-commertial using
Group: Sciences/Mathematics
Url: https://www.cgal.org/

# https://github.com/CGAL/cgal/releases
Source: CGAL-%version.tar
Source1: CGAL-%version-doc_html.tar

BuildRequires: gcc-c++ gcc-fortran cmake qt5-base-devel qt5-svg-devel
BuildRequires: boost-devel libgmp-devel libgmpxx-devel eigen3
BuildRequires: libGLU-devel libGL-devel libmpfr-devel libtbb-devel
BuildRequires: zlib-devel libX11 phonon-devel
BuildRequires: liblapack-devel libtaucs-devel

ExcludeArch: armh

%description
The goal of the CGAL Open Source Project is to provide easy access to
efficient and reliable geometric algorithms in the form of a C++
library.

%package devel
Summary: Development files of CGAL
Group: Development/C++
Conflicts: %name < %EVR
Obsoletes: %name < %EVR
Conflicts: lib%name-devel < %EVR
Obsoletes: lib%name-devel < %EVR

%description devel
The goal of the CGAL Open Source Project is to provide easy access to
efficient and reliable geometric algorithms in the form of a C++
library.

This Package contains developemnt files of CGAL.

%package devel-doc
Summary: Documentation for CGAL
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
The goal of the CGAL Open Source Project is to provide easy access to
efficient and reliable geometric algorithms in the form of a C++
library.

Thid package contains development documentation for CGAL.

%prep
%setup

%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DCGAL_INSTALL_DOC_DIR=%_defaultdocdir/%name \
	-DWITH_demos:BOOL=false \
	-DWITH_examples:BOOL=false \
	%nil

%cmake_build VERBOSE=1

%install
%cmakeinstall_std

install -d %buildroot%_docdir/%name
cp -fR doc_html %buildroot%_docdir/%name
cp -fR examples %buildroot%_docdir/%name

pushd %buildroot%_docdir/%name
tar -xf %SOURCE1
popd

%files devel
%_bindir/*
%_man1dir/*
%_includedir/*
%_libdir/cmake/CGAL

%files devel-doc
%doc %_docdir/%{name}*

%changelog
* Thu Jul 23 2020 Andrey Cherepanov <cas@altlinux.org> 5.0.2-alt1.1
- NMU: exclude armh from build architectures.

* Wed Apr 15 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.2-alt1
- Updated to upstream version 5.0.2.

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 4.12-alt4
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 4.12-alt3
- NMU: remove %%ubt from release

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.12-alt2
- NMU: rebuilt with boost-1.67.0

* Fri Apr 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.12-alt1
- Updated to upstream version 4.12.

* Tue Sep 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.10-alt2
- Rebuilt with boost 1.65.0.
- Added %%ubt to release.

* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.10-alt1
- Updated to upstream version 4.10
- Qt3 and Qt4 libraries are no longer provided by upstream
- Packaged Qt5 libraries

* Fri Apr 08 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.6-alt2.2
- fix packaging on 64-bit arches other than x86_64

* Thu Apr 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.6-alt2.1
rebuild with new boost (1.57 -> 1.58)

* Mon May 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6-alt2
- Applied changes from FEniCS's mshr

* Mon Apr 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6-alt1
- Version 4.6

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.2-alt1
- Version 4.5.2

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 4.5.1-alt1.1
- rebuild with boost 1.57.0

* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.1-alt1
- Version 4.5.1

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5-alt1
- Version 4.5

* Fri Apr 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4-alt1
- Version 4.4

* Fri Oct 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3-alt1
- Version 4.3

* Fri Apr 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1
- Version 4.2

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt3
- Rebuilt with Boost 1.53.0

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt2
- Rebuilt with Boost 1.52.0

* Thu Oct 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt1
- Version 4.1

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2
- Rebuilt with Boost 1.51.0

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt5
- Rebuilt with new GMP

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt4
- Rebuilt with Boost 1.49.0

* Mon Mar 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt3
- Version 4.0 (release)

* Fri Feb 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt2.beta1
- Built without OSMesa

* Mon Feb 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.beta1
- Version 4.0-beta1

* Thu Dec 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9-alt2
- Version 3.9 (release), thnx iv@

* Sat Aug 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9-alt1.beta1
- Version 3.9-beta1

* Tue Jul 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8-alt2
- Rebuilt with Boost 1.47.0

* Mon May 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8-alt1
- Version 3.8

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7-alt6
- Built with GotoBLAS2 instead of ATLAS

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7-alt5
- Built with GotoBLAS2 instead of ATLAS

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7-alt4
- Rebuilt with Boost 1.46.1

* Thu Mar 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7-alt3
- Rebuilt for debuginfo

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7-alt2
- Rebuilt for soname set-versions

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7-alt1
- Version 3.7

* Tue Jun 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6-alt1
- Version 3.6

* Wed Mar 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt3
- Rebuilt with new Boost

* Thu Dec 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt2
- Add pkg-config file

* Thu Dec 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt0.M51.1
- port into branch 5.1

* Thu Dec 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt1
- Initial build for Sisyphus

