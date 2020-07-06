Name: installed-db-office-server
Version: 1.4.7
Release: alt1
Summary: Databases and config files for moodle, mediawiki and rujel (common)
License: GPL
Group: System/Configuration/Other
Source: %name.tar.gz
BuildArch: noarch

Requires: pwgen
Requires: MySQL-server-control

%description
Databases and config files for moodle, mediawiki and rujel (commom part)

%package mediawiki
Group: System/Configuration/Other
Requires: mediawiki mediawiki-apache2 mediawiki-ldap
Requires: %name = %version-%release
Summary: Databases and config files for mediawiki
Requires: mediawiki
Requires: mediawiki-mysql
Requires: mediawiki-ldap

%description mediawiki
Databases and config files for mediawiki

%package moodle
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: moodle-install-tools
Requires: moodle
Requires: moodle-apache2
Requires: moodle-base
Requires: moodle-local-mysql
Summary: Databases and config files for moodle

%description moodle
Databases and config files for moodle

%package nextcloud
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: nextcloud
Requires: nextcloud-apache2
Requires: php7-pcntl
Requires: php7-pdo_mysql
Provides: %name-owncloud = %EVR
Obsoletes: %name-owncloud < %EVR
Summary: Databases and config files for nextcloud

%description nextcloud
Databases and config files for nextcloud

%package rujel
Group: System/Configuration/Other
Requires: %name = %version-%release
Summary:  Databases and config files for rujel 
Requires: rujel

%description rujel
Databases and config files for rujel

%prep
%setup -q -c

%build

%install

mkdir -p %buildroot/usr/share/%name
install -Dp -m755 %name/80-office-server %buildroot%_sysconfdir/firsttime.d/80-office-server
#install -Dp -m755 %name/95-office-server-postinstall %buildroot/usr/share/install2/postinstall.d/95-office-server-postinstall
install -Dp -m755 %name/root.d %buildroot/usr/lib/alterator/hooks/root.d/installed-db
install -Dp -m755 %name/moodle %buildroot/etc/hooks/hostname.d/94-moodle-ldap
install -Dp -m755 %name/mediawiki %buildroot/etc/hooks/hostname.d/95-mediawiki-ldap
install -Dp -m755 %name/nextcloud %buildroot/etc/hooks/hostname.d/96-nextcloud-ldap
install -Dp -m755 %name/rujel %buildroot/etc/hooks/hostname.d/97-rujel-ldap

cp -r %name/data/* %buildroot/usr/share/%name/
install -Dp -m755 %name/apache-office-server %buildroot/usr/share/%name/
install -Dp -m755 %name/mysql-office-server %buildroot/usr/share/%name/
mkdir -p %buildroot/var/www/webapps/mediawiki
# ln -s /usr/share/doc/alt-docs/indexhtml/img/project-logo.png %buildroot/var/www/webapps/mediawiki/project-logo.png

%files
# /var/www/webapps/mediawiki/project-logo.png
/usr/share/%name
%_sysconfdir/firsttime.d/80-office-server
#/usr/share/install2/postinstall.d/*
/usr/lib/alterator/hooks/root.d/*

%files mediawiki
/etc/hooks/hostname.d/*-mediawiki-ldap

%files moodle
/etc/hooks/hostname.d/*-moodle-ldap

%files nextcloud
/etc/hooks/hostname.d/*-nextcloud-ldap

%files rujel
/etc/hooks/hostname.d/*-rujel-ldap


%changelog
* Thu Jul 02 2020 Andrey Cherepanov <cas@altlinux.org> 1.4.7-alt1
- Fix set admin password for nextcloud.

* Wed Oct 09 2019 Andrey Cherepanov <cas@altlinux.org> 1.4.6-alt1
- Remove 95-office-server-postinstall as sp package is unsupported.

* Mon Jul 15 2019 Andrey Cherepanov <cas@altlinux.org> 1.4.5-alt1
- Open pages after deploy to pass cache errors
- Fix write all output include stderr to log

* Fri Jul 05 2019 Andrey Cherepanov <cas@altlinux.org> 1.4.4-alt1
- Fix run chkconfig under systemd for httpd2 enable
- Fix arguments passed for nextcloud deploy
- Replace installed-db-office-server-owncloud for -nextcloud

* Mon Jun 24 2019 Andrey Cherepanov <cas@altlinux.org> 1.4.3-alt1
- Set shell for su in nextcloud deploy.
- Fix warning about memory_limit for nextcloud deploy.

* Tue Jun 18 2019 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt1
- Fix Moodle wwwroot.
- Fix admin password change.
- Add hostname to trusted domains for Nextcloud.

* Mon Jun 17 2019 Andrey Cherepanov <cas@altlinux.org> 1.4.1-alt1
- Requires all needed packages.
- Supports nextcloud and moodle 3.6.
- Move all deploy actions to firsttime.d.
- Log deploy to /root/.install-log/office-server-deploy.log.

* Mon Jul 25 2016 Andrey Cherepanov <cas@altlinux.org> 1.4-alt13
- Support moodle2.5 instead of moodle2.2
- Enable mod_filter

* Tue Apr 14 2015 Andrey Cherepanov <cas@altlinux.org> 1.4-alt12
- New hook in postinstall.d/95-office-server-postinstall
- Fix path to School Portal in DocumentRoot
- Update MediaWiki database
- Remove trusted domains and leave maintenance mode for Owncloud
- Update initial database settings for Owncloud 7.0.4

* Tue Dec 10 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt11
- owncloud with ldap integration fixed

* Thu Apr 25 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt10
- unconditional chkconfig httpd2 on

* Wed Mar 27 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt9
- owncloud with ldap integration fixed

* Tue Mar 26 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt6
- owncloud installation without wiki fixed

* Fri Mar 22 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt4
- premature exit fixed
- data files placement fixed

* Fri Mar 01 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt3
- lost script re-added into package

* Wed Feb 27 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt2
- interpackage requires added

* Wed Feb 27 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4-alt1
- split on mediawiki, moodle, owncloud and rujel packages

* Thu Aug 30 2012 Andrey Cherepanov <cas@altlinux.org> 1.3-alt10
- updated rujel user access privileges for MySQL (thanks Gennady Kushnir)

* Thu May 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt9
- moodle domain changing fixed

* Thu May 17 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt8
- passwords changing fixed
- moodle language setting fixed

* Wed May 16 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt7
- hardcoded russian language for moodle

* Mon May 14 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt6
- moodle siteurl fixed

* Thu May 10 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt5
- moodle-install-tools support

* Mon Apr 23 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt4
- fixed for owncloud 3.0.2

* Fri Apr 06 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt3
- owncloud ldap connection fixed

* Fri Apr 06 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt2
- owncloud setup fixed

* Fri Apr 06 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt1
- owncloud setup added

* Thu Apr 05 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2-alt1
- set root password for services

* Thu Dec 15 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1-alt3
- setup user-visible domain name on mediawiki config

* Wed Dec 14 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1-alt2
- mediawiki-ldap run priority fixed

* Tue Dec 13 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1-alt1
- dependences on mediawiki packages added
- new mediawiki database dump
- mediawiki config and config place fixed
- mediawiki script moved to hostname.d

* Thu Dec 23 2010 Andrey Cherepanov <cas@altlinux.org> 1.0-alt11
- fix RUJEL deployment script

* Tue Dec 14 2010 Andrey Cherepanov <cas@altlinux.org> 1.0-alt10
- don't create empty database 'rujel'

* Wed Dec 08 2010 Andrey Cherepanov <cas@altlinux.org> 1.0-alt9
- fix RUJEL grant statements
- enable gpm by default

* Tue Dec 07 2010 Andrey Cherepanov <cas@altlinux.org> 1.0-alt8
- fix RUJEL database creation
- add files for RUJEL LDAP authentication

* Wed Dec 01 2010 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt7
- Completely fixed access denided messages while mysqld configuration
- Added rujel database

* Mon Nov 29 2010 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt6
- Fixed access denided messages in mysqld configuration

* Thu Mar 04 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt5
- Enable mod_rewrite (ALT #23075)

* Wed Oct 14 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt4
- specify httpd2 runlevels

* Thu Aug 13 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt3
- Change first day of the week to monday in moodle

* Fri Jul 31 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2
- Update

* Thu Jul 30 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1
- Initial based on installed-db-school-server
