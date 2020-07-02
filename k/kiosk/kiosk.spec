Name: kiosk
Version: 0.4
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
%make_build all

%install
%makeinstall
%find_lang kiosk

%files -f kiosk.lang
%_bindir/kiosk
%_man1dir/kiosk.1.xz

%changelog
* Mon Jun 29 2020 Oleg Solovyov <mcpain@altlinux.org> 0.4-alt1
- translate kiosk, add manpages

* Fri Jun 19 2020 Oleg Solovyov <mcpain@altlinux.org> 0.3-alt1
- remove system-list restrictions

* Wed Mar 25 2020 Oleg Solovyov <mcpain@altlinux.org> 0.2-alt1
- change netlink family
- fix error messages

* Wed Feb 05 2020 Oleg Solovyov <mcpain@altlinux.org> 0.1-alt1
- initial build for ALT

