# hey Emacs, its -*- mode: rpm-spec; coding: cp1251; -*-

## Things users may want to change
#
# User (and group) name under which the Tor daemon runs
%define toruser _tor

# Root directory for chrooted environment, must not be
# same as real system root.
%define _tor_root %_localstatedir/%name

Name: tor
Version: 0.4.3.6
Release: alt1

Summary: Anonymizing overlay network for TCP (The onion router)
Group: System/Servers
License: BSD-3-Clause
Url: http://tor.eff.org/

Source0: http://tor.eff.org/dist/%name-%version.tar
Source1: %name.init
Source2: %name.systemd.service
Source3: %name.tmpfiles

# Automatically added by buildreq on Fri Jun 24 2011
# optimized out: fontconfig fonts-type1-urw ghostscript-classic libcom_err-devel libkrb5-devel tex-common texlive-base texlive-base-bin texlive-common texlive-latex-base texlive-latex-recommended
BuildRequires: ghostscript-common libevent-devel libssl-devel texlive-fonts-recommended texlive-generic-recommended transfig zlib-devel
BuildRequires: libcap-devel libsystemd-devel liblzma-devel libzstd-devel
%ifarch %ix86 x86_64 aarch64
BuildRequires: libseccomp-devel
%endif

%description
Tor is a connection-based low-latency anonymous communication system.
This package provides the "tor" program, which serves as both a client
and a relay node.

Applications connect to the local Tor proxy using the SOCKS
protocol. The local proxy chooses a path through a set of relays, in
which each relay knows its predecessor and successor, but no
others. Traffic flowing down the circuit is unwrapped by a symmetric
key at each relay, which reveals the downstream relay.

Warnings: Tor does no protocol cleaning.  That means there is a danger
that application protocols and associated programs can be induced to
reveal information about the initiator. Tor depends on Privoxy and
similar protocol cleaners to solve this problem. This is alpha code,
and is even more likely than released code to have anonymity-spoiling
bugs. The present network is very small -- this further reduces the
strength of the anonymity provided. Tor is not presently suitable
for high-stakes anonymity.

%prep
%setup

# Set default configuration values
sed -i 's:^#Log notice file.*:Log notice file %_var/log/%name/%name.log:' src/config/torrc.sample.in
sed -i 's:^#DataDirectory.*:DataDirectory %_var/cache/%name:' src/config/torrc.sample.in

%build
%configure --with-tor-user=%{toruser} --with-tor-group=%{toruser} --localstatedir=/var
%make_build

%install
%makeinstall_std

install -pD -m755 %SOURCE1 %buildroot/%_initdir/%name
mv %buildroot/%_sysconfdir/%name/torrc.sample %buildroot/%_sysconfdir/%name/torrc
mkdir -p %buildroot%_tor_root
mkdir -p %buildroot%_var/{cache/%name,log/%name,run/%name}
mkdir -p %buildroot%_tmpfilesdir

install -D -p -m 0644 %SOURCE2 %buildroot/%_unitdir/%{name}.service
sed 's/@TOR_USER@/%toruser/g' %SOURCE3 > %buildroot%_tmpfilesdir/%name.conf

mkdir -p %buildroot%_sysconfdir/logrotate.d
cat >%buildroot%_sysconfdir/logrotate.d/%name <<__EOF__
%_var/log/%name/*log {
	weekly
	rotate 5
	compress
	missingok
	notifempty
	sharedscripts
	postrotate
		%_initdir/%name condreload >/dev/null
	endscript
}
__EOF__

# Chroot config
#mkdir -p %buildroot%_tor_root{/lib,%_var/{nis,yp/binding,log},%_sysconfdir/%name}

%pre
/usr/sbin/groupadd -r -f %toruser
/usr/sbin/useradd -r -g %toruser -d %_tor_root -s /dev/null -c 'Tor user' %toruser >/dev/null 2>&1 ||:
if [ $1 -gt 1 ]; then
	chown %toruser:auth /etc/tcb/%toruser
	/usr/sbin/usermod -d %_tor_root %toruser
fi

%post
#%_sysconfdir/chroot.d/%name.all force
%post_service %name

%preun
%preun_service %name

#if [ $1 = 0 ]; then
#	rm -f %_tor_root/lib/* %_tor_root/var/yp/binding/*
#fi

%define docdir %_docdir/%name

%files
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/torrc
%config %_sysconfdir/logrotate.d/%name
%{_unitdir}/%{name}.service
%_bindir/tor
%_bindir/tor-print-ed-signing-cert
# torify is moved to torsocks package to avoid automatic dependency on it
%exclude %_bindir/torify
%_bindir/tor-resolve
%_bindir/tor-gencert
%_man1dir/*.1.*
%_initdir/%name
%_tmpfilesdir/%name.conf
%dir %_datadir/%name
%_datadir/%name/geoip
%_datadir/%name/geoip6
%doc README LICENSE ChangeLog INSTALL doc/HACKING
%dir %docdir
%docdir/*.html


%defattr(640,root,%toruser,2710)
%_tor_root
%defattr(640,root,%toruser,3770)
%_var/log/%name
%defattr(640,root,%toruser,2730)
%_var/run/%name
%defattr(640,%toruser,%toruser,2700)
%_var/cache/%name

%changelog
* Thu Jul 9 2020 Vladimir Didenko <cow@altlinux.ru> 0.4.3.6-alt1
- new version (fixes CVE-2020-15572)

* Fri May 15 2020 Vladimir Didenko <cow@altlinux.ru> 0.4.3.5-alt1
- new version

* Wed Mar 18 2020 Vladimir Didenko <cow@altlinux.ru> 0.4.2.7-alt1
- new version (fixes CVE-2020-10592)

* Sat Feb 22 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.4.2.6-alt2
- build against libcap, libsystemd, liblzma and libzstd
- build against libseccomp on ix86, x86_64 and aarch64
- spec:
  + update license field according to SPDX format
  + remove packager field

* Thu Jan 30 2020 Vladimir Didenko <cow@altlinux.ru> 0.4.2.6-alt1
- new version

* Tue Dec 10 2019 Vladimir Didenko <cow@altlinux.ru> 0.4.2.5-alt1
- new version
- fix license name

* Thu Sep 19 2019 Vladimir Didenko <cow@altlinux.ru> 0.4.1.6-alt1
- new version

* Thu Sep 5 2019 Vladimir Didenko <cow@altlinux.ru> 0.4.1.5-alt1
- new version

* Mon May 6 2019 Vladimir Didenko <cow@altlinux.ru> 0.4.0.5-alt1
- new version

* Fri Feb 22 2019 Vladimir Didenko <cow@altlinux.ru> 0.3.5.8-alt1
- new version (fixes: CVE-2019-8955)

* Wed Jan 9 2019 Vladimir Didenko <cow@altlinux.ru> 0.3.5.7-alt1
- new version

* Fri Nov 23 2018 Vladimir Didenko <cow@altlinux.ru> 0.3.4.9-alt1
- new version

* Tue Sep 11 2018 Vladimir Didenko <cow@altlinux.ru> 0.3.4.8-alt1
- new version
- get rid of ubt macros

* Thu Aug 30 2018 Grigory Ustinov <grenka@altlinux.org> 0.3.3.9-alt1.S1.1
- NMU: Rebuild with new openssl 1.1.0.

* Mon Jul 16 2018 Vladimir Didenko <cow@altlinux.ru> 0.3.3.9-alt1%ubt
- new version

* Wed May 23 2018 Vladimir Didenko <cow@altlinux.ru> 0.3.3.6-alt1%ubt
- new version

* Tue Mar 13 2018 Vladimir Didenko <cow@altlinux.ru> 0.3.2.10-alt1%ubt
- new version (Fixes: CVE-2018-0491)

* Fri Jan 26 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.3.2.9-alt2%ubt
- add tmpfiles.d conf (fix service startup)

* Fri Jan 12 2018 Vladimir Didenko <cow@altlinux.ru> 0.3.2.9-alt1%ubt
- new version

* Fri Dec 1 2017 Vladimir Didenko <cow@altlinux.ru> 0.3.1.9-alt1%ubt
- new version (Fixes: CVE-2017-8819, CVE-2017-8820, CVE-2017-8821,
CVE-2017-8822, CVE-2017-8823)

* Fri Oct 27 2017 Vladimir Didenko <cow@altlinux.ru> 0.3.1.8-alt1%ubt
- new version

* Mon Sep 18 2017 Vladimir Didenko <cow@altlinux.ru> 0.3.1.7-alt1%ubt
- new version (Fixes: CVE-2017-0380)

* Wed Aug 2 2017 Vladimir Didenko <cow@altlinux.ru> 0.3.0.10-alt1%ubt
- new version

* Fri Jun 30 2017 Vladimir Didenko <cow@altlinux.ru> 0.3.0.9-alt1%ubt
- new version (Fixes: CVE-2017-0377)

* Thu Jun 8 2017 Vladimir Didenko <cow@altlinux.ru> 0.3.0.8-alt1%ubt
- new version

* Tue May 16 2017 Vladimir Didenko <cow@altlinux.ru> 0.3.0.7-alt1%ubt
- new version

* Fri Apr 28 2017 Vladimir Didenko <cow@altlinux.ru> 0.3.0.6-alt1%ubt
- new version

* Mon Mar 6 2017 Vladimir Didenko <cow@altlinux.ru> 0.2.9.10-alt1%ubt
- new version

* Tue Jan 24 2017 Vladimir Didenko <cow@altlinux.ru> 0.2.9.9-alt1%ubt
- new version

* Tue Dec 20 2016 Vladimir Didenko <cow@altlinux.ru> 0.2.9.8-alt1%ubt
- new version

* Fri Dec 09 2016 Anton Farygin <rider@altlinux.ru> 0.2.8.11-alt1%ubt
- new version
- %%ubt macros added for easy backporting to stable branches

* Fri Dec 2 2016 Vladimir Didenko <cow@altlinux.ru> 0.2.8.10-alt1
- new version

* Tue Oct 18 2016 Vladimir Didenko <cow@altlinux.ru> 0.2.8.9-alt1
- new version that fixes security issue (closes: #32634)

* Tue Oct 4 2016 Vladimir Didenko <cow@altlinux.ru> 0.2.8.8-alt1
- new version

* Thu Aug 4 2016 Vladimir Didenko <cow@altlinux.ru> 0.2.8.6-alt3
- don't run unit tests (requires IPv6 support)

* Thu Aug 4 2016 Vladimir Didenko <cow@altlinux.ru> 0.2.8.6-alt2
- print log of failed test

* Wed Aug 3 2016 Vladimir Didenko <cow@altlinux.ru> 0.2.8.6-alt1
- new version

* Tue Dec 15 2015 Vladimir Didenko <cow@altlinux.ru> 0.2.7.6-alt2
- add sticky bit on log directory

* Mon Dec 14 2015 Vladimir Didenko <cow@altlinux.ru> 0.2.7.6-alt1
- new version

* Mon Jul 13 2015 Vladimir Didenko <cow@altlinux.ru> 0.2.6.10-alt1
- new version

* Fri Jun 12 2015 Vladimir Didenko <cow@altlinux.ru> 0.2.6.9-alt1
- new version

* Thu Apr 9 2015 Vladimir Didenko <cow@altlinux.ru> 0.2.5.12-alt1
- new version

* Wed Mar 25 2015 Vladimir Didenko <cow@altlinux.ru> 0.2.5.11-alt1
- new version

* Wed Dec 24 2014 Vladimir Didenko <cow@altlinux.ru> 0.2.5.10-alt2
- don't pack torify (moved to torsocks package)

* Fri Dec 05 2014 Vladimir Didenko <cow@altlinux.ru> 0.2.5.10-alt1
- new version
- systemd support

* Mon Oct 07 2013 Anton Farygin <rider@altlinux.ru> 0.2.3.25-alt1
- new version

* Fri Jun 24 2011 Dmitry V. Levin <ldv@altlinux.org> 0.2.1.30-alt1
- Blindly updated 0.2.1.30 (fixes numerous bugs including CVE-2011-0427).
- Updated build dependencies.

* Tue Dec 07 2010 Mykola Grechukh <gns@altlinux.ru> 0.2.1.27-alt2
- new version. Rebuilt with openssl-1.0b

* Fri Sep 24 2010 Mykola Grechukh <gns@altlinux.ru> 0.2.1.26-alt2
- added torify

* Wed Jun 09 2010 Mykola Grechukh <gns@altlinux.ru> 0.2.1.26-alt1
- updated to 0.2.1.26

* Tue Jun 30 2009 Sviatoslav Sviridov <svd@altlinux.ru> 0.2.0.35-alt2
- Added directory /usr/share/tor to file list

* Mon Jun 29 2009 Sviatoslav Sviridov <svd@altlinux.ru> 0.2.0.35-alt1
- Updated to 0.2.0.35
- Packaged files:
  + /usr/bin/tor-gencert
  + /usr/share/tor/geoip

* Wed Sep 10 2008 Sviatoslav Sviridov <svd@altlinux.ru> 0.2.0.31-alt1
- Updated to 0.2.0.31

* Sun Sep 02 2007 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.2.17-alt1
- Updated to 0.1.2.17

* Thu Aug 09 2007 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.2.16-alt1
- Updated to 0.1.2.16
  + Major security fixes: close immediately after missing authentication
    on control port; do not allow multiple authentication attempts.

* Tue Jul 24 2007 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.2.15-alt1
- Updated to 0.1.2.15

* Sun May 27 2007 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.2.14-alt1
- Updated to 0.1.2.14
- Packaged more tor specs

* Sun Dec 17 2006 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.1.26-alt1
- Updated to 0.1.1.26

* Sun Dec 10 2006 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.1.25-alt1
- Updated to 0.1.1.25

* Tue Oct 10 2006 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.1.24-alt1
- Updated to 0.1.1.24
- Removed doc files (disappeared in upstream): doc/CLIENTS, doc/FAQ,
  doc/tor-doc.css, doc/tor-doc.html

* Wed May 24 2006 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.1.20-alt1
- Updated to 0.1.1.20 (first stable release of the 0.1.1.x branch)

* Sun Feb 19 2006 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.0.17-alt1
- Updated to 0.1.0.17

* Wed Jan 04 2006 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.0.16-alt1
- Updated to 0.1.0.16

* Mon Oct 10 2005 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.0.15-alt1
- Updated to 0.1.0.15

* Sat Aug 27 2005 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.0.14-alt1
- Updated to 0.1.0.14

* Wed Jul 13 2005 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.0.11-alt1
- First build for ALT Linux
- Known problems:
  + service is not being chrooted
