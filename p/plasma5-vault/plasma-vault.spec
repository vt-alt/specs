%define rname plasma-vault

Name: plasma5-vault
Version: 5.16.5
Release: alt1
Epoch: 1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Encrypted vaults support for KDE
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: fuse
#Requires: fuse-encfs >= 1.9.1
#Requires: fuse-cryfs >= 0.9.6

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Dec 26 2017 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules qt5-base-common qt5-base-devel rpm-build-qml
#BuildRequires: extra-cmake-modules kf5-kactivities-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kpackage-devel kf5-libksysguard-devel kf5-plasma-framework-devel libssl-devel qt5-declarative-devel
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: qt5-declarative-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kactivities-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel
BuildRequires: kf5-kpackage-devel plasma5-libksysguard-devel kf5-plasma-framework-devel
BuildRequires: kf5-networkmanager-qt-devel

Provides: kf5-plasma-vault = %EVR
Obsoletes: kf5-plasma-vault < %EVR

%description
%name provides encrypted vaults.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Provides: kf5-plasma-vault-common = %EVR
Obsoletes: kf5-plasma-vault-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Provides: kf5-plasma-vault-devel = %EVR
Obsoletes: kf5-plasma-vault-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5plasma-vault
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n libkf5plasma-vault
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --all-name

%files -f %name.lang
%doc COPYING*
%_K5plug/kf5/kfileitemaction/*.so
%_K5plug/kf5/kded/*vault*.so
%_K5plug/plasma/applets/*vault*.so
%_K5data/plasma/plasmoids/*vault*/
%_K5srv/*vault*.desktop

%changelog
* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.5-alt1
- new version

* Thu Aug 01 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.4-alt1
- new version

* Thu Jul 11 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.3-alt1
- new version

* Wed Jun 26 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.2-alt1
- new version

* Tue Jun 18 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.1-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.15.5-alt2
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.15.5-alt1
- new version

* Wed Apr 24 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.15.4-alt1
- new version

* Tue Mar 05 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.12.8-alt1
- new version

* Thu Sep 27 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.12.7-alt1
- new version

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.12.6-alt2%ubt
- fix version

* Tue Jul 03 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt2%ubt
- update russian translation

* Wed Jun 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1%ubt
- new version

* Thu May 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1%ubt
- new version

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1%ubt
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1%ubt
- new version

* Thu Mar 01 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1%ubt
- new version

* Mon Feb 19 2018 Maxim Voronov <mvoronov@altlinux.org> 5.12.0-alt2%ubt
- renamed kf5-plasma-vault -> plasma5-vault

* Wed Feb 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1%ubt
- new version

* Thu Jan 11 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt1%ubt
- new version

* Tue Dec 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.4-alt1%ubt
- initial build
