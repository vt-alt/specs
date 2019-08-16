%define oname libqwt
%define ver_major 6.1
Name: %{oname}6-qt5
Version: %ver_major.4
Release: alt2

Summary: 2D plotting widget extension to the Qt5 GUI

License: LGPL
Group: System/Libraries
Url: http://sourceforge.net/projects/qwt

# https://qwt.svn.sourceforge.net/svnroot/qwt/trunk/qwt
Source: http://sourceforge.net/projects/qwt/files/qwt/%version/qwt-%version.tar.bz2
#Source: qwt-%version.tar
Patch0: qwt-6.1.1-pkgconfig.patch
Patch1: qwt-6.1.2-qt_install_paths.patch
Patch2: qwt-6.1.3-no_rpath.patch
Patch3: qwt-qt5.patch

#Provides: %oname = %version-%release
BuildRequires(pre): rpm-macros-qt5
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-svg-devel
BuildRequires: libXext-devel doxygen graphviz
BuildRequires: chrpath

%description
Qwt is an extension to the Qt GUI library from Troll Tech AS.
The Qwt library contains widgets and components which are
primarily useful for technical and scientifical purposes.
It includes a 2-D plotting widget, different kinds of sliders,
and much more.

Package build with Qt5.

%package devel
Summary: Development tools for programs which uses Qwt Widget set
Group: Development/C
#Provides: %oname-devel = %version-%release
Requires: %name = %version-%release

%description devel
The libqwt-devel package contains the header files and libraries
necessary for developing programs using the Qwt Widget set

If you want to develop programs which will use this set of widgets,
you should install this package. You need also to install the libqwt package.

Package build with Qt5.

%prep
%setup -n qwt-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

find . -type f -name '*.pro' |while read f; do
echo 'QMAKE_CXXFLAGS += %optflags' >> $f
done

%build
%qmake_qt5 QWT_CONFIG+=QwtMathML QWT_CONFIG+=QwtPkgConfig
%make_build

%install
%make_install install INSTALL_ROOT=%buildroot
rm -fr %buildroot%_datadir/qt5/doc
rm -fr %buildroot%_datadir/qt5/features

%files
%doc README COPYING
%_libdir/libqwt-qt5.so.*
%_libdir/libqwtmathml-qt5.so.*

%files devel
%_includedir/qt5/qwt
%_libdir/libqwt-qt5.so
%_libdir/libqwtmathml-qt5.so
%_libdir/pkgconfig/*.pc

%changelog
* Mon Aug 12 2019 Anton Midyukov <antohami@altlinux.org> 6.1.4-alt2
- Fix install PATHs
- Add pkgconfig

* Sun Mar 24 2019 Andrey Cherepanov <cas@altlinux.org> 6.1.4-alt1
- Initial build for Sisyphus.
