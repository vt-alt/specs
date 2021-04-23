# spec file for package dehydrated
#

Name: dehydrated
Version: 0.7.0
Release: alt1

Summary: ACME client for signing certificates implemented in Bash

License: %mit
Group:  Security/Networking
Url: https://github.com/lukas2511/dehydrated

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Patch1:  %name-0.7.0-alt-os-release.patch

Source1: %name.config

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses


%description
The dehydrated ACME client for signing certificates with an ACME (Automated
Certificate Management Environment) server (currently only provided by Let's
Encrypt certificate authority).

It is implemented as a relatively simple bash-script that uses the openssl
utility for handling keys and certificates, and cURL to communicate with
the ACME server.

The ACME (Automated Certificate Management Environment) protocol makes
it possible to automatically obtain browser-trusted certificate.

Current features:
* Signing of a list of domains
* Signing of a CSR
* Renewal if a certificate is about to expire or SAN (subdomains) changed
* Certificate revocation


%prep
%setup -n %name-%version
%patch0

%patch1

%build
mv -- docs/examples .

%install
install -D -m 0755 -- %name %buildroot/%_bindir/%name

mkdir -p %buildroot%_sysconfdir/%name/conf.d/
install -m 0644 -- %SOURCE1           %buildroot%_sysconfdir/%name/config
install -m 0755 -- examples/hook.sh   %buildroot%_sysconfdir/%name/hook.sh

mkdir -p -- %buildroot/%_localstatedir/%name/acme-challenge
mkdir -p -- %buildroot/%_localstatedir/%name/accounts
mkdir -p -- %buildroot/%_localstatedir/%name/certs
mkdir -p -- %buildroot/%_localstatedir/%name/chains
mkdir -p -- %buildroot/%_localstatedir/%name/archive
mkdir -p -- %buildroot/%_localstatedir/%name/locks


touch -- %buildroot%_sysconfdir/%name/domains.txt
touch -- %buildroot%_sysconfdir/%name/conf.d/local.sh

%pre
%_sbindir/groupadd -r -f _%name &>/dev/null ||:


%files
%doc README.md CHANGELOG LICENSE
%doc docs/ examples/

%_bindir/%name

%attr(0750,root,_%name) %dir %_sysconfdir/%name
%config(noreplace)  %_sysconfdir/%name/config
%config(noreplace)  %_sysconfdir/%name/hook.sh
%ghost              %_sysconfdir/%name/domains.txt
%dir                %_sysconfdir/%name/conf.d
%ghost              %_sysconfdir/%name/conf.d/local.sh

%attr(0755,root,root)   %dir %_localstatedir/%name
%attr(2770,root,_%name) %dir %_localstatedir/%name/accounts
%attr(2770,root,_%name) %dir %_localstatedir/%name/certs
%attr(2770,root,_%name) %dir %_localstatedir/%name/chains
%attr(2770,root,_%name) %dir %_localstatedir/%name/archive
%attr(2770,root,_%name) %dir %_localstatedir/%name/locks
%attr(2771,root,_%name) %dir %_localstatedir/%name/acme-challenge


%changelog
* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.7.0-alt1
- New version

* Wed Sep 04 2019 Nikolay A. Fetisov <naf@altlinux.org> 0.6.5-alt1
- New version

* Wed May 09 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.6.2-alt1
- New version

* Wed Mar 14 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.6.1-alt1
- New version (Closes: #34642)

* Wed May 10 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.4.0-alt1
- Initial build for ALT Linux Sisyphus
