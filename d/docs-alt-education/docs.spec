%define variant alt-education
%define Variant ALT Education

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite docs-school-teacher docs-alt-education docs-alt-kworkstation docs-alt-server docs-alt-workstation docs-alt-spworkstation docs-alt-server-v

Name: docs-%variant
Version: 9.0
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
* Tue Oct 15 2019 Elena Mishina <lepata@altlinux.org> 9.0-alt1
- update to latest public distr of ALT Education 9.0

* Wed Jul 31 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt2
Beta version of ALT Education 9.0

* Tue Jun 25 2019 Elena Mishina <lepata@altlinux.org> 8.90-alt1
Alpha version of ALT Education 9.0

* Wed Feb 13 2019 Elena Mishina <lepata@altlinux.org> 8.2-alt5
- added moodle, mediawiki, owncloud, rujel
- added install fonts (closes: 35820)

* Tue Jan 15 2019 Elena Mishina <lepata@altlinux.org> 8.2-alt4
- added kde
- added boot option

* Wed Oct 17 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt3
- fix typo
- update documentation

* Fri Mar 16 2018 Elena Mishina <lepata@altlinux.org> 8.2-alt2
- update documentation

* Mon Dec 4 2017 Elena Mishina <lepata@altlinux.org> 8.2-alt1
- updated to 8.2

* Wed May 24 2017 Elena Mishina <lepata@altlinux.org> 8.1-alt4
- fix typo
- update documentation

* Fri Feb 10 2017 Elena Mishina <lepata@altlinux.org> 8.1-alt3
- update Conflicts list
- update documentation

* Thu Jan 19 2017 Artem Zolochevskiy <azol@altlinux.ru> 8.1-alt2
- updated to latest public distr

* Fri Oct 28 2016 Artem Zolochevskiy <azol@altlinux.ru> 8.1-alt1
- updated to 8.1
- added 'guest session' description

* Sun Aug 07 2016 Artem Zolochevskiy <azol@altlinux.ru> 8.0-alt2
- removed obsolete stuff

* Thu Aug 04 2016 Artem Zolochevskiy <azol@altlinux.ru> 8.0-alt1
- initial build for Sisyphus
