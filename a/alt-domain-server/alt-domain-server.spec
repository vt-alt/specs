Name: alt-domain-server
Version: 0.5.3
Release: alt1

Summary: All needed for alt-domain server
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Source: %name-%version.tar
Requires: bind alterator-bind
Requires: openldap-servers krb5-kdc krb5-kadmin krb5-kinit ldap-user-tools
Requires: dhcp-server alterator-dhcp
Requires: alterator-net-domain alterator-ldap-users ldap-user-tools
Requires: samba
Requires: alterator-kdc alterator-ldap-groups alterator-net-eth

Provides: installer-feature-setup-openldap
Obsoletes: installer-feature-setup-openldap

%description
Install this package if you need alt-domain server

%prep
%setup -q

%install
mkdir -p %buildroot/etc/
cp -a hooks %buildroot/etc/
mkdir -p %buildroot/usr/share/install2/preinstall.d
cp preinstall.d/* %buildroot/usr/share/install2/preinstall.d/

%files
/etc/hooks/hostname.d/*
/usr/share/install2/preinstall.d/*

%changelog
* Tue Oct 08 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.5.3-alt1
- samba configuration fixed

* Tue Oct 08 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.5.2-alt1
- move hook for reissue service certificates to first place

* Fri Mar 01 2019 Andrey Cherepanov <cas@altlinux.org> 0.5.1-alt1
- add hook for reissue service certificates for new domain

* Sun Jul  8 2018 Leonid Krivoshein <klark@altlinux.org> 0.5-alt1
- fix preinstall script for work with openldap >= 2.4.45-alt3
- removed virtual dependency to /usr/sbin/smbd
- introduced dependency to samba

* Thu Nov 27 2014 Mikhail Efremov <sem@altlinux.org> 0.4-alt1
- Use variable to control Samba services activation.

* Fri Feb 01 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- version independent samba dependence

* Thu Jan 31 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- i-f-setup-openldap moved here

* Tue Aug 07 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build

