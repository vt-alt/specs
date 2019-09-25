%define subscribers_dir /lib/resolvconf

Name: openresolv
Version: 3.9.2
Release: alt1

Summary: A framework for managing DNS information 
License: %bsdstyle
Group: System/Configuration/Networking

URL: http://roy.marples.name/projects/%name
Source: %name-%version.tar
Source1: test
Patch0: %name-%version-%release.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

Requires: filesystem >= 2.3.5

# pdnsd support
%def_with pdnsd
# PowerDNS support
%def_with pdns

%define _unpackaged_files_terminate_build 1

%description
resolvconf is the middleman between the network
configuration services and /etc/resolv.conf.
resolvconf itself is just a script that stores,
removes and lists a full resolv.conf generated
for the interface. It then calls all the helper
scripts it knows about so it can configure the real
/etc/resolv.conf and optionally any local nameservers
other can libc.

%package bind
Summary: bind subscriber for openresolv
Group: System/Configuration/Networking
Requires: %name = %version-%release
Requires: bind

%description bind
bind subscriber for openresolv

%package dnsmasq
Summary: dnsmasq subscriber for openresolv
Group: System/Configuration/Networking
Requires: %name = %version-%release
Requires: dnsmasq >= 2.65-alt1

%description dnsmasq
dnsmasq subscriber for openresolv

%package unbound
Summary: unbound subscriber for openresolv
Group: System/Configuration/Networking
Requires: %name = %version-%release
Requires: unbound

%description unbound
unbound subscriber for openresolv

%if_with pdnsd
%package pdnsd
Summary: pdnsd subscriber for openresolv
Group: System/Configuration/Networking
Requires: %name = %version-%release
Requires: pdnsd

%description pdnsd
pdnsd subscriber for openresolv
%endif

%if_with pdns
%package pdns
Summary: PowerDNS subscriber for openresolv
Group: System/Configuration/Networking
Requires: %name = %version-%release
Requires: pdns

%description pdns
PowerDNS subscriber for openresolv
%endif

%prep
%setup -q
%patch0 -p1
cp %SOURCE1 .

%build
./test
%configure --sbindir=/sbin --libexecdir=/lib/resolvconf \
           --localstatedir=%_var \
           --rundir=%_var/run \
           --os=linux
%make

%install
%makeinstall_std

mkdir -p %buildroot%_sysconfdir/dnsmasq.conf.d
touch %buildroot%_sysconfdir/dnsmasq.conf.d/60-resolvconf
touch %buildroot%_sysconfdir/resolv.conf.dnsmasq
mkdir -p %buildroot%_localstatedir/bind/etc
touch %buildroot%_localstatedir/bind/etc/resolvconf-zones.conf
touch %buildroot%_localstatedir/bind/etc/resolvconf-options.conf

%files
/sbin/*
%_man5dir/*
%_man8dir/*
%dir %subscribers_dir
%subscribers_dir/libc
%config(noreplace) %_sysconfdir/resolvconf.conf

%files bind
%subscribers_dir/named
%ghost %_localstatedir/bind/etc/resolvconf-zones.conf
%ghost %_localstatedir/bind/etc/resolvconf-options.conf

%files dnsmasq
%subscribers_dir/dnsmasq
%config(noreplace) %_sysconfdir/resolv.conf.dnsmasq
%ghost %_sysconfdir/dnsmasq.conf.d/60-resolvconf

%files unbound
%subscribers_dir/unbound

%if_with pdnsd
%files pdnsd
%subscribers_dir/pdnsd
%else
%exclude %subscribers_dir/pdnsd
%endif

%if_with pdns
%files pdns
%subscribers_dir/pdns_recursor
%else
%exclude %subscribers_dir/pdns_recursor
%endif

%changelog
* Mon Sep 23 2019 Mikhail Efremov <sem@altlinux.org> 3.9.2-alt1
- Package PowerDNS subscriber.
- pdns_recursor: Fix service name.
- Updated to 3.9.2.

* Tue Aug 20 2019 Mikhail Efremov <sem@altlinux.org> 3.9.1-alt1
- Updated to 3.9.1.

* Mon Feb 18 2019 Mikhail Efremov <sem@altlinux.org> 3.9.0-alt3
- dnsmasq: Fix first start.

* Tue May 08 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.9.0-alt2
- Rebuilt with pdnsd subscriber subpackage.

* Mon Jan 09 2017 Mikhail Efremov <sem@altlinux.org> 3.9.0-alt1
- Updated to 3.9.0.

* Fri Jun 10 2016 Mikhail Efremov <sem@altlinux.org> 3.8.1-alt1
- man: Drop note about /etc/net/ifaces/lo.
- Updated to 3.8.1.

* Wed Apr 13 2016 Mikhail Efremov <sem@altlinux.org> 3.8.0-alt1
- Drop resolvconf-restartcmd.
- Simplify detect_init().
- Updated to 3.8.0.

* Thu Feb 25 2016 Mikhail Efremov <sem@altlinux.org> 3.7.3-alt1
- Fix search string with multiple domains.
- Updated to 3.7.3.

* Wed Oct 28 2015 Mikhail Efremov <sem@altlinux.org> 3.7.1-alt1
- Fix --help option.
- Updated to 3.7.1.

* Tue May 05 2015 Mikhail Efremov <sem@altlinux.org> 3.7.0-alt1
- Updated to 3.7.0.

* Wed Nov 05 2014 Mikhail Efremov <sem@altlinux.org> 3.6.1-alt1
- Updated to 3.6.1.

* Thu Oct 23 2014 Mikhail Efremov <sem@altlinux.org> 3.6.0-alt1
- Updated to 3.6.0.

* Mon Jul 21 2014 Mikhail Efremov <sem@altlinux.org> 3.5.7-alt1
- Updated to 3.5.7.

* Tue Jul 16 2013 Mikhail Efremov <sem@altlinux.org> 3.5.6-alt1
- Updated to 3.5.6.

* Mon Jun 17 2013 Mikhail Efremov <sem@altlinux.org> 3.5.5-alt1
- Updated to 3.5.5.

* Mon May 13 2013 Mikhail Efremov <sem@altlinux.org> 3.5.4-alt4
- resolvconf-restartcmd: Use sd_booted utility.
- resolvconf-restartcmd: Don't use absolute paths for commands.

* Thu Mar 07 2013 Mikhail Efremov <sem@altlinux.org> 3.5.4-alt3
- Updated test script.
- Own auto generated files.
- dnsmasq.in: Don't check files existence.
- Use /etc/dnsmasq.conf.d for auto-generated dnsmasq config.

* Tue Jan 29 2013 Mikhail Efremov <sem@altlinux.org> 3.5.4-alt2
- Fix rundir.

* Tue Jan 29 2013 Mikhail Efremov <sem@altlinux.org> 3.5.4-alt1
- Added resolvconf-restartcmd script.
- Updated tests.
- Fix resolvconf.conf(5) man page.
- Fix 'metric changed' logic.
- Updated to 3.5.4.

* Tue May 22 2012 Mikhail Efremov <sem@altlinux.org> 3.4.2-alt2
- Skip backup files in hooks directories.

* Thu Jul 07 2011 Mikhail Efremov <sem@altlinux.org> 3.4.2-alt1
- Set PATH before subscribers call.
- libc subscriber: Don't use hardcoded path.
- Updated to 3.4.2.

* Mon Apr 04 2011 Mikhail Efremov <sem@altlinux.org> 3.4.1-alt1
- Use service nscd restart instead of reload.
- Check for nscd service presence and running (closes: #25375).
- Updated to 3.4.1.

* Tue Nov 23 2010 Mikhail Efremov <sem@altlinux.org> 3.4.0-alt1
- Update tests.
- Drop old logic for 127.* based on LIBC_NAMESERVERS variable,
    use upstream's LOCALNAMESERVERS instead.
- Updated to 3.4.0.

* Mon Sep 27 2010 Mikhail Efremov <sem@altlinux.org> 3.3.6-alt1
- 3.3.6

* Tue Jun 15 2010 Mikhail Efremov <sem@altlinux.org> 3.3.5-alt1
- add note about name_servers to man page.
- add interface_order and dynamic_order to resolvconf.conf.
- drop comments about name_servers from resolvconf.conf.
- add 'metric changed' test.
- Not skip resolv.conf generating if metric is changed.
- 3.3.5

* Wed Dec 09 2009 Mikhail Efremov <sem@altlinux.org> 3.3.4-alt2
- move subscribers to separate packages.

* Mon Dec 07 2009 Mikhail Efremov <sem@altlinux.org> 3.3.4-alt1
- 3.3.4

* Mon Nov 23 2009 Mikhail Efremov <sem@altlinux.org> 3.3.3-alt1
- 3.3.3

* Wed Nov 04 2009 Mikhail Efremov <sem@altlinux.org> 3.3.2-alt7
- use condrestart for dnsmasq service.

* Tue Oct 06 2009 Mikhail Efremov <sem@altlinux.org> 3.3.2-alt6
- remove /etc/hooks/resolv.conf.d from %files.
- use 'test' script when package building.

* Thu Jul 23 2009 Mikhail Efremov <sem@altlinux.org> 3.3.2-alt5
- fixed adding nameservers to LIBC_NAMESERVERS variable (closes: #20854)

* Wed Jul 22 2009 Mikhail Efremov <sem@altlinux.org> 3.3.2-alt4
- Using separate variable LIBC_NAMESERVERS with '127.*' nameservers
    for libc subscriber.
- added resolv.conf head message.

* Mon Jun 22 2009 Mikhail Efremov <sem@altlinux.org> 3.3.2-alt3
- added dnsmasq subscriber configuration files to resolvconf.conf.
- dnsmasq subscriber: not to do anything if files does not exist.
- use 'condreload' command for dnsmasq restart
- added 'lo.*' to default interface_order.

* Wed Jun 10 2009 Mikhail Efremov <sem@altlinux.org> 3.3.2-alt2
- Allow 'nameserver 127.0.0.1' from all interfaces (closes: #20345).

* Tue Jun 02 2009 Mikhail Efremov <sem@altlinux.org> 3.3.2-alt1
- 3.3.2

* Tue May 19 2009 Mikhail Efremov <sem@altlinux.org> 3.3-alt2
- fixed dnsmasq restart.

* Fri Apr 24 2009 Mikhail Efremov <sem@altlinux.org> 3.3-alt1
- 3.3

* Mon Apr 20 2009 Mikhail Efremov <sem@altlinux.org> 3.2-alt2
- fixed FILES section in man page.

* Mon Apr 20 2009 Mikhail Efremov <sem@altlinux.org> 3.2-alt1
- 3.2

* Mon Mar 30 2009 Mikhail Efremov <sem@altlinux.org> 3.1.1-alt3
- fix service restarting

* Mon Mar 23 2009 Mikhail Efremov <sem@altlinux.org> 3.1.1-alt2
- some minor changes in dnsmasq and named subscribers scripts.
- Set more quotes, masquerade dnsmasq and dbus-tools deps (thx raorn@).

* Fri Mar 20 2009 Mikhail Efremov <sem@altlinux.org> 3.1.1-alt1
- 3.1.1 

* Mon Mar 16 2009 Stanislav Ievlev <inger@altlinux.org> 2.0.1-alt2
- Build for Sisyphus

* Wed Feb 25 2009 Mikhail Efremov <sem@altlinux.org> 2.0.1-alt1
- initial build

