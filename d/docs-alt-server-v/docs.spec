%define variant alt-server-v
%define Variant ALT Server V

%define _documentationdir %_defaultdocdir/documentation
%define _docsinstalldir %_defaultdocdir/%variant

%define variants docs-office-server docs-backup-server docs-desktop docs-school-master docs-school-junior docs-school-lite docs-school-server docs-kdesktop docs-school-terminal docs-school-newlite docs-centaurus docs-simply-linux docs-lxdesktop docs-lxdesktop-lite docs-school-teacher docs-alt-education docs-alt-kworkstation docs-alt-server docs-alt-workstation docs-alt-spworkstation docs-alt-server-v

Name: docs-%variant
Version: 9.1
Release: alt2

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
* Wed Sep 16 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt2
- update to latest public distr
- fix some typos

* Mon Sep 14 2020 Elena Mishina <lepata@altlinux.org> 9.1-alt1
- update to latest public distr

* Mon Dec 16 2019 Elena Mishina <lepata@altlinux.org> 9.0-alt2
- fix screen

* Thu Dec 05 2019 Elena Mishina <lepata@altlinux.org> 9.0-alt1
- initial build
