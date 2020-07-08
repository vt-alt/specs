%define _unpackaged_files_terminate_build 1

Name: local-policy
Version: 0.4.2
Release: alt1

Summary: ALT Local policies
License: GPLv2+
Group: Other
Url: http://git.altlinux.org/people/sin/packages/local-policy.git

BuildArch: noarch

Requires: control

Source0: %name-%version.tar

%description
Local policies for ALT solutions based on Sisyphus
includes additional control facilities and default policies
templates in PReg format converted to XML.

%prep
%setup -q

%install
for i in sshd-gssapi-auth \
         sshd-allow-groups-list \
         ssh-gssapi-auth \
         krb5-conf-ccache \
         ldap-reverse-dns-lookup \
         ldap-tls-cert-check \
         sssd-ad-gpo-access-control \
         sssd-ad-gpo-ignore-unreadable \
         sssd-cache-credentials \
         autofs-browse-mode
do
        install -pD -m755 "controls/$i" \
                "%buildroot%_sysconfdir/control.d/facilities/$i"
done

mkdir -p "%buildroot%_datadir/%name"
cp -r policies/* "%buildroot%_datadir/%name"
mkdir -p "%buildroot%_sysconfdir/%name"

%pre
%_sbindir/groupadd -r -f remote 2> /dev/null ||:

%files
%dir %_sysconfdir/%name
%_sysconfdir/control.d/facilities/*
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Sat Jul 04 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.4.2-alt1
- Add sssd-ad-gpo-access-control control

* Wed Jul 01 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.4.1-alt1
- Add sssd-cache-credentials control
- Update sssd-ad-gpo-ignore-unreadable control

* Wed Jul 01 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.4.0-alt1
- Add autofs-browse-mode and sssd-ad-gpo-ignore-unreadable controls
- Open SSH port by default for all templates

* Tue Apr 21 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.3.0-alt1
- Replace machine local Registry policy in Samba backup format
- krb5-conf-ccache control added for Kerberos client default credential cache:
 + keyring: Keyring persistent cache stored in unswappable kernel memory
 + tmpfile: Traditional, simplest and most portable cache stored in temporary file
 + rundir: Directory cache stored in run-time variable data
 + kcm: Kerberos credential manager (requires service like sssd-kcm)
 + default: Default credential cache (usualy same as temporary file)
- Add ad-domain-controller policy template

* Thu Apr 16 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.2.0-alt4
- Add empty default local-policy

* Thu Apr 16 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.2.0-alt3
- Add local-policy sysconfig directory to package

* Thu Apr 16 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.2.0-alt2
- Add data directory to package
- Remove default symlink (it is a bad idea to pack it due rpm limitations)

* Mon Apr 13 2020 Igor Chudov <nir@altlinux.org> 0.2.0-alt1
- Multiple policy templates introduced

* Wed Feb 12 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt3
- Update project URL

* Fri Feb 07 2020 Ivan Savin <iv17@altlinux.org> 0.1.0-alt2
- Add gpupdate to local.xml

* Thu Nov 28 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt1
- Add default policies templates in PReg format converted to XML
- Change license to GPLv2+

* Fri Nov 08 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.0.5-alt1
- sshd-allow-groups-list added
- sshd-gssapi-auth: remove kill -HUP from control
- create group "remote" for sshd allow groups list policy

* Mon Oct 14 2019 Igor Chudov <nir@altlinux.org> 0.0.4-alt1
- ssh-gssapi-auth added
- Package made architecture-independent
- sshd-allow-gssapi renamed to sshd-gssapi-auth

* Thu Oct 10 2019 Igor Chudov <nir@altlinux.org> 0.0.3-alt1
- ldap-tls-cert-check control for 'tls_reqcert' option
- Build fixes

* Wed Oct 09 2019 Igor Chudov <nir@altlinux.org> 0.0.2-alt1
- ldap-reverse-dns-lookup control for 'sasl_nocanon' option of OpenLDAP

* Tue Sep 17 2019 Igor Chudov <nir@altlinux.org> 0.0.1-alt1
- Initial release with `sshd-allow-gssapi` script

