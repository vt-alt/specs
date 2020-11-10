%define		php7_extension	pdo_mysql

Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release

Summary:	MySQL driver for PHP Data Objects Interface

Group:		System/Servers
License:	PHP Licence
URL:		http://www.php.net/manual/en/ref.pdo-mysql.php
#		http://pecl.php.net/package/PDO_MYSQL

Packager:       Nikolay A. Fetisov <naf@altlinux.ru>

#Source0:	standart PHP module
Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh


BuildRequires(pre): rpm-build-php7
BuildRequires: gcc-c++ libMySQL-devel
BuildRequires: php7-devel = %php7_version
Conflicts: php7-mysqlnd-%php7_extension

PreReq: php7-pdo = %php7_version-%release
Provides: php7-pdo-driver


%description
PHP PDO extension provides a uniform data access interface, supporting advanced
features such as prepared statements and bound parameters. 
This package contains a MySQL driver for PDO.

%prep
%setup -T -c
cp -pr -- %php7_extsrcdir/%php7_extension/* .

# Fix path to pdo*.h
subst 's@php/ext@php/%_php7_version/ext@g' config.m4

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version

# Fix for config.m4 in %%prep would't work for some reason
subst 's@php/ext@php/%_php7_version/ext@g' configure

%configure \
	--with-%php7_extension \
	--with-libdir=%_lib \
	--with-pdo-mysql=%_usr \
	#

%php7_make

%install
%php7_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

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

* Sun Mar 03 2019 Nikolai Kostrigin <nickel@altlinux.org> 7.2.15.20180912-alt1.1
- Fix FTBFS against libmysqlclient21
