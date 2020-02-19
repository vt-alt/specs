%define rname libkleo

%define sover 5
%define libkf5libkleo libkf5libkleo%sover

Name: kde5-%rname
Version: 19.12.2
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: KDE5 %rname library
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Apr 28 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ libEGL-devel libGL-devel libgpg-error libgpg-error-devel libkf5gpgmepp-pthread libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: boost-devel-headers extra-cmake-modules kde5-gpgmepp-devel kde5-kpimtextedit-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-sonnet-devel libgpgme-devel python-module-google python3-dev rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: boost-devel extra-cmake-modules
BuildRequires: libgpgme-devel libassuan-devel
BuildRequires: kde5-kpimtextedit-devel
BuildRequires: kf5-kcompletion-devel kf5-kconfig-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel kf5-sonnet-devel kf5-kcodecs-devel kf5-kitemmodels-devel

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

%package -n %libkf5libkleo
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5libkleo
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data libkleopatra
%find_lang %name --with-kde --all-name

%files common -f %name.lang
#%doc COPYING*
%config(noreplace) %_K5xdgconf/*rc
#%config(noreplace) %_K5xdgconf/*.*categories
%_datadir/qlogging-categories5/*.*categories
%_K5data/libkleopatra/

%files devel
%_K5inc/libkleo_version.h
%_K5inc/Libkleo/
%_K5inc/libkleo/
%_K5link/lib*.so
%_K5lib/cmake/KF5Libkleo/
%_K5archdata/mkspecs/modules/qt_Libkleo.pri

%files -n %libkf5libkleo
%_K5lib/libKF5Libkleo.so.%sover
%_K5lib/libKF5Libkleo.so.*

%changelog
* Thu Feb 13 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt1
- new version

* Thu Jan 16 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Fri Nov 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Wed Oct 23 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.2-alt1
- new version

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

* Wed Mar 15 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.2-alt1%ubt
- new version

* Mon Nov 28 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt0.M80P.1
- build for M80P

* Fri Nov 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Fri Aug 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Thu Jun 30 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Wed Apr 27 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.0-alt1
- initial build
