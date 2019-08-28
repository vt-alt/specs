%define rname konsole

%define sover 19
%define libkonsoleprivate libkonsoleprivate%sover

Name: kde5-%rname
Version: 19.08.0
Release: alt1
%K5init

Group: Terminals
Summary: Terminal emulator for KDE
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires(post,preun): alternatives >= 0.2
Provides: xvt, %_x11bindir/xvt
#Requires: fonts-bitmap-misc

Source: %rname-%version.tar
Patch10: alt-no-transparency.patch
Patch11: alt-konsole-profiles.patch
Patch12: alt-def-font.patch

# Automatically added by buildreq on Mon Apr 27 2015 (-bi)
# optimized out: alternatives cmake cmake-modules docbook-dtds docbook-style-xsl elfutils kf5-kdoctools-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXrender-devel libXt-devel libcloog-isl4 libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-script libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms python-base qt5-base-devel ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kpty-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdb4-devel libxkbfile-devel python-module-google qt5-script-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: libalternatives-devel
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel qt5-script-devel
BuildRequires: libdb4-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
BuildRequires: kf5-kdelibs4support kf5-kdelibs4support-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kdesignerplugin-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel
BuildRequires: kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel
BuildRequires: kf5-knotifyconfig-devel kf5-kparts-devel kf5-kpty-devel kf5-kservice-devel kf5-ktextwidgets-devel
BuildRequires: kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel
BuildRequires: kf5-sonnet-devel kf5-knewstuff-devel kf5-kglobalaccel-devel
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel
BuildRequires: libXmu-devel libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel
BuildRequires: libxkbfile-devel

%description
As well as being a standalone program, it is also used by other KDE programs
such as the Kate editor and KDevelop development environment to provide easy
access to a terminal window. Konsole's features and usage are explained and
illustrated in the Konsole handbook, which can be accessed by browsing to
"help:/konsole" in Konqueror.

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

%package -n %libkonsoleprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkonsoleprivate
KF5 library

%prep
%setup -q -n %rname-%version
%patch10 -p1 -b .transparency
#%patch11 -p1
%patch12 -p1

%build
%K5build \
    -DDATA_INSTALL_DIR=%_K5data \
    #

%install
%K5install
%K5install_move data konsole khotkeys
%find_lang %name --with-kde --all-name

# install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/kde5-konsole <<__EOF__
%_x11bindir/xvt %_K5bin/konsole        50
__EOF__


%files common -f %name.lang
%doc COPYING*
%_datadir/qlogging-categories5/*.*categories

%files
%config %_sysconfdir/alternatives/packages.d/kde5-konsole
# konsole may problems for some reasons because sgid
#%attr(2711,root,utempter) %_K5bin/konsole
%_K5bin/konsole
%_K5bin/konsoleprofile
%_K5lib/libkdeinit5_konsole.so
%_K5plug/konsole*.so
%_K5xdgapp/org.kde.konsole.desktop
%_K5data/konsole/
%_K5data/khotkeys/konsole.khotkeys
%_K5srv/*.desktop
%_K5srv/ServiceMenus/konsole*.desktop
%_K5srvtyp/*.desktop
%_K5notif/*
%_K5data/knsrcfiles/*konsole*

%files -n %libkonsoleprivate
%_K5lib/libkonsoleprivate.so.*
%_K5lib/libkonsoleprivate.so.%sover

%changelog
* Tue Aug 27 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Wed Jul 17 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Fri Jul 05 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt3
- don't use utempter

* Thu Jul 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt2
- using utempter

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

* Mon Aug 21 2017 Oleg Solovyov <mcpain@altlinux.org> 17.04.3-alt2%ubt
- fix tabdrag (ALT#33507)

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jul 05 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt2%ubt
- set Monospace font by default to scale with hi resolution
- intense bold fonts by default

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Thu Mar 23 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Jan 12 2017 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt2%ubt
- update code from upstream

* Thu Nov 24 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt0.M80P.1
- build for M80P

* Wed Nov 23 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Tue Oct 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt3
- add upstream fix for KDEBUG#367746

* Fri Sep 23 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt2
- disable kcrash

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Thu Sep 08 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt2
- don't intense bold fonts by default

* Tue Sep 06 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- new version
- use Fixed font instead of Terminus by default

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

* Fri Dec 25 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt2
- fix default font

* Tue Dec 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Fri Dec 11 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt2
- set Terminus font by default

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Mon Sep 21 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt2
- disable transparency by default
- add profile entry for root

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Thu Aug 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Mon Jun 01 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.2-alt1
- new version

* Mon Apr 27 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.0-alt1
- initial build
