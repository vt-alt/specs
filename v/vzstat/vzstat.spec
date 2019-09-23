
Name: vzstat
Version: 7.0.20
Release: alt1
Summary: vzstat utility for node monitoring

Group: System/Base
License: GPL2+
Url: https://src.openvz.org/projects/OVZ/repos/vzstat
Source: %name-%version.tar
Patch: %name-%version.patch
ExclusiveArch: x86_64

BuildRequires: libvzctl-devel
BuildRequires: libncurses-devel
BuildRequires: libuuid-devel
BuildRequires: kernel-headers-ovz-el7 >= 3.10.0

%description
This package contains statistic monitoring utility for OpenVZ HW node.

%prep
%setup
%patch -p1

%build
%make_build

%install
%makeinstall_std MANDIR="%_mandir"

%files
%_sbindir/%name
%config(noreplace) %_sysconfdir/vz/%name.conf
%_man8dir/%name.*
%doc README.md COPYING

%changelog
* Mon Sep 16 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.20-alt1
- 7.0.20

* Sun Nov 04 2018 Alexey Shabalin <shaba@altlinux.org> 7.0.19-alt1
- initial packaging

