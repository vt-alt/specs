%define rname plasma-desktop

%define kfontinst_sover 5
%define libkfontinst libkfontinst%kfontinst_sover
%define kfontinstui_sover 5
%define libkfontinstui libkfontinstui%kfontinstui_sover


Name: plasma5-desktop
Version: 5.18.5
Release: alt2
%K5init altplace no_appdata

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 plasma desktop view furniture
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: plasma5-workspace
Requires: polkit-kde-plasma-desktop
# for ibus-ui-emojier-plasma
Requires: ibus-dicts

Source: %rname-%version.tar
Patch1: alt-def-font.patch
Patch2: alt-menu-icon.patch
Patch3: alt-def-apps-menu.patch
Patch4: alt-def-kicker.patch
Patch5: alt-multimedia-player-chooser.patch
Patch6: alt-def-panel.patch
Patch7: alt-def-desktop-containment.patch
Patch8: alt-def-desktop-widgets.patch
Patch10: alt-def-session.patch
Patch11: alt-def-key-numlock.patch
Patch12: alt-def-layout-indicator.patch
Patch13: alt-def-taskman.patch
#
Patch15: alt-menu-add-tooltip.patch
#
Patch17: alt-def-krunners.patch

# Automatically added by buildreq on Mon Mar 23 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glib2-devel glibc-devel-static kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libcloog-isl4 libdbusmenu-qt52 libfreetype-devel libgpg-error libjson-c libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-sql libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libusb-compat libxcb-devel libxcbutil-image libxcbutil-keysyms libxkbfile-devel mkfontscale pkg-config python-base qt5-base-devel rpm-build-gir ruby ruby-stdlibs xml-common xml-utils xorg-fixesproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-renderproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: boost-devel-headers extra-cmake-modules gcc-c++ iceauth kf5-baloo-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kpackage-devel kf5-kparts-devel kf5-krunner-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwin-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-libksysguard-devel kf5-plasma-framework-devel kf5-plasma-workspace-devel kf5-solid-devel kf5-sonnet-devel libGLU-devel libcanberra-devel libpulseaudio-devel libusb-compat-devel libxapian-devel libxcbutil-image-devel mkfontdir python-module-google qt5-declarative-devel qt5-phonon-devel qt5-svg-devel qt5-x11extras-devel rpm-build-ruby xset
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: boost-devel extra-cmake-modules gcc-c++
BuildRequires: qt5-declarative-devel qt5-phonon-devel qt5-svg-devel qt5-x11extras-devel
BuildRequires: scim-devel libibus-devel libgio-devel glib2-devel
BuildRequires: libudev-devel
BuildRequires: libGLU-devel libcanberra-devel libpulseaudio-devel libusb-compat-devel libxapian-devel
BuildRequires: libxcbutil-devel libxcbutil-image-devel libxkbcommon-devel
BuildRequires: xorg-drv-synaptics-devel xorg-sdk xorg-drv-evdev-devel xkeyboard-config-devel xorg-drv-libinput-devel
BuildRequires: iceauth mkfontdir xset
BuildRequires: kf5-baloo-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel
BuildRequires: kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kpackage-devel kf5-kparts-devel
BuildRequires: kf5-krunner-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel plasma5-kwin-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel plasma5-libksysguard-devel
BuildRequires: kf5-plasma-framework-devel plasma5-workspace-devel kf5-solid-devel kf5-sonnet-devel
BuildRequires: kf5-kdeclarative-devel kf5-kpeople-devel kf5-kactivities-stats-devel
BuildRequires: kf5-kded kf5-kded-devel plasma5-kscreenlocker-devel plasma5-breeze-devel

Provides: kf5-plasma-desktop = %EVR
Obsoletes: kf5-plasma-desktop < %EVR

%description
Plasma desktop view furniture.

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

%package -n %libkfontinst
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkfontinst
KF5 library

%package -n %libkfontinstui
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkfontinstui
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1
###%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
#%patch8 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
#
%patch15 -p1
#
%patch17 -p1

#Fix translate in Input Method Panel (kimpanel) widget.
#If the po-file is called differently than "plasma_applet_org.kde.plasma.kimpanel.po", the kimpanel widget menu will be in English only.
#find po/ -maxdepth 2 -name plasma_applet_org.kde.kimpanel.po -type f -exec rename plasma_applet_org.kde.kimpanel.po plasma_applet_org.kde.plasma.kimpanel.po '{}' \;

%build
%K5cmake \
    -DLIBEXEC_INSTALL_DIR=%_K5exec \
    -DCMAKE_BUILD_TYPE=Debug \
    #
%K5make

%install
%K5install

%K5install_move data color-schemes doc kcmmouse knsrcfiles kglobalaccel
%K5install_move data kcm_componentchooser kcminput kcmkeyboard kcmkeys kcm_phonon kcmsolidactions
%K5install_move data kconf_update kcontrol kdisplay kfontinst konqsidebartng ksmserver solid kpackage
%K5install_move data plasma/desktoptheme plasma/plasmoids/touchpad

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_datadir/locale/*/LC_SCRIPTS/kfontinst/
%_K5icon/*/*/*/*.*

%files
#%config(noreplace) %_K5xdgconf/*
%_K5dbus/system.d/*.conf
%_K5bin/*
%_K5exec/*
%_K5libexecdir/kauth/*
%_K5cf_bin/*
%_K5lib/libkdeinit5_*.so
%_K5plug/*.so
%_K5plug/kcms/*.so
%_K5plug/kf5/kded/*.so
%_K5plug/plasma/dataengine/*.so
%_K5qml/org/kde/plasma/private/*/
%_K5qml/org/kde/private/*/
%_K5qml/org/kde/plasma/activityswitcher/
%_K5qml/org/kde/activities/settings/
%_K5xdgapp/*
%_K5cfg/*
%_K5srv/ServiceMenus/*.desktop
%_K5srv/kded/*.desktop
%_K5srv/*.desktop
%_K5srv/*.protocol
%_K5srvtyp/*.desktop
%_K5xmlgui/*
%_K5notif/*
%_K5data/solid/devices/solid-*.desktop
#%_K5data/color-schemes/*
%_K5data/kcm*/
%_K5cf_upd/*
%_K5data/kactivitymanagerd/
%_K5data/kpackage/kcms/*
%_K5data/plasma/plasmoids/*
%_K5data/plasma/packages/*
%_K5data/plasma/layout-templates/*
%_K5data/plasma/shells/*/
%_K5data/plasma/services/*
%_K5data/plasma/desktoptheme/default/icons/*
%_K5data/kcontrol/
%_K5data/kcmmouse/
%_K5data/kdisplay/
%_K5data/kglobalaccel/*.desktop
%_K5data/kfontinst/
%_K5data/konqsidebartng/
%_K5data/knsrcfiles/*.knsrc
%_K5dbus_srv/*.service
%_K5dbus_sys_srv/*.service

%files -n polkit-kde-plasma-desktop
%_datadir/polkit-1/actions/*fontinst*.policy
%_datadir/polkit-1/actions/*kcmclock*.policy

%files devel
%_K5link/lib*.so
%_K5dbus_iface/*.xml

%files -n %libkfontinst
%_K5lib/libkfontinst.so.*
%_K5lib/libkfontinst.so.%kfontinst_sover
%files -n %libkfontinstui
%_K5lib/libkfontinstui.so.*
%_K5lib/libkfontinstui.so.%kfontinstui_sover

%changelog
* Tue Jul 28 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.5-alt2
- support chromium-gost in favorites menu

* Thu May 07 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.5-alt1
- new version

* Tue Apr 21 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.4-alt2
- fix requires

* Thu Apr 02 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.4-alt1
- new version

* Wed Apr 01 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.3-alt3
- disable plasma krunner plugin by default

* Fri Mar 20 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.3-alt2
- improve taskmanager defaults

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.3-alt1
- new version

* Wed Feb 19 2020 Sergey V Turchin <zerg@altlinux.org> 5.18.1-alt1
- new version

* Thu Jan 09 2020 Sergey V Turchin <zerg@altlinux.org> 5.17.5-alt1
- new version

* Thu Dec 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.4-alt1
- new version

* Wed Nov 20 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.3-alt2
- add main menu items tooltip

* Wed Nov 13 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.3-alt1
- new version

* Fri Nov 01 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.2-alt1
- new version

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.1-alt1
- new version

* Thu Oct 17 2019 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.5-alt1
- new version

* Thu Aug 01 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.4-alt1
- new version

* Thu Jul 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.3-alt1
- new version

* Tue Jul 02 2019 Ivan Razzhivin <underwit@altlinux.org> 5.16.2-alt2
- fix patch alt-menu-add-tooltip.patch

* Wed Jun 26 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.2-alt1
- new version

* Tue Jun 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.16.1-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt2
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.5-alt1
- new version

* Wed Apr 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.4-alt1
- new version

* Wed Apr 10 2019 Pavel Moseev <mars@altlinux.org> 5.12.8-alt3
- fix translate in Input Method Panel (kimpanel) widget

* Tue Apr 02 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt2
- fix menu settings russian translation

* Tue Mar 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt1
- new version

* Wed Feb 13 2019 Oleg Solovyov <mcpain@altlinux.org> 5.12.7-alt7
- plasmashell: filter out items from disabled folderviews

* Mon Jan 14 2019 Oleg Solovyov <mcpain@altlinux.org> 5.12.7-alt6
- use better patch from upstream

* Thu Dec 27 2018 Oleg Solovyov <mcpain@altlinux.org> 5.12.7-alt5
- plasmashell: fix moving icons when we're overlapping with existing ones

* Thu Dec 20 2018 Oleg Solovyov <mcpain@altlinux.org> 5.12.7-alt4
- plasmashell: no more phantom icons after creating something on a fresh desktop
- plasmashell: create new icons in place

* Fri Oct 26 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt3
- disable kwin runner by default

* Tue Oct 02 2018 Oleg Solovyov <mcpain@altlinux.org> 5.12.7-alt2
- plasmashell: fix moving icons between separate desktops on different monitors
- plasmashell: fix incorrect behavior after creating folders

* Thu Sep 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version

* Tue Sep 11 2018 Oleg Solovyov <mcpain@altlinux.org> 5.12.6-alt4%ubt
- systemsettings: fix locales preview

* Tue Sep 4 2018 Ivan Razzhivin <underwit@altlinux.org> 5.12.6-alt3%ubt
- fix tooltip for appentry

* Fri Aug 31 2018 Ivan Razzhivin <underwit@altlinux.org> 5.12.6-alt2%ubt
- add tooltip for appentry

* Wed Jun 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1%ubt
- new version

* Mon May 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt2%ubt
- add fix against KDEBUG-394013

* Thu May 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1%ubt
- new version

* Thu Apr 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt2%ubt
- add Falkon to favorite menu apps

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1%ubt
- new version

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt2%ubt
- exclude krb5-ticket-watcher from saved session by default

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1%ubt
- new version

* Thu Mar 01 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1%ubt
- new version

* Mon Feb 19 2018 Maxim Voronov <mvoronov@altlinux.org> 5.12.0-alt2%ubt
- renamed kf5-plasma-desktop -> plasma5-desktop

* Wed Feb 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1%ubt
- new version

* Wed Jan 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt1%ubt
- new version

* Mon Dec 11 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.4-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1%ubt
- new version

* Tue Nov 07 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Mon Sep 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt1%ubt
- new version

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt1%ubt
- new version

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.3-alt2%ubt
- apply fix against KDEBUG-378262 (ALT#33663)

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.3-alt1%ubt
- new version

* Fri Jun 23 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt2%ubt
- add application generic name to kikoff menu search results

* Wed Apr 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Thu Apr 13 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt2%ubt
- fix taskmanager for Qt 5.6

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

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt4.M80P.1
- build for M80P

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt5
- show name and generic name in main menu by default

* Tue Nov 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt2.M80P.1
- build for M80P

* Tue Nov 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt3
- add Places widget to panel by default

* Thu Oct 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1.M80P.1
- build for M80P

* Thu Oct 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt2
- fix default panel with absent widget

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt0.M80P.1
- build for M80P

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1
- new version

* Tue Oct 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt0.M80P.1
- build for M80P

* Fri Oct 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt1
- new version

* Tue Oct 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Wed Sep 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt4
- fix kicker menu width

* Wed Sep 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt3
- fix kicker menu width

* Tue Sep 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt2
- set kicker main menu by default

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

* Fri May 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.4-alt2
- update menu default favorites

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.4-alt1
- new version

* Tue Apr 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.3-alt2
- set default keyboard layout swithcing policy

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.3-alt1
- new version

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt3
- update menu favorites defaults

* Thu Mar 31 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt2
- update requires

* Wed Mar 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Tue Mar 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt2
- update kbd defaults

* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.5-alt1
- new version

* Wed Feb 03 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt3
- return set of available languages list by systemsettings translations

* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- new version

* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt2
- start empty session by default

* Thu Jan 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt1
- new version

* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt1
- new version

* Mon Dec 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt3
- fix menu default apps

* Wed Dec 23 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt2
- simplify menu favorites apps patch

* Thu Dec 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Thu Nov 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt3
- rebuild

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt1
- new version

* Tue Oct 27 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt3
- set desktop defaults

* Fri Oct 23 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt2
- set panel defaults

* Wed Oct 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Tue Sep 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt4
- add default multimedia players chooser

* Mon Sep 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt3
- fix languages list in translations settings

* Fri Sep 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt2
- set default favorites menu apps

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Wed Aug 26 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Sat Aug 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.95-alt1
- new version

* Fri Aug 21 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt4
- rebuild with new baloo

* Mon Jul 27 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt3
- return default menu icon

* Fri Jul 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt2
- set default menu icon

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Fri May 15 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt2
- update from Plasma/5.3 branch

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
