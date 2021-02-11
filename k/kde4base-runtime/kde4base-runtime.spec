%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir
%add_findreq_skiplist %_K4exec/khc_*
%add_findreq_skiplist %_K4exec/kdeeject

%def_disable gcc5ready
%def_disable ntrack

%define rname kdebase-runtime
%define major 16
%define minor 04
%define bugfix 1
Name: kde4base-runtime
Version: %major.%minor.%bugfix
Release: alt6
%define libname lib%name

Group: Graphical desktop/KDE
Summary: K Desktop Environment - Runtime
License: GPLv2
Url: http://www.kde.org/

Requires: %name-core = %EVR

Source0: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebase-runtime-%version.tar
Source1: kde4
Source10: search-yandex.desktop
Source11: search-altbugzilla.desktop
# ALT
Patch1001: kdebase-runtime-4.3.2-alt-compiz.patch
Patch1002: kdebase-runtime-4.8.0-alt-def-nepomuk.patch
Patch1003: kdebase-runtime-15.12.1-alt-perl-checks.patch
Patch1004: kdebase-runtime-4.10.0-alt-def-trash.patch
Patch1005: kdebase-runtime-4.8.0-alt-nepomuk-backup-on.patch
Patch1006: kdebase-runtime-4.9.3-alt-multimedia-player-chooser.patch
Patch1007: kdebase-runtime-4.12.3-alt-use-kwallet.patch

BuildRequires(pre): kde4pimlibs-devel attica-devel
BuildRequires: gcc-c++ cmake bzlib-devel liblzma-devel xml-utils
BuildRequires: libalsa-devel libjpeg-devel libpcre-devel libgcrypt-devel
BuildRequires: libstrigi-devel
#BuildRequires: libclucene-core-devel
BuildRequires: libqt4-devel libsmbclient-devel
#NetworkManager-glib-devel
BuildRequires: kde4-kactivities-devel
BuildRequires: libungif-devel libxkbfile-devel openexr-devel libwebp-devel
BuildRequires: libcanberra-devel glib2-devel libpulseaudio-devel
BuildRequires: libopenslp-devel libqca2-devel libgpgme-devel
#BuildRequires: libqzeitgeist-devel
%{?_enable_ntrack:BuildRequires: libntrack-qt4-devel}
%if_enabled gcc5ready
BuildRequires: libexiv2-devel exiv2
%endif
BuildRequires: libssh-devel phonon-devel
BuildRequires: kde4libs-devel kde4pimlibs-devel

%description
Core runtime for the K Desktop Environment 4.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package core
Summary: Core files for %name
Group: Graphical desktop/KDE
Requires: %libname = %EVR
Requires: phonon-backend
Requires: qt4-dbus icon-theme-breeze shared-desktop-ontologies kde4pimlibs
%description core
Core files for  %name

%package -n %libname
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libname
KDE 4 library.

%package devel
Summary: Headers files for %name
Group: Development/KDE and QT
Requires: kde4libs-devel
Requires: %libname = %EVR
%description devel
Headers files needed to build applications based on kdegames applications.

%package -n kde4-menu-resources
Summary: menu resources for the original KDE menu
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: %name-common = %EVR
%description -n kde4-menu-resources
Menu resources for the original KDE menu.

%prep
%setup -q -n %rname-%version
#
#%patch1 -p1
#
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1
%patch1004 -p1
%patch1005 -p1
%patch1006 -p1
%patch1007 -p1

install -m 0644 %SOURCE10 kurifilter-plugins/ikws/searchproviders/yandex.desktop
install -m 0644 %SOURCE11 kurifilter-plugins/ikws/searchproviders/altbugzilla.desktop

cat %SOURCE1 >kde4

%build
%K4build \
    -DKDE4_ENABLE_FPIE:BOOL=ON

%install
%K4install
mkdir -p %buildroot/%_K4doc/en/common

%ifdef _kde_alternate_placement
mkdir -p %buildroot/%_K4bindir/
pushd %buildroot/%_kde4_bindir
for f in *4
do
    ln -sf `relative %buildroot/%_kde4_bindir/$f %buildroot/%_K4bindir/$f` %buildroot/%_K4bindir/$f
done
popd
ln -sf `relative %_kde4_bindir/kde4 %_K4bindir/kde4` %buildroot/%_K4bindir/kde4
%endif


%files
%files common
%files core
%_K4conf_bin/*
%_K4plug/phonon_platform/kde.so
%dir %_K4apps/kcm_phonon/
%_K4apps/kcm_phonon/listview-background.png
%dir %_K4apps/libphonon/
%_K4apps/libphonon/hardwaredatabase
%dir %_K4apps/phonon/
%_K4apps/phonon/phonon.notifyrc
#
%_K4dbus_services/*
#
%exclude %_kde4_xdg_menu/*.menu
%_kde4_bindir/*
%ifdef _kde_alternate_placement
%_K4bindir/*4
%endif
%attr(2711,root,nobody) %_K4exec/kdesud
%_K4exec/drkonqi
%_K4exec/kcmremotewidgetshelper
%_K4exec/kdeeject
%_K4exec/kdesu
%_K4exec/kdontchangethehostname
%_K4exec/khc_*
%_K4exec/kioexec
#%_K4exec/klocaldomainurifilterhelper
%_K4exec/knetattach
%_K4libdir/attica_kde.so
%_K4libdir/libkdeinit4_*.so
%_K4libdir/libknotifyplugin.so
#%_K4libdir/strigi/*.so*
%_K4lib/*.so*
%_K4lib/platformimports/touch/org/kde/*
%_K4lib/imports/org/kde/*
%_K4lib/plugins/imageformats/kimg_*.so
#%_K4start/nepomukcontroller.desktop
%_K4apps/desktoptheme/
%_K4apps/kglobalaccel
%_K4apps/khelpcenter/
%_K4apps/ksmserver/
%_K4apps/konqsidebartng/
%_K4apps/kwalletd/
%_K4apps/hardwarenotifications/
%_K4cfg/*
%_K4conf/*
%_K4emo/kde4/
%ifdef _kde_alternate_placement
%_kde4_iconsdir/hicolor/index.theme
%endif
%_kde4_iconsdir/hicolor/*/*/*
%_kde4_xdg_apps/*
%_K4xdg_mime/network.xml
%_K4xdg_mime/webp.xml
%_K4i18n/*
%_K4snd/*
%_K4srv/*
%_K4srvtyp/*
%_man1dir/*
%_K4doc/en/*
%_K4dbus_system/org.kde.kcontrol.kcmremotewidgets.conf
%_K4dbus_sys_services/org.kde.kcontrol.kcmremotewidgets.service
%_datadir/polkit-1/actions/org.kde.kcontrol.kcmremotewidgets.policy
%exclude %_K4doc/en/common

%_K4apps/drkonqi/
%_K4apps/kcm_componentchooser/
%_K4apps/kcmlocale/
%_K4apps/kconf_update/
%_K4apps/kde/
%_K4apps/kio_*/
%_K4apps/konqueror/
%_K4apps/remoteview/

%files -n kde4-menu-resources
%_kde4_xdg_dirs/*.directory

%files -n %libname
%_K4libdir/lib*.so.*

%files devel
%_K4link/*.so
%_K4includedir/*
%_K4apps/cmake/
%_K4dbus_interfaces/*

%changelog
* Mon Dec 09 2019 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt6
- clean requires

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 16.04.1-alt5
- NMU: remove rpm-build-ubt from BR:

* Thu Jan 10 2019 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt4
- build without clucene and NetworkManager

* Tue Oct 10 2017 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt3
- rebuild with new libwebp

* Fri May 20 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt2
- fix PATH in kde4 wrapper script

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version
- fix requires

* Mon Jan 25 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt2
- fix to build

* Mon Jan 25 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Wed Nov 18 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version
- update kde4 wrapper

* Tue Sep 29 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version
- fix requires to qdbus

* Fri Aug 28 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Wed Jun 24 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.2-alt2
- rebuild with new libgcrypt

* Thu Jun 11 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.2-alt1
- new version
- temporary build without exiv2

* Tue Apr 21 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.0-alt1
- new version

* Wed Mar 11 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.3-alt1
- new version

* Fri Feb 06 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.2-alt1
- new version

* Mon Jan 26 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.1-alt1
- new version

* Thu Nov 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt1
- new version

* Tue Oct 14 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.2-alt1
- new version

* Wed Sep 17 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.1-alt1
- new version

* Tue Aug 12 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Tue Jun 17 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.2-alt1
- new version

* Wed Jun 04 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.1-alt2
- fix build requires

* Tue May 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.1-alt1
- new version

* Thu Apr 17 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Thu Mar 27 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt1.M70P.3
- fix find libssh with old cmake (ALT#29911)

* Thu Mar 27 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt1.M70P.2
- rebuilt with new libssh

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt1.M70P.1
- built for M70P

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt2
- don't offer gpg for kwallet by default

* Thu Mar 06 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt1
- new version

* Thu Jan 30 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt1
- new version

* Sat Jan 11 2014 Sergey V Turchin <zerg@altlinux.org> 4.11.5-alt0.M70P.1
- built for M70P

* Fri Jan 10 2014 Sergey V Turchin <zerg@altlinux.org> 4.11.5-alt1
- new version

* Fri Dec 06 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt1.M70P.1
- built for M70P

* Fri Dec 06 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt2
- add patch from Fedora to fix notifications volume

* Wed Dec 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt0.M70P.1
- built for M70P

* Wed Dec 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt1
- new version

* Thu Nov 07 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt0.M70P.1
- built for M70P

* Wed Nov 06 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt0.M70P.1
- built for M70P

* Wed Oct 02 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt1
- new version

* Thu Sep 12 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt2
- fix taskbar applet needs doubleclicking

* Wed Sep 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Fri Jul 19 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt2
- offer to use kwallet by default

* Mon Jul 01 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt1
- new version

* Mon Jun 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.4-alt1
- new version

* Tue May 07 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.3-alt1
- new version

* Wed Apr 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt1
- new version

* Tue Mar 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt1
- new version

* Fri Mar 01 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt2
- update from 4.10 branch

* Fri Feb 22 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt1
- update from 4.10 branch

* Tue Jan 29 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.6
- update from 4.10 branch

* Fri Jan 25 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.5
- don't split libs

* Thu Jan 24 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.4
- rebuilt whith new exiv2

* Thu Jan 10 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.3
- update from 4.10 branch

* Wed Dec 19 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.2
- update from 4.10 branch

* Mon Dec 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Thu Dec 06 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.4-alt1
- new version

* Tue Dec 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt3
- improve componentchooser multimedia players list

* Tue Nov 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt2
- add multimedia players to componentchooser

* Thu Nov 08 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt1
- new version

* Mon Oct 15 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.2-alt1
- new version

* Wed Sep 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Thu Aug 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt0.M60P.1
- built for M60P

* Wed Aug 01 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt1
- new version
- built without libcanberra

* Fri Jul 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt4
- rebuilt with new attica

* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt2.M60P.1
- built for M60P

* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt3
- turn on nepomuk autobackup by default

* Fri Jun 08 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt2
- rebuilt with new soprano

* Tue Jun 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Wed May 30 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1.M60P.1
- build for M60P

* Thu May 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt2
- update from 4.8 branch

* Thu May 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt0.M60P.1
- build for M60P

* Wed May 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Wed Apr 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1.M60P.1
- build for M60P

* Wed Apr 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt2
- remove plasma-mobile patches

* Wed Apr 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Tue Mar 06 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Thu Mar 01 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt4
- add plasma-active patches

* Mon Feb 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt3
- fix to disable file indexing in UI by default

* Fri Feb 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- add soname for libnepomukdatamanagement

* Wed Jan 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Mon Dec 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1.M60P.1
- built for M60P

* Wed Dec 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt2
- don't build activitymanager (now separate package)

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Fri Dec 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Wed Nov 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt2
- rebuilt with new exiv2

* Sat Oct 29 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt0.M60T.1
- built for M60T

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Thu Sep 29 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt2
- rebuilt with pulse

* Thu Sep 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Wed Jul 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt0.M60P.1
- built for M60P

* Fri Jul 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version

* Tue Jun 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt0.M60P.1
- built for M60P

* Mon Jun 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Fri May 20 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt2
- built without ntrack

* Wed May 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Thu Apr 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt2
- add new system freedesktop menu support; thanks viy@alt

* Tue Apr 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Mon Feb 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version

* Fri Feb 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt2
- decrease default notify volume

* Thu Jan 27 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Mon Nov 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Tue Oct 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Mon Aug 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Tue Aug 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Fri Jul 23 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.92-alt1
- new version

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Mon Jun 07 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt2
- rebuilt with new exiv2

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Mon May 31 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Wed May 26 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt2.M51.2
- built for M51

* Tue May 25 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt3
- fix to build with new attica

* Mon May 24 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1.M51.1
- built for M51

* Mon May 24 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt2
- increase oxygen style submenu pupup delay

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Fri Apr 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Mon Mar 29 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Mon Mar 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Wed Feb 10 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Tue Jan 19 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Mon Nov 30 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Fri Oct 30 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Thu Oct 08 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Thu Sep 24 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt2
- build with LZMA/XZ compression support

* Mon Aug 31 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Thu Aug 20 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt3
- don't start nepomukserver by default

* Tue Aug 18 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt2
- add old kde binaries path to kde4 script

* Tue Aug 04 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Tue Aug 04 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt2
- revert fish:/ to 4.2.4

* Wed Jul 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Wed Jul 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Mon Jul 13 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt2.M50.1
- built for M50

* Fri Jul 10 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt3
- add Yandex and ALT Linux bugzilla search providers

* Wed Jul 08 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt2
- fix to start compiz with kde4-window-decorator

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Fri Jun 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Mon May 04 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Thu Apr 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt2
- add symlink kcmshell4 to /usr/bin

* Thu Apr 02 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Wed Mar 25 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.1-alt2
- add patch to start nepomuk after plasma

* Mon Mar 02 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Thu Feb 26 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt3
- fix build requires
- add script kde4 to allow execute kde4 apps via it

* Thu Feb 19 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt2
- fix to don't require kdebase-libs

* Wed Jan 28 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Wed Jan 14 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version
- remove deprecated macroses from specfile

* Thu Nov 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Thu Oct 09 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- new version

* Mon Sep 01 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt1
- new version

* Wed Jul 30 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt1
- new version

* Wed May 28 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.80-alt1
- 4.1 beta1

* Tue May 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.72-alt1
- new version

* Tue Apr 01 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.3-alt1
- new version

* Tue Mar 11 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt2
- rebuilt with Qt4 buildkey change

* Thu Mar 06 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.2-alt1
- new version

* Wed Feb 27 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt2
- rebuilt with new openexr

* Fri Feb 15 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.1-alt1
- built for ALT

