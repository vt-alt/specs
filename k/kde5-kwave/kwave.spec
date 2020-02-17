%define rname kwave

%define sover 19
%define libkwavegui libkwavegui%sover
%define libkwave libkwave%sover

Name: kde5-%rname
Version: 19.12.1
Release: alt2
%K5init

Group: Sound
Summary: Simple Sound Editor
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: KDEBUG-394358.patch

# Automatically added by buildreq on Mon Apr 03 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ glib-networking gtk-update-icon-cache kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kdoctools-devel kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libflac-devel libgdk-pixbuf libgpg-error libogg-devel libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libwayland-client libwayland-server libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: ImageMagick-tools dconf doxygen extra-cmake-modules kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-kiconthemes-devel kf5-kio-devel kf5-ktextwidgets-devel libGConf libalsa-devel libaudiofile-devel libfftw3-devel libflac++-devel libopus-devel libpulseaudio-devel libsamplerate-devel libvorbis-devel python-module-google python3-dev qt5-multimedia-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-multimedia-devel
BuildRequires: dconf doxygen
BuildRequires: libGConf libalsa-devel libaudiofile-devel libfftw3-devel libflac++-devel libopus-devel libpulseaudio-devel libsamplerate-devel libvorbis-devel
BuildRequires: id3lib-devel libmad-devel
BuildRequires: kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-kiconthemes-devel kf5-kio-devel kf5-ktextwidgets-devel
BuildRequires: kf5-karchive-devel

%description
Kwave is a simple sound editor.

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

%package -n %libkwavegui
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libkwavegui
%name library

%package -n %libkwave
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkwave
%name library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build \
    -DWITH_DOC=OFF \
    #

%install
%K5install
%K5install_move data kwave
%find_lang %name --with-kde --all-name

%files common -f %name.lang
#%doc COPYING*
%_K5srvtyp/*kwave*.desktop

%files
%_K5bin/kwave
%_K5plug/kwave/
%_K5data/kwave/
%_K5icon/*/*/*/*kwave*.*
%_K5xdgapp/*kwave*.desktop

#%files devel
#%_K5inc/kwave_version.h
#%_K5inc/kwave/
#%_K5link/lib*.so
#%_K5lib/cmake/kwave
#%_K5archdata/mkspecs/modules/qt_kwave.pri

%files -n %libkwave
%_K5lib/libkwave.so.%sover
%_K5lib/libkwave.so.*
%files -n %libkwavegui
%_K5lib/libkwavegui.so.%sover
%_K5lib/libkwavegui.so.*

%changelog
* Fri Feb 14 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt2
- add fix against crash on application quit
- clean build requires

* Tue Jan 21 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Fri Nov 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Fri Oct 25 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.2-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Tue Aug 27 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

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

* Thu Jan 25 2018 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt2%ubt
- fix build requires

* Mon Nov 13 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Thu Mar 16 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- initial build
