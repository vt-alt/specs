Name: alterator-luks
Version: 0.3.1
Release: alt2

Source:%name-%version.tar

Packager: Timur Aitov <timonbl4@altlinux.org>

Summary: alterator module for change LUKS passphrase
License: GPL
Group: System/Configuration/Other
BuildArch: noarch

BuildRequires: alterator

Requires: alterator
Requires: alterator-l10n
Requires: cryptsetup => 1.6.8-alt1

Conflicts: livecd-install < 0.7.2-alt1

%description
alterator module for for change LUKS passphrase

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_datadir/alterator/steps/*/
%_alterator_backend3dir/*

%changelog
* Thu Jan 16 2020 Oleg Solovyov <mcpain@altlinux.org> 0.3.1-alt2
- Don't change password on containers having passwords (Closes: #37662)

* Tue Dec 24 2019 Oleg Solovyov <mcpain@altlinux.org> 0.3.1-alt1
- Don't change password on inactive containers (Closes: #37662)

* Tue Mar 27 2018 Oleg Solovyov <mcpain@altlinux.org> 0.3.0-alt2
- fix "no key available with this passphrase" (Closes: #31895)

* Wed Apr 27 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- Show error message if cryptsetup failed.
- Use --force-password for cryptsetup.

* Mon Feb 04 2013 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Added 'luks' step for installer.
- code style (by Timur Aitov).

* Wed Dec 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- don't ask for password if no lusk devices found

* Wed Dec 19 2012 Timur Aitov <timonbl4@altlinux.org> 0.1-alt1
- initial build
