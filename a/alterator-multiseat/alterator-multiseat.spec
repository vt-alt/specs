Name: alterator-multiseat
Version: 0.0.3
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
* Fri Apr 16 2021 Ivan Razzhivin <underwit@altlinux.org> 0.0.3-alt1
- disable saving configuration
- hide /drm/card0
- fix popup message (closes: #39916)
- fix help

* Tue Apr 13 2021 Ivan Razzhivin <underwit@altlinux.org> 0.0.2-alt1
- disable test activation (closes: #39911)
- add multiple selection in the device list (closes: #39915)
- show a message box when activated (closes: #39916)
- flush-devices when remove seat (closes: #39913)
- rename buttons (closes: #39918, #39912)
- update help (closes: #39910, #39914)

* Wed Mar 10 2021 Ivan Razzhivin <underwit@altlinux.org> 0.0.1-alt1
- init
