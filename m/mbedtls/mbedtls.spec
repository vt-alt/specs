%define so_tls_version 12
%define so_crypto_version 3
%define so_x509_version 0
%def_disable static

Name: mbedtls
Version: 2.16.3
Release: alt2

Summary: Transport Layer Security protocol suite
License: Apache
Group: System/Libraries

Url: https://tls.mbed.org/
Packager: Nazarov Denis <nenderus@altlinux.org>
Source: https://tls.mbed.org/download/%name-%version-apache.tgz

Patch0: %name-threading-alt.patch

BuildRequires: cmake
BuildRequires: libpkcs11-helper-devel
BuildRequires: python-modules-compiler
BuildRequires: zlib-devel

%description
mbed TLS is a light-weight open source cryptographic and SSL/TLS
library written in C. mbed TLS makes it easy for developers to include
cryptographic and SSL/TLS capabilities in their (embedded)
applications with as little hassle as possible.

%package -n lib%name%so_tls_version
Summary: Transport Layer Security protocol suite
Group: System/Libraries
Conflicts: hiawatha

%description -n lib%name%so_tls_version
mbed TLS is a light-weight open source cryptographic and SSL/TLS
library written in C. mbed TLS makes it easy for developers to include
cryptographic and SSL/TLS capabilities in their (embedded)
applications with as little hassle as possible.

%package -n libmbedcrypto%so_crypto_version
Summary: Cryptographic base library for mbedtls
Group: System/Libraries

%description -n libmbedcrypto%so_crypto_version
This subpackage of mbedtls contains a library that exposes
cryptographic ciphers, hashes, algorithms and format support such as
AES, MD5, SHA, Elliptic Curves, BigNum, PKCS, ASN.1, BASE64.

%package -n libmbedx509-%so_x509_version
Summary: Library to work with X.509 certificates
Group: System/Libraries
Conflicts: hiawatha < 10.10

%description -n libmbedx509-%so_x509_version
This subpackage of mbedtls contains a library that can read, verify
and write X.509 certificates, read/write Certificate Signing Requests
and read Certificate Revocation Lists.

%package -n lib%name-devel
Summary: Development files for mbed TLS
Group: Development/C
Conflicts: hiawatha

%description -n lib%name-devel
Contains libraries and header files for
developing applications that use mbed TLS

%if_enabled static
%package -n lib%name-devel-static
Summary: Static libraries for mbed TLS
Group: Development/C

%description -n lib%name-devel-static
Static libraries for developing applications
that use mbed TLS
%endif

%package utils
Summary: Utilities for PolarSSL
Group: Development/Tools

%description utils
Cryptographic utilities based on mbed TLS 

%prep
%setup
%patch0 -p1

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DENABLE_ZLIB_SUPPORT:BOOL=TRUE \
	-DLIB_INSTALL_DIR:PATH=%_libdir \
	-DUSE_SHARED_MBEDTLS_LIBRARY:BOOL=TRUE \
%if_enabled static
    -DUSE_STATIC_MBEDTLS_LIBRARY:BOOL=TRUE \
%else
    -DUSE_STATIC_MBEDTLS_LIBRARY:BOOL=FALSE \
%endif
	-DUSE_PKCS11_HELPER_LIBRARY:BOOL=TRUE \
	-DCMAKE_BUILD_TYPE:STRING="Release" \
	-Wno-dev

popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform
%__mkdir_p %buildroot%_libexecdir/%name
%__mv %buildroot%_bindir/* %buildroot%_libexecdir/%name
%__rm -rf %buildroot%_bindir

%files -n lib%name%so_tls_version
%_libdir/lib%name.so.*

%files -n libmbedcrypto%so_crypto_version
%_libdir/libmbedcrypto.so.*

%files -n libmbedx509-%so_x509_version
%_libdir/libmbedx509.so.*

%files -n lib%name-devel
%doc apache-2.0.txt ChangeLog LICENSE README.md
%dir %_includedir/%name
%_includedir/%name/*.h
%_libdir/libmbedcrypto.so
%_libdir/lib%name.so
%_libdir/libmbedx509.so

%if_enabled static
%files -n lib%name-devel-static
%_libdir/libmbedcrypto.a
%_libdir/lib%name.a
%_libdir/libmbedx509.a
%endif

%files utils
%dir %_libexecdir/%name
%_libexecdir/%name/*

%changelog
* Tue Nov 05 2019 Nazarov Denis <nenderus@altlinux.org> 2.16.3-alt2
- Fix conflict libmbedx509 with hiawatha package less than 10.10 (ALT #37417)

* Sat Nov 02 2019 Nazarov Denis <nenderus@altlinux.org> 2.16.3-alt1
- Version 2.16.3
- Fix conflict with hiawatha package (ALT #37417)

* Sun Apr 07 2019 Nazarov Denis <nenderus@altlinux.org> 2.16.1-alt1
- Version 2.16.1 (ALT #36525)
- Remove %ubt macro (ALT #36525)

* Tue Jul 24 2018 Nazarov Denis <nenderus@altlinux.org> 2.11.0-alt2%ubt
- Separate subpackages

* Sun Jul 22 2018 Nazarov Denis <nenderus@altlinux.org> 2.11.0-alt1%ubt
- Version 2.11.0

* Thu Apr 12 2018 Nazarov Denis <nenderus@altlinux.org> 2.8.0-alt2%ubt
- Build with with MBEDTLS_THREADING_PTHREAD and MBEDTLS_THREADING_C enabled

* Mon Mar 26 2018 Nazarov Denis <nenderus@altlinux.org> 2.8.0-alt1%ubt
- Version 2.8.0

* Thu Mar 08 2018 Nazarov Denis <nenderus@altlinux.org> 2.7.0-alt1%ubt
- Version 2.7.0

* Sun Nov 12 2017 Nazarov Denis <nenderus@altlinux.org> 2.6.0-alt1%ubt
- Version 2.6.0

* Sun Jul 30 2017 Nazarov Denis <nenderus@altlinux.org> 2.5.1-alt1%ubt
- Version 2.5.1

* Thu Apr 20 2017 Nazarov Denis <nenderus@altlinux.org> 2.4.2-alt0.M80P.1
- Build for branch p8

* Sun Mar 26 2017 Nazarov Denis <nenderus@altlinux.org> 2.4.2-alt1
- Version 2.4.2

* Wed Nov 02 2016 Nazarov Denis <nenderus@altlinux.org> 2.4.0-alt1
- Version 2.4.0

* Sun Jul 17 2016 Nazarov Denis <nenderus@altlinux.org> 2.3.0-alt0.M80P.1
- Build for branch p8

* Wed Jul 13 2016 Nazarov Denis <nenderus@altlinux.org> 2.3.0-alt1
- Version 2.3.0

* Mon Jan 11 2016 Nazarov Denis <nenderus@altlinux.org> 2.2.1-alt1
- Version 2.2.1

* Fri Dec 04 2015 Nazarov Denis <nenderus@altlinux.org> 2.2.0-alt1
- Version 2.2.0

* Sat Nov 07 2015 Nazarov Denis <nenderus@altlinux.org> 2.1.2-alt1
- Version 2.1.2

* Wed Jul 29 2015 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Fri Jun 26 2015 Nazarov Denis <nenderus@altlinux.org> 1.3.11-alt0.M70T.1
- Build for branch t7

* Tue Jun 23 2015 Nazarov Denis <nenderus@altlinux.org> 1.3.11-alt1
- Version 1.3.11

* Mon Mar 23 2015 Andrey Cherepanov <cas@altlinux.org> 1.3.10-alt1.M70P.1
- Backport new version to p7 branch

* Sat Mar 07 2015 Nazarov Denis <nenderus@altlinux.org> 1.3.10-alt0.M70T.1
- Build for branch t7

* Sat Mar 07 2015 Nazarov Denis <nenderus@altlinux.org> 1.3.10-alt2
- Package libmbedtls renamed according to Shared Libs Policy

* Sat Feb 28 2015 Nazarov Denis <nenderus@altlinux.org> 1.3.10-alt1
- Renamed package to mbed TLS
- Version 1.3.10

* Sat Nov 29 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.9-alt1
- Version 1.3.9

* Thu Aug 07 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.8-alt1
- Version 1.3.8

* Thu May 08 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.7-alt1
- Version 1.3.7

* Tue Apr 22 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.6-alt1
- Version 1.3.6

* Sat Apr 05 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.5-alt1
- Version 1.3.5

* Sat Feb 08 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.4-alt0.M70T.1
- Build for branch t7

* Sat Feb 01 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.4-alt1
- Version 1.3.4

* Sun Jan 12 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.3-alt1
- Version 1.3.3

* Wed Nov 06 2013 Nazarov Denis <nenderus@altlinux.org> 1.3.2-alt1
- Version 1.3.2

* Sun Nov 03 2013 Nazarov Denis <nenderus@altlinux.org> 1.3.1-alt1
- Initial build for ALT Linux
