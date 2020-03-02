Name: vpnc
Version: 0.5.3
Release: alt7

Summary: Client for cisco vpn concentrator
Group: Networking/Remote access
License: GPL

Url: http://www.unix-ag.uni-kl.de/~massar/vpnc/

Source: %name-%version.tar
Patch: %name-%version-%release.patch
Patch2: 0001-vpnc-skip-parsing-responder-lifetime-payload.patch

Packager: Ilya Mashkin <oddity@altlinux.org>

BuildRequires: libgcrypt-devel libgnutls-devel perl-autodie
Requires: iproute2 vpnc-script

%add_findreq_skiplist %_sysconfdir/vpnc/vpnc-script

%description
vpnc is supposed to work with:

* Cisco VPN concentrator 3000 Series
* Cisco IOS routers
* Cisco PIX / ASA Zecurity Appliances
* Juniper / Junos / SRX / Netscreen

Supported Authentications: Pre-Shared-Key + XAUTH, Pre-Shared-Key
Supported IKE DH-Groups: dh1 dh2 dh5
Supported Hash Algo (IKE/IPSEC): md5 sha1
Supported Encryptions (IKE/IPSEC): (null) (1des) 3des aes128 aes192 aes256
Perfect Forward Secrecy: nopfs dh1 dh2 dh5

%package script
Summary: Routing setup script for vpnc and openconnect
Group: Networking/Remote access
BuildArch: noarch

%description script
This script sets up routing for VPN connectivity, when invoked by vpnc
or openconnect.

%prep
%setup -q
%patch -p1
%patch2 -p1

%build
CFLAGS="$RPM_OPT_FLAGS -fPIE" LDFLAGS="$RPM_OPT_FLAGS -pie" %make PREFIX=%_prefix

%install
%makeinstall_std PREFIX=%_prefix

mkdir -p %buildroot%_tmpfilesdir
install -m 0644 vpnc-tmpfiles.conf %buildroot%_tmpfilesdir/%name.conf

mkdir -p %buildroot%_runtimedir/%name
touch %buildroot%_runtimedir/%name/defaultroute \
      %buildroot%_runtimedir/%name/resolv.conf-backup

%files
%doc README TODO COPYING juniper.txt nortel.txt
%config(noreplace) %_sysconfdir/%name/default.conf
%_bindir/*
%_sbindir/*
%_man1dir/*
%_man8dir/*
%_tmpfilesdir/%name.conf
%dir %_runtimedir/%name
%ghost %verify(not md5 size mtime) %_runtimedir/%name/defaultroute
%ghost %verify(not md5 size mtime) %_runtimedir/%name/resolv.conf-backup

%files script
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/vpnc-script

%changelog
* Wed Feb 26 2020 Lenar Shakirov <snejok@altlinux.org> 0.5.3-alt7
- 0001-vpnc-skip-parsing-responder-lifetime-payload.patch

* Thu Apr 07 2016 Alexey Shabalin <shaba@altlinux.ru> 0.5.3-alt6
- rebuild with new gnutls
- fixed Vendor option (ALT#30117)

* Sat Oct 10 2015 Sergey V Turchin <zerg@altlinux.org> 0.5.3-alt5.1
- NMU: rebuild with new libgcrypt (ALT#31332)

* Wed Jun 18 2014 Alexey Shabalin <shaba@altlinux.ru> 0.5.3-alt5
- svn snapshot r550 (fixed ALT#26600, ALT#29351, ALT#26761, ALT#26726)
- add JunOS support from https://github.com/ndpgroup/vpnc (ALT#30117)

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.5.3-alt4.qa1
- NMU: rebuilt for debuginfo.

* Sun Nov 21 2010 Alexey Shabalin <shaba@altlinux.ru> 0.5.3-alt4
- update buildreq
- add PIE to CFLAGS, pie to LDFLAGS (patch5)

* Sun Jan 17 2010 Alexey Shabalin <shaba@altlinux.ru> 0.5.3-alt3
- package /var/run/vpnc as ghost
- split vpnc-script out into separate package (for openconnect)
- update vpnc-script to support IPv6 properly from git://git.infradead.org/users/dwmw2/vpnc-scripts.git

* Thu Mar 05 2009 Mikhail Efremov <sem@altlinux.org> 0.5.3-alt2
- added add_findreq_skiplist vpnc-script
	(to avoid resolvconf require)

* Sun Dec 28 2008 Ilya Mashkin <oddity@altlinux.org> 0.5.3-alt1
- 0.5.3

* Thu Mar 15 2007 Igor Zubkov <icesik@altlinux.org> 0.4.0-alt1
- build for Sisyphus

