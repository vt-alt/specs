%define _unpackaged_files_terminate_build 1
%def_with check

Name: oddjob
Version: 0.34.6
Release: alt1
Summary: A D-Bus service which runs odd jobs on behalf of client applications

Group: System/Servers
License: %bsdstyle
Url: https://pagure.io/oddjob

Source: %name-%version.tar
Source1: oddjobd.init
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: xmlto
BuildRequires: libdbus-devel
BuildRequires: libxml2-devel
BuildRequires: libpam0-devel
BuildRequires: libselinux-devel
BuildRequires: libsasl2-devel
BuildRequires: libkrb5-devel
BuildRequires: libcom_err-devel
BuildRequires: libsystemd-devel
BuildRequires: libldap-devel

%if_with check
BuildRequires: dbus-tools-gui
BuildRequires: /proc
%endif

%description
oddjob is a D-Bus service which performs particular tasks for clients
which connect to it and issue requests using the system-wide message
bus.

%package mkhomedir
Summary: An oddjob helper which creates and populates home directories
Group: System/Servers
Requires: %name = %EVR

%description mkhomedir
This package contains the oddjob helper which can be used by the
pam_oddjob_mkhomedir module to create a home directory for a user
at login-time.

%package sample
Summary: A sample oddjob service
Group: System/Servers
Requires: %name = %EVR

%description sample
This package contains a trivial sample oddjob service.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
    --disable-static \
    --enable-pie \
    --enable-now \
    --with-selinux-acls \
    --with-selinux-labels \
    --without-python \
    --enable-xml-docs \
    --enable-systemd \
    --disable-sysvinit \
    --enable-sample
%make_build

%install
%makeinstall_std

# Make sure we don't needlessly make these docs executable.
chmod -x src/reload src/mkhomedirfor src/mkmyhomedir

# Install initscript
install -Dm0755 %SOURCE1 %buildroot%_initdir/oddjobd

# Sample
install -m644 sample/oddjobd-sample.conf	%buildroot/%_sysconfdir/%{name}d.conf.d/
install -m644 sample/oddjob-sample.conf		%buildroot/%_sysconfdir/dbus-1/system.d/
install -m755 sample/oddjob-sample.sh		%buildroot/%_libexecdir/%name/

mkdir -p %buildroot/%_lib/security
mv %buildroot%_libdir/security/pam_oddjob_mkhomedir.so \
%buildroot/%_lib/security/
rm %buildroot%_libdir/security/pam_oddjob_mkhomedir.la

%check
%make check

%files
%doc *.dtd COPYING NEWS QUICKSTART doc/oddjob.html src/reload
%_unitdir/oddjobd.service
%_initdir/oddjobd
%_bindir/*
%_sbindir/*
%config(noreplace) %_sysconfdir/dbus-*/system.d/oddjob.conf
%config(noreplace) %_sysconfdir/oddjobd.conf
%dir %_sysconfdir/oddjobd.conf.d
%config(noreplace) %_sysconfdir/oddjobd.conf.d/oddjobd-introspection.conf
%dir %_sysconfdir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/sanity.sh
%_mandir/*/oddjob.*
%_mandir/*/oddjob_request.*
%_mandir/*/oddjobd.*
%_mandir/*/oddjobd-introspection.*

%files mkhomedir
%doc src/mkhomedirfor src/mkmyhomedir
%_libexecdir/%name/mkhomedir
/%_lib/security/pam_oddjob_mkhomedir.so
%_mandir/*/pam_oddjob_mkhomedir.*
%_mandir/*/oddjob-mkhomedir.*
%_mandir/*/oddjobd-mkhomedir.*
%config(noreplace) %_sysconfdir/dbus-*/system.d/oddjob-mkhomedir.conf
%config(noreplace) %_sysconfdir/oddjobd.conf.d/oddjobd-mkhomedir.conf


%files sample
%_libexecdir/%name/oddjob-sample.sh
%config %_sysconfdir/dbus-*/system.d/oddjob-sample.conf
%config %_sysconfdir/oddjobd.conf.d/oddjobd-sample.conf

%post
%post_service oddjobd

%preun
%preun_service oddjobd

%changelog
* Tue May 12 2020 Stanislav Levin <slev@altlinux.org> 0.34.6-alt1
- 0.34.4 -> 0.34.6 (fixes: CVE-2020-10737).

* Fri Jun 07 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.34.4-alt4
- Fix DBus error messages with disabled SELinux (RH#510457, RHBA-2010:0668)

* Tue Feb 05 2019 Stanislav Levin <slev@altlinux.org> 0.34.4-alt3
- Enable debug logging for testing.

* Mon Oct 22 2018 Stanislav Levin <slev@altlinux.org> 0.34.4-alt2
- Fixed the location of PAM module.

* Wed Oct 10 2018 Stanislav Levin <slev@altlinux.org> 0.34.4-alt1
- 0.34.3 -> 0.34.4.

* Mon Jun 27 2016 Mikhail Efremov <sem@altlinux.org> 0.34.3-alt1
- Initial build.

