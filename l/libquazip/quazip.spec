# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define oname quazip
Name: libquazip
Version: 0.8.1
Release: alt1
Summary: Qt/C++ wrapper for the minizip library
License: GPLv2+ or LGPLv2+
Group: System/Libraries
Url: https://github.com/stachenov/quazip
Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: libqt4-devel
BuildRequires: qt5-base-devel
BuildRequires: doxygen graphviz

%description
QuaZIP is a simple C++ wrapper over Gilles Vollant's ZIP/UNZIP package that
can be used to access ZIP archives. It uses Trolltech's Qt toolkit.

QuaZIP allows you to access files inside ZIP archives using QIODevice API,
and - yes! - that means that you can also use QTextStream, QDataStream or
whatever you would like to use on your zipped files.

QuaZIP provides complete abstraction of the ZIP/UNZIP API, for both reading
from and writing to ZIP archives.

%package devel
Summary: Development files for %oname
Group: Development/C
Requires: %name
Requires: libqt4-devel

%description devel
The %name-devel package contains libraries, header files and documentation
for developing applications that use %oname.

%package qt5
Summary: Qt5 wrapper for the minizip library
Group: System/Libraries

%description qt5
QuaZIP is a simple C++ wrapper over Gilles Vollant's ZIP/UNZIP package that
can be used to access ZIP archives. It uses Trolltech's Qt toolkit.

QuaZIP allows you to access files inside ZIP archives using QIODevice API,
and - yes! - that means that you can also use QTextStream, QDataStream or
whatever you would like to use on your zipped files.

QuaZIP provides complete abstraction of the ZIP/UNZIP API, for both reading
from and writing to ZIP archives.

%package qt5-devel
Summary: Development files for %name
Group: Development/C
Requires: %name-qt5
Requires: qt5-base-devel%{?_isa}

%description qt5-devel
The %name-devel package contains libraries, header files and documentation
for developing applications that use %name.

%prep
%setup

%build
mkdir build-qt4
pushd build-qt4
%cmake_insource .. -DBUILD_WITH_QT4:BOOL=ON
%make_build
popd

mkdir build-qt5
pushd build-qt5
%cmake_insource .. -DBUILD_WITH_QT4:BOOL=OFF
%make_build
popd

doxygen Doxyfile
for file in doc/html/*; do
    touch -r Doxyfile $file
done

%install
%make_install install/fast DESTDIR=%buildroot -C build-qt5
%make_install install/fast DESTDIR=%buildroot -C build-qt4

#remove static library
rm -f %buildroot%_libdir/*.a

%files
%doc COPYING NEWS.txt README.md
%_libdir/libquazip.so.1*

%files devel
%doc doc/html
%_includedir/quazip/
%_libdir/libquazip.so
%_datadir/cmake/Modules/FindQuaZip.cmake

%files qt5
%doc COPYING NEWS.txt README.md
%_libdir/libquazip5.so.1*

%files qt5-devel
%doc doc/html
%_includedir/quazip5/
%_libdir/libquazip5.so
%_datadir/cmake/Modules/FindQuaZip5.cmake

%changelog
* Fri Aug 16 2019 Anton Midyukov <antohami@altlinux.org> 0.8.1-alt1
- Version 0.8.1

* Sat Nov 17 2018 Anton Midyukov <antohami@altlinux.org> 0.7.6-alt1
- Version 0.7.6

* Fri Nov 10 2017 Anton Midyukov <antohami@altlinux.org> 0.7.3-alt1
- Version 0.7.3

* Thu Jun 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1
- Version 0.6.2

* Mon Dec 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1_1.2
- Rebuilt with optflags

* Mon Dec 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1_1.1
- Built for Sisyphus

* Sat Dec 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_1
- converted for ALT Linux by srpmconvert tools

