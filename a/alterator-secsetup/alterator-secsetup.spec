Name: alterator-secsetup
Version: 1.14
Release: alt1

Source: %name-%version.tar

Summary: alterator module for managing security settings
License: GPL
Group: System/Configuration/Other

BuildPreReq: alterator
BuildRequires: gcc gcc-c++ gcc-c++-common librpm-devel 
Requires: tcb-hash-prefix-control

AutoReq: no

%description
alterator module for managing security settings

%prep
%setup -q

%build
%make_build RPM_V413=$(rpm --version | cut -d. -f2) LIBDIR=%_libdir

%install
%makeinstall 
mkdir -p -m 0755 %buildroot%_unitdir
install -m 0644 macrosblock.service %buildroot%_unitdir/
mkdir -p -m 0755 %buildroot%_sysctldir/
install -m 0644 secsetup.conf %buildroot%_sysctldir/

%files
%_bindir/*
%_datadir/alterator/applications/*
%_libexecdir/alterator/backend3/*
%_datadir/alterator/ui/*
%_unitdir/*
%config(noreplace) %_sysctldir/*

%changelog
* Tue Jul 07 2020 Ivan Razzhivin <underwit@altlinux.org> 1.14-alt1
- add the ability to enable/disable pam_access.so
- update translation

* Tue Mar 31 2020 Ivan Razzhivin <underwit@altlinux.org> 1.13-alt1
- set right path to the help

* Tue Feb 04 2020 Slava Aseev <ptrnine@altlinux.org> 1.12-alt1
- Add checkbox for enabling gost_yescrypt hashing algorithm

* Wed Jan 22 2020 Ivan Razzhivin <underwit@altlinux.org> 1.11-alt1
- fix ui text
- update translation

* Fri Jan 17 2020 Ivan Razzhivin <underwit@altlinux.org> 1.10-alt1
- fix desktop file

* Wed Jan 15 2020 Ivan Razzhivin <underwit@altlinux.org> 1.9-alt1
- ui fix

* Wed Jan 15 2020 Ivan Razzhivin <underwit@altlinux.org> 1.8-alt1
- if user is not selected do not show tty list
- multiselect for tty
- correct user list
- correct tty list

* Fri Jan 10 2020 Ivan Razzhivin <underwit@altlinux.org> 1.7-alt1
- small fixes

* Fri Jan 10 2020 Ivan Razzhivin <underwit@altlinux.org> 1.6-alt1
- add localization

* Fri Jan 10 2020 Ivan Razzhivin <underwit@altlinux.org> 1.5-alt1
- add tty blocking

* Wed Dec 25 2019 Ivan Razzhivin <underwit@altlinux.org> 1.4-alt1
- add button apply
- show message if the alt hardening module is inactive

* Fri Dec 13 2019 Ivan Razzhivin <underwit@altlinux.org> 1.3-alt1
- add sysctl default config for AltHa
- settings are saved after reboot

* Thu Dec 12 2019 Ivan Razzhivin <underwit@altlinux.org> 1.2-alt1
- add additional parameters

* Wed Dec 11 2019 Ivan Razzhivin <underwit@altlinux.org> 1.1-alt1
- add support AltHa (Alt Hardening)

* Mon Nov 18 2019 Ivan Razzhivin <underwit@altlinux.org> 1.0-alt1
- initial build
