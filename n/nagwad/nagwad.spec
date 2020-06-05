Name: 	  nagwad
Version:  0.9.6
Release:  alt2

Summary:  Nagios watch daemon
License:  GPLv3
Group:    Monitoring
Url: 	  http://git.altlinux.org/people/nbr/packages/nagwad.git


Source:   %name-%version.tar

BuildArch: noarch
BuildRequires: discount

Requires:  systemd audit
Requires:  osec-cronjob
Requires:  nagios-nrpe >= 3.2.1-alt4

%description
Daemon that listens to journald and generates alerts based on journal messages
Example configuration works with alterator-ports-access. It provides Nagios
alerts when unauthorized USB devices are inserted.

%prep
%setup

%package templates
Summary: Nagios templates for a nagwad node
Group:   Monitoring
Obsoletes: %name-server
Conflicts: %name-server
Conflicts: nagios < 3.0.6-alt9
Requires: xvt openssh-clients

%description templates
These are Nagios configuration templates for monitoring a nagwad-node.

%package actions
Summary: Nagstamon actions for a nagwad node
Group:   Monitoring
Requires: xvt openssh-clients

%description actions
These are Nagstamon action commands suitable for a nagwad-node.

%build

markdown -f links,smarty,toc,autolink -o signal.html signal.md

%install
install -Dm 0755 scripts/nsca-shell %buildroot%_bindir/nsca-shell
install -Dm 0755 scripts/nagwad %buildroot%_sbindir/nagwad
install -Dm 0755 scripts/nagwad.sh  %buildroot%_libexecdir/nagwad/nagwad.sh
install -Dm 0755 scripts/nrpe/check_authdata %buildroot/%_libexecdir/nagios/plugins/check_authdata
install -Dm 0755 scripts/nrpe/check_devices %buildroot/%_libexecdir/nagios/plugins/check_devices
install -Dm 0755 scripts/nrpe/check_login %buildroot/%_libexecdir/nagios/plugins/check_login
install -Dm 0755 scripts/nrpe/check_osec %buildroot/%_libexecdir/nagios/plugins/check_osec

install -Dm 0644 conf/audit/rules.d/50-nagwad.rules %buildroot%_sysconfdir/audit/rules.d/50-nagwad.rules
install -Dm 0644 conf/nagios/templates/50-nagwad.cfg %buildroot%_sysconfdir/nagios/templates/50-nagwad.cfg
install -Dm 0644 conf/nagwad/authdata/authdata.regexp %buildroot%_sysconfdir/nagwad/authdata/authdata.regexp
install -Dm 0644 conf/nagwad/device/device.regexp %buildroot%_sysconfdir/nagwad/device/device.regexp
install -Dm 0644 conf/nagwad/login/login.regexp %buildroot%_sysconfdir/nagwad/login/login.regexp
install -Dm 0644 conf/nagwad/osec/osec.regexp %buildroot%_sysconfdir/nagwad/osec/osec.regexp
install -Dm 0644 conf/nagios/nrpe/nagwad.cfg %buildroot%_sysconfdir/nagios/nrpe-commands/nagwad.cfg
install -Dm 0644 conf/nagstamon/actions/action_Lock_host.conf %buildroot%_sysconfdir/nagstamon/actions/action_Lock_host.conf
install -Dm 0644 conf/nagstamon/actions/action_NSCA_shell.conf %buildroot%_sysconfdir/nagstamon/actions/action_NSCA_shell.conf

install -Dm 0644 unit/nagwad.service %buildroot/%_unitdir/nagwad.service

mkdir -p %buildroot/var/log/nagwad

%files
%doc README.md signal.html signal.md
%_bindir/nsca-shell
%_sbindir/nagwad
%_libexecdir/nagwad
%_unitdir/nagwad.*
%_libexecdir/nagios/plugins/*
%_sysconfdir/nagwad
%config(noreplace) %_sysconfdir/audit/rules.d/*nagwad*.rules
%config(noreplace) %_sysconfdir/nagwad/*/*.regexp
%config(noreplace) %_sysconfdir/nagios/nrpe-commands/nagwad.cfg
/var/log/nagwad

%files templates
%doc README.md signal.html signal.md
%config(noreplace) %_sysconfdir/nagios/templates/*nagwad*.cfg

%files actions
%config(noreplace) %_sysconfdir/nagstamon/actions/*.conf

%changelog
* Thu May 28 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.6-alt2
- Fixed documentation (signal.md):
  -- replace '.cnf' with '.cfg' (thx vercha@);
  -- added "nagstamon" package to the server list (thx nbr@).

* Fri May 22 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.6-alt1
- Use root@$ADDRESS$ for the Lock_host action.
- Produce and install signal.html.
- Updated the README.
- Added signal.md (and html) --- the manual in Russian.

* Thu May 07 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.5-alt1
- Fixed quotation in NSCA shell action.
- Fixed OSEC regular expression for Nagwad.

* Wed Apr 22 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.4-alt2
- Switch to cronjob until timerunit patch is accepted by the OSEC's
  maintainer.

* Mon Apr 13 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.4-alt1
- Verbose descriptions in template checks.

* Mon Mar 02 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.3-alt1
- Conflicts with nagios < 3.0.6-alt9.
- Fixed nsca-shell missing show_usage().
- Added hostgroup "nagwad-nodes" and bind nagwad checks to it.

* Wed Feb 12 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.2-alt1
- Fix/improve: Force SSH to allocate a PTY.
- Fix/improve the nsca-shell: pass shell arguments after --rcfile.
- Fix/improve: Make the login.regexp react to an auth error from
  any service.

* Wed Feb 12 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.1-alt1
- Added Nagstamon actions (package '%name-actions').
- Install /etc/... files with %%config(noreplace).
- Fixed check_authdata checker.
- Obsolete nagwad-server.
- Fix: Rename NRPE script: check_devices.

* Fri Feb 07 2020 Paul Wolneykien <manowar@altlinux.org> 0.9-alt1
- Define the nagwad NRPE commands in the separate
  /etc/nagios/nrpe-commands/nagwad.cfg (requires nagios-nrpe >=
  3.2.1-alt4).
- Switch to /etc/nagwad and /var/log/nagwad directories.
- Moved osec timerunit to the osec SRC RPM.
- Use auditd to watch for /etc/passwd and group changes.
- Sanitized and modernized nagwad scripts.
- Added the wrapper command 'nsca-shell' for sending shell
  typescript to the Nagios server using the NSCA interface.

* Wed Jan 22 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.8-alt4
- build for sisyphus

* Wed Oct 09 2019 Denis Medvedev <nbr@altlinux.org> 0.8-alt3.M80C.7
- changed the behavour of osec's pipe to leave a log in /var/log

* Thu Aug 08 2019 Denis Medvedev <nbr@altlinux.org> 0.8-alt3.M80C.6
- added example  nagwad.sh

* Tue Apr 16 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8-alt3.M80C.5
- Updated provides for osec.

* Mon Mar 18 2019 Denis Medvedev <nbr@altlinux.org> 0.8-alt3.M80C.4
- osec now by default read-only on base, if READABLE= global var not set.

* Fri Jan 19 2018 Denis Medvedev <nbr@altlinux.org> 0.8-alt3.M80C.3
- reduce of default dir list to check for osec

* Wed May 17 2017 Denis Medvedev <nbr@altlinux.org> 0.8-alt3.M80C.2
- switch to systemd in logging in c8

* Wed May 17 2017 Denis Medvedev <nbr@altlinux.org> 0.8-alt3%ubt
- fix permissions for /var/lib/osec

* Mon Apr 24 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.8-alt2%ubt
- move provides/conflicts for osec-timerunit from description

* Fri Apr 14 2017 Denis Medvedev <nbr@altlinux.org> 0.8-alt1%ubt
- extracted osec-timerunit package

* Fri Mar 31 2017 Denis Medvedev <nbr@altlinux.org> 0.7-alt4%ubt
- fix for dependences

* Thu Mar 30 2017 Denis Medvedev <nbr@altlinux.org> 0.7-alt3%ubt
- Change license to GPLv3,  dependencies added

* Thu Mar 30 2017 Denis Medvedev <nbr@altlinux.org> 0.7-alt2%ubt
- added universal build tag

* Thu Mar 30 2017 Denis Medvedev <nbr@altlinux.org> 0.7-alt1
- added osec timer and service for starting osec without cron.
Instructions for start is in signal.odt

* Thu Mar 02 2017 Denis Medvedev <nbr@altlinux.org> 0.6-alt1
- More mature version that checks 3 additional signals.

* Mon Feb 27 2017 Denis Medvedev <nbr@altlinux.org> 0.5-alt1
 Initial release

