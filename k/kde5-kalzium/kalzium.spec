%define rname kalzium

%def_disable avogadro
%def_disable facile

%define sover 5
%define libscience libscience%sover

Name: kde5-%rname
Version: 19.12.1
Release: alt1
%K5init

Group: Education
Summary: Periodic system of the elements
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

%if_enabled avogadro
Requires: avogadro
%endif
Requires: chemical-mime-data

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Apr 04 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-attica-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms ocaml4 perl pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: eigen3 extra-cmake-modules facile kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-khtml-devel kf5-kio-devel kf5-kjs-devel kf5-knewstuff-devel kf5-kplotting-devel libopenbabel-devel llvm-devel openbabel python-module-google python3-dev qt5-declarative-devel qt5-script-devel qt5-svg-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-declarative-devel qt5-script-devel qt5-svg-devel
BuildRequires: eigen3 ocaml
BuildRequires: libopenbabel-devel llvm-devel openbabel
%if_enabled avogadro
BuildRequires: libopenbabel-devel openbabel avogadro-devel
%endif
%if_enabled facile
BuildRequires: facile
%endif
BuildRequires: kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-khtml-devel kf5-kio-devel kf5-kjs-devel kf5-knewstuff-devel kf5-kplotting-devel

%description
Kalzium is an application which will show you some information about the
periodic system of the elements. Therefore you could use it as an
information database.

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

%package -n %libscience
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libscience
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%K5install_move data kalzium libkdeedu
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%config(noreplace) %_K5xdgconf/*kalzium*

%files
%_K5bin/kalzium
%_K5data/kalzium/
%_K5xdgapp/*kalzium*.desktop
%_K5cfg/*kalzium*
%_K5data/libkdeedu/data/*
%_K5icon/*/*/apps/kalzium.*
%_K5xmlgui/kalzium/

%files devel
%_K5inc/libkdeedu/*.h
%_K5link/lib*.so

%files -n %libscience
%_K5lib/libscience.so.%sover
%_K5lib/libscience.so.*

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

* Thu Mar 16 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- initial build
