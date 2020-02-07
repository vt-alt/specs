%define rname minuet
%define minuet_sover 0.3.0
%define libminuetinterfaces libminuetinterfaces%minuet_sover

Name: kde5-%rname
Version: 19.12.1
Release: alt1
%K5init

Group: Education
Summary: Music Education Software
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch: alt-clean-bindir.patch

# Automatically added by buildreq on Thu May 26 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libalsa-devel libdrumstick-alsa1 libdrumstick-file1 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 xml-common xml-utils
#BuildRequires: drumstick-devel extra-cmake-modules kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel python-module-google python3-dev qt5-declarative-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-declarative-devel qt5-quickcontrols2-devel qt5-svg-devel
BuildRequires: drumstick-devel libalsa-devel libfluidsynth-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kio-devel
BuildRequires: kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel kf5-solid-devel

%description
Minuet is an application for music education. It features a set of ear training exercises regarding intervals, chords, scales and more.

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

%package -n %libminuetinterfaces
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libminuetinterfaces
KF5 library

%prep
%setup -n %rname-%version
%patch -p1

sed -i 's|^#set(FluidSynth_VERSION|set(FluidSynth_VERSION|' cmake/FindFluidSynth.cmake

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%K5install_move data minuet
%find_lang %name --with-kde --all-name

%files
%_K5bin/minuet
%_K5data/minuet/
%_K5icon/hicolor/*/apps/minuet.*
%_K5icon/hicolor/*/actions/minuet-*.*
%_K5xdgapp/org.kde.minuet.desktop
%_K5plug/minuet/

%files common -f %name.lang
%doc COPYING*

%files -n %libminuetinterfaces
%_K5lib/libminuetinterfaces.so.*
%_K5lib/libminuetinterfaces.so.%minuet_sover

%files devel
%_K5link/libminuetinterfaces.so
%_K5inc/minuet/

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

* Fri Jan 18 2019 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt2
- rebuild with new fluidsynth

* Thu Jul 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Wed Jun 06 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt2%ubt
- update translations

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Fri Nov 17 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt2%ubt
- update translations

* Tue Nov 14 2017 Oleg Solovyov <mcpain@altlinux.org> 17.08.3-alt1%ubt
- update to 17.08.3

* Tue Nov 14 2017 Oleg Solovyov <mcpain@altlinux.org> 16.04.1-alt3
- fix requires

* Tue Sep 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 16.04.1-alt2
- Fixed build with new toolchain.

* Thu May 26 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- initial build
