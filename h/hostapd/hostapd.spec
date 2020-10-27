Name: hostapd
Version: 2.9
Release: alt2

Summary: User space daemon for extended IEEE 802.11 management
License: BSD
Group: System/Kernel and hardware
Url: http://hostap.epitest.fi/

Source0: %name-%version-%release.tar
Source1: src-%version-%release.tar
Source2: hostapd.sysconfig
Source3: hostapd.service
Source4: hostapd.init

BuildRequires: libssl-devel libnl3-devel

Obsoletes: hostap-tools

%description
This is a user space daemon for access point and authentication servers.
It implements IEEE 802.11 access point management, IEEE 802.1X/WPA/WPA2/EAP
Authenticators, RADIUS client, EAP server, and RADIUS authentication server.

%prep
%setup -c -a1

%build
cp %name/defconfig %name/.config
CFLAGS='%optflags' \
make -C %name

%install
install -pD -m0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -pD -m0644 %SOURCE3 %buildroot%_unitdir/%name.service
install -pD -m0755 %SOURCE4 %buildroot%_initdir/%name

install -pD -m0755 %name/%name %buildroot%_sbindir/%name
install -p -m0755 %name/%{name}_cli %buildroot%_sbindir

install -pD -m0600 %name/hostapd.conf %buildroot%_sysconfdir/%name/%name.conf
install -pm0600 %name/hostapd.accept  %name/hostapd.deny %buildroot%_sysconfdir/%name
install -pm0644 -D %name/%name.8 %buildroot%_man8dir/%name.8
install -pm0644 -D %name/%{name}_cli.1 %buildroot%_man1dir/%{name}_cli.1

%post
%post_service %name

%preun
%preun_service %name

%files
%doc %name/ChangeLog %name/README %name/README-WPS %name/eap_testing.txt

%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.conf
%config(noreplace) %_sysconfdir/%name/%name.accept
%config(noreplace) %_sysconfdir/%name/%name.deny

%config(noreplace) %_sysconfdir/sysconfig/%name

%_unitdir/%name.service
%_initdir/%name

%_sbindir/hostapd
%_sbindir/hostapd_cli

%_man1dir/*
%_man8dir/*

%changelog
* Fri Oct 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.9-alt2
- AP: Silently ignore management frame from unexpected source address
  (Fixes: CVE-2019-16275) (Closes: 39131)

* Mon Aug 19 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.9-alt1
- 2.9 released

* Tue Dec 18 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.7-alt1
- 2.7 released

* Fri Aug 31 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6-alt3
- rebuilt with recent openssl

* Mon Oct 16 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6-alt2
- multiple vulnerabilities (so-called KRACK attack) fixed:
  + CVE-2017-13077
  + CVE-2017-13078
  + CVE-2017-13079
  + CVE-2017-13080
  + CVE-2017-13081
  + CVE-2017-13082
  + CVE-2017-13086
  + CVE-2017-13087
  + CVE-2017-13088

* Fri Dec 23 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6-alt1
- 2.6 released

* Thu Sep 01 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5-alt1
- 2.5 released

* Thu May 07 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4-alt2
- updated with upstream fixes for EAP-pwd missing payload length validation

* Tue Apr 14 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4-alt1
- 2.4 released

* Sat Oct 11 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3-alt1
- 2.3 released

* Mon Jun 09 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt1
- 2.2 released

* Wed Feb 05 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt1
- 2.1 released

* Thu Jan 31 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0-alt1
- 2.0 released

* Sat Oct 02 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.3-alt2
- rebuilt with recent libcrypto

* Sun Sep 12 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.3-alt1
- 0.7.3 released

* Tue Apr 20 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.2-alt1
- 0.7.2 released

* Wed Dec  9 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.0-alt1
- 0.7.0 release

* Fri Mar 27 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.9-alt1
- 0.6.9

* Mon Dec 22 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.6-alt1
- 0.6.6

* Tue Nov 18 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Sat Mar 22 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Fri Nov 16 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.9-alt2.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Sep 02 2006 Alexei Takaseev <taf@altlinux.ru> 0.4.9-alt2
- rebuild with madwifi 0.9.2
- move dump-file /tmp -> /root/tmp

* Wed May 17 2006 Alexei Takaseev <taf@altlinux.ru> 0.4.9-alt1
- 0.4.9

* Tue Apr 11 2006 Alexei Takaseev <taf@altlinux.ru> 0.4.8-alt2
- rebuild with new madwifi-ng (20060411)

* Sun Feb 12 2006 Alexei Takaseev <taf@altlinux.ru> 0.4.8-alt1
- 0.4.8

* Mon Feb 06 2006 Alexei Takaseev <taf@altlinux.ru> 0.4.7-alt2
- rebuild with new madwifi-ng (0.9.4.5)

* Sun Dec 11 2005 Alexei Takaseev <taf@altlinux.ru> 0.4.7-alt1
- 0.4.7

* Thu Jun 23 2005 Alexei Takaseev <taf@altlinux.ru> 0.3.9-alt2
- rebuild with new madwifi (0.9.14.9)

* Tue Jun 14 2005 Alexei Takaseev <taf@altlinux.ru> 0.3.9-alt1
- 0.3.9

* Tue Mar 15 2005 Alexei Takaseev <taf@altlinux.ru> 0.3.7-alt1
- 0.3.7
- Add support wired, madwifi and prism54 drivers

* Tue Jan 04 2005 Alexei Takaseev <taf@altlinux.ru> 0.2.6-alt1
- 0.2.6

* Thu Oct 07 2004 Alexei Takaseev <taf@altlinux.ru> 0.2.5-alt1
- 0.2.5

* Sun Jul 18 2004 Alexei Takaseev <taf@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Mon Feb 09 2004 Alexei Takaseev <taf@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Mon Nov 03 2003 Alexei Takaseev <taf@altlinux.ru> 0.1.0-alt1
- first build for ALT Sisyphus
