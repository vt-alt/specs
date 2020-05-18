%define rname liquidshell

%def_disable packagekit

%define liquidshell_sover 5
%define libliquidshell liquidshell%liquidshell_sover

Name: kde5-liquidshell
Version: 1.7.1
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE 5 plasma dekstop shell alternative
Url: https://cgit.kde.org/liquidshell.git/
License: GPLv3

Requires: plasma5-workspace
Requires: polkit-kde-plasma-desktop

Source: %rname-%version.tar
Patch2: alt-def-quicklaunch.patch
Patch3: alt-def-date-format.patch
Patch4: alt-panel-minimum-rows.patch
Patch5: alt-widgets-order.patch
Patch6: alt-def-wallpaper.patch
Patch7: alt-clean-device-notifier.patch
Patch8: alt-start-menu-icon.patch
Patch9: alt-start_liquidshell.patch

# Automatically added by buildreq on Sat Jun 09 2018 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgio-devel libgpg-error libnm-devel libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3
#BuildRequires: extra-cmake-modules git-core gtk-update-icon-cache kf5-bluez-qt-devel kf5-karchive-devel kf5-kcmutils-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kwindowsystem-devel kf5-networkmanager-qt-devel libssl-devel python3-dev qt5-x11extras-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-x11extras-devel
BuildRequires: kf5-bluez-qt-devel kf5-karchive-devel kf5-kcmutils-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-knewstuff-devel kf5-knotifications-devel
BuildRequires: kf5-kwindowsystem-devel kf5-networkmanager-qt-devel
%if_enabled packagekit
BuildRequires: appstream-qt-devel packagekit-qt-devel
%endif

%description
Alternative desktop replacement for Plasma, using QtWidgets instead of QtQuick to ensure hardware acceleration is not required.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Provides: kf5-plasma-desktop-common = %EVR
Obsoletes: kf5-plasma-desktop-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Provides: kf5-plasma-desktop-devel = %EVR
Obsoletes: kf5-plasma-desktop-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n polkit-kde-plasma-desktop
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name-common = %version-%release
Provides: polkit-kde-kfontinst
Provides: polkit-kde-kcmclock
%description -n polkit-kde-plasma-desktop
Common polkit files for %name

%package -n %libliquidshell
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libliquidshell
%name library

%prep
%setup -n %rname-%version
%patch2 -p1
%patch3 -p1
#%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1 -b .start

%build
%K5build

%install
%K5install

#K5install_move data doc

# install session
mkdir -p %buildroot/%_x11sysconfdir/wmsession.d/
cat <<__EOF__ >%buildroot/%_x11sysconfdir/wmsession.d/02LIQUIDSHELL
NAME=Liquidshell
DESC=Liquid Desktop Workspace
ICON=/usr/share/kf5/icons/hicolor/48x48/apps/liquidshell.png
EXEC=/usr/bin/start_liquidshell
SCRIPT:
exec /usr/bin/start_liquidshell
__EOF__
install -Dm 0755 org.kde.liquidshell.desktop %buildroot/%_kf5_xdgapp/
install -Dm 0644 liquidshell-session.desktop %buildroot/%_datadir/xsessions/liquidshell-session.desktop
mkdir -p %buildroot/%_bindir/
mv %buildroot/%_K5bin/start_liquidshell %buildroot/%_bindir/

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc README stylesheet.css
%_K5bin/liquidshell
%_K5icon/*/*/apps/liquidshell.*
%_K5xdgapp/*liquidshell*.desktop
%_K5notif/*liquidshell*
%_x11sysconfdir/wmsession.d/02LIQUIDSHELL
%_bindir/start_liquidshell
%_datadir/xsessions/liquidshell-session.desktop

%changelog
* Fri May 15 2020 Sergey V Turchin <zerg@altlinux.org> 1.7.1-alt1
- new version

* Thu Nov 28 2019 Sergey V Turchin <zerg@altlinux.org> 1.5-alt5
- allow configure virtual desktops (Closes: 37527)

* Thu Nov 28 2019 Sergey V Turchin <zerg@altlinux.org> 1.5-alt4
- add upstream fix to reduce minimum panel height

* Tue Nov 26 2019 Sergey V Turchin <zerg@altlinux.org> 1.5-alt3
- add upstream fixes

* Fri Nov 22 2019 Sergey V Turchin <zerg@altlinux.org> 1.5-alt2
- allow configure virtual desktops (Closes: 37527)

* Mon Nov 18 2019 Sergey V Turchin <zerg@altlinux.org> 1.5-alt1
- new version

* Thu Apr 11 2019 Sergey V Turchin <zerg@altlinux.org> 1.4-alt4
- build without packagekit

* Mon Mar 11 2019 Sergey V Turchin <zerg@altlinux.org> 1.4-alt3
- update from master branch

* Mon Jan 28 2019 Sergey V Turchin <zerg@altlinux.org> 1.4-alt2
- update from master branch
- build with packagekit
- install xsession

* Thu Nov 08 2018 Sergey V Turchin <zerg@altlinux.org> 1.4-alt1
- new version

* Tue Aug 21 2018 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt3%ubt
- update from master branch

* Wed Jun 13 2018 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt2%ubt
- set default wallpaper
- set start menu icon

* Sat Jun 09 2018 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1%ubt
- initial build
