%define rname plasma-nm
%def_disable openswan

Name: plasma5-nm
Version: 5.18.1
Release: alt1
Epoch: 1
%K5init altplace no_appdata

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 Plasma applet written in QML for managing network connections
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: NetworkManager-daemon
Requires: NetworkManager-adsl NetworkManager-wifi
Requires: mobile-broadband-provider-info
Requires: qca-qt5-ossl
#Requires: wireguard-tools

Provides: kf5-plasma-nm = %EVR
Obsoletes: kf5-plasma-nm < %EVR

Source: %rname-%version.tar
Source1: plasmanetworkmanagement-kded.po
Source10: 01-plasma-nm.js
# ALT
Patch11: alt-old-openconnectauth.patch
Patch12: alt-def-allow-all.patch
Patch13: alt-explain-password-request.patch

# Automatically added by buildreq on Tue Mar 03 2015 (-bi)
# optimized out: cmake cmake-modules elfutils glib2-devel kf5-kdoctools-devel libEGL-devel libGL-devel libcloog-isl4 libgio-devel libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms pkg-config python-base qt5-base-devel ruby ruby-stdlibs
#BuildRequires: ModemManager-devel extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kpackage-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-libmm-qt-devel kf5-networkmanager-qt-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel libnm-devel libopenconnect-devel python-module-google qt5-declarative-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt5-declarative-devel qt5-tools-devel-static
BuildRequires: mobile-broadband-provider-info libqca-qt5-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdeclarative-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel
BuildRequires: kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-knotifications-devel kf5-kpackage-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel
BuildRequires: kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel kf5-plasma-framework-devel
BuildRequires: kf5-solid-devel kf5-sonnet-devel
BuildRequires: ModemManager-devel libopenconnect-devel
BuildRequires: libnm-devel
BuildRequires: kf5-modemmanager-qt-devel kf5-networkmanager-qt-devel

%description
Plasma applet and editor for managing your network connections in KDE using
the default NetworkManager service.

%package maxi
Group: Graphical desktop/KDE
Summary: Mobile support for %name
BuildArch: noarch
Requires: %name
Requires: %name-connect-mobile
Requires: %name-connect-openvpn
Requires: %name-connect-fortisslvpn
Requires: %name-connect-vpnc
Requires: %name-connect-openconnect
Requires: %name-connect-openswan
Requires: %name-connect-strongswan
Requires: %name-connect-iodine
Requires: %name-connect-l2tp
Requires: %name-connect-pptp
Requires: %name-connect-sstp
Requires: %name-connect-ssh
Provides: kf5-plasma-nm-maxi = %EVR
Obsoletes: kf5-plasma-nm-maxi < %EVR
%description maxi
%summary.

%package connect-mobile
Group: Graphical desktop/KDE
Summary: Mobile support for %name
BuildArch: noarch
Requires: %name
Requires: ModemManager NetworkManager-bluetooth NetworkManager-wwan mobile-broadband-provider-info
Provides: kf5-plasma-nm-connect-mobile = %EVR
Obsoletes: kf5-plasma-nm-connect-mobile < %EVR
%description connect-mobile
%summary.

%package connect-openvpn
Group: Graphical desktop/KDE
Summary: OpenVPN support for %name
Requires: %name
Requires: NetworkManager-openvpn
Provides: kf5-plasma-nm-connect-openvpn = %EVR
Obsoletes: kf5-plasma-nm-connect-openvpn < %EVR
%description connect-openvpn
%summary.

%package connect-fortisslvpn
Group: Graphical desktop/KDE
Summary: Fortinet SSLVPN support for %name
Requires: %name
Provides: kf5-plasma-nm-connect-fortisslvpn = %EVR
Obsoletes: kf5-plasma-nm-connect-fortisslvpn < %EVR
%description connect-fortisslvpn
%summary.

%package connect-vpnc
Group: Graphical desktop/KDE
Summary: Vpnc support for %name
Requires: %name
Requires: NetworkManager-vpnc
Provides: kf5-plasma-nm-connect-vpnc = %EVR
Obsoletes: kf5-plasma-nm-connect-vpnc < %EVR
%description connect-vpnc
%summary.

%package connect-openconnect
Group: Graphical desktop/KDE
Summary: OpenConnect support for %name
Requires: %name
Requires: NetworkManager-openconnect
Provides: kf5-plasma-nm-connect-openconnect = %EVR
Obsoletes: kf5-plasma-nm-connect-openconnect < %EVR
%description connect-openconnect
%summary.

%package connect-iodine
Group: Graphical desktop/KDE
Summary: Iodine DNS tunnel support for %name
Requires: %name
Requires: NetworkManager-iodine
Provides: kf5-plasma-nm-connect-iodine = %EVR
Obsoletes: kf5-plasma-nm-connect-iodine < %EVR
%description connect-iodine
%summary.

%package connect-openswan
Group: Graphical desktop/KDE
Summary: Openswan support for %name
Requires: %name
%if_enabled openswan
Requires: NetworkManager-openswan
%endif
Provides: kf5-plasma-nm-connect-openswan = %EVR
Obsoletes: kf5-plasma-nm-connect-openswan < %EVR
%description connect-openswan
%summary.

%package connect-strongswan
Group: Graphical desktop/KDE
Summary: Strongswan support for %name
Requires: %name
Requires: strongswan
Provides: kf5-plasma-nm-connect-strongswan = %EVR
Obsoletes: kf5-plasma-nm-connect-strongswan < %EVR
%description connect-strongswan
%summary.

%package connect-l2tp
Group: Graphical desktop/KDE
Summary: L2TP support for %name
Requires: %name
Requires: NetworkManager-l2tp
Provides: kf5-plasma-nm-connect-l2tp = %EVR
Obsoletes: kf5-plasma-nm-connect-l2tp < %EVR
%description connect-l2tp
%summary.

%package connect-pptp
Group: Graphical desktop/KDE
Summary: PPTP support for %name
Requires: %name
Requires: NetworkManager-pptp
Provides: kf5-plasma-nm-connect-pptp = %EVR
Obsoletes: kf5-plasma-nm-connect-pptp < %EVR
%description connect-pptp
%summary.

%package connect-sstp
Group: Graphical desktop/KDE
Summary: SSTP support for %name
Requires: %name
Requires: NetworkManager-sstp
Provides: kf5-plasma-nm-connect-sstp = %EVR
Obsoletes: kf5-plasma-nm-connect-sstp < %EVR
%description connect-sstp
%summary.

%package connect-ssh
Group: Graphical desktop/KDE
Summary: SSH support for %name
Requires: %name
Requires: NetworkManager-ssh
Provides: kf5-plasma-nm-connect-ssh = %EVR
Obsoletes: kf5-plasma-nm-connect-ssh < %EVR
%description connect-ssh
%summary.

%prep
%setup -n %rname-%version
%patch11 -p1
%patch12 -p1
%patch13 -p1

cat %SOURCE1 >> po/ru/plasmanetworkmanagement-kded.po

%build
%K5build

%install
%K5install
%K5install_move data kcm_networkmanagement

install -m0644 -p -D %SOURCE10 %buildroot/%_K5data/plasma/updates/01-plasma-nm.js

%find_lang %name --all-name

%files -f %name.lang
%doc COPYING*
#%_K5bin/kde5-nm-connection-editor
%_K5lib/libplasmanm_*.so
%_K5plug/kf5/kded/networkmanagement.so
%_K5plug/kcm_networkmanagement.so
%_K5qml/org/kde/plasma/networkmanagement/
#%_K5xdgapp/kde5-nm-connection-editor.desktop
%_K5data/kcm_networkmanagement/
%_K5data/plasma/plasmoids/org.kde.plasma.networkmanagement/
%_K5data/plasma/updates/*
%_K5notif/networkmanagement.notifyrc
%_K5srv/kcm_networkmanagement.desktop
%_K5srv/plasma-applet-org.kde.plasma.networkmanagement.desktop
%_K5srvtyp/*networkmanagement*.desktop
#%_K5xmlgui/kde5-nm-connection-editor/

%files maxi
%files connect-mobile

%files connect-iodine
%_K5plug/libplasmanetworkmanagement_iodineui.so
%_K5srv/plasmanetworkmanagement_iodineui.desktop

%files connect-openvpn
%_K5plug/libplasmanetworkmanagement_openvpnui.so
%_K5srv/plasmanetworkmanagement_openvpnui.desktop

%files connect-fortisslvpn
%_K5plug/libplasmanetworkmanagement_fortisslvpnui.so
%_K5srv/plasmanetworkmanagement_fortisslvpnui.desktop

%files connect-vpnc
%_K5plug/libplasmanetworkmanagement_vpncui.so
%_K5srv/plasmanetworkmanagement_vpncui.desktop

%files connect-openconnect
%_K5plug/libplasmanetworkmanagement_openconnectui.so
%_K5srv/plasmanetworkmanagement_openconnect*.desktop

%files connect-openswan
%_K5plug/libplasmanetworkmanagement_openswanui.so
%_K5srv/plasmanetworkmanagement_openswanui.desktop

%files connect-strongswan
%_K5plug/libplasmanetworkmanagement_strongswanui.so
%_K5srv/plasmanetworkmanagement_strongswanui.desktop

%files connect-l2tp
%_K5plug/libplasmanetworkmanagement_l2tpui.so
%_K5srv/plasmanetworkmanagement_l2tpui.desktop

%files connect-pptp
%_K5plug/libplasmanetworkmanagement_pptpui.so
%_K5srv/plasmanetworkmanagement_pptpui.desktop

%files connect-sstp
%_K5plug/libplasmanetworkmanagement_sstpui.so
%_K5srv/plasmanetworkmanagement_sstpui.desktop

%files connect-ssh
%_K5plug/libplasmanetworkmanagement_sshui.so
%_K5srv/plasmanetworkmanagement_sshui.desktop

%changelog
* Wed Feb 19 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.1-alt1
- new version

* Thu Jan 09 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.17.5-alt1
- new version

* Thu Dec 05 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.4-alt1
- new version

* Wed Nov 13 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.3-alt1
- new version

* Fri Nov 01 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.2-alt1
- new version

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.1-alt1
- new version

* Thu Oct 17 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.0-alt1
- new version

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

* Tue May 07 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.15.4-alt2
- password dialog: validate wireless keys

* Thu Apr 25 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.15.4-alt1
- new version

* Thu Apr 25 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.8-alt5
- applet: fix disappearing wireless connections

* Thu Apr 04 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.8-alt4
- fix package

* Thu Apr 04 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.8-alt3
- fix package

* Wed Apr 03 2019 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.8-alt2
- password dialog: explain why password is requested

* Tue Mar 05 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.12.8-alt1
- new version

* Thu Dec 20 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.12.7-alt2
- fix to build with networkmanager

* Thu Sep 27 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.12.7-alt1
- new version

* Wed Aug 08 2018 Ivan Razzhivin <underwit@altlinux.org> 1:5.12.6-alt3%ubt
- fix a text label in the password dialog

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
- renamed kf5-plasma-nm -> plasma5-nm

* Wed Feb 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1%ubt
- new version

* Wed Jan 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt1%ubt
- new version

* Mon Dec 11 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.4-alt1%ubt
- new version

* Mon Dec 04 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt2%ubt
- store passwords for all users by default

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1%ubt
- new version

* Tue Nov 07 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Mon Sep 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt1%ubt
- new version

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.3-alt1%ubt
- new version

* Wed Apr 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Tue Apr 18 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt2%ubt
- fix compile with old openconnect

* Mon Apr 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.1-alt1%ubt
- new version

* Fri Dec 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt1%ubt
- new version

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt0.M80P.1
- build for M80P

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt1
- new version

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt0.M80P.1
- build for M80P

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1
- new version

* Tue Oct 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt0.M80P.1
- build for M80P

* Fri Oct 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt1
- new version

* Mon Oct 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1.M80P.1
- build for M80P

* Mon Oct 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt2
- rebuild with new openconnect

* Tue Oct 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Tue Aug 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt1
- new version

* Mon Aug 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.3-alt1
- new version

* Tue Jul 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.2-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1
- new version

* Wed Jul 06 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt1
- new version

* Wed Jun 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.5-alt1
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.4-alt1
- new version

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.3-alt1
- new version

* Wed Mar 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.5-alt1
- new version

* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- new version

* Thu Jan 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt1
- new version

* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt1
- new version

* Thu Dec 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Thu Nov 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt3
- rebuild

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt1
- new version

* Wed Oct 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Wed Aug 26 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Sat Aug 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.95-alt1
- new version

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.1
- test

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
