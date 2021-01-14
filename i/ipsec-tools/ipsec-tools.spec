Summary: IPsec-Tools package use the IPsec functionality in the linux-2.5+ kernels.
Name: ipsec-tools
Version: 0.8.2
Release: alt3
URL: http://ipsec-tools.sourceforge.net/
License: BSD
Group: Security/Networking
Requires: libipsec = %version-%release

Source0: http://sourceforge.net/projects/ipsec-tools/files/ipsec-tools/%{version}/ipsec-tools-%{version}.tar
Source1: %name-racoon.init
Source2: %name-racoon.sysconfig
Source3: p1_up_down
Source4: racoon.conf
Source5: racoon.pam
Source6: racoon.service

# patches from ipsec-tools-0.8.0-2.fc16.src.rpm
# Ignore acquires that are sent by kernel for SAs that are already being
# negotiated (#234491)
Patch3: ipsec-tools-0.8.0-acquires.patch
# Support for labeled IPSec on loopback
Patch4: ipsec-tools-0.8.0-loopback.patch
# Create racoon as PIE
Patch11: ipsec-tools-0.7.1-pie.patch
# Fix leak in certification handling
Patch14: ipsec-tools-0.7.2-moreleaks.patch
# Do not install development files
Patch16: ipsec-tools-0.8.0-nodevel.patch
# Use krb5 gssapi mechanism
Patch18: ipsec-tools-0.7.3-gssapi-mech.patch
# Silence strict aliasing warnings
Patch20: ipsec-tools-0.8.0-aliasing.patch
# CVE-2015-4047
Patch21: ipsec-tools-0.8.2-CVE-2015-4047.patch
# Calling_station-Id attribute for xauth RADIUS requests
Patch22: ipsec-tools-0.8.2-952413.patch

Patch100: ipsec-tools-0.7.2-alt-werror.patch
Patch101: ipsec-tools-0.8.0-alt-makefile.patch
Patch102: ipsec-tools-0.7.2-alt-config.patch
Patch103: ipsec-tools-0.7.2-alt-unres.patch
Patch104: ipsec-tools-0.7.2-alt-gcc44-warns.patch
Patch105: ipsec-tools-0.8.0-alt-wildcard-psk.patch
Patch106: ipsec-tools-0.8.2-alt-selinux-compat.patch

# Debian patches
Patch201: ipsec-tools-0.8.2-make-peer_certfile-dnssec-validate-dnssec.patch
Patch203: ipsec-tools-0.8.2-configure-pass-Wl-with-R.patch
Patch204: ipsec-tools-0.8.2-include-stdint.patch
Patch205: ipsec-tools-0.8.2-asn1_utf8.patch
Patch206: ipsec-tools-0.8.2-ipv6literalaltname.patch
Patch207: ipsec-tools-0.8.2-checkpoint-xauth.patch
Patch209: ipsec-tools-0.8.2-implicit-int.patch
Patch210: ipsec-tools-0.8.2-glibc-bsd-source-obsolete.patch
Patch211: ipsec-tools-0.8.2-CVE-2016-10396.patch
Patch212: ipsec-tools-0.8.2-gcc7-support.patch
Patch213: ipsec-tools-0.8.2-shared-libfl.patch
Patch214: ipsec-tools-0.8.2-openssl1.1.patch
Patch215: ipsec-tools-0.8.2-fix-uninitialized-vars.patch
Patch216: ipsec-tools-0.8.2-sprintf-sizes.patch

#optimized out: libcom_err-devel
BuildRequires: flex libaudit-devel libpam-devel libselinux-devel libssl-devel libldap-devel libkrb5-devel

%description
This is the IPsec-Tools package.  You need this package in order to
really use the IPsec functionality in the linux-2.5+ kernels.  This
package builds:

- setkey, a program to directly manipulate policies and SAs
- racoon, an IKEv1 keying daemon

%package -n libipsec
Summary: IPSec-Tools shared libraries
Group: System/Libraries

%description -n libipsec
IPSec-Tools shared libraries package.


%package -n libipsec-devel
Summary: IPSec-Tools development files
Group: Development/C
Requires: %name = %version-%release
Provides: %name-devel = %version
Obsoletes: %name-devel

%description -n libipsec-devel
IPSec-Tools development files package.


%prep
%setup -q

%patch3 -p1 -b .acquires
%patch4 -p1 -b .loopback

%patch11 -p1 -b .pie
%patch14 -p1 -b .moreleaks
#%patch16 -p1 -b .nodevel
%patch18 -p1 -b .gssapi-mech
%patch20 -p1 -b .aliasing
%patch21 -p1 -b .cve_2015_4047
%patch22 -p1 -b .station_id

#%patch100 -p1 -b .werror
%patch101 -p1 -b .altmake
%patch102 -p1 -b .syscfg
%patch103 -p1 -b .unres
%patch104 -p1 -b .gcc4warn
%patch105 -p1 -b .wildcard
%patch106 -p2

%patch201 -p1
%patch203 -p1
%patch204 -p1
%patch205 -p1
%patch206 -p1
%patch207 -p1
%patch209 -p1
%patch210 -p1
%patch211 -p1
%patch212 -p1
%patch213 -p1
%patch214 -p1
%patch215 -p1
%patch216 -p1

sed -i 's|-Werror||g' configure*

%build
./bootstrap
%configure \
	--disable-static \
	--with-kernel-headers=/usr/include \
	--enable-shared \
	--sysconfdir=/etc/racoon \
	--enable-hybrid \
	--enable-frag \
	--enable-stats \
	--enable-dpd \
	--enable-natt=kernel \
	--enable-natt \
	--enable-security-context \
	--enable-audit \
	--enable-gssapi \
	--with-libpam \
	--with-libldap \
	--without-readline \
	--enable-adminport=yes

%make

%install
%make install DESTDIR=%buildroot

mkdir -p %buildroot/%_sysconfdir/racoon/certs
mkdir -p %buildroot/%_sysconfdir/racoon/scripts
mkdir -p %buildroot/%_initdir
mkdir -p %buildroot/%_unitdir
mkdir -p %buildroot/%_sysconfdir/sysconfig
mkdir -p %buildroot/%_sysconfdir/pam.d
install -p -m0600 src/racoon/samples/psk.txt %buildroot%_sysconfdir/racoon/
install -p -m0644 %SOURCE4 %buildroot%_sysconfdir/racoon/
install -p -m0700 %SOURCE3 %buildroot%_sysconfdir/racoon/scripts/
install -m 0755 %SOURCE1 %buildroot%_initdir/racoon
install -m 0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/racoon
install -p -m0644 %SOURCE5 %buildroot%_sysconfdir/pam.d/racoon
install -p -m0644 %SOURCE6 %buildroot%_unitdir/racoon.service

%preun
%preun_service racoon

%post
%post_service racoon

%files
%_initdir/racoon
%_unitdir/racoon.service
%config(noreplace) %_sysconfdir/racoon/racoon.conf
%config(noreplace) %_sysconfdir/racoon/psk.txt
%config(noreplace) %_sysconfdir/sysconfig/racoon
%config(noreplace) %_sysconfdir/pam.d/racoon
%_sysconfdir/racoon/scripts/p1_up_down
%dir %_sysconfdir/racoon/certs
%dir %_sysconfdir/racoon/scripts
%dir %_sysconfdir/racoon/
%_sbindir/plainrsa-gen
%_sbindir/racoon
%_sbindir/racoonctl
%_sbindir/setkey
%_man3dir/*
%_man5dir/*
%_man8dir/*
%doc ChangeLog NEWS README src/racoon/doc/* src/racoon/samples/roadwarrior src/racoon/samples/*sample*
%dir %_localstatedir/racoon

%files -n libipsec
%_libdir/libipsec.so.*
%_libdir/libracoon.so.*

%files -n libipsec-devel
%_libdir/libipsec.so
%_libdir/libracoon.so
%_includedir/libipsec/*
%dir %_includedir/libipsec
%_includedir/racoon/*
%dir %_includedir/racoon


%changelog
* Mon Aug 03 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.2-alt3
- NMU: fixed build with new selinux.

* Wed Aug 29 2018 Alexey Shabalin <shaba@altlinux.org> 0.8.2-alt2
- build with openssl-1.1
- add patches from Debian
- fixed CVE-2016-10396

* Sun Feb 21 2016 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt1
- 0.8.2
- fixed CVE-2015-4047

* Thu May 23 2013 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1
- add systemd unit file
- build with ldap support

* Wed Feb 20 2013 Denis Baranov <baraka@altlinux.ru> 0.8.0-alt2
- add compile option enable-adminport=yes

* Thu Dec 29 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0
- enable ipv6
- build with pam support
- add support wildcard in psk.txt (patch105)

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 0.7.2-alt1.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sun May 24 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 0.7.2-alt1.1
- fix package build

* Sun May 24 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 0.7.2-alt1
- 0.7.2 (closes: #19917)
- move shared libraries to 'libipsec' package
- add libipsec-devel package

* Sun Dec 14 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.7.1-alt1
- 0.7.1 with patches from ipsec-tools-0.7.1-6.fc11

* Wed Aug 27 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.6.7-alt2
- CVE-2008-3651 and CVE-2008-3652 patches from RedHat package
  ipsec-tools-0.6.5-9.3:
  + for DoS through various memory leaks (rh#456660, rh#458846)
- other patches from RH

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.6.7-alt1.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Sun May 13 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 0.6.7-alt1
- 0.6.7
- CVE-2007-1841
- ALT bug #11604 fixed
- add init-script for racoon daemon

* Wed Dec 20 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 0.6.6-alt1
- fix build requires

* Fri Oct 27 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 0.6.6-alt0
- 0.6.6

* Wed Mar 2 2005 Maxim Tyurin <mrkooll@altlinux.ru> 0.5-alt1
- New version (fixed CAN-2004-0155) and fixed potencial buffer ovefflow.

* Thu Jun 10 2004 Maxim Tyurin <mrkooll@altlinux.ru> 0.2.3-alt1
- Initial build.

