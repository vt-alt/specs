%define rname analitza

%define sover 8
%define libanalitzaplot libanalitzaplot%sover
%define libanalitzagui libanalitzagui%sover
%define libanalitzawidgets libanalitzawidgets%sover
%define libanalitza libanalitza%sover

Name: kde5-%rname
Version: 19.08.0
Release: alt1
%K5init

Group: System/Libraries
Summary: Mathematical features
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Mar 30 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ libEGL-devel libGL-devel libqt5-core libqt5-gui libqt5-network libqt5-opengl libqt5-qml libqt5-quick libqt5-svg libqt5-test libqt5-widgets libqt5-xml libstdc++-devel python-base python-modules python3 qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: eigen3 extra-cmake-modules libGLU-devel python-module-google python3-base qt5-declarative-devel qt5-svg-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: eigen3 extra-cmake-modules libGLU-devel qt5-declarative-devel qt5-svg-devel qt5-tools-devel
BuildRequires: kf5-ki18n-devel

%description
The analitza library will let you add mathematical features to your program.

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

%package -n %libanalitzaplot
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libanalitzaplot
KF5 library

%package -n %libanalitzagui
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libanalitzagui
KF5 library

%package -n %libanalitzawidgets
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libanalitzawidgets
KF5 library

%package -n %libanalitza
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libanalitza
KF5 library

%prep
%setup -n %rname-%version

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%K5install_move data libanalitza
%find_lang %name --with-kde --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
%doc COPYING*

%files devel
#%_K5inc/analitza_version.h
%_K5inc/Analitza5/
%_K5link/lib*.so
%_K5lib/cmake/Analitza5
#%_K5archdata/mkspecs/modules/qt_Analitza.pri

%files -n %libanalitzaplot
%_K5lib/libAnalitzaPlot.so.%sover
%_K5lib/libAnalitzaPlot.so.*
%_K5qml/org/kde/analitza/
%_K5data/libanalitza/
%files -n %libanalitzagui
%_K5lib/libAnalitzaGui.so.%sover
%_K5lib/libAnalitzaGui.so.*
%files -n %libanalitzawidgets
%_K5lib/libAnalitzaWidgets.so.%sover
%_K5lib/libAnalitzaWidgets.so.*
%files -n %libanalitza
%_K5lib/libAnalitza.so.%sover
%_K5lib/libAnalitza.so.*

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

* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Sep 22 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
