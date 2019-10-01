
%def_enable apidox

%define _libexecdir %prefix/libexec
%define sover 1
%define libname libaccounts-qt5%sover

Name: accounts-qt5
Version: 1.16
Release: alt1

Group: System/Libraries
Summary: Accounts framework Qt 5 bindings
Url: https://gitlab.com/groups/accounts-sso
License: LGPLv2

# https://drive.google.com/#folders/0B8fX9XOwH_g4alFsYV8tZTI4VjQ
# https://groups.google.com/forum/#!forum/accounts-sso-announce
Source: %name-%version.tar

# Automatically added by buildreq on Mon May 25 2015 (-bi)
# optimized out: elfutils fontconfig fonts-bitmap-misc glib2-devel kf5-attica-devel kf5-kjs-devel libaccounts-glib libgio-devel libqt5-core libqt5-xml libstdc++-devel libwayland-client libwayland-server pkg-config python-base python3 python3-base qt5-base-devel qt5-declarative-devel qt5-script-devel qt5-webkit-devel ruby ruby-stdlibs
#BuildRequires: doxygen fonts-bitmap-terminus fonts-otf-stix fonts-ttf-dejavu fonts-ttf-google-droid-kufi fonts-ttf-google-droid-sans fonts-ttf-google-droid-serif fonts-type1-urw gcc-c++ glibc-devel-static graphviz kf5-bluez-qt-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdesu-devel kf5-kdewebkit-devel kf5-kdnssd-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kpeople-devel kf5-kpty-devel kf5-kross-devel kf5-krunner-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-kxmlrpcclient-devel kf5-libkscreen-devel kf5-networkmanager-qt-devel kf5-solid-devel kf5-sonnet-devel libaccounts-glib-devel libdb4-devel qt5-connectivity-devel qt5-location-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel qt5-sensors-devel qt5-serialport-devel qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-websockets-devel qt5-x11extras-devel qt5-xmlpatterns-devel rpm-build-python3 rpm-build-ruby
BuildRequires: graphviz doxygen qt5-base-devel
%if_enabled apidox
BuildRequires: qt5-tools
%endif
BuildRequires: libaccounts-glib-devel

%description
Framework to provide accounts for Qt 5.

%package -n %libname
Group: System/Libraries
Summary: %name library
%description -n %libname
%name library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: libaccounts-glib-devel qt5-base-devel
%description devel
Headers, development libraries and documentation for %name.

%prep
%setup -n %name-%version
sed -i '/^SUBDIRS/s|tests||'  accounts-qt.pro

%build
export PATH=%_qt5_bindir:$PATH
%qmake_qt5 \
    QMAKE_STRIP=echo \
    QMF_INSTALL_ROOT=%prefix \
    CONFIG+=release \
    PREFIX=%_prefix \
    LIBDIR=%_libdir \
    LIBEXECDIR=%_libexecdir \
    accounts-qt.pro \
    #
%make_build

%install
export PATH=%_qt5_bindir:$PATH
%install_qt5 STRIP=echo

%if_enabled apidox
# install docs
mkdir %buildroot/%_qt5_docdir
rm -f %buildroot/%_docdir/accounts-qt/html/installdox
mv %buildroot/%_docdir/accounts-qt/html %buildroot/%_qt5_docdir/accounts
mv %buildroot/%_docdir/accounts-qt/qch/accounts.qch %buildroot/%_qt5_docdir/
%else
rm -rf %buildroot/%_docdir/accounts-qt/
%endif

%files -n %libname
%_libdir/libaccounts-qt5.so.%sover
%_libdir/libaccounts-qt5.so.*

%files devel
%doc doc/html
%_qt5_libdir/libaccounts-qt5.so
%_qt5_libdatadir/libaccounts-qt5.so
%_includedir/accounts-qt5/
%_pkgconfigdir/accounts-qt5.pc
%_libdir/cmake/AccountsQt5/
%if_enabled apidox
%_qt5_docdir/accounts/
%_qt5_docdir/accounts.qch
%endif

%changelog
* Mon Sep 30 2019 Sergey V Turchin <zerg@altlinux.org> 1.16-alt1
- new version

* Wed Apr 10 2019 Sergey V Turchin <zerg@altlinux.org> 1.15-alt3
- fix compile docs

* Tue Jun 26 2018 Sergey V Turchin <zerg@altlinux.org> 1.15-alt2
- enable debuginfo

* Mon Jun 19 2017 Sergey V Turchin <zerg@altlinux.org> 1.15-alt1
- new version

* Thu Jan 21 2016 Sergey V Turchin <zerg@altlinux.org> 1.13-alt4
- clean build options

* Thu Oct 29 2015 Sergey V Turchin <zerg@altlinux.org> 1.13-alt3
- sync patches with FC

* Wed Jun 03 2015 Sergey V Turchin <zerg@altlinux.org> 1.13-alt2
- fix requires

* Mon May 25 2015 Sergey V Turchin <zerg@altlinux.org> 1.13-alt1
- initial build
