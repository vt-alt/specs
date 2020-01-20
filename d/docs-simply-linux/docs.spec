%define variant simply-linux
%define Variant Simply Linux

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite docs-school-teacher docs-alt-education docs-alt-kworkstation docs-alt-server docs-alt-workstation docs-alt-spworkstation docs-alt-server-v

Name: docs-%variant
Version: 8.92
Release: alt1

Summary: %Variant documentation
License: %fdl
Group: Documentation

Packager: ALT Docs Team <docs@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version-%release.tar

Conflicts: %(for n in %variants ; do [ "$n" = %name ] || echo -n "$n "; done)

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
* Thu Jan 09 2020 Elena Mishina <lepata@altlinux.org> 8.92-alt1
- updated to latest public distr

* Tue Dec 10 2019 Elena Mishina <lepata@altlinux.org> 8.91-alt1
- update to beta verson of Simply Linux 9.0

* Thu Oct 17 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt1
- update to alpha verson of Simply Linux 9.0

* Wed Oct 17 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt2
- fix typo
- update documentation

* Fri Mar 16 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt1
- initial 8.2 version
- update documentation

* Thu Jun 29 2017 Elena Mishina <lepata@altlinux.org> 8.0-alt1
- initial 8.0 version

* Wed May 24 2017 Elena Mishina <lepata@altlinux.org> 7.0.5-alt4
- closes bug: #29801

* Thu Feb 16 2017 Elena Mishina <lepata@altlinux.org> 7.0.5-alt3
- update Conflicts list

* Sat Jan 23 2016 Artem Zolochevskiy <azol@altlinux.org> 7.0.5-alt2
- rebuild with publclian4

* Sat Jan 23 2016 Artem Zolochevskiy <azol@altlinux.org> 7.0.5-alt1
- update to 7.0.5

* Tue May 13 2014 Artem Zolochevskiy <azol@altlinux.ru> 7.0.1-alt1
- switch to publican
- fix screenshots

* Tue Jun 25 2013 Artem Zolochevskiy <azol@altlinux.ru> 7.0-alt4
- update dvd- usb-burn section

* Thu May 16 2013 Alexandr Boltris <alex@altlinux.org> 7.0-alt3
- update set-up printer (thx Nickolay Rogalskiy)
- added acc method for package install
- added text about platform (p7)

* Mon May 13 2013 Artem Zolochevskiy <azol@altlinux.ru> 7.0-alt2
- update screenshots

* Mon Apr 29 2013 Artem Zolochevskiy <azol@altlinux.ru> 7.0-alt1
- initial 7.0 version

* Fri Mar 09 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0.1-alt3
- fix some typos

* Tue Mar 06 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0.1-alt2
- improve sumode section
- add docs-lxdesktop, docs-lxdesktop-lite to conflicts list

* Tue Feb 21 2012 Artem Zolochevskiy <azol@altlinux.ru> 6.0.1-alt1
- initial 6.0.1 adaptation

* Fri Oct 21 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt9
- update documentation
- closes bug: #26457

* Mon Aug 29 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt8
- fix some typos

* Fri Aug 26 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt7
- update

* Fri Aug 19 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt6
- update

* Thu Aug 18 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt5
- update

* Thu Jun 30 2011 Alexandr Boltris <alex@altlinux.org> 6.0-alt4
- add initial livecd section
- add system-start section
- desktop-software: add initial brasero description
- packages: remove apt-get section
- system-management: remove nm-applet section
- system-start: add initial system-login-gdm
- some rephrasings / typo and formatting fixes

* Fri Jun 10 2011 Alexandr Boltris <alex@altlinux.ru> 6.0-alt3
- system-management: add initial network section
- desktop-software: add initial audacity description
- desktop-software: update thunderbird description
- desktop-xfce: initial xfce-setting-manager description
- install-guide: add missing first step
- some rephrasings / typo fixes
- update screenschots

* Mon Jun 06 2011 Alexandr Boltris <alex@altlinux.ru> 6.0-alt2
- add initial Thunar description

* Mon Jun 06 2011 Artem Zolochevskiy <azol@altlinux.ru> 6.0-alt1
- initial build
