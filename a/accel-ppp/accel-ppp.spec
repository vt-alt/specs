Name: accel-ppp
Version: 1.12.0
Release: alt3
Summary: High performance PPTP/L2TP/PPPoE server
Group: System/Servers

Packager: Alexei Takaseev <taf@altlinux.ru>

License: GPLv2
Url: http://sourceforge.net/projects/accel-ppp/
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
Requires: snmp-mibs-std
AutoProv: yes

BuildRequires: cmake libnet-snmp-devel libpcre-devel libnl-devel libssl-devel liblua5.3-devel glibc-kernheaders
BuildPreReq: rpm-build-kernel

%description
The ACCEL-PPP is completly new implementation of PPTP/PPPoE/L2TP
which was written from scratch. Userspace daemon has its own PPP
implementation, so it does not uses pppd and one process (multi-threaded)
manages all connections. ACCEL-PPP uses only kernel-mode implementations
of pptp/l2tp/pppoe.

Features:
- IPoE server
- PPTP server
- PPPoE server
- L2TPv2 server
- Radius CoA/DM (PoD)
- Built-in shaper (htb)
- Command line interface (telnet)
- SNMP
- IPv6 (including builtin Neighbor Discovery and DHCPv6)

%package -n kernel-source-%name
Summary: Kernel module for accel-ppp IPoE
License: GPLv2
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%name
Provide accel-ppp ipoe kernel module


%prep
%setup
%patch0 -p1
tar -cjf ../%name-%version.tar.bz2 ../%name-%version

%build
%cmake \
      -DCMAKE_SKIP_RPATH:BOOL=FALSE \
      -DCMAKE_SKIP_INSTALL_RPATH:BOOL=FALSE \
      -DBUILD_DRIVER=FALSE \
      -DCMAKE_INSTALL_PREFIX=%prefix \
      -DRADIUS=TRUE \
      -DNETSNMP=TRUE \
      -DLOG_PGSQL=FALSE \
      -DLUA=5.3 \
      -DBUILD_INSTALL_PREFIX=%buildroot \
      -DCMAKE_BUILD_TYPE=Debug \
      -DMEMDEBUG=TRUE

%cmake_build

%install
make install/fast DESTDIR=%buildroot -C BUILD

install -Dpm 644 alt-linux/%name.tmpfiles %buildroot%_tmpfilesdir/%name.conf
install -d %buildroot%_sysconfdir/{rc.d/init.d,sysconfig,logrotate.d}
install -pDm0644 alt-linux/%name.sysconfig	%buildroot%_sysconfdir/sysconfig/%name
install -pDm0755 alt-linux/%name.init		%buildroot%_initdir/%name
install -pDm0644 alt-linux/%name.logrotate	%buildroot%_sysconfdir/logrotate.d/%name
mkdir -p %buildroot%_runtimedir/accel-ppp

mkdir -p %kernel_srcdir
install -pDm0644 ../%name-%version.tar.bz2 %kernel_srcdir/%name-%version.tar.bz2

%post
%post_service %name

%preun
%preun_service %name

%files
%doc COPYING README accel-pppd/extra/net-snmp/ACCEL-PPP-MIB.txt alt-linux/IPoE_ru.txt alt-linux/IPoE_dhcp_lua_ru.txt
%config(noreplace) %_initdir/*
%config(noreplace) %_sysconfdir/sysconfig/*
%config %_sysconfdir/logrotate.d/*
%config(noreplace) %_tmpfilesdir/*
%_sysconfdir/accel-ppp.conf.dist
%_bindir/accel-cmd
%_sbindir/accel-pppd
%_libdir/%name
%_datadir/accel-ppp/
%_mandir/man1/accel-cmd*
%_mandir/man5/accel-ppp.conf.5*
%_runtimedir/accel-ppp/
%_logdir/accel-ppp/

%files -n kernel-source-%name
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Mon Jun 22 2020 Alexei Takaseev <taf@altlinux.org> 1.12.0-alt3
- Set default metric to 128 for delegate v6 prefixes

* Sun Jan 26 2020 Alexei Takaseev <taf@altlinux.org> 1.12.0-alt2
- ipoe,vlan_mon: add support for kernels 5.2+

* Tue Aug 06 2019 Alexei Takaseev <taf@altlinux.org> 1.12.0-alt1
- 1.12.0

* Tue Apr 23 2019 Alexei Takaseev <taf@altlinux.org> 1.11.2-alt12
- Rebuild with lua 5.3

* Thu Sep 06 2018 Alexei Takaseev <taf@altlinux.org> 1.11.2-alt11
- update upstream to git:20da79b5ee071e4eda75645d1f812f4137e81062
    * triton: fixed improper locking
    * ipoe: lua: introduced hwaddr field to session object
    * ipoe: use lua function to generate username for UP sessions too

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.11.2-alt10.1
- NMU: Rebuild with new openssl 1.1.0.

* Fri May 04 2018 Alexei Takaseev <taf@altlinux.org> 1.11.2-alt10
    * pppoe: fixed invalid behaviour after changing pado-delay

* Wed Apr 04 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.11.2-alt9
- build fixed for kernels 4.15+ (upstream cherry-pick)

* Sun Mar 04 2018 Alexei Takaseev <taf@altlinux.org> 1.11.2-alt8
- update upstream to git:f5313ce5dc5192f4539eceacd621bfe193a0eb97
    * pppoe: fixed PADO delaying function
    * ppp: fix use-after-free in ppp_auth_failed()
    * radius: fixed invalid behaviour when route to radius server is not existing

* Tue Feb 06 2018 Alexei Takaseev <taf@altlinux.org> 1.11.2-alt7
- Fix build with glibc-kernheaders >= 4.15

* Mon Jan 29 2018 Alexei Takaseev <taf@altlinux.org> 1.11.2-alt6
- update upstream to git:435c18ba35f9515727e63b4de92912d7567b5534
    * ppp: fixed bug in ppp_terminate

* Tue Dec 26 2017 Alexei Takaseev <taf@altlinux.org> 1.11.2-alt5
- update upstream to git:cb9cf0a9c1e88e5fea156b5048be439d9763dc70
    * shaper: define UINT16_MAX if not set

* Wed Oct 11 2017 Alexei Takaseev <taf@altlinux.org> 1.11.2-alt4
- update upstream to git:dc9638c595cffb142d0ae302a0e3210c67e83087
    * ppp_lcp: fixed missing braces (possible bug)
    * ipoe: more verbose netlink errors
    * radius: split request queue to 2 subqueues

* Thu Sep 28 2017 Alexei Takaseev <taf@altlinux.org> 1.11.2-alt3
- update upstream to git:08e048a76d1d566bf280e3c09d4d839ff40f7af7
    * libnetlink: added function iplink_set_mtu
    * ipoe: introduced interface option mtu=N
    * cli: introduced ip6 and ip6-dp fields in "show sessions" command

* Fri Aug 11 2017 Alexei Takaseev <taf@altlinux.org> 1.11.2-alt2
- Fix build with kernels >= 4.10

* Thu Aug 10 2017 Alexei Takaseev <taf@altlinux.org> 1.11.2-alt1
- 1.11.2

* Thu Feb 16 2017 Alexei Takaseev <taf@altlinux.org> 1.11.1-alt2.git20161210
- update upstream to git:444385f2be198318d6092c049bbebf5cc981eeca
    * ipoe: fixed typo (incorrect assignment)
    * ipoe: add support for peer-to-peer client interfaces
    * ipoe: assign point-to-point addresses to non-shared physical interface
            (prevents route cleaning by interface renaming)
    * fixed compilation
    * shaper: fixed conditions to install limiter (may install only up or
            only down limiter)

* Mon Jan 16 2017 Alexei Takaseev <taf@altlinux.org> 1.11.1-alt2
- Build with lua 5.1

* Tue Nov 29 2016 Alexei Takaseev <taf@altlinux.org> 1.11.1-alt1
- 1.11.1

* Wed Jul 13 2016 Alexei Takaseev <taf@altlinux.org> 1.11.0-alt1
- 1.11.0

* Thu May 12 2016 Alexei Takaseev <taf@altlinux.org> 1.10.2-alt1
- 1.10.2

* Wed Jan 06 2016 Alexei Takaseev <taf@altlinux.org> 1.10.0-alt3
- Update packet.c
    radius server error packet may be coredump.

* Sat Dec 26 2015 Alexei Takaseev <taf@altlinux.org> 1.10.0-alt2
- ppp_auth: fixed broken noauth mode
- pppd_compat: change mode of radattr files to 0644

* Tue Dec 22 2015 Alexei Takaseev <taf@altlinux.org> 1.10.0-alt1
- 1.10.0

* Thu Sep 03 2015 Alexei Takaseev <taf@altlinux.org> 1.9.0-alt4
- update upstream to git:30cff41b56be0d4c3e407e8aa4de5b289eef2ab0

* Thu Jul 09 2015 Alexei Takaseev <taf@altlinux.org> 1.9.0-alt3
- pppoe: check for tag length in print_packet function (fixes sigsegv)
- shaper: fixed parsing ecn/noecn for fq_codel
- ipoe: fixed authentication with chap-secrets

* Tue Dec 30 2014 Alexei Takaseev <taf@altlinux.org> 1.9.0-alt2
- ipoe: fixed incorrect timer deletion
- ipoe: fixed mask calculation from ipaddr radius attribute

* Wed Dec 10 2014 Alexei Takaseev <taf@altlinux.org> 1.9.0-alt1
- 1.9.0

* Tue Dec 09 2014 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt6
- ipoe: support for kernels 3.16-3.18

* Wed Nov 26 2014 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt5
- update upstream to git:e09279c7491a8bd16a25b123e03ddd0cd77b566d

* Mon Oct 13 2014 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt4
- update upstream to git:8d3351d4cdfcaf45aa2c918b0f8920798be4dc04

* Mon Sep 01 2014 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt3
- update upstream to git:ec9968885ed2f273c4d2c18297986c463fb9cf9b

* Tue Aug 05 2014 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt2
- update upstream to git:2cdd67782c6d11af141992dba2943e03134593b5

* Fri May 09 2014 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt1
- 1.8.0

* Tue Apr 22 2014 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt0.beta.2
- update upstream to git:b1a4c68fa51d69283deb9e22c370349ee36d3cca

* Mon Apr 14 2014 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt0.beta.1
- Build with IPoE

* Mon Apr 14 2014 Alexei Takaseev <taf@altlinux.org> 1.7.3-alt8
- update upstream to git:0d5e6d03c74f3ab6b83d2333480b2441df9a6522
    * ppp: don't unconditionaly load pppoe/pptp/l2tp modules,
      fixes false start warning if they're running already
    * pppoe: check for tag format validity in PADR messages
    * increase size of buffer for netlink messages

* Wed Nov 20 2013 Alexei Takaseev <taf@altlinux.org> 1.7.3-alt7
- Fix rpath

* Sat Nov 09 2013 Alexei Takaseev <taf@altlinux.org> 1.7.3-alt6
- update upstream to git:da7bb06e70252ba11751f4e3a9f8b97144500d9e
    * fixed sigsegv in 'shaper restore all'
    * fixed socket leak
    * fixed many race conditions

* Sat Aug 10 2013 Alexei Takaseev <taf@altlinux.org> 1.7.3-alt5
- auth_chap: fixed incorrect check for received buffer size
- triton: Fix race upon termination

* Thu Jul 04 2013 Alexei Takaseev <taf@altlinux.org> 1.7.3-alt4
- update to git:b77ca8764985ebae18d769cdf115e2242bbac98d

* Wed Jun 05 2013 Alexei Takaseev <taf@altlinux.org> 1.7.3-alt3
- Move tmpfiles.d from etc to %%_tmpfilesdir/

* Sun Jun 02 2013 Alexei Takaseev <taf@altlinux.org> 1.7.3-alt2
- update to git:3cc23d37c3c93ca7240f52fe5121513bcd6c3db8

* Tue Dec 11 2012 Alexei Takaseev <taf@altlinux.org> 1.7.3-alt1
- 1.7.3

* Sat Nov 03 2012 Alexei Takaseev <taf@altlinux.org> 1.7.2-alt4
- ppp: force to send dns

* Thu Oct 18 2012 Alexei Takaseev <taf@altlinux.org> 1.7.2-alt3
- remove unresolved=relaxed

* Thu Oct 04 2012 Alexei Takaseev <taf@altlinux.org> 1.7.2-alt2
- Add log messages for terminate sessions

* Thu Sep 06 2012 Alexei Takaseev <taf@altlinux.org> 1.7.2-alt1
- 1.7.2

* Tue Aug 28 2012 Alexei Takaseev <taf@altlinux.org> 1.7.1-alt2
- fix build with glibc-2.16

* Mon Jul 30 2012 Alexei Takaseev <taf@altlinux.org> 1.7.1-alt1
- 1.7.1

* Sat Jun 30 2012 Alexei Takaseev <taf@altlinux.org> 1.7.0-alt2
- Build git 20120630

* Mon Jun 18 2012 Alexei Takaseev <taf@altlinux.org> 1.7.0-alt1
- 1.7.0

* Mon Jun 11 2012 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt7
- update upstream to git:fa315a7a7584f6f4954888c010e3cc84c2b33330

* Sun May 27 2012 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt6
- Fix underlinked libraries for libnet-snmp.so

* Fri May 18 2012 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt5
- update upstream to git:cf358fcdc57dd52d30ca490b1164d832cf11fe8b
- add config for systemd-tmpfiles

* Mon Apr 30 2012 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt4
- fix deadlock interface when restart service

* Sat Apr 21 2012 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt3
- quoted username in log messages
- Add username to disconnect log messages

* Wed Apr 04 2012 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt2
- add MIB file

* Sun Mar 25 2012 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt1
- Initial RPM release
