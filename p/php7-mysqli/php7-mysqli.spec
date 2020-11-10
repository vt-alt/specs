%define		php7_extension	mysqli

Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release.2

Summary:	MySQL Improved Extension for PHP

License:	PHP Licence
Group:		System/Servers
URL:		http://www.php.net/manual/en/ref.mysqli.php

#Source0:	standart PHP module
Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh
Conflicts: php7-mysqlnd-mysqli

BuildRequires(pre): rpm-build-php7 
BuildRequires: php7-devel = %php7_version
BuildRequires: libmysqlclient-devel >= 5.1.50-alt5

%description
MySQLi (improved) - MySQL interface for PHP and MySQL 4.1.3+

%prep
%setup -T -c
cp -pr -- %php7_extsrcdir/%php7_extension/* .

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version
%configure \
	--with-%php7_extension \
	--with-libdir=%_lib \
	--with-mysqli=%_bindir/mysql_config \
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

* Tue Dec 18 2018 Nikolai Kostrigin <nickel@altlinux.org> 7.2.13-alt1.2
- Modify php7-mysql8-transition.patch: remove excessive definitions

* Fri Dec 07 2018 Nikolai Kostrigin <nickel@altlinux.org> 7.2.12-alt1.1
- Fix build with MySQL8 client library

* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 5.3.18.20121017-alt1
- Rebuild with php5-5.3.18.20121017-alt1

* Fri Sep 14 2012 Anton Farygin <rider@altlinux.ru> 5.3.17.20120913-alt1
- Rebuild with php5-5.3.17.20120913-alt1

* Mon Feb 13 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1
- Rebuild with php5-5.3.10.20120202-alt1

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt1
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 5.3.6.20110317-alt1
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt2
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt1
- Rebuild with php5-5.3.5.20110105-alt1

* Thu Oct 28 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt3
- Rebuild with php5-5.3.3.20100722-alt3

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt2
- Rebuild with php5-5.3.3.20100722-alt1
- build with libmysqlclient_r (closes: #24142)

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt1
- Rebuild with php5-5.3.3.20100722-alt1

* Wed Aug 04 2010 Anton Farygin <rider@altlinux.ru> 5.2.14.20100721-alt1
- Rebuild with php5-5.2.14.20100721-alt1

* Tue Mar 09 2010 Anton Farygin <rider@altlinux.ru> 5.2.13.20100205-alt1
- Rebuild with php5-5.2.13.20100205-alt1

* Mon Feb 01 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt4
- Rebuild with php5-5.2.12.20091216-alt4

* Fri Jan 29 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt2
- force build with libmysqlclient_r
- rebuild with new php5 build

* Wed Jan 27 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt1
- Rebuild with new php (5.2.12.20091216-alt1)

* Fri Jul 24 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.11.20090722-alt1
- NMU: Rebuild with php5-5.2.11.20090722-alt1.

* Thu Feb 12 2009 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.9.20090205-alt1
- Rebuild with php5-5.2.9.20090205-alt1

* Sun Oct 12 2008 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.7.20080920-alt1
- Rebuild for PHP 5.2.7.20080920 

* Fri Jul 11 2008 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.7.20080627-alt1
- Rebuild for PHP 5.2.7

* Sun Apr 06 2008 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.5-alt1
- Rebuild for PHP 5.2.5-alt1

* Wed Jun 06 2007 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.3-alt1
- Rebuild for PHP 5.2.3-alt1

* Tue May 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.2-alt1
- Rebuild for PHP 5.2.2-alt1

* Wed Apr 18 2007 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.1-alt2
- Rebuild for PHP 5.2.1-alt2

* Thu Mar 22 2007 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.1-alt1
- Initial build for ALT Linux

* Fri Dec 22 2006 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.0-alt1
- Initial build

