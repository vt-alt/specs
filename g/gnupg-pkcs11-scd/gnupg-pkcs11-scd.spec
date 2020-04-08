%def_disable LibreSSL
%def_enable openssl
%def_disable gnutls

Name: gnupg-pkcs11-scd
Version: 0.9.2
Release: alt8

Summary: A GnuPG PKCS#11 token daemon
Group: System/Configuration/Hardware
License: BSD
Url: https://github.com/alonbl/gnupg-pkcs11-scd

Source: %name-%version.tar
Patch0: %name-%version-gost.patch

%if_enabled LibreSSL
BuildRequires: LibreSSL-devel
%else %if_enabled openssl
BuildRequires: libssl-devel
%endif
%if_enabled gnutls
BuildRequires: libgnutls-devel
%endif
BuildRequires: libassuan-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgpg-error-devel
BuildRequires: libpkcs11-helper-devel

Requires: libpkcs11-helper(vko) >= 2.0.0

%description
gnupg-pkcs11 is a project to implement a BSD-licensed smart-card daemon to
enable the use of PKCS#11 tokens with GnuPG.

PKCS#11 is the de-facto standard for accessing cryptographic tokens, and thus
we strongly disagree with WK\'s attitude towards it.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure --enable-proxy --localstatedir=%_var
%make_build

%install
%makeinstall_std

%check
#%make check

%files
%_bindir/*
%exclude %_docdir/%name/COPYING
%_docdir/%name/README
%_docdir/%name/*.conf.example
%_man1dir/*.1.*

%changelog
* Wed Oct 16 2019 Paul Wolneykien <manowar@altlinux.org> 0.9.2-alt8
- GOST 2012 NIDs, OIDs and PKCS#11 mechanisms.
- Require libpkcs11-helper(vko) >= 2.0.0.
- Adapt for the new key+UKM format used in GnuPG.
- Fixed the typo about Libgcrypt initialization.
- Fixed pk_decrypt() for an RSA key.
- Fixed typo in the "key-friendly" messages.
- Don't abort on error when LEARN the certificates.
- Reverse the digest for GOST signatures.
- Additional GOST 2001 OpenSSL NIDs (XchA, XchB).
- Update to the new OpenSSL version.

* Thu Feb 21 2019 Paul Wolneykien <manowar@altlinux.org> 0.9.2-alt7
- Fixed copying of overlapped memory areas.

* Tue Dec 18 2018 Paul Wolneykien <manowar@altlinux.org> 0.9.2-alt6
- Don't reverse the UKM.

* Thu Oct 04 2018 Paul Wolneykien <manowar@altlinux.org> 0.9.2-alt5
- Fixed OpenSSL 1.1 build: Indirect access of EC GOST key using the
  API function.
- Fixed OpenSSL initialization.
  
* Wed Oct 03 2018 Paul Wolneykien <manowar@altlinux.org> 0.9.2-alt4
- Fix: Use OpenSSL general EC functions to get the key coords.
- Require libpkcs11-helper(vko) >= 1.0.0.

* Wed Oct 03 2018 Paul Wolneykien <manowar@altlinux.org> 0.9.2-alt3
- Generate the GOST patch with gear.

* Tue Sep 04 2018 Paul Wolneykien <manowar@altlinux.org> 0.9.2-alt1
- Switch back to OpenSSL.
- Update to version 0.9.2.

* Wed Jul 25 2018 Paul Wolneykien <manowar@altlinux.org> 0.9.2-alt2
- Build with GOST patch (sign, crypt).

* Wed Jul 25 2018 Paul Wolneykien <manowar@altlinux.org> 0.9.2-alt1
- Fresh up to the version 0.9.2.

* Sat Mar 24 2018 Paul Wolneykien <manowar@altlinux.org> 0.9.1-alt2
- Build with LibreSSL.

* Fri Mar 23 2018 Paul Wolneykien <manowar@altlinux.org> 0.9.1-alt1
- gnupg-pkcs11-scd-0.9.1 (thx Alon Bar-Lev).
- proxy: systemd: enable user's group using SupplementaryGroups
  (thx Alon Bar-Lev).
- scdaemon: introduce GNUPG_PKCS11_SOCKETDIR environment (thx Alon Bar-Lev).
- build: support freebsd usock creds (thx Alon Bar-Lev).
- post gnupg-pkcs11-scd-0.9.0 (thx Alon Bar-Lev).

* Wed Feb 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt2
- Fixed localstatedir location.

* Fri Sep 15 2017 Paul Wolneykien <manowar@altlinux.org> 0.9.0-alt1
- Version 0.9.0: Initial build.
