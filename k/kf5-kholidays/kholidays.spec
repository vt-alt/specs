%define rname kholidays

Name: kf5-%rname
Version: 5.66.0
Release: alt1
Epoch: 1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE library for regional holiday information
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Mon May 21 2018 (-bi)
# optimized out: cmake cmake-modules elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libqt5-core libqt5-gui libqt5-network libqt5-qml libqt5-xml libstdc++-devel perl python-base python-modules python3 python3-base qt5-base-devel qt5-tools rpm-build-python3 rpm-build-qml ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules libssl-devel python3-dev qt5-declarative-devel qt5-tools-devel rpm-build-kf5 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-declarative-devel qt5-tools-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Provides: kde5-kholidays-common = 18
Obsoletes: kde5-kholidays-common < 18
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Provides: kde5-kholidays-devel = 18
Obsoletes: kde5-kholidays-devel < 18
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5holidays
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %EVR
%description -n libkf5holidays
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
mkdir -p %buildroot/%_K5data/libkholidays/
%find_lang %name --with-kde --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
#%doc COPYING*
%_K5data/libkholidays/

%files devel
%_K5inc/kholidays_version.h
%_K5inc/KHolidays/
%_K5link/lib*.so
%_K5lib/cmake/KF5Holidays/
%_K5archdata/mkspecs/modules/qt_KHolidays.pri
#%_K5plug/designer/*.so

%files -n libkf5holidays
%_K5lib/libKF5Holidays.so.*
%_K5qml/org/kde/kholidays/

%changelog
* Mon Jan 13 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.66.0-alt1
- new version

* Mon Dec 16 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.65.0-alt1
- new version

* Mon Nov 11 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.64.0-alt1
- new version

* Tue Oct 15 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.63.0-alt1
- new version

* Mon Sep 16 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.62.0-alt1
- new version

* Mon Aug 12 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.61.0-alt1
- new version

* Mon Jul 15 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.60.0-alt1
- new version

* Tue Jun 11 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.59.0-alt1
- new version

* Mon Jun 03 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.58.0-alt1
- new version

* Mon Apr 15 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.57.0-alt1
- new version

* Fri Mar 15 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.56.0-alt1
- new version

* Mon Feb 11 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.55.0-alt1
- new version

* Thu Jan 24 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.54.0-alt2
- new version

* Tue Jan 15 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.54.0-alt1
- new version

* Tue Dec 11 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.53.0-alt1
- new version

* Mon Nov 12 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.52.0-alt1
- new version

* Wed Oct 17 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.51.0-alt1
- new version

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:5.50.0-alt1.qa1%ubt
- NMU: applied repocop patch

* Mon Sep 10 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.50.0-alt1%ubt
- new version

* Tue Aug 21 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.49.0-alt1%ubt
- new version

* Thu Jul 19 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.48.0-alt1%ubt
- new version

* Fri Jun 15 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.47.0-alt1%ubt
- new version

* Mon May 21 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.46.0-alt1%ubt
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

* Mon Jul 10 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt2%ubt
- update to fix Turkish Holiday File

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Mon May 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Mon Apr 24 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Fri Mar 31 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt2%ubt
- fix compile flags

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

* Mon Apr 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.0-alt1
- new version

* Tue Mar 22 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Thu Feb 25 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Tue Jan 19 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Mon Dec 21 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Thu Aug 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Mon Aug 10 2015 Sergey V Turchin <zerg@altlinux.org> 15.7.90-alt1
- initial build
