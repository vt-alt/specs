
%global qt_module qttools
%def_disable bootstrap
%def_disable qtconfig

%define kf5_bindir %prefix/lib/kf5/bin

Name: qt5-tools
Version: 5.12.9
Release: alt2
%define major %{expand:%(X='%version'; echo ${X%%%%.*})}
%define minor %{expand:%(X=%version; X=${X%%.*}; echo ${X#*.})}
%define bugfix %{expand:%(X='%version'; echo ${X##*.})}

Group: System/Libraries
Summary: Qt5 - QtTool components
Url: http://qt.io/
License: LGPLv2 / GPLv3

Requires: %name-common = %EVR

Source: %qt_module-everywhere-src-%version.tar

Source20: assistant.desktop
Source21: designer.desktop
Source22: linguist.desktop
Source23: qdbusviewer.desktop
Source24: qtconfig.desktop

# FC
Patch1: qttools-opensource-src-5.5.0-qmake-qt5.patch
# ALT
Patch10: alt-build-qtconfig.patch

# Automatically added by buildreq on Tue Oct 01 2013 (-bi)
# optimized out: elfutils libGL-devel libgst-plugins libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-v8 libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-xml libstdc++-devel pkg-config python-base python3 python3-base qt5-base-devel qt5-declarative-devel ruby ruby-stdlibs
#BuildRequires: desktop-file-utils gcc-c++ glibc-devel-static python-module-distribute qt5-webkit-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-ubt rpm-macros-qt5
%ifnarch %e2k
BuildRequires: clang-devel llvm-devel
%endif
BuildRequires: desktop-file-utils gcc-c++ glibc-devel libicu-devel
%if_enabled qtconfig
BuildRequires: /usr/bin/convert
%endif
BuildRequires: qt5-base-devel qt5-declarative-devel-static qt5-xmlpatterns-devel
#BuildRequires: qt5-webkit-devel
BuildRequires: libXext-devel libX11-devel
#BuildRequires: gstreamer-devel gst-plugins-devel
BuildRequires: libxslt-devel libudev-devel libgio-devel libsqlite3-devel
BuildRequires: rpm-macros-alternatives
%if_disabled bootstrap
BuildRequires: qt5-tools
%endif

%description
%summary.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: qt5-base-common
BuildArch: noarch
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt5-base-devel
Requires: %name
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

%package -n qt5-assistant
Group: Text tools
Summary: Documentation browser for Qt5
Requires: %name-common = %EVR
Requires: %name = %EVR
%description -n qt5-assistant
%summary.

%package -n qt5-designer
Group: Development/KDE and QT
Summary: Designer for the Qt5
Requires: %name-common = %EVR
Requires: %name = %EVR
Provides: qt5-linguist = %EVR
%description -n qt5-designer
%summary.

%package -n qt5-dbus
Group: System/Configuration/Other
Summary: This package contains D-Bus utilities for Qt5
Requires: %name-common = %EVR
%description -n qt5-dbus
This package contains D-Bus utilities for Qt5.

%package -n qt5-qtconfig
Group: System/Configuration/Other
Summary: A configuration tool for Qt5
Requires: %name-common = %EVR
%description -n qt5-qtconfig
This package contains a configuration tool for Qt5.

%package -n libqt5-uitools
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common = %EVR
%description -n libqt5-uitools
%summary

%package -n libqt5-clucene
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common = %EVR
%description -n libqt5-clucene
%summary

%package -n libqt5-designer
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
%description -n libqt5-designer
%summary

%package -n libqt5-designercomponents
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
%description -n libqt5-designercomponents
%summary

%package -n libqt5-help
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
%description -n libqt5-help
%summary

%prep
%setup -n %qt_module-everywhere-src-%version
%patch1 -p1
%if_enabled qtconfig
%patch10 -p1
%endif

%build
# needed for documentation generation
# when some Qt header include paths
# are specified using '-isystem $path' arguments
%add_optflags -DQDOC_PASS_ISYSTEM

%qmake_qt5
%make_build
%if_disabled bootstrap
export QT_HASH_SEED=0
%make docs
%endif

%install
>main.filelist
%install_qt5
%make INSTALL_ROOT=%buildroot install_docs

# fix pc-files
sed -i -e '/^Requires:/s/Qt5UiPlugin//' %buildroot/%_pkgconfigdir/*.pc

# Add desktop files
desktop-file-install \
  --dir=%buildroot/%_desktopdir \
  --vendor="qt5" \
  %SOURCE20 %SOURCE21 %SOURCE22 %SOURCE23 \
%if_enabled qtconfig
  %SOURCE24 \
%endif
  #

# install qdbus alternative
QDBUS_ALTPRIO=`printf '%%.2d%%.2d%%.2d%%.2d\n' 0 %major %minor %bugfix`
mkdir -p %buildroot/%_altdir/
cat > %buildroot/%_altdir/qdbus-%_qt5 <<__EOF__
%_bindir/qdbus %_qt5_bindir/qdbus $QDBUS_ALTPRIO
__EOF__
cat > %buildroot/%_altdir/qdbusviewer-%_qt5 <<__EOF__
%_bindir/qdbusviewer %_qt5_bindir/qdbusviewer $QDBUS_ALTPRIO
__EOF__
mkdir -p %buildroot%kf5_bindir/
#ln -s `relative %_bindir/qdbus-%_qt5 %kf5_bindir/qdbus` %buildroot%kf5_bindir/qdbus
#ln -s `relative %_bindir/qtpaths-%_qt5 %kf5_bindir/qtpaths` %buildroot%kf5_bindir/qtpaths
for qt_tool in qdbus qtpaths
do
    ln -s `relative %_bindir/${qt_tool}-%_qt5 %kf5_bindir/${qt_tool}` %buildroot%kf5_bindir/${qt_tool}
done

# icons
install -m644 -p -D src/assistant/assistant/images/assistant.png %buildroot/%_iconsdir/hicolor/32x32/apps/assistant-qt5.png
install -m644 -p -D src/assistant/assistant/images/assistant-128.png %buildroot/%_iconsdir/hicolor/128x128/apps/assistant-qt5.png
install -m644 -p -D src/designer/src/designer/images/designer.png %buildroot/%_iconsdir/hicolor/128x128/apps/designer-qt5.png
install -m644 -p -D src/qdbus/qdbusviewer/images/qdbusviewer.png %buildroot/%_iconsdir/hicolor/32x32/apps/qdbusviewer-qt5.png
install -m644 -p -D src/qdbus/qdbusviewer/images/qdbusviewer-128.png %buildroot/%_iconsdir/hicolor/128x128/apps/qdbusviewer-qt5.png
%if_enabled qtconfig
convert -resize 32x32 src/qtconfig/images/appicon.png %buildroot/%_iconsdir/hicolor/32x32/apps/qtconfig-qt5.png
%endif
# linguist icons
for icon in src/linguist/linguist/images/icons/linguist-*-32.png ; do
  size=$(echo $(basename ${icon}) | cut -d- -f2)
  install -p -m644 -D ${icon} %buildroot/%_iconsdir/hicolor/${size}x${size}/apps/linguist-qt5.png
done

if [ -e %buildroot/%_qt5_bindir/qdoc ] ; then
cat >>main.filelist <<__EOF__
%_bindir/qdoc*
%_qt5_bindir/qdoc*
__EOF__
fi

%files common
%_qt5_datadir/phrasebooks/

%files -f main.filelist
%_bindir/lconvert*
%_bindir/lrelease*
%_bindir/lupdate*
%_bindir/pixeltool*
%_bindir/qcollectiongenerator*
%_bindir/qhelpgenerator*
%_bindir/qtpaths*
%_bindir/qtdiag*
%_bindir/qtplugininfo*
%_bindir/qtattributionsscanner*
%_bindir/qdistancefieldgenerator*
%_qt5_bindir/lconvert*
%_qt5_bindir/lrelease*
%_qt5_bindir/lupdate*
%_qt5_bindir/pixeltool*
%_qt5_bindir/qcollectiongenerator*
%_qt5_bindir/qhelpgenerator*
%_qt5_bindir/qtpaths*
%_qt5_bindir/qtdiag*
%_qt5_bindir/qtplugininfo*
%_qt5_bindir/qtattributionsscanner*
%_qt5_bindir/qdistancefieldgenerator*
%kf5_bindir/qtpaths

%if_enabled qtconfig
%files -n qt5-qtconfig
%_bindir/qtconfig-qt5
%_qt5_bindir/qtconfig
%_desktopdir/*qtconfig.desktop
%_iconsdir/hicolor/*/apps/qtconfig*.*
%endif

%files -n qt5-assistant
%_bindir/assistant-qt5
%_qt5_bindir/assistant
%_desktopdir/*assistant.desktop
%_iconsdir/hicolor/*/apps/assistant*.*
%if_disabled bootstrap
%_qt5_docdir/qtassistant/
%_qt5_docdir/qtassistant.qch
%endif

%files -n qt5-dbus
%_altdir/qdbus-%_qt5
%_bindir/qdbus-qt5
%_qt5_bindir/qdbus
%kf5_bindir/qdbus
%_altdir/qdbusviewer-%_qt5
%_bindir/qdbusviewer*
%_qt5_bindir/qdbusviewer*
%_desktopdir/*qdbusviewer.desktop
%_iconsdir/hicolor/*/apps/qdbusviewer*.*

%files -n qt5-designer
%_bindir/designer*
%_bindir/linguist*
%_qt5_bindir/linguist*
%_qt5_bindir/designer*
%_qt5_plugindir/designer/lib*.so
%_desktopdir/*designer.desktop
%_desktopdir/*linguist.desktop
%_iconsdir/hicolor/*/apps/designer*.*
%_iconsdir/hicolor/*/apps/linguist*.*

%files devel
#%_qt5_headerdir/QtCLucene/
%_qt5_headerdir/QtDesigner/
%_qt5_headerdir/QtDesignerComponents/
%_qt5_headerdir/QtHelp/
%_qt5_headerdir/QtUiTools/
%_qt5_headerdir/QtUiPlugin/
%_qt5_libdir/libQt*.prl
%_qt5_libdatadir/libQt*.prl
%_qt5_libdir/libQt*.so
%_qt5_libdatadir/libQt*.so
#%_qt5_libdir/pkgconfig/Qt*CLucene.pc
#%_qt5_libdir/pkgconfig/Qt*DesignerComponents.pc
%_qt5_libdir/pkgconfig/Qt*Designer.pc
%_qt5_libdir/pkgconfig/Qt*Help.pc
%_qt5_libdir/pkgconfig/Qt*UiPlugin.pc
%_qt5_archdatadir/mkspecs/modules/*.pri
%_libdir/cmake/Qt*/

%files devel-static
%_qt5_libdir/libQt?*.a
%_qt5_libdatadir/libQt?*.a
%_pkgconfigdir/Qt?UiTools.pc

%files doc
%if_disabled bootstrap
%_qt5_docdir/*
%exclude %_qt5_docdir/qtassistant/
%exclude %_qt5_docdir/qtassistant.qch
%endif
%_qt5_examplesdir/*

#%files -n libqt5-uitools
#%_qt5_libdir/libQt5UiTools.so.*
#%files -n libqt5-clucene
#%_qt5_libdir/libQt5CLucene.so.*
%files -n libqt5-designer
%_qt5_libdir/libQt5Designer.so.*
%files -n libqt5-designercomponents
%_qt5_libdir/libQt5DesignerComponents.so.*
%files -n libqt5-help
%_qt5_libdir/libQt5Help.so.*

%changelog
* Fri Jul 03 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.9-alt2
- build docs

* Mon Jun 22 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.9-alt1
- new version

* Thu Apr 16 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt2
- build docs

* Thu Apr 09 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt1
- new version

* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.12.7-alt3
- Fixed docs generation

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt2
- build docs

* Thu Feb 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version

* Mon Dec 16 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1
- new version

* Fri Oct 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt2
- build docs

* Mon Oct 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1
- new version

* Wed Aug 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt2
- fix build requires for e2k

* Mon Jun 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1
- new version

* Thu Apr 25 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version

* Wed Mar 06 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Mon Sep 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1%ubt
- new version

* Thu Aug 16 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt2%ubt
- build docs

* Fri Aug 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt1%ubt
- new version

* Thu Jul 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.6-alt2%ubt
- fix menu items russian translation, icons

* Wed Jun 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.6-alt1%ubt
- new version

* Tue Apr 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1%ubt
- new version

* Wed Mar 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt.2
- build docs

* Mon Feb 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt.1
- don't build docs

* Thu Jan 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1%ubt
- new version

* Tue Dec 05 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1%ubt
- new version

* Mon Oct 23 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt2%ubt
- build docs

* Fri Oct 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1%ubt
- new version

* Thu Dec 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1%ubt
- new version

* Fri Oct 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1.M80P.1
- build for M80P

* Fri Oct 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt2
- add qtpaths to KDE5 PATH

* Sun Oct 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt0.M80P.1
- build for M80P

* Wed Oct 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1
- new version

* Mon Jun 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Tue May 31 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt3
- hide qdbusviewer from menu

* Thu Mar 31 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt2
- build docs

* Thu Mar 24 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Tue Nov 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt2
- fix find qmake

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Fri Sep 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt2
- add alternavices for qdbus and qdbusviewer

* Mon Jul 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Tue Jun 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Tue Dec 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Wed Sep 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Wed Jun 25 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Tue Jun 03 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Thu Feb 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.M70P.1
- built for M70P

* Thu Feb 13 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- new version

* Wed Jan 29 2014 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt5.M70P.1
- built for M70P

* Wed Jan 29 2014 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt6
- fix cmake config file (ALT#29761)

* Tue Jan 28 2014 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt4.M70P.1
- built for M70P

* Tue Jan 28 2014 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt5
- fix paths in cmake config (ALT#29761)

* Tue Nov 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt3.M70P.2
- build docs

* Mon Nov 25 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt3.M70P.1
- built for M70P

* Thu Oct 31 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt4
- built qtconfig

* Fri Oct 25 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt3
- built docs

* Wed Oct 23 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt2
- move static libs to separate package

* Mon Sep 30 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build

