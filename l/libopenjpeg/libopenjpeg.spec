%define _unpackaged_files_terminate_build 1

%define oname openjpeg
%define sover 5

Name: lib%oname
Version: 1.5.2
Release: alt1

Summary: JPEG 2000 codec library
License: BSD
Group: System/Libraries
URL: http://www.openjpeg.org/

# https://github.com/uclouvain/openjpeg.git
Source: %name-%version.tar

Patch1: %name-alt-dont-install-extra-files.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: libtiff-devel liblcms2-devel libpng-devel zlib-devel

%description
OpenJPEG is an open-source JPEG 2000 codec written in C. This package contains
runtime libraries for applications that use OpenJPEG.

%package -n lib%oname%sover
Summary: JPEG 2000 codec library
Group: System/Libraries

%description -n lib%oname%sover
OpenJPEG is an open-source JPEG 2000 codec written in C. This package contains
runtime libraries for applications that use OpenJPEG.

%package devel
Summary: Development tools for programs which will use the %oname library
Group: Development/C
Requires: lib%oname%sover = %EVR

%description devel
The %name-devel package includes the header files necessary for developing
programs which will use the %oname library.

%package -n %oname-tools
Summary: JPEG 2000 command line tools
Group: Graphics
Requires: lib%oname%sover = %EVR

%description -n %oname-tools
OpenJPEG is an open-source JPEG 2000 codec written in C.

%prep
%setup
%patch1 -p1

# remove bundled libraries to ensure system ones are used
rm -rf thirdparty/{include,liblcms2,libpng,libtiff,libz}

%build
%cmake \
	-DOPENJPEG_INSTALL_LIB_DIR=%_lib \
	%nil

%cmake_build

%install
%cmakeinstall_std

# compat symlink, currently used at least by gpac
ln -s openjpeg-1.5/openjpeg.h %buildroot%_includedir/openjpeg.h

%files -n lib%oname%sover
%doc LICENSE
%doc AUTHORS CHANGES NEWS README THANKS
%_libdir/lib*.so.*

%files devel
%_includedir/*
%_libdir/lib*.so
%_libdir/openjpeg-*
%_pkgconfigdir/*.pc
%_man3dir/*.3*

%files -n %oname-tools
%_bindir/*
%_man1dir/*.1*

%changelog
* Mon Jul 29 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.2-alt1
- Updated to upstream version 1.5.2.
- Switched to soname proposed by upstream.

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.3
- Rebuilt with libtiff5

* Tue Aug 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.2
- Rebuilt for debuginfo

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.1
- Rebuilt for soname set-versions

* Mon Feb 22 2010 Victor Forsiuk <force@altlinux.org> 1.3-alt1
- Initial build.
