%define rname kdeedu-data

Name: kde5-%rname
Version: 19.08.0
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: Common KDE EDU data
Url: http://www.kde.org
License: GPLv2+

Requires: kf5-filesystem

BuildArch: noarch

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5 rpm-build-ubt

# Automatically added by buildreq on Fri Mar 18 2016 (-bi)
# optimized out: cmake cmake-modules gcc-c++ gtk-update-icon-cache libqt5-core libstdc++-devel python-base python3 python3-base rpm-build-python3
BuildRequires: extra-cmake-modules qt5-base-devel kf5-ki18n-devel

%description
%summary

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data apps

%files
%doc COPYING*
%_K5data/apps/kvtml/
%_K5icon/*/*/actions/*.*

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

* Sat Mar 19 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt2
- make package noarch

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
