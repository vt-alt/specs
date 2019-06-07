%define rname okular
%def_enable msits
%def_enable mobile

%define sover 9
%define libokularcore libokular5core%sover

Name: kde5-%rname
Version: 19.04.1
Release: alt1
%K5init

Group: Office
Summary: Document Viewer
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: %name-core = %EVR

Source: %rname-%version.tar
Patch1: alt-chm-encoding.patch
Patch2: alt-def-memory-level.patch

# Automatically added by buildreq on Tue Jan 19 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ gtk-update-icon-cache kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libfreetype-devel libgpg-error libjson-c libpoppler1-qt5 libqca-qt5 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms pkg-config python-base python-modules python3 python3-base qt5-base-devel ruby ruby-stdlibs xml-common xml-utils xz zlib-devel
#BuildRequires: ebook-tools-devel extra-cmake-modules kde5-libkexiv2-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjs-devel kf5-knotifications-devel kf5-kparts-devel kf5-kpty-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-libkscreen-devel kf5-solid-devel kf5-sonnet-devel kf5-threadweaver-devel libchm-devel libdjvu-devel libjpeg-devel libpoppler-qt5-devel libqca-qt5-devel libspectre-devel libtiff-devel python-module-google qt5-declarative-devel qt5-phonon-devel qt5-svg-devel rpm-build-python3 rpm-build-ruby zlib-devel-static
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-declarative-devel qt5-phonon-devel qt5-svg-devel
BuildRequires: qt5-speech-devel
BuildRequires: zlib-devel libdiscount-devel
BuildRequires: ebook-tools-devel libdjvu-devel libjpeg-devel libpoppler-qt5-devel libqca-qt5-devel libspectre-devel libtiff-devel
BuildRequires: kde5-libkexiv2-devel
BuildRequires: plasma5-libkscreen-devel
#BuildRequires: kf5-purpose-devel
BuildRequires: kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel
BuildRequires: kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kguiaddons-devel kf5-khtml-devel
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-kjs-devel kf5-knotifications-devel kf5-kparts-devel kf5-kpty-devel kf5-kservice-devel kf5-ktextwidgets-devel
BuildRequires: kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel
BuildRequires: kf5-solid-devel kf5-sonnet-devel kf5-threadweaver-devel
BuildRequires: qt5-quickcontrols2-devel kf5-kirigami-devel
%if_enabled msits
BuildRequires: libchm-devel libzip-devel
%endif

%description
Document viewer; support different kinds of documents.

%package mobile
Summary: Mobile Document Viewer
Group: Office
Requires: %name-core = %EVR
Requires: kf5-kdeclarative kf5-kirigami
%description mobile
Document viewer; support different kinds of documents.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package core
Summary: Core files for %name
Group: Graphical desktop/KDE
Requires: %name-common = %EVR
%description core
Core files for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libokularcore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %EVR
%description -n %libokularcore
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
sed -i '/^add_subdirectory.*ooo/d' generators/CMakeLists.txt

%build
%K5build \
    -DLIBZIP_INCLUDE_DIR=%_includedir/libzip \
    -DINCLUDE_INSTALL_DIR=%_K5inc \
    -Ddiscount_INCLUDE_DIR=%_includedir \
    -Ddiscount_LIBRARIES=%_libdir/libmarkdown.so \
    -Ddiscount_FOUND:BOOL=TRUE \
    #

%install
%K5install
%K5install_move data okular kpackage kconf_update
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_K5xdgconf/okular.categories
%_K5srvtyp/*.desktop
%_K5icon/hicolor/*/apps/okular.*

%files
%_K5bin/okular
%_K5xmlgui/okular/
%_K5xdgapp/org.kde.okular.desktop
%_K5xdgapp/okularApplication_*.desktop

%if_enabled mobile
%files mobile
%_K5bin/okularkirigami
%_K5xdgapp/org.kde.okular.kirigami.desktop
%_K5xdgapp/org.kde.mobile.okular_*.desktop
%else
%exclude %_K5data/kpackage/genericqml/org.kde.mobile.okular/
%exclude %_K5xdgapp/org.kde.mobile.okular.desktop
%exclude %_K5xdgapp/org.kde.mobile.okular_*.desktop
%endif

%files core
%_K5data/okular/
%_K5qml/org/kde/okular/
%_K5plug/okular/
%_K5plug/okularpart.so
%_K5srv/okular*.desktop
%_K5conf_up/okular*
%_K5cfg/*okular*
%_K5cfg/*settings*
%if_enabled msits
%_K5plug/kio_msits.so
%_K5srv/ms-its.protocol
%endif

%files devel
%_K5inc/okular/
%_K5link/lib*.so
%_K5lib/cmake/Okular5/

%files -n %libokularcore
%_K5lib/libOkular5Core.so.%sover
%_K5lib/libOkular5Core.so.*

%changelog
* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Mon May 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Tue Feb 19 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Mon Nov 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt3
- build without purpose

* Fri Sep 21 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt2%ubt
- use low memory usage level profile by default (ALT#35091)

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Wed May 30 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt2%ubt
- update build requires

* Tue May 22 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Thu Mar 22 2018 Oleg Solovyov <mcpain@altlinux.org> 17.12.3-alt2%ubt
- apply CHM patch

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Mar 06 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Thu Dec 28 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt2%ubt
- exclude internal ooo generator

* Mon Nov 13 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Wed Aug 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt2%ubt
- fix CHM default encoding

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Thu Mar 23 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Wed Feb 08 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.1-alt1%ubt
- new version

* Wed Nov 23 2016 Sergey V Turchin <zerg@altlinux.org> 16.11.80-alt0.M80P.1
- build for M80P

* Wed Nov 23 2016 Sergey V Turchin <zerg@altlinux.org> 16.11.80-alt1
- new beta

* Thu Nov 10 2016 Sergey V Turchin <zerg@altlinux.org> 16.11.60-alt0.M80P.2
- build for M80P

* Thu Nov 10 2016 Sergey V Turchin <zerg@altlinux.org> 16.11.60-alt1
- 16.12 beta

* Tue Aug 30 2016 Sergey V Turchin <zerg@altlinux.org> 4.90.0-alt5
- update from frameworks branch

* Thu Aug 04 2016 Sergey V Turchin <zerg@altlinux.org> 4.90.0-alt4
- update from frameworks branch

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 4.90.0-alt3
- fix package

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 4.90.0-alt2
- update from frameworks branch

* Mon Mar 14 2016 Sergey V Turchin <zerg@altlinux.org> 4.90.0-alt1
- initial build
