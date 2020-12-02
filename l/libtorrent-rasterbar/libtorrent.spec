%define _unpackaged_files_terminate_build 1

%def_disable debug
%def_disable static
%def_with python2

%define upname libtorrent-rasterbar
%define soname 9

Name: libtorrent-rasterbar
Epoch: 3
Version: 1.1.13
Release: alt2

Summary: libTorrent is a BitTorrent library written in C++ for *nix
License: BSD
Group: System/Libraries

Url: https://www.rasterbar.com/products/libtorrent/
# https://github.com/arvidn/libtorrent.git
Source: %name-%version.tar
Patch: %name-1.1.9-fedora-system-tommath.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libssl-devel
BuildRequires: gcc-c++ zlib-devel
BuildRequires: glibc-devel glibc-core
BuildRequires: boost-devel boost-asio-devel boost-filesystem
BuildRequires: boost-filesystem-devel boost-program_options-devel
BuildRequires: boost-multiprecision-devel
BuildRequires: python3-devel boost-python3-devel
BuildRequires: libGeoIP-devel
BuildRequires: libtommath-devel

%if_with python2
BuildRequires: python-devel boost-python-devel
%endif

%description
libTorrent is designed to avoid redundant copying and storing of data
that other clients and libraries suffer from. libTorrent features:

* The client has full control over the polling of sockets.
* Sigc++ signals makes it easy for the client to react to events.
* Fast resume which checks the file modification time.
* Direct reading and writing from network to mmap'ed files.
* File hash check uses the same thread; client can control the rate;
  non-blocking and preload to memory with the mincore and madvise.
* File handler: fine-grained use of file read/write permissions, allows
  seeding of read-only files; allows torrents with unlimited number of
  files; opens closed files when mapping chunks to memory, with graceful
  error handling; support for files larger than 2 GB; different download
  priorities for files in the torrent.
* Multi-tracker support.
* No dependency on any specific HTTP library, the client implements a
  wrapper class.
* Dynamic request pipe size.
* Upload and download throttle.
* And much more...

%package -n %name%soname
Summary: libTorrent is a BitTorrent library written in C++ for *nix
Group: System/Libraries
# TODO: remove this obsolete on next soname change
Obsoletes: %name <= 3:1.1.9-alt1

%description -n %name%soname
libTorrent is designed to avoid redundant copying and storing of data
that other clients and libraries suffer from. libTorrent features:

* The client has full control over the polling of sockets.
* Sigc++ signals makes it easy for the client to react to events.
* Fast resume which checks the file modification time.
* Direct reading and writing from network to mmap'ed files.
* File hash check uses the same thread; client can control the rate;
  non-blocking and preload to memory with the mincore and madvise.
* File handler: fine-grained use of file read/write permissions, allows
  seeding of read-only files; allows torrents with unlimited number of
  files; opens closed files when mapping chunks to memory, with graceful
  error handling; support for files larger than 2 GB; different download
  priorities for files in the torrent.
* Multi-tracker support.
* No dependency on any specific HTTP library, the client implements a
  wrapper class.
* Dynamic request pipe size.
* Upload and download throttle.
* And much more...

%package -n %upname-devel
Summary: Development libraries and header files for libTorrent
Group: Development/C++
Requires: %name%soname = %EVR
Provides: libtorrent-rasterbar8-devel = %EVR
Conflicts: libtorrent-rasterbar8-devel < %EVR
Obsoletes: libtorrent-rasterbar8-devel < %EVR
Conflicts: libtorrent-rasterbar7-devel < %EVR
Obsoletes: libtorrent-rasterbar7-devel < %EVR
Conflicts: libtorrent-devel

%description -n %upname-devel
The libtorrent-devel package contains libraries and header files needed
to develop applications using libTorrent.

%if_enabled static
%package -n %upname-devel-static
Summary: Development static libraries for libTorrent
Group: Development/C++
Requires: %name%soname = %EVR
Provides: libtorrent-rasterbar7-devel-static = %EVR
Conflicts: libtorrent-rasterbar7-devel-static < %EVR

%description -n %upname-devel-static
The libtorrent-devel package contains static libraries needed
to develop applications using libTorrent.
%endif

%if_with python2
%package -n python-module-%upname
Summary: libTorrent python bindings
Group: Development/Python
Requires: %name%soname = %EVR
Provides: python-module-libtorrent-rasterbar7 = %EVR
Conflicts: python-module-libtorrent-rasterbar7 < %EVR

%description -n python-module-%upname
The python-module-libtorrent-rasterbar contains
python bindings to libTorrent.
%endif

%package -n python3-module-%upname
Summary: libTorrent python bindings
Group: Development/Python3
Requires: %name%soname = %EVR

%description -n python3-module-%upname
The python3-module-libtorrent-rasterbar contains
python-3 bindings to libTorrent.

%prep
%setup
%patch -p1

mkdir -p build-aux
touch build-aux/config.rpath

%if_with python2
cp -r . ../build-python2
%endif

%build
%add_optflags -fno-strict-aliasing -DTORRENT_USE_WSTRING=1 -DTORRENT_EXPORT_EXTRA=1
%add_optflags -I%_includedir/tommath

%if_with python2
pushd ../build-python2

export PYTHON=%_bindir/python2

%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.20
%add_optflags -std=c++11
%endif

%autoreconf
%configure \
	%{subst_enable static} \
	%{subst_enable debug} \
	--with-boost-libdir=%_libdir \
	--enable-python-binding \
	--with-boost-python=boost_python%{python_version_nodots python2} \
	%nil

%make_build V=1
popd
%endif

export PYTHON=%_bindir/python3

%autoreconf
%configure \
	%{subst_enable static} \
	%{subst_enable debug} \
	--with-boost-libdir=%_libdir \
	--enable-python-binding \
	--with-boost-python=boost_python%{python_version_nodots python3} \
	%nil

%make_build V=1

%install
%if_with python2
pushd ../build-python2/bindings/python
%python_install
popd
%endif

%makeinstall_std

rm -f %buildroot%_libdir/*.la
%if_disabled static
rm -f %buildroot%_libdir/*.a
%endif

%files -n %name%soname
%doc AUTHORS ChangeLog NEWS README.rst
%doc COPYING LICENSE
%_libdir/*.so.*

%files -n %upname-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%if_enabled static
%files -n %upname-devel-static
%_libdir/*.a
%endif

%if_with python2
%files -n python-module-%upname
%python_sitelibdir/libtorrent.so
%python_sitelibdir/*.egg-info
%endif

%files -n python3-module-%upname
%python3_sitelibdir/libtorrent*.so
%python3_sitelibdir/*.egg-info

%changelog
* Thu Nov 07 2019 Michael Shigorin <mike@altlinux.org> 3:1.1.13-alt2
- E2K: explicit -std=c++11
- Minor spec cleanup

* Thu Jul 11 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 3:1.1.13-alt1
- Updated to upstream version 1.1.13.
- Built bindings for python-3 (Closes: #31679).

* Mon Jan 28 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 3:1.1.12-alt1
- Updated to upstream version 1.1.12.
- Updated package names to support shared libs policy.

* Wed Sep 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3:1.1.9-alt1
- Updated to upstream version 1.1.9.

* Wed Jun 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3:1.1.7-alt2
- Rebuilt with fixes pulled from upstream.

* Tue Apr 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3:1.1.7-alt1
- Updated to upstream version 1.1.7.

* Fri Sep 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3:1.1.4-alt2
- Fixed build with new boost.

* Tue Aug 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3:1.1.4-alt1
- Updated to upstream version 1.1.4.

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3:0.16.19-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Fri May 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3:0.16.19-alt1
- Version 0.16.19

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 2:1.0.0-alt3.git20130318.1
- rebuild with boost 1.57.0

* Thu Nov 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:1.0.0-alt3.git20130318
- New snapshot

* Thu Jul 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:1.0.0-alt2.svn8186
- New snapshot

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:1.0.0-alt2.svn7980
- Rebuilt with Boost 1.53.0

* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:1.0.0-alt1.svn7980
- Version 1.0.0

* Mon Dec 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.16.1-alt5.svn7387
- Added necessary provides and conflicts

* Sat Dec 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.16.1-alt4.svn7387
- libtorrent-rasterbar7-devel is libtorrent-rasterbar-devel

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.16.1-alt3.svn7387
- Built release type instead of debug

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.16.1-alt2.svn7387
- Rebuilt with Boost 1.52.0

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.16.1-alt1.svn7387
- Version 0.16.1

* Wed Apr 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.16.0-alt3.svn6278
- Fixed build

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.16.0-alt2.svn6278
- Rebuilt with Boost 1.49.0

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.16.0-alt1.svn6278
- Version 0.16.0

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2:0.15.5-alt0.1.svn6106.1
- Rebuild with Python-2.7

* Wed Oct 12 2011 Alexey Morsov <swi@altlinux.ru> 2:0.15.5-alt0.1.svn6106
- new svn version
- add stealth gear actions

* Thu Sep 01 2011 Alexey Morsov <swi@altlinux.ru> 2:0.15.5-alt0.1.svn5932
- new svn version

* Fri Apr 08 2011 Alexey Morsov <swi@altlinux.ru> 2:0.15.5-alt0.1.svn5420
- new svn version
- fix libboost_serialization version

* Fri Mar 11 2011 Alexey Morsov <swi@altlinux.ru> 2:0.15.5-alt0.1.svn5348
- new svn version
- add libGeoIP
- add optflags to compile against new boost

* Tue Jan 25 2011 Alexey Morsov <swi@altlinux.ru> 2:0.15.0-alt0.1.svn5184
- new svn version

* Fri Dec 17 2010 Alexey Morsov <swi@altlinux.ru> 2:0.15.0-alt0.1.svn5086
- new svn version
- rebuild for boost 1.45

* Tue Dec 07 2010 Alexey Morsov <swi@altlinux.ru> 2:0.15.0-alt0.1.svn5051
- new svn version

* Thu Nov 04 2010 Alexey Morsov <swi@altlinux.ru> 2:0.15.0-alt0.1.svn4956
- new svn version

* Sun Oct 17 2010 Alexey Morsov <swi@altlinux.ru> 2:0.15.0-alt0.1.svn4895
- new svn version

* Mon Aug 23 2010 Alexey Morsov <swi@altlinux.ru> 2:0.15.0-alt0.1.svn4787
- new svn version (commit 67cef5f3c9dfe8b57e77a8b4fd354a6f339d3de0)

* Tue May 25 2010 Alexey Morsov <swi@altlinux.ru> 2:0.15.0-alt0.1.svn4606
- new svn version (commit b60467eb1e34813bfc1e95ccb8fbe0d8615fc0dc)

* Fri Jan 22 2010 Alexey Morsov <swi@altlinux.ru> 2:0.15.0-alt0.1.svn4196
- new svn version (commit a7f780c9249ac9029c558fd194fbad02115d8138)

* Fri Jan 15 2010 Alexey Morsov <swi@altlinux.ru> 2:0.15.0-alt0.1.svn4163
- new svn version (commit 191f998b58045659bfe7a94925049ab420204912)

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.15.0-alt0.1.svn4022.1
- Rebuilt with python 2.6

* Fri Nov 20 2009 Alexey Morsov <swi@altlinux.ru> 2:0.15.0-alt0.1.svn4022
- new svn version (commit efc50b962721acf6e0c360afc74dc1b0413d1f89)

* Sun Nov 01 2009 Alexey Morsov <swi@altlinux.ru> 2:0.15.0-alt0.1.svn3950
- new svn version (commit b2e23dc3212944e4e05dac57d9a029bb1831e298)

* Mon Oct 19 2009 Alexey Morsov <swi@altlinux.ru> 2:0.14.6-alt1
- new version

* Sat Jun 13 2009 Alexey Morsov <swi@altlinux.ru> 2:0.14.4-alt1.1
- build python bindings (patch from crux)

* Tue Jun 09 2009 Alexey Morsov <swi@altlinux.ru> 2:0.14.4-alt1
- new version
- fix #19429 (thanks to viy)

* Sat Mar 21 2009 Alexey Morsov <swi@altlinux.ru> 2:0.14.2-alt1
- new version

* Wed Feb 25 2009 Alexey Morsov <swi@altlinux.ru> 2:0.14.1-alt2
- fix -devel name 

* Wed Dec 31 2008 Alexey Morsov <swi@altlinux.ru> 2:0.14.1-alt1
- new version

* Mon Oct 27 2008 Alexey Morsov <swi@altlinux.ru> 2:0.13.1-alt1.1
- fix build with new boost
  + add boost-asio-devel 

* Sun Jul 20 2008 Alexey Morsov <swi@altlinux.ru> 2:0.13.1-alt1
[ Alexey Morsov ]
- new version
  + change name for libtorrent-rasterbar0.13
    (upstream name change and dso compliance
- spec cleanup
  + remove static
  + put .so only in -devel

* Wed Jun 25 2008 Alexey Morsov <swi@altlinux.ru> 2:0.13-alt3.svn.r2433
- new svn version

* Mon Jun 16 2008 Alexey Morsov <swi@altlinux.ru> 2:0.13-alt2.svn.r2411
- new svn version

* Sat Jun 07 2008 Alexey Morsov <swi@altlinux.ru> 2:0.13-alt2.svn.r2335
- new svn version

* Wed Apr 23 2008 Alexey Morsov <swi@altlinux.ru> 2:0.13-alt1
- 0.13 release

* Tue Mar 25 2008 Alexey Morsov <swi@altlinux.ru> 1:0.13-alt2.rc3
- 0.13rc3

* Wed Jan 02 2008 Alexey Morsov <swi@altlinux.ru> 1:0.13-alt1.svn.r1876
- 0.13svn.r1876

* Mon Dec 10 2007 Alexey Morsov <swi@altlinux.ru> 1:0.13-alt1.svn.r1806b
- 0.13svn.r1806b

* Sat Nov 24 2007 Alexey Morsov <swi@altlinux.ru> 1:0.13-alt1.svn.r1762
- 0.13svn.r1762

* Sat Nov 17 2007 Alexey Morsov <swi@altlinux.ru> 1:0.13-alt1.svn.r1727
- 0.13svn.r1727

* Sat Nov 03 2007 Alexey Morsov <swi@altlinux.ru> 1:0.13-alt1.svn.r1719
- version 0.13svn.r1719

* Thu Oct 25 2007 Alexey Morsov <swi@altlinux.ru> 1:0.13-alt1.svn.r1683
- added support for sparse files.
- introduced speed categories for peers and pieces, to separate
slow and fast peers.
- bug fixes

* Sat Oct 13 2007 Alexey Morsov <swi@altlinux.ru> 1:0.13-alt1.svn.r1672d
- bugs fixes
- some new functionality

* Fri Oct 05 2007 Alexey Morsov <swi@altlinux.ru> 1:0.13-alt1.svn.r1615
- bug fixes
- some improvements
- added UPnP support
- added support for local peer discovery
- added encryption support

* Wed Aug 15 2007 Alexey Morsov <swi@altlinux.ru> 1:0.12-alt1
- version 0.12 release

* Tue Apr 10 2007 Alexey Morsov <swi@altlinux.ru> 0.12-alt1.rc2
- new version
- truncate changelog for this is not the same libtorrent 
(old libtorrent now renamed to librtorrent)

* Fri Dec 22 2006 Alexey Morsov <swi@altlinux.ru> 0.11-alt1
- NMU: version 0.11 (for qBittorrent)
- fix BuildRequires
- add patch for configure (add boost.serialization test)

