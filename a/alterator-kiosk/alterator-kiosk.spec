Name: alterator-kiosk
Version: 1.5
Release: alt2

Source: %name-%version.tar
Source1: activate-kiosk.sh
Source2: kiosk.service

Summary: alterator module for managing kiosk mode
License: GPLv2+
Group: System/Configuration/Other
BuildArch: noarch

BuildRequires: alterator
Requires: kiosk
Requires: kiosk-profiles = %EVR

%description
alterator module for managing kiosk mode

%package -n kiosk-profiles
Summary: profiles for kiosk
License: GPLv2+
Group: System/Configuration/Other
BuildArch: noarch

%description -n kiosk-profiles
profiles for kiosk

%prep
%setup -q

%install
%makeinstall
install -Dm 0755 %SOURCE1 %buildroot%_bindir/activate-kiosk.sh
install -Dm 0644 %SOURCE2 %buildroot%_unitdir/kiosk.service

%post
%post_service kiosk

%preun
%preun_service kiosk

%files
%_sysconfdir/alterator/kiosk/
%exclude %_sysconfdir/alterator/kiosk/profiles/
%_datadir/alterator/applications/*
%_libexecdir/alterator/backend3/*
%_datadir/alterator/ui/*
%_unitdir/kiosk.service
%_bindir/activate-kiosk.sh

%files -n kiosk-profiles
%_sysconfdir/alterator/kiosk/profiles/

%changelog
* Fri Aug 28 2020 Oleg Solovyov <mcpain@altlinux.org> 1.5-alt2
- require kiosk-profiles

* Tue Aug 25 2020 Oleg Solovyov <mcpain@altlinux.org> 1.5-alt1
- add chromium to profiles
- make a new package with profiles

* Wed Jul 08 2020 Ivan Razzhivin <underwit@altlinux.org> 1.4-alt1
- remove kiosk mode

* Mon Jun 22 2020 Oleg Solovyov <mcpain@altlinux.org> 1.3-alt1
- KDE: fix profiles
- enable service when committing changes

* Mon Jun 22 2020 Oleg Solovyov <mcpain@altlinux.org> 1.2-alt2
- add service

* Fri Jun 19 2020 Oleg Solovyov <mcpain@altlinux.org> 1.2-alt1
- remove system restrictions

* Wed Mar 25 2020 Oleg Solovyov <mcpain@altlinux.org> 1.1-alt1
- remove altha from error message

* Mon Jan 27 2020 Ivan Razzhivin <underwit@altlinux.org> 1.0-alt1
- init


