%define rname okteta

%define okteta3core_sover 0
%define libokteta3core libokteta3core%okteta3core_sover
%define okteta3gui_sover 0
%define libokteta3gui libokteta3gui%okteta3gui_sover
%define kasten4controllers_sover 0
%define libkasten4controllers libkasten4controllers%kasten4controllers_sover
%define kasten4okteta2controllers_sover 0
%define libkasten4okteta2controllers libkasten4okteta2controllers%kasten4okteta2controllers_sover
%define kasten4okteta2gui_sover 0
%define libkasten4okteta2gui libkasten4okteta2gui%kasten4okteta2gui_sover
%define kasten4okteta2core_sover 0
%define libkasten4okteta2core libkasten4okteta2core%kasten4okteta2core_sover
%define kasten4core_sover 0
%define libkasten4core libkasten4core%kasten4core_sover
%define kasten4gui_sover 0
%define libkasten4gui libkasten4gui%kasten4gui_sover


Name: kde5-%rname
Version: 0.26.1
Release: alt1
Epoch: 1
%K5init altplace

Group: Development/Tools
Summary: Viewing and editing of data on the byte level
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: %rname-alt-castxml-compat.patch

# Remove 'gccxml' from 'Requires'
%define __find_provides sh -c '/usr/lib/rpm/find-provides | sort | uniq'
%define __find_requires sh -c '/usr/lib/rpm/find-requires | sort | uniq | sed "/^gccxml$/d"'

# Automatically added by buildreq on Thu Oct 01 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqca-qt5 libqt5-core libqt5-dbus libqt5-designer libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base python3 python3-base qt5-base-devel qt5-script-devel rpm-build-gir ruby ruby-stdlibs shared-mime-info xml-common xml-utils
#BuildRequires: extra-cmake-modules gccxml kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libqca-qt5-devel python-module-google qt5-quick1-devel qt5-tools-devel rpm-build-python3 rpm-build-ruby xsltproc
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel qt5-declarative-devel qt5-tools-devel qt5-script-devel
BuildRequires: libqca-qt5-devel xsltproc
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel
BuildRequires: kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel
BuildRequires: kf5-solid-devel kf5-sonnet-devel kf5-kcrash-devel

%description
%summary.

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

%package -n %libokteta3core
Group: System/Libraries
Summary: KF5 library
Requires: %name-common
%description -n %libokteta3core
KF5 library

%package -n %libokteta3gui
Group: System/Libraries
Summary: KF5 library
Requires: %name-common
%description -n %libokteta3gui
KF5 library

%package -n %libkasten4controllers
Group: System/Libraries
Summary: KF5 library
Requires: %name-common
%description -n %libkasten4controllers
KF5 library

%package -n %libkasten4okteta2controllers
Group: System/Libraries
Summary: KF5 library
Requires: %name-common
%description -n %libkasten4okteta2controllers
KF5 library

%package -n %libkasten4okteta2gui
Group: System/Libraries
Summary: KF5 library
Requires: %name-common
%description -n %libkasten4okteta2gui
KF5 library

%package -n %libkasten4okteta2core
Group: System/Libraries
Summary: KF5 library
Requires: %name-common
%description -n %libkasten4okteta2core
KF5 library

%package -n %libkasten4core
Group: System/Libraries
Summary: KF5 library
Requires: %name-common
%description -n %libkasten4core
KF5 library

%package -n %libkasten4gui
Group: System/Libraries
Summary: KF5 library
Requires: %name-common
%description -n %libkasten4gui
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build \
    -DINCLUDE_INSTALL_DIR=%_K5inc \
    #

%install
%K5install
%K5install_move data okteta
%find_lang %name --with-kde --all-name
mv %buildroot/%_K5xdgmime/okteta{,5}.xml

%files common -f %name.lang
%doc COPYING*

%files
%config(noreplace) %_K5xdgconf/*.knsrc
%_K5bin/*
%_K5plug/kf5/parts/*.so
%_K5plug/designer/*.so
%_K5data/okteta/
#%_K5xmlgui/*/
%_K5xdgmime/*.xml
%_K5xdgapp/*.desktop
%_K5icon/*/*/apps/*.*
%_K5cfg/*.kcfg
%_K5srv/*.desktop

%files devel
#%_K5inc/okteta_version.h
%_K5inc/*/
%_K5link/lib*.so
%_K5lib/cmake/*/
%_pkgconfigdir/Okteta*.pc
%_K5archdata/mkspecs/modules/qt_Okteta*.pri

%files -n %libokteta3core
%_K5lib/libOkteta3Core.so.%okteta3core_sover
%_K5lib/libOkteta3Core.so.*
%files -n %libokteta3gui
%_K5lib/libOkteta3Gui.so.%okteta3gui_sover
%_K5lib/libOkteta3Gui.so.*
%files -n %libkasten4controllers
%_K5lib/libKasten4Controllers.so.%kasten4controllers_sover
%_K5lib/libKasten4Controllers.so.*
%files -n %libkasten4okteta2controllers
%_K5lib/libKasten4Okteta2Controllers.so.%kasten4okteta2controllers_sover
%_K5lib/libKasten4Okteta2Controllers.so.*
%files -n %libkasten4okteta2gui
%_K5lib/libKasten4Okteta2Gui.so.%kasten4okteta2gui_sover
%_K5lib/libKasten4Okteta2Gui.so.*
%files -n %libkasten4okteta2core
%_K5lib/libKasten4Okteta2Core.so.%kasten4okteta2core_sover
%_K5lib/libKasten4Okteta2Core.so.*
%files -n %libkasten4core
%_K5lib/libKasten4Core.so.%kasten4core_sover
%_K5lib/libKasten4Core.so.*
%files -n %libkasten4gui
%_K5lib/libKasten4Gui.so.%kasten4gui_sover
%_K5lib/libKasten4Gui.so.*


%changelog
* Mon Jun 17 2019 Sergey V Turchin <zerg@altlinux.org> 1:0.26.1-alt1
- new version

* Mon Mar 12 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1
- new version

* Mon Sep 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 17.04.3-alt2
- Patched struct2osd script to work with castxml.

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1
- new version

* Fri Jun 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1
- new version

* Thu May 04 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1
- new version

* Tue Apr 04 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1
- new version

* Mon Dec 05 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Thu Jul 14 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Fri Feb 26 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Tue Dec 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Wed Sep 30 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- initial build
