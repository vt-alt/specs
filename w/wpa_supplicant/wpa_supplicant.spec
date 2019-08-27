Name: wpa_supplicant
Version: 2.9
Release: alt1

Summary: wpa_supplicant is an implementation of the WPA Supplicant component
License: BSD
Group: Security/Networking
Url: http://hostap.epitest.fi/

Source0: %name-%version-%release.tar
Source1: src-%version-%release.tar

Requires: dbus

BuildRequires: libdbus-devel libnl-devel >= 3.2.21
BuildRequires: docbook-utils libncurses-devel libpcsclite-devel libreadline-devel libssl-devel
BuildRequires: gcc-c++ inkscape libxml2-devel qt5-base-devel qt5-tools

%description
wpa_supplicant is an implementation of the WPA Supplicant component,
i.e., the part that runs in the client stations. It implements WPA key
negotiation with a WPA Authenticator and EAP authentication with
Authentication Server. In addition, it controls the roaming and IEEE
802.11 authentication/association of the wlan driver.

wpa_supplicant is designed to be a "daemon" program that runs in the
background and acts as the backend component controlling the wireless
connection. wpa_supplicant supports separate frontend programs and an
example text-based frontend, wpa_cli, is included with wpa_supplicant.

%package -n wpa_gui
Summary: wpa_supplicant GUI
Group: Security/Networking
Requires: wpa_supplicant = %version-%release

%description -n wpa_gui
wpa_supplicant is an implementation of the WPA Supplicant component,
i.e., the part that runs in the client stations. It implements WPA key
negotiation with a WPA Authenticator and EAP authentication with
Authentication Server. In addition, it controls the roaming and IEEE
802.11 authentication/association of the wlan driver.

This package provides GUI to wpa_supplicant

%prep
%setup -c -a1
cp %name/defconfig %name/.config

%build
make -C %name
make -C %name/doc/docbook man

%install
install -pm0644 -D %name/%name.conf %buildroot%_sysconfdir/wpa_supplicant.conf
install -pm0755 -D %name/wpa_supplicant %buildroot%_sbindir/wpa_supplicant
install -pm0755 %name/wpa_cli %buildroot%_sbindir
install -pm0755 -D %name/wpa_gui-qt4/wpa_gui %buildroot%_bindir/wpa_gui

mkdir -p %buildroot%systemd_unitdir
mkdir -p %buildroot%_sysconfdir/%name
install -pm0644 %name/systemd/*.service %buildroot%systemd_unitdir

install -pm0755 -D %name/wpa_passphrase %buildroot%_bindir/wpa_passphrase
install -pm0644 -D %name/dbus/dbus-wpa_supplicant.conf %buildroot%_sysconfdir/dbus-1/system.d/dbus-%name.conf

mkdir -p %buildroot%_datadir/dbus-1/system-services
install -pm0644 -D %name/dbus/*.service %buildroot%_datadir/dbus-1/system-services/

install -pm0644 -D %name/doc/docbook/%name.conf.5 %buildroot%_man5dir/%name.conf.5
install -pm0644 -D %name/doc/docbook/%name.8 %buildroot%_man8dir/%name.8
install -pm0644 %name/doc/docbook/wpa_{cli,passphrase,background,priv}.8 %buildroot%_man8dir

mkdir -p %buildroot%_iconsdir
install -pm0644 -D %name/wpa_gui-qt4/wpa_gui.desktop %buildroot%_desktopdir/wpa_gui.desktop
tar c -C %name/wpa_gui-qt4/icons hicolor |tar x -C %buildroot%_iconsdir

%files
%doc %name/README %name/README-HS20 %name/README-P2P %name/README-WPS
%doc %name/ChangeLog %name/examples

%dir %_sysconfdir/%name
%config(noreplace) %attr(0600,root,root) %_sysconfdir/wpa_supplicant.conf
%config %_sysconfdir/dbus-1/system.d/dbus-%name.conf

%systemd_unitdir/wpa_supplicant.service
%systemd_unitdir/wpa_supplicant@.service
%systemd_unitdir/wpa_supplicant-nl80211@.service
%systemd_unitdir/wpa_supplicant-wired@.service

%_datadir/dbus-1/system-services/fi.w1.wpa_supplicant1.service

%_sbindir/wpa_supplicant
%_sbindir/wpa_cli
%_bindir/wpa_passphrase

%_man5dir/wpa_supplicant.conf.*

%_man8dir/wpa_background.*
%_man8dir/wpa_cli.*
%_man8dir/wpa_supplicant.*
%_man8dir/wpa_passphrase.*

%files -n wpa_gui
%_bindir/wpa_gui
%_desktopdir/wpa_gui.desktop
%_iconsdir/hicolor/*/*/*.png

%changelog
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
- 2.6-alt1 released

* Thu Sep 01 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5-alt1
- 2.5 released

* Thu May 07 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4-alt3
- updated with upstream fixes for EAP-pwd missing payload length validation

* Fri Apr 24 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4-alt2
- CVE-2015-1863

* Tue Apr 14 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4-alt1
- 2.4 released

* Sat Oct 11 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3-alt1
- 2.3 released

* Mon Jun 09 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt1
- 2.2 released

* Wed Feb 05 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt1
- 2.1 released

* Fri Feb 22 2013 Terechkov Evgenii <evg@altlinux.org> 2.0-alt2
- Fix build with libnl3

* Thu Jan 31 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0-alt1
- 2.0 released

* Tue Oct 02 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.3-alt4
- fixed build witn gcc-4.7

* Sat Feb 26 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.3-alt3
- updated for use with nm-0.9

* Sat Oct 02 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.3-alt2
- WPS support turned on

* Sun Sep 12 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.3-alt1
- 0.7.3 released

* Thu Apr 22 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.2-alt3
- fix interoperation with nm (#23376, by sem@)

* Thu Apr 22 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.2-alt2
- fix path to wpa_supplicant in dbus service file

* Tue Apr 20 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.2-alt1
- 0.7.2 released

* Mon Dec 14 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.0-alt2
- restore old DBUS interface support

* Fri Dec  4 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.0-alt1
- 0.7.0 release

* Thu Mar 26 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.9-alt1
- 0.6.9 release

* Wed Feb 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.7-alt1
- 0.6.7 release

* Mon Dec 22 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.6-alt1
- 0.6.6 release

* Fri Nov 21 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.5-alt1
- 0.6.5 release

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.5.10-alt3.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Tue May 06 2008 Anton Farygin <rider@altlinux.ru> 0.5.10-alt3
- enabled dbus support

* Thu Apr 24 2008 Mikhail Efremov <sem@altlinux.org> 0.5.10-alt2.1
- rebuild with D-Bus support

* Tue Apr 15 2008 Anton Farygin <rider@altlinux.ru> 0.5.10-alt2
- added kernel-source-madwifi build requires

* Mon Apr 14 2008 Anton Farygin <rider@altlinux.ru> 0.5.10-alt1
- new version

* Sat Mar 08 2008 L.A. Kostis <lakostis@altlinux.ru> 0.5.9-alt2
- rebuild with madwifi-0.9.4.

* Wed Jan 16 2008 Stanislav Ievlev <inger@altlinux.org> 0.5.9-alt1
- 0.5.9
- minimize deps on kernel-source-madwifi version

* Wed Jun 06 2007 Stanislav Ievlev <inger@altlinux.org> 0.5.8-alt1
- 0.5.8

* Wed May 23 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 0.5.7-alt4
- rebuild with madwifi 0.9.3.1.

* Fri May 18 2007 Stanislav Ievlev <inger@altlinux.org> 0.5.7-alt3
- fix buildreq

* Fri May 11 2007 L.A. Kostis <lakostis@altlinux.ru> 0.5.7-alt2
- rebuild with madwifi 0.9.3.

* Thu May 10 2007 Stanislav Ievlev <inger@altlinux.org> 0.5.7-alt1
- 0.5.7

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.9-alt3.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Sep 02 2006 Alexei Takaseev <taf@altlinux.ru> 0.4.9-alt3
- rebuild with madwifi 0.9.2

* Sat Jul 22 2006 Alexei Takaseev <taf@altlinux.ru> 0.4.9-alt2
- rebuild with new libpcsclite

* Thu May 18 2006 Alexei Takaseev <taf@altlinux.ru> 0.4.9-alt1
- 0.4.9
- fix #9553

* Tue Apr 11 2006 Alexei Takaseev <taf@altlinux.ru> 0.4.8-alt2
- Rebuild with new madwifi-ng 20060411

* Sun Feb 12 2006 Alexei Takaseev <taf@altlinux.ru> 0.4.8-alt1
- 0.4.8
- Add debug logging

* Wed Feb 01 2006 Alexei Takaseev <taf@altlinux.ru> 0.4.7-alt2
- Rebuild with madwifi-ng 20060201

* Sun Dec 11 2005 Alexei Takaseev <taf@altlinux.ru> 0.4.7-alt1
- 0.4.7
- Remove unneeded wpa_supplicant-driver_ipw.c.patch

* Mon Sep 12 2005 Alexei Takaseev <taf@altlinux.ru> 0.3.9-alt3
- add madwifi driver support
- fix pid-file creation

* Sat Jul 02 2005 Alexei Takaseev <taf@altlinux.ru> 0.3.9-alt2
- fix ipw2100/ipw2200 drivers

* Tue Jun 14 2005 Alexei Takaseev <taf@altlinux.ru> 0.3.9-alt1
- 0.3.9

* Sun May 15 2005 Alexei Takaseev <taf@altlinux.ru> 0.3.8-alt3
- change RPM group to "Security/Networking"

* Fri Apr 22 2005 Alexei Takaseev <taf@altlinux.ru> 0.3.8-alt2
- Add support:
	* CTRL_IFACE
	* XSUPPLICANT_IFACE
	* PKCS12
	* DRIVER_IPW
	* EAP_AKA
	* EAP_PSK

* Wed Mar 16 2005 Alexei Takaseev <taf@altlinux.ru> 0.3.8-alt1
- 0.3.8

* Wed Feb 16 2005 Alexei Takaseev <taf@altlinux.ru> 0.2.7-alt1
- 0.2.7

* Tue Jan 04 2005 Alexei Takaseev <taf@altlinux.ru> 0.2.6-alt1
- 0.2.6

* Thu Oct 07 2004 Alexei Takaseev <taf@altlinux.ru> 0.2.5-alt1
- first build for ALT Sisyphus
