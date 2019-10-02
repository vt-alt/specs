Name:    chromium-disable-webfonts
Version: 1.0
Release: alt1

Summary: Disable webfonts in Chromium
License: GPL
Group:   Networking/WWW
URL:     http://altlinux.org
Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

Source1:  %name.sh

%description
Completely disable webfonts in Chromium (run chromium with
--disable-remote-fonts).

%install
install -Dm0755 %SOURCE1 %buildroot%_sysconfdir/profile.d/%name.sh

%files
%attr(0755,root,root) %_sysconfdir/profile.d/%name.sh

%changelog
* Wed Oct 02 2019 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus.
