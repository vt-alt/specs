
Name:		driverctl
Version:	0.110
Release:	alt12
Summary:	Device driver control utility

Group:      System/Configuration/Hardware
License:	LGPLv2
URL:		https://gitlab.com/driverctl/driverctl
BuildArch:	noarch

Source:	%name-%version.tar

BuildRequires: pkgconfig(udev) pkgconfig(systemd) 

%description
driverctl is a tool for manipulating and inspecting the system
device driver choices.

Devices are normally assigned to their sole designated kernel driver
by default. However in some situations it may be desireable to
override that default, for example to try an older driver to
work around a regression in a driver or to try an experimental alternative
driver. Another common use-case is pass-through drivers and driver
stubs to allow userspace to drive the device, such as in case of
virtualization.

driverctl integrates with udev to support overriding
driver selection for both cold- and hotplugged devices from the
moment of discovery, but can also change already assigned drivers,
assuming they are not in use by the system. The driver overrides
created by driverctl are persistent across system reboots
by default.

%prep
%setup -q
sed -i 's|/usr/lib/udev/vfio_name|/lib/udev/vfio_name|' 89-vfio-uio.rules
sed -i 's|/usr/sbin/driverctl|/sbin/driverctl|' driverctl@.service

%install
%makeinstall_std SBINDIR=/sbin

%files
%doc README TODO
/sbin/driverctl
%_udevrulesdir/*.rules
%_udevrulesdir/../vfio_name
%_unitdir/driverctl@.service
%dir %_sysconfdir/driverctl.d
%_datadir/bash-completion/
%_man8dir/driverctl.8*

%changelog
* Fri Jan 10 2020 Alexey Shabalin <shaba@altlinux.org> 0.110-alt12
- Fixed ExecStart in systemd unit

* Mon Dec 23 2019 Alexey Shabalin <shaba@altlinux.org> 0.110-alt11
- Initial build

