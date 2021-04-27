%define osg_version %(pkg-config --modversion openscenegraph)

Name: osgEarth
Version: 3.1
Release: alt1

Summary: Dynamic map generation toolkit for OpenSceneGraph
License: LGPL
Group: Graphics

Url: http://osgearth.org
Source: osgearth-%version.tar
Patch: geos-3_8-support.patch
Packager: Dmitry Derjavin <dd@altlinux.org>

# Automatically added by buildreq on Wed Sep 22 2010
BuildRequires: cmake gcc-c++ libGL-devel libOpenSceneGraph-devel libXrandr-devel libXrender-devel libXt-devel libcurl-devel libexpat-devel libgdal-devel libgeos-devel libsqlite3-devel libzip-devel
BuildRequires: libGLU-devel
BuildRequires: /usr/bin/osgversion

%description
osgEarth is a scalable terrain rendering toolkit for
OpenSceneGraph. Just create a simple XML file, point it at your
imagery, elevation, and vector data, load it into your favorite OSG
application, and go! osgEarth supports all kinds of data and comes
with lots of examples to help you get up and running quickly and
easily.

%package -n lib%name
Summary: Runtime libraries for osgEarth
Group: System/Libraries

%description -n lib%name
osgEarth is a scalable terrain rendering toolkit for
OpenSceneGraph. Just create a simple XML file, point it at your
imagery, elevation, and vector data, load it into your favorite OSG
application, and go! osgEarth supports all kinds of data and comes
with lots of examples to help you get up and running quickly and
easily.

This package contains runtime libraries for osgEarth.

%package -n lib%name-devel
Summary: Development files for osgEarth
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
osgEarth is a scalable terrain rendering toolkit for
OpenSceneGraph. Just create a simple XML file, point it at your
imagery, elevation, and vector data, load it into your favorite OSG
application, and go! osgEarth supports all kinds of data and comes
with lots of examples to help you get up and running quickly and
easily.

This package contains development files for osgEarth.

%package examples
Summary: Sample applications for osgEarth
Group: Development/Documentation
Requires: %name-data

%description examples
osgEarth is a scalable terrain rendering toolkit for
OpenSceneGraph. Just create a simple XML file, point it at your
imagery, elevation, and vector data, load it into your favorite OSG
application, and go! osgEarth supports all kinds of data and comes
with lots of examples to help you get up and running quickly and
easily.

This package contains sample applications for osgEarth.

%package data
Summary: Sample data files for osgEarth
Group: Development/Documentation
BuildArch: noarch

%description data
osgEarth is a scalable terrain rendering toolkit for
OpenSceneGraph. Just create a simple XML file, point it at your
imagery, elevation, and vector data, load it into your favorite OSG
application, and go! osgEarth supports all kinds of data and comes
with lots of examples to help you get up and running quickly and
easily.

This package contains sample data files for osgEarth.

%prep
%setup -n osgearth-%version
%patch -p1

%build
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.12
%add_optflags -std=c++11
%endif
mkdir BUILD
pushd BUILD
cmake \
	-DCMAKE_BUILD_TYPE="Release" \
	-DCMAKE_INSTALL_PREFIX:PATH=%_usr \
	-DCMAKE_CXX_FLAGS="%optflags" \
	..
%make_build VERBOSE=1
popd

%install
pushd BUILD
%makeinstall_std
# Supposed to take data files
mkdir -p %buildroot%_datadir/osgEarth
cp -a ../data ../tests %buildroot%_datadir/osgEarth
popd

%files -n lib%name
%doc README.md
%_libdir/libosgEarth*.so.*
%_libdir/osgdb*.so

%files -n lib%name-devel
%_includedir/osg*
%_libdir/libosg*.so

%files examples
%_bindir/*

%files data
%_datadir/osgEarth

%changelog
* Mon Dec 07 2020 Andrey Cherepanov <cas@altlinux.org> 3.1-alt1
- New version.

* Tue Jun 16 2020 Andrey Cherepanov <cas@altlinux.org> 3.0-alt1
- New version.

* Tue Mar 03 2020 Grigory Ustinov <grenka@altlinux.org> 2.10.2-alt3
- Fix build with gdal 3.0.4.

* Sat Jul 13 2019 Michael Shigorin <mike@altlinux.org> 2.10.2-alt2
- ensure our CXXFLAGS instead of hardwired -O2
- E2K: explicit -std=c++11

* Fri Jul 12 2019 Andrey Cherepanov <cas@altlinux.org> 2.10.2-alt1
- New version.

* Mon Apr 22 2019 Andrey Cherepanov <cas@altlinux.org> 2.10.1-alt1
- New version.

* Fri Nov 16 2018 Andrey Cherepanov <cas@altlinux.org> 2.10-alt1
- New version.

* Mon Oct 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.9-alt3.gitbc65245
- NMU: Use upstream fix for geos 3.7.0.

* Sat Jun 23 2018 Vitaly Lipatov <lav@altlinux.ru> 2.9-alt2
- NUM: rebuild against OpenSceneGraph 3.4.1

* Fri Feb 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.9-alt1
- New version.
- Drop obsoleted patch.

* Fri Aug 18 2017 Andrey Cherepanov <cas@altlinux.org> 2.8-alt1
- New version
- Add GEOS >= 3.6.0 compatibility from upsteam commit

* Wed Aug 16 2017 Andrey Cherepanov <cas@altlinux.org> 2.7-alt2
- Rebuild with geos 3.6.2

* Thu Oct 01 2015 Michael Shigorin <mike@altlinux.org> 2.7-alt1
- 2.7 built against OpenSceneGraph 3.4.0

* Wed Sep 30 2015 Michael Shigorin <mike@altlinux.org> 2.1.1-alt1.5
- rebuilt against current OpenSceneGraph

* Tue Jul 29 2014 Michael Shigorin <mike@altlinux.org> 2.1.1-alt1.4
- rebuilt against OpenSceneGraph 3.2.1

* Thu Jul 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.3
- Rebuilt with updated geos

* Wed Nov 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.2
- Rebuilt with updated geos

* Thu Sep 26 2013 Michael Shigorin <mike@altlinux.org> 2.1.1-alt1.1.1
- rebuilt against OpenSceneGraph 3.2.0

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.1
- Rebuilt with updated geos

* Wed Apr 18 2012 Dmitry Derjavin <dd@altlinux.org> 2.1.1-alt1
- 2.1.1

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt2.1
- Rebuilt with geos 3.4.0

* Wed Nov 30 2011 Dmitry Derjavin <dd@altlinux.org> 2.1-alt2
- /usr/bin/osgversion dependency added (thanks to iv@);
- osgdb_osgearth moved to osgPlugins;
- examples updated.

* Tue Oct 04 2011 Dmitry Derjavin <dd@altlinux.org> 2.1-alt1
- 2.1

* Wed Dec 22 2010 Dmitry Derjavin <dd@altlinux.org> 1.4.1-alt2
- libGLU-devel added to BuildRequires.

* Wed Sep 22 2010 Dmitry Derjavin <dd@altlinux.org> 1.4.1-alt1
- Initial ALTLinux build.
