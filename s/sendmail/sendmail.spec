Name: sendmail

%define tarbolversion 8.16.0.45

Version: %tarbolversion
Release: alt1

Packager: Sergey Y. Afonin <asy@altlinux.ru>

Summary: A widely used Mail Transport Agent (MTA)
License: Sendmail-8.23
Group: System/Servers
URL: http://www.sendmail.org

Source0: %name.%tarbolversion.tar.gz
Source1: %name.init
Source2: %name-submit.init
Source3: %name-aliases
Source4: %name.sysconfig
Source5: %name-etc-mail-Makefile
Source6: %name-alt.mc

Source7:  %name-sasl.conf
Source8:  %name.pam
Source9:  %name-altlinux-site.config.m4
Source10: %name-README.alt
Source11: %name-submit.mc
Source12: %name-rhsbl.m4
Source14: %name-virtuserdomains
Source15: %name-certs.sh
Source16: %name-milters_watchdog

Source20: %name-access.main
Source21: %name-access.dynamic
Source22: %name-access.spam
Source23: %name-access.virus
Source24: %name-access.other
Source25: %name-access.sendmail.org

# Cyrus-imap integration
Source30: %name-README.cyrus-imap
Source31: %name-mrs.m4
Source32: %name-mrs_cyrus.m4
Source33: %name-cyrusv2.m4
Source34: %name-cyrus-imap-mailertable.mc
Source36: %name-cyrus-imap-localrelay.mc

# Patches section
Patch0: %name-8.15.1-alt.patch
Patch1: %name-8.10.0-makemapman.patch
Patch2: %name-8.16.0.45-smrsh.patch
Patch3: %name-8.8.7-rmail.patch
Patch4: %name-8.12.2-aliasesDoS.patch
Patch5: %name-8.11.1-up-limit.patch
Patch6: %name-8.11.0-m4path.patch

# experimental
Patch7: %name-8.14.4-BODY_7BIT_IGNORED-srvrsmtp.c.patch

# Cyrus-imap integration
Patch10: %name-mrs-8.12.11.patch

Patch50: %name-contrib-expn.pl-tempfile.patch

#errata
#Patch100:

%add_findreq_skiplist */include/*

Provides: MTA, MailTransportAgent, smtpdaemon

Conflicts: postfix, meta1, exim-common

Requires: %name-submit = %{version}-%{release}, makemap = %{version}-%{release}

BuildConflicts: bind-devel
BuildRequires(pre): libpam0-devel sendmail-common

# Not detected by buildreq
BuildRequires: openssl
# Automatically added by buildreq on Thu Apr 21 2005
BuildRequires: glibc-devel groff-base libdb4-devel libgdbm-devel libldap-devel libsasl2-devel libssl-devel

# for cidrexpand
BuildRequires: perl-Net-CIDR

%description
The Sendmail program is a widely used Mail Transport Agent (MTA).
MTAs send mail from one machine to another.

Sendmail is not a client program, which you use to read your e-mail.
Sendmail is a behind-the-scenes program which actually moves your
e-mail over networks or the Internet to where you want it to go.

If you ever need to reconfigure Sendmail, you'll also need to have the
sendmail-cf package installed. If you need documentation on Sendmail,
you can install the sendmail-doc package (sendmail-doc contains ALT Linux
specific recomendations README.alt and README.cyrus-imap).

%package submit
Summary: sendmail's submit service
License: Sendmail-8.23
Group: System/Servers
Conflicts: postfix
AutoReq: yes, noshell

%description submit
This package need for sending mail from command line

%package -n makemap
Summary: makemap utility of sendmail
License: Sendmail-8.23
Group: Databases

%description -n makemap
Makemap creates the database maps used by the keyed map lookups in
sendmail(8) and in some other software. It's working with Berkeley DB.

%package doc
Summary: Documentation about the Sendmail Mail Transport Agent program
License: Sendmail-8.23
Group: System/Servers
AutoReq: yes, noshell
Conflicts: %name < %version-%release, %name > %version-%release
BuildArch: noarch

%description doc
The %name-doc package contains documentation about the Sendmail
Mail Transport Agent (MTA) program, including release notes, the
Sendmail FAQ and a few papers written about Sendmail. The papers are
provided in PostScript(TM) and troff formats.

Install the %name-doc package if you need documentation about
Sendmail.

%package cf
Summary: The files needed to reconfigure Sendmail
License: Sendmail-8.23
Group: System/Servers
Requires: make, m4
Conflicts: %name < %version-%release, %name > %version-%release
BuildArch: noarch

%description cf
This package includes the configuration files which you'd need to generate the
%name.cf file distributed with the %name package.

You'll need the %name-cf package if you ever need to reconfigure and rebuild
your %name.cf file. For example, the default %name.cf file is not
configured for UUCP. If someday you needed to send and receive mail over UUCP,
you'd need to install the %name-cf package to help you reconfigure Sendmail.

Install the %name-cf package if you need to reconfigure your
%name.cf file.

%package devel
Summary: Sendmail static libraries and headers file
Group: Development/Other
Requires: libmilter = %{version}-%{release}
Conflicts: %name < %version-%release, %name > %version-%release

%description devel
This package includes the static libraries and header files

%package -n libmilter
Summary: Sendmail's shared libraries (libmilter only)
Group: System/Libraries
Conflicts: %name < %version-%release, %name > %version-%release
Provides: sendmail-libs

%description -n libmilter
This package includes the shared libraries of Senadmail (now only 
libmilter.so). Main packadge isn't use shared libraries.

%package -n vacation
Summary: E-mail auto-responder
Group: Networking/Mail

%description -n vacation
Vacation returns a message, ~/.vacation.msg by default, to the sender informing 
them that you are currently not reading your mail.

%prep
%setup -q -n %name-%tarbolversion
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%patch10 -p1

%patch50 -p1

#errata
#patch100 -p0

%__sed -e 's|@@PATH@@|\.\.|' < %SOURCE6 > cf/cf/altlinux.mc
%__sed -e 's|@@PATH@@|\.\.|' < %SOURCE11> cf/cf/submit.mc
%__sed -e 's|@@PATH@@|\.\.|' < %SOURCE34> cf/cf/cyrus-imap-mailertable.mc
%__sed -e 's|@@PATH@@|\.\.|' < %SOURCE36> cf/cf/cyrus-imap-localrelay.mc

%__cp %{SOURCE31} cf/feature/mrs.m4
%__cp %{SOURCE32} cf/feature/mrs_cyrus.m4
%__cp -f %{SOURCE33} cf/mailer/cyrusv2.m4

%__cp %{SOURCE9} devtools/Site/site.config.m4

%build
%make_build

pushd cf/cf
m4 altlinux.mc > altlinux.cf
m4 cyrus-imap-mailertable.mc > cyrus-imap-mailertable.cf
m4 cyrus-imap-localrelay.mc > cyrus-imap-localrelay.cf
popd

%install
for i in %_bindir %_libdir %_mandir/man{1,5,8} %_sbindir %_logdir %_spooldir %_datadir/%name-cf %_initdir %_sysconfdir/sysconfig %_spooldir/mqueue/queue00{1,2} %_sysconfdir/smrsh %_sysconfdir/mail %_spooldir/clientmqueue var/run/%name %_sysconfdir/pam.d %_includedir ; do
	%__mkdir_p "$RPM_BUILD_ROOT/$i"
done

OBJDIR=obj.$(uname -s).$(uname -r).$(arch)

# fix default id and gid during install steps
export ID=" SBINOWN=`id -nu` UBINOWN=`id -nu` \
	    SBINGRP=`id -ng` UBINGRP=`id -ng` \
	    MSPQOWN=`id -nu` GBINGRP=`id -ng` \
	    GBINOWN=`id -nu` \
	    CFOWN=`id -nu` CFGRP=`id -ng` \
	    BINOWN=`id -nu` BINGRP=`id -ng` \
	    MANOWN=`id -nu` MANGRP=`id -ng` \
	    LIBOWN=`id -nu` LIBGRP=`id -ng` LIBMODE=644 \
	    INCOWN=`id -nu` INCGRP=`id -ng` INCMODE=644 \
	    MANROOT=%_mandir/man CFMODE=0644"

%makeinstall LIBDIR=%_libdir DESTDIR=$RPM_BUILD_ROOT CF=real-time $ID
rm -f $RPM_BUILD_ROOT%_libdir/*.a

#mailq and newaliases provided by sendmail-common package
rm -f $RPM_BUILD_ROOT%_bindir/{mailq,newaliases}

%make_build DESTDIR=$RPM_BUILD_ROOT $ID force-install -C $OBJDIR/rmail
%make_build DESTDIR=$RPM_BUILD_ROOT $ID force-install -C $OBJDIR/mail.local

# generate shared libmilter
pushd $OBJDIR/libmilter
rm -f *.a
gcc -shared -o libmilter.so.3 -Wl,-soname,libmilter.so.3 *.o -lpthread
popd

# install include & libs
#find $OBJDIR/lib* -name "*.a" -exec %__cp {} $RPM_BUILD_ROOT%_libdir \;
find $OBJDIR/lib* -name "*.so*" -exec %__cp {} $RPM_BUILD_ROOT%_libdir \;

# genegate symlink for *.so (only libmilter.so.3 now)
pushd $RPM_BUILD_ROOT%_libdir
find *.so.* -type f|\
 while read f; do \
    temp_name=`echo -n $f|sed -r "s/^(\w+)\..*/\1/g"`; \
    %__ln_s -f $f $temp_name.so; \
 done
popd

%__ln_s -f ../sbin/makemap $RPM_BUILD_ROOT%_bindir/makemap

%__cp -ar include $RPM_BUILD_ROOT%prefix

# install docs by hand
%__mkdir_p $RPM_BUILD_DIR/%name-%tarbolversion/docs
%__cp -ar FAQ LICENSE KNOWNBUGS README RELEASE_NOTES doc $RPM_BUILD_DIR/%name-%tarbolversion/docs/
%__cp smrsh/README $RPM_BUILD_DIR/%name-%tarbolversion/docs/README.smrsh
%__cp sendmail/README $RPM_BUILD_DIR/%name-%tarbolversion/docs/README.sendmail
%__cp sendmail/SECURITY $RPM_BUILD_DIR/%name-%tarbolversion/docs/
%__cp sendmail/TRACEFLAGS $RPM_BUILD_DIR/%name-%tarbolversion/docs/
%__cp sendmail/TUNING $RPM_BUILD_DIR/%name-%tarbolversion/docs/
%__cp mail.local/README $RPM_BUILD_DIR/%name-%tarbolversion/docs/README.mail.local
%__cp cf/README $RPM_BUILD_DIR/%name-%tarbolversion/docs/README.cf
%__cp cf/cf/README $RPM_BUILD_DIR/%name-%tarbolversion/docs/README.install-cf
%__cp %SOURCE10 $RPM_BUILD_DIR/%name-%tarbolversion/docs/README.alt
%__cp %SOURCE30 $RPM_BUILD_DIR/%name-%tarbolversion/docs/README.cyrus-imap
%__cp libmilter/README $RPM_BUILD_DIR/%name-%tarbolversion/docs/README.libmilter
%__cp -ar libmilter/docs/ $RPM_BUILD_DIR/%name-%tarbolversion/docs/libmilter
%__cp %SOURCE15 $RPM_BUILD_DIR/%name-%tarbolversion/docs/

# Dadou: Remove ugly bad dependencies in doc package
find contrib -type f |xargs fgrep -l /usr/local/bin/perl |
	xargs -r %__subst -p 's|/usr/local/bin/perl|%_bindir/perl|g'

#	xargs -r perl -pi -e 's|/usr/local/bin/perl|%_bindir/perl|g'
find contrib -type f |xargs fgrep -l '!/bin/perl' |
	xargs -r %__subst -p 's|#!/bin/perl|#!%_bindir/perl|g'

#	xargs -r perl -pi -e 's|#!/bin/perl|#!%_bindir/perl|g'

# install the cf files
%make_build DESTDIR=$RPM_BUILD_ROOT $ID CF=altlinux install-cf -C cf/cf
pushd cf
%__cp -ar * $RPM_BUILD_ROOT%_datadir/%name-cf
%__rm -f $RPM_BUILD_ROOT%_datadir/%name-cf/*/*.m4path
%__make -C cf altlinux.cf
popd

# Create /etc/mail/ files

%__sed -e 's|@@PATH@@|%_datadir/%name-cf|' < %SOURCE6 > $RPM_BUILD_ROOT%_sysconfdir/mail/%name-alt.mc
%__sed -e 's|@@PATH@@|%_datadir/%name-cf|' < %SOURCE11> $RPM_BUILD_ROOT%_sysconfdir/mail/submit.mc

echo "# local-host-names - include all aliases for your machine here." > $RPM_BUILD_ROOT%_sysconfdir/mail/local-host-names
echo -n >$RPM_BUILD_ROOT%_logdir/%name.st
( echo "# trusted-users - users that can send mail as others without a warning"
echo "# apache, mailman, majordomo, uucp, are good candidates" ) \
	> $RPM_BUILD_ROOT%_sysconfdir/mail/trusted-users

# for CIDR support in mail/access (see /etc/mail/Makefile)
%__cp contrib/cidrexpand $RPM_BUILD_ROOT%_sbindir/cidrexpand

# /etc/mail/access parts
%__mkdir_p $RPM_BUILD_ROOT/%_sysconfdir/mail/access.d.shared
%__mkdir_p $RPM_BUILD_ROOT/%_sysconfdir/mail/access.d
%__sed -e 's|@@NAMEDOCVERSION@@|%name-doc-%version|' < %SOURCE20 > $RPM_BUILD_ROOT%_sysconfdir/mail/access.main
%__cp %SOURCE21 $RPM_BUILD_ROOT%_sysconfdir/mail/access.d.shared/dynamic.access
%__cp %SOURCE22 $RPM_BUILD_ROOT%_sysconfdir/mail/access.d.shared/spam.access
%__cp %SOURCE23 $RPM_BUILD_ROOT%_sysconfdir/mail/access.d.shared/virus.access
%__cp %SOURCE24 $RPM_BUILD_ROOT%_sysconfdir/mail/access.d/other.access
%__cp %SOURCE25 $RPM_BUILD_ROOT%_sysconfdir/mail/access.d/sendmail.org.access

for map in virtusertable access domaintable mailertable; do
    touch $RPM_BUILD_ROOT%_sysconfdir/mail/${map}
    %__chmod 0644 $RPM_BUILD_ROOT%_sysconfdir/mail/${map}
done
%__install -m644 %SOURCE3 $RPM_BUILD_ROOT%_sysconfdir/mail/aliases
%__install -m644 %SOURCE14 $RPM_BUILD_ROOT%_sysconfdir/mail/virtuserdomains
%__install -m644 %SOURCE5 $RPM_BUILD_ROOT%_sysconfdir/mail/Makefile

%__ln_s %_sysconfdir/mail/aliases $RPM_BUILD_ROOT%_sysconfdir/aliases

# other /etc/
%__install -m644 %SOURCE4 $RPM_BUILD_ROOT%_sysconfdir/sysconfig/%name
%__install -m755 %SOURCE1 $RPM_BUILD_ROOT%_initdir/%name
%__install -m755 %SOURCE2 $RPM_BUILD_ROOT%_initdir/%name-submit
%__install -m644 %SOURCE8 $RPM_BUILD_ROOT%_sysconfdir/pam.d/smtp

# configugations for libsasl2 in /etc/sasl2/ in AltLinux
%__install -m755 -d $RPM_BUILD_ROOT/%_sysconfdir/sasl2
%__install -m644 %SOURCE7 $RPM_BUILD_ROOT/%_sysconfdir/sasl2/Sendmail.conf

# add certs directory for STARTTLS
%__mkdir -p $RPM_BUILD_ROOT/%_sysconfdir/mail/certs
## create placeholder certs
#pushd $RPM_BUILD_ROOT/%_sysconfdir/mail/certs
#sh %{SOURCE15}
#popd

# create fake *.db
pushd $RPM_BUILD_ROOT/%_sysconfdir/mail
touch access.db domaintable.db mailertable.db virtusertable.db
popd

%__install -m755 %SOURCE16 %buildroot%_bindir/sendmail-milters_watchdog
%__install -m755 -d %buildroot%_sysconfdir/cron.d
cat <<EOF >%buildroot%_sysconfdir/cron.d/sendmail-milters_watchdog
#*/5 * * * *       root    %_bindir/sendmail-milters_watchdog
EOF
cat <<EOF >%buildroot%_sysconfdir/mail/milters_watchdog.conf
#MILTERS_LIST="mailfromd"
EOF

%pre

%post

# rebuild *.db (possibe new DB)
{
    pushd %_sysconfdir/mail
    touch virtusertable access domaintable mailertable aliases
    make db
    popd
} &>/dev/null ||:

%post_service %name

%preun
%preun_service %name

%pre submit
%_sbindir/groupadd -r -f smmsp
%_sbindir/useradd -M -r -g smmsp -s /dev/null -c smmsp smmsp &>/dev/null ||:

%post submit
%post_service %name-submit

%preun submit
%preun_service %name-submit

%files
%_bindir/hoststat
%_bindir/purgestat
%_bindir/rmail
%_bindir/sendmail-milters_watchdog

%_sbindir/editmap
%_sbindir/mail.local
%_sbindir/mailstats
%_sbindir/praliases
%_sbindir/smrsh
%_sbindir/cidrexpand

%attr(644,root,root) %_mandir/man?/*
%exclude  %_mandir/man1/vacation.*
%exclude  %_mandir/man8/makemap.*
%attr(640,root,root) %_logdir/%name.st
%attr(640,root,root) %_logdir/statistics

%dir %_sysconfdir/smrsh

%dir %_sysconfdir/mail/certs
#%attr(0600,root,root) %config(noreplace) %_sysconfdir/mail/certs/*

%attr(0444,root,wheel) %config(noreplace) %_sysconfdir/mail/%name.cf

%exclude %_sysconfdir/mail/submit.mc
%attr(0644,root,root) %config %_sysconfdir/mail/*.mc

%attr(0640,root,root) %config(noreplace) %_sysconfdir/mail/local-host-names
%attr(0640,root,root) %config(noreplace) %_sysconfdir/mail/trusted-users
%attr(0640,root,root) %config(noreplace) %_sysconfdir/mail/aliases
%_sysconfdir/aliases
%attr(0644,root,root) %config(noreplace) %_sysconfdir/mail/virtuserdomains
%attr(0644,root,root) %config(noreplace) %_sysconfdir/mail/virtusertable

%ghost %_sysconfdir/mail/*.db

%ghost %_sysconfdir/mail/access
%config(noreplace) %_sysconfdir/mail/access.main
%dir %_sysconfdir/mail/access.d
%config(noreplace) %_sysconfdir/mail/access.d/*.access
%dir %_sysconfdir/mail/access.d.shared
%config(noreplace) %_sysconfdir/mail/access.d.shared/*.access

%attr(0644,root,root) %config(noreplace) %_sysconfdir/mail/domaintable
%attr(0644,root,root) %config(noreplace) %_sysconfdir/mail/mailertable
%attr(0640,root,root) %config(noreplace) %_sysconfdir/mail/helpfile
%attr(0644,root,root) %config(noreplace) %_sysconfdir/mail/milters_watchdog.conf

%config(noreplace) %_sysconfdir/sysconfig/%name

%config %_sysconfdir/mail/Makefile

%attr(0755,root,root) %config(noreplace) %_initdir/%name

%attr(0750,root,wheel) %dir %_spooldir/mqueue
%attr(0750,root,wheel) %dir %_spooldir/mqueue/queue*

%config(noreplace) %_sysconfdir/sasl2/Sendmail.conf
%config(noreplace) %_sysconfdir/pam.d/smtp
%config(noreplace) %_sysconfdir/cron.d/*
%doc docs/LICENSE

%files submit
%dir %_sysconfdir/mail
%attr(2711,root,smmsp) %_sbindir/%name
%attr(0444,root,wheel) %config(noreplace) %_sysconfdir/mail/submit.cf
%attr(0644,root,root) %config %_sysconfdir/mail/submit.mc
%attr(0770,smmsp,smmsp) %dir %_spooldir/clientmqueue
%ghost %dir /var/run/%name
%attr(0755,root,root) %config(noreplace) %_initdir/%name-submit
%doc docs/LICENSE

%files -n makemap
%_bindir/makemap
%_sbindir/makemap
%_mandir/man8/makemap.*
%doc docs/LICENSE

%files cf
%_datadir/%name-cf

%files doc
%doc contrib docs

%files devel
%doc libsm/{*.html,README} docs/{libmilter,README.libmilter}
%_includedir/lib*
%_includedir/sendmail
%_includedir/sm
%_libdir/lib*.so

%files -n libmilter
%exclude %_libdir/lib*.so
%_libdir/lib*.so*

%files -n vacation
%_bindir/vacation
%_mandir/man1/vacation.*
%doc docs/LICENSE

%changelog
* Sun May 10 2020 Sergey Y. Afonin <asy@altlinux.org> 8.16.0.45-alt1
- New version
- updated smrsh.patch for 8.16.0.45
- used gethostbyname2 instead of gethostbyname/RES_USE_INET6,
  removed sendmail-8.15.2-glibc-2.30.patch

* Sun Mar 29 2020 Sergey Y. Afonin <asy@altlinux.org> 8.16.0.41-alt3
- fixed FTBFS: added sendmail-8.15.2-glibc-2.30.patch (from OpenSUSE)
- Updated License tag to SPDX syntax

* Wed Mar 06 2019 Sergey Y. Afonin <asy@altlinux.ru> 8.16.0.41-alt2
- sendmail-access.main: added IPv6 example for cidrexpand

* Mon Feb 25 2019 Sergey Y. Afonin <asy@altlinux.ru> 8.16.0.41-alt1
- New version
- enabled _FFR_AUTH_FAIL_LOG_USER

* Thu Aug 30 2018 Sergey Y. Afonin <asy@altlinux.ru> 8.16.0.29-alt2
- disabled tcpwrappers support
- rebuilt with openssl 1.1

* Tue Aug 28 2018 Sergey Y. Afonin <asy@altlinux.ru> 8.16.0.29-alt1
- New version (with openssl 1.1 support)
- enabled the use of elliptic curve cryptography in STARTTLS

* Wed Jul 04 2018 Sergey Y. Afonin <asy@altlinux.ru> 8.15.2-alt6
- added configurable submit queue time in sendmail-submit init script
- removed linker's flag with nsl (fixed FTBFS)

* Wed Jan 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 8.15.2-alt5
- rebuilt without NIS support.

* Sun Feb 12 2017 Sergey Y. Afonin <asy@altlinux.ru> 8.15.2-alt4
- added to *.mc of ALT (except submit.mc) confMILTER_MACROS_ENVRCPT
  definition for mailfromd

* Sat Feb 04 2017 Sergey Y. Afonin <asy@altlinux.ru> 8.15.2-alt3
- synced submit.mc with original 8.15.2/cf/cf/submit.mc
- added FEATURE(`nocanonify') to submit.mc
- set confDIRECT_SUBMISSION_MODIFIERS to 'C' in submit.mc

* Thu May 26 2016 Sergey Y. Afonin <asy@altlinux.ru> 8.15.2-alt2
- packaged cidrexpand from contrib directory
- used cidrexpand in /etc/mail/Makefile

* Sat Oct 17 2015 Sergey Y. Afonin <asy@altlinux.ru> 8.15.2-alt1
- New version

* Fri Dec 12 2014 Sergey Y. Afonin <asy@altlinux.ru> 8.15.1-alt2
- added FEATURE(`nocanonify') to *.mc
- removed old examples of *.mc
- removed sendmail-cf-8.13-0.4.1.corvax.tar.bz2
- refactored sendmail-X.Y.Z-alt.patch (site.config.m4 the
  separate file now)

* Sun Dec 07 2014 Sergey Y. Afonin <asy@altlinux.ru> 8.15.1-alt1
- New version (incompatible change in IPv6 configuration,
  please check RELEASE_NOTES before update)

* Wed May 28 2014 Sergey Y. Afonin <asy@altlinux.ru> 8.14.9-alt1
- New version (security update)
- some cleanups in *.mc
- updated access.d/sendmail.org.access

* Thu Jan 30 2014 Sergey Y. Afonin <asy@altlinux.ru> 8.14.8-alt2
- 8.14.8-alt1 pushed with 8.14.7 tarball. :-(
  So alt2 is realy new version.

* Wed Jan 29 2014 Sergey Y. Afonin <asy@altlinux.ru> 8.14.8-alt1
- New version
- enabled reject for mail which contains a NUL byte
  (in configs for Cyrus-IMAP)

* Thu Sep 12 2013 Sergey Y. Afonin <asy@altlinux.ru> 8.14.7-alt2
- rebuilt with cyrus-sasl 2.1.26

* Fri Sep 06 2013 Sergey Y. Afonin <asy@altlinux.ru> 8.14.7-alt1
- New version (built with -D_FFR_REJECT_NUL_BYTE)
- added patch for ignore BODY=7BIT in smtp "mail from" command

* Sat Apr 13 2013 Sergey Y. Afonin <asy@altlinux.ru> 8.14.6-alt2
- cleanups:
  - access.d.shared/helo.access removed (a part of Corvax hacks,
    see changelog for 8.14.2-alt2)

* Sat Apr 13 2013 Sergey Y. Afonin <asy@altlinux.ru> 8.14.6-alt1
- New version (with errata 2013-01-18: 8.14.6.milter.EHLOmacros)

* Mon May 28 2012 Sergey Y. Afonin <asy@altlinux.ru> 8.14.5-alt3
- fixed building with --no-copy-dt-needed-entries in new ld
- do not create demo ssl certs

* Thu Aug 25 2011 Sergey Y. Afonin <asy@altlinux.ru> 8.14.5-alt2
- fixed processing of two AUTH lines (patch from comp.mail.sendmail)

* Thu Jun 09 2011 Sergey Y. Afonin <asy@altlinux.ru> 8.14.5-alt1
- New version
- build with NETINET6
- removed deprecated parts from %%pre and %%post
- some cleanups in spec

* Wed Apr 06 2011 Sergey Y. Afonin <asy@altlinux.ru> 8.14.4-alt4
- added %%ghost for /var/run/%name
- fixed typo in call of chown in init scripts.

* Fri Feb 25 2011 Sergey Y. Afonin <asy@altlinux.ru> 8.14.4-alt3
- changed SMTP_MAILER_MAX to confMAX_MESSAGE_SIZE in ALT's *.mc
- disabled default auth mechanisms in ALT's *.mc
- fixed build on x86_64

* Tue Feb 23 2010 Sergey Y. Afonin <asy@altlinux.ru> 8.14.4-alt2
- some cleanups in spec
- rebuild with new libssl

* Mon Feb 22 2010 Sergey Y. Afonin <asy@altlinux.ru> 8.14.4-alt1
- New version, security update (CVE-2009-4565)
  addition: look to Errata 2010-01-04 on http://www.sendmail.org/releases/8.14.4
  if used FEATURE(`ldap_routing')

* Fri Dec 25 2009 Sergey Y. Afonin <asy@altlinux.ru> 8.14.3-alt6
- Removed runlevel list from start/stop sections of lsb init header
  in init-scripts

* Tue Sep 01 2009 Sergey Y. Afonin <asy@altlinux.ru> 8.14.3-alt5
- rebuild with new libldap

* Sat Jan 17 2009 Sergey Y. Afonin <asy@altlinux.ru> 8.14.3-alt4
- fixed repocop's warnings:
  added exim-common to Conflicts in sendmail package
  added postfix to Conflicts in sendmail-submit package

* Thu Nov 13 2008 Sergey Y. Afonin <asy@altlinux.ru> 8.14.3-alt3
- removed ldconfig calling due to new rpm

* Thu Sep 25 2008 Sergey Y. Afonin <asy@altlinux.ru> 8.14.3-alt2
- fixed usage of "/tmp" in contrib/expn.pl
- added "BuildArch: noarch" to "doc" and "cf" packages
- changed GID for *.db to "mail"

* Mon May 19 2008 Sergey Y. Afonin <asy@altlinux.ru> 8.14.3-alt1
- New version
- moved %_libdir/sasl/Sendmail.conf to %_sysconfdir/sasl2/
- moved libmilter.so to devel package

* Sun Mar 30 2008 Sergey Y. Afonin <asy@altlinux.ru> 8.14.2-alt2
- sendmail-cf-8.13-0.4.1.corvax.tar.bz2 is not packaged (replaced by mailfromd)
- *.mc cleanup
- bounceerror and mailerror aliases are used by default
- FEATURE(`greet_pause', `5000') is used by default

* Fri Nov 02 2007 Sergey Y. Afonin <asy@altlinux.ru> 8.14.2-alt1
- New version

* Tue Jun 05 2007 Sergey Y. Afonin <asy@altlinux.ru> 8.14.1-alt5
- fixed: restored default "aliases" from 8.13.6-alt3

* Mon May 07 2007 Sergey Y. Afonin <asy@altlinux.ru> 8.14.1-alt4
- moved 'makemap' to the separate package
- added %%doc docs/LICENSE to all undepended packages with binary

* Sat May 05 2007 Sergey Y. Afonin <asy@altlinux.ru> 8.14.1-alt3
- added to *.mc
  dnl define(`confMILTER_MACROS_EOM', confMILTER_MACROS_EOM`, {client_addr}')dnl Need for: mailfromd

* Tue Apr 17 2007 Sergey Y. Afonin <asy@altlinux.ru> 8.14.1-alt2
- fixed: empty sendmail-cf (#11520)

* Wed Apr 04 2007 Sergey Y. Afonin <asy@altlinux.ru> 8.14.1-alt1
- New version
- *.mc cleanup (some checks have to move to mailfromd)

* Thu Feb 01 2007 Sergey Y. Afonin <asy@altlinux.ru> 8.14.0-alt1
- New version
- errata: http://www.sendmail.org/patches/milter.rcpt.rej.p0

* Wed Dec 20 2006 Sergey Y. Afonin <asy@altlinux.ru> 8.13.8-alt5
- fixed: *.db generation in /etc/mail/Makefile
- fixed in spec: 
  - License changed from "BSD" to "SENDMAIL"
  - LICENSE file added to sendmail and sendmail-submit packages
  - symlinks mailq and newaliases is removed after %%makeinstall
  - second attempt to fix #1072 (sendmail/{SECURITY,TRACEFLAGS,TUNING} to doc)

* Mon Nov 20 2006 Dmitry V. Levin <ldv@altlinux.org> 8.13.8-alt4.1
- Do not package %_bindir/{mailq,newaliases} provided by
  sendmail-common package.

* Tue Oct 17 2006 Sergey Y. Afonin <asy@altlinux.ru> 8.13.8-alt4
- added: -DBROKEN_PTHREAD_SLEEP to devtools/Site/site.config.m4
  (according mailfromd documentation)

* Fri Sep 22 2006 Sergey Y. Afonin <asy@altlinux.ru> 8.13.8-alt3
- removed: BuildRequires: pmake

* Mon Sep 04 2006 Sergey Y. Afonin <asy@altlinux.ru> 8.13.8-alt2
- errata: http://www.sendmail.org/patches/client_name.assert.p0

* Tue Aug 29 2006 Sergey Y. Afonin <asy@altlinux.ru> 8.13.8-alt1
- New version, security update (CVE-2006-4434)

* Fri Aug 04 2006 Sergey Y. Afonin <asy@altlinux.ru> 8.13.7-alt4
- fixed: restoring some files replaced by files from 8.13.7-alt0.M24.1

* Wed Jul 19 2006 Sergey Y. Afonin <asy@altlinux.ru> 8.13.7-alt3
- added: definitions for mailfromd milter to *.mc

* Mon Jul 03 2006 Sergey Y. Afonin <asy@altlinux.ru> 8.13.7-alt2
- errata: http://www.sendmail.org/patches/main.c.DaemonPid.p0

* Thu Jun 15 2006 Sergey Y. Afonin <asy@altlinux.ru> 8.13.7-alt1
- New version
- security update
- errata: http://www.sendmail.org/patches/queue.c.20060614 

* Fri Mar 31 2006 Sergey Y. Afonin <asy@altlinux.ru> 8.13.6-alt3
- errata: http://www.sendmail.org/8.13.6.html#ERRATA (2006-03-28)

* Fri Mar 24 2006 Sergey Y. Afonin <asy@altlinux.ru> 8.13.6-alt2
- fixed: added %%post submit and %%preun submit to spec
- fixed: added -ldb to site.config.m4 (it is not added automatically on x86_64)

* Wed Mar 22 2006 Sergey Y. Afonin <asy@altlinux.ru> 8.13.6-alt1
- New version
- security update

* Sun Mar 19 2006 Sergey Y. Afonin <asy@altlinux.ru> 8.13.5-alt5
- fix: [--as-needed] build libmilter.so with -lpthread
- change: set MAX_DAEMON_CHILDREN in *.mc from 500 to 100
  ("soft nproc 256" in default limits.conf in ALT Linux)

* Mon Nov 07 2005 Sergey Y. Afonin <asy@altlinux.ru> 8.13.5-alt4
- change: move 'submit' to the separate package

* Mon Oct 31 2005 Sergey Y. Afonin <asy@altlinux.ru> 8.13.5-alt3
- fix: error "m4: cyrus-imap.mc: No such file or directory" then rebuild

* Fri Oct 14 2005 Sergey Y. Afonin <asy@altlinux.ru> 8.13.5-alt2
- add: sendmail-milters_watchdog 

* Wed Sep 28 2005 Sergey Y. Afonin <asy@altlinux.ru> 8.13.5-alt1
- New version

* Sat May 28 2005 Sergey Y. Afonin <asy@altlinux.ru> 8.13.4-alt4
- add: use_client_ptr to *.mc

* Fri May 27 2005 Sergey Y. Afonin <asy@altlinux.ru> 8.13.4-alt3
- fix: #1072
- fix: Requires: sendmail-libs for sendmail-devel
- change: in *.mc: ratecontrol and conncontrol with nodelay and terminate now
- change: error messages in mrs_cyrus.m4
- add: verify-sender and milter-regex milter definitions to *.mc examples.
- add: sendmail-access.whitelist.sendmail.org

* Thu Apr 21 2005 Sergey Y. Afonin <asy@altlinux.ru> 8.13.4-alt2
- fix: BuildRequires ( glibc-devel-static > glibc-devel, libdb4.2-devel-static > libdb4-devel )
- change: https://bugzilla.altlinux.org/show_bug.cgi?id=6503
    move some access.* to subdirectories (see /etc/mail/Makefile)
- change: improved interaction between /etc/mail/Makefile and /etc/init.d/sendmail

* Tue Mar 29 2005 Sergey Y. Afonin <asy@altlinux.ru> 8.13.4-alt1
- New version 

* Tue Feb 01 2005 Sergey Y. Afonin <asy@altlinux.ru> 8.13.3-alt1
- New version
- errata: http://www.sendmail.org/8.13.3.html#ERRATA (2005-01-17)
- add sendmail-certs.sh from Mandrake package (ssl certs generator) to doc

* Thu Oct 07 2004 Sergey Y. Afonin <asy@altlinux.ru> 8.13.1-alt3
- fix: Merge /etc/mail/aliases with Postfix package in AltLinux
- change: /etc/mail/access build from access.* (see /etc/mail/Makefile)
    (temporary convertor for access was added to spec)
- spec cleanaps:
    remove check.tar.bz2 from src.rpm (a long time it is not used in binary packages)
    remove old Mandrake access config convertor
     (relay_allow, ip_allow, name_allow -> access)
    remove old Mandrake sendmail.cw -> local-host-names convertor

* Tue Sep 14 2004 Sergey Y. Afonin <asy@altlinux.ru> 8.13.1-alt2
- errata: http://www.sendmail.org/8.13.1.html#ERRATA (2004-08-24)
- fix: set Timeout.aconnect to 6m
- add: virtuserdomains definition
- change: new mqueue definition 
- change: new sendmail-cf-8.13-0.4.1.corvax.tar.bz2

* Tue Aug 03 2004 Sergey Y. Afonin <asy@altlinux.ru> 8.13.1-alt1
- New version
- add: hack collection from Victor Ustugov (sendmail-cf-8.13-0.4.corvax.tgz,
    some spam control improvements, see README.corvax)

* Sat Jul 24 2004 Sergey Y. Afonin <asy@altlinux.ru> 8.13.0-alt1
- New version
- add: Url to spec
- add: improved cyrus-imap intergation from Andrzej Filip:
    http://anfi.webhop.net/sendmail/rtcyrus2.html
- add: config examples with new Cyrus-IMAP's integration (see cf/cf/cyrus-imap-*.mc) 
    and small how-to (README.cyrus-imap)
- add: enable rate limits and connection limits per IP in /etc/mail/access
- change: SMTP_MAILER_MAX set to 52428800 (50M)

* Tue Jun 15 2004 Stanislav Ievlev <inger@altlinux.org> 8.12.11-alt6.1
- NMU: /etc/aliases not under alternatives control now

* Fri May 07 2004 Sergey Y. Afonin <asy@altlinux.ru> 8.12.11-alt6
- change: remove libmilter.a from "devel" packadge, create "libs" 
    packadge with libmilter.so (while unused by sendmail).

* Sat Apr 03 2004 Sergey Y. Afonin <asy@altlinux.ru> 8.12.11-alt5
- fix: misprint in socket's name of clamav-milter in *.mc

* Thu Apr 01 2004 Sergey Y. Afonin <asy@altlinux.ru> 8.12.11-alt4
- fix: change PID-file name for submit to submit.pid
- fix: run queue for submit
- fix: add unpackaged /var/log/statistics to package 
- fix: add update-alternatives to PreReq
- add: rhsbl.m4 (for definiton Domain-Based Blacklist Zones, such as 
    some rfc-ignorant's blacklist zones)
- add: some changes in sendmail-alt.mc and sendmail-real-time.mc
  (leave as commented):
  - Clam AV milter 
  - rfc-ignorant's blacklists
  - separate addresses for bounce and mail errors
- add: some changes in aliases (leave as commented)
  - bounceerror and mailerror (point to postmaster)
- change: comment FEATURE(`relay_based_on_MX') in sendmail-alt.mc 
  and sendmail-real-time.mc
- change: MaxDaemonChildren from unlimited to 500 in sendmail-alt.mc
  and sendmail-real-time.mc

* Wed Mar 03 2004 Konstantin Timoshenko <kt@altlinux.ru> 8.12.11-alt3
- move 'vacation' to the separate package by "Ed V. Bartosh" <ed@altlinux.org>

* Sun Feb 22 2004 Konstantin Timoshenko <kt@altlinux.ru> 8.12.11-alt1
- 8.12.11
- rebuild with Berkeley DB 4.2

* Wed Dec 17 2003 Konstantin Timoshenko <kt@altlinux.ru> 8.12.10-alt4
- fix BuildRequires

* Thu Nov 27 2003 Konstantin Timoshenko <kt@altlinux.ru> 8.12.10-alt3
- chmod 750 /var/spool/mqueue

* Fri Sep 19 2003 Konstantin Timoshenko <kt@altlinux.ru> 8.12.10-alt2
- remove broked prereq.

* Thu Sep 18 2003 Konstantin Timoshenko <kt@altlinux.ru> 8.12.10-alt1
- 8.12.10
- Rewritten start/stop script to new rc scheme.

* Mon Mar 31 2003 Konstantin Timoshenko <kt@altlinux.ru> 8.12.9-alt1
- 8.12.9

* Tue Mar 04 2003 Konstantin Timoshenko <kt@altlinux.ru> 8.12.8-alt1
- 8.12.8

* Wed Jan 08 2003 Konstantin Timoshenko <kt@altlinux.ru> 8.12.7-alt1
- 8.12.7
- remove patch 8

* Sun Nov 10 2002 Konstantin Timoshenko <kt@altlinux.ru> 8.12.6-alt2
- rebuild with libgdbm
- rebuild with libwrap

* Tue Oct 15 2002 Konstantin Timoshenko <kt@altlinux.ru> 8.12.6-alt1
- 8.12.6

* Fri Aug 09 2002 Stanislav Ievlev <inger@altlinux.ru> 8.12.5-alt1.1
- fixed suid/sgid file permissions

* Tue Jul 02 2002 Konstantin Timoshenko <kt@altlinux.ru> 8.12.5-alt1
- 8.12.5

* Tue Jun 04 2002 Konstantin Timoshenko <kt@altlinux.ru> 8.12.4-alt1
- 8.12.4

* Tue May 28 2002 Konstantin Timoshenko <kt@altlinux.ru> 8.12.3-alt2
- security update

* Sat Apr 06 2002 Konstantin Timoshenko <kt@altlinux.ru> 8.12.3-alt1
- 8.12.3

* Wed Apr 03 2002 Dmitry V. Levin <ldv@alt-linux.org> 8.12.2-alt2
- Build with db4.
- Build without bind-devel.

* Thu Jan 17 2002 Konstantin Timoshenko <kt@altlinux.ru> 8.12.2-alt1
- 8.12.2

* Wed Oct 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.12.1-alt2
- Fixed few %%_bindir/* and %%_sbindir/* permissions.
- Fixed include files list in devel subpackage.

* Tue Oct  2 2001 Kostya Timoshenko <kt@altlinux.ru> 8.12.1-alt1
- 8.12.1
- added MailFilter support
- added devel package

* Fri Sep 14 2001 Kostya Timoshenko <kt@altlinux.ru> 8.12.0-alt1
- 8.12.0
- moved sendmail.cf in /etc/mail
- moved aliases in /etc/mail
- fix spec file
- changed /var/spool/mqueue to 700

* Tue Aug 21 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.11.6-alt1
- 8.11.6 (security update).

* Thu Aug 09 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.11.5-alt1
- 8.11.5 (bugfix/security update).

* Thu May 31 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.11.4-alt1
- 8.11.4 (security update).

* Fri Apr  6 2001 Kostya Timoshenko <kt@altlinux.ru> 8.11.3-ipl2mdk
- Added db3 to Requires.

* Thu Mar  1 2001 Kostya Timoshenko <kt@petr.kz> 8.11.3-ipl1mdk
- 8.11.3

* Fri Feb 23 2001 Dmitry V. Levin <ldv@fandra.org> 8.11.2-ipl11mdk
- Moved commonly used sendmail links to sendmail-common package.
- Added sendmail-common to PreReqs.

* Mon Feb 19 2001 Kostya Timoshenko <kt@petr.kz> 8.11.2-ipl10mdk
- add provides MTA

* Thu Feb  8 2001 Kostya Timoshenko <kt@petr.kz> 8.11.2-ipl9mdk
- fix run level in sendmail init script

* Tue Feb  6 2001 Kostya Timoshenko <kt@petr.kz> 8.11.2-ipl8mdk
- Rebuild with db3-3.2.9

* Tue Jan 30 2001 Kostya Timoshenko <kt@petr.kz> 8.11.2-ipl7mdk
- put back sendmail setuid as required by "Brian J. Murrell" <cooker-in@interlinx.bc.ca>

* Wed Jan 17 2001 Kostya Timoshenko <kt@petr.kz> 8.11.2-ipl6mdk
- fix aliases path in cfhead.m4

* Sat Jan 06 2001 Dmitry V. Levin <ldv@fandra.org> 8.11.2-ipl5mdk
- Rebuild with db3-3.2.3e.
- Fixed PreReq tag.
- Minor specfile cleanup and uncompression of patches.

* Wed Jan  3 2001 Kostya Timoshenko <kt@petr.kz>
- 8.11.2
- remove sendmail-8.10.0-smrsh-paths.patch,sendmail-8.10.0-movefiles.patch
- add sendmail-8.11.2-smrsh-paths.patch,sendmail-8.11.2-movefiles.patch

* Tue Jan  2 2001 Kostya Timoshenko <kt@petr.kz>
- adding sendmail-8.11.1-ipl-mdk.patch
- Build for RE

* Tue Nov 14 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 8.11.1-3mdk
- Set sendmail a suid.

* Sat Nov 11 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 8.11.1-2mdk
- QUEUE_LA, REFUSE_LA as 100.

* Sun Oct 29 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 8.11.1-1mdk
- put a new and shiny source in cooker.

* Wed Oct 11 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 8.11.0-4mdk
- provides MailTransportAgent for fetchmail

* Mon Sep  4 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 8.11.0-3mdk
- config-noreplace initscript

* Sat Aug 26 2000 David BAUDENS <baudens@mandrakesoft.com> 8.11.0-2mdk
- Fix bad dependencies on Perl
- %%config(noreplace) /etc/sendmail.cf

* Wed Aug 23 2000 Philippe Libat <philippe@mandrakesoft.com> 8.11.0-1mdk
- version 8.11.0
- replace %%_mandir, %%_initdir

* Fri May 12 2000 Saugey Vincent <vince@mandrakesoft.com> 8.10.1-2mdk
- Fix good directory to use makemap with sendmail installed
- Remove strip of file

* Mon Apr 17 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 8.10.1-1mdk
- updated to 8.10.1
- re-did ppc fixes
- Merged with RedHat:
  remove compatiblity chkconfig links
  break the hard link for makemap and create it as a symlnk (#8223)
  change perms on /etc/sysconfig/sendmail from 0755 to 0644
  allow compressed man-pages
  add patch to prevent the DoS when rebuilding aliases
  Fix location of mailertable (Bug #6035)
  fixes for non-root builds (#8178)
  install man pages, not groff output (#3746).
  use dnl not '#' in m4 comment (#3749).
  add FEATURE(mailtertable) to the config -- example file needs this (#4649).

* Mon Mar 27 2000 Frederic Lepied <flepied@mandrakesoft.com> 8.9.3-22mdk
- fixed install step not to depend on already installed stuff.
- new groups.

* Sun Mar 19 2000 John Buswell <johnb@mandrakesoft.com> 8.9.3-21mdk
- Added PPC fixes

* Wed Jan 12 2000 Philippe Libat <philippe@mandrakesoft.com>
- Add attr to aliases.db in sendmail.spec

* Wed Nov 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Die if lord postfix is present.

* Tue Oct 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge with redhat patch.

* Wed Jul 07 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- more sleep deprivation derived type-o's

* Wed Jul 07 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- sendmail init now checks for postfix

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale
- fix handling of RPM_OPT_FLAGS

* Tue Mar 16 1999 Cristian Gafton <gafton@redhat.com>
- version 8.9.3

* Tue Dec 29 1998 Cristian Gafton <gafton@redhat.com>
- build for 6.0
- use the libdb1 stuff correctly

* Mon Sep 21 1998 Michael K. Johnson <johnsonm@redhat.com>
- Allow empty QUEUE in /etc/sysconfig/sendmail for those who
  want to run sendmail in daemon mode without processing the
  queue regularly.

* Thu Sep 17 1998 Michael K. Johnson <johnsonm@redhat.com>
- /etc/sysconfig/sendmail

* Fri Aug 28 1998 Jeff Johnson <jbj@redhat.com>
- recompile statically linked binary for 5.2/sparc

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- enhanced initscripts

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- added a rmail patch

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- argh!  Fixed some of the db1 handling that had to be added for glibc 2.1

* Fri Oct 24 1997 Donnie Barnes <djb@redhat.com>
- added support for db1 on SPARC

* Thu Oct 16 1997 Donnie Barnes <djb@redhat.com>
- added chkconfig support
- various spec file cleanups
- changed group to Networking/Daemons (from Daemons).  Sure, it runs on
  non networked systems, but who really *needs* it then?

* Wed Oct 08 1997 Donnie Barnes <djb@redhat.com>
- made /etc/mail/deny.db a ghost
- removed preun that used to remove deny.db (ghost handles that now)
- NOTE: upgrading from the sendmail packages in 4.8, 4.8.1, and possibly
  4.9 (all Red Hat betas between 4.2 and 5.0) could cause problems.  You
  may need to do a makemap in /etc/mail and a newaliases after upgrading
  from those packages.  Upgrading from 4.2 or prior should be fine.

* Mon Oct 06 1997 Erik Troan <ewt@redhat.com>
- made aliases.db a ghost

* Tue Sep 23 1997 Donnie Barnes <djb@redhat.com>
- fixed preuninstall script to handle aliases.db on upgrades properly

* Mon Sep 15 1997 Donnie Barnes <djb@redhat.com>
- fixed post-install output and changed /var/spool/mqueue to 755

* Thu Sep 11 1997 Donnie Barnes <djb@redhat.com>
- fixed /usr/lib/sendmail-cf paths

* Tue Sep 09 1997 Donnie Barnes <djb@redhat.com>
- updated to 8.8.7
- added some spam filtration
- combined some makefile patches
- added BuildRoot support

* Wed Sep 03 1997 Erik Troan <ewt@redhat.com>
- marked initscript symlinks as missingok
- run newalises after creating /var/spool/mqueue

* Thu Jun 12 1997 Erik Troan <ewt@redhat.com>
- built against glibc, udated release to -6 (skipped -5!)

* Tue Apr 01 1997 Erik Troan <ewt@redhat.com>
- Added -nsl on the Alpha (for glibc to provide NIS functions).

* Mon Mar 03 1997 Erik Troan <ewt@redhat.com>
- Added nis support.
