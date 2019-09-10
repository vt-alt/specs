%define rname kitinerary

%define sover 5
%define libkpimitinerary libkpimitinerary%sover

Name: kde5-%rname
Version: 19.08.1
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Itinerary data model
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
# Automatically added by buildreq on Mon Feb 04 2019 (-bi)
# optimized out: cmake cmake-modules elfutils fontconfig gcc-c++ gem-power-assert glibc-kernheaders-generic glibc-kernheaders-x86 libGL-devel libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-test libqt5-xml libsasl2-3 libstdc++-devel pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel rpm-build-python3 rpm-build-ruby ruby ruby-bundler ruby-rake ruby-rdoc ruby-stdlibs sh4 xml-utils zlib-devel
BuildRequires: extra-cmake-modules qt5-base-devel qt5-declarative-devel
BuildRequires: libpoppler-devel libxml2-devel xsltproc zlib-devel
BuildRequires: kde5-kcalcore-devel kde5-kcontacts-devel kde5-kmime-devel kde5-kpkpass-devel
BuildRequires: kf5-karchive-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kcoreaddons-devel kf5-ki18n-devel

%description
A library containing itinerary data model and itinerary extraction code.

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

%package -n %libkpimitinerary
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
Provides: libkpimitinerary = %EVR
Obsoletes: libkpimitinerary < %EVR
%description -n %libkpimitinerary
%name library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%find_lang %name --all-name


%files common -f %name.lang
%doc COPYING.LIB README.md
#%config(noreplace) %_K5xdgconf/*.*categories
%_datadir/qlogging-categories5/*.*categories

%files devel
#%_K5inc/kitinerary_version.h
%_K5inc/KPim/??tinerary/
%_K5link/lib*.so
%_K5lib/cmake/KPimItinerary/
#%_K5archdata/mkspecs/modules/qt_kitinerary.pri

%files -n %libkpimitinerary
%_K5exec/kitinerary*
%_K5lib/libKPimItinerary.so.%sover
%_K5lib/libKPimItinerary.so.*

%changelog
* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Fri Aug 16 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Tue Jul 16 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Fri Jun 07 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Tue Apr 30 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Thu Apr 11 2019 Sergey V Turchin <zerg@altlinux.org> 19.03.90-alt1
- new version

* Fri Mar 15 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Fri Feb 08 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Wed Feb 06 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.1-alt2
- track so version

* Mon Feb 04 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.1-alt1
- initial build
