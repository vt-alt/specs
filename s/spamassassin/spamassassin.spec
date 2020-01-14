%define pname Mail-SpamAssassin

# build spamc with SSL support enabled?
%def_enable ssl

Name: spamassassin
Version: 3.4.3
Release: alt1

Summary: Spam filter for email written in perl
License: Apache-2.0
Group: Networking/Mail

URL: http://www.spamassassin.org/
Source0: http://www.cpan.org/authors/id/K/KM/KMCGRAIL/SpamAssassin/Mail-SpamAssassin-%{version}.tar.bz2
Source1: spamd.init
Source2: spamassassin_local.cf
Source3: spamd.sysconfig

# from Debian:
Patch10: spamassassin-deb-10_change_config_paths.patch
Patch11: spamassassin-deb-20_edit_spamc_pod.patch
Patch12: spamassassin-deb-55_disable_nagios_epm.patch
Patch13: spamassassin-deb-90_pod_cleanup.patch

%def_without test
# normal method nukes on errors :(
%define _perl_req_method relaxed

%{?_enable_ssl:BuildRequires: LibreSSL-devel}

# Automatically added by buildreq on Thu Jul 21 2011
# optimized out: libcom_err-devel libkrb5-devel perl-Compress-Raw-Bzip2 perl-Compress-Raw-Zlib perl-Digest-SHA perl-Digest-SHA1 perl-Encode perl-Error perl-HTML-Parser perl-HTTP-Date perl-HTTP-Message perl-IO-Compress perl-IO-Socket-INET6 perl-IO-String perl-IO-Zlib perl-Net-DNS perl-Net-SSLeay perl-NetAddr-IP perl-Package-Constants perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-Socket6 perl-URI perl-libnet perl-podlators
BuildRequires: perl-Archive-Tar perl-DBI perl-DBM perl-Encode-Detect perl-IO-Socket-SSL perl-IP-Country perl-Mail-DKIM perl-Mail-SPF perl-Razor perl-devel perl-libwww zlib-devel perl(Pod/Man.pm)

# Was needed by sa-stats from tools/ (currently not shipped in tarball so)
BuildRequires: perl-Parse-Syslog

# Optimized out, but let them be on list (to reassure they will not drop out in future)
BuildRequires: perl-Net-DNS
BuildRequires: perl-HTML-Parser

BuildRequires: perl-BSD-Resource perl-TermReadKey

Requires: perl-%pname = %version-%release

# Versioned requires for sa-update (see INSTALL in sources for required versions):
Requires: perl-IO-Zlib >= 1.04
Requires: perl-Archive-Tar >= 1.23

# I doubt this is sensible, Ident protocol is pointless, potentially dangerous
# and ineffective for spamassassin:
# BuildRequires: perl-Net-Ident

%description
SpamAssassin provides you with a way to reduce if not completely eliminate
Unsolicited Commercial Email (SPAM) from your incoming email. It can be
invoked by a MTA such as exim or postfix, or can be called from a procmail
script, .forward file, etc. It uses a genetic-algorithm evolved scoring
system to identify messages which look spammy, then adds headers to the
message so they can be filtered by the user's mail reading software.

%package spamd
Summary: spamd - daemonized version of spamassassin
Group: Networking/Mail
BuildArch: noarch

Requires: perl-%pname = %version-%release

# To synchronize spamd and spamc version if they installed both:
Requires: %name-version = %version-%release

# Not autodetected by rpm, needed for spamc/spamd SSL communication:
Requires: perl-IO-Socket-SSL

# Use of Storable module removed in 3.1.0!
# Requires: perl-Storable

Requires(pre): shadow-utils
Requires(post): %post_service
Requires(preun): %preun_service

%description spamd
The purpose of this program is to provide a daemonized version of the
spamassassin executable. The goal is improving throughput performance
for automated mail checking.

This is intended to be used alongside "spamc", a fast, low-overhead C
client program.

%package spamc
Summary: spamc - client for spamd
Group: Networking/Mail
Requires(post): shadow-utils

# To synchronize spamd and spamc version if they installed both:
Requires: %name-version = %version-%release

%description spamc
Spamc is the client half of the spamc/spamd pair. It should be used in place
of "spamassassin" in scripts to process mail. It will read the mail from
STDIN, and spool it to its connection to spamd, then read the result back and
print it to STDOUT. Spamc has extremely low overhead in loading, so it should
be much faster to load than the whole spamassassin program.

%package -n perl-%pname
Summary: Mail::SpamAssassin - SpamAssassin e-mail filter libraries
Group: Development/Perl
BuildArch: noarch

# Non-autodetectable (usually due to eval'ed using) deps listed below:
Requires: perl-Net-DNS
# Needed by SPF plugin
Requires: perl-Mail-SPF
# Needed by RelayCountry plugin
Requires: perl-IP-Country
# Needed by DKIM plugin
Requires: perl-Mail-DKIM

# Since 3.3.0 upstream ships spamassassin rules separately
Requires: spamassassin-rules = %version

# Versioned requires:
Requires: perl-HTML-Parser >= 3.46

%description -n perl-%pname
Mail::SpamAssassin is a Mail::Audit plugin to identify spam using text
analysis and several internet-based realtime blacklists. Using its rule
base, it uses a wide range of heuristic tests on mail headers and body
text to identify ``spam'', also known as unsolicited commercial email.
Once identified, the mail can then be optionally tagged as spam for
later filtering using the user's own mail user-agent application.

%package version
Summary: Empty package to synchronize other spamassassin subpackages versions with
Group: Networking/Mail
BuildArch: noarch

%description version
This package contains no files and exist just to synchronize other spamassassin
subpackages versions with.

%prep
%setup -q -n Mail-SpamAssassin-%{version}
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
cp -f spamc/spamc.pod spamc/spamc
%perl_vendor_build LOCALRULESDIR=%_sysconfdir/spamassassin INSTALLMAN1DIR=%_man1dir BUILD_SPAMC=no

# Rebuild spamc wirh SSL
pushd spamc
%autoreconf
%configure \
	--sysconfdir=%_sysconfdir/spamassassin \
	--datadir=%_datadir/spamassassin \
	%{subst_enable ssl}
popd
rm -f spamc/spamc
%make_build blib/script/spamc

%install
mkdir -p %buildroot{/var/spool/spamassassin,%_localstatedir/spamd,/var/run/spamd,/var/lib/spamassassin}

%perl_vendor_install \
	SYSCONFDIR=%buildroot%_sysconfdir \
	B_CONFDIR=%buildroot%_sysconfdir/spamassassin \
	I_CONF_DIR=%buildroot%_sysconfdir/spamassassin \
	B_DATADIR=%buildroot%_datadir/spamassassin \
	install

find %buildroot -name .svn -exec rm -rf -- {} \;

install -pD -m755 %SOURCE1 %buildroot%_initdir/spamd
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/spamassassin/local.cf
install -pD -m644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/spamd

install -d -m700 %buildroot%_sysconfdir/spamassassin/sa-update-keys

# NO! We don't want dependancy on PostgreSQL generated by findreq from this file:
%add_findreq_skiplist %perl_vendor_privlib/Mail/SpamAssassin/BayesStore/PgSQL.pm

pod2man spamc/spamc.pod %buildroot%_man1dir/spamc.1

install -d %buildroot%_sysconfdir/cron.d
cat <<EOF >%buildroot%_sysconfdir/cron.d/sa-update
# you can switch "space" to "tab" between minutes and hours
# for stop randomization when when spamassasin installing
30 01 * * *    root    %_bindir/sa-update && [ -f /var/run/spamd.pid ] && %_initdir/spamd restart
EOF

#warning: Installed (but unpackaged) file(s) found:
#    /usr/lib/perl5/perllocal.pod
rm -f %buildroot%perl_vendor_archlib/perllocal.pod

%post
# randomize time of sa rules updating
RNDM1=$[$RANDOM/555]   # 0-59
RNDM2=$[$RANDOM/1424]  # 0-23
sed "s/^[0-9]\+ \+[0-9]\+/$RNDM1 $RNDM2/" -i %_sysconfdir/cron.d/sa-update >/dev/null 2>&1 ||:

%post spamd
%post_service spamd

%preun spamd
%preun_service spamd

%post spamc
/usr/sbin/groupadd -r -f spamd
/usr/sbin/useradd -r -g spamd -d /dev/null -s /dev/null -n spamc >/dev/null 2>&1 ||:

%pre spamd
/usr/sbin/groupadd -r -f spamd
/usr/sbin/useradd -r -g spamd -d %_localstatedir/spamd -s /dev/null -n spamd >/dev/null 2>&1 ||:

%files
%doc CREDITS INSTALL README TRADEMARK USAGE procmailrc.example Changes sample-nonspam.txt sample-spam.txt
%doc ldap sql
%_bindir/spamassassin
%_bindir/sa-awl
%_bindir/sa-compile
%_bindir/sa-learn
%_bindir/sa-update
%config(noreplace) %_sysconfdir/cron.d/sa-update
%_man1dir/spamassassin*
%_man1dir/sa-compile*
%_man1dir/sa-learn*
%_man1dir/sa-update*
%_man1dir/sa-awl*
# sa-update download rules to /var/lib/spamassassin, so both should be in one subpackage:
%dir /var/lib/spamassassin

%files version

%files spamd
%doc spamd/README spamd/PROTOCOL
%config %_initdir/spamd
%config(noreplace) %_sysconfdir/sysconfig/spamd
%_bindir/spamd
%_bindir/sa-check_spamd
%_man1dir/spamd*
%attr(700,spamd,spamd) %_localstatedir/spamd/
#attr(3770,root,spamd) /var/run/spamd/

%files spamc
%_bindir/spamc
%_man1dir/spamc*

%files -n perl-%pname
%doc sample-nonspam.txt sample-spam.txt
%dir %_sysconfdir/spamassassin
%dir %attr(0700,root,root) %_sysconfdir/spamassassin/sa-update-keys
%config(noreplace) %_sysconfdir/spamassassin/*.*
%_datadir/spamassassin
%dir %attr(0775,root,mail) /var/spool/spamassassin
%perl_vendor_privlib/Mail
%perl_vendor_privlib/spamassassin-run.pod
#%_man3dir/*

%changelog
* Fri Jan 03 2020 Sergey Y. Afonin <asy@altlinux.org> 3.4.3-alt1
- 3.4.3 (fixes: CVE-2018-11805, CVE-2019-12420)
- updated %%License to SPDX syntax

* Mon Dec 31 2018 Igor Vlasenko <viy@altlinux.ru> 3.4.2-alt1
- NMU: 3.4.2

* Wed Sep 05 2018 Sergey Y. Afonin <asy@altlinux.ru> 3.4.1-alt2
- rebuilt with LibreSSL-devel
- disabled SSL v3 (applied Debian's patch)

* Sun Nov 15 2015 Sergey Y. Afonin <asy@altlinux.ru> 3.4.1-alt1
- NMU: 3.4.1
- added cron's rule for sa-update (ALT #26682)

* Thu Jun 19 2014 Sergey Y. Afonin <asy@altlinux.ru> 3.4.0-alt1
- NMU: 3.4.0 (ALT #30063)
- fixed start, stop, reload and status options in init.d/spamd (ALT #28789)
- changed permisson for sa-update-keys directory to 700
- added lsb init header for init.d/spamd
- removed /var/run/spamd directory (/var/run used for pid file)
- added CHILDUSER variable and described it in the /etc/sysconfig/spamd

* Tue Nov 05 2013 Igor Vlasenko <viy@altlinux.ru> 3.3.2-alt3
- NMU: added missing Pod dependencies

* Wed Apr 03 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.3.2-alt2
- hackaround build

* Thu Jul 21 2011 Victor Forsiuk <force@altlinux.org> 3.3.2-alt1
- 3.3.2

* Mon Jan 31 2011 Victor Forsiuk <force@altlinux.org> 3.3.1-alt2
- Fix warnings with perl 5.12.

* Fri Oct 08 2010 Victor Forsiuk <force@altlinux.org> 3.3.1-alt1
- 3.3.1

* Wed Mar 03 2010 Victor Forsiuk <force@altlinux.org> 3.3.0-alt1
- 3.3.0

* Wed Jan 13 2010 Victor Forsyuk <force@altlinux.org> 3.2.5-alt2
- Quick fix for much talked-of "Y2K10 Rule Bug".

* Wed Aug 20 2008 Victor Forsyuk <force@altlinux.org> 3.2.5-alt1
- 3.2.5
- perl-Mail-SpamAssassin is noarch now.
- Add empty subpackage to synchronize other spamassassin subpackages
  versions with. Use this method to fix ALT#13776.

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 3.2.4-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Thu Mar 13 2008 Victor Forsyuk <force@altlinux.org> 3.2.4-alt1
- 3.2.4

* Thu Aug 16 2007 Victor Forsyuk <force@altlinux.org> 3.2.3-alt1
- 3.2.3
- Move spamassassin spool directory to perl-Mail-SpamAssassin subpackage.
- Switch from legacy Mail::SPF::Query to Mail::SPF.

* Thu Jun 14 2007 Victor Forsyuk <force@altlinux.org> 3.2.1-alt1
- 3.2.1 (fixes CVE-2007-2873).

* Thu May 03 2007 Victor Forsyuk <force@altlinux.org> 3.2.0-alt1
- 3.2.0

* Thu Mar 15 2007 Victor Forsyuk <force@altlinux.org> 3.1.8-alt1
- 3.1.8 (fixes CVE-2007-0451).

* Mon Jan 22 2007 Victor Forsyuk <force@altlinux.org> 3.1.7-alt2
- perl-IO-Socket-SSL required by spamd for spamc/spamd SSL communication.
- Change all instances of /etc/mail/spamassassin in the documentation
  to /etc/spamassassin, since thats where the configuration is going.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 3.1.7-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Fri Nov 10 2006 Victor Forsyuk <force@altlinux.org> 3.1.7-alt1
- 3.1.7
- Add Requires for packages needed by SA plugins. So now we have more
  dependencies, but all enabled plugins will 'just work'!

* Tue Jun 06 2006 Victor Forsyuk <force@altlinux.ru> 3.1.3-alt1
- 3.1.3 (fixes CVE-2006-2447).

* Tue Mar 28 2006 Victor Forsyuk <force@altlinux.ru> 3.1.1-alt1
- 3.1.1
- Updated build reqs.

* Tue Oct 04 2005 Victor Forsyuk <force@altlinux.ru> 3.1.0-alt1
- 3.1.0
- Small fixes in local.cf.

* Tue Jun 07 2005 Victor Forsyuk <force@altlinux.ru> 3.0.4-alt1
- 3.0.4
- Added russian translation of spamassassin messages.
- Create pseudousers and directories for spamd (suggested by ldv@).

* Fri Apr 29 2005 Victor Forsyuk <force@altlinux.ru> 3.0.3-alt1
- 3.0.3
- Allow replacement of rc.d service script during upgrades
  (i.e., remove "noreplace" in spec).
- Relocate configuration from /etc/mail/spamassassin to /etc/spamassassin.

* Mon Feb 14 2005 Victor Forsyuk <force@altlinux.ru> 3.0.2-alt2
- spamd requires perl-Storable to run. Add dependancy.
- Add patch from SA bugzilla #4046.

* Tue Dec 28 2004 Victor Forsyuk <force@altlinux.ru> 3.0.2-alt1
- New version.
- Build spamc with ssl support enabled by default.
- Updated package dependencies (thanx to ldv@).

* Wed Oct 27 2004 Victor Forsyuk <force@altlinux.ru> 3.0.1-alt1
- 3.0.1.
- sa-stats requires perl-Parse-Syslog.

* Fri Oct 15 2004 Victor Forsyuk <force@altlinux.ru> 3.0.0-alt6
- Fix bug #5271 (issues with dccproc when using SA with amavisd).

* Thu Sep 23 2004 Victor Forsyuk <force@altlinux.ru> 3.0.0-alt5
- New and shiny version.
- Install sa-stats script.

* Wed Sep 15 2004 Victor Forsyuk <force@altlinux.ru> 3.0.0-alt4.rc5
- 3.0.0-rc5.

* Mon Aug 30 2004 Victor Forsyuk <force@altlinux.ru> 3.0.0-alt3.rc2
- 3.0.0-rc2.

* Mon Aug 16 2004 Victor Forsyuk <force@altlinux.ru> 3.0.0-alt2.rc1
- Packaged 3.0.0-rc1 with security fix that prevents a DoS attack.
  All 3.0.0-prex versions to date was affected.

* Tue Aug 03 2004 Victor Forsyuk <force@altlinux.ru> 3.0.0-alt1.pre3
- 3.0.0-pre3.

* Thu Jan 22 2004 Victor Forsyuk <force@altlinux.ru> 2.63-alt1
- New version.
- Increase start priority to get spamd running before MTA starts.
- Enable network checks by default in local.cf.
- User need to be in group 'mail' to be able to train bayes database.

* Mon Jan 19 2004 Victor Forsyuk <force@altlinux.ru> 2.62-alt1
- New version.
- Package sql/ and tools/ (as %%doc files).

* Thu Dec 11 2003 Victor Forsyuk <force@altlinux.ru> 2.61-alt1
- Added spool directory (used for site-wide bayes databases and
  auto-whitelisting).
- Activate site-wide bayes in local.cf.
- Remove options for auto-whitelisting and creating user
  preferences files from default spamd sysconfig.

* Wed Oct 15 2003 Victor Forsyuk <force@altlinux.ru> 2.60-alt1
- local.cf tuning

* Mon Sep 29 2003 Victor Forsyuk <force@altlinux.ru> 2.60-alt0
- Initial build for Sisyphus.
