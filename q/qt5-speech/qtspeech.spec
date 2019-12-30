%define qdoc_found %{expand:%%(if [ -e %_qt5_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtspeech

Name: qt5-speech
Version: 5.12.6
Release: alt1

Group: System/Libraries
Summary: Qt5 - QtSpeech component
Url: http://qt-project.org/
License: LGPLv2 / GPLv3

Source: %qt_module-everywhere-src-%version.tar

# Automatically added by buildreq on Fri Aug 07 2015 (-bi)
# optimized out: elfutils glib2-devel kf5-attica-devel kf5-kjs-devel libqt5-core libstdc++-devel pkg-config python-base python3 python3-base qt5-base-devel qt5-declarative-devel qt5-script-devel qt5-webkit-devel ruby ruby-stdlibs
#BuildRequires: gcc-c++ glibc-devel-static kde5-gpgmepp-devel kf5-bluez-qt-devel kf5-kactivities-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdesu-devel kf5-kdewebkit-devel kf5-kdnssd-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kpeople-devel kf5-kplotting-devel kf5-kpty-devel kf5-kross-devel kf5-krunner-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-kxmlrpcclient-devel kf5-libkscreen-devel kf5-networkmanager-qt-devel kf5-solid-devel kf5-sonnet-devel kf5-threadweaver-devel libdb4-devel libspeechd-devel qt5-connectivity-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel qt5-sensors-devel qt5-serialport-devel qt5-svg-devel qt5-tools-devel qt5-websockets-devel qt5-x11extras-devel qt5-xmlpatterns-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-ubt rpm-macros-qt5 qt5-tools
BuildRequires: gcc-c++ glibc-devel qt5-base-devel qt5-multimedia-devel
BuildRequires: pkg-config glib2-devel
BuildRequires: libspeechd-devel flite-devel libalsa-devel

%description
Qt Speech support.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: qt5-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt5-base-devel
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: %name-devel
%description devel-static
%summary.

%package doc
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-texttospeech
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
%description -n libqt5-texttospeech
%summary.

%prep
%setup -n %qt_module-everywhere-src-%version

ln -s /usr/include config.tests/flite/flite
ln -s /usr/include config.tests/flite_alsa/flite
ln -s /usr/include src/plugins/tts/flite/flite

%build
%qmake_qt5 "QMAKE_CXXFLAGS += -I/usr/include/speech-dispatcher"
%make_build
%if %qdoc_found
%make docs
%endif

%install
%install_qt5
%if %qdoc_found
%make INSTALL_ROOT=%buildroot install_docs ||:
%endif

%files common
%dir %_qt5_plugindir/texttospeech/

%files -n libqt5-texttospeech
%_qt5_libdir/libQt?TextToSpeech.so.*
%_qt5_plugindir/texttospeech/*.so

%files devel
%_qt5_headerdir/Qt*/
%_qt5_libdir/libQt*.so
%_qt5_libdatadir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_libdatadir/libQt*.prl
%_qt5_libdir/cmake/Qt*/
%_qt5_libdir/pkgconfig/Qt*.pc
%_qt5_archdatadir/mkspecs/modules/*.pri

%files doc
%if %qdoc_found
%_qt5_docdir/*
%endif
%_qt5_examplesdir/*

%changelog
* Mon Dec 16 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1
- new version

* Mon Oct 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1
- new version

* Mon Jun 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1
- new version

* Thu Apr 25 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version

* Thu Mar 14 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Mon Sep 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Fri Aug 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt1%ubt
- new version

* Wed Jun 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.6-alt1%ubt
- new version

* Tue Apr 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Thu Jan 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Thu Dec 21 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Fri Aug 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- initial build
