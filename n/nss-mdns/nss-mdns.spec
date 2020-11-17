Name: nss-mdns
Version: 0.14.1
Release: alt1

Summary: nss-mdns provides host name resolution via Multicast DNS
License: GPL
Group: System/Libraries
Url: https://github.com/lathiat/nss-mdns

Source: v%version.tar.gz

BuildRequires: gcc-c++ libavahi-devel lynx

%package -n lib%name
Group: System/Libraries
Summary: nss-mdns provides host name resolution via Multicast DNS
Requires: avahi-daemon >= 0.6.21-alt1
Requires(pre): chrooted >= 0.3.5-alt1 chrooted-resolv sed
Requires(postun): chrooted >= 0.3.5-alt1 sed

%description
nss-mdns is a plugin for the GNU Name Service Switch (NSS) functionality
of the GNU C Library (glibc) providing host name resolution via
Multicast DNS (aka Zeroconf, aka Apple Rendezvous, aka Apple Bonjour),
effectively allowing name resolution by common Unix/Linux programs in
the ad-hoc mDNS domain .local.

nss-mdns provides client functionality only, which means that you have to run
a mDNS responder daemon seperately from nss-mdns if you want to register
the local host name via mDNS.

It is necessary to change "hosts" in /etc/nsswitch.conf to
hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4

%description -n lib%name
nss-mdns is a plugin for the GNU Name Service Switch (NSS) functionality
of the GNU C Library (glibc) providing host name resolution via
Multicast DNS (aka Zeroconf, aka Apple Rendezvous, aka Apple Bonjour),
effectively allowing name resolution by common Unix/Linux programs in
the ad-hoc mDNS domain .local.

nss-mdns provides client functionality only, which means that you have to run
a mDNS responder daemon seperately from nss-mdns if you want to register
the local host name via mDNS.

It is necessary to change "hosts" in /etc/nsswitch.conf to
hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4

%prep
%setup

%build
%autoreconf
%configure  --libdir=/%_lib --localstatedir=%_var --enable-avahi --disable-static
%make_build

%install
%make install DESTDIR=%buildroot

%post -n lib%name
if [ -f /etc/nsswitch.conf ] ; then
	sed -i.bak '
	/^hosts:/ !b
	/\<mdns\(4\|6\)\?\(_minimal\)\?\>/ b
	s/\([[:blank:]]\+\)dns\>/\1mdns4_minimal [NOTFOUND=return] dns/g
	' /etc/nsswitch.conf
	update_chrooted all
fi

%postun -n lib%name
if [ "$1" -eq 0 -a -f /etc/nsswitch.conf ] ; then
	sed -i.bak '
	/^hosts:/ !b
	s/[[:blank:]]\+mdns\(4\|6\)\?\(_minimal\( \[NOTFOUND=return\]\)\?\)\?//g
	' /etc/nsswitch.conf
	update_chrooted all
fi

%files -n lib%name
%doc *.md
/%_lib/libnss_*.so.*

%changelog
* Thu Dec 05 2019 Fr. Br. George <george@altlinux.ru> 0.14.1-alt1
- Autobuild version bump to 0.14.1

* Thu Dec 05 2019 Fr. Br. George <george@altlinux.ru> 0.14-alt1
- submajor version update

* Tue Jun 11 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.10-alt4
- post scripts got from Fedora (closes #29051)
- postuntrigger removed

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.10-alt3.qa1
- NMU: rebuilt for debuginfo.

* Tue Dec 30 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10-alt3
- prereq on chrooted >= 0.3.5-alt1 moved to subpackage (#18401)

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10-alt2
- obsolete by filetriggers macros removed

* Thu Aug 23 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10-alt1
- 0.10 released

* Tue Jan 30 2007 Sergey V Turchin <zerg at altlinux dot org> 0.9-alt1
- initial specfile
