%def_with libidn2

Name: dnsmasq
Version: 2.83

Release: alt1
Summary: A lightweight caching nameserver
License: GPLv2+
Group: System/Servers
Url: http://www.thekelleys.org.uk/dnsmasq
Vcs: git://thekelleys.org.uk/dnsmasq.git
Source0: %name-%version.tar
Source1: %name.init
Source2: %name.sysconfig
Source3: %name-helper
Source4: %name.service
Patch: %name-%version-%release.patch

BuildPreReq: glibc-kernheaders

# IDN
%if_with libidn2
BuildRequires: libidn2-devel
%else
BuildRequires: libidn-devel
%endif

# DNSSEC
BuildRequires: libnettle-devel libgmp-devel

%define sysconfig_file %_sysconfdir/sysconfig/%name
%define _unpackaged_files_terminate_build 1

Summary(ru_RU.UTF-8): Компактный сервер DNS и DHCP для локальных сетей

%description
Dnsmasq is lightweight, easy to configure DNS forwarder and DHCP server. It
is designed to provide DNS and, optionally, DHCP, to a small network. It can
serve the names of local machines which are not in the global DNS. The DHCP
server integrates with the DNS server and allows machines with DHCP-allocated
addresses to appear in the DNS with names configured either in each host or
in a central configuration file. Dnsmasq supports static and dynamic DHCP
leases and BOOTP for network booting of diskless machines.

%description -l ru_RU.UTF-8
Dnsmasq - это компактный, простой в настройке сервер DNS и DHCP,
разработанный для использования в небольших сетях.
По умолчанию он использует общесистемные файлы /etc/hosts и /etc/resolv.conf,
поэтому может использоваться без настройки сразу после установки.

Очень удобными функциями являются прозрачное переопределение внешних имён
через /etc/hosts и трансляция имени в наиболее подходящий клиенту IP-адрес,
если для имени определено несколько адресов из разных подсетей.

%package        utils
Summary:        Utilities for manipulating DHCP server leases
Group:          Networking/Other

%description    utils
Utilities that use the standard DHCP protocol to
query/remove a DHCP server's leases.

%prep
%setup
%patch -p1

# Setup version
sed -r -i "s;-DVERSION=.+;-DVERSION='\\\\\"%version\\\\\"';" Makefile

#enable IDN support
%if_with libidn2
sed -i 's;/\* #define HAVE_LIBIDN2 \*/;#define HAVE_LIBIDN2;' src/config.h
%else
sed -i 's;/\* #define HAVE_IDN \*/;#define HAVE_IDN;' src/config.h
%endif

#enable DNSSEC support
sed -i 's;/\* #define HAVE_DNSSEC \*/;#define HAVE_DNSSEC;' src/config.h

%build
%make_build
%make_build -C contrib/lease-tools

%install
%makeinstall_std PREFIX=%prefix

install -d -m770 %buildroot%_sysconfdir/dnsmasq.conf.d
install -pD -m744 %SOURCE1            %buildroot%_initdir/%name
install -pD -m600 %SOURCE2            %buildroot%sysconfig_file
install -pD -m600 %name.conf.example  %buildroot%_sysconfdir/%name.conf
install -pD -m755 %SOURCE3            %buildroot%_sbindir/%name-helper
install -pD -m644 %SOURCE4            %buildroot%_unitdir/%name.service

# For utils package
install -pD -m 755 contrib/lease-tools/dhcp_release %buildroot%_bindir/dhcp_release
install -pD -m 644 contrib/lease-tools/dhcp_release.1 %buildroot%_man1dir/dhcp_release.1
install -pD -m 755 contrib/lease-tools/dhcp_lease_time %buildroot%_bindir/dhcp_lease_time
install -pD -m 644 contrib/lease-tools/dhcp_lease_time.1 %buildroot%_man1dir/dhcp_lease_time.1

# For DNSSEC support
install -pD -m 644 trust-anchors.conf %buildroot%_datadir/%name/trust-anchors.conf

%pre
# Upgrade configuration from previous versions
if test -e %sysconfig_file; then
if egrep -q '^[^#]*ALL *=' %sysconfig_file; then
    if ! egrep -q '^[^#]*ALL_DEV *=' %sysconfig_file; then
	echo 'NOTE: You should put ALL_DEV=<interface> to %sysconfig_file'
	echo '      for keeping DHCP broadcasts mode.'
    fi
fi
fi
# Create dnsmasq user
groupadd -r -f _dnsmasq ||:
useradd -r -g _dnsmasq -d /dev/null -s /dev/null -N _dnsmasq >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc CHANGELOG FAQ doc.html setup.html CHANGELOG.archive
%config(noreplace) %_sysconfdir/%name.conf
%dir %_datadir/%name/
%config(noreplace) %_datadir/%name/trust-anchors.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%dir %_sysconfdir/dnsmasq.conf.d
%_unitdir/%name.service
%_initdir/%name
%_sbindir/%{name}*
%_man8dir/%{name}*
%doc contrib/dnslist contrib/dynamic-dnsmasq

%files utils
%_bindir/dhcp_*
%_man1dir/dhcp_*

%changelog
* Fri Jan 22 2021 Mikhail Efremov <sem@altlinux.org> 2.83-alt1
- Use useradd -N instead of -n.
- Updated to 2.83 (fixes: CVE-2020-25681, CVE-2020-25682, CVE-2020-25683,
    CVE-2020-25684, CVE-2020-25685, CVE-2020-25686, CVE-2020-25687).

* Mon Jul 27 2020 Mikhail Efremov <sem@altlinux.org> 2.82-alt1
- Updated to 2.82.

* Mon Apr 13 2020 Mikhail Efremov <sem@altlinux.org> 2.81-alt1
- Add Vcs tag.
- Don't use rpm-build-licenses.
- Updated to 2.81.

* Thu Aug 15 2019 Mikhail Efremov <sem@altlinux.org> 2.80-alt3
- Patches from upstream:
  + Fix breakage of dhcp_lease_time utility.
  + Fix memory leak in helper.c.
  + Fix build with libnettle 3.5.

* Mon Jul 08 2019 Mikhail Efremov <sem@altlinux.org> 2.80-alt2
- Fix build with glibc kernheaders 5.2.
- dnsmasq.init: Fix indentation.
- dnsmasq-helper: Fix indentation.

* Tue Oct 23 2018 Mikhail Efremov <sem@altlinux.org> 2.80-alt1
- init: Don't use netstat (closes: #34783).
- Use its own user to run dnsmasq service.
- Updated to 2.80.

* Wed Apr 18 2018 Mikhail Efremov <sem@altlinux.org> 2.79-alt1
- Updated to 2.79.

* Mon Jan 22 2018 Mikhail Efremov <sem@altlinux.org> 2.78-alt2
- Build with libidn2 instead of libidn.

* Fri Oct 06 2017 Mikhail Efremov <sem@altlinux.org> 2.78-alt1
- Updated to 2.78 (fixes: CVE-2017-13704, CVE-2017-14491,
    CVE-2017-14492, CVE-2017-14493, CVE-2017-14494, CVE-2017-14495,
    CVE-2017-14496).

* Wed Jun 14 2017 Mikhail Efremov <sem@altlinux.org> 2.77-alt1
- Patch from upstream:
  + Fix logic of appending ".<layer>" to PXE basename.
- Add libidn2 support, but disable it by default.
- Drop obsoleted patch.
- Convert Russian description to UTF-8.
- Updated to 2.77.

* Tue May 02 2017 Mikhail Efremov <sem@altlinux.org> 2.76-alt3
- dnsmasq.{init,service}: Don't use dnsmasq-helper prestart.
- dnsmasq-helper: Don't rely on AUTO_LOCAL_RESOLVER in
  stop_resolvconf().
- dnsmasq-helper: First call stop_relovconf() at poststop.
- dnsmasq-helper: Move start_resolvconf() to poststart.

* Thu Dec 15 2016 Mikhail Efremov <sem@altlinux.org> 2.76-alt2
- Rebuilt with libnettle-3.3 due to ABI breakage.
- Handle binding upstream servers to an interface.

* Fri May 20 2016 Mikhail Efremov <sem@altlinux.org> 2.76-alt1
- Updated to 2.76.

* Thu Dec 03 2015 Mikhail Efremov <sem@altlinux.org> 2.75-alt3
- Rebuild with nettle-3.x.

* Fri Sep 18 2015 Mikhail Efremov <sem@altlinux.org> 2.75-alt2
- Avoid dependency on /sbin/resolvconf.

* Fri Aug 07 2015 Mikhail Efremov <sem@altlinux.org> 2.75-alt1
- systemd: Add Wants=network-online.target.
- Updated to 2.75.

* Mon Jun 15 2015 Mikhail Efremov <sem@altlinux.org> 2.73-alt1
- systemd: Fix dnsmasq start order (closes: #31025).
- Updated to 2.73.

* Tue Nov 11 2014 Lenar Shakirov <snejok@altlinux.ru> 2.72-alt2
- /usr/sbin/dnsmasq{-helper} mode relaxed from 700 to 755

* Mon Sep 29 2014 Mikhail Efremov <sem@altlinux.org> 2.72-alt1
- Updated to 2.72.

* Mon May 26 2014 Mikhail Efremov <sem@altlinux.org> 2.71-alt1
- Updated to 2.71.

* Mon Apr 14 2014 Mikhail Efremov <sem@altlinux.org> 2.69-alt1
- Fix conf-file path for DNSSEC.
- Enable DNSSEC support.
- Cleanup changelog.
- Updated to 2.69.

* Wed Jan 15 2014 Mikhail Efremov <sem@altlinux.org> 2.68-alt2
- Add 'utils' subpackage (thx Denis Pynkin) (closes: #29726).

* Mon Dec 09 2013 Mikhail Efremov <sem@altlinux.org> 2.68-alt1
- Updated to 2.68.

* Mon Oct 28 2013 Mikhail Efremov <sem@altlinux.org> 2.67-alt1
- Updated to 2.67.

* Fri Apr 19 2013 Mikhail Efremov <sem@altlinux.org> 2.66-alt1
- Patch from upstream git:
  + Fix wrong size in memset() call.
- Enable IDN support.
- Drop obsoleted patch.
- Updated to 2.66.

* Mon Mar 11 2013 Mikhail Efremov <sem@altlinux.org> 2.65-alt2
- dnsmasq-helper: Fix exit status (closes: #28658).

* Wed Mar 06 2013 Mikhail Efremov <sem@altlinux.org> 2.65-alt1
- Patch from Fedora:
  + Fix for CVE-2013-0198 (checking of TCP connection interfaces)
- Improved resolvconf support.
- Added dnsmasq.service.
- Added dnsmasq-helper script.
- Drop 'build without resolvconf' support.
- Updated to 2.65.

* Fri Aug 24 2012 Mikhail Efremov <sem@altlinux.org> 2.63-alt1
- Updated to new version 2.63.

* Thu Jun 07 2012 Mikhail Efremov <sem@altlinux.org> 2.62-alt1
- Updated to new version 2.62.

* Tue May 01 2012 Mikhail Efremov <sem@altlinux.org> 2.61-alt1
- updated to new version 2.61.

* Sun Mar 11 2012 Mikhail Efremov <sem@altlinux.org> 2.60-alt1
- updated to new version 2.60.

* Tue Nov 01 2011 Mikhail Efremov <sem@altlinux.org> 2.59-alt1
- updated to new version 2.59.

* Sat Feb 26 2011 Mikhail Efremov <sem@altlinux.org> 2.57-alt1
- Minor spec cleanup.
- updated to new version 2.57 (closes: #25157).

* Thu Feb 17 2011 Mikhail Efremov <sem@altlinux.org> 2.56-alt1
- init script: Drop ALT Linux version less then M24 support.
- updated to new version 2.56

* Mon Sep 06 2010 Mikhail Efremov <sem@altlinux.org> 2.55-alt2
- init script: fix failure handling during start.

* Tue Jun 08 2010 Mikhail Efremov <sem@altlinux.org> 2.55-alt1
- updated to new version 2.55

* Mon Jun 07 2010 Mikhail Efremov <sem@altlinux.org> 2.53-alt1
- drop -fno-strict-aliasing compiler option.
- updated to new version 2.53

* Mon Mar 01 2010 Mikhail Efremov <sem@altlinux.org> 2.52-alt1
- updated to new version 2.52

* Wed Dec 09 2009 Mikhail Efremov <sem@altlinux.org> 2.51-alt1
- updated to new version 2.51

* Wed Dec 09 2009 Mikhail Efremov <sem@altlinux.org> 2.46-alt1.3
- require openresolv-dnsmasq.

* Mon Nov 09 2009 Mikhail Efremov <sem@altlinux.org> 2.46-alt1.2
- slightly spec cleanup.
- Don't remove files for resolvconf if dnsmasq under NM is present.

* Mon Jun 22 2009 Mikhail Efremov <sem@altlinux.org> 2.46-alt1.1
- NMU:
- fno-strict-aliasing compiler option is added.
- fixed pointer cast.
- do not start dnsmasq by default.
- init script: condreload is added.
- resolvconf support (closes: #17398, #19369).

* Mon Jan 12 2009 Ilya Evseev <evseev@altlinux.ru> 2.46-alt1
- updated to new version 2.46

* Sun Sep 28 2008 Ilya Evseev <evseev@altlinux.ru> 2.45-alt2
- added packager field, upgrade kernel-headers dependency

* Sat Sep 27 2008 Ilya Evseev <evseev@altlinux.ru> 2.45-alt2
- updated to new version 2.45

* Tue Apr 29 2008 Ilya Evseev <evseev@altlinux.ru> 2.41-alt3
- enable ISC DHCPD reader, needed for libvirt/qemu

* Wed Apr  9 2008 Ilya Evseev <evseev@altlinux.ru> 2.41-alt2
- bugfix #15277

* Fri Feb 15 2008 Ilya Evseev <evseev@altlinux.ru> 2.41-alt1
- updated to new version 2.41

* Sun Sep  2 2007 Ilya Evseev <evseev@altlinux.ru> 2.40-alt1
- updated to new version 2.40

* Tue May  1 2007 Ilya Evseev <evseev@altlinux.ru> 2.39-alt1
- updated to new version 2.39

* Sat Feb 24 2007 Ilya Evseev <evseev@altlinux.ru> 2.38-alt1
- updated to new version 2.38
- specfile: better russian description

* Wed Feb  7 2007 Ilya Evseev <evseev@altlinux.ru> 2.37-alt1
- updated to new version 2.37
- cleanup specfile from obsoleted ALM22-related stuff

* Mon Jan 22 2007 Ilya Evseev <evseev@altlinux.ru> 2.36-alt1
- updated to new version 2.36

* Thu Jan  4 2007 Ilya Evseev <evseev@altlinux.ru> 2.35-alt2
- adopt build for modern Sisyphus without kernel-std-up

* Sun Oct 29 2006 Ilya Evseev <evseev@altlinux.ru> 2.35-alt1
- updated to new version 2.35

* Tue Oct 17 2006 Ilya Evseev <evseev@altlinux.ru> 2.34-alt1
- updated to new version 2.34

* Tue Aug  8 2006 Ilya Evseev <evseev@altlinux.ru> 2.33-alt1
- updated to new version 2.33

* Tue Jul 25 2006 Ilya Evseev <evseev@altlinux.ru> 2.32-alt1
- updated to new version 2.32

* Fri May 12 2006 Ilya Evseev <evseev@altlinux.ru> 2.31-alt1
- updated to new version 2.31

* Thu Apr 20 2006 Ilya Evseev <evseev@altlinux.ru> 2.28-alt2
- specfile bugfixes: added dependency from kernel headers

* Tue Apr 18 2006 Ilya Evseev <evseev@altlinux.ru> 2.28-alt1
- updated to new version 2.28

* Fri Mar 17 2006 Ilya Evseev <evseev@altlinux.ru> 2.27-alt1
- updated to new version 2.27

* Sun Jan 22 2006 Ilya Evseev <evseev@altlinux.ru> 2.26-alt1
- updated to new version 2.26

* Sun Jan 15 2006 Ilya Evseev <evseev@altlinux.ru> 2.25-alt1
- updated to new version 2.25

* Tue Nov 29 2005 Ilya Evseev <evseev@altlinux.ru> 2.24-alt1
- update to new version 2.24
- new option 'localise-query' is now enabled by default
- some stuff from contrib/ is added to docs/.

* Tue Aug 30 2005 Ilya Evseev <evseev@altlinux.ru> 2.23-alt1
- update to new version 2.23

* Mon Jul 11 2005 Ilya Evseev <evseev@altlinux.ru> 2.22-alt2
- bugfix #7223: use '/sbin/ip route' instead 'sbin/route' in service script
- service script bugfix: m4 previously intercepts 'shift' as keyword

* Sun Apr  3 2005 Ilya Evseev <evseev@altlinux.ru> 2.22-alt1
- Updated to version 2.22, patch #1 is no more needed

* Fri Mar 25 2005 Ilya Evseev <evseev@altlinux.ru> 2.21-alt1
- Updated to version 2.21
- Added includes patch (P1)

* Tue Jan 25 2005 Ilya Evseev <evseev@altlinux.ru> 2.20-alt1
- 2.20
- URL is changed back from mantainer site to author site

* Sat Dec 18 2004 Ilya Evseev <evseev@altlinux.ru> 2.19-alt1
- version 2.19
- IMPORTANT bugfixes in service script

* Thu Nov 25 2004 Ilya Evseev <evseev@altlinux.ru> 2.18-alt1
- version 2.18

* Wed Oct 27 2004 Ilya Evseev <evseev@altlinux.ru> 2.16-alt1
- version 2.16

* Wed Sep 22 2004 Ilya Evseev <evseev@altlinux.ru> 2.15-alt1
- version 2.15

* Sun Sep 12 2004 Ilya Evseev <evseev@altlinux.ru> 2.14-alt1
- version 2.14

* Tue Sep  7 2004 Ilya Evseev <evseev@altlinux.ru> 2.13-alt4
- service script bugfixes:
   + domain name detection: added 'hostname --domain'
   + options are previously not passed to daemon
- sysconfig: added listening on 127.0.0.1 only for better security
- dnsmasq.conf: domain-needed and expand-hosts are enabled by default

* Sat Aug 28 2004 Ilya Evseev <evseev@altlinux.ru> 2.13-alt3
- more once attempt to fit hasher restrictions:
   + detection rule is changed again
   + removed 'BuildPreReq: initscripts'

* Fri Aug 27 2004 Ilya Evseev <evseev@altlinux.ru> 2.13-alt2
- added 'BuildPreReq: initscripts' for correct platform detection
  in build environment like hasher/sisyphus_check; changed detection rule.

* Sun Aug 22 2004 Ilya Evseev <evseev@altlinux.ru> 2.13-alt1
- new release
- also update configuration file
- service script is generated separately
  for ALTLinux 2.2 (classic style) and 2.4beta (modern style)
- removed 'Requires: initscripts' for preventing problems with sisyphus_check

* Wed Aug  4 2004 Ilya Evseev <evseev@altlinux.ru> 2.10-alt2
- added 'Requires: initscripts' for preventing problems with automated building

* Tue Jul 29 2004 Ilya Evseev <evseev@altlinux.ru> 2.10-alt1
- initial build

## EOF ##
