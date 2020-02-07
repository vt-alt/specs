%define rname juk
%def_disable tunepimp

Name: kde5-%rname
Version: 19.12.1
Release: alt1
%K5init

Group: Sound
Summary: Music Player
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Dec 21 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules qt5-base-common qt5-base-devel xml-common xml-utils
#BuildRequires: extra-cmake-modules gtk-update-icon-cache kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-kglobalaccel-devel kf5-kiconthemes-devel kf5-kio-devel kf5-knotifications-devel kf5-ktextwidgets-devel kf5-kwallet-devel kf5-kwindowsystem-devel libssl-devel libtag-devel qt5-phonon-devel qt5-svg-devel
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-phonon-devel qt5-svg-devel
BuildRequires: libssl-devel libtag-devel
BuildRequires: kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-kglobalaccel-devel kf5-kiconthemes-devel
BuildRequires: kf5-kio-devel kf5-knotifications-devel kf5-ktextwidgets-devel kf5-kwallet-devel kf5-kwindowsystem-devel
BuildRequires: kf5-kdbusaddons-devel
%if_enabled tunepimp
BuildRequires: libtunepimp-devel
%endif

%description
Juk is a jukebox, tagger and music collection manager.

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

%package -n libkf5juk
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n libkf5juk
%name library


%prep
%setup -n %rname-%version
%if_disabled tunepimp
sed -i '/^find_package.*TunePimp/d' CMakeLists.txt
%endif

%build
%K5build

%install
%K5install
%K5install_move data juk
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/juk
%_K5xdgapp/org.kde.juk.desktop
%_K5data/juk/
%_K5xmlgui/juk/
%_K5icon/*/*/apps/juk.*
%_K5srv/ServiceMenus/*juk*
%_K5notif/juk.notifyrc

%changelog
* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Mon Nov 25 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Wed Aug 28 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Tue May 07 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Mon Feb 25 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Thu Jan 18 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.1-alt1%ubt
- new version

* Wed Dec 20 2017 Sergey V Turchin <zerg@altlinux.org> 17.12.0-alt1%ubt
- initial build
