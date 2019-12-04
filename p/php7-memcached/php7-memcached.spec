# TODO: build with igbinary
%define		php7_extension	memcached
%define 	real_name	memcached
%define		real_version	3.1.4

Name:	 	php7-%{php7_extension}
Version:	%php7_version
Release:	%php7_release

Summary:	php7 extension for interfacing with memcached via libmemcached library

License:	PHP License
Group:		System/Servers
URL:		http://pecl.php.net/package/memcached

# Source0-url:	https://github.com/php-memcached-dev/php-memcached/archive/v%real_version.tar.gz
Source0: %name-%real_version.tar
Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh

BuildRequires(pre): rpm-build-php7
BuildRequires: php7-devel = %php7_version
BuildRequires: libmemcached-devel zlib-devel
BuildRequires: php7 memcached /proc

%description
php7-memcached extension uses libmemcached library to provide
API for communicating with memcached servers.

memcached is a high-performance, distributed memory object
caching system, generic in nature, but intended for use in
speeding up dynamic web applications by alleviating database
load.

%prep
%setup -n %name-%real_version

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version

%configure \
	--with-%php7_extension \
	--with-libdir=%_lib \
	--enable-memcached \
	--enable-memcached-json \
	--disable-memcached-sasl \
	%nil
#	--enable-memcached-protocol \
#	--enable-memcached-igbinary \

%php7_make

%install
%php7_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%check
memcached -d
NO_INTERACTION=1 make test

%files
%doc CREDITS README.markdown LICENSE

%php7_extconf/%php7_extension
%php7_extdir/*

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%version-%release

* Wed Apr 19 2017 Vitaly Lipatov <lav@altlinux.ru> 7.1.3-alt1
- initial build 3.0.3 for ALT Sisyphus
