
Name: phpipam
Version: 1.40.000
Release: alt3
Summary: PHP-based virtual machine control tool
Group: Networking/WWW
License: GPLv3
Url: http://phpipam.net
Source: %name-%version.tar
Source21: captcha.tar
Source22: GoogleAuthenticator.tar
Source23: PHPMailer.tar
Source24: php-saml.tar
Source25: qrcodejs.tar
Source11: %name-apache.conf
# Patch: %name-%version-%release.patch

Provides: %name-php = %EVR
Provides: %name-php7 = %EVR
Obsoletes: %name-php7 < %EVR
Conflicts: %name-php5
BuildArch: noarch
Requires: webserver-common
Requires: php7-gmp php7-ldap php7-sockets php7-openssl php7-pdo php7-pdo_mysql php7-pcntl php7-mbstring php7-mcrypt php7-snmp php7-gd2 pear-core

BuildRequires(pre): rpm-macros-webserver-common rpm-macros-apache2


%description
phpipam is an open-source web IP address management application.
Its goal is to provide light and simple IP address management application.
It is ajax-based using jQuery libraries, it uses php scripts and javascript
and some HTML5/CSS3 features, so some modern browser is preferred
to be able to display javascript quickly and correctly.

Features and tools:
- Section / Subnet separation
- Subnet nesting
- IPv4/IPv6 support
- REST API
- Subnet ICMP/telnet scanning and automatic status updates
- Displays free range and number of clients
- Subnet statistics
- User management
- AD/LDAP/OpenLDAP/NetIQ/Radius authentication support (multiple servers)
- E-Mail notification with IP details
- Import IP addresses from XLS / CSV file
- Export IP database to XLS file
- IPv4/IPv6 calculator
- Search IP database
- IP request module
- Custom IP address fields
- and much more...
- PowerDNS integration (3.4+);

%package apache2
Group: Networking/WWW
BuildArch: noarch
Summary: apache2 configs for %name
Requires: %name = %version-%release
Requires: apache2-httpd-prefork-like php-engine

%description apache2
%summary

%prep
%setup
tar -xf %SOURCE21 -C app/login/captcha
tar -xf %SOURCE22 -C functions/GoogleAuthenticator
tar -xf %SOURCE23 -C functions/PHPMailer
tar -xf %SOURCE24 -C functions/php-saml
tar -xf %SOURCE24 -C functions/qrcodejs
#%patch -p1

%install
mkdir -p %buildroot%webserver_webappsdir
cp -r ../%name-%version %buildroot%webserver_webappsdir/%name
#cleaup
#rm -rf %buildroot%webserver_webappsdir/%name/misc
rm -f %buildroot%webserver_webappsdir/%name/{INSTALL.txt,README,UPDATE}
rm -f %buildroot%webserver_webappsdir/%name/.gitattributes
rm -f %buildroot%webserver_webappsdir/%name/.gitignore
rm -f %buildroot%webserver_webappsdir/%name/.gitmodules

install -pDm644 %SOURCE11 %buildroot%apache2_extra_available/%name.conf
%__subst 's|--dir--|%webserver_webappsdir/%name|g' %buildroot%apache2_extra_available/%name.conf

chmod 644 INSTALL.txt README.md UPDATE misc/CHANGELOG misc/Roadmap

# Cleanup
rm -f %buildroot%webserver_webappsdir/%name/functions/PHPMailer/.gitattributes
rm -f %buildroot%webserver_webappsdir/%name/functions/PHPMailer/.gitignore
rm -f %buildroot%webserver_webappsdir/%name/functions/PHPMailer/.scrutinizer.yml
rm -f %buildroot%webserver_webappsdir/%name/functions/PHPMailer/.travis.yml
rm -f %buildroot%webserver_webappsdir/%name/functions/PHPMailer/travis.phpunit.xml.dist
rm -rf %buildroot%webserver_webappsdir/%name/functions/PHPMailer/{.github,docs,examples,test}
rm -f %buildroot%webserver_webappsdir/%name/functions/php-saml/.gitattributes
rm -f %buildroot%webserver_webappsdir/%name/functions/php-saml/.gitignore
rm -f %buildroot%webserver_webappsdir/%name/functions/php-saml/.travis.yml
rm -rf %buildroot%webserver_webappsdir/%name/functions/php-saml/{demo-old,demo1,demo2,docs,tests}
rm -f %buildroot%webserver_webappsdir/%name/functions/qrcodejs/.gitignore
rm -f %buildroot%webserver_webappsdir/%name/app/login/captcha/.gitattributes
rm -rf %buildroot%webserver_webappsdir/%name/app/login/captcha/examples
rm -f %buildroot%webserver_webappsdir/%name/functions/GoogleAuthenticator/.gitignore
rm -f %buildroot%webserver_webappsdir/%name/functions/GoogleAuthenticator/.travis.yml
rm -rf %buildroot%webserver_webappsdir/%name/functions/GoogleAuthenticator/tests

%files
%doc INSTALL.txt README.md UPDATE misc/CHANGELOG misc/Roadmap
%dir %webserver_webappsdir/%name/
%webserver_webappsdir/%name/*
%webserver_webappsdir/%name/.htaccess
%dir %attr(0770, root, _webserver) %webserver_webappsdir/%name/app/admin/import-export/upload
%dir %attr(0770, root, _webserver) %webserver_webappsdir/%name/app/subnets/import-subnet/upload

%files apache2
%config(noreplace) %apache2_extra_available/%name.conf

%changelog
* Fri Jun 05 2020 Alexey Shabalin <shaba@altlinux.org> 1.40.000-alt3
- snapshot of 1.4 branch e4ae4ce1dae77125b7878b3cdc2f72f24f841ce8

* Thu Aug 15 2019 Alexey Shabalin <shaba@altlinux.org> 1.40.000-alt2
- snapshot of 1.4 branch fc4e92dc1025aa1eaa9fa2b73adbfd72a0b1eb54
- update PHPMailer submodule to v6.0.7
- backported MySQL 8.0 compatibility

* Thu Jul 11 2019 Alexey Shabalin <shaba@altlinux.org> 1.40.000-alt1
- 1.4

* Wed May 29 2019 Alexey Shabalin <shaba@altlinux.org> 1.32.004-alt1
- 1.32 rev004

* Tue Mar 05 2019 Alexey Shabalin <shaba@altlinux.org> 1.32.003-alt1
- 1.32 rev003
- drop php5 and php7 packages

* Fri Jul 06 2018 Alexey Shabalin <shaba@altlinux.ru> 1.32.000-alt1
- 1.3.2 release

* Fri Dec 22 2017 Alexey Shabalin <shaba@altlinux.ru> 1.31.000-alt1
- 1.3.1 release

* Thu Jun 15 2017 Alexey Shabalin <shaba@altlinux.ru> 1.30.000-alt1
- 1.3 release

* Wed May 10 2017 Alexey Shabalin <shaba@altlinux.ru> 1.30.000-alt0.6
- git snapshot of master branch  66d0e19ebea1fd6e670a75a5cfb9897f7010d6e6

* Wed Apr 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.30.000-alt0.5
- set permitions for upload dirs

* Tue Apr 25 2017 Alexey Shabalin <shaba@altlinux.ru> 1.30.000-alt0.4
- git snapshot of master branch 377139d7489376ac3622d936dbce16b1823358a1

* Thu Mar 16 2017 Alexey Shabalin <shaba@altlinux.ru> 1.30.000-alt0.3
- git snapshot of master branch 80c3f0614ed9d9d694592f7d0cb38e0b731892e7

* Mon Feb 27 2017 Alexey Shabalin <shaba@altlinux.ru> 1.30.000-alt0.2
- git snapshot of master branch cfda8c9b3a20ee60e693ae7cbcf87c61c109bbe9

* Wed Feb 22 2017 Alexey Shabalin <shaba@altlinux.ru> 1.30.000-alt0.1
- 1.3

* Mon Feb 13 2017 Alexey Shabalin <shaba@altlinux.ru> 1.29.011-alt2
- git snapshot of master branch 7edd5343ddd878de97eb41f3340fcce4fcd3a510
- add php5 and php7 subpackages

* Thu Jan 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.29.011-alt1
- git snapshot of master branch 84916b3c3add90b9cb1c39c9623cf04bb0f3bcd6

* Tue Jan 10 2017 Alexey Shabalin <shaba@altlinux.ru> 1.27.002-alt1
- git snapshot of master branch d55883ff28a3cf347f18e0cc717cf64b7556706a
- update PHPMailer to 5.2.22 (fixed CVE-2017-5223)

* Mon Dec 26 2016 Alexey Shabalin <shaba@altlinux.ru> 1.26.050-alt1
- git snapshot of master branch b99412648829471f3a336036f5cd138b8f131721
- install PHPMailer from upstream (fixed CVE-2015-8476,CVE-2016-10033,CVE-2016-10045)

* Wed Apr 20 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt2
- git snapshot of branch 1.2 - 7a5cb1a2ea065096d1d393ccc5b52a5bb7983c39

* Tue Feb 16 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus
