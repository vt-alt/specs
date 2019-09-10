%define rname kdepim-addons


%define sover 5
%define libkaddressbookmergelibprivate libkaddressbookmergelibprivate%sover
%define libkaddressbookimportexportlibprivate libkaddressbookimportexportlibprivate%sover
%define libshorturlpluginprivate libshorturlpluginprivate%sover
%define libadblocklibprivate libadblocklibprivate%sover
%define libgrammarcommon libgrammarcommon%sover
%define libkmailgrammalecte libkmailgrammalecte%sover
%define libkmaillanguagetool libkmaillanguagetool%sover
%define libkmailmarkdown libkmailmarkdown%sover

Name: kde5-pim-addons
Version: 19.08.1
Release: alt1
%K5init

%add_findreq_skiplist %_K5bin/kmail_*.sh

Group: Graphical desktop/KDE
Summary: PIM addons
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: %name-kaddressbook
Requires: %name-kmail
Requires: %name-korganizer
Requires: %name-plugins

Source: %rname-%version.tar
Patch1: alt-akonadi-plugins-dir.patch

# Automatically added by buildreq on Thu Sep 01 2016 (-bi)
# optimized out: boost-devel-headers cmake cmake-modules elfutils fontconfig gcc-c++ grantlee5-devel kde5-libkleo-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libgpg-error-devel libgpgme-devel libgst-plugins1.0 libical-devel libjson-c libkf5gpgmepp-pthread libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sensors libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webengine libqt5-webenginecore libqt5-webenginewidgets libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-webchannel-devel qt5-webkit-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules kde5-akonadi-calendar-devel kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-akonadi-notes-devel kde5-calendarsupport-devel kde5-eventviews-devel kde5-gpgmepp-devel kde5-grantleetheme-devel kde5-incidenceeditor-devel kde5-kcalcore-devel kde5-kcalutils-devel kde5-kcontacts-devel kde5-kdgantt2-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kmailtransport-devel kde5-kmime-devel kde5-kpimtextedit-devel kde5-ktnef-devel kde5-libgravatar-devel kde5-libkdepim-devel kde5-mailcommon-devel kde5-messagelib-devel kde5-pim-apps-libs-devel kde5-pimcommon-devel kf5-kdeclarative-devel kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel kf5-kpackage-devel kf5-kwallet-devel kf5-libkgapi-devel libsasl2-devel python-module-google python3-dev qt5-webengine-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-webengine-devel
BuildRequires: libpoppler-qt5-devel libdiscount-devel
BuildRequires: libsasl2-devel libgpgme-devel libassuan-devel
BuildRequires: kde5-libkgapi-devel
BuildRequires: kde5-akonadi-calendar-devel kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-akonadi-notes-devel
BuildRequires: kde5-calendarsupport-devel kde5-eventviews-devel kde5-grantleetheme-devel kde5-incidenceeditor-devel kde5-libksieve-devel
BuildRequires: kde5-kcalcore-devel kde5-kcalutils-devel kde5-kcontacts-devel kde5-kidentitymanagement-devel
BuildRequires: kde5-kimap-devel kde5-kmailtransport-devel kde5-kmime-devel kde5-kpimtextedit-devel kde5-ktnef-devel kde5-libgravatar-devel
BuildRequires: kde5-libkdepim-devel kde5-mailcommon-devel kde5-messagelib-devel kde5-pim-apps-libs-devel kde5-pimcommon-devel
BuildRequires: kde5-mailimporter-devel kde5-akonadi-import-wizard-devel kde5-kontactinterface-devel
BuildRequires: kde5-kpkpass-devel kde5-kitinerary-devel
BuildRequires: kf5-kdeclarative-devel kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel kf5-kpackage-devel
BuildRequires: kf5-kwallet-devel kf5-syntax-highlighting-devel kf5-prison-devel kf5-kholidays-devel

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

%package -n %libkaddressbookmergelibprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkaddressbookmergelibprivate
KF5 library

%package -n %libkaddressbookimportexportlibprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkaddressbookimportexportlibprivate
KF5 library

%package -n %libshorturlpluginprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libshorturlpluginprivate
KF5 library

%package -n %libadblocklibprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libadblocklibprivate
KF5 library

%package -n %libgrammarcommon
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libgrammarcommon
KF5 library

%package -n %libkmailgrammalecte
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkmailgrammalecte
KF5 library

%package -n %libkmaillanguagetool
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkmaillanguagetool
KF5 library

%package -n %libkmailmarkdown
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkmailmarkdown
KF5 library

%package kaddressbook
Summary: addon
Group: Graphical desktop/KDE
Requires: %name-common
%description kaddressbook
%summary.

%package kmail
Summary: addon
Group: Graphical desktop/KDE
Requires: %name-common
%description kmail
%summary.

%package korganizer
Summary: addon
Group: Graphical desktop/KDE
Requires: %name-common
%description korganizer
%summary.

%package plugins
Summary: addon
Group: Graphical desktop/KDE
Requires: %name-common
%description plugins
%summary.

%prep
%setup -n %rname-%version
#%patch1 -p1

%build
%K5build \
    -DKDEPIMADDONS_BUILD_EXAMPLES=OFF \
    #

%install
%K5install
%K5install_move data kmail2 messageviewer kconf_update contacteditor
%find_lang %name --with-kde --all-name


%files

%files common -f %name.lang
#%doc COPYING*
%config(noreplace) %_K5xdgconf/kmail.*
%_datadir/qlogging-categories5/*.*categories
%_K5conf_up/*.upd

%files kaddressbook
%_K5plug/kaddressbook/
%_K5lib/contacteditor/editorpageplugins/cryptopageplugin.so
%_K5plug/contacteditor/
%_K5data/contacteditor/

%files kmail
%_K5bin/kmail_*.sh
%_K5plug/kmail/
%_K5plug/mailtransport/mailtransport_sendplugin.so
%_K5data/kmail2/pics/*.*

%files korganizer
%_K5plug/korg_*.so
%_K5srv/korganizer/
%_K5plug/plasmacalendarplugins/
%_K5qml/org/kde/plasma/PimCalendars/

%files plugins
%_K5plug/libksieve/*.so
%_K5plug/pimcommon/
%_K5plug/messageviewer/
#%_K5plug/messageviewer_*.so
%_K5plug/importwizard/
%_K5plug/templateparser/
%_K5plug/webengineviewer/
#%_K5data/messageviewer/

#%files devel
#%_K5inc/kdepim-addons_version.h
#%_K5inc/kdepim-addons/
#%_K5link/lib*.so
#%_K5lib/cmake/kdepim-addons
#%_K5archdata/mkspecs/modules/qt_kdepim-addons.pri
#%_datadir/qtcreator/templates/*/

%files -n %libkaddressbookmergelibprivate
%_K5lib/libkaddressbookmergelibprivate.so.%sover
%_K5lib/libkaddressbookmergelibprivate.so.*
%files -n %libkaddressbookimportexportlibprivate
%_K5lib/libkaddressbookimportexportlibprivate.so.%sover
%_K5lib/libkaddressbookimportexportlibprivate.so.*
%files -n %libshorturlpluginprivate
%_K5lib/libshorturlpluginprivate.so.%sover
%_K5lib/libshorturlpluginprivate.so.*
%files -n %libadblocklibprivate
%_K5lib/libadblocklibprivate.so.%sover
%_K5lib/libadblocklibprivate.so.*
%files -n %libgrammarcommon
%_K5lib/libgrammarcommon.so.%sover
%_K5lib/libgrammarcommon.so.*
%files -n %libkmailgrammalecte
%_K5lib/libkmailgrammalecte.so.%sover
%_K5lib/libkmailgrammalecte.so.*
%files -n %libkmaillanguagetool
%_K5lib/libkmaillanguagetool.so.%sover
%_K5lib/libkmaillanguagetool.so.*
%files -n %libkmailmarkdown
%_K5lib/libkmailmarkdown.so.%sover
%_K5lib/libkmailmarkdown.so.*

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

* Wed Apr 12 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt2%ubt
- fix build requires

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
