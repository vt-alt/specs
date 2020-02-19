%define rname messagelib

%define sover 5
%define libkf5messagecomposer libkf5messagecomposer%sover
%define libkf5messagecore libkf5messagecore%sover
%define libkf5messageviewer libkf5messageviewer%sover
%define libkf5messagelist libkf5messagelist%sover
%define libkf5messageparser libkf5messageparser%sover
%define libkf5mimetreeparser libkf5mimetreeparser%sover
%define libkf5webengineviewer libkf5webengineviewer%sover

Name: kde5-%rname
Version: 19.12.2
Release: alt1
%K5init

Group: System/Libraries
Summary: KDE5 %rname library
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: alt-gpgme17.patch

# Automatically added by buildreq on Thu Apr 28 2016 (-bi)
# optimized out: boost-devel-headers cmake cmake-modules elfutils gcc-c++ glibc-devel-static kde5-akonadi-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libgpg-error-devel libgst-plugins1.0 libical-devel libjson-c libkf5gpgmepp-pthread libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-sensors libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-tools-devel qt5-webkit-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules grantlee5-devel kde5-akonadi-search-devel kde5-gpgmepp-devel kde5-grantleetheme-devel kde5-kcalcore-devel kde5-kcontacts-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kldap-devel kde5-kmailtransport-devel kde5-kmbox-devel kde5-kmime-devel kde5-kpimtextedit-devel kde5-libgravatar-devel kde5-libkdepim-devel kde5-libkleo-devel kde5-pim-apps-libs-devel kde5-pimcommon-devel kde5-pimlibs-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libgpgme-devel libldap-devel libsasl2-devel python-module-google python3-dev qt5-tools-devel-static rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-tools-devel-static qt5-webengine-devel
BuildRequires: grantlee5-devel libqca-qt5-devel
BuildRequires: libgpgme-devel libassuan-devel libldap-devel libsasl2-devel
BuildRequires: kde5-akonadi-search-devel kde5-grantleetheme-devel kde5-kcalcore-devel kde5-kcontacts-devel
BuildRequires: kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kldap-devel kde5-kmailtransport-devel kde5-kmbox-devel
BuildRequires: kde5-kmime-devel kde5-kpimtextedit-devel kde5-libgravatar-devel kde5-libkdepim-devel kde5-libkleo-devel
BuildRequires: kde5-pim-apps-libs-devel kde5-pimcommon-devel
BuildRequires: boost-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-akonadi-contacts-devel kde5-akonadi-notes-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support-devel
BuildRequires: kf5-kdesignerplugin-devel kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kguiaddons-devel
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel
BuildRequires: kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel
BuildRequires: kf5-solid-devel kf5-sonnet-devel kf5-syntax-highlighting-devel kf5-knewstuff-devel

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

%package -n %libkf5messagecomposer
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5messagecomposer
KF5 library

%package -n %libkf5messagecore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5messagecore
KF5 library

%package -n %libkf5messageviewer
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5messageviewer
KF5 library

%package -n %libkf5messagelist
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5messagelist
KF5 library

%package -n %libkf5messageparser
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5messageparser
KF5 library

%package -n %libkf5mimetreeparser
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5mimetreeparser
KF5 library

%package -n %libkf5webengineviewer
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkf5webengineviewer
KF5 library

%prep
%setup -n %rname-%version
#%patch1 -p1

%build
%K5build \
    -DDATA_INSTALL_DIR=%_K5data \
    -DQGpgme_DIR=%_libdir/cmake/Gpgmepp/ \
    #

%install
%K5install
%K5install_move data libmessageviewer messagelist messageviewer kconf_update
%K5install_move data org.kde.syntax-highlighting knsrcfiles
%find_lang %name --with-kde --all-name

%files common -f %name.lang
#%doc COPYING*
%_datadir/qlogging-categories5/*.*categories
%_K5data/*message*/
%_K5data/org.kde.syntax-highlighting/
%_K5data/knsrcfiles/*message*.knsrc
%_K5cfg/*.kcfg
%_K5conf_up/*message*.upd
%_K5notif/*message*.notifyrc

%files devel
%_K5inc/*er_version.h
%_K5inc/*essage*/
%_K5inc/*emplate*/
%_K5inc/?ime?ree?arser/
%_K5inc/?eb?ngine?iewer/
%_K5link/lib*.so
%_K5lib/cmake/*essage*/
%_K5lib/cmake/*emplate*/
%_K5lib/cmake/KF5MimeTreeParser/
%_K5lib/cmake/KF5WebEngineViewer/
%_K5archdata/mkspecs/modules/qt_*.pri

%files -n %libkf5messagecomposer
%_K5lib/libKF5MessageComposer.so.%sover
%_K5lib/libKF5MessageComposer.so.*
%files -n %libkf5messagecore
%_K5lib/libKF5MessageCore.so.%sover
%_K5lib/libKF5MessageCore.so.*
%files -n %libkf5messageviewer
%_K5lib/libKF5MessageViewer.so.%sover
%_K5lib/libKF5MessageViewer.so.*
%_K5plug/messageviewer/messageviewer_*.so
%_K5plug/messageviewer/grantlee/
%files -n %libkf5messagelist
%_K5lib/libKF5MessageList.so.%sover
%_K5lib/libKF5MessageList.so.*
%files -n %libkf5messageparser
%_K5lib/libKF5TemplateParser.so.%sover
%_K5lib/libKF5TemplateParser.so.*
%files -n %libkf5mimetreeparser
%_K5lib/libKF5MimeTreeParser.so.%sover
%_K5lib/libKF5MimeTreeParser.so.*
%files -n %libkf5webengineviewer
%_K5lib/libKF5WebEngineViewer.so.%sover
%_K5lib/libKF5WebEngineViewer.so.*

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

* Mon Aug 27 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt2%ubt
- update Russian translation

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
