Name: nextcloud-client
Version: 2.6.4
Release: alt3

Group: Networking/File transfer
Summary: Nextcloud Desktop Client
License: GPLv2
Url: https://github.com/nextcloud/desktop


Provides: mirall = %version-%release
Obsoletes: mirall <= %version-%release

Provides: nextcloud-desktop = %version-%release

Source0: %name-%version.tar
Source2: nextcloud-client.desktop
Patch1: alt-dont-check-updates.patch
Patch2: alt-confdir.patch
Patch3: alt-static-libs.patch
Patch4: %name-2.3.3-alt-fix-help-url.patch
Patch5: alt-move-deleted-to-trash.patch
Patch6: alt-qt5.15.patch

BuildRequires: kde-common-devel rpm-build-kf5
BuildRequires: doxygen extra-cmake-modules graphviz kf5-kio-devel libqtkeychain-qt5-devel libsqlite3-devel libssl-devel python3-dev qt5-tools-devel zlib-devel
BuildRequires: qt5-webengine-devel libgio-devel glib2-devel qt5-svg-devel
BuildRequires: kf5-kwindowsystem-devel

%description
The Nextcloud Desktop Client is a tool to synchronize files from Nextcloud Server with your computer.

%package kde5
Summary: KDE5 %name integration
Group: Graphical desktop/KDE
Requires: %name
%description kde5
KDE5 %name integration

%prep
%setup
%patch6 -p1

%build
%add_optflags %optflags_shared
%Kbuild \
    -DBUILD_WITH_QT4=OFF \
    -DDATA_INSTALL_DIR=%_datadir \
    -DCMAKE_INSTALL_SYSCONFDIR=/etc/%name \
    -DKDE_INSTALL_PLUGINDIR=%_K5plug \
    -DKDE_INSTALL_KSERVICES5DIR=%_K5srv \
    -DCMAKE_BUILD_TYPE=Release \
    -DNO_SHIBBOLETH=1

%install
%Kinstall
mkdir -p %buildroot/%_desktopdir
desktop-file-install \
    --dir=%buildroot/%_desktopdir %SOURCE2
cd %buildroot/%_libdir
ln -s nextcloud/libocsync.so.%version libocsync.so.0; cd ../..
%find_lang --with-qt --output=%name.lang client

%files -f %buildroot/%name.lang
%doc README.md
%dir %_datadir/nextcloud
%dir %_datadir/nextcloud/i18n
%dir %_sysconfdir/Nextcloud
%dir %_libdir/nextcloud
%config(noreplace) %_sysconfdir/Nextcloud/sync-exclude.lst
%_bindir/nextcloud
%_bindir/nextcloudcmd
%_libdir/lib*sync.*
%_libdir/nextcloud/*
%_desktopdir/%name.desktop
%_datadir/nautilus-python/extensions/
%_datadir/caja-python/extensions/
%_iconsdir/hicolor/*/apps/Nextcloud.*
%_iconsdir/hicolor/*/apps/Nextcloud_*.*

%files kde5
%_K5lib/libnextclouddolphinpluginhelper.so
%_K5plug/kf5/overlayicon/
%_K5plug/*nextcloud*.so
%_K5srv/*nextcloud*.desktop

%changelog
* Tue Oct 06 2020 Sergey V Turchin <zerg@altlinux.org> 2.6.4-alt3
- fix to build with Qt-5.15

* Mon Apr 20 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.6.4-alt2
- fixed kde5 build

* Mon Apr 20 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.6.4-alt1
- new version

* Fri Feb 14 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.6.2-alt1
- new version (ALT#38086)

* Tue Dec 24 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.6.1-alt1
- new version (ALT#37647)

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt2
- NMU: remove rpm-build-ubt from BR:

* Mon Mar 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.5.2-alt1
- new version (ALT#36361)

* Mon Sep 03 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.5.0_beta2-alt1
- new version

* Wed Jan 17 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.3-alt4.M80P.1
- move remote-deleted files to trash (patch from owncloud-client 2.3.4-alt2)

* Wed Nov 22 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.3-alt3.M80P.1
- updated "client_theming" (beta1->release)

* Wed Oct 18 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.3-alt2.M80P.1
- fixed URL of docs

* Wed Oct 18 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.3-alt1.M80P.1
- new version (beta1)

* Fri Sep 22 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.2-alt3.M80P.1
- build for M80P

* Fri Sep 22 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.2-alt4
- fixed unowned files

* Fri Jul 14 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.2-alt2.M80P.1
- build for M80P

* Fri Jul 14 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.2-alt3
- updated "client_theming" (beta1->release)

* Fri Jun 16 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.2-alt1.M80P.1
- build for M80P

* Fri Jun 16 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.2-alt2
- build "nextcloud-client"

* Fri Jun 16 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.2-alt1
- new version

* Thu Nov 03 2016 Sergey V Turchin <zerg@altlinux.org> 2.2.4-alt1.M80P.1
- build for M80P

* Thu Nov 03 2016 Sergey V Turchin <zerg@altlinux.org> 2.2.4-alt2
- rebuild with new libqt5keychain

* Mon Oct 24 2016 Sergey V Turchin <zerg@altlinux.org> 2.2.4-alt0.M80P.1
- build for M80P

* Mon Oct 24 2016 Sergey V Turchin <zerg@altlinux.org> 2.2.4-alt1
- new version (ALT#32649)

* Mon Feb 08 2016 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt1
- new version

* Wed Oct 21 2015 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt1
- new version

* Wed Oct 21 2015 Sergey V Turchin <zerg@altlinux.org> 1.8.4-alt0.M70P.1
- build for M70P

* Mon Jul 13 2015 Sergey V Turchin <zerg@altlinux.org> 1.8.4-alt1
- new version

* Wed Jul 08 2015 Sergey V Turchin <zerg@altlinux.org> 1.8.3-alt1
- new version

* Mon Feb 02 2015 Sergey V Turchin <zerg@altlinux.org> 1.7.1-alt0.M70P.1
- build for M70P

* Mon Feb 02 2015 Sergey V Turchin <zerg@altlinux.org> 1.7.1-alt1
- new version

* Thu Sep 25 2014 Sergey V Turchin <zerg@altlinux.org> 1.6.3-alt1.M70P.1
- built for M70P

* Thu Sep 25 2014 Sergey V Turchin <zerg@altlinux.org> 1.6.3-alt2
- obsolete mirall

* Thu Sep 25 2014 Sergey V Turchin <zerg@altlinux.org> 1.6.3-alt0.M70P.1
- built for M70P

* Fri Sep 19 2014 Sergey V Turchin <zerg@altlinux.org> 1.6.3-alt1
- new version

* Fri Aug 24 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt1
- new version

* Thu Aug 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt3.M60P.2
- built for M60P

* Thu Aug 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt4
- don't conflict with mirall
- bump release

* Thu Aug 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt1.M60P.1
- built for M60P

* Thu Aug 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt2
- fix menu item

* Wed Aug 22 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt0.M60P.1
- built for M60P

* Wed Aug 22 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt1
- initial build
