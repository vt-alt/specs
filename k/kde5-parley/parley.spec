%define rname parley

Name: kde5-%rname
Version: 19.12.1
Release: alt1
%K5init

%add_findreq_skiplist %_K5data/parley/plugins/*.py

Group: Education
Summary: Vocabulary training application
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: kde5-kdeedu-data

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Mar 18 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms libxml2-devel pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-gir rpm-build-python3 xml-common xml-utils
#BuildRequires: extra-cmake-modules kde5-libkeduvocdocument-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjs-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kparts-devel kf5-kross-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libxslt-devel python-module-google python3.3-site-packages qt5-multimedia-devel qt5-script-devel qt5-svg-devel ruby ruby-stdlibs xsltproc
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-multimedia-devel qt5-script-devel qt5-svg-devel qt5-webengine-devel
BuildRequires: libxslt-devel xsltproc
BuildRequires: kde5-libkeduvocdocument-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdelibs4support
BuildRequires: kf5-kdoctools kf5-kdoctools-devel-static kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel
BuildRequires: kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjs-devel kf5-knewstuff-devel kf5-knotifications-devel
BuildRequires: kf5-kparts-devel kf5-kross-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

%description
Parley is a program to help you memorize things.

Parley supports many language specific features but can be used for other
learning tasks just as well. It uses the spaced repetition learning method,
also known as flash cards.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data parley
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%config(noreplace) %_K5xdgconf/parley*.knsrc
%_K5bin/parley
%_K5data/parley/
%_K5xmlgui/parley/
%_K5xdgapp/org.kde.parley.desktop
%_K5icon/*/*/apps/parley.*
%_K5icon/*/*/apps/parley-*.*
%_kf5_icon/oxygen/*/actions/*.*
%_K5cfg/documentsettings.kcfg
%_K5cfg/languagesettings.kcfg
%_K5cfg/parley.kcfg

%changelog
* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Wed Nov 27 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Thu Aug 29 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Fri Jul 19 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Wed May 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Thu Mar 21 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Thu Feb 28 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Thu Jul 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
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

* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt2
- fix requires

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
