%def_disable zeitgeist

Name: qt5-phonon
Version: 4.10.3
Release: alt2

Group: Graphical desktop/KDE
Summary: KDE5 Multimedia Framework
Url: http://phonon.kde.org/
License: LGPLv2+

#Source: ftp://ftp.kde.org/pub/kde/stable/%name/%version/%name-%version.tar.bz2
Source: phonon4qt5-%version.tar
# FC

# ALT
Patch100: alt-no-rpath.patch
Patch101: alt-fix-install.patch
Patch102: alt-fix-qt-visibility-test.patch

BuildRequires(pre): qt5-base-devel
BuildRequires: qt5-tools-devel qt5-declarative-devel
BuildRequires: libEGL-devel libGL-devel
BuildRequires: cmake extra-cmake-modules
BuildRequires: libalsa-devel libpulseaudio-devel
BuildRequires: rpm-build-kf5
%if_enabled zeitgeist
BuildRequires: libqzeitgeist-devel
%endif

%description
Phonon is the KDE5 Multimedia Framework

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
%description common
%name common package

%package -n libphonon4qt5experimental
Group: System/Libraries
Summary: Phonon library
Requires: %name-common
%description -n libphonon4qt5experimental
Phonon library.

%package -n libphonon4qt5
Group: System/Libraries
Summary: Phonon library
Requires: %name-common
%description -n libphonon4qt5
Phonon library.

%package devel
Group: Development/KDE and QT
Summary: Header files and documentation for compiling Phonon applications
Requires: %name-common
%description devel
This package includes the header files you will need to compile applications
with Phonon.


%prep
%setup -qn phonon4qt5-%version
%patch100 -p1
%patch101 -p1
%patch102 -p1


%build
%add_optflags %optflags_shared -UPIE -U__PIE__
#%add_optflags %optflags_shared
%K5cmake \
    -DPHONON_BUILD_PHONON4QT5:BOOL=ON \
    -DSHARE_INSTALL_PREFIX:PATH=%_datadir \
    -DLOCALE_INSTALL_DIR:PATH=%_K5i18n \
    -DPLUGIN_INSTALL_DIR:PATH=%_qt5_archdatadir \
    -DINCLUDE_INSTALL_DIR:PATH=%_includedir/phonon4qt5 \
    -DPHONON_INSTALL_QT_COMPAT_HEADERS:BOOL=ON \
    -DPHONON_INSTALL_QT_EXTENSIONS_INTO_SYSTEM_QT:BOOL=ON \
    #
%K5make

%install
%K5install

ls -1 %buildroot/%_K5link/lib*.so 2>/dev/null |
while read p
do
    [ -L "$p" ] || continue
    f=`basename $(readlink "$p")`
    l=`basename "$p"`
    ln -sf "$f" "%buildroot/%_libdir/$l"
    rm -f "$p"
done
mkdir -p %buildroot/%_datadir/dbus-1/interfaces/
mv %buildroot/%_K5dbus_iface/* %buildroot/%_datadir/dbus-1/interfaces/

mkdir -p %buildroot/%_qt5_plugindir/phonon4qt5_backend

%K5find_qtlang libphonon_qt

%files common -f libphonon_qt.lang

%files -n libphonon4qt5experimental
%_libdir/libphonon4qt5experimental.so.*

%files -n libphonon4qt5
%dir %_qt5_plugindir/phonon4qt5_backend/
%_libdir/libphonon4qt5.so.*

%files devel
%_includedir/phonon4qt5
#%_includedir/KDE
%_libdir/libphonon4qt5.so
%_libdir/libphonon4qt5experimental.so
%dir %_datadir/phonon4qt5/
%_datadir/phonon4qt5/buildsystem/
%_libdir/cmake/phonon4qt5/
%_qt5_plugindir/designer/phononwidgets.so
%_qt5_archdatadir/mkspecs/modules/qt_phonon4qt5.pri
%_pkgconfigdir/phonon4qt5.pc
%_datadir/dbus-1/interfaces/org.kde.Phonon4Qt5.AudioOutput.xml

%changelog
* Wed Aug 28 2019 Sergey V Turchin <zerg@altlinux.org> 4.10.3-alt2
- fix build requires

* Mon Jul 22 2019 Sergey V Turchin <zerg@altlinux.org> 4.10.3-alt1
- new version

* Mon Jun 17 2019 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt1
- new version

* Fri Apr 27 2018 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt1
- new version

* Wed Apr 05 2017 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Mon Nov 28 2016 Sergey V Turchin <zerg@altlinux.org> 4.9.0-alt0.M80P.1
- build for M80P

* Mon Nov 14 2016 Sergey V Turchin <zerg@altlinux.org> 4.9.0-alt1
- new version

* Mon Apr 18 2016 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt4
- fix conflict with phonon debuginfo (ALT#31977)

* Mon Apr 04 2016 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt3
- fix to build with new Qt

* Thu Jul 02 2015 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt2
- rebuild with gcc5

* Fri Dec 19 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Tue Dec 02 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Tue Oct 21 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Mon Sep 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt3
- fix cmake configs

* Fri Sep 12 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- fix install paths

* Fri Sep 12 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Aug 28 2014 Sergey V Turchin <zerg@altlinux.org> 4.7.80-alt0.M70P.1
- build for M70P

* Mon Aug 25 2014 Sergey V Turchin <zerg@altlinux.org> 4.7.80-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- initial build
