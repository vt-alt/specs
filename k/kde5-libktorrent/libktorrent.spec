
%define sover 6
%define libkf5torrent libkf5torrent%sover

Name: kde5-libktorrent
Version: 2.2.0
Release: alt1
%K5init

Group: System/Libraries
Summary: BitTorrent library for KDE
Url: http://ktorrent.org/
License: GPL-2.0-only

Source: libktorrent-%version.tar

# Automatically added by buildreq on Mon Apr 18 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ libEGL-devel libGL-devel libgpg-error libgpg-error-devel libqca-qt5 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: boost-devel-headers doxygen extra-cmake-modules graphviz kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libgcrypt-devel libgmp-devel libqca-qt5-devel python-module-google python3-dev rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: boost-devel doxygen extra-cmake-modules graphviz
BuildRequires: libgcrypt-devel libgmp-devel libqca-qt5-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel

%description
Library that allow using BitTorrent with KDE programs

%package common
BuildArch: noarch
Summary: Common %name files
Group: System/Configuration/Other
%description common
Common %name files

%package -n %libkf5torrent
Summary: KTorrent library
Group: System/Libraries
Requires: %name-common
%description -n %libkf5torrent
KTorrent library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: libgcrypt-devel libqca-qt5-devel
%description devel
This package contains the development files for %name.


%prep
%setup -qn libktorrent-%version

%build
%K5build \
    -DKDE_INSTALL_LOCALEDIR=%_K5i18n \
  #

%install
%K5install
%find_lang --with-kde --all-name %name

%files common -f %name.lang

%files -n %libkf5torrent
%_libdir/libKF5Torrent.so.%sover
%_libdir/libKF5Torrent.so.%sover.*

%files devel
%_K5lib/cmake/KF5Torrent/
%_K5inc/libktorrent/
%_K5link/lib*.so

%changelog
* Fri Jul 17 2020 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt1
- new version

* Thu Sep 19 2019 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt1
- new version

* Fri Jun 14 2019 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt2
- dont use ubt macro

* Mon Oct 02 2017 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt1
- new version

* Mon Apr 18 2016 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt1
- initial build
