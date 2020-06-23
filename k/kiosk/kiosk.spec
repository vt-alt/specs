Name: kiosk
Version: 0.3
Release: alt1

Source: %name-%version.tar

Summary: Utility for managing kiosk mode
License: GPLv2+
Group: System/Configuration/Other

BuildRequires: libnl-devel

%description
Utility for managing kiosk mode

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_bindir/kiosk

%changelog
* Fri Jun 19 2020 Oleg Solovyov <mcpain@altlinux.org> 0.3-alt1
- remove system-list restrictions

* Wed Mar 25 2020 Oleg Solovyov <mcpain@altlinux.org> 0.2-alt1
- change netlink family
- fix error messages

* Wed Feb 05 2020 Oleg Solovyov <mcpain@altlinux.org> 0.1-alt1
- initial build for ALT

