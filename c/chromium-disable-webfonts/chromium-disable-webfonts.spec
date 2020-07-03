Name:    chromium-disable-webfonts
Version: 2.0
Release: alt1

Summary: Disable webfonts in Chromium
License: GPL-3.0
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
* Mon Jun 29 2020 Andrey Cherepanov <cas@altlinux.org> 2.0-alt1
- Add parameter to $CHROMIUM_FLAGS instead of $CHROMIUM_USER_FLAGS because
  $CHROMIUM_USER_FLAGS completely overrides system-wide $CHROMIUM_FLAGS.
- Use GPL-3.0 for the code.

* Wed Oct 02 2019 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus.
