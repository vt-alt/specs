Name: 	  nagwad
Version:  0.8
Release:  alt4

Summary:  Nagios watch daemon
License:  GPLv3
Group:    System/Servers
Url: 	  http://git.altlinux.org/people/nbr/packages/nagwad.git


Source:   %name-%version.tar

BuildArch: noarch
Requires:  systemd
Requires:  osec-timerunit

%description
Daemon that listens to journald and generates alerts based on journal messages
Example configuration works with alterator-ports-access. It provides Nagios
alerts when unauthorized USB devices are inserted.

%prep
%setup


%package -n osec-timerunit

Summary: Osec job started from systemd unit
Group: System/Servers
Requires: systemd
Requires: osec-mailreport
Conflicts: osec-cronjob
Provides: osec-cron

%description -n osec-timerunit
A set of systemd units that allow periodical start of osec job without using cron

%package server

Summary: Server for nagwad example data and docs
Group:   System/Servers

%description server
These are examples of configuration of Nagios for the controlling machine.

%pre
/usr/sbin/groupadd -r -f osec
/usr/sbin/useradd -r -g osec -d /dev/null -s /dev/null -n osec >/dev/null 2>&1 ||:



%install
install -Dm 0755 usr/sbin/nagwad %buildroot%_sbindir/nagwad
mkdir -p  %buildroot%_libexecdir/nagwad/device
mkdir -p  %buildroot%_libexecdir/nagwad/audit
mkdir -p  %buildroot%_libexecdir/nagwad/authdata
mkdir -p  %buildroot%_libexecdir/nagwad/osec
install -Dm 0755 usr/lib/nagwad/nagwad.sh  %buildroot%_libexecdir/nagwad/
install -Dm 0755 usr/lib/nagwad/device/*  %buildroot%_libexecdir/nagwad/device/
install -Dm 0755 usr/lib/nagwad/audit/*  %buildroot%_libexecdir/nagwad/audit/
install -Dm 0755 usr/lib/nagwad/authdata/*  %buildroot%_libexecdir/nagwad/authdata/
install -Dm 0755 usr/lib/nagwad/osec/*  %buildroot%_libexecdir/nagwad/osec/
install -Dm 0755 unit/nagwad.service %buildroot/%_unitdir/nagwad.service
install -Dm 0755 unit/osec.service %buildroot/%_unitdir/osec.service
install -Dm 0755 unit/osec.timer %buildroot/%_unitdir/osec.timer

mkdir -p  %buildroot%_libexecdir/nagios/plugins/
install -Dm 0755 nagios/plugins/* %buildroot/%_libexecdir/nagios/plugins/
mkdir -p %buildroot/%_docdir
install -Dm 0755 README.md  %buildroot/%_docdir
mkdir -p %buildroot/%_docdir/examples/nrpe
install -Dm 0755 examples/nrpe/*  %buildroot/%_docdir/examples/nrpe/
mkdir -p %buildroot/%_docdir/examples/nagios/server/objects
mkdir -p %buildroot/%_docdir/examples/nagios/server/templates
cp -ar examples/nagios/*  %buildroot/%_docdir/examples/nagios/
install -Dm 0755 signal.odt %buildroot/%_docdir
mkdir -p %buildroot/var/lib/nagwad/audit
mkdir -p %buildroot/var/lib/nagwad/audit_archived
mkdir -p %buildroot/var/lib/nagwad/authdata
mkdir -p %buildroot/var/lib/nagwad/authdata_archived
mkdir -p %buildroot/var/lib/nagwad/osec
mkdir -p %buildroot/var/lib/nagwad/osec_archived
mkdir -p %buildroot/var/lib/nagwad/device
mkdir -p %buildroot/var/lib/nagwad/device_archived

mkdir -p %buildroot/var/lib/osec
chmod 775 %buildroot/var/lib/osec
mkdir -p %buildroot/etc/osec
mkdir -p %buildroot/%_datadir/osec
install -Dm 0755 osec.cron  %buildroot/%_datadir/osec/
install -Dm 0755 osec/* %buildroot/etc/osec/


%files

%_sbindir/*
%_libexecdir/nagwad/*
%_unitdir/nagwad.service
%_libexecdir/nagios/plugins/*
/var/lib/nagwad/
%_docdir/README.md
%_docdir/examples/nrpe/*


%files server
%_docdir/examples/nagios/*
%_docdir/signal.odt

%files -n osec-timerunit
/etc/osec/*
%attr(770,root,osec) /var/lib/osec/
%_datadir/osec/*
%_unitdir/osec.service
%_unitdir/osec.timer

%changelog
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

