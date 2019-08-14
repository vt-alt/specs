%define rname ktp-auth-handler

Name: kde5-%rname
Version: 19.04.3
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Provide UI/KWallet Telepathy Integration
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: qca-qt5-ossl
Requires: signon-plugin-oauth2

Source: %rname-%version.tar
Patch1: alt-oauth2-only-google.patch

# Automatically added by buildreq on Wed Jun 17 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libaccounts-glib libaccounts-qt51 libdbusmenu-qt52 libgpg-error libjson-c libqca-qt5 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libsignon-qt51 libstdc++-devel libtelepathy-logger-qt5 libtelepathy-qt5 libtelepathy-qt5-devel libxcbutil-keysyms python-base python-module-google python3 python3-base qt5-base-devel telepathy-logger-qt5-devel
#BuildRequires: accounts-qt5-devel extra-cmake-modules gcc-c++ kde5-kaccounts-integration-devel kde5-ktp-common-internals-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libdb4-devel libqca-qt5-devel libtelepathy-qt5-devel rpm-build-python3 ruby ruby-stdlibs signon-devel
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: accounts-qt5-devel libqca-qt5-devel telepathy-qt5-devel signon-devel
BuildRequires: kde5-kaccounts-integration-devel kde5-ktp-common-internals-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel
BuildRequires: kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel

%description
Provide UI/KWallet Integration For Passwords and SSL Errors on Account Connect

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

%package -n libkf5tp-auth-handler
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5tp-auth-handler
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build \
    -DLIBEXEC_INSTALL_DIR=%_K5exec \
    #

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5exec/ktp-auth-handler
%_K5dbus_srv/org.freedesktop.Telepathy.Client.*.service
%_datadir/telepathy/clients/KTp.*.client

#%files devel
#%_K5inc/ktp-auth-handler_version.h
#%_K5inc/ktp-auth-handler/
#%_K5link/lib*.so
#%_K5lib/cmake/ktp-auth-handler
#%_K5archdata/mkspecs/modules/qt_ktp-auth-handler.pri

#%files -n libkf5tp-auth-handler
#%_K5lib/libktp-auth-handler.so.*

%changelog
* Tue Aug 13 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Wed Jun 19 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt2
- new version

* Tue May 07 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Thu Mar 21 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Tue Feb 26 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Wed Jul 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Tue Oct 10 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt2%ubt
- fix build requires

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Mon Jul 10 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt2%ubt
- use oauth2 only with google

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Tue Jun 06 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Tue Apr 04 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Wed Sep 21 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Fri Jul 15 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Tue Mar 22 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Mon Feb 29 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Thu Jan 21 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Tue Dec 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Fri Nov 06 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt2
- fix LIBEXEC_INSTALL_DIR

* Thu Nov 05 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Tue Sep 08 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Thu Jul 09 2015 Sergey V Turchin <zerg@altlinux.org> 15.04.3-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.2-alt0.1
- initial build
