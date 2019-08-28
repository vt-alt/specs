
%def_disable qtkeychain

%define rname kio-gdrive
%define sover 16
%define libktcore libktcore%sover

Name: kde5-%rname
Version: 1.2.5
Release: alt2
%K5init

Group:     Networking/File transfer
Summary:   KIO-client for Google Drive
License:   GPLv2 / GPLv3
URL:       https://cgit.kde.org/kio-gdrive.git/

Source: %rname-%version.tar
Source10: kio5_gdrive_ru.po
# upstream
Patch1: 0001-Adapt-to-LibKGAPI-setFields-changes.patch
Patch2: 0002-Port-away-from-deprecated-insert.patch
Patch3: 0003-Remove-useless-FileFetchJob.patch

BuildRequires(pre): rpm-build-kf5

# Automatically added by buildreq on Mon Nov 07 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ kde5-kcalcore-devel kde5-kcontacts-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libgpg-error libgst-plugins1.0 libical-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-sensors libqt5-sql libqt5-svg libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel kf5-libkgapi-devel libqtkeychain-qt5-devel python-module-google python3-dev rpm-build-ruby
BuildRequires(pre): rpm-build-ubt
BuildRequires: extra-cmake-modules
%if_enabled qtkeychain
BuildRequires: libqtkeychain-qt5-devel
%else
BuildRequires: intltool signon-devel accounts-qt5-devel kde5-kaccounts-integration-devel
%endif
BuildRequires: kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel kf5-libkgapi-devel

%description
Now you are ready to use the slave. Either click on "Google Drive File Manager"
in the application launcher (which will open Dolphin with the `gdrive:/` URL) or run:
    $ kioclient5 exec gdrive:/

%prep
%setup -q -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
cat %SOURCE10 >po/ru/kio5_gdrive.po

%build
%K5build

%install
%K5install
%K5install_move data remoteview
%find_lang --with-kde --all-name %rname

%files -f %rname.lang
%_K5data/remoteview/*drive*.desktop
%_K5plug/kf5/kio/*drive*.so
%if_enabled qtkeychain
%else
%_K5plug/kaccounts/daemonplugins/*drive*.so
%_datadir/accounts/services/kde/*drive*.service
%_K5notif/*drive*.notifyrc
%endif

%changelog
* Wed Aug 21 2019 Sergey V Turchin <zerg@altlinux.org> 1.2.5-alt2
- fix compile with new libkgapi

* Tue Dec 04 2018 Sergey V Turchin <zerg@altlinux.org> 1.2.5-alt1
- new version

* Tue May 08 2018 Sergey V Turchin <zerg@altlinux.org> 1.2.3-alt1%ubt
- new version

* Thu Apr 12 2018 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt1%ubt
- new version

* Tue Mar 06 2018 Sergey V Turchin <zerg@altlinux.org> 1.2.1-alt1%ubt
- new version

* Fri Jun 23 2017 Sergey V Turchin <zerg@altlinux.org> 1.2.0.1-alt3%ubt
- build with kaccounts again

* Wed Jun 21 2017 Sergey V Turchin <zerg@altlinux.org> 1.2.0.1-alt2%ubt
- build without kaccounts and with qtkeychain

* Mon Jun 19 2017 Sergey V Turchin <zerg@altlinux.org> 1.2.0.1-alt1%ubt
- new version

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 1.1.1-alt2%ubt
- rebuild with new libkgapi

* Thu Mar 23 2017 Sergey V Turchin <zerg@altlinux.org> 1.1.1-alt1%ubt
- new version

* Mon Jan 09 2017 Sergey V Turchin <zerg@altlinux.org> 1.0.4-alt1%ubt
- new version

* Mon Nov 07 2016 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt0.M80P.1
- build for M80P

* Wed Nov 02 2016 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt1
- initial build
