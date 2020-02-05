# -*- mode: rpm-spec; mode: folding -*-
# vim: set ft=spec:
# vim600: set fdm=marker:

%define patchlevel %nil
#define patchlevel -P1

%define _unpackaged_files_terminate_build 1

Name: dhcp
Version: 4.4.2
Release: alt1
Epoch: 1

Summary: Dynamic Host Configuration Protocol (DHCP) distribution
License: MPL-2.0
Group: System/Servers
Url: https://www.isc.org/dhcp/

%define srcname dhcp-%version%{?patchlevel:%patchlevel}
Source0: dhcp-%version.tar
Source1: dhcp-dynamic-dns-examples.tar
Source2: dhcpd.conf.sample
Source3: update_dhcp.pl
Source4: dhcpd.init
Source5: dhcrelay.init
Source8: dhcpd.sysconfig
Source9: dhcrelay.sysconfig
Source10: dhcpd.chroot.all
Source11: dhcpd.chroot.conf
Source12: dhcpd.chroot.lib
Source14: dhclient-script.alt
Source15: dhclient-hooks.tar
Source16: dhclient.sysconfig
Source17: dhcpd6.init
Source18: dhcpd6.sysconfig
Source19: dhcpd6.chroot.all
Source20: dhcpd6.chroot.conf
Source21: dhcpd6.chroot.lib
Source22: dhcrelay6.init
Source23: dhcrelay6.sysconfig
Source24: dhcrelay6
Source25: dhcpd.service
Source26: dhcpd6.service
Source27: dhcrelay.service
Source28: dhcrelay6.service

Patch0001: 0001-Apply-dhcp-3.0.5-alt-warnings.patch.patch
Patch0002: 0002-Apply-dhcp-3.0.3-alt-defaults.patch.patch
Patch0003: 0003-Apply-dhcp-3.0.3-alt-daemonize.patch.patch
Patch0004: 0004-Apply-dhcp-3.0.5-owl-alt-support-contact.patch.patch
Patch0005: 0005-Update-and-apply-dhcp-3.0.4-owl-bound.patch.patch
Patch0006: 0006-Apply-dhcp-3.0.3-rh-dhcpctl-man.patch.patch
Patch0007: 0007-Apply-dhcp-3.0.3-rh-assemble_udp_ip_header.patch.patch
Patch0008: 0008-Apply-dhcp-3.0.3-rh-failover-ports.patch.patch
Patch0009: 0009-Apply-manpage-correction-from-RH-184484.patch
Patch0010: 0010-Update-and-apply-dhcp-3.0.3-owl-alt-drop_priv.patch.patch
Patch0011: 0011-dhclient-Add-several-command-line-options-which-etcn.patch
Patch0012: 0012-dhclient-Check-if-dhclient-already-running.patch
Patch0013: 0013-dhclient-Request-more-options-by-default.patch
Patch0014: 0014-Prevent-file-descriptors-leak.patch
Patch0015: 0015-Drop-garbage-char.patch
Patch0016: 0016-Fix-segfault-in-case-of-NULL-timeout.patch
Patch0017: 0017-Ensure-64-bit-platforms-parse-lease-file-dates-times.patch
Patch0018: 0018-Support-Classless-Static-Route-Option-for-DHCPv4-RFC.patch
Patch0019: 0019-Don-t-send-log-messages-to-the-stderr-with-f-option.patch
Patch0020: 0020-Document-ALT-specific-in-the-dhclient-script-manpage.patch
Patch0021: 0021-Ignore-checksums-on-the-loopback-interface.patch
Patch0022: 0022-dhcpd-and-dhcrelay-Override-default-user-jail-dir-an.patch
Patch0023: 0023-examples-dhcpd-dhcpv6.conf-Drop-dhcpv6-lease-file-na.patch
Patch0024: 0024-fix-segfault-on-x86-64-on-8-network.patch
Patch0025: 0025-Apply-dhcp-4.3.5-bound.diff.patch
Patch0026: 0026-dhclient-Add-onetime-and-nounicast-options.patch
Patch0027: 0027-dhclient-rename-timeout-option-to-timeout.patch
Patch0028: 0028-Build-with-extern-bind-libraries.patch
Patch0029: 0029-explicitly-include-bind-headers-that-are-required.patch
Patch0030: 0030-Fix-possible-bufer-overflow.patch
Patch0031: 0031-Silence-format-truncation-warning.patch
Patch0032: 0032-Fix-printf-format.patch
Patch0033: 0033-Fix-linking.patch
Patch0034: 0034-Build-libdhcp-as-static-library.patch
Patch0035: 0035-dhclient-Fix-divide-by-zero-error.patch
Patch0036: 0036-dhclient-Don-t-hang-before-returning.patch
Patch0037: 0037-dhcrelay-fix-relaying-of-return-packets.patch
Patch0038: 0038-dhcpctl.3-avoid-undefined-manpage-macro.patch
Patch0039: 0039-fix-spelling-mistakes.patch

# due to copy_resolv_conf/copy_resolv_lib
BuildPreReq: chrooted >= 0.3

BuildPreReq: groff-base, libcap-devel

# Chrooted environments
%define ROOT %_localstatedir/%name

BuildRequires: libcap-devel
BuildRequires: libisc-export-dhcp-devel

%package common
Summary: Dynamic Host Configuration Protocol (DHCP) distribution
Group: System/Servers
BuildArch: noarch

%package client
Summary: The ISC DHCP client daemon
Group: System/Servers
Requires(pre): %name-common = %epoch:%version-%release
Requires: %name-libs = %epoch:%version-%release
# NetworkManager can use dhclient
Provides: nm-dhcp-client

%package server
Summary: The ISC DHCP server daemon
Group: System/Servers
Requires(pre): %name-common = %epoch:%version-%release
Requires: %name-libs = %epoch:%version-%release
Requires: /var/empty
Provides: %name = %epoch:%version-%release
Obsoletes: dhcp, dhcpd

%package relay
Summary: The ISC DHCP relay daemon
Group: System/Servers
Requires(pre): %name-common = %epoch:%version-%release
Requires: %name-libs = %epoch:%version-%release
Requires: /var/empty

%package omshell
Summary: The ISC DHCP OMAPI command shell tool
Group: System/Servers
Requires(pre): %name-common = %epoch:%version-%release
Requires: %name-libs = %epoch:%version-%release

%package devel
Summary: Development headers and libraries for interfacing to the DHCP server
Group: Development/Other
Requires: dhcp-common = %epoch:%version-%release
Requires: %name-libs = %epoch:%version-%release

%package libs
Summary: Shared libraries used by ISC dhcp client and server
Group: System/Libraries

# {{{ descriptions
%description
The ISC Dynamic Host Configuration Protocol distribution provides a
freely redistributable reference implementation of all aspects of the
DHCP protocol.

%description common
The ISC Dynamic Host Configuration Protocol distribution provides a
freely redistributable reference implementation of all aspects of the
DHCP protocol.

This package contains files and directories common for the ISC DHCP
client, server and relay subpackages.

%description client
The Internet Software Consortium DHCP Client, dhclient, provides a
means for configuring one or more network interfaces using the Dynamic
Host Configuration Protocol, BOOTP protocol, or if these protocols
fail, by statically assigning an address.

%description server
The Internet Software Consortium DHCP Server, dhcpd, implements the
Dynamic Host Configuration Protocol (DHCP) and the Internet Bootstrap
Protocol (BOOTP).  DHCP allows hosts on a TCP/IP network to request
and be assigned IP addresses, and also to discover information about
the network to which they are attached.  BOOTP provides similar
functionality, with certain restrictions.

%description relay
The Internet Software Consortium DHCP Relay Agent, dhcrelay, provides a
means for relaying DHCP and BOOTP requests from a subnet to which no
DHCP server is directly connected to one or more DHCP servers on other
subnets.

You will have to define the environment variable SERVERS and optionally
OPTIONS in /etc/sysconfig/dhcrelay before starting the server.

%description omshell
The OMAPI Command Shell, omshell, provides an interactive way to connect
to, query, and possibly change, the ISC DHCP Server's state via OMAPI,
the Object Management API.  By using OMAPI and omshell, you do not have
to stop, make changes, and then restart the DHCP server, but can make
the changes while the server is running.  Omshell provides a way of
accessing OMAPI.

%description devel
DHCP devel contains header files and libraries for developing
with the Internet Software Consortium (ISC) dhcpctl API.

%description libs
This package contains shared libraries used by ISC dhcp client and
server

# }}}

%prep
%setup -a1 -a15
%patch0001 -p2
%patch0002 -p2
%patch0003 -p2
%patch0004 -p2
%patch0005 -p2
%patch0006 -p2
%patch0007 -p2
%patch0008 -p2
%patch0009 -p2
%patch0010 -p2
%patch0011 -p2
%patch0012 -p2
%patch0013 -p2
%patch0014 -p2
%patch0015 -p2
%patch0016 -p2
%patch0017 -p2
%patch0018 -p2
%patch0019 -p2
%patch0020 -p2
%patch0021 -p2
%patch0022 -p2
%patch0023 -p2
%patch0024 -p2
%patch0025 -p2
%patch0026 -p2
%patch0027 -p2
%patch0028 -p2
%patch0029 -p2
%patch0030 -p2
%patch0031 -p2
%patch0032 -p2
%patch0033 -p2
%patch0034 -p2
%patch0035 -p2
%patch0036 -p2
%patch0037 -p2
%patch0038 -p2
%patch0039 -p2

install -pm644 %_sourcedir/update_dhcp.pl .
find -type f -print0 |
	xargs -r0 grep -EZl '(/etc|ETCDIR)/(dhclient|dhcpd|dhcrelay)' -- |
	xargs -r0 sed -i 's,\(/etc\|ETCDIR\)/\(dhclient\|dhcpd\|dhcrelay\),\1/%name/\2,g' --
find client -type f -not -name Makefile\* -print0 |
	xargs -r0 grep -FZl DBDIR -- |
	xargs -r0 sed -i 's,DBDIR,%ROOT/dhclient/state,g' --
find server -type f -not -name Makefile\* -print0 |
	xargs -r0 grep -FZl DBDIR -- |
	xargs -r0 sed -i 's,DBDIR,%ROOT/dhcpd/state,g' --
find server -type f -not -name Makefile\* -print0 |
	xargs -r0 grep -FZl '%ROOT/dhcpd/state/dhcpd6' -- |
	xargs -r0 sed -i 's,%ROOT/dhcpd/state/dhcpd6,%ROOT/dhcpd6/state/dhcpd6,g' --

%build
%add_optflags -fpie -fno-strict-aliasing -Wno-unused -Dlint
%ifnarch %e2k
# lcc: omapi.c:854: -Werror=array-bounds
%add_optflags -Werror
%endif

cp configure.ac+lt configure.ac
%autoreconf
%configure \
	--with-libbind=%{_includedir}/bind9 \
	--with-libbind-libs=%{_libdir}
## ./configure --copts "%optflags"
%make_build DEBUG=
## CC=%__cc DEBUG=

# {{{ install

%install
rln()
{
	local target=$1 && shift
	local source=$1 && shift
	target=`relative "$target" "$source"`
	ln -snf "$target" "%buildroot$source"
}

mkdir -p %buildroot{%ROOT,/etc/{sysconfig,%name/dhclient.d}}
%makeinstall_std \
	INSTALL='install -pm644' \
	MANINSTALL='$(INSTALL)' \
	LIBDIR=%_libdir \
	INCDIR=%_includedir \
	ADMMANDIR=%_mandir/man8 \
	FFMANDIR=%_mandir/man5 \
	LIBMANDIR=%_mandir/man3 \
	USRMANDIR=%_mandir/man1 \
	#

# dhcpd
install -pD -m600 %_sourcedir/dhcpd.conf.sample \
	%buildroot/etc/%name/dhcpd.conf.sample

install -pD -m600 doc/examples/dhcpd-dhcpv6.conf \
	%buildroot/etc/%name/dhcpd6.conf.sample

mv %buildroot/etc/*.example %buildroot/etc/%name/

for dhcpd in dhcpd dhcpd6; do
	install -pD -m755 %_sourcedir/$dhcpd.init \
		%buildroot%_initdir/$dhcpd
	install -pD -m644 %_sourcedir/$dhcpd.sysconfig \
		%buildroot/etc/sysconfig/$dhcpd
	install -pD -m644 %_sourcedir/$dhcpd.service \
		%buildroot/%systemd_unitdir/$dhcpd.service
	mkdir -p %buildroot%ROOT/$dhcpd/state
	touch %buildroot%ROOT/$dhcpd/state/$dhcpd.leases
	# Make use of syslogd-1.4.1-alt11 /etc/syslog.d/ feature.
	mkdir -p %buildroot%ROOT/$dhcpd/dev
	mksock %buildroot%ROOT/$dhcpd/dev/log
	mkdir -p %buildroot/etc/syslog.d
	ln -s %ROOT/$dhcpd/dev/log %buildroot/etc/syslog.d/$dhcpd
	# Resolver infrastructure
	for n in all conf lib; do
		install -pD -m750 "%_sourcedir/$dhcpd.chroot.$n" \
			"%buildroot/etc/chroot.d/$dhcpd.$n"
	done
	sed -i "s,%%ROOT,%ROOT/$dhcpd,g" "%buildroot/etc/chroot.d/$dhcpd."*
	mkdir -p %buildroot%ROOT/$dhcpd{/etc,/%_lib,/var/{nis,yp/binding}}
	touch %buildroot%ROOT/$dhcpd{/etc/{localtime,hosts,services,{host,nsswitch,resolv}.conf},/var/nis/NIS_COLD_START}
done

# dhcrelay
install -pD -m750 %SOURCE24 %buildroot%_sbindir/dhcrelay6
for dhcrelay in dhcrelay dhcrelay6; do
	install -pD -m755 %_sourcedir/$dhcrelay.init \
		%buildroot%_initdir/$dhcrelay
	install -pD -m644 %_sourcedir/$dhcrelay.service \
		%buildroot/%systemd_unitdir/$dhcrelay.service
	install -pD -m644 %_sourcedir/$dhcrelay.sysconfig \
		%buildroot/etc/sysconfig/$dhcrelay
done

# dhclient
mkdir -p %buildroot/%_sysconfdir/sysconfig/
install -pD -m644 %_sourcedir/dhclient.sysconfig \
	%buildroot/%_sysconfdir/sysconfig/dhclient

install -pD -m755 %SOURCE14 %buildroot/sbin/dhclient-script
rln /sbin/dhclient-script /etc/%name/
rln %_sbindir/dhclient /sbin/dhclient

mkdir -p %buildroot%ROOT/dhclient/state
touch %buildroot%ROOT/dhclient/state/dhclient.leases
echo '# DHCP client config file' > %buildroot/etc/%name/dhclient.conf
chmod 644 %buildroot/etc/%name/dhclient.conf
mkdir -p %buildroot/etc/%name/dhclient-hooks.d
cp -a dhclient-hooks/* %buildroot/etc/%name/dhclient-hooks.d
chmod 644 %buildroot/etc/%name/dhclient-hooks.d/*

# docs
%define docdir %_docdir/%srcname
rm -rf %buildroot%docdir
mkdir -p %buildroot%docdir
cp -a LICENSE README RELNOTES update_dhcp.pl doc \
	%buildroot%docdir/

# }}}

# {{{ scripts

%pre common
%_sbindir/groupadd -r -f %name

%pre client
rm -f /var/run/dhclient.restart
if [ $1 -ge 2 ] && /sbin/start-stop-daemon --stop --test --exec /sbin/dhclient --pidfile /var/run/dhclient.pid --user root >/dev/null 2>&1; then
	touch /var/run/dhclient.restart
fi

# relocate dhcp.d
if [ ! -d /etc/%name/dhclient.d -a -d /etc/%name/dhcp.d ]; then
	mv -v /etc/%name/dhcp.d /etc/%name/dhclient.d
fi

# relocate dhclient.leases
if [ ! -f %ROOT/dhclient/state/dhclient.leases -a -f %ROOT/dhclient.leases ]; then
	mkdir -p %ROOT/dhclient/state
	cp -pv %ROOT/dhclient.leases %ROOT/dhclient/state/
fi

%post client
if [ -f /var/run/dhclient.restart ]; then
	rm -f /var/run/dhclient.restart
	echo 'Please restart the ISC DHCP client daemon manually.'
fi

%pre server
%_sbindir/useradd -r -n -g %name -d %ROOT/dhcpd -s /dev/null -c 'The ISC DHCP server daemon' dhcpd >/dev/null 2>&1 ||:
%_sbindir/useradd -r -n -g %name -d %ROOT/dhcpd6 -s /dev/null -c 'The ISC DHCPv6 server daemon' dhcpd6 >/dev/null 2>&1 ||:
rm -f /var/run/dhcpd.restart
# stop _old_ dhcpd if running
if [ $1 -eq 1 ] && [ -x %_initdir/dhcpd ] && %_initdir/dhcpd status >/dev/null 2>&1; then
	%_initdir/dhcpd condstop && touch /var/run/dhcpd.restart ||:
fi

# relocate dhcpd.conf
if [ ! -f /etc/%name/dhcpd.conf -a -f /etc/dhcpd.conf ]; then
	mkdir -p /etc/%name
	mv -v /etc/dhcpd.conf /etc/%name/
fi

# relocate dhcpd.leases
if [ ! -f %ROOT/dhcpd/state/dhcpd.leases -a -f %ROOT/dhcpd.leases ]; then
	mkdir -p %ROOT/dhcpd/state
	mv -v %ROOT/dhcpd.leases %ROOT/dhcpd/state/
fi

if [ $1 = 0 ]; then
	rm -f %ROOT/dhcpd/%_lib/* %ROOT/dhcpd/var/yp/binding/*
fi

%post server
%post_service dhcpd
%post_service dhcpd6
if [ -f /var/run/dhcpd.restart ]; then
	rm -f /var/run/dhcpd.restart
	%_initdir/dhcpd start ||:
fi

%preun server
%preun_service dhcpd
%preun_service dhcpd6

%triggerpostun -- %name
[ $1 = 0 ] || exit 0
/sbin/chkconfig --add dhcpd

%pre relay
%_sbindir/useradd -r -n -g %name -d /var/empty -s /dev/null -c 'The ISC DHCP relay daemon' dhcrelay >/dev/null 2>&1 ||:
%_sbindir/useradd -r -n -g %name -d /var/empty -s /dev/null -c 'The ISC DHCPv6 relay daemon' dhcrelay6 >/dev/null 2>&1 ||:
rm -f /var/run/dhcrelay.restart
if [ $1 -ge 2 ] && [ -x %_initdir/dhcrelay ] && %_initdir/dhcrelay status >/dev/null 2>&1; then
	%_initdir/dhcrelay condstop && touch /var/run/dhcrelay.restart ||:
fi

%post relay
if [ -f /var/run/dhcrelay.restart ]; then
	rm -f /var/run/dhcrelay.restart
	%_initdir/dhcrelay start ||:
else
	%post_service dhcrelay
fi
%post_service dhcrelay6

%preun relay
%preun_service dhcrelay
%preun_service dhcrelay6

# }}}

# {{{ files

%files common
%dir %ROOT
%dir /etc/%name
%dir %docdir
%docdir/[A-Z]*
%docdir/doc

%exclude %docdir/doc/ja_JP.eucJP

%files client
%doc /etc/%name/dhclient.*.example
%config(noreplace) /etc/%name/dhclient.conf
%config(noreplace) %_sysconfdir/sysconfig/dhclient
%_sysconfdir/%name/dhclient-hooks.d
%attr(755,root,dhcp) /etc/%name/dhclient-script
%attr(750,root,dhcp) /sbin/dhclient*
%attr(750,root,dhcp) %_sbindir/dhclient*
%_man5dir/dhclient.*
%_man8dir/dhclient*
%attr(700,root,dhcp) %dir %ROOT/dhclient
%attr(700,root,dhcp) %dir %ROOT/dhclient/state
%attr(644,root,dhcp) %config(noreplace) %verify(not md5 mtime size) %ROOT/dhclient/state/dhclient.leases

%files server
/etc/syslog.d/*
%config /etc/chroot.d/dhcpd.*
%config /etc/chroot.d/dhcpd6.*
%config %_initdir/dhcpd
%config %_initdir/dhcpd6
%systemd_unitdir/dhcpd.service
%systemd_unitdir/dhcpd6.service
%config(noreplace) /etc/sysconfig/dhcpd
%config(noreplace) /etc/sysconfig/dhcpd6
%attr(750,root,dhcp) %_sbindir/dhcpd
%_man5dir/dhcpd.*
%_man5dir/dhcp-options.*
%_man5dir/dhcp-eval.*
%_man8dir/dhcpd.*
# IPv4 chroot
%attr(0750,root,dhcp) %dir %ROOT/dhcpd
%attr(1770,root,dhcp) %dir %ROOT/dhcpd/state
%attr(0644,dhcpd,dhcp) %config(noreplace) %verify(not md5 mtime size) %ROOT/dhcpd/state/dhcpd.leases
%dir %attr(0710,root,dhcp) %ROOT/dhcpd/dev
%ghost %attr(666,root,root) %ROOT/dhcpd/dev/*
#IPv6 chroot
%attr(0750,root,dhcp) %dir %ROOT/dhcpd6
%attr(1770,root,dhcp) %dir %ROOT/dhcpd6/state
%attr(0644,dhcpd6,dhcp) %config(noreplace) %verify(not md5 mtime size) %ROOT/dhcpd6/state/dhcpd6.leases
%dir %attr(0710,root,dhcp) %ROOT/dhcpd6/dev
%ghost %attr(666,root,root) %ROOT/dhcpd6/dev/*

# Resolver infrastructure
# IPv4
%dir %ROOT/dhcpd/%_lib
%dir %ROOT/dhcpd/etc
%ghost %verify(not md5 mtime size) %ROOT/dhcpd/etc/*
%dir %ROOT/dhcpd/var
%dir %ROOT/dhcpd/var/nis
%ghost %config(missingok) %verify(not md5 mtime size) %ROOT/dhcpd/var/nis/NIS_COLD_START
%dir %ROOT/dhcpd/var/yp
%dir %ROOT/dhcpd/var/yp/binding
# IPv6
%dir %ROOT/dhcpd6/%_lib
%dir %ROOT/dhcpd6/etc
%ghost %verify(not md5 mtime size) %ROOT/dhcpd6/etc/*
%dir %ROOT/dhcpd6/var
%dir %ROOT/dhcpd6/var/nis
%ghost %config(missingok) %verify(not md5 mtime size) %ROOT/dhcpd6/var/nis/NIS_COLD_START
%dir %ROOT/dhcpd6/var/yp
%dir %ROOT/dhcpd6/var/yp/binding

%dir /etc/%name
%doc /etc/%name/dhcpd.*.example
%doc /etc/%name/dhcpd.conf.sample
%doc /etc/%name/dhcpd6.conf.sample
%dir %docdir
%docdir/update_dhcp.pl

%files relay
%config %_initdir/dhcrelay
%systemd_unitdir/dhcrelay.service
%config(noreplace) /etc/sysconfig/dhcrelay
%config %_initdir/dhcrelay6
%systemd_unitdir/dhcrelay6.service
%config(noreplace) /etc/sysconfig/dhcrelay6
%attr(750,root,dhcp) %_sbindir/dhcrelay
%attr(750,root,dhcp) %_sbindir/dhcrelay6
%_man8dir/dhcrelay.*

%files omshell
%_bindir/omshell
%_man1dir/omshell.*
  
%files devel
%_includedir/*
%_libdir/libdhcpctl.so
%_libdir/libomapi.so
%_man3dir/*

%files libs
%_libdir/libdhcpctl.so.*
%_libdir/libomapi.so.*

%exclude %_libdir/lib*.a

# }}}

%changelog
* Fri Jan 24 2020 Mikhail Efremov <sem@altlinux.org> 1:4.4.2-alt1
- Fixed license tag.
- Updated patches.
- Updated to 4.4.2.

* Fri Oct 25 2019 Mikhail Efremov <sem@altlinux.org> 1:4.4.1-alt2
- Don't use deprecated PreReq.
- Fixed build on e2kv4 through %%e2k macro (by Michael Shigorin).
- Fixed build with gcc-9.
- Updated Url.
- Updated license.

* Fri Dec 07 2018 Mikhail Efremov <sem@altlinux.org> 1:4.4.1-alt1
- Added patches from Debian.
- Updated patches.
- Updated to 4.4.1.

* Wed Feb 28 2018 Mikhail Efremov <sem@altlinux.org> 1:4.3.6.P1-alt1
- Updated patches.
- Updated to 4.3.6-P1 (fixes: CVE-2017-3144,CVE-2018-5732,CVE-2018-5733).

* Tue Aug 29 2017 Mikhail Efremov <sem@altlinux.org> 1:4.3.6-alt1
- dhclient: rename -timeout option to --timeout.
- dhclient: Add --onetime and --nounicast options.
- Added bound.patch.
- dhclient: rename our -R option to --request-options.
- dhclient: rename our -I option to -C.
- Updated patches.
- Updated to 4.3.6.

* Wed Apr 05 2017 Michael Shigorin <mike@altlinux.org> 1:4.3.3-alt5.1
- E2K: ignore array bounds warning (lcc).

* Wed Feb 01 2017 Mikhail Efremov <sem@altlinux.org> 1:4.3.3-alt5
- Use _unpackaged_files_terminate_build.
- Build with bind-9.9.9 libraries (closes: #33053).

* Thu Jan 12 2017 Mikhail Efremov <sem@altlinux.org> 1:4.3.3-alt4
- Rebuilt with bind 9.10.4.
- Patches tweaked for use with recent bind (by Sergey Bolshakov).

* Wed Jan 11 2017 Dmitry V. Levin <ldv@altlinux.org> 1:4.3.3-alt3
- Rebuilt with bind-9.9.9.

* Wed Jan 13 2016 Fr. Br. George <george@altlinux.ru> 1:4.3.3-alt2
- Update to 4.3.3-P1

* Mon Dec 21 2015 Fr. Br. George <george@altlinux.ru> 1:4.3.3-alt1
- Update to 4.3.3
- Fix patches

* Mon Dec 21 2015 Fr. Br. George <george@altlinux.ru> 1:4.3.2-alt1
- Update to 4.3.2
- Fix patches

* Mon Dec 21 2015 Fr. Br. George <george@altlinux.ru> 1:4.3.1-alt4
- Rabuild with bind-9.9.8

* Wed Jul 29 2015 Fr. Br. George <george@altlinux.ru> 1:4.3.1-alt3
- Rebuild with bind-9.9.7

* Tue Nov 25 2014 Fr. Br. George <george@altlinux.ru> 1:4.3.1-alt2
- Rebuild with bind-9.9.6

* Tue Sep 23 2014 Fr. Br. George <george@altlinux.ru> 1:4.3.1-alt1
- Update to ftp://ftp.isc.org/isc/dhcp/4.3.1/dhcp-4.3.1.tar.gz
- Fix patches (drop some reimplemented by upstream)

* Thu Sep 18 2014 Fr. Br. George <george@altlinux.ru> 1:4.3.0-alt1
- Update to ftp://ftp.isc.org/isc/dhcp/4.3.0/dhcp-4.3.0.tar.gz
- Fix patches

* Wed Feb 05 2014 Fr. Br. George <george@altlinux.ru> 1:4.2.6-alt1
- Update to ftp://ftp.isc.org/isc/dhcp/4.2.6/dhcp-4.2.6.tar.gz

* Wed Oct 02 2013 Fr. Br. George <george@altlinux.ru> 1:4.2.5-alt3
- Rebuild with bind-9.9.4

* Thu Jun 13 2013 Fr. Br. George <george@altlinux.ru> 1:4.2.5-alt2
- Update to ftp://ftp.isc.org/isc/dhcp/4.2.5-P1/dhcp-4.2.5-P1.tar.gz
- Rebuild with bind-9.9.3

* Mon Feb 25 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:4.2.5-alt1
- george@:
  + Version update to 4.2.5
  + Fix patches
  + Add example files
- fix segfault on x86_64 (ALT #28559)

* Tue Dec 04 2012 Mikhail Efremov <sem@altlinux.org> 1:4.2.4.P2-alt5
- Add *.service files for systemd (closes: #28041).
- Add dhcrelay6 wrapper.

* Wed Nov 28 2012 Mikhail Efremov <sem@altlinux.org> 1:4.2.4.P2-alt4
- Install dhcpd6.conf.sample.
- dhcp-client: Provide nm-dhcp-client.
- dhclient-hooks: Handle classless-static-routes.
- Drop dhcpv6-lease-file-name from dhcpd6.conf.sample.

* Mon Nov 26 2012 Mikhail Efremov <sem@altlinux.org> 1:4.2.4.P2-alt3
- Fix dhcrelay permissions.
- dhcrelay6: Added init script and config.
- dhcpd6: Added init script and configs.
- dhcpd and dhcrelay: Override default user and jail dir for DHCPv6.
- Added lost command-line options.

* Tue Oct 30 2012 Mikhail Efremov <sem@altlinux.org> 1:4.2.4.P2-alt2
- Don't package ja_JP man pages.
- dhcpd.init: Update dhcpd chroot jail on start.
- Add patch from Debian and patch for manpage.
- Package libdhcpctl.so.* and libomapi.so.* as separate subpackage.
- Package dhclient.sysconfig.
- Add patches from Fedora.
- Add ALT-specific dhclient script.

* Thu Oct 18 2012 Fr. Br. George <george@altlinux.ru> 1:4.2.4.P2-alt1
- Major (!) version up to 4.2.4-P2
- Switching back to patches + upstream packaging scheme


* Fri Dec 02 2011 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.7-alt8
- Fixed build on Linux 3.x.

* Mon Feb 07 2011 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.7-alt7
- Minor specfile cleanup.

* Wed Dec 15 2010 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.7-alt6
- %name-common: packaged as noarch.

* Wed Dec 15 2010 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.7-alt5
- Fixed build with gcc-4.5.

* Thu Jul 16 2009 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.7-alt4
- server/dhcp.c (ack_lease): Imported fix for potential
  premature server termination (Christoph Biedl; CVE-2009-1892).

* Wed Jul 15 2009 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.7-alt3
- dhclient: Imported upstream fix for potential stack-based
  buffer overflow (CVE-2009-0692).

* Tue May 12 2009 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.7-alt2
- Fixed build with fresh toolchain (by Dmitry Afanasov).

* Thu May 29 2008 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.7-alt1
- Updated to 3.0.7 release.

* Thu Oct 18 2007 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.6-alt2
- Replaced contrib/sethostname.sh with clean implementation.
- Disabled startup scripts by default (#11858).
- Simplified lowering privileges algorithm.

* Mon Jul 09 2007 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.6-alt1
- Updated to 3.0.6 release.

* Mon Nov 06 2006 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.5-alt1
- Updated to 3.0.5 release.
- Imported a bounds checking patch from Owl.

* Fri Oct 13 2006 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.5-alt0.3
- Updated to 3.0.5 rc3.
- Fixed build with -D_FORTIFY_SOURCE=2 -Werror.

* Tue Sep 05 2006 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.5-alt0.2
- Updated to 3.0.5 rc2.

* Thu Jun 08 2006 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.4-alt1
- Updated to 3.0.4 release.
- Packaged libdst.a (#8990).

* Wed Oct 26 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.3-alt1
- Updated to 3.0.3 release.
- Updated patches.
- Imported few patches from RH's dhcp-3.0.3-10 package.
- dhcpd, dhcrelay: Fixed daemonize code.
- dhcpd: Enhanced droppriv patch to handle failover protocol
  (fixes #8346).

* Mon Apr 18 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.2-alt1
- Updated to 3.0.2 release.
- Updated patches.
- Fixed license tag (distributable -> BSD-like).
- Provided the proper support contact information.
- dhcp-server:
  + disabled %%verify check for files which are
    ususally changed after package installation.
  + relocated dhcpd.conf.sample to /etc/%name/,
    changed startup script to point at this sample
    when needed (#5676).

* Thu Oct 28 2004 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.1-alt12
- dhcp-server: Package /etc/syslog.d/%name symlink.

* Thu Aug 12 2004 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.1-alt11
- dhcp-server: Complemented resolver infrastructure added
  in previous release.

* Wed Aug 11 2004 Dmitry V. Levin <ldv@altlinux.org> 1:3.0.1-alt10
- Updated to 3.0.1 release.
- Added resolver infrastructure to the dhcpd chroot jail.

* Mon Jul  5 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:3.0.1-alt9
- fixed #4665

* Sun Jun 27 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:3.0.1-alt8
- 3.0.1rc14
- applying changes from Dmitry V. Levin <ldv@altlinux.org> :
  + Renamed dhcp subpackage to dhcp-server subpackage.
  + Merged -devel-static subpackage into -devel subpackage.
  + Merged Owl patches:
    rh-owl-alt-script, owl-man, owl-alt-warnings, owl-alt-drop_priv.
  + Implemented chroot jailing for dhcpd and dhcrelay by default;
    changed location of leases files.
  + Rewritten startup scripts to new rc scheme;
    removed extra ifconfig logic for a while.
  + Updated summaries and descriptions.
  + Corrected interpackage dependencies.
  + Moved update_dhcp.pl script to %%doc.
  + Relocated documentation to %_docdir/%srcname.
  + Changed default dhcpd config location to /etc/%name/dhcpd.conf.
  + Changed /etc/%name/dhcp.d to /etc/%name/dhclient.d.
  + Specfile cleanup.

* Wed Jun 23 2004 Grigory Milev <week@altlinux.ru> 1:3.0.1-alt7.rc14
- new version released

* Thu Feb 26 2004 Grigory Milev <week@altlinux.ru> 1:3.0.1-alt6.rc13
- new version released
- fix start/stop dhcprelay script
- fix start/stop dhcp script

* Mon Apr 21 2003 Grigory Milev <week@altlinux.ru> 1:3.0.1-alt5
- new version released (3.0.1rc11)
- added config dir /etc/dhcp && hooks dir /etc/dhcp/dhcp.d
- added dhclient-enter-hooks && dhclient-exit-hooks

* Mon Dec  9 2002 Grigory Milev <week@altlinux.ru> 1:3.0.1-alt4
- new rc version released
- security patch added: Potential Vulnerabilities in ISC DHCPD [VU#284857]

* Wed Oct 30 2002 Stanislav Ievlev <inger@altlinux.ru> 1:3.0.1-alt3
- real changelog fix. Grigory, please use normal add_changelog util

* Fri Oct 25 2002 Grigory Milev <week@altlinux.ru> 3.0.1-alt2
- rebuild with gcc3.2
- mv dhclient-script to /sbin
  make link /sbin/dhclient-script -> /etc/dhclient-script for compatible

* Wed Oct 23 2002 Grigory Milev <week@altlinux.ru> 3.0.1-alt1
- rebuild with gcc3

* Wed May 15 2002 Grigory Milev <week@altlinux.ru> 3.0.1-alt0.8
- new rc version released with security patches

* Tue Mar 26 2002 Grigory Milev <week@altlinux.ru> 3.0.1-alt0.7
- make dhcpd.leases as noreplace config file

* Thu Mar 21 2002 Grigory Milev <week@altlinux.ru> 3.0.1-alt0.6
- Fixed init script to work with chkconfig

* Thu Feb 21 2002 Grigory Milev <week@altlinux.ru> 3.0.1-alt0.5
- rewriten init script, for correct work with ethernet
  aliases (ex: eth0:1) and subnet test for available
  in dhcpd.conf (thanks to Vadim Illarionov <DIMMeach@NewMail.ru>)

* Wed Feb 20 2002 Grigory Milev <week@altlinux.ru> 3.0.1-alt0.4
- fixed init script
- remake post and preun scripts

* Fri Feb 15 2002 Grigory Milev <week@altlinux.ru> 3.0.1-alt0.3
- fixed post uninstall script

* Tue Feb 12 2002 Grigory Milev <week@altlinux.ru> 3.0.1-alt0.2
- correct init script for find interfaces from ifcfg scripts
- if you need dhcp on some interface, add DHCP=yes to ifcfg script
- minor spec cleanup

* Mon Nov 05 2001 Konstantin Volckov <goldhead@altlinux.ru> 3.0.1-alt0.1
- 3.0.1rc3
- Added devel, devel-static, omshell, relay & common packages

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 2.0pl5-ipl2mdk
- RE adaptions.

* Fri Nov 17 2000 Florin Grad <florin@mandrakesoft.com> 2.0pl5-2mdk
- chkconfig is now set to 3,4,5

* Mon Nov 06 2000 Florin Grad <florin@mandrakesoft.com> 2.0pl5-1mdk
- Mandrake adaptations. this is the actual stable version

* Sun Sep 10 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 2.0pl5
- redo buildroot patch

* Wed Aug 30 2000 Matt Wilson <msw@redhat.com>
- rebuild to cope with glibc locale binary incompatibility, again

* Mon Aug 14 2000 Preston Brown <pbrown@redhat.com>
- check for existence of /var/lib/dhcpd.leases in initscript before starting

* Wed Jul 19 2000 Jakub Jelinek <jakub@redhat.com>
- rebuild to cope with glibc locale binary incompatibility

* Sat Jul 15 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jul  7 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- /etc/rc.d/init.d -> /etc/init.d
- fix /var/state/dhcp -> /var/lib/dhcp

* Fri Jun 16 2000 Preston Brown <pbrown@redhat.com>
- condrestart for initscript, graceful upgrades.

* Thu Feb 03 2000 Erik Troan <ewt@redhat.com>
- gzipped man pages
- marked /etc/rc.d/init.d/dhcp as a config file

* Mon Jan 24 2000 Jakub Jelinek <jakub@redhat.com>
- fix booting of JavaStations
  (reported by Pete Zaitcev <zaitcev@metabyte.com>).
- fix SIGBUS crashes on SPARC (apparently gcc is too clever).

* Fri Sep 10 1999 Bill Nottingham <notting@redhat.com>
- chkconfig --del in %preun, not %postun

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging

* Fri Jun 25 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.0.

* Fri Jun 18 1999 Bill Nottingham <notting@redhat.com>
- don't run by default

* Wed Jun  2 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.0b1pl28.

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip binaries

* Mon Apr 05 1999 Cristian Gafton <gafton@redhat.com>
- copy the source file in %prep, not move

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Mon Jan 11 1999 Erik Troan <ewt@redhat.com>
- added a sample dhcpd.conf file
- we don't need to dump rfc's in /usr/doc

* Sun Sep 13 1998 Cristian Gafton <gafton@redhat.com>
- modify dhcpd.init to exit if /etc/dhcpd.conf is not present

* Sat Jun 27 1998 Jeff Johnson <jbj@redhat.com>
- Upgraded to 2.0b1pl6 (patch1 no longer needed).

* Thu Jun 11 1998 Erik Troan <ewt@redhat.com>
- applied patch from Chris Evans which makes the server a bit more paranoid
  about dhcp requests coming in from the wire

* Mon Jun 01 1998 Erik Troan <ewt@redhat.com>
- updated to dhcp 2.0b1pl1
- got proper man pages in the package

* Tue Mar 31 1998 Erik Troan <ewt@redhat.com>
- updated to build in a buildroot properly
- don't package up the client, as it doens't work very well <sigh>

* Tue Mar 17 1998 Bryan C. Andregg <bandregg@redhat.com>
- Build rooted and corrected file listing.

* Mon Mar 16 1998 Mike Wangsmo <wanger@redhat.com>
- removed the actual inet.d links (chkconfig takes care of this for us)
  and made the %postun section handle upgrades.

* Mon Mar 16 1998 Bryan C. Andregg <bandregg@redhat.com>
- First package.

