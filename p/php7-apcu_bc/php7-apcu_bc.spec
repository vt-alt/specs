%define		php7_extension	apcu_bc
%define 	real_name	apcu_bc
%define		real_version	1.0.5

Name:	 	php7-%{php7_extension}
Version:	%php7_version
Release:	%php7_release

Summary:	PHP7 extension apcu_bc - APCu Backwards Compatibility Module

License:	PHP License
Group:		System/Servers
URL:		https://pecl.php.net/package/apcu_bc
#URL:		https://github.com/krakjoe/apcu-bc

Packager:	Nikolay A. Fetisov <naf@altlinux.org>

Source0:	%real_name-%real_version.tar
Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh
Source3:	apcu-headers.tar

BuildRequires(pre): rpm-build-php7
BuildRequires: php7-devel = %php7_version

Requires: php7-apcu

%description
PHP extension apcu_bc provides a backwards APC compatible
API using APCu.

%prep
%setup -c

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version
%configure \
	--with-%php7_extension \
	--with-libdir=%_lib \
	--enable-apc \
	--enable-apc-mmap \
	#

# We need APCu headers - put them into current directory
sed -e 's#ext/apcu/#apcu/#' -i php_apc.c
tar xvf %SOURCE3

%php7_make

%install
%php7_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%files
%doc README.md LICENSE

%php7_extconf/%php7_extension
%php7_extdir/*

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%version-%release

* Mon Nov 11 2019 Anton Farygin <rider@altlinux.ru> 1.0.5-alt1
- updated to 1.0.5

* Mon Jan 22 2018 Nikolay A. Fetisov <naf@altlinux.org> 7.1.12-alt1.S1
- Initial build for ALT Linux Sisyphus
