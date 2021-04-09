Name: alterator-multiseat
Version: 0.0.1
Release: alt1

Source: %name-%version.tar

Summary: alterator module for setup multiseat configuration
License: GPL
Group: System/Configuration/Other

BuildPreReq: alterator

BuildArch: noarch

%description
alterator module for setup multiseat configuration

%prep
%setup -q

%build


%install
%makeinstall 


%files
%_datadir/alterator/applications/*
%_libexecdir/alterator/backend3/*
%_datadir/alterator/ui/*

%changelog
* Wed Mar 10 2021 Ivan Razzhivin <underwit@altlinux.org> 0.0.1-alt1
- init
