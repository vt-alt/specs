%define rname konqueror

%def_disable text2speech

%define kf5konq_sover 6
%define libkf5konq libkf5konq%kf5konq_sover
%define konquerorprivate_sover 5
%define libkonquerorprivate libkonquerorprivate%konquerorprivate_sover
%define konqsidebarplugin_sover 5
%define libkonqsidebarplugin libkonqsidebarplugin%konqsidebarplugin_sover

Name: kde5-%rname
Version: 19.08.0
Release: alt1
%K5init

Group: Networking/WWW
Summary: Web browser for KDE
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

PreReq(post,preun): alternatives >= 0.2
Requires: indexhtml
Provides: webclient %_bindir/xbrowser %_bindir/x-www-browser
Provides: kde5-www-browser
Provides: kde5-konqueror-plugins = %version-%release
Obsoletes: kde5-konqueror-plugins < %version-%release
Provides: kf5-konqueror-plugins = %version-%release
Obsoletes: kf5-konqueror-plugins < %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Mar 29 2017 (-bi)
# optimized out: alternatives cmake cmake-modules desktop-file-utils docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ gtk-update-icon-cache kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbusmenu-qt52 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-svg libqt5-test libqt5-webchannel libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel libxcbutil-keysyms libxkbfile-devel perl python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-webchannel-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: extra-cmake-modules kf5-kactivities-devel kf5-kcmutils-devel kf5-kded kf5-kded-devel kf5-kdelibs4support-devel kf5-kdesu-devel kf5-kdoctools-devel-static kf5-khtml-devel kf5-kio-devel kf5-kjs-devel kf5-kpty-devel libXres-devel libtidy-devel python-module-google python3-dev qt5-script-devel qt5-webengine-devel qt5-x11extras-devel rpm-build-ruby zlib-devel-static
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-script-devel qt5-webengine-devel qt5-x11extras-devel
BuildRequires: libXres-devel libtidy-devel zlib-devel
BuildRequires: kf5-kactivities-devel kf5-kcmutils-devel kf5-kded kf5-kded-devel kf5-kdelibs4support-devel
BuildRequires: kf5-kdesu-devel kf5-kdoctools-devel-static kf5-khtml-devel kf5-kio-devel kf5-kjs-devel kf5-kpty-devel
BuildRequires: kf5-kwallet-devel

%if_enabled text2speech
BuildRequires: qt5-speech-devel
%endif

%description
Web browser for KDE

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Conflicts: kde5-baseapps-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkf5konq
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %EVR
%description -n %libkf5konq
KF5 library

%package -n %libkonquerorprivate
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %EVR
%description -n %libkonquerorprivate
KF5 library

%package -n %libkonqsidebarplugin
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %EVR
%description -n %libkonqsidebarplugin
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
#if [ -d %buildroot/%_K5data/konqueror ] ; then
#    cp -arl %buildroot/%_K5data/konqueror/* %buildroot/%_datadir/konqueror/
#    rm -rf %buildroot/%_K5data/konqueror/
#fi
%K5install_move data akregator doc dolphinpart domtreeviewer fsview kcmcss kcontrol khtml kwebkitpart templates konqueror webenginepart

# install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/kde5-konqueror <<__EOF__
%_bindir/xbrowser       %_K5bin/konqueror      61
%_bindir/x-www-browser       %_K5bin/konqueror      61
__EOF__

# terminate nspluginviewer
install -d %buildroot/%_sysconfdir/cron.daily/
cat > %buildroot/%_sysconfdir/cron.daily/kde5-nsplugins <<__EOF__
#!/bin/sh
killall nspluginviewer >/dev/null 2>&1 ||:
sleep 2s
killall -9 nspluginviewer >/dev/null 2>&1 ||:
__EOF__
chmod 0755 %buildroot/%_sysconfdir/cron.daily/kde5-nsplugins

# add mime types categories
#
desktop-file-install --mode=0755 --dir %buildroot/%_K5xdgapp \
    --add-mime-type=x-scheme-handler/http \
    --add-mime-type=x-scheme-handler/https \
    %buildroot/%_K5xdgapp/kfmclient_html.desktop
#
#desktop-file-install --mode=0755 --dir %buildroot/%_K5xdgapp \
#    --add-mime-type=x-scheme-handler/ftp \
#    --add-mime-type=x-scheme-handler/trash \
#    %buildroot/%_K5xdgapp/kfmclient_dir.desktop
rm -f %buildroot/%_K5xdgapp/kfmclient_dir.desktop

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_K5icon/*/*/apps/konqueror.*
%_K5icon/*/*/apps/fsview.*
%_K5icon/*/*/apps/webengine.*
%_K5icon/*/*/actions/htmlvalidator.*
%_K5icon/*/*/actions/validators.*
%_K5icon/*/*/actions/babelfish.png
%_K5icon/*/*/actions/cssvalidator.png
%_K5icon/*/*/actions/imagegallery.png
%_K5icon/*/*/actions/webarchiver.png
%_K5srvtyp/*.desktop
%_datadir/qlogging-categories5/*.*categories

%files
%config /%_sysconfdir/alternatives/packages.d/kde5-konqueror
%config(noreplace) %_K5xdgconf/*
%_K5bin/konqueror
%_K5bin/kfmclient
%_K5bin/fsview
%_K5lib/libkdeinit5_konqueror.so
%_K5lib/libkdeinit5_kfmclient.so
%_K5lib/libkwebenginepart.so
%_K5plug/*.so
%_K5plug/kf5/kfileitemaction/*.so
%_K5plug/kf5/parts/*.so
%_K5start/konqy_preload.desktop
%_K5data/fsview/
%_K5data/kbookmark/
%_K5data/konqueror/
%_K5data/khtml/
%_K5data/kwebkitpart/
%_K5data/webenginepart/
%_K5data/kcmcss/
%_K5data/dolphinpart/
%_K5data/domtreeviewer/
%_K5data/akregator/pics/*
%_K5data/kcontrol/pics/*
%_K5cfg/*.kcfg
%_K5srv/*.desktop
%_K5xdgapp/*.desktop
%_K5xmlgui/*/
%if_enabled text2speech
%_K5plug/khtmlttsplugin.so
%endif

%files devel
%_K5inc/*konq*
%_K5link/lib*.so
%_K5lib/cmake/KF5Konq/
%_K5dbus_iface/*.xml

%files -n %libkf5konq
%_K5lib/libKF5Konq.so.%kf5konq_sover
%_K5lib/libKF5Konq.so.*
%files -n %libkonquerorprivate
%_K5lib/libkonquerorprivate.so.%konquerorprivate_sover
%_K5lib/libkonquerorprivate.so.*
#%files -n %libkonqsidebarplugin
#%_K5lib/libkonqsidebarplugin.so.%konqsidebarplugin_sover
#%_K5lib/libkonqsidebarplugin.so.*

%changelog
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

* Tue Feb 19 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Tue May 22 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Mar 06 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Mon Nov 13 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Mon Oct 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt2%ubt
- conflict with kde5-baseapps-common

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Thu Mar 16 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- initial build
