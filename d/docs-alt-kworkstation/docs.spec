%define variant alt-kworkstation
%define Variant ALT KWorkstation

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite docs-school-teacher docs-alt-education docs-alt-kworkstation docs-alt-server docs-alt-workstation docs-alt-spworkstation docs-alt-server-v

Name: docs-%variant
Version: 9.0
Release: alt3

Summary: %Variant documentation
License: %fdl
Group: Documentation

Packager: ALT Docs Team <docs@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version-%release.tar

Conflicts: %(for n in %variants ; do [ "$n" = %name ] || echo -n "$n "; done)

Provides: docs-kworkstation = 8.0-alt1
Obsoletes: docs-kworkstation <= 8.0

BuildRequires(pre):rpm-build-licenses
BuildRequires: publican
BuildRequires: perl-podlators

%description
%Variant documentation.

%prep
%setup -n %name-%version-%release

%build
%make_build

%install
%make_install DESTDIR=%buildroot docdir=%_docsinstalldir install
ln -s $(relative %_docsinstalldir %_documentationdir) %buildroot%_documentationdir

%files
%_docsinstalldir
%_documentationdir

%changelog
* Tue Jul 21 2020 Elena Mishina <lepata@altlinux.org> 9.0-alt3
- update restrictions section
- update screenshots
- fix some typos

* Mon Jun 29 2020 Elena Mishina <lepata@altlinux.org> 9.0-alt2
- system-management add FreeIPA, sambadc server, autostart/save sessions
- starting-os add qtvirtualkeyboard
- server-network add alterator
- restrictions add altha, kiosk
- functionl add openvpn-gost, openssh-gost

* Thu Apr 09 2020 Elena Mishina <lepata@altlinux.org> 9.0-alt1
- update to ALT Kworkstation 9.0

* Mon Mar 02 2020 Elena Mishina <lepata@altlinux.org> 8.90-alt6
- desktop-software add ark
- desktop-software add dolhin hash, encrypt GOST
- system-management add kde5-kcm-grub2
- system-management add sessions (sddm, krdc, alt-app-starter)

* Wed Feb 05 2020 Elena Mishina <lepata@altlinux.org> 8.90-alt5
- update to 8.95
- update desktop-software section

* Thu Jan 16 2020 Elena Mishina <lepata@altlinux.org> 8.90-alt4
- desktop-software add discover
- desktop-software add ksysguard
- update screenshots

* Mon Dec 23 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt3
- updated to latest public distr

* Tue Aug 13 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt2
Beta version of ALT Kworkstation 9.0

* Mon Aug 05 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt1
Alpha version of ALT Kworkstation 9.0

* Mon Nov 19 2018 Elena Mishina <lepata@altlinux.org> 8.3-alt1
- Version fix

* Wed Oct 17 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt3
- fix typo
- update documentation

* Fri Mar 16 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt2
- update documentation

* Tue Aug 29 2017 Elena Mishina <lepata@altlinux.org> 8.2-alt1
- Version fix

* Wed May 31 2017 Elena Mishina <lepata@altlinux.org> 8.1-alt5
- renamed docs-kworkstation->docs-alt-kworkstation

* Wed May 24 2017 Elena Mishina <lepata@altlinux.org> 8.1-alt4
- fix typo
- update doc

* Fri Feb 10 2017 Elena Mishina <lepata@altlinux.org> 8.1-alt3
- update Conflicts list

* Thu Jan 19 2017 Artem Zolochevskiy <azol@altlinux.ru> 8.1-alt2
- updated to latest public distr

* Fri Jan 13 2017 Artem Zolochevskiy <azol@altlinux.ru> 8.1-alt1
- renamed to alt-kworkstation

* Sat Sep 24 2016 Artem Zolochevskiy <azol@altlinux.org> 8.0-alt1
- initial kworkstation doc

* Sat Mar 5 2016 Artem Zolochevskiy <azol@altlinux.org> 7.0.5-alt3
- fix changelog

* Sat Mar 5 2016 Artem Zolochevskiy <azol@altlinux.org> 7.0.5-alt2
- rebuild with publclian4

* Sat Jan 23 2016 Artem Zolochevskiy <azol@altlinux.org> 7.0.5-alt1
- update to 7.0.5

* Tue Aug 19 2014 Artem Zolochevskiy <azol@altlinux.ru> 7.0.3-alt1
- update doc
- switch to publican

* Sat Jul 13 2013 Alexandr Boltris <alex@altlinux.org> 7.0.0-alt2
- Version fix

* Wed Jul 10 2013 Alexandr Boltris <alex@altlinux.org> 7.0.0-alt1
- Add info about support *.docx in app libreOffice
  (thx Nickolay Rogalskiy)
- add 11 step to "install-guide" This step is about setting up
  password for LUKS partition(s) (thx Nickolay Rogalskiy)
- desktop-software/internet/im: telepathy replaces kopete
- desktop-software/multimedia/kde: remove Dragonplayer
- install-guide: added section for RAID, LVM and LUSK setup
- install-guide: update installation from USB flash
- support/index.txt: add more Community/Company links
  (thx Artem Zolochevskiy)
- whatis-alt: added text about platform (p7)
- update screenshots
- spellcheck

* Tue Jun 25 2013 Artem Zolochevskiy <azol@altlinux.ru> 6.0.2-alt1
- update dvd- usb-burn section

* Mon Mar 19 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0.1-alt1
- update for 6.0.1

* Fri Mar 09 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt14
- fix some typos

* Tue Mar 08 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt13
- improve sumode section
- add docs-lxdesktop, docs-lxdesktop-lite to conflicts list

* Fri Oct 21 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt9
- update documentation
- closes bug: #26457

* Mon Aug 29 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt8
- fix some typos

* Fri Aug 26 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt7
- update

* Fri Aug 19 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt6
- fix previous changelog entry

* Fri Aug 18 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt5
- update

* Thu Aug 18 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt4
- update

* Fri Jul 01 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt3
- some rephrasings / typo fixes

* Fri Jun 09 2011 Alexandr Boltris <alex@altlinux.ru> 6.0-alt2
- system-management: add initial network section
- kde-quickstart: update system-tray description
- add packages section
- desktop-software: update software descriptions
- some rephrasings / typo fixes
- update screenshots

* Mon Jun 06 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt1
- update for ALT Linux 6.0 KDesktop

* Mon Mar 07 2011 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt8
- update Conflicts list

* Fri Feb 26 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt7
- install-guide: fix info on RAID creation during install
- whatis-alt: fix 'Le Mythe de Sisyphe' link
- add docs-school-terminal to Conflicts list

* Mon Feb 22 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt6
- simplify datetime section (#19084)
- typo and punctuation fixes
- small rephrasings

* Fri Jan 29 2010 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt5
- typo fixes, small improvements

* Wed Dec 23 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt4
- update screenshots (thx Sergey V Turchin)

* Fri Dec 18 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt3
- add initial 'applications' section

* Fri Nov 27 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt2
- add dolphin section

* Thu Nov 26 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt1
- initial build for Sisyphus
  + based on docs-desktop-5.0-alt8 package
