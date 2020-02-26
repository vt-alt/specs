%define rname kopete

%if_enabled kde_mobile
%def_disable desktop
%else
%def_enable desktop
%endif

%def_disable kopete_irc
%def_disable mediastreamer

%add_findreq_skiplist %_K5bin/kopete_*.sh
%add_findreq_skiplist %_K5bin/winpopup-*.sh
%add_findreq_skiplist %_K5data/kopete_skype/call_*

%define sover 0
%define libkopete_oscar libkopete_oscar%sover
%define libkopete_videodevice libkopete_videodevice%sover
%define libkopetestatusmenu libkopetestatusmenu%sover
%define liboscar liboscar%sover
%define libkopeteaddaccountwizard libkopeteaddaccountwizard%sover
%define libkopeteprivacy libkopeteprivacy%sover
%define libkopete_otr_shared libkopete_otr_shared%sover
%define libqgroupwise libqgroupwise%sover
%define libkopete libkopete%sover
%define libkyahoo libkyahoo%sover
%define libkopetecontactlist libkopetecontactlist%sover
%define libkopeteidentity libkopeteidentity%sover
%define libkopetechatwindow_shared libkopetechatwindow_shared%sover
%define libqgroupwise libqgroupwise%sover

Name: kde5-kopete
Version: 19.12.2
Release: alt1
%K5init

Group: Networking/Instant messaging
Summary: Instant Messaging client
License: GPLv2
Url: http://www.kde.org/applications/internet/kopete/

Requires: qca-qt5-ossl
%if_enabled mediastreamer
Requires: libmediastreamer-ilbc
%endif
Conflicts: kde4-kopete

Source: %rname-%version.tar
# ALT
Patch100: alt-mobile.patch
Patch101: alt-soversion.patch

BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: rpm-macros-browser-plugins
BuildRequires: gcc-c++ cmake extra-cmake-modules
BuildRequires: boost-devel glib2-devel zlib-devel
BuildRequires: libqca-qt5-devel qt5-phonon-devel
BuildRequires: libgpgme-devel
BuildRequires: libexpat-devel libjasper-devel libjpeg-devel
BuildRequires: libidn-devel
BuildRequires: libgadu-devel libgnutls-devel libtasn1-devel jsoncpp-devel
BuildRequires: libmeanwhile-devel libalsa-devel
BuildRequires: libotr-devel
%if_enabled mediastreamer
BuildRequires: libmediastreamer-devel libmediastreamer-ilbc
%endif
BuildRequires: libsqlite3-devel
BuildRequires: libsrtp-devel libortp-devel libv4l-devel libxslt-devel python-devel
BuildRequires: kf5-kdelibs4support-devel kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdoctools-devel kf5-kemoticons-devel kf5-ki18n-devel
BuildRequires: kf5-kcmutils-devel kf5-khtml-devel kf5-knotifyconfig-devel kf5-kparts-devel
BuildRequires: kf5-ktextwidgets-devel kf5-ktexteditor-devel kf5-kwallet-devel kf5-kio-devel
BuildRequires: kf5-kxmlgui-devel kf5-kjs-devel kf5-kcodecs-devel kde5-kcontacts-devel
BuildRequires: kde5-kidentitymanagement-devel kde5-kpimtextedit-devel kde5-libkleo-devel
BuildRequires: kf5-kdnssd-devel

%description
Kopete is an Instant Messaging client
designed to be modular and plugin based.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
%description common
%name common package

%package core
Summary: Core files for %name
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description core
Core files for %name

%package -n %libkopete
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n %libkopete
%name libraries

%package -n %libkopete_videodevice
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n %libkopete_videodevice
%name libraries

%package -n %libkopeteaddaccountwizard
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n %libkopeteaddaccountwizard
%name libraries

%package -n %libkopeteprivacy
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n %libkopeteprivacy
%name libraries

%package -n %libkopetechatwindow_shared
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n %libkopetechatwindow_shared
%name libraries

%package -n %libkopete_oscar
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n %libkopete_oscar
%name libraries

%package -n %liboscar
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n %liboscar
%name libraries

%package -n %libkopete_otr_shared
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n %libkopete_otr_shared
%name libraries

%package -n %libkopeteidentity
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n %libkopeteidentity
%name libraries

%package -n %libkopetestatusmenu
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n %libkopetestatusmenu
%name libraries

%package -n %libkopetecontactlist
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n %libkopetecontactlist
%name libraries

%package -n %libkyahoo
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n %libkyahoo
%name libraries

%package -n %libqgroupwise
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n %libqgroupwise
%name libraries

%if_enabled kopete_irc
%package -n %libkirc_client
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n %libkirc_client
%name libraries

%package -n %libkirc
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n %libkirc
%name libraries
%endif

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Requires: %name-common = %version-%release
%description devel
This package contains header files needed if you wish to build applications
based on %name.

%prep
%setup -q -n %rname-%version
%if_disabled desktop
%patch100 -p1
%endif
%patch101 -p1

# avoid conflicts with KDE4
find -type f -name CMakeLists.txt | \
while read f ; do
    sed -i -e '/set_target_properties/s/[[:space:]]SOVERSION[[:space:]]1[[:space:]]*/ SOVERSION 0 /' $f
    sed -i -e '/set_target_properties/s/[[:space:]]VERSION[[:space:]]1\.0.\0[[:space:]]/ VERSION 0.0.0 /' $f
done

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    -DWITH_irc:BOOL=%{?_enable_kopete_irc:ON}%{!?_enable_kopete_irc:OFF} \
    -DWITH_wlm:BOOL=OFF \
    -DMOZPLUGIN_INSTALL_DIR:PATH=%browser_plugins_path \
    #

%install
%K5install
%K5install_move data kconf_update kopete kopete_history locale sounds
%find_lang --all-name --with-kde %rname

%files common -f %rname.lang
%doc AUTHORS IDENTITY_REFACTORY README TODO
%dir %_K5srv/kconfiguredialog/
%_K5icon/*/*/*/*.*
%config(noreplace) %_K5xdgconf/*rc
%_datadir/qlogging-categories5/*.*categories

%files
%if_enabled mediastreamer
%_K5bin/libjingle-call
%endif
%_K5bin/kopete
#%_K5bin/kopete_latexconvert.sh
%_K5bin/winpopup-install
%_K5bin/winpopup-send
%_K5plug/chattexteditpart.so
%_K5plug/kcm_kopete_*
%_K5plug/kopete_*
%_K5plug/accessible/chatwindowaccessiblewidgetfactory.so
#%browser_plugins_path/skypebuttons.so
%_K5conf_up/kopete-*
%_K5xdgapp/*kopete*.desktop
#%_K5conf/kopeterc
%_K5cfg/*.kcfg
%_K5srv/*.protocol
%_K5srv/*.desktop
%_K5srv/kconfiguredialog/kopete_*
%_K5srvtyp/kopete*
%_K5snd/Kopete_*.ogg
%_K5data/kopete/
%_K5data/kopete_*/
#%_K5data/kopeterichtexteditpart/
%_K5xmlgui/kopete*/
%_K5notif/kopete*

%if_enabled kopete_irc
%files -n %libkirc
%_K5lib/libkirc.so.*
%_K5lib/libkirc.so.%sover
%files -n %libkirc_client
%_K5lib/libkirc_client.so.*
%_K5lib/libkirc_client.so.%sover
%endif
%files -n %libkopete_oscar
%_K5lib/libkopete_oscar.so.*
%_K5lib/libkopete_oscar.so.%sover
%files -n %libkopete_videodevice
%_K5lib/libkopete_videodevice.so.*
%_K5lib/libkopete_videodevice.so.%sover
#%files -n %libkyahoo
#%_K5lib/libkyahoo.so.*
#%_K5lib/libkyahoo.so.%sover
%files -n %libkopeteaddaccountwizard
%_K5lib/libkopeteaddaccountwizard.so.*
%_K5lib/libkopeteaddaccountwizard.so.%sover
%files -n %libkopete
%_K5lib/libkopete.so.*
%_K5lib/libkopete.so.%sover
%files -n %libkopeteprivacy
%_K5lib/libkopeteprivacy.so.*
%_K5lib/libkopeteprivacy.so.%sover
%files -n %libkopetechatwindow_shared
%_K5lib/libkopetechatwindow_shared.so.*
%_K5lib/libkopetechatwindow_shared.so.%sover
%files -n %libkopete_otr_shared
%_K5lib/libkopete_otr_shared.so.*
%_K5lib/libkopete_otr_shared.so.%sover
%files -n %liboscar
%_K5lib/liboscar.so.*
%_K5lib/liboscar.so.%sover
%files -n %libkopeteidentity
%_K5lib/libkopeteidentity.so.*
%_K5lib/libkopeteidentity.so.%sover
%files -n %libkopetestatusmenu
%_K5lib/libkopetestatusmenu.so.*
%_K5lib/libkopetestatusmenu.so.%sover
%files -n %libkopetecontactlist
%_K5lib/libkopetecontactlist.so.*
%_K5lib/libkopetecontactlist.so.%sover
%files -n %libqgroupwise
%_K5lib/libqgroupwise.so.*
%_K5lib/libqgroupwise.so.%sover

%files devel
%_K5link/*.so
%_K5inc/*/
%_K5dbus_iface/*

%changelog
* Fri Feb 14 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt1
- new version

* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Wed Aug 28 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Tue May 07 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Mon Feb 25 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Fri Dec 07 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt4
- return XMPP

* Wed Dec 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt3
- disable XMPP module (https://lists.altlinux.org/pipermail/devel/2018-November/205998.html)

* Fri Aug 31 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt2%ubt
- fix build requires

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Mon Jun 04 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Fri Apr 20 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.0-alt1%ubt
- new version

* Mon Apr 09 2018 Sergey V Turchin <zerg@altlinux.org> 18.03.90-alt1%ubt
- new beta

* Fri Mar 30 2018 Sergey V Turchin <zerg@altlinux.org> 18.03.80-alt3%ubt
- fix build requires

* Fri Mar 30 2018 Igor Vlasenko <viy@altlinux.ru> 18.03.80-alt2%ubt
- NMU: added Url

* Tue Mar 27 2018 Sergey V Turchin <zerg@altlinux.org> 18.03.80-alt1%ubt
- initial build
