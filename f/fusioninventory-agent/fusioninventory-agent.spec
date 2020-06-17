Name:     fusioninventory-agent
Version:  2.5.2
Release:  alt1

Summary:  FusionInventory Agent
License:  GPL-2.0
Group:    Other
Url:      https://github.com/fusioninventory/fusioninventory-agent

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:  %name-%version.tar
Source1: %name.cron
Source2: %name.service
Source3: %name.conf

# Track USB printers (thanks Mikhail Fiskov)
Patch1: %name-track-usb-printers.patch

BuildArch: noarch

%add_perl_lib_path %buildroot%_datadir/fusioninventory/lib
%set_findreq_skiplist %_bindir/%name

BuildRequires: perl-File-Copy-Recursive
BuildRequires: perl-HTTP-Proxy
BuildRequires: perl-HTTP-Server-Simple
BuildRequires: perl-HTTP-Server-Simple-Authen
BuildRequires: perl-IO-Capture
BuildRequires: perl-IO-Socket-SSL
BuildRequires: perl-IPC-Run
BuildRequires: perl-LWP-Protocol-https
BuildRequires: perl-Memoize
BuildRequires: perl-Module-Install
BuildRequires: perl-Net-IP
BuildRequires: perl-Net-SNMP
BuildRequires: perl-Parallel-ForkManager
BuildRequires: perl-Parse-EDID
BuildRequires: perl-Test-Compile
BuildRequires: perl-Test-Deep
BuildRequires: perl-Test-Exception
BuildRequires: perl-Test-MockModule
BuildRequires: perl-Test-MockObject
BuildRequires: perl-Test-NoWarnings
BuildRequires: perl-Text-Template
BuildRequires: perl-XML-TreePP
BuildRequires: perl-XML-XPath

%description
FusionInventory Agent is an application designed to help a network
or system administrator to keep track of the hardware and software
configurations of computers that are installed on the network.
This agent can send information about the computer to a OCS Inventory NG
or GLPI server with the FusionInventory for GLPI plugin.
You can add additional packages for optional tasks:
* fusioninventory-agent-task-network
  Network Discovery and Inventory support
* fusioninventory-agent-inventory
  Local inventory support for FusionInventory
* fusioninventory-agent-task-deploy
  Software deployment support
* fusioninventory-agent-task-esx
  vCenter/ESX/ESXi remote inventory
* fusioninventory-agent-task-collect
  Custom information retrieval support
* fusioninventory-agent-task-wakeonlan
  not included due to a licensing issue for perl-Net-Write

%prep
%setup
%patch1 -p1
sed \
    -e "s/logger = .*/logger = syslog/" \
    -e "s/logfacility = .*/logfacility = LOG_DAEMON/" \
    -e 's|#include "conf\.d/"|include "conf\.d/"|' \
    -i etc/agent.cfg

rm -f t/apps/agent.t

%build
perl Makefile.PL \
     PREFIX=%_prefix \
     SYSCONFDIR=%_sysconfdir/fusioninventory \
     LOCALSTATEDIR=%_localstatedir/%name \
     VERSION=%version

%install
%makeinstall_std
install -Dm0755 %SOURCE1 %buildroot%_sysconfdir/cron.hourly/%name
install -Dm0644 %SOURCE2 %buildroot%_unitdir/%name.service
install -Dm0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name

mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_sysconfdir/fusioninventory/conf.d

# Remove Windows-specific modules
rm -rf %buildroot%_datadir/fusioninventory/lib/FusionInventory/Agent/Tools/Win32* \
       %buildroot%_datadir/fusioninventory/lib/FusionInventory/Agent/Task/Deploy/UserCheck/WTS.pm

find %buildroot -name .packlist -delete

%preun
%preun_service %name

%post
%post_service %name

%files
%doc README.md README.Cron THANKS
%config(noreplace) %_sysconfdir/fusioninventory/agent.cfg
%config(noreplace) %_sysconfdir/fusioninventory/conf.d
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/fusioninventory/inventory-server-plugin.cfg
%config(noreplace) %_sysconfdir/fusioninventory/proxy-server-plugin.cfg
%config(noreplace) %_sysconfdir/fusioninventory/proxy2-server-plugin.cfg
%config(noreplace) %_sysconfdir/fusioninventory/server-test-plugin.cfg
%config(noreplace) %_sysconfdir/fusioninventory/ssl-server-plugin.cfg
%_sysconfdir/cron.hourly/%name
%_unitdir/%name.service
%_bindir/fusioninventory*
%_datadir/fusioninventory
%_man1dir/fusioninventory*.1*
%dir %_localstatedir/%name

%changelog
* Mon Dec 16 2019 Andrey Cherepanov <cas@altlinux.org> 2.5.2-alt1
- New version.

* Thu Jul 04 2019 Andrey Cherepanov <cas@altlinux.org> 2.5.1-alt1
- New version.

* Sun Apr 14 2019 Andrey Cherepanov <cas@altlinux.org> 2.5-alt1
- New version.

* Sat Feb 23 2019 Andrey Cherepanov <cas@altlinux.org> 2.4.3-alt1
- New version.

* Thu Dec 27 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.2-alt1
- Initial build for Sisyphus (ALT #35816).
