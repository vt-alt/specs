%define rname krfb

%define sover 5
%define libkrfbprivate libkrfbprivate%sover

Name: kde5-%rname
Version: 19.08.2
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Desktop Sharing
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Jan 12 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ kf5-kdoctools-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbusmenu-qt52 libgpg-error libjson-c libp11-kit libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms libxkbfile-devel python-base python-modules python3 python3-base qt5-base-devel ruby ruby-stdlibs xml-common xml-utils xorg-inputproto-devel xorg-kbproto-devel xorg-xextproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: extra-cmake-modules kf5-kauth-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdnssd-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel kf5-knotifications-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel libvncserver-devel python-module-google qt5-x11extras-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-x11extras-devel
BuildRequires: libvncserver-devel libxcbutil-image-devel pipewire-libs-devel
BuildRequires: kf5-kauth-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdnssd-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel kf5-knotifications-devel kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-kwindowsystem-devel

%description
KDE Desktop Sharing (krfb) is a small server for the RFB protocol, better known as VNC.
Unlike most other Unix/Linux RFB servers, KRfb allows you to share your X11 session
instead of creating a new X11 session.

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

%package -n %libkrfbprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkrfbprivate
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data krfb
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files
%_K5bin/
%_K5plug/krfb/
%_K5xdgapp/org.kde.krfb.desktop
%_K5data/krfb/
%_K5srvtyp/krfb-*.desktop
%_K5icon/*/*/apps/krfb.*

#%files devel
#%_K5inc/krfb_version.h
#%_K5inc/krfb/
#%_K5link/lib*.so
#%_K5lib/cmake/krfb
#%_K5archdata/mkspecs/modules/qt_krfb.pri

%files -n %libkrfbprivate
%_K5lib/libkrfbprivate.so.%sover
%_K5lib/libkrfbprivate.so.*

%changelog
* Fri Oct 25 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.2-alt1
- new version

* Wed Sep 11 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt2
- build screencast plugin

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

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Tue May 22 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Mar 06 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Mon Nov 13 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Thu Mar 23 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Feb 09 2017 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt2%ubt
- fix compile with gcc6

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

* Tue Jan 12 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt2
- fix packaging

* Wed Sep 30 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- initial build
