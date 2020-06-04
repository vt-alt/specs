%define _unpackaged_files_terminate_build 1

Name: kdevelop5
Version: 5.4.80
Release: alt0.1.p9
Summary: A cross-platform IDE for C, C++, Python, QML/JavaScript and PHP
Group: Development/Tools
License: GPLv2
Url: http://www.kdevelop.org/
Source: v%version.tar.gz

%add_python_req_skip lldb
%add_python_req_skip gdb
%add_python3_req_skip gdb

BuildRequires(pre): rpm-build-kf5 rpm-build-python3

# Automatically added by buildreq on Sun Aug 12 2018
# optimized out: clang6.0-devel clang6.0-libs cmake cmake-modules docbook-dtds docbook-style-xsl gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-svg libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms llvm-libs python-base python-modules python3 python3-base qt5-base-common qt5-base-devel qt5-declarative-devel sh3 shared-mime-info xml-common xml-utils xz
BuildRequires: boost-devel-headers extra-cmake-modules grantlee5-devel gtk-update-icon-cache kde5-libkomparediff2-devel kde5-okteta-devel kf5-karchive-devel kf5-kcmutils-devel kf5-kcrash-devel kf5-kdeclarative-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-kguiaddons-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemmodels-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kpackage-devel kf5-kparts-devel kf5-krunner-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-purpose-devel kf5-threadweaver-devel libssl-devel llvm10.0-devel plasma5-libksysguard-devel qt5-webkit-devel
BuildRequires: python-tools-2to3 libqt5-svg libqt5-webchannel libqt5-help kdevelop-pg-qt qt5-webengine-devel

%description
KDevelop is a free software integrated development environment (IDE)
developed under the KDE Umbrella. KDevelop provides support for a wide
variety of languages (such as C/C++, Python, PHP, Ruby, ...) via an
extensible plugin framework.

%prep
%setup  -n kdevelop-%version
sed -i '/.etc.bash[.]bashrc/s/^/#/' kdevplatform/util/kdevplatform_shell_environment.sh
2to3 -w plugins/gdb/printers/*.py

%build
%K5cmake
%K5make

%install
%K5install
%K5install_move data kdevelop kconf_update
%K5install_move bin 'kdevelop!' kdevplatform_shell_environment.sh
echo '#!/bin/sh
exec '%_K5bin/'kdevelop!'' "$@"
' > %buildroot/%_bindir/kdevelop!
chmod +x %buildroot/%_bindir/kdevelop!

echo '#!/bin/sh
exec '%_K5bin/'kdevelop'' "$@"
' > %buildroot/%_bindir/kdevelop5
chmod +x %buildroot/%_bindir/kdevelop5

%find_lang %name --with-kde --all-name

%files -f %name.lang
%_K5bin/*
%_bindir/*
%_K5data/kdevelop
%_datadir/metainfo/*
%_xdgmimedir/packages/*
%_datadir/plasma/plasmoids/*
%_datadir/plasma/services/*
%_K5notif/*
%_K5srv/*
%_K5srvtyp/*
%_datadir/kdev*
%_K5icon/hicolor/*/*/*
%_libdir/lib*.so.*
%_qt5_plugindir/*
%_K5qml/org/kde/kdevplatform
%_kf5_xdgapp/*
%_libdir/cmake/KDevelop
%_includedir/kdevelop

%_datadir/knsrcfiles/*
%_datadir/qlogging-categories5/*

%_includedir/kdevplatform
%_libdir/cmake/KDevPlatform
%_K5link/*

%changelog
* Mon Jun 01 2020 Andrey Cherepanov <cas@altlinux.org> 5.4.80-alt0.1.p9
- Backport new version to p9 branch.

* Thu Jan 23 2020 Fr. Br. George <george@altlinux.ru> 5.4.80-alt1
- Autobuild version bump to 5.4.80

* Mon Nov 18 2019 Fr. Br. George <george@altlinux.ru> 5.4.4-alt1
- Autobuild version bump to 5.4.4

* Mon Jun 17 2019 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt2
- Rebuild witn new okteta

* Mon Mar 18 2019 Fr. Br. George <george@altlinux.ru> 5.3.2-alt1
- Autobuild version bump to 5.3.2

* Thu Feb 07 2019 Fr. Br. George <george@altlinux.ru> 5.3.1-alt1
- Autobuild version bump to 5.3.1

* Tue Oct 09 2018 Fr. Br. George <george@altlinux.ru> 5.2.80-alt2
- Fix user binary

* Thu Oct 04 2018 Fr. Br. George <george@altlinux.ru> 5.2.80-alt1
- Autobuild version bump to 5.2.80

* Sun Aug 12 2018 Fr. Br. George <george@altlinux.ru> 5.2.3-alt1
- Autobuild version bump to 5.2.3

* Sun Aug 12 2018 Fr. Br. George <george@altlinux.ru> 5.2.1-alt1
- Initial build for ALT

