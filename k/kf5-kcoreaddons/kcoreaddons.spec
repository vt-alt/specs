%define rname kcoreaddons
%def_disable python
%if_enabled python
%define sipver2 %(rpm -q --qf '%%{VERSION}' python-module-sip)
%define sipver3 %(rpm -q --qf '%%{VERSION}' python3-module-sip)
%endif

Name: kf5-%rname
Version: 5.63.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 Tier 1 addon with various classes on top of QtCore
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: alt-simplify-kde4home.patch

# Automatically added by buildreq on Thu Dec 25 2014 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libqt5-core libqt5-gui libqt5-test libqt5-widgets libqt5-xml libstdc++-devel python-base qt5-base-devel qt5-tools ruby ruby-stdlibs shared-mime-info
#BuildRequires: extra-cmake-modules gcc-c++ python-module-google qt5-tools-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
%if_enabled python
BuildRequires(pre): python3-module-sip-devel python-module-sip-devel
BuildRequires: python-module-PyQt5-devel
%endif
BuildRequires: gcc-c++ extra-cmake-modules qt5-base-devel qt5-tools-devel
BuildRequires: shared-mime-info

%description
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

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
Requires: qt5-base-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5coreaddons
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5coreaddons
KF5 library

%if_enabled python
%package -n python-module-pykf5
Summary: common package for KF5 python bindings
License: GPLv2+ / LGPLv2+
Group: Development/Python
Requires: %name-common = %version-%release
%description -n python-module-pykf5
common package for KF5 python bindings

%package -n python-module-%rname
Summary: Python bindings for KCoreAddons
License: GPLv2+ / LGPLv2+
Group: Development/Python
Requires: %name-common = %version-%release
Requires: python-module-pykf5
Requires: python-module-sip = %sipver2
%description -n python-module-%rname
Python bindings for KCoreAddons

%package -n python-module-%rname-devel
Summary: Sip files for python-module-%rname
Group: Development/Python
BuildArch: noarch
%description -n python-module-%rname-devel
Sip files for python-module-%rname

%package -n python3-module-pykf5
Summary: common package for KF5 python3 bindings
License: GPLv2+ / LGPLv2+
Group: Development/Python3
Requires: %name-common = %version-%release
%description -n python3-module-pykf5
common package for KF5 python3 bindings

%package -n python3-module-%rname
Summary: Python3 bindings for KCoreAddons
License: GPLv2+ / LGPLv2+
Group: Development/Python3
Requires: %name-common = %version-%release
Requires: python3-module-sip = %sipver3
%description -n python3-module-%rname
Python3 bindings for KCoreAddons

%package -n python3-module-%rname-devel
Summary: Sip files for python3-module-%rname
Group: Development/Python3
BuildArch: noarch
%description -n python3-module-%rname-devel
Sip files for python3-module-%rname
%endif

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build \
    -DKDE4_DEFAULT_HOME=".kde4" \
    -D_KDE4_DEFAULT_HOME_POSTFIX=4 \
    #

%install
%K5install
%find_lang %name --all-name
%K5find_qtlang %name --all-name


%files common -f %name.lang
%doc COPYING.LIB README.md
%_datadir/qlogging-categories5/*.*categories
%_xdgmimedir/packages/kde5.xml
%_K5data/licenses/

%files devel
%_K5bin/desktoptojson
%_K5inc/kcoreaddons_version.h
%_K5inc/KCoreAddons/
%_K5link/lib*.so
%_K5lib/cmake/KF5CoreAddons
%_K5archdata/mkspecs/modules/qt_KCoreAddons.pri

%files -n libkf5coreaddons
%_K5lib/libKF5CoreAddons.so.*

%if_enabled python
%files -n python-module-pykf5
%dir %python_sitelibdir/PyKF5/
%python_sitelibdir/PyKF5/__init__.py*
%dir %_datadir/sip/PyKF5/
%files -n python-module-%rname
%python_sitelibdir/PyKF5/*.so
%files -n python-module-%rname-devel
%_datadir/sip/PyKF5/KCoreAddons/
%files -n python3-module-pykf5
%dir %python3_sitelibdir/PyKF5/
%python3_sitelibdir/PyKF5/__init__.py
%python3_sitelibdir/PyKF5/__pycache__/
%dir %_datadir/sip3/PyKF5/
%files -n python3-module-%rname
%python3_sitelibdir/PyKF5/*.so
%files -n python3-module-%rname-devel
%_datadir/sip3/PyKF5/KCoreAddons/
%endif

%changelog
* Tue Oct 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.63.0-alt1
- new version

* Mon Sep 16 2019 Sergey V Turchin <zerg@altlinux.org> 5.62.0-alt1
- new version

* Mon Aug 12 2019 Sergey V Turchin <zerg@altlinux.org> 5.61.0-alt1
- new version

* Mon Jul 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.60.0-alt1
- new version

* Tue Jun 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.59.0-alt1
- new version

* Mon Jun 03 2019 Sergey V Turchin <zerg@altlinux.org> 5.58.0-alt1
- new version

* Mon Apr 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.57.0-alt1
- new version

* Fri Mar 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.56.0-alt1
- new version

* Mon Feb 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.55.0-alt1
- new version

* Thu Jan 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.54.0-alt2
- new version

* Tue Jan 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.54.0-alt1
- new version

* Mon Dec 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.53.1-alt1
- new version

* Tue Dec 11 2018 Sergey V Turchin <zerg@altlinux.org> 5.53.0-alt1
- new version

* Mon Nov 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.52.0-alt1
- new version

* Wed Oct 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.51.0-alt1
- new version

* Mon Sep 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.50.0-alt1%ubt
- new version

* Tue Aug 21 2018 Sergey V Turchin <zerg@altlinux.org> 5.49.0-alt1%ubt
- new version

* Thu Jul 19 2018 Sergey V Turchin <zerg@altlinux.org> 5.48.0-alt1%ubt
- new version

* Fri Jul 13 2018 Oleg Solovyov <mcpain@altlinux.org> 5.47.0-alt2%ubt
- cleanup


* Fri Jul 13 2018 Oleg Solovyov <mcpain@altlinux.org> 5.47.0-alt2%ubt

- cleanup

* Fri Jun 15 2018 Sergey V Turchin <zerg@altlinux.org> 5.47.0-alt1%ubt
- new version

* Mon May 14 2018 Sergey V Turchin <zerg@altlinux.org> 5.46.0-alt1%ubt
- new version

* Fri May 04 2018 Sergey V Turchin <zerg@altlinux.org> 5.45.0-alt1%ubt
- new version

* Thu Apr 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.44.0-alt1%ubt.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Mar 20 2018 Sergey V Turchin <zerg@altlinux.org> 5.44.0-alt1%ubt
- new version

* Mon Mar 05 2018 Oleg Solovyov <mcpain@altlinux.org> 5.42.0-alt2%ubt
- build python bindings

* Thu Jan 18 2018 Sergey V Turchin <zerg@altlinux.org> 5.42.0-alt1%ubt
- new version

* Tue Dec 12 2017 Sergey V Turchin <zerg@altlinux.org> 5.41.0-alt1%ubt
- new version

* Tue Nov 21 2017 Sergey V Turchin <zerg@altlinux.org> 5.40.0-alt1%ubt
- new version

* Tue Oct 24 2017 Sergey V Turchin <zerg@altlinux.org> 5.39.0-alt1%ubt
- new version

* Tue Sep 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.38.0-alt1%ubt
- new version

* Wed Aug 16 2017 Sergey V Turchin <zerg@altlinux.org> 5.37.0-alt1%ubt
- new version

* Mon Jul 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.36.0-alt1%ubt
- new version

* Thu Jun 29 2017 Sergey V Turchin <zerg@altlinux.org> 5.35.0-alt1%ubt
- new version

* Fri May 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.34.0-alt1%ubt
- new version

* Mon Apr 17 2017 Sergey V Turchin <zerg@altlinux.org> 5.33.0-alt1%ubt
- new version

* Wed Mar 29 2017 Sergey V Turchin <zerg@altlinux.org> 5.32.0-alt1%ubt
- new version

* Mon Feb 13 2017 Sergey V Turchin <zerg@altlinux.org> 5.31.0-alt1%ubt
- new version

* Wed Feb 08 2017 Sergey V Turchin <zerg@altlinux.org> 5.30.0-alt1%ubt
- new version

* Tue Dec 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.29.0-alt1%ubt
- new version

* Fri Nov 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.28.0-alt0.M80P.1
- build for M80P

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.28.0-alt1
- new version

* Thu Oct 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.27.0-alt0.M80P.1
- build for M80P

* Tue Oct 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.27.0-alt1
- new version

* Mon Sep 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.26.0-alt1
- new version

* Thu Aug 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.25.0-alt2
- don't try ~/.kde as kde4 home dir

* Mon Aug 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.25.0-alt1
- new version

* Mon Jul 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.24.0-alt1
- new version

* Tue Jun 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.23.0-alt1
- new version

* Fri May 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.22.0-alt1
- new version

* Mon Apr 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.21.0-alt1
- new version

* Tue Mar 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.20.0-alt1
- new version

* Tue Feb 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.19.0-alt1
- new version

* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.18.0-alt1
- new version

* Fri Dec 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Wed Nov 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.16.0-alt1
- new version

* Mon Oct 12 2015 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Mon Sep 14 2015 Sergey V Turchin <zerg@altlinux.org> 5.14.0-alt1
- new version

* Wed Aug 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.13.0-alt1
- new version

* Fri Jul 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1
- new version

* Tue Jun 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.11.0-alt1
- new version

* Mon May 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.10.0-alt1
- new version

* Fri Apr 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt1
- new version

* Mon Apr 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Wed Mar 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt0.1
- test

* Mon Feb 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt0.1
- test

* Fri Jan 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt0.1
- test

* Mon Dec 22 2014 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- initial build
