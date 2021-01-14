Name: vixie-cron
Version: 4.1.20060426
Release: alt10.2

%def_with selinux

Summary: The Vixie cron daemon for executing specified programs at set times
License: BSD-style
Group: System/Servers
Url: http://git.altlinux.org/people/ldv/packages/vixie-cron.git

Source0: vixie-cron-%version.tar
Source1: crond.init
Source2: crontab.template
Source3: crond.pamd
Source4: crond.limits
Source5: crond.service

Provides: %_sysconfdir/cron.d, at = %version-%release
Obsoletes: at

PreReq: crontab-control
Requires: vitmp

Patch1:  vixie-cron-4.1.20060426-alt-warnings.patch
Patch2:  vixie-cron-4.1.20060426-owl-alt-linux.patch
Patch3:  vixie-cron-4.1.20040916-owl-vitmp.patch
Patch4:  vixie-cron-4.1.20040916-owl-crond.patch
Patch5:  vixie-cron-4.1.20060426-owl-st_nlink.patch
Patch6:  vixie-cron-4.1.20040916-alt-makefile.patch
Patch7:  vixie-cron-4.1.20040916-alt-progname.patch
Patch8:  vixie-cron-4.1.20040916-alt-crontab-template.patch
Patch9:  vixie-cron-4.1.20040916-alt-sigpipe.patch
Patch10: vixie-cron-4.1.20040916-alt-pam.patch
Patch11: vixie-cron-4.1.20040916-alt-setlocale.patch
Patch12: vixie-cron-4.1.20040916-alt-children.patch
Patch13: vixie-cron-4.1.20060426-owl-tmp.patch
Patch14: vixie-cron-4.1.20040916-alt-setproctitle.patch
Patch15: vixie-cron-4.1.20060426-alt-crontab-list.patch
Patch16: vixie-cron-4.1.20060426-alt-path.patch
Patch17: vixie-cron-4.1.20060426-alt-selinux.patch

BuildRequires: libpam-devel, setproctitle-devel
%{?_with_selinux:BuildRequires: libselinux-devel}

%description
cron is a daemon that runs specified programs at scheduled times.  This
package contains Paul Vixie's implementation of cron, with significant
modifications by the NetBSD, OpenBSD, Red Hat, Owl and ALT teams.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%{?_with_selinux:%patch17 -p1}

sed -i 's/^\(static char const rcsid\[\] =\).*/\1 "%name-%version-%release";/' \
	usr.sbin/cron/crontab.c
find -type f -name \*.orig -delete

%build
for i in usr.sbin/cron usr.bin/crontab usr.bin/at; do
%make_build .CURDIR=. -C "$i"
done

%install
mkdir -p %buildroot{%_sysconfdir/cron.d,/var/spool/{cron,at}}

for i in usr.sbin/cron usr.bin/crontab usr.bin/at; do
%makeinstall_std .CURDIR=. -C "$i"
done

for i in atq atrm batch; do
	ln -s at %buildroot%_bindir/$i
done

ln -s at.1 %buildroot%_man1dir/batch.1
ln -s cron.8 %buildroot%_man8dir/crond.8

install -pD -m755 %_sourcedir/crond.init \
	%buildroot%_initdir/crond
install -pD -m644 %_sourcedir/crond.service \
	%buildroot%systemd_unitdir/crond.service
install -pD -m644 %_sourcedir/crontab.template \
	%buildroot%_sysconfdir/crontab.template
install -pD -m600 %_sourcedir/crond.pamd \
	%buildroot%_sysconfdir/pam.d/crond
install -pD -m644 %_sourcedir/crond.limits \
	%buildroot%_sysconfdir/sysconfig/limits.d/crond

touch %buildroot%_sysconfdir/{at,cron}.{allow,deny}

%pre
%pre_control crontab at

%post
%post_control crontab at
%post_service crond

%preun
%preun_service crond

%files
%_sbindir/*
%attr(700,root,root) %_bindir/at
%attr(700,root,root) %_bindir/crontab
%_bindir/atq
%_bindir/atrm
%_bindir/batch
%_mandir/man?/*
%config %_initdir/crond
%systemd_unitdir/crond.service
%attr(640,root,crontab) %ghost %_sysconfdir/at.allow
%attr(640,root,crontab) %ghost %_sysconfdir/cron.allow
%attr(640,root,crontab) %config(noreplace) %_sysconfdir/at.deny
%attr(640,root,crontab) %config(noreplace) %_sysconfdir/cron.deny
%config(noreplace) %_sysconfdir/crontab.template
%config(noreplace) %_sysconfdir/pam.d/crond
%config(noreplace) %_sysconfdir/sysconfig/limits.d/crond
%attr(1770,root,crontab) %dir /var/spool/at
%attr(3730,root,crontab) %dir /var/spool/cron
%attr(700,root,root) %dir %_sysconfdir/cron.d

%changelog
* Mon Aug 03 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.20060426-alt10.2
- NMU: fixed build with new selinux.

* Sun Apr 01 2018 Igor Vlasenko <viy@altlinux.ru> 4.1.20060426-alt10.1
- NMU: added URL

* Thu May 19 2016 Dmitry V. Levin <ldv@altlinux.org> 4.1.20060426-alt10
- crond.service: fixed race condition that affected user crontabs
  (closes: #32095).

* Tue Sep 20 2011 Dmitry V. Levin <ldv@altlinux.org> 4.1.20060426-alt9
- Fixed uninitialized pointer bug in case when SELinux is not enabled
  (by Sergey Vlasov; closes: #26285).

* Thu Jul 07 2011 Dmitry V. Levin <ldv@altlinux.org> 4.1.20060426-alt8
- Added SELinux support (by Mikhail Efremov).
- crond: added systemd support (by Alexey Shabalin; closes: #25463).
- crond: changed default $PATH to something reasonable (closes: #25846).

* Wed Jun 23 2010 Dmitry V. Levin <ldv@altlinux.org> 4.1.20060426-alt7
- /etc/pam.d/crond: Changed to use common-login.

* Tue Apr 07 2009 Dmitry V. Levin <ldv@altlinux.org> 4.1.20060426-alt6
- Added pam_loginuid.so to the head of PAM session stack.

* Thu Nov 13 2008 Dmitry V. Levin <ldv@altlinux.org> 4.1.20060426-alt5
- Added config file for limited(8).

* Sun May 04 2008 Dmitry V. Levin <ldv@altlinux.org> 4.1.20060426-alt4
- crontab: Skip the top few comments in "list" mode,
  based on patch from Slava Semushin (#14751).

* Wed Apr 11 2007 Dmitry V. Levin <ldv@altlinux.org> 4.1.20060426-alt3
- Corrected License tag.

* Wed Mar 28 2007 Dmitry V. Levin <ldv@altlinux.org> 4.1.20060426-alt2
- Hardened /etc/cron.d access permissions to 0700.
- Hardened /etc/pam.d/crond access permissions to 0600.
- Hardened system crontab files access permissions check to
  "st_mode & 07533 == 0400".
- Hardened spool crontab files access permissions check to
  "st_mode & 07577 == 0400".
- Restricted link count check to spool crontab files.

* Mon May 01 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.20060426-alt1
- Updated to OpenBSD CVS snapshot dated 2006/04/26.
- Changed crontab to use $TMPDIR for creating temporary file.

* Mon Mar 06 2006 Dmitry V. Levin <ldv@altlinux.org> 4.1.20040916-alt3
- Fixed build with --as-needed.

* Thu Jan 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 4.1.20040916-alt2.1
- Rebuilt for new style PAM dependencies generated by rpm-build-4.0.4-alt55.

* Sat Dec 18 2004 Dmitry V. Levin <ldv@altlinux.org> 4.1.20040916-alt2
- Applied few corrections to owl-alt-linux and owl-crond patches,
  as suggested by Jarno Huuskonen.
- Fixed children handling in crond.
- Enabled setproctitle.

* Wed Nov 03 2004 Dmitry V. Levin <ldv@altlinux.org> 4.1.20040916-alt1
- Updated to OpenBSD snapshot 200409162011, based on ISC Cron V4.1.
- Updated patches.

* Sat Jun 12 2004 Dmitry V. Levin <ldv@altlinux.org> 4.0.b1.20040604-alt2
- crond, crontab: do not call setlocale(3).

* Mon Jun 07 2004 Dmitry V. Levin <ldv@altlinux.org> 4.0.b1.20040604-alt1
- Updated to OpenBSD snapshot 20040604, with all
  non-linux-specific fixes applied.
- Updated patches.

* Mon May 31 2004 Dmitry V. Levin <ldv@altlinux.org> 4.0b1-alt3
- Restore default action for SIGPIPE and SIGUSR1 right before
  user scripts execution.
- PAMified crond.

* Fri May 28 2004 Dmitry V. Levin <ldv@altlinux.org> 4.0b1-alt2
- Fixed bugs found since -alt1 release.

* Thu May 27 2004 Stanislav Ievlev <inger@altlinux.org> 4.0b1-alt1
- Updated to vixie-cron-4.0b1 with patches from OpenBSD-3.5 and Owl,
  which also provides "at" functionality.
- Applied patch from Jarno Huuskonen (Owl) for cleaner build on linux.
- Updated ALT patches.
- Keep "crontab" and "at" at mode "restricted" in the package, but
  default it to "public" in %%post when the package is first installed.
  This avoids a race and fail-open behaviour.
- Moved control files to separate subpackage.

* Fri Apr 25 2003 Dmitry V. Levin <ldv@altlinux.org> 3.0.1-ipl57mdk
- Daemonize properly (#0002546).
- Clear environment at startup.
- Use proper default PATH value.
- Rewritten start/stop script to new rc scheme.

* Mon Nov 18 2002 Dmitry V. Levin <ldv@altlinux.org> 3.0.1-ipl56mdk
- crontab: added /etc/crontab.template support.

* Sun Oct 13 2002 Dmitry V. Levin <ldv@altlinux.org> 3.0.1-ipl55mdk
- Rediffed our unified patch.
- Compiled with -DLINT, to ignore rcsid[] stuff.
- Added control support for crontab.

* Wed Sep 25 2002 Dmitry V. Levin <ldv@altlinux.org> 3.0.1-ipl54mdk
- Provides: %_sysconfdir/cron.d

* Fri May 17 2002 Dmitry V. Levin <ldv@altlinux.org> 3.0.1-ipl53mdk
- Ensure all files are closed in crontab(1) when the editor is run.
- Set default crontab(1) editor to vitmp(1).

* Thu May 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.0.1-ipl52mdk
- Use service macros.
- Fixed tmp files handling in crontab.

* Wed May 16 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.0.1-ipl51mdk
- Made unified patch.
- Added shadow-utils to prereqs.
- Skip junk files from /var/spool/cron and %_sysconfdir/cron.d

* Mon May 14 2001 Stanislav Ievlev <inger@altlinux.ru> 3.0.1-ipl50mdk
- Add new patches from MDK and Owl.

* Fri Feb 23 2001 Dmitry V. Levin <ldv@fandra.org> 3.0.1-ipl49mdk
- Fixed build with glibc-2.2.2

* Wed Feb 14 2001 Dmitry V. Levin <ldv@fandra.org> 3.0.1-ipl48mdk
- Fixed some strcpy calls.

* Mon Feb 12 2001 Dmitry V. Levin <ldv@fandra.org> 3.0.1-ipl47mdk
- Enhanced error reporting.
- Account for shifts in system clock (rh).

* Wed Dec 27 2000 Dmitry V. Levin <ldv@fandra.org> 3.0.1-ipl46mdk
- Added PreReq on initscripts.

* Thu Sep 14 2000 Dmitry V. Levin <ldv@fandra.org> 3.0.1-ipl45mdk
- RE adaptions.

* Tue Sep 12 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.0.1-45mdk
- force crond to use syslog.

* Mon Aug 21 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 3.0.1-44mdk
- Macro's
- BM
- /etc/rc.d/init.d --> /etc/init.d
- Geoff <snailtalk@mandrakesoft.com> no we actually use _initrddir ..

* Mon Jul 17 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.0.1-43mdk
- remove useless man-pages compression and let spec-helper work

* Sat Jul 15 2000 Stefan van der Eijk <s.vandereijk@chello.nl>
- changed way manpages are compressed, use find instead of for

* Mon Apr 10 2000 Christopher Molnar <molnarc@mandrakesoft.com> 3.0.1-42mdk
- Fixed group

* Sun Mar 19 2000 John Buswell <johnb@mandrakesoft.com> 3.0.1-41mdk
- Added PPC patches

* Tue Jan 11 2000 Pixel <pixel@linux-mandrake.com>
- non root build

* Tue Oct 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Move some to from %postun to %preun.
- Merge with redhat patchs.

* Thu Apr 29 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Mandrake adaptations.

* Wed Apr 14 1999 Michael K. Johnson <johnsonm@redhat.com>
- add note to man page about DST conversion causing strangeness
- documented cron.d patch

* Tue Apr 13 1999 Michael K. Johnson <johnsonm@redhat.com>
- improved cron.d patch

* Mon Apr 12 1999 Erik Troan <ewt@redhat.com>
- added cron.d patch

* Tue Mar 23 1999 Bill Nottingham <notting@redhat.com>
- logrotate changes

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- clean up log files on deinstallation

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 28)

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Wed Jun 10 1998 Jeff Johnson <jbj@redhat.com>
- reset SIGCHLD before grandchild execle (problem #732)

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- enhanced initscript

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Dec 11 1997 Cristian Gafton <gafton@redhat.com>
- added a patch to get rid of the dangerous sprintf() calls
- added BuildRoot and Prereq: /sbin/chkconfig

* Sun Nov 09 1997 Michael K. Johnson <johnsonm@redhat.com>
- fixed cron/crond dichotomy in init file.

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- fixed bad init symlinks

* Thu Oct 23 1997 Erik Troan <ewt@redhat.com>
- force it to use SIGCHLD instead of defunct SIGCLD

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- updated for chkconfig
- added status, restart options to init script

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Wed Feb 19 1997 Erik Troan <ewt@redhat.com>
- Switch conditional from "axp" to "alpha"

