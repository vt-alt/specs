%define rname kontact

%define pim_sover 5
%define libkontactprivate libkontactprivate%pim_sover

Name: kde5-%rname
Version: 19.12.2
Release: alt1
%K5init no_appdata

Group: Graphical desktop/KDE
Summary: Integrated solution to the KDE PIM
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Provides: kde5-pim-kontact = %EVR
Obsoletes: kde5-pim-kontact < %EVR

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Mar 17 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ gtk-update-icon-cache kde5-libkleo-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kdoctools-devel kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libgpg-error libgpgme-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sql libqt5-svg libqt5-webchannel libqt5-webengine libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-webchannel-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: boost-devel-headers extra-cmake-modules kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-grantleetheme-devel kde5-kcontacts-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kmime-devel kde5-kontactinterface-devel kde5-kpimtextedit-devel kde5-libkdepim-devel kde5-mailcommon-devel kde5-messagelib-devel kde5-pim-apps-libs-devel kde5-pimcommon-devel kf5-kcmutils-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-kiconthemes-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kparts-devel kf5-ktextwidgets-devel kf5-kwindowsystem-devel libsasl2-devel python-module-google python3-dev qt5-webengine-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-webengine-devel
BuildRequires: boost-devel libsasl2-devel
BuildRequires: kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-grantleetheme-devel kde5-kcontacts-devel
BuildRequires: kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kmime-devel kde5-kontactinterface-devel kde5-kpimtextedit-devel
BuildRequires: kde5-libkdepim-devel kde5-mailcommon-devel kde5-messagelib-devel kde5-pim-apps-libs-devel kde5-pimcommon-devel
BuildRequires: kf5-kcmutils-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static
BuildRequires: kf5-kiconthemes-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kparts-devel kf5-ktextwidgets-devel kf5-kwindowsystem-devel

%description
Integrated solution to the KDE PIM.

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

%package -n %libkontactprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libkontactprivate
%name library

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data kontact kconf_update messageviewer
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
#%config(noreplace) %_K5xdgconf/*.*categories
%_datadir/qlogging-categories5/*.*categories

%files
%_K5bin/*kontact*
%_K5plug/*kontact*.so
%_K5xdgapp/*kontact*.desktop
#%_K5data/kontact/
%_K5data/messageviewer/about/default/*kontact*
%_K5cfg/*kontact*.kcfg
%_K5cf_upd/*kontact*
#%_K5xmlgui/*kontact*/
%_K5srv/*kontact*.desktop
%_K5icon/*/*/apps/*kontact*.*
%_K5dbus_srv/*kontact*.service

#%files devel
#%_K5inc/kontact_version.h
#%_K5inc/kontact/
#%_K5link/lib*.so
#%_K5lib/cmake/kontact
#%_K5archdata/mkspecs/modules/qt_kontact.pri

%files -n %libkontactprivate
%_K5lib/libkontactprivate.so.%pim_sover
%_K5lib/libkontactprivate.so.*

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
