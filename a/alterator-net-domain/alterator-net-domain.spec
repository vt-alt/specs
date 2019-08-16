Name:    alterator-net-domain
Version: 0.7.0
Release: alt8
Source:  %name-%version.tar

Summary: Alterator module to provision system network domain
License: GPL
Group:   System/Configuration/Other
Requires: alterator >= 5.0
Requires: alterator-l10n >= 2.0-alt2

Conflicts: ldap-user-tools < 0.8.1
Conflicts: alterator-lookout < 1.6-alt6
Conflicts: alterator-fbi < 5.9-alt2


%ifarch %e2k
BuildRequires: guile20-devel libguile20-devel
%else
BuildRequires: guile22-devel
%endif
BuildRequires: rpm-build >= 4.0.4-alt103
BuildRequires: alterator >= 5.0 alterator-fbi >= 5.33-alt1

%description
Alterator module to provision system network domain.
Supported domain type: BIND, ALT-domain, Active Directory
and FreeIPA domain.

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/
%_alterator_libdir/ui/*/
%_alterator_backend3dir/*
%dir %_libexecdir/alterator/hooks/net-domain.d
%_bindir/*-sh-functions

%changelog
* Fri Aug 16 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.7.0-alt8
- samba-DC is samba-dc now

* Sun Jul  8 2018 Leonid Krivoshein <klark@altlinux.org> 0.7.0-alt7
- alt-domain-server installer feature no more required (ALT #31712).

* Fri Apr 13 2018 Grigory Ustinov <grenka@altlinux.org> 0.7.0-alt6.1.1
- NMU: Replace BuildRequires for guile on e2k arch.

* Mon May 22 2017 Paul Wolneykien <manowar@altlinux.org> 0.7.0-alt6
- Fixed: Cleanup smb.conf before activating ALT Domain.
- Fix: Stop extra services for the simple DNS mode.

* Fri May 05 2017 Paul Wolneykien <manowar@altlinux.org> 0.7.0-alt5
- Fixed DNS-only domain update.
- Fixed ALT-domain configuration parsing.

* Wed Apr 26 2017 Paul Wolneykien <manowar@altlinux.org> 0.7.0-alt4
- Fix: Cleanup BIND (named) configuration before enabling the service.
- Report the IPA parameters only when the current domain type is 'ipa'.

* Tue Apr 25 2017 Paul Wolneykien <manowar@altlinux.org> 0.7.0-alt3
- Do not explicitly depend on '389-ds-base'.
- Make use of 'alterator-service-functions' to control the system servies.
- Cleanup the Kerberos configuration before Samba AD setup (closes: 33409).
- Improved IPA installed/uninstalled status detection.

* Wed Apr 19 2017 Paul Wolneykien <manowar@altlinux.org> 0.7.0-alt2
- Do not explicitly depend on 'freeipa-server'.

* Wed Apr 19 2017 Paul Wolneykien <manowar@altlinux.org> 0.7.0-alt1
- Setup and configure a FreeIPA domain.

* Thu Oct 13 2016 Andrey Cherepanov <cas@altlinux.org> 0.6.3-alt1
- Set Active Directory domain in resolvconf and run hooks for it
- [Active Directory] Set dns forwarders and password of Administrator
- Localize Active Directory service status

* Wed Sep 21 2016 Andrey Cherepanov <cas@altlinux.org> 0.6.2-alt1
- Enable samba service during Active Directory provision

* Tue Sep 20 2016 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt1
- Stop and disable any conflict services during Active Directory
  provision
- Extend description

* Thu Aug 04 2016 Andrey Cherepanov <cas@altlinux.org> 0.6-alt1
- Support provision Active Directory domain
- Refactor module ui: choose domain type, make unavailable option
  disabled

* Tue Jun 07 2016 Mikhail Efremov <sem@altlinux.org> 0.5-alt1
- Write domain in the resolvconf.conf.

* Tue Oct 14 2014 Mikhail Efremov <sem@altlinux.org> 0.4-alt19
- Drop QT UI leftovers.

* Wed Jan 30 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt18
- delete dependence on samba, this package should not depend on it
  95-smb hook moved to alt-domain-server package

* Thu Nov 08 2012 Andrey Cherepanov <cas@altlinux.org> 0.4-alt17
- Fix netlogon section creation

* Wed Nov 07 2012 Andrey Cherepanov <cas@altlinux.org> 0.4-alt16
- Add netlogon share for netlogon script

* Wed Nov 07 2012 Andrey Cherepanov <cas@altlinux.org> 0.4-alt15
- Fix system group 'users' mapping
- Fix Samba scripts call

* Sat Nov 03 2012 Andrey Cherepanov <cas@altlinux.org> 0.4-alt14
- Fix group create
- Add requires on samba and ldap-user-tools

* Fri Nov 02 2012 Andrey Cherepanov <cas@altlinux.org> 0.4-alt13
- Create Samba configuration for NT domain

* Mon Oct 29 2012 Andrey Cherepanov <cas@altlinux.org> 0.4-alt12
- Check domain name validity according RFC 1035

* Tue May 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt11
- fix enabling krb5 without name change

* Wed Apr 18 2012 Mikhail Efremov <sem@altlinux.org> 0.4-alt10
- Change warning message.

* Wed Jun 15 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt9
- buttons rapaid in nonkerberos mode

* Fri Jun 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt8
- now module is html only

* Fri Apr 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt7
- hide kerberos domain status when disabled

* Tue Mar 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt6
- move samba restart to after all changes

* Tue Mar 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt5
- reread data after write
- start smbd when creating domain

* Tue Mar 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt4
- fix previous fix :(

* Mon Mar 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt3
- work in nonmaster mode fixed

* Mon Mar 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt2
- test for dhcpd
- checkbox for kerberos domain

* Thu Mar 24 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- tests for ldap/kerberos domain status added

* Wed Dec 08 2010 Mikhail Efremov <sem@altlinux.org> 0.3-alt4
- More restrict possible domain names.

* Tue Oct 26 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt3
- always run net-domain.d hooks

* Mon Oct 25 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt2
- always run hooks

* Fri Oct 08 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- master if no role defined

* Fri Apr 16 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt5
- no roles now

* Wed Mar 03 2010 Mikhail Efremov <sem@altlinux.org> 0.2-alt4
- check hostname length.

* Fri Dec 11 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- bugfix: write role before writing of domain name

* Wed Dec 09 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- restrict possible domain names

* Thu Oct 22 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- use workflow 'none', share callbacks between qt and html.

* Fri Aug 07 2009 Mikhail Efremov <sem@altlinux.org> 0.1-alt8
- write domain to /etc/net/ifaces/lo/resolv.conf.

* Thu Jun 11 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt7
- role is 'master' by default.

* Thu Apr 02 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt6
- menu file: move to group 'system'

* Mon Mar 30 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- fix runhooks '#t' variant (used by firsttime)

* Wed Mar 18 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- add hook system
- add domain name to zeroconf information

* Fri Mar 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- fix typo

* Fri Mar 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- edit server role

* Wed Mar 04 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build

