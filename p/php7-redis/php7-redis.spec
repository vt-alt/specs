%define		php7_extension	redis
%define 	real_name	redis
Name:	 	php7-%php7_extension
Version:	5.1.1
Release:	alt%php7_version.%php7_release.1
Summary:	Client extension for Redis key-value store
License:	PHP-3.01
Group:		System/Servers
URL:		https://github.com/nicolasff/phpredis

# Source-url:	https://github.com/phpredis/phpredis/archive/%version.tar.gz
Source:		%name-%version.tar

Source1: redis.ini
Source2: php-redis-params.sh

BuildRequires(pre): rpm-build-php7
BuildRequires: php7-devel = %php7_version

%description
The phpredis extension provides an API for communicating with the Redis key-value store.

%prep
%setup

%build
phpize

%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version
%configure \
	--with-libdir=%_lib

%php7_make

%install
%php7_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%files
%doc CREDITS *.markdown
%php7_extconf/%php7_extension
%php7_extdir/*

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%php7_version-%php7_release

* Fri Dec 13 2019 Anton Farygin <rider@altlinux.org> 5.1.1-alt1
- 3.1.2 -> 5.1.1

* Wed May 17 2017 Vitaly Lipatov <lav@altlinux.ru> 3.1.2-alt7.1.3.alt1.0
- initial build for ALT Sisyphus
