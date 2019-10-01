Name: signon-plugin-oauth2
Version: 0.24
Release: alt5

Group: System/Libraries
Summary: OAuth2 plugin for the Accounts framework
Url: https://gitlab.com/accounts-sso/signon-plugin-oauth2
License: LGPLv2

Requires: signon-ui

Source: signon-oauth2-%version.tar

# Automatically added by buildreq on Thu Jul 09 2015 (-bi)
# optimized out: elfutils kf5-attica-devel kf5-kjs-devel libqt5-core libqt5-network libqt5-xmlpatterns libsignon-plugins1 libsignon-qt51 libstdc++-devel pkg-config python-base python3 python3-base qt5-base-devel qt5-declarative-devel qt5-script-devel qt5-webkit-devel ruby ruby-stdlibs
#BuildRequires: gcc-c++ glibc-devel-static kf5-bluez-qt-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdesu-devel kf5-kdewebkit-devel kf5-kdnssd-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kpeople-devel kf5-kpty-devel kf5-kross-devel kf5-krunner-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-kxmlrpcclient-devel kf5-libkscreen-devel kf5-networkmanager-qt-devel kf5-solid-devel kf5-sonnet-devel libdb4-devel python-module-google qt5-connectivity-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel qt5-sensors-devel qt5-serialport-devel qt5-svg-devel qt5-tools-devel qt5-websockets-devel qt5-x11extras-devel qt5-xmlpatterns-devel rpm-build-python3 rpm-build-ruby signon-devel
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel qt5-xmlpatterns-devel
BuildRequires: signon-devel libproxy-devel
BuildRequires: doxygen graphviz

%description
%summary.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
%summary.

%prep
%setup -qn signon-oauth2-%version
sed -i '/^SUBDIRS/s/tests//' signon-oauth2.pro
sed -i '/^SUBDIRS/s/example//' signon-oauth2.pro
%ifarch %e2k
# moc_base-plugin.cpp:30: offsetof against non-POD
%add_optflags -Wno-error=invalid-offsetof
%endif

%build
export PATH=%_qt5_bindir:$PATH
%qmake_qt5 \
    QMF_INSTALL_ROOT=%prefix \
    PREFIX=%prefix \
    CONFIG+=release \
    LIBDIR=%_libdir \
    signon-oauth2.pro

%make_build

%install
%install_qt5

sed -i 's|/lib|/%_lib|' %buildroot/%_pkgconfigdir/signon-oauth2plugin.pc
sed -i 's|^Version:.*|Version: %version|' %buildroot/%_pkgconfigdir/signon-oauth2plugin.pc

%files
%_libdir/signon/liboauth2plugin.so

%files devel
%_includedir/signon-plugins/*.h
%_libdir/pkgconfig/signon-oauth2plugin.pc

%changelog
* Tue Jun 25 2019 Sergey V Turchin <zerg@altlinux.org> 0.24-alt5
- fix minor spec cleanup

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.24-alt4
- NMU: remove rpm-build-ubt from BR:

* Tue Jun 18 2019 Michael Shigorin <mike@altlinux.org> 0.24-alt3
- E2K: ftbfs workaround
- minor spec cleanup

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.24-alt2
- NMU: remove %ubt from release

* Mon Jun 19 2017 Sergey V Turchin <zerg@altlinux.org> 0.24-alt1%ubt
- new version

* Mon Jan 25 2016 Sergey V Turchin <zerg@altlinux.org> 0.22-alt1
- new version

* Thu Jul 09 2015 Sergey V Turchin <zerg@altlinux.org> 0.21-alt1
- initial build
