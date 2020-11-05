Name: phpMyAdmin
Version: 5.0.4
Release: alt1

Summary: phpMyAdmin - web-based MySQL administration

License: GPL
Group: System/Servers
Url: http://www.phpmyadmin.net

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source: http://prdownloads.sourceforge.net/phpmyadmin/%name-%version-all-languages.tar
Source: https://files.phpmyadmin.net/phpMyAdmin/%version/phpMyAdmin-%version-all-languages.tar
Source2: %name-README.ALT
Source3: %name.htaccess
Source6: %name.A.conf
Source8: %name-apache2.control

Provides: phpmyadmin
Obsoletes: %name-common

BuildArch: noarch

Requires: pwgen webserver-common control
Requires: apache2-base >= 2.4

BuildPreReq: rpm-build-apache2 rpm-macros-webserver-common

BuildRequires: apache2-base >= 2.4
BuildRequires: control

AutoReq:yes,noshell,nomingw32,nopython

%description
phpMyAdmin can administer a whole MySQL-server (needs a super-user)
but also a single database. To accomplish the latter you'll need a
properly set up MySQL-user who can read/write only the desired
database. It's up to you to look up the appropiate part in the MySQL
manual. Currently phpMyAdmin can:
  - create and drop databases
  - create, copy, drop and alter tables
  - delete, edit and add fields
  - execute any SQL-statement, even batch-queries
  - manage keys on fields
  - load text files into tables
  - create (*) and read dumps of tables
  - export (*) and import data to CSV values
  - administer multiple servers and single databases
  - communicate in more than 20 different languages

%if_with php5
%package apache2
Summary: phpMyAdmin - web-based MySQL administration (for apache 2.x and php5)
Group: System/Servers
Requires: %name = %version-%release
Requires: apache2-mod_php5 >= 5.2.0
Requires: apache2-base
Requires: php5-mysqli
Requires: php5-mcrypt
Requires: php5-mbstring
Requires: php5-gd2
Conflicts: %name-apache2-php7

%description apache2
phpMyAdmin can administer a whole MySQL-server (needs a super-user)
but also a single database. To accomplish the latter you'll need a
properly set up MySQL-user who can read/write only the desired
database. It's up to you to look up the appropiate part in the MySQL
manual. Currently phpMyAdmin can:
  - create and drop databases
  - create, copy, drop and alter tables
  - delete, edit and add fields
  - execute any SQL-statement, even batch-queries
  - manage keys on fields
  - load text files into tables
  - create (*) and read dumps of tables
  - export (*) and import data to CSV values
  - administer multiple servers and single databases
  - communicate in more than 20 different languages

Install this package if you need phpMyAdmin for apache 2.x and php5.

%endif

%package apache2-php7
Summary: phpMyAdmin - web-based MySQL administration (for apache 2.4 and php7)
Group: System/Servers
Requires: %name = %version-%release
Requires: apache2-mod_php7 >= 7.0.0
Requires: apache2-base
# needed MYSQLI_TYPE_JSON exists only in mysqlnd
Requires: php7-mysqlnd-mysqli
Requires: php7-mcrypt
Requires: php7-mbstring
Requires: php7-gd2
Requires: php7-zip
Conflicts: %name-apache2

%description apache2-php7
phpMyAdmin can administer a whole MySQL-server (needs a super-user)
but also a single database. To accomplish the latter you'll need a
properly set up MySQL-user who can read/write only the desired
database. It's up to you to look up the appropiate part in the MySQL
manual. Currently phpMyAdmin can:
  - create and drop databases
  - create, copy, drop and alter tables
  - delete, edit and add fields
  - execute any SQL-statement, even batch-queries
  - manage keys on fields
  - load text files into tables
  - create (*) and read dumps of tables
  - export (*) and import data to CSV values
  - administer multiple servers and single databases
  - communicate in more than 20 different languages

Install this package if you need phpMyAdmin for apache 2.4 and php7.

%prep
%setup

%install
mkdir -p %buildroot%webserver_webappsdir

cp config.sample.inc.php config.inc.php
# see https://bugzilla.altlinux.org/show_bug.cgi?id=37954
echo "\$cfg['TempDir'] = '/tmp';" >> config.inc.php

cp -r ../%name-%version %buildroot%webserver_webappsdir/%name

# remove unneeded
rm -rf %buildroot%webserver_webappsdir/%name/test/
rm -rf %buildroot%webserver_webappsdir/%name/doc/{_ext,doctrees,Makefile,make.bat,conf.py,*.rst}
rm -f %buildroot%webserver_webappsdir/%name/{.coveralls.yml,.editorconfig,.eslintignore,.eslintrc.json}

cp -a %SOURCE3 %buildroot%webserver_webappsdir/%name/.htaccess
cp %SOURCE2 .

%__mkdir_p %buildroot%apache2_extra_available
%__mkdir_p %buildroot%apache2_extra_enabled
cp %SOURCE6 %buildroot%apache2_extra_available/%name.conf
%__subst 's|--dir--|%webserver_webappsdir/%name|g' %buildroot%apache2_extra_available/%name.conf
ln -s %apache2_extra_available/%name.conf %buildroot%apache2_extra_enabled/%name.conf

#make control modules
#__mkdir_p %buildroot%_controldir
#cp %SOURCE8 %buildroot%_controldir/%name-apache2
#__subst 's|--dir--|%apache2_extra_available|g' %buildroot%_controldir/%name-apache2

%post
%__subst "s|\(blowfish_secret'\] = \)''|\1'$(pwgen -0s1 32)'|" %webserver_webappsdir/%name/config.inc.php

#pre apache2
#pre_control %name-apache2

#post apache2
#post_control -s restricted %name-apache2

%files
%doc phpMyAdmin-README.ALT README* ChangeLog
%dir %webserver_webappsdir/%name/
%webserver_webappsdir/%name/*
%config(noreplace) %webserver_webappsdir/%name/.htaccess
# yes, will notify about duplicate file
%attr(640,root,%webserver_group) %config(noreplace) %webserver_webappsdir/%name/config.inc.php
%exclude %webserver_webappsdir/%name/setup

%if_with php5
%files apache2
%config(noreplace) %apache2_extra_available/%name.conf
%apache2_extra_enabled/%name.conf
#attr(755,root,root) %_controldir/%name-apache2
%endif

%files apache2-php7
%config(noreplace) %apache2_extra_available/%name.conf
%apache2_extra_enabled/%name.conf
#attr(755,root,root) %_controldir/%name-apache2

%changelog
* Thu Oct 29 2020 Vitaly Lipatov <lav@altlinux.ru> 5.0.4-alt1
- new version 5.0.4 (with rpmrb script)

* Tue Oct 13 2020 Vitaly Lipatov <lav@altlinux.ru> 5.0.3-alt1
- new version 5.0.3 (with rpmrb script)
- several important security fixes:
 + PMASA-2020-5 XSS vulnerability with transformation feature
 + MASA-2020-6 SQL injection vulnerability with the search feature

* Thu Jun 04 2020 Vitaly Lipatov <lav@altlinux.ru> 5.0.2-alt1
- new version 5.0.2 (with rpmrb script)

* Fri Jan 31 2020 Vitaly Lipatov <lav@altlinux.ru> 5.0.1-alt3
- fix blowfish_secret length, add tmp dir path (ALT bug 37954)

* Wed Jan 22 2020 Vitaly Lipatov <lav@altlinux.ru> 5.0.1-alt2
- use php7-mysqlnd-mysqli (contains MYSQLI_TYPE_JSON)

* Thu Jan 16 2020 Vitaly Lipatov <lav@altlinux.ru> 5.0.1-alt1
- new version 5.0.1 (with rpmrb script)
- PMASA-2020-1 is an SQL injection vulnerability

* Sat Nov 23 2019 Vitaly Lipatov <lav@altlinux.ru> 4.9.2-alt1
- new version 4.9.2 (with rpmrb script)

* Tue Jun 11 2019 Vitaly Lipatov <lav@altlinux.ru> 4.9.0.1-alt1
- new version 4.9.0.1 (with rpmrb script)
+ PMASA-2019-3 is an SQL injection flaw in the Designer feature
+ PMASA-2019-4 is a CSRF attack that's possible through the 'cookie' login form

* Mon Mar 04 2019 Vitaly Lipatov <lav@altlinux.ru> 4.8.5-alt2
- disable php5 subpackage

* Thu Feb 21 2019 Vitaly Lipatov <lav@altlinux.ru> 4.8.5-alt1
- new version 4.8.5 (with rpmrb script)

* Fri Aug 24 2018 Vitaly Lipatov <lav@altlinux.ru> 4.8.3-alt1
- new version 4.8.3 (with rpmrb script)

* Fri Jun 22 2018 Vitaly Lipatov <lav@altlinux.ru> 4.8.2-alt1
- new version (4.8.2) with rpmgs script
- restore subpackage for php5

* Mon May 28 2018 Vitaly Lipatov <lav@altlinux.ru> 4.8.1-alt1
- new version 4.8.1 (with rpmrb script)
- drop php5 support

* Tue Mar 20 2018 Vitaly Lipatov <lav@altlinux.ru> 4.7.9-alt1
- new version 4.7.9 (with rpmrb script)

* Thu Jan 25 2018 Vitaly Lipatov <lav@altlinux.ru> 4.7.7-alt1
- new version 4.7.7 (with rpmrb script)

* Wed Aug 30 2017 Vitaly Lipatov <lav@altlinux.ru> 4.7.4-alt1
- new version 4.7.4 (with rpmrb script)

* Fri Jul 28 2017 Vitaly Lipatov <lav@altlinux.ru> 4.7.3-alt1
- new version 4.7.3 (with rpmrb script)

* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 4.7.2-alt1
- new version 4.7.2 (with rpmrb script)

* Fri Jun 23 2017 Vitaly Lipatov <lav@altlinux.ru> 4.7.1-alt1
- new version 4.7.1 (with rpmrb script)

* Sat May 13 2017 Vitaly Lipatov <lav@altlinux.ru> 4.7.0-alt1
- new version 4.7.0 (with rpmrb script)

* Sat Mar 04 2017 Vitaly Lipatov <lav@altlinux.ru> 4.6.6-alt1
- new version 4.6.6 (with rpmrb script)

* Wed Dec 07 2016 Vitaly Lipatov <lav@altlinux.ru> 4.6.5.2-alt1
- new version 4.6.5.2 (with rpmrb script)

* Fri Jul 15 2016 Vitaly Lipatov <lav@altlinux.ru> 4.6.3-alt1
- new version 4.6.3 (with rpmrb script)

* Sat May 21 2016 Vitaly Lipatov <lav@altlinux.ru> 4.6.1-alt1
- new version 4.6.1 (with rpmrb script)
- drop apache subpackage (was for Apache 1.3)

* Fri Dec 05 2014 Vitaly Lipatov <lav@altlinux.ru> 4.2.13.1-alt1
- new version 4.2.13.1 (with rpmrb script)

* Tue Nov 25 2014 Vitaly Lipatov <lav@altlinux.ru> 4.2.12-alt1
- new version 4.2.12 (with rpmrb script)

* Thu Nov 13 2014 Vitaly Lipatov <lav@altlinux.ru> 4.2.11-alt1
- new version 4.2.11 (with rpmrb script)

* Wed Oct 01 2014 Vitaly Lipatov <lav@altlinux.ru> 4.2.9.1-alt1
- new version 4.2.9.1 (with rpmrb script)

* Tue Sep 23 2014 Vitaly Lipatov <lav@altlinux.ru> 4.2.9-alt1
- new version 4.2.9 (with rpmrb script)

* Sat Sep 13 2014 Vitaly Lipatov <lav@altlinux.ru> 4.2.8.1-alt1
- new version 4.2.8.1 (with rpmrb script)

* Tue Sep 02 2014 Vitaly Lipatov <lav@altlinux.ru> 4.2.8-alt1
- new version 4.2.8 (with rpmrb script)

* Fri Aug 22 2014 Vitaly Lipatov <lav@altlinux.ru> 4.2.7.1-alt1
- new version 4.2.7.1 (with rpmrb script)

* Mon Jul 28 2014 Vitaly Lipatov <lav@altlinux.ru> 4.2.6-alt1
- new version 4.2.6 (with rpmrb script)

* Mon May 05 2014 Vitaly Lipatov <lav@altlinux.ru> 4.1.14-alt1
- new version 4.1.14 (with rpmrb script)

* Wed Apr 09 2014 Vitaly Lipatov <lav@altlinux.ru> 4.1.12-alt1
- new version 4.1.12 (with rpmrb script)

* Wed Nov 13 2013 Vitaly Lipatov <lav@altlinux.ru> 4.0.9-alt1
- new version 4.0.9 (with rpmrb script)
- comment out memory_limit in .htaccess (ALT bug #29570)

* Sun Oct 13 2013 Vitaly Lipatov <lav@altlinux.ru> 4.0.8-alt1
- new version 4.0.8 (with rpmrb script)

* Sat Sep 07 2013 Vitaly Lipatov <lav@altlinux.ru> 4.0.6-alt1
- new version 4.0.6 (with rpmrb script)

* Thu Sep 05 2013 Vitaly Lipatov <lav@altlinux.ru> 4.0.5-alt1
- new version 4.0.5 (with rpmrb script)
- require php5-mysqli
- drop doc source from binary package (was require python sphinx)

* Wed Apr 10 2013 Vitaly Lipatov <lav@altlinux.ru> 3.5.8-alt1
- new version 3.5.8 (with rpmrb script)
- cleanup spec, mark conf files as config
- fix default configs

* Wed Dec 19 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.5.4-alt2
- Require apache2-base, apache-base package (ALT #28238)

* Mon Dec 03 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.5.4-alt1
- 3.3.10 -> 3.5.4
- Repocop: altlinux-policy-obsolete-httpd2-reload
- security bug fix
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-3.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-4.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-5.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-6.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-7.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-8.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-9.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-10.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-11.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-12.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-13.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-14.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-15.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-16.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-17.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-18.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-19.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-20.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2012-1.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2012-2.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2012-3.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2012-4.php

* Tue Mar 22 2011 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.3.10-alt1
- 3.3.7 -> 3.3.10
- FIX #24423
- security bug fix
  + http://www.phpmyadmin.net/home_page/security/PMASA-2010-6.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2010-7.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2010-8.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2010-9.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2010-10.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-1.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2011-2.php

* Fri Sep 10 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.3.7-alt1
- 3.3.5 -> 3.3.7
- security bug fix
  + http://www.phpmyadmin.net/home_page/security/PMASA-2010-5.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2010-6.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2010-7.php

* Wed Aug 11 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.3.5-alt1
- 3.3.3 -> 3.3.5
- Fix alias for apache2 (phpMyAdmin)

* Wed May 26 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.3.3-alt2
- fixed php_value for php5

* Wed May 26 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.3.3-alt1
- 3.3.2-rc1 -> 3.3.3

* Mon Apr 19 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.3.2-alt0.1
- 3.2.4 -> 3.3.2-rc1

* Sun Jan 10 2010 Dmitriy Kulik <lnkvisitor at altlinux.org> 3.2.4-alt3.1
- fix chmod for control modules
- fix pach in control modules
- fix requires

* Sun Jan 10 2010 Dmitriy Kulik <lnkvisitor at altlinux.org> 3.2.4-alt3
- rebased with WebPolicy
- added control modules
- removed common package
- relocated to group System/Servers

* Fri Dec 25 2009 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.2.4-alt2
- (ALT #22561)

* Wed Dec 23 2009 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.2.4-alt1
- 3.1.1 -> 3.2.4
- security bug fix (ALT #20402, #20647)
  + http://www.phpmyadmin.net/home_page/security/PMASA-2009-1.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2009-2.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2009-3.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2009-4.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2009-5.php
  + http://www.phpmyadmin.net/home_page/security/PMASA-2009-6.php

* Sat Dec 13 2008 Dmitriy Kulik  <lnkvisitor@altlinux.org> 3.1.1-alt1
- 3.1.0 -> 3.1.1
- security bug fix:
  + SQL injection through XSRF on several pages
  + http://www.phpmyadmin.net/home_page/security/PMASA-2008-10.php

* Fri Dec 12 2008 Dmitriy Kulik  <lnkvisitor@altlinux.org> 3.1.0-alt1
- 2.11.9.3 -> 3.1.0
- removed subpackage phpMyAdmin-apache-php4
- removed subpackage phpMyAdmin-apache2-php4
- renamed subpackage phpMyAdmin-apache-php5 to phpMyAdmin-apache
- renamed subpackage phpMyAdmin-apache2-php5 to phpMyAdmin-apache2

* Sun Nov 02 2008 Dmitriy Kulik  <lnkvisitor@altlinux.org> 2.11.9.3-alt1
- 2.11.8.1 -> 2.11.9.3
- Added apache config for alias /phpMyAdmin (bugfix #17713)
- Added phpMyAdmin default configuration file and generate blowfish_secret
- security bug fix:
  + Code execution vulnerability
  + http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2008-7
  + XSS in MSIE using NUL byte
  + http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2008-8
  + XSS on a Designer component
  + http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2008-9

* Sat Aug 02 2008 Igor Zubkov <icesik@altlinux.org> 2.11.8.1-alt1
- 2.11.7.1 -> 2.11.8.1
- this is security bug fix release:
  + Cross-site Framing; XSS in setup.php
  + http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2008-6

* Sun Jul 20 2008 Igor Zubkov <icesik@altlinux.org> 2.11.7.1-alt1
- 2.11.7 -> 2.11.7.1
- this is security bug fix release:
  + XSRF/CSRF for creating a database and modifying user charset
  + http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2008-5

* Wed Jun 25 2008 Igor Zubkov <icesik@altlinux.org> 2.11.7-alt1
- 2.11.6 -> 2.11.7
- this is security bug fix release:
  + XSS on plausible insecure PHP installation
  + http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2008-4

* Wed Apr 30 2008 Igor Zubkov <icesik@altlinux.org> 2.11.6-alt1
- 2.11.5.2 -> 2.11.6

* Wed Apr 23 2008 Igor Zubkov <icesik@altlinux.org> 2.11.5.2-alt1
- 2.11.5.1 -> 2.11.5.2
- this is security bug fix release:
  + File disclosure on shared hosts via a crafted HTTP POST request
  + http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2008-3

* Sun Mar 30 2008 Igor Zubkov <icesik@altlinux.org> 2.11.5.1-alt1
- 2.11.5 -> 2.11.5.1
- this is security bug fix release:
  + Credentials disclosure on shared hosts via session data
  + http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2008-2

* Tue Mar 04 2008 Igor Zubkov <icesik@altlinux.org> 2.11.5-alt1
- 2.11.4 -> 2.11.5
- this is security bug fix release:
  + SQL injection vulnerability (Delayed Cross Site Request Forgery)
  + http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2008-1

* Tue Jan 15 2008 Igor Zubkov <icesik@altlinux.org> 2.11.4-alt1
- 2.11.3 -> 2.11.4
- this is security bug fix release:
  + path disclosure on darkblue_orange/layout.inc.php

* Wed Dec 12 2007 Igor Zubkov <icesik@altlinux.org> 2.11.3-alt1
- 2.11.2.2 -> 2.11.3

* Wed Nov 21 2007 Igor Zubkov <icesik@altlinux.org> 2.11.2.2-alt1
- 2.11.2.1 -> 2.11.2.2
- this is security bug fix release, see:
  + http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2007-8

* Sun Nov 11 2007 Igor Zubkov <icesik@altlinux.org> 2.11.2.1-alt1
- 2.11.2 -> 2.11.2.1
- this is security bug fix release, see:
  + http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2007-7

* Tue Oct 30 2007 Igor Zubkov <icesik@altlinux.org> 2.11.2-alt1
- 2.11.1.2 -> 2.11.2

* Tue Oct 23 2007 Igor Zubkov <icesik@altlinux.org> 2.11.1.2-alt1
- 2.11.1.1 -> 2.11.1.2
- this is security bug fix release, see:
  + http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2007-6

* Tue Oct 23 2007 Igor Zubkov <icesik@altlinux.org> 2.11.1.1-alt1
- 2.10.3 -> 2.11.1.1
- this is security bug fix release, see:
  + http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2007-5

* Fri Jul 20 2007 Igor Zubkov <icesik@altlinux.org> 2.10.3-alt1
- 2.10.2 -> 2.10.3

* Mon Jun 18 2007 Igor Zubkov <icesik@altlinux.org> 2.10.2-alt3
- add configure tutorial (closes #11719)

* Sat Jun 16 2007 Igor Zubkov <icesik@altlinux.org> 2.10.2-alt2
- 2.10.2-rc1 -> 2.10.2 (bugfix release)

* Sun Jun 10 2007 Igor Zubkov <icesik@altlinux.org> 2.10.2-alt1.rc1
- 2.10.1 -> 2.10.2-rc1 (bugfix release)

* Tue Apr 24 2007 Igor Zubkov <icesik@altlinux.org> 2.10.1-alt3
- 2.10.1-rc1 -> 2.10.1
- this is security bug fix release, see:
  + http://secunia.com/advisories/24952/ (cross-site scripting)

* Sat Apr 21 2007 Igor Zubkov <icesik@altlinux.org> 2.10.1-alt2.rc1
- new subpackage -> phpMyAdmin-apache2-php4

* Sun Apr 15 2007 Igor Zubkov <icesik@altlinux.org> 2.10.1-alt1.rc1
- 2.10.0.2 -> 2.10.1-rc1
- fix requires (closes #11498)
  + add php-mcrypt and php-mbstring to phpMyAdmin-apache-php4
  + add php5-mcrypt and php5-mbstring to phpMyAdmin-apache-php5
  + add php5-mcrypt and php5-mbstring to phpMyAdmin-apache2-php5

* Sat Mar 03 2007 Igor Zubkov <icesik@altlinux.org> 2.10.0.2-alt1
- http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2007-3
  + aka CVE-2006-1549

* Thu Mar 01 2007 Igor Zubkov <icesik@altlinux.org> 2.10.0.1-alt1
- 2.9.2 -> 2.10.0.1

* Wed Feb 21 2007 Igor Zubkov <icesik@altlinux.org> 2.9.2-alt1
- 2.9.1.1 -> 2.9.2 (security bug fix)
- http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2007-1
- http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2007-2

* Mon Nov 20 2006 Igor Zubkov <icesik@altlinux.org> 2.9.1.1-alt1
- 2.9.1-rc2 -> 2.9.1.1 (security bug fix)
- http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2006-7
- http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2006-8
- http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2006-9

* Wed Nov 01 2006 Igor Zubkov <icesik@altlinux.org> 2.9.1-alt1.rc2
- 2.9.1-rc1 -> 2.9.1-rc2 (security bug fix)
- http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2006-6
- remove from phpMyAdmin requires mod_php and php-mysql
- add to phpMyAdmin package requires phpMyAdmin-engine
- add contribs to phpMyAdmin package

* Thu Sep 28 2006 Igor Zubkov <icesik@altlinux.ru> 2.9.1-alt1.rc1
- 2.9.0-beta1 -> 2.9.1-rc1

* Fri Sep 08 2006 Igor Zubkov <icesik@altlinux.ru> 2.9.0-alt1.beta1
- 2.8.2.4 -> 2.9.0-beta1

* Fri Sep 08 2006 Igor Zubkov <icesik@altlinux.ru> 2.8.2.4-alt3
- realy fix #9743

* Wed Aug 23 2006 Igor Zubkov <icesik@altlinux.ru> 2.8.2.4-alt2
- #9743

* Wed Aug 23 2006 Igor Zubkov <icesik@altlinux.ru> 2.8.2.4-alt1
- 2.8.2.3 -> 2.8.2.4

* Tue Aug 22 2006 Igor Zubkov <icesik@altlinux.ru> 2.8.2.3-alt1
- 2.8.2.2 -> 2.8.2.3

* Tue Aug 15 2006 Igor Zubkov <icesik@altlinux.ru> 2.8.2.2-alt1
- 2.8.2.1 -> 2.8.2.2

* Fri Aug 04 2006 Igor Zubkov <icesik@altlinux.ru> 2.8.2.1-alt1
- 2.8.2.1

* Fri Jun 30 2006 Igor Zubkov <icesik@altlinux.ru> 2.8.2-alt1
- 2.8.2 (security bug fix)
- http://www.phpmyadmin.net/home_page/security.php?issue=PMASA-2006-4

* Thu May 25 2006 Igor Zubkov <icesik@altlinux.ru> 2.8.1-alt1
- 2.8.1
- security bug fix

* Wed May 17 2006 Igor Zubkov <icesik@altlinux.ru> 2.8.0.4-alt1
- 2.8.0.4
- security bug fix

* Sat Apr 08 2006 Igor Zubkov <icesik@altlinux.ru> 2.8.0.3-alt1
- 2.8.0.3
- security bug fix

* Tue Aug 31 2004 Michael Shigorin <mike@altlinux.ru> 2.5.7-alt2pl1
- added Provides: phpmyadmin (#5100)

* Thu Jul 01 2004 Michael Shigorin <mike@altlinux.ru> 2.5.7-alt1pl1
- 2.5.7pl1 (major security fixes)

* Sat Jan 31 2004 Michael Shigorin <mike@altlinux.ru> 2.5.5-alt1pl1
- 2.5.5pl1
- removed unneeded mysql dependency

* Mon Oct 20 2003 Michael Shigorin <mike@altlinux.ru> 2.5.4-alt1
- 2.5.4 (minor bugfixes)

* Wed Sep 24 2003 Michael Shigorin <mike@altlinux.ru> 2.5.3-alt3
- #3031 fixed; thanks to Alex Murygin (murygin@)
  (hmm... should I "copy what's needed and remove what's not"
  to avoid such situations?)

* Tue Sep 23 2003 Michael Shigorin <mike@altlinux.ru> 2.5.3-alt2
- #3031 fixed; thanks to Dmitry Lebkov (dlebkov@)
- file layout somewhat straightened/updated
- perms updated (mostly -x)

* Mon Sep 08 2003 Michael Shigorin <mike@altlinux.ru> 2.5.3-alt1
- 2.5.3
- we've no "webmaster" user -- let it be root for now since rpm would
  get it that way anyways

* Thu Jul 31 2003 Michael Shigorin <mike@altlinux.ru> 2.5.2pl1-alt1
- 2.5.2-pl1 (security fixes)

* Mon May 26 2003 Michael Shigorin <mike@altlinux.ru> 2.3.3pl1-alt2
- killed phpinfo.php (crazy people!)

* Tue Feb 11 2003 Michael Shigorin <mike@altlinux.ru> 2.3.3pl1-alt1
- 2.3.3pl1
- default access control implemented (from TODO) -- don't use 2.3.1-alt1
- fixed config.inc.php owner (root->webmaster)

* Fri Oct 04 2002 Michael Shigorin <mike@altlinux.ru> 2.3.1-alt1
- built for ALT Linux
- spec adapted from PLD

* Tue Oct 01 2002 PLD Team <feedback@pld.org.pl> 2.3.1-1
All persons listed below can be reached at <cvs_login>@pld.org.pl
ppv, blues, kloczek, orzech, pioklo, qboosh, tiwek
