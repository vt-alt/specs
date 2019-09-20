%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

%define opencv_ver %{get_version libopencv-devel}

%def_disable baloo
%def_enable mysql
%_K5if_ver_gteq %ubt_id M90
%def_enable obsolete_kde4
%else
%def_disable obsolete_kde4
%endif
%_K5if_ver_lt %opencv_ver 3
%def_disable opencv3
%else
%def_enable opencv3
%endif

%define rname digikam
%define label digiKam
%define sover 6
%define libdigikamdatabase libdigikamdatabase%sover
%define libdigikamcore libdigikamcore%sover
%define libdigikamgui libdigikamgui%sover

Name: kde5-%rname
%define lname lib%name
Version: 6.3.0
Release: alt1
%K5init %{?_enable_obsolete_kde4:no_altplace}

Summary: digiKam is an advanced digital photo management application for linux
License: GPLv2+
Group: Graphics
Url: http://www.digikam.org/

Provides: digikam = %version-%release
%if_enabled obsolete_kde4
Provides: kde4-digikam = %version-%release
Obsoletes: kde4-digikam < %version-%release
%endif

Requires: qt5-sql-sqlite
#Requires: kde5-runtime
Requires: %name-data = %version-%release
%if_enabled mysql
Requires: qt5-sql-mysql
%endif
# libs/dimg/filters/icc
Requires: icc-profiles

BuildRequires(pre): rpm-build-kf5 rpm-build-ubt libopencv-devel
# Automatically added by buildreq on Wed Jul 20 2016 (-bi)
# optimized out: boost-devel-headers cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ glib2-devel glibc-devel-static gtk-update-icon-cache kde5-akonadi-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kguiaddons-devel kf5-kiconthemes-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libEGL-devel libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdb4-devel libdbusmenu-qt52 libdc1394-22 libgdk-pixbuf libgpg-error libgphoto2-6 libgphoto2_port-12 libgst-plugins1.0 libical-devel libjson-c libopencore-amrnb0 libopencore-amrwb0 libp11-kit libpangox-compat libpng-devel libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-sensors libqt5-sql libqt5-svg libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libraw1394-11 libstdc++-devel libwayland-client libwayland-server libxcbutil-keysyms libxkbfile-devel perl pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-gir rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: doxygen eigen3 extra-cmake-modules flex git-core graphviz kde4-marble-devel kde5-kcalcore-devel kde5-kcontacts-devel kde5-libkipi-devel kde5-libksane-devel kde5-pimlibs-devel kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-ki18n-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-knotifyconfig-devel kf5-sonnet-devel kf5-threadweaver-devel libXres-devel libexiv2-devel libexpat-devel libgomp-devel libgphoto2-devel libjasper-devel libjpeg-devel liblcms2-devel liblensfun-devel liblqr-devel libopencv-devel libtiff-devel libusb-devel python-module-google python3-dev qt4-dbus qt5-multimedia-devel qt5-webkit-devel qt5-x11extras-devel rpm-build-ruby sqlite3 zlib-devel-static
BuildRequires: doxygen eigen3 extra-cmake-modules flex graphviz
BuildRequires: qt5-multimedia-devel qt5-webengine-devel qt5-x11extras-devel qt5-xmlpatterns-devel
BuildRequires: libqtav-devel
BuildRequires: libXres-devel libexiv2-devel libexpat-devel libgomp-devel libgphoto2-devel libjasper-devel libjpeg-devel libpng-devel
BuildRequires: liblcms2-devel liblensfun-devel liblqr-devel libtiff-devel libusb-devel libtbb-devel libxml2-devel libxslt-devel
BuildRequires: libEGL-devel libGL-devel libGLU-devel
BuildRequires: libImageMagick-devel
BuildRequires: sqlite3 zlib-devel
BuildRequires: kde5-marble-devel
BuildRequires: kde5-akonadi-devel kde5-akonadi-mime-devel kde5-kcalcore-devel kde5-kcontacts-devel kde5-kmime-devel kde5-kcalcore-devel
BuildRequires: kde5-libkipi-devel kde5-libksane-devel kde5-akonadi-contacts-devel
BuildRequires: kf5-kdelibs4support-devel kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kfilemetadata-devel kf5-ki18n-devel kf5-kinit-devel
BuildRequires: kf5-kio-devel kf5-kitemmodels-devel kf5-knotifyconfig-devel kf5-sonnet-devel kf5-threadweaver-devel
%if_enabled mysql
BuildRequires: libmysqlclient-devel
%endif
%if_enabled baloo
BuildRequires: kf5-baloo-devel
%endif
%if_enabled opencv3
BuildRequires: libopencv-devel-static
%endif

Source0: %rname-%version.tar
Source1: po.tar
Source2: doc.tar
Source3: doc-translated.tar
Source10: mysql_install_db
# ALT
Patch100: alt-libraw-aarch64.patch
Patch101: alt-exiv2-req.patch
Patch102: alt-own-mysql-install-db.patch

%description
DigiKam is an advanced digital photo management application for KDE.
Photos can be collected into albums which can be sorted chronologically,
by directory layout or by custom collections.
DigiKam also provides tagging functionality. Images can be tagged despite of
their position and digiKam provides fast and intuitive ways to browse them.
User comments and customized meta-information added to images, are stored
into a database and retrieved to make them available into the user interface.
As soon as the camera is plugged in digikam allows you to preview, download,
upload and delete images.
DigiKam also includes tools like Image Editor, to modify photos using plugins
such as red eye correction or Gamma correction, exif management,...
Light Table to make artistic photos and an external image editor such
as Showfoto.
DigiKam also uses KIPI plugins (KDE Image Plugin Interface) to increase
its functionalities.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package -n %libdigikamdatabase
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libdigikamdatabase
%name library

%package -n %libdigikamcore
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libdigikamcore
%name library

%package -n %libdigikamgui
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libdigikamgui
%name library

%package data
Group: Graphics
Summary: A Photo Management Application for KDE
Requires: %name-common = %version-%release
BuildArch: noarch
%description data
DigiKam is an advanced digital photo management application for KDE.
Photos can be collected into albums which can be sorted chronologically,
by directory layout or by custom collections.
DigiKam also provides tagging functionality. Images can be tagged despite of
their position and digiKam provides fast and intuitive ways to browse them.
User comments and customized meta-information added to images, are stored
into a database and retrieved to make them available into the user interface.
As soon as the camera is plugged in digikam allows you to preview, download,
upload and delete images.
DigiKam also includes tools like Image Editor, to modify photos using plugins
such as red eye correction or Gamma correction, exif management,...
Light Table to make artistic photos and an external image editor such
as Showfoto.
DigiKam also uses KIPI plugins (KDE Image Plugin Interface) to increase
its functionalities.

%package devel
Group: Development/KDE and QT
Summary: Development files for %label
%description devel
Development files for %label.

%prep
%setup -n %rname-%version  -a1 -a2 -a3
%patch100 -p1
%patch101 -p1
%patch102 -p1

# change double to qreal for casting on arm
#find -type f -name \*.cpp | \
#while read f ; do
#    sed -i 's|<double>|<qreal>|g' $f
#done
#find -type f -name \*.h | \
#while read f ; do
#    sed -i 's|<double>|<qreal>|g' $f
#done

#sed -i 's|add_subdirectory|ECM_OPTIONAL_ADD_SUBDIRECTORY|' doc-translated/CMakeLists.txt
#rm -rf doc-translated/showfoto
rm -rf doc-translated/sv/
sed -i '/add_subdirectory.*sv.*/d' doc-translated/CMakeLists.txt

cat >> CMakeLists.txt <<__EOF__
find_package(KF5I18n CONFIG REQUIRED)
ki18n_install(po)
find_package(KF5 ${KF5_MIN_VERSION} REQUIRED COMPONENTS DocTools)
ECM_OPTIONAL_ADD_SUBDIRECTORY(doc)
ECM_OPTIONAL_ADD_SUBDIRECTORY(doc-translated)
__EOF__

find -type f -name CMakeLists.txt -o -name \*Target.cmake | \
while read f ; do
    sed -i '/^set_target_properties.*digikam.*SOVERSION.*DIGIKAM_VERSION_SHORT/s|\(SOVERSION.*\)DIGIKAM_VERSION_SHORT}|\1DIGIKAM_MAJOR_VERSION}|' $f
%if_disabled obsolete_kde4
    sed -i 's|${DATA_INSTALL_DIR}/digikam|${KDE_INSTALL_DATADIR_KF5}/digikam|' $f
%endif
done

%build
%K5build \
%ifarch ppc64le
    -DENABLE_FACESENGINE_DNN=OFF \
%endif
    -DENABLE_QWEBENGINE=ON \
    -DENABLE_INTERNALMYSQL=%{?_enable_mysql:ON}%{!_enable_mysql:OFF} \
    -DENABLE_MYSQLSUPPORT=%{?_enable_mysql:ON}%{!_enable_mysql:OFF} \
    -DENABLE_KFILEMETADATASUPPORT=%{?_enable_baloo:ON}%{!?_enable_baloo:OFF} \
    -DBUILD_TESTING=OFF \
    -DENABLE_OPENCV3=%{?_enable_opencv3:ON}%{!?_enable_opencv3:OFF} \
    #

%install
%K5install
%K5install_move data kconf_update solid
%if_disabled obsolete_kde4
%K5install_move data showfoto locale
%endif
install -m 0755 %SOURCE10 %buildroot/%_K5bin/digikam_mysql_install_db
rm -f %buildroot/%_K5i18n/*/*/kipiplugin*
rm -f %buildroot/%_datadir/locale/*/*/kipiplugin*
rm -f %buildroot/%_K5i18n/*/*/lib*
rm -f %buildroot/%_datadir/locale/*/*/lib*
rm -rf %buildroot/%_K5doc/*/kipi-plugins
%find_lang --with-kde %rname
%find_lang --with-kde --append --output=%rname.lang showfoto

%files common
%dir %_datadir/%rname/
%if_enabled obsolete_kde4
%dir %_datadir/showfoto/
%else
%dir %_K5data/%rname/
%dir %_K5data/showfoto/
%endif

%files
%_K5bin/%rname
%_K5bin/digikam_mysql_install_db
%_datadir/%rname/utils/
%_K5bin/showfoto
%_K5bin/cleanup_digikamdb
%_K5bin/digitaglinktree
%_K5plug/digikam/
%_K5xdgapp/*.desktop
%_K5xmlgui/%rname/
%_K5xmlgui/showfoto/
%_K5notif/%rname.notifyrc
%_K5data/solid/actions/%rname-*.desktop
%if_enabled obsolete_kde4
%_datadir/metainfo/*.xml
%endif

%files data -f %rname.lang
#%doc AUTHORS ChangeLog HACKING NEWS README* TODO
%if_enabled obsolete_kde4
%_datadir/%rname/about/
%_datadir/%rname/colorschemes/
%_datadir/%rname/data/
%_datadir/%rname/database/
%_datadir/%rname/facesengine/
%_datadir/%rname/geoiface/
%_datadir/%rname/geolocationedit/
%_datadir/%rname/metadata/
%_datadir/%rname/profiles/
%_datadir/%rname/templates/
%_datadir/%rname/themes/
%_datadir/showfoto/*
%else
%_K5data/%rname/*
%_K5data/showfoto/*
%endif
%_K5icon/hicolor/*/apps/%rname.*
%_K5icon/hicolor/*/apps/dk-*.*
%_K5icon/hicolor/*/apps/showfoto.*
%_K5icon/hicolor/*/apps/panorama.*
%_K5icon/hicolor/*/apps/expoblending.*
%_K5icon/hicolor/*/actions/tag-*.*
%_K5icon/hicolor/*/actions/albumfolder-*.*
%_K5icon/hicolor/*/actions/tag.*
%_K5icon/hicolor/*/actions/overexposure.*
%_K5icon/hicolor/*/actions/underexposure.*

%files devel
%_K5link/*.so
%_includedir/digikam/
%_libdir/cmake/Digikam*/

%files -n %libdigikamdatabase
%_K5lib/libdigikamdatabase.so.%sover
%_K5lib/libdigikamdatabase.so.*
%files -n %libdigikamcore
%_K5lib/libdigikamcore.so.%sover
%_K5lib/libdigikamcore.so.*
%files -n %libdigikamgui
%_K5lib/libdigikamgui.so.%sover
%_K5lib/libdigikamgui.so.*

%changelog
* Thu Sep 19 2019 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Thu Aug 15 2019 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Wed Jul 03 2019 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt3
- fix to build on ppc64le

* Tue Jun 04 2019 Pavel Moseev <mars@altlinux.org>  6.1.0-alt2
- update translation

* Tue May 07 2019 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- new version

* Mon Mar 04 2019 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt1
- new version

* Thu May 31 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt2
- build with mysql

* Fri Mar 30 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt1
- new version

* Fri Mar 02 2018 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt2
- rebuild with new libKF5CalendarCore

* Mon Feb 05 2018 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Thu Sep 28 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt2
- decrease exiv2 requirement

* Tue Sep 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt1
- new version

* Mon Jul 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Wed Jan 18 2017 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Mon Nov 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.M80P.1
- build for M80P

* Fri Nov 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Mon Sep 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.2.0-alt1
- new version

* Wed Aug 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt1
- new version

* Fri Jul 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt4
- fix requires
- fix solid actions

* Fri Jul 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt3
- fix requires

* Mon Jul 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt2
- split libraries

* Mon Jul 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt1
- initial build
