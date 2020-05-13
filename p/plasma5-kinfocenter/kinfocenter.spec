%define rname kinfocenter

Name: plasma5-%rname
Version: 5.18.5
Release: alt1
%K5init altplace no_appdata

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 Info Center
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: usbids kf5-kirigami
Provides:  kf5-kinfocenter = %EVR kf5-kinfocenter-common = %EVR plasma5-kinfocenter-common = %EVR
Obsoletes: kf5-kinfocenter < %EVR kf5-kinfocenter-common < %EVR plasma5-kinfocenter-common < %EVR

Source: %rname-%version.tar
Patch1: alt-usbids-path.patch

# Automatically added by buildreq on Thu Mar 26 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils glibc-devel-static kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXrender-devel libXt-devel libcloog-isl4 libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libraw1394-11 libstdc++-devel libwayland-client libwayland-server libxcbutil-keysyms pkg-config python-base ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libGLU-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libpci-devel libraw1394-devel libxkbfile-devel python-module-google qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel qt5-declarative-devel
BuildRequires: libpci-devel libraw1394-devel
BuildRequires: libGLU-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel
BuildRequires: libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel
BuildRequires: libxkbfile-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel
BuildRequires: kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel
BuildRequires: kf5-kwayland-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel
BuildRequires: kf5-kdeclarative-devel kf5-kpackage-devel

%description
KDE Info Center.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Provides: kf5-kinfocenter-common = %EVR
Obsoletes: kf5-kinfocenter-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Provides: kf5-kinfocenter-devel = %EVR
Obsoletes: kf5-kinfocenter-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5infocenter
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5infocenter
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install

#K5install_move data all
%K5install_move data desktop-directories kcmusb kcmview1394 kpackage 
%K5install_move menu all

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/*
%_K5plug/kcms/
%_K5plug/*.so
%_K5xdgapp/*.desktop
%_K5xdgdir/*.directory
%_K5xdgmenu/*.menu
%_K5data/kcm*/
%_K5data/kpackage/
%_K5srv/*
%_K5srvtyp/*
%_K5xmlgui/*

%changelog
* Thu May 07 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.5-alt1
- new version

* Thu Apr 02 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.4-alt1
- new version

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.3-alt1
- new version

* Wed Feb 19 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.1-alt1
- new version

* Fri Feb 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.17.5-alt2
- Applied upstream patch fixing crash in energyinfo widget (Closes: #37644)

* Thu Jan 09 2020 Sergey V Turchin <zerg@altlinux.org> 5.17.5-alt1
- new version

* Thu Dec 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.4-alt1
- new version

* Wed Nov 13 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.3-alt1
- new version

* Fri Nov 01 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.2-alt1
- new version

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.1-alt1
- new version

* Thu Oct 17 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.5-alt1
- new version

* Thu Aug 01 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.4-alt1
- new version

* Thu Jul 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.3-alt1
- new version

* Wed Jun 26 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.2-alt1
- new version

* Tue Jun 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.1-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt2
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt1
- new version

* Wed Apr 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.4-alt1
- new version

* Tue Mar 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt1
- new version

* Thu Sep 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version

* Wed Jun 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1%ubt
- new version

* Thu May 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1%ubt
- new version

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1%ubt
- new version

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt2%ubt
- fix package translations and docs

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1%ubt
- new version

* Thu Mar 01 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1%ubt
- new version

* Mon Feb 19 2018 Maxim Voronov <mvoronov@altlinux.org> 5.12.0-alt2%ubt
- renamed kf5-kinfocenter -> plasma5-kinfocenter

* Wed Feb 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1%ubt
- new version

* Wed Jan 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt1%ubt
- new version

* Mon Dec 11 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.4-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1%ubt
- new version

* Tue Nov 07 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Mon Sep 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt1%ubt
- new version

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.3-alt1%ubt
- new version

* Wed Apr 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Mon Apr 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.1-alt1%ubt
- new version

* Fri Dec 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt1%ubt
- new version

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt0.M80P.1
- build for M80P

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt1
- new version

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1
- new version

* Tue Oct 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt0.M80P.1
- build for M80P

* Fri Oct 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt1
- new version

* Tue Oct 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Tue Aug 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt1
- new version

* Mon Aug 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.3-alt1
- new version

* Tue Jul 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.2-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1
- new version

* Wed Jul 06 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt1
- new version

* Wed Jun 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.5-alt1
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.4-alt1
- new version

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.3-alt1
- new version

* Wed Mar 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.5-alt1
- new version

* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- new version

* Thu Jan 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt1
- new version

* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt1
- new version

* Thu Dec 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Thu Nov 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt3
- rebuild

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt1
- new version

* Wed Oct 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Wed Aug 26 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Sat Aug 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.95-alt1
- new version

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.1
- test

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
