#set capability dropping library.
#Currently supported values are "libcap" and "native".
%define capabilities libcap
%def_enable addrblock
%def_enable agent
%def_enable ccm
%def_enable cisco_quirks
%def_enable ctr
%def_enable curl
%def_enable dhcp
%def_enable eap_aka
%def_enable eap_gtc
%def_enable eap_identity
%def_enable eap_md5
%def_enable eap_mschapv2
%def_enable eap_radius
%def_enable eap_sim
%def_enable eap_sim-file
%def_enable eap_tls
%def_enable eap_tnc
%def_enable eap_ttls
%def_enable farp
%def_enable gcm
%def_enable ha
%def_enable kernel_klips
%def_enable kernel_netlink
%def_enable kernel_pfkey
%def_enable ldap
%def_enable medcli
%def_enable mediation
%def_enable nat_transport
%def_enable ntru
%def_enable openssl
%def_enable pkcs11
%def_enable self_test
%def_enable smartcard
%def_enable smp
%def_enable sql
%def_enable stroke
%def_enable swanctl
%def_disable dumm
%def_disable load_tests
%def_disable manager
%def_disable medsrv
%def_disable mysql
%def_disable nm
%def_disable sqlite
%def_disable static
%def_disable uci
%def_disable unit_tests
# this one requires that libhydra and libcharon be
# underlinked on purpose, contact mike@ for email
# explanation by Tobias Brunner (11 May 2010)
%def_disable integrity-test

%ifarch %ix86
%def_enable padlock
%else
%def_disable padlock
%endif

%define beta %nil

Name: strongswan
Version: 5.8.1
Release: alt1

Summary: strongSwan IPsec implementation
License: GPLv2+
Group: System/Servers

# git://git.strongswan.org/strongswan.git
Url: http://www.strongswan.org
Source0: %name-%version%beta.tar.gz
Source1: ipsec.init
Source2: ipsec.service
Source100: strongswan.watch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Mon Jul 02 2012
# optimized out: pkg-config
BuildRequires: flex gperf libcap-devel libcurl-devel libgmp-devel libldap-devel libpam-devel libssl-devel libxml2-devel

Provides: libstrongswan = %version-%release
Obsoletes: libstrongswan < 4.3

%define pkgdocdir %_docdir/%name-%version
%add_verify_elf_skiplist %_libdir/%name/ipsec/plugins/*

%description
strongSwan is a free implementation of IPsec & IKE for Linux. IPsec is the
Internet Protocol Security and uses strong cryptography to provide both
authentication and encryption services. These services allow you to build
secure tunnels through untrusted networks. Everything passing through the
untrusted net is encrypted by the ipsec gateway machine and decrypted by the
gateway at the other end of the tunnel. The resulting tunnel is a virtual
private network or VPN.

This package contains the service and userland tools for setting up strongSwan
on a freeswan enabled kernel.

%package testing
Summary: %name testing
Group: Documentation
Requires: %name = %version
BuildArch: noarch

%description testing
This package contains testing scripts and configuration snippets
of strongSwan documentation

%prep
%setup -n %name-%version%beta

%build
%autoreconf
%configure \
	--sysconfdir=%_sysconfdir/%name \
	--libexecdir=%_libdir/%name \
	%{subst_enable addrblock} \
	%{subst_enable agent} \
	%{subst_enable ccm} \
	%{subst_enable ctr} \
	%{subst_enable curl} \
	%{subst_enable dhcp} \
	%{subst_enable dumm} \
	%{subst_enable farp} \
	%{subst_enable gcm} \
	%{subst_enable ha} \
	%{subst_enable ldap} \
	%{subst_enable manager} \
	%{subst_enable medcli} \
	%{subst_enable mediation} \
	%{subst_enable medsrv} \
	%{subst_enable mysql} \
	%{subst_enable ntru} \
	%{subst_enable openssl} \
	%{subst_enable padlock} \
	%{subst_enable smartcard} \
	%{subst_enable smp} \
	%{subst_enable sql} \
	%{subst_enable sqlite} \
	%{subst_enable static} \
	%{subst_enable stroke} \
	%{subst_enable swanctl} \
	%{subst_enable uci} \
	%{subst_enable nm} \
	--with-capabilities=%capabilities \
	%{subst_enable pkcs11} \
	--with-default-pkcs11=%_libdir/pkcs11/opensc-pkcs11.so \
	%{?_enable_cisco_quirks: --enable-cisco-quirks} \
	%{?_enable_unit_tests: --enable-unit-tests} \
	%{?_enable_load_tests: --enable-load-tests} \
	%{?_enable_eap_radius: --enable-eap-radius} \
	%{?_enable_eap_identity: --enable-eap-identity} \
	%{?_enable_eap_mschapv2: --enable-eap-mschapv2} \
	%{?_enable_eap_tls: --enable-eap-tls} \
	%{?_enable_eap_ttls: --enable-eap-ttls} \
	%{?_enable_eap_tnc: --enable-eap-tnc} \
	%{?_enable_eap_sim: --enable-eap-sim} \
	%{?_enable_eap_sim_file: --enable-eap-sim-file} \
	%{?_enable_eap_md5: --enable-eap-md5} \
	%{?_enable_eap_gtc: --enable-eap-gtc} \
	%{?_enable_eap_aka: --enable-eap-aka} \
	%{?_enable_kernel_netlink: --enable-kernel-netlink} \
	%{?_enable_kernel_pfkey: --enable-kernel-pfkey} \
	%{?_enable_kernel_klips: --enable-kernel-klips} \
	%{?_enable_nat_transport: --enable-nat-transport} \
	%{?_enable_integrity_test: --enable-integrity-test} \
	%{?_enable_self_test: --enable-self-test}

#
%make_build

%install
%makeinstall_std
mkdir -p %buildroot{%pkgdocdir,%systemd_unitdir}

install -pDm755 %SOURCE1 %buildroot%_initdir/ipsec
install -pm644 %SOURCE2 %buildroot%systemd_unitdir/
install -pm644 ChangeLog NEWS README TODO %buildroot%pkgdocdir/
rm -f %buildroot%_libdir/lib%name.{a,so}
rm -f testing/do-tests* testing/Makefile.*
cp -a testing/ %buildroot%pkgdocdir/

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find $RPM_BUILD_ROOT \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

%files
%dir %pkgdocdir
%pkgdocdir/[A-Z]*
%attr(700,root,root) %dir %_sysconfdir/%name
%attr(700,root,root) %dir %_sysconfdir/%name/ipsec.d/
%attr(700,root,root) %dir %_sysconfdir/%name/ipsec.d/acerts
%attr(700,root,root) %dir %_sysconfdir/%name/ipsec.d/aacerts
%attr(700,root,root) %dir %_sysconfdir/%name/ipsec.d/ocspcerts
%attr(700,root,root) %dir %_sysconfdir/%name/ipsec.d/certs
%attr(700,root,root) %dir %_sysconfdir/%name/ipsec.d/cacerts
%attr(700,root,root) %dir %_sysconfdir/%name/ipsec.d/crls
%attr(700,root,root) %dir %_sysconfdir/%name/ipsec.d/private
%attr(700,root,root) %dir %_sysconfdir/%name/%name.d/*/
%attr(700,root,root) %dir %_sysconfdir/%name/%name.d/
%attr(700,root,root) %dir %_sysconfdir/%name/swanctl/
%config(noreplace) %_sysconfdir/%name/swanctl/swanctl.conf
%config(noreplace) %_sysconfdir/%name/%name.d/*/*.conf
%config(noreplace) %_sysconfdir/%name/%name.d/*.conf
%config(noreplace) %_sysconfdir/%name/%name.conf
%config(noreplace) %_sysconfdir/%name/ipsec.conf
%config(noreplace) %_sysconfdir/%name/ipsec.secrets
%config(noreplace) %_initdir/ipsec
%_unitdir/ipsec.service
%_datadir/%name/
%_libdir/%name/
%_libdir/ipsec/
%_sbindir/*
%_bindir/*
%_mandir/*/*

%files testing
%pkgdocdir/testing/

# TODO:
# - libstrongswan{,-devel} subpackages
# - review configurables (see also fedora-proposed spec)

%changelog
* Wed Sep 04 2019 Michael Shigorin <mike@altlinux.org> 5.8.1-alt1
- new version (watch file uupdate)

* Tue May 21 2019 Michael Shigorin <mike@altlinux.org> 5.8.0-alt1
- new version (watch file uupdate)

* Thu Dec 27 2018 Michael Shigorin <mike@altlinux.org> 5.7.2-alt1
- new version (watch file uupdate)

* Fri Oct 05 2018 Michael Shigorin <mike@altlinux.org> 5.7.1-alt1
- new version (watch file uupdate)

* Mon Sep 24 2018 Michael Shigorin <mike@altlinux.org> 5.7.0-alt1
- new version (watch file uupdate)

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 5.6.3-alt1.qa1.1
- NMU: Rebuild with new openssl 1.1.0.

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 5.6.3-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * backup-file-in-package for strongswan-testing

* Mon May 28 2018 Michael Shigorin <mike@altlinux.org> 5.6.3-alt1
- new version (watch file uupdate)

* Mon Feb 19 2018 Michael Shigorin <mike@altlinux.org> 5.6.2-alt1
- new version (watch file uupdate)

* Sun Nov 19 2017 Michael Shigorin <mike@altlinux.org> 5.6.1-alt1
- new version (watch file uupdate)

* Mon Aug 14 2017 Michael Shigorin <mike@altlinux.org> 5.6.0-alt1
- new version (watch file uupdate)

* Wed May 31 2017 Michael Shigorin <mike@altlinux.org> 5.5.3-alt1
- new version (watch file uupdate)

* Tue Mar 28 2017 Michael Shigorin <mike@altlinux.org> 5.5.2-alt1
- new version (watch file uupdate)

* Fri Oct 21 2016 Michael Shigorin <mike@altlinux.org> 5.5.1-alt1
- new version (watch file uupdate)

* Tue Jul 26 2016 Michael Shigorin <mike@altlinux.org> 5.5.0-alt1
- new version (watch file uupdate)

* Wed Mar 23 2016 Michael Shigorin <mike@altlinux.org> 5.4.0-alt1
- new version (watch file uupdate)

* Fri Nov 27 2015 Michael Shigorin <mike@altlinux.org> 5.3.5-alt1
- new version (watch file uupdate)
  + fixups upon 5.3.4

* Mon Nov 16 2015 Michael Shigorin <mike@altlinux.org> 5.3.4-alt1
- new version (watch file uupdate)
  + fixes CVE-2015-8023: authentication bypass in eap-mschapv2, see
    https://www.strongswan.org/blog/2015/11/16/

* Mon Sep 07 2015 Michael Shigorin <mike@altlinux.org> 5.3.3-alt1
- new version (watch file uupdate)

* Tue Jun 09 2015 Michael Shigorin <mike@altlinux.org> 5.3.2-alt1
- new version (watch file uupdate)
  + fixes CVE-2015-4171: client info disclosure, see
    https://www.strongswan.org/blog/2015/06/08/

* Tue Jun 02 2015 Michael Shigorin <mike@altlinux.org> 5.3.1-alt1
- new version (watch file uupdate)
  + fixes CVE-2015-3991: DoS with potential code execution, see
    https://www.strongswan.org/blog/2015/06/01/

* Wed Apr 08 2015 Michael Shigorin <mike@altlinux.org> 5.3.0-alt2
- built for Sisyphus (thx Vadim)

* Wed Apr 08 2015 Vadim Illarionov <gbIMoBou@gmail.com> 5.3.0-alt1.1
- added systemd service
- compiled with swanctl

* Mon Mar 30 2015 Michael Shigorin <mike@altlinux.org> 5.3.0-alt1
- new version (watch file uupdate)

* Mon Jan 05 2015 Michael Shigorin <mike@altlinux.org> 5.2.2-alt1
- new version (watch file uupdate)
- fixes CVE-2014-9221 (DoS)

* Sun Oct 19 2014 Michael Shigorin <mike@altlinux.org> 5.2.1-alt1
- new version (watch file uupdate)

* Wed Jul 09 2014 Michael Shigorin <mike@altlinux.org> 5.2.0-alt1
- new version (watch file uupdate)

* Tue Apr 15 2014 Michael Shigorin <mike@altlinux.org> 5.1.3-alt1
- new version (watch file uupdate)
- fixes CVE-2014-2338 (authentication bypass via rekeying)

* Sun Mar 09 2014 Michael Shigorin <mike@altlinux.org> 5.1.2-alt2
- added watch file

* Mon Mar 03 2014 Michael Shigorin <mike@altlinux.org> 5.1.2-alt1
- 5.1.2: http://wiki.strongswan.org/versions/50
  + new default configuration file layout is introduced
  + NTRUEncrypt support
- dropped patches (done upstream in a slightly different way)

* Wed Aug 07 2013 Michael Shigorin <mike@altlinux.org> 5.1.0-alt1
- 5.1.0: CVE-2013-5018 fix (charon DoS, see also
  http://www.strongswan.org/blog/2013/08/01/)

* Tue Apr 30 2013 Michael Shigorin <mike@altlinux.org> 5.0.4-alt1
- 5.0.4: CVE-2013-2944 fix (ECDSA signature vulnerability
  if openssl backend is loaded)

* Sat Apr 06 2013 Michael Shigorin <mike@altlinux.org> 5.0.3-alt1
- 5.0.3

* Thu Oct 04 2012 Michael Shigorin <mike@altlinux.org> 5.0.1-alt1
- 5.0.1

* Mon Jul 02 2012 Michael Shigorin <mike@altlinux.org> 5.0.0-alt1
- 5.0.0
- buildreq

* Mon Jun 25 2012 Michael Shigorin <mike@altlinux.org> 5.0.0-alt0.1
- 5.0.0rc1
  + pluto is there no more, see also
    http://www.strongswan.org/blog/2012/06/20/bye-bye-pluto.html

* Fri Jun 01 2012 Michael Shigorin <mike@altlinux.org> 4.6.4-alt1
- 4.6.4
  + CVE-2012-2388 is fixed (an attacker presenting a forged
    signature and/or certificate can authenticate as any
    legitimate user provided that "gmp" plugin is in use
    and a connection definition using RSA auth exists)

* Thu May 03 2012 Michael Shigorin <mike@altlinux.org> 4.6.3-alt1
- 4.6.3
  + patch2 unneeded (included upstream)

* Tue Feb 21 2012 Michael Shigorin <mike@altlinux.org> 4.6.2-alt1
- 4.6.2
- added upstream patch to fix trivial FTBFS

* Thu Dec 29 2011 Alexey Shabalin <shaba@altlinux.ru> 4.5.3-alt3
- add configure options: pkcs11,eap-*,dhcp,farp,ha,ctr,ccm,gcm,addrblock
- fix subst_enable for options with "-"
- build with libcap

* Mon Oct 03 2011 Michael Shigorin <mike@altlinux.org> 4.5.3-alt2
- drop testing/do-tests as it's not targeted at deployments
  but rather used for regression testing by upstream
  (maybe the whole subpackage should be purged)
- include all plugin-related files
- buildreq

* Fri Aug 05 2011 Michael Shigorin <mike@altlinux.org> 4.5.3-alt1
- 4.5.3
  + NB: libstrongswan and plugins moved into a private directory

* Wed May 25 2011 Michael Shigorin <mike@altlinux.org> 4.5.2-alt1
- 4.5.2

* Sun Mar 20 2011 Michael Shigorin <mike@altlinux.org> 4.5.1-alt2
- fix buildrequires

* Sat Feb 12 2011 Michael Shigorin <mike@altlinux.org> 4.5.1-alt1
- 4.5.1
  + NB: strongswan.conf parser changes:
    - 'include' statements implemented
    - configuration syntax for the attr plugin has changed

* Sun Oct 31 2010 Michael Shigorin <mike@altlinux.org> 4.5.0-alt1
- 4.5.0
  + see http://download.strongswan.org/CHANGES4.txt
  + IMPORTANT: IKEv2 becomes the default key exchange mode
- disabled patch0 (deals with non-issue, actually)

* Tue Oct 12 2010 Michael Shigorin <mike@altlinux.org> 4.4.1-alt1.1
- rebuilt against openssl-1.0.0a

* Wed Sep 22 2010 Michael Shigorin <mike@altlinux.org> 4.4.1-alt1
- 4.4.1
- added patch following earlier explanation by Tobias Brunner
  to force proper linking of libcharon and libhydra against
  libstrongswan (this breaks optional integrity tests though)

* Tue Aug 03 2010 Michael Shigorin <mike@altlinux.org> 4.3.7-alt1
- 4.3.7: major security fix for snprintf() misuse
  introduced in 4.3.3

* Mon May 10 2010 Michael Shigorin <mike@altlinux.org> 4.4.0-alt1
- 4.4.0
  + see http://download.strongswan.org/CHANGES4.txt
- updated patch
- buildreq

* Mon Feb 22 2010 Michael Shigorin <mike@altlinux.org> 4.3.6-alt1
- 4.3.6
  + NB: 4.3.5 has seen some plugin shuffling,
    check upstream changelog in case of doubt
- buildreq (including gperf)

* Tue Sep 15 2009 Michael Shigorin <mike@altlinux.org> 4.3.4-alt1
- 4.3.4

* Sun Jul 26 2009 Michael Shigorin <mike@altlinux.org> 4.3.3-alt3
- fixed incomplete patch (forgot to actually use prepared variable)

* Fri Jul 24 2009 Michael Shigorin <mike@altlinux.org> 4.3.3-alt2
- moved testing docs into a noarch subpackage (thanks repocop)
- patched testing script to avoid 100%% predictable /tmp paths

* Thu Jul 23 2009 Michael Shigorin <mike@altlinux.org> 4.3.3-alt1
- 4.3.3 (closes: #20849)
  + the RDN parser vulnerability discovered by Orange Labs research team
    was not completely fixed in version 4.3.2. Some more modifications
    had to be applied to the asn1_length() function to make it robust.
  + thanks crux@ for prompt notification

* Wed Jul 08 2009 Michael Shigorin <mike@altlinux.org> 4.3.2-alt1
- 4.3.2
  + disabled patch0 (applied upstream)
  + dropped patch1 (irrelevant with 4.3.x)
- finally got around to merging strongswan.git by ildar@
  (also closes: #18260)
  + including library subpackage removal
  + initscript status fix
- disabled VIA Padlock support on non-x86_32 (fails to build)
- spec cleanup
- buildreq

* Tue Jun 23 2009 Michael Shigorin <mike@altlinux.org> 4.2.16-alt1
- 4.2.16 fixes DoS vulnerability in the ASN.1 parser;
  thanks crux@ for notification (closes: #20527)

* Thu May 28 2009 Michael Shigorin <mike@altlinux.org> 4.2.15-alt1
- 4.2.15 fixes two DoS issues with charon
  + sending a malformed IKE_SA_INIT request leaved an incomplete state
    which caused a null pointer dereference if a subsequent
    CREATE_CHILD_SA request was sent
  + sending an IKE_AUTH request with either a missing TSi or TSr payload
    caused a null pointer derefence because the checks for TSi and TSr
    were interchanged
  + patch2 unneeded (included upstream)
- thanks crux@ for heads-up (closes: #20206)

* Wed May 13 2009 Michael Shigorin <mike@altlinux.org> 4.2.14-alt1
- 4.2.14 fixes CVE-2009-0790: DoS against dead peer detection code
- fixed FTBFS with glibc-2.9
- appled vendor patch fixing invalid IKE state issue

* Sat Jan 10 2009 Michael Shigorin <mike@altlinux.org> 4.2.10-alt3
- added a patch to avoid superfluous file dependencies

* Thu Jan 08 2009 Michael Shigorin <mike@altlinux.org> 4.2.10-alt2
- fixed ntpd comments in initscript ;-)

* Thu Jan 08 2009 Michael Shigorin <mike@altlinux.org> 4.2.10-alt1
- 4.2.10
- removed patches (builds as is)
- spec cleanup

* Sat Dec 20 2008 Ildar Mulyukov <ildar@altlinux.ru> 4.2.9-alt1
- new version
- many new features
- spec refactoring

* Wed Oct 10 2007 Grigory Milev <week@altlinux.ru> 4.1.6-alt2
- Rebuild for x86_64
- cleanup spec
- move libraries to separate package

* Mon Sep 03 2007 $inister <sinister@altlinux.ru> 4.1.6-alt1
- new version

* Tue Aug 28 2007 $inister <sinister@altlinux.ru> 4.1.5-alt1
- initial packaging
