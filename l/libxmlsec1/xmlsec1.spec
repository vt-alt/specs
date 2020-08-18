%global _unpackaged_files_terminate_build 1

Name: libxmlsec1
Version: 1.2.28
Release: alt1
License: MIT
Summary: Library providing support for "XML Signature" and "XML Encryption" standards
Group: System/Libraries
Source: %name-%version.tar
Url: https://www.aleksey.com/xmlsec/

BuildRequires: help2man libltdl7-devel man
BuildRequires: libxml2-devel >= 2.8.0 libxslt-devel >= 1.0.20
BuildRequires: libssl-devel >= 1.0.0
BuildRequires: libnss-devel >= 3.11.1 libnspr-devel >= 4.4.1
BuildRequires: libgcrypt-devel >= 1.4.0
BuildRequires: libgnutls-devel >= 2.8.0

%description
XML Security Library is a C library based on LibXML2  and OpenSSL.
The library was created with a goal to support major XML security
standards "XML Digital Signature" and "XML Encryption".

%package devel
Summary: Libraries, includes, etc. to develop applications with XML Digital Signatures and XML Encryption support
Group: System/Libraries
Requires: libxmlsec1

%description devel
Libraries, includes, etc. you can use to develop applications with XML Digital
Signatures and XML Encryption support.

%package openssl
Summary: OpenSSL crypto plugin for XML Security Library
Group: System/Libraries
Requires: libxmlsec1

%description openssl
OpenSSL plugin for XML Security Library provides OpenSSL based crypto services
for the xmlsec library.

%package openssl-devel
Summary: OpenSSL crypto plugin for XML Security Library
Group: System/Libraries
Requires: libxmlsec1-devel libxmlsec1-openssl

%description openssl-devel
Libraries, includes, etc. for developing XML Security applications with OpenSSL

%package gcrypt
Summary: GCrypt crypto plugin for XML Security Library
Group: System/Libraries
Requires: libxmlsec1

%description gcrypt
GCrypt plugin for XML Security Library provides GCrypt based crypto services
for the xmlsec library.

%package gcrypt-devel
Summary: GCrypt crypto plugin for XML Security Library
Group: System/Libraries
Requires: libxmlsec1-devel libxmlsec1-gcrypt

%description gcrypt-devel
Libraries, includes, etc. for developing XML Security applications with GCrypt.

%package gnutls
Summary: GNUTls crypto plugin for XML Security Library
Group: System/Libraries
Requires: libxmlsec1 libxmlsec1-gcrypt

%description gnutls
GNUTls plugin for XML Security Library provides GNUTls based crypto services
for the xmlsec library.

%package gnutls-devel
Summary: GNUTls crypto plugin for XML Security Library
Group: System/Libraries
Requires: libxmlsec1-devel libxmlsec1-gcrypt-devel libxmlsec1-gnutls

%description gnutls-devel
Libraries, includes, etc. for developing XML Security applications with GNUTls.

%package nss
Summary: NSS crypto plugin for XML Security Library
Group: System/Libraries
Requires: libxmlsec1

%description nss
NSS plugin for XML Security Library provides NSS based crypto services
for the xmlsec library

%package nss-devel
Summary: NSS crypto plugin for XML Security Library
Group: System/Libraries
Requires: libxmlsec1-devel libxmlsec1-nss

%description nss-devel
Libraries, includes, etc. for developing XML Security applications with NSS.

%prep
%setup

%build
%autoreconf
%configure --disable-static --enable-gost2012
%make_build

## positively ugly but only sane way to get around #192756
## sed 's+/lib64+/$archlib+g' < xmlsec1-config | sed 's+/lib+/$archlib+g' | sed 's+ -DXMLSEC_NO_SIZE_T++' > xmlsec1-config.$$ && mv xmlsec1-config.$$ xmlsec1-config
sed -i 's/ -DXMLSEC_NO_SIZE_T//' xmlsec1-config

%install
mkdir -p %buildroot/usr/bin
mkdir -p %buildroot/usr/include/xmlsec1
mkdir -p %buildroot%_libdir
mkdir -p %buildroot/usr/man/man1

make DESTDIR=%buildroot install
rm -f %buildroot%_libdir/*.la

%check
# TODO for those who care
true || LD_LIBRARY_PATH=%buildroot%_libdir make check

%files
%doc AUTHORS ChangeLog NEWS README Copyright
%doc %_mandir/man1/xmlsec1.1*
%_libdir/libxmlsec1.so.*
%_bindir/xmlsec1

%files devel
%doc %_defaultdocdir/xmlsec1
%_bindir/xmlsec1-config
%dir %_includedir/xmlsec1
%dir %_includedir/xmlsec1/xmlsec
%dir %_includedir/xmlsec1/xmlsec/private
%_includedir/xmlsec1/xmlsec/*.h
%_includedir/xmlsec1/xmlsec/private/*.h
%_libdir/libxmlsec1.so
%_libdir/pkgconfig/xmlsec1.pc
%_libdir/xmlsec1Conf.sh
%doc AUTHORS HACKING ChangeLog NEWS README Copyright
%_datadir/aclocal/xmlsec1.m4
%_man1dir/xmlsec1-config.*

%files openssl
%_libdir/libxmlsec1-openssl.so.*
%_libdir/libxmlsec1-openssl.so

%files openssl-devel
%_includedir/xmlsec1/xmlsec/openssl/
%_libdir/pkgconfig/xmlsec1-openssl.pc

%files gcrypt
%_libdir/libxmlsec1-gcrypt.so.*
%_libdir/libxmlsec1-gcrypt.so

%files gcrypt-devel
%_includedir/xmlsec1/xmlsec/gcrypt/
%_libdir/pkgconfig/xmlsec1-gcrypt.pc

%files gnutls
%_libdir/libxmlsec1-gnutls.so.*
%_libdir/libxmlsec1-gnutls.so

%files gnutls-devel
%_includedir/xmlsec1/xmlsec/gnutls/
%_libdir/pkgconfig/xmlsec1-gnutls.pc

%files nss
%_libdir/libxmlsec1-nss.so.*
%_libdir/libxmlsec1-nss.so

%files nss-devel
%_includedir/xmlsec1/xmlsec/nss/
%_libdir/pkgconfig/xmlsec1-nss.pc

%changelog
* Thu Sep 12 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.28-alt1
- new version 1.2.28

* Sat Mar 30 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.27-alt1
- 1.2.27

* Mon Sep 10 2018 Alexey Shabalin <shaba@altlinux.org> 1.2.26-alt1
- 1.2.26
- build with openssl-1.1

* Wed Feb 28 2018 Alexey Shabalin <shaba@altlinux.ru> 1.2.25-alt1
- 1.2.25

* Tue Aug 08 2017 Alexey Shabalin <shaba@altlinux.ru> 1.2.24-alt3
- rebuild with Universal Branch Tag

* Mon Aug 07 2017 Alexey Shabalin <shaba@altlinux.ru> 1.2.24-alt2
- Fix missing links to unversioned shared library files (ALT#33703)

* Fri May 19 2017 Fr. Br. George <george@altlinux.ru> 1.2.24-alt1
- Autobuild version bump to 1.2.24

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 1.2.23-alt1
- Autobuild version bump to 1.2.23

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 1.2.22-alt1
- Autobuild version bump to 1.2.22

* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 1.2.20-alt1.1
- NMU: Rebuild with libgnutls30.

* Mon Jun 09 2014 Fr. Br. George <george@altlinux.ru> 1.2.20-alt1
- Autobuild version bump to 1.2.20

* Sun Mar 31 2013 Fr. Br. George <george@altlinux.ru> 1.2.19-alt1
- Autobuild version bump to 1.2.19

* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 1.2.18-alt1
- Initial build from FC
