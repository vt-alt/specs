
%define _libexecdir %prefix/libexec
%define sover 1
%define libsignon_extension libsignon-extension%sover
%define libsignon_plugins_common libsignon-plugins-common%sover
%define libsignon_plugins libsignon-plugins%sover
%define libsignon_qt5 libsignon-qt5%sover

Name: signon
Version: 8.60
Release: alt1

Group: System/Servers
Summary: Accounts framework for Linux and POSIX based platforms
Url: https://gitlab.com/accounts-sso/signond
License: LGPLv2

Requires: dbus

# https://drive.google.com/drive/#folders/0B8fX9XOwH_g4alFsYV8tZTI4VjQ
# https://groups.google.com/forum/#!topic/accounts-sso-announce/
Source: signon-%version.tar
# FC
Patch1: signon-8.57-no_static.patch
# ALT
Patch10: alt-fix-compile.patch

# Automatically added by buildreq on Fri May 29 2015 (-bi)
# optimized out: elfutils fontconfig fonts-bitmap-misc kf5-attica-devel kf5-kjs-devel libGL-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-sql libqt5-test libqt5-xml libstdc++-devel libwayland-client libwayland-server pkg-config python-base python3 python3-base qt5-base-devel qt5-declarative-devel qt5-script-devel qt5-webkit-devel ruby ruby-stdlibs
#BuildRequires: doxygen fonts-bitmap-terminus fonts-otf-stix fonts-ttf-dejavu fonts-ttf-google-droid-kufi fonts-ttf-google-droid-sans fonts-ttf-google-droid-serif fonts-type1-urw gcc-c++ glibc-devel-static graphviz kf5-bluez-qt-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdesu-devel kf5-kdewebkit-devel kf5-kdnssd-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kpeople-devel kf5-kpty-devel kf5-kross-devel kf5-krunner-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-kxmlrpcclient-devel kf5-libkscreen-devel kf5-networkmanager-qt-devel kf5-solid-devel kf5-sonnet-devel libdb4-devel libproxy-devel python-module-google qt5-connectivity-devel qt5-location-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel qt5-sensors-devel qt5-serialport-devel qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-websockets-devel qt5-x11extras-devel qt5-xmlpatterns-devel rpm-build-python3 rpm-build-ruby
BuildRequires: gcc-c++ qt5-base-devel qt5-tools doxygen graphviz libproxy-devel libdbus-devel

%description
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%package common
Summary: %name common package
Group: System/Configuration/Other
%description common
%name common package

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
Headers, development libraries and documentation for %name.

%package -n %libsignon_extension
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libsignon_extension
%name library

%package -n %libsignon_plugins_common
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libsignon_plugins_common
%name library

%package -n %libsignon_plugins
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libsignon_plugins
%name library

%package -n %libsignon_qt5
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libsignon_qt5
%name library

%prep
%setup -n signon-%version
%patch1 -p1 -b .no_static
%patch10 -p1

sed -i '/^SUBDIRS/s|tests||'  signon.pro

find -type f -name \*.pc.in -o -name \*.h | \
while read f ; do
    sed -i 's|/usr/lib|%_libdir|' $f
done

%build
export PATH=%_qt5_bindir:$PATH
%qmake_qt5 \
    signon.pro \
    CONFIG+=release \
    PREFIX=%_prefix \
    QMF_INSTALL_ROOT=%_prefix \
    LIBDIR=%_libdir \
    LIBEXECDIR=%_libexecdir \
    CONFIG+=enable-p2p \
    #
%make_build

%install
export PATH=%_qt5_bindir:$PATH
%installqt5

# create/own libdir/extensions
mkdir -p %buildroot/%_libdir/signon/extensions/

%files common
%doc README* TODO NOTES
%dir %_libdir/signon/
%dir %_libdir/signon/extensions/

%files
%config(noreplace) %_sysconfdir/signond.conf
%_bindir/signon*
%_libdir/signon/*
%_datadir/dbus-1/services/*.service

%files devel
%_includedir/signon*/
%_libdir/lib*.so
%_pkgconfigdir/*.pc
%_libdir/cmake/SignOnQt5/
#%_datadir/dbus-1/interfaces/*.xml
#
%_docdir/signon/
%_docdir/libsignon-qt/
%_docdir/signon-plugins/
%_docdir/signon-plugins-dev/

%files -n %libsignon_extension
%_libdir/libsignon-extension.so.%sover
%_libdir/libsignon-extension.so.*
%files -n %libsignon_plugins_common
%_libdir/libsignon-plugins-common.so.%sover
%_libdir/libsignon-plugins-common.so.*
%files -n %libsignon_plugins
%_libdir/libsignon-plugins.so.%sover
%_libdir/libsignon-plugins.so.*
%files -n %libsignon_qt5
%_libdir/libsignon-qt5.so.%sover
%_libdir/libsignon-qt5.so.*

%changelog
* Mon Sep 30 2019 Sergey V Turchin <zerg@altlinux.org> 8.60-alt1
- new version

* Mon Jun 17 2019 Sergey V Turchin <zerg@altlinux.org> 8.59-alt2
- dont use ubt macro

* Mon Jun 19 2017 Sergey V Turchin <zerg@altlinux.org> 8.59-alt1
- new version

* Wed Sep 21 2016 Sergey V Turchin <zerg@altlinux.org> 8.58-alt1
- update to 8.58 20151106

* Fri Jan 22 2016 Sergey V Turchin <zerg@altlinux.org> 8.57-alt6
- enable dbus p2p

* Thu Jan 21 2016 Sergey V Turchin <zerg@altlinux.org> 8.57-alt5
- redefine _libexecdir

* Mon Nov 02 2015 Sergey V Turchin <zerg@altlinux.org> 8.57-alt4
- fix .pc files

* Tue Aug 04 2015 Sergey V Turchin <zerg@altlinux.org> 8.57-alt3
- fix package shared directories

* Mon Aug 03 2015 Sergey V Turchin <zerg@altlinux.org> 8.57-alt2
- own extensions directory

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 8.57-alt1
- initial build
