Name: installer-feature-kdesktop-services
Version: 0.9.1
Release: alt1

Summary: Setup services for start/not start on boot
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Source: %name-%version.tar

%description
Setup services for start/not start on boot

%prep
%setup

%build

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Thu Jan 16 2020 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt1
- don't disable ahttpd

* Thu Jul 11 2019 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt1
- enable user obex service

* Fri Apr 12 2019 Sergey V Turchin <zerg@altlinux.org> 0.8.3-alt1
- enable rngd service

* Thu Aug 23 2018 Sergey V Turchin <zerg@altlinux.org> 0.8.2-alt1
- update services list

* Thu Nov 03 2016 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt1
- fix to enable services

* Wed Nov 02 2016 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- enable fstrim.timer

* Thu Apr 28 2016 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt1
- enable real display-manager

* Mon Apr 25 2016 Sergey V Turchin <zerg@altlinux.org> 0.6.5-alt1
- disable debug-shell console-getty console-shell getty@tty1

* Wed Apr 20 2016 Sergey V Turchin <zerg@altlinux.org> 0.6.4-alt1
- disable colord and openl2tp

* Tue Jul 16 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.3-alt1
- fix disable services

* Mon Jul 15 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt1
- disable NetworkManager-wait-online

* Tue Apr 23 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.1-alt1
- fix setup services

* Mon Apr 22 2013 Sergey V Turchin <zerg@altlinux.org> 0.6.0-alt1
- update default services list

* Mon Apr 08 2013 Sergey V Turchin <zerg@altlinux.org> 0.5.2-alt1
- enable crond

* Fri Mar 15 2013 Sergey V Turchin <zerg@altlinux.org> 0.5.1-alt1
- force enable postfix

* Mon Feb 04 2013 Sergey V Turchin <zerg@altlinux.org> 0.5.0-alt1
- remove sysvinit support

* Fri Jul 20 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- add systemd support

* Thu May 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.3-alt1
- turn off clamd by default

* Fri Sep 30 2011 Sergey V Turchin <zerg@altlinux.org> 0.3.2-alt1
- turn off lircd by default

* Thu Jun 23 2011 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- turn off nscd by default

* Tue May 17 2011 Sergey V Turchin <zerg@altlinux.org> 0.3-alt1
- turn on samba by default

* Mon Feb 14 2011 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- turn off hal by default

* Tue Oct 12 2010 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build

