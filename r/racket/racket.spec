%define _unpackaged_files_terminate_build 1

%define sover 7.3
Name: racket
Version: 7.3
Release: alt1

Summary: Racket programming language

License: LGPL
Group: Development/Scheme
Url: https://racket-lang.org/

Source: %name-%version.tar
Patch1: %name-alt-debuginfo.patch

# do not scan collects for requires and provides
%add_findreq_skiplist  %_libdir/%name/collects/*/*
%add_findreq_skiplist  %_libdir/%name/collects/*/*/*
%add_findprov_skiplist %_libdir/%name/collects/*/*
%add_findprov_skiplist %_libdir/%name/collects/*/*/*

Provides: plt = %EVR
Obsoletes: plt < %EVR

BuildRequires: /proc
BuildRequires: gcc-c++ zlib-devel libjpeg-devel libpng-devel
BuildRequires: libcairo-devel libXaw-devel libXext-devel libXft-devel
BuildRequires: gcc-fortran libpango-devel
BuildRequires: desktop-file-utils libffi-devel libgc-devel
BuildRequires: libgtk+3-devel libgtkglext-devel libwxGTK3.1-devel
BuildRequires: libssl-devel zlib-devel

Requires: lib%name = %EVR
Requires: %name-data = %EVR

%description
Depending on how you look at it, Racket is

* a programming language - a dialect of Lisp and a descendant of
  Scheme;

* a family of programming languages - variants of Racket, and more; or

* a set of tools - for using a family of programming languages.

%package data
Summary: Data for Racket
Group: Development/Scheme

%description data
Depending on how you look at it, Racket is

* a programming language - a dialect of Lisp and a descendant of
  Scheme;

* a family of programming languages - variants of Racket, and more; or

* a set of tools - for using a family of programming languages.

This package contains data for Racket.

%package doc
Summary: Documentation for Racket
Group: Documentation
BuildArch: noarch

%description doc
Depending on how you look at it, Racket is

* a programming language - a dialect of Lisp and a descendant of
  Scheme;

* a family of programming languages - variants of Racket, and more; or

* a set of tools - for using a family of programming languages.

This package contains documentation for Racket.

%package -n lib%name
Summary: Shared libraries of Racket
Group: System/Libraries

%description -n lib%name
Depending on how you look at it, Racket is

* a programming language - a dialect of Lisp and a descendant of
  Scheme;

* a family of programming languages - variants of Racket, and more; or

* a set of tools - for using a family of programming languages.

This package contains shared libraries of Racket.

%package -n lib%name-devel
Summary: Development files of Racket
Group: Development/Scheme
Requires: lib%name = %EVR
Provides: libmzscheme-devel = %EVR
Obsoletes: libmzscheme-devel < %EVR

%description -n lib%name-devel
Depending on how you look at it, Racket is

* a programming language - a dialect of Lisp and a descendant of
  Scheme;

* a family of programming languages - variants of Racket, and more; or

* a set of tools - for using a family of programming languages.

This package contains development files of Racket.

%prep
%setup
%patch1 -p2

%build
# FIXME: %%autoreconf?
# But the configure.ac is not in src/. (It's in src/racket.)
pushd src
%ifarch %ix86
%add_optflags -march=i686 -mtune=i686
%endif
%add_optflags %optflags_shared
%configure \
	--docdir=%_docdir/%name-%version \
	--enable-shared \
	--enable-pthread \
	--enable-gl \
	--enable-xrender \
	--enable-xft \
	--enable-docs=yes \
	--disable-strip
%make_build
popd

%install
# make -j1 avoids a nasty race in Makefile, which made it hang on ppc64le,mipsel
# (and perhaps sometimes on aarch64), and basically doesn't affect the time,
# because "raco setup" should decide on parallelism based on "(processor-count)"
# and limit the number of parallel jobs to 8 on 64bit and 4 on 32bit platforms
# (see racket/collects/setup/option.rkt line 56). However, in practice, we see
# this parallelism on i586,x86_64, but not on ppc64le,aarch64 (it takes 8 hrs).
#
# FIXME: on ppc64le, racket doesn't detect the number of processors:
#
# $ hsh-run --mount=/proc,/dev/pts -- racket -e '(processor-count)'
# 1
# [imz@ppc imz]$ hsh-run --mount=/proc,/dev/pts -- nproc
# 128
#
# Let's set the parameter by force to speedup our builds:
%if "%_pointer_size" == "32"
# don't eat too much memory on 32bit platforms
export PLT_SETUP_OPTIONS="-j $(( %__nprocs > 8 ? 8 : %__nprocs ))"
%else
export PLT_SETUP_OPTIONS='-j %__nprocs'
%endif
%makeinstall_std -j1 -C src docdir=%_docdir/%name-%version

install -p -m644 README %buildroot%_docdir/%name-%version/
sed -i 's|%buildroot||g' %buildroot%_desktopdir/*.desktop

# remove static libraries
rm -f %buildroot%_libdir/*.a

%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/README
%_bindir/*
%_libdir/%name
%_desktopdir/*
%_man1dir/*
%_sysconfdir/*

%files data
%_datadir/%name

%files doc
%doc %_docdir/%name-%version
%exclude %_docdir/%name-%version/README

%files -n lib%name
%_libdir/*-%sover.so

%files -n lib%name-devel
%doc src/README.txt
%_libdir/*.so
%exclude %_libdir/*-%sover.so
%_includedir/*

%changelog
* Tue Jul 16 2019 Mikhail Gordeev <obirvalger@altlinux.org> 7.3-alt1
- Updated to upstream version 7.3

* Tue Jul 16 2019 Ivan Zakharyaschev <imz@altlinux.org> 6.12-alt2
- (.spec):
  + Avoided a nasty race in Makefile.
  + Sped up the build by force on non-intel.

* Mon Dec 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.12-alt1
- Updated to upstream version 6.12 (Closes: #35721)

* Tue Sep 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.10.1-alt1
- Updated to upstream version 6.10.1.

* Wed Jun 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.1-alt2
- Removed %%buildroot from desktop files

* Tue Jun 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.1-alt1
- Version 6.0.1

* Wed Nov 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.6-alt1
- Version 5.3.6

* Tue Jul 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.5-alt1
- Version 5.3.5

* Mon Feb 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.3-alt1
- Version 5.3.3

* Mon Sep 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1
- Version 5.3

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt3
- Fixed build with new glibc

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt2
- Removed RPATH

* Mon Mar 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt1
- Initial build for Sisyphus

