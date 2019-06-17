Name: libfreeimage
Version: 3.18.0
Release: alt4

Summary: Multi-format image decoder library
Group: System/Libraries
License: GPL and FIPL (see the license-fi.txt)
Url: http://freeimage.sourceforge.net/

%define srcversion %(echo %version | tr -d .)

Source: http://downloads.sourceforge.net/freeimage/FreeImage%srcversion.zip
# Unbundle bundled libraries (based on fc patch)
Patch: FreeImage_unbundle.patch
# Fix incorrect path in doxyfile
Patch1: FreeImage_doxygen.patch
# Fix incorrect variable names in BIGENDIAN blocks
Patch2: FreeImage_bigendian.patch
Patch3: FreeImage-3.18.0-alt-return-type.patch

BuildRequires: gcc-c++ libgomp-devel libmng-devel libpng-devel openexr-devel unzip
BuildPreReq: rpm-macros-make libraw-devel zlib-devel libwebp-devel
BuildPreReq: libtiff-devel libopenjpeg2.0-devel libjxr-devel
BuildRequires: dos2unix

%define nameplus %{name}plus

%description
FreeImage is a library project for developers who would like to support
popular graphics image formats like PNG, BMP, JPEG, TIFF and others as needed by
multimedia applications. FreeImage is easy to use, fast, multithreading, safe.

%package -n %nameplus
Summary: FreeImagePlus is a C++ wrapper for FreeImage
Group: System/Libraries
Requires: %name = %version-%release

%description -n %nameplus
The %nameplus package contains C++ wrapper library for %name.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files
for developing applications that use %name.

%package -n %nameplus-devel
Summary: Development files for %nameplus
Group: Development/C++
Requires: %nameplus = %version-%release

%description -n %nameplus-devel
The %nameplus-devel package contains libraries and header files
for developing C++ applications that use %nameplus.

%prep
%setup -n FreeImage
# fix line endings
find ./ -type f -print0| xargs -r0 dos2unix --

%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p2

# remove bundled libraries
rm -r Source/Lib* Source/ZLib Source/OpenEXR
# fix Makefile
sed -i 's|\-o root -g root ||g' Makefile.*
# we can't built due to dependencies on private headers
# see syslibs patch
> Source/FreeImage/PluginG3.cpp
> Source/FreeImageToolkit/JPEGTransform.cpp

%build
sh ./gensrclist.sh
sh ./genfipsrclist.sh
%add_optflags %optflags_shared -fvisibility=hidden
%make_build -f Makefile.gnu
%make_build -f Makefile.fip

%install
%makeinstall_std INSTALLDIR=%buildroot%_libdir
%makeinstall_std INSTALLDIR=%buildroot%_libdir -f Makefile.fip

%files
%_libdir/%name.so.*
%_libdir/%name-%version.so
%doc license-fi.txt Whatsnew.txt README.linux

%files -n %nameplus
%_libdir/%nameplus.so.*
%_libdir/%nameplus-%version.so

%exclude %_libdir/*.a

%files devel
%_includedir/*
%_libdir/libfreeimage.so

%files -n %nameplus-devel
%_libdir/%nameplus.so

%changelog
* Fri May 31 2019 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt4
- added libfreeimageplus{,-devel} subpackages (thx Dmitry Pugachev)

* Thu Apr 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt3
- updated unbundle patch for turbojpeg-2.0.2

* Tue Feb 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt2
- fixed build with -Werror=return-type enabled in g++

* Sat Aug 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0 with modified fc patches and some tricks

* Mon Sep 18 2017 Yuri N. Sedunov <aris@altlinux.org> 3.17.0-alt3
- rebuilt against libwebp.so.7

* Thu Dec 29 2016 Yuri N. Sedunov <aris@altlinux.org> 3.17.0-alt2
- rebuilt against libraw.so.16

* Mon Jun 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.17.0-alt1.1
- small spec cleanup

* Thu Feb 04 2016 Yuri N. Sedunov <aris@altlinux.org> 3.17.0-alt1
- 3.17.0

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt2.2
- rebuilt against libraw.so.15

* Mon Jun 15 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.16.0-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Apr 01 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.16.0-alt2
- Rebuilt with -fvisibility=hidden (ALT#30891).

* Sat Sep 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.16.0-alt1
- Version 3.16.0 (ALT #26750)

* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.15.4-alt2
- Rebuilt with new libraw

* Tue Feb 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.15.4-alt1
- Version 3.15.4

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.15.3-alt3
- Rebuilt with libpng15

* Mon Sep 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.15.3-alt2
- Rebuilt with internal libtiff

* Tue Aug 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.15.3-alt1
- Version 3.15.3

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.0-alt2
- Rebuilt for debuginfo

* Thu Jan 20 2011 Igor Vlasenko <viy@altlinux.ru> 3.12.0-alt1.1
- rebuild for set:provides by request of mithraen

* Tue Sep 08 2009 Victor Forsyuk <force@altlinux.org> 3.12.0-alt1
- 3.12.0
- Build with system libraries instead of internal copies.

* Tue Dec 16 2008 Victor Forsyuk <force@altlinux.org> 3.11.0-alt2
- Remove obsolete ldconfig calls.

* Thu Jul 31 2008 Victor Forsyuk <force@altlinux.org> 3.11.0-alt1
- 3.11.0

* Wed Jul 02 2008 Victor Forsyuk <force@altlinux.org> 3.10.0-alt2
- Fix FTBFS on 64 bit arch.

* Tue Jul 01 2008 Victor Forsyuk <force@altlinux.org> 3.10.0-alt1
- Initial build.
