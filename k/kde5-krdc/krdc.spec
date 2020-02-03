%define rname krdc

%define sover 5
%define libkrdccore libkrdccore%sover

Name: kde5-%rname
Version: 19.12.1
Release: alt1
%K5init

Group: Networking/Remote access
Summary: Remote Desktop Client
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: xfreerdp freerdp-plugins-standard

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Mar 30 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kdoctools-devel kf5-kwidgetsaddons-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libp11-kit libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils zlib-devel
#BuildRequires: extra-cmake-modules kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcompletion-devel kf5-kdelibs4support kf5-kdnssd-devel kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kiconthemes-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kservice-devel kf5-kwallet-devel kf5-kxmlgui-devel libvncserver-devel python-module-google python3-dev rpm-build-ruby xfreerdp
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: libvncserver-devel xfreerdp libssh-devel
BuildRequires: kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcompletion-devel kf5-kdelibs4support kf5-kdnssd-devel
BuildRequires: kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kiconthemes-devel kf5-knotifications-devel kf5-knotifyconfig-devel
BuildRequires: kf5-kservice-devel kf5-kwallet-devel kf5-kxmlgui-devel
BuildRequires: kf5-kwindowsystem-devel

%description
Remote Desktop Client.
is a client application that allows you to view or even control
the desktop session on another machine that is running a compatible server.
VNC and RDP is supported.

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

%package -n %libkrdccore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkrdccore
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%K5install_move data krdc 
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*

%files
%_K5bin/krdc
%_K5plug/krdc/
%_K5data/krdc/
%_K5xdgapp/org.kde.krdc.desktop
%_K5cfg/krdc.kcfg
%_K5srv/krdc_*.desktop
%_K5srv/rdp.protocol
%_K5srv/vnc.protocol
%_K5srv/ServiceMenus/smb2rdc.desktop
%_K5xmlgui/krdc/

%files devel
%_K5inc/krdccore_export.h
%_K5inc/krdc/
%_K5link/lib*.so

%files -n %libkrdccore
%_K5lib/libkrdccore.so.%sover
%_K5lib/libkrdccore.so.*

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

* Mon May 20 2019 Pavel Moseev <mars@altlinux.org> 19.04.0-alt2
- update translation

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

* Thu Mar 16 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- initial build
