%define rname akregator

%define sover 5
%define libakregatorinterfaces libakregatorinterfaces%sover
%define libakregatorprivate libakregatorprivate%sover

Name: kde5-%rname
Version: 19.12.1
Release: alt1
%K5init no_appdata

Group: Networking/News
Summary: RSS/Atom feed reader
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Provides: kde5-pim-akregator = %EVR
Obsoletes: kde5-pim-akregator < %EVR

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Mar 15 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ grantlee5-devel gtk-update-icon-cache kde5-libkleo-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kdoctools-devel kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libgpg-error-devel libgpgme-devel libgst-plugins1.0 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sensors libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webengine libqt5-webenginecore libqt5-webenginewidgets libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-webchannel-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-webengine-devel
BuildRequires: boost-devel libassuan-devel libsasl2-devel
BuildRequires: kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-grantleetheme-devel kde5-kcontacts-devel kde5-kimap-devel
BuildRequires: kde5-kmime-devel kde5-kontactinterface-devel kde5-kpimtextedit-devel kde5-libkdepim-devel kde5-messagelib-devel kde5-pimcommon-devel
BuildRequires: kf5-kcmutils-devel kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-kiconthemes-devel
BuildRequires: kf5-kio-devel kf5-kitemmodels-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-ktexteditor-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kwindowsystem-devel
BuildRequires: kf5-syndication-devel

%description
RSS/Atom feed reader for KDE.
 
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

%package -n %libakregatorinterfaces
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libakregatorinterfaces
%name library

%package -n %libakregatorprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libakregatorprivate
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data akregator kconf_update kontact messageviewer
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
#%config(noreplace) %_K5xdgconf/*akregator*.*categories
%_datadir/qlogging-categories5/*.*categories
%_K5srvtyp/*akregator*.desktop

%files
%_K5bin/akregator
%_K5bin/akregatorstorageexporter
%_K5plug/akregator_*.so
%_K5plug/akregatorpart.so
%_K5plug/kontact_akregatorplugin.so
%_K5xdgapp/org.kde.akregator.desktop
%_K5data/akregator/
%_K5cfg/*akregator*.kcfg
%_K5cf_upd/*akregator*
#%_K5xmlgui/akregator/
%_K5notif/akregator.notifyrc
%_K5srv/kontact/akregatorplugin.desktop
%_K5srv/akregator_*.desktop
%_K5srv/feed.protocol
%_K5icon/*/*/apps/akregator*.*
%_K5data/kontact/ksettingsdialog/*akregator*
#%_K5data/messageviewer/about/default/*akregator*

#%files devel
#%_K5inc/akregator_version.h
#%_K5inc/akregator/
#%_K5link/lib*.so
#%_K5lib/cmake/akregator
#%_K5archdata/mkspecs/modules/qt_akregator.pri

%files -n %libakregatorinterfaces
%_K5lib/libakregatorinterfaces.so.%sover
%_K5lib/libakregatorinterfaces.so.*
%files -n %libakregatorprivate
%_K5lib/libakregatorprivate.so.%sover
%_K5lib/libakregatorprivate.so.*

%changelog
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

* Thu Mar 16 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Wed Mar 15 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.2-alt1%ubt
- initial build
