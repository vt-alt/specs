
Name: cacti
Version: 1.2.15
Release: alt3

%define cactidir %_datadir/%name
%define cacticonfdir %_sysconfdir/%name
%define username cacti

Summary: The complete RRDTool-based graphing solution.
Summary(ru_RU.UTF8): Полнофункциональная оболочка для RRDTool.

License: GPL
Group: Monitoring

URL: http://www.cacti.net/
Source: %name-%version.tar
Source2: %name-readme.alt
Source3: %name.logrotate
Source5: %name-rrdpath.sql
Source7: %name-apache.conf
Source8: %name-lighttpd.conf

Patch: %name-%version-%release.patch

#The following plugins have been merged into the core Cacti
Provides: cacti-plugin-aggregate = %version-%release
Conflicts: cacti-plugin-aggregate < %version-%release
Provides: cacti-plugin-discovery = %version-%release
Conflicts: cacti-plugin-discovery < %version-%release
Provides: cacti-plugin-settings = %version-%release
Conflicts: cacti-plugin-settings < %version-%release
Provides: cacti-plugin-ssl = %version-%release
Conflicts: cacti-plugin-ssl < %version-%release


Requires: webserver webserver-common rrd-utils net-snmp net-snmp-utils
Requires: php7-snmp php7-sockets php7-pdo php7-pdo_mysql php7-mbstring php7-openssl php7-gd2 php7-gmp

BuildRequires(pre): rpm-macros-webserver-common
BuildArch: noarch
# build docs
BuildRequires: lynx docbook-utils


%description
Cacti is a complete frontend to RRDTool. It stores all of the necessary 
information to create graphs and populate them with data in a MySQL database. 
The frontend is completely PHP driven. Along with being able to maintain graphs, 
data sources, and round robin archives in a database, Cacti also handles the data 
gathering. There is SNMP support for those used to creating traffic graphs with 
MRTG.

%description -l ru_RU.UTF8
Cacti - это полнофункциональная оболочка для RRDTool. Программа хранит всю
необходимую информацию для создания и наполнения графиков в базе MySQL.
Программа полностью написана на PHP. Вместе с возможностью управления
графиками, источниками данных и архивами round robin Cacti также занимается
сбором данных.

%package setup
Summary: Cacti setup package
Group: Monitoring
BuildArch: noarch
Requires: %name = %version-%release

%description setup
Install this package to configure initial Cacti installation. You
should uninstall this package when you're done, as it considered
insecure to keep the setup files in place.

%description -l ru_RU.UTF8 setup
Установите этот пакет для первоначальной инициализации Cacti.
После завершения настройки Cacti Вы должны удалить этот пакет, что бы обеспечить
безопасную работу приложения.

%prep
%setup -q
%patch -p1


%build
chmod a+rx scripts/*
chmod a+rx cli/*

%install -n %name-%version
mkdir -p %buildroot{%_sbindir,%_sysconfdir/cron.d,%cacticonfdir,%cactidir/plugins,%_localstatedir/%name/rra,%_logdir/%name}

cp -a *.php README.md LICENSE %buildroot%cactidir
cp -ar cli formats images include install lib locales mibs plugins resource scripts %buildroot%cactidir
mv -f %buildroot{%cactidir/poller.php,%_sbindir/cacti-poller}
chmod 755 %buildroot%_sbindir/cacti-poller
install -m 0640 include/config.php.dist %buildroot%cacticonfdir/config.php
touch %buildroot%_logdir/%name/%name.log

# you should run this sql if your database contains path to %{_datadir}...
cp %SOURCE5 docs/
cp %SOURCE2 docs/README_ALT.txt
cp %SOURCE7 docs/
cp %SOURCE8 docs/
ln -sf %_docdir/%name-doc-%version %buildroot%cactidir/docs


# install cron
cat << EOF > %buildroot%_sysconfdir/cron.d/cacti
MAILTO=root

*/5 * * * * cacti umask 022; exec /usr/sbin/cacti-poller > /dev/null
EOF

# logrotate
install -D -m 0644 %SOURCE3 %buildroot%_sysconfdir/logrotate.d/cacti

%pre
%_sbindir/useradd -M -d %cactidir -r %username -G %webserver_group > /dev/null 2>&1 ||:
if LANG=C %_bindir/id %username 2>/dev/null | \
grep -qv "groups=[^[:space:]]*(%webserver_group)"; then
echo 'Warning: User %username was not included in the group %webserver_group!'
%_bindir/gpasswd -a %username %webserver_group 
echo '     Added user %username to group %webserver_group.'
fi

%post
%post_service crond

%triggerpostun -- %name < 0.8.7e-alt1
# Migration from previous version
if [ $2 -gt 0 ]; then
echo "Fixing permissions and location rrd,log files after previous package:"
mv -f %_var/www/html/%name/log/* %_logdir/%name/
mv -f %_var/www/html/%name/rra/* %_localstatedir/%name/rra/
chown -v root:%webserver_group  %_logdir/%name/* %_localstatedir/%name/*
chmod -v 660 %_logdir/%name/* %_localstatedir/%name/*
fi

%files
%doc docs/README_ALT.txt docs/%name-rrdpath.sql CHANGELOG LICENSE README.md cacti.sql
%config(noreplace) %_sysconfdir/cron.d/cacti
%_sbindir/cacti-poller
%dir %attr(750,root,%webserver_group) %cacticonfdir
%attr(640,root,%webserver_group) %config(noreplace) %cacticonfdir/config.php
%config(noreplace) %_sysconfdir/logrotate.d/%name
%dir %cactidir
%cactidir/*.php
%cactidir/cli
%cactidir/formats
%cactidir/images
%cactidir/include
%cactidir/lib
%cactidir/locales
%cactidir/mibs
%cactidir/plugins
%cactidir/resource
%dir %cactidir/scripts
%attr(755,root,root) %cactidir/scripts/*

%attr(755,root,%webserver_group) %dir %_localstatedir/%name
%attr(2775,root,%webserver_group) %dir %_localstatedir/%name/rra
%attr(730,root,%webserver_group) %dir %_logdir/%name
%attr(660,root,%webserver_group) %ghost %_logdir/%name/cacti.log

%files setup
%cactidir/install

%changelog
* Fri Nov 27 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.15-alt3
- Fixed merge issue in lib/clog_webapi.php found by Alexander Makeenkov.

* Wed Nov 25 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.15-alt2
- Fixed issues in 1.2.15 release.

* Mon Nov 23 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.15-alt1
- Updated to upstream version 1.2.15 (Fixes: CVE-2020-13230, CVE-2020-13231).

* Thu Mar 19 2020 Alexey Shabalin <shaba@altlinux.org> 1.2.10-alt3
- fix syntax error in include/global.php (thx to vercha@)

* Wed Mar 18 2020 Alexey Shabalin <shaba@altlinux.org> 1.2.10-alt2
- package cacti.sql to doc dir

* Sun Mar 15 2020 Alexey Shabalin <shaba@altlinux.org> 1.2.10-alt1
- 1.2.10
- Fixes:
  + CVE-2019-17357 When viewing graphs, some input variables are not properly checked (SQL injection possible)
  + CVE-2019-17358 When deserializating data, ensure basic sanitization has been performed
  + CVE-2019-16723 Security issue allows to view all graphs
  + CVE-2020-7106 Lack of escaping on some pages can lead to XSS exposure
  + CVE-2020-7237 Remote Code Execution due to input validation failure in Performance Boost Debug Log
  + CVE-2020-8813 When guest users have access to realtime graphs, remote code could be executed

* Fri Apr 05 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.3-alt1
- 1.2.3

* Tue Mar 05 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.2-alt1
- 1.2.2
- drop php5 package, php7 package merge with main

* Fri Jan 04 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.0-alt1
- 1.2.0

* Thu Feb 16 2017 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- 1.0.3
- add php7 subpackage

* Tue May 10 2016 Alexey Shabalin <shaba@altlinux.ru> 0.8.8h-alt1
- 0.8.8h
- fixed CVE-2014-2326,CVE-2014-2327,CVE-2014-2328,CVE-2014-5025,
        CVE-2014-5026,CVE-2014-4002,CVE-2013-5588,CVE-2013-5589,
        CVE-2015-4342,CVE-2015-4634,CVE-2015-8377,CVE-2015-8604,
        CVE-2016-3659

* Tue May 06 2014 Alexey Shabalin <shaba@altlinux.ru> 0.8.8b-alt2
- fixed:
 + CVE-2014-2326 Unspecified HTML Injection Vulnerability
 + CVE-2014-2328 Unspecified Remote Command Execution Vulnerability
 + CVE-2014-2709 shell escaping issues in lib/rrd.php
 + CVE-2014-2708 SQL injection issues in graph_xport.php

* Wed Aug 14 2013 Alexey Shabalin <shaba@altlinux.ru> 0.8.8b-alt1
- 0.8.8b

* Wed May 02 2012 Alexey Shabalin <shaba@altlinux.ru> 0.8.8a-alt1
- 0.8.8a

* Fri Apr 06 2012 Alexey Shabalin <shaba@altlinux.ru> 0.8.8-alt1
- 0.8.8

* Tue Jan 10 2012 Alexey Shabalin <shaba@altlinux.ru> 0.8.7i-alt2
- add official patch settings_checkbox.patch

* Wed Dec 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.7i-alt1
- 0.8.7i

* Wed Oct 05 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.7h-alt1
- 0.8.7h

* Mon Sep 27 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7g-alt3
- add official patches:
  + Fix issue with multi selection data source deactivation
  + Graph List View Searching
  + Repair various interface display issues
  + Fix LDAP authenication with group restrictions enabled
  + Update script server to properly process command line arguments that are quoted
  + Fixes issue with Cacti ping library
  + Fixes issue with 1 minute polling with 1 minute rra

* Tue Jul 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7g-alt2
- fix url_path in config.php

* Mon Jul 12 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7g-alt1
- 0.8.7g

* Tue Jun 01 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7f-alt1
- 0.8.7f:
  + SQL injection and shell escaping issues reported by Bonsai Information Security
  + Cross-site scripting issues reported by VUPEN Security
  + MOPS-2010-023: Cacti Graph Viewer SQL Injection Vulnerability
  + Fixed various issues with exporting and importing templates that contain special characters
  + Fixed condition that could cause RRDtool to segfault
  + Many fixes to html generation and presentation

* Tue May 11 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7e-alt4
- Adding official patch to fix sql vulnerability

* Mon Apr 05 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7e-alt3
- fix permition /var/lib/cacti

* Tue Mar 30 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7e-alt2
- add cacti/plugins/index.php

* Wed Mar 24 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7e-alt1
- 0.8.7e
- poller:
 + in sbin
 + no hide of errors in cron
 + use exec to avoid /bin/sh in process table
- cacti in /usr/share
- log in /var/log/cacti
- triggerpostun for migration
- add cacti user to _webserver group

* Wed Dec 10 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.7b-alt4
- Fix simlink /var/www/html/cacti/docs -> /usr/share/doc/cacti-doc-0.8.7b (Thanks at@)
- Remove package cacti-config-php

* Sat Nov 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.7b-alt3
- Add new subpackage %name-doc
- Convert spec to UTF8
- Add official patche reset_each_patch

* Thu Mar 13 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.7b-alt2
- Add official patches
- Fix url_path in include/global.php
- Join sql scripts to one
- Add link to docs
- Add README_ALT.txt
- Add version-release to Requires: cacti-config
- Add Conflicts: cacti-config-php to cacti-config-php5
- Add Conflicts: cacti-config-php5 to cacti-config-php

* Tue Feb 19 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.7b-alt1
- New version
- Update cacti-plugin-arch

* Fri Nov 30 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.7a-alt1
- New version
- Remove all patches (in upstream)

* Fri Apr 13 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.6j-alt1
- Add official patches:
  + %name-%version-thumbnail_graphs_not_working.patch
  + %name-%version-graph_debug_lockup_fix.patch
- Add net-snmp-utils in Requires

* Mon Jan 29 2007 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.8.6j-alt0
- New version
- Add official patches:
  + %name-%version-ping_php_version4_snmpgetnext.patch
  + %name-%version-tree_console_missing_hosts.patch
- Add cacti-plugin-arch
- Separate cactid in own package
- Add BuildArch: noarch (#10675)
- Add %_sysconfdir/cron.d/cacti
- Add virtual packages for different depends

* Sat Jan 13 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6i-alt2
- Security fixes (CVE-2006-6799)

* Mon Dec 04 2006 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6i-alt1
- New version
- Spec cleanups 
- config.php was marked as config with noreplace

* Fri Apr 14 2006 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6h-alt2
- Fixed BuildRequires

* Wed Apr 05 2006 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6h-alt1
- New version
- Spec cleanups

* Sun Jul 10 2005 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6f-alt1
- Many critical security bugfixes in upstream
- Spec fixes (now daemon and main module may have different versions)

* Fri Oct 22 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6b-alt1
- New version

* Sun Sep 19 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6-alt4
- Removed BuildArch tag because our rpm doesn't support multiple buildarch's
  in one spec ;-( Now php stuff has i586 arch ;-)

* Fri Sep 17 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6-alt3
- Spec fixups (correct %%setup macroses)

* Thu Sep 16 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6-alt2
- Spec update (information for upgrade)

* Thu Sep 16 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6-alt1
- New upstream version (has many new features)
- Russian translation for spec
- cactid now in separated package
- spec cleanups (permissions, path)

* Mon Aug 09 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.5a-alt6
- Added missing buildrequires (libssl and other)

* Fri Aug 06 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.5a-alt5
- New version

* Fri Jul 09 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.5-alt4
- New build

* Fri Mar 12 2004 Andrew Kornilov <andy@eva.dp.ua> 0.8.5-alt3
- Removed redundant docs from /var/www/html/cacti

* Fri Mar 12 2004 Andrew Kornilov <andy@eva.dp.ua> 0.8.5-alt2
- Added -M to useradd to skip homedir skeleton 

* Tue Mar 09 2004 Andrew Kornilov <andy@eva.dp.ua> 0.8.5-alt1
- First alpha build for Sisyphus. All works, but...;-)
