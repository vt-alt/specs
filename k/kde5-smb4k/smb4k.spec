
%define sover 6
%define libsmb4kcore libsmb4kcore%sover

%define rname smb4k
Name: kde5-%rname
Version: 3.0.6
Release: alt1
%K5init altplace

Group: Networking/Other
Summary: A KDE SMB/CIFS share browser
License: GPLv2+
Url: http://smb4k.sourceforge.net/

Requires: samba-client cifs-utils
Requires: %libsmb4kcore = %version-%release

Source: %name-%version.tar

# Automatically added by buildreq on Fri Mar 10 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kdoctools-devel kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-declarative-devel
BuildRequires: libsmbclient-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-kiconthemes-devel kf5-kio-devel
BuildRequires: kf5-knotifications-devel kf5-kpackage-devel kf5-kparts-devel kf5-ktextwidgets-devel kf5-kwallet-devel
BuildRequires: kf5-kwindowsystem-devel kf5-plasma-framework-devel kf5-kcrash-devel

%description
Smb4K is an SMB/CIFS share browser for KDE. It uses the Samba software suite to
access the SMB/CIFS shares of the local network neighborhood. Its purpose is to
provide a program that's easy to use and has as many features as possible.


%package -n %libsmb4kcore
Summary: %name core library
Group: System/Libraries
%description -n %libsmb4kcore
%name core library

%package devel
Summary: Developemnt files for %name
Group: Development/KDE and QT
%description devel
Developemnt files for %name


%prep
%setup -q

rm -rf po/*/docs

%build
%K5build

%install
%K5install
%K5install_move data kconf_update
%find_lang %name --with-kde --all-name

%files -f %name.lang
%_K5bin/*
%_K5plug/*.so
%_K5libexecdir/kauth/mounthelper
%_K5qml/org/kde/smb4k/smb4kqmlplugin/
%_K5conf_up/*
%_K5xdgapp/org.kde.smb4k.desktop
%_K5data/plasma/plasmoids/org.kde.smb4kqml/
%_K5cfg/smb4k.kcfg
%_K5icon/*/*/apps/*.*
#%_K5conf_dbus_sysd/org.kde.smb4k.mounthelper.conf
%_K5dbus/system.d/org.kde.smb4k.mounthelper.conf
%_K5dbus_sys_srv/org.kde.smb4k.mounthelper.service
%_K5xmlgui/smb4k/
%_K5notif/smb4k.*
%_K5srv/*smb4k*.desktop
%_datadir/polkit-1/actions/org.kde.smb4k.mounthelper.policy

%files -n %libsmb4kcore
%_K5lib/libsmb4kcore.so.%sover
%_K5lib/libsmb4kcore.so.%sover.*

%changelog
* Fri Jul 24 2020 Sergey V Turchin <zerg@altlinux.org> 3.0.6-alt1
- new version

* Wed Jun 19 2019 Sergey V Turchin <zerg@altlinux.org> 3.0.1-alt1
- new version

* Fri Mar 22 2019 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt1
- new version

* Fri May 19 2017 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt1%ubt
- security fixes: CVE-2017-8849

* Fri May 05 2017 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt2%ubt
- fix polkit rule placement

* Wed Apr 05 2017 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt1%ubt
- 2.0.0 release

* Fri Mar 10 2017 Sergey V Turchin <zerg@altlinux.org> 1.9.90-alt1%ubt
- inittial build
