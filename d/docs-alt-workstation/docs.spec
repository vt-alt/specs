%define variant alt-workstation
%define Variant ALT Workstation

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite docs-school-teacher docs-alt-education docs-alt-kworkstation docs-alt-server docs-alt-workstation docs-alt-spworkstation docs-alt-server-v

Name: docs-%variant
Version: 9.1
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
* Tue Jul 14 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt1
- update to latest public distr of ALT Workstation 9.1

* Fri Oct 04 2019 Elena Mishina <lepata@altlinux.org> 9.0-alt1
- update to latest public distr of ALT Workstation 9.0

* Mon Jul 29 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt2
- update to beta verson of ALT Workstation 9.0
- fix pam_mount options (ALT #37031)

* Mon Jul 01 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt1
- update to alpha verson of ALT Workstation 9.0

* Wed Oct 17 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt3
- fix typo
- update documentation

* Fri Mar 16 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt2
- update documentation

* Mon Nov 27 2017 Elena Mishina <lepata@altlinux.org> 8.2-alt1
- fix typo
- update doc

* Wed May 24 2017 Elena Mishina <lepata@altlinux.org> 8.1-alt4
- fix typo
- update doc

* Fri Feb 10 2017 Elena Mishina <lepata@altlinux.org> 8.1-alt3
- update Conflicts list

* Thu Jan 19 2017 Artem Zolochevskiy <azol@altlinux.ru> 8.1-alt2
- updated to latest public distr

* Tue Nov 15 2016 Michael Shigorin <mike@altlinux.org> 8.1-alt1
- update for 8.1 release

* Tue Jun 21 2016 Michael Shigorin <mike@altlinux.org> 8.0-alt3
- renamed to docs-alt-workstation

* Tue Apr 19 2016 Artem Zolochevskiy <azol@altlinux.org> 8.0-alt2
- update to alpha verson (18/04/2016)

* Mon Apr 4 2016 Artem Zolochevskiy <azol@altlinux.org> 8.0-alt1
- initial build
