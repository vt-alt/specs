Name: steam
Version: 1.0.0.63
Release: alt1

Summary: Launcher for the Steam software distribution service
License: Proprietary
Group: Games/Other

URL: http://www.steampowered.com/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: %ix86

Source0: http://repo.steampowered.com/%name/pool/%name/s/%name/%{name}_%version.tar.gz
Patch0: %name-apt-alt.patch
Patch1: %name-desktop-alt.patch

Requires: bash >= 4.4
Requires: curl
Requires: glibc-pthread >= 2.15
Requires: glibc-nss >= 2.15
Requires: libdbusmenu-gtk2
Requires: libGL
Requires: libnsl1
Requires: libnss
Requires: xz

%description
Steam is a software distribution service with an online store, automated
installation, automatic updates, achievements, SteamCloud synchronized
savegame and screenshot functionality, and many social features.

%prep
%setup -n %name-launcher
%patch0 -p1
%patch1 -p1

%install
%makeinstall_std
%__rm -rf %buildroot%_bindir/%{name}deps
%__install -Dp -m0644 subprojects/%name-devices/60-%name-input.rules %buildroot%_udevrulesdir/60-%name-input.rules
%__install -Dp -m0644 subprojects/%name-devices/60-%name-vr.rules %buildroot%_udevrulesdir/60-%name-vr.rules

%files
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/*
%_desktopdir/%name.desktop
%dir %_defaultdocdir/%name
%_defaultdocdir/%name/*
%_iconsdir/hicolor/*/apps/%name.png
%_man6dir/%{name}*
%_pixmapsdir/%{name}*.png
%config %_udevrulesdir/60-%name-input.rules
%config %_udevrulesdir/60-%name-vr.rules

%changelog 
* Thu Jun 11 2020 Nazarov Denis <nenderus@altlinux.org> 1.0.0.63-alt1
- Version 1.0.0.63

* Fri Jun 05 2020 Nazarov Denis <nenderus@altlinux.org> 1.0.0.62-alt2
- Remove dirs not related to steam package

* Fri Apr 24 2020 Nazarov Denis <nenderus@altlinux.org> 1.0.0.62-alt1
- Version 1.0.0.62

* Mon Mar 16 2020 Nazarov Denis <nenderus@altlinux.org> 1.0.0.61-alt6
- Remove build requires

* Thu Aug 29 2019 Nazarov Denis <nenderus@altlinux.org> 1.0.0.61-alt5
- Remove symlink on CA certificates

* Fri May 03 2019 Nazarov Denis <nenderus@altlinux.org> 1.0.0.61-alt4
- Fix system tray icon

* Tue Apr 30 2019 Nazarov Denis <nenderus@altlinux.org> 1.0.0.61-alt3
- Add require on libnsl1 (ALT #36376)
- Remove patch bash4

* Sun Apr 28 2019 Nazarov Denis <nenderus@altlinux.org> 1.0.0.61-alt2
- Remove patch udev rules

* Tue Apr 23 2019 Nazarov Denis <nenderus@altlinux.org> 1.0.0.61-alt1
- Version 1.0.0.61

* Tue Jan 15 2019 Nazarov Denis <nenderus@altlinux.org> 1.0.0.59-alt2
- Remove %ubt macro

* Fri Dec 14 2018 Nazarov Denis <nenderus@altlinux.org> 1.0.0.59-alt1%ubt
- Version 1.0.0.59

* Thu Aug 30 2018 Nazarov Denis <nenderus@altlinux.org> 1.0.0.56-alt1%ubt
- Version 1.0.0.56

* Mon Jul 30 2018 Nazarov Denis <nenderus@altlinux.org> 1.0.0.55-alt1%ubt
- Version 1.0.0.55

* Wed Sep 06 2017 Nazarov Denis <nenderus@altlinux.org> 1.0.0.54-alt6%ubt
- Fix connection via SSL (ALT #33849)

* Fri Sep 01 2017 Nazarov Denis <nenderus@altlinux.org> 1.0.0.54-alt5%ubt
- Fix use bash4

* Sat Aug 19 2017 Nazarov Denis <nenderus@altlinux.org> 1.0.0.54-alt4%ubt
- Add patch for desktop-file (ALT #33771)

* Sat Nov 26 2016 Nazarov Denis <nenderus@altlinux.org> 1.0.0.54-alt0.M80P.1
- Build for branch p8

* Sat Nov 26 2016 Nazarov Denis <nenderus@altlinux.org> 1.0.0.54-alt3
- Fix udev rules for correctly emulation gamepad with Steam Controller after reconnect

* Sat Nov 26 2016 Nazarov Denis <nenderus@altlinux.org> 1.0.0.54-alt2
- Add patch to fix udev rules for correctly emulation gamepad with Steam Controller

* Thu Nov 24 2016 Nazarov Denis <nenderus@altlinux.org> 1.0.0.54-alt1
- Version 1.0.0.54

* Sat Oct 29 2016 Nazarov Denis <nenderus@altlinux.org> 1.0.0.53-alt0.M70P.1
- Build for branch p7

* Thu Oct 27 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.0.53-alt0.M80P.1
- Backport new version to p8 branch

* Wed Oct 26 2016 Nazarov Denis <nenderus@altlinux.org> 1.0.0.53-alt1
- Version 1.0.0.53

* Sat Apr 02 2016 Nazarov Denis <nenderus@altlinux.org> 1.0.0.52-alt0.M70P.1
- Build for branch p7

* Sat Apr 02 2016 Nazarov Denis <nenderus@altlinux.org> 1.0.0.52-alt1
- Version 1.0.0.52

* Sat Nov 28 2015 Nazarov Denis <nenderus@altlinux.org> 1.0.0.51-alt0.M70P.1
- Build for branch p7

* Fri Nov 27 2015 Nazarov Denis <nenderus@altlinux.org> 1.0.0.51-alt1
- Version 1.0.0.51

* Wed May 06 2015 Nazarov Denis <nenderus@altlinux.org> 1.0.0.50-alt0.M70P.1
- Build for branch p7

* Wed May 06 2015 Nazarov Denis <nenderus@altlinux.org> 1.0.0.50-alt1
- Version 1.0.0.50

* Fri Sep 19 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0.49-alt1.M70P.1
- Build for branch p7

* Fri Sep 19 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0.49-alt2
- Added require on libnss (fix error "Failed to load NSS libraries")

* Fri Aug 29 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0.49-alt0.M70P.1
- Build for branch p7

* Thu Aug 28 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0.49-alt1
- Version 1.0.0.49

* Fri Jun 20 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0.48-alt0.M70P.1
- Build for branch p7

* Thu Jun 19 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0.48-alt1
- Version 1.0.0.48

* Fri Feb 14 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0.47-alt0.M70P.1
- Build for branch p7

* Fri Feb 14 2014 Nazarov Denis <nenderus@altlinux.org> 1.0.0.47-alt1
- Version 1.0.0.47

* Wed Nov 27 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.45-alt0.M70P.1
- Build for branch p7

* Wed Nov 27 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.45-alt1
- Version 1.0.0.45

* Thu Nov 14 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.44-alt0.M70P.1
- Build for branch p7

* Thu Nov 14 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.44-alt0.M70T.1
- Build for branch t7

* Thu Nov 14 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.44-alt1
- Version 1.0.0.44

* Thu Oct 10 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.43-alt0.M70P.1
- Build for branch p7

* Thu Oct 10 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.43-alt1
- Version 1.0.0.43

* Tue Sep 10 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.42-alt0.M70P.1
- Build for branch p7

* Tue Sep 10 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.42-alt1
- Version 1.0.0.42

* Wed Sep 04 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.41-alt0.M70P.1
- Build for branch p7 (ALT #29322)

* Wed Sep 04 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.41-alt1
- Version 1.0.0.41

* Thu Aug 29 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.40-alt0.M70P.1
- Build for branch p7

* Thu Aug 29 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.40-alt1
- Version 1.0.0.40

* Sun May 12 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.39-alt0.M70P.1
- Build for branch p7

* Sat May 11 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.39-alt1
- Version 1.0.0.39

* Sun May 05 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.38-alt0.M70P.1
- Build for branch p7

* Sat Apr 27 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.38-alt1
- Version 1.0.0.38

* Wed Apr 24 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.37-alt1
- Version 1.0.0.37

* Wed Mar 13 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.36-alt1
- Version 1.0.0.36

* Wed Mar 06 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.35-alt2
- Fix resolved DNS on x86_64 (ALT #28640)

* Sat Mar 02 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.35-alt1
- Version 1.0.0.35

* Mon Feb 25 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.34-alt1
- Version 1.0.0.34
- Added requires on curl and xz

* Sun Feb 24 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.33-alt2
- Fix summary title

* Sun Feb 24 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.33-alt1
- Version 1.0.0.33

* Wed Feb 20 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.29-alt1
- Version 1.0.0.29

* Sat Feb 16 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.28-alt1
- Version 1.0.0.28
- Added require on mozilla-plugin-adobe-flash

* Fri Feb 15 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.27-alt1
- Version 1.0.0.27

* Mon Feb 11 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.25-alt2
- Fix end of line in desktop file

* Sun Feb 10 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.25-alt1
- Initial build for ALT Linux

