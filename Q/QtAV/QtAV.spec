# TODO
%define _qt5_mkspecs %_libdir/qt5/mkspecs
%define libname libqtav

Name: QtAV
Version: 1.13.0
Release: alt1

Summary: A cross-platform multimedia framework based on Qt and FFmpeg
License: LGPL v2.1
Group: System/Libraries

Url: http://qtav.org/
# Source-git: https://github.com/wang-bin/QtAV.git
Source: %name-%version.tar
Patch1: alt-qt5.15.patch

BuildRequires(pre): rpm-macros-qt5
BuildRequires: gcc-c++

# Automatically added by buildreq on Mon Dec 12 2016
# optimized out: fontconfig gcc-c++ libGL-devel libX11-devel libXext-devel libavcodec-devel libavutil-devel libcdio-paranoia libdc1394-22 libgpg-error libjson-c libopencore-amrnb0 libopencore-amrwb0 libp11-kit libqt5-core libqt5-gui libqt5-network libqt5-opengl libqt5-qml libqt5-quick libqt5-sql libqt5-svg libqt5-widgets libraw1394-11 libstdc++-devel python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-script-devel qt5-xmlpatterns-devel xorg-videoproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: libXv-devel libass-devel libuchardet-devel libva-devel
BuildRequires: qt5-base-devel qt5-multimedia-devel qt5-phonon-devel qt5-websockets-devel qt5-declarative-devel qt5-svg-devel
BuildRequires: libavdevice-devel libavfilter-devel libavformat-devel libswscale-devel
BuildRequires: libopenal-devel libpulseaudio-devel libswresample-devel


%description
A cross-platform multimedia framework based on Qt and FFmpeg.
High performance. User & developer friendly.
Supports Android, iOS, Windows store and desktops.

%package -n %libname-devel-doc
BuildArch: noarch
Summary: Documentation files for %name
Group: Development/C++

%description -n %libname-devel-doc
Documentation files for %name.

%package -n %libname
Summary: A cross-platform multimedia framework based on Qt and FFmpeg
Group: System/Libraries
Conflicts: %libname-qml-devel < %EVR

%description -n %libname
A cross-platform multimedia framework based on Qt and FFmpeg.
High performance. User & developer friendly.
Supports Android, iOS, Windows store and desktops.

%package -n %libname-widgets
Summary: A cross-platform multimedia framework based on Qt and FFmpeg
Group: System/Libraries
Requires: %libname = %version-%release

%description -n %libname-widgets
A cross-platform multimedia framework based on Qt and FFmpeg.
High performance. User & developer friendly.
Supports Android, iOS, Windows store and desktops.
Widgets part.

%package -n %libname-devel
Summary: Development files for %name
Group: Development/Other
Requires: %libname = %version-%release
Requires: qt5-base-devel

%description -n %libname-devel
Development files for %name.

%package -n %libname-qml-devel
Summary: Development files for %name qml
Group: Development/Other
Requires: %libname-devel = %version-%release

%description -n %libname-qml-devel
Development files for %name qml.

%prep
%setup
%patch1 -p1
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -name '*.cpp' -o -name '*.hpp' -o -name '*.h' |
	xargs -r sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
# broken build with gnu++14 (gcc6's default)
%add_optflags -std=gnu++11
%qmake_qt5 -config no_rpath
%make_build

%install
# TODO: use install_qt5
%installqt5
# drop Player / QML Player
rm -rf %buildroot/{%_desktopdir,%_docdir,%_iconsdir,%_qt5_prefix/bin,%_bindir}
rm -f examples/*/Makefile
rm -f examples/Makefile

%files -n %libname
%doc README.md
%_libdir/libQtAV.so.*
%_qt5_qmldir/QtAV/

%files -n %libname-widgets
%_libdir/libQtAVWidgets.so.*

%files -n %libname-devel
%_qt5_headerdir/QtAV/
%_qt5_headerdir/QtAVWidgets/

%_qt5_mkspecs/features/*.prf
%_qt5_mkspecs/modules/*.pri
%_libdir/libQtAV.prl
%_libdir/libQtAVWidgets.prl
%_libdir/libQtAV.so
%_libdir/libQtAVWidgets.so

%files -n %libname-devel-doc
%doc examples Changelog
%doc doc/UseQtAVinYourProjects.md

%changelog
* Mon Sep 07 2020 Sergey V Turchin <zerg@altlinux.org> 1.13.0-alt1
- new version

* Sun Sep 01 2019 Michael Shigorin <mike@altlinux.org> 1.12.0-alt5
- E2K: strip UTF-8 BOM for lcc < 1.24

* Tue Feb 26 2019 Vitaly Lipatov <lav@altlinux.ru> 1.12.0-alt3
- rebuild with libass9

* Tue Jun 19 2018 Anton Farygin <rider@altlinux.ru> 1.12.0-alt2
- rebuilt for ffmpeg-4.0

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.12.0-alt1.1
- NMU: added URL

* Sat Aug 05 2017 Vitaly Lipatov <lav@altlinux.ru> 1.12.0-alt1
- new version 1.12.0 (with rpmrb script)

* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt3
- rebuild with ffmpeg

* Tue Jan 24 2017 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt2
- drop unneeded qml subpackage (ALT bug #33012), thanks, @zerg

* Mon Dec 12 2016 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt1
- initial build for ALT Linux Sisyphus
