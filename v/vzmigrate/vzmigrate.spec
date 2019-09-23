Name:     vzmigrate
Version:  7.0.124
Release:  alt4

Summary:  Virtuozzo migration tool
License:  GPLv2+
Group:    Other
Url:      https://src.openvz.org/scm/ovz/vzmigrate.git

Packager: Andrew A. Vasilyev <andy@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: x86_64

# these reqs are for vz helper scripts
Requires: ploop >= 7.0.160
Requires: network-config-subsystem
Requires: libvzctl
Requires: libvztt

BuildRequires: gcc-c++
BuildRequires: glibc-devel libuuid-devel
BuildRequires: systemd-devel libudev-devel
BuildRequires: libvzctl-devel >= 7.0.535
BuildRequires: libvzsock-devel
BuildRequires: libssl-devel openssl libkrb5-devel
BuildRequires: libploop-devel >= 7.0.160
BuildRequires: libvztt-devel
BuildRequires: libzstd-devel
BuildRequires: kernel-headers-ovz-el7 >= 3.10.0
BuildRequires: boost-asio-devel boost-devel boost-devel-headers

%define _libexecdir /usr/libexec
%define vzdir /etc/vz
%define confdir %vzdir/conf
%define namesdir %vzdir/names
%define lockdir /var/lib/vz/lock
%define vzctl_lockdir /var/lock/vzctl
%define spooldir /var/lib/vz
%define netdir /etc/sysconfig/network-scripts
%define bashcompldir /etc/bash_completion.d

#add_optflags "-D_GNU_SOURCE -DVERSION=\\"%version-%release\\""

%description
%summary

%prep
%setup
%patch -p1

%build
#make_build CFLAGS="%optflags -D_GNU_SOURCE -DVERSION=\\\"%version-%release\\\""
%make_build

%install
make install \
        DESTDIR=%buildroot \
        SBINDIR=%_sbindir \
        MANDIR=%_mandir \
        SYSTEMDDIR=%_unitdir \
        NETSCRIPTDIR=%netdir \
        VZDIR=%vzdir \
        CONFDIR=%confdir \
        VZLOCKDIR=%lockdir \
        VZCTLLOCKDIR=%vzctl_lockdir \
        VZSPOOLDIR=%spooldir \
        BASHCOMPLDIR=%bashcompldir \
        LOGRDIR=%_logrotatedir

%files
%_sbindir/*
%_man8dir/*
%_datadir/%name/
%_datadir/pmigrate/
%config(noreplace) %_logrotatedir/%name
%doc *.md

%changelog
* Wed Sep 18 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.124-alt4
- fix double slashes in symlinks

* Tue Sep 17 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.124-alt3
- remove deprecated cipher and message

* Mon Aug 26 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.124-alt2
- fix build with static vzsock

* Fri Aug 23 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.124-alt1
- 7.0.124

* Mon Aug 19 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.123-alt2
- more specific requirements
- revert define macros patch

* Fri Aug 16 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.123-alt1
- Initial build for Sisyphus
