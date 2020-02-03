%define rname audiocd-kio

%define sover 5
%define libaudiocdplugins libaudiocdplugins%sover

Name: kde5-%rname
Version: 19.12.1
Release: alt1
%K5init

Group: Sound
Summary: Audio CD ioslave
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: lame

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Mar 30 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libogg-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: extra-cmake-modules kde5-libkcddb-devel kde5-libkcompactdisc-devel kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel lame libalsa-devel libcdparanoia-devel libflac-devel libvorbis-devel python-module-google python3-dev qt5-phonon-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-phonon-devel
BuildRequires: lame libalsa-devel libcdparanoia-devel libflac-devel libvorbis-devel
BuildRequires: kde5-libkcddb-devel kde5-libkcompactdisc-devel
BuildRequires: kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kio-devel
BuildRequires: kf5-kcmutils-devel

%description
Allows treating audio CDs like a 'real' filesystem, where tracks
are represented as files and, when copied from the folder,
are digitally extracted from the CD. This ensures a perfect
copy of the audio data.

%package -n kde5-kio-audiocd
Group: Sound
Summary: Audio CD ioslave
Requires: %name-common = %version-%release
Requires: lame
%description -n kde5-kio-audiocd
Allows treating audio CDs like a 'real' filesystem, where tracks
are represented as files and, when copied from the folder,
are digitally extracted from the CD. This ensures a perfect
copy of the audio data.

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

%package -n %libaudiocdplugins
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libaudiocdplugins
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%K5install_move data konqsidebartng solid
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_datadir/qlogging-categories5/*.*categories

%files -n kde5-kio-audiocd
%_K5plug/*audiocd*.so
%_K5plug/kf5/kio/*audiocd*.so
%_K5cfg/*audiocd*
%_K5data/konqsidebartng/virtual_folders/services/*audiocd*
%_K5data/solid/actions/*audiocd*
%_K5srv/*audiocd*

%files devel
%_K5inc/*.h
#%_K5inc/audiocd-kio/
%_K5link/lib*.so
#%_K5lib/cmake/audiocd-kio
#%_K5archdata/mkspecs/modules/qt_audiocd-kio.pri

%files -n %libaudiocdplugins
%_K5lib/libaudiocdplugins.so.%sover
%_K5lib/libaudiocdplugins.so.*

%changelog
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
