Name: amavisd-new
Version: 2.11.1
Release: alt2
Epoch: 1

Summary: A Mail Virus Scanner
License: BSD-2-Clause and GPL-2.0
Group: Networking/Mail
Url: http://www.ijs.si/software/amavisd/
Packager: Alexey Shabalin <shaba@altlinux.ru>

Source: %name-%version.tar.gz
Source1: amavisd.init
Source2: amavisd-new-notify.tar.gz
Source3: conf.d.tar.gz
Source6: amavisd-new-README.postfix.ALT.KOI8-R
Source7: amavisd-new-README.postfix.ALT.UTF8
Source8: %name.cron
Source10: amavisd-av-control
Source11: amavisd-spam-control
Source12: amavisd-new.tmpfiles.conf

Patch1: amavisd-skipsomedeps.patch

BuildArch: noarch
Provides: amavisd

Requires: file
Requires: perl-Archive-Zip >= 1.14
Requires: perl-BerkeleyDB 
Requires: perl-Convert-UUlib
Requires: perl-Convert-TNEF
Requires: perl-IO-stringy
Requires: perl-IO-Zlib
Requires: perl-MailTools
Requires: perl-Mail-DKIM >= 0.31
Requires: perl-IO-Socket-INET6

BuildRequires: perl-BerkeleyDB
BuildRequires: perl-IO-stringy
BuildRequires: perl-Unix-Syslog
BuildRequires: perl-Compress-Zlib
BuildRequires: perl-MIME-tools
BuildRequires: perl-Net-Server
BuildRequires: perl-Net-LibIDN
BuildRequires: perl-Digest-SHA

%description
Amavisd-new is a high-performance interface between mailer (MTA) and content
checkers: virus scanners, and/or SpamAssassin. It is written in Perl for
maintainability, without paying a significant price for speed.  It talks to MTA
via (E)SMTP or LMTP, or by using helper programs.  Best with Postfix, fine with
dual-sendmail setup and Exim v4, works with sendmail/milter, or with any MTA as
a SMTP relay. For Courier and qmail MTA there is a patch in the distributed
package.

%package utils
Summary: Utils package for amavisd-new.
Group: Networking/Mail
Requires: %name

%description utils
This package contains amavisd-new utils: snmp-agent, nanny, release.

%package smtpd
Summary: Virtual package for amavisd-new with MTA.
Group: Networking/Mail
Requires: %name
Requires: smtpdaemon

%description smtpd
This package contains require MTA daemon. If you use postfix, sendmail or exim
you will need to install %name-smtpd.

%package cron
Summary: Cron package for clean quarantine.
Group: Networking/Mail
Requires: %name
Requires: stmpclean
Requires: crontabs

%description cron
This package contains cron script for clean quarantine.

%package spamassassin
Summary: Virtual package for amavisd-new with SpamAssassin.
Group: Networking/Mail
Requires: %name
Requires: perl-Mail-SpamAssassin
Requires: spamassassin >= 2.60

%description spamassassin
This package contains require SpamAssassin perl module.
If you use SpamAssassin, you will need to install %name-spamassassin.

%package razor
Summary: Virtual package for amavisd-new with razor.
Group: Networking/Mail
Requires: %name
Requires: perl-Razor

%description razor
This package contains require razor. If you use razor,
you will need to install %name-razor.

%package clamav
Summary: Virtual package for amavisd-new with clamav antivirus.
Group: Networking/Mail
Requires: %name
Requires: clamav

%description clamav
This package contains require razor. If you use razor,
you will need to install %name-clamav.

%package ext-archives
Summary: Virtual package for amavisd-new with external archives.
Group: Networking/Mail
Requires: %name
Requires: bzip2
Requires: lha
Requires: lzop
Requires: ncompress
#Requires:	nomarch
#Requires:	arc
Requires: unace
Requires: unarj
Requires: unrar
#Requires:	zoo

%description ext-archives
This package contains require external archives.

%package mysql
Summary: Virtual package is supported lookups in mysql.
Group: Networking/Mail
Requires: %name
Requires: perl-DBD-mysql

%description mysql
Amavisd-new is supported for storing information
about processed mail (logging/reporting) and optionally for quarantining
to a SQL database.

%package postgresql
Summary: Virtual package SQL is supported lookups in PostgreSQL.
Group: Networking/Mail
Requires: %name
Requires: perl-DBD-Pg

%description postgresql
Amavisd-new is supported for storing information
about processed mail (logging/reporting) and optionally for quarantining
to a SQL database.

%package ldap-client
Summary: Virtual package is supported lookups in LDAP.
Group: Networking/Mail
Requires: %name
Requires: perl-ldap >= 0.32

%description ldap-client
Amavisd-new is supported lookups multiple search attributes
in LDAP.

%package ldap-server
Summary: Package is supported lookups in LDAP.
Group: Networking/Mail
Requires: openldap-servers

%description ldap-server
Amavisd-new is supported lookups multiple search attributes
in LDAP.


%package p0f
Summary: Virtual package for amavisd-new with p0f.
Group: Networking/Mail
Requires: %name
Requires: p0f

%description p0f
This package contains require p0f and perl script p0f-analyzer.pl. If you use
p0f, you will need to install %name-p0f.

%package complete
Summary: Package contein all subpackages amavisd-new.
Group: Networking/Mail
Requires: %name
Requires: %name-utils
Requires: %name-cron
Requires: %name-spamassassin
Requires: %name-razor
Requires: %name-clamav
Requires: %name-ext-archives
Requires: %name-mysql
Requires: %name-postgresql
Requires: %name-ldap-client
Requires: %name-smtpd
Requires: %name-ldap-server
Requires: %name-p0f

%description complete
All subpackages Amavisd-new.

%prep
%setup -q
%patch1 -p2

%install
mkdir -p \
	%buildroot%_initdir \
	%buildroot%_sysconfdir/amavis \
	%buildroot%_tmpfilesdir \
	%buildroot%_sbindir \
	%buildroot%_bindir \
	%buildroot%_spooldir/amavis \
	%buildroot%_spooldir/amavis/db \
	%buildroot%_spooldir/amavis/quarantine \
	%buildroot%_spooldir/amavis/tmp \
	%buildroot%_var/run/amavis \
        %buildroot%_sysconfdir/cron.daily \
        %buildroot%_sysconfdir/openldap/schema \
        %buildroot%_controldir

install -m 755 %SOURCE1 %buildroot%_initdir/amavisd
install -m 640 amavisd.conf %buildroot%_sysconfdir/amavis/amavisd.conf-old
install -m 640 amavisd.conf-default %buildroot%_sysconfdir/amavis/amavisd.conf-default
install -m 700 %SOURCE8 %buildroot%_sysconfdir/cron.daily/%name
install -m 755 amavisd %buildroot%_sbindir/amavisd
install -m 755 amavisd-agent %buildroot%_bindir/amavisd-agent
install -m 755 amavisd-nanny %buildroot%_bindir/amavisd-nanny
install -m 755 amavisd-release %buildroot%_bindir/amavisd-release
install -m 755 p0f-analyzer.pl %buildroot%_bindir/p0f-analyzer.pl

install -m444 LDAP.schema %buildroot%_sysconfdir/openldap/schema/amavisd-new.schema

tar -xzf %SOURCE2 -C %buildroot%_sysconfdir/amavis/
tar -xzf %SOURCE3 -C %buildroot%_sysconfdir/amavis/

###
## Install Attention README
###
install -m 0644 %SOURCE6 README.ALT.KOI8-R
install -m 0644 %SOURCE7 README.ALT.UTF

install -m 755 %SOURCE10 %buildroot%_controldir/amavisd-av
install -m 755 %SOURCE11 %buildroot%_controldir/amavisd-spam

install -m 644 %SOURCE12 %buildroot%_tmpfilesdir/amavisd.conf

%post
%post_service amavisd

%preun
%preun_service amavisd

%files
%doc AAAREADME.first INSTALL LICENSE README_FILES RELEASE_NOTES test-messages
%doc LDAP.schema TODO
%doc README.ALT.UTF README.ALT.KOI8-R
%config %_initdir/amavisd
%config %_tmpfilesdir/amavisd.conf
# %attr(640,root,mail) %config(noreplace) %_sysconfdir/amavis/amavisd.conf
%_controldir/amavisd-*
%attr(750,root,mail) %dir %_sysconfdir/amavis/conf.d
%attr(640,root,mail) %config(noreplace) %_sysconfdir/amavis/conf.d/*
%attr(640,root,mail) %_sysconfdir/amavis/amavisd.conf-*
%attr(640,root,mail) %_sysconfdir/amavis/notify_*
%_sbindir/amavisd
%attr(775,mail,mail) %dir %_spooldir/amavis
%attr(770,mail,mail) %dir %_spooldir/amavis/db
%attr(750,mail,mail) %dir %_spooldir/amavis/quarantine
%attr(750,mail,mail) %dir %_spooldir/amavis/tmp
%attr(775,root,mail) %dir %_var/run/amavis

%files utils
%_bindir/amavisd-agent 
%_bindir/amavisd-nanny
%_bindir/amavisd-release

%files cron
%_sysconfdir/cron.daily/%name

%files spamassassin
%files razor
%files clamav
%files ext-archives
%files mysql
%files postgresql
%files ldap-client
%files smtpd
%files ldap-server
%attr(644,root,ldap) %_sysconfdir/openldap/schema/amavisd-new.schema
%files p0f
%_bindir/p0f-analyzer.pl

%files complete

%changelog
* Wed Sep 02 2020 Andrey Cherepanov <cas@altlinux.org> 1:2.11.1-alt2
- Requires perl-IO-Socket-INET6 (ALT #38859).

* Tue Aug 25 2020 Andrey Cherepanov <cas@altlinux.org> 1:2.11.1-alt1
- New version (ALT #27110).
- Fix /var/run/amavis permissions (ALT #37488).
- Fix License tag according to SPDX.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:2.6.6-alt3.qa1
- NMU: applied repocop patch

* Sun Sep 22 2013 Vladimir Lettiev <crux@altlinux.ru> 1:2.6.6-alt3
- fixed amavisd-new with Perl 5.18
- enable auto requires

* Wed Oct 05 2011 Alexey Shabalin <shaba@altlinux.ru> 1:2.6.6-alt2
- fix perm for config dir

* Thu Jun 09 2011 Alexey Shabalin <shaba@altlinux.ru> 1:2.6.6-alt1
- 2.6.6
- cleanup spec
- add LSB header to init script
- add tmpfiles config for systemd

* Mon Sep 07 2009 Alexey Shabalin <shaba@altlinux.ru> 1:2.6.4-alt1
- 2.6.4
- update altlinux mailing list emails in 35-ruleslisting.conf

* Fri Mar 27 2009 Alexey Borovskoy <alb@altlinux.ru> 1:2.6.2-alt0.M40.1
- 2.6.2.
- DKIM disabled in config file.
- Disable third-party AV's in config. Enable it manually if needed.
- Small spec cleanup. Replace patches with git branches.

* Thu Dec 13 2007 Alexey Shabalin <shaba@altlinux.ru> 1:2.5.3-alt1
- 2.5.3

* Thu Nov 08 2007 Alexey Shabalin <shaba@altlinux.ru> 1:2.5.2-alt1
- 2.5.2
- update russian template notify_sender.txt

* Sat Jun 02 2007 Alexey Shabalin <shaba@altlinux.ru> 1:2.5.1-alt1
- 2.5.1
- revised config files
- Warning! Add suffix "conf" for config files in /etc/amavis/conf.d (bugs read *.rpmsave,*.rpmnew)
- Remove Requires: amavisd-new-ldap-client in amavisd-new-ldap-server (#11783)

* Mon Apr 30 2007 Alexey Shabalin <shaba@altlinux.ru> 1:2.5.0-alt1
- 2.5.0
- drop support for Archive::Tar
- drop the use of libnet (modules Net::SMTP and Net::Cmd)

* Tue Apr 03 2007 Alexey Shabalin <shaba@altlinux.ru> 1:2.4.5-alt2
- add Requires: perl-MIME-tools >= 1:5.417 (#11104)

* Thu Feb 01 2007 Alexey Shabalin <shaba@altlinux.ru> 1:2.4.5-alt1
- 2.4.5

* Wed Dec 06 2006 Alexey Shabalin <shaba@altlinux.ru> 1:2.4.4-alt2
- bugfix - no remove old conf.d/*
- fix config patch in amavisd daemon (patch3)
- fix $sockname in amavisd-release
- fix $unix_socketname in conf.d/15-mta

* Fri Nov 24 2006 Alexey Shabalin <shaba@altlinux.ru> 1:2.4.4-alt1
- 2.4.4
- add control facility for enabled/disabled anti-virus and anti-spam check
- update README.ALT
- rename amavisd-new-README.postfix.ALT to README.ALT.KOI8-R and README.ALT.UTF
- starting amavisd before postfix (#10241)

* Thu Nov 02 2006 Alexey Shabalin <shaba@altlinux.ru> 1:2.4.3-alt1
- 2.4.3
- WARNING! New scheme configs
- default disabled anti-spam and anti-virus check, to enabled edit /etc/amavis/conf.d/01-disable

* Mon Jul 31 2006 Alexey Shabalin <shaba@altlinux.ru> 1:2.4.2-alt2
- AutoReq: noperl, no requires perl/SAVI

* Fri Jul 14 2006 Alexey Shabalin <shaba@altlinux.ru> 1:2.4.2-alt1
- 2.4.1
- add  package p0f
- update patch

* Wed May 17 2006 Alexey Shabalin <shaba@altlinux.ru> 1:2.4.1-alt1
- 2.4.1

* Mon Apr 17 2006 Alexey Shabalin <shaba@altlinux.ru> 1:2.4.0-alt1
- new version (2.4.0)
- require minimal versions of module Net::Server 0.91

* Mon Nov 28 2005 Alexey Shabalin <shaba@altlinux.ru> 1:2.3.3-alt2
- fix summary
- add packages amavisd-new-{utils,ldap-server,cron}
- add virtual packages amavisd-new-{spamassassin,razor,clamav,mysql,postgresql,ldap-client,smtpd}
- package ldap-server require perl-ldap >= 0.32 (#8552)
- package utils contain amavisd-release utility (#8550)

* Wed Sep 14 2005 Alexey Shabalin <shaba@altlinux.ru> 1:2.3.3-alt1
- update 2.3.3
- require minimal versions of module Compress::Zlib 1.35

* Tue Jul 19 2005 Alexey Shabalin <shaba@altlinux.ru> 1:2.3.2-alt2
- Remove Requires: clamav (#4683) 

* Wed Jun 29 2005 Alexey Shabalin <shaba@altlinux.ru> 1:2.3.2-alt1
- update 2.3.2
- require minimal versions of module Archive::Zip 1.14 

* Tue May 24 2005 Alexey Shabalin <shaba@altlinux.ru> 1:2.3.1-alt1
- update 2.3.1
- add depend perl-IO-Zlib
- add cron.daily script for clean quarantine

* Thu Apr 28 2005 Alexey Shabalin <shaba@altlinux.ru> 1:2.3.0-alt1
- update to relise 2.3.0

* Wed Oct 20 2004 Alexey Shabalin <shaba@altlinux.ru> 1:2.1.2-alt1.1
- fix init script - amavisd status (bug #5361)

* Thu Oct 07 2004 Alexey Shabalin <shaba@altlinux.ru> 1:2.1.2-alt1
- update to relise 2.1.2

* Thu Jun 24 2004 Alexey Shabalin <shaba@altlinux.ru> 20030616-alt9.2
- remove script create alias virusalert (#4135)
- Change default email in virus_admin from virusalert to postmaster (#4135)

* Sun May 09 2004 Alexey Shabalin <shaba@altlinux.ru> 20030616-alt9.1
- Update amavisd-new-20030616-p9
- Remove Requires:postfix

* Fri Mar 12 2004 Alexey Shabalin <shaba@altlinux.ru> 20030616-alt8.1
- Update amavisd-new-20030616-p8
- Disable Russian notify by default (for enable edit amavisd.conf)
- Remove amavisd-checkcfg, amavisd-mboxlearnham, amavisd-mboxlearnspam
- Add  amavisd-new-README.postfix.ALT
- Initial build for Sisyphus.

* Thu Dec 11 2003 Alexey Shabalin <shaba@altlinux.ru> 20030616-alt0.1
- First relise for Daedalus
