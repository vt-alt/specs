Name: blueberry
Version: 1.2.9
Release: alt1
Summary: A Bluetooth configuration tool
License: GPLv3
Group: System/Configuration/Hardware
Url: https://github.com/linuxmint/blueberry

Obsoletes: blueman
Provides: blueman

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-gir rpm-build-python3
%add_python3_path %_datadir/%name
%add_typelib_req_skiplist typelib(St)


BuildArch: noarch
Requires: rfkill wmctrl gnome-bluetooth bluez-tools

%description
Utility for Bluetooth devices graphical configuration

%package -n cinnamon-applet-%name
Summary: Blueberry applet for Cinnamon
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: %name = %version-%release

%description -n cinnamon-applet-%name
Blueberry applet for Cinnamon

%prep
%setup
%patch0 -p1

%build
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_sysconfdir/xdg/autostart/%name-tray.desktop
%_sysconfdir/xdg/autostart/%name-obex-agent.desktop
%_bindir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/*.xml
%_iconsdir/hicolor/*/status/*

%files -n cinnamon-applet-%name
%_datadir/cinnamon/applets/blueberry@cinnamon.org

%changelog
* Thu Aug 1 2019 Vladimir Didenko <cow@altlinux.org> 1.2.9-alt1
- 1.2.9

* Wed Jul 10 2019 Vladimir Didenko <cow@altlinux.org> 1.2.7-alt1
- 1.2.7

* Mon Jul 1 2019 Vladimir Didenko <cow@altlinux.org> 1.2.6-alt1
- 1.2.6

* Mon Jun 17 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.5-alt5
- added %_datadir/blueberry to _python3_path
- added typelib(St) provided by gnome-shell to _typelib_req_skiplist

* Mon Jun 17 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.5-alt4
- fixed {Build,}Requires

* Mon Jun 17 2019 Vladimir Didenko <cow@altlinux.org> 1.2.5-alt3
- update to the git82682e9f for python3 build (closes: #36908)

* Fri Apr 5 2019 Vladimir Didenko <cow@altlinux.org> 1.2.5-alt2
- add libnotify-gir to requires and fix Makefile to install
  obex-agent desktop file (fixes: #36451)
- fix path in /usr/lib/blueberry/* files (fixes: #36487)

* Wed Dec 26 2018 Vladimir Didenko <cow@altlinux.org> 1.2.5-alt1
- 1.2.5

* Wed Dec 5 2018 Vladimir Didenko <cow@altlinux.org> 1.2.4-alt1
- 1.2.4

* Fri Oct 26 2018 Pavel Moseev <mars@altlinux.org> 1.2.3-alt2
- Updated translations

* Wed Jul 4 2018 Vladimir Didenko <cow@altlinux.org> 1.2.3-alt1
- 1.2.3

* Thu May 31 2018 Vladimir Didenko <cow@altlinux.org> 1.2.1-alt1
- 1.2.1

* Tue May 8 2018 Vladimir Didenko <cow@altlinux.org> 1.2.0-alt1
- 1.2.0

* Tue Dec 26 2017 Vladimir Didenko <cow@altlinux.org> 1.1.20-alt1
- 1.1.20

* Thu Nov 23 2017 Vladimir Didenko <cow@altlinux.org> 1.1.18-alt1
- 1.1.18

* Mon Oct 30 2017 Vladimir Didenko <cow@altlinux.org> 1.1.16-alt1
- 1.1.16

* Thu Jun 29 2017 Vladimir Didenko <cow@altlinux.org> 1.1.15-alt1
- 1.1.15

* Wed Jun 7 2017 Vladimir Didenko <cow@altlinux.org> 1.1.12-alt1
- 1.1.12

* Fri May 19 2017 Vladimir Didenko <cow@altlinux.org> 1.1.11-alt1
- 1.1.11

* Mon Mar 6 2017 Vladimir Didenko <cow@altlinux.org> 1.1.10-alt1
- 1.1.10

* Wed Dec 14 2016 Vladimir Didenko <cow@altlinux.org> 1.1.9-alt1
- 1.1.9

* Thu Nov 24 2016 Vladimir Didenko <cow@altlinux.org> 1.1.8-alt1
- 1.1.8
- add gnome-bluetooth to requires

* Tue Jul 12 2016 Valery Inozemtsev <shrek@altlinux.ru> 1.1.5-alt1
- 1.1.5
- obsoletes blueman
- updates tray icons

* Fri Dec 18 2015 Vladimir Didenko <cow@altlinux.org> 1.1.0-alt1
- 1.1.0

* Sat Jun 27 2015 Vladimir Didenko <cow@altlinux.org> 1.0.9-alt2
- add wmctrl to deps

* Sat Jun 27 2015 Vladimir Didenko <cow@altlinux.org> 1.0.9-alt1
- 1.0.9
- added missed deps (closes: #31108)

* Fri Mar 27 2015 Vladimir Didenko <cow@altlinux.org> 1.0.3-alt1
- initial release
