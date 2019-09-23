
Name: vzctl
Version: 7.0.207
Release: alt5

Summary: OpenVZ Virtual Environments control utility
License: GPL
Group: System/Configuration/Other
Url: http://openvz.org/

# git-vsc https://src.openvz.org/scm/ovzl/vzctl.git
Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: x86_64

# these reqs are for vz helper scripts
Requires: ploop >= 7.0.160
Requires: network-config-subsystem
Requires: libvzctl

BuildRequires: glibc-devel libuuid-devel
BuildRequires: systemd-devel libudev-devel
BuildRequires: libvzctl-devel >= 7.0.535
BuildRequires: libploop-devel >= 7.0.160
BuildRequires: kernel-headers-ovz-el7 >= 3.10.0

%define _libexecdir /usr/libexec
%define vzdir /etc/vz
%define confdir %vzdir/conf
%define namesdir %vzdir/names
%define lockdir /var/lib/vz/lock
%define vzctl_lockdir /var/lock/vzctl
%define spooldir /var/lib/vz
%define netdir /etc/sysconfig/network-scripts
%define bashcompldir /etc/bash_completion.d

%description
OpenVZ is an Operating System-level server virtualization solution, built
on Linux.  OpenVZ creates isolated, secure virtual private servers on a
single physical server enabling better server utilization and ensuring
that applications do not conflict.  Each VE performs and executes exactly
like a stand-alone server; VEs can be rebooted independently and have
root access, users, IP addresses, memory, processes, files, applications,
system libraries and configuration files.

This package contain the control tool to manipulate
OpenVZ Virtual Environments.

%prep
%setup
%patch -p1

%build
#make_build CFLAGS="%optflags -D_GNU_SOURCE -DVERSION=\\\"%version-%release\\\""
%make CFLAGS="%optflags -D_GNU_SOURCE -DVERSION=\\\"%version-%release\\\""

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

ln -s -r %buildroot%_unitdir/vzevent.service %buildroot%_unitdir/vzeventd.service

%post
# rm -f /dev/vzctl
# mknod -m 600 /dev/vzctl c 126 0
# rm -rf %vzdir/dev/vzlink
# mknod -m 600 %vzdir/dev/vzlink c 125 0

%post_service vzeventd

# Load sysctls
sysctl -p /etc/sysctl.d/99-vzctl.conf > /dev/null 2>&1

# First installation, not upgrade.
#if [ $1 -eq 1 ]; then
#	# Insert iptables rules.
#	%_libexecdir/vz-iptables-config.py add > /dev/null 2>&1
#fi
exit 0

%preun
%preun_service vz
%preun_service vzeventd
# Last deinstallation, not upgrade.
#if [ $1 -eq 0 ]; then
#	# Remove iptables rules.
#	%_libexecdir/vz-iptables-config.py remove > /dev/null 2>&1
#fi

%files
%dir %vzdir
%dir %confdir
%dir %namesdir
%dir %vzdir/dev
%vzdir/vzevent.d
%attr(700,root,root) %lockdir
%spooldir
%bashcompldir/*
%_target_libdir_noarch/dracut/modules.d/*
%_sbindir/*
%_unitdir/*.service
#%_initdir/*
%_libexecdir/vz
%config(noreplace) %_logrotatedir/vzctl
%confdir/*sample
%_man8dir/*
%_man5dir/*

%config(noreplace) %confdir/networks_classes
%config(noreplace) %vzdir/vz.conf
%config(noreplace) %_sysconfdir/modprobe.d/*.conf
%config %_sysconfdir/sysctl.d/*.conf
%config %_sysconfdir/modules-load.d/*.conf

%changelog
* Tue Aug 27 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.207-alt5
- spec cleanup

* Tue Aug 27 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.207-alt4
- network and service changes for ALT

* Mon Aug 26 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.207-alt3
- change prlctl to vzlist/vzctl

* Thu Aug 22 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.207-alt2
- drop sysv rc scripts

* Mon Aug 19 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.207-alt1
- Update to 7.0.207

* Sun Nov 04 2018 Alexey Shabalin <shaba@altlinux.org> 7.0.191-alt1
- Update to 7.0.191

* Mon Feb 12 2018 Alexey Shabalin <shaba@altlinux.ru> 7.0.182-alt1
- Initial build vzctl-7.0.182 for VZ-7

* Tue Aug 25 2015 Terechkov Evgenii <evg@altlinux.org> 4.9.4-alt1
- Updated to vzctl-4.9.4

