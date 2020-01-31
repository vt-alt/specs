Name: alterator-zram-swap
Version: 1.0
Release: alt1

Source: %name-%version.tar

Summary: alterator module for managing zram-swap
License: GPL
Group: System/Configuration/Other
BuildArch: noarch

BuildPreReq: alterator

%description
alterator module for managing zram-swap

%prep
%setup -q

%install
%makeinstall unitdir=%buildroot%_unitdir

%files
%_bindir/*
%_datadir/alterator/applications/*
%_libexecdir/alterator/backend3/*
%_datadir/alterator/ui/*
%_unitdir/*

%changelog
* Fri Jan 17 2020 Ivan Razzhivin <underwit@altlinux.org> 1.0-alt1
- init
