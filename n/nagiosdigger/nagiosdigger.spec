%define nagios_grp nagiosnew
%define plugins_cmddir   %_sysconfdir/nagios/commands
%define configdir   %_sysconfdir/nagios/%name
%define nagios_plugindir %_libexecdir/nagios/plugins

Name: nagiosdigger
Version: 0.9
Release: alt4

Url: https://www.vanheusden.com/nagiosdigger/
Packager: Paul Wolneykien <manowar@altlinux.org>

Source:%name-%version.tar

Patch0: %name-%version-mysqli.patch
Patch1: %name-%version-sql.patch
Patch2: %name-%version-css.patch
Patch3: %name-%version-config.patch
Patch4: %name-%version-alt.patch

BuildArch: noarch

Summary: A powerfull web frontend for the logging produced by Nagios
License: GPL-2.0
Group: Monitoring

Requires: nagios-www >= 3.0.6-alt12
Requires: apache2-base apache2-mod_php7
Requires: perl-DBI perl-DBD-mysql
Requires: php7-jpgraph php7-mysqli
Conflicts: nagios < 3.0.6-alt12

BuildRequires: perl-DBI perl-DBD-mysql perl-Config-INI

%description
Nagiosdigger is a powerfull web frontend for the logging produced by
Nagios. It enables you to dig trough all the data (problem events)
enabling you to quickly determine trends and/or systems with problems.
Searching, SLA calculations and problem predictions are some of the
features.

It requires a MySQL database as well as the JPGraph graph creating library.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%make_build

%install
%makeinstall_std sysconfdir=%_sysconfdir \
                 libexecdir=%_libexecdir \
                 sbindir=%_sbindir

%post
a2enextra httpd-addon.d
/sbin/service httpd2 condreload
[ ! -f %_initdir/nagios ] || /sbin/service nagios condreload

%files
%doc readme.txt upgrading.txt create_tables.sql
%dir %_var/www/webapps/%name
%_var/www/webapps/%name/*.php
%attr(0640,root,%nagios_grp) %_var/www/webapps/%name/config.inc.php
%_var/www/webapps/%name/*.css
%config(noreplace) %_sysconfdir/httpd2/conf/addon.d/A.%name.conf
%config(noreplace) %plugins_cmddir/50-nagiosdigger.cfg
%dir %configdir
%attr(0640,root,%nagios_grp) %config(noreplace) %configdir/config.ini
%_sbindir/%name-import
%nagios_plugindir/nagiosdigger_event_handler

%changelog
* Thu May 07 2020 Paul Wolneykien <manowar@altlinux.org> 0.9-alt4
- Fixed nagios dependency: require >= 3.0.6-alt12 (needed for
  "nagiosnew" group)
- Updated the readme.txt reflecting config.ini.
- Use a single INI configuration file for both PHP and Perl.

* Mon Apr 20 2020 Paul Wolneykien <manowar@altlinux.org> 0.9-alt3
- Switch to PHP7.

* Mon Apr 20 2020 Paul Wolneykien <manowar@altlinux.org> 0.9-alt2
- Fix: Make 50-nagiosdigger.cfg world-readable
- Reload nagios service after install.

* Fri Apr 17 2020 Paul Wolneykien <manowar@altlinux.org> 0.9-alt1
- Initial version for ALT.
