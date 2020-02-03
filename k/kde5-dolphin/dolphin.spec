%define rname dolphin

%define sover 5
%define libdolphinprivate libdolphinprivate%sover
%define libdolphinvcs libdolphinvcs%sover

Name: kde5-%rname
Version: 19.12.1
Release: alt1
%K5init

Group: File tools
Summary: The file manager for KDE
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: kf5-kio
#Requires: kf5-kio-extras

Source: %rname-%version.tar
Patch1: alt-dbus-service.patch
Patch2: alt-close-inactive-panel.patch
Patch3: alt-linking.patch

# Automatically added by buildreq on Fri Apr 17 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libcloog-isl4 libdbusmenu-qt52 libgpg-error libjson-c libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base qt5-base-devel ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: extra-cmake-modules gcc-c++ kf5-baloo-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libxapian-devel python-module-google qt5-phonon-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt5-phonon-devel
BuildRequires: libxapian-devel desktop-file-utils
BuildRequires: kf5-kfilemetadata-devel kf5-baloo-devel kde5-baloo-widgets-devel
BuildRequires: kf5-baloo-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel
BuildRequires: kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel
BuildRequires: kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kguiaddons-devel
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel
BuildRequires: kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

%description
Dolphin is a file manager for KDE focusing on usability.

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

%package -n %libdolphinprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libdolphinprivate
KF5 library

%package -n %libdolphinvcs
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libdolphinvcs
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    -DDATA_INSTALL_DIR=%_K5data \
    #

%install
%K5install
%K5install_move data kglobalaccel
%find_lang %name --with-kde --all-name

desktop-file-install --mode=0755 --dir %buildroot/%_K5xdgapp \
    --add-mime-type=x-scheme-handler/ftp \
    --add-mime-type=x-scheme-handler/trash \
    %buildroot/%_K5xdgapp/org.kde.dolphin.desktop
# kf5-kio-extras
#    --add-mime-type=x-scheme-handler/network \
# kf5-plasma-workspace
#    --add-mime-type=x-scheme-handler/desktop \
#    --add-mime-type=x-scheme-handler/remote \
#    --add-mime-type=x-scheme-handler/programs \
#    --add-mime-type=x-scheme-handler/applications \

%files common -f %name.lang
%doc COPYING*
%_datadir/locale/*/LC_SCRIPTS/dolphin/
%_datadir/qlogging-categories5/*.*categories

%files
%config(noreplace) %_K5xdgconf/*
%_K5bin/*
%_K5lib/libkdeinit5_dolphin.so
%_K5plug/*dolphin*.so
%_K5xdgapp/*dolphin*.desktop
%_K5cfg/dolphin*
%_K5srv/*.desktop
%_K5srvtyp/*.desktop
%_K5data/kglobalaccel/*dolphin*
%_K5dbus_srv/org.kde.dolphin.FileManager1.service

%files devel
%_K5inc/?olphin*
%_K5link/lib*.so
%_K5lib/cmake/DolphinVcs/
%_K5dbus_iface/org.freedesktop.FileManager1.xml

%files -n %libdolphinprivate
%_K5lib/libdolphinprivate.so.*
%_K5lib/libdolphinprivate.so.%sover
%files -n %libdolphinvcs
%_K5lib/libdolphinvcs.so.*
%_K5lib/libdolphinvcs.so.%sover

%changelog
* Tue Jan 21 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Fri Nov 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Fri Oct 25 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.2-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Tue Aug 27 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Mon May 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Tue Feb 19 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Wed Aug 15 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt4%ubt
- update russian translation

* Thu Aug 09 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt3%ubt
- update russian translation

* Tue Aug 07 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt2%ubt
- update russian translation

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Tue May 22 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Tue May 08 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt2%ubt
- update russian translation

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Mar 06 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Mon Nov 13 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Tue Aug 22 2017 Oleg Solovyov <mcpain@altlinux.org> 17.04.3-alt5%ubt
- revert to: F3 closes inactive panel

* Tue Aug 22 2017 Oleg Solovyov <mcpain@altlinux.org> 17.04.3-alt4%ubt
- revert previous changes

* Fri Aug 18 2017 Oleg Solovyov <mcpain@altlinux.org> 17.04.3-alt3%ubt
- add buttons closing left/right panel

* Mon Jul 24 2017 Oleg Solovyov <mcpain@altlinux.org> 17.04.3-alt2%ubt
- Fix: crash after closing left panel + changing tab

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Thu Jul 06 2017 Oleg Solovyov <mcpain@altlinux.org> 17.04.2-alt2%ubt
- F3 closes inactive panel

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Thu Mar 23 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Nov 24 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt0.M80P.1
- build for M80P

* Wed Nov 23 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Tue Sep 06 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- new version

* Thu Jul 14 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Fri Jul 01 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Fri Feb 26 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Tue Dec 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Mon Aug 24 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt2
- rebuild with new baloo

* Thu Aug 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Tue Aug 04 2015 Sergey V Turchin <zerg@altlinux.org> 15.7.80-alt2
- build with baloo

* Mon Aug 03 2015 Sergey V Turchin <zerg@altlinux.org> 15.7.80-alt1
- new beta

* Thu May 14 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.95-alt1
- update from master branch

* Sat Apr 18 2015 Sergey V Turchin <zerg@altlinux.org> 0.0.1-alt2
- fix requires

* Fri Apr 17 2015 Sergey V Turchin <zerg@altlinux.org> 0.0.1-alt1
- initial build
