%define _unpackaged_files_terminate_build 1
%set_verify_elf_method strict

%define dbdir %_localstatedir/%name

Name: dhcpcd
Epoch: 1
Version: 8.1.5
Release: alt1

Summary: DHCP Client
License: BSD-2-Clause
Group: System/Servers

URL: https://roy.marples.name/projects/%name
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

AutoReq: yes, noshell

Conflicts: etcnet < 0.9.10-alt6

# NetworkManager can use dhcpcd
Provides: nm-dhcp-client


%description
dhcpcd is an implementation of the DHCP client specified in RFC2131.

It gets the host information (IP address, netmask, broadcast address, etc.)
from a DHCP server and configures the network interface of the machine on
which it is running. It also tries to renew the lease time according to RFC2131.

%prep
%setup -q
%patch0 -p1

%build
%add_optflags -fpie
export LDFLAGS=-pie
%configure \
        --sbindir=/sbin \
        --rundir=/var/run \
        --libexecdir=/lib/%name \
        --dbdir=%dbdir \
        --serviceexists='[ -x %_initdir/"$1" ]' \
        --servicecmd='/sbin/service "$1" >/dev/null 2>&1' \
        --with-hook=ntp.conf \
        --with-hook=lookup-hostname \
        --enable-ipv4 \
        --enable-ipv6 \
		--enable-dhcp6 \
		--enable-auth \
		--enable-ipv4ll \
        --without-udev
%make_build

%install
%makeinstall_std BINMODE=0755

# These files changed their name/location since 7.0.0.
# Don't move lease files, they can be used and often removed when dhcpcd
# is exited.
%triggerpostun -- %name < 1:7.0.0
for f in duid secret; do
	if [ -e %_sysconfdir/dhcpcd.$f ] && [ ! -e %dbdir/$f ]; then
		echo "%_sysconfdir/dhcpcd.$f found, moving to %dbdir/$f"
		mv "%_sysconfdir/dhcpcd.$f" "%dbdir/$f"
	fi
done
if [ ! -e %dbdir/rdm_monotonic ] && [ -e %dbdir/dhcpcd-rdm.monotonic ]; then
	mv %dbdir/dhcpcd-rdm.monotonic %dbdir/rdm_monotonic
fi

%files
/sbin/*
%_man8dir/*
%_man5dir/*
%config(noreplace) %_sysconfdir/%name.conf
%dir %_localstatedir/%name
%dir /lib/%name
%dir /lib/%name/%name-hooks
/lib/%name/%name-hooks/*
/lib/%name/%name-run-hooks

# Ingnore all additional hooks:
#   wpa_supplicant: wpa_supplicant should be handled by etcnet
#   tzupdate: it should use tzupdate but what about configuration files?
%exclude %_datadir/%name/

%changelog
* Thu Jan 09 2020 Mikhail Efremov <sem@altlinux.org> 1:8.1.5-alt1
- Updated to 8.1.5.

* Mon Dec 23 2019 Mikhail Efremov <sem@altlinux.org> 1:8.1.4-alt1
- Fixed license.
- Updated to 8.1.4.

* Thu Nov 14 2019 Mikhail Efremov <sem@altlinux.org> 1:8.1.2-alt1
- Drop obsoleted patch.
- Updated to 8.1.2.

* Tue Nov 12 2019 Mikhail Efremov <sem@altlinux.org> 1:8.1.1-alt2
- Patch drom upstream:
  + INET: Fix corruption of IPv4 address flags when renewing.

* Tue Oct 22 2019 Mikhail Efremov <sem@altlinux.org> 1:8.1.1-alt1
- Drop "Don't use BSD semantics for UDP." patch.
- Drop obsoleted patch.
- Updated to 8.1.1.

* Fri Sep 13 2019 Mikhail Efremov <sem@altlinux.org> 1:8.0.6-alt1
- Updated to 8.0.6.

* Wed Sep 04 2019 Mikhail Efremov <sem@altlinux.org> 1:8.0.4-alt1
- Updated to 8.0.4.

* Thu Aug 22 2019 Mikhail Efremov <sem@altlinux.org> 1:8.0.3-alt1
- Updated to 8.0.3.

* Thu Aug 15 2019 Mikhail Efremov <sem@altlinux.org> 1:8.0.2-alt1
- Updated to 8.0.2.

* Wed Jul 03 2019 Mikhail Efremov <sem@altlinux.org> 1:7.2.3-alt1
- Updated url.
- Updated to 7.2.3.

* Tue May 14 2019 Mikhail Efremov <sem@altlinux.org> 1:7.2.2-alt1
- Drop obsoleted patch.
- Updated to 7.2.2.

* Mon Apr 29 2019 Mikhail Efremov <sem@altlinux.org> 1:7.2.1-alt1
- Patch drom upstream:
  + Fix BPF buffer overflow.
- Drop obsoleted patches.
- Updated to 7.2.1.

* Tue Apr 23 2019 Mikhail Efremov <sem@altlinux.org> 1:7.2.0-alt2
- Patches from upstream git.

* Thu Apr 18 2019 Mikhail Efremov <sem@altlinux.org> 1:7.2.0-alt1
- Updated to 7.2.0.

* Fri Feb 08 2019 Mikhail Efremov <sem@altlinux.org> 1:7.1.1-alt1
- Updated to 7.1.1.

* Tue Jan 22 2019 Mikhail Efremov <sem@altlinux.org> 1:7.1.0-alt1
- resolv.conf hook: Initialize more local variables.
- Updated to 7.1.0.

* Thu Jul 26 2018 Mikhail Efremov <sem@altlinux.org> 1:7.0.7-alt1
- Updated to 7.0.7.

* Fri Jun 22 2018 Mikhail Efremov <sem@altlinux.org> 1:7.0.6-alt1
- Drop obsoleted patch.
- Updated to 7.0.6.

* Fri Jun 15 2018 Mikhail Efremov <sem@altlinux.org> 1:7.0.5b-alt2
- Don't ignore carrier loss on IPv4 addresses.

* Wed Jun 13 2018 Mikhail Efremov <sem@altlinux.org> 1:7.0.5b-alt1
- Updated to 7.0.5b.

* Thu May 03 2018 Mikhail Efremov <sem@altlinux.org> 1:7.0.4-alt1
- Updated to 7.0.4.

* Fri Apr 06 2018 Mikhail Efremov <sem@altlinux.org> 1:7.0.3-alt1
- Updated to 7.0.3.

* Tue Mar 27 2018 Mikhail Efremov <sem@altlinux.org> 1:7.0.2-alt1
- Drop obsoleted patch.
- Updated to 7.0.2.

* Mon Jan 29 2018 Mikhail Efremov <sem@altlinux.org> 1:7.0.1-alt1
- Drop obsoleted patches.
- Use local variables in scripts.
- Updated to 7.0.1.

* Thu Jan 25 2018 Mikhail Efremov <sem@altlinux.org> 1:7.0.0-alt2
- Drop trigger for updating dhcpcd from version < 5.0.0.
- Don't disable kernel RA if IPv6 in the dhcpcd is disabled
  (closes: #34472).
- Don't use netlink's IFA_FLAGS on kernels that doesn't support them.

* Fri Jan 12 2018 Mikhail Efremov <sem@altlinux.org> 1:7.0.0-alt1
- During update move files to new location.
- Add patches from upstream git.
- Enable ntp_servers option again.
- Build with -pie.
- Fix build with make-3.x.
- Updated to 7.0.0.

* Mon Oct 10 2016 Mikhail Efremov <sem@altlinux.org> 1:6.11.5-alt1
- Updated to 6.11.5.

* Mon Aug 22 2016 Mikhail Efremov <sem@altlinux.org> 1:6.11.3-alt1
- Updated to 6.11.3.

* Mon Aug 01 2016 Mikhail Efremov <sem@altlinux.org> 1:6.11.2-alt1
- Fix License.
- Updated to 6.11.2.

* Mon Jun 20 2016 Mikhail Efremov <sem@altlinux.org> 1:6.11.1-alt1
- Drop obsoleted patch.
- Updated to 6.11.1.

* Sat Jun 04 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:6.11.0-alt2
- Patch from upstream:
  + Handle truncated DHCP messages.

* Tue May 10 2016 Mikhail Efremov <sem@altlinux.org> 1:6.11.0-alt1
- Updated to 6.11.0.

* Thu Apr 21 2016 Mikhail Efremov <sem@altlinux.org> 1:6.10.3-alt1
- Drop obsoleted patches.
- Updated to 6.10.3.

* Mon Jan 25 2016 Mikhail Efremov <sem@altlinux.org> 1:6.10.1-alt1
- Patches from upstream:
  + Don't allow blank hostname.
  + Fix CVE-2014-7913.
- Drop obsoleted patch.
- Updated to 6.10.1.

* Tue Jan 12 2016 Mikhail Efremov <sem@altlinux.org> 1:6.10.0-alt2
- Patch from upstream:
  + Fix segfault when handling interface departure.

* Mon Jan 11 2016 Mikhail Efremov <sem@altlinux.org> 1:6.10.0-alt1
- Don't install additional hooks.
- Drop obsoleted patch.
- 50-ntp.conf: Don't return error if config doesn't exist.
- Updated to 6.10.0.

* Thu Dec 17 2015 Mikhail Efremov <sem@altlinux.org> 1:6.9.4-alt3
- Fix routing table (patch from upstream).

* Tue Dec 15 2015 Mikhail Efremov <sem@altlinux.org> 1:6.9.4-alt2
- Fix up hostname (closes: #31632).

* Tue Dec 01 2015 Mikhail Efremov <sem@altlinux.org> 1:6.9.4-alt1
- Update 50-ntp.conf.
- Drop obsoleted patch.
- Updated to 6.9.4.

* Thu Nov 12 2015 Mikhail Efremov <sem@altlinux.org> 1:6.9.3-alt1
- Force the sending of the short hostname by default (closes: #31203).
- Always honor hostname_short option.
- Disable IPv6 by default.
- Updated to 6.9.3.

* Thu Jul 09 2015 Mikhail Efremov <sem@altlinux.org> 1:6.9.1-alt1
- Updated to 6.9.1.

* Tue May 19 2015 Mikhail Efremov <sem@altlinux.org> 1:6.9.0-alt1
- Updated to 6.9.0.

* Tue May 05 2015 Mikhail Efremov <sem@altlinux.org> 1:6.8.2-alt1
- Updated to 6.8.2.

* Mon Mar 30 2015 Mikhail Efremov <sem@altlinux.org> 1:6.8.1-alt1
- Updated to 6.8.1.

* Fri Jan 30 2015 Mikhail Efremov <sem@altlinux.org> 1:6.7.1-alt1
- Updated to 6.7.1.

* Mon Jan 12 2015 Mikhail Efremov <sem@altlinux.org> 1:6.6.7-alt1
- Updated to 6.6.7.

* Thu Dec 18 2014 Mikhail Efremov <sem@altlinux.org> 1:6.6.6-alt1
- Updated to 6.6.6.

* Wed Dec 10 2014 Mikhail Efremov <sem@altlinux.org> 1:6.6.5-alt1
- Updated to 6.6.5.

* Thu Nov 27 2014 Mikhail Efremov <sem@altlinux.org> 1:6.6.4-alt1
- Updated to 6.6.4.

* Wed Nov 26 2014 Mikhail Efremov <sem@altlinux.org> 1:6.6.3-alt1
- Updated to 6.6.3.

* Fri Nov 14 2014 Mikhail Efremov <sem@altlinux.org> 1:6.6.2-alt1
- Updated to 6.6.2.

* Mon Nov 10 2014 Mikhail Efremov <sem@altlinux.org> 1:6.6.1-alt1
- Updated to 6.6.1.

* Wed Nov 05 2014 Mikhail Efremov <sem@altlinux.org> 1:6.6.0-alt1
- Updated to 6.6.0.

* Tue Oct 14 2014 Mikhail Efremov <sem@altlinux.org> 1:6.5.0-alt1
- Updated to 6.5.0.

* Wed Oct 01 2014 Mikhail Efremov <sem@altlinux.org> 1:6.4.7-alt1
- Updated to 6.4.7.

* Tue Mar 11 2014 Mikhail Efremov <sem@altlinux.org> 1:6.3.1-alt2
- Fix crash with '--dumplease' option.

* Tue Mar 04 2014 Mikhail Efremov <sem@altlinux.org> 1:6.3.1-alt1
- Do not package timezone hook.
- Updated to 6.3.1.

* Thu Jan 16 2014 Mikhail Efremov <sem@altlinux.org> 1:6.2.1-alt1
- dhcpcd.conf: Disable wpa_supplicant hook by default.
- wpa_supplicant hook: Use wpa_supplicant.conf for the interface.
- Updated to 6.2.1.

* Fri Sep 20 2013 Mikhail Efremov <sem@altlinux.org> 1:6.1.0-alt1
- Disable 'persistent' option by default.
- Don't package 70-vendor-encap hook.
- Updated to 6.1.0.

* Mon Aug 12 2013 Mikhail Efremov <sem@altlinux.org> 1:6.0.5-alt1
- hostname hook: Fix exit status.
- Actually validate the search list (from upstream git).
- Updated to 6.0.5.

* Mon Jul 22 2013 Mikhail Efremov <sem@altlinux.org> 1:6.0.3-alt1
- Updated to 6.0.3.

* Tue Jul 09 2013 Mikhail Efremov <sem@altlinux.org> 1:6.0.2-alt2
- Use Client ID instead of DUID by default.

* Mon Jul 01 2013 Mikhail Efremov <sem@altlinux.org> 1:6.0.2-alt1
- Updated to 6.0.2.

* Tue Apr 09 2013 Mikhail Efremov <sem@altlinux.org> 1:5.6.8-alt1
- Fix a memory leak (from upstream git).
- Updated to 5.6.8.

* Thu Feb 21 2013 Mikhail Efremov <sem@altlinux.org> 1:5.6.7-alt1
- Updated to 5.6.7.

* Thu Dec 27 2012 Mikhail Efremov <sem@altlinux.org> 1:5.6.6-alt1
- Patch from upstream:
    + Preserve the space in static routes on the command line.
- Updated to 5.6.6.

* Wed Nov 28 2012 Mikhail Efremov <sem@altlinux.org> 1:5.5.6-alt5
- Provide nm-dhcp-client.

* Fri Aug 31 2012 Mikhail Efremov <sem@altlinux.org> 1:5.5.6-alt4
- dhcpcd-run-hooks: Print hook's exit code to log.
- dhcpcd.conf: Disable solicition of IPv6 RA by default.
- ntp.conf hook: Fix exit status.
- Don't set if_up or if_down as true when testing
    (from upstream git).
- Improve patch for check netlink messages sender
    (from upstream git).
- dhcpcd-run-hooks: Don't run *.rpm* and *~ scripts.

* Fri Aug 24 2012 Mikhail Efremov <sem@altlinux.org> 1:5.5.6-alt3
- Accept netlink messages only from kernel.

* Tue Aug 14 2012 Mikhail Efremov <sem@altlinux.org> 1:5.5.6-alt2
- resolv.conf hook: Don't use metric.

* Thu Mar 29 2012 Mikhail Efremov <sem@altlinux.org> 1:5.5.6-alt1
- Updated to 5.5.6.

* Thu Feb 16 2012 Mikhail Efremov <sem@altlinux.org> 1:5.5.4-alt2
- Fix dhcpcd permissions (closes: #26939).

* Wed Feb 08 2012 Mikhail Efremov <sem@altlinux.org> 1:5.5.4-alt1
- Updated to 5.5.4.

* Thu Feb 02 2012 Mikhail Efremov <sem@altlinux.org> 1:5.5.1-alt1
- Updated to 5.5.1.

* Wed Oct 26 2011 Mikhail Efremov <sem@altlinux.org> 1:5.2.12-alt1
- config: Disable vendor-encap hook.
- Updated to 5.2.12.

* Wed Apr 27 2011 Mikhail Efremov <sem@altlinux.org> 1:4.0.15-alt5
- Allow both domain-name and domain-search options.
- Allow RFC violating search in domain.
- Fix support multiple domains in search (closes: #25521).

* Thu Apr 07 2011 Mikhail Efremov <sem@altlinux.org> 1:4.0.15-alt4
- Escape | and & characters when passing to the shell
    (fixes CVE-2011-996, backport from dhcpcd-5).

* Tue Aug 03 2010 Mikhail Efremov <sem@altlinux.org> 1:4.0.15-alt3
- drop Packager from spec.
- Don't use fixed buffer for netlink messages (backport from dhcpcd-5)
- fix hostname check.

* Mon Dec 28 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.15-alt2
- Not request the options that are given with --nooption
    (closes #22574).

* Tue Sep 29 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.15-alt1
- 4.0.15

* Sat Aug 15 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.14-alt2
- minor changes in vendor-encap hook script.
- update-chrooted hook script is removed.
- use update_chrooted in resolv.conf hook script if needed.
- don't install dhcpcd-compat hook script.

* Fri Aug 14 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.14-alt1
- 4.0.14

* Wed Apr 22 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.13-alt2
- added 70-vendor-encap hook script.
- fixed interface name truncation in log messages.

* Mon Apr 20 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.13-alt1
- 4.0.13
- minor changes in 50-ntp.conf.

* Mon Apr 06 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.12-alt5
- fixed ntpd restart

* Fri Apr 03 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.12-alt4
- write info files in /var/lib/dhcpcd.

* Tue Mar 17 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.12-alt3
- Don't run update_chrooted if resolvconf is installed.

* Mon Mar 02 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.12-alt2
- fixed License

* Fri Feb 27 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.12-alt1
- 4.0.12
- fixed URL.

* Fri Feb 20 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.11-alt1
- 4.0.11
- pack source as tar instead tar.gz

* Sun Feb 15 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.10-alt3
- add 'noarp' option in dhcpcd.conf (close ALT bug #18703)

* Thu Feb 12 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.10-alt2
- install lookup-hostname hook script, but disable it by default

* Wed Feb 04 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.10-alt1
- version 4.0.10

* Mon Feb 02 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.7-alt3
- use "servers" keyword instead "server" in ntpd.conf

* Wed Jan 28 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.7-alt2
- handle POLLERR (fix segfault when device is removed).

* Mon Jan 26 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.7-alt1
- fixes from led@ spec:
    fixed URL
    fixed License
    fixed paths

* Wed Jan 21 2009 Mikhail Efremov <sem@altlinux.org> 4.0.7-alt0.4
- applied led@ patches:   
    dhcpcd-4.0.1-alt-hooks.patch
    dhcpcd-4.0.1-alt-linux.patch.
- build both ntpd.conf and ntp.conf if them is exists.

* Tue Dec 09 2008 Mikhail Efremov <sem@altlinux.org> 4.0.7-alt0.3
- add noipv4ll option to config file.
- install ntp.conf hook script.
- ntp.conf hook script fixed for work with openntp.

* Mon Dec 08 2008 Mikhail Efremov <sem@altlinux.org> 4.0.7-alt0.2
- install dhcpcd-compat hook script

* Thu Dec 04 2008 Mikhail Efremov <sem@altlinux.org> 4.0.7-alt0.1
- version 4.0.7

* Mon Aug 18 2008 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt0.1.rc5
- 4.0.0-rc5
- dhcpcd-4.0.0-alt-hostname_hook.patch removed  (obsolete)

* Mon Jul 28 2008 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt0.1.rc4
- 4.0.0-rc4
- dhcpcd-4.0.0-alt-makefile.patch and dhcpcd-4.0.0-alt-noipv4ll_option_fix.patch
  removed (obsolete)

* Mon Jul 28 2008 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt0.1.rc3
- version 4.0.0-rc3

* Fri Mar 28 2008 Michael Shigorin <mike@altlinux.org> 1:3.0.17-alt4
- rollback to 3.0.17 for there are too many regressions (seemingly
  specific to us as no upstream problems are spotted) and I'm unable
  to reliably reproduce the problem; see also #15042 and #15131
- if anyone needs 3.2.x features please look into Daedalus and 
  preferably help with finding out the trouble source (or patch)

* Thu Mar 06 2008 Michael Shigorin <mike@altlinux.org> 3.0.17-alt2.M40.1
- built for M40 (reportedly good enough and tested, see #14643)
- spec cleanup

* Tue Feb 26 2008 Michael Shigorin <mike@altlinux.org> 3.2.3-alt0.2
- added a configure.c patch by shrek@ (mentioned in #14643)
- seems tested & working

* Mon Feb 25 2008 Michael Shigorin <mike@altlinux.org> 3.2.3-alt0.1
- NMU: 3.2.3 (#14643)
- spec macro abuse cleanup
- updated patch1, patch2, patch3
- removed patch4 (obsolete)
- fixed %%config(noreplace) typo in %%files

* Mon May 21 2007 Stanislav Ievlev <inger@altlinux.org> 3.0.17-alt3
- fix -H option (backport from 3.1.0 with fixes)

* Mon May 14 2007 Stanislav Ievlev <inger@altlinux.org> 3.0.17-alt2
- ignore -D option (for backward compatibility with previous installations)

* Tue May 08 2007 Stanislav Ievlev <inger@altlinux.org> 3.0.17-alt1
- 3.0.17

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.22pl4-alt3.0
- Automated rebuild.

* Thu Apr 21 2005 Denis Ovsienko <pilot@altlinux.ru> 1.3.22pl4-alt3
- improved alt-config patch to fix #6133

* Thu Jul 01 2004 Dmitry V. Levin <ldv@altlinux.org> 1.3.22pl4-alt2
- %_sysconfdir/dhcpc/%name.exe:
  + added wlan* interface support (#4348);
  + minor fixes (#4158).

* Mon Oct 20 2003 Dmitry V. Levin <ldv@altlinux.org> 1.3.22pl4-alt1
- Updated to 1.3.22pl4, rediffed patches.
- Install %_sysconfdir/dhcpc/%name.exe by default;
  Patch %_sysconfdir/dhcpc/%name.exe to run update_chrooted.
  (should address #2406).

* Fri Nov 15 2002 Dmitry V. Levin <ldv@altlinux.org> 1.3.22pl3-alt1
- 1.3.22pl3.

* Thu Jul 11 2002 Dmitry V. Levin <ldv@altlinux.org> 1.3.22pl1-alt1
- 1.3.22pl1.
- Fixed ntp driftfile location.
- Avoid false config files renaming.
- Added PidDir option support, /var/run by default (mdk).

* Mon Nov 05 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.3.21pl1-alt1
- 1.3.21pl1.
- Removed patch0 - now it's outdated

* Sun Feb 25 2001 Dmitry V. Levin <ldv@fandra.org> 1.3.19pl7-ipl1mdk
- 1.3.19pl7.

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 1.3.19pl6-ipl1mdk
- RE adaptions.
- Feature: execute scripts on interface up/down.

* Thu Dec 21 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.3.19pl4-1mdk
- new and shiny source.

* Thu Oct 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3.19pl1-2mdk
- Add patch for gcc2.96(rh).

* Tue Aug 08 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.3.19pl1-1mdk
- rebuild to use _sysconfdir
- s|1.3.18pl5|1.3.19pl1|

* Fri Jul 28 2000 Vincent Saugey <vince@mandrakesoft.com> 1.3.18pl5-3mdk
- BM, macros

* Tue Apr 18 2000 Vincent Saugey <vince@mandrakesoft.com> 1.3.18pl5-2mdk
- Add patch for dynamic build
- remove bzip and strip file

* Fri Mar 31 2000 Vincent Saugey <vince@mandrakesoft.com> 1.3.18pl5-1mdk
- Correct group
- Update to 1.3.18-pl5

* Sun Nov  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.3.18-pl3
- add /etc/dhcpc

* Sun Jul 18 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- 1.3.17pl9

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Mon Apr 19 1999 Bill Nottingham <notting@redhat.com>
- build for 6.0

* Wed Dec 23 1998 Jeff Johnson <jbj@redhat.com>
- mark default route up.

* Sun Jun  7 1998 Jeff Johnson <jbj@redhat.com>
- Fix packet alignment problems on sparc.
- build root.

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Wed May  6 1998 Alan Cox
- fixed some potential buffer exploits reported by Chris Evans

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- spec file cleanups

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- built against glibc, updated to 0.65

* Mon Apr 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed summary line... was a summary for tar.
