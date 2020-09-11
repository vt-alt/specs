%define _unpackaged_files_terminate_build 1

%def_with openimageio

# TODO: build docs, build and run tests

%define oname opencolorio

Name:           lib%oname
Version:        1.1.1
Release:        alt4
Summary:        Enables color transforms and image display across graphics apps
Group:          System/Libraries

License:        BSD
URL:            https://opencolorio.org/

# https://github.com/imageworks/OpenColorIO.git
Source:         %name-%version.tar

# patches from Fedora

# Work with system libraries instead of bundled.

# Fix build against yaml-cpp 0.6.0+
# This patch is fine for our case (building against system yaml-cpp)
# but probably a bit too simple-minded to upstream as-is. See
# https://github.com/imageworks/OpenColorIO/issues/517
Patch1:         ocio-1.1.0-yamlcpp060.patch
Patch2:         ocio-glext_h.patch

Patch3:         ocio-1.1.1-upstream-typo-fix.patch

# Utilities
BuildRequires:  cmake gcc-c++
BuildRequires:  help2man

# WARNING: OpenColorIO and OpenImageIO are cross dependent.
# If an ABI incompatible update is done in one, the other also needs to be
# rebuilt.
%if_with openimageio
BuildRequires:  libopenimageio-devel
%endif
BuildRequires:  openexr-devel

# Libraries
BuildRequires:  libGL-devel libGLU-devel
BuildRequires:  libX11-devel libXmu-devel libXi-devel
BuildRequires:  libfreeglut-devel
BuildRequires:  libGLEW-devel
BuildRequires:  zlib-devel

#######################
# Unbundled libraries #
#######################
BuildRequires:  tinyxml-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libyaml-cpp-devel
BuildRequires:  boost-devel

%description
OCIO enables color transforms and image display to be handled in a consistent
manner across multiple graphics applications. Unlike other color management
solutions, OCIO is geared towards motion-picture post production, with an
emphasis on visual effects and animation color pipelines.


%package -n %oname-tools
Summary:        Command line tools for %name
Group:          Other
Requires:       %name = %EVR

%description -n %oname-tools
Command line tools for %oname.


%package devel
Summary:        Development libraries and headers for %name
Group:          Development/Other
Requires:       %name = %EVR

%description devel
Development libraries and headers for %oname.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Remove bundled libraries
rm -f ext/lcms*
rm -f ext/tinyxml*
rm -f ext/yaml*

%ifarch %e2k
# lcc: Lut3DOp.cpp is too sloppy code for my -Werror!
sed -i 's, -Werror,,' src/core/CMakeLists.txt src/pyglue/CMakeLists.txt
%add_optflags -std=c++11
%endif

%build
%cmake_insource \
	-DOCIO_BUILD_STATIC=OFF \
	-DOCIO_BUILD_DOCS=OFF \
	-DOCIO_BUILD_PYGLUE=OFF \
	-DOCIO_BUILD_TESTS=OFF \
	-DUSE_EXTERNAL_YAML=TRUE \
	-DUSE_EXTERNAL_TINYXML=TRUE \
	-DUSE_EXTERNAL_LCMS=TRUE \
%ifnarch x86_64 %e2k
	-DOCIO_USE_SSE=OFF \
%endif
%ifnarch %e2k
	-DOpenGL_GL_PREFERENCE=GLVND \
%endif
	%nil

# LD_LIBRARY_PATH is needed for proper doc generation
LD_LIBRARY_PATH=$(pwd)/src/core %make_build

%install
LD_LIBRARY_PATH=$(pwd)/src/core %makeinstall_std

# Generate man pages
mkdir -p %buildroot%_man1dir
LD_LIBRARY_PATH=$(pwd)/src/core help2man -N -s 1 --version-string=%version \
	-o %buildroot%_man1dir/ociocheck.1 \
	src/apps/ociocheck/ociocheck
LD_LIBRARY_PATH=$(pwd)/src/core help2man -N -s 1 --version-string=%version \
	-o %buildroot%_man1dir/ociobakelut.1 \
	src/apps/ociobakelut/ociobakelut

%if_with openimageio
LD_LIBRARY_PATH=$(pwd)/src/core help2man -N -s 1 --version-string=%version \
	-o %buildroot%_man1dir/ocioconvert.1 \
	src/apps/ocioconvert/ocioconvert
LD_LIBRARY_PATH=$(pwd)/src/core help2man -N -s 1 --version-string=%version \
	-o %buildroot%_man1dir/ociolutimage.1 \
	src/apps/ociolutimage/ociolutimage
%endif

# Fix location of cmake files.
mkdir -p %buildroot%_datadir/cmake/Modules
find %buildroot -name "*.cmake" -exec mv {} %buildroot%_datadir/cmake/Modules/ \;

%files
%doc LICENSE
%doc ChangeLog README.md
%_libdir/*.so.*
%dir %_datadir/ocio
%_datadir/ocio/setup_ocio.sh

%files -n %oname-tools
%_bindir/*
%_man1dir/*

%files devel
%_datadir/cmake/Modules/*
%_includedir/OpenColorIO/
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Tue Apr 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt4
- Rebuilt with openimageio support.

* Tue Apr 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt3
- Bootstrapped rebuild.

* Mon Jul 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt2
- Rebuilt with openimageio support.

* Sat Jul 13 2019 Michael Shigorin <mike@altlinux.org> 1.1.1-alt1.1
- E2K:
  + explicit -std=c++11
  + avoid unwarranted -Werror
  + build without libglvnd for now

* Mon May 27 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt1
- Updated to upstream version 1.1.1.

* Mon Oct 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1
- Initial build for ALT.

* Mon Sep 24 2018 Richard Shaw <hobbes1069@gmail.com> - 1.1.0-9
- Obsolete Python2 library and build Python3 library.

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-8
- Rebuilt for glew 2.1.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 22 2018 Adam Williamson <awilliam@redhat.com> - 1.1.0-6
- Rebuild with bootstrap disabled, so we get docs again

* Thu Feb 22 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.0-5
- Rebuild

* Tue Feb 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.1.0-4
- support %%bootstrap (no docs, no tests)
- enable bootstrap mode on f28+ to workaround bug #1546964

* Mon Feb 19 2018 Adam Williamson <awilliam@redhat.com> - 1.1.0-3
- Fix build with yaml-cpp 0.6+ (patch out bogus hidden visibility)
- Fix build with GCC 8 (issues in Python bindings, upstream PR #518)
- Rebuild for yaml-cpp 0.6.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Richard Shaw <hobbes1069@gmail.com> - 1.1.0-1
- Update to latest upstream release.

* Sun Jan 07 2018 Richard Shaw <hobbes1069@gmail.com> - 1.0.9-20
- Rebuild for OpenImageIO 1.8.7.

* Wed Dec 06 2017 Richard Shaw <hobbes1069@gmail.com> - 1.0.9-19
- Fix ambiguous Python 2 dependency declarations
  https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3
  
* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.0.9-16
- Rebuild due to bug in RPM (RHBZ #1468476)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 1.0.9-14
- Rebuild for glew 2.0.0

* Mon Oct 03 2016 Richard Shaw <hobbes1069@gmail.com> - 1.0.9-13
- Rebuild for new OpenImageIO.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Richard Shaw <hobbes1069@gmail.com> - 1.0.9-10
- Rebuild for OpenImageIO 1.6.9.

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 1.0.9-9
- Rebuild for glew 1.13

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.9-7
- Rebuilt for GCC 5 C++11 ABI change

* Wed Jan 28 2015 Richard Shaw <hobbes1069@gmail.com> - 1.0.9-6
- Rebuild for OpenImageIO 1.5.11.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Richard Shaw <hobbes1069@gmail.com> - 1.0.9-3
- Rebuild for updated OpenImageIO 1.4.7.

* Mon Jan 13 2014 Richard Shaw <hobbes1069@gmail.com> - 1.0.9-2
- Add OpenImageIO as build requirement to build additional command line tools.
  Fixes BZ#1038860.

* Wed Nov  6 2013 Richard Shaw <hobbes1069@gmail.com> - 1.0.9-1
- Update to latest upstream release.

* Mon Sep 23 2013 Richard Shaw <hobbes1069@gmail.com> - 1.0.8-6
- Rebuild against yaml-cpp03 compatibility package.

* Mon Aug 26 2013 Richard Shaw <hobbes1069@gmail.com> - 1.0.8-5
- Fix for new F20 feature, unversion doc dir. Fixes BZ#1001264

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 11 2012 Richard Shaw <hobbes1069@gmail.com> - 1.0.8-1
- Update to latest upstream release.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 26 2012 Richard Shaw <hobbes1069@gmail.com> - 1.0.7-4
- Only use SSE instructions on x86_64.

* Wed Apr 25 2012 Richard Shaw <hobbes1069@gmail.com> - 1.0.7-3
- Misc spec cleanup for packaging guidelines.
- Disable testing for now since it fails on the build servers.

* Wed Apr 18 2012 Richard Shaw <hobbes1069@gmail.com> - 1.0.7-1
- Latest upstream release.

* Thu Apr 05 2012 Richard Shaw <hobbes1069@gmail.com> - 1.0.6-1
- Latest upstream release.

* Wed Nov 16 2011 Richard Shaw <hobbes1069@gmail.com> - 1.0.2-1
- Initial release.
