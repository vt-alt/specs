Name: bind
Version: 9.11.19
%define src_version 9.11.19
Release: alt1

Summary: ISC BIND - DNS server
License: MPL-2.0
Group: System/Servers
Url: http://www.isc.org/products/BIND/

# ftp://ftp.isc.org/isc/bind9/%src_version/bind-%src_version.tar.gz
Source0: %name-%version.tar
Source2: rfc1912.txt
Source3: bind.README.bind-devel
Source4: bind.README.ALT

Source11: bind.init
Source12: lwresd.init

Source21: rndc.conf
Source22: rndc.key

Source31: bind.named.conf
Source32: bind.options.conf
Source33: bind.rndc.conf
Source34: bind.local.conf
Source35: bind.rfc1912.conf
Source36: bind.rfc1918.conf
Source37: bind.sysconfig

Source41: bind.localhost
Source42: bind.localdomain
Source43: bind.127.in-addr.arpa
Source44: bind.empty

Source50: bind.service

# NB: there must be at least one patch :)
Patch0001: 0001-owl-warnings.patch
Patch0002: 0002-openbsd-owl-pidfile.patch
Patch0003: 0003-openbsd-owl-chroot-defaults.patch
Patch0004: 0004-alt-owl-chroot.patch
Patch0005: 0005-owl-checkconf-chroot.patch
Patch0006: 0006-alt-man.patch
Patch0007: 0007-alt-nofile.patch
Patch0008: 0008-alt-ads-remove.patch
Patch0009: 0009-Minimize-linux-capabilities.patch
Patch0010: 0010-Link-libirs-with-libdns-libisc-and-libisccfg.patch

# root directory for chrooted environment.
%define _chrootdir %_localstatedir/bind

# common directory for documentation.
%define docdir %_docdir/bind-%version

%ifndef timestamp
%define timestamp %(TZ=UTC LC_TIME=C date +%%Y%%m%%d)
%endif

%def_disable static
%def_enable ipv6
%def_with openssl
%def_with libjson
%def_without python

Provides: bind-chroot(%_chrootdir)
Obsoletes: bind-chroot, bind-debug, bind-slave, caching-nameserver
# Because of /etc/syslog.d/ feature.
Conflicts: syslogd < 1.4.1-alt11
Requires(pre): bind-control >= 1.2

# due to %_chrootdir/dev/log
BuildPreReq: coreutils

# due to broken configure script
BuildPreReq: gcc-c++

# for better --enable-linux-caps experience
BuildPreReq: libcap-devel

%{?_with_openssl:BuildPreReq: libssl-devel}
%{?_with_libjson:BuildPreReq: libjson-c-devel}
BuildPreReq: libkrb5-devel

%package utils
Summary: Utilities provided by ISC BIND
Group: Networking/Other
Requires: libbind = %EVR

%package -n libbind
Summary: Shared library used by ISC BIND
Group: System/Libraries
Provides: libdns = %EVR
Provides: libisc = %EVR
Provides: libisccc = %EVR
Provides: libisccfg = %EVR
Provides: liblwres = %EVR
Obsoletes: libdns8, libdns9, libdns10, libdns11, libdns16
Obsoletes: libisc4, libisc7, libisccc0, libisccfg0, liblwres1

%package devel
Summary: ISC BIND development libraries and headers
Group: Development/C
Requires: libbind = %EVR
Provides: libisc-export-devel = %EVR
Obsoletes: libisc-export-devel < %version

%package devel-static
Summary: ISC BIND static development libraries
Group: Development/C
Requires: %name-devel = %EVR

%package doc
Summary: Documentation for ISC BIND
Group: Development/Other
BuildArch: noarch
Prefix: %prefix

%package -n lwresd
Summary: Lightweight resolver daemon
Group: System/Servers
Requires: libbind = %EVR

%description
The Berkeley Internet Name Domain (BIND) implements an Internet domain
name server.  BIND is the most widely-used name server software on the
Internet, and is supported by the Internet Software Consortium (ISC).

This package provides the %src_version server and related
configuration files.

%description utils
This package contains various utilities related to DNS that are derived
from the BIND %src_version source tree, including dig, host,
nslookup and nsupdate.

%description -n libbind
This package contains shared libraries used by BIND's %src_version
daemons and clients.

%description devel
This package contains development libraries, header files, and API man
pages for libdns, libisc, libisccc, libisccfg and liblwres. These are
only needed if you want to compile packages that need more BIND
%src_version nameserver API than the resolver code provided by
glibc.

%description devel-static
This package contains development static libraries, header files, and
API man pages for libdns, libisc, libisccc, libisccfg and liblwres.
These are only needed if you want to compile statically linked packages
that need more BIND %src_version nameserver API than the resolver
code provided by glibc.

%description doc
This package provides various documents that are useful for maintaining
a working BIND %src_version installation.

%description -n lwresd
This package contains lwresd, the daemon providing name lookup services
to clients that use the BIND %src_version lightweight resolver
library. It is essentially a stripped-down, caching-only name server
that answers queries using the BIND 9 lightweight resolver protocol
rather than the DNS protocol.

%prep
%setup

# NB: there must be at least one patch :)
%patch0001 -p2
%patch0002 -p2
%patch0003 -p2
%patch0004 -p2
%patch0005 -p2
%patch0006 -p2
%patch0007 -p2
%patch0008 -p2
#%%patch0009 -p2
%patch0010 -p2

install -D -pm644 %_sourcedir/rfc1912.txt doc/rfc/rfc1912.txt
install -pm644 %_sourcedir/bind.README.bind-devel README.bind-devel
install -pm644 %_sourcedir/bind.README.ALT README.ALT

mkdir addon
install -pm644 %_sourcedir/{bind,lwresd}.init addon/
install -pm644 %_sourcedir/bind.{named,options,rndc,local,rfc1912,rfc1918}.conf \
	addon/
install -pm644 %_sourcedir/bind.{localhost,localdomain,127.in-addr.arpa,empty,sysconfig,service} \
	addon/
install -pm644 %_sourcedir/rndc.{conf,key} addon/

find -type f -print0 |
	xargs -r0 grep -lZ '@[A-Z_]\+@' -- |
	xargs -r0 sed -i \
'
s,@ROOT@,%_chrootdir,g;
s,@LWRESD_ROOT@,/var/resolv,g;
s,@DOCDIR@,%docdir,g;
s,@SBINDIR@,%_sbindir,g;
' --

sed -i '/# Large File/iAC_SYS_LARGEFILE/' configure.ac

%build
%autoreconf
%configure \
	--localstatedir=/var \
	--with-randomdev=/dev/random \
	--enable-threads \
	--enable-linux-caps \
	--enable-fixed-rrset \
	--disable-seccomp \
	 %{subst_with openssl} \
	 %{subst_with libjson} \
	 %{subst_with python} \
	 %{subst_enable ipv6} \
	 %{subst_enable static} \
	--includedir=%{_includedir}/bind9 \
	--with-libtool \
	--with-gssapi=yes \
	--disable-isc-spnego \
	#

%make_build
# Build queryperf
pushd contrib/queryperf
	%configure
	%make_build
popd # contrib/queryperf

%install
%makeinstall_std

# Install additional headers.
install -pm644 lib/isc/unix/errno2result.h %buildroot%_includedir/bind9/isc/

# Install queryperf.
install -pm755 contrib/queryperf/queryperf %buildroot%_sbindir/

# Install startup scripts.
install -pD -m755 addon/bind.init %buildroot%_initdir/bind
install -pD -m755 addon/lwresd.init %buildroot%_initdir/lwresd

# Install systemd service
install -pD -m644 addon/bind.service %buildroot%_unitdir/bind.service

# Install configurations files
install -pm640 addon/rndc.conf %buildroot%_sysconfdir/
install -pD -m644 addon/bind.sysconfig %buildroot%_sysconfdir/sysconfig/bind

# Create a chrooted environment...
mkdir -p %buildroot%_chrootdir/{dev,%_sysconfdir,var/{run,tmp},session,zone/slave}
for n in named options rndc local rfc1912 rfc1918; do
	install -pm640 "addon/bind.$n.conf" \
		"%buildroot%_chrootdir%_sysconfdir/$n.conf"
done
for n in localhost localdomain 127.in-addr.arpa empty; do
	install -pm640 "addon/bind.$n" \
		"%buildroot%_chrootdir/zone/$n"
	sed -i s/YYYYMMDDNN/%{timestamp}00/ \
		"%buildroot%_chrootdir/zone/$n"
done

install -pm640 addon/rndc.key bind.keys %buildroot%_chrootdir%_sysconfdir/
ln -snfr %buildroot%_sysconfdir/bind/{named.conf,bind.keys} \
	%buildroot%_sysconfdir/

# Create symlinks for unchrooted bind.
ln -snf . %buildroot%_chrootdir%_sysconfdir/bind
ln -snf ../zone %buildroot%_chrootdir%_sysconfdir/zone
ln -snfr %buildroot%_chrootdir%_sysconfdir %buildroot%_sysconfdir/bind

# Make use of syslogd-1.4.1-alt11 /etc/syslog.d/ feature.
/usr/bin/mksock %buildroot%_chrootdir/dev/log
mkdir %buildroot%_sysconfdir/syslog.d
ln -s %_chrootdir/dev/log %buildroot%_sysconfdir/syslog.d/bind
#... end of the chroot configuration.

# Create ndc compatibility symlinks.
ln -s rndc %buildroot%_sbindir/ndc
ln -s rndc.8 %buildroot%_man8dir/ndc.8

# Create ghost files
touch %buildroot/var/run/{named,lwresd}.pid

# Package documentation files
mkdir -p %buildroot%docdir
cp -a CHANGES COPYRIGHT README* \
	doc/{arm,misc,rfc} \
	%buildroot%docdir/
install -pm644 contrib/queryperf/README %buildroot%docdir/README.queryperf

xz -9 %buildroot%docdir/{*/*.txt,CHANGES}
rm -v %buildroot%docdir/*/{Makefile*,README-SGML,*.xml}

%define _unpackaged_files_terminate_build 1

%pre
/usr/sbin/groupadd -r -f named
/usr/sbin/useradd -r -g named -d %_chrootdir -s /dev/null -n -c "Domain Name Server" named >/dev/null 2>&1 ||:
[ -f %_initdir/named -a ! -L %_initdir/named ] && /sbin/chkconfig --del named ||:
%pre_control bind-chroot bind-debug bind-slave

%preun
%preun_service bind

%post
SYSLOGD_SCRIPT=/etc/init.d/syslogd
SYSLOGD_CONFIG=/etc/sysconfig/syslogd
if grep -qs '^SYSLOGD_OPTIONS=.*-a %_chrootdir/dev/log' "$SYSLOGD_CONFIG"; then
	# Remove artefacts of pre-syslog.d epoch.
	sed -i 's|^\(SYSLOGD_OPTIONS=.*\) \?-a %_chrootdir/dev/log|\1|' "$SYSLOGD_CONFIG"
	if [ -x "$SYSLOGD_SCRIPT" ]; then
		"$SYSLOGD_SCRIPT" condreload ||:
	fi
fi

%post_control -s enabled bind-chroot
%post_control -s disabled bind-debug bind-slave
%post_service bind

%pre -n lwresd
/usr/sbin/groupadd -r -f lwresd
/usr/sbin/useradd -r -g lwresd -d / -s /dev/null -n -c "Lightweight Resolver Daemon" lwresd >/dev/null 2>&1 ||:

%post -n lwresd
%post_service lwresd

%preun -n lwresd
%preun_service lwresd

%triggerun -- bind < 9.10.4
F=/etc/sysconfig/bind
if [ $2 -gt 0 -a -f $F ]; then
	grep -q '^#\?CHROOT=' $F || echo '#CHROOT="-t /"' >> $F
fi

%files -n libbind
%_libdir/lib*.so.*
%dir %docdir
%docdir/COPYRIGHT

%files -n lwresd
%config %_initdir/lwresd
%_sbindir/lwresd
%_man8dir/lwresd.*
%ghost %attr(644,root,root) /var/run/lwresd.pid

%files devel
%_libdir/*.so
%_bindir/bind9-config
%_bindir/isc-config.sh
%_includedir/bind9
%_man1dir/bind9-config.1*
%_man3dir/*
%dir %docdir
%docdir/README.bind-devel

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%files
%_bindir/arpaname
%_bindir/named-rrchecker
%exclude %_sbindir/lwresd
%exclude %_man8dir/lwresd*
%_sbindir/*
%_sysconfdir/bind
%_sysconfdir/bind.keys
%_sysconfdir/named.conf
%config %_initdir/bind
%config %_sysconfdir/sysconfig/bind
%config(noreplace) %attr(640,root,named) %_sysconfdir/rndc.conf
%_unitdir/bind.service

%_man1dir/named-rrchecker.1*
%_man5dir/*
%_man8dir/*
%_man1dir/arpaname*

%dir %docdir
%docdir/README*
%docdir/misc
%exclude %docdir/README.bind-devel

%ghost %attr(644,root,root) /var/run/named.pid

#chroot
%_sysconfdir/syslog.d/*
%defattr(640,root,named,710)
%dir %_chrootdir
%dir %_chrootdir/dev
%dir %_chrootdir%_sysconfdir
%dir %_chrootdir/zone
%dir %attr(700,root,named) %verify(not mode) %_chrootdir/zone/slave
%dir %attr(700,root,named) %verify(not mode) %_chrootdir/var
%dir %attr(1770,root,named) %_chrootdir/var/run
%dir %attr(1770,root,named) %_chrootdir/var/tmp
%dir %attr(700,root,named) %_chrootdir/session
%config(noreplace) %_chrootdir%_sysconfdir/*.conf
%config(noreplace) %verify(not md5 mtime size) %_chrootdir%_sysconfdir/rndc.key
%_chrootdir%_sysconfdir/bind.keys
%attr(-,root,root) %_chrootdir%_sysconfdir/bind
%attr(-,root,root) %_chrootdir%_sysconfdir/zone
%config %_chrootdir/zone/localhost
%config %_chrootdir/zone/localdomain
%config %_chrootdir/zone/127.in-addr.arpa
%config %_chrootdir/zone/empty

%ghost %attr(666,root,root) %_chrootdir/dev/*

%files utils
%_bindir/delv
%_bindir/dig
%_bindir/mdig
%_bindir/host
%_bindir/nslookup
%_bindir/nsupdate
%_man1dir/delv.*
%_man1dir/dig.*
%_man1dir/mdig.*
%_man1dir/host.*
%_man1dir/nslookup.*
%_man1dir/nsupdate.*
%_man1dir/isc-config.sh.*

%files doc
%docdir
%exclude %docdir/README*
%exclude %docdir/misc
%exclude %docdir/COPYRIGHT

%changelog
* Tue May 19 2020 Stanislav Levin <slev@altlinux.org> 9.11.19-alt1
- 9.11.18 -> 9.11.19 (fixes: CVE-2020-8616, CVE-2020-8617).

* Fri Apr 17 2020 Stanislav Levin <slev@altlinux.org> 9.11.18-alt1
- 9.11.13 -> 9.11.18.

* Thu Nov 21 2019 Stanislav Levin <slev@altlinux.org> 9.11.13-alt1
- 9.11.12 -> 9.11.13 (fixes: CVE-2019-6477).

* Wed Oct 16 2019 Stanislav Levin <slev@altlinux.org> 9.11.12-alt1
- 9.11.10 -> 9.11.12.

* Wed Sep 18 2019 Stanislav Levin <slev@altlinux.org> 9.11.10-alt2
- Fixed integration with ipa-dnskeysync.

* Tue Aug 27 2019 Stanislav Levin <slev@altlinux.org> 9.11.10-alt1
- 9.11.9 -> 9.11.10.

* Thu Aug 01 2019 Stanislav Levin <slev@altlinux.org> 9.11.9-alt1
- 9.11.8 -> 9.11.9.

* Thu Jun 20 2019 Stanislav Levin <slev@altlinux.org> 9.11.8-alt1
- 9.11.7 -> 9.11.8 (fixes: CVE-2019-6471).

* Thu May 16 2019 Stanislav Levin <slev@altlinux.org> 9.11.7-alt1
- 9.11.6.P1 -> 9.11.7.

* Thu Apr 25 2019 Stanislav Levin <slev@altlinux.org> 9.11.6.P1-alt1
- 9.11.6 -> 9.11.6.P1 (fixes: CVE-2018-5743).

* Wed Mar 27 2019 Stanislav Levin <slev@altlinux.org> 9.11.6-alt2
- Fixed support for GSSAPI (closes: #36429).

* Fri Mar 01 2019 Stanislav Levin <slev@altlinux.org> 9.11.6-alt1
- 9.11.5.P4 -> 9.11.6.

* Fri Feb 22 2019 Stanislav Levin <slev@altlinux.org> 9.11.5.P4-alt1
- 9.11.5 -> 9.11.5.P4 (fixes: CVE-2018-5744, CVE-2018-5745, CVE-2019-6465).

* Fri Nov 23 2018 Stanislav Levin <slev@altlinux.org> 9.11.5-alt1
- 9.11.4.P2 -> 9.11.5.

* Thu Sep 20 2018 Stanislav Levin <slev@altlinux.org> 9.11.4.P2-alt1
- 9.11.4.P1 -> 9.11.4.P2.

* Fri Aug 31 2018 Stanislav Levin <slev@altlinux.org> 9.11.4.P1-alt2
- Build with new openssl1.1.

* Mon Aug 13 2018 Stanislav Levin <slev@altlinux.org> 9.11.4.P1-alt1
- 9.11.3 -> 9.11.4.P1 (fixes: CVE-2018-5738, CVE-2018-5740).

* Wed Apr 04 2018 Stanislav Levin <slev@altlinux.org> 9.11.3-alt1
- 9.11.2.P1 -> 9.11.3

* Wed Feb 28 2018 Stanislav Levin <slev@altlinux.org> 9.11.2.P1-alt2
- Build with libjson support (statistics channels)

* Wed Jan 17 2018 Stanislav Levin <slev@altlinux.org> 9.11.2.P1-alt1
- 9.11.2 -> 9.11.2-P1 (fixes: CVE-2017-3145).

* Thu Dec 07 2017 Stanislav Levin <slev@altlinux.org> 9.11.2-alt2
- Fix lack of rndc.key in non-chrooted bind (closes: #34292).

* Fri Nov 03 2017 Stanislav Levin <slev@altlinux.org> 9.11.2-alt1
- 9.10.6 -> 9.11.2.

* Fri Jul 28 2017 Dmitry V. Levin <ldv@altlinux.org> 9.10.6-alt1
- 9.10.5-P3 -> 9.10.6.

* Tue Jul 11 2017 Dmitry V. Levin <ldv@altlinux.org> 9.10.5.P3-alt1
- 9.10.4-P8 -> 9.10.5-P3
  (fixes: CVE-2017-3140, CVE-2017-3141, CVE-2017-3142, CVE-2017-3143).

* Wed Apr 12 2017 Dmitry V. Levin <ldv@altlinux.org> 9.10.4.P8-alt1
- 9.10.4-P6 -> 9.10.4-P8 (fixes: CVE-2017-3136, CVE-2017-3137, CVE-2017-3138).
- bind.service: pass $CHROOT to named-checkconf (closes: #33239).
- bind.init: check named configuration on startup.

* Wed Feb 08 2017 Dmitry V. Levin <ldv@altlinux.org> 9.10.4-alt2
- 9.10.4-P5 -> 9.10.4-P6 (fixes CVE-2017-3135).

* Thu Jan 12 2017 Dmitry V. Levin <ldv@altlinux.org> 9.10.4-alt1
- 9.9.9-P5 -> 9.10.4-P5 (closes: #30124, #32590).
- Enabled multiprocessing support.
- bind: bind.service: fixed EnvironmentFile.
- bind: options.conf: fixed typo in comment (closes: #31359).
- bind: enabled "fixed" ordering support in rrset-order statement.
- bind: packaged named-rrchecker.
- bind: imported "dynamic-db" statement support from Fedora
  (by Sergey Bolshakov).
- bind: placed chrooted mode under control(1) (by Sergey Bolshakov).
- bind-devel: packaged bind9-config.
- bind-utils: packaged delv.

* Sat Jan 07 2017 Dmitry V. Levin <ldv@altlinux.org> 9.9.9-alt1
- 9.9.8-P4 -> 9.9.9-P5.
- Implemented early drop of linux capabilities.

* Wed Nov 02 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 9.9.8-alt5
- Applied upstream fix for CVE-2016-8864.

* Tue Sep 27 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 9.9.8-alt4
- Applied upstream fix for CVE-2016-2776.

* Thu Mar 10 2016 Fr. Br. George <george@altlinux.ru> 9.9.8-alt3
- Update to ftp://ftp.isc.org/isc/bind9/9.9.8-P2/bind-9.9.8-P4.tar.gz
- Build with --enable-fetchlimit (Closes: #31701)

* Wed Jan 20 2016 Fr. Br. George <george@altlinux.ru> 9.9.8-alt2
- Update to ftp://ftp.isc.org/isc/bind9/9.9.8-P2/bind-9.9.8-P3.tar.gz

* Thu Dec 17 2015 Fr. Br. George <george@altlinux.ru> 9.9.8-alt1
- Update to ftp://ftp.isc.org/isc/bind9/9.9.8-P2/bind-9.9.8-P2.tar.gz

* Thu Sep 03 2015 Fr. Br. George <george@altlinux.ru> 9.9.7-alt3
- Update to ftp://ftp.isc.org/isc/bind9/9.9.7-P3/bind-9.9.7-P3.tar.gz

* Wed Jul 29 2015 Fr. Br. George <george@altlinux.ru> 9.9.7-alt2
- Update to ftp://ftp.isc.org/isc/bind9/9.9.7-P2/bind-9.9.7-P2.tar.gz

* Tue Jul 28 2015 Fr. Br. George <george@altlinux.ru> 9.9.7-alt1
- Update to ftp://ftp.isc.org/isc/bind9/9.9.7-P1/bind-9.9.7-P1.tar.gz
- CVE-2015-5477 fix

* Thu Dec 11 2014 Fr. Br. George <george@altlinux.ru> 9.9.6-alt2
- Update to ftp://ftp.isc.org/isc/bind9/9.9.6-P1/bind-9.9.6-P1.tar.gz

* Tue Nov 18 2014 Fr. Br. George <george@altlinux.ru> 9.9.6-alt1
- Update to ftp://ftp.isc.org/isc/bind9/9.9.6/bind-9.9.6.tar.gz
- Fix old style autoheader AC_DEFINE
- Enable ratelimits (Closes: #30398)
- Provide initial rndc_keygen (Closes: #28034)

* Mon Oct 06 2014 Fr. Br. George <george@altlinux.ru> 9.9.5-alt3
- Build with GSSAPI

* Tue Jun 17 2014 Fr. Br. George <george@altlinux.ru> 9.9.5-alt2
- Updated to ftp://ftp.isc.org/isc/bind9/9.9.5-P1/bind-9.9.5-P1.tar.gz

* Mon Feb 03 2014 Fr. Br. George <george@altlinux.ru> 9.9.5-alt1
- Update to ftp://ftp.isc.org/isc/bind9/9.9.5/bind-9.9.5.tar.gz
- Don't package bind9-config (in favour of lib*-export)

* Thu Nov 28 2013 Fr. Br. George <george@altlinux.ru> 9.9.4-alt2
- Update to ftp://ftp.isc.org/isc/bind9/9.9.4-P1/bind-9.9.4-P1.tar.gz
- (CVE-2013-6230 is fixed in this version)

* Tue Oct 01 2013 Fr. Br. George <george@altlinux.ru> 9.9.4-alt1
- Update to ftp://ftp.isc.org/isc/bind9/9.9.4/bind-9.9.4.tar.gz

* Sun Jul 28 2013 Fr. Br. George <george@altlinux.ru> 9.9.3-alt3
- Update to ftp://ftp.isc.org/isc/bind/9.9.3-P2/bind-9.9.3-P2.tar.gz

* Tue Jun 11 2013 Fr. Br. George <george@altlinux.ru> 9.9.3-alt2
- Update to ftp://ftp.isc.org/isc/bind9/9.9.3-P1/bind-9.9.3-P1.tar.gz

* Thu Jun 06 2013 Fr. Br. George <george@altlinux.ru> 9.9.3-alt1
- Update to ftp://ftp.isc.org/isc/bind9/9.9.3/bind-9.9.3.tar.gz
- Drop alt-isc-config.patch

* Thu Mar 28 2013 Fr. Br. George <george@altlinux.ru> 9.9.2-alt5
- Update to ftp://ftp.isc.org/isc/bind9/9.9.2-P2/bind-9.9.2-P2.tar.gz
- Turn regex support off

* Fri Dec 28 2012 Fr. Br. George <george@altlinux.ru> 9.9.2-alt4
- Service file fixup

* Tue Dec 11 2012 Fr. Br. George <george@altlinux.ru> 9.9.2-alt3
- Update to 9.9.2-P1 (CVE-2012-5688 and bugfixes)
- Add systemd service file (from FC)

* Wed Nov 07 2012 Fr. Br. George <george@altlinux.ru> 9.9.2-alt2
- Fix pidfile recreation try on reload
- Replace index IDs in patches to dummy ones

* Wed Oct 17 2012 Fr. Br. George <george@altlinux.ru> 9.9.2-alt1
- Version up to 9.9.2 (CVE 5166 included)

* Wed Oct 15 2012 Fr. Br. George <george@altlinux.ru> 9.9.1-alt1
- Version up to 9.9.1-P3 (6 middle versions jump!)
- Drop outdated patches (including CVE 5166, this is insecure build)
- Adapt actual patches

* Wed Oct 10 2012 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt8
- Imported fixes for several vulnerabilities from RH bind-9.3.6-20.P1.5
  (CVE-2012-{1033,1667,4244,5166}).

* Fri Dec 16 2011 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt7
- Imported fixes for several DNSSEC vulnerabilities from RH bind
  (CVE-2009-4022, CVE-2010-0097, CVE-2010-3762, CVE-2011-4313);
  note that DNSSEC is not enabled by default.
- Enabled IPv6 support.
- Fixed RPATH issue.

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt6
- Rebuilt with libcrypto.so.10.

* Tue Jul 28 2009 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt5
- Backported upstream fix for a remote DoS bug (CVE-2009-0696).

* Thu Apr 30 2009 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt4
- Removed resolver(5) manual page (closes: #19784).

* Fri Mar 06 2009 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt3
- options.conf:
  + Removed root-delegation-only directive.
  + Added interface-interval directive example.
- Made "max open files" limit by default as large as default "max sockets" limit.

* Wed Jan 07 2009 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt2
- Updated to 9.3.6-P1 release.

* Mon Nov 24 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt1
- Updated to 9.3.6 release.

* Sun Aug 10 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.5-alt4
- Implemented automatic fdsets expansion to overcome FD_SETSIZE limit.

* Thu Aug 07 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.5-alt3
- Updated to 9.3.5-P2 release.

* Fri Jun 06 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.5-alt2
- Updated to 9.3.5-P1 release (fixes VU#800113/CVE-2008-1447).

* Wed Apr 16 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.5-alt1
- Updated to 9.3.5 release.

* Mon Nov 05 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt5
- options.conf: Added recursing-file directive.
- Updated L.ROOT-SERVERS.NET: 198.32.64.12 -> 199.7.83.42.

* Tue Jul 24 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt4
- Updated to 9.3.4-P1 release (fixes CVE-2007-2926).

* Fri Apr 06 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt3
- rndc-confgen: Revert previous change.
- Changed startup script to use /dev/urandom as a source
  of randomness during rndc key generation.

* Wed Apr 04 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt2
- rndc-confgen: Restore default key size (#11321).

* Thu Jan 25 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt1
- Updated to 9.3.4 release.

* Fri Dec 29 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.3-alt2
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Dec 09 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.3-alt1
- Updated to 9.3.3 release.

* Fri Nov 03 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.3-alt0.2
- Updated to 9.3.3 RC3.

* Sat Sep 23 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.3-alt0.1
- Updated to 9.3.3 RC2.

* Wed Sep 06 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.2-alt2
- Updated to 9.3.2 P1.

* Thu Mar 30 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.2-alt1
- Updated to 9.3.2 release.

* Tue Sep 27 2005 Dmitry V. Levin <ldv@altlinux.org> 9.3.1-alt2
- Fixed /etc/syslog.d/bind bug introduced in previous release:
  /etc/syslog.d/* must be absolute symlinks.

* Wed Sep 21 2005 Dmitry V. Levin <ldv@altlinux.org> 9.3.1-alt1
- Updated to 9.3.1 release.
- Synced with Owl's bind-9.3.1-owl1 package.
- Applied few fixes from RH and SuSE bind packages.
- Merged all shared libraries into single package, libbind.
- Replaced -debug and -slave subpackages with control facilities.
- Converted absolute symlinks into relative.

* Sat Feb 12 2005 Dmitry V. Levin <ldv@altlinux.org> 9.2.4.rel-alt2
- Fixed build of queryperf utility on x86_64 platform (closes #6083).

* Fri Sep 24 2004 Dmitry V. Levin <ldv@altlinux.org> 9.2.4.rel-alt1
- Updated to 9.2.4 release (== 9.2.4rc8).

* Sun Sep 05 2004 Dmitry V. Levin <ldv@altlinux.org> 9.2.4.rc8-alt1
- Updated to 9.2.4rc8.
- Renamed subpackage according to soname change:
  libdns11 -> libdns16.
- Updated startup script to make use of new "status --lockfile" option.

* Wed Jun 30 2004 Dmitry V. Levin <ldv@altlinux.org> 9.2.4.rc5-alt1
- Updated to 9.2.4rc5.
- Updated patches.

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 9.2.3.rel-alt2.1
- Rebuilt with openssl-0.9.7d.

* Wed Mar 10 2004 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rel-alt2
- Updated build dependencies.
- Do not build static library by default.

* Mon Nov 24 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rel-alt1
- Updated to 9.2.3 release.
- Rediffed patches.
- Do not package .la files.
- named.8: fixed reference to the BIND 9 Administrator Reference Manual.

* Mon Sep 22 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rc4-alt1
- Updated to 9.2.3rc4.
- Renamed subpackage according to soname change:
  libdns10 -> libdns11.
- Replaced "delegation-only" defaults implemented in previous release
  with new option, root-delegation-only, and enabled it by default.

* Thu Sep 18 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rc2-alt1
- Updated to 9.2.3rc2.
- Renamed subpackage according to soname change:
  libdns9 -> libdns10.
- Marked all known gTLDs and ccTLDs as delegation-only by default.

* Thu Sep 11 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rc1-alt2
- Merged patches from OpenBSD, thanks to Jarno Huuskonen:
  + write pidfile before chroot (#2866);
  + use chroot jailing by default, no -u/-t options are necessary;
- Make named-checkconf use chroot jail by default (Jarno Huuskonen).
- options.conf: added few samples (#2968).

* Tue Aug 26 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rc1-alt1
- Updated to 9.2.3rc1.
- Removed alt-lib_dns_rootns patch (merged upstream).
- Explicitly disable use of linux capabilities.
- Renamed subpackages according to soname changes:
  libdns8 -> libdns9, libisc4 -> libisc7.

* Tue Jul 29 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.2.rel-alt2
- Fixed message from 'service bind reload' (#0002411).
- Moved 'include "/etc/rfc1912.conf";' directive
  from bind.conf to local.conf (#0002791).
- Rewritten start/stop script to new rc scheme.

* Tue Mar 04 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.2.rel-alt1
- Updated to 9.2.2 release.

* Wed Feb 12 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.2.rc1-alt2
- Relocated initial rndc key generation from %%post to startup script.
- Added some information about ALT specific to named(8) and rndc(8).
- Added README.ALT.

* Thu Feb 06 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.2.rc1-alt1
- Migrated to 9.2.2rc1.
- Build --with-libtool --with-openssl --disable-ipv6 --disable-threads.
- Do not package contrib.
- Package queryperf utility.
- Package each shared library separately:
  libdns8 libisc4 libisccc0 libisccfg0 liblwres1.
- Package lwresd separately (chrooted to /var/resolv).
- Moved %_chrootdir/zone/slave to separate subpackage, %name-slave.
- Moved %_chrootdir/var/run to separate subpackage, %name-debug.
- Added nslookup(1) and resolver(5) manpages from bind8.
- Minor manpage corrections.
- isc-config.sh: fixed --cflags.
- libdns: updated root_ns list to 2002110501.
- rndc-confgen: added "-A" option support.
- Implemented default rndc settings.
- named: patched to get correct chroot jailing support.
- Updated chroot jail and relocated it to /var/lib/bind:
  default CE is now readonly.
- Renamed %_initdir/named to %_initdir/bind.
- Merged caching-nameserver into bind package.
- Split named.conf into several configurations files.
- Added more rfc1912 zones by default.
- Added rfc1918 zones (not enabled by default).

* Wed Nov 13 2002 Dmitry V. Levin <ldv@altlinux.org> 8.3.3-alt2
- Security fixes from ISC:
  + 1469. buffer length calculation for PX was wrong.
  + 1468. ns_name_ntol() could overwite a zero length buffer.
  + 1467. off by one bug in ns_makecannon().
  + 1466. large ENDS UDP buffer size could trigger a assertion.
  + 1465. possible NULL pointer dereference in db_sec.c
  + 1464. the buffer used to construct the -ve record was not
    	  big enough for all possible SOA records.  use pointer
    	  arithmetic to calculate the remaining size in this
    	  buffer.
  + 1463. use serial space arithmetic to determine if a SIG is
    	  too old, in the future or has internally constistant
    	  times.
  + 1462. write buffer overflow in make_rr().
- Changed named.init:
  + added condreload();
  + fixed argument for "-c" option.
- Changed bind chroot jail:
  + removed /var/lib;
  + removed /etc/{host,nsswitch}.conf;
  + added /etc/{protocols,services}.
- Use subst instead of perl in %%post script.
- Dont't calc perl dependencies for -contrib.

* Mon Jul 01 2002 Dmitry V. Levin <ldv@altlinux.org> 8.3.3-alt1
- Updated code to 8.3.3 release.
- Explicitly use mksock from fileutils.
- Fixed build when glibc-core-archopt is installed.
- Updated packager information.

* Tue Apr 16 2002 Dmitry V. Levin <ldv@alt-linux.org> 8.3.1-alt1
- Updated code to 8.3.1 release.
- Fixed bind to use /dev/null from core system.
- Make use of syslogd-1.4.1-alt9 /etc/syslog.d/ feature.
- Renamed /etc/chroot.d/named.* to /etc/chroot.d/bind.*
- Relaxed dependencies (conflicts instead of requires).

* Wed Oct 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.5-alt1
- 8.2.5

* Tue Sep 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.4-alt3
- Corrected manpages according to chrooted scheme.
- More manpages moved to man-pages package.

* Tue Jul 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.4-alt2
- Moved chroot from /var/named to %_localstatedir/named (according to FHS).
- Merged bind-chroot into main package.
- Updated scripts to handle new syslogd.
- Removed restart support from named.

* Thu May 31 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.4-alt1
- 8.2.4

* Mon Mar 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.3-ipl4mdk
- Updated PreReqs.

* Mon Feb 05 2001 Dmitry V. Levin <ldv@fandra.org> 8.2.3-ipl3mdk
- Fixed %%devel subpackage.

* Wed Jan 31 2001 Dmitry V. Levin <ldv@fandra.org> 8.2.3-ipl2mdk
- Pacthed db_defs.h to ease finding errors.
- Added %%triggerpostun.
- Added call for chrooted environment adjustment before server start.

* Sun Jan 28 2001 Dmitry V. Levin <ldv@fandra.org> 8.2.3-ipl1mdk
- 8.2.3
- Ported to new chrooted scheme.

* Thu Nov 16 2000 Dmitry V. Levin <ldv@fandra.org> 8.2.2_P7-ipl1mdk
- 8.2.2_P7
- Moved chrooted environment to separate subpackage.
- Removed few manpages, obsoleted by new man-pages package.

* Sat May 13 2000 Dmitry V. Levin <ldv@fandra.org>
- xfer tmpdir patch
- chrooted environment fix

* Fri Mar 10 2000 Dmitry V. Levin <ldv@fandra.org>
- fixed startup script to exit with error if no configuration available
- updated to rpm-3.0.4

* Thu Nov 11 1999 Dmitry V. Levin <ldv@fandra.org>
- 8.2.2-P3

* Sun Oct 31 1999 Dmitry V. Levin <ldv@fandra.org>
- chrooted environment
- doc and contrib packages
- optimal manpage compression
- Fandra adaptions

* Sat Oct 09 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Add lame server patch

* Fri Jul 16 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- 8.2.1

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Wed Mar 31 1999 Bill Nottingham <notting@redhat.com>
- add ISC patch
- add quick hack to make host not crash
- add more docs

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- add probing information in the init file to keep linuxconf happy
- dont strip libbind

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Wed Mar 17 1999 Preston Brown <pbrown@redhat.com>
- removed 'done' output at named shutdown.

* Tue Mar 16 1999 Cristian Gafton <gafton@redhat.com>
- version 8.2

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- patch to use the __FDS_BITS macro
- build for glibc 2.1

* Wed Sep 23 1998 Jeff Johnson <jbj@redhat.com>
- change named.restart to /usr/sbin/ndc restart

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- install man pages correctly.
- change K10named to K45named.

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- don't start if /etc/named.conf doesn't exist.

* Sat Aug  8 1998 Jeff Johnson <jbj@redhat.com>
- autmagically create /etc/named.conf from /etc/named.boot in %post
- remove echo in %post

* Wed Jun 10 1998 Jeff Johnson <jbj@redhat.com>
- merge in 5.1 mods

* Sun Apr 12 1998 Manuel J. Galan <manolow@step.es>
- Several essential modifications to build and install correctly.
- Modified 'ndc' to avoid deprecated use of '-'

* Mon Dec 22 1997 Scott Lampert <fortunato@heavymetal.org>
- Used buildroot
- patched bin/named/ns_udp.c to use <libelf/nlist.h> for include
  on Redhat 5.0 instead of <nlist.h>
