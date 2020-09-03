%define rname ring-kde

%define ringqt_sover 1.0.0
%define libringqt libringqt%ringqt_sover

Name: ring-client-kde5
Version: 3.1.0
Release: alt3
%K5init no_altplace

Group: Communications
Summary: Ring KDE Client
# https://projects.kde.org/projects/playground/pim/ring-kde/
Url: http://www.kde.org
License: GPLv2+

Requires(post,preun): alternatives >= 0.2
Requires: ring-daemon kf5-kirigami

Source: %rname-%version.tar
Source1: add-po
Patch1: alt-add-translations.patch
Patch2: alt-fix-compile.patch
Patch3: alt-desktop-translation.patch
Patch4: alt-qt515.patch

# Automatically added by buildreq on Mon Sep 05 2016 (-bi)
# optimized out: alternatives cmake cmake-modules elfutils gcc-c++ gtk-update-icon-cache kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libical-devel libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3
#BuildRequires: boost-devel-headers extra-cmake-modules kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-kcalcore-devel kde5-kcontacts-devel kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kglobalaccel-devel kf5-kio-devel kf5-knotifyconfig-devel libGLU-devel libringclient-devel python-module-google python3-dev qt5-svg-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5
BuildRequires: boost-devel-headers extra-cmake-modules
BuildRequires: qt5-declarative-devel qt5-quickcontrols2-devel qt5-svg-devel qt5-tools qt5-tools-devel
BuildRequires: libGLU-devel
BuildRequires: libringclient-devel >= 1.0.1
BuildRequires: kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-kcalcore-devel kde5-kcontacts-devel
BuildRequires: kf5-kpackage-devel kf5-kguiaddons-devel kf5-kitemmodels-devel
BuildRequires: kf5-kdeclarative-devel kf5-kdoctools-devel-static kf5-kglobalaccel-devel kf5-kio-devel kf5-knotifyconfig-devel
BuildRequires: kf5-ki18n-devel kf5-kdbusaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel
BuildRequires: kf5-knotifications-devel kf5-kiconthemes-devel kf5-kcrash-devel kf5-kirigami-devel

%description
Ring-KDE is a Qt based client for the Ring(www.ring.cx) daemon.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libringqt
Group: System/Libraries
Summary: Ring client library
#Requires: %name-common >= %EVR
%description -n %libringqt
Client library for GNU Ring.


%prep
%setup -n %rname-%version
%patch1 -p1
#%patch2 -p1
%patch3 -p1
%patch4 -p1

# add translations
mv .gear/po ./
#cat %SOURCE1 >> CMakeLists.txt

mkdir BUILD
mv .gear/kquickitemviews  libkquickitemviews
ln -s ../libkquickitemviews/src src/KQuickItemViews
mv .gear/libringqt libringqt
ln -s %_datadir/dbus-1/interfaces BUILD/xml

# fake git binary presence
mkdir bin2
ln -s /bin/true bin2/git

%build
export PATH=$PATH:$PWD/bin2

%K5build \
    -DENABLE_LIBWRAP:BOOL=FALSE \
    #

%install
%K5install
rm -f %buildroot/%_K5bin/ring

# install alternative
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_bindir/ring.cx       %_K5bin/ring-kde      50
__EOF__

%find_lang ring-kde --with-kde
%find_lang lrc --with-qt

%files -f ring-kde.lang
%dir %_datadir/libringqt/
%doc COPYING* AUTHORS
%config /%_sysconfdir/alternatives/packages.d/%name
%_K5bin/ring-kde
%_datadir/ring-kde/
%_K5xdgapp/org.kde.ring-kde.desktop
%_K5cfg/ring-kde.kcfg
%_K5xmlgui/ring-kde/
%_K5notif/ring-kde.notifyrc
%_K5icon/hicolor/*/apps/ring-kde.*

%files -n %libringqt -f lrc.lang
%_libdir/libringqt.so.%ringqt_sover
%_libdir/libringqt.so.*

%files devel
%_includedir/libringqt/
%_libdir/cmake/LibRingQt/
%_K5link/lib*.so
%_K5dbus_iface/cx.ring.ring-kde.xml

%changelog
* Fri Aug 28 2020 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt3
- fix to build with qt-5.15

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt2
- NMU: remove rpm-build-ubt from BR:

* Tue Feb 12 2019 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt1
- new version

* Thu Aug 02 2018 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt4%ubt
- update russian translation

* Thu Jul 19 2018 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt3%ubt
- fix requires

* Thu Jul 19 2018 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt2%ubt
- load libringqt translations

* Wed Jul 18 2018 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt1%ubt
- fix requires

* Tue Jul 17 2018 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt0.1%ubt
- new version

* Thu Jul 12 2018 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.6%ubt
- update russian translation

* Tue Jul 25 2017 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.5%ubt
- rebuild

* Mon Feb 27 2017 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.4%ubt
- update from master branch

* Mon Sep 05 2016 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.3
- update build requires

* Thu May 19 2016 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.2
- add translations

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.1
- new version

* Wed Mar 16 2016 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt0.1
- initial build
