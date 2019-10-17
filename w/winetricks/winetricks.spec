Name: winetricks
Version: 20190912
Release: alt1

Summary: Work around common problems in Wine

License: LGPLv2+
Group: File tools
Url: https://github.com/Winetricks/winetricks

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

ExclusiveArch: %ix86 x86_64 %arm aarch64

#BuildRequires: wine-common
BuildRequires: desktop-file-utils

# runtime dependencies
#Requires: /usr/bin/wine
Requires: cabextract gzip unzip wget which

#Requires: hicolor-icon-theme
Conflicts: wine-vanilla < 3.18
Conflicts: wine < 3.18
Conflicts: wine-etersoft < 4.0

%description
Winetricks is an easy way to work around common problems in Wine.

It has a menu of supported games/apps for which it can do all the
workarounds automatically. It also lets you install missing DLLs
or tweak various Wine settings individually.
 
%prep
%setup

# fix req. Disable autoreq at all?
%__subst 's|fusermount|a= fusermount|' src/winetricks

sed -i -e "s:steam::" -e "s:flash::" tests/*

%build
# not needed

%install
%makeinstall_std
# some tarballs do not install appdata
install -m0644 -D -t %buildroot%_datadir/metainfo src/%name.appdata.xml

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop

%files
%doc COPYING debian/copyright
%doc README.md
%_bindir/%name
%_man1dir/%name.1*
%_iconsdir/hicolor/scalable/apps/%name.svg
%_desktopdir/%name.desktop
%_datadir/metainfo/%name.appdata.xml
%_datadir/bash-completion/completions/winetricks
#exclude %_datadir/appdata/%name.appdata.xml

%changelog
* Thu Sep 26 2019 Vitaly Lipatov <lav@altlinux.ru> 20190912-alt1
- new version 20190912 (with rpmrb script)

* Sat Jun 22 2019 Vitaly Lipatov <lav@altlinux.ru> 20190615-alt1
- new version 20190615 (with rpmrb script)

* Fri Apr 19 2019 Vitaly Lipatov <lav@altlinux.ru> 20190310-alt2
- fix wine-etersoft conflicts

* Mon Mar 18 2019 Vitaly Lipatov <lav@altlinux.ru> 20190310-alt1
- new version 20190310 (with rpmrb script)

* Wed Dec 19 2018 Vitaly Lipatov <lav@altlinux.ru> 20181203-alt2
- fix zenity/kdialog requires (ALT bug 35750)

* Fri Dec 07 2018 Vitaly Lipatov <lav@altlinux.ru> 20181203-alt1
- new version 20181203 (with rpmrb script)

* Sat Oct 13 2018 Vitaly Lipatov <lav@altlinux.ru> 20180815-alt1
- new version (20180815) with rpmgs script

* Sat Oct 13 2018 Vitaly Lipatov <lav@altlinux.ru> 20180603-alt1
- initial build for ALT Sisyphus

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180603-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Raphael Groner <projects.rg@smart.ms> - 20180603-2
- avoid shebang warning of rpmlint for appdata

* Sat Jun 23 2018 Raphael Groner <projects.rg@smart.ms> - 20180603-1
- new version

* Mon Mar 05 2018 Raphael Groner <projects.rg@smart.ms> - 20180217-1
- new version
- drop obsolete scriptlets
- move appdata into mimeinfo

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171222-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Ben Rosser <rosser.bjr@gmail.com> - 20171222-1
- Updated to latest upstream release. (#1528622)
- Moved appdata file to new appdata location, /usr/share/metainfo.
- Removed dependency on 'time' package as per #1533795.

* Sun Dec 03 2017 Raphael Groner <projects.rg@smart.ms> - 20171018-1
- new version
- ensure appdata gets installed

* Sun Aug 13 2017 Raphael Groner <projects.rg@smart.ms> - 20170731-1
- new snapshot
- add appdata

* Sun Aug 13 2017 Raphael Groner <projects.rg@smart.ms> - 20170614-1
- new version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170517-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Raphael Groner <projects.rg@smart.ms> - 20170517-1
- new version

* Tue Mar 28 2017 Raphael Groner <projects.rg@smart.ms> - 20170326-1
- new version

* Sat Feb 11 2017 Raphael Groner <projects.rg@smart.ms> - 20170207-1
- new version
- drop additional icon and desktop file in favor of upstream ones

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20161107-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 05 2016 Builder <projects.rg@smart.ms> - 20161107-2
- add ExcludeArch

* Wed Nov 09 2016 Raphael Groner <projects.rg@smart.ms> - 20161107-1
- new version

* Mon Nov 07 2016 Raphael Groner <projects.rg@smart.ms> - 20161012-1
- new version
- disable architectures without available wine
- don't check explicitly for wine version

* Sun Oct 09 2016 Raphael Groner <projects.rg@smart.ms> - 20161005-2
- use apps subfolder for icon

* Sun Oct 09 2016 Raphael Groner <projects.rg@smart.ms> - 20161005-1
- new version
- add copyright
- add icon

* Fri Jul 29 2016 Raphael Groner <projects.rg@smart.ms> - 20160724-1
- new version

* Mon Jul 11 2016 Raphael Groner <projects.rg@smart.ms> - 20160709-1
- initial
