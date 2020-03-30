%define choqok_sover 1
%define libchoqok libchoqok%choqok_sover
%define twitterapihelper_sover 1
%define libtwitterapihelper libtwitterapihelper%twitterapihelper_sover
%define gnusocialapihelper_sover 1
%define libgnusocialapihelper libgnusocialapihelper%gnusocialapihelper_sover

%def_disable webkit

Name: choqok
Version: 1.7.0
Release: alt2
%K5init no_altplace appdata

Group: Networking/Instant messaging
Summary: Micro-Blogging Client
Url: http://choqok.gnufolks.org/
License: GPLv2+

Source: %name-%version.tar
Patch1: 0007-twitter-Don-t-overwrite-original-contents-of-retweet.patch
Patch2: 0010-Link-to-the-original-post-for-retweets.patch
Patch3: 0019-Fix-retrieving-Twitter-conversations.patch
Patch100: choqok-0.9.85-alt-dbus-services-install.patch

# Automatically added by buildreq on Fri Nov 18 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kdoctools-devel kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libgst-plugins1.0 libjson-c libqca-qt5 libqt4-core libqt4-network libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-sensors libqt5-sql libqt5-svg libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libtelepathy-qt5-farstream0 libtelepathy-qt5-service0 libtelepathy-qt50 libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-webkit-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: extra-cmake-modules kf5-kcmutils-devel kf5-kdelibs4support kf5-kdewebkit-devel kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-kio-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-ktextwidgets-devel kf5-kwallet-devel libqca-qt5-devel python-module-google python3-dev qoauth-devel rpm-build-ruby telepathy-qt5-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-networkauth-devel
BuildRequires: qoauth-qt5-devel
BuildRequires: libqca-qt5-devel telepathy-qt5-devel
BuildRequires: kf5-kcmutils-devel kf5-kdelibs4support
%if_enabled webkit
BuildRequires: kf5-kdewebkit-devel
%endif
BuildRequires: kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kglobalaccel-devel
BuildRequires: kf5-kguiaddons-devel kf5-kio-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-ktextwidgets-devel
BuildRequires: kf5-kwallet-devel kf5-purpose-devel

%description
Choqok is a Free/Open Source micro-blogging client for K Desktop Environment


%package -n %libchoqok
Summary: %name library
Group: System/Libraries
Obsoletes: libchoqok0
Conflicts: libchoqok0
%description -n %libchoqok
%name library.

%package -n %libtwitterapihelper
Summary: %name library
Group: System/Libraries
Obsoletes: libtwitterapihelper0
Conflicts: libtwitterapihelper0
%description -n %libtwitterapihelper
%name library.

%package -n %libgnusocialapihelper
Summary: %name library
Group: System/Libraries
%description -n %libgnusocialapihelper
%name library.

%package devel
Summary: %name development files
Group: Development/KDE and QT
Requires: %libchoqok = %version-%release
%description devel
This package contains header files needed if you wish to build applications
based on %name.


%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch100 -p1

%if_disabled webkit
sed -i '/find_package.*KF5WebKit/d' plugins/CMakeLists.txt
%endif

%build
%K5build


%install
%K5install
%find_lang --with-kde %name



%files -f %name.lang
%doc COPYING AUTHORS changelog
%_K5bin/choqok
%_K5plug/*choqok*.so
%_K5plug/kf5/purpose/*.so
%if_enabled webkit
%_K5plug/kf5/parts/*choqok*.so
%_K5srv/ServiceMenus/*choqok*.desktop
%endif
%_K5xdgapp/*choqok*.desktop
%_datadir/choqok/
%_K5cfg/*.kcfg
%_K5icon/*/*/*/*choqok*.*
%_iconsdir/*/*/*/*_microblog.*
%_iconsdir/*/*/*/*_uploader.*
%_iconsdir/*/*/*/*retweet.*
%_K5srv/*choqok*.desktop
%_K5srvtyp/*choqok*.desktop
%_K5dbus_srv/org.kde.choqok.service
%_K5xmlgui/*choqok*/
%_K5notif/*choqok*.notifyrc
%_datadir/metainfo/*choqok*.xml

%files -n %libchoqok
%_K5lib/libchoqok.so.%choqok_sover
%_K5lib/libchoqok.so.%choqok_sover.*

%files -n %libtwitterapihelper
%_K5lib/libtwitterapihelper.so.%twitterapihelper_sover
%_K5lib/libtwitterapihelper.so.%twitterapihelper_sover.*

%files -n %libgnusocialapihelper
%_K5lib/libgnusocialapihelper.so.%gnusocialapihelper_sover
%_K5lib/libgnusocialapihelper.so.%gnusocialapihelper_sover.*

%files devel
%_datadir/cmake/modules/FindChoqok.cmake
%_K5link/lib*.so
%_includedir/choqok/


%changelog
* Thu Mar 26 2020 Sergey V Turchin <zerg@altlinux.org> 1.7.0-alt2
- add upstream fixes

* Fri Mar 06 2020 Sergey V Turchin <zerg@altlinux.org> 1.7.0-alt1
- new version

* Mon Jan 27 2020 Sergey V Turchin <zerg@altlinux.org> 1.6-alt4
- fix compile with new Qt

* Fri Jun 14 2019 Sergey V Turchin <zerg@altlinux.org> 1.6-alt3
- don't use ubt macro

* Wed Aug 23 2017 Sergey V Turchin <zerg@altlinux.org> 1.6-alt2
- build without kdewebkit

* Mon Nov 21 2016 Sergey V Turchin <zerg@altlinux.org> 1.6-alt0.M80P.1
- build for M80P

* Fri Nov 18 2016 Sergey V Turchin <zerg@altlinux.org> 1.6-alt1
- new version

* Thu Feb 19 2015 Sergey V Turchin <zerg@altlinux.org> 1.5-alt0.M70P.1
- build for M70P

* Thu Feb 19 2015 Sergey V Turchin <zerg@altlinux.org> 1.5-alt1
- new version

* Mon Sep 02 2013 Sergey V Turchin <zerg@altlinux.org> 1.4-alt1
- new version

* Thu Aug 02 2012 Sergey V Turchin <zerg@altlinux.org> 1.3-alt1.M60P.1
- built for M60P

* Fri Jul 27 2012 Sergey V Turchin <zerg@altlinux.org> 1.3-alt2
- rebuilt with new attica

* Sat May 05 2012 Sergey V Turchin <zerg@altlinux.org> 1.3-alt0.M60P.1
- new version

* Sat May 05 2012 Sergey V Turchin <zerg@altlinux.org> 1.3-alt1
- new version

* Tue Feb 07 2012 Sergey V Turchin <zerg@altlinux.org> 1.2-alt1.M60P.1
- built for M60P

* Fri Jan 27 2012 Sergey V Turchin <zerg@altlinux.org> 1.2-alt2
- rebuilt with new attica

* Mon Jan 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.2-alt0.M60P.1
- built for M60P

* Fri Jan 20 2012 Sergey V Turchin <zerg@altlinux.org> 1.2-alt1
- new version

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.1-alt3.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * specfile-macros-get_dep-is-deprecated for choqok

* Wed Apr 06 2011 Sergey V Turchin <zerg@altlinux.org> 1.1-alt3
- fix conflict with libchoqok0

* Wed Apr 06 2011 Sergey V Turchin <zerg@altlinux.org> 1.1-alt2
- fix conflict with libtwitterapihelper0

* Tue Apr 05 2011 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- 1.1

* Tue Feb 08 2011 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- 1.0

* Tue Dec 07 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.98-alt1
- 1.0-RC1

* Fri Oct 22 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.92-alt0.M51.1
- built for M51

* Fri Oct 22 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.92-alt1
- 1.0-beta4

* Wed Sep 15 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.90-alt0.M51.1
- built for M51

* Wed Sep 15 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.90-alt1
- 1.0-beta3

* Mon Aug 16 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.85-alt1
- 1.0-beta2

* Wed May 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.55-alt1.M51.1
- built for M51

* Wed May 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.55-alt2
- fix build requires

* Wed May 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.55-alt1
- initial specfile
