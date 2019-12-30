%define qdoc_found %{expand:%%(if [ -e %_qt5_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%add_verify_elf_skiplist %_qt5_libdir/libQt5WebKit.so.*
%add_verify_elf_skiplist %_qt5_libdir/libQt5WebKitWidgets.so.*

%global qt_module qtwebkit
%def_disable bootstrap

Name: qt5-webkit
Version: 5.212.0
Release: alt15

Group: System/Libraries
Summary: Qt5 - QtWebKit components
License: LGPL-2.1-or-later and BSD-3-Clause
Url: http://qt.io/
Source: %qt_module-everywhere-src-%version.tar

# FC
Patch2: qtwebkit-5.212.0_cmake_cmp0071.patch
# ALT
Patch10: alt-flags.patch

# Automatically added by buildreq on Mon Sep 30 2013 (-bi)
# optimized out: elfutils fontconfig glib2-devel glibc-devel-static gstreamer-devel libGL-devel libX11-devel libXfixes-devel libfreetype-devel libgst-plugins libqt5-core libqt5-gui libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-v8 libqt5-widgets libstdc++-devel libxml2-devel pkg-config python-base python-modules python-modules-compiler python-modules-encodings python-modules-xml python3 python3-base qt5-base-devel qt5-declarative-devel ruby ruby-stdlibs xorg-compositeproto-devel xorg-fixesproto-devel xorg-renderproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: flex fontconfig-devel gcc-c++ gperf gst-plugins-devel libXcomposite-devel libXext-devel libXrender-devel libgio-devel libicu-devel libjpeg-devel libpng-devel libsqlite3-devel libudev-devel libwebp-devel libxslt-devel perl-Term-ANSIColor python-module-distribute python-module-simplejson qt5-webkit-devel rpm-build-python3 rpm-build-ruby zlib-devel-static
BuildRequires(pre): rpm-macros-qt5
%if_disabled bootstrap
BuildRequires(pre): qt5-tools
%endif
BuildRequires: cmake
BuildRequires: flex fontconfig-devel gcc-c++ libicu-devel libjpeg-devel libpng-devel
BuildRequires: libsqlite3-devel libudev-devel libwebp-devel libxslt-devel libpcre-devel gperf
BuildRequires: pkgconfig(glib-2.0) pkgconfig(gio-2.0)
# pkgconfig(gstreamer-1.0) pkgconfig(gstreamer-plugins-base-1.0) pkgconfig(gstreamer-app-1.0)
BuildRequires: libXcomposite-devel libXext-devel libXrender-devel libdrm-devel
# libGL-devel
BuildRequires: python-module-distribute python-module-simplejson python-module-json rpm-build-python
BuildRequires: ruby ruby-libs
BuildRequires: perl(Term/ANSIColor.pm) perl(Perl/Version.pm) perl(Digest/Perl/MD5.pm)
BuildRequires: zlib-devel libxml2-devel
#BuildRequires: libleveldb-devel
BuildRequires: qt5-base-devel qt5-xmlpatterns-devel qt5-declarative-devel qt5-webchannel-devel
#qt5-location-devel qt5-multimedia-devel qt5-sensors-devel

%description
%summary

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt5-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt5-base-devel
Requires: qt5-declarative-devel
%description devel
%summary.

%package doc
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
BuildArch: noarch
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-webkit
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
%description -n libqt5-webkit
%summary

%package -n libqt5-webkitwidgets
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
%description -n libqt5-webkitwidgets
%summary


%prep
%setup -n %qt_module-everywhere-src-%version
%patch2 -p1
#
%patch10 -p1
syncqt.pl-qt5 Source -version %version

# remove rpath
#find ./ -type f -name \*.pr\* | \
#while read f; do
#    sed -i 's|\(^CONFIG[[:space:]][[:space:]]*+=[[:space:]].*\)rpath|\1|' $f
#    sed -i 's|\([[:space:]]CONFIG[[:space:]][[:space:]]*+=[[:space:]].*\)rpath|\1|' $f
#done

# fix linking
#echo 'QMAKE_LIBS_OPENGL += -lpthread' >> Source/api.pri

%build
%remove_optflags '-g'
%add_optflags -g1 -fpermissive
export LDFLAGS="$LDFLAGS -Wl,--no-keep-memory"
%if_disabled bootstrap
export QT_HASH_SEED=0
%endif
export QT_INSTALL_DOCS="%_qt5_docdir"
export QT_VER="%_qt5_version" QT_VERSION="%_qt5_version"
export QT_VERSION_TAG=`echo "%_qt5_version" | sed 's|\.||g'`
export BUILDDIR="$PWD"
#    -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
cmake \
    -DCMAKE_INSTALL_PREFIX=%_qt5_prefix \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    -DKDE_INSTALL_INCLUDEDIR:PATH=%_qt5_headerdir \
    -DKDE_INSTALL_LIBEXECDIR:PATH=%_qt5_libexecdir \
    -DKDE_INSTALL_LIBDIR:PATH=%_qt5_libdir \
    -DKDE_INSTALL_QMLDIR=%_qt5_qmldir \
    -DPORT=Qt \
    -DCMAKE_BUILD_TYPE=Release \
    -DENABLE_TOOLS=OFF \
    -DCMAKE_C_FLAGS_RELEASE:STRING="%optflags -DNDEBUG" \
    -DCMAKE_CXX_FLAGS_RELEASE:STRING="%optflags -DNDEBUG" \
    -DUSE_LD_GOLD=OFF \
    \
    -DUSE_GSTREAMER=OFF \
    -DUSE_QT_MULTIMEDIA=OFF \
    -DENABLE_GEOLOCATION=OFF \
    -DENABLE_DEVICE_ORIENTATION=OFF \
    -DENABLE_NETSCAPE_PLUGIN_API=OFF \
    -DUSE_LIBHYPHEN=OFF \
    -DUSE_WOFF2=OFF \
    -DENABLE_INSPECTOR_UI=OFF \
    -DENABLE_LINK_PREFETCH=OFF \
    \
%ifnarch %arm aarch64 %ix86 x86_64
    -DENABLE_JIT=OFF \
%endif
%ifnarch %arm aarch64 %ix86 x86_64
    -DUSE_SYSTEM_MALLOC=ON \
%endif
%if_disabled bootstrap
    -DGENERATE_DOCUMENTATION=ON \
%endif
    #
[ "%__nprocs" != 1 ] || export NPROCS=3
%make_build

%install
export QT_INSTALL_DOCS="%_qt5_docdir"
export QT_VER="%_qt5_version" QT_VERSION="%_qt5_version"
export QT_VERSION_TAG=`echo "%_qt5_version" | sed 's|\.||g'`
export BUILDDIR="$PWD"
%make install DESTDIR=%buildroot
%install_qt5_post_qt
%install_qt5_post_common

find %buildroot/%_libdir/cmake/ -type f -name \*.cmake | \
while read f ; do
    sed -i 's|${_IMPORT_PREFIX}/../../\([[:alpha:]]\)|/usr/\1|g' $f
done

%files common
%doc Source/WebCore/LICENSE*

%files doc
%if_disabled bootstrap
%if %qdoc_found
%_qt5_docdir/*
%endif
%endif

%files -n libqt5-webkit
%_qt5_libdir/libQt5WebKit.so.*
%_qt5_libexecdir/QtWeb?*Process
%_qt5_archdatadir/qml/QtWebKit/

%files -n libqt5-webkitwidgets
%_qt5_libdir/libQt5WebKitWidgets.so.*
%_qt5_libexecdir/QtWebProcess

%files devel
%_qt5_headerdir/Qt*/
%_qt5_libdir/libQt*.so
%_qt5_libdatadir/libQt*.so
#%_qt5_libdir/libQt*.prl
#%_qt5_libdatadir/libQt*.prl
%_qt5_libdir/cmake/Qt*/
%_qt5_archdatadir/mkspecs/modules/*.pri
%_pkgconfigdir/Qt*.pc

%changelog
* Tue Dec 17 2019 Sergey V Turchin <zerg@altlinux.org> 5.212.0-alt15
- update from 5.212 branch

* Thu Nov 14 2019 Sergey V Turchin <zerg@altlinux.org> 5.212.0-alt14
- depend on libqt5-core version

* Wed Oct 23 2019 Sergey V Turchin <zerg@altlinux.org> 5.212.0-alt13
- update from 5.212 branch

* Fri Oct 04 2019 Sergey V Turchin <zerg@altlinux.org> 5.212.0-alt12
- update from 5.212 branch

* Thu Mar 21 2019 Sergey V Turchin <zerg@altlinux.org> 5.212.0-alt11
- fix build requires

* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.212.0-alt10
- rebuild with new Qt

* Wed Oct 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.212.0-alt9
- rebuild with new icu

* Mon Sep 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.212.0-alt8
- rebuild with new Qt

* Tue Aug 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.212.0-alt7
- rebuild with new Qt

* Fri Jul 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.212.0-alt6
- fix includes dir in .pc (ALT#35184)

* Wed Jun 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.212.0-alt5
- rebuild with new Qt

* Tue Apr 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.212.0-alt4
- fix build options for aarch64

* Tue Apr 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.212.0-alt3
- rebuild with new Qt

* Thu Feb 01 2018 Sergey V Turchin <zerg@altlinux.org> 5.212.0-alt2
- fix cmake-files

* Tue Jan 30 2018 Sergey V Turchin <zerg@altlinux.org> 5.212.0-alt1
- update to 5.212

* Thu Jan 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1
- new version

* Tue Dec 05 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1
- new version

* Wed Oct 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt2
- turn off multimedia support

* Fri Oct 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1
- new version

* Thu Dec 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1
- new version

* Sun Oct 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt0.M80P.1
- build for M80P

* Wed Oct 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1
- new version

* Mon Jun 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Thu Mar 24 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Wed Feb 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt3
- fix compile on arm64

* Mon Jan 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt2
- rebuild with new libwebp

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Mon Jul 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Tue Jun 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt2
- 5.4.2 release

* Fri Jun 05 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Tue Feb 24 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Fri Dec 12 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Wed Oct 01 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt2
- build with gstreamer-1.0

* Wed Sep 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Wed Jun 25 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Mon Jun 02 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Thu Feb 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.M70P.1
- built for M70P

* Thu Feb 13 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- new version

* Tue Nov 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1.M70P.2
- build docs

* Mon Nov 25 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1.M70P.1
- built for M70P

* Fri Oct 25 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt2
- build docs

* Fri Sep 27 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build
