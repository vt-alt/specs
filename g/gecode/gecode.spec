Name: gecode
Version: 4.2.1
Release: alt2.git20140902
Summary: Gecode constraint programming solver
License: MIT
Group: Development/Tools
Url: http://www.gecode.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ampl/gecode.git
Source: %name-%version.tar

BuildPreReq: gcc-c++ doxygen graphviz flex
BuildPreReq: libmpfr-devel libqt4-devel libgmp-devel

Requires: lib%name = %EVR

%description
Gecode is a toolkit for developing constraint-based systems and
applications. Gecode provides a constraint solver with state-of-the-art
performance while being modular and extensible.

%package -n lib%name
Summary: Shared libraries of %name
Group: System/Libraries

%description -n lib%name
Gecode is a toolkit for developing constraint-based systems and
applications. Gecode provides a constraint solver with state-of-the-art
performance while being modular and extensible.

This package contains shared libraries of %name.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C++
Requires: lib%name = %EVR
Requires: %name = %EVR

%description -n lib%name-devel
Gecode is a toolkit for developing constraint-based systems and
applications. Gecode provides a constraint solver with state-of-the-art
performance while being modular and extensible.

This package contains development files of %name.

%package -n lib%name-devel-docs
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
Gecode is a toolkit for developing constraint-based systems and
applications. Gecode provides a constraint solver with state-of-the-art
performance while being modular and extensible.

This package contains development documentation for %name.

%prep
%setup

%build
make -f Makefile.contribs
%autoreconf
%configure \
	--enable-examples=no
%make_build

doxygen doxygen.conf

%install
%makeinstall_std

%files
%_bindir/*
%_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-devel-docs
%doc examples doc/html

%changelog
* Tue Jun 04 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.2.1-alt2.git20140902
- Fixed build on ppc64le architecture.

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1.git20140902
- Initial build for Sisyphus

