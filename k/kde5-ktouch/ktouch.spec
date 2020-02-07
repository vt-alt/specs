%define rname ktouch

Name: kde5-%rname
Version: 19.12.1
Release: alt1
%K5init

Group: Education
Summary: A program for learning touch typing
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: kde5-kqtquickcharts

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Apr 04 2017 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kdoctools-devel kf5-ki18n-devel kf5-kwidgetsaddons-devel kf5-sonnet-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sql libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libqt5-xmlpatterns libstdc++-devel libxcb-devel libxcbutil-keysyms libxkbfile-devel perl pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel rpm-build-python3 xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: extra-cmake-modules kf5-kcmutils-devel kf5-kcompletion-devel kf5-kdeclarative-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-kitemviews-devel kf5-kpackage-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel libXres-devel python-module-google python3-dev qt5-script-devel qt5-x11extras-devel qt5-xmlpatterns-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules
BuildRequires: qt5-base-devel qt5-script-devel qt5-x11extras-devel qt5-xmlpatterns-devel qt5-quickcontrols2-devel
BuildRequires: desktop-file-utils
BuildRequires: libXres-devel
BuildRequires: kf5-kcmutils-devel kf5-kcompletion-devel kf5-kdeclarative-devel kf5-kdelibs4support kf5-kdoctools-devel-static
BuildRequires: kf5-kitemviews-devel kf5-kpackage-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel
BuildRequires: kf5-kiconthemes-devel

%description
KTouch is a program for learning touch typing. KTouch is a way to learn
to type on a keyboard quickly and correctly. Every finger has its place
on the keyboard with associated keys to press.

KTouch helps you learn to touch typing by providing you with something
to write. KTouch can also help you to remember what fingers to use.


%prep
%setup -n %rname-%version

%build
%K5build \
    -DCOMPILE_QML=OFF \
    #

%install
%K5install
%K5install_move data ktouch
LC_ALL="ru_RU.UTF-8" desktop-file-edit --set-key='Comment[ru]' --set-value="Программа обучения быстрому и точному набору текста" %buildroot/%_K5xdgapp/org.kde.ktouch.desktop
chmod 0755 %buildroot/%_K5xdgapp/org.kde.ktouch.desktop
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/ktouch
%_K5xdgapp/org.kde.ktouch.desktop
%_K5icon/*/*/apps/ktouch.*
%_K5data/ktouch/
%_K5cfg/ktouch.kcfg

%changelog
* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Wed Nov 27 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Thu Aug 29 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Fri Jul 19 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Mon Jun 03 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt2
- update desktop-file russian translation

* Wed May 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Thu Mar 21 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Thu Feb 28 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Thu Jul 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Wed Jun 07 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Thu Mar 16 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- initial build
