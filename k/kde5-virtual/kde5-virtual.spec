
Name: kde5-virtual
Version: 5.15.0
Release: alt1

Group: Graphical desktop/KDE
Summary: Virtual packages for KDE 5
License: Public Domain

BuildArch: noarch
BuildRequires(pre): rpm-build-ubt

%description
%summary

%package -n kde5-network-manager-0-dummy
Group: Graphical desktop/KDE
Summary: Dummy network manager
Provides: kde5-network-manager = %EVR
Provides: kde5-network-manager-dummy = %EVR
Requires: kf5-filesystem
%description -n kde5-network-manager-0-dummy
%summary

%package -n kde5-network-manager-2-etcnet
Group: Graphical desktop/KDE
Summary: /etc/net network manager
Provides: kde5-network-manager = %EVR
Provides: kde5-network-manager-etcnet = %EVR
Requires: kf5-filesystem
Requires: etcnet alterator-net-wifi alterator-net-openvpn alterator-net-pppoe alterator-net-pptp alterator-net-l2tp
%description -n kde5-network-manager-2-etcnet
%summary

%package -n kde5-network-manager-4-nm
Group: Graphical desktop/KDE
Summary: NetworkManager network manager
Provides: kde5-network-manager = %EVR
Provides: kde5-network-manager-nm = %EVR
Requires: kf5-filesystem
Requires: plasma5-nm-maxi
%description -n kde5-network-manager-4-nm
%summary

%package -n kde5-video-player-0-dummy
Group: Graphical desktop/KDE
Summary: Dummy video player
Provides: kde5-video-player = %EVR
Provides: kde5-video-player-dummy = %EVR
Requires: kf5-filesystem
%description -n kde5-video-player-0-dummy
%summary

%package -n kde5-video-player-2-dragon
Group: Graphical desktop/KDE
Summary: Dragon video player
Provides: kde5-video-player = %EVR
Provides: kde5-video-player-dragon = %EVR
Requires: kf5-filesystem
Requires: kde5-dragon
%description -n kde5-video-player-2-dragon
%summary

%package -n kde5-video-player-3-kaffeine
Group: Graphical desktop/KDE
Summary: Kaffeine video player
Provides: kde5-video-player = %EVR
Provides: kde5-video-player-kaffeine = %EVR
Requires: kf5-filesystem
Requires: kde5-kaffeine
%description -n kde5-video-player-3-kaffeine
%summary

%package -n kde5-video-player-4-smplayer
Group: Graphical desktop/KDE
Summary: SMplayer video player
Provides: kde5-video-player = %EVR
Provides: kde5-video-player-smplayer = %EVR
Requires: kf5-filesystem
Requires: kde5-smplayer
%description -n kde5-video-player-4-smplayer
%summary

%package -n kde5-volume-control-0-dummy
Group: Graphical desktop/KDE
Summary: Dummy volume control
Provides: kde5-volume-control = %EVR
Provides: kde5-volume-control-dummy = %EVR
Requires: kf5-filesystem
%description -n kde5-volume-control-0-dummy
%summary

%package -n kde5-volume-control-2-kmix
Group: Graphical desktop/KDE
Summary: KMix volume control
Provides: kde5-volume-control = %EVR
Provides: kde5-volume-control-kmix = %EVR
Requires: kf5-filesystem
Requires: kde5-kmix
%description -n kde5-volume-control-2-kmix
%summary

%package -n kde5-volume-control-4-plasmapulse
Group: Graphical desktop/KDE
Summary: Plasma PulseAudio volume control
Provides: kde5-volume-control = %EVR
Provides: kde5-volume-control-plasmapulse = %EVR
Requires: kf5-filesystem
Requires: plasma5-pa
%description -n kde5-volume-control-4-plasmapulse
%summary

%package -n kde5-email-client-0-dummy
Group: Graphical desktop/KDE
Summary: Dummy email client
Provides: kde5-email-client = %EVR
Provides: kde5-email-client-dummy = %EVR
Requires: kf5-filesystem
%description -n kde5-email-client-0-dummy
%summary

%package -n kde5-email-client-2-kmail
Group: Graphical desktop/KDE
Summary: KMail email client
Provides: kde5-email-client = %EVR
Provides: kde5-email-client-kmail = %EVR
Requires: kf5-filesystem
Requires: kde5-kmail kde5-pim-addons-kmail kde5-pim-addons-plugins bogofilter bogofilter-utils
Requires: kde5-akonadi-import-wizard kde5-kmail-account-wizard kde5-mbox-importer kde5-pim-sieve-editor
%description -n kde5-email-client-2-kmail
%summary

%package -n kde5-email-client-4-thunderbird
Group: Graphical desktop/KDE
Summary: Thunderbird email client
Provides: kde5-email-client = %EVR
Provides: kde5-email-client-thunderbird = %EVR
Requires: kf5-filesystem
Requires: thunderbird thunderbird-ru thunderbird-lightning-ru
#Requires: thunderbird-enigmail http://bugs.altlinux.org/36447
%description -n kde5-email-client-4-thunderbird
%summary

%package -n kde5-audio-player-0-dummy
Group: Graphical desktop/KDE
Summary: Dummy audio player
Provides: kde5-audio-player = %EVR
Provides: kde5-audio-player-dummy = %EVR
Requires: kf5-filesystem
%description -n kde5-audio-player-0-dummy
%summary

%package -n kde5-audio-player-4-qmmp
Group: Graphical desktop/KDE
Summary: QMMP audio player
Provides: kde5-audio-player = %EVR
Provides: kde5-audio-player-qmmp = %EVR
Requires: kf5-filesystem
Requires: qmmp1
%description -n kde5-audio-player-4-qmmp
%summary

%package -n kde5-messenger-client-0-dummy
Group: Graphical desktop/KDE
Summary: QMMP audio player
Provides: kde5-messenger-client = %EVR
Provides: kde5-messenger-client-dummy = %EVR
Requires: kf5-filesystem
%description -n kde5-messenger-client-0-dummy
%summary

%package -n kde5-messenger-client-2-kopete
Group: Graphical desktop/KDE
Summary: QMMP audio player
Provides: kde5-messenger-client = %EVR
Provides: kde5-messenger-client-kopete = %EVR
Requires: kf5-filesystem
Requires: kde5-kopete
%description -n kde5-messenger-client-2-kopete
%summary

%package -n kde5-messenger-client-4-telepathy
Group: Graphical desktop/KDE
Summary: QMMP audio player
Provides: kde5-messenger-client = %EVR
Provides: kde5-messenger-client-telepathy = %EVR
Requires: kf5-filesystem
Requires: kde5-telepathy
%description -n kde5-messenger-client-4-telepathy
%summary

%files -n kde5-network-manager-0-dummy
%files -n kde5-network-manager-2-etcnet
%files -n kde5-network-manager-4-nm

%files -n kde5-video-player-0-dummy
%files -n kde5-video-player-2-dragon
%files -n kde5-video-player-3-kaffeine
%files -n kde5-video-player-4-smplayer

%files -n kde5-volume-control-0-dummy
%files -n kde5-volume-control-2-kmix
%files -n kde5-volume-control-4-plasmapulse

%files -n kde5-email-client-0-dummy
%files -n kde5-email-client-2-kmail
%files -n kde5-email-client-4-thunderbird

%files -n kde5-audio-player-0-dummy
%files -n kde5-audio-player-4-qmmp

%files -n kde5-messenger-client-0-dummy
%files -n kde5-messenger-client-2-kopete
%files -n kde5-messenger-client-4-telepathy

%changelog
* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- add kde5-messenger-client

* Thu Apr 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1
- remove thunderbird-enigmail requires (http://bugs.altlinux.org/36447)

* Tue Mar 26 2019 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- add enigmail to thunderbird

* Mon Mar 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1%ubt
- update Plasma requires

* Thu Mar 23 2017 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1%ubt
- update kmail requires

* Tue Jul 05 2016 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt2
- fix requires

* Tue Jul 05 2016 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- add dummies for all alternatives
- add kaffeine video player

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- update requires

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- add kde5-audio-player

* Fri Apr 22 2016 Sergey V Turchin <zerg@altlinux.org> 5.2.0-alt1
- add kde5-volume-control and kde5-email-client

* Fri Apr 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt1
- add kde5-video-player

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.1-alt1
- fix requires

* Mon Mar 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt1
- initial build
