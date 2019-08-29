%define rname rocs

%define rocsgraphtheory_sover 0
%define librocsgraphtheory librocsgraphtheory%rocsgraphtheory_sover

Name: kde5-%rname
Version: 19.08.0
Release: alt1
%K5init

Group: Education
Summary: Graph Theory
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Apr 01 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libgpg-error libgst-plugins1.0 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sensors libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libqt5-xmlpatterns libstdc++-devel libxcbutil-keysyms python-base python-modules python3 qt5-base-devel qt5-declarative-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: boost-devel-headers extra-cmake-modules grantlee5-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdeclarative-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kpackage-devel kf5-kparts-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel python-module-google python3-base qt5-script-devel qt5-svg-devel qt5-webkit-devel qt5-xmlpatterns-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: boost-devel extra-cmake-modules grantlee5-devel
BuildRequires: qt5-script-devel qt5-svg-devel qt5-webkit-devel qt5-xmlpatterns-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdeclarative-devel kf5-kdelibs4support
BuildRequires: kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-kpackage-devel kf5-kparts-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

%description
Rocs is a Graph Theory IDE for designing and analyzing graph algorithms.
It provides an easy to use visual editor for creating graphs, a scripting engine
to execute algorithms, and several helper tools for simulations and experiments.
Algorithms are specified in JavaScript.

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

%package -n %librocsgraphtheory
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %librocsgraphtheory
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%K5install_move data rocsgraphtheory rocs
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
#%_K5data/rocsgraphtheory/

%files
%_K5bin/
%_K5plug/rocs/
%_K5data/rocs/
%_K5icon/*/*/apps/rocs.*
%_K5icon/*/*/actions/rocs*.*
%_K5xdgapp/org.kde.rocs.desktop
%_K5cfg/rocs.kcfg
%_K5xmlgui/rocs/

%files devel
%_K5inc/rocs/
%_K5link/lib*.so

%files -n %librocsgraphtheory
%_K5lib/librocsgraphtheory.so.%rocsgraphtheory_sover
%_K5lib/librocsgraphtheory.so.*

%changelog
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

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
