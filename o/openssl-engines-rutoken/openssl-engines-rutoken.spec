Summary: Rutoken PKCS#11 engine for OpenSSL
Name: openssl-engines-rutoken
Version: 190628
Release: alt1.88d4ce
License: Proprietary
URL: https://www.rutoken.ru/solutions/freeware/openssl/
#Download: https://www.rutoken.ru/support/download/get/sdk.html

Group: System/Libraries
Source0: %name-%version.tar

ExclusiveArch: %ix86 x86_64

Requires: openssl-engines
Requires: librtpkcs11ecp

%description
Rutoken PKCS#11 engine for OpenSSL

%prep
%setup

%install
mkdir -p %buildroot%_libdir/openssl/engines
%ifarch %ix86
cp -a linux_glibc-x86/lib/librtengine.so* %buildroot%_libdir/openssl/engines/
%else
cp -a linux_glibc-x86_64/lib/librtengine.so* %buildroot%_libdir/openssl/engines/
%endif

%files
%doc license.ru.html
%_libdir/openssl/engines/librtengine.so*

%changelog
* Mon Sep 16 2019 Andrey Cherepanov <cas@altlinux.org> 190628-alt1.88d4ce
- New version from sdk-280619-88d4ce.zip.

* Tue Apr 04 2017 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
