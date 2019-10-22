

%define rname qimageblitz
%define sover 5
%define libqimageblitz libqimageblitz%sover

Name: qimageblitz5
Version: 5.0.0
Release: alt0.2

Summary: Graphical effect and filter library for KDE
License: BSD
Group: System/Libraries
Url: http://www.kde.org/
Packager: Sergey V Turchin <zerg@altlinux.org>

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Apr 17 2019 (-bi)
# optimized out: cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libGL-devel libqt4-devel libqt5-core libqt5-gui libqt5-widgets libsasl2-3 libssl-devel libstdc++-devel pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 sh4
#BuildRequires: cmake python3-dev qt5-wayland-devel
BuildRequires(pre): qt5-base-devel
BuildRequires: cmake kde-common-devel

%description 
Blitz is a graphical effect and filter library for KDE that contains
many improvements over KDE 3.x's kdefx library including bugfixes,
memory and speed improvements, and MMX/SSE support.


%package -n %libqimageblitz
Summary: Graphical effect and filter library for KDE
Group: System/Libraries
%description -n %libqimageblitz
Blitz is a graphical effect and filter library for KDE that contains
many improvements over KDE 3.x's kdefx library including bugfixes,
memory and speed improvements, and MMX/SSE support.

%package devel
Summary: %name development library and headers
Group: Development/C++
Conflicts: libqimageblitz-devel
%description devel
Blitz is a graphical effect and filter library for KDE that contains
many improvements over KDE 3.x's kdefx library including bugfixes,
memory and speed improvements, and MMX/SSE support.

This package contains %name development library and headers.


%prep
%setup -qn %rname-%version

# don't build test
sed -i '/add_subdirectory.*test/d' CMakeLists.txt
sed -i 's| -ansi ||' CMakeLists.txt
# fix requires
sed -i '/^Requires:[[:space:]]*QtGui$/s|QtGui|Qt5Gui|' blitz/qimageblitz.pc.cmake


%build
%Kbuild \
    -DQT4_BUILD=OFF \
    #

%install
%Kinstall



%files -n %libqimageblitz
%_libdir/libqimageblitz.so.*
%_libdir/libqimageblitz.so.%sover

%files devel
%doc README.BLITZ README.PORTING
%_libdir/lib*.so
%_includedir/%rname/
%_pkgconfigdir/*.pc

%changelog
* Tue Oct 22 2019 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt0.2
- fix compile flags

* Wed Apr 17 2019 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt0.1
- build with Qt5

* Thu Sep 11 2014 Sergey V Turchin <zerg@altlinux.org> 0.0.6-alt4
- Added a patch from FC to fix "executable-stack" rpmlint warning

* Wed Sep 28 2011 Dmitry V. Levin <ldv@altlinux.org> 0.0.6-alt3
- Fixed interpackage dependencies.
- Rebuilt for debuginfo.

* Mon Dec 06 2010 Sergey V Turchin <zerg@altlinux.org> 0.0.6-alt2
- rebuilt

* Tue Apr 20 2010 Sergey V Turchin <zerg@altlinux.org> 0.0.6-alt0.M51.1
- build for M51

* Wed Apr 07 2010 Sergey V Turchin <zerg@altlinux.org> 0.0.6-alt1
- buildsystem updated

* Wed Jul 22 2009 Sergey V Turchin <zerg@altlinux.org> 0.0.4-alt3
- update from svn r1000977

* Sun Jan 13 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.0.4-alt2
- use optflags
- add watch file

* Sat Jan 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.0.4-alt1
- initial build
