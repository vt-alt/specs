%define php7_extension	xdebug

Name: php7-%php7_extension
Version: %php7_version
Release: %php7_release

Summary: xdebug extensions
Group: System/Servers
License: PHP Licence

# Source-url: https://xdebug.org/files/xdebug-2.8.0.tgz
Source: php7-%php7_extension.tar
Source1: php-%php7_extension.ini
Source2: php-%php7_extension-params.sh

BuildRequires(pre): rpm-build-php7
BuildRequires: php7-devel = %php7_version
BuildRequires: php7 = %php7_version

%description
Xdebug is an extension for PHP to assist with debugging and development.
It contains a single step debugger to use with IDEs;
it upgrades PHP's var_dump() function;
it adds stack traces for Notices, Warnings, Errors and Exceptions;
it features functionality for recording every function call and
variable assignment to disk; it contains a profiler;
and it provides code coverage functionality for use with PHPUnit.

%prep
%setup -n php7-%php7_extension
%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version
%configure \
	--with-%php7_extension=%_usr
%php7_make

%install
install -D -m 644 modules/xdebug.so %buildroot%php7_extdir/xdebug.so
install -D -m 644 %SOURCE1 %buildroot%php7_extconf/%php7_extension/config
install -D -m 644 %SOURCE2 %buildroot%php7_extconf/%php7_extension/params

%files
%php7_extconf/%php7_extension
%php7_extdir/xdebug.so

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%php7_version-%php7_release

* Mon Nov 11 2019 Anton Farygin <rider@altlinux.ru> 7.3.10-alt1
- updated to 2.8.0

* Fri Dec 21 2018 Anton Farygin <rider@altlinux.ru> 7.2.13-alt1.1
- updated to 2.6.1
- removed fullpath to module in config

* Tue Jan 30 2018 Vitaly Lipatov <lav@altlinux.ru> 7.1.12-alt0
- initial build xdebug 2.6.0 for ALT Sisyphus

