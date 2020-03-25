%define _altdata_dir %_datadir/alterator

Name: cert-sh-functions
Version: 1.0.6
Release: alt1

BuildArch: noarch

Source: %name-%version.tar

Summary: helper functions for ssl certificate generation
License: GPL
Group: System/Base
Requires: openssl

%description
helper functions for ssl certificate generation

%prep
%setup

%install
install -Dpm755 cert-sh %buildroot%_bindir/cert-sh
install -Dpm644 %name %buildroot%_bindir/%name

%files
%doc README
%_bindir/*

%changelog
* Fri Mar 13 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.6-alt1
- Use sha256 algorithm for cert generate for request (ALT #38213).

* Mon Dec 23 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- Return ssl_fatal() for compatibility (ALT #37212).

* Wed Apr 17 2019 Mikhail Efremov <sem@altlinux.org> 1.0.4-alt1
- Check for openssl-config existance (closes: #36602).

* Fri Mar 01 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- Support hostname redifinition by HOSTNAME environment variable.

* Fri Dec 04 2015 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1
- Use SHA256 for certificates (thx naf@) (closes #31538).

* Thu Nov 12 2015 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1
- Make DH bits and certificate days configurable.
- Always separate rm's options from arguments.

* Wed Jul 08 2015 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Minor spec cleanup.
- ssl_generate(): Make errors fatal.
- Make new self-signed certificate if expired (closes: #19082).
- Make errors not fatal.
- Fix ssl_check_pem() (closes: #24983).
- Use 1024 bits for dhparam as default.
- Allow set number of bits as argument to ssl_make_key().
- Use 2048 bits for RSA key by default (closes: #31116).

* Thu Apr 23 2009 Alexey I. Froloff <raorn@altlinux.org> 0.3-alt1
- cert-sh: simple wrapper for cert-sh-functions

* Tue Mar 10 2009 Sir Raorn <raorn@altlinux.ru> 0.2-alt1
- Version bump
- Fix certificate sign request generation (ALT#19116)
- Add -batch option to openssl req invocation

* Wed Feb 25 2009 Sir Raorn <raorn@altlinux.ru> 0.1-alt5
- NMU:
     Create link from *.cert to *.pem and rehash SSL_CERTDIR
     ssl_make_req(): accept subject and openssl(1) options as arguments
     Renamed ssl_make_req2() to _ssl_make_req()

* Mon Feb 02 2009 Sir Raorn <raorn@altlinux.ru> 0.1-alt4
- NMU:
     Support for PEM certificates with included key (ALT#15480)
     Make /usr/bin/cert-sh-function non-executable

* Fri Feb 01 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- merge with ldv:
     Source /etc/init.d/functions (ALT#11813)
     ssl_exit_handler: Fix typo
- add README 

* Mon Jan 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- add support for DH parameters generation

* Mon Apr 09 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial release
