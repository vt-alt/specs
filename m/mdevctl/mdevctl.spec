Name:		mdevctl
Version:	0.69
Release:	alt1
Summary:	Mediated device management and persistence utility

Group:		System/Configuration/Hardware
License:	LGPLv2
URL:		https://github.com/mdevctl/mdevctl
BuildArch:	noarch

Source0:	%name-%version.tar
Patch0:     %name-%version.patch

BuildRequires: pkgconfig(udev)
Requires: coreutils udev jq

%description
mdevctl is a utility for managing and persisting devices in the
mediated device device framework of the Linux kernel.  Mediated
devices are sub-devices of a parent device (ex. a vGPU) which
can be dynamically created and potentially used by drivers like
vfio-mdev for assignment to virtual machines.

%prep
%setup
%patch0 -p1

%install
%makeinstall_std

%files
%doc README.md
%_sbindir/mdevctl
%_sbindir/lsmdev
%_udevrulesdir/60-mdevctl.rules
%dir %_sysconfdir/mdevctl.d
%_man8dir/mdevctl.8*
%_man8dir/lsmdev.8*

%changelog
* Tue Sep 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.69-alt1
- 0.69

* Fri Jul 10 2020 Alexey Shabalin <shaba@altlinux.org> 0.61-alt1
- Initial build


