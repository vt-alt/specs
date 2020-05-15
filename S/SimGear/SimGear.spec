%define origver 2020.1

Name: SimGear
Version: %origver
Release: alt1

Summary: Simulator Construction Tools

License: GPL
Group: System/Libraries
Url: http://www.flightgear.org

Packager: Michael Shigorin <mike@altlinux.org>

# Source-url: https://sourceforge.net/projects/flightgear/files/release-%origver/simgear-%version.tar.bz2
Source: %name-%version.tar
Patch0: simgear-3.2.0-fedora-format.patch
Patch1: simgear-3.6.0-fedora-aarch64.patch
Patch2: %name-g++8.patch
Patch3: simgear-2018.2.2-alt-e2k.patch

# Automatically added by buildreq on Sat Mar 03 2012
# optimized out: cmake-modules libGL-devel libICE-devel libOpenThreads-devel libSM-devel libX11-devel libXau-devel libXext-devel libopenal-devel libstdc++-devel xorg-kbproto-devel xorg-xproto-devel
BuildRequires: boost-devel-headers cmake gcc-c++ libGLU-devel libOpenSceneGraph-devel libXi-devel libXt-devel libalut-devel libapr1-devel zlib-devel libcurl-devel

BuildRequires: cmake libapr1-devel
BuildRequires: libexpat-devel

%description
SimGear is a set of open-source libraries designed to be used
as building blocks for quickly assembling 3d simulations, games,
and visualization applications.

%package -n libsimgear
Summary: Simulation library
Group: System/Libraries

%description -n libsimgear
SimGear is a set of open-source libraries designed to be used
as building blocks for quickly assembling 3d simulations, games,
and visualization applications.

%package -n libsimgear-devel
Summary: Simulation library (development part)
Group: Development/C
Provides: SimGear = %version
Provides: SimGear-devel = %version
Obsoletes: SimGear-devel < 1.0.0
Conflicts: SimGear-devel < 1.0.0

# from SimGearTargets.cmake
Requires: libOpenSceneGraph-devel libOpenThreads-devel
Requires: zlib-devel libcurl-devel libopenal-devel libGL-devel libGLU-devel

%description -n libsimgear-devel
SimGear is a set of open-source libraries designed to be used as
building blocks for quickly assembling 3d simulations, games,
and visualization applications.

This package contains header files for SimGear.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p2
%patch3 -p2
#sed -i "s|\${CMAKE_INSTALL_LIBDIR}/cmake/SimGear|%_libdir/cmake/SimGear|" CMakeLists.txt

%build
%add_optflags %optflags_shared
# /usr/src/RPM/BUILD/SimGear-2020.1/simgear/io/HTTPRepository.cxx:267:16: error: return-statement with a value, in function returning 'void' [-fpermissive]
#         return "";
%add_optflags -fpermissive
%ifarch e2k
%add_optflags -fno-error-always-inline
%endif
%cmake_insource \
	-DCMAKE_BUILD_TYPE=Release \
	-DSIMGEAR_SHARED=ON \
	-DSYSTEM_EXPAT=ON \
	-DENABLE_TESTS=OFF
%make_build

%install
%makeinstall_std

%files -n libsimgear
%doc AUTHORS README* Thanks
%_libdir/*.so.*

%files -n libsimgear-devel
%_libdir/*.so
%_includedir/simgear
%_libdir/cmake/%name/

%changelog
* Tue May 12 2020 Michael Shigorin <mike@altlinux.org> 2020.1-alt1
- 2020.1
- build with system expat
- turn -devel-static subpackage into -devel

* Sun Aug 04 2019 Michael Shigorin <mike@altlinux.org> 2018.2.2-alt3
- E2K: initial support (ported from the skipped 2017.2.1-alt1)

* Wed Feb 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 2018.2.2-alt2
- no return statement in the non-void function fixed (according g++8)

* Thu Jun 21 2018 Vitaly Lipatov <lav@altlinux.ru> 2018.2.2-alt1
- new version (2018.2.2) with rpmgs script

* Sat Feb 20 2016 Michael Shigorin <mike@altlinux.org> 2016.1.1-alt1
- 2016.1

* Wed Sep 30 2015 Michael Shigorin <mike@altlinux.org> 3.6.0-alt0.1
- 3.6.0-RC
- updated fedora patches

* Fri Jul 24 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt2
- added another fedora patch
- disabled tests following fedora too (to fix FTBFS)

* Thu Feb 19 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Feb 10 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt0.2
- 3.4.0-RC2

* Wed Oct 22 2014 Michael Shigorin <mike@altlinux.org> 3.2.0-alt1
- 3.2.0

* Sat Feb 22 2014 Michael Shigorin <mike@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Feb 05 2014 Michael Shigorin <mike@altlinux.org> 3.0.0-alt0.3
- 3.0.0-rc3

* Tue Nov 26 2013 Michael Shigorin <mike@altlinux.org> 2.12.1-alt1
- 2.12.1

* Thu Sep 26 2013 Michael Shigorin <mike@altlinux.org> 2.12.0-alt1
- 2.12.0

* Mon Feb 18 2013 Michael Shigorin <mike@altlinux.org> 2.10.0-alt1
- 2.10
- added svn client support to fetch scenery

* Wed Nov 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0-alt2.1
- Rebuilt with -fPIC

* Thu Sep 06 2012 Michael Shigorin <mike@altlinux.org> 2.8.0-alt2
- added patch by iv@ to fix FTBFS against boost-1.51

* Sat Aug 18 2012 Michael Shigorin <mike@altlinux.org> 2.8.0-alt1
- 2.8.0

* Mon Jun 25 2012 Michael Shigorin <mike@altlinux.org> 2.6.0-alt2
- applied fedora patch to fix CVE-2012-2090

* Sat Mar 03 2012 Michael Shigorin <mike@altlinux.org> 2.6.0-alt1
- 2.6.0
  + cmake build
  + patch dropped (fix included with this release)
- minor spec cleanup
- buildreq

* Thu Dec 15 2011 Michael Shigorin <mike@altlinux.org> 2.4.0-alt3
- band-aid to build against boost 1.48

* Mon Sep 26 2011 Michael Shigorin <mike@altlinux.org> 2.4.0-alt2
- rebuilt against libOpenSceneGraph-3.0.1

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 2.4.0-alt1.3
- updated an Url:

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 2.4.0-alt1.2
- backdated 2.0.0-alt2 merge (was a mere soname rebuild)

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 2.4.0-alt1.1
- rebuilt for Sisyphus

* Sun Sep 11 2011 Andrew Clark <andyc@altlinux.org> 2.4.0-alt1
- version update to 2.4.0-alt1

* Thu Mar 10 2011 Michael Shigorin <mike@altlinux.org> 2.0.0-alt2
- rebuilt with current OpenSceneGraph

* Thu Mar 11 2010 Andrew Clark <andyc@altlinux.org> 2.0.0-alt1
- version update to 2.0.0-alt1
- spec cleanup
- buildreq

* Sun May 31 2009 Michael Shigorin <mike@altlinux.org> 1.9.1-alt3
- added Conflicts: SimGear-devel (as there obviously is)

* Wed May 13 2009 Michael Shigorin <mike@altlinux.org> 1.9.1-alt2
- adapted gentoo patch to fix FTBFS with gcc-4.4

* Sun Mar 22 2009 Michael Shigorin <mike@altlinux.org> 1.9.1-alt1
- 1.9.1
- merged spec with one from my git.alt (see also #13080)
- me as a Packager:
- buildreq

* Wed Dec 03 2008 Igor Zubkov <icesik@altlinux.org> 1.0.0-alt2
- fix build

* Wed Jan 09 2008 Albert R. Valiev <darkstar@altlinux.ru> 1.0.0-alt1.1
- Fixed buildrequies (autoconf/automake dependecies)

* Tue Jan 08 2008 Albert R. Valiev <darkstar@altlinux.ru> 1.0.0-alt1
- 1.0.0
- Now uses system libexpat (#8251)

* Sat Dec 22 2007 Michael Shigorin <mike@altlinux.org> 1.0.0-alt1
- 1.0.0
- renamed binary package to libsimgear-devel-static (#13080)
- built with JPEG Factory

* Sat Aug 05 2006 Michael Shigorin <mike@altlinux.org> 0.3.10-alt1
- 0.3.10

* Thu Mar 02 2006 Albert R. Valiev <darkstar@altlinux.ru> 0.3.9-alt1.1
- Updated build requirements.

* Sat Dec 03 2005 Albert R. Valiev <darkstar@altlinux.ru> 0.3.9-alt1
- new version

* Tue Mar 01 2005 Albert R. Valiev <darkstar@altlinux.ru> 0.3.8-alt2
- Parallel build turned of (cause it fails to build with it...)

* Fri Jan 21 2005 Albert R. Valiev <darkstar@altlinux.ru> 0.3.8-alt1
- Update to 0.3.9 version

* Tue Sep 14 2004 Albert R. Valiev <darkstar@altlinux.ru> 0.3.7-alt1.pre1
- Update to 0.3.7-pre1 version

* Sat Jun 14 2003 Albert R. Valiev <darkstar@altlinux.ru> 0.3.3-alt2
- Fixed rights in package

* Sat Jun 14 2003 Albert R. Valiev <darkstar@altlinux.ru> 0.3.3-alt1
- Initial build to sisyphus
