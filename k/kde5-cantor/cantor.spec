%define rname cantor

%def_enable python2
%def_enable python3
%def_disable luajit

%define cantor_sover 23
%define libcantorlibs libcantorlibs%cantor_sover
%define cantor_pythonbackend_sover 0
%define libcantor_pythonbackend libcantor_pythonbackend%cantor_pythonbackend_sover
%define cantor_config_sover 0
%define libcantor_config libcantor_config%cantor_config_sover

Name: kde5-%rname
Version: 19.08.0
Release: alt1
%K5init

Group: Education
Summary: KDE Frontend to Mathematical Software
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: kde5-kalgebra

Source: %rname-%version.tar
Patch1: alt-lib-so-ver.patch
Patch2: alt-find-luajit.patch

# Automatically added by buildreq on Wed Mar 30 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ gtk-update-icon-cache kf5-attica-devel kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-script libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libqt5-xmlpatterns libstdc++-devel libxcbutil-keysyms pkg-config python-base python-devel python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: extra-cmake-modules kde5-analitza-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-kparts-devel kf5-kpty-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libcln-devel liblua5-devel libluajit-devel libspectre-devel python-module-google python3-dev qt5-svg-devel qt5-xmlpatterns-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-svg-devel qt5-xmlpatterns-devel
BuildRequires: libcln-devel libspectre-devel libdiscount-devel
%{?_enable_python2:BuildRequires: python-devel}
%{?_enable_python3:BuildRequires: python3-devel}
%{?_enable_luajit:BuildRequires: liblua5-devel libluajit-devel}
BuildRequires: kde5-analitza-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools-devel-static
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-knewstuff-devel kf5-kparts-devel kf5-kpty-devel kf5-kservice-devel kf5-ktexteditor-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel
BuildRequires: kf5-syntax-highlighting-devel

%description
Cantor is a front-end to powerful mathematics and statistics packages.
Cantor integrates them into the KDE Platform and provides a nice, worksheet-based, graphical user interface.
It supports environments for KAlgebra, Lua, Maxima, R, Sage, Octave, Python, Scilab, and Qalculate!

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libcantorlibs
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libcantorlibs
KF5 library

%package -n %libcantor_pythonbackend
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libcantor_pythonbackend
KF5 library

%package -n %libcantor_config
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libcantor_config
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

#LUA_BASE_VER=`echo "%{get_version libluajit-devel}" | sed -E 's|^([[:digit:]]+\.[[:digit:]]).*|\1|'`
#pushd src/backends/lua
#for f in *.{h,cpp} ; do
#    sed -i "s|luajit-2.0/lua.hpp|luajit-${LUA_BASE_VER}/lua.hpp|" $f
#done
#popd

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%K5install_move data cantor
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files
%config(noreplace) %_K5xdgconf/cantor.knsrc
%config(noreplace) %_K5xdgconf/cantor_*.knsrc
%_K5bin/cantor*
%_K5plug/libcantorpart.so
%_K5plug/cantor/
%_K5data/cantor/
%_K5cfg/*.kcfg
%_K5xdgapp/org.kde.cantor.desktop
%_K5icon/*/*/apps/*.*
%_K5xmlgui/cantor/

%files devel
#%_K5inc/cantor_version.h
%_K5inc/cantor/
%_K5link/lib*.so
%_libdir/cmake/Cantor/
#%_K5archdata/mkspecs/modules/qt_Cantor.pri

%files -n %libcantorlibs
%_K5lib/libcantorlibs.so.%cantor_sover
%_K5lib/libcantorlibs.so.*
%files -n %libcantor_pythonbackend
%_K5lib/libcantor_pythonbackend.so.%cantor_pythonbackend_sover
%_K5lib/libcantor_pythonbackend.so.*
%files -n %libcantor_config
%_K5lib/libcantor_config.so.%cantor_config_sover
%_K5lib/libcantor_config.so.*

%changelog
* Thu Aug 29 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Fri Jul 19 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Wed May 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Thu Mar 21 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Thu Feb 28 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Thu Jul 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 17.12.3-alt1%ubt.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Wed Jun 07 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version
- don't build lua backend

* Thu Apr 13 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt2%ubt
- fix to build with luajit-2.0

* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Sep 22 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Sun Apr 03 2016 Ivan Zakharyaschev <imz@altlinux.org> 15.12.2-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
