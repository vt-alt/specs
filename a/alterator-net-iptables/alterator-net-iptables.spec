Name: alterator-net-iptables
Version: 4.19.8
Release: alt1

Packager: Vladislav Zavjalov <slazav@altlinux.org>

Summary: alterator module for simple iptables configuration
License: GPL
Group: System/Configuration/Other
Url: http://wiki.sisyphus.ru/Alterator

Source: %name-%version.tar

Requires: alterator >= 5.0-alt4
Requires: alterator-l10n >= 2.0-alt2
Requires: iptables etcnet
Requires: alterator-sh-functions >= 0.10-alt1
Requires: alterator-net-functions >= 1.3.1-alt1
Requires: alterator-net-common >= 0.4-alt1
Conflicts: alterator-fbi < 5.23-alt1

BuildPreReq: alterator >= 5.0

%ifarch %e2k
BuildRequires: guile20-devel libguile20-devel
%else
BuildRequires: guile22-devel
%endif

BuildRequires: alterator >= 5.0 alterator-fbi >= 5.33-alt1

%description
Alterator module for simple iptables configuration

%prep
%setup -q

%build
%make_build

%install
%makeinstall
mkdir -p -- %buildroot%_logdir
touch -- %buildroot%_logdir/%name

%files
%dir %_sysconfdir/alterator/net-iptables/
%config(noreplace) %_sysconfdir/alterator/net-iptables.conf
%config(noreplace) %_sysconfdir/alterator/net-iptables/*.conf
%_sysconfdir/alterator/net-iptables/List
%_sysconfdir/alterator/net-iptables/*.desktop
%dir %_sysconfdir/alterator/net-ip6tables/
%config(noreplace) %_sysconfdir/alterator/net-ip6tables.conf
%config(noreplace) %_sysconfdir/alterator/net-ip6tables/*.conf
%_sysconfdir/alterator/net-ip6tables/List
%_sysconfdir/alterator/net-ip6tables/*.desktop
%_alterator_backend3dir/*
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/*.scm
%_alterator_datadir/ui/*/*.html
%_alterator_libdir/ui/*/*.go
%_alterator_datadir/type/*.scm
%_alterator_libdir/type/*.go
%_bindir/*
%_mandir/man?/*
%dir %_libexecdir/alterator/hooks/net-iptables.d/
%dir %_libexecdir/alterator-net-iptables/
%_libexecdir/alterator-net-iptables/*
%_logdir/alterator-net-iptables

%changelog
* Wed May 20 2020 Georgy A Bystrenin <gkot@altlinux.org> 4.19.8-alt1
- net-iptables: Add host mode support (Closes: #38505)

* Mon Jun 10 2019 Fr. Br. George <george@altlinux.ru> 4.19.7-alt3
- Add default values to net-iptables.conf (Closes: #34291)

* Thu May 31 2018 Paul Wolneykien <manowar@altlinux.org> 4.19.7-alt2
- Don't require a particular rpm-build version.

* Fri Apr 13 2018 Grigory Ustinov <grenka@altlinux.org> 4.19.7-alt1.1.1
- NMU: Replace BuildRequires for guile on e2k arch.

* Fri Jul 14 2017 Paul Wolneykien <manowar@altlinux.org> 4.19.7-alt1
- Build with new alterator (guile2).
- Use quote_shell_var instead of plain eval (closes: #33646).
- Use typed params everywhere it is possible.

* Tue Feb 24 2015 Mikhail Efremov <sem@altlinux.org> 4.19.6-alt1
- Set restart_network to 'on' by default.
- net-iptables.conf: Add restart_network option.

* Mon Feb 16 2015 Mikhail Efremov <sem@altlinux.org> 4.19.5-alt1
- Fix ULOG counters (closes: #25489).

* Tue Dec 09 2014 Mikhail Efremov <sem@altlinux.org> 4.19.4-alt1
- Only show IP version selector if more then one is available.

* Thu Oct 23 2014 Mikhail Efremov <sem@altlinux.org> 4.19.3-alt1
- Fix disabling firewall.

* Mon Aug 11 2014 Mikhail Efremov <sem@altlinux.org> 4.19.2-alt1
- Don't show IPv6 in the list if IPv6 is disabled.

* Mon Jun 03 2013 Mikhail Efremov <sem@altlinux.org> 4.19.1-alt1
- index.scm: Update ifaces and services lists on IP version change.

* Wed Nov 14 2012 Mikhail Efremov <sem@altlinux.org> 4.19-alt1
- iptables_helper: Allow networks in the IR module.
- iptables_helper: Fix regexp for default services.
- iptables_helper: Add default services for each IP.
- iptables_helper: Allow default services for internal ifaces.
- net-iptables-manual: Add IPv6 support.
- net-tc: Add IPv6 support.
- net-tc: Use 'ip neighbour' instead of 'arp'.
- net-bl: Add IPv6 support.
- net-iptables: Add IPv6 support.
- Add *.desktop files and config files for IPv6.
- iptables_helper: Add ip6tables support.
- Use 'conntrack' match instead of 'state'.
- ip comments support in ir module (by Vladislav Zavjalov).

* Tue Apr 19 2011 Vladislav Zavjalov <slazav@altlinux.org> 4.18-alt2
- cups.desktop: add udp:631 (closes: 25467)

* Sun Feb 06 2011 Vladislav Zavjalov <slazav@altlinux.org> 4.18-alt1
- allow any protocol names in service lists
- vpn.desktop: gre:;tcp:1723 (closes: 25036)

* Sun Jan 16 2011 Vladislav Zavjalov <slazav@altlinux.org> 4.17-alt2
- desktop-files: add uk translations (thanks to Roman Savochenko)

* Tue Feb 16 2010 Vladislav Zavjalov <slazav@altlinux.org> 4.17-alt1
- iptables_helper: add logging

* Thu Dec 24 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.16-alt5
- net-iptables-manual.desktop: add X-Alterator-UI=html

* Tue Dec 22 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.16-alt4
- sip.desktop: add tcp:1720 (h323) and udp:10000-20000 (RTP) ports

* Fri Dec 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.16-alt3
- fix desktop-files (add Firewall menu group)

* Thu Dec 10 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.16-alt2
- use gateway made by default
- fix manpage

* Thu Nov 12 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.16-alt1
- net-tc ajax.scm: go to default section after delete
- net-tc backend: don't write empty ip
- iptables_helper: add support for commit_mode
- add net-iptables-manual alterator module
- add manual mode warnings in other modules
- fix manpage

* Wed Oct 14 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.15-alt1
- ajax.scm: use new card-index module

* Wed Oct 14 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.14-alt3
- rewrite net-iptables/ajax.scm, fix l10n

* Wed Oct 14 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.14-alt2
- fix typo in net-iptables/ajax.scm

* Tue Oct 13 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.14-alt1
- net-iptables html ui: use wf=none

* Tue Oct 06 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.13-alt1
- iptables_helper: fix broken iptables rule

* Wed Sep 30 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.12-alt1
- net-iptables backend: add firsttime action
- openvpn.desktop: add tcp:1194 port

* Tue Sep 29 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.11-alt3
- net-tc/ajax.scm: fix translations of backend messages

* Tue Sep 29 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.11-alt2
- net-tc/ajax.scm: add xgettext domain

* Fri Sep 25 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.11-alt1
- update desktop-files
- net-tc html ui: more informative labels

* Fri Sep 04 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.10-alt1
- iptables_helper: allow ESTABLISHED,RELATED packets in FORWARD and OUTPUT chains

* Fri Sep 04 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.9-alt1
- iptables_helper: fix firewalling rules

* Fri Sep 04 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.8-alt1
- fix net-tc and net-bl alterator modules
- use lib/srv.sh library for working with service lists
- allow port ranges
- update service list

* Wed Sep 02 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.7-alt1
- net-tc: rewrite ajax.scm
- add default net-iptables.conf (closes: #21118)
- add default config for internal restrictions module
- add icmp in list of services
- iptables_helper: fix ir_del()
- iptables_helper: add DNAT rules to nat/OUTPUT

* Tue Sep 01 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.6-alt1
- rewrite alterator-net-tc script
- fix errors in iptables_helper script
- fix errors in net-tc, net-dnat, net-bl alterator modules

* Fri Aug 28 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.5-alt2
- fix net-bl/ajax.scm

* Fri Aug 28 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.5-alt1
- fix labels
- backends: do nothing on delete action with empty target

* Fri Aug 28 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.4-alt1
- add blacklist module (net-bl)
- fix del action in port redirection module
- allow port ranges in port redirection module
- remove old-style port redirection (-S parameter)

* Thu Aug 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.3-alt1
- iptables_helper: add ulogd module
- iptables_helper: fix shell_config_set1()

* Thu Aug 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.2-alt1
- iptables_helper: add port redirection module

* Thu Aug 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.1-alt1
- rewrite DNAT module
- fix IR module

* Tue Aug 25 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.0-alt1
- rewrite module for Internal network restrictions
  - add firewalling for internal clients
  - change iptables_helper script interface
    (see iptables_script ir help)
  - fix labels in net-tc.desktop (closes: #21145)
  some fixes in iptables_helper script

* Fri Aug 14 2009 Vladislav Zavjalov <slazav@altlinux.org> 3.3-alt1
- fix forwarding rules
- add -m physdev --physdev-is-bridged -j ACCEPT rule to FORWARD chain
  (allow forwarding through bridges)

* Fri Aug 14 2009 Vladislav Zavjalov <slazav@altlinux.org> 3.2-alt3
- explicitely exit on fatals in subshells

* Fri Aug 14 2009 Vladislav Zavjalov <slazav@altlinux.org> 3.2-alt2
- fix error on adding transparent squid rules

* Thu Aug 13 2009 Vladislav Zavjalov <slazav@altlinux.org> 3.2-alt1
- Allow forwarding from each external iface to its networks (closes: #20143)
- net-tc: some fixes

* Thu Jul 02 2009 Vladislav Zavjalov <slazav@altlinux.org> 3.1-alt2
- fix writng to net-tc.conf

* Thu Jul 02 2009 Vladislav Zavjalov <slazav@altlinux.org> 3.1-alt1
- add module for traffic control, remove old fixmac module

* Tue Jun 09 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.15-alt1
- net-iptables backend: use netdev_read_info() from alterator-hw-functions
  instead of ifaceinfo script from alterator-net-functions. (Don't use
  hal/dbus, don't restart hal/dbus at every action.)

* Tue Jun 09 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.14-alt1
- fixmac: log rejected packets via syslog

* Tue Jun 09 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.13-alt1
- add fixmac alterator module
- cleanup net-dnat backend
- update manpage
- iptables_helper: fix test_vars() to pass hidden services

* Fri Jun 05 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.12-alt1
- use /etc/alterator/services/List to specify services shown in interfaces
- cleanup desktop-files

* Mon Jun 01 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.11-alt1
- iptables_helper
 - fix forwarding rule for DNAT (closes: #20187)
 - show -i and -e prints ifaces separated by \n
 - add experimental fixmac feature

* Fri May 08 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.10-alt2
- fix spec to avoid ownerless dirs

* Fri May 08 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.10-alt1
- add ip_conntrack_ftp to /etc/net/ifaces/default/fw/iptables/modules
  (closes: #19948)

* Thu Apr 30 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.9-alt1
- iptables_helper: open icmp by default (closes: #19865)

* Wed Apr 22 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.8-alt1
- add openvpn.desktop (udp:1194)

* Fri Apr 17 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.7-alt1
- iptables_helper script:
  - fix manpage
  - shorten help message
  - add warnings to autogenerated config files

* Thu Apr 16 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.6-alt1
- iptables_helper: don't require ifaces to be existent
- iptables_helper: keep ifaces in config separated only by ";"

* Tue Apr 14 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.5-alt1
- add alterator-net-iptables -> iptables_helper symlink
- add manpage
- allow forwarding for dnat'ed packets (closes: #19301)

* Thu Apr 02 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.4-alt2
- update desktop-file translations

* Wed Apr 01 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.4-alt1
- Fix forwarding rules: drop all packets from external
  ifaces except ones with --state ESTABLISHED,RELATED

* Wed Mar 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.3-alt1
- backends: fix interface info

* Wed Mar 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.2-alt1
- fix label

* Wed Mar 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.1-alt1
- fix po-domain in net-dnat module

* Wed Mar 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.0-alt1
- add alterator module for DNAT (with QT and HTML UI)
- move html templates to ui directory
- iptables_helper:
  + DROP all FORWARD packets from external ifaces
  + fix error in iptables_helper with writing to nat/PREROUTING table
  + change format of DNAT rules to <proto>:<ip>:<port>:<ip>:<port>

* Thu Mar 05 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.11-alt1
- iptables_helper: fix efw restarting
- iptables_helper: add DNAT stuff
- add zeroconf.desktop (udp:5353)

* Tue Mar 03 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.10-alt1
- iptables_helper: fix internal interface list

* Tue Mar 03 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.9-alt1
- run-parts /usr/lib/alterator/hooks/net-iptables.d/ on write

* Tue Feb 24 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt1
- add ip to iface list
- html ui: add class="text" to text inputs

* Tue Feb 24 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.7-alt1
- iptables_helper:
  + fix modify_list() to work with empty values
  + add -d option for reset action
  + fix help
- backend: use router mode by default
- write network interface controller names (by inger@)
  rearrange ui for these long interface names

* Fri Feb 20 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.6-alt1
- add options for show action ("iptables_helper show -e" shows external interfaces etc.)

* Fri Feb 13 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt1
- correct work without initial config

* Wed Feb 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.4-alt1
- iptables_helper: move ulogd rules setting on top (before DROP rule)
- iptables_helper: add transparent squid translations
- iptables_helper: change of command line options

* Tue Feb 10 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt1
- iptables_helper: options for adding and removing values from existing lists
- iptables_helper: update help

* Mon Feb 09 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt1
- fix ulogd rules

* Mon Feb 09 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt1
- don't eval set_locale()
- change labels: firewall/gateway -> router/gateway

* Fri Feb 06 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt1
- Rewrite all. Use iptables_helper script (see `iptables_helper help`)

* Fri Jan 30 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt2
- backend: fix reset_basic function - 2

* Fri Jan 30 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt1
- backend: fix reset_basic function

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt4
- show warning if alterator port is closed on any interface

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt3
- move help and translations to alterator-l10n

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt2
- fix work with empty chainfiles

* Mon Jan 26 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt1
- change policy reset function
- add ldap.desktop

* Mon Jan 26 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt3
- add dhcp.desktop

* Fri Jan 23 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt2
- forwarding setting does not depends on firewall

* Tue Jan 20 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt1
- more visible warning about closing alterator port
- don't ask for a confirmation when firewall is off
- don't remove foreign rules (without -j ACCEPT, -j DROP, -P)

* Mon Dec 29 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt8
- add ip_conntrack_ftp to /etc/net/ifaces/default/fw/iptables/modules 
  (for ftp passive mode)

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt7
- add cups.desktop

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt6
- rebuild with new l10n

* Thu Dec 04 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt5
- fix spec

* Thu Dec 04 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt4
- simplify warning logic when closing ahttpd port
- fix problem with desktop file translations

* Wed Dec 03 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt3
- warning when closing ahttpd port

* Tue Nov 25 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt2
- add support for extra port lists
- cache desktop data
- fix backend logic for action write
- join forms

* Thu Aug 28 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- join to common translation database

* Wed Aug 27 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
