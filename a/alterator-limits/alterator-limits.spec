Name: alterator-limits
Version: 0.1
Release: alt1

Source: %name-%version.tar

Summary: alterator module for managing limits
License: GPLv2+
Group: System/Configuration/Other
BuildArch: noarch

BuildRequires: alterator

%define limitsdir %_sysconfdir/security/limits.d

%description
alterator module for managing limits

%prep
%setup -q

%install
%makeinstall

mkdir -p %buildroot%limitsdir/
touch %buildroot%limitsdir/95-alterator-limits.conf

%files
%_datadir/alterator/applications/*
%_libexecdir/alterator/backend3/*
%_datadir/alterator/ui/*
%config(noreplace) %limitsdir/95-alterator-limits.conf

%changelog
* Fri Jul 24 2020 Oleg Solovyov <mcpain@altlinux.org> 0.1-alt1
- initial build for ALT

