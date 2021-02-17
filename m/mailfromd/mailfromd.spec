#%%define %_libexecdir %_sbindir
%define snapshot 1

%define _unpackaged_files_terminate_build 1

Name: mailfromd

%define baseversion 8.9.90

%if %snapshot
%define snapshotdate 20210215
Version: %baseversion
Release: alt0.%snapshotdate.1
%define srcdir %name-%baseversion-%snapshotdate
%else
Version: %baseversion
Release: alt1
%define srcdir %name-%version
%endif

Summary: Universal flexible smtp data supervisor for Sendmail, MeTA1 and Postfix

License: GPL-3.0-or-later
Group: System/Servers
Requires: makemap m4

Url: http://puszcza.gnu.org.ua/projects/mailfromd/
%if %snapshot
Source0:        %name-%baseversion-%snapshotdate.tar.bz2
%else
Source0:        %name-%version.tar.bz2
%endif

Source10: mailfromd.init
Source11: mailfromd.sysconfig
Source12: mailfromd-Makefile
Source13: mailfromd-cron

Source20: mailfromd.mf
Source21: mailfromd-localconf.mf
Source22: mailfromd-userfunctions.mf
Source23: mailfromd.conf
Source24: mailfromd-localtests.mf

Source30: mailfromd-whitelist.main
Source31: mailfromd-sendmail.wl
Source32: mailfromd-shared.wl

Source50: mailfromd-clamav_only.mf

# "not_found" placed to the cache when the MX is not responding
# too. SMTP reply 5xx must not be returned at this case. This
# behavior discovered in 7.99.92 (git 2012-03-21).
# This patch is attempt to disable caching mf_timeout status.
Patch1: mailfromd-savsrv.c-not_cache_mf_timeout.diff

#Errata
#Patch10:

# Automatically added by buildreq on Mon Oct 07 2013
# optimized out: emacs-X11 emacs-base emacs-cedet-speedbar emacs-common fontconfig libX11-locales libgdk-pixbuf libgpg-error libp11-kit libtinfo-devel mailutils pkg-config
BuildRequires: emacs-X11 flex libdb4-devel libgcrypt-devel libgdbm-devel libgnutls-devel libldap-devel libncurses-devel libpam-devel libreadline-devel libtokyocabinet-devel

BuildRequires: libmailutils-devel >= 3.6
BuildRequires: mailutils
BuildRequires: makeinfo
BuildRequires: libadns-devel >= 1.5

%description
Milter-filter for Sendmail v8, MeTA1 and Postfix (since 2.3; please
look documentation of Postfix for checking some limitations).

It provide many verifications at different stages of reception of the
messages, including smtp callback checking, gray listing, regexp checking,
ClamAV and SpamAssassin lookup and other. Nominally it is replacement for
verify_sender, milter-regex, clamav-milter, milter-greylist ang other.

%package cfg_full
Summary: Full featured configuration of mailfromd.
License: GPL-3.0-or-later
Requires: %name = %version-%release
Provides: %name-config
Group: System/Servers
BuildArch: noarch

%description cfg_full
Full featured configuration of mailfromd (can be used with Sendmail since 8.14)

%package cfg_clamav
Summary: clamav-milter replacement configuration.
License: GPL-3.0-or-later
Requires: %name = %version-%release
Provides: %name-config
Group: System/Servers
BuildArch: noarch

%description cfg_clamav
clamav-milter replacement configuration.

%package doc
Summary: Documentation for mailfromd.
License: GFDL-1.2
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation for mailfromd.

%package mfl
Summary: GNU Emacs MFL extention for mailfromd.
License: GPL-3.0-or-later
Requires: emacs-base
Group: System/Servers
BuildArch: noarch

%description mfl
MFL sources are usual ASCII files and you may edit them with any editor
you like.  However, the best choice for this job (as well as for many
others) is, without doubt, GNU Emacs.  To ease the work of editing
script files, the `mailfromd' package provides a special Emacs mode,
called "MFL mode".

%package locales
Summary: National Language files for mailfromd
License: GPL-3.0-or-later
Group: System/Servers
BuildArch: noarch

%description locales
National Language files for mailfromd (Polish and Ukrainian)

%prep

%setup -q -n %srcdir

%patch1 -p1

#Errata
#patch10 -p1

gzip ChangeLog

%build

#autoreconf
#undefine __libtoolize
#libtoolize --ltdl --copy --force

LIBS="-lresolv" \
%configure \
    --sysconfdir=%_sysconfdir/mailfromd \
    --with-berkeley-db \
    --enable-ipv6 \
#   --enable-syslog-async \
    #

./config.status | sed -n '/[*]\+/,/[*]\+/p' > README-build-config

# NO SMP BUILD
%make V=1

%check

%make check

%install

make install DESTDIR=%buildroot
install -d $RPM_BUILD_ROOT%_localstatedir/mailfromd

install -d $RPM_BUILD_ROOT%{_sysconfdir}/{rc.d/init.d,sysconfig,cron.daily}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/mailfromd/{config.d,config.d.shared}

touch $RPM_BUILD_ROOT%_sysconfdir/mailfromd/whitelist
touch $RPM_BUILD_ROOT%_sysconfdir/mailfromd/whitelist.db

sed -e 's|@@CFG_NAME@@|mailfromd|g' < %SOURCE10 > $RPM_BUILD_ROOT%_initdir/mailfromd
chmod 755 $RPM_BUILD_ROOT%_initdir/mailfromd
sed -e 's|@@CFG_NAME@@|mailfromd|g' < %SOURCE11 > $RPM_BUILD_ROOT%_sysconfdir/sysconfig/mailfromd
sed -e 's|@@CFG_NAME@@|mailfromd|g' < %SOURCE13 > $RPM_BUILD_ROOT%_sysconfdir/cron.daily/mailfromd
chmod 744 $RPM_BUILD_ROOT%_sysconfdir/cron.daily/mailfromd

cp -f %SOURCE12 $RPM_BUILD_ROOT%_sysconfdir/mailfromd/Makefile

cp -f %SOURCE20 $RPM_BUILD_ROOT%_sysconfdir/mailfromd/mailfromd.mf
cp -f %SOURCE21 $RPM_BUILD_ROOT%_sysconfdir/mailfromd/localconf.mf
cp -f %SOURCE22 $RPM_BUILD_ROOT%_sysconfdir/mailfromd/userfunctions.mf
cp -f %SOURCE23 $RPM_BUILD_ROOT%_sysconfdir/mailfromd/mailfromd.conf
cp -f %SOURCE24 $RPM_BUILD_ROOT%_sysconfdir/mailfromd/localtests.mf

#rm $RPM_BUILD_ROOT%_libexecdir/mailfromd/postfix-macros.sed
#cp etc/postfix-macros.sed $RPM_BUILD_ROOT%_datadir/mailfromd/postfix-macros.sed

install -m644 %SOURCE30 $RPM_BUILD_ROOT%_sysconfdir/mailfromd/whitelist.main
install -m644 %SOURCE31 $RPM_BUILD_ROOT%_sysconfdir/mailfromd/config.d/sendmail.wl
install -m644 %SOURCE32 $RPM_BUILD_ROOT%_sysconfdir/mailfromd/config.d.shared/shared.wl

%find_lang mailfromd

#
# cfg_clamav
#
install -d $RPM_BUILD_ROOT%_localstatedir/mailfromd-clamav

pushd $RPM_BUILD_ROOT%_sbindir
    ln -s mailfromd mailfromd-clamav
popd

sed -e 's|@@CFG_NAME@@|mailfromd-clamav|g' < %SOURCE10 > $RPM_BUILD_ROOT%_initdir/mailfromd-clamav
chmod 755 $RPM_BUILD_ROOT%_initdir/mailfromd-clamav
sed -e 's|@@CFG_NAME@@|mailfromd-clamav|g' < %SOURCE11 > $RPM_BUILD_ROOT%_sysconfdir/sysconfig/mailfromd-clamav
sed -e 's|@@CFG_NAME@@|mailfromd-clamav|g' < %SOURCE13 > $RPM_BUILD_ROOT%_sysconfdir/cron.daily/mailfromd-clamav
chmod 744 $RPM_BUILD_ROOT%_sysconfdir/cron.daily/mailfromd-clamav

cp -f %SOURCE50 $RPM_BUILD_ROOT%_sysconfdir/mailfromd/mailfromd-clamav.mf

%post

%preun

%post cfg_full
{
    pushd %_sysconfdir/mailfromd
    make
    popd

} &>/dev/null ||:
%post_service mailfromd
rm -f %_localstatedir/mailfromd/*.db &>/dev/null ||:

%preun cfg_full
%preun_service mailfromd

%post cfg_clamav
{
    pushd %_sysconfdir/mailfromd
    make
    popd

} &>/dev/null ||:
%post_service mailfromd-clamav
rm -f %_localstatedir/mailfromd-clamav/*.db &>/dev/null ||:

%preun cfg_clamav
%preun_service mailfromd-clamav

%files
%doc COPYING README* AUTHORS INSTALL NEWS THANKS ChangeLog.gz

%dir %_sysconfdir/mailfromd
%dir %_sysconfdir/mailfromd/config.d
%dir %_sysconfdir/mailfromd/config.d.shared

%config(noreplace) %_sysconfdir/mailfromd/localconf.mf
%config(noreplace) %_sysconfdir/mailfromd/localtests.mf
%config(noreplace) %_sysconfdir/mailfromd/userfunctions.mf
%config(noreplace) %_sysconfdir/mailfromd/Makefile
%config(noreplace) %_sysconfdir/mailfromd/mailfromd.conf

%config(noreplace) %_sysconfdir/mailfromd/whitelist.main
%config %_sysconfdir/mailfromd/config.d/sendmail.wl
%config(noreplace) %_sysconfdir/mailfromd/config.d.shared/shared.wl

%ghost %_sysconfdir/mailfromd/whitelist
%ghost %_sysconfdir/mailfromd/whitelist.db

%_sbindir/mailfromd
%_sbindir/calloutd
%_bindir/mtasim
%_bindir/mfdbtool

%dir %_datadir/mailfromd
%dir %_datadir/mailfromd/%baseversion
%dir %_datadir/mailfromd/%baseversion/include
%_datadir/mailfromd/%baseversion/include/*
%_datadir/mailfromd/postfix-macros.sed

%attr(3775,root,mail) %dir %_localstatedir/mailfromd

%files cfg_full
%attr(0755,root,root) %_initdir/mailfromd

%config(noreplace) %_sysconfdir/mailfromd/mailfromd.mf
%config(noreplace) %_sysconfdir/sysconfig/mailfromd
%config %_sysconfdir/cron.daily/mailfromd

%attr(3775,root,mail) %dir %_localstatedir/mailfromd

%files cfg_clamav
%_sbindir/mailfromd-clamav
%attr(0755,root,root) %_initdir/mailfromd-clamav

%config(noreplace) %_sysconfdir/mailfromd/mailfromd-clamav.mf
%config(noreplace) %_sysconfdir/sysconfig/mailfromd-clamav
%config %_sysconfdir/cron.daily/mailfromd-clamav

%attr(3775,root,mail) %dir %_localstatedir/mailfromd-clamav

%files doc
%_infodir/*

%files mfl
%_datadir/emacs/site-lisp/*

%files locales -f mailfromd.lang

%changelog
* Tue Feb 16 2021 Sergey Y. Afonin <asy@altlinux.org> 8.9.90-alt0.20210215.1
- new version
- changes in mailfromd.mf:
  + increased SpamAssassinStreamMaxLength to 1048576
  + refactored some tests in prog envfrom
  + updated exceptions by "rcpt to" value for working with
    multiple recipients if they have equal exceptions

* Mon Oct 19 2020 Sergey Y. Afonin <asy@altlinux.org> 8.8-alt1
- new version
- changed Copyright tags to License tags, updated their to SPDX syntax
- removed the Packager tag

* Sun Mar 17 2019 Sergey Y. Afonin <asy@altlinux.ru> 8.7-alt3
- changes in mailfromd.mf:
  + implemented delayed check (action in "data" callback)
  + implemented exceptions by "rcpt to" value (for messages with one
    recipient only); available when action in "data" callback
  + reordered some checks
- built without libdspam-devel (disabled dspam support)

* Mon Mar 04 2019 Sergey Y. Afonin <asy@altlinux.ru> 8.7-alt2
- Moved %%doc macro to mailfromd subpackage
- Renamed README-config.status to README-build-config

* Fri Jan 11 2019 Sergey Y. Afonin <asy@altlinux.ru> 8.7-alt1
- new version

* Tue Dec 11 2018 Sergey Y. Afonin <asy@altlinux.ru> 8.6.90-alt0.20181109.1
- new version, disabled errata patches
- packaged report of config.status

* Wed Nov 22 2017 Sergey Y. Afonin <asy@altlinux.ru> 8.4-alt6
- applied upstream's commit b3eb87d520

* Wed Nov 22 2017 Sergey Y. Afonin <asy@altlinux.ru> 8.4-alt5
- applied upstream's commit c659e6efca

* Tue Nov 21 2017 Sergey Y. Afonin <asy@altlinux.ru> 8.4-alt4
- applied upstream's commit 47011c42b5

* Mon Nov 20 2017 Sergey Y. Afonin <asy@altlinux.ru> 8.4-alt3
- applied upstream's commit 59f7cf0f14

* Mon Nov 20 2017 Sergey Y. Afonin <asy@altlinux.ru> 8.4-alt2
- BuildRequires: libadns-devel >= 1.5
- changes in mailfromd.mf:
  + don't compare mx and host's name for mail from:<>

* Mon Nov 13 2017 Sergey Y. Afonin <asy@altlinux.ru> 8.4-alt1
- new version

* Thu Mar 09 2017 Sergey Y. Afonin <asy@altlinux.ru> 8.1-alt2.20170306.1
- new snapshot
- removed mailfromd-mfd-dns.diff (in upstream now)
- updated userfunctions.mf:
   added sa_format_report_header2 function
- changes in mailfromd.mf:
  + used sa_format_report_header2 instead of sa_format_report_header

* Thu Feb 16 2017 Sergey Y. Afonin <asy@altlinux.ru> 8.1-alt2
- BuildRequires: libmailutils-devel >= 3.1.1
- changes in mailfromd.mf:
  + fixed: global variables initialized with "precious" modificator
  + variable's type is used for initializing variables
  + implemented Broken_SPF_reject switch for selecting SPF error handling

* Wed Feb 15 2017 Sergey Y. Afonin <asy@altlinux.ru> 8.1-alt1
- new version
- removed "--remove" option from daemon's command line
- changes in mailfromd.mf:
  + handled TempError for SPF checking
  + added #include </etc/mailfromd/localtests.mf> to prog envfrom
  + improved messages in log and smtp reply

* Sun Feb 05 2017 Sergey Y. Afonin <asy@altlinux.ru> 7.99.94-alt0.20160706.2
- fixed handling of last dot in domain-spec (patch from gray@gnu)
- changes in mailfromd.mf:
  + spamreject variable replaced by SpamScoreRejectLimit
  + added Broken_SPF_Excludes variable

* Sat Jul 09 2016 Sergey Y. Afonin <asy@altlinux.ru> 7.99.94-alt0.20160706.1
- new snapshot
- changes in mailfromd.mf:
  + handled PermError for SPF checking

* Thu Jun 09 2016 Sergey Y. Afonin <asy@altlinux.ru> 7.99.94-alt0.20160426.1
- new snapshot
- changes in mailfromd.mf:
  + reject connections with local hostname in helo
  + graylist and content filter are enabled if level 2 domain of sender's
    PTR is not correspond with level 2 part of sender's helo
  + graylist and content filter are enabled if SPF check passed with +all
  + expanded good CIDR to /23 for SPF check
  + graylist and content filter are enabled if ${client_resolve} is not "OK"
  + some changes in the order of checks

* Tue Dec 01 2015 Sergey Y. Afonin <asy@altlinux.ru> 7.99.94-alt0.20151112.2
- added makeinfo to BuildRequires
  https://lists.altlinux.org/pipermail/devel/2015-November/200445.html

* Thu Nov 12 2015 Sergey Y. Afonin <asy@altlinux.ru> 7.99.94-alt0.20151112.1
- new version
- updated configuration (fixed some errors)

* Mon Oct 07 2013 Sergey Y. Afonin <asy@altlinux.ru> 7.99.92-alt0.20130730.1
- new snapshot
- disabled cacheing result "mf_timeout"
  (mailfromd-savsrv.c-not_cache_mf_timeout.diff)
- changes in mailfromd.mf:
  + removed temporary workaround for cache behavior with "not_found" value

* Wed Jun 13 2012 Sergey Y. Afonin <asy@altlinux.ru> 7.99.92-alt0.20120321.3
- fixed compacting of databases
- changes in mailfromd.mf:
  + temporary workaround for cache behavior with "not_found" value
    (see description in mailfromd.mf)
  + graylist and content filter are disabled if level 2 domain part of MX
    correspond with sender's PTR
  + ignored mechanisms in SPF check:
     +all
     ip4 then CIDR less /24
  + some changes in the order of checks

* Tue Apr 03 2012 Sergey Y. Afonin <asy@altlinux.ru> 7.99.92-alt0.20120321.2
- changes in mailfromd.mf:
  + added SPF check
  + graylist and content filter are disabled if SPF passed
  + reject untidy E-Mail from relays w/o reverse name

* Sat Mar 31 2012 Sergey Y. Afonin <asy@altlinux.ru> 7.99.92-alt0.20120321.1
- new snapshot

* Sat Mar 17 2012 Sergey Y. Afonin <asy@altlinux.ru> 7.99.92-alt0.20120226.1
- new version
- workaround for fix permission of *.db
  (in init file; mfdbtool change it to 644)
- known problem: ipv6 is not enabled when build on git.alt

* Mon Feb 20 2012 Sergey Y. Afonin <asy@altlinux.ru> 7.99.91-alt0.20120208.2
- fixed compacting of databases (function moved from mailfromd to mfdbtool)

* Thu Feb 09 2012 Sergey Y. Afonin <asy@altlinux.ru> 7.99.91-alt0.20120208.1
- new version (fixed ipv6 configuration test)
- regenerated BuildRequires by buildreq
- enabled dspam support
- changes in mailfromd.mf:
  + new syntax for clamav()

* Thu Aug 25 2011 Sergey Y. Afonin <asy@altlinux.ru> 7.99.90-alt0.20110718.2
- changes in mailfromd.conf
  + changed back default socket (to unix, randomly changed since 7.99.90-alt0)

* Wed Jul 27 2011 Sergey Y. Afonin <asy@altlinux.ru> 7.99.90-alt0.20110718.1
- new snapshot
- changes in *.mf:
  + reject a mail if PTR is "localhost"
  + reject a mail if MX is "localhost"

* Sun Jul 03 2011 Sergey Y. Afonin <asy@altlinux.ru> 7.99.90-alt0.20110630.1
- new version (with IPv6 support)

* Fri Jan 21 2011 Sergey Y. Afonin <asy@altlinux.ru> 7.0-alt3
- added escaping for character "%%" in smtp replies
  (mailfromd-7.0-context-percent.diff)
- added smtp timeouts in mailfromd.conf
- changes in *.mf:
  + renamed "good_mx" to "good_relay"
  + excluded "good_relay" from mass allocated checking

* Mon Dec 06 2010 Sergey Y. Afonin <asy@altlinux.ru> 7.0-alt2
- added mailfromd-7.0-rateok.patch

* Sat Nov 13 2010 Sergey Y. Afonin <asy@altlinux.ru> 7.0-alt1
- new version (warning: v7.0 can't run with default configuration of
  5.9.91-alt0.20091119.7, some pragmas unsupported now)
- renamed *.rc to *.mf
- changes in *.mf:
  + removed unsupported pragmas
  + fixed deprecated syntax

* Wed Oct 20 2010 Sergey Y. Afonin <asy@altlinux.ru> 5.9.91-alt0.20091119.7
- added checking "auth_authen" macro (messages from authenticated senders
  will accepted without any tests exept connect and helo stages)

* Tue Aug 17 2010 Sergey Y. Afonin <asy@altlinux.ru> 5.9.91-alt0.20091119.6
- fixed name clashes with the existing variables (MF_VAR_SET_STRING.patch)

* Fri May 07 2010 Sergey Y. Afonin <asy@altlinux.ru> 5.9.91-alt0.20091119.5
- changes in mailfromd.rc:
  + added %%ClamdStreamMaxLength (resolved problem with access to clamd)
  + added %%SpamAssassinStreamMaxLength
  + updated %%good_mx
  + changed global while list checking (used whitelist_chk_global)
- changes in userfunctions.rc:
  + new function: whitelist_chk_global

* Fri Dec 25 2009 Sergey Y. Afonin <asy@altlinux.ru> 5.9.91-alt0.20091119.4
- removed runlevels list from start/stop sections of lsb init header
  in init-script

* Sat Dec 19 2009 Sergey Y. Afonin <asy@altlinux.ru> 5.9.91-alt0.20091119.3
- changes in mailfromd.rc:
  + rewrote error messages for smtp reply

* Mon Dec 14 2009 Sergey Y. Afonin <asy@altlinux.ru> 5.9.91-alt0.20091119.2
- changes in mailfromd.rc:
  + disabled graylist by default in all cases (%%usegraylist variable)
  + optimized checking for enabling graylist in "prog envrcpt"

* Sun Nov 22 2009 Sergey Y. Afonin <asy@altlinux.ru> 5.9.91-alt0.20091119.1
- new snapshot

* Fri Nov 06 2009 Sergey Y. Afonin <asy@altlinux.ru> 5.9.90-alt0.20091105.1
- new snapshot
  + changes in mailfromd.rc:
  + corrected syntax mailfromd.rc in accordance with the current changes
    in language

* Tue Oct 20 2009 Sergey Y. Afonin <asy@altlinux.ru> 5.9.90-alt0.20091009.1
- new snapshot
- changed flex-old to flex in BuildRequires
- added %%check section
- removed %%__ macroses

* Tue Sep 29 2009 Sergey Y. Afonin <asy@altlinux.ru> 5.2.90-alt0.20090928.1
- new snapshot

* Fri Aug 28 2009 Sergey Y. Afonin <asy@altlinux.ru> 5.2-alt0.20090828.1
- new version
- removed %name-config from Requires

* Tue Jul 14 2009 Sergey Y. Afonin <asy@altlinux.ru> 5.1.91-alt0.20090714.1
- new snapshot

* Fri May 22 2009 Sergey Y. Afonin <asy@altlinux.ru> 5.1-alt1
- new version

* Mon May 04 2009 Sergey Y. Afonin <asy@altlinux.ru> 5.0.92-alt0.20090503.1
- new snapshot

* Mon Apr 20 2009 Sergey Y. Afonin <asy@altlinux.ru> 5.0.92-alt0.20090419.1
- new snapshot

* Mon Apr 06 2009 Sergey Y. Afonin <asy@altlinux.ru> 5.0.90-alt0.20090320.3
- changes in mailfromd.rc and localconf.rc
  + renamed spamcheckactive to spam_verification_needed
  + updated massallocated_regexps
  + updated good_mx
  + better logging graylisted reason

* Fri Apr 03 2009 Sergey Y. Afonin <asy@altlinux.ru> 5.0.90-alt0.20090320.2
- fixed: remove last dot in `hostname' output if it there
  (/etc/sysconfig/mailfromd)

* Fri Mar 20 2009 Sergey Y. Afonin <asy@altlinux.ru> 5.0.90-alt0.20090320.1
- new snapshot
- changes in mailfromd.rc
  + ignoring smtp callback if mx matches %%not_verifiable_mx and message graylisted.

* Thu Mar 12 2009 Sergey Y. Afonin <asy@altlinux.ru> 5.0.90-alt0.20090311.1
- new snapshot
- changes in mailfromd.rc
  + fixed: added variables for SA support to mailfromd.rc

* Wed Nov 12 2008 Sergey Y. Afonin <asy@altlinux.ru> 4.9.96-alt0.20081111.1
- new svn
- changes in mailfromd.rc
  + added "tolower" call for *.db lookup
  + added partial lookup access.db of sendmail (see %%mta in rc)
    configuration for spamd (Spamassassin)

* Thu Oct 16 2008 Sergey Y. Afonin <asy@altlinux.ru> 4.9.95-alt0.20081016.1
- new svn
- moved %%configure to %%build (thanks to Led for point this)
- changed emacs-X11 to emacs-nox in BuildRequires (thanks to Led for point this)
- added %%install_info/%%uninstall_info to doc package

* Mon Sep 22 2008 Sergey Y. Afonin <asy@altlinux.ru> 4.9.93-alt1.20080920.1
- new svn

* Wed Jul 16 2008 Sergey Y. Afonin <asy@altlinux.ru> 4.9.92-alt1.20080704.1
- new svn
- changes in mailfromd.rc
  + added check for bad "mail from" (%%bad_mail_from = ".*\\|.*" by default)

* Sat May 31 2008 Sergey Y. Afonin <asy@altlinux.ru> 4.9.92-alt1.20080516.2
- changes in mailfromd.rc
  + added callback_chk_exclude list
  + added graylist_exclude list
  + changed gltime interval to 25 minutes

* Thu May 22 2008 Sergey Y. Afonin <asy@altlinux.ru> 4.9.92-alt1.20080516.1
- fixed: removal *.db is restored in mailfromd's localstatedir in %%post of cfg_*
- changes in mailfromd.rc
  + rewrote log_header_line: behavior of substring() was changed in mainstream

* Sat May 17 2008 Sergey Y. Afonin <asy@altlinux.ru> 4.9.92-alt1.20080516
- new svn
- changed %%make_build to %%make in spec (a problem with SMP build since branch 4.1)

* Thu Apr 10 2008 Sergey Y. Afonin <asy@altlinux.ru> 4.9.92-alt1.20080408
- new svn (see "Upgrading from 4.4 to 5.0")

* Tue Mar 11 2008 Sergey Y. Afonin <asy@altlinux.ru> 4.4-alt1
- new version

* Tue Mar 04 2008 Sergey Y. Afonin <asy@altlinux.ru> 4.3.1-alt1
- new version

* Wed Feb 20 2008 Sergey Y. Afonin <asy@altlinux.ru> 4.2-alt1
- new version

* Fri Sep 21 2007 Sergey Y. Afonin <asy@altlinux.ru> 4.1.1-alt3.svn20070810
- fixed #12864 (problem in reload section of init script)

* Thu Aug 16 2007 Sergey Y. Afonin <asy@altlinux.ru> 4.1.1-alt2.svn20070810
- added m4 to Requires

* Sat Aug 11 2007 Sergey Y. Afonin <asy@altlinux.ru> 4.1.1-alt1.svn20070810
- new version, Relicense everything under the GPLv3

* Tue May 29 2007 Sergey Y. Afonin <asy@altlinux.ru> 4.0-alt2
- added "-C /dev/null" in calling of   makemap in Makefile
- correcded reply when last_poll_recv = "nothing"

* Sat May 12 2007 Sergey Y. Afonin <asy@altlinux.ru> 4.0-alt1
- new version
- changes in mailfromd.rc
  + default value for graylist_exclude set to "\n"

* Thu May 10 2007 Sergey Y. Afonin <asy@altlinux.ru> 3.1.92-alt0.20070510
- new svn
- added makemap to Requires

* Wed May 09 2007 Sergey Y. Afonin <asy@altlinux.ru> 3.1.92-alt0.20070508
- new svn
- created some different configurations (%name-cfg_clamav, %name-cfg_full)
- fixed: removing %_localstatedir/*.db instead of compacting in %%post (#11666)
- changes in mailfromd.rc 
  + reply changed for "when not_found"
  + some functions moved to userfunctions.rc
  + common witelist
  + fixed: ${client_addr} -> ${client_ptr} in massallocated_hit call

* Mon Apr 02 2007 Sergey Y. Afonin <asy@altlinux.ru> 3.1.91-alt0.20070403
- new svn, uncompatible changes since alt0.20070322:
  need to replace all occurrences of `next' with `pass'
- added executing "mailfromd --compact --all" in %%post and in %_sysconfdir/cron.daily
- changes in %_sysconfdir/sysconfig/mailfromd:
  moved definitions of variable to /etc/mailfromd/localconf.rc
- changes in localconf.rc
  + added \#pragma option port
  + added clamd_port
  + added massallocated_regexps
  + renamed "trusted_networks" to "massallocated_chk_exclude"
  + changed value of \#pragma stacksize to 16383 (resizable stack now)
  + changed format of massallocated_chk_exclude
- changes in mailfromd.rc 
  + all which correspond to localconf.rc
  + common white list (changes is not compatible with previous white lists)
  + ${client_addr} used in prog helo, you must update Milter.macros.helo in sendmail.cf

* Thu Mar 22 2007 Sergey Y. Afonin <asy@altlinux.ru> 3.1.91-alt0.20070322
- new svn
  (see documentation for checking uncompatible changes in mailfromd.rc
  "Upgrading from 3.1.x to 3.2" section)
- updated Summary
- changes in mailfromd.rc:
  + converted to 3.2 format
  + moved all host specific definitions to %_sysconfdir/sysconfig/mailfromd
  + added "catch failure" for message_header_decode in "prog header"
- changes in %_sysconfdir/sysconfig/mailfromd:
  + added -v ehlo_domain=`hostname`
  + added -v virusmaster="admvirus@localhost"
  + added -v explain_msg=''
  + added -v trusted_networks="127.0.0.0/8,192.168.0.0/16,172.16.0.0/12,10.0.0.0/8"

* Thu Mar 15 2007 Sergey Y. Afonin <asy@altlinux.ru> 3.1.4-alt1
- new version
- changed Summary
- changes in mailfromd.rc:
  + \#pragma stacksize 65535 (for "prog header")
  + connect to clamd via local socket

* Thu Jan 11 2007 Sergey Y. Afonin <asy@altlinux.ru> 3.1.2-alt2
- fixed: Makefile missed in %%files
- added: *.db generation in %%post

* Wed Jan 10 2007 Sergey Y. Afonin <asy@altlinux.ru> 3.1.2-alt1
- new version
- changed: flex to flex-old in BuildRequires (removed mailfromd-flex2.5.4a-to-flex2.5.33.patch)
- added: /etc/maildromd/Makefile
- added: /etc/maildromd/{lists.d,lists.d.shared}
- added: /etc/maildromd/{whitelist_graylist,whitelist_massalocated}
- added: mailfromd-message_header_code.patch (from CVS)
  (message_header_decode and message_header_encode support)
- changes in mailfromd.rc:
  added graylist section
  some modifications in "prog envfrom"

* Wed Dec 13 2006 Sergey Y. Afonin <asy@altlinux.ru> 3.1.1-alt1
- new version
  (see documentation for checking uncompatible changes in mailfromd.rc)
- changed: moved configuration files from /etc/mail to /etc/mailfromd
- changed: replaced orgiginal mailfromd.rc
- changed: version is not necessary now in --with-berkeley-db=4
- changes in mailfromd.rc:
  + added variables for using in templates:
    msg_header
    msg_header_last_received
    infected_received_from
    mail_from
    rcpt_to
    queue_id
  + modified regular expressions for detection mass allocated networks
  + added ClamAV section (mailutils-1.0-alt4 or latest required)

* Tue Nov 07 2006 Sergey Y. Afonin <asy@altlinux.ru> 3.0-alt1
- new version
- added: mailfromd-flex2.5.4a-to-flex2.5.33.patch
- changed: description and summary

* Thu Oct 05 2006 Sergey Y. Afonin <asy@altlinux.ru> 2.0.1-alt2
- fixed: change LDFLAGS="-lresolv" to export LIBS="-lresolv" (for x86_64 build)

* Fri Sep 22 2006 Sergey Y. Afonin <asy@altlinux.ru> 2.0.1-alt1
- new version
- changed: added --with-berkeley-db=4
- added: post_service and preun_service

* Fri Sep 22 2006 Sergey Y. Afonin <asy@altlinux.ru> 2.0-alt1
- New version

* Thu Aug 03 2006 Sergey Y. Afonin <asy@altlinux.ru> 1.4-alt2
- fixed: add LDFLAGS="-lresolv" (it is not added automatically on x86_64)

* Sat Jan 21 2006 Sergey Y. Afonin <asy@altlinux.ru> 1.4-alt1
- Initial release for AltLinux
