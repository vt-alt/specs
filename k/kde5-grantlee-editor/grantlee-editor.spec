%define rname grantlee-editor

%define pim_sover 5
%define libgrantleethemeeditor libgrantleethemeeditor%pim_sover

Name: kde5-%rname
Version: 19.08.1
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: Mail Header and Contact Theme Editor
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Mar 21 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ grantlee5-devel kde5-libkleo-devel kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kdoctools-devel kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libgpg-error libgpg-error-devel libgpgme-devel libgst-plugins1.0 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sensors libqt5-sql libqt5-svg libqt5-webchannel libqt5-webengine libqt5-webenginecore libqt5-webenginewidgets libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-webchannel-devel rpm-build-python3 xml-common xml-utils
#BuildRequires: boost-devel-headers extra-cmake-modules kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-grantleetheme-devel kde5-kcontacts-devel kde5-kimap-devel kde5-kmime-devel kde5-kpimtextedit-devel kde5-libkdepim-devel kde5-messagelib-devel kde5-pim-apps-libs-devel kde5-pimcommon-devel kf5-karchive-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-kio-devel kf5-kitemmodels-devel kf5-knewstuff-devel kf5-kparts-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwallet-devel kf5-syntax-highlighting-devel libassuan-devel libsasl2-devel python-module-google python3-dev qt5-webengine-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-webengine-devel
BuildRequires: boost-devel libassuan-devel libsasl2-devel
BuildRequires: kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-grantleetheme-devel kde5-kcontacts-devel
BuildRequires: kde5-kimap-devel kde5-kmime-devel kde5-kpimtextedit-devel kde5-libkdepim-devel kde5-messagelib-devel
BuildRequires: kde5-pim-apps-libs-devel kde5-pimcommon-devel
BuildRequires: kf5-karchive-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static
BuildRequires: kf5-kio-devel kf5-kitemmodels-devel kf5-knewstuff-devel kf5-kparts-devel kf5-ktexteditor-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kwallet-devel kf5-syntax-highlighting-devel

%description
KMail Header and KAddressbook Contact Theme Editor.

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

%package -n %libgrantleethemeeditor
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libgrantleethemeeditor
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files
%_K5bin/*editor*
#%_K5conf_up/*editor*
%_K5xdgapp/*editor*.desktop
%_K5cfg/*editor*
#%_K5notif/*editor*
%_datadir/qlogging-categories5/*.*categories

#%files devel
#%_K5inc/grantlee-editor_version.h
#%_K5inc/grantlee-editor/
#%_K5link/lib*.so
#%_K5lib/cmake/grantlee-editor
#%_K5archdata/mkspecs/modules/qt_grantlee-editor.pri

%files -n %libgrantleethemeeditor
%_K5lib/libgrantleethemeeditor.so.%pim_sover
%_K5lib/libgrantleethemeeditor.so.*

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

* Thu Mar 16 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- initial build
