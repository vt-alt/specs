%define rname kalarm

Name: kde5-%rname
Version: 19.08.0
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: Personal Alarm Scheduler
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Provides: kde5-pim-kalarm = %EVR
Obsoletes: kde5-pim-kalarm < %EVR
Conflicts: kde5-pim-common < 16.12

Source: %rname-%version.tar
Patch: alt-kalarm-ignore-tz.patch

# Automatically added by buildreq on Thu Mar 16 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ gtk-update-icon-cache kde5-libkleo-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdb4-devel libdbusmenu-qt52 libgpg-error libgpgme-devel libical-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sql libqt5-svg libqt5-webchannel libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcb-devel libxcbutil-keysyms libxkbfile-devel perl pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: boost-devel-headers extra-cmake-modules kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-kalarmcal-devel kde5-kcalcore-devel kde5-kcalutils-devel kde5-kcontacts-devel kde5-kholidays-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kmailtransport-devel kde5-kmime-devel kde5-kpimtextedit-devel kde5-libkdepim-devel kde5-mailcommon-devel kde5-messagelib-devel kde5-pim-apps-libs-devel kde5-pimcommon-devel kf5-kcmutils-devel kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel kf5-kwallet-devel libXres-devel libsasl2-devel python-module-google python3-dev qt5-phonon-devel qt5-x11extras-devel ruby ruby-stdlibs xsltproc
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-phonon-devel qt5-x11extras-devel
BuildRequires: boost-devel xsltproc libXres-devel libsasl2-devel
BuildRequires: kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-kalarmcal-devel kde5-kcalcore-devel kde5-kcalutils-devel
BuildRequires: kde5-kcontacts-devel kf5-kholidays-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kmailtransport-devel kde5-kmime-devel
BuildRequires: kde5-kpimtextedit-devel kde5-libkdepim-devel kde5-mailcommon-devel kde5-messagelib-devel kde5-pim-apps-libs-devel kde5-pimcommon-devel
BuildRequires: kf5-kcmutils-devel kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel kf5-kwallet-devel
BuildRequires: kf5-kglobalaccel-devel

%description
Personal Alarm Scheduler.

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

%package -n libkf5alarm
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5alarm
KF5 library


%prep
%setup -n %rname-%version
#%patch -p3

%build
%K5build

%install
%K5install
%K5install_move data kalarm kconf_update
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_datadir/qlogging-categories5/*.*categories
#%config(noreplace) %_K5conf_dbus_sysd/org.kde.kalarm.rtcwake.conf
%_K5bin/kalarm
%_K5bin/kalarmautostart
%_K5libexecdir/kauth/kalarm_helper
%_K5start/kalarm.autostart.desktop
%_K5xdgapp/org.kde.kalarm.desktop
%_K5cfg/*kalarm*.kcfg
%_K5cf_upd/*kalarm*
%_K5data/kalarm/
%_K5xmlgui/kalarm/
%_K5icon/*/*/apps/kalarm.*
#%doc %_K5doc/en/kalarm/
%_K5dbus_sys_srv/org.kde.kalarm.rtcwake.service
%_K5dbus/system.d/org.kde.kalarm.rtcwake.conf
%_datadir/polkit-1/actions/org.kde.kalarm.rtcwake.policy


%changelog
* Fri Aug 16 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Tue Jul 16 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Wed Jun 19 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt2
- fix package

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

* Thu Mar 01 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Thu Mar 01 2018 Oleg Solovyov <mcpain@altlinux.org> 17.08.3-alt2%ubt
- default: ignore timezone

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
