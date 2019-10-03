%def_disable palemoon

Name: update-pepperflash
Version: 1.6
Release: alt2

Summary: Pepper Flash Player legacy package
License: GPLv3+
Group: Networking/WWW
Url: http://altlinux.org/PepperFlash

ExclusiveArch: %ix86 x86_64

Source1: update-pepperflash

%description
This package contains update-pepperflash program which currently does
nothing, rely on ppapi-plugin-adobe-flash packeage.

%package -n chromium-pepperflash
Summary: Pepper Flash Player - browser plugin for Chromium
Group: Networking/WWW
Requires: ppapi-plugin-adobe-flash
Requires: chromium

%description -n chromium-pepperflash
Pepper Flash Player - browser plugin for Chromium (virtual package)

%package -n firefox-pepperflash
Summary: Pepper Flash Player - browser plugin for Firefox
Group: Networking/WWW
Requires: /usr/bin/firefox
Requires: ppapi-plugin-adobe-flash
Requires: freshplayerplugin

%description -n firefox-pepperflash
Pepper Flash Player - browser plugin for Firefox (virtual package)

%package -n palemoon-pepperflash
Summary: Pepper Flash Player - browser plugin for Pale Moon
Group: Networking/WWW
Requires: palemoon
Requires: ppapi-plugin-adobe-flash
Requires: freshplayerplugin

%description -n palemoon-pepperflash
Pepper Flash Player - browser plugin for Firefox (virtual package)

%prep
%install
install -D -m 0755 %SOURCE1 %buildroot%_sbindir/update-pepperflash
mkdir -p %buildroot%_libdir/pepper-plugins
touch %buildroot%_libdir/pepper-plugins/libpepflashplayer.so
mkdir -p %buildroot%_cachedir/pepperflash

%preun
[ "$1" -eq "0" ] && %_sbindir/update-pepperflash --uninstall --quiet ||:
exit 0

%files
%_sbindir/update-pepperflash
%dir %_cachedir/pepperflash

%files -n chromium-pepperflash
%files -n firefox-pepperflash
%if_enabled palemoon
%files -n palemoon-pepperflash
%endif

%changelog
* Wed Oct 02 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.6-alt2
- Dropped palemoon subpackage.
- Added ExclusiveArch tag to limit architectures to x86-only.

* Thu Sep 29 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.6-alt1
- Added R: ppapi-plugin-adobe-flash.
- Removed all download code (ALT#32540).
- Fixed uninstall mode (ALT#32517)

* Mon Apr 11 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1.5.4-alt2
- Fixed the  Requires to the  palemoon

* Fri Dec 04 2015 Andrey Cherepanov <cas@altlinux.org> 1.5.4-alt1
- Replace strings  call by sed regexp (do not require binutils)

* Tue Dec 01 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.5.3-alt3
- Add palemoon-pepperflash virtual package.

* Fri Oct 23 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.5.3-alt2.1
- Bumped release to force PPAPI flashplayer upgrade.

* Wed Jul 15 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.5.3-alt2
- Bumped release to force pepflashplayer upgrade.

* Tue Mar 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.5.3-alt1
- update-pepperflash:
 + Cleanup cache dir after successful installation.
 + Change dl.google.com URLs to https.
- Rename main package to to update-pepperflash.
- Add {chromium,firefox}-pepperflash virtual packages.

* Tue Oct 14 2014 Andrey Cherepanov <cas@altlinux.org> 1.5.2-alt3
- Force update from alt2 to prevent wrong %%preun trigger

* Mon Oct 13 2014 Andrey Cherepanov <cas@altlinux.org> 1.5.2-alt2
- Do not remove plugin on update

* Thu Oct 09 2014 Andrey Cherepanov <cas@altlinux.org> 1.5.2-alt1
- Use only IPv4 for curl (fix hang up in %%post script)
- Show status on %%post section

* Tue Sep 16 2014 Andrey Cherepanov <cas@altlinux.org> 1.5.1-alt1
- Fix version detect in new plugin versions
- Add arguments --clean and --version
- Change plugin location to %%_libdir/pepper-plugins

* Mon Sep 01 2014 Andrey Cherepanov <cas@altlinux.org> 1.5-alt3
- Remove unnecessary require of glibc-utils

* Fri Aug 29 2014 Andrey Cherepanov <cas@altlinux.org> 1.5-alt2
- Mark plugin file as %%ghost file (ALT #30225)
- Package cache directory

* Tue Jul 29 2014 Andrey Cherepanov <cas@altlinux.org> 1.5-alt1
- Initial build in Sisyphus adapted from Debian

