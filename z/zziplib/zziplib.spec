%def_with largefile
%def_with manpages

Name: zziplib
Version: 0.13.69
Release: alt3

Summary: Lightweight library to easily extract data from zip files
License: LGPL/MPL
Group: System/Libraries

URL: http://zziplib.sourceforge.net/
Source: http://downloads.sourceforge.net/zziplib/zziplib-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: libSDL-devel python-modules xmlto zip zlib-devel

%description
The zziplib provides read access to zipped files in a zip-archive, using
compression based solely on free algorithms provided by zlib. It also provides
a functionality to overlay the archive filesystem with the filesystem of the
operating system environment.

%package devel
Summary: Files needed to develop programs using zziplib
Group: Development/C
Requires: %name = %version-%release

%description devel
The zziplib provides read access to zipped files in a zip-archive, using
compression based solely on free algorithms provided by zlib. It also provides
a functionality to overlay the archive filesystem with the filesystem of the
operating system environment.

This package contains files needed to develop programs using zziplib.

%package utils
Summary: ZZipLib utilites
Group: Archiving/Compression
Requires: %name = %version-%release

%description utils
The zziplib provides read access to zipped files in a zip-archive, using
compression based solely on free algorithms provided by zlib. It also provides
a functionality to overlay the archive filesystem with the filesystem of the
operating system environment.

This package contains some useful ZZipLib utilites.

%prep
%setup
%patch0 -p1
sed -i 's|^\(CFLAGS.*\)|\1 -g|' $(find ./ -name Makefile.in)

%build
export PYTHON=/usr/bin/python2
find . -name '*.py' | xargs sed -i 's@#! /usr/bin/python@#! %__python@g;s@#! /usr/bin/env python@#! %__python@g'
autoconf
%configure --enable-sdl --disable-static %{subst_with largefile}
# strip rpath
subst 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' */libtool
subst 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' */libtool
%make_build

%install
%makeinstall_std %{?_with_manpages: install-man3}

%files
%_libdir/lib*.so.*

%files devel
%doc docs/README.SDL
%_libdir/lib*.so
%_pkgconfigdir/*.pc
%_datadir/aclocal/*.m4
%_includedir/*
%if_with manpages
%_man3dir/*
%endif

%files utils
%_bindir/*

%changelog
* Mon Nov 18 2019 Anton Farygin <rider@altlinux.ru> 0.13.69-alt3
- force python-2.7 to build documentation

* Wed Aug 21 2019 Anton Farygin <rider@altlinux.ru> 0.13.69-alt2
- added upstream fixes for security issues (fixes: CVE-2018-16548, CVE-2018-17828)

* Tue Apr 03 2018 Anton Farygin <rider@altlinux.ru> 0.13.69-alt1
- 0.13.69

* Sun Jul 23 2017 Anton Farygin <rider@altlinux.ru> 0.13.66-alt1
- 0.13.66

* Fri Mar 16 2012 Victor Forsiuk <force@altlinux.org> 0.13.62-alt1
- 0.13.62

* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 0.13.60-alt2
- Fix RPATH issue.

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.60-alt1.1
- Rebuilt for debuginfo

* Thu Dec 30 2010 Victor Forsiuk <force@altlinux.org> 0.13.60-alt1
- 0.13.60

* Fri Nov 26 2010 Victor Forsiuk <force@altlinux.org> 0.13.59-alt2
- Rebuilt for soname set-versions.

* Tue Apr 06 2010 Victor Forsiuk <force@altlinux.org> 0.13.59-alt1
- 0.13.59

* Thu Jul 09 2009 Victor Forsyuk <force@altlinux.org> 0.13.56-alt1
- 0.13.56

* Thu Jun 18 2009 Victor Forsyuk <force@altlinux.org> 0.13.54-alt1
- 0.13.54

* Mon Dec 29 2008 Victor Forsyuk <force@altlinux.org> 0.13.50-alt1
- 0.13.50

* Wed Dec 17 2008 Victor Forsyuk <force@altlinux.org> 0.13.49-alt2
- Remove obsolete ldconfig calls.

* Tue Mar 20 2007 Victor Forsyuk <force@altlinux.org> 0.13.49-alt1
- 0.13.49 with security fix, see http://www.securitylab.ru/forum/read.php?FID=21&TID=40858&MID=326187
- More accurate License tag (dual LGPL/MPL).
- Build (conditionally) with man pages.

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.13.38-alt1.1
- Rebuilt for new pkg-config dependencies.

* Mon May 16 2005 Victor Forsyuk <force@altlinux.ru> 0.13.38-alt1
- Author suggests not to use unmaintained and deep frozen 0.10.x anymore.
  So we switch to developer branch - 0.13.
- Add URL.
- Enable build with SDL.
- Update buildreqs.

* Thu May 06 2004 Sir Raorn <raorn@altlinux.ru> 0.10.82-alt1
- Built for Sisyphus
