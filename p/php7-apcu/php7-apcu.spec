%define		php7_extension	apcu
%define 	real_name	APCu
%define		real_version	5.1.18

Name:	 	php7-%{php7_extension}
Version:	%php7_version
Release:	%php7_release

Summary:	PHP7 extension APCu - APC User Cache

License:	PHP License
Group:		System/Servers
URL:		http://pecl.php.net/package/APCu
#URL:		https://github.com/krakjoe/apcu

Packager:	Nikolay A. Fetisov <naf@altlinux.org>

Source0:	%real_name-%real_version.tar
Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh


BuildRequires(pre): rpm-build-php7
# Automatically added by buildreq on Tue Jun 13 2017
# optimized out: gnu-config perl php7-libs python-base python-modules python3 python3-base
BuildRequires: glibc-devel-static

BuildRequires: php7-devel = %php7_version
BuildRequires: php7 = %php7_version

%description
PHP extension APCu is an APC stripped of opcode caching in
preparation for the deployment of Zend Optimizer+ as the
primary solution to opcode caching in future versions of PHP.

APCu only supports userland caching (and dumping) of variables,
providing an upgrade path for the APC users. The tried and 
tested APC codebase provides far superior support for local
storage of PHP variables.

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

%php7_make

%install
%php7_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%check
NO_INTERACTION=1 make test

%files
%doc README.md TECHNOTES.txt NOTICE LICENSE

%php7_extconf/%php7_extension
%php7_extdir/*

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%version-%release

* Fri Jan 26 2018 Nikolay A. Fetisov <naf@altlinux.org> 7.1.12-alt1.S1
- New externsion version 5.1.9

* Tue Jun 13 2017 Nikolay A. Fetisov <naf@altlinux.org> 7.1.6-alt1.S1
- Initial build for ALT Linux Sisyphus
