# vim: set ft=spec: -*- rpm-spec -*-

Name: alterator-ca
Version: 0.5.8
Release: alt1

Summary: Office Server CA Manager
Group: System/Base
License: GPL

Packager: Alexey I. Froloff <raorn@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

Requires: alterator >= 4.6-alt3
Requires: alterator-l10n >= 2.4-alt4
Conflicts: alterator-fbi < 5.7-alt4

BuildPreReq: alterator >= 4.6-alt3

%description
Certification Authority Manager for Office Server.

%prep
%setup

%build
%make_build

%install
%makeinstall

mkdir -p %buildroot{%_sysconfdir/alterator-ca,%_localstatedir/alterator-ca/{CA,in,out},%_libexecdir/alterator/hooks/trust.d}
install -p -m644 etc/dnparam.txt %buildroot%_sysconfdir/alterator-ca/
install -p -m755 hook/ca %buildroot%_libexecdir/alterator/hooks/trust.d

%files
%dir %_sysconfdir/alterator-ca
%config(noreplace) %_sysconfdir/alterator-ca/dnparam.txt
%_bindir/ca-sh-functions
%_sbindir/ca-sko
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_datadir/alterator/interfaces/guile/type/*
%_datadir/alterator-ca
%_alterator_backend3dir/*
%_libexecdir/alterator/hooks/trust.d/ca
%dir %attr(700,root,root) %_localstatedir/alterator-ca
%dir %_localstatedir/alterator-ca/CA
%dir %_localstatedir/alterator-ca/in
%dir %_localstatedir/alterator-ca/out

%changelog
* Sun May 10 2020 Andrey Cherepanov <cas@altlinux.org> 0.5.8-alt1
- Hide all messages from c_rehash (ALT #38463).

* Tue Mar 24 2020 Slava Aseev <ptrnine@altlinux.org> 0.5.7-alt1
- Use sha256 default_md (Closes: #38213)

* Mon Dec 23 2019 Andrey Cherepanov <cas@altlinux.org> 0.5.6-alt1
- Use compat nameopt for certificate Subject for openssl 1.1.

* Fri Oct 07 2016 Andrey Cherepanov <cas@altlinux.org> 0.5.5-alt1
- Fix URL replace with CSRF preventing token (ALT #32428)
- Fix indentation of form fields

* Tue Nov 24 2009 Alexey I. Froloff <raorn@altlinux.org> 0.5.4-alt1
- Updated for workflow=none (inger)

* Mon Sep 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.5.3-alt1
- Fix remote certificate display

* Mon Aug 10 2009 Alexey I. Froloff <raorn@altlinux.org> 0.5.2-alt1
- Check sign request validity

* Fri Jul 17 2009 Alexey I. Froloff <raorn@altlinux.org> 0.5.1-alt1
- Fix certificate display

* Wed Jun 17 2009 Alexey I. Froloff <raorn@altlinux.org> 0.5-alt2
- Updated deps on alterator-l10n

* Tue May 26 2009 Alexey I. Froloff <raorn@altlinux.org> 0.5-alt1
- Fix file download when ahttpd runs as unprivileged user (closes: #20179)
- Fix upload button (closes: #20181)
- Do not show certificates without matching sign request

* Mon May 25 2009 Alexey I. Froloff <raorn@altlinux.org> 0.4-alt1
- Allow root certificate and sign request download
- Ability to sign uploaded request

* Fri Apr 17 2009 Alexey I. Froloff <raorn@altlinux.org> 0.3-alt1
- Leave Country and Organization empty by default

* Fri Apr 17 2009 Alexey I. Froloff <raorn@altlinux.org> 0.2-alt1
- Announce CA in avahi
- Fix CA path in CA.cnf

* Fri Apr 10 2009 Alexey I. Froloff <raorn@altlinux.org> 0.1-alt1
- Initial build

