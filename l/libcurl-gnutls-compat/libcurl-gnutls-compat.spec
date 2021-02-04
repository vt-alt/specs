%define libname3 libcurl-gnutls.so.3
%define libname4 libcurl-gnutls.so.4

%if "%_libsuff" == "64"
%define libsuffix (64bit)
%else
%define libsuffix %nil
%endif

Name: libcurl-gnutls-compat
Version: 1.0
Release: alt1

Summary: Libcurl-gnutls compatibility library

License: GPLv3+
Group: System/Libraries
Url: https://github.com/EasyCoding/compat-libcurl-gnutls

BuildRequires: libgnurl
Requires: libgnurl

Provides: %libname3%libsuffix
Provides: %libname3(CURL_GNUTLS_3)%libsuffix
Provides: libcurl3-gnutls

Provides: %libname4%libsuffix
Provides: %libname4(CURL_GNUTLS_4)%libsuffix
Provides: libcurl4-gnutls

%description
Provides libcurl-gnutls compatibility library for different 3rdparty
applications.

%install
mkdir -p %buildroot%_libdir/
ln -s %_libdir/libgnurl.so.4 %buildroot%_libdir/%libname3
ln -s %_libdir/libgnurl.so.4 %buildroot%_libdir/%libname4

%files
%_libdir/%libname3
%_libdir/%libname4

%changelog
* Wed Jan 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus

* Thu May 17 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0-2
- Fixed build under Fedora 28+.
- Resolved new issues with GitKraken.

* Mon Apr 02 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0-1
- Initial release.
