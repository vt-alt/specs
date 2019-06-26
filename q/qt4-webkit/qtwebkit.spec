
%def_disable gstreamer

Name: qt4-webkit
Version: 2.3.4
Release: alt7
Epoch: 1

Group: System/Libraries
Summary: WebKit library for the Qt4 GUI toolkit
License: LGPLv2 / GPLv3
Url: http://trac.webkit.org/wiki/QtWebKit

Source: qtwebkit-%version.tar
# FC
Patch1: qtwebkit-2.3-save_memory.patch
Patch2: webkit-qtwebkit-23-no_rpath.patch
Patch3: webkit-qtwebkit-23-gcc5.patch
Patch4: webkit-qtwebkit-23-private_browsing.patch
# SuSE
Patch101: 04_enable_debug_information.diff
Patch102: 03_hide_std_symbols.diff
Patch103: 02_add_nostrip_for_debug_packages.diff
Patch104: defines_qt_webkit.diff
Patch105: do-not-force-optimization-level.diff
Patch106: libQtWebKit4-gcc47.patch
Patch107: MediaPlayerPrivateGStreamer-should-take-ownership-of-the-playbin.patch
Patch108: buffer-ranges.patch

# Automatically added by buildreq on Sat May 16 2015 (-bi)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel glibc-devel-static gstreamer1.0-devel kde4libs libGL-devel libX11-devel libXext-devel libXrender-devel libcloog-isl4 libdbusmenu-qt2 libfreetype-devel libgio-devel libgnome-keyring libgpg-error libgst-plugins1.0 libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-location libqt4-network libqt4-opengl libqt4-script libqt4-sensors libqt4-sql libqt4-svg libqt4-test libqt4-xml libqt4-xmlpatterns libstdc++-devel libxml2-devel pkg-config python-base python-modules python-modules-encodings python-modules-xml ruby ruby-stdlibs xorg-renderproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: flex gcc-c++ git-core gperf gst-plugins1.0-devel libdb4-devel libjpeg-devel libsqlite3-devel libsubversion-auth-gnome-keyring libsubversion-auth-kwallet libudev-devel libwebp-devel libxslt-devel perl-Term-ANSIColor phonon-devel python-module-google python-modules-json qt4-mobility-devel rpm-build-ruby subversion zlib-devel-static
BuildRequires: flex gcc-c++ gperf
%if_enabled gstreamer
BuildRequires: pkgconfig(gstreamer-1.0) pkgconfig(gstreamer-app-1.0)
%endif
BuildRequires: libjpeg-devel libwebp-devel libpng-devel
BuildRequires: libpcre-devel libicu-devel libsqlite3-devel libxslt-devel zlib-devel
BuildRequires: perl-Term-ANSIColor rpm-build-ruby python-modules-json python-modules-xml
BuildRequires: libqt4-devel phonon-devel
#BuildRequires: qt4-mobility-devel

%description
%summary

%package -n libqt4-webkit
Summary: %summary
Group: System/Libraries
#Requires: qt4-common
Provides: libQtWebKit4 = %version-%release
%description -n libqt4-webkit
%summary

%package -n libqt4-webkit-devel
Group: Development/KDE and QT
Summary: Development files for %name
Conflicts: qt4-devel <= 4.8.6-alt4
%description -n libqt4-webkit-devel
%summary.

%prep
%setup -q -n qtwebkit-%version

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1

%build
%remove_optflags '-g'
%add_optflags -Wno-expansion-to-defined
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
export PATH=`pwd`/bin:%_qt4dir/bin:$PATH
export QTDIR=%_qt4dir

jitopts=""
%ifnarch x86_64
jitopts="DEFINES+=ENABLE_JIT=0 DEFINES+=ENABLE_YARR_JIT=0 DEFINES+=ENABLE_ASSEMBLER=0"
%endif

mkdir -p BUILD
pushd    BUILD
export WEBKITOUTPUTDIR=`pwd`
../Tools/Scripts/build-webkit \
  --qt \
  --no-webkit2 \
  --release \
  --qmakearg="CONFIG+=production_build CONFIG+=use_system_icu QMAKE_CFLAGS+=\"%optflags\" QMAKE_CXXFLAGS+=\"%optflags\" \
%if_enabled gstreamer
  DEFINES+=USE_GSTREAMER=1 \
%endif
  DEFINES+=ENABLE_VIDEO=0 DEFINES+=ENABLE_NETSCAPE_PLUGIN_API=0 DEFINES+=ENABLE_WEB_AUDIO=0 DEFINES+=ENABLE_WEBGL=0 \
  DEFINES+=HAVE_LIBWEBP=1 $jitopts" \
%ifarch %ix86
  --no-force-sse2 \
%endif
  --system-malloc \
  #
popd


%install
make install INSTALL_ROOT=%buildroot -C BUILD/Release

# clean .pc
for f in %buildroot/%_pkgconfigdir/*.pc
do
    sed -i -E "s|-L$RPM_BUILD_DIR/?\S+||g" $f
done


%files -n libqt4-webkit
%_libdir/libQtWebKit.so.4*
%_qt4dir/imports/QtWebKit/*

%files -n libqt4-webkit-devel
%_datadir/qt4/mkspecs/modules/qt_webkit.pri
%_includedir/qt4/QtWebKit/
%_libdir/libQtWebKit.prl
%_libdir/libQtWebKit.so
%_pkgconfigdir/QtWebKit.pc

%changelog
* Tue Jun 25 2019 Sergey V Turchin <zerg@altlinux.org> 1:2.3.4-alt7
- simplify features

* Fri Oct 19 2018 Sergey V Turchin <zerg@altlinux.org> 1:2.3.4-alt6
- fix build requires

* Tue Oct 02 2018 Sergey V Turchin <zerg@altlinux.org> 1:2.3.4-alt5
- build without qtmobility
- remove -g compile flag for all archs

* Tue Oct 10 2017 Sergey V Turchin <zerg@altlinux.org> 1:2.3.4-alt4
- rebuild with new libwebp

* Mon Jan 25 2016 Sergey V Turchin <zerg@altlinux.org> 1:2.3.4-alt3
- rebuild with new libwebp

* Tue Dec 01 2015 Sergey V Turchin <zerg@altlinux.org> 1:2.3.4-alt2
- provide libQtWebKit4

* Fri May 15 2015 Sergey V Turchin <zerg@altlinux.org> 1:2.3.4-alt1
- initial build

