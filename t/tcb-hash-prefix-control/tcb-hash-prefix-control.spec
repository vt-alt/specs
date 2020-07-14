Name: tcb-hash-prefix-control
Version: 1.1
Release: alt1

Summary: Password hashing facilities control
License: GPL
Group: System/Servers
BuildArch: noarch

Source0: tcb-hash-prefix.control

%description
This package contains control rules for password hashing facilities.
See control(8) for details.

%install
install -pD -m755 %SOURCE0 %buildroot%_controldir/tcb-hash-prefix

%files
%config %_controldir/*

%changelog
* Mon Jul 13 2020 Slava Aseev <ptrnine@altlinux.org> 1.1-alt1
- Fix with the new pam-config, allow adding hash prefixes

* Mon Feb 03 2020 Slava Aseev <ptrnine@altlinux.org> 1.0-alt1
- Initial build for ALT

