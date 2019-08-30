
%define rname kfilemetadata
Name: kde4-kfilemetadata
Version: 4.14.3
Release: alt8

Group: System/Libraries
Summary: A library for extracting file metadata
Url: https://projects.kde.org/projects/kde/kdelibs/%rname
License: LGPLv2 / LGPLv3

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Apr 18 2014 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libavcodec-devel libavutil-devel libcloog-isl4 libdbus-devel libfreetype-devel libopencore-amrnb0 libopencore-amrwb0 libpng-devel libpoppler4-qt4 libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-test libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby ruby-stdlibs xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: ebook-tools-devel gcc-c++ glib2-devel kde4libs-devel libavdevice-devel libavformat-devel libexiv2-devel libicu50 libpoppler-qt4-devel libpostproc-devel libswscale-devel libtag-devel python-module-protobuf qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires: ebook-tools-devel gcc-c++ kde4libs-devel
BuildRequires: libexiv2-devel
#BuildRequires: libpoppler-qt4-devel
#BuildRequires: libavresample-devel libavdevice-devel libpostproc-devel libswscale-devel
#BuildRequires: libavcodec-devel libavformat-devel libavutil-devel
BuildRequires: libtag-devel
BuildRequires: kde-common-devel
#BuildRequires: qmobipocket-devel

%description
%summary.

%package devel
Group: Development/KDE and QT
Summary: Developer files for %name
Requires: kde4libs-devel
%description devel
%summary.

%package -n libkfilemetadata4
Group: System/Libraries
Summary: %name library
%description -n libkfilemetadata4
%name library

%prep
%setup -qn %rname-%version

%build
%K4build

%install
%K4install


%files -n libkfilemetadata4
%_K4libdir/libkfilemetadata.so.*
%_K4lib/kfilemetadata_*extractor.so
%_K4srv/kfilemetadata_*extractor.desktop
%_K4srvtyp/kfilemetadataextractor.desktop

%files devel
%_K4includedir/kfilemetadata/
%_K4link/lib*.so
%_K4libdir/cmake/KFileMetaData/

%changelog
* Wed Jun 26 2019 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt8
- build without poppler-qt4

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.14.3-alt7
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 4.14.3-alt6
- NMU: remove %ubt from release

* Thu Jun 14 2018 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt5
- build without ffmpeg

* Tue Jun 20 2017 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt4
- rebuild with ffmpeg

* Mon Aug 31 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt3
- update from 4.14 branch

* Tue Jun 30 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt2
- rebuild with new exiv2

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.14.3-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Fri Apr 03 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt1
- new version

* Fri Apr 03 2015 Sergey V Turchin <zerg@altlinux.org> 4.13.1-alt2
- fix build requires

* Tue May 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.1-alt1
- new version

* Fri Apr 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- initial build
