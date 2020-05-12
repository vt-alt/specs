%define _ldapconfdir %_sysconfdir/openldap
%define _hooksdir %_sysconfdir/hooks/hostname.d

Name:    ldap-user-tools
Version: 0.9.5
Release: alt1

Summary: Utilities to work with LDAP users
Group:   Development/Other
License: GPL

Source:  %name-%version.tar

BuildArch: noarch

BuildRequires: gettext-tools
Requires: ruby-ldap openldap-servers perl-Crypt-SmbHash alterator-kdc
Requires: alterator-openldap-functions >= 0.3

%description
Utilities to work with LDAP users

%prep
%setup

%build
make -C po

%install
for i in scripts/*; do
install -Dpm755 "$i" "%buildroot%_sbindir/${i##*/}"
done
install -Dpm640 data/slapd-hdb-template.conf %buildroot/%_ldapconfdir/slapd-hdb-template.conf
install -Dpm640 data/slapd-mdb-template.conf %buildroot/%_ldapconfdir/slapd-mdb-template.conf
install -Dpm444 schema/kerberos.schema %buildroot/%_ldapconfdir/schema/kerberos.schema
install -Dpm755 bin/mkntpasswd %buildroot/%_sbindir/mkntpasswd
install -Dpm755 hooks/ldap-domain %buildroot/%_hooksdir/21-ldap-domain
install -pm755 -d %buildroot/%_sysconfdir/alterator/openldap
%makeinstall_std -C po

%find_lang %name

%files -f %name.lang
%_sbindir/ldap-*
%_sbindir/mkntpasswd
%_ldapconfdir/slapd-hdb-template.conf
%_ldapconfdir/slapd-mdb-template.conf
%_ldapconfdir/schema/kerberos.schema
%_hooksdir/21-ldap-domain
%dir %_sysconfdir/alterator/openldap

%changelog
* Tue May 05 2020 Andrey Cherepanov <cas@altlinux.org> 0.9.5-alt1
- Check full name of added group member (ALT #38441).

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.1
- Rebuild with new Ruby autorequirements.

* Sun Jul  8 2018 Leonid Krivoshein <klark@altlinux.org> 0.9.4-alt1
- deprecated backend template renamed to slapd-hdb-template.conf
- added new MDB template for work with openldap >= 2.4.45-alt3
- new MDB backend template now used by default (ALT #35095)
- added support both database backends: deprecated HDB and new MDB
- before create DN may set key SLAPD_BACKEND in /etc/sysconfig/ldap
- for create HDB-based DN's also may run: 'ldap_dn create <DN> --hdb'

* Wed Jun 08 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.9.3-alt1
- no more direct calls of /etc/init.d/slapd

* Mon Sep 29 2014 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt1
- ldap-useradd: Create user mail spool file.

* Tue Aug 27 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9.1-alt1
- misstemplation of slapd-template.conf fixed

* Tue Aug 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9.0-alt2
- +requires_preauth added to addprinc call

* Tue Aug 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9.0-alt1
- actual kerberos.schema
- acl rules make kdc able to store last{Susessfull/Failed}LoginTime

* Tue Jun 18 2013 Andrey Cherepanov <cas@altlinux.org> 0.8.4-alt1
- Fix username check regexp for workstation
- Fix missing workstation list in ldap-getent
- Fix workstation remove in ldap-userdel

* Wed Jun 05 2013 Andrey Cherepanov <cas@altlinux.org> 0.8.3-alt1
- Add support to map and unmap Samba and domain groups
- Add -g <gid> option to ldap-groupmod to change group GID
- Correct check missing values for options in ldap-groupmod

* Tue Apr 23 2013 Andrey Cherepanov <cas@altlinux.org> 0.8.2-alt2
- Allow only lowercase letters in username
- Add localization files for use from alterator-ldap-users

* Wed Nov 07 2012 Andrey Cherepanov <cas@altlinux.org> 0.8.2-alt1
- Check if Kerberos is working

* Tue Oct 30 2012 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt1
- ldap-groupadd --default reads initial group list and put all users
  to groups
- Add -m and -x options to ldap-groupmod to manage group membership
- Add -g option to ldap-usermod to set user primary group
- More significant error messages

* Mon Oct 22 2012 Andrey Cherepanov <cas@altlinux.org> 0.8.0-alt1
- Support add, list and delete workstation records:
  * add: ldap-useradd -w -i <ws>
  * list: ldap-getent ws
  * delete: ldap-userdel -w <ws>
- More reliable primary group deletion on user delete

* Wed Oct 03 2012 Andrey Cherepanov <cas@altlinux.org> 0.7.2-alt2
- Add -r option to ldap-userdel to delete home directory and mail spool

* Mon Oct 01 2012 Andrey Cherepanov <cas@altlinux.org> 0.7.2-alt1
- Fix user creation in Alterator
- Correct creation on missed first_name

* Thu Sep 27 2012 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt1
- Partial support useradd(8) syntax in ldap-useradd (ALT #27271)
- ldap-useradd create user homedir
- ldap-passwd supports password as parameter

* Fri Sep 21 2012 Andrey Cherepanov <cas@altlinux.org> 0.7-alt1
- Use default LDAP configuration if DN_CONF is empty
- Add --help and --version arguments support in scripts
- Write short help for ldap-* scripts

* Tue Jul 12 2011 Fr. Br. George <george@altlinux.ru> 0.6-alt4
- Fix "ldap-dn find" exit status and output bug

* Thu May 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt3
- dependence to alterator-openldap removed

* Thu Mar 31 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt2
- enable one-letter domain components

* Wed Mar 30 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- setup slapd to listen ldaps

* Thu Aug 20 2009 Lebedev Sergey <barabashka@altlinux.org> 0.5-alt1.2
- added previous fix (after merge with raorn, didn't add reverted commit)

* Wed Aug 19 2009 Lebedev Sergey <barabashka@altlinux.org> 0.5-alt1.1
- fixed ldap-passwd ldif

* Mon Aug 03 2009 Alexey I. Froloff <raorn@altlinux.org> 0.5-alt1
- Force input to be always UTF-8 (closes: #20942)

* Wed Jul 08 2009 Lebedev Sergey <barabashka@altlinux.org> 0.4-alt4
- added initial DB_CONFIG into database dir (for openldap 2.4.*)
- added actions
  + ldap-dn list
  + ldap-dn master

* Thu May 14 2009 Lebedev Sergey <barabashka@altlinux.org> 0.4-alt3.1
- fixed #19961

* Mon May 04 2009 Lebedev Sergey <barabashka@altlinux.org> 0.4-alt3
- added param (add, delete, replace) LDAP::MOD for ldap-usermod
- made krb functions silent (improved error reporting)

* Thu Apr 30 2009 Lebedev Sergey <barabashka@altlinux.org> 0.4-alt2
- removed info messages
- removed home and mail spool managing (creating and removing)

* Wed Apr 22 2009 Lebedev Sergey <barabashka@altlinux.org> 0.4-alt1
- now using alterator-openldap-functions
- code cleanup
- moved logic ldap-config to alterator-openldap-functions
- deleted ldap-proxyuser
- deleted ldap-sshkeygen
- added ldap-groupmod
- fixed #19808

* Mon Apr 20 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt4.1
- fixed typo

* Mon Apr 20 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt4
- hook renamed to ldap-domain
- enable_schema removed to alterator-openldap hook

* Thu Apr 02 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt3
- added kerberos.schema file
- added kerberos schema enabling in openldap hook

* Mon Mar 30 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt2
- rewrote ldap-init #19371

* Mon Mar 23 2009 Lebedev Sergey <barabashka@altlinux.org> 0.3-alt1
- invoke supplemental kdc ops when applicable (by sbolshakov)

* Fri Mar 20 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt9
- fixed renaming dn
- added support ou=kdcroot for kerberos

* Fri Mar 20 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt8
- fixed openldap hook (domain creation)
- added support for kdc (sbolshakov)

* Thu Mar 19 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt7
- moved openldap.hook to openldap
- added domain renaming into openldap hook
- added dn renaming into ldap-dn

* Tue Mar 17 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt6
- improved finding included conf files in slapd.conf

* Thu Mar 12 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt5.1
- fixed slapd restart and ldap-init

* Wed Mar 11 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt5
- added openldap.hook

* Fri Feb 27 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt4
- added mkntpasswd tool
- added Requires perl-Crypt-SmbHash
- added samba attributes support
- added find in ldap-dn
- added mail spool support

* Thu Feb 26 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt3.2
- renamed template.conf
- improved error messaging
- updated check_dn_name (ldap_dn)
- added get_slapd_status (ldap_dn)

* Wed Feb 25 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt3.1
- added template.conf for dn creation
- some coding style fixes

* Wed Feb 25 2009 Lebedev Sergey <barabashka@altlinux.org> 0.2-alt3
- added ldap-dn (dn manager)
- added support for different SLAPD_CONF
- changed localhost to 127.0.0.1

* Tue Feb 10 2009 Sir Raorn <raorn@altlinux.ru> 0.2-alt2
- Fix problem with ldap-passwd

* Fri Feb 06 2009 Sir Raorn <raorn@altlinux.ru> 0.2-alt1
- [0.2]
- ldap-getent:
 + use ruby-ldap for LDIF parsing
 + allow search key specification
 + allow search fields specification when searching "passwd" database
- ldap-passwd:
 + use blowfish for {CRYPT}'ed passwords
 + accept password as command-line argument
 + use ldap-usermod instead of direct ldapmodify call
- ldap-usermod:
 + use ruby-ldap for LDIF generation
 + accept unquoted "key:value" pairs on stdin
- ldap-useradd:
 + use ldap-getent when guessing gidNumber
- Spec cleanup

* Wed Feb 04 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt2.M50.2
- coding style fixes
- "binddn" type
- removed " from binddn,rootdn,bindpw,rootpw
- added  objectclasses in ldap-useradd:
  + person
	+ organizationalPerson
	+ inetOrgPerson
- removed objectclass in ldap-useradd:
  + account

* Wed Feb 04 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt2.M50.1
- first build for 5.0

* Mon Feb 02 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt2.M41.1
- fixed ldap-config

* Fri Jan 30 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt2.M41
- working version for alterator-ldap-auth alterator-ldap-users

* Fri Jan 30 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1-alt1.M41
- initial version based on cl-user-tools

