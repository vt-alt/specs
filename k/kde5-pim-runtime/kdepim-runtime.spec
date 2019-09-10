%define rname kdepim-runtime

%define pim_sover 5
%define libmaildir libmaildir%pim_sover
%define libfolderarchivesettings libfolderarchivesettings%pim_sover
%define libakonadi_filestore libakonadi-filestore%pim_sover
%define libkmindexreader libkmindexreader%pim_sover
%define libakonadi_singlefileresource libakonadi-singlefileresource%pim_sover

Name: kde5-pim-runtime
Version: 19.08.1
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Akonadi resources
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

#Requires: kde5-akonadi-contacts kde5-akonadi-notes
Provides: kde5-pimlibs = %EVR
Obsoletes: kde5-pimlibs < %EVR

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Sep 10 2015 (-bi)
# optimized out: boost-devel-headers cmake cmake-modules elfutils kde5-akonadi-devel kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libgst-plugins1.0 libical-devel libjson-c libkolabxml-devel libqt5-core libqt5-dbus libqt5-declarative libqt5-gui libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-sql libqt5-svg libqt5-test libqt5-texttospeech libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libqt5-xmlpatterns libsasl2-3 libstdc++-devel libxcbutil-keysyms pkg-config python-base python3 python3-base qt5-base-devel qt5-script-devel ruby ruby-stdlibs shared-mime-info
#BuildRequires: extra-cmake-modules gcc-c++ kde5-akonadi-calendar-devel kde5-kalarmcal-devel kde5-kcalcore-devel kde5-kcalutils-devel kde5-kcontacts-devel kde5-kholidays-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kmailtransport-devel kde5-kmbox-devel kde5-kmime-devel kde5-kpimtextedit-devel kde5-pimlibs-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kparts-devel kf5-kross-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-libkgapi-devel kf5-solid-devel kf5-sonnet-devel libkolab-devel libsasl2-devel python-module-google qt5-quick1-devel qt5-speech-devel qt5-webkit-devel qt5-xmlpatterns-devel rpm-build-python3 rpm-build-ruby xsltproc
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel qt5-declarative-devel qt5-webengine-devel qt5-xmlpatterns-devel
BuildRequires: qt5-speech-devel qt5-networkauth-devel
BuildRequires: libqca-qt5-devel
BuildRequires: xsltproc libsasl2-devel boost-devel
#BuildRequires: libkolab-devel
BuildRequires: kde5-akonadi-calendar-devel kde5-kalarmcal-devel kde5-kcalcore-devel kde5-kcalutils-devel kde5-kcontacts-devel kf5-kholidays-devel
BuildRequires: kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kmailtransport-devel kde5-kmbox-devel kde5-kmime-devel kde5-kpimtextedit-devel
BuildRequires: kde5-kdav-devel
BuildRequires: kde5-akonadi-devel kde5-akonadi-mime-devel kde5-akonadi-contacts-devel kde5-akonadi-notes-devel kde5-pimcommon-devel
BuildRequires: kde5-libkgapi-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel
BuildRequires: kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel-static kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel
BuildRequires: kf5-knotifyconfig-devel kf5-kparts-devel kf5-kross-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel

%description
This package contains the Akonadi resources which can be used without the applications in kdepim.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Provides: kde5-pimlibs-common = %EVR
Obsoletes: kde5-pimlibs-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libmaildir
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libmaildir
KF5 library

%package -n %libfolderarchivesettings
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libfolderarchivesettings
KF5 library

%package -n %libakonadi_filestore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libakonadi_filestore
KF5 library

%package -n %libkmindexreader
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkmindexreader
KF5 library

%package -n %libakonadi_singlefileresource
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libakonadi_singlefileresource
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
# workaround against sasl plugins dir
#for sffx in 3 4 5 6 ; do
#    mkdir -p  %buildroot/%_libdir/sasl2-$sffx
#    for f in %buildroot/%_libdir/sasl2/*.so* ; do
#	fname=`basename "$f"`
#	ln -s ../sasl2/"$fname" %buildroot/%_libdir/sasl2-$sffx/"$fname"
#    done
#done

%find_lang %name --with-kde --all-name

mv %buildroot/%_K5xdgmime/kdepim{,5}-mime.xml

%files common -f %name.lang
%doc COPYING*
#%config(noreplace) %_K5xdgconf/*.*categories
%_datadir/qlogging-categories5/*.*categories
%_K5xdgmime/kdepim5-mime.xml
%_K5icon/*/*/apps/ox.*
%_K5icon/*/*/apps/akonadi-ews.*

%files
%_K5bin/gidmigrator
%_K5bin/akonadi_*
%_K5plug/akonadi/config/*.so
%_K5plug/kf5/kio/akonadi.so
%_K5plug/kf5/kio/pop3.so
%_datadir/akonadi5/accountwizard/*
%_datadir/akonadi5/agents/*
%_datadir/akonadi5/firstrun/*
%_K5srv/akonadi.protocol
%_K5srv/pop3*.protocol
%_K5srv/akonadi/davgroupware-providers/
%_K5srvtyp/*provider.desktop
%_K5notif/akonadi_*

%files devel
#%_K5link/lib*.so
%_K5dbus_iface/*.xml

%files -n %libmaildir
%_K5lib/libmaildir.so.%pim_sover
%_K5lib/libmaildir.so.*
%files -n %libfolderarchivesettings
%_K5lib/libfolderarchivesettings.so.%pim_sover
%_K5lib/libfolderarchivesettings.so.*
%files -n %libakonadi_filestore
%_K5lib/libakonadi-filestore.so.%pim_sover
%_K5lib/libakonadi-filestore.so.*
%files -n %libkmindexreader
%_K5lib/libkmindexreader.so.%pim_sover
%_K5lib/libkmindexreader.so.*
%files -n %libakonadi_singlefileresource
%_K5lib/libakonadi-singlefileresource.so.%pim_sover
%_K5lib/libakonadi-singlefileresource.so.*

%changelog
* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Fri Aug 16 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Tue Jul 16 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Fri Jun 07 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Tue Apr 30 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Thu Apr 11 2019 Sergey V Turchin <zerg@altlinux.org> 19.03.90-alt1
- new version

* Fri Mar 15 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Fri Feb 08 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Wed Jan 30 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.1-alt1
- new version

* Mon Aug 27 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt2%ubt
- update Russian translation

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Tue Jun 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Tue May 15 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Feb 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.2-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Mon May 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Mon Apr 24 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Wed Mar 15 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.2-alt1%ubt
- new version

* Mon Nov 28 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt0.M80P.1
- build for M80P

* Fri Nov 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Sep 05 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt2
- obsolete kde5-pimlibs

* Fri Aug 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Thu Jun 30 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Mon Apr 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.0-alt1
- new version

* Tue Mar 22 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Thu Feb 25 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Tue Jan 19 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Mon Dec 21 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Mon Oct 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt2
- build without qt5-speech

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- initial build
