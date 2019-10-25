%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

%_K5if_ver_gteq %ubt_id M90
%def_enable obsolete_kde4
%else
%def_disable obsolete_kde4
%endif

%define sover 7
%define libk3blib libk3blib%sover
%define libk3bdevice libk3bdevice%sover

#define req_permhelper alterator-control
%define req_permhelper /usr/bin/gpasswd

%define req_std_burning cdrkit cdrdao dvd+rw-tools cdrskin
%define req_std_common kf5-filesystem %req_permhelper
%define req_multimedia sox-play libsox-fmt-pulseaudio transcode vcdimager normalize lame flac mpc
#req_multimedia transcode
%define req_mini %req_std_burning %req_std_common
%define req_all %req_mini %req_multimedia

%define rname k3b
Name: kde5-%rname
Version: 19.08.2
Release: alt1
%K5init %{?_enable_obsolete_kde4:no_altplace}

Group: Archiving/Cd burning
Summary: The CD Kreator (Complete set)
Summary(ru_RU.UTF-8): Программа записи CD (Полный набор)
URL: http://www.k3b.org/
License: GPLv2

Provides: k3b = %version-%release
Requires: %req_all
Conflicts: k3b-mini < 1.0.5-alt7
%if_enabled obsolete_kde4
Provides: kde4-k3b = %version-%release
Obsoletes: kde4-k3b < %version-%release
%endif

Source0: %rname-%version.tar
Patch1: alt-permhelper.patch
Patch2: alt-return-wodim.patch
Patch3: alt-permhelper-install.patch

# Automatically added by buildreq on Mon May 23 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ glibc-devel-static gtk-update-icon-cache kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libavcodec-devel libavutil-devel libdbusmenu-qt52 libflac-devel libgpg-error libgst-plugins1.0 libjson-c libogg-devel libopencore-amrnb0 libopencore-amrwb0 libp11-kit libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-sensors libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs shared-mime-info xml-common xml-utils
#BuildRequires: extra-cmake-modules kde5-libkcddb-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-kfilemetadata-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libavdevice-devel libavformat-devel libdvdread-devel libflac++-devel liblame-devel libmad-devel libmpcdec-devel libmusicbrainz-devel libmusicbrainz3-devel libpostproc-devel libsamplerate-devel libsndfile-devel libswscale-devel libtag-devel libvorbis-devel python-module-google python3-dev qt5-multimedia-devel qt5-webkit-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-multimedia-devel qt5-declarative-devel
BuildRequires: libavdevice-devel libavformat-devel libpostproc-devel libswscale-devel
BuildRequires: libdvdread-devel libflac++-devel liblame-devel libmad-devel libmpcdec-devel
BuildRequires: libmusicbrainz-devel
BuildRequires: libsamplerate-devel libsndfile-devel libtag-devel libvorbis-devel
BuildRequires: kde5-libkcddb-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools-devel-static
BuildRequires: kf5-kfilemetadata-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel
BuildRequires: kf5-knewstuff-devel

%description
K3b is a GUI frontend to the cd recording programs. 
It's aim is to provide a very user friendly interface to all the tasks that 
come with cd recording. 
This package contains all requiremnts and libraries necessary for full 
program functionality.
%description -l ru_RU.UTF-8
K3b - это мощная графическая оболочка для программ записи компакт дисков.
Она создана для предоставления дружественного интерфейса ко всем задачам, сопровождающим
процесс записи компакт-дисков. 
Этот пакет cодержит зависимости и библиотеки, необходимые для 
полнофункциональной работы программы.


%package mini
Summary: The CD Creator
Summary(ru_RU.UTF-8): Программа записи CD
License: GPL
Group: Archiving/Cd burning
Requires: %req_mini
%description mini
K3b is a GUI frontend to the cd recording programs. 
It's aim is to provide a very user friendly interface to all the tasks that 
come with cd recording.
Install 'k3b' package to get all of the program's features.
%description mini -l ru_RU.UTF-8
K3b - это мощная графическая оболочка для программ записи компакт дисков.
Она создана для предоставления дружественного интерфейса ко всем задачам, сопровождающим
процесс записи компакт-дисков.
Для полнофункцмональной работы Вы можете установить пакет 'k3b'.


%package devel
Summary: The CD Kreator (Development package.)
Summary(ru_RU.UTF-8): Программа записи CD (Пакет разработчика.)
License: GPL
Group: Development/KDE and QT
%description devel
K3b is a GUI frontend to the cd recording programs. 
It's aim is to provide a very user friendly interface to all the tasks that 
come with cd recording. 
This package contains k3b development files and libraries.
%description devel -l ru_RU.UTF-8
K3b - это мощная графическая оболочка для программ записи компакт дисков.
Она создана для предоставления дружественного интерфейса ко всем задачам, сопровождающим
процесс записи компакт-дисков. 
Этот пакет содержит файлы и библиотеки, необходимые разработчику 
модулей k3b.

%package -n %libk3blib
Summary: KDE 4 library
Group: System/Libraries
%description -n %libk3blib
KDE 4 library.

%package -n %libk3bdevice
Summary: KDE 4 library
Group: System/Libraries
%description -n %libk3bdevice
KDE 4 library.

%prep
%setup -q -n %rname-%version
#%patch1 -p1
#%patch2 -p1
%patch3 -p1

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%K5install_move data k3b solid konqsidebartng

mv %buildroot/%_K5xdgmime/x-k3b.xml \
    %buildroot/%_K5xdgmime/kde5-x-k3b.xml


%find_lang --with-kde --all-name %name


%files -f %name.lang
%config(noreplace) %_K5xdgconf/k3btheme.knsrc
%doc README.txt FAQ.txt PERMISSIONS.txt ChangeLog
%_K5bin/%rname
%_K5plug/%{rname}*.so
%_K5plug/kcm_%{rname}*.so
%_K5xdgapp/org.kde.%rname.desktop
%_K5data/solid/actions/%{rname}_*.desktop
%_K5data/%rname/
%_K5xdgmime/*%{rname}*.xml
%_K5srv/%{rname}*.*
%_K5srv/kcm_%{rname}*.*
%_K5srv/ServiceMenus/%{rname}*.desktop
%_K5srvtyp/%{rname}plugin.desktop
%_K5xmlgui/%rname/
%_K5notif/%rname.notifyrc
%_K5icon/hicolor/*/apps/%rname.*
%_K5icon/hicolor/*/mimetypes/application-x-%rname.*
%_datadir/metainfo/*k3b*.xml
#
%_K5plug/kf5/kio/videodvd.so
%_K5data/konqsidebartng/virtual_folders/services/videodvd.desktop
%_K5srv/videodvd.protocol
# permhelper
%_K5libexecdir/kauth/k3bhelper
%_K5dbus_sys_srv/org.kde.k3b.service
%_K5dbus/system.d/org.kde.k3b.conf
%_datadir/polkit-1/actions/org.kde.k3b.policy

%files -n %libk3blib
%_K5lib/libk3blib.so.%sover
%_K5lib/libk3blib.so.%sover.*

%files -n %libk3bdevice
%_K5lib/libk3bdevice.so.%sover
%_K5lib/libk3bdevice.so.%sover.*

%files devel
%_K5link/*.so
%_K5inc/k3b*.h

%changelog
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

* Mon Mar 11 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt2
- build without musicbrainz

* Tue Feb 19 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Tue Oct 16 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt2
- fix build

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Fri Jun 15 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt2%ubt
- remove requires to transcode

* Tue May 22 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Mon May 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt2%ubt
- build without qtwebkit

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Mar 06 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Thu Feb 22 2018 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt2%ubt
- obsolete kde4-k3b

* Mon Nov 13 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Wed Apr 05 2017 Sergey V Turchin <zerg@altlinux.org> 17.03.80-alt1%ubt
- new beta

* Mon Nov 07 2016 Sergey V Turchin <zerg@altlinux.org> 2.10.0-alt0.2.M80P.1
- build for M80P

* Mon Nov 07 2016 Sergey V Turchin <zerg@altlinux.org> 2.10.0-alt0.3
- update from master branch

* Mon Sep 26 2016 Sergey V Turchin <zerg@altlinux.org> 2.10.0-alt0.2
- return wodim support

* Thu Sep 22 2016 Sergey V Turchin <zerg@altlinux.org> 2.10.0-alt0.1
- update from master branch

* Fri Jul 29 2016 Sergey V Turchin <zerg@altlinux.org> 2.9.90-alt2
- update from KF5 branch

* Tue May 24 2016 Sergey V Turchin <zerg@altlinux.org> 2.9.90-alt1
- initial build
