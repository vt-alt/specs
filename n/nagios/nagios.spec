%define nagios_usr nagios
%define nagios_grp nagiosnew
%define plugins_cmddir   %_sysconfdir/nagios/commands
%define templates_cfgdir %_sysconfdir/nagios/templates
%define time_cfgdir      %_sysconfdir/nagios/timeperiods
%define contacts_cfgdir  %_sysconfdir/nagios/contacts
%define objects_cfgdir   %_sysconfdir/nagios/objects
%define extinfo_cfgdir   %_sysconfdir/nagios/extinfo

%define webconfigdir  %_sysconfdir/nagios/webserver
%define nagios_moddir %_libexecdir/nagios/modules
%define nagios_evhdir %_libexecdir/nagios/eventhandlers

Name: nagios
Version: 3.0.6
Release: alt13

Summary: Services and network monitoring system
License: GPL
Group: Monitoring
URL: http://www.nagios.org

Packager: Dmitry Lebkov <dlebkov@altlinux.ru>

Source0: %name-%version.tar.gz
Source1: %name-init

# default user/password file for Nagios(R)
# contains defaults: user=nagios, password=nagios
Source2: %name.web-users

# Apache config for Nagios(R)
Source10: %name-apache.conf

# Apache config for Nagios(R)
Source11: 100-%name.mods.conf
Source15: 100-%name.extra.conf
Source12: %name-apache2.conf

# Lighttpd config for Nagios(R)
Source13: %name-lighttpd.conf

# tmpfiles template
Source14: nagios-tmpfiles.conf

# fix some default paths
Patch0: nagios-3.0.2-alt-makefile.patch
Patch1: nagios-3.0.2-alt-eperlfix.patch
Patch2: nagios-3.0-alt-paths.patch
Patch3: nagios-3.0.6-alt-scripts.patch
Patch4: nagios-3.0.6-alt-config.patch
Patch10: nagios-3.0.2-nagiosdevlist-disable-contactgroup-svc-notifications.patch
Patch11: nagios-3.0.6-alt-warnings.patch
Patch12: nagios-3.0.6-alt-ignore-empty-hostgroups.patch
Patch13: nagios-3.0.6-alt-format-comments.patch

###########################################
# Provide the abstract service names (which are virtual pkg names),
# specify their origin (our pkg name as the epoch + version-release):
Provides: nagios-daemon = %name:%version-%release

# Conflict with all other real pkgs which provide the same services
# (they should specify the origin the same way, so the epoch-version-release
# of the virtual pkgs NRPE will always differ from that of ours if
# they are provided by a different real pkg):
Conflicts: nagios-daemon < %name:%version-%release
Conflicts: nagios-daemon > %name:%version-%release
#
########################################
PreReq: %name-common = %version-%release
Requires: nagios-plugins

# Automatically added by buildreq on Mon Oct 17 2011
BuildRequires: glib2-devel libgd2-devel libjpeg-devel libltdl7-devel libpng-devel perl-devel traceroute

%description
Nagios(R) is a host and service monitor designed to inform you of network
problems before your clients, end-users or managers do. It has been
designed to run under the Linux operating system, but works fine under
most *NIX variants as well. The monitoring daemon runs intermittent
checks on hosts and services you specify using external "plugins" which
return status information to Nagios(R). When problems are encountered, the
daemon can send notifications out to administrative contacts in a variety
of different ways (email, instant message, SMS, etc.). Current status
information, historical logs, and reports can all be accessed via a web
browser.

%package common
Summary: Services and network monitor, common files
Group: Monitoring

%description common
Nagios(R) is a host and service monitor designed to inform you of network
problems before your clients, end-users or managers do. It has been
designed to run under the Linux operating system, but works fine under
most *NIX variants as well. The monitoring daemon runs intermittent
checks on hosts and services you specify using external "plugins" which
return status information to Nagios(R). When problems are encountered, the
daemon can send notifications out to administrative contacts in a variety
of different ways (email, instant message, SMS, etc.). Current status
information, historical logs, and reports can all be accessed via a web
browser.

%package www
Summary: Nagios(R) web-interface
Group: Monitoring
#reReq: %name-common = %version-%release webserver
PreReq: %name-common = %version-%release
Obsoletes: nagios-default-www nagios-mysql-www nagios-pgsql-www

%description www
Nagios(R) is a host and service monitor designed to inform you of network
problems before your clients, end-users or managers do. It has been
designed to run under the Linux operating system, but works fine under
most *NIX variants as well. The monitoring daemon runs intermittent
checks on hosts and services you specify using external "plugins" which
return status information to Nagios(R). When problems are encountered, the
daemon can send notifications out to administrative contacts in a variety
of different ways (email, instant message, SMS, etc.). Current status
information, historical logs, and reports can all be accessed via a web
browser.


%package www-apache2
Summary: Apache 2.x web-server configuration for Nagios(R) web-interface
Group: Monitoring
PreReq: %name-www = %version-%release apache2

%description www-apache2
Web-server settings and environment tuning for run Nagios(R) web-interface
with Apache 2.x.

%package www-lighttpd
Summary: Lighttpd web-server configuration for Nagios(R) web-interface
Group: Monitoring
PreReq: %name-www = %version-%release lighttpd

%description www-lighttpd
Web-server settings and environment tuning for run Nagios(R) web-interface
with Lighttpd.

%package doc
Summary: Services and network monitor, HTML-documentation
Group: Monitoring
BuildArch: noarch

%description doc
HTML-documentation for Nagios(R) monitoring system.

%package full
Summary: Services and network monitor. Virtual package for complete install
Group: Monitoring
PreReq: nagios-common
PreReq: nagios
PreReq: nagios-www
Requires: nagios-plugins
Requires: nagios-plugins-local
Requires: nagios-plugins-network
Requires: nagios-plugins-perl

%description full
Virtual package for complete install of Nagios(R) monitoring system.

%prep
%setup -q
%patch0 -p1 -b .p0
%patch1 -p1 -b .p1
%patch2 -p1 -b .p2
%patch3 -p1 -b .p3
%patch4 -p1 -b .p4
%patch10 -p1 -b .p10
%patch11 -p1 -b .p11
%patch12 -p2 -b .p12
%patch13 -p2 -b .p13

%build
PATH=$PATH:/usr/sbin
%configure \
	--enable-nanosleep \
	--enable-event-broker \
	--enable-embedded-perl \
	--with-nagios-user=%nagios_usr \
	--with-nagios-group=%nagios_grp \
	--with-command-user=%nagios_usr \
	--with-command-group=%nagios_grp \
	--with-cgiurl=/%name/cgi-bin \
	--with-htmurl=/%name \
	--with-init-dir=%_initdir \
	--localstatedir=%_var \
	--with-lockfile=/var/run/%name/%name.pid \
	--with-mail=/bin/mail \
	--with-perlcache \
	--with-httpd-conf=%webconfigdir \
	--with-checkresult-dir=%_spooldir/%name

%make_build all
cd contrib
%make_build all
cd ..

%install
make DESTDIR=%buildroot install
make DESTDIR=%buildroot install-commandmode
make DESTDIR=%buildroot install-config
make DESTDIR=%buildroot install-contrib

# install init-script
mkdir -p %buildroot/%_initrddir
install -m 0755 %SOURCE1 %buildroot/%_initrddir/%name

# install modules and eventhandlers
mkdir -p %buildroot/%nagios_moddir
mkdir -p -m 0755 %buildroot/%nagios_evhdir
pushd contrib/eventhandlers
 for file in `/bin/find ./ -type f -print` ; do
  install -m 0755 $file %buildroot/%nagios_evhdir
 done
popd

# misc dirs and files
mkdir -p %buildroot/%extinfo_cfgdir
mkdir -p %buildroot/%_localstatedir/%name/tmp
mkdir -p %buildroot/%_spooldir/%name
mkdir -p %buildroot/var/run/%name
/bin/touch %buildroot/var/run/%name/%name.pid

#instal docs
mkdir -p -m 0755 %buildroot/%_docdir/%name-%version/html
cp -r html/docs/* %buildroot/%_docdir/%name-%version/html
install -m 0644 Changelog %buildroot/%_docdir/%name-%version/
install -m 0644 INSTALLING %buildroot/%_docdir/%name-%version/
install -m 0644 LEGAL %buildroot/%_docdir/%name-%version/
install -m 0644 README %buildroot/%_docdir/%name-%version/
install -m 0644 THANKS %buildroot/%_docdir/%name-%version/
install -m 0644 UPGRADING %buildroot/%_docdir/%name-%version/
install -m 0644 OutputTrap.pm %buildroot/%_docdir/%name-%version/

# install Nagios(R) .htusers default file
install -m 0640 %SOURCE2 %buildroot/%_sysconfdir/%name/


# apache2 configs
install -pDm0644 %SOURCE11 %buildroot/%_sysconfdir/httpd2/conf/mods-start.d/100-nagios.conf
install -pDm0644 %SOURCE15 %buildroot/%_sysconfdir/httpd2/conf/extra-start.d/100-nagios.conf
install -pDm0644 %SOURCE12 %buildroot/%_sysconfdir/httpd2/conf/addon.d/A.nagios.conf

# lighttpd configs
install -pDm0644 %SOURCE13 %buildroot/%_sysconfdir/lighttpd/nagios.conf

# tmpfiles creation
install -pDm0644 %SOURCE14 %buildroot/%_sysconfdir/tmpfiles.d/nagios.conf

%pre common
%_sbindir/groupadd -r -f %nagios_grp &>/dev/null
%_sbindir/useradd -r -n -g %nagios_grp -d %_localstatedir/%name \
    -s /bin/false -c 'Nagios(R) account' %nagios_usr &>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%post www
echo
echo "By default this package contains only CGI binary and HTML pages."
echo "Web-server specific settings for Nagios(R) web-interface exists"
echo "in the follow packages:"
echo "  nagios-www-apache2  -- Apache 1.x configs"
echo "  nagios-www-lighttpd -- Lighttpd configs"
echo


%post www-apache2
gpasswd -a apache2 %nagios_grp
a2chkconfig
%_initdir/httpd2 condrestart
%postun www-apache2
[ "$1" = "1" ] || gpasswd -d apache2 %nagios_grp
[ "$1" = "1" ] || a2chkconfig
[ "$1" = "1" ] || %_initdir/httpd2 condrestart

%post www-lighttpd
gpasswd -a lighttpd %nagios_grp
echo '# Nagios(R) web-interface settings' >> /etc/lighttpd/lighttpd.conf
echo 'include "nagios.conf"' >> /etc/lighttpd/lighttpd.conf
%_initdir/lighttpd condrestart

%postun www-lighttpd
gpasswd -d lighttpd %nagios_grp
subst 's|include "nagios.conf"||' /etc/lighttpd/lighttpd.conf
subst 's|# Nagios(R) web-interface settings||' /etc/lighttpd/lighttpd.conf
%_initdir/lighttpd condrestart

%files
%attr(0640,root,%nagios_grp) %config(noreplace) %_sysconfdir/%name/nagios.cfg
%attr(0640,root,%nagios_grp) %config(noreplace) %_sysconfdir/%name/resource.cfg
%dir %plugins_cmddir
%config(noreplace) %plugins_cmddir/00-commands.cfg
%dir %contacts_cfgdir
%config(noreplace) %contacts_cfgdir/00-contacts.cfg
%dir %templates_cfgdir
%config(noreplace) %templates_cfgdir/00-templates.cfg
%dir %time_cfgdir
%config(noreplace) %time_cfgdir/00-timeperiods.cfg
%dir %objects_cfgdir
%config(noreplace) %_sysconfdir/%name/objects/localhost.cfg
%dir %extinfo_cfgdir

%_initrddir/%name
%_sbindir/nagios
%_sbindir/nagiostats

%dir %_libexecdir/%name
%dir %nagios_moddir
%dir %nagios_evhdir
%nagios_evhdir/disable_active_service_checks
%nagios_evhdir/disable_notifications
%nagios_evhdir/enable_active_service_checks
%nagios_evhdir/enable_notifications
%nagios_evhdir/handle-master-host-event
%nagios_evhdir/handle-master-proc-event
%nagios_evhdir/obsessive_svc_handler
%nagios_evhdir/submit_check_result
%nagios_evhdir/submit_check_result_via_nsca
%_libexecdir/%name/p1.pl
%dir %_libexecdir/%name/contrib
%_libexecdir/%name/contrib/*

%dir %_datadir/%name

%attr(2751,%nagios_usr,%nagios_grp) %dir %_localstatedir/%name
%attr(2771,root,%nagios_grp) %dir /var/run/nagios
%attr(0644,%nagios_usr,%nagios_grp) /var/run/nagios/%name.pid
%attr(2751,%nagios_usr,%nagios_grp) %dir %_localstatedir/%name/rw
%attr(0700,%nagios_usr,%nagios_grp) %dir %_localstatedir/%name/tmp
%attr(2751,%nagios_usr,%nagios_grp) %dir %_spooldir/%name
%attr(0751,%nagios_usr,%nagios_grp) %dir %_logdir/%name
%attr(0751,%nagios_usr,%nagios_grp) %dir %_logdir/%name/archives

%dir %_sysconfdir/%name/examples
%_sysconfdir/%name/examples/*
%dir %_docdir/%name-%version
%_docdir/%name-%version/*
%exclude %_docdir/%name-%version/html

%files common
%dir %_sysconfdir/%name
%_sysconfdir/tmpfiles.d/nagios.conf

%dir %plugins_cmddir

%files www
%config(noreplace) %_sysconfdir/%name/cgi.cfg
%attr(0640,root,%nagios_grp) %config(noreplace) %_sysconfdir/%name/%name.web-users
%dir %_datadir/%name/html
%_datadir/%name/html/*
%dir %_libexecdir/%name
%dir %_libexecdir/%name/cgi
%_libexecdir/%name/cgi/avail.cgi
%_libexecdir/%name/cgi/cmd.cgi
%_libexecdir/%name/cgi/config.cgi
%_libexecdir/%name/cgi/extinfo.cgi
%_libexecdir/%name/cgi/histogram.cgi
%_libexecdir/%name/cgi/history.cgi
%_libexecdir/%name/cgi/notifications.cgi
%_libexecdir/%name/cgi/outages.cgi
%_libexecdir/%name/cgi/showlog.cgi
%_libexecdir/%name/cgi/status.cgi
%_libexecdir/%name/cgi/statusmap.cgi
%_libexecdir/%name/cgi/statuswml.cgi
%_libexecdir/%name/cgi/statuswrl.cgi
%_libexecdir/%name/cgi/summary.cgi
%_libexecdir/%name/cgi/tac.cgi
%_libexecdir/%name/cgi/trends.cgi


%files www-apache2
%config(noreplace) %_sysconfdir/httpd2/conf/mods-start.d/100-nagios.conf
%config(noreplace) %_sysconfdir/httpd2/conf/extra-start.d/100-nagios.conf
%config(noreplace) %_sysconfdir/httpd2/conf/addon.d/A.nagios.conf

%files www-lighttpd
%config(noreplace) %_sysconfdir/lighttpd/nagios.conf

%files doc
%dir %_docdir/%name-%version/html
%_docdir/%name-%version/html/*

%files full

%changelog
* Wed May 13 2020 Paul Wolneykien <manowar@altlinux.org> 3.0.6-alt13
- Fix: Require "authn_core" module in 100-nagios.mods.conf.

* Wed Apr 15 2020 Paul Wolneykien <manowar@altlinux.org> 3.0.6-alt12
- Fixed www-apache2 upgrade: enable httpd-addon.d with
  extra-start.d/100-nagios.conf.

* Wed Apr 15 2020 Paul Wolneykien <manowar@altlinux.org> 3.0.6-alt11
- Fixed "www-apache2" package upgrade: keep "apache2" user in the
  "%nagios_grp" group.

* Mon Mar 02 2020 Paul Wolneykien <manowar@altlinux.org> 3.0.6-alt10
- Pretty-print the comments (patch).

* Wed Feb 26 2020 Paul Wolneykien <manowar@altlinux.org> 3.0.6-alt9
- Silently ignore empty hostgroups (patch).

* Wed Jan 22 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 3.0.6-alt8
- merge sisyphus and c8.1

* Fri Feb 15 2019 Denis Medvedev <nbr@altlinux.org> 3.0.6-alt7
- added tmpfiles declaration for lockfile

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.6-alt6.1
- rebuild with new perl 5.28.1

* Thu Jan 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.6-alt6
- Fixed localstatedir location.

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.6-alt5.1
- rebuild with new perl 5.26.1

* Thu Sep 28 2017 Denis Medvedev <nbr@altlinux.org> 3.0.6-alt5
- (Fixes: CVE-2009-2288, CVE-2011-1523, CVE-2012-6096, CVE-2013-2214,
 CVE-2013-7108, CVE-2013-7205)

* Tue Jun 27 2017 Denis Medvedev <nbr@altlinux.org> 3.0.6-alt4
- removed apache1 as unsupported

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.6-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 3.0.6-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.6-alt3.1
- rebuild with new perl 5.20.1

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 3.0.6-alt3
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 3.0.6-alt2
- rebuilt for perl-5.16

* Mon Oct 17 2011 Alexey Tourbin <at@altlinux.ru> 3.0.6-alt1.2
- rebuilt for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 3.0.6-alt1.1
- rebuilt with perl 5.12

* Mon Jan 12 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 3.0.6-alt1
- 3.0.6

* Tue Aug 12 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 3.0.3-alt1
- 3.0.3
- add /etc/nagios/extinfo directory for hosts and services extended info
- set SERVICEPERFDATA output to 4096 chars (original is 256) for ePN

* Thu May 01 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 3.0.1-alt1
- 3.0.1
- prepare to packages reordering
- add follow directories to default config
  + /etc/nagios/commands    - default place for addons command definitions
  + /etc/nagios/contacts    - default place for contacts
  + /etc/nagios/templates   - default place for templates
  + /etc/nagios/timeperiods - default place for timeperiods
  + /etc/nagios/objects     - default place for monitored objects
  + set prefix '00-' for commands.cfg, contacts.cfg, templates.cfg
    and timeperiods.cfg files. Move that files to appropriate directories.
- add /var/run/nagios directory (UID:GID root:nagios, 2771) for Nagios
  and related daemons PID-files
- add patch from nagios-devel list for config host dependency parsing
- web-related configs now in their own packages:
  + nagios-www-apache   - for Apache 1.x
  + nagios-www-apache2  - for Apache 2.x
  + nagios-www-lighttpd - for Lighttpd

* Thu Mar 13 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.11-alt1
- 2.11

* Sun May 06 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.9-alt1
- 2.9

* Sat Jan 27 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.7-alt1
- 2.7

* Thu Nov 30 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.6-alt1
- 2.6

* Mon Jul 03 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.4-alt2
- spec-file fixes for x86_64 build

* Sat Jul 01 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.4-alt1
- 2.4
- add virtual package nagios-full with Requires:
   + nagios nagios-www
   + nagios-plugins
   + nagios-plugins-local
   + nagios-plugins-network
   + nagios-plugins-perl
- add package nagios-doc with HTML-documentation from web-interface
- nagios-www:
   + add webserver into 'Requires' list 
   + config file for Apache moved to /etc/httpd/conf/addon-modules.d/

* Sun Feb 12 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0-alt1
- 2.0 release

* Sat Dec 24 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0-alt0.b6
- 2.0b6
- nagios-www:
   + config file for Apache moved to /etc/httpd/conf/addon-modules/

* Sun Nov 06 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0-alt0.b4.2
- 2.0b4

* Tue May 24 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0-alt0.b3.1
- 2.0b3
- #6817 fixed

* Sun Feb 13 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0-alt0.b2.1
- 2.0b2

* Fri Jan 07 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0-alt0.b1.1
- new beta
- support for MySQL and PgSQL dropped in upstream
- sub-packages redesign

* Sun Apr 18 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 1.2-alt1
- v1.2 -- bugfix release

* Wed Dec 17 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.1-alt2
- spec-file fixes

* Thu Jul 03 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.1-alt1
- v1.1
- fix bugs #2605 and #2672
- init-script changed according to new requirements

* Wed Jun 18 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt2.1
- move to new alternatives scheme

* Wed Apr 02 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.0-alt2
- nagios-default-www:
  + change 'Requires:' from  nagios-mysql to nagios-default.

* Sun Mar 30 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.0-alt1
- fix 'Provides' and 'Requires' for nagios-daemon virtual package

* Wed Feb 26 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.0-alt0.2
- binary RPM-packages redesign
- template-based configuration support for the '-mysql' and '-pgsql' packages
- SQL-scripts for create MySQL- and PgSQL-tables placed into the %_docdir
- spec-file:
  + wrong home-dir for user nagios fixed
  + fix files/dir permissions, so CGI-scripts now can read Nagios(R) logs
    and write into the nagios.cmd file
  + add 'Provides: nagios-daemon' and 'Requires: nagios-plugins' into
    '-default', '-mysql' and '-pgsql' packages
  + cosmetic fixes

* Wed Dec 04 2002 Dmitry Lebkov <dlebkov@altlinux.ru> 1.0-alt0.1
- initial build for ALT Linux
