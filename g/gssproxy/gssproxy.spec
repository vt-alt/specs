%define _unpackaged_files_terminate_build 1
%define pubconfpath %_sysconfdir/gssproxy
%define gpstatepath %_sharedstatedir/gssproxy
%define _localstatedir %_var
%define gssproxy_user _gssproxy

%def_with check

Name: gssproxy
Version: 0.8.3
Release: alt1
Summary: GSSAPI Proxy

Group: System/Servers
License: %mit
Url: https://github.com/gssapi/gssproxy

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libxslt
BuildRequires: xsltproc
BuildRequires: libxml2
BuildRequires: docbook-style-xsl
BuildRequires: doxygen
BuildRequires: gettext-devel
BuildRequires: pkg-config
BuildRequires: libkrb5-devel
BuildRequires: libselinux-devel
BuildRequires: libkeyutils-devel
BuildRequires: libini_config-devel >= 1.3.1
BuildRequires: libverto-devel
BuildRequires: libpopt-devel
BuildRequires: systemd
BuildRequires: po4a
BuildRequires: libcap-devel

%if_with check
BuildRequires: /proc
BuildRequires: krb5-kdc
BuildRequires: krb5-doc
BuildRequires: nss_wrapper
BuildRequires: socket_wrapper
BuildRequires: openldap-clients
BuildRequires: openldap-servers

# https://pagure.io/gssproxy/issue/227
%ifnarch %ix86 mipsel ppc64le
BuildRequires: valgrind
%endif

BuildRequires: python3
%endif

%description
A proxy for GSSAPI credential handling.

%package nfs-server
Summary: GSSAPI Proxy configuration for NFS server
Group: System/Base
Requires: %name

%description nfs-server
GSSAPI Proxy configuration for NFS server

%package nfs-client
Summary: GSSAPI Proxy configuration for NFS client
Group: System/Base
Requires: %name

%description nfs-client
GSSAPI Proxy configuration for NFS client

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
        --with-cap \
	--with-pubconf-path=%pubconfpath \
	--with-gpstate-path=%gpstatepath \
	--with-initscript=systemd \
	--with-systemdunitdir=%_unitdir \
	--disable-static \
	--disable-rpath \
	--with-gpp-default-behavior=REMOTE_FIRST

%make_build all

%check
%make_build test_proxymech

# https://pagure.io/gssproxy/issue/227
%make check \
%ifarch %ix86 mipsel ppc64le
	CHECKARGS="--valgrind-cmd=" \
%endif
	%nil


%install
%makeinstall_std

install -d -m0755 %buildroot%_sysconfdir/gssproxy
install -m0644 examples/gssproxy.conf %buildroot%_sysconfdir/gssproxy/gssproxy.conf
install -m0644 examples/24-nfs-server.conf %buildroot%_sysconfdir/gssproxy/
install -m0644 examples/99-nfs-client.conf %buildroot%_sysconfdir/gssproxy/
mkdir -p %buildroot%_sysconfdir/gss/mech.d
install -m0644 examples/mech %buildroot%_sysconfdir/gss/mech.d/gssproxy.conf
mkdir -p %buildroot%gpstatepath/rcache
mkdir -p %buildroot%_runtimedir
install -d -m0770 %buildroot%_runtimedir/gssproxy
# do not pack la files
rm -f %buildroot%_libdir/%name/proxymech.la

# setup non-privileged user
grep -qs 'run_as_user' %buildroot%_sysconfdir/gssproxy/gssproxy.conf && exit 1
echo 'run_as_user = %gssproxy_user' >> %buildroot%_sysconfdir/gssproxy/gssproxy.conf

%pre
%_sbindir/groupadd -r -f %gssproxy_user >/dev/null 2>&1 ||:
%_sbindir/useradd -r -g %gssproxy_user -G _keytab -d %_sharedstatedir/gssproxy \
-s /dev/null -c "User for gssproxy" %gssproxy_user >/dev/null 2>&1 ||:

%post
%post_service gssproxy

%post nfs-server
%post_service gssproxy

%post nfs-client
%post_service gssproxy

%preun
%preun_service gssproxy

%preun nfs-server
%preun_service gssproxy

%preun nfs-client
%preun_service gssproxy

%triggerpostun -- gssproxy < 0.8.0-alt2
/bin/chown %gssproxy_user:%gssproxy_user %gpstatepath/rcache/* >/dev/null 2>&1 ||:
/bin/chown %gssproxy_user:%gssproxy_user %gpstatepath/clients/* >/dev/null 2>&1 ||:

%files
%_unitdir/%name.service
%_sbindir/%name
%attr(0755,root,%gssproxy_user) %dir %pubconfpath
%attr(0640,root,%gssproxy_user) %config(noreplace) %_sysconfdir/gssproxy/gssproxy.conf
%attr(0644,root,root) %config(noreplace) %_sysconfdir/gss/mech.d/gssproxy.conf
%attr(0775,root,%gssproxy_user) %dir %gpstatepath
%attr(0770,root,%gssproxy_user) %dir %gpstatepath/clients
%attr(0770,root,%gssproxy_user) %dir %gpstatepath/rcache
%attr(0770,root,%gssproxy_user) %dir %_runtimedir/gssproxy
%dir %_libdir/%name
%_libdir/%name/proxymech.so
%_man5dir/*
%_man8dir/*

%files nfs-server
%attr(0640,root,%gssproxy_user) %config(noreplace) %_sysconfdir/gssproxy/24-nfs-server.conf

%files nfs-client
%attr(0640,root,%gssproxy_user) %config(noreplace) %_sysconfdir/gssproxy/99-nfs-client.conf

%changelog
* Mon Apr 20 2020 Stanislav Levin <slev@altlinux.org> 0.8.3-alt1
- 0.8.2 -> 0.8.3.

* Tue May 21 2019 Stanislav Levin <slev@altlinux.org> 0.8.2-alt1
- 0.8.1 -> 0.8.2.

* Wed Apr 17 2019 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1
- 0.8.0 -> 0.8.1.

* Wed Mar 06 2019 Ivan A. Melnikov <iv@altlinux.org> 0.8.0-alt3
- Run tests without valgrind on %%ix86 and mipsel.

* Sun Dec 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.0-alt2
- Added gssproxy config for nfs-server.
- Enabled running gssproxy as a non-privileged user.
- Enabled testing on aarch64.

* Thu Mar 15 2018 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.7.0 -> 0.8.0

* Wed Nov 01 2017 Stanislav Levin <slev@altlinux.org> 0.7.0-alt1
- New 0.7.0 version

* Thu Jul 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Initial build.
