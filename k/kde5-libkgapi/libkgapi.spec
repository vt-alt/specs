%define rname libkgapi

%define sover 5
%define libkpimgapidrive libkpimgapidrive%sover
%define libkpimgapilatitude libkpimgapilatitude%sover
%define libkpimgapicore libkpimgapicore%sover
%define libkpimgapicalendar libkpimgapicalendar%sover
%define libkpimgapiblogger libkpimgapiblogger%sover
%define libkpimgapimaps libkpimgapimaps%sover
%define libkpimgapicontacts libkpimgapicontacts%sover
%define libkpimgapitasks libkpimgapitasks%sover

Name: kde5-%rname
Version: 19.08.1
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Google services APIs
Url: http://www.kde.org
License: GPLv2+

Provides: kf5-libkgapi = %EVR
Obsoletes: kf5-libkgapi < %EVR

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Sep 01 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libgst-plugins1.0 libical-devel libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-sensors libqt5-sql libqt5-svg libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules kde5-kcalcore-devel kde5-kcontacts-devel kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel python-module-google python3-dev qt5-webkit-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-webengine-devel qt5-tools-devel
BuildRequires: libsasl2-devel
BuildRequires: kde5-kcalcore-devel kde5-kcontacts-devel
BuildRequires: kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel kf5-kwallet-devel

%description
LibKGAPI is a C++ library that implements APIs for various Google services.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Provides: kf5-libkgapi-common = %EVR
Obsoletes: kf5-libkgapi-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: kf5-kcoreaddons-devel kde5-kcalcore-devel kde5-kcontacts-devel
Provides: kf5-libkgapi-devel = %EVR
Obsoletes: kf5-libkgapi-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkpimgapilatitude
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkpimgapilatitude
KF5 library

%package -n %libkpimgapidrive
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkpimgapidrive
KF5 library

%package -n %libkpimgapicore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkpimgapicore
KF5 library

%package -n %libkpimgapicalendar
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkpimgapicalendar
KF5 library

%package -n %libkpimgapiblogger
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkpimgapiblogger
KF5 library

%package -n %libkpimgapimaps
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkpimgapimaps
KF5 library

%package -n %libkpimgapicontacts
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkpimgapicontacts
KF5 library

%package -n %libkpimgapitasks
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkpimgapitasks
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install

# workaround against sasl plugins dir
for sffx in 3 4 5 6 ; do
    mkdir -p  %buildroot/%_libdir/sasl2-$sffx
    for f in %buildroot/%_libdir/sasl2/*.so* ; do
	fname=`basename "$f"`
	ln -s ../sasl2/"$fname" %buildroot/%_libdir/sasl2-$sffx/"$fname"
    done
done

%find_lang %name --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSE*
#%config(noreplace) %_K5xdgconf/*.*categories
%_datadir/qlogging-categories5/*.*categories

%files devel
%_K5inc/KPim/kgapi_version.h
%_K5inc/KPim/KGAPI/
%_K5link/lib*.so
%_K5lib/cmake/KPimGAPI/
#%_K5lib/cmake/KF5GAPI/
%_K5archdata/mkspecs/modules/qt_KGAPI*.pri

%files -n %libkpimgapidrive
%_K5lib/libKPimGAPIDrive.so.*
%_libdir/sasl2*/*.so*
%files -n %libkpimgapilatitude
%_K5lib/libKPimGAPILatitude.so.*
%files -n %libkpimgapicore
%_K5lib/libKPimGAPICore.so.*
%files -n %libkpimgapicalendar
%_K5lib/libKPimGAPICalendar.so.*
%files -n %libkpimgapiblogger
%_K5lib/libKPimGAPIBlogger.so.*
%files -n %libkpimgapimaps
%_K5lib/libKPimGAPIMaps.so.*
%files -n %libkpimgapicontacts
%_K5lib/libKPimGAPIContacts.so.*
%files -n %libkpimgapitasks
%_K5lib/libKPimGAPITasks.so.*

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

* Wed Jan 30 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.1-alt1
- new version

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Tue Jun 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Tue May 15 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Feb 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.2-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Mon May 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Mon Apr 24 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Mon Apr 24 2017 Sergey V Turchin <zerg@altlinux.org> 17.03.90-alt1%ubt
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt2%ubt
- rebuild with new kcontacts

* Wed Nov 02 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M80P.1
- build for M80P

* Wed Nov 02 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Thu Sep 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt2
- fix requires

* Thu Sep 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt2
- update from 5.1 branch

* Tue Dec 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt1
- new version

* Fri Aug 21 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt1
- new version

* Wed Aug 12 2015 Sergey V Turchin <zerg@altlinux.org> 4.80.0-alt1
- initial build
