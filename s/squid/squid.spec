
%def_disable poll
%def_enable epoll
%def_enable ecap
%def_enable esi
%def_with nettle
# gnutls for squidclient
%def_with gnutls
%def_with systemd

Name: squid
Version: 4.13
Release: alt1
%define langpack_ver 20170901 
Summary: The Squid proxy caching server
License: GPLv2
Group: System/Servers
Url: http://www.squid-cache.org/
Source0: %name-%version.tar
Source1: %name-langpack-%langpack_ver.tar
Source2: %name.init
Source3: %name.logrotate
Source4: wbinfo_group.sh
Source5: %name.sysconfig
Source6: %name.pam
Source7: %name.service
Source8: %name.tmpfiles

Patch: %name-%version-%release.patch
Obsoletes: %name-novm %name-pinger
Requires: net-snmp-mibs
Provides: %name-common = %version-%release
Obsoletes: %name-common
Provides: %name-server = %version-%release
Obsoletes: %name-server
Provides: %name-cachemgr = %version-%release
Obsoletes: %name-cachemgr
Conflicts: %name-conf-host2cat < 1.01-alt5
Provides: %name-conf-default = %version-%release
Obsoletes: %name-conf-default

# epoll is enabled by default, so disable it if plain poll is enabled
%{?_enable_poll:%force_disable epoll}

BuildConflicts: bind-devel
BuildRequires(pre): rpm-build >= 4.0.4-alt10

# Automatically added by buildreq on Fri Nov 30 2018 (-bb)
# optimized out: ca-trust cppunit ed elfutils glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libcom_err-devel libcrypt-devel libnfnetlink-devel libp11-kit libsasl2-3 libstdc++-devel perl perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-parent perl-podlators pkg-config python-base sh3 xz
# BuildRequires: cppunit-devel doxygen gcc-c++ libcap-devel libdb4-devel libecap-devel libexpat-devel libgnutls-devel libkrb5-devel libldap-devel libltdl7-devel libnetfilter_conntrack-devel libnettle-devel libpam-devel libsasl2-devel libssl-devel libxml2-devel linuxdoc-tools perl-Crypt-OpenSSL-X509 perl-DBI perl-Digest-SHA perl-Pod-Usage perl-URI samba-client samba-winbind-clients

BuildRequires: cppunit-devel doxygen gcc-c++ libcap-devel libdb4-devel libkrb5-devel libldap-devel libltdl7-devel libnetfilter_conntrack-devel libpam-devel libsasl2-devel libssl-devel linuxdoc-tools perl-Crypt-OpenSSL-X509 perl-DBI perl-Digest-SHA perl-Pod-Usage perl-URI samba-client samba-winbind-clients
%{?_enable_ecap:BuildRequires: libecap-devel >= 1.0}
%{?_enable_esi:BuildRequires: libxml2-devel libexpat-devel}
%{?_with_nettle:BuildRequires: libnettle-devel}
%{?_with_gnutls:BuildRequires: libgnutls-devel >= 3.1.5}
%{?_with_systemd:BuildRequires: libsystemd-devel}

%description
Squid is a high-performance proxy caching server for Web clients,
supporting FTP, gopher, and HTTP data objects. Unlike traditional
caching software, Squid handles all requests in a single,
non-blocking, I/O-driven process. Squid keeps meta data and especially
hot objects cached in RAM, caches DNS lookups, supports non-blocking
DNS lookups, and implements negative caching of failed requests.


%package doc
Summary: Squid documantation
Group: Documentation
Conflicts: %name < 3.1.22-alt3
BuildArch: noarch

%description doc
Squid is a high-performance proxy caching server for Web clients,
supporting FTP, gopher, and HTTP data objects. Unlike traditional
caching software, Squid handles all requests in a single,
non-blocking, I/O-driven process. Squid keeps meta data and especially
hot objects cached in RAM, caches DNS lookups, supports non-blocking
DNS lookups, and implements negative caching of failed requests.
Install squid if you need a proxy caching server.

This package contains documentation for Squid.


%package helpers
Summary: Squid helpers
Group: System/Servers
Requires: %name = %version-%release
Provides: %name-helpers-perl = %version-%release
Obsoletes: %name-helpers-perl

%description helpers
This package contains Squid helpers for different kinds of authentication.


%prep
%setup -q %{?langpack_ver:-a 1}
%patch -p1

sed -i -r '1s|^(#!/usr/)local(/bin/perl)|\1\2|' {contrib,scripts}/*.pl

RELEASE_TIME="$(date +%%s)"

sed -i -e "s|%version-VCS|%version|" configure.ac
sed -i -e "s|squid_curtime|$RELEASE_TIME|" include/version.h

%build
%define _localstatedir %_var
%add_optflags %optflags_shared
./bootstrap.sh
%configure \
	--disable-arch-native \
	--bindir=%_sbindir \
	--libexecdir=%_libexecdir/%name \
	--sysconfdir=%_sysconfdir/%name \
	--datadir=%_datadir/%name \
	--with-logdir=%_logdir/%name \
	--with-swapdir=%_localstatedir/spool/%name \
	--enable-strict-error-checking \
	--with-dl \
	--with-pthreads \
	--with-aio \
	--with-openssl \
	--with-libcap \
	--enable-forw-via-db \
%if_enabled debug
	--with-valgrind-debug \
	--disable-optimizations --enable-debug-cbdata --enable-stacktraces --enable-cpu-profiling \
%else
	--without-valgrind-debug \
	--enable-optimizations --enable-inline --disable-debug-cbdata --disable-stacktraces --disable-cpu-profiling \
%endif
	%{subst_enable poll} \
	%{subst_enable epoll} \
	%{subst_enable esi} \
	%{subst_enable ecap} \
	%{subst_with nettle} \
	%{subst_with gnutls} \
	%{subst_with systemd} \
	--enable-ipv6 \
	--enable-unlinkd \
	--enable-cachemgr-hostname=localhost \
	--enable-follow-x-forwarded-for \
	--enable-default-hostsfile=%_sysconfdir/hosts \
	--enable-snmp \
	--enable-removal-policies="lru heap" \
	--enable-delay-pools \
	--enable-icmp \
	--enable-htcp \
	--enable-async-io=16 \
	--enable-wccp \
	--enable-wccpv2 \
	--enable-arp-acl \
	--enable-ssl-crtd \
	--enable-forw-via-db \
	--enable-useragent-log \
	--enable-referer-log \
	--disable-ident-lookups \
	--enable-carp \
	--enable-cache-digests \
	--enable-x-accelerator-vary \
	--enable-auth \
	--enable-auth-basic="DB LDAP NCSA PAM RADIUS SASL SMB SMB_LM fake getpwnam" \
	--enable-auth-ntlm="fake SMB_LM" \
	--enable-auth-digest="LDAP eDirectory file" \
	--enable-auth-negotiate="kerberos wrapper" \
	--enable-external-acl-helpers="LDAP_group delayer eDirectory_userip file_userip kerberos_ldap_group session unix_group wbinfo_group time_quota" \
	--enable-storeio="aufs diskd rock ufs" \
	--enable-disk-io \
	--enable-translation \
	--enable-default-err-language="English" \
	--enable-icap-client \
	--disable-ipfw-transparent --disable-ipf-transparent --disable-pf-transparent \
	--enable-linux-netfilter \
	--with-netfilter-conntrack \
	--enable-linux-tproxy \
	--with-large-files \
	--with-filedescriptors=65536 \
	--with-default-user="%name"


%make_build \
%ifarch mipsel
    LIBS=-latomic \
%endif
    %nil


sed -r 's/dyn/html/g;s/CALL(|ER_GRAPH)/#/' squid3.dox | doxygen -


%install
%makeinstall_std

install -pD -m 0755 %SOURCE2 %buildroot%_initddir/%name
install -pD -m 0644 %SOURCE3 %buildroot%_sysconfdir/logrotate.d/%name

install -d -m 0755 %buildroot{%_logdir,%_spooldir,%_runtimedir}/%name

install -p -m 0755 %SOURCE4 %buildroot%_libexecdir/%name/
install -d -m 0755 %buildroot%_datadir/snmp/mibs
mv %buildroot%_datadir/%name/mib.txt %buildroot%_datadir/snmp/mibs/SQUID-MIB.txt

install -pD -m 0644 %SOURCE5 %buildroot%_sysconfdir/sysconfig/%name
install -pD -m 0644 %SOURCE6 %buildroot%_sysconfdir/pam.d/%name
install -pD -m 0644 %SOURCE7 %buildroot%_unitdir/%name.service
install -pD -m 0644 %SOURCE8 %buildroot%_tmpfilesdir/%name.conf

install -d -m 0755 %buildroot%_docdir/%name-%version/{html,scripts}
#install -d -m 0755 %buildroot%_docdir/%name-%version/html/Programming-Guide
#install -p -m 0644 doc/Programming-Guide/html/*{css,html,png} %buildroot%_docdir/%name-%version/html/Programming-Guide/
#install -p -m 0644 doc/release-notes/*.html %buildroot%_docdir/%name-%version/html/
install -p -m 0644 COPYING README ChangeLog QUICKSTART SPONSORS doc/debug-sections.txt %buildroot%_docdir/%name-%version/
install -p -m 0644 scripts/*.pl %buildroot%_docdir/%name-%version/scripts/

%check
%make_build check

%post
%post_service %name

%preun
%preun_service %name

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -N -M -g %name -d %_spooldir/%name -s /dev/null %name 2>/dev/null ||:
# fixing #6321, step 1/2
%_bindir/gpasswd -a squid shadow >/dev/null ||:

chown %name:%name %_logdir/%name/*.log >/dev/null 2>&1 ||:
chmod 660 %_logdir/%name/*.log >/dev/null 2>&1 ||:

# fix conflict between symlink and dir
if [ $1 -gt 1 ]; then
  for lang in zh-cn zh-tw; do
    lang=/usr/share/squid/errors/$lang
    if [ -d $lang -a ! -L $lang ]; then
      rm -rf $lang
    fi
  done
fi

%triggerpostun -- squid < 2.4.STABLE4-alt1
[ $2 -gt 0 ] || exit 0
chown -R %name:%name %_spooldir/%name >/dev/null 2>&1 ||:

%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/COPYING
%attr(750,root,%name) %dir %_sysconfdir/%name
%attr(750,root,%name) %dir %_libexecdir/%name
%config(noreplace) %_sysconfdir/%name/*
%config(noreplace) %_sysconfdir/sysconfig/*
%_initddir/*
%_unitdir/%name.service
%_tmpfilesdir/%name.conf
%config %_sysconfdir/logrotate.d/%name
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/snmp
%_sbindir/*
%_man8dir/squid.*
%_man1dir/*
%_libexecdir/%name/log_file_daemon
%attr(4710,root,%name) %_libexecdir/%name/pinger
%_libexecdir/%name/unlinkd
%_libexecdir/%name/diskd
%attr(3770,root,%name) %dir %_logdir/%name
%attr(2770,root,%name) %dir %_spooldir/%name
%attr(2770,root,%name) %dir %_runtimedir/%name

%files doc
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/ChangeLog
%doc %_docdir/%name-%version/QUICKSTART
%doc %_docdir/%name-%version/README
%doc %_docdir/%name-%version/SPONSORS
%doc %_docdir/%name-%version/debug-sections.txt
%doc %_docdir/%name-%version/html

%files helpers
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/scripts
%_libexecdir/%name/*
%attr(640,root,auth) %config(noreplace) %_sysconfdir/pam.d/%name
# fixing #6321, step 2/2
%attr(2711,root,auth) %_libexecdir/%name/basic_pam_auth
%_man8dir/*
%exclude %_libexecdir/%name/log_file_daemon
%exclude %_libexecdir/%name/pinger
%exclude %_libexecdir/%name/unlinkd
%exclude %_libexecdir/%name/diskd
%exclude %_libexecdir/%name/cachemgr.cgi
%exclude %_man8dir/squid.*
%exclude %_man8dir/cachemgr.cgi.*

%changelog
* Sat Oct 24 2020 Alexey Shabalin <shaba@altlinux.org> 4.13-alt1
- 4.13 (Fixes: CVE-2020-15811, CVE-2020-15810, CVE-2020-24606)

* Sat Oct 24 2020 Alexey Shabalin <shaba@altlinux.org> 4.12-alt1
- 4.12 (Fixes: CVE-2020-14059, CVE-2020-14058, CVE-2020-15049)

* Fri May 01 2020 Alexey Shabalin <shaba@altlinux.org> 4.11-alt1
- 4.11 (Fixes: CVE-2019-12519, CVE-2019-12521, CVE-2020-11945)
- build with systemd sd_notify support

* Sat Mar 14 2020 Alexey Shabalin <shaba@altlinux.org> 4.10-alt1
- Updated to 4.10.
- Fixes:
  + CVE-2019-12526 Heap Overflow issue in URN processing.
  + CVE-2019-12523 Multiple issues in URI processing.
  + CVE-2019-18676 Multiple issues in URI processing.
  + CVE-2019-18677 Cross-Site Request Forgery issue in HTTP Request processing.
  + CVE-2019-18678 HTTP Request Splitting issue in HTTP message processing.
  + CVE-2019-18679 Information Disclosure issue in HTTP Digest Authentication.
  + CVE-2020-8449 Improper Input Validation issues in HTTP Request processing.
  + CVE-2020-8450 Improper Input Validation issues in HTTP Request processing.
  + CVE-2019-12528 Information Disclosure issue in FTP Gateway.
  + CVE-2020-8517 Buffer Overflow issue in ext_lm_group_acl helper.

* Mon Jul 15 2019 Alexey Shabalin <shaba@altlinux.org> 4.8-alt1
- Updated to 4.8
- Fixes:
  + CVE-2019-12854 Denial of Service issue in cachemgr.cgi
  + CVE-2019-12529 Denial of Service in HTTP Basic Authentication
  + CVE-2019-12525 Denial of Service in HTTP Digest Authentication
  + CVE-2019-12527 Heap Overflow issue in HTTP Basic Authentication
  + CVE-2019-13345 Multiple Cross-Site Scripting issues in cachemgr.cgi

* Wed Apr 03 2019 Ivan A. Melnikov <iv@altlinux.org> 4.6-alt1.0.mips1
- Link with -latomic on mipsel

* Tue Apr 02 2019 Alexey Shabalin <shaba@altlinux.org> 4.6-alt1
- Updated to 4.6

* Mon Feb 11 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.5-alt2
- Fixed build with default -Werror=return-type flag.

* Sun Jan 06 2019 Alexey Shabalin <shaba@altlinux.org> 4.5-alt1
- Updated to 4.5

* Fri Nov 30 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.4-alt2
- Cleaned up BuildRequires.

* Wed Nov 28 2018 Alexey Shabalin <shaba@altlinux.org> 4.4-alt1
- Updated to 4.4

* Tue Oct 16 2018 Alexey Shabalin <shaba@altlinux.org> 4.3-alt1
- Updated to 4.3

* Thu Aug 30 2018 Alexey Shabalin <shaba@altlinux.org> 4.2-alt1
- 4.2

* Wed Jan 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.26-alt3
- Rebuilt without NIS support.

* Fri Jul 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.26-alt2
- Fixed build with new cppunit

* Tue Jun 06 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.5.26-alt1
- Updated to 3.5.26.

* Wed Apr 12 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.5.25-alt1
- Updated to 3.5.25.

* Mon Jan 30 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.5.24-alt1
- Updated to 3.5.24.

* Mon Dec 19 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.5.23-alt1
- Updated to 3.5.23.

* Wed Oct 12 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.5.22-alt1
- Updated to 3.5.22.

* Mon Sep 12 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.5.21-alt1
- Updated to 3.5.21.

* Tue Jul 05 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.5.20-alt1
- Updated to 3.5.20.

* Mon May 09 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.5.19-alt1
- Updated to 3.5.19 (inludes fixes for CVE-2016-4553, CVE-2016-4554,
  CVE-2016-4555, CVE-2016-4556).

* Sun May 01 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.5.17-alt1
- Updated to 3.5.17.

* Fri Apr 29 2016 Andrey Cherepanov <cas@altlinux.org> 3.5.15-alt1.1
- (ldv@) Fix remove conflict directories and symlinks (ALT #31812)

* Tue Mar 15 2016 Alexey Shabalin <shaba@altlinux.ru> 3.5.15-alt1
- 3.5.15
- fix files conflict for upgrade langpack (ALT#31812)

* Sat Feb 20 2016 Alexey Shabalin <shaba@altlinux.ru> 3.5.14-alt1
- 3.5.14

* Fri Jan 22 2016 Alexey Shabalin <shaba@altlinux.ru> 3.5.13-alt1
- 3.5.13

* Tue Dec 08 2015 Mikhail Efremov <sem@altlinux.org> 3.5.12-alt2
- Rebuild with nettle-3.x.

* Tue Dec 08 2015 Alexey Shabalin <shaba@altlinux.ru> 3.5.12-alt1
- 3.5.12

* Tue Oct 20 2015 Alexey Shabalin <shaba@altlinux.ru> 3.5.10-alt1
- 3.5.10
- fixed CVE-2015-5400

* Tue Oct 20 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.5.3-alt1.1
- rebuild with c++11 abi

* Wed Apr 15 2015 Alexey Shabalin <shaba@altlinux.ru> 3.5.3-alt1
- 3.5.3

* Wed Jan 21 2015 Alexey Shabalin <shaba@altlinux.ru> 3.4.11-alt1
- 3.4.11
- update configure options
- added /var/run/squid dir to host sockets in SMP configuration

* Thu Jun 26 2014 Led <led@altlinux.ru> 3.4.6-alt1
- 3.4.6

* Wed Jun 04 2014 Led <led@altlinux.ru> 3.4.5-alt4
- upstream fixes

* Wed May 21 2014 Led <led@altlinux.ru> 3.4.5-alt3
- Fix segfault setting up server SSL connnection

* Thu May 15 2014 Led <led@altlinux.ru> 3.4.5-alt2
- upstream fixes

* Mon May 05 2014 Led <led@altlinux.ru> 3.4.5-alt1
- 3.4.5

* Tue Apr 29 2014 Led <led@altlinux.ru> 3.4.4.2-alt3
- increase default max_filedescriptors to 65536 (ALT#30040)
- fixed inverted test on CONNECT payload existence

* Sat Apr 26 2014 Led <led@altlinux.ru> 3.4.4.2-alt2
- Revert "Bug 3371: CONNECT with data sent at once loses data"

* Thu Apr 24 2014 Led <led@altlinux.ru> 3.4.4.2-alt1
- 3.4.4.2

* Tue Apr 15 2014 Led <led@altlinux.ru> 3.4.4-alt5
- upstream fixes

* Wed Apr 09 2014 Led <led@altlinux.ru> 3.4.4-alt4
- upstream updates and fixes
- with nettle

* Tue Apr 01 2014 Led <led@altlinux.ru> 3.4.4-alt3
- disabled arch-native

* Tue Apr 01 2014 Led <led@altlinux.ru> 3.4.4-alt2
- fixed Requires

* Sun Mar 30 2014 Led <led@altlinux.ru> 3.4.4-alt1
- 3.4.4 (ALT#29914)

* Sun Mar 16 2014 Led <led@altlinux.ru> 3.3.12-alt1
- 3.3.12

* Thu Feb 27 2014 Led <led@altlinux.ru> 3.3.11-alt1
- 3.3.11
- langpack 20140220

* Thu Nov 21 2013 Led <led@altlinux.ru> 3.2.13-alt7
- build with automake 1.11

* Sun Oct 06 2013 Led <led@altlinux.ru> 3.2.13-alt6
- enabled ecap (through fixed libecap-devel package)

* Fri Oct 04 2013 Led <led@altlinux.ru> 3.2.13-alt5
- provide/obsolete squid-conf-default (ALT#29426)
- disabled ecap (through broken libecap-devel package)

* Fri Aug 16 2013 Led <led@altlinux.ru> 3.2.13-alt4
- squid.init: made SQUID_EXTRA_SHUTDOWN_TIMEOUT configurable

* Wed Aug 14 2013 Led <led@altlinux.ru> 3.2.13-alt3
- squid.init: use config values for shutdown timeout and effective squid user
  (ALT#29236)

* Tue Jul 30 2013 Led <led@altlinux.ru> 3.2.13-alt2
- squid.init: fixed stopping service (ALT#29236)

* Mon Jul 15 2013 Led <led@altlinux.ru> 3.2.13-alt1
- 3.2.13

* Fri Jul 12 2013 Led <led@altlinux.ru> 3.2.12-alt1
- 3.2.12

* Mon May 20 2013 Led <led@altlinux.ru> 3.2.11-alt2
- added upstream fixes

* Tue May 07 2013 Led <led@altlinux.ru> 3.2.11-alt1
- 3.2.11

* Sun Apr 28 2013 Led <led@altlinux.ru> 3.2.10-alt1
- 3.2.10

* Fri Apr 26 2013 Led <led@altlinux.ru> 3.2.9-alt5
- added upstream fixes

* Wed Apr 17 2013 Led <led@altlinux.ru> 3.2.9-alt4
- updated BuildRequires
- negotiate_kerberos_auth: fix config.test (ALT#28859)

* Thu Apr 11 2013 Led <led@altlinux.ru> 3.2.9-alt3
- updated Conflicts

* Mon Apr 08 2013 Led <led@altlinux.ru> 3.2.9-alt2
- added upstream fixes

* Tue Mar 12 2013 Led <led@altlinux.ru> 3.2.9-alt1
- 3.2.9

* Mon Mar 11 2013 Led <led@altlinux.ru> 3.2.8-alt1
- 3.2.8 with postrelease fixes

* Wed Mar 06 2013 Led <led@altlinux.ru> 3.2.5-alt1
- 3.2.5

* Wed Mar 06 2013 Led <led@altlinux.ru> 3.1.23-alt2
- fixed cachemgr.cgi crash with authentication

* Mon Jan 28 2013 Led <led@altlinux.ru> 3.1.23-alt1
- 3.1.23 (CVE-2012-5643)

* Tue Dec 25 2012 Led <led@altlinux.ru> 3.1.22-alt10
- added langpack (ALT#28266)

* Sat Dec 22 2012 Led <led@altlinux.ru> 3.1.22-alt9
- squid.init: clean ups
- spec: fix pre script

* Fri Dec 21 2012 Led <led@altlinux.ru> 3.1.22-alt8
- squid.init: fix typo

* Fri Dec 21 2012 Led <led@altlinux.ru> 3.1.22-alt7
- removed %%name-cachemgr subpackages (merged to %%name)
- cleaned up init script

* Thu Dec 20 2012 Led <led@altlinux.ru> 3.1.22-alt6
- enabled:
  + ecap
  + esi

* Thu Dec 20 2012 Led <led@altlinux.ru> 3.1.22-alt5
- Conflicts %%name-conf-host2cat (ALT#28241)

* Wed Dec 19 2012 Led <led@altlinux.ru> 3.1.22-alt4
- fixed init script for use parameters from %%_sysconfdie/sysconfig/squid
- doc: fix man pages generation

* Tue Dec 18 2012 Led <led@altlinux.ru> 3.1.22-alt3
- cleaned up spec
- updated BuildRequires
- fixed detect '-fhuge-objects' flag
- added subpackage %%name-doc
- removed subpackages
  + %%name-common
  + %%name-server (merged to %%name)
  + %%name-helpers-perl (merged to %%name-helpers)

* Tue Dec 18 2012 Led <led@altlinux.ru> 3.1.22-alt2
- fixed build with --enable-strict-error-checking
- enabled strict-error-checking

* Tue Dec 18 2012 Led <led@altlinux.ru> 3.1.22-alt1
- 3.1.22
- moved tests to %%check section
- disabled strict-error-checking

* Thu Jul 05 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.20-alt1
- 3.1.20

* Fri May 04 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.19-alt2
- Add systemd unit file

* Mon Apr 23 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.19-alt1
- 3.1.19

* Thu Dec 08 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.18-alt1
- 3.1.18

* Mon Oct 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.16-alt1
- 3.1.16

* Wed Sep 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.15-alt1
- 3.1.15 (with CVE-2011-3205 fix)

* Tue Jul 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.14-alt1
- 3.1.14

* Fri Jul 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.13-alt1
- 3.1.13

* Mon Apr 11 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.12-alt1
- 3.1.12

* Wed Mar 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.11-alt2
- repair build

* Tue Feb 08 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.11-alt1
- 3.1.11

* Fri Dec 24 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.10-alt1
- 3.1.10

* Mon Nov 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.9-alt2
- fix build

* Tue Oct 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.9-alt1
- 3.1.9

* Sun Oct 03 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.8-alt2
- rebuild with openssl-1.0.0a

* Tue Sep 14 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.8-alt1
- 3.1.8

* Tue Aug 31 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.7-alt1
- 3.1.7

* Fri Sep 25 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE19-alt1
- New upstream release.

* Mon Aug 24 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE18-alt2
- Export Kerberos keytab name (ALT #20413).

* Wed Aug 05 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE18-alt1
- Bugfix for previous release.

* Tue Aug 04 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE17-alt1
- New upstream release, including SQUID-2009:2 fix.
- squid_unix_group: new -K switch to strip kerberos realm
  from username (ALT #20840).
- Require exact sub-packages version by squid umbrella (ALT #20723).

* Thu Jul 02 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE16-alt1
- New upstream release.
- Include PAM config for pam_auth helper (#20665).

* Fri Jun 26 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE15-alt2
- Helpers were moved to %%_libexecdir according to GNU Coding Standards.
- KRB5_KTNAME was set in the initscript and in the /etc/sysconfig/squid.

* Mon May 18 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE15-alt1
- New upstream release.
- Fix building with gcc-4.4.

* Fri May 15 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE13-alt4
- Set default http_port to 3128.

* Fri May 08 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE13-alt3
- Enable Linux netfilter.

* Mon Apr 13 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE13-alt2
- Default config is separated.

* Tue Apr 07 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE13-alt1
- New upstream release.
- Obsolete FAQ is removed.
- squid_radius_auth helper is enabled.

* Mon Nov 10 2008 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE22-alt1
- New upstream release.

* Wed May 21 2008 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE20-alt1
- New upstream release.

* Sat Feb 16 2008 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE18-alt1
- New upstream release.

* Sun Jan 27 2008 Dmitry V. Levin <ldv@altlinux.org> 2.6.STABLE17-alt2
- Fixed build with fresh autotools.

* Sun Dec 02 2007 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE17-alt1
- New upstream release.
  + security fix for SQUID-2007:2
- Post-install scripts were moved to common and server packages.

* Fri Sep 28 2007 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE16-alt1
- New upstream release (#12920).
- Cumulative patch from git.
- Prefer epoll to poll (#12919).
- More authentication helpers.
- Specfile cleanup.

* Sun May 13 2007 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE13-alt1
- New upstream release.
- ICAP patch cleaned up.

* Wed Apr 11 2007 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE12-alt3
- Reload service in a safe manner.

* Thu Mar 29 2007 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE12-alt2
- Provide %_datadir/%name directory.

* Wed Mar 21 2007 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE12-alt1
- New upstream release
  + includes security fix SQUID-2007:1.
- Official ICAP patch updated and cleaned up.
- DrWeb's ICAP patch obsoleted (disabled).

* Thu Feb 22 2007 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE9-alt2
- Remove extra access_log directive from config.
- Export default port settings into separate patch.

* Thu Feb 08 2007 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE9-alt1
- New upstream release
 + includes NTLM authentication DoS fix, see squid bug #1873.
- Official ICAP patch updated.

* Mon Dec 25 2006 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE6-alt3
- Set absolute link to chpasswd.cgi tarball.
- Applied:
 + DrWeb's ICAP patch
 + Config updated: redirector template
 + ACL max_body_size

* Wed Dec 20 2006 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE6-alt2
- Don't ban underscores in hostname.
- By default use poll.

* Wed Dec 13 2006 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE6-alt1
- New upstream release.
- Applied:
 + ICAP support
 + correct file location in QUICKSTART
 + config-driven maximum file descriptor number
 + build with HTCP, WCCPv2, SNMP but disable in config
 + open rsync, snews, CUPS, SWAT by default
 + prevent appending local domain to localhost
 + update smb_auth.sh
 + run unlinkd on diskd and ufs only
 + helpers list update
 + get back default port to listen to
 + get back default access logging
 + use epoll instead of poll
 + allow X-Forwarded-For following
 + allow forward_log config directive
 + allow Referer logging
 + allow Ident (RFC931) lookups
 + allow multicast notification of cache misses
 + suggest -c option to digest auth helper
 + squid-pinger obsoleted by squid-server
 + add libdb4-devel to BuildRequires
 + quote percent sign (%%) in changelog
- Included into upstream:
 + squid-2.5.STABLE13-libaio-2.patch
 + squid-2.5.STABLE13-header_leak.patch
 + squid-2.5.STABLE13-ident_leak.patch
 + squid-2.5.STABLE13-htcp_leak.patch
 + squid-2.5.STABLE13-icons.patch
 + squid-2.5.STABLE13-hostnamelen.patch
 + squid-2.5.STABLE13-stable13.patch
- Obsoleted:
 + squid-2.4.STABLE6-alt-without-bind.patch
 + squid-2.5-automake.patch
 + squid-2.5.STABLE10-alt-perlreq.patch

* Wed May 17 2006 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE13-alt1
- STABLE13
- applied:
 + 2006-05-13 13:16 (Minor) On some systems POSIX AIO functions are in libaio
 + 2006-05-14 15:41 (Medium) Memory leak in header processing related to external_acl or custom log formats
 + 2006-05-14 15:41 (Major) memory leak in ident processing
 + 2006-05-14 15:41 (Medium) Memleak in HTCP client code
 + 2006-05-14 15:41 (Minor) Mime icons are not displayed when viewing ftp sites when
 + 2006-05-14 15:41 (Cosmetic) SQUIDHOSTNAMELEN issues
 + 2006-05-14 15:41 (Cosmetic) Current release is STABLE13, not 12..
- updated FAQ to v 1.263 2006/03/16

* Sun Oct 30 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE12-alt1
- STABLE12
- applied:
 + 2005-10-26 20:31 (Minor) fails to compile with undefined reference to setenv

* Wed Sep 28 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE11-alt2
- applied:
 + 2005-09-27 22:29 (Major) Truncated responses when using delay pools

* Sun Sep 25 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE11-alt1
- STABLE11 includes all patches issued for STABLE10
- replaced max filedescriptors override trick with configure option
- updated FAQ to v 1.253 2005/09/07

* Fri Sep 16 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE10-alt6
- applied:
 + 2005-09-13 02:59 (Minor) Solaris 10 SPARC transparent proxy build problem with ipfilter
 + 2005-09-03 09:41 (Minor) E-mail sent when cache dies is blocked from many antispam rules
 + 2005-09-11 00:57 (Minor) LDAP helpers does not work with TLS (-Z option)
 + 2005-09-11 01:21 (Cosmetic) Incorrect store dir selection debug message on objects >2G
 + 2005-09-11 01:21 (Cosmetic) enums can not be assumed to be signed ints
 + 2005-09-11 01:42 (Cosmetic) Allow leaving core dumps on Linux
 + 2005-09-11 01:53 (Medium) Clients bypassing delay pools by faking a cache hit
 + 2005-09-13 23:59 (Minor) Transparent proxy problem with IP Filter
 + 2005-09-15 09:56 (Medium) Odd results on pipelined CONNECT requests
 + 2005-09-16 11:10 (Major) FATAL: Incorrect scheme in auth header

* Sat Sep 03 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE10-alt5
- applied:
 + 2005-08-14 17:05 (Cosmetic) New 'mail_program' configuration option in squid.conf 
 + 2005-08-19 09:31 (Minor) sync redeclarations when support for ARP acls
 + 2005-09-01 20:27 (Major) Segmentation fault in sslConnectTimeout
 + 2005-09-01 21:56 (Medium) assertion failed: StatHist.c:93: ((int) floor(0.99L + statHistVal(H, 0) - min)) == 0
 + 2005-09-01 22:09 (Minor) More chroot_dir and squid -k reconfigure issues
 + 2005-09-01 22:18 (Cosmetic) Odd URLs when failing to forward request via parent and several error messages inconsistent in reported request details
 + 2005-09-01 22:26 (Cosmetic) Fails to compile with glibc -D_FORTIFY_SOURCE=2
 + 2005-09-01 22:31 (Minor) Some odd FTP servers respond with 250 where 226 is expected
 + 2005-09-01 22:39 (Cosmetic) Greek translation of error messages
 + 2005-09-01 22:44 (Major) assertion failed: store.c:523: "e->store_status == STORE_PENDING"
 + 2005-09-01 22:49 (Minor) squid_ldap_auth -U does not work
 + 2005-09-01 22:57 (Minor) snmo cacheClientTable fails on "long" IP addresses

* Thu Aug 11 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE10-alt4
- fixed #2713 (wrong SAMBAPREFIX)
- applied:
 + 2005-07-03 08:24 (Cosmetic) "make all" gives many warnings
 + 2005-07-09 08:58 (Cosmetic) Allow wb_ntlm_auth to run more silent
 + 2005-07-11 00:46 (Cosmetic) The new --with-build-environment=... option doesn't work

* Thu Jun 30 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE10-alt3
- pinger, diskd and unlinkd move to squid-server
- updated:
 + 2005-06-27 21:24 (Minor) squid -k fails in combination with chroot after patch for bug 1157
 + 2005-06-30 08:49 (Minor) Core dump with --enable-ipf-transparent if access to NAT device not granted
- applied:
 + 2005-06-29 20:36 (Minor) wbinfo_group.pl only looks into the first group specified

* Wed Jun 29 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE10-alt2
- impoving #6321 resolution

* Fri Jun 24 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE10-alt1
- new version
- #6321 fix
- #1491 and associated cleanups
- #6307 fix
- #7062 fix
- eliminated pinger package
- applied:
 + 2005-05-25 23:01 (Cosmetic) Double content-length often harmless
 + 2005-06-06 21:38 (Cosmetic) Updated Spanish error messages
 + 2005-06-09 08:01 (Minor) Squid internal icons served up with slightly incorrect HTTP headers
 + 2005-06-13 22:55 (Minor) squid -k fails in combination with chroot after patch for bug 1157
 + 2005-06-13 22:55 (Minor) Core dump with --enable-ipf-transparent if access to NAT device not granted
 + 2005-06-13 22:55 (Minor) httpd_accel_signle_host incompatible with redireection
 + 2005-06-19 09:39 (Minor) squid -k reconfigure internal corruption if the type of a cache_dir is changed
 + 2005-06-19 21:03 (Minor) SNMP GETNEXT fails if the given OID is outside the Squid MIB
 + 2005-06-22 10:45 (Cosmetic) Title in FTP listings somewhat messed up
 + 2005-06-21 22:28 (Minor) FTP listings uses "BASE HREF" much more than it needs to

* Thu May 12 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE9-alt3
- applied:
 + 2005-04-20 14:59 (Medium) Fails to process requests for files larger than 2GB in size
 + 2005-03-26 23:53 (Minor) rename() related cleanup
 + 2005-03-29 09:52 (Cosmetic) New cachemgr pending_objects and client_objects actions
 + 2005-03-30 22:51 (Cosmetic) external acls requiring authentication does not request new credentials on access denials like proxy_auth does.
 + 2005-04-26 04:42 (Cosmetic) should syslog to daemon facility not local4
 + 2005-04-20 21:36 (Cosmetic) Error template substitution for authenitcated user name
 + 2005-04-21 10:46 (Cosmetic) Missing newlines in debug statements
 + 2005-04-20 21:55 (Minor) fix transparent proxying when squid listens on NATed non-80 port
 + 2005-04-20 21:55 (Minor) Unable to run "squid -k" when hostname cannot be determined
 + 2005-04-21 10:31 (Cosmetic) Correctly read DOS/Windows formatted config files with CRLF as line terminator
 + 2005-04-22 20:21 (Minor) Unrecognized cache-control directives are silently dropped
 + 2005-04-24 16:35 (Minor) Make the use of the %%m error page to return auth info messages
 + 2005-04-22 20:48 (Cosmetic) PID file check fails when chrooting
 + 2005-04-26 04:30 (Minor Security) Fix for CVE-1999-0710: cachemgr malicouse use
 + 2005-04-25 16:36 (Cosmetic) Minor aufs improvements
 + 2005-04-30 12:58 (Medium) Poor hot object cache hit ratio and sporadic assertion failed: store_swapin.c: e->mem_status == NOT_IN_MEMORY
 + 2005-05-01 10:58 (Cosmetic) Cosmetic change to DISKD statistics
 + 2005-05-04 18:09 (Minor) SNMP Agent updates to support SNMP Version 2 and bulk requests
 + 2005-05-08 14:01 (Cosmetic) Minor arp ACL improvements
 + 2005-05-09 01:51 (Minor) Allow dstdomain and dstdom_regex to match IP based hosts
 + 2005-05-11 19:19 (Security issue) DNS lookups unreliable on untrusted networks
 + 2005-05-10 22:33 (Medium) assertion failed: store_client.c:343: "storeSwapOutObjectBytesOnDisk(mem) > sc->copy_offset"
 + 2005-05-10 23:11 (Cosmetic) Extended documentation of the always_direct directive
- updated:
 + 2005-04-19 22:46 (Cosmetic) LDAP helpers fails to compile with SUN LDAP SDK
 + 2005-03-29 08:45 (Minor) Several minor aufs issues
- updated FAQ to v 1.250 2005/04/22
- enabled 2GB+ files support
- disabled aa patch for now

* Tue Mar 22 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE9-alt2
- applied:
 + 2005-03-03 02:26 (Minor Security) Race condition related to Set-Cookie header 
 + 2005-03-04 11:55 (Minor) Fails to parse the EPLF FTP directory format
 + 2005-03-04 11:55 (Minor) Links in FTP listings without / fails due to missing BASE HREF
 + 2005-03-04 22:48 (Cosmetic Security) Unexpected access control results on configuration errors
 + 2005-03-09 15:46 (Minor) Handle odd date formats
 + 2005-03-09 15:46 (Minor) reload_into_ims fails to revalidate negatively cached entries
 + 2005-03-09 15:46 (Cosmetic) Clarify delay_access function
 + 2005-03-09 15:46 (Cosmetic) Check several squid.conf directives for int overflows
 + 2005-03-09 15:46 (Minor) bzero is a non-standard function not available on all platforms
 + 2005-03-15 04:27 (Minor) compile warnings due to pid_t not being an int
 + 2005-03-10 23:38 (Minor) Incorrect use of ctype functions
 + 2005-03-09 15:46 (Cosmetic) Defer digest fetch if the peer is not allowed to be used
 + 2005-03-09 15:46 (Cosmetic) Duplicate content-length headers logged as conflicting with relaxed_header_parser off
 + 2005-03-09 15:46 (Cosmetic) Extend relaxed_header_parser to work around "excess data from" errors from many major web servers.
 + 2005-03-19 11:42 (Minor) Several minor aufs issues
 + 2005-03-19 00:25 (Minor) Basic authentication fails with very long login or password
 + 2005-03-21 20:44 (Minor) CONNECT requests truncated if client side disconnects first assertion failed: comm.c:430: "quot;ntohs(address->sin_port) != 0"quot;
 + 2005-03-19 01:11 (Cosmetic) LDAP helpers fail to compile with SUN LDAP SDK
 + 2005-03-19 01:35 (Minor) --disable-hostname-checks not working
 + 2005-03-19 23:57 (Cosmetic) aufs warning about open event filedescriptors on shutdown
- updated FAQ to v 1.246 2005/03/04 23:49:39

* Tue Mar 01 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE9-alt1
- upstream merged:
 + 2005-02-20 10:47 (Minor) Relax header parsing slightly again to work around broken web servers
 + 2005-02-20 19:11 (Cosmetic) GCC4 warnings
 + 2005-02-21 01:38 (Cosmetic) Doesn't work specifying the AR variable to configure
 + 2005-02-21 02:58 (Minor) Peer related memory leaks on "squid -k reconfigure"
 + 2005-02-21 03:38 (Cosmetic) Display FTP URLs in decoded format to allow for sane display of national characters etc
 + 2005-02-21 17:02 (Minor) fqdn lookups with spaces may confuse redirectors
 + 2005-02-23 00:11 (Medium) Should not automatically retry request on 403 and other server errors
- upstream updated and merged:
 + 2005-02-20 11:03 (Cosmetic) Cross-platform format fixes
- updated FAQ to v 1.245 2005/02/24 23:29:59

* Wed Feb 16 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE8-alt1
- upstream merged:
 + 2005-02-04 11:41 (Minor) WCCP easily disturbed by forged packets 
 + 2005-02-06 00:57 (Cosmetic) Improve password handling in FTP gatewaying of ftp://user@host URLs
 + 2005-02-11 10:59 (Major) Data corruption when HTTP reply headers is split in several packets
- upstream updated and merged:
 + 2005-01-31 01:50 (Security issue) Strengthen Squid from HTTP response splitting cache pollution attack
 + 2005-02-10 10:14 (Security issue) Reject malformed HTTP requests and responses that conflict with the HTTP specifications
- applied new:
 + 2005-02-13 05:58 (Major) Assertion failure on certain odd DNS responses
 + 2005-02-15 00:03 (Cosmetic) Cross-platform format fixes
 + 2005-02-15 01:07 (Cosmetic) Allow high characters in generated FTP and Gopher directory listings
 + 2005-02-15 02:14 (Cosmetic) FTP URL cleanups


* Fri Feb 04 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE7-alt8
- libpam-devel -> libpam0-devel
- Russian description
- applied:
 + 2005-01-31 22:50 (Security issue) Correct handling of oversized reply headers
 + 2005-02-03 23:17 (Minor) LDAP helpers sends slightly malformed search requests
 + 2005-02-03 23:27 (Minor) Sporadic segmentation fault when using ntlm authentication
 + 2005-02-04 00:12 (Major) Segmentation fault on failed PUT/POST request
 + 2005-02-04 00:33 (Medium) Persistent connection trouble on failed PUT/POST requests

* Sat Jan 29 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE7-alt7
- updated squid-2.5.STABLE7-header_parsing.patch once more
- applied:
 + 2005-01-28 23:16 (Security issue) Buffer overflow in WCCP recvfrom() call

* Mon Jan 24 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE7-alt6
- applied current patches:
 + 2005-01-21 12:43 (Security issue) Strengthen Squid from HTTP response splitting cache pollution attack
 + 2005-01-21 12:10 (Minor) Icons fails to load on non-anonymous FTP when using short_icons_url directive
 + 2005-01-21 12:10 (Minor) FTP data connection fails on some FTP servers when requesting directory without a trailing slash
 + 2005-01-21 12:10 (Minor) Disable Path-MTU discovery on intercepted requests
 + 2005-01-24 14:29 (Security issue) Reject malformed HTTP requests and responses that conflict with the HTTP specifications
 + 2005-01-17 04:29 (Minor Secuity issue) Sanity check usernames in squid_ldap_auth
 + 2005-01-17 02:52 (Minor) FQDN names truncated on compressed DNS responses
 + 2005-01-17 02:52 (Minor) Internal DNS memory leak on malformed responses

* Thu Jan 13 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE7-alt5
- applied current patches:
 + 2005-01-12 17:21 (Security issue) Denial of service with forged WCCP messages
 + 2005-01-12 17:19 (Security issue) buffer overflow bug in gopherToHTML()
 + 2005-01-08 03:13 (Medium) fakeauth_auth memory leak and NULL pointer access
 + 2004-12-28 12:55 (Minor) Don't close "other" filedescriptors on startup
 + 2004-12-21 17:50 (Minor Security) Confusing results on empty acl declarations
 + 2004-12-08 00:00 (Minor) PURGE is allowed to delete internal objects
- fix for #5767 (config patch and initgroups)
- fix for #5616 (squid MIB)
- fix for #5707 (wbinfo_group.pl and spaces)
- updated FAQ to 1.240 2005/01/08 00:16:21
- used macro instead of env var for rpm build root

* Thu Dec 09 2004 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE7-alt4
- applied current patches:
 + 2004-12-08 01:03 (Minor) cachemgr vm_objects segfault
 + 2004-12-08 00:47 (Minor) httpd_accel_port 0 (virtual) not working correctly
 + 2004-12-07 23:45 (Cosmetic / Minor Security issue) Random error messages in response to malformed host name

* Sat Dec 04 2004 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE7-alt3
- applied current patches:
 + 2004-11-07 23:37 (Minor) Squid fails to close TCP connection after blank HTTP response
 + 2004-11-06 21:42 (Minor) 100%% CPU on startup on new/experimental Linux kernels due to O_NONBLOCK
 + 2004-11-06 15:28 (Minor) Failure to shut down busy helpers on -k rotate/reconfigure
 + 2004-10-20 23:23 (Minor) The new req_header and resp_header acls segfaults immediately on parse of squid.conf
 + 2004-10-19 10:09 (Cosmetic) Document -v (protocol version) option to LDAP helpers
 + 2004-10-14 22:48 (Minor) 100%% CPU usage on half-closed PUT/POST requests

* Sun Nov 14 2004 Dmitry V. Levin <ldv@altlinux.org> 2.5.STABLE7-alt2
- Cleaned up build dependencies, was too superfluous
  since 2.5.STABLE6-alt1.
- Rebuilt with openldap-2.2.18-alt3.

* Tue Oct 12 2004 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE7-alt1
- 2.5.STABLE7 (security fix)
- updated FAQ to 1.235 2004/10/04
- rediffed patches

* Sat Sep 04 2004 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE6-alt3
- more patches

* Tue Aug 17 2004 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE6-alt2
- Updated FAQ to 2004-08-10
- Added and rediffed official patches up to 2004-08-14
- build with 16384 file descriptors

* Fri Jul 23 2004 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE6-alt1
- 2.5.STABLE6
- Official bugfixes from www.%name-cache.org.
- add patch-aa.patch: makes squid write info in access.log by pieces as far as the
  receipt of data but not after downloading whole file. See -x options.

* Thu Jun 10 2004 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE5-alt4
- Official bugfixes from www.%name-cache.org.
- fix bugs id #4330

* Wed May 26 2004 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE5-alt3
- fix bugs id #1629

* Fri May 14 2004 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE5-alt2
- build with 8192 file descriptors
- Official bugfixes from www.%name-cache.org.

* Wed May 12 2004 ALT QA Team Robot <qa-robot@altlinux.org> 2.5.STABLE5-alt1.1
- Rebuilt with openssl-0.9.7d.

* Wed Mar 03 2004 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE5-alt1
- 2.5.STABLE5

* Thu Dec 18 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE4-alt5
- fix build with libsasl2

* Mon Dec 08 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE4-alt4
- Official bugfixes from www.%name-cache.org.
- cosmetics spec file

* Tue Nov 04 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE4-alt3
- Fixed %%pre script.

* Tue Oct 21 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE4-alt2
- Official bugfixes from www.%name-cache.org.
- disable default ICP setup.

* Fri Sep 26 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE4-alt1
- 2.5.STABLE4

* Mon Jul 21 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE3-alt3
- fix errors in squid init file.

* Mon Jul 14 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE3-alt2
- Added Belarusian error pages by Vital Khilko (dojlid@mova.org)

* Fri Jul 11 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE3-alt1
- 2.5.STABLE3
- fix bugs id #0002717
- Official bugfixes from www.%name-cache.org.
- Rewritten start/stop script to new rc scheme.

* Thu Nov 28 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE1-alt5
- fix build support for the authentication schemes
- Official bugfixes from www.%name-cache.org.

* Mon Nov 25 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE1-alt4
- fix documentations and manuals path

* Fri Nov 01 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE1-alt3
- fix documentation

* Thu Oct 24 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE1-alt2
- Fixed path on directories: %_var/run, %_logdir/%name and %_spooldir/%name.

* Tue Oct 22 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE1-alt1
- 2.5.STABLE1
- misc adaptions

* Thu Aug 29 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.4.STABLE7-alt4
- buildprereq autoconf = 2.13
- adding --enable-storeio

* Sun Jul 07 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.4.STABLE7-alt3
- Official bugfixes from www.%name-cache.org.

* Thu Jul 04 2002 Stanislav Ievlev <inger@altlinux.ru> 2.4.STABLE7-alt2
- Relocated "chown" cleanup code from %%pre to %%triggerpostun (#1051).

* Wed Jul 03 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.4.STABLE7-alt1
- 2.4.STABLE7

* Fri Jun 28 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4.STABLE6-alt4
- Official bugfixes from www.%name-cache.org.

* Thu Jun 27 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4.STABLE6-alt3
- Official bugfixes from www.%name-cache.org.

* Wed Apr 03 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.STABLE6-alt2
- Build without bind-devel.

* Fri Mar 22 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.STABLE6-alt1
- 2.4.STABLE6.

* Wed Mar 06 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.4.STABLE4-alt2
- adding subpackage pinger.
- remove link to errors dir.

* Wed Feb 20 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.STABLE4-alt1
- 2.4.STABLE4-alt1
- Fixed permissions on directories:
  %_sysconfdir/%name, %_libdir/%name, %_logdir/%name and %_spooldir/%name.

* Mon Feb 18 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.STABLE3-alt2
- Added official patches for 2.4.STABLE3:
  + "htcp_port 0" fails to disable the HTCP port
  + Coredup on certain ftp:// style URL's
  + SNMP memory leaks
- Fixed %%pre script.

* Fri Feb 15 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.4.STABLE3-alt1
- 2.4.STABLE3

* Mon Sep 24 2001 Kostya Timoshenko <kt@altlinux.ru> 2.4.STABLE2-alt1
- enable auth-modules LDAP, MSNT, NCSA, PAM, SMB, YP, getpwnam
- bugfix patches

* Mon Apr 16 2001 Kostya Timoshenko <kt@altlinux.ru> 2.4.STABLE1-ipl2mdk
- enable wccp, gnu-regex, cache-digests

* Mon Mar 26  2001 Kostya Timoshenko <kt@petr.kz> 2.4.STABLE1-ipl1mdk
- 2.4.STABLE1

* Mon Feb  5 2001 Kostya Timoshenko <kt@petr.kz> 2.3.STABLE4-ipl4mdk
- enable useragen log, icmp, async-io

* Wed Jan 17 2001 Kostya Timoshenko <kt@petr.kz>
- security fix for tmpfile problems (patch#20)

* Wed Jan  3 2001 Kostya Timoshenko <kt@petr.kz>
- fixed squid.init

* Wed Dec 27 2000 Kostya Timoshenko <kt@petr.kz>
- Rebuild for RE

* Sun Nov 12 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.3.STABLE4-1mdk
- shiny version.
- comment out already applied patches.

* Tue Sep  5 2000 Etienne Faure  <etienne@mandraksoft.com> 2.3.STABLE2-3mdk
- rebuilt with %%doc macro
- added noreplace tag for config files

* Tue May  2 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 2.3.STABLE2-2mdk
- fixed %post script
- three more bugfix patches from the squid people
- buildprereq jade, sgmltools

* Fri Apr  7 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 2.3.STABLE2-1mdk
- merged with redhat again

* Sun Mar 26 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- make %pre more portable

* Thu Mar 16 2000 Bill Nottingham <notting@redhat.com>
- bugfix patches
- fix dependency on /usr/local/bin/perl

* Sat Mar  4 2000 Bill Nottingham <notting@redhat.com>
- 2.3.STABLE2

* Mon Feb 14 2000 Bill Nottingham <notting@redhat.com>
- Yet More Bugfix Patches

* Tue Feb  8 2000 Bill Nottingham <notting@redhat.com>
- add more bugfix patches
- --enable-heap-replacement

* Mon Jan 31 2000 Cristian Gafton <gafton@redhat.com>
- rebuild to fix dependencies

* Fri Jan 28 2000 Bill Nottingham <notting@redhat.com>
- grab some bugfix patches

* Mon Jan 10 2000 Bill Nottingham <notting@redhat.com>
- 2.3.STABLE1 (whee, another serial number)

* Tue Dec 21 1999 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix compliance with ftp RFCs
  (http://www.wu-ftpd.org/broken-clients.html)
- Work around a bug in some versions of autoconf
- BuildPrereq sgml-tools - we're using sgml2html

* Mon Oct 18 1999 Bill Nottingham <notting@redhat.com>
- add a couple of bugfix patches

* Wed Oct 13 1999 Bill Nottingham <notting@redhat.com>
- update to 2.2.STABLE5.
- update FAQ, fix URLs.

* Sat Sep 11 1999 Cristian Gafton <gafton@redhat.com>
- transform restart in reload and add restart to the init script

* Tue Aug 31 1999 Bill Nottingham <notting@redhat.com>
- add squid user as user 23.

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging
- fix conflict between logrotate & squid -k (#4562)

* Wed Jul 28 1999 Bill Nottingham <notting@redhat.com>
- put cachemgr.cgi back in /usr/lib/squid

* Wed Jul 14 1999 Bill Nottingham <notting@redhat.com>
- add webdav bugfix patch (#4027)

* Mon Jul 12 1999 Bill Nottingham <notting@redhat.com>
- fix path to config in squid.init (confuses linuxconf)

* Wed Jul  7 1999 Bill Nottingham <notting@redhat.com>
- 2.2.STABLE4

* Wed Jun 9 1999 Dale Lovelace <dale@redhat.com>
- logrotate changes
- errors from find when /var/spool/squid or
- /var/log/squid didn't exist

* Thu May 20 1999 Bill Nottingham <notting@redhat.com>
- 2.2.STABLE3

* Thu Apr 22 1999 Bill Nottingham <notting@redhat.com>
- update to 2.2.STABLE.2

* Sun Apr 18 1999 Bill Nottingham <notting@redhat.com>
- update to 2.2.STABLE1

* Thu Apr 15 1999 Bill Nottingham <notting@redhat.com>
- don't need to run groupdel on remove
- fix useradd

* Mon Apr 12 1999 Bill Nottingham <notting@redhat.com>
- fix effective_user (bug #2124)

* Mon Apr  5 1999 Bill Nottingham <notting@redhat.com>
- strip binaries

* Thu Apr  1 1999 Bill Nottingham <notting@redhat.com>
- duh. adduser does require a user name.
- add a serial number

* Tue Mar 30 1999 Bill Nottingham <notting@redhat.com>
- add an adduser in %pre, too

* Thu Mar 25 1999 Bill Nottingham <notting@redhat.com>
- oog. chkconfig must be in %preun, not %postun

* Wed Mar 24 1999 Bill Nottingham <notting@redhat.com>
- switch to using group squid
- turn off icmp (insecure)
- update to 2.2.DEVEL3
- build FAQ docs from source

* Tue Mar 23 1999 Bill Nottingham <notting@redhat.com>
- logrotate changes

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Wed Feb 10 1999 Bill Nottingham <notting@redhat.com>
- update to 2.2.PRE2

* Wed Dec 30 1998 Bill Nottingham <notting@redhat.com>
- cache & log dirs shouldn't be world readable
- remove preun script (leave logs & cache @ uninstall)

* Tue Dec 29 1998 Bill Nottingham <notting@redhat.com>
- fix initscript to get cache_dir correct

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- update to 2.1.PATCH2
- merge in some changes from RHCN version

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- version 1.1.22

* Sun May 10 1998 Cristian Gafton <gafton@redhat.com>
- don't make packages conflict with each other...

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- added a proxy auth patch from Alex deVries <adevries@engsoc.carleton.ca>
- fixed initscripts

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- rebuilt for Manhattan

* Fri Mar 20 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.1.21/1.NOVM.21

* Mon Mar 02 1998 Cristian Gafton <gafton@redhat.com>
- updated the init script to use reconfigure option to restart squid instead
  of shutdown/restart (both safer and quicker)

* Sat Feb 07 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.1.20
- added the NOVM package and tryied to reduce the mess in the spec file

* Wed Jan 7 1998 Cristian Gafton <gafton@redhat.com>
- first build against glibc
- patched out the use of setresuid(), which is available only on kernels
  2.1.44 and later
