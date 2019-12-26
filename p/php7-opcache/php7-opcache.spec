%define		php7_extension	opcache

Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release.2

Summary:	Zend Opcache extension for opcode caching and optimization

Group:		System/Servers
License:	PHP Licence
URL:		http://php.net/manual/en/book.opcache.php
#		http://pecl.php.net/package/ZendOpcache

Packager:       Nikolay A. Fetisov <naf@altlinux.org>

#Source0:	standart PHP module
Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh

Patch0: php7-opcache-sapi-names.patch
Patch1: php7-opcache-file_cache.patch

BuildRequires(pre): rpm-build-php7
BuildRequires: gcc-c++
BuildRequires: php7-devel = %php7_version
BuildRequires: php7 = %php7_version


%description
php7 Opcache extension provides faster PHP execution through
opcode caching and optimization. It improves PHP performance
by storing precompiled script bytecode in the shared memory.
This eliminates the stages of reading code from the disk and
compiling it on future access. In addition, it applies a few
bytecode optimization patterns that make code execution
faster.

%prep
%setup -T -c
cp -pr -- %php7_extsrcdir/%php7_extension/* .

%patch0
%patch1

# Fix path to pdo*.h
subst 's@php/ext@php/%_php7_version/ext@g' config.m4

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
%ifarch %e2k
%add_optflags -U__AVX__ -U__SSE2__
%endif
export LDFLAGS=-lphp-%_php7_version

# Fix for config.m4 in %%prep would't work for some reason
subst 's@php/ext@php/%_php7_version/ext@g' configure

%configure \
	--with-libdir=%_lib \
	--enable-%php7_extension \
	--enable-%php7_extension-file \
	%nil

%php7_make

%install
%php7_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%check
NO_INTERACTION=1 make test

%files
%php7_extconf/%php7_extension
%php7_extdir/*
%doc README

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%version-%release

* Thu Nov 28 2019 Michael Shigorin <mike@altlinux.org> 7.3.12-alt1.2
- Fix build on %%e2k (SIMD needs proper porting)

* Fri Jun 16 2017 Nikolay A. Fetisov <naf@altlinux.org> 7.1.6-alt1.S1.1
- Fix build with enabled Opcache file cache

* Tue Jun 13 2017 Nikolay A. Fetisov <naf@altlinux.org> 7.1.6-alt1.S1
- Initial build for ALT Linux Sisyphus

