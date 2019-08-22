%def_with libproxy
%def_with stoken
# openssl or gnutls
%def_without openssl
%def_with gnutls

Name: openconnect
Version: 8.04
Release: alt1
Summary: Open client for Cisco AnyConnect VPN

Group: Networking/Remote access
License: LGPLv2.1+
Url: http://www.infradead.org/openconnect.html

Source: %name-%version.tar

Requires: lib%name = %version-%release
BuildRequires: pkgconfig(liblz4)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(zlib)
%{?_with_gnutls:BuildRequires: pkgconfig(gnutls) > 3.2.10 pkgconfig(p11-kit-1) libtrousers-devel pkgconfig(libtasn1)}
%{?_with_openssl:BuildRequires: pkgconfig(openssl) pkgconfig(p11-kit-1) pkgconfig(libp11) >= 0.4.7}
%{?_with_libproxy:BuildRequires: pkgconfig(libproxy-1.0)}
%{?_with_stoken:BuildRequires: pkgconfig(stoken)}
BuildRequires: pkgconfig(libpcsclite)
BuildRequires: vpnc-script
BuildRequires: libkrb5-devel
BuildRequires: python3 groff-extra
Requires: vpnc-script
%{?_with_openssl:Requires: openssl >= 1.0.1e}

%description
This package provides a client for Cisco's "AnyConnect" VPN, which uses
HTTPS and DTLS protocols.

%package -n lib%name
Group: System/Libraries
Summary: Shared libraries for %name

%description -n lib%name
%summary

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q

%build
%autoreconf
%configure \
	--enable-static=no \
	%{subst_with libproxy} \
	%{subst_with stoken} \
	%{subst_with liboath} \
	--with-system-cafile=/usr/share/ca-certificates/ca-bundle.crt

echo "const char *openconnect_version_str = \"v%version\";" > version.c
%make_build

%install
make DESTDIR=%buildroot install
%find_lang %name

%files -f %name.lang
%doc TODO COPYING.LGPL
%_sbindir/%name
%_man8dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Wed Aug 21 2019 Alexey Shabalin <shaba@altlinux.org> 8.04-alt1
- new version 8.04

* Sat Jul 20 2019 Alexey Shabalin <shaba@altlinux.org> 8.03-alt1
- new version 8.03

* Sat Feb 02 2019 Alexey Shabalin <shaba@altlinux.org> 8.02-alt1
- new version 8.02

* Tue Jan 08 2019 Alexey Shabalin <shaba@altlinux.org> 8.01-alt1
- new version 8.01
- fixed clear form submissions before freeing (CVE-2018-20319)

* Fri Dec 30 2016 Alexey Shabalin <shaba@altlinux.ru> 7.08-alt1
- 7.08

* Sat Nov 19 2016 Alexey Shabalin <shaba@altlinux.ru> 7.07-alt1
- 7.07
- switch to gnutls
- build with pkcs11 support

* Fri Oct 07 2016 Vladimir Didenko <cow@altlinux.ru> 7.06-alt1
- 7.06 (closes: #32583)
- build with stoken

* Wed Jul 30 2014 Alexey Shabalin <shaba@altlinux.ru> 6.00-alt1
- 6.00

* Wed Mar 05 2014 Alexey Shabalin <shaba@altlinux.ru> 5.99-alt1
- 5.99
- switch to openssl back

* Wed Sep 04 2013 Alexey Shabalin <shaba@altlinux.ru> 5.01-alt1
- 5.01

* Wed Jan 30 2013 Alexey Shabalin <shaba@altlinux.ru> 4.07-alt1
- 4.07

* Mon Aug 06 2012 Alexey Shabalin <shaba@altlinux.ru> 4.06-alt1
- 4.06

* Tue May 22 2012 Alexey Shabalin <shaba@altlinux.ru> 3.20-alt1
- 3.20

* Wed Nov 16 2011 Alexey Shabalin <shaba@altlinux.ru> 3.14-alt1
- 3.14

* Thu Sep 15 2011 Alexey Shabalin <shaba@altlinux.ru> 3.12-alt1
- 3.12

* Fri May 27 2011 Alexey Shabalin <shaba@altlinux.ru> 3.02-alt1
- 3.02

* Wed Apr 20 2011 Alexey Shabalin <shaba@altlinux.ru> 2.26-alt2
- update BR:

* Fri Nov 12 2010 Alexey Shabalin <shaba@altlinux.ru> 2.26-alt1
- 2.26

* Tue Oct 12 2010 Alexey Shabalin <shaba@altlinux.ru> 2.25-alt2
- pre 2.26

* Sun May 16 2010 Alexey Shabalin <shaba@altlinux.ru> 2.25-alt1
- 2.25

* Mon Mar 15 2010 Alexey Shabalin <shaba@altlinux.ru> 2.22-alt1.git9b782
- git snapshot 9b782af3aa4d2fb3b238bbfdd12b217db80f83cd
- rebuild with new libproxy-0.4.0

* Wed Mar 03 2010 Alexey Shabalin <shaba@altlinux.ru> 2.21-alt2.git357c85
- git snapshot 357c85e8db1949565e99695b17cf5dadbc679269

* Sat Jan 16 2010 Alexey Shabalin <shaba@altlinux.ru> 2.21-alt1
- Initial packaging
