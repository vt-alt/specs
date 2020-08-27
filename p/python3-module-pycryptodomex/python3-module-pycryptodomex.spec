%define  modulename pycryptodomex

Name:    python3-module-%modulename
Version: 3.9.8
Release: alt1

Summary: A self-contained cryptographic library for Python
License: BSD-2-Clause
Group:   Development/Python3
URL:     https://github.com/Legrandin/pycryptodome

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: libtomcrypt-devel
BuildRequires: python3-module-sphinx

Source:  %modulename-%version.tar
Patch1:  python-pycryptodomex-3.7.3-use_external_libtomcrypt.patch

Provides: python3-pycryptodomex = %EVR
Obsoletes: python3-pycryptodomex < %EVR

%description
PyCryptodome is a self-contained Python package of low-level cryptographic
primitives.

PyCryptodome is a fork of PyCrypto. It brings the following enhancements with
respect to the last official version of PyCrypto (2.6.1):
- Authenticated encryption modes (GCM, CCM, EAX, SIV, OCB)
- Accelerated AES on Intel platforms via AES-NI
- First class support for PyPy
- Elliptic curves cryptography (NIST P-256, P-384 and P-521 curves only)
- Better and more compact API (nonce and iv attributes for ciphers, automatic
  generation of random nonces and IVs, simplified CTR cipher mode, and more)
- SHA-3 (including SHAKE XOFs), truncated SHA-512 and BLAKE2 hash algorithms
- Salsa20 and ChaCha20/XChaCha20 stream ciphers
- Poly1305 MAC
- ChaCha20-Poly1305 and XChaCha20-Poly1305 authenticated ciphers
- scrypt, bcrypt and HKDF derivation functions
- Deterministic (EC)DSA
- Password-protected PKCS#8 key containers
- Shamir's Secret Sharing scheme
- Random numbers get sourced directly from the OS (and not from a CSPRNG in
  userspace)
- Simplified install process, including better support for Windows
- Cleaner RSA and DSA key generation (largely based on FIPS 186-4)
- Major clean ups and simplification of the code base

%prep
%setup -n %modulename-%version
%patch1 -p1

%build
%add_optflags -I%_includedir/tomcrypt
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc AUTHORS.rst README.rst
%python3_sitelibdir/Cryptodome
%python3_sitelibdir/*.egg-info

%changelog
* Fri Aug 14 2020 Andrey Cherepanov <cas@altlinux.org> 3.9.8-alt1
- Initial build for Sisyphus
