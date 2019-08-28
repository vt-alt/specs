%define rname korganizer

%define pim_sover 5
%define libkorganizer_core libkorganizer_core%pim_sover
%define libkorganizer_interfaces libkorganizer_interfaces%pim_sover
%define libkorganizerprivate libkorganizerprivate%pim_sover

Name: kde5-%rname
Version: 19.08.0
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: Electronic organizer
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Provides: kde5-pim-korganizer = %EVR
Obsoletes: kde5-pim-korganizer < %EVR
Requires: kde5-akonadi kde5-pim-runtime kde5-akonadi-search

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Mar 17 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ gtk-update-icon-cache kde5-libkleo-devel kf5-attica-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdb4-devel libdbusmenu-qt52 libgpg-error libgpg-error-devel libgpgme-devel libgst-plugins1.0 libical-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sensors libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webenginecore libqt5-webenginewidgets libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms libxkbfile-devel perl pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-tools-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: boost-devel-headers extra-cmake-modules kde5-akonadi-calendar-devel kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-akonadi-notes-devel kde5-akonadi-search-devel kde5-calendarsupport-devel kde5-eventviews-devel kde5-incidenceeditor-devel kde5-kcalcore-devel kde5-kcalutils-devel kde5-kcontacts-devel kde5-kholidays-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kldap-devel kde5-kmailtransport-devel kde5-kmime-devel kde5-kontactinterface-devel kde5-kpimtextedit-devel kde5-libkdepim-devel kde5-mailcommon-devel kde5-messagelib-devel kde5-pim-apps-libs-devel kde5-pimcommon-devel kf5-kcmutils-devel kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel kf5-knewstuff-devel kf5-kwallet-devel libXres-devel libassuan-devel libldap-devel libsasl2-devel python-module-google python3-dev qt5-phonon-devel qt5-tools-devel-static qt5-x11extras-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-phonon-devel qt5-tools-devel-static qt5-x11extras-devel
BuildRequires: boost-devel libXres-devel libassuan-devel libldap-devel libsasl2-devel
BuildRequires: kde5-akonadi-calendar-devel kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-akonadi-notes-devel
BuildRequires: kde5-akonadi-search-devel kde5-calendarsupport-devel kde5-eventviews-devel kde5-incidenceeditor-devel kde5-kcalcore-devel
BuildRequires: kde5-kcalutils-devel kde5-kcontacts-devel kf5-kholidays-devel kde5-kidentitymanagement-devel kde5-kimap-devel
BuildRequires: kde5-kldap-devel kde5-kmailtransport-devel kde5-kmime-devel kde5-kontactinterface-devel kde5-kpimtextedit-devel
BuildRequires: kde5-libkdepim-devel kde5-mailcommon-devel kde5-messagelib-devel kde5-pim-apps-libs-devel kde5-pimcommon-devel
BuildRequires: kf5-kcmutils-devel kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel kf5-knewstuff-devel kf5-kwallet-devel

%description
Electronic organizer.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Conflicts: kde5-pim-common < 16.12
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkorganizer_core
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libkorganizer_core
%name library

%package -n %libkorganizer_interfaces
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libkorganizer_interfaces
%name library

%package -n %libkorganizerprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libkorganizerprivate
%name library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DDATA_INSTALL_DIR=%_K5data \
    #

%install
%K5install
%K5install_move data korgac korganizer kontact kconf_update
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_K5srvtyp/*.desktop
%_K5icon/*/*/actions/*
%_datadir/qlogging-categories5/*.*categories

%files
%_K5bin/korgac
%_K5bin/korganizer
#%_K5bin/ical2vcal
%_K5plug/*korganizer*.so
%_K5plug/kcm_apptsummary.so
%_K5plug/kcm_todosummary.so
%_K5plug/kcm_sdsummary.so
%_K5plug/kontact_journalplugin.so
%_K5plug/kontact_todoplugin.so
%_K5plug/kontact_specialdatesplugin.so
%_K5start/org.kde.korgac.desktop
%_K5xdgapp/korganizer-import.desktop
%_K5xdgapp/org.kde.korganizer.desktop
%_K5data/korgac/
%_K5data/korganizer/
%_K5data/kontact/ksettingsdialog/*
%_K5data/knsrcfiles/*korganizer*
%_K5cfg/*korganizer*
%_K5cf_upd/*korganizer*
#%_K5xmlgui/korganizer/
%_K5srv/kontact/korganizerplugin.desktop
%_K5srv/korganizer_*.desktop
%_K5srv/webcal.protocol
%_K5srv/kcmapptsummary.desktop
%_K5srv/kcmsdsummary.desktop
%_K5srv/kcmtodosummary.desktop
%_K5srv/kontact/journalplugin.desktop
%_K5srv/kontact/specialdatesplugin.desktop
#%_K5srv/kontact/summaryplugin.desktop
%_K5srv/kontact/todoplugin.desktop
%_K5icon/*/*/apps/korganizer.*
%_K5icon/*/*/apps/korg-*.*
%_K5icon/*/*/apps/quickview.*
#%doc %_K5doc/en/korganizer

#%files devel
#%_K5inc/korganizer_version.h
#%_K5inc/korganizer/
#%_K5link/lib*.so
#%_K5lib/cmake/korganizer
#%_K5archdata/mkspecs/modules/qt_korganizer.pri

%files -n %libkorganizer_core
%_K5lib/libkorganizer_core.so.%pim_sover
%_K5lib/libkorganizer_core.so.*
%files -n %libkorganizer_interfaces
%_K5lib/libkorganizer_interfaces.so.%pim_sover
%_K5lib/libkorganizer_interfaces.so.*
%files -n %libkorganizerprivate
%_K5lib/libkorganizerprivate.so.%pim_sover
%_K5lib/libkorganizerprivate.so.*

%changelog
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

* Thu Mar 16 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Wed Mar 15 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.2-alt1%ubt
- initial build
