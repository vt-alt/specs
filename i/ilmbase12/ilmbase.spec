%define libsover 12
%define rname IlmBase

Name: ilmbase12
Version: 2.2.0
Release: alt2

%define common %name-common
%define libhalf libhalf%libsover
%define libiex libiex%libsover
%define libilmthread libilmthread%libsover
%define libimath libimath%libsover
%define libiexmath libiexmath%libsover

Group: System/Libraries
Summary: A high-dynamic-range image file library
License: Modified BSD
URL: http://www.openexr.org/

Requires: %libhalf
Requires: %libiex
Requires: %libilmthread
Requires: %libimath
Requires: %libiexmath
Provides: %rname = %version-%release
Obsoletes: %rname < %version-%release

Source: ilmbase-%version.tar
# ALT
Patch10: ilmbase-2.1.0-alt-linking.patch
Patch11: ilmbase-2.1.0-alt-cmakefiles.patch
Patch12: ilmbase-2.1.0-alt-pkgconfig.patch

# Automatically added by buildreq on Wed Apr 20 2011 (-bi)
# optimized out: elfutils libGL-devel libstdc++-devel pkg-config
#BuildRequires: gcc-c++ glibc-devel libGLU-devel libstdc++-devel
BuildRequires: gcc-c++ glibc-devel libGLU-devel zlib-devel
BuildRequires: cmake kde-common-devel

%description
Half is a class that encapsulates our 16-bit floating-point format.

IlmThread is a thread abstraction library for use with OpenEXR
and other software packages.  It currently supports pthreads and
Windows threads.

Imath implements 2D and 3D vectors, 3x3 and 4x4 matrices, quaternions
and other useful 2D and 3D math functions.

Iex is an exception-handling library.

%package -n %common
Group: System/Configuration/Other
Summary: Common empty package for %name
%description -n %common
Common empty package for %name

%package -n %libhalf
Group: System/Libraries
Summary: %rname library
Requires: %common = %version-%release
Conflicts: ilmbase <= 1.0.1-alt1
%description -n %libhalf
Half is a class that encapsulates our 16-bit floating-point format.

%package -n %libiex
Group: System/Libraries
Summary: %rname library
Requires: %common = %version-%release
Conflicts: ilmbase <= 1.0.1-alt1
%description -n %libiex
Iex is an exception-handling library.

%package -n %libilmthread
Group: System/Libraries
Summary: %rname library
Requires: %common = %version-%release
Conflicts: ilmbase <= 1.0.1-alt1
%description -n %libilmthread
IlmThread is a thread abstraction library for use with OpenEXR
and other software packages.  It currently supports pthreads and
Windows threads.

%package -n %libimath
Group: System/Libraries
Summary: %rname library
Requires: %common = %version-%release
Conflicts: ilmbase <= 1.0.1-alt1
%description -n %libimath
Imath implements 2D and 3D vectors, 3x3 and 4x4 matrices, quaternions
and other useful 2D and 3D math functions.

%package -n %libiexmath
Group: System/Libraries
Summary: %rname library
Requires: %common = %version-%release
%description -n %libiexmath
Imath implements 2D and 3D vectors, 3x3 and 4x4 matrices, quaternions
and other useful 2D and 3D math functions.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/Other
Requires: %common = %version-%release
Conflicts: openexr-devel < 1.6
Conflicts: ilmbase-devel
%description devel
This package contains the static libraries and header files needed for
developing applications with %name


%prep
%setup -q -n ilmbase-%version
%patch10 -p1
%patch11 -p1
%patch12 -p1


%build
%Kcmake
%Kmake

%install
%Kinstall

# create compatibility symlinks
for f in %buildroot/%_libdir/lib*.so ; do
    fname=`basename $f`
    newname=`echo $fname | sed 's|-.*|.so|'`
    [ "$fname" == "$newname" ] \
	|| ln -s $fname %buildroot/%_libdir/$newname
done

%files -n %common

%files
%doc AUTHORS ChangeLog COPYING LICENSE NEWS README

%files -n %libhalf
%_libdir/libHalf.so.%libsover
%_libdir/libHalf.so.%libsover.*

%files -n %libiex
%_libdir/libIex-*.so.%libsover
%_libdir/libIex-*.so.%libsover.*

%files -n %libilmthread
%_libdir/libIlmThread-*.%libsover
%_libdir/libIlmThread-*.so.%libsover.*

%files -n %libimath
%_libdir/libImath-*.so.%libsover
%_libdir/libImath-*.so.%libsover.*

%files -n %libiexmath
%_libdir/libIexMath-*.so.%libsover
%_libdir/libIexMath-*.so.%libsover.*

%files devel
%doc AUTHORS ChangeLog COPYING LICENSE NEWS README
%_includedir/OpenEXR
%_libdir/*.so
%_libdir/pkgconfig/*


%changelog
* Fri Sep 20 2019 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt2
- create compatibility package

* Mon Jun 15 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.2.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Dec 02 2014 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt1
- new version

* Wed Dec 18 2013 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt2
- fix pkgconfig file

* Thu Dec 12 2013 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt1
- new version

* Wed Apr 20 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt6
- fix build requires

* Mon Oct 25 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt5
- fix build requires

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt4
- remove obsoleted macroses

* Fri Aug 22 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0.1-alt3
- fix to package common subpackage

* Fri Aug 22 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0.1-alt2
- split lib* subpackages

* Fri Feb 22 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0.1-alt1
- initial specfile

