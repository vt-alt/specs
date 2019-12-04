%define		php7_extension	xmlrpc

Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release

Summary:	PHP7 module to write XML-RPC servers and clients
Group:		System/Servers
License:	PHP Licence
URL: http://php.net/manual/en/book.xmlrpc.php

Packager:       Nikolay A. Fetisov <naf@altlinux.org>

#Source0:	standart PHP module
Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh

BuildRequires(pre): rpm-build-php7
# Automatically added by buildreq on Tue Jun 13 2017
# optimized out: gnu-config perl php7-libs python-base python-modules python3 python3-base
BuildRequires: glibc-devel-static libxml2-devel

BuildRequires:	php7-devel = %php7_version
BuildRequires:	php7 = %php7_version

%description
PHP7 module XML-RPC can be used to write XML-RPC servers and clients.

%prep
%setup -T -c
cp -pr %php7_extsrcdir/%php7_extension/* .

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version
%configure \
	PHP_ICONV=yes \
	PHP_LIBXML_SHARED=yes \
	--with-libxml-dir=%_usr \
	--with-expat-dir=%_usr \
	--with-%php7_extension
%php7_make

%install
%php7_make_install
install -D -m 644 %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%check
NO_INTERACTION=1 make test

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

* Tue Jun 13 2017 Nikolay A. Fetisov <naf@altlinux.org> 7.1.6-alt1.S1
- Initial build for ALT Linux Sisyphus
