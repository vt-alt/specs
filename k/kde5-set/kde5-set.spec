
Name: kde5-set
Version: 19.12.4
Release: alt1

Group: Graphical desktop/KDE
Summary: Set of KDE 5 applications
License: Public Domain

BuildArch: noarch

%description
%summary

%package -n kde5-runtime
Summary: %summary
Group: Graphical desktop/KDE
Requires: qt5-phonon-backend qt5-quickcontrols qt5-quickcontrols2 qt5-graphicaleffects qt5-imageformats qt5-translations
Requires: kf5-kio kf5-kded kf5-kinit plasma5-kwayland-integration
%description -n kde5-runtime
%summary

%package -n kde5-mini
Summary: %summary
Group: Graphical desktop/KDE
Requires: kde5-runtime
Requires: qt5-dbus plasma5-kde-cli-tools plasma5-kwin plasma5-desktop kf5-kinit kf5-kdeclarative
Requires: kde5-dolphin kde5-kdialog
%description -n kde5-mini
%summary

%package -n kde5-small
Summary: %summary
Group: Graphical desktop/KDE
Requires: kde5-mini
Requires: kde5-volume-control
Requires: webclient
#
Requires: icon-theme-breeze
Requires: kf5-kwallet kf5-kconfig kf5-kglobalaccel kf5-kimageformats kde5-svgpart
Requires: plasma5-sddm-kcm plasma5-polkit-kde-agent kf5-kio-extras plasma5-breeze plasma5-oxygen plasma5-powerdevil plasma5-ksysguard
Requires: plasma5-drkonqi plasma5-milou plasma5-systemsettings plasma5-integration
Requires: kde5-ark kde5-konsole kde5-gwenview kde5-okular kde5-kwrite kde5-kwalletmanager
Requires: kde5-kcalc kde5-kdebugsettings kde5-kross-python
%description -n kde5-small
%summary

%package -n kde5
Summary: %summary
Group: Graphical desktop/KDE
Provides: kde5-normal = %EVR kde5-default = %EVR
Obsoletes: kde5-normal < %EVR kde5-default < %EVR
Requires: kde5-small
Requires: kde5-video-player
Requires: kde5-audio-player
Requires: kde5-network-manager
#
##Requires: pam0_kwallet5
Requires: gtk3-theme-breeze
Requires: gtk2-theme-breeze
Requires: kf5-qqc2-desktop-style
Requires: kde5-plasma-applet-places-widget
Requires: plasma5-kde-gtk-config kf5-baloo plasma5-bluedevil plasma5-kscreen plasma5-ksshaskpass kde5-krdc kde5-kgpg
Requires: plasma5-khotkeys plasma5-kinfocenter plasma5-addons plasma5-browser-integration
Requires: kde5-khelpcenter kde5-kolourpaint kde5-kio-audiocd
Requires: plasma5-kmenuedit plasma5-kgamma plasma5-thunderbolt
Requires: kde5-kfind kde5-filelight kde5-kcharselect kde5-kteatime kde5-ktimer kde5-spectacle
Requires: kde5-kamera kde5-network-filesharing kde5-ktorrent
##Requires: kde5-kget
Requires: kde5-kio-zeroconf kde5-sweeper
%description -n kde5
%summary

%package -n kde5-big
Summary: %summary
Group: Graphical desktop/KDE
Requires: kde5
Requires: kde5-email-client
Requires: kde5-messenger-client
#
Requires: plasma5-xdg-desktop-portal-kde
Requires: plasma5-workspace-wallpapers
Requires: plasma5-kwrited
Requires: plasma5-user-manager kde5-ksystemlog
Requires: kde5-konversation kde5-kate
Requires: kde5-pim kde5-pim-addons kde5-kcron kde5-kruler kde5-ffmpegthumbs
Requires: kde5-krfb
Requires: kde5-kdf
Requires: kid3-ui-kde5
Requires: kde5-kipi-plugins-core
%description -n kde5-big
%summary

%package -n kde5-maxi
Summary: %summary
Group: Graphical desktop/KDE
# webclient
Requires: kde5-big
Requires: kde5-edu
Requires: kde5-games
Requires: kde5-printing
Requires: kde5-scanning
#
Requires: plasma5-discover-maxi
Requires: kde5-konqueror kde5-keditbookmarks
Requires: kde5-kfloppy
Requires: kde5-dragon
Requires: kde5-kmousetool kde5-kmag
Requires: kde5-juk kde5-kmouth
Requires: kdenlive kde5-connect
Requires: kde5-k3b kde5-kwave
Requires: kde5-digikam kde5-kipi-plugins
%description -n kde5-maxi
%summary

%package -n kde5-somedevel
Summary: %summary
Group: Graphical desktop/KDE
Requires: kde5-runtime
Requires: kde5-dolphin-plugins
Requires: kde5-lokalize kde5-okteta kde5-kapptemplate kde5-dev-scripts kde5-kompare
Requires: kde5-sdk-thumbnailers kde5-poxml kde5-umbrello
Requires: kde5-kcachegrind
Requires: kde5-kimagemapeditor
%description -n kde5-somedevel
%summary

%package -n kde5-edu
Summary: Educational software based on the KDE technologies
Group: Graphical desktop/KDE
Requires: kde5-runtime
Requires: kde5-kanagram kde5-khangman kde5-parley kde5-kwordquiz kde5-kturtle kde5-marble
Requires: kde5-step kde5-kstars kde5-kig kde5-kmplot kde5-kalgebra kde5-cantor kde5-rocs
Requires: kde5-kbruch kde5-kgeography kde5-ktouch kde5-kalzium
Requires: kde5-minuet
%description -n kde5-edu
Educational software based on the KDE technologies

%package -n kde5-games
Summary: Set of KDE-based games
Group: Graphical desktop/KDE
Requires: kde5-runtime
Requires: kde5-lskat kde5-kmines kde5-kshisen kde5-ktuberling kde5-bovo kde5-knetwalk
Requires: kde5-katomic kde5-knavalbattle kde5-kpat kde5-kmahjongg
Requires: kde5-ksudoku kde5-kigo kde5-knights kde5-kreversi kde5-granatier
Requires: kde5-kolf kde5-ksirk kde5-palapeli
%description -n kde5-games
High quality gaming and entertainment software.

%package -n kde5-printing
Summary: Set of printing support applications
Group: Graphics
Requires: kde5-runtime
Requires: kde5-print-manager cups printer-drivers-X11
#system-config-printer-udev
%description -n kde5-printing
KDE printing support applications.

%package -n kde5-scanning
Summary: Set of image scanning support applications
Group: Graphics
Requires: kde5-runtime
#Requires: kde5-skanlite
Requires: xsane
Requires: hplip-sane libsane-gphoto2 sane
%description -n kde5-scanning
KDE image scanning support applications.

%package -n kde5-pim
Summary: %summary
Group: Graphical desktop/KDE
Requires: kde5-kontact kde5-pim-data-exporter
##Requires: kde5-akonadiconsole
Requires: kde5-email-client
Requires: kde5-akregator kde5-kalarm kde5-knotes
Requires: kde5-korganizer kde5-akonadi-calendar-tools
Requires: kde5-kaddressbook
##Requires:  kde5-blogilo
# akonadi based email client
#Requires: kde5-akonadi-import-wizard kde5-mbox-importer kde5-pim-sieve-editor kde5-mbox-importer kde5-pim-sieve-editor kde5-grantlee-editor
%description -n kde5-pim
%summary


%files -n kde5-runtime
%files -n kde5-mini
%files -n kde5-small
%files -n kde5
%files -n kde5-big
%files -n kde5-maxi
%files -n kde5-somedevel
#
%files -n kde5-edu
%files -n kde5-games
%files -n kde5-printing
%files -n kde5-scanning
%files -n kde5-pim

%changelog
* Mon Jul 06 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.4-alt1
- use xsane for scanning

* Mon Apr 20 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt1
- clear pim requires

* Thu Mar 12 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt1
- add plasma5-browser-integration

* Wed Feb 26 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- add plasma5-discover-maxi

* Tue Feb 18 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.0-alt1
- add thunderbolt

* Mon Jan 13 2020 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- move kfloppy from -big to -maxi

* Fri Jun 28 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- add more games

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- update requires

* Wed Nov 14 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt2
- clean requires

* Tue Sep 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1
- clean pim requires

* Tue Sep 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1
- clean kmail requires

* Fri Sep 21 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1
- clean requires

* Wed Jul 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.0-alt1
- update requires

* Fri Mar 16 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1
- update requires

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.1-alt1
- update requires

* Mon Mar 12 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.0-alt1
- update Plasma requires

* Tue Dec 26 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.1-alt1
- update PIM requires

* Fri Dec 22 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.0-alt1
- update requires

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1
- update PIM requires

* Thu Apr 13 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.2-alt1
- update requires

* Tue Apr 04 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.1-alt1
- update requires

* Thu Mar 23 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.0-alt1
- update PIM requires

* Tue Nov 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- update requires

* Fri Oct 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt2
- clean requires

* Mon Oct 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- update requires

* Thu Oct 06 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt1
- update requires

* Wed Oct 05 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt1
- update requires

* Tue Sep 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- update requires

* Thu Sep 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- require kde5-email-client for kde5-big

* Tue Aug 02 2016 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- use digikam, kipi-plugins

* Mon Aug 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- temporary exclude digikam, kipi-plugins

* Fri Jul 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- add k3b, digikam, kipi-plugins

* Mon Jul 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- fix package deskription

* Thu May 19 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- update requires

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- update requires

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.2.0-alt3
- fix requires

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.2.0-alt2
- fix requires

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.2.0-alt1
- require kde5-audio-player
- update requires

* Tue Apr 19 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.2-alt1
- update requires

* Fri Apr 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt4
- fix requires

* Wed Apr 13 2016 Sergey V Turchin <zerg at altlinux dot org> 5.1.1-alt3
- fix requires

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt2
- fix requires

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- update requires

* Thu Mar 31 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt2
- update requires

* Thu Mar 24 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt1
- add kde5-edu kde5-games kde5-printing kde5-scanning packages

* Thu Mar 24 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt29
- update requires

* Wed Mar 23 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt28
- update requires

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt27
- update requires

* Wed Mar 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt26
- update requires

* Mon Mar 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt25
- update requires

* Thu Feb 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt24
- update requires

* Mon Feb 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt23
- update requires

* Fri Jan 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt22
- update requires

* Tue Jan 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt21
- update requires

* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt20
- update requires

* Tue Dec 08 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt19
- fix requires

* Tue Nov 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt18
- update requires

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt17
- update requires

* Tue Oct 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt16
- update requires

* Fri Oct 02 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt15
- move development tools to separate package

* Thu Oct 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt14
- update requires

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt13
- update requires

* Fri Sep 04 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt12
- update requires

* Fri Aug 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt11
- clean requires

* Thu Aug 27 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt10
- update requires

* Thu Aug 27 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt9
- update requires

* Thu Aug 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt8
- update requires

* Wed Aug 05 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt7
- update requires

* Wed Jul 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt6
- update requires

* Wed Apr 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt5
- update requires

* Mon Apr 27 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt4
- update requires

* Wed Apr 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt3
- update requires

* Tue Apr 21 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt2
- update requires

* Mon Apr 20 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt1
- initial build
