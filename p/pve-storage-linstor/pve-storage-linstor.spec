
Name: pve-storage-linstor
Version: 5.1.2
Release: alt1
Summary: LINSTOR Proxmox Plugin
Group: System/Servers
License: GPLv2+
Url: https://github.com/LINBIT/linstor-proxmox.git
Source: %name-%version.tar
ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-build-perl
BuildRequires: pve-storage
BuildRequires: perl-JSON-XS
BuildRequires: perl(REST/Client.pm)
Requires: linstor-controller

%add_perl_lib_path %buildroot%perl_vendor_privlib

%description
LINSTOR Proxmox Plugin

%prep
%setup

%build
#Empty build

%install
	install -D -m 0644 ./LINSTORPlugin.pm %buildroot%perl_vendor_privlib/PVE/Storage/Custom/LINSTORPlugin.pm
	install -D -m 0644 ./LINBIT/Linstor.pm %buildroot%perl_vendor_privlib/LINBIT/Linstor.pm
	install -D -m 0644 ./LINBIT/PluginHelper.pm %buildroot%perl_vendor_privlib/LINBIT/PluginHelper.pm

%post
%post_service pvedaemon

%postun
%post_service pvedaemon

%files
%doc README.md
%dir %perl_vendor_privlib/PVE/Storage/Custom
%perl_vendor_privlib/PVE/Storage/Custom/LINSTORPlugin.pm
%dir %perl_vendor_privlib/LINBIT
%perl_vendor_privlib/LINBIT/Linstor.pm
%perl_vendor_privlib/LINBIT/PluginHelper.pm

%changelog
* Tue Jun 23 2020 Andrew A. Vasilyev <andy@altlinux.org> 5.1.2-alt1
- 5.1.2

* Tue Mar 17 2020 Andrew A. Vasilyev <andy@altlinux.org> 4.1.2-alt1
- initial build for ALT

