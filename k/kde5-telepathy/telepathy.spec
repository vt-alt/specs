Name: kde5-telepathy
Version: 19.12.2
Release: alt1

Group: Graphical desktop/KDE
Summary: KDE Telepathy handler
Url: http://projects.kde.org/projects/extragear/network/telepathy/
License: GPLv2+

BuildArch: noarch

#Requires: mjpegtools
#
Requires: telepathy-accounts-signon
Requires: telepathy-mission-control
Requires: telepathy-gabble
#Requires: telepathy-haze
Requires: telepathy-idle
Requires: telepathy-rakia
Requires: telepathy-salut
#
Requires: kde5-ktp-accounts-kcm
Requires: kde5-ktp-approver
Requires: kde5-ktp-auth-handler
Requires: kde5-ktp-desktop-applets
Requires: kde5-ktp-contact-list
Requires: kde5-ktp-contact-runner
Requires: kde5-ktp-filetransfer-handler
Requires: kde5-ktp-kded-module
Requires: kde5-ktp-send-file
Requires: kde5-ktp-text-ui
#Requires: kde5-ktp-call-ui
#
Requires: kde5-signon-kwallet-extension
Requires: kde5-kaccounts-providers

BuildRequires(pre): rpm-build-ubt

%description
%summary

%files

%changelog
* Tue Jan 19 2021 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt1
- clean requires

* Mon Sep 14 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- don't require kde5-ktp-call-ui

* Fri Mar 27 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.0-alt1
- don't require telepathy-haze

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- require kde5-ktp-call-ui

* Thu Mar 21 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.0-alt1
- don't require kde5-ktp-call-ui

* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.0-alt1%ubt
- update requires

* Mon Oct 19 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt3
- update requires

* Tue Aug 04 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.3-alt2
- update requires

* Fri Jul 10 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.3-alt1
- initial build
