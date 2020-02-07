%define rname kimagemapeditor

Name: kde5-%rname
Version: 19.12.1
Release: alt1
%K5init

Group: Development/Other
Summary: An HTML imagemap editor
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Jan 23 2020 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 gtk-update-icon-cache kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libgdk-pixbuf libglvnd-devel libgpg-error libopencore-amrnb0 libopencore-amrwb0 libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-svg libqt5-webchannel libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libx265-176 libxcbutil-keysyms python-modules python2-base python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-webchannel-devel rpm-build-python3 sh4 xml-common xml-utils
#BuildRequires: appstream extra-cmake-modules kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-kguiaddons-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kparts-devel kf5-ktextwidgets-devel libssl-devel python-modules-compiler python3-dev qt5-wayland-devel qt5-webengine-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: qt5-wayland-devel qt5-webengine-devel
BuildRequires: kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-kguiaddons-devel
BuildRequires: kf5-kiconthemes-devel kf5-kio-devel kf5-kparts-devel kf5-ktextwidgets-devel

%description
An HTML imagemap editor.

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

%package -n libkf5imagemapeditor
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n libkf5imagemapeditor
%name library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data kimagemapeditor
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/kimagemapeditor
%_K5plug/kimagemapeditor.so
%_K5xdgapp/org.kde.kimagemapeditor.desktop
%_K5icon/*/*/actions/*.*
%_K5icon/*/*/apps/kimagemapeditor.*
%_K5data/kimagemapeditor/
%_K5srv/kimagemapeditorpart.desktop
#%_K5xmlgui/kimagemapeditor/
%_datadir/qlogging-categories5/*.*categories

%changelog
* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Mon Nov 25 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.2-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Wed Aug 28 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Tue May 07 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Mon Feb 25 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1
- new version

* Thu Jan 18 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.1-alt1
- new version

* Wed Dec 20 2017 Sergey V Turchin <zerg@altlinux.org> 17.12.0-alt1
- initial build
