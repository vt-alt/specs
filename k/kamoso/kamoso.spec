Name:           kamoso
Version:        19.08.0
Release:        alt1

Group:          Video
Summary:        Application for taking pictures and videos from a webcam
URL:            https://userbase.kde.org/Kamoso

License:        GPLv2+

Source0:        %name-%version.tar
Source1:	%name.watch

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-graphicaleffects
BuildRequires: kf5-kauth-devel
BuildRequires: kf5-kbookmarks-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kirigami-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-kpackage-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-purpose-devel
BuildRequires: kf5-solid-devel
BuildRequires: libkf5quickaddons
BuildRequires: kf5-kdoctools-devel-static
BuildRequires: kf5-kdoctools
BuildRequires: libudev-devel
BuildRequires: gstreamer1.0-devel
BuildRequires: gst-plugins1.0-devel

Requires: libkf5quickaddons
Requires: kf5-purpose

%description
Kamoso is an application to take pictures and videos out of your webcam.

%prep
%setup -q

%build
%add_optflags -I%_libdir/gstreamer-1.0/include
%K5init no_altplace
%K5build

%install
%K5install
%find_lang %name --all

%files -f %name.lang
%doc AUTHORS COPYING* README TODO
%_K5bin/%name
%_K5icon/hicolor/*/*/*.*
%_K5xdgapp/*%name.desktop
%_datadir/metainfo/org.kde.kamoso.appdata.xml
%doc %_K5doc/*/%name
%_datadir/sounds/kamoso-shutter.wav
%_libdir/gstreamer-1.0/gstkamosoqt5videosink.so
%_K5notif/%name.notifyrc

%changelog
* Fri Aug 16 2019 Andrey Cherepanov <cas@altlinux.org> 19.08.0-alt1
- New version.

* Mon Aug 05 2019 Andrey Cherepanov <cas@altlinux.org> 19.07.90-alt1
- New version.

* Mon Jul 22 2019 Andrey Cherepanov <cas@altlinux.org> 19.07.80-alt1
- New version.

* Thu Jul 11 2019 Andrey Cherepanov <cas@altlinux.org> 19.04.3-alt1
- New version.

* Fri Jun 07 2019 Andrey Cherepanov <cas@altlinux.org> 19.04.2-alt1
- New version.

* Thu May 09 2019 Andrey Cherepanov <cas@altlinux.org> 19.04.1-alt1
- New version.

* Fri Apr 19 2019 Andrey Cherepanov <cas@altlinux.org> 19.04.0-alt1
- New version.

* Sat Mar 23 2019 Andrey Cherepanov <cas@altlinux.org> 19.03.80-alt1
- New version.

* Fri Mar 22 2019 Andrey Cherepanov <cas@altlinux.org> 18.12.3-alt2
- Build from actial tag.
- Build without qt5-gstreamer1 (ALT #36345).

* Sat Mar 09 2019 Andrey Cherepanov <cas@altlinux.org> 18.12.3-alt1
- New version.

* Sat Feb 09 2019 Andrey Cherepanov <cas@altlinux.org> 18.12.2-alt1
- New version.

* Fri Jan 11 2019 Andrey Cherepanov <cas@altlinux.org> 18.12.1-alt1
- New version.

* Fri Dec 14 2018 Andrey Cherepanov <cas@altlinux.org> 18.12.0-alt1
- New version.

* Fri Nov 30 2018 Andrey Cherepanov <cas@altlinux.org> 18.11.90-alt1
- New version.

* Sun Nov 18 2018 Andrey Cherepanov <cas@altlinux.org> 18.11.80-alt1
- New version.

* Mon Nov 12 2018 Andrey Cherepanov <cas@altlinux.org> 18.08.3-alt1
- New version.

* Fri Oct 12 2018 Andrey Cherepanov <cas@altlinux.org> 18.08.2-alt1
- New version.

* Fri Sep 14 2018 Andrey Cherepanov <cas@altlinux.org> 18.08.1-alt1
- New version.

* Sun Aug 19 2018 Andrey Cherepanov <cas@altlinux.org> 18.08.0-alt1
- New version.

* Mon Aug 13 2018 Andrey Cherepanov <cas@altlinux.org> 18.07.90-alt1
- New version.

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 18.07.80-alt1
- New version.

* Fri Jul 13 2018 Andrey Cherepanov <cas@altlinux.org> 18.04.3-alt1
- New version.

* Fri Jun 08 2018 Andrey Cherepanov <cas@altlinux.org> 18.04.2-alt1
- New version.

* Fri May 11 2018 Andrey Cherepanov <cas@altlinux.org> 18.04.1-alt1
- New version.

* Mon Apr 23 2018 Andrey Cherepanov <cas@altlinux.org> 18.04.0-alt1
- New version.

* Wed Apr 11 2018 Andrey Cherepanov <cas@altlinux.org> 18.03.90-alt1
- New version.

* Wed Mar 21 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.4-alt1
- New version.
- Add watch file.

* Sat Feb 25 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt1
- new version 3.2.3

* Wed Jun 15 2016 Andrey Cherepanov <cas@altlinux.org> 3.2-alt1
- New version
- New appdata.xml name

* Tue Mar 15 2016 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version used KF5

* Fri Feb 26 2016 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt11
- Build without nepomuk

* Mon Oct 05 2015 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt10
- Fix build with gstreamer1.0

* Mon Sep 29 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt9
- build with qt-gstreamer1

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt7.M70P.1
- built for M70P

* Tue Sep 10 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt8
- built with new libkipi

* Thu Dec 13 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt7
- built with new libkipi

* Fri Oct 12 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt6
- fix desktopfile translation

* Mon Oct 08 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt5
- rebuilt with new kde

* Thu Aug 16 2012 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt4
- Add Russian localization of program

* Thu Aug 16 2012 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt3
- Translate dekstop files on Russian

* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt1.M60P.1
- new version

* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt2
- fix build requires

* Fri Apr 27 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt0.M60P.2
- rebuild

* Fri Feb 24 2012 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt0.M60P.1
- Backport to p6 branch

* Tue Feb 21 2012 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1
- Initial build for Sisyphus
