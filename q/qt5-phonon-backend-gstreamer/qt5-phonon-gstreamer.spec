
Name: qt5-phonon-backend-gstreamer
Version: 4.10.0
Release: alt1

Group: System/Libraries
Summary: Gstreamer phonon backend
License: LGPLv2+
Url: http://phonon.kde.org/

Source: %name-%version.tar

BuildRequires(pre): qt5-base-devel qt5-phonon-devel
BuildRequires: qt5-x11extras-devel qt5-tools-devel
BuildRequires: cmake extra-cmake-modules glibc-devel gst-plugins1.0-devel libalsa-devel libxml2-devel libGL-devel libEGL-devel
BuildRequires: rpm-build-kf5

%description
Gstreamer phonon backend

%package -n qt5-phonon-backend-5-gstreamer
Group: System/Libraries
Summary: Gstreamer phonon backend
Provides: qt5-phonon-backend = %{get_version qt5-phonon-devel}
Provides: qt5-phonon-backend-gstreamer = %EVR qt5-phonon-gstreamer = %EVR
Requires: gst-plugins-base1.0 gst-plugins-good1.0 gst-plugins-bad1.0 gst-plugins-ugly1.0
%description -n qt5-phonon-backend-5-gstreamer
Gstreamer phonon backend

%prep
%setup -q

%build
%add_optflags %optflags_shared -UPIE -U__PIE__
%K5cmake \
    -DPHONON_BUILD_PHONON4QT5=ON \
    -DLOCALE_INSTALL_DIR=%_K5i18n \
    -DINCLUDE_INSTALL_DIR=%_K5inc \
    -DICON_INSTALL_DIR=%_K5icon \
    -DPLUGIN_INSTALL_DIR:PATH=%_qt5_plugindir \
    #
#pushd BUILD*/gstreamer
#for gstheader in gst/gstconfig.h gst/gl/gstglconfig.h ; do
#    if [ ! -e %_includedir/gstreamer-1.0/$gstheader -a -e %_libdir/gstreamer-1.0/include/$gstheader ]
#    then
#	mkdir -p `dirname $gstheader`
#	[ -e $gstheader ] || \
#        ln -s %_libdir/gstreamer-1.0/include/$gstheader $gstheader
#    fi
#done
#popd
%K5make

%install
%K5install
%K5find_qtlang phonon_gstreamer_qt

%files -n qt5-phonon-backend-5-gstreamer -f phonon_gstreamer_qt.lang
%_qt5_plugindir/phonon4qt5_backend/phonon_gstreamer.so
#_K5srv/phononbackends/gstreamer.desktop
%_datadir/kf5/icons/hicolor/*/apps/phonon-gstreamer.*

%changelog
* Fri Jan 17 2020 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt1
- new version

* Wed Aug 28 2019 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt2
- fix build requires

* Mon Jul 22 2019 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Wed Jun 19 2019 Sergey V Turchin <zerg@altlinux.org> 4.9.0-alt3
- dont use ubt macro

* Fri Apr 27 2018 Sergey V Turchin <zerg@altlinux.org> 4.9.0-alt2
- rebuild with new phonon

* Mon Nov 28 2016 Sergey V Turchin <zerg@altlinux.org> 4.9.0-alt0.M80P.1
- build for M80P

* Mon Nov 14 2016 Sergey V Turchin <zerg@altlinux.org> 4.9.0-alt1
- new version

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Tue Mar 24 2015 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt2
- fix icon paths

* Fri Dec 19 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Fri Sep 12 2014 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Mon Sep 01 2014 Sergey V Turchin <zerg@altlinux.org> 4.7.80-alt0.M70P.1
- build for M70P

* Mon Aug 25 2014 Sergey V Turchin <zerg@altlinux.org> 4.7.80-alt1
- new version

* Tue Jul 01 2014 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- initial build
