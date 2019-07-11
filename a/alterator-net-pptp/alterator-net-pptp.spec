Name: alterator-net-pptp
Version: 0.10.5
Release: alt1

Url: http://www.altlinux.org/Alterator
Source: %name-%version.tar
Packager: Mikhail Efremov <sem@altlinux.org>

Summary: Alterator module to configure PPTP connections
License: GPL
Group: System/Configuration/Other

Requires: alterator >= 5.0-alt5
Requires: alterator-sh-functions >= 0.3-alt2
Requires: alterator-net-functions >= 0.8-alt1
Requires: alterator-hw-functions
Requires: pptp-client
Conflicts: alterator-fbi < 5.10-alt1
Conflicts: alterator-lookout < 1.6-alt8

BuildPreReq: alterator >= 5.0


%ifarch %e2k
BuildRequires: guile20-devel libguile20-devel
%else
BuildRequires: guile22-devel
%endif
BuildRequires: rpm-build >= 4.0.4-alt103
BuildRequires: alterator >= 5.0 alterator-fbi >= 5.33-alt1

%description
Alterator module to configure PPTP connections

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/*.scm
%_alterator_datadir/ui/*/*.html
%_alterator_libdir/ui/*/*.go
%_alterator_backend3dir/*

# TODO:
# - add "compression on/off" knob
# - cleanup PPTP-over-PPP hasty fix

%changelog
* Thu Jul 11 2019 Andrey Cherepanov <cas@altlinux.org> 0.10.5-alt1
- Use hostname-or-ip field type to support IP address (ALT #37010).

* Fri Apr 13 2018 Grigory Ustinov <grenka@altlinux.org> 0.10.4-alt1.1.1
- NMU: Replace BuildRequires for guile on e2k arch.

* Mon Jul 17 2017 Paul Wolneykien <manowar@altlinux.org> 0.10.4-alt1
- Use typed parameters (closes: #33657).
- Build with guile2.0.

* Thu Jul 10 2014 Timur Aitov <timonbl4@altlinux.org> 0.10.3-alt1
- add maxfail, holdoff, lcp-echo-interval, lcp-echo-failure options

* Sat Aug 20 2011 Michael Shigorin <mike@altlinux.org> 0.10.2-alt1
- implemented --clamp-mss-to-pmtu autosetup (closes: #26124)
  + should help when a remote host pings and works ok from gateway
    setup using this module but a workstation behind it will ping
    that remote host but timeout on e.g. http due to oversized packets
  + you might need to explicitly enable /etc/net firewall by adding
    CONFIG_FW=yes to /etc/net/ifaces/default/options; if that's ever
    needed, please amend http://bugzilla.altlinux.org/26124

* Tue Sep 07 2010 Michael Shigorin <mike@altlinux.org> 0.10.1-alt1
- disabled Van Jacobson compression by default (reported symptom:
  ICMP ping would work just fine, while HTTP HEAD would get stuck;
  forward port of 0.5.10-alt1)
- updated Packager:
- added an Url:

* Fri Jan 15 2010 Mikhail Efremov <sem@altlinux.org> 0.10-alt1
- use setsid for ifup comand.

* Sun Oct 04 2009 Mikhail Efremov <sem@altlinux.org> 0.9-alt1
- disable UI if connections do not exist (closes: #21693).
- join callbacks for qt and html.
- improve connection start (by inger@)

* Mon Apr 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.8-alt2
- qt ui: add margin
- backend: replace own start/stop functions with standard from alterator-net-functions

* Fri Apr 10 2009 Stanislav Ievlev <inger@altlinux.org> 0.8-alt1
- use modern form library, ajax interface and alterator-net-functions

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt6
- move translations and help to alterator-l10n

* Mon Jan 19 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt5
- merge with inger

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt4.2
- use help from l10n

* Tue Nov 11 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt4.1
- minor module update
- backend: don't work with empty names

* Wed Nov 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt3
- add DOCTYPE to html template

* Sat Nov 01 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt2
- remove title and h1 from html template

* Tue Sep 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- replace constraints with types

* Wed Jun 18 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt4
- use write_debug from alterator-sh-functions

* Tue Jun 17 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt3
- move most functions to alterator-net-common

* Mon Jun 16 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt2
- join to common translation database

* Thu May 15 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- use alterator-sh-functions
- rewrite UI

* Mon May 12 2008 Michael Shigorin <mike@altlinux.org> 0.5.9-alt1
- add "usepeerdns" by default into pppoptions (#14116)

* Tue Apr 22 2008 Michael Shigorin <mike@altlinux.org> 0.5.8-alt1
- "kludgy krap" release
- hacked to allow PPTP-over-PPP:
  + start PPTP interface numbering with "ppp1"
  + if ppp0 is active (via dialer, not etcnet) on module startup,
    append it to interface list
  + don't try to REQUIRE dynamic interface like that either

* Thu Mar 20 2008 Michael Shigorin <mike@altlinux.org> 0.5.7-alt1
- mtu: 1460->1400 (Alexey Novikov reported that his connection
  seems to have required 1432)

* Thu Mar 20 2008 Michael Shigorin <mike@altlinux.org> 0.5.6-alt1
- clamp mtu to 1460 on interfaces being created: ISP or link
  related issues might sort of mandate this (in case of
  "lost or reordered" GRE packets you might try to lower it
  to 1400 as WinXP would do by default);
  thanks Sergey Vlasov (vsu@) for insightful advice;
  see also #14730

* Tue Mar 04 2008 Michael Shigorin <mike@altlinux.org> 0.5.5-alt3
- rebuild

* Tue Mar 04 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5.5-alt2
- Change help paths to the new style.

* Sun Mar 02 2008 Michael Shigorin <mike@altlinux.org> 0.5.5-alt1
- don't attempt to start interface upon "Apply" button unless
  it's marked to start at boot (probably shouldn't start at all,
  there are Start/Stop buttons now and currently the module sorta
  hangs if unable to connect)

* Sun Mar 02 2008 Michael Shigorin <mike@altlinux.org> 0.5.4-alt1
- applied patch by Konstantin Uvarin (lodin@) to move password
  from chap-secrets which is shared by all connections into
  interface-specific pppoptions (#14649)

* Sat Feb 23 2008 Michael Shigorin <mike@altlinux.org> 0.5.3-alt1
- add "nodeflate" and "nobsdcomp" options to created PPP interfaces
  since these compression types are unsupported on Windows(TM) and
  hence have better chance to be untested/broken on server-side;
  thanks Sergey Vlasov (vsu@) for a note

* Tue Jan 15 2008 Michael Shigorin <mike@altlinux.org> 0.5.2-alt1
- disable buttons and inputs that are useless
  (e.g. when no connection is configured) (#14026)
- retry ifup/ifdown 3 times, not 5

* Tue Jan 15 2008 Michael Shigorin <mike@altlinux.org> 0.5.1-alt1
- fixed subtle thinko in start_iface() -- which wouldn't trigger
  any problems in that particular script but did manifest later
- added "Start" and "Stop" buttons to directly manipulate the
  connection status
- updated strings/translations

* Tue Jan 15 2008 Michael Shigorin <mike@altlinux.org> 0.5.0-alt1
- first strike at routing issues (#13966): this version will setup
  an additional static route to VPN gateway via current defult gw
  (not exactly ideal but this seems to be done properly in etcnet)
- added onboot and persist controls (another part of #11988)
- updated strings and translations
- somewhat tested

* Thu Dec 06 2007 Michael Shigorin <mike@altlinux.org> 0.4.1-alt1
- added MPPE checkbox (partial fix for #11988)
- s/throw/through/ (#13336)
- s/net-pppoe/net-pptp/
- uk.po update

* Thu Jul 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- use alterator-net-common common library

* Wed Jun 13 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt13
- add desktop file

* Thu May 31 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt12
- rebuild with latest standalone
- add interface status info

* Fri May 25 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt11
- switch to new card-index scripts

* Mon Apr 23 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt10
- update Ukrainian translation

* Thu Apr 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt9
- little CSS optimizations

* Thu Apr 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt8
- remove config-*

* Mon Apr 02 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt7
- add Ukrainian translation
- help improvements from kirill@

* Fri Mar 30 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt6
- improve po template generation
- add documentation

* Wed Mar 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt5
- assign 'Network' group

* Wed Mar 07 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt4
- more translations
- use gridbox

* Thu Feb 22 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt3
- use ifup/ifdown instead of whole network restart
- enable auto-select

* Mon Feb 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- simplify backend
- fix ethernet interface listing

* Thu Feb 08 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- add fbi data

* Wed Feb 07 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- fix constraints for server name (bug #10780)

* Mon Jan 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- require gettext
- add label constraints

* Wed Dec 13 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt6
- fix backend (read on /)

* Wed Dec 06 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- move "first available interface" logic from UI to backend
- list all available eth interfaces itself

* Wed Nov 29 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- add constraints visualization

* Thu Nov 16 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- add translations
- enable constraints

* Wed Nov 08 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- use native message boxes

* Wed Nov 01 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- initial release


