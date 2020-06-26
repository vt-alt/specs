%define _altdata_dir %_datadir/alterator

Name: alterator-net-openvpn
Version: 0.8.15
Release: alt1
License: %gpl2plus
Group: System/Configuration/Other
Summary: Alterator module for openvpn connections configuration
Packager: Mikhail Efremov <sem@altlinux.org>
Source: %name-%version.tar

Requires: alterator >= 5.2-alt1 alterator-sh-functions >= 0.6-alt5 libshell >= 0.0.1-alt4
Requires: alterator-net-functions >= 0.8-alt2
Requires: alterator-sslkey
Requires: cert-sh-functions
Requires: alterator-l10n >= 2.7-alt12
Requires: openvpn >= 2.1
Requires: etcnet
Requires: openresolv
Requires: alterator-openvpn-sh-functions

BuildPreReq: alterator >= 4.7-alt3

BuildRequires: rpm-build-licenses

BuildArch: noarch

%description
Alterator module for openvpn connections configuration

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*/
%_alterator_backend3dir/*

%changelog
* Thu Jun 18 2020 Slava Aseev <ptrnine@altlinux.org> 0.8.15-alt1
- Fix broken web interface in 0.8.14-alt1
- Fix import of CA certificate

* Tue Jun 09 2020 Slava Aseev <ptrnine@altlinux.org> 0.8.14-alt1
- Add ability to disable NCP

* Fri Feb 28 2020 Slava Aseev <ptrnine@altlinux.org> 0.8.13-alt1
- Add ability to select cipher, tls-cipher and digest

* Fri Aug 31 2018 Paul Wolneykien <manowar@altlinux.org> 0.8.12-alt1
- Fix: Allow to use either a hostname or an IP-address as the
  server address.

* Thu Aug 16 2018 Paul Wolneykien <manowar@altlinux.org> 0.8.11-alt1
- Use strict data types for "dev" and "dev_type" parameters.

* Tue Jan 20 2015 Mikhail Efremov <sem@altlinux.org> 0.8.10-alt1
- Add tmp-dir option to ovpnoptions.
- backend: Rename IFACEDIR to IFACESDIR.

* Fri Dec 21 2012 Mikhail Efremov <sem@altlinux.org> 0.8.9-alt1
- Added initial GOST support.
- Disable LZO by default.
- Use 'dev-type' instead of 'dev'.
- Use its own CA certificate for each connection (closes: #28203).
- Set resolve timeout to 15s.
- Use 'resolve' as well as 'dig' (closes: #27560).

* Mon Jan 17 2011 Mikhail Efremov <sem@altlinux.org> 0.8.7-alt1
- desktop file: add uk translation (by Roman Savochenko).

* Wed Dec 01 2010 Mikhail Efremov <sem@altlinux.org> 0.8.6-alt1
- QT UI: fix label.

* Mon Oct 25 2010 Mikhail Efremov <sem@altlinux.org> 0.8.5-alt1
- Validate CA certificate.
- add "Use a TCP connection" checkbox.

* Tue Apr 20 2010 Mikhail Efremov <sem@altlinux.org> 0.8.4-alt1
- check ssl certificates before start.

* Sat Jan 02 2010 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt1
- added 'script-security 2' option to openvpn config.

* Wed Oct 21 2009 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt1
- fix display empty connection list.

* Tue Sep 29 2009 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1
- disable UI if connections do not exist.

* Mon Sep 28 2009 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- don't use separate page for upload CA certificate.
- don't update keys list if it is not necessary.
- UI improved (closes: #21695).
- use wf 'none'.

* Thu Aug 20 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- move translations to alterator-l10n.
- Updated Russian translation.
- added button 'Keys managament'.

* Tue Jul 21 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1
- removed ssl keys and sign request generating.
- fixed 'status' label.

* Tue Jun 02 2009 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt1
- Updated Russian translation.
- disable 'Apply' button when connections list is empty.

* Mon Jun 01 2009 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1
- added QT certificates interface.
- relocate 'Delete' button.

* Wed May 27 2009 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1
- use ca-root.pem instead root.pem.

* Fri May 15 2009 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- remove leading spaces from config values.
- set ONBOOT=no by default.

* Thu May 14 2009 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1
- Updated Russian translation.
- write config even if key and certificate not specified.
- added 'LZO compression' checkbox.
- use ui-file instead ui-blob.
- moved certificates/key managment to separate page.

* Fri May 08 2009 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt2
- fix Requires

* Thu May 07 2009 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1
- use type hostname for server name.
- added 'Default route via VPN' checkbox.
- sort tun/tap devices in listbox.

* Tue May 05 2009 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1
- lookup keys in /etc/openvpn/keys too.
- removed iptables rules for tun/tap.
- remove csr when certificate uploaded.

* Tue May 05 2009 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- fixed device selecting in listbox when connection created/deleted.
- added 'Start at boot' checkbox.
- UI improved.

* Tue Apr 28 2009 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- fix ifup-post and ifdown-post scripts.

* Tue Apr 28 2009 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt2
- openresolv requires is added

* Mon Apr 27 2009 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- use ui-blob for .csr file.
- fix name in .desktop file

* Mon Apr 27 2009 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- use OpenVPN server's DNS

* Thu Apr 16 2009 Mikhail Efremov <sem@altlinux.org> 0.1.5-alt1
- Russian translation 

* Wed Apr 15 2009 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1
- UI improved.
- use radio buttons for device type removed 'reset' button.

* Tue Apr 14 2009 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1
- UI improved.
- rename 'OpenVPN client' -> 'OpenVPN connections'.
- use next_iface from alterator-net-functions.

* Fri Apr 03 2009 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- remove old ssl files before creating new ones.
- fix typo.

* Thu Apr 02 2009 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- use cert-sh-functions.
- fixed certificates upload

* Thu Apr 02 2009 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt2
- fix files section

* Wed Apr 01 2009 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- 0.1.0

* Tue Mar 17 2009 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1
- initial release

