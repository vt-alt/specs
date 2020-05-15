%define installdir %webserver_webappsdir/%name

Name: glpi
Version: 9.4.5
Release: alt1

Summary: IT and asset management software
License: GPLv2
Group: Networking/Other

URL: http://www.glpi-project.org
Packager: Pavel Zilke <zidex at altlinux dot org>
BuildArch: noarch

Source0: http://www.glpi-project.org/IMG/gz/%name-%version.tar.gz
Source1: apache2.conf
Source2: README.ALT
Patch: patch0.patch

Requires: webserver-common php-engine curl lynx
BuildRequires(pre): rpm-macros-webserver-common

%description
GLPI is the Information Resource-Manager with an additional Administration-
Interface.
You can use it to build up a database with an inventory for your company
(computer, software, printers...).
It has enhanced functions to make the daily life for the administrators easier,
like a job-tracking-system with mail-notification and methods to build a
database with basic information about your network-topology.

%package apache2
Summary: Apache 2.x web-server configuration for %name
Group: Networking/Other
Requires: %name = %version-%release, apache2
%description apache2
Apache 2.x web-server configuration for %name

%package php7
Summary: PHP7 dependencies for %name
Group: Networking/Other
Requires: %name = %version-%release, php7-mysqli, php7-ldap, php7-imap, php7-curl, php7-gd2, php7-fileinfo, php7-mbstring, php7-apcu, php7-opcache, php7-xmlrpc, php7-exif
%description php7
PHP7 dependencies for %name

%prep
%setup
%patch -p0

%build

%install
# install apache config
install -pD -m0644 %_sourcedir/apache2.conf %buildroot%_sysconfdir/httpd2/conf/sites-available/%name.conf

# install glpi
mkdir -p %buildroot%installdir
cp -rp * %buildroot%installdir/

#install README.ALT
install -pD -m0644 %_sourcedir/README.ALT README.ALT

# remove .htaccess files - we're use apache config instead
find %buildroot%installdir -name .htaccess -delete

# remove files
find %buildroot%installdir -name remove.txt -delete
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

%post

%post apache2
if [ "$1" = "1" ]; then
  a2ensite %name
  %_initdir/httpd2 condreload
fi

%preun apache2
if [ "$1" = "0" ]; then
  a2dissite %name
fi

%postun apache2
if [ "$1" = "0" ]; then
  %_initdir/httpd2 condreload
fi

%files
%dir %installdir
%dir %attr(2770,root,%webserver_group) %installdir/config
#%config %attr(0664,root,%webserver_group) %installdir/config/based_config.php
#%config %attr(0664,root,%webserver_group) %installdir/config/config.php
#%config %attr(0664,root,%webserver_group) %installdir/config/define.php
%dir %attr(2770,root,%webserver_group) %installdir/files
%attr(2770,root,%webserver_group) %installdir/files/*
%installdir/ajax
%installdir/bin
%installdir/config
%installdir/css
%installdir/files
%installdir/front
%installdir/inc
%installdir/install
%installdir/js
%installdir/lib
%installdir/locales
%installdir/pics
%installdir/plugins
%installdir/scripts
%installdir/sound
%installdir/vendor
%installdir/*.php
#%installdir/*.js
#%installdir/*.json
%installdir/COPYING.txt
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc README.md
%doc SUPPORT.md
%doc apirest.md
%doc README.ALT

%files apache2
%config(noreplace) %attr(0644,root,root) %_sysconfdir/httpd2/conf/sites-available/%name.conf

%files php7

%changelog
* Sun Dec 29 2019 Pavel Zilke <zidex at altlinux dot org> 9.4.5-alt1
- New version 9.4.5

* Sun Dec 29 2019 Pavel Zilke <zidex at altlinux dot org> 9.4.4-alt1
- New version 9.4.4
- This is a security release, upgrading is highly recommended

* Tue Jun 25 2019 Pavel Zilke <zidex at altlinux dot org> 9.4.3-alt1
- New version 9.4.3
- This is a security release, upgrading is highly recommended

* Wed Apr 17 2019 Pavel Zilke <zidex at altlinux dot org> 9.4.2-alt1
- New version 9.4.2
- This is a security release, upgrading is highly recommended

* Tue Apr 09 2019 Pavel Zilke <zidex at altlinux dot org> 9.4.1-alt1
- New version 9.4.1

* Tue Mar 05 2019 Pavel Zilke <zidex at altlinux dot org> 9.4.0-alt2
- Deleted glpi-php5

* Thu Feb 28 2019 Pavel Zilke <zidex at altlinux dot org> 9.4.0-alt1
- New version 9.4.0

* Wed Feb 06 2019 Pavel Zilke <zidex at altlinux dot org> 9.3.3-alt2
- Fixed glpi-apache2 postun

* Sun Dec 30 2018 Pavel Zilke <zidex at altlinux dot org> 9.3.3-alt1
- New verion 9.3.3
- PHP7 support

* Thu Sep 21 2017 Pavel Zilke <zidex at altlinux dot org> 9.1.6-alt2
- Delete glpi-apache

* Thu Sep 21 2017 Pavel Zilke <zidex at altlinux dot org> 9.1.6-alt1
- New version 9.1.6

* Fri Apr 28 2017 Pavel Zilke <zidex at altlinux dot org> 9.1.3-alt1
- New version 9.1.3

* Fri Apr 14 2017 Pavel Zilke <zidex at altlinux dot org> 9.1.2-alt1
- New version 9.1.2

* Wed Sep 28 2016 Pavel Zilke <zidex at altlinux dot org> 9.1-alt1
- New version 9.1

* Thu Aug 25 2016 Pavel Zilke <zidex at altlinux dot org> 0.90.5-alt2
- Conf for Apache2 moved to sites-available

* Thu Aug 25 2016 Pavel Zilke <zidex at altlinux dot org> 0.90.5-alt1
- New version 0.90.5

* Fri Dec 25 2015 Pavel Zilke <zidex at altlinux dot org> 0.90.1-alt1
- Include bugfixes and some minor features

* Fri Dec 25 2015 Pavel Zilke <zidex at altlinux dot org> 0.90-alt1
- New version 0.90

* Sun Oct 11 2015 Pavel Zilke <zidex at altlinux dot org> 0.85.5-alt1
- This is maintenance release to fix several minor bugs.

* Sat Jun 20 2015 Pavel Zilke <zidex at altlinux dot org> 0.85.4-alt1
- This version correct several minor bugs.

* Sat Jun 20 2015 Pavel Zilke <zidex at altlinux dot org> 0.85.3-alt1
- This version fix several minor bugs and a security bug

* Thu Jan 22 2015 Pavel Zilke <zidex at altlinux dot org> 0.85.2-alt1
- This version correct several minor bugs.

* Wed Jan 07 2015 Pavel Zilke <zidex at altlinux dot org> 0.85.1-alt1
- This version fix several minor bugs and a security bug

* Wed Jan 07 2015 Pavel Zilke <zidex at altlinux dot org> 0.85-alt1
- New version 0.85

* Mon Oct 20 2014 Pavel Zilke <zidex at altlinux dot org> 0.84.8-alt1
- This version fix several minor bugs and a security bug.

* Sat Aug 09 2014 Pavel Zilke <zidex at altlinux dot org> 0.84.7-alt1
- New version 0.84.5 This version correct several minor bugs.

* Thu Mar 13 2014 Pavel Zilke <zidex at altlinux dot org> 0.84.5-alt1
- New version 0.84.5 This version correct several minor bugs.

* Fri Feb 07 2014 Pavel Zilke <zidex at altlinux dot org> 0.84.4-alt1
- New version 0.84.4 This version correct several minor bugs.

* Fri Nov 15 2013 Pavel Zilke <zidex at altlinux dot org> 0.84.3-alt1
- New version 0.84.3

* Fri Sep 20 2013 Pavel Zilke <zidex at altlinux dot org> 0.84.2-alt1
- Security fixes:
 + CVE-2013-5696 : SQL Injection, PHP Code Execution, CSRF 

* Tue Sep 10 2013 Pavel Zilke <zidex at altlinux dot org> 0.84.1-alt1
- New version 0.84.1

* Sat Aug 17 2013 Pavel Zilke <zidex at altlinux dot org> 0.84-alt1
- New version 0.84

* Sun Jul 21 2013 Pavel Zilke <zidex at altlinux dot org> 0.83.9.1-alt1
- Security fixes:
 + CVE-2013-2225 + CVE-2013-2227 : Security fix ( serialize + filter classname for autoload) (ALT #29189)

* Tue Apr 16 2013 Pavel Zilke <zidex at altlinux dot org> 0.83.8-alt1
- New version 0.83.8

* Sun Dec 16 2012 Pavel Zilke <zidex at altlinux dot org> 0.83.7-alt1
- New version 0.83.7

* Wed Oct 17 2012 Pavel Zilke <zidex at altlinux dot org> 0.83.6-alt1
- New version 0.83.6

* Thu Aug 16 2012 Pavel Zilke <zidex at altlinux dot org> 0.83.4-alt1
- New version 0.83.4 

* Sat Jun 09 2012 Pavel Zilke <zidex at altlinux dot org> 0.83.2-alt1
- New version 0.83.2

* Thu Apr 19 2012 Pavel Zilke <zidex at altlinux dot org> 0.83.1-alt1
- New version 0.83.1

* Fri Apr 06 2012 Pavel Zilke <zidex at altlinux dot org> 0.83-alt1
- New version 0.83

* Mon Feb 13 2012 Pavel Zilke <zidex at altlinux dot org> 0.80.7-alt1
- New version 0.80.7

* Wed Jan 11 2012 Pavel Zilke <zidex at altlinux dot org> 0.80.61-alt1
- New version 0.80.61

* Tue Oct 25 2011 Pavel Zilke <zidex at altlinux dot org> 0.80.5-alt1
- New version 0.80.5

* Wed Sep 28 2011 Pavel Zilke <zidex at altlinux dot org> 0.80.4-alt1
- New version 0.80.4

* Thu Jul 07 2011 Pavel Zilke <zidex at altlinux dot org> 0.80.1-alt1
- New version 0.80.1 This version correct several bugs.

* Thu Jun 02 2011 Pavel Zilke <zidex at altlinux dot org> 0.80-alt1
- New version 0.80

* Sun Mar 13 2011 Pavel Zilke <zidex at altlinux dot org> 0.78.3-alt1
- New version 0.78.3

* Tue Jan 18 2011 Pavel Zilke <zidex at altlinux dot org> 0.78.2-alt1
- New version 0.78.2

* Tue Nov 23 2010 Pavel Zilke <zidex at altlinux dot org> 0.78.1-alt1
- New version 0.78.1

* Wed Oct 13 2010 Pavel Zilke <zidex at altlinux dot org> 0.78-alt1
- New version 0.78

* Fri Apr 02 2010 Pavel Zilke <zidex at altlinux dot org> 0.72.4-alt1
- New version 0.72.4

* Tue Nov 10 2009 Pavel Zilke <zidex at altlinux dot org> 0.72.3-alt2
- remove Thumbs.db files

* Tue Nov 03 2009 Pavel Zilke <zidex at altlinux dot org> 0.72.3-alt1
- New version 0.72.3

* Wed Oct 07 2009 Pavel Zilke <zidex at altlinux dot org> 0.72.2-alt2
- spec bugfix

* Thu Sep 17 2009 Pavel Zilke <zidex at altlinux dot org> 0.72.2-alt1
- New version 0.72.21
- fixed export to pdf
- fixed import from OCS Inventory NG

* Wed Aug 12 2009 Pavel Zilke <zidex at altlinux dot org> 0.72.1-alt1
- New version 0.72.1-alt1

* Thu Jun 04 2009 Pavel Zilke <zidex at altlinux dot org> 0.71.6-alt2
- Fixed README.ALT location

* Tue Jun 02 2009 Pavel Zilke <zidex at altlinux dot org> 0.71.6-alt1
- New version 0.71.6-alt1

* Mon Feb 02 2009 Pavel Zilke <zidex at altlinux dot org> 0.71.5-alt1
- First build for ALT Linux

