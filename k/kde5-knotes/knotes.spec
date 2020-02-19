%define rname knotes

%define pim_sover 5
%define libknotesprivate libknotesprivate%pim_sover
%define libnotesharedprivate libnotesharedprivate%pim_sover

Name: kde5-%rname
Version: 19.12.2
Release: alt1
%K5init no_appdata

Group: Graphical desktop/KDE
Summary: Post-It notes on the KDE desktop
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Provides: kde5-pim-knotes = %EVR
Obsoletes: kde5-pim-knotes < %EVR
Requires: kde5-akonadi kde5-pim-runtime kde5-akonadi-search

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Mar 17 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ gtk-update-icon-cache kf5-attica-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbusmenu-qt52 libgpg-error libical-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcb-devel libxcbutil-keysyms libxkbfile-devel perl pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: boost-devel-headers extra-cmake-modules grantlee5-devel kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-akonadi-notes-devel kde5-akonadi-search-devel kde5-kcalcore-devel kde5-kcalutils-devel kde5-kcontacts-devel kde5-kimap-devel kde5-kmime-devel kde5-kontactinterface-devel kde5-kpimtextedit-devel kde5-libkdepim-devel kde5-pimcommon-devel kf5-kcmutils-devel kf5-kdelibs4support-devel kf5-kdnssd-devel kf5-kdoctools-devel-static kf5-kglobalaccel-devel kf5-kio-devel kf5-knewstuff-devel kf5-knotifyconfig-devel libXres-devel libsasl2-devel python-module-google python3-dev qt5-x11extras-devel rpm-build-ruby xsltproc
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-x11extras-devel
BuildRequires: boost-devel grantlee5-devel libXres-devel libsasl2-devel xsltproc
BuildRequires: kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-akonadi-notes-devel kde5-akonadi-search-devel
BuildRequires: kde5-kcalcore-devel kde5-kcalutils-devel kde5-kcontacts-devel kde5-kimap-devel kde5-kmime-devel kde5-kontactinterface-devel
BuildRequires: kde5-kpimtextedit-devel kde5-libkdepim-devel kde5-pimcommon-devel kde5-grantleetheme-devel
BuildRequires: kf5-kcmutils-devel kf5-kdelibs4support-devel kf5-kdnssd-devel kf5-kdoctools-devel-static kf5-kglobalaccel-devel
BuildRequires: kf5-kio-devel kf5-knewstuff-devel kf5-knotifyconfig-devel

%description
Post-It notes on the KDE desktop.

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

%package -n %libnotesharedprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libnotesharedprivate
%name library

%package -n %libknotesprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libknotesprivate
%name library

%prep
%setup -n %rname-%version

%build
%K5build \
    -DDATA_INSTALL_DIR=%_K5data \
    #

%install
%K5install
%K5install_move data knotes kconf_update kontact knsrcfiles
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_datadir/qlogging-categories5/*.*categories
%_K5cfg/*note*

%files
%_K5bin/*note*
%_K5plug/*note*.so
%_K5xdgapp/org.kde.*note*.desktop
%_K5data/*note*/
%_K5data/kontact/ksettingsdialog/*note*
%_K5data/knsrcfiles/*note*
%_K5cf_upd/*note*
%_K5xmlgui/*note*/
%_K5srv/kontact/*note*.desktop
%_K5srv/*note*.desktop
%_K5icon/*/*/apps/*note*.*
%_K5icon/*/*/actions/*note*.*
%_K5notif/*note*.notifyrc
%_datadir/akonadi5/agents/*note*
#%doc %_K5doc/en/knotes

#%files devel
#%_K5inc/knotes_version.h
#%_K5inc/knotes/
#%_K5link/lib*.so
#%_K5lib/cmake/knotes
#%_K5archdata/mkspecs/modules/qt_knotes.pri

%files -n %libknotesprivate
%_K5lib/libknotesprivate.so.%pim_sover
%_K5lib/libknotesprivate.so.*

%files -n %libnotesharedprivate
%_K5lib/libnotesharedprivate.so.%pim_sover
%_K5lib/libnotesharedprivate.so.*

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

* Wed Jul 18 2018 Oleg Solovyov <mcpain@altlinux.org> 18.04.2-alt2%ubt
- fix: duplicated notes

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
