%define variant alt-server
%define Variant ALT Server

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite docs-school-teacher docs-alt-education docs-alt-kworkstation docs-alt-server docs-alt-workstation docs-alt-kworkstation docs-alt-spworkstation docs-alt-server-v

Name: docs-%variant
Version: 9.1
Release: alt1

Summary: %Variant documentation
License: %fdl
Group: Documentation

Packager: ALT Docs Team <docs@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version-%release.tar

Obsoletes: docs-basealt-desktop <= 8.0-alt2
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
- update to latest public distr of ALT Server 9.1

* Fri Oct 04 2019 Elena Mishina <lepata@altlinux.org> 9.0-alt1
- update to latest public distr

* Mon Jul 29 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt1
- update to beta verson of ALT Server 9.0

* Wed Oct 17 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt4
- fix typo
- update documentation

* Fri Mar 16 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt3
- update documentation

* Thu Dec 11 2017 Elena Mishina <lepata@altlinux.org> 8.2-alt2
- fix conflict package

* Thu Nov 30 2017 Elena Mishina <lepata@altlinux.org> 8.2-alt1
- updated to latest public distr
- fix typo

* Wed May 24 2017 Elena Mishina <lepata@altlinux.org> 8.0-alt6
- update documentation
- fix typo

* Thu Mar 20 2017 Elena Mishina <lepata@altlinux.org> 8.0-alt5
- update documentation
- fix typo

* Thu Feb 09 2017 Elena Mishina <lepata@altlinux.org> 8.0-alt4
- update Conflicts list
- update documentation

* Thu Jan 19 2017 Artem Zolochevskiy <azol@altlinux.ru> 8.0-alt3
- updated to latest public distr

* Fri Jan 13 2017 Artem Zolochevskiy <azol@altlinux.org> 8.0-alt2
- update doc

* Fri Jan 13 2017 Artem Zolochevskiy <azol@altlinux.org> 8.0-alt1
- initial build
