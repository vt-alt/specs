Name: alterator-setup-kworkstation
Version: 0.0.1
Release: alt1

Summary: Perform initial setup of an OEM installation
License: GPLv2
Group: System/Configuration/Other

Url: http://www.altlinux.org/Alterator
Source: %name-%version.tar

BuildArch: noarch

Requires: alterator-setup
Requires: alterator-notes
Requires: alterator-sysconfig
Requires: alterator-datetime
Requires: alterator-root
Requires: alterator-users
Requires: alterator-net-eth
Requires: alterator-net-wifi


%description
%summary

%prep
%setup

%install
install -pD -m755 custom.steps %buildroot%_sysconfdir/%name/custom.steps
cp -a steps %buildroot%_sysconfdir/%name/
install -pD -m755 93-remove-package.sh %buildroot%_libexecdir/alterator/hooks/setup-postinstall.d/93-remove-package.sh
install -pD -m755 70-copy-connections.sh %buildroot%_libexecdir/alterator/hooks/setup-postinstall.d/70-copy-connections.sh

%files
%_sysconfdir/%name/custom.steps
%_sysconfdir/%name/steps/*
%_libexecdir/alterator/hooks/setup-postinstall.d/93-remove-package.sh
%_libexecdir/alterator/hooks/setup-postinstall.d/70-copy-connections.sh

%post
/usr/bin/cat %_sysconfdir/%name/custom.steps > %_sysconfdir/alterator-setup/steps
/bin/cp -r -u %_sysconfdir/%name/steps %_datadir/alterator/

%changelog
* Fri Nov 06 2020 Ivan Razzhivin <underwit@altlinux.org> 0.0.1-alt1
- init
