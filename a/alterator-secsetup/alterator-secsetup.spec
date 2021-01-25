Name: alterator-secsetup
Version: 2.0
Release: alt3

Source: %name-%version.tar

Summary: alterator module for managing security settings
License: GPL
Group: System/Configuration/Other

BuildPreReq: alterator
Requires: tcb-hash-prefix-control

AutoReq: no

BuildArch: noarch

%description
alterator module for managing security settings

%prep
%setup -q

%build
%make_build

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
%dir %_datadir/alterator-secsetup
%_datadir/alterator-secsetup/*

%changelog
* Tue Jan 19 2021 Danil Shein <dshein@altlinux.org> 2.0-alt3
- fixed LibreOffice extension installer path

* Tue Jan 19 2021 Danil Shein <dshein@altlinux.org> 2.0-alt2
- fixed secsetup-macrosblocker script failure if VLC files not found

* Fri Jan 15 2021 Danil Shein <dshein@altlinux.org> 2.0-alt1
- new macros blocker helper executable (Closes: #37893)
  + helper executable modifies LibreOffice menu xml files
  + macros security level settings managed with LibreOffice extension

* Tue Aug 25 2020 Ivan Razzhivin <underwit@altlinux.org> 1.18-alt1
- fix translation

* Mon Aug 24 2020 Ivan Razzhivin <underwit@altlinux.org> 1.17-alt1
- change capital case to lowercase

* Mon Aug 03 2020 Ivan Razzhivin <underwit@altlinux.org> 1.16-alt1
- fix checkbox label

* Mon Jul 13 2020 Slava Aseev <ptrnine@altlinux.org> 1.15-alt1
- Set 'default' hash prefix instead of 'bcrypt_2y' if gost_yescrypt disabled

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
