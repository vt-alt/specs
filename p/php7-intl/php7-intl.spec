%define		php7_extension	intl

Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release

Summary:	Internationalization extension is a wrapper for ICU library
Group:		System/Servers
License:	PHP Licence
URL: http://php.net/manual/en/book.intl.php

Packager:       Nikolay A. Fetisov <naf@altlinux.org>

#Source0:	standart PHP module
Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh

BuildRequires(pre): rpm-build-php7
# Automatically added by buildreq on Tue Jun 13 2017
# optimized out: gnu-config libstdc++-devel perl php7-libs python-base python-modules python3 python3-base
BuildRequires: gcc-c++ glibc-devel-static libicu-devel

BuildRequires:	php7-devel = %php7_version


%description
Internationalization extension (further is referred as Intl) is a wrapper
for ICU library, enabling PHP programmers to perform UCA-conformant
collation and date/time/number/currency formatting in their scripts.

It tends to closely follow ICU APIs, so that people having experience
working with ICU in either C/C++ or Java could easily use the PHP
API. Also, this way ICU documentation would be useful to understand
various ICU functions.

%prep
%setup -T -c
cp -pr %php7_extsrcdir/%php7_extension/* .

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
%ifarch %e2k
# lcc-1.23.12: char16_t is undefined otherwise; see also mcst#4060
%add_optflags -std=gnu++11
%endif
export LDFLAGS=-lphp-%_php7_version
%configure \
	--with-php-config=%_bindir/php-config \
	--with-%php7_extension
%php7_make

%install
%php7_make_install
install -D -m 644 %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%files
%php7_extconf/%php7_extension
%php7_extdir/*
%doc CREDITS

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%version-%release

* Sun May 12 2019 Michael Shigorin <mike@altlinux.org> 7.1.8-alt1.1
- Fixed build with lcc 1.23 on e2k

* Tue Jun 13 2017 Nikolay A. Fetisov <naf@altlinux.org> 7.1.6-alt1.S1
- Initial build for ALT Linux Sisyphus
