%def_disable plug_expoblending
%def_disable plug_panorama
%def_disable plug_imgur
%def_disable plug_jalbum

%define libsover 5
%define libkf5kipiplugins libkf5kipiplugins%libsover

%define rname kipi-plugins
Name: kde5-%rname
Version: 5.9.1
Release: alt1
%K5init

Group: Graphics
Summary: KDE image Interface Plugins
License: GPLv2
Url: http://www.kipi-plugins.org/

Source0: %rname-%version.tar
Source1: doc.tar

Requires: %name-core
%if_enabled plug_expoblending
Requires: %name-expoblending
%endif
%if_enabled plug_panorama
Requires: %name-panorama
%endif

# Automatically added by buildreq on Thu Jul 28 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ gtk-update-icon-cache kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kdoctools-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libEGL-devel libGL-devel libgpg-error libqt4-core libqt4-gui libqt4-network libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libqt5-xmlpatterns libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: extra-cmake-modules git-core kde5-libkipi-devel kf5-karchive-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kwindowsystem-devel libkqoauth-devel python-module-google python3-dev qt5-svg-devel qt5-xmlpatterns-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: qt5-svg-devel qt5-xmlpatterns-devel
BuildRequires: libkqoauth-qt5-devel
BuildRequires: kde5-libkipi-devel
BuildRequires: kf5-karchive-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel
BuildRequires: kf5-kwindowsystem-devel

%description
The library of the KDE Image Plugin Interface used by digiKam and Gwenview

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kf5-filesystem
%description common
%name common package

%package core
Group: Graphics
Summary: Core files for %name
Requires: %name-common = %version-%release
# dngconverter/dngwriter/extra/dng_sdk
Requires: icc-profiles
#Requires: /usr/bin/convert
%description core
Core files for %name

%package expoblending
Group: Graphics
Summary: A tool to blend bracketed images
Requires: %name-common = %version-%release
Requires: hugin enblend
%description expoblending
A tool to blend bracketed images

%package panorama
Group: Graphics
Summary: A tool to assemble images as a panorama
Requires: %name-common = %version-%release
Requires: hugin enblend
%description panorama
A tool to assemble images as a panorama

%package -n %libkf5kipiplugins
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n %libkf5kipiplugins
%name library.

%prep
%setup -q -n %rname-%version -a1
rm -rf PORT.KF5

# hide
#echo "NoDisplay=true" >>acquireimages/scangui.desktop

# change double to qreal for casting on arm
find -type f -name \*.cpp | \
while read f ; do
    sed -i 's|<double>|<qreal>|g' $f
done
find -type f -name \*.h | \
while read f ; do
    sed -i 's|<double>|<qreal>|g' $f
done

# set lib soname
find -type f -name CMakeLists.txt | \
while read f ; do
    sed -i '/.*SOVERSION.*KIPIPLUGINS_LIB_SO_VERSION_STRING/s|\(SOVERSION.*\)KIPIPLUGINS_LIB_SO_VERSION_STRING}|\1KIPIPLUGINS_MAJOR_VERSION}|' $f
done

%if_disabled plug_imgur
    sed -i 's|add_subdirectory(imgur)||' CMakeLists.txt
    rm -rf imgur
%endif
%if_disabled plug_jalbum
    sed -i 's|add_subdirectory(jalbum)||' CMakeLists.txt
    rm -rf jalbum
%endif

# build docs
cat >> CMakeLists.txt <<__EOF__
find_package(KF5 ${KF5_MIN_VERSION} REQUIRED COMPONENTS DocTools)
ECM_OPTIONAL_ADD_SUBDIRECTORY(doc)
__EOF__

%build
%K5build

%install
%K5install
%K5install_move data locale kipiplugin_flashexport kipiplugin_piwigo kipiplugin_printimages

rm -f %buildroot/%_K5i18n/*/*/digikam*
rm -f %buildroot/%_K5i18n/*/*/libkvkontakte*
%find_lang --with-kde %rname
find %buildroot/%_K5i18n -type f -name kipiplugin\*.mo | sed "s|\.mo$||" | \
while read f; do echo `basename "$f"`; done | sort -u | \
while read n
do
    %find_lang --with-kde --append --output=%rname.lang "$n"
done

%files
%files common -f %rname.lang
%dir %_K5xmlgui/kipi/
%_K5icon/hicolor/*/apps/kipi-*.*

%files core
%doc AUTHORS ChangeLog README TODO NEWS COPYING-*

%_K5plug/kipiplugin_*.so
%_K5srv/kipiplugin_*.desktop
%_K5xmlgui/kipi/kipiplugin_*.rc
%_K5xdgapp/kipiplugins.desktop
%_K5data/kipiplugin_*/

%if_enabled plug_expoblending
# exclude expoblending
%exclude %_K5plug/kipiplugin_expoblending.so
%exclude %_K5srv/kipiplugin_expoblending.desktop
%exclude %_K5data/kipiplugin_expoblending
%endif
%if_enabled plug_panorama
# exclude panorama
%exclude %_K5plug/kipiplugin_panorama.so
%exclude %_K5data/kipi/kipiplugin_panoramaui.rc
%exclude %_K5data/kipiplugin_panorama/
%exclude %_K5srv/kipiplugin_panorama.desktop
%endif

%if_enabled plug_expoblending
%files expoblending
%_K5bin/expoblending
%_K5plug/kipiplugin_expoblending.so
%_K5data/kipiplugin_expoblending
%_K5srv/kipiplugin_expoblending.desktop
%_K5xdgapp/expoblending.desktop
%endif

%if_enabled plug_panorama
%files panorama
%_K5bindir/panoramagui
%_K5plug/kipiplugin_panorama.so
%_K5data/kipi/kipiplugin_panoramaui.rc
%_K5data/kipiplugin_panorama/
%_K5srv/kipiplugin_panorama.desktop
%_K5xdgapp/panoramagui.desktop
%endif

%files -n %libkf5kipiplugins
%_K5lib/libKF5kipiplugins.so.%libsover
%_K5lib/libKF5kipiplugins.so.%libsover.*

%changelog
* Thu Sep 19 2019 Sergey V Turchin <zerg@altlinux.org> 5.9.1-alt1
- new version

* Fri Feb 08 2019 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt3
- fix build requires

* Tue Nov 06 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt2
- remove jalbum plugin

* Fri Mar 30 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt1
- new version

* Mon Feb 05 2018 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Wed Sep 27 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt1
- new version

* Mon Jul 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Thu Jan 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Mon Nov 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.M80P.1
- build for M80P

* Fri Nov 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Mon Sep 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.2.0-alt1
- new version

* Wed Aug 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt1
- new version

* Tue Aug 02 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt2
- disable imgur plugin

* Thu Jul 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt1
- initial build
