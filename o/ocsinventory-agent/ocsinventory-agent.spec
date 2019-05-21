Name: ocsinventory-agent
Version: 2.6.0
Release: alt1
Epoch: 1

Summary: Hardware and software inventory tool (Agent)
Group: System/Servers
License: GPL
Url: http://www.ocsinventory-ng.org/

Packager: Pavel Zilke <zidex at altlinux dot org>

BuildArch: noarch

Source0: %name-%version.tar
Source1: README.ALT

Requires: smartmontools nmap pciutils perl-XML-Simple perl-libwww perl-Net-IP perl-Net-SSLeay

BuildRequires: smartmontools
BuildRequires: nmap
BuildRequires: pciutils
BuildRequires: perl-XML-Simple
BuildRequires: perl-devel
BuildRequires: perl-libwww
BuildRequires: perl-Net-IP
BuildRequires: perl-Pod-Parser
BuildRequires: perl-IO-Socket-SSL
BuildRequires: perl-Parse-EDID

%description
Open Computer and Software Inventory Next Generation is an application
designed to help a network or system administrator keep track of the
computers configuration and software that are installed on the network.

Information about Hardware and Operating System are collected.
OCS Inventory is also able to detect all active devices on your network,
such as switch, router, network printer and unattended devices.
It also allows deploying softwares, commands or files on client computers.

This package contains the 'Agent' part.

%prep
%setup

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
mkdir -p %buildroot{%_sysconfdir/{ocsinventory,logrotate.d,cron.daily},%_datadir/%name,%_localstatedir/%name/{ipd,download},%_var/log/%name}
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%perl_vendorlib
mkdir -p %buildroot%_man1dir

cp %name %buildroot%_bindir
cp -rf ./blib/lib/Ocsinventory %buildroot%perl_vendorlib
cp -rf ./blib/man1/* %buildroot%_man1dir

cat <<EOF >%buildroot%_sysconfdir/logrotate.d/%name
%_var/log/%name/*.log {
	daily
	rotate 7
	compress
	notifempty
	missingok
}
EOF

cat <<EOF >%buildroot%_sysconfdir/ocsinventory/ocsinventory-agent.cfg
basevardir = %_var/lib/ocsinventory-agent
logger  = File
logfile = %_var/log/ocsinventory-agent/ocsinventory-agent.log
server = localhost
EOF

cat <<EOF >%buildroot%_sysconfdir/cron.daily/ocsinventory-agent
#!/bin/sh
PATH=/bin:/usr/bin:/sbin:/usr/sbin
exec %_bindir/ocsinventory-agent --lazy > /dev/null 2>&1
EOF

#install README.ALT
install -pD -m0644 %_sourcedir/README.ALT README.ALT

# cleanup
rm -f %buildroot%perl_vendorlib/Ocsinventory/postinst.pl

%files
%defattr(-,root, root)
%doc AUTHORS Changes LICENSE README* THANKS
%doc README.ALT
%_man1dir/%name.*
%config(noreplace) %attr(0750,root,root) %_sysconfdir/cron.daily/%name
%config(noreplace) %_sysconfdir/logrotate.d/%name
%config(noreplace) %_sysconfdir/ocsinventory
%attr(0755,root,root) %_bindir/%name
%perl_vendorlib/Ocsinventory
%_var/log/%name
%_var/lib/%name

%changelog
* Tue May 21 2019 Andrey Cherepanov <cas@altlinux.org> 1:2.6.0-alt1
- New version.

* Tue Sep 25 2018 Andrey Cherepanov <cas@altlinux.org> 1:2.4.2-alt1
- New version.

* Wed Dec 01 2010 Pavel Zilke <zidex at altlinux dot org> 1:1.1.2-alt2
- Fixed build

* Fri Mar 05 2010 Pavel Zilke <zidex at altlinux dot org> 1:1.1.2-alt1
- New version 1.1.2

* Wed Jan 06 2010 Pavel Zilke <zidex at altlinux dot org> 1.02-alt5
- Fixed #22617

* Tue Dec 22 2009 Pavel Zilke <zidex at altlinux dot org> 1.02-alt4
- Fixed cron.daily

* Tue Dec 15 2009 Pavel Zilke <zidex at altlinux dot org> 1.02-alt3
- Fixed error unsafe-tmp-usage-in-scripts

* Tue Nov 24 2009 Pavel Zilke <zidex at altlinux dot org> 1.02-alt2
- Added README.ALT

* Tue Nov 03 2009 Pavel Zilke <zidex at altlinux dot org> 1.02-alt1
- Initial build for ALT Linux



