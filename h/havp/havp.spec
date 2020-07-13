Name: havp
Version: 0.93
Release: alt1

Summary: (HTTP Antivirus Proxy) is a proxy with anti-virus scanner

License: GPL-2.0-only
Group: System/Servers

Url: http://www.havp.org/
Source: http://www.havp.org/download/%name-%version.tar.gz
Source1: havp.init
Source2: havp_spool_disk.config
Source3: havp_README.ALT.txt

Patch0: havp-0.93-alt.patch

Summary(ru_RU.UTF8): Прокси сервер с антивирусным сканированием трафика

Requires: clamav-freshclam

BuildPreReq: libssl-devel zlib-devel
# Automatically added by buildreq on Wed Jun 13 2007
BuildRequires: gcc-c++ libclamav-devel

%description
The main aims are continuous, non-blocking downloads and smooth scanning 
of dynamic and password protected HTTP traffic. Havp antivirus proxy has 
a parent and transparent proxy mode. It can be used with squid or standalone.

%description -l ru_RU.UTF8
Основная цель: - прозрачное антивирусное сканирование HTTP трафика.
Может работать как родительский или прозрачный прокси сервер.
Может использоваться со сквидом или автономно.
Поддерживает такие антивирусы:
 - ClamAV through libclamav (используется по умолчанию)
 - ClamAV through clamd
 - Kaspersky (aveserver daemon)
 - Trend Micro (Trophie)
 - AVG
 - F-Prot
 - NOD32
 - Sophos (необходима пересборка с библиотекой)
 
%prep
%setup -q
%patch0 -p1

find %_builddir/%name-%version/etc/%name -type d -print0 | xargs -r0 chmod 755
find %_builddir/%name-%version/etc/%name -type f -print0 | xargs -r0 chmod 644

%build
%configure --localstatedir=/var --enable-ssl-tunnel
%make_build

%install
%make DESTDIR=%buildroot install
%__mkdir_p %buildroot%_logdir/%name
%__mkdir_p %buildroot%_spooldir/%name
%__mkdir_p %buildroot%_var/run/%name
%__mkdir_p %buildroot%_initrddir
%__mkdir_p %buildroot%_sysconfdir/logrotate.d


%__install -p -m 755 %SOURCE1  %buildroot%_initrddir/havp
%__install -p -m 640 etc/havp/havp.config %buildroot%_sysconfdir/%name/havp.config
%__install -p -m 640 %SOURCE2  %buildroot%_sysconfdir/%name/spool_disk.config
%__install -p -m 644 %SOURCE3  README.ALT

%__cat << EOF > %buildroot%_sysconfdir/logrotate.d/havp
/var/log/havp/access.log {
    create 644 root havp
    weekly
    rotate 5
    copytruncate
    compress
    notifempty
    missingok
}
/var/log/havp/havp.log {
    create 644 root havp
    weekly
    rotate 5
    copytruncate
    compress
    notifempty
    missingok
    postrotate
        /sbin/service havp reload >/dev/null
    endscript
}
EOF


%pre
/usr/sbin/groupadd -r -f %name &> /dev/null ||:
/usr/sbin/useradd -r -g %name -d /dev/null -c 'Proxy with antivirus scan' -s /dev/null -n %name &> /dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%postun

%files
%doc ChangeLog INSTALL COPYING README.ALT
%_sbindir/*
%config %_initrddir/%name
%config %_sysconfdir/logrotate.d/*
%_sysconfdir/%name/%name.config.default
%config(noreplace) %verify(not md5 size mtime) %_sysconfdir/%name/%name.config
%config(noreplace) %verify(not md5 size mtime) %_sysconfdir/%name/spool_disk.config
%config(noreplace) %verify(not md5 size mtime) %_sysconfdir/%name/whitelist
%config(noreplace) %verify(not md5 size mtime) %_sysconfdir/%name/blacklist
%config(noreplace) %verify(not md5 size mtime) %_sysconfdir/%name//templates/*/*
%dir %_sysconfdir/%name/templates
%dir %_sysconfdir/%name/templates/*
%dir %attr(750,root,%name) %_sysconfdir/%name
%dir %attr(775,root,%name) %_var/run/%name
%dir %attr(2770,root,%name) %_spooldir/%name
%dir %attr(3770,%name,root) %_logdir/%name

%changelog
* Tue Jun 09 2020 Sergey Y. Afonin <asy@altlinux.org> 0.93-alt1
- 0.93 (added support for ClamAV 0.101)
- removed Packager tag
- updated License tag to SPDX syntax
- updated URL

* Thu Dec 03 2015 Sergey Y. Afonin <asy@altlinux.ru> 0.92-alt2
- NMU: rebuilt with new libclamav
- applied security fix from 0.92a

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.92-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Jul 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.92-alt1
- Update to 0.92
  + Add SCANMIME and SKIPMIME options
  + Add TIMEFORMAT option
  + Add VIRUSLOG option
  + Add PARENTUSER/PARENTPASSWORD (thanks to James Brotchie)
  + DISABLELOCKINGFOR default has changed in favor of ClamAV 0.96,
    it only contains AVG:ALL now

* Tue Jul 20 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.91-alt2
- Remove packages-info-i18n-common

* Tue Aug 11 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.91-alt1
- Update to 0.91
  + Fix possible segfault on dns lookups (thanks Gavin McCullagh)
  + Fix compiling with gcc 4.4
  + Support AVG version 8.5 (default AVGPORT 54322) (thanks Markus Wigge)

* Thu Jun 25 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.90-alt2
- Rebuild with new clamav

* Mon May 11 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.90-alt1
- Update to 0.90
  + ClamAV library 0.95 support (recompile needed)
  + Support NOD32 version 3 (set NOD32VERSION 30 in config)
  + Add PRELOADZIPHEADER config (Squid 3.x might not work if enabled)
  + Add SYSLOGVIRUSLEVEL config
- Switch to git
- Fix build with gcc4.4

* Thu Sep 11 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.89-alt1
- Update to 0.89
  + Fix possible retry loop and hang (thanks to Peter Warasin @ endian.it)
  + Always send Via: header, fixes some IIS problems (e.g. MSNBC)
- Convert spec to UTF8

* Thu Apr 17 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.88-alt1
- Update to 0.88
  + ClamAV library 0.93 support (new option CLAMMAXSCANSIZE)
  + CLAMMAXFILESIZE default is now 100MB (so 0.93 even starts scanning big files)
  + Fix random seed issue (ClamAV generated some temporary file errors)
  + Added DISABLELOCKINGFOR config (fix for ZIP handling in ClamAV 0.93)
  + Arcavir version 2008 support (set ARCAVIRVERSION)
  + Log scanner errors to errorlog
  + Relaxed SSL/CONNECT port limits
    (It is _not_ recommended to use --enable-ssl-tunnel, you should use Squid)
- Convert README.ALT from koi8-r to utf8

* Tue Feb 19 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.87-alt1
- Update %name-%version-alt.patch
- Update to 0.87
  + DrWeb scanner support
  + F-Prot support for v6.0 added (also check FPROTOPTIONS)
  + If false, X_FORWARDED_FOR drops also Via: header for privacy
  + Fix Avast and AVG bugs
  + Templates support <!--url--> and <!--clientip--> tags
  + Uses supplementary groups for user if defined
  + Added TRICKLINGBYTES config
  + Reduced *MAXFILES settings to 50 for performance
  + Add missing HTTP methods (MKACTIVITY, CHECKOUT, MERGE)

* Wed Jun 13 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.86-alt1
- Update to 0.86
- Add patch %name-%version-alt.patch
- Move %_datadir/templates to %_sysconfdir/%name/
  + Experimental support for chunked Transfer-Encoding, fixes some broken sites
  + Added IGNOREVIRUS config for whitelisting virus names
  + Added CLAMBLOCKBROKEN config
  + HAVP is killed if database reloading fails for Library Scanner
  + Log URL when crashed scanner process detected, for troubleshooting
  + Build system updated (--prefix --sbindir --sysconfdir --localstatedir)

* Thu Mar 01 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.85-alt1
- Add --prefix=/ in %%configure

* Wed Feb 28 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.85-alt0
- Update to 0.85
  + Added support for ClamAV 0.90 library

* Thu Jan 25 2007 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.84-alt0
- Update to 0.84
  + Fix bug in tcp buffer, requests could leak to other clients sometimes
  + Support for multiple IPs in hostnames, all are tried if necessary
  + Pass Proxy-Authorization header to parent proxy (thanks Mateus)
  + Ignore scanner errors if MAXSCANSIZE reached (thanks Vittorio)
  + Default for MAXSCANSIZE 5000000, not suggested to be 0 anymore

* Thu Dec 21 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.83-alt1
- Change Requires: clamav -> clamav-freshclam

* Thu Oct 19 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.83-alt0
- Update to 0.83
- Fix #10159, #10162

* Fri Sep 15 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.82-alt0
- Update to 0.82
- Improved ZIP handling (header pre-fetch, scans ZIPs larger than MAXSCANSIZE)
- Added SCANIMAGES config
- Ignore RAR errors from clamd
- Fixes to HTTP header handling
- Added syslog logging option
- Signal HUP re-opens logfiles, making rotation possible
- Fixed binding to low ports (<1024)
- Fixed FreeBSD, downloads that took longer than TRICKLING did not work
- Experimental FreeBSD support (no mandatory locking, KEEPBACK not supported!)
- Avast! scanner support
- Added MAXDOWNLOADSIZE config
- Added X_FORWARD_FOR config to control the header
- Added some archive scanning parameters for Trophie
- Added TCP support for clamd
- Ignore RAR errors from ClamAV (use ClamAV-devel if you want to scan RARv3)
- Fixed bug in socket buffer, sometimes caused nasty effects with POST etc.
- Fixed KeepAlive for HTTP/1.1 clients, now on by default
- Access logging format changed a bit

* Mon Apr 10 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.79-alt0
- update to 0.79
- MULTIPLE SCANNER SUPPORT! (see havp.config how to enable scanners)
- NOD32, Sophos and Clamd scanner support
- Parentproxy error on SSL tunneling is passed to browser
- Whitelisted sites can use HTTP Range requests (for Windowsupdate..)
- Added STREAMUSERAGENT/STREAMSCANSIZE config to reduce stream scanning
- Added SCANNERTIMEOUT option to catch scanners gone wild
- Added scanning options for ClamLib

* Thu Mar 30 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.78-alt1
- Change BIND_ADDRESS "NULL" to BIND_ADDRESS "127.0.0.1" as default
- Change stop priority to 9

* Tue Mar 14 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.78-alt0
- update to 0.78
- Added TEMPDIR, LOGLEVEL, FAILSCANERROR and WHITELISTFIRST config
- KEEPBACKTIME config added to complement KEEPBACKBUFFER setting
- Basic HTTP Keep-Alive support, improves network performance
- HTTPS/SSL tunneling support
- FTP is supported when FTP supporting parent proxy is used
- Logging improved
- Added reload-lists in %_initrddir/%name

* Mon Mar 06 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.77-alt1
- Add mount in loop
- Add REDME.ALT

* Wed Mar 01 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.77-alt0
- initial build
