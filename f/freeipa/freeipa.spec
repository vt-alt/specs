# build defines
%define _unpackaged_files_terminate_build 1

%ifarch %ix86
%def_with only_client
%else
%def_without only_client
%endif

%if_without only_client
%def_with fastlint
%def_with fasttest
%def_with lint
%endif

%if_with lint
    %define linter_options --enable-pylint --with-jslint
%else
    %define linter_options --disable-pylint --without-jslint
%endif

# paths defines
%define _libexecdir /usr/libexec
%define plugin_dir %_libdir/dirsrv/plugins
%define _localstatedir %_var
%define _runtimedir /run
%define plugin_dir %_libdir/dirsrv/plugins
%define etc_systemd_dir %_sysconfdir/systemd/system

# versions defines
%define apache_version 2.4.41-alt3
%define bind_version 9.11
%define bind_dyndb_ldap_version 11.1-alt7
%define certmonger_version 0.79.7
%define ds_version 1.4.1.6
%define gssproxy_version 0.8.0-alt2
%define krb5_version 1.16.3
%define pki_version 10.7.3
%define python_ldap_version 3.2.0
%define samba_version 4.7.6
%define slapi_nis_version 0.56.3
%define sssd_version 1.16.3
%define openldap_version 2.4.47-alt2

Name: freeipa
Version: 4.8.6
Release: alt2

Summary: The Identity, Policy and Audit system
License: GPLv3+
Group: System/Base

Url: http://www.freeipa.org/
Source0: %name-%version.tar
Source1: freeipa-server.filetrigger
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: libcmocka-devel
BuildRequires: libini_config-devel
BuildRequires: libkrb5-devel >= %krb5_version
BuildRequires: libnss-devel
BuildRequires: libpopt-devel
BuildRequires: libsasl2-devel
BuildRequires: libssl-devel
BuildRequires: libxmlrpc-devel
BuildRequires: openldap-devel >= %openldap_version

%if_without only_client
BuildRequires(pre): rpm-macros-apache2

BuildRequires: libuuid-devel
BuildRequires: libsss_idmap-devel
BuildRequires: libsss_certmap-devel
BuildRequires: libsss_nss_idmap-devel >= %sssd_version
BuildRequires: libunistring-devel
BuildRequires: libsystemd-devel

BuildRequires: 389-ds-base-devel >= %ds_version
BuildRequires: samba-devel >= %samba_version
BuildRequires: node-uglify-js
%endif # only_client

# python
BuildRequires: python3-module-lesscpy
BuildRequires: python3-module-setuptools
#
# Build dependencies for makeapi/makeaci
#
BuildRequires: python3-module-cffi
BuildRequires: python3-module-dns
BuildRequires: python3-module-ldap >= %python_ldap_version
BuildRequires: python3-module-netaddr
BuildRequires: python3-module-pyasn1
BuildRequires: python3-module-pyasn1-modules
BuildRequires: python3-module-six
BuildRequires: python3-module-sss_nss_idmap

%if_with fasttest
BuildRequires: keyutils
BuildRequires: systemd
%endif

#
# Build dependencies for wheel packaging and PyPI upload
#
%if_with wheels
BuildRequires: python3(tox)
BuildRequires: python3(twine)
BuildRequires: python3(wheel)
%endif

#
# Build dependencies for lint and fastcheck
#
%if_with lint
BuildRequires: git-core
BuildRequires: softhsm
BuildRequires: jsl

BuildRequires: python3-module-augeas
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-custodia
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-dbus
BuildRequires: python3-module-dns
BuildRequires: python3-module-docker
BuildRequires: python3-module-gssapi
BuildRequires: python3-module-ipa_hbac
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-jwcrypto
BuildRequires: python3-module-ldap >= %python_ldap_version
BuildRequires: python3-module-lib389 >= %ds_version
BuildRequires: python3-module-lxml
BuildRequires: python3-module-netaddr
BuildRequires: python3-module-netifaces
BuildRequires: python3-module-paste
BuildRequires: python3-module-pki-base >= %pki_version
BuildRequires: python3-module-polib
BuildRequires: python3-module-pyasn1
BuildRequires: python3-module-pyasn1-modules
BuildRequires: python3-module-pycodestyle
BuildRequires: python3-module-pylint
BuildRequires: python3-module-pytest-multihost
BuildRequires: python3-module-pytest_sourceorder
BuildRequires: python3-module-qrcode
BuildRequires: python3-module-samba
BuildRequires: python3-module-sss
BuildRequires: python3-module-sss_nss_idmap
BuildRequires: python3-module-sss-murmur
BuildRequires: python3-module-sssdconfig >= %sssd_version
BuildRequires: python3-module-systemd
BuildRequires: python3-module-yubico

%endif

%description
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).

###############################################################################

%if_without only_client
%package server
Summary: The IPA authentication server
Group: System/Base
Requires: %name-client = %EVR
Requires: acl
Requires: gssproxy >= %gssproxy_version
Requires: sssd-dbus >= %sssd_version
Requires: selinux-policy-alt
Requires: pki-ca >= %pki_version
Requires: pki-kra >= %pki_version
Requires: certmonger >= %certmonger_version
Requires: 389-ds-base >= %ds_version
Requires: openssl
Requires: softhsm
Requires: libp11-kit
Requires: gzip
Requires: oddjob
Requires: 389-ds-base >= %ds_version
Requires: openldap-clients >= %openldap_version
Requires: nss-utils
Requires: krb5-kdc >= %krb5_version
Requires: libsasl2-plugin-gssapi
Requires: fonts-font-awesome
Requires: fonts-ttf-open-sans
Requires: apache2-mod_auth_gssapi
Requires: apache2-mod_ssl
Requires: apache2-mod_lookup_identity
Requires: apache2-mod_wsgi-py3
Requires: python3-module-ipaserver = %EVR
Requires: python3-module-ldap >= %python_ldap_version
Requires: python3-module-gssapi
Requires: python3-module-systemd
Requires: slapi-nis >= %slapi_nis_version

# upgrade path from monolithic -server to -server + -server-dns
Obsoletes: %name-server <= 4.2.0
# Versions of nss-pam-ldapd < 0.8.4 require a mapping from uniqueMember to
# member.
Conflicts: nss-ldapd < 0.8.4

%description server
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are installing an IPA server, you need to install this package.

###############################################################################

%package -n python3-module-ipaserver
Summary: Python libraries used by IPA server
Group: System/Libraries
Requires: %name-server-common = %EVR
Requires: python3-module-augeas
Requires: python3-module-gssapi
Requires: python3-module-ipaclient = %EVR
Requires: python3-module-kdcproxy
Requires: python3-module-ldap >= %python_ldap_version
Requires: python3-module-pki-base >= %pki_version
Requires: python3-module-sssdconfig >= %sssd_version
Requires: python3-module-samba
Requires: librpm
Obsoletes: python3-module-ipaserver-ntp < %EVR
Provides: python3-module-ipaserver-ntp = %EVR

%description -n python3-module-ipaserver
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are installing an IPA server, you need to install this package.

###############################################################################

%package server-common
Summary: Common files used by IPA server
Group: System/Base
Requires: %name-client-common = %EVR
Requires: apache2-base >= %apache_version
%add_python3_path %_datadir/ipa/
%add_python3_compile_exclude %_datadir/ipa/

%description server-common
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are installing an IPA server, you need to install this package.

###############################################################################

%package server-dns
Summary: IPA integrated DNS server with support for automatic DNSSEC signing
Group: System/Base
Requires: %name-server = %EVR
Requires: bind-dyndb-ldap >= %bind_dyndb_ldap_version
Requires: bind >= %bind_version
Requires: bind-utils >= %bind_version
Requires: opendnssec

# upgrade path from monolithic -server to -server + -server-dns
Obsoletes: %name-server <= 4.2.0

%description server-dns
IPA integrated DNS server with support for automatic DNSSEC signing.
Integrated DNS server is BIND 9. OpenDNSSEC provides key management.

###############################################################################

%package server-trust-ad
Summary: Virtual package to install packages required for Active Directory trusts
Group: System/Base
Requires: %name-server = %EVR
Requires: %name-common = %EVR

Requires: samba-dc-mitkrb5 >= %samba_version
Requires: samba-winbind

Requires: python3-module-samba
Requires: python3-module-sss_nss_idmap
Requires: python3-module-sss

%description server-trust-ad
Cross-realm trusts with Active Directory in IPA require working Samba 4
installation. This package is provided for convenience to install all required
dependencies at once.

%endif # only_client
###############################################################################

%package client
Summary: IPA authentication for use on clients
Group: System/Base
# Requires: authselect >= 0.4-2
Requires: libsasl2-plugin-gssapi
Requires: curl
Requires: sssd-krb5
Requires: sssd-ipa >= %sssd_version
Requires: sssd-tools >= %sssd_version
Requires: libsss_sudo
Requires: certmonger >= %certmonger_version
Requires: nss-utils
Requires: bind-utils
Requires: oddjob-mkhomedir
Requires: policycoreutils
Requires: python3-module-gssapi
Requires: python3-module-ipaclient = %EVR
Requires: python3-module-ldap >= %python_ldap_version
Requires: python3-module-sssdconfig >= %sssd_version

Obsoletes: %name-admintool < 4.4.1
Provides: %name-admintools = %EVR

%description client
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If your network uses IPA for authentication, this package should be
installed on every client machine.
This package provides command-line tools for IPA administrators.

###############################################################################

%package client-samba
Summary: Tools to configure Samba on IPA client
Group: System/Base
Requires: %name-client = %EVR
Requires: python3-module-samba
Requires: samba-client
Requires: samba-winbind
Requires: samba-common-tools
Requires: samba
Requires: sssd-winbind-idmap
Requires: tdb-utils
Requires: cifs-utils

%description client-samba
This package provides command-line tools to deploy Samba domain member
on the machine enrolled into a FreeIPA environment

###############################################################################

%package client-automount
Summary: IPA Automount for use on clients
Group: System/Base
Requires: %name-client = %EVR
Requires: autofs-sss
Requires: libsss_autofs
Requires: sssd-nfs-idmap
Requires: nfs-clients

%description client-automount
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If your network uses IPA for authentication and you would like to use
Automount, this package should be installed.

###############################################################################

%package -n python3-module-ipaclient
Summary: Python libraries used by IPA client
Group: System/Libraries
Requires: %name-client-common = %EVR
Requires: python3-module-freeipa = %EVR
Requires: python3-module-dns
Obsoletes: python3-module-ipaclient-ntp < %EVR
Provides: python3-module-ipaclient-ntp = %EVR

%description -n python3-module-ipaclient
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If your network uses IPA for authentication, this package should be
installed on every client machine.

###############################################################################

%package client-common
Summary: Common files used by IPA client
Group: System/Base
Requires: ca-trust

%description client-common
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If your network uses IPA for authentication, this package should be
installed on every client machine.

###############################################################################

%package -n python3-module-freeipa
Summary: Python3 libraries used by IPA
Group: System/Libraries
Requires: %name-common = %EVR
Requires: gnupg2
Requires: keyutils
Requires: less
Requires: krb5-kinit >= %krb5_version
Requires: python3-module-cffi
Requires: python3-module-ipa_hbac
Requires: python3-module-ldap >= %python_ldap_version
Requires: python3-module-pyusb
Requires: python3-module-qrcode
Requires: python3-module-requests
Requires: python3-module-sss-murmur
Requires: python3-module-yubico
%py3_provides ipaplatform
%py3_provides ipaplatform.constants
%py3_provides ipaplatform.osinfo
%py3_provides ipaplatform.paths
%py3_provides ipaplatform.services
%py3_provides ipaplatform.tasks
%py3_provides ipaplatform._importhook

%description -n python3-module-freeipa
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are using IPA with Python 3, you need to install this package.

###############################################################################

%package common
Summary: Common files used by IPA
Group: System/Libraries

%description common
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
If you are using IPA, you need to install this package.

###############################################################################

%package -n python3-module-ipatests
Summary: IPA tests and test tools
Group: System/Base
Requires: python3-module-ipaclient = %EVR
Requires: python3-module-ipaserver = %EVR
Requires: tar
Requires: xz
Requires: python3-module-coverage
Requires: python3-module-sssdconfig >= %sssd_version
Requires: openssh-clients
Requires: sshpass
Requires: iptables
# Tests have a huge amount useless Provides
%set_findprov_skiplist %python3_sitelibdir/ipatests/*

%description -n python3-module-ipatests
IPA is an integrated solution to provide centrally managed Identity (users,
hosts, services), Authentication (SSO, 2FA), and Authorization
(host access control, SELinux user roles, services). The solution provides
features for further integration with Linux based clients (SUDO, automount)
and integration with Active Directory based infrastructures (Trusts).
This package contains tests that verify IPA functionality under Python 3.

###############################################################################

%prep
%setup -n %name-%version
%if_with lint
# we need it to generate cumulative patch without context
# this patch includes changes made by sed too
git init
git config user.email "you@example.com"
git config user.name "Your Name"
git add .
git commit -m "upstream version"
git checkout -b "patch"
%endif # lint

%patch -p1
# change port from 8080 to 8090
# Port 8080 is used by alterator-ahttpd-server
grep -rl 8080 | xargs sed -i 's/\(\W\|^\)8080\(\W\|$\)/\18090\2/g'

%if_with lint
git add .
git commit -am 'with our changes'
%endif

%build

export PYTHON=%__python3
%autoreconf
%configure --with-vendor-suffix=-%release \
%if_without only_client
           --enable-server \
           --with-ipatests \
%else
           --disable-server \
           --without-ipatests \
%endif
           %linter_options
%make_build

%install
%makeinstall_std

# remove files which are useful only for make uninstall
find %buildroot -wholename '*/site-packages/*/install_files.txt' -exec rm {} \;

# since we package python modules as arch dependent
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

%find_lang ipa

%if_without only_client
# Remove .la files from libtool - we don't want to package these files
rm %buildroot/%plugin_dir/libipa_pwd_extop.la
rm %buildroot/%plugin_dir/libipa_enrollment_extop.la
rm %buildroot/%plugin_dir/libipa_winsync.la
rm %buildroot/%plugin_dir/libipa_repl_version.la
rm %buildroot/%plugin_dir/libipa_uuid.la
rm %buildroot/%plugin_dir/libipa_modrdn.la
rm %buildroot/%plugin_dir/libipa_lockout.la
rm %buildroot/%plugin_dir/libipa_cldap.la
rm %buildroot/%plugin_dir/libipa_dns.la
rm %buildroot/%plugin_dir/libipa_sidgen.la
rm %buildroot/%plugin_dir/libipa_sidgen_task.la
rm %buildroot/%plugin_dir/libipa_extdom_extop.la
rm %buildroot/%plugin_dir/libipa_range_check.la
rm %buildroot/%plugin_dir/libipa_otp_counter.la
rm %buildroot/%plugin_dir/libipa_otp_lasttoken.la
rm %buildroot/%plugin_dir/libtopology.la
rm %buildroot/%_libdir/krb5/plugins/kdb/ipadb.la
rm %buildroot/%_libdir/samba/pdb/ipasam.la

# So we can own our Apache configuration
mkdir -p %buildroot%apache2_confdir/{sites-available,extra-available,extra-enabled}
/bin/touch %buildroot%apache2_sites_available/ipa.conf
/bin/touch %buildroot%apache2_extra_enabled/{ipa-kdc-proxy.conf,ipa-pki-proxy.conf,ipa-rewrite.conf}
/bin/touch %buildroot%_datadir/ipa/html/{ca.crt,krb.con,krb5.ini,krbrealm.con}

mkdir -p %buildroot%etc_systemd_dir/httpd2.service.d
touch %buildroot%etc_systemd_dir/httpd2.service.d/ipa.conf

mkdir -p %buildroot%_sysconfdir/cron.d

mkdir -p %buildroot%_sysconfdir/bind
touch %buildroot%_sysconfdir/bind/ipa-ext.conf

mkdir -p %buildroot%_sharedstatedir/ipa/backup
mkdir -p %buildroot%_sharedstatedir/ipa/gssproxy
mkdir -p %buildroot%_sharedstatedir/ipa/sysrestore
mkdir -p %buildroot%_sharedstatedir/ipa/sysupgrade
mkdir -p %buildroot%_sharedstatedir/ipa/pki-ca
mkdir -p %buildroot%_sharedstatedir/ipa/certs
mkdir -p %buildroot%_sharedstatedir/ipa/private
mkdir -p %buildroot%_sharedstatedir/ipa/passwds
mkdir -p %buildroot%_sharedstatedir/bind/zone/dyndb-ldap
mkdir -p %buildroot%_sharedstatedir/bind/data
mkdir -p %buildroot%_sharedstatedir/bind/dynamic
touch %buildroot%_sharedstatedir/bind/zone/dyndb-ldap/ipa
touch %buildroot%_sharedstatedir/ipa/pki-ca/publish
touch %buildroot%_sysconfdir/ipa/kdcproxy/ipa-kdc-proxy.conf

mkdir -p %buildroot%_runtimedir
install -d -m 0700 %buildroot%_runtimedir/ipa
install -d -m 0700 %buildroot%_runtimedir/ipa/ccaches

# install filetrigger
mkdir -p %buildroot%_rpmlibdir
install -D -p -m 0755 %SOURCE1 %buildroot%_rpmlibdir/freeipa-server.filetrigger

# We use alternatives to divert winbind_krb5_locator.so plugin to libkrb5
# on the installes where server-trust-ad subpackage is installed because
# IPA AD trusts cannot be used at the same time with the locator plugin
# since Winbindd will be configured in a different mode
mkdir -p %buildroot%_altdir
printf '%_libdir/krb5/plugins/libkrb5/winbind_krb5_locator.so\t/dev/null\t90\n' > %buildroot%_altdir/winbind_krb5_locator.so

%endif # only_client

/bin/touch %buildroot%_sysconfdir/ipa/{default.conf,ca.crt}
# NSS
## new sql format
touch %buildroot%_sysconfdir/ipa/nssdb/pwdfile.txt
touch %buildroot%_sysconfdir/ipa/nssdb/cert9.db
touch %buildroot%_sysconfdir/ipa/nssdb/key4.db
touch %buildroot%_sysconfdir/ipa/nssdb/pkcs11.txt

mkdir -p %buildroot%_sysconfdir/pki/ca-trust/source
touch %buildroot%_sysconfdir/pki/ca-trust/source/ipa.p11-kit

mkdir -p %buildroot%_sharedstatedir/ipa-client
mkdir -p %buildroot%_sharedstatedir/ipa-client/pki
mkdir -p %buildroot%_sharedstatedir/ipa-client/sysrestore

%check
# run tests in upstream PR manner
%{?_with_fastlint:make "GIT_BRANCH=master" fastlint}
%{?_with_fasttest:make fasttest}
%{?_with_lint:make lint}
%make check VERBOSE=yes LIBDIR=%_libdir

%if_without only_client

%post server
/bin/systemctl daemon-reload 2>&1 ||:
# upgrade
if [ $1 -gt 1 ] ; then
    /bin/systemctl condrestart certmonger.service 2>&1 ||:
fi
/bin/systemctl try-reload-or-restart \
    dbus \
    oddjobd ||:

systemd-tmpfiles --create ipa.conf >/dev/null 2>&1 ||:

%preun server
# removal
if [ $1 -eq 0 ]; then
    /bin/systemctl -q --no-reload disable ipa.service ||:
    /bin/systemctl -q stop ipa.service ||:
    /bin/systemctl try-reload-or-restart \
        dbus \
        oddjobd ||:
fi

%pre server
# Stop ipa_kpasswd if it exists before upgrading so we don't have a
# zombie process when we're done.
if [ -e /usr/sbin/ipa_kpasswd ]; then
    /bin/systemctl stop ipa_kpasswd.service >/dev/null 2>&1 ||:
fi

%pre server-common
# create users and groups
# create kdcproxy group and user
getent group kdcproxy >/dev/null || groupadd -f -r kdcproxy ||:
getent passwd kdcproxy >/dev/null || useradd -r -g kdcproxy -s /sbin/nologin -d / -c "IPA KDC Proxy User" kdcproxy ||:
# create ipaapi group and user
getent group ipaapi >/dev/null || groupadd -f -r ipaapi ||:
getent passwd ipaapi >/dev/null || useradd -r -g ipaapi -s /sbin/nologin -d / -c "IPA Framework User" ipaapi ||:
# add apache to ipaaapi group
id -Gn apache2 | grep '\bipaapi\b' >/dev/null || usermod apache2 -a -G ipaapi ||:

%post server-dns
# first installation
if [ $1 -eq 1 ] ; then
    /bin/systemctl -q preset \
        ipa-dnskeysyncd \
        ipa-ods-exporter.socket \
        ipa-ods-exporter.service ||:
fi

%preun server-dns
# removal
# preun_service(P9) doesn't handle not *.service systemd names
if [ $1 -eq 0 ] ; then
    /bin/systemctl --no-reload disable --now \
        ipa-dnskeysyncd \
        ipa-ods-exporter.socket \
        ipa-ods-exporter.service ||:
fi

%post server-trust-ad
/bin/systemctl try-reload-or-restart \
    dbus \
    oddjobd ||:

%preun server-trust-ad
if [ $1 -eq 0 ]; then
    /bin/systemctl try-reload-or-restart \
        dbus \
        oddjobd ||:
fi
%endif # only_client

%post client
if [ $1 -gt 1 ] ; then
    # Has the client been configured?
    restore=0
    test -f '/var/lib/ipa-client/sysrestore/sysrestore.index' && restore=$(wc -l '/var/lib/ipa-client/sysrestore/sysrestore.index' | awk '{print $1}') ||:

    if [ -f '/etc/sssd/sssd.conf' -a $restore -ge 2 ]; then
        if ! grep -E -q '/var/lib/sss/pubconf/krb5.include.d/' /etc/krb5.conf  2>/dev/null ; then
            echo "includedir /var/lib/sss/pubconf/krb5.include.d/" > /etc/krb5.conf.ipanew
            cat /etc/krb5.conf >> /etc/krb5.conf.ipanew
            mv -Z /etc/krb5.conf.ipanew /etc/krb5.conf
        fi
    fi

    if [ $restore -ge 2 ]; then
        if grep -E -q '\s*pkinit_anchors = FILE:/etc/ipa/ca.crt$' /etc/krb5.conf 2>/dev/null; then
            sed -E 's|(\s*)pkinit_anchors = FILE:/etc/ipa/ca.crt$|\1pkinit_anchors = FILE:/var/lib/ipa-client/pki/kdc-ca-bundle.pem\n\1pkinit_pool = FILE:/var/lib/ipa-client/pki/ca-bundle.pem|' /etc/krb5.conf >/etc/krb5.conf.ipanew
            mv -Z /etc/krb5.conf.ipanew /etc/krb5.conf
            cp /etc/ipa/ca.crt /var/lib/ipa-client/pki/kdc-ca-bundle.pem
            cp /etc/ipa/ca.crt /var/lib/ipa-client/pki/ca-bundle.pem
        fi
        %__python3 -c 'from ipaclient.install.client import configure_krb5_snippet; configure_krb5_snippet()' >>/var/log/ipaupgrade.log 2>&1
    fi

    if [ $restore -ge 2 ]; then
        %__python3 -c 'from ipaclient.install.client import update_ipa_nssdb; update_ipa_nssdb()' >/var/log/ipaupgrade.log 2>&1
    fi

    if [ $restore -ge 2 ]; then
        sed -E --in-place=.orig 's/^(HostKeyAlgorithms ssh-rsa,ssh-dss)$/# disabled by ipa-client update\n# \1/' /etc/openssh/ssh_config
    fi
fi

%triggerin client -- openssh-server
# Has the client been configured?
restore=0
test -f '/var/lib/ipa-client/sysrestore/sysrestore.index' && restore=$(wc -l '/var/lib/ipa-client/sysrestore/sysrestore.index' | awk '{print $1}') ||:

if [ -f '/etc/openssh/sshd_config' -a $restore -ge 2 ]; then
    if grep -E -q '^(AuthorizedKeysCommand /usr/bin/sss_ssh_authorizedkeys|PubKeyAgent /usr/bin/sss_ssh_authorizedkeys %%u)$' /etc/openssh/sshd_config 2>/dev/null; then
        sed -r '
            /^(AuthorizedKeysCommand(User|RunAs)|PubKeyAgentRunAs)[ \t]/ d
        ' /etc/openssh/sshd_config >/etc/openssh/sshd_config.ipanew

        if /usr/sbin/sshd -t -f /dev/null -o 'AuthorizedKeysCommand=/usr/bin/sss_ssh_authorizedkeys' -o 'AuthorizedKeysCommandUser=nobody' 2>/dev/null; then
            sed -ri '
                s/^PubKeyAgent (.+) %%u$/AuthorizedKeysCommand \1/
                s/^AuthorizedKeysCommand .*$/\0\nAuthorizedKeysCommandUser nobody/
            ' /etc/openssh/sshd_config.ipanew
        elif /usr/sbin/sshd -t -f /dev/null -o 'AuthorizedKeysCommand=/usr/bin/sss_ssh_authorizedkeys' -o 'AuthorizedKeysCommandRunAs=nobody' 2>/dev/null; then
            sed -ri '
                s/^PubKeyAgent (.+) %%u$/AuthorizedKeysCommand \1/
                s/^AuthorizedKeysCommand .*$/\0\nAuthorizedKeysCommandRunAs nobody/
            ' /etc/openssh/sshd_config.ipanew
        elif /usr/sbin/sshd -t -f /dev/null -o 'PubKeyAgent=/usr/bin/sss_ssh_authorizedkeys %%u' -o 'PubKeyAgentRunAs=nobody' 2>/dev/null; then
            sed -ri '
                s/^AuthorizedKeysCommand (.+)$/PubKeyAgent \1 %%u/
                s/^PubKeyAgent .*$/\0\nPubKeyAgentRunAs nobody/
            ' /etc/openssh/sshd_config.ipanew
        fi

        mv -Z /etc/openssh/sshd_config.ipanew /etc/openssh/sshd_config
        chmod 600 /etc/openssh/sshd_config

        /bin/systemctl condrestart sshd.service 2>&1 ||:
    fi
fi

%if_without only_client
%files server
%_sbindir/ipa-backup
%_sbindir/ipa-restore
%_sbindir/ipa-ca-install
%_sbindir/ipa-kra-install
%_sbindir/ipa-server-install
%_sbindir/ipa-replica-conncheck
%_sbindir/ipa-replica-install
%_sbindir/ipa-replica-manage
%_sbindir/ipa-csreplica-manage
%_sbindir/ipa-server-certinstall
%_sbindir/ipa-server-upgrade
%_sbindir/ipa-ldap-updater
%_sbindir/ipa-otptoken-import
%_sbindir/ipa-compat-manage
%_sbindir/ipa-nis-manage
%_sbindir/ipa-managed-entries
%_sbindir/ipactl
%_sbindir/ipa-advise
%_sbindir/ipa-cacert-manage
%_sbindir/ipa-winsync-migrate
%_sbindir/ipa-pkinit-manage
%_sbindir/ipa-crlgen-manage
%_sbindir/ipa-cert-fix
%_libexecdir/certmonger/dogtag-ipa-ca-renew-agent-submit
%_libexecdir/certmonger/ipa-server-guard
%dir %_libexecdir/ipa
%_libexecdir/ipa/ipa-custodia
%_libexecdir/ipa/ipa-custodia-check
%_libexecdir/ipa/ipa-httpd-kdcproxy
%_libexecdir/ipa/ipa-httpd-pwdreader
%_libexecdir/ipa/ipa-pki-retrieve-key
%_libexecdir/ipa/ipa-pki-wait-running
%_libexecdir/ipa/ipa-otpd
%dir %_libexecdir/ipa/custodia
%attr(755,root,root) %_libexecdir/ipa/custodia/ipa-custodia-dmldap
%attr(755,root,root) %_libexecdir/ipa/custodia/ipa-custodia-pki-tomcat
%attr(755,root,root) %_libexecdir/ipa/custodia/ipa-custodia-pki-tomcat-wrapped
%attr(755,root,root) %_libexecdir/ipa/custodia/ipa-custodia-ra-agent
%dir %_libexecdir/ipa/oddjob
%attr(0755,root,root) %_libexecdir/ipa/oddjob/org.freeipa.server.conncheck
%attr(0755,root,root) %_libexecdir/ipa/oddjob/org.freeipa.server.trust-enable-agent
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.freeipa.server.conf
%config(noreplace) %_sysconfdir/oddjobd.conf.d/ipa-server.conf
%dir %_libexecdir/ipa/certmonger
%attr(755,root,root) %_libexecdir/ipa/certmonger/*
# NOTE: systemd specific section
%attr(644,root,root) %_unitdir/ipa.service
%attr(644,root,root) %_unitdir/ipa-otpd.socket
%attr(644,root,root) %_unitdir/ipa-otpd@.service
# END
%attr(755,root,root) %plugin_dir/libipa_pwd_extop.so
%attr(755,root,root) %plugin_dir/libipa_enrollment_extop.so
%attr(755,root,root) %plugin_dir/libipa_winsync.so
%attr(755,root,root) %plugin_dir/libipa_repl_version.so
%attr(755,root,root) %plugin_dir/libipa_uuid.so
%attr(755,root,root) %plugin_dir/libipa_modrdn.so
%attr(755,root,root) %plugin_dir/libipa_lockout.so
%attr(755,root,root) %plugin_dir/libipa_cldap.so
%attr(755,root,root) %plugin_dir/libipa_dns.so
%attr(755,root,root) %plugin_dir/libipa_range_check.so
%attr(755,root,root) %plugin_dir/libipa_otp_counter.so
%attr(755,root,root) %plugin_dir/libipa_otp_lasttoken.so
%attr(755,root,root) %plugin_dir/libtopology.so
%attr(755,root,root) %plugin_dir/libipa_sidgen.so
%attr(755,root,root) %plugin_dir/libipa_sidgen_task.so
%attr(755,root,root) %plugin_dir/libipa_extdom_extop.so
%attr(755,root,root) %_libdir/krb5/plugins/kdb/ipadb.so
%_man1dir/ipa-replica-conncheck.1*
%_man1dir/ipa-replica-install.1*
%_man1dir/ipa-replica-manage.1*
%_man1dir/ipa-csreplica-manage.1*
%_man1dir/ipa-server-certinstall.1*
%_man1dir/ipa-server-install.1*
%_man1dir/ipa-server-upgrade.1*
%_man1dir/ipa-ca-install.1*
%_man1dir/ipa-kra-install.1*
%_man1dir/ipa-compat-manage.1*
%_man1dir/ipa-nis-manage.1*
%_man1dir/ipa-managed-entries.1*
%_man1dir/ipa-ldap-updater.1*
%_man1dir/ipa-backup.1*
%_man1dir/ipa-restore.1*
%_man1dir/ipa-advise.1*
%_man1dir/ipa-otptoken-import.1*
%_man1dir/ipa-cacert-manage.1*
%_man1dir/ipa-winsync-migrate.1*
%_man1dir/ipa-pkinit-manage.1*
%_man1dir/ipa-crlgen-manage.1*
%_man1dir/ipa-cert-fix.1*
%_man8dir/ipactl.8*

%_rpmlibdir/freeipa-server.filetrigger

%files -n python3-module-ipaserver
%python3_sitelibdir/ipaserver/
%python3_sitelibdir/ipaserver-*.egg-info/

%files server-common
%dir %attr(0700,root,root) %_runtimedir/ipa
%dir %attr(0700,root,root) %_runtimedir/ipa/ccaches
%dir %attr(0755,root,root) %_sysconfdir/ipa/kdcproxy
%config(noreplace) %_sysconfdir/ipa/kdcproxy/kdcproxy.conf
/lib/tmpfiles.d/ipa.conf
%attr(644,root,root) %_unitdir/ipa-custodia.service
%ghost %attr(644,root,root) %etc_systemd_dir/httpd2.service.d/ipa.conf
%_datadir/ipa/wsgi.py
%_datadir/ipa/kdcproxy.wsgi
%_datadir/ipa/ipaca*.ini
%_datadir/ipa/*.ldif
%_datadir/ipa/*.uldif
%_datadir/ipa/*.template
%_datadir/ipa/bind.ipa-ext.conf
%_datadir/ipa/advise/
%_datadir/ipa/profiles/
%dir %_datadir/ipa/html
%_datadir/ipa/html/*.html
%_datadir/ipa/migration/
%_datadir/ipa/ui/
%_datadir/ipa/wsgi/
%dir %_sysconfdir/ipa
%dir %_sysconfdir/ipa/html
%config(noreplace) %_sysconfdir/ipa/html/ssbrowser.html
%config(noreplace) %_sysconfdir/ipa/html/unauthorized.html
%ghost %attr(0644,root,root) %config(noreplace) %apache2_sites_available/ipa.conf
%ghost %attr(0644,root,root) %config(noreplace) %apache2_extra_enabled/ipa-rewrite.conf
%ghost %attr(0644,root,root) %config(noreplace) %apache2_extra_enabled/ipa-kdc-proxy.conf
%ghost %attr(0640,root,root) %config(noreplace) %apache2_extra_enabled/ipa-pki-proxy.conf
%ghost %attr(0644,root,root) %config(noreplace) %_sysconfdir/ipa/kdcproxy/ipa-kdc-proxy.conf
%ghost %attr(0644,root,root) %config(noreplace) %_datadir/ipa/html/ca.crt
%ghost %attr(0640,root,named) %config(noreplace) %_sysconfdir/bind/ipa-ext.conf
%ghost %attr(0644,root,root) %_datadir/ipa/html/krb.con
%ghost %attr(0644,root,root) %_datadir/ipa/html/krb5.ini
%ghost %attr(0644,root,root) %_datadir/ipa/html/krbrealm.con
%dir %_datadir/ipa/updates/
%_datadir/ipa/updates/*
%dir %_sharedstatedir/ipa
%attr(700,root,root) %dir %_sharedstatedir/ipa/backup
%ghost %attr(770,root,_gssproxy) %dir %_sharedstatedir/ipa/gssproxy
%attr(711,root,root) %dir %_sharedstatedir/ipa/sysrestore
%attr(700,root,root) %dir %_sharedstatedir/ipa/sysupgrade
%attr(755,root,root) %dir %_sharedstatedir/ipa/pki-ca
%attr(755,root,root) %dir %_sharedstatedir/ipa/certs
%attr(700,root,root) %dir %_sharedstatedir/ipa/private
%attr(700,root,root) %dir %_sharedstatedir/ipa/passwds
%attr(770,root,named) %dir %_sharedstatedir/bind/data
%attr(770,root,named) %dir %_sharedstatedir/bind/dynamic
%ghost %attr(775,root,pkiuser) %_sharedstatedir/ipa/pki-ca/publish
%ghost %attr(770,named,named) %_sharedstatedir/bind/zone/dyndb-ldap/ipa

%dir %attr(0700,root,root) %_sysconfdir/ipa/custodia
%dir %_datadir/ipa/schema.d
%attr(0644,root,root) %_datadir/ipa/schema.d/README
%attr(0644,root,root) %_datadir/ipa/gssapi.login
%_datadir/ipa/ipakrb5.aug

%files server-dns
%config(noreplace) %_sysconfdir/sysconfig/ipa-dnskeysyncd
%config(noreplace) %_sysconfdir/sysconfig/ipa-ods-exporter
%dir %attr(0755,root,root) %_sysconfdir/ipa/dnssec
%_libexecdir/ipa/ipa-dnskeysyncd
%_libexecdir/ipa/ipa-dnskeysync-replica
%_libexecdir/ipa/ipa-ods-exporter
%_man1dir/ipa-dns-install.1*
%_sbindir/ipa-dns-install
%attr(644,root,root) %_unitdir/ipa-dnskeysyncd.service
%attr(644,root,root) %_unitdir/ipa-ods-exporter.socket
%attr(644,root,root) %_unitdir/ipa-ods-exporter.service

%files server-trust-ad
%_sbindir/ipa-adtrust-install
%_datadir/ipa/smb.conf.empty
%attr(755,root,root) %_libdir/samba/pdb/ipasam.so
%_man1dir/ipa-adtrust-install.1*
%_sysconfdir/dbus-1/system.d/oddjob-ipa-trust.conf
%_sysconfdir/oddjobd.conf.d/oddjobd-ipa-trust.conf
%_libexecdir/ipa/oddjob/com.redhat.idm.trust-fetch-domains
%_altdir/winbind_krb5_locator.so

%files -n python3-module-ipatests
%python3_sitelibdir/ipatests/
%python3_sitelibdir/ipatests-*.egg-info
%_bindir/ipa-run-tests
%_bindir/ipa-test-config
%_bindir/ipa-test-task
%_man1dir/ipa-run-tests.1*
%_man1dir/ipa-test-config.1*
%_man1dir/ipa-test-task.1*

%endif # only_client

%files client
%_sbindir/ipa-client-install
%_sbindir/ipa-certupdate
%_sbindir/ipa-getkeytab
%_sbindir/ipa-rmkeytab
%_sbindir/ipa-join
%_bindir/ipa
%config %_sysconfdir/bash_completion.d
%config %_sysconfdir/sysconfig/certmonger
%_mandir/man1/ipa.1*
%_mandir/man1/ipa-getkeytab.1*
%_mandir/man1/ipa-rmkeytab.1*
%_mandir/man1/ipa-client-install.1*
%_mandir/man1/ipa-certupdate.1*
%_mandir/man1/ipa-join.1*

%files client-samba
%_sbindir/ipa-client-samba
%_man1dir/ipa-client-samba.1*

%files client-automount
%_sbindir/ipa-client-automount
%_mandir/man1/ipa-client-automount.1*
%python3_sitelibdir/ipaclient/install/ipa_client_automount.py

%files -n python3-module-ipaclient
%python3_sitelibdir/ipaclient/
%exclude %python3_sitelibdir/ipaclient/install/ipa_client_automount.py
%python3_sitelibdir/ipaclient-*.egg-info/

%files client-common
%dir %attr(0755,root,root) %_sysconfdir/ipa/
%ghost %attr(0644,root,root) %config(noreplace) %_sysconfdir/ipa/default.conf
%ghost %attr(0644,root,root) %config(noreplace) %_sysconfdir/ipa/ca.crt
%dir %attr(0755,root,root) %_sysconfdir/ipa/nssdb
# new sql format
%ghost %attr(644,root,root) %config(noreplace) %_sysconfdir/ipa/nssdb/cert9.db
%ghost %attr(644,root,root) %config(noreplace) %_sysconfdir/ipa/nssdb/key4.db
%ghost %attr(644,root,root) %config(noreplace) %_sysconfdir/ipa/nssdb/pkcs11.txt
%ghost %attr(600,root,root) %config(noreplace) %_sysconfdir/ipa/nssdb/pwdfile.txt
%ghost %attr(644,root,root) %config(noreplace) %_sysconfdir/pki/ca-trust/source/ipa.p11-kit
%dir %_sharedstatedir/ipa-client
%dir %_sharedstatedir/ipa-client/pki
%dir %_sharedstatedir/ipa-client/sysrestore
%_man5dir/default.conf.5*
%dir %_datadir/ipa/client
%_datadir/ipa/client/*.template

%files common -f ipa.lang
%doc COPYING README.md Contributors.txt
%dir %_datadir/ipa

%files -n python3-module-freeipa
%python3_sitelibdir/ipapython/
%python3_sitelibdir/ipalib/
%python3_sitelibdir/ipaplatform/
%python3_sitelibdir/ipapython-*.egg-info/
%python3_sitelibdir/ipalib-*.egg-info/
%python3_sitelibdir/ipaplatform-*.egg-info/
%python3_sitelibdir/ipaplatform-*-nspkg.pth

%changelog
* Fri Jun 05 2020 Stanislav Levin <slev@altlinux.org> 4.8.6-alt2
- Applied upstream fixes.

* Tue Apr 07 2020 Stanislav Levin <slev@altlinux.org> 4.8.6-alt1
- 4.7.4 -> 4.8.6.

* Thu Feb 06 2020 Evgeny Sinelnikov <sin@altlinux.org> 4.7.4-alt3
- Fixed compatibility with Samba 4.11
- Backported fix Pylint with python3: Remove subclassing from object

* Mon Dec 16 2019 Stanislav Levin <slev@altlinux.org> 4.7.4-alt2
- Fixed automount NFS share.
- Fixed trust creation.

* Tue Nov 26 2019 Stanislav Levin <slev@altlinux.org> 4.7.4-alt1
- 4.7.3 -> 4.7.4 (fixes: CVE-2019-14867, CVE-2019-10195).

* Fri Sep 20 2019 Stanislav Levin <slev@altlinux.org> 4.7.3-alt1
- 4.7.2 -> 4.7.3.

* Mon Aug 26 2019 Stanislav Levin <slev@altlinux.org> 4.7.2-alt4
- ALT: Fixed upgrade 4.3.3 -> 4.7.2.

* Mon Jul 15 2019 Stanislav Levin <slev@altlinux.org> 4.7.2-alt3
- Added support for CI testing (ALT).

* Mon May 27 2019 Stanislav Levin <slev@altlinux.org> 4.7.2-alt2
- Fixed `without_lint` build.
- Fixed replica install.

* Wed May 01 2019 Stanislav Levin <slev@altlinux.org> 4.7.2-alt1
- 4.7.1 -> 4.7.2.
- Enabled smoke tests.
- Backported upstream patches for 389-ds 1.4.1.2.

* Wed Apr 03 2019 Evgeny Sinelnikov <sin@altlinux.org> 4.7.1-alt8
- Backport patch for samba-4.10.0 complatibility from upstream

* Tue Mar 26 2019 Evgeny Sinelnikov <sin@altlinux.org> 4.7.1-alt7
- Rebuild with samba-4.10.0 (freeipa-server-trust-ad depens on libsmbconf.so.0)

* Fri Feb 08 2019 Stanislav Levin <slev@altlinux.org> 4.7.1-alt6
- Fixed work with new 389-ds (1.4.x).

* Fri Dec 28 2018 Stanislav Levin <slev@altlinux.org> 4.7.1-alt5
- Fixed support for gssproxy non-privileged user.
- Fixed support for Automount NFS.
- Dropped build of freeipa-server for i586.

* Tue Dec 04 2018 Stanislav Levin <slev@altlinux.org> 4.7.1-alt4
- Drop Requires on selinux-policy (closes: #35686).

* Wed Oct 24 2018 Stanislav Levin <slev@altlinux.org> 4.7.1-alt3
- Added support for separated IPA plugins.

* Mon Oct 15 2018 Stanislav Levin <slev@altlinux.org> 4.7.1-alt2
- Fixed client upgrade from 4.6 to 4.7.

* Tue Oct 09 2018 Stanislav Levin <slev@altlinux.org> 4.7.1-alt1
- 4.7.0 -> 4.7.1.

* Mon Oct 01 2018 Stanislav Levin <slev@altlinux.org> 4.7.0-alt2
- Fixed client's requirements to server modules (by mrdrew@).
- Fixed JS errors on web pages(ssbrowser and unauthorized) at production mode.

* Fri Sep 07 2018 Stanislav Levin <slev@altlinux.org> 4.7.0-alt1
- 4.6.3 -> 4.7.0.

* Wed Sep 05 2018 Stanislav Levin <slev@altlinux.org> 4.6.3-alt8
- Build with new softhsm.

* Fri Aug 31 2018 Stanislav Levin <slev@altlinux.org> 4.6.3-alt7
- Build with new openssl1.1.

* Fri Jun 29 2018 Ivan Zakharyaschev <imz@altlinux.org> 4.6.3-alt6
- Improved formal deps (in python*-module-freeipa, dropped the
  unnecessary explicit dep on setuptools in favor of autoreqs) so that
  there is more flexibility in the base system where freeipa can be
  installed (i.e., gcc won't be required since the split of
  python*-module-setuptools-1:39.2.0-alt3).

* Tue Apr 03 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.6.3-alt5
- Rebuilt due to selinux update.

* Sat Mar 24 2018 Evgeny Sinelnikov <sin@altlinux.org> 4.6.3-alt4
- Rebuild with samba-4.7

* Wed Mar 14 2018 Stanislav Levin <slev@altlinux.org> 4.6.3-alt3
- Fix WebUI translations
- Fix upgrade process

* Mon Feb 19 2018 Stanislav Levin <slev@altlinux.org> 4.6.3-alt2
- Fix applying of ipa rewrite rules

* Tue Feb 13 2018 Stanislav Levin <slev@altlinux.org> 4.6.3-alt1
- v4.6.2 -> v4.6.3

* Wed Jan 31 2018 Stanislav Levin <slev@altlinux.org> 4.6.2-alt2
- Fix build against krb5-1.16 (new KDB DAL version 7.0)

* Fri Jan 19 2018 Stanislav Levin <slev@altlinux.org> 4.6.2-alt1
- 4.6.1 -> 4.6.2

* Mon Dec 25 2017 Stanislav Levin <slev@altlinux.org> 4.6.1-alt3
- Fix ipa-cacert-manage renew scenario

* Tue Dec 12 2017 Stanislav Levin <slev@altlinux.org> 4.6.1-alt2
- Add openntpd support (based on patches from Mikhail Efremov) (closes: #34307)
- Save and restore state of apache modules during installation/uninstallation

* Sat Oct 07 2017 Stanislav Levin <slev@altlinux.org> 4.6.1-alt1
- 4.4.4 -> 4.6.1

* Thu Oct 06 2017 Stanislav Levin <slev@altlinux.org> 4.4.4-alt4
- Fix ipa client schema cache: Handle malformed server info data gracefully
- Fix ipa client requirements
- Import patches from 4.3.3-alt9

* Thu Oct 05 2017 Mikhail Efremov <sem@altlinux.org> 4.3.3-alt9
- selinux: Allow digits in SELinux user names (closes: #33838).
- Require zip.

* Thu Oct 4 2017 Stanislav Levin <slev@altlinux.org> 4.4.4-alt3
- Fix ipa server upgrade

* Thu Oct 2 2017 Stanislav Levin <slev@altlinux.org> 4.4.4-alt2
- Import patches from 4.3.3-alt8

* Wed Sep 27 2017 Mikhail Efremov <sem@altlinux.org> 4.3.3-alt8
- Fix replica creation (closes: #33513):
    + Don't try to use bundled urllib3 in the python-module-request.
    + Use ipa CA certificate for https checks.

* Thu Sep 25 2017 Stanislav Levin <slev@altlinux.org> 4.4.4-alt1
- Update to upstream's 4.4.4 version

* Thu Aug 24 2017 Mikhail Efremov <sem@altlinux.org> 4.3.3-alt7
- httpd2: Update existing ipa.conf for fontawesome path.

* Wed Aug 23 2017 Mikhail Efremov <sem@altlinux.org> 4.3.3-alt6
- Requires: fonts-ttf-fontawesome-web -> fonts-font-awesome.
- Change paths to fontawesome.

* Mon Aug 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3.3-alt5
- Enabled tests.

* Thu Aug 10 2017 Mikhail Efremov <sem@altlinux.org> 4.3.3-alt4
- Add %%apache_conf_dir macro.
- Move ipa_configured script to server-common subpackage.
- Init argument for slapi_pblock_get() (closes: #33538).
- Fix httpd2 configuration (closes: #33513, #33466).

* Tue May 16 2017 Mikhail Efremov <sem@altlinux.org> 4.3.3-alt3
- server: Require pki-kra.
- Run ipa-server-upgrade at package update.
- Add ipa_configured script.
- Fix ipa-server-upgrade (closes: #33463).
- Set JAVA_STACK_SIZE to 8m.

* Wed Apr 26 2017 Mikhail Efremov <sem@altlinux.org> 4.3.3-alt2
- Fix build with 389-ds-1.3.6.4.

* Fri Apr 21 2017 Mikhail Efremov <sem@altlinux.org> 4.3.3-alt1
- client: Require bind-utils.
- client: Require krb5-kinit.
- Updated to 4.3.3.

* Tue Feb 28 2017 Mikhail Efremov <sem@altlinux.org> 4.3.2-alt9
- Fix chown krb5.keytab.

* Tue Feb 28 2017 Mikhail Efremov <sem@altlinux.org> 4.3.2-alt8
- Use ALT-specific SELinux users.
- Grant read access to krb5.keytab file for _keytab group.
- ipaclient: Reduce ntpdate timeout.
- client: Require ntpdate.

* Wed Feb 15 2017 Mikhail Efremov <sem@altlinux.org> 4.3.2-alt7
- Explicitly require python-module-samba.
- Fixed %%_runtimedir/ipa_memcached permissions.
- server-trust-ad: Require samba and samba-winbind (closes: #33084).
- openntpd support.
- Change dogtag default insecure port to 8090.
- client: Require libsss_sudo.

* Mon Jan 23 2017 Mikhail Efremov <sem@altlinux.org> 4.3.2-alt6
- client: Require nss-utils (closes: #33031).
- Patches from upstream:
  + Fixed CVE-2016-7030.
  + Fixed CVE-2016-9575.

* Mon Jan 16 2017 Mikhail Efremov <sem@altlinux.org> 4.3.2-alt5
- bindinstance: Drop 'generating rndc key' step.
- bindinstance: Use resolvconf if needed.
- tasks: Implement {set/restore}_control_state() functions.
- Disable bind chroot and fix paths in configs.
- altlinux/tasks.py: Implement check_selinux_status().
- ipa-client-automount: Configure nsswitch.conf for sssd.
- Configure nsswitch.conf for use sssd.
- Require ntpd in the client subpackage.

* Wed Dec 28 2016 Mikhail Efremov <sem@altlinux.org> 4.3.2-alt4
- Move some requires to client subpackage (closes: #32952).
- Require slapi-nis.
- Require fonts for web ui.
- web ui: Fix fonts.
- Use bash as default login shell.
- Update server-dns description.
- Disable DNSSEC support for now.
- Require openssl.
- Fix opendnssec paths.
- Update named.conf and paths.
- Increase httpd.service start timeout.
- Enable/disable apache2 modules/configs.
- Enable dyndb-ldap.

* Fri Nov 25 2016 Mikhail Efremov <sem@altlinux.org> 4.3.2-alt3
- Require java-1.8.0-openjdk.
- Require pki.
- Drop hack for old certmonger.

* Thu Nov 10 2016 Mikhail Efremov <sem@altlinux.org> 4.3.2-alt2
- Merge spec with Fedora.

* Tue Nov 08 2016 Mikhail Efremov <sem@altlinux.org> 4.3.2-alt1
- Patch from upstream:
    + ipa-kdb: Allow to build with samba 4.5
- Update spec.
- ipa-client-install: Hack for old certmonger.
- Fix opendnssec user/group.
- Disable dyndb-ldap stuff for now.
- Fix httpd2 confs paths.
- Fix user for ipa_memcached.
- Fix NSSCertificateDatabase path.
- ipa.conf: Fix paths.
- Add nss.conf.
- constants: Fix apache user name.
- Fix apache user name for oddjobd.
- Fix path to custodia socket.
- Hack bind configuration for now.
- Fix ipa.conf.
- Fix httpd.service.
- Add initial ALT Linux platform support.
- Updated to 4.3.2.

* Wed May 04 2016 Mikhail Efremov <sem@altlinux.org> 4.3.1-alt1
- Updated to 4.3.1.

* Fri Nov 20 2015 Mikhail Efremov <sem@altlinux.org> 4.2.3-alt1
- Updated to 4.2.3.

* Mon Apr 28 2014 Timur Aitov <timonbl4@altlinux.org> 3.3.5-alt1
- new version

* Wed Mar 26 2014 Timur Aitov <timonbl4@altlinux.org> 3.3.4-alt1
- first build for alt

* Fri Oct 25 2013 Martin Kosek <mkosek@redhat.com> - 3.3.2-1
- Remove mod_ssl conflict, it can now live with mod_nss installed

* Wed Sep 4 2013 Ana Krivokapic <akrivoka@redhat.com> - 3.3.0-3
- Conform to tmpfiles.d packaging guidelines

* Wed Aug 28 2013 Petr Viktorin <pviktori@redhat.com> - 3.3.0-2
- Add man pages to the tests subpackage

* Mon Aug 12 2013 Petr Viktorin <pviktori@redhat.com> - 3.3.0-1
- Downgrade required version of python-paramiko for the tests subpackage

* Thu Aug 8 2013 Martin Kosek <mkosek@redhat.com> - 3.2.99-13
- Require slapi-nis 0.47.7 and sssd 1.11.0-0.1.beta2 required for core
  features of 3.3.0 release

* Fri Jul 26 2013 Martin Kosek <mkosek@redhat.com> - 3.2.99-12
- Require pki-ca 10.0.4 which fixes external CA installation (#986901)

* Wed Jul 24 2013 Petr Viktorin <pviktori@redhat.com> - 3.2.99-11
- Add tar and xz dependencies to freeipa-tests

* Wed Jul 24 2013 Tomas Babej <tbabej@redhat.com> - 3.2.99-10
- Move requirement for keyutils from freeipa-server to freeipa-python

* Wed Jul 24 2013 Martin Kosek <mkosek@redhat.com> - 3.2.99-9
- Bump minimum version of sssd to 1.10.92 to pick up latest SSSD 1.11 Beta
  development

* Thu Jul 18 2013 Ana Krivokapic <akrivoka@redhat.com> - 3.2.99-8
- Bump minimum version of sssd to 1.10.90 for the 'ipa_server_mode' option.

* Wed Jul 17 2013 Martin Kosek <mkosek@redhat.com> - 3.2.99-7
- Require selinux-policy 3.12.1-65 containing missing policy after removal of
  freeipa-server-selinux subpackage

* Tue Jul 16 2013 Tomas Babej <tbabej@redhat.com> - 3.2.99-6
- Do not create /var/lib/ipa/pki-ca/publish, retain reference as ghost

* Thu Jul 11 2013 Martin Kosek <mkosek@redhat.com> - 3.2.99-5
- Run ipa-upgradeconfig and server restart in posttrans to avoid inconsistency
  issues when there are still old parts of software (like entitlements plugin)

* Wed Jul 10 2013 Ana Krivokapic <akrivoka@redhat.com> - 3.2.99-4
- Bump minimum version of 389-ds-base to 1.3.1.3 for user password change fix.

* Wed Jun 26 2013 Jan Cholasta <jcholast@redhat.com> - 3.2.99-3
- Bump minimum version of 389-ds-base to 1.3.1.1 for SASL mapping priority
  support.

* Mon Jun 17 2013 Petr Viktorin <pviktori@redhat.com> - 3.2.99-2
- Add the freeipa-tests subpackage

* Thu Jun 13 2013 Martin Kosek <mkosek@redhat.com> - 3.2.99-1
- Drop freeipa-server-selinux subpackage
- Drop redundant directory /var/cache/ipa/sessions

* Fri May 10 2013 Martin Kosek <mkosek@redhat.com> - 3.1.99-13
- Add requires for openldap-2.4.35-4 to pickup fixed SASL_NOCANON behavior for
  socket based connections (#960222)

* Tue May  7 2013 Petr Viktorin <pviktori@redhat.com> - 3.1.99-12
- Require libsss_nss_idmap-python in Fedora 19+

* Mon May  6 2013 Petr Vobornik <pvoborni@redhat.com> - 3.1.99-11
- Web UI plugins

* Fri May  3 2013 Rob Crittenden <rcritten@redhat.com> - 3.1.99-10
- Require pki-ca 10.0.2 for 501 response code on find for d9 -> d10 upgrades

* Tue Apr 30 2013 Rob Crittenden <rcritten@redhat.com> - 3.1.99-9
- Add Conflicts on nss-pam-ldapd < 0.8.4. The mapping from uniqueMember to
  member is now done automatically and having it in the config file raises
  an error.

* Tue Apr 30 2013 Jan Cholasta <jcholast@redhat.com> - 3.1.99-8
- Add triggerin scriptlet to update sshd_config on openssh-server update

* Thu Apr 25 2013 Rob Crittenden <rcritten@redhat.com> - 3.1.99-7
- Update nss and nss-tools dependency to fix certutil problem (#872761)

* Mon Apr 15 2013 Martin Kosek <mkosek@redhat.com> - 3.1.99-6
- Require samba 4.0.5, includes new passdb API
- Require krb5 1.11.2-1, fixes missing PAC issue
- Change permissions on backup dir to 700

* Fri Apr  5 2013 Rob Crittenden <rcritten@redhat.com> - 3.1.99-5
- Add backup and restore
- Own /var/lib/ipa/backup

* Thu Apr  4 2013 Alexander Bokovoy <abokovoy@redhat.com> - 3.1.99-4
- Make sure build against Krb5 1.11 in Fedora 18 environment creates proper dependencies

* Tue Apr  2 2013 Martin Kosek <mkosek@redhat.com> - 3.1.99-3
- Require 389-base-base >= 1.3.0.5 to pull the following fixes:
- upgrade deadlock caused by DNA plugin reconfiguration
- CVE-2013-1897: unintended information exposure when
  nsslapd-allow-anonymous-access is set to rootdse

* Wed Mar 27 2013 Martin Kosek <mkosek@redhat.com> - 3.1.99-2
- Remove conflict with krb5-server > 1.11 as ipa-kdb is compatible
- ipa-ldap-updater show produce errors only
- update policycoreutils version to 2.1.12-5 to match Requires in Fedora
- require at least systemd 38 which provides the journal (we no longer
  need to require syslog.target)

* Thu Mar 21 2013 Martin Kosek <mkosek@redhat.com> - 3.1.99-1
- Require selinux-policy 3.11.1-86 to fix Fedora 17 to 18 upgrade issue

* Tue Jan 29 2013 Petr Viktorin <pviktori@redhat.com> - 3.0.99-14
- Use ipa-ldap-updater --quiet instead of redirecting to /dev/null

* Tue Jan 29 2013 Rob Crittenden <rcritten@redhat.com> - 3.0.99-13
- Set certmonger minimum version to 0.65 for NSS locking during
  renewal
- Set selinux-policy to 3.11.1-73 so certmonger can run in post
  scriptlet

* Thu Jan 24 2013 Rob Crittenden <rcritten@redhat.com> - 3.0.99-12
- Add certmonger condrestart to server post scriptlet
- Make certmonger a (pre) Requires on the server subpackage

* Tue Jan 22 2013 Petr Vobornik <pvoborni@redhat.com> - 3.0.99-11
- dependency fix
- Add BuildRequires: java-1.7.0-openjdk.
- Removed BuildRequires: rhino

* Fri Jan 18 2013 Petr Vobornik <pvoborni@redhat.com> - 3.0.99-10
- Add Web UI layer JS files in ui/js/{dojo,freeipa,libs} directories
- Add BuildRequires: rhino

* Fri Dec 7 2012 Endi S. Dewata <edewata@redhat.com> - 3.0.99-9
- Bump minimum version of pki-ca to 10.0.0-0.54.b3

* Fri Dec 7 2012 Martin Kosek <mkosek@redhat.com> - 3.0.99-8
- Bump minimum version of 389-ds-base to 1.3.0 to get transaction support

* Thu Dec  6 2012 Rob Crittenden <rcritten@redhat.com> - 3.0.99-7
- Set min for selinux-policy to 3.11.1-60 to fix errors including sssd
  domain mapping in krb5.conf (#873429)

* Wed Nov 21 2012 Alexander Bokovoy <abokovoy@redhat.com> - 3.0.99-6
- Replace python-crypto by m2crypto dependency

* Fri Nov 16 2012 Rob Crittenden <rcritten@redhat.com> - 3.0.99-5
- Bump minimum version of slapi-nis to 0.44

* Wed Nov 14 2012 Martin Kosek <mkosek@redhat.com> - 3.0.99-4
- Remove compatibility definitions for unsupported Fedora versions (Fedora 16 and lower)
  - Do not require specific package version when the package was available in Fedora 17
  - Remove old SysV initscript compatibility code - we run on systemd now
- Add Requires for the new Dogtag 10 and dogtag-pki-server-theme
- Remove Requires on tomcat6 for Fedora 18 and later, Dogtag 10 pulls tomcat7 itself
- Add Requires for tar (used by ipa-replica-prepare)

* Fri Nov 09 2012 Martin Kosek <mkosek@redhat.com> - 3.0.99-3
- Set min for bind-dyndb-ldap to 2.3-2 to pick up disabling global
  forwarder per-zone

* Fri Oct 26 2012 Sumit Bose <sbose@redhat.com> - 3.0.99-2
- Restart httpd in post install of server-trust-ad

* Wed Oct 24 2012 Martin Kosek <mkosek@redhat.com> - 3.0.99-1
- Add strict Requires for 389-ds-base and policycoreutils to avoid user
  removing them during package lifetime

* Wed Oct 17 2012 Martin Kosek <mkosek@redhat.com> - 2.99.0-51
- Print ipa-upgradeconfig errors during RPM update

* Wed Oct 10 2012 Alexander Bokovoy <abokovoy@redhat.com> - 2.99.0-50
- Make sure server-trust-ad subpackage alternates winbind_krb5_locator.so
  plugin to /dev/null since they cannot be used when trusts are configured

* Wed Oct 10 2012 Petr Viktorin <pviktori@redhat.com> - 2.99.0-49
- Add zip dependency, needed for creating unsigned Firefox extensions

* Mon Oct  8 2012 Martin Kosek <mkosek@redhat.com> - 2.99.0-48
- Add directory /var/lib/ipa/pki-ca/publish for CRL published by pki-ca

* Mon Oct  1 2012 Martin Kosek <mkosek@redhat.com> - 2.99.0-47
- Require samba packages instead of samba4 packages obsoleted in Fedora 18 and later
- Add libwbclient-devel BuildRequires to pick up libwbclient.h on Fedora 18 and later

* Tue Sep 18 2012 Petr Viktorin <pviktori@redhat.com> - 2.99.0-46
- Set certmonger minimum version to 0.60 for Dogtag 10 support.

* Mon Sep 17 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-45
- Set min for 389-ds-base to 1.2.11.14-1 on F17+ to pull in updated
  RUV code and nsslapd-readonly schema.

* Fri Sep 14 2012 Sumit Bose <sbose@redhat.com> - 2.99.0-44
- Updated samba4-devel dependency due to API change

* Mon Aug 20 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-43
- Set min for 389-ds-base to 1.2.11.9-1 on F17+ to pull in warning about
  low nsslapd-cachememsize.

* Mon Aug 20 2012 Tomas Babej <tbabej@redhat.com> - 2.99.0-42
- Add samba4-winbind to build dependencies for AD server-side code

* Fri Aug 17 2012 Martin Kosek <mkosek@redhat.com> - 2.99.0-41
- Set min for bind-dyndb-ldap to 1.1.0-0.16.rc1 to pick up complete zone transfer
  support

* Thu Aug 2 2012 Martin Kosek <mkosek@redhat.com> - 2.99.0-40
- Set min for bind-dyndb-ldap to 1.1.0-0.15.rc1 to pick up SOA serial autoincrement
  feature

* Tue Jul 24 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-39
- Set minimum certmonger to 0.58 for dogtag cert renewal

* Wed Jul 18 2012 Alexander Bokovoy <abokovoy@redhat.com> - 2.99.0-38
- Require samba4-devel >= 4.0.0-128 due to passdb API change in beta4

* Fri Jun 29 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-37
- Add Requires on openssl
- Set minimum tomcat6 to 6.0.35-4 in F-18
- Set minimum mod_auth_kerb to 5.4-16 in F-18

* Thu Jun 21 2012 Sumit Bose <sbose@redhat.com> - 2.99.0-36
- Add extdom extop plugin

* Thu Jun 21 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-35
- Add client requires on libsss-autofs, autofs, libnfsidmap and nfs-utils
  for configuring automount and NFS.

* Thu Jun 21 2012 Petr Vobornik <pvoborni@redhat.com> - 2.99.0-34
- Add Web UI reset password pages

* Wed Jun 20 2012 Ondrej Hamada <ohamada@redhat.com> - 2.99.0-33
- Set min for 389-ds-base to 1.2.11.5-1 on F17 to fix installation issue
- Set min for 389-ds-base to 1.2.10.10-1 on F16 (and lower) to fix CN case persistence

* Fri Jun 8 2012 Martin Kosek <mkosek@redhat.com> - 2.99.0-32
- Add directory /var/lib/ipa/sysupgrade for package upgrade metadata
- Set min for bind-dyndb-ldap to 1.1.0-0.12.rc1 to pick up persistent search
  related bug fixes

* Mon Jun  4 2012 Alexander Bokovoy <abokovoy@redhat.com> - 2.99.0-31
- Add python-crypto to build dependencies for AD server-side code

* Tue May 29 2012 Alexander Bokovoy <abokovoy@redhat.com> - 2.99.0-30
- Add freeipa-server-trust-ad virtual package to capture all required dependencies
  for Active Directory trust management

* Fri May 11 2012 Martin Kosek <mkosek@redhat.com> - 2.99.0-29
- Replace used DNS client library (acutil) with python-dns

* Tue Apr 10 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-28
- Set min for selinux-policy to 3.10.0-110 on F-17 to pick up certmonger
  policy for restarting services.
- Set min for certmonger to 0.53 so we have the -C option to set restart
  commands.

* Thu Apr  5 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-27
- Bump minimum version of slapi-nis to 0.40

* Tue Mar 27 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-26
- Add python-krbV Requires on client package

* Mon Mar 26 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-25
- Set min for 389-ds-base to 1.2.10.4-2 to fix upgrade issue

* Fri Mar 23 2012 Petr Viktorin <pviktori@redhat.com> - 2.99.0-24
- Add python-lxml and python-pyasn1 to BuildRequires

* Mon Mar 19 2012 Martin Kosek <mkosek@redhat.com> - 2.99.0-23
- Set min for bind-dyndb-ldap and bind to pick up new features and bug fixes

* Thu Mar 1 2012 Jan Cholasta <jcholast@redhat.com> - 2.99.0-22
- Set min nvr of sssd to 1.8.0 for SSH support
- Add BuildRequires on sssd >= 1.8.0

* Wed Feb 29 2012 Petr Vobornik <pvoborni@redhat.com> - 2.99.0-21
- Add Web UI form based login page
- Removed ipa_migration.css

* Wed Feb 29 2012 Petr Vobornik <pvoborni@redhat.com> - 2.99.0-20
- Add Web UI logout page

* Mon Feb 27 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-19
- Add Requires to ipa-client on oddjob-mkhomedir

* Fri Feb 24 2012 Martin Kosek <mkosek@redhat.com> - 2.99.0-18
- Set min for bind-dyndb-ldap to 1.1.0-0.8.a2 to pick up new features

* Thu Feb 23 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-17
- Add Conflicts on mod_ssl

* Thu Feb 16 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-16
- Set min for 389-ds-base to 1.2.10.1-1 to fix install segfault,
  schema replication.

* Tue Jan 31 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-15
- Set min for krb5-server to 1.9.2-6 to pick up needed s4u2proxy patches

* Wed Jan 11 2012 Rob Crittenden <rcritten@redhat.com> - 2.99.0-14
- Set min for mod_auth_kerb to 5.4-8 to pick up s4u2proxy support

* Fri Dec 9 2011 Alexander Bokovoy <abokovoy@redhat.com> - 2.99.0-13
- Fix dependency for samba4-devel package

* Thu Nov 17 2011 Simo Sorce <simo@redhat.com> - 2.99.0-12
- Add CLDAP plugin
- Set min nvr of 389-ds-base to 1.2.10-0.5.a5 for SLAPI_PLUGIN_CONFIG_ENTRY
  support

* Mon Nov 14 2011 Endi S. Dewata <edewata@redhat.com> - 2.99.0-11
- Make sure changes to extension.js are not removed.

* Wed Oct 26 2011 Endi S. Dewata <edewata@redhat.com> - 2.99.0-10
- Moved UI images into install/ui/images

* Mon Oct 24 2011 Endi S. Dewata <edewata@redhat.com> - 2.99.0-9
- Removed hbac-deny-remove.html

* Fri Oct 21 2011 Alexander Bokovoy <abokovoy@redhat.com> - 2.99.0-8
- Default to systemd for Fedora 16 and onwards

* Fri Oct 14 2011 Rob Crittenden <rcritten@redhat.com> - 2.99.0-7
- Set min nvr of 389-ds-base to 1.2.10-0.4.a4 for limits fixes (740942, 742324)

* Fri Oct  7 2011 Adam Young <ayoung@redhat.com> - 2.99.0-6
- Add explicit dependency on pki-setup.

* Tue Sep 13 2011 Alexander Bokovoy <abokovoy@redhat.com> - 2.99.0-5
- Make sure platform adaptation is packaged in -python sub-package

* Fri Sep 9 2011 Martin Kosek <mkosek@redhat.com> - 2.99.0-4
- Add soft dependency for bind and bind-dyndb-ldap required versions

* Wed Aug 31 2011 Rob Crittenden <rcritten@redhat.com> - 2.99.0-3
- Set min nvr of 389-ds-base to 1.2.9.7-1 for BZ 728605

* Mon Aug 29 2011 Rob Crittenden <rcritten@redhat.com> - 2.99.0-2
- Set min nvr of pki-ca to 9.0.12 for fix in BZ 700505

* Thu Aug 25 2011 Simo Sorce <ssorce#redhat.com> - 2.99.0-1
- Remove ipa_kpasswd.

* Tue Aug 23 2011 Jan Cholasta <jcholast@redhat.com> - 2.1.0-1
- Add subscription-manager dependency for RHEL.

* Thu Aug 11 2011 Martin Kosek <mkosek@redhat.com> - 2.0.90-12
- Set min nvr of 389-ds-base to 1.2.9.6 for fix in BZ 725743,
  723937, and 725542
- Set min nvr of pki-ca to 9.0.11 for fix in BZ 728332

* Thu Aug 11 2011 Martin Kosek <mkosek@redhat.com> - 2.0.90-11
- Set min nvr of xmlrpc-c and libcurl to make sure GSSAPI delegation
  support is in

* Tue Aug 2 2011 Endi S. Dewata <edewata@redhat.com> - 2.0.90-10
- Add *.ico files

* Fri Jul 29 2011 Alexander Bokovoy <abokovoy@redhat.com> - 2.0.90-9
- Add libipa_hbac-python dependency for hbactest plugin

* Thu Jul 28 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.90-8
- Set min nvr of pki-ca to 9.0.10 on F-15+ to pick up updated
  caIPAserviceCert.cfg profile

* Wed Jul 20 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.90-7
- Make cyrus-sasl-gssapi requires arch-specific

* Thu Jul 14 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.90-6
- Add ipa-csreplica-manage tool.

* Wed Jul  6 2011 Adam Young <ayoung@redhat.com> - 2.0.90-5
- Add HTML file describing issues with HBAC deny rules

* Fri Jun 17 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.90-4
- Ship ipa-ca-install utility

* Thu May 12 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.90-3
- Set min nvr of selinux-policy to 3.9.16-18 on F-15+
- Set min nvr of pki-ca to 9.0.7 on F-15+

* Thu May  5 2011 Martin Kosek <mkosek@redhat.com> - 2.0.90-2
- Add BuildRequires on pylint, python-rhsm to enable a build with enforced
  pylint check

* Tue May  3 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.90-1
- Bump version to 2.0.90

* Tue Apr  5 2011 Rob Crittenden <rcritten@redhat.com> - 1.99-47
- Set min version of 389-ds-base to 1.2.8.0-1 for fix in BZ 693466.

* Thu Mar 17 2011 Rob Crittenden <rcritten@redhat.com> - 1.99-46
- Automatically apply updates when the package is upgraded.

* Thu Feb 17 2011 Jakub Hrozek <jhrozek@redhat.com> - 1.99-45
- Set minimum version of python-nss to 0.11 to make sure IPv6 support is in

* Wed Feb  9 2011 Rob Crittenden <rcritten@redhat.com> - 1.99-44
- Set minimum version of sssd to 1.5.1

* Wed Feb  2 2011 Rob Crittenden <rcritten@redhat.com> - 1.99-43
- Set min version of 389-ds-base to 1.2.8
- Set min version of mod_nss 1.0.8-10
- Set min version of selinux-policy to 3.9.7-27

* Thu Jan 27 2011 Rob Crittenden <rcritten@redhat.com> - 1.99-42
- Apply changes discovered in Fedora package review process (#672986)

* Tue Jan 25 2011 Rob Crittenden <rcritten@redhat.com> - 1.99-41
- Re-arrange doc and defattr to clean up rpmlint warnings
- Remove conditionals on older releases
- Move some man pages into admintools subpackage
- Remove some explicit Requires in client that aren't needed
- Consistent use of buildroot vs RPM_BUILD_ROOT

* Wed Jan 19 2011 Adam Young <ayoung@redhat.com> - 1.99-40
- Moved directory install/static to install/ui

* Thu Jan 13 2011 Simo Sorce <ssorce@redhat.com> - 1.99-39
- Remove dependency on nss_ldap/nss-pam-ldapd
- The official client is sssd and that's what we use by default.

* Thu Jan 13 2011 Simo Sorce <ssorce@redhat.com> - 1.99-38
- Remove radius subpackages

* Thu Jan 13 2011 Rob Crittenden <rcritten@redhat.com> - 1.99-37
- Set minimum pki-ca and pki-silent versions to 9.0.0

* Wed Jan 12 2011 Rob Crittenden <rcritten@redhat.com> - 1.99-36
- Drop BuildRequires on mozldap-devel

* Mon Dec 13 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-35
- Add Requires on krb5-pkinit-openssl

* Fri Dec 10 2010 Jr Aquino <jr.aquino@citrix.com> - 1.99-34
- Add ipa-host-net-manage script

* Tue Dec  7 2010 Simo Sorce <ssorce@redhat.com> - 1.99-33
- Add ipa init script

* Fri Nov 19 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-32
- Set minimum level of 389-ds-base to 1.2.7 for enhanced memberof plugin

* Wed Nov  3 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-31
- remove ipa-fix-CVE-2008-3274

* Wed Oct  6 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-30
- Remove duplicate %%files entries on share/ipa/static
- Add python default encoding shared library

* Mon Sep 20 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-29
- Drop requires on python-configobj (not used any more)
- Drop ipa-ldap-updater message, upgrades are done differently now

* Wed Sep  8 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-28
- Drop conflicts on mod_nss
- Require nss-pam-ldapd on F-14 or higher instead of nss_ldap (#606847)
- Drop a slew of conditionals on older Fedora releases (< 12)
- Add a few conditionals against RHEL 6
- Add Requires of nss-tools on ipa-client

* Fri Aug 13 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-27
- Set minimum version of certmonger to 0.26 (to pck up #621670)
- Set minimum version of pki-silent to 1.3.4 (adds -key_algorithm)
- Set minimum version of pki-ca to 1.3.6
- Set minimum version of sssd to 1.2.1

* Tue Aug 10 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-26
- Add BuildRequires for authconfig

* Mon Jul 19 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-25
- Bump up minimum version of python-nss to pick up nss_is_initialize() API

* Thu Jun 24 2010 Adam Young <ayoung@redhat.com> - 1.99-24
- Removed python-asset based webui

* Thu Jun 24 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-23
- Change Requires from fedora-ds-base to 389-ds-base
- Set minimum level of 389-ds-base to 1.2.6 for the replication
  version plugin.

* Tue Jun  1 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-22
- Drop Requires of python-krbV on ipa-client

* Mon May 17 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-21
- Load ipa_dogtag.pp in post install

* Mon Apr 26 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-20
- Set minimum level of sssd to 1.1.1 to pull in required hbac fixes.

* Thu Mar  4 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-19
- No need to create /var/log/ipa_error.log since we aren't using
  TurboGears any more.

* Mon Mar 1 2010 Jason Gerard DeRose <jderose@redhat.com> - 1.99-18
- Fixed share/ipa/wsgi.py so .pyc, .pyo files are included

* Wed Feb 24 2010 Jason Gerard DeRose <jderose@redhat.com> - 1.99-17
- Added Require mod_wsgi, added share/ipa/wsgi.py

* Thu Feb 11 2010 Jason Gerard DeRose <jderose@redhat.com> - 1.99-16
- Require python-wehjit >= 0.2.2

* Wed Feb  3 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-15
- Add sssd and certmonger as a Requires on ipa-client

* Wed Jan 27 2010 Jason Gerard DeRose <jderose@redhat.com> - 1.99-14
- Require python-wehjit >= 0.2.0

* Fri Dec  4 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-13
- Add ipa-rmkeytab tool

* Tue Dec  1 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-12
- Set minimum of python-pyasn1 to 0.0.9a so we have support for the ASN.1
  Any type

* Wed Nov 25 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-11
- Remove v1-style /etc/ipa/ipa.conf, replacing with /etc/ipa/default.conf

* Fri Nov 13 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-10
- Add bash completion script and own /etc/bash_completion.d in case it
  doesn't already exist

* Tue Nov  3 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-9
- Remove ipa_webgui, its functions rolled into ipa_httpd

* Mon Oct 12 2009 Jason Gerard DeRose <jderose@redhat.com> - 1.99-8
- Removed python-cherrypy from BuildRequires and Requires
- Added Requires python-assets, python-wehjit

* Mon Aug 24 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-7
- Added httpd SELinux policy so CRLs can be read

* Thu May 21 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-6
- Move ipalib to ipa-python subpackage
- Bump minimum version of slapi-nis to 0.15

* Wed May  6 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-5
- Set 0.14 as minimum version for slapi-nis

* Wed Apr 22 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-4
- Add Requires: python-nss to ipa-python sub-package

* Thu Mar  5 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-3
- Remove the IPA DNA plugin, use the DS one

* Wed Mar  4 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-2
- Build radius separately
- Fix a few minor issues

* Tue Feb  3 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-1
- Replace TurboGears requirement with python-cherrypy

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 1.2.1-3
- rebuild with new openssl

* Fri Dec 19 2008 Dan Walsh <dwalsh@redhat.com> - 1.2.1-2
- Fix SELinux code

* Mon Dec 15 2008 Simo Sorce <ssorce@redhat.com> - 1.2.1-1
- Fix breakage caused by python-kerberos update to 1.1

* Fri Dec 5 2008 Simo Sorce <ssorce@redhat.com> - 1.2.1-0
- New upstream release 1.2.1

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.2.0-4
- Rebuild for Python 2.6

* Fri Nov 14 2008 Simo Sorce <ssorce@redhat.com> - 1.2.0-3
- Respin after the tarball has been re-released upstream
  New hash is 506c9c92dcaf9f227cba5030e999f177

* Thu Nov 13 2008 Simo Sorce <ssorce@redhat.com> - 1.2.0-2
- Conditionally restart also dirsrv and httpd when upgrading

* Wed Oct 29 2008 Rob Crittenden <rcritten@redhat.com> - 1.2.0-1
- Update to upstream version 1.2.0
- Set fedora-ds-base minimum version to 1.1.3 for winsync header
- Set the minimum version for SELinux policy
- Remove references to Fedora 7

* Wed Jul 23 2008 Simo Sorce <ssorce@redhat.com> - 1.1.0-3
- Fix for CVE-2008-3274
- Fix segfault in ipa-kpasswd in case getifaddrs returns a NULL interface
- Add fix for bug #453185
- Rebuild against openldap libraries, mozldap ones do not work properly
- TurboGears is currently broken in rawhide. Added patch to not build
  the UI locales and removed them from the ipa-server files section.

* Wed Jun 18 2008 Rob Crittenden <rcritten@redhat.com> - 1.1.0-2
- Add call to /usr/sbin/upgradeconfig to post install

* Wed Jun 11 2008 Rob Crittenden <rcritten@redhat.com> - 1.1.0-1
- Update to upstream version 1.1.0
- Patch for indexing memberof attribute
- Patch for indexing uidnumber and gidnumber
- Patch to change DNA default values for replicas
- Patch to fix uninitialized variable in ipa-getkeytab

* Fri May 16 2008 Rob Crittenden <rcritten@redhat.com> - 1.0.0-5
- Set fedora-ds-base minimum version to 1.1.0.1-4 and mod_nss minimum
  version to 1.0.7-4 so we pick up the NSS fixes.
- Add selinux-policy-base(post) to Requires (446496)

* Tue Apr 29 2008 Rob Crittenden <rcritten@redhat.com> - 1.0.0-4
- Add missing entry for /var/cache/ipa/kpasswd (444624)
- Added patch to fix permissions problems with the Apache NSS database.
- Added patch to fix problem with DNS querying where the query could be
  returned as the answer.
- Fix spec error where patch1 was in the wrong section

* Fri Apr 25 2008 Rob Crittenden <rcritten@redhat.com> - 1.0.0-3
- Added patch to fix problem reported by ldapmodify

* Fri Apr 25 2008 Rob Crittenden <rcritten@redhat.com> - 1.0.0-2
- Fix Requires for krb5-server that was missing for Fedora versions > 9
- Remove quotes around test for fedora version to package egg-info

* Fri Apr 18 2008 Rob Crittenden <rcritten@redhat.com> - 1.0.0-1
- Update to upstream version 1.0.0

* Tue Mar 18 2008 Rob Crittenden <rcritten@redhat.com> 0.99-12
- Pull upstream changelog 722
- Add Conflicts mod_ssl (435360)

* Fri Feb 29 2008 Rob Crittenden <rcritten@redhat.com> 0.99-11
- Pull upstream changelog 698
- Fix ownership of /var/log/ipa_error.log during install (435119)
- Add pwpolicy command and man page

* Thu Feb 21 2008 Rob Crittenden <rcritten@redhat.com> 0.99-10
- Pull upstream changelog 678
- Add new subpackage, ipa-server-selinux
- Add Requires: authconfig to ipa-python (bz #433747)
- Package i18n files

* Mon Feb 18 2008 Rob Crittenden <rcritten@redhat.com> 0.99-9
- Pull upstream changelog 641
- Require minimum version of krb5-server on F-7 and F-8
- Package some new files

* Thu Jan 31 2008 Rob Crittenden <rcritten@redhat.com> 0.99-8
- Marked with wrong license. IPA is GPLv2.

* Tue Jan 29 2008 Rob Crittenden <rcritten@redhat.com> 0.99-7
- Ensure that /etc/ipa exists before moving user-modifiable html files there
- Put html files into /etc/ipa/html instead of /etc/ipa

* Tue Jan 29 2008 Rob Crittenden <rcritten@redhat.com> 0.99-6
- Pull upstream changelog 608 which renamed several files

* Thu Jan 24 2008 Rob Crittenden <rcritten@redhat.com> 0.99-5
- package the sessions dir /var/cache/ipa/sessions
- Pull upstream changelog 597

* Thu Jan 24 2008 Rob Crittenden <rcritten@redhat.com> 0.99-4
- Updated upstream pull (596) to fix bug in ipa_webgui that was causing the
  UI to not start.

* Thu Jan 24 2008 Rob Crittenden <rcritten@redhat.com> 0.99-3
- Included LICENSE and README in all packages for documentation
- Move user-modifiable content to /etc/ipa and linked back to
  /usr/share/ipa/html
- Changed some references to /usr to the {_usr} macro and /etc
  to {_sysconfdir}
- Added popt-devel to BuildRequires for Fedora 8 and higher and
  popt for Fedora 7
- Package the egg-info for Fedora 9 and higher for ipa-python

* Tue Jan 22 2008 Rob Crittenden <rcritten@redhat.com> 0.99-2
- Added auto* BuildRequires

* Mon Jan 21 2008 Rob Crittenden <rcritten@redhat.com> 0.99-1
- Unified spec file

* Thu Jan 17 2008 Rob Crittenden <rcritten@redhat.com> - 0.6.0-2
- Fixed License in specfile
- Include files from /usr/lib/python*/site-packages/ipaserver

* Fri Dec 21 2007 Karl MacMillan <kmacmill@redhat.com> - 0.6.0-1
- Version bump for release

* Wed Nov 21 2007 Karl MacMillan <kmacmill@mentalrootkit.com> - 0.5.0-1
- Preverse mode on ipa-keytab-util
- Version bump for relase and rpm name change

* Thu Nov 15 2007 Rob Crittenden <rcritten@redhat.com> - 0.4.1-2
- Broke invididual Requires and BuildRequires onto separate lines and
  reordered them
- Added python-tgexpandingformwidget as a dependency
- Require at least fedora-ds-base 1.1

* Thu Nov  1 2007 Karl MacMillan <kmacmill@redhat.com> - 0.4.1-1
- Version bump for release

* Wed Oct 31 2007 Karl MacMillan <kmacmill@redhat.com> - 0.4.0-6
- Add dep for freeipa-admintools and acl

* Wed Oct 24 2007 Rob Crittenden <rcritten@redhat.com> - 0.4.0-5
- Add dependency for python-krbV

* Fri Oct 19 2007 Rob Crittenden <rcritten@redhat.com> - 0.4.0-4
- Require mod_nss-1.0.7-2 for mod_proxy fixes

* Thu Oct 18 2007 Karl MacMillan <kmacmill@redhat.com> - 0.4.0-3
- Convert to autotools-based build

* Tue Sep 25 2007 Karl MacMillan <kmacmill@redhat.com> - 0.4.0-2

* Fri Sep 7 2007 Karl MacMillan <kmacmill@redhat.com> - 0.3.0-1
- Added support for libipa-dna-plugin

* Fri Aug 10 2007 Karl MacMillan <kmacmill@redhat.com> - 0.2.0-1
- Added support for ipa_kpasswd and ipa_pwd_extop

* Sun Aug  5 2007 Rob Crittenden <rcritten@redhat.com> - 0.1.0-3
- Abstracted client class to work directly or over RPC

* Wed Aug  1 2007 Rob Crittenden <rcritten@redhat.com> - 0.1.0-2
- Add mod_auth_kerb and cyrus-sasl-gssapi to Requires
- Remove references to admin server in ipa-server-setupssl
- Generate a client certificate for the XML-RPC server to connect to LDAP with
- Create a keytab for Apache
- Create an ldif with a test user
- Provide a certmap.conf for doing SSL client authentication

* Fri Jul 27 2007 Karl MacMillan <kmacmill@redhat.com> - 0.1.0-1
- Initial rpm version
