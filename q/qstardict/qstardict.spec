%def_disable plasma

Name: qstardict
Version: 1.3
Release: alt1

Summary: QStarDict Qt clone of StarDict
License: GPLv2
Group: System/Internationalization
Url: http://qstardict.ylsoftware.com

Source: %name-%version.tar
Source10: qstardict-ru_RU.ts
Patch1: alt-l10n.patch

# Automatically added by buildreq on Mon Dec 18 2017 (-bi)
# optimized out: desktop-file-utils elfutils gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 kde5-kcalcore-devel kde5-kcontacts-devel kde5-kmime-devel kde5-libkleo-devel kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjs-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libGL-devel libX11-devel libdbusmenu-qt52 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base python3-module-yieldfrom qt5-base-common qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-tools qt5-webchannel-devel rpm-build-python3 ruby ruby-stdlibs xorg-kbproto-devel xorg-xproto-devel
#BuildRequires: kde5-akonadi-calendar-devel kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-akonadi-notes-devel kde5-calendarsupport-devel kde5-eventviews-devel kde5-grantleetheme-devel kde5-incidenceeditor-devel kde5-kalarmcal-devel kde5-kcalutils-devel kde5-kdav-devel kde5-kdb-devel kde5-kholidays-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kmailtransport-devel kde5-kmbox-devel kde5-kpimtextedit-devel kde5-ktnef-devel kde5-libgravatar-devel kde5-libkcddb-devel kde5-libkdepim-devel kde5-libksieve-devel kde5-mailcommon-devel kde5-mailimporter-devel kde5-marble-devel kde5-messagelib-devel kde5-pim-apps-libs-devel kde5-pimcommon-devel kde5-syndication-devel kf5-kactivities-devel kf5-kactivities-stats-devel kf5-karchive-devel kf5-kcmutils-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdesu-devel kf5-kdiagram-devel kf5-kdnssd-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kio-devel kf5-kirigami-devel kf5-kitemmodels-devel kf5-kjsembed-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kplotting-devel kf5-kpty-devel kf5-kreport-devel kf5-kross-devel kf5-krunner-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwayland-devel kf5-kxmlrpcclient-devel kf5-libkgapi-devel kf5-libkscreen-devel kf5-modemmanager-qt-devel kf5-networkmanager-qt-devel kf5-prison-devel kf5-syntax-highlighting-devel kf5-threadweaver-devel python-module-google python3-dev python3-module-zope qt5-connectivity-devel qt5-multimedia-devel qt5-phonon-devel qt5-quickcontrols2-devel qt5-script-devel qt5-sensors-devel qt5-serialport-devel qt5-speech-devel qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-webengine-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel qt5-xmlpatterns-devel rpm-build-ruby zlib-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: kf5-kglobalaccel-devel kf5-kwindowsystem-devel kf5-knotifications-devel
%if_enabled plasma
BuildRequires: kf5-plasma-framework-devel kf5-kdelibs4support-devel
%endif
BuildRequires: glib2-devel qt5-base-devel qt5-tools zlib-devel
BuildRequires: desktop-file-utils

Provides: stardict = 2.4.5

%description
QStarDict Qt clone of StarDict.

%package kde5
Group: Graphical desktop/KDE
Summary: QStarDict KDE Plasma integration
Requires: %name
%description kde5
QStarDict KDE Plasma integration

%prep
%setup
%patch1 -p1
cat %SOURCE10 > qstardict/translations/qstardict-ru_RU.ts
%if_enabled plasma
sed -i 's|INCLUDE_DIRECTORIES(|INCLUDE_DIRECTORIES(${CMAKE_CURRENT_BINARY_DIR} |' kdeplasma/dataengine/CMakeLists.txt
%endif
sed -i -E 's|(^[[:space:]]+ENABLED_PLUGINS=.*)|\1 kdeintegration|' plugins/plugins.pri
%qmake_qt5 \
    PLUGINS_DIR=%_libdir/qstardict/plugins \
    "QMAKE_LFLAGS += -L%_K5link" \
    "QT.KGlobalAccel.libs = %_K5link" \
    "QT.KNotifications.libs = %_K5link" \
    "QT.KWindowSystem.libs = %_K5link" \
    #

%build
%make
%if_enabled plasma
pushd kdeplasma
%add_optflags -I%_K5inc/KDELibs4Support/KDE -I%_K5inc/KDELibs4Support
%K5build
popd
%endif

%install
%installqt5
%if_enabled plasma
pushd kdeplasma
%K5install
popd
%endif

desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--add-category=TextTools \
	--add-category=Office \
	%buildroot%_desktopdir/qstardict.desktop

%find_lang %name --all-name --with-qt

%files -f %{name}.lang
%doc AUTHORS ChangeLog README THANKS
%_bindir/%name
%dir %_datadir/%name/
%dir %_datadir/%name/translations/
%_desktopdir/*.desktop
%_iconsdir/*/*/apps/%{name}.*
%dir %_libdir/%name/
%dir %_libdir/%name/plugins/
%_libdir/%name/plugins/*.so
%exclude %_libdir/%name/plugins/libkdeintegration.so

%files kde5
%_libdir/%name/plugins/libkdeintegration.so

%changelog
* Wed Jul 10 2019 Sergey V Turchin <zerg@altlinux.org> 1.3-alt1
- new version

* Mon Apr 08 2019 Sergey V Turchin <zerg@altlinux.org> 1.2-alt4
- update russian translation

* Fri Apr 05 2019 Sergey V Turchin <zerg@altlinux.org> 1.2-alt3
- fix desktop-file translation

* Fri Apr 05 2019 Sergey V Turchin <zerg@altlinux.org> 1.2-alt2
- fix load Qt translation

* Mon Dec 18 2017 Sergey V Turchin <zerg@altlinux.org> 1.2-alt1
- new version

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.0.1-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Mon May 28 2012 Terechkov Evgenii <evg@altlinux.org> 1.0.1-alt1
- 1.0.1

* Fri Apr 27 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt1.2
- rebuilt with rpm optflags

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1
- Fixed build with new glib2

* Thu Jul  7 2011 Terechkov Evgenii <evg@altlinux.org> 1.0-alt1
- 1.0

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.13.1-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for qstardict

* Fri May  8 2009 Terechkov Evgenii <evg@altlinux.ru> 0.13.1-alt2
- Build with gcc4.4 fixed

* Wed Feb 25 2009 Terechkov Evgenii <evg@altlinux.ru> 0.13.1-alt1.1
- Provide: stardict added (closes #18960)

* Fri Feb 20 2009 Terechkov Evgenii <evg@altlinux.ru> 0.13.1-alt1
- 0.13.1

* Sun Feb  8 2009 Terechkov Evgenii <evg@altlinux.ru> 0.13-alt1
- 0.13

* Sat Jun 14 2008 Terechkov Evgenii <evg@altlinux.ru> 0.12.9-alt1.1
- Build for x86_64 fixed (brain-deat upstream defaults)

* Fri Jun 13 2008 Terechkov Evgenii <evg@altlinux.ru> 0.12.9-alt1
- 0.12.9

* Sat Mar 29 2008 Terechkov Evgenii <evg@altlinux.ru> 0.12-alt1
- 0.12

* Wed Mar 26 2008 Terechkov Evgenii <evg@altlinux.ru> 0.10-alt1
- 0.10

* Sun Mar 23 2008 Terechkov Evgenii <evg@altlinux.ru> 0.09-alt1
- 0.09

* Sat Sep 22 2007 Terechkov Evgenii <evg@altlinux.ru> 0.07-alt1
- 0.07
- License changed to GPLv2 (package relicensed)

* Tue Aug 14 2007 Terechkov Evgenii <evg@altlinux.ru> 0.04-alt1.2
- Wrong Provides: tag removed (Shame on me!)

* Fri Aug 10 2007 Terechkov Evgenii <evg@altlinux.ru> 0.04-alt1.1
- gpl3 changed to gpl3plus (due change to rpm-build-licenses)

* Sat Jul 28 2007 Terechkov Evgenii <evg@altlinux.ru> 0.04-alt1
- 0.04

* Sun Jul  8 2007 Terechkov Evgenii <evg@altlinux.ru> 0.03-alt2
- "Fix" conflict with stardict-gtk (see #12267,#12268) by providing stardict=2.4.2

* Sun Jul  8 2007 Terechkov Evgenii <evg@altlinux.ru> 0.03-alt1
- Initial build for Sisyphus
