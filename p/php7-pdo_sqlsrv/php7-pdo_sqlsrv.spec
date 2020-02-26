%define		php7_extension	pdo_sqlsrv
%define		real_version	5.8.0

Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release.1

Summary:	Microsoft Drivers for PHP PDO for SQL Server

License:	%mit
Group:		System/Servers
URL:		https://pecl.php.net/package/pdo_sqlsrv
#URL: https://github.com/Microsoft/msphpsql
#URL: https://docs.microsoft.com/ru-ru/sql/connect/php/microsoft-php-driver-for-sql-server

# This extension can't be used on 32bit or ARM systems - there are no support for 32bit or ARM systems from Microsoft.
ExclusiveArch: x86_64
#BuildArch: x86_64

Packager:	Nikolay A. Fetisov <naf@altlinux.org>

Source0:	%php7_extension.tar
Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh
Source3:	README.ALT
Patch0: php7-pdo_sqlsrv-5.2.0-alt-gcc8.patch

BuildRequires(pre): rpm-build-php7 rpm-build-licenses

# Automatically added by buildreq on Tue Sep 26 2017
# optimized out: gnu-config libstdc++-devel libunixODBC-devel-compat perl php7-libs python-base python-modules python3 python3-base
BuildRequires: gcc-c++ glibc-devel-static libunixODBC-devel php7-devel

BuildRequires: php7-devel = %php7_version

%description
The php7-pdo_sqlsrv package contains the Microsoft Drivers for PHP for SQL
Server are PHP extensions that allow for the reading and writing of SQL Server
data from within PHP scripts. The SQLSRV extension provides a procedural
interface while the PDO_SQLSRV extension implements PDO for accessing data
in all editions of SQL Server 2008 R2 and later (including Azure SQL DB).
These drivers rely on the Microsoft ODBC Driver for SQL Server to handle
the low-level communication with SQL Server.

This package contains only the PDO_SQLSRV driver. Microsoft ODBC Driver 13
must be installed for this extension to work - see README.ALT for details.

%prep
%setup -c
%patch0 -p2

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version
%configure \
	--with-%php7_extension \
	--with-libdir=%_lib \
	#

%php7_make

%install
%php7_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

install -D -m 644 -- %SOURCE3 README.ALT

%files
%php7_extconf/%php7_extension
%php7_extdir/*
%doc CREDITS README.ALT

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%version-%release

* Thu Feb 13 2020 Anton Farygin <rider@altlinux.org> 7.3.14-alt1
- update to 5.8.0

* Tue Sep 26 2017 Nikolay A. Fetisov <naf@altlinux.org> 7.2.6-alt1
- Initial build for ALT Linux Sisyphus

* Tue Sep 26 2017 Nikolay A. Fetisov <naf@altlinux.org> 7.1.9-alt1
- Initial build
