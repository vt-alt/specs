%define rname akonadi-contacts

Name: kde5-%rname
Version: 19.12.1
Release: alt1
%K5init

Group: System/Libraries
Summary: Contact Management in Akonadi
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: alt-no-qwebengine.patch

# Automatically added by buildreq on Tue Aug 23 2016 (-bi)
# optimized out: cmake cmake-modules elfutils fontconfig gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libgpg-error libical-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webengine libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-webchannel-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: boost-devel-headers extra-cmake-modules grantlee5-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-kcalcore-devel kde5-kcontacts-devel kde5-kmime-devel kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel python-module-google python3-dev qt5-webengine-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: boost-devel extra-cmake-modules qt5-base-devel qt5-webengine-devel
BuildRequires: grantlee5-devel
BuildRequires: kde5-akonadi-devel kde5-akonadi-mime-devel kde5-kcalcore-devel kde5-kcontacts-devel kde5-kmime-devel
BuildRequires: kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel kf5-prison-devel

%description
Libraries and daemons to implement Contact Management in Akonadi.

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

%package -n libkf5akonadicontact
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5akonadicontact
KF5 library

%package -n libkf5contacteditor
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5contacteditor
KF5 library


%prep
%setup -n %rname-%version
#%patch1 -p1

%build
%K5build

%install
%K5install
%K5install_move data akonadicontact contacteditor
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
#%config(noreplace) %_K5xdgconf/*contact*.*categories
%_datadir/qlogging-categories5/*.*categories

%files devel
#%_K5inc/akonadi-contact_version.h
%_K5inc/?konadi/?ontact/
%_K5inc/*ontact*/
%_K5link/lib*.so
%_K5lib/cmake/KF5*Contact*/
%_K5archdata/mkspecs/modules/qt_*Contact*.pri

%files -n libkf5akonadicontact
%_K5lib/libKF5AkonadiContact.so.*
%_K5plug/*akonadicontact*.so
#%_K5srv/akonadi/contact/
%_K5srv/*akonadicontact*.desktop
#
%_K5plug/akonadi_serializer_addressee.so
%_datadir/akonadi5/plugins/serializer/akonadi_serializer_addressee.desktop
#
%_datadir/akonadi5/contact/
#%_K5srvtyp/*.desktop

%files -n libkf5contacteditor
%_K5lib/libKF5ContactEditor.so.*
#%_K5plug/*contacteditor*.so
%_K5plug/akonadi/contacts/plugins/categorieseditwidgetplugin.so
#%_K5data/contacteditor/
#
%_K5plug/akonadi_serializer_contactgroup.so
%_datadir/akonadi5/plugins/serializer/akonadi_serializer_contactgroup.desktop

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

* Wed Mar 15 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.2-alt1%ubt
- new version

* Wed Dec 07 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt2%ubt
- build without QWebEngine

* Mon Nov 28 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt0.M80P.1
- build for M80P

* Fri Nov 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Sep 05 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt2
- update conflicts

* Mon Aug 22 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- initial build
