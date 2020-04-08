%define _name pkcs11-helper
%def_disable LibreSSL
%def_enable openssl
%def_disable LibreSSL # depends on openssl switch above
%def_disable gnutls
%def_disable nss
%def_disable polarssl
%def_disable mbedtls

Name: lib%_name
Version: 1.25.1
Release: alt7
Summary: A library for using PKCS#11 providers

Group: Development/Other
License: GPLv2 or BSD
Url: https://github.com/OpenSC/pkcs11-helper

Source: %name-%version.tar

Provides: %_name = %version-%release
Obsoletes: %_name < %version-%release

%define vkoversion 2.0.0
Patch0: %name-%version-gost-derive.patch
Provides: %name(vko) = %vkoversion

BuildRequires: doxygen graphviz
%if_enabled openssl
%if_enabled LibreSSL
BuildRequires: LibreSSL-devel
%else
BuildRequires: libssl-devel
%endif
%endif
%{?_enable_gnutls:BuildRequires: pkgconfig(gnutls) >= 1.4}
%{?_enable_nss:BuildRequires: pkgconfig(nss) >= 3.11}
%{?_enable_polarssl:BuildRequires: libpolarssl-devel}
%{?_enable_mbedtls:BuildRequires: libmbedtls-devel}

%description
pkcs11-helper is a library that simplifies the interaction with PKCS#11
providers for end-user applications using a simple API and optional OpenSSL
engine. The library allows using multiple PKCS#11 providers at the same time,
enumerating available token certificates, or selecting a certificate directly
by serialized id, handling card removal and card insert events, handling card
re-insert to a different slot, supporting session expiration and much more all
using a simple API.

%package devel
Summary: Development files for pkcs11-helper
Group: Development/Other
Requires: %name = %version-%release
Provides: %_name-devel = %version-%release
Obsoletes: %_name-devel < %version-%release

%description devel
This package contains header files and documentation necessary for developing
programs using the pkcs11-helper library.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure \
		--disable-static \
		--enable-doc \
		--with-apidocdir \
		%{?_disable_openssl:--disable-openssl --disable-crypto-engine-openssl} \
		%{?_disable_gnutls:--disable-crypto-engine-gnutls} \
		%{?_disable_nss:--disable-crypto-engine-nss} \
		%{?_disable_polarssl:--disable-crypto-engine-polarssl} \
		%{?_disable_mbedtls:--disable-crypto-engine-mbedtls} \
		--enable-tests
%make_build

%install
%makeinstall_std INSTALL="install -p"

rm -rf %buildroot%_docdir/%_name/

# Remove libtool .la files
rm -f %buildroot%_libdir/*.la

%files
%doc AUTHORS ChangeLog COPYING* README THANKS
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_aclocaldir/*.m4
%_man8dir/*.8*

%changelog
* Wed Oct 16 2019 Paul Wolneykien <manowar@altlinux.org> 1.25.1-alt7
- Added support for GOST 2012 VKO.
- Don't diversify the resulting GOST key.
- Adapt to the new key derivation data format: key + UKM.

* Mon Feb 18 2019 Paul Wolneykien <manowar@altlinux.org> 1.25.1-alt6
- Pass the decrypt/unwrap/derive result code out of the decryptAny()
  function.

* Mon Feb 18 2019 Paul Wolneykien <manowar@altlinux.org> 1.25.1-alt5
- Really fix bad result code override.

* Mon Feb 18 2019 Paul Wolneykien <manowar@altlinux.org> 1.25.1-alt4
- Fix: Don't override the bad result code of the key decrypt,
  unwrap and derive operations.

* Wed Oct 03 2018 Paul Wolneykien <manowar@altlinux.org> 1.25.1-alt3
- Build with GOST-derive patch. Generate it with gear.
- Deversify the KEK.
- GOST derive: Split the source on UKM and the public key.
- Define the GOST derive mechs.
- Add support for the KeyDerive operation.

* Tue Sep 04 2018 Paul Wolneykien <manowar@altlinux.org> 1.25.1-alt2
- Add the option to build with LibreSSL (currently is off).

* Fri Aug 31 2018 Alexey Shabalin <shaba@altlinux.org> 1.25.1-alt1
- 1.25.1

* Sat Mar 24 2018 Paul Wolneykien <manowar@altlinux.org> 1.22.0-alt2
- Build with LibreSSL.

* Fri Nov 10 2017 Alexey Shabalin <shaba@altlinux.ru> 1.22.0-alt1
- 1.22

* Fri Jun 30 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.12.0-alt3.git20140427
- build with openssl, prevent acidental rebuilds with libressl

* Mon Dec 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.12.0-alt2.git20140427
- fix build (drop BR: libpolarssl-devel)
- rename to libpkcs11-helper
- build with openssl support only

* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.0-alt1.git20140427
- Version 1.12.0

* Tue Apr 26 2011 Mykola Grechukh <gns@altlinux.ru> 1.08-alt1
- new version

* Tue Apr 26 2011 Mykola Grechukh <gns@altlinux.ru> 1.07-alt1
- initial build for ALT Linux Sisyphus

* Mon Jul 13 2009 Kalev Lember <kalev@smartlink.ee> - 1.07-2.1
- Fix EPEL-5 build by adding pkgconfig to BuildRequires.

* Sat Jul 11 2009 Kalev Lember <kalev@smartlink.ee> - 1.07-2
- Make devel package depend on automake for %_datadir/aclocal

* Tue Jun 23 2009 Kalev Lember <kalev@smartlink.ee> - 1.07-1
- Initial RPM release.
