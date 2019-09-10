%define rname kstars

Name: kde5-%rname
Version: 3.3.6
Release: alt1
Epoch: 1
%K5init

Group: Education
Summary: Desktop Planetarium
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: indi

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Mar 18 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel rpm-build-gir rpm-build-python3 xml-common xml-utils zlib-devel
#BuildRequires: eigen3 extra-cmake-modules kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kparts-devel kf5-kplotting-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libGLU-devel libcfitsio-devel libindi-devel python-module-google python3.3-site-packages qt5-multimedia-devel qt5-svg-devel ruby ruby-stdlibs wcslib-devel xplanet zlib-devel-static
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-declarative-devel qt5-multimedia-devel qt5-svg-devel qt5-websockets-devel
BuildRequires: qt5-datavis3d-devel
BuildRequires: libsecret-devel libqtkeychain-qt5-devel
BuildRequires: xplanet eigen3 libGLU-devel zlib-devel
BuildRequires: libcfitsio-devel libindi-devel wcslib-devel libraw-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kparts-devel kf5-kplotting-devel
BuildRequires: kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel
BuildRequires: kf5-solid-devel kf5-sonnet-devel kf5-kcrash-devel kf5-knotifyconfig-devel

%description
KStars is a Desktop Planetarium for KDE. It provides an accurate graphical
simulation of the night sky, from any location on Earth, at any date and
time. The display includes 130,000 stars, 13,000 deep-sky objects,all 8
planets, the Sun and Moon, and thousands of comets and asteroids.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data kstars sounds
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
#%config(noreplace) %_K5xdgconf/kstars.knsrc
%_K5bin/kstars
%_K5data/kstars/
%_K5icon/*/*/apps/kstars.*
#%_K5icon/*/*/actions/kstars_*.*
%_K5snd/KDE-KStars-*.*
%_K5xdgapp/org.kde.kstars.desktop
#%_K5xmlgui/kstars/
%_K5notif/kstars.notifyrc
# kauth
#%_K5libexecdir/kauth/kauth_kstars_helper
#%_K5conf_dbus_sysd/*kstars*.conf
#%_K5dbus_sys_srv/*kstars*.service
#%_datadir/polkit-1/actions/*kstars*.policy
%_K5cfg/kstars.kcfg

%changelog
* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 1:3.3.6-alt1
- new version

* Thu Dec 27 2018 Sergey V Turchin <zerg@altlinux.org> 1:3.0.0-alt1
- new version

* Wed Aug 01 2018 Sergey V Turchin <zerg@altlinux.org> 1:2.9.7-alt2%ubt
- fix build requires

* Fri Jul 27 2018 Sergey V Turchin <zerg@altlinux.org> 1:2.9.7-alt1%ubt
- new version

* Fri Apr 13 2018 Sergey V Turchin <zerg@altlinux.org> 1:2.9.4-alt2%ubt
- fix build requires

* Thu Apr 12 2018 Sergey V Turchin <zerg@altlinux.org> 1:2.9.4-alt1%ubt
- new version

* Fri Jan 19 2018 Sergey V Turchin <zerg@altlinux.org> 1:2.9.1-alt1%ubt
- new version

* Mon Dec 25 2017 Sergey V Turchin <zerg@altlinux.org> 1:2.8.9-alt1%ubt
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Wed Jun 07 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Sep 22 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Mon Apr 04 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt4
- fix build requires

* Tue Mar 22 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt3
- rebuild with new wcslib

* Tue Mar 22 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt2
- rebuild with new cfitsio

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
