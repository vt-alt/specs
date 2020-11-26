%define sover 1.0.0
%define libquazip libquazip1-qt5_%sover

%define rname quazip
Name: quazip-qt5
Version: 1.1
Release: alt1

Group: System/Libraries
Summary: Qt/C++ wrapper for the minizip library
Url: https://github.com/stachenov/quazip
License: GPL-2.0-or-later OR LGPL-2.1-or-later

Source: %name-%version.tar

# Automatically added by buildreq on Wed Nov 18 2020 (-bi)
# optimized out: cmake-modules elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libqt5-core libqt5-network libqt5-test libsasl2-3 libssl-devel libstdc++-devel pkg-config python-modules python2-base python3 python3-base python3-module-paste rpm-build-python3 sh4 zlib-devel
#BuildRequires: cmake doxygen fonts-ttf-dejavu fonts-ttf-gnu-freefont-mono fonts-ttf-google-droid-sans graphviz python3-dev python3-module-mpl_toolkits qt5-base-devel zlib-devel-static
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: qt5-base-devel zlib-devel
BuildRequires: doxygen graphviz

%description
QuaZip is the C++ wrapper for Gilles Vollant's ZIP/UNZIP package
(AKA Minizip) using Trolltech's Qt library.

If you need to write files to a ZIP archive or read files from one
using QIODevice API, QuaZip is exactly the kind of tool you need.

%package -n %libquazip
Summary: Qt wrapper for the minizip library
Group: System/Libraries
%description -n %libquazip
QuaZip is the C++ wrapper for Gilles Vollant's ZIP/UNZIP package
(AKA Minizip) using Trolltech's Qt library.

If you need to write files to a ZIP archive or read files from one
using QIODevice API, QuaZip is exactly the kind of tool you need.

%package devel
Summary: Development files for %rname
Group: Development/C
Requires: %libquazip
Requires: qt5-base-devel
%description devel
The %name-devel package contains libraries, header files and documentation
for developing applications that use %rname.

%prep
%setup


%build
%cmake \
    -DQUAZIP_QT_MAJOR_VERSION=5 \
    #
%cmake_build

doxygen Doxyfile
for file in doc/html/*; do
    touch -r Doxyfile $file
done


%install
%make install -C BUILD DESTDIR=%buildroot


%files -n %libquazip
%doc COPYING NEWS.txt *.md
%_libdir/libquazip1-qt5.so.%sover
%_libdir/libquazip1-qt5.so.*

%files devel
%doc doc/html
%_includedir/QuaZip-Qt*/
%_libdir/lib*.so
%_libdir/cmake/QuaZip-Qt*/
%_pkgconfigdir/quazip*-qt*.pc

%changelog
* Wed Nov 18 2020 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- initial build

