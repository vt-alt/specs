%def_disable bootstrap

Name: xfce4
Version: 4.14
Release: alt7
Summary: Set of Xfce4 Desktop installers.
License: %gpl2plus
Group: Graphical desktop/XFce
URL: http://www.xfce.org
Packager: Xfce Team <xfce@packages.altlinux.org>


BuildRequires(pre): rpm-build-licenses

%description
A set of virtual packages for Xfce4 Desktop installation.

%package common
Summary: Common directories for Xfce4 Desktop Environment.
Group: Graphical desktop/XFce

%description common
This package contains common directories for Xfce4 Desktop
Environment.

%package minimal
Summary: Minimal installation of Xfce4 Desktop
Summary(ru_RU.UTF8): Минимальная установка Xfce4
Group: Graphical desktop/XFce
BuildArch: noarch
Requires: xfce4-panel
Requires: xfce4-session
Requires: xfce4-settings
Requires: xfconf-utils
Requires: xfdesktop
Requires: xfwm4

%description minimal
%name-minimal is a virtual package to provide minimal installation
of Xfce4 Desktop.

%description -l ru_RU.UTF8
%name-minimal устанавливает минимальный набор пакетов необходимых
для работы с окружением рабочего стола Xfce 4.

%package default
Summary: Default installation of Xfce4 Desktop
Group: Graphical desktop/XFce
BuildArch: noarch
Requires: %name-minimal = %version-%release
Requires: xfce4-power-manager
Requires: xfce4-appfinder
Requires: xfce4-notifyd
Requires: xfce4-taskmanager
Requires: xfce4-terminal
Requires: tumbler
Requires: thunar
Requires: thunar-volman-plugin
Requires: thunar-media-tags-plugin
Requires: thunar-archive-plugin
# Icon themes
Requires: icon-theme-adwaita
# It was proposed as default GTK theme for Xfce-4.14.
Requires: gtk2-theme-greybird
Requires: gtk3-theme-greybird
Requires: xfwm4-theme-greybird
Requires: xfce4-notifyd-theme-greybird
# for trash and network in Thunar
Requires: gvfs gvfs-backends

%description default
%name-default is a virtual package to provide default installation
of Xfce4 Desktop.

%define commonreqs \
Requires: xfwm4-themes \
Requires: xfce4-dict \
Requires: orage \
Requires: xfce4-screenshooter \
Requires: xarchiver \
Requires: ristretto \
Requires: mousepad \
Requires: parole \
Requires: xfce4-panel-profiles \
# Panel plugins \
Requires: xfce4-battery-plugin \
Requires: xfce4-calculator-plugin \
Requires: xfce4-clipman-plugin \
Requires: xfce4-cpufreq-plugin \
Requires: xfce4-cpugraph-plugin \
Requires: xfce4-datetime-plugin \
Requires: xfce4-diskperf-plugin \
Requires: xfce4-eyes-plugin \
Requires: xfce4-fsguard-plugin \
Requires: xfce4-genmon-plugin \
Requires: xfce4-hardware-monitor-plugin \
Requires: xfce4-kbdleds-plugin \
Requires: xfce4-mailwatch-plugin \
Requires: xfce4-mount-plugin \
Requires: xfce4-netload-plugin \
Requires: xfce4-notes-plugin \
Requires: xfce4-places-plugin \
Requires: xfce4-sensors-plugin \
Requires: xfce4-smartbookmark-plugin \
Requires: xfce4-stopwatch-plugin \
Requires: xfce4-systemload-plugin \
Requires: xfce4-time-out-plugin \
Requires: xfce4-timer-plugin \
Requires: xfce4-verve-plugin \
Requires: xfce4-weather-plugin \
Requires: xfce4-whiskermenu-plugin \
Requires: xfce4-xkb-plugin

%package full
Summary: Full installation of Xfce4 Desktop
Group: Graphical desktop/XFce
BuildArch: noarch
Requires: %name-default = %version-%release
Requires: xfce-polkit
Requires: xfce4-screensaver
Requires: desktop-screensaver-modules-xscreensaver
Requires: desktop-screensaver-modules-xscreensaver-gl
%commonreqs
Requires: xfce4-pulseaudio-plugin
# For xfce4-pulseaudio-plugin
Requires: pavucontrol

# No xfce4-mpc-plugin on aarch64
#Requires: xfce4-mpc-plugin

# Thunar plugins
# It requires additional configuration in /etc/samba/smb.conf.
#Requires: thunar-shares-plugin

%description full
%name-full is a virtual package to provide full installation
of Xfce4 Desktop.

%package regular
Summary: Virtual package for use in the regular-xfce distro
Group: Graphical desktop/XFce
BuildArch: noarch
Requires: %name-default = %version-%release
Requires: gnome-icon-theme
Requires: gnome-themes-extra
%commonreqs

%description regular
%summary

%install
mkdir -p %buildroot/%_datadir/xfce4
mkdir -p %buildroot/%_libdir/xfce4
mkdir -p %buildroot/%_sysconfdir/xdg/xfce4

%files common
%dir %_datadir/xfce4
%dir %_libdir/xfce4
%dir %_sysconfdir/xdg/xfce4

%if_disabled bootstrap
%files minimal
%files default
%files full
%files regular
%endif

%changelog
* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 4.14-alt7
- full,regular: Add xfce4-stopwatch-plugin.

* Wed Jul 03 2019 Mikhail Efremov <sem@altlinux.org> 4.14-alt6
- default: Drop gtk2-themes-xfce4.
- full: Add xscreensaver modules.

* Tue May 21 2019 Mikhail Efremov <sem@altlinux.org> 4.14-alt5
- full,regular: Drop xfce4-session-engines.

* Mon Apr 08 2019 Mikhail Efremov <sem@altlinux.org> 4.14-alt4
- cleanup: Remove commented out xfce4-radio-plugin.
- full,regular: Drop xfce4-wmdock-plugin.
- full,regular: Drop xfce4-quicklauncher-plugin.

* Fri Mar 22 2019 Mikhail Efremov <sem@altlinux.org> 4.14-alt3
- regular: Add gnome-themes-extra (closes: #36273).

* Thu Jan 31 2019 Mikhail Efremov <sem@altlinux.org> 4.14-alt2
- full,regular: Drop xfce4-mpc-plugin again.

* Thu Jan 31 2019 Mikhail Efremov <sem@altlinux.org> 4.14-alt1
- common: Drop %%_datadir/xfce4/doc/.
- full,regular: Add xfce4-mpc-plugin.
- Move xfce4-screensaver default -> full.
- full,regular: Add xfce4-panel-profiles.
- cosmetic: List plugins in alphabetical order.
- default: Add xfce4-screensaver.
- default: Add Greybird GTK+ theme.
- default: Replace icon themes with icon-theme-adwaita.
- cleanup: Remove xfce4-volumed from comments.

* Fri Mar 31 2017 Mikhail Efremov <sem@altlinux.org> 4.12-alt6
- Add bootstrap switch.
- default: Drop screen-saver-engine.

* Mon Nov 07 2016 Michael Shigorin <mike@altlinux.org> 4.12-alt5
- NMU: rework full/regular metapackages so that -regular one
  is suitable for sysvinit-based systems again (xfce-polkit
  fails to start properly there at the moment)

* Wed May 11 2016 Mikhail Efremov <sem@altlinux.org> 4.12-alt4
- default: Add gnome-icon-theme (closes: #32003).
- full: Add xfce-polkit (closes: #32075).

* Tue Mar 01 2016 Mikhail Efremov <sem@altlinux.org> 4.12-alt3
- regular: Drop firefox.

* Mon Feb 08 2016 Mikhail Efremov <sem@altlinux.org> 4.12-alt2
- full: Add xfce4-calculator-plugin.
- Move pavucontrol from regular to full.

* Thu Mar 19 2015 Mikhail Efremov <sem@altlinux.org> 4.12-alt1
- regular: Add pavucontrol.
- full: Add xfce4-smartbookmark-plugin.
- full: Add xfce4-pulseaudio-plugin.
- full: Drop xfce4-mixer.
- full: Add xfce4-whiskermenu-plugin.
- full: Add parole.

* Mon Jan 20 2014 Mikhail Efremov <sem@altlinux.org> 4.10-alt5
- default: Drop xfce4-volumed.
- Move xfce4-mixer from default to full.
- Fix Xfce name (XFce,XFCE -> Xfce).
- full: Fix summary.
- default: Replace xfce4-icon-theme with rodent-icon-theme.

* Wed Apr 10 2013 Mikhail Efremov <sem@altlinux.org> 4.10-alt4
- minimal: Drop ConsoleKit.
- full: Added mousepad.

* Thu Jan 31 2013 Mikhail Efremov <sem@altlinux.org> 4.10-alt3
- Added 'regular' subpackage.
- default: Terminal -> xfce4-terminal.

* Mon Dec 03 2012 Mikhail Efremov <sem@altlinux.org> 4.10-alt2
- Add common subpackage.
- full: Add ristretto again.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 4.10-alt1
- Bump version to 4.10.
- default: Thunar -> thunar.
- minimal: Drop xfce-utils.
- full: Drop xfce4-radio-plugin.
- full: xfcalendar -> orage.

* Tue Nov 22 2011 Mikhail Efremov <sem@altlinux.org> 4.8-alt7
- default: Drop tango-icon-theme.

* Mon Oct 17 2011 Mikhail Efremov <sem@altlinux.org> 4.8-alt6
- full: Add xfce4-kbdleds-plugin and xfce4-sensors-plugin.
- full: Add xfce4-session-engines.

* Tue Jun 07 2011 Mikhail Efremov <sem@altlinux.org> 4.8-alt5
- full: Drop xfce4-xfapplet-plugin.

* Fri May 27 2011 Mikhail Efremov <sem@altlinux.org> 4.8-alt4
- full: Drop xfce4-globalmenu-plugin.

* Thu Apr 21 2011 Mikhail Efremov <sem@altlinux.org> 4.8-alt3
- default: Add tango-icon-theme.
- full: Drop restretto.

* Mon Apr 18 2011 Mikhail Efremov <sem@altlinux.org> 4.8-alt2
- default: Add xfce4-volumed.

* Wed Mar 30 2011 Mikhail Efremov <sem@altlinux.org> 4.8-alt1
- Add xfce4-{minimal,default,full} virtual subpackages.
- Rename to xfce4, rewrite spec.

* Sun May 24 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6-alt1
- Fix for bug #20148.
- Added Thunar as depency.

* Fri Dec 24 2004 Andrey Astafiev <andrei@altlinux.ru> 4.2-alt1
- Added xfce4-session.

* Mon Nov 10 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0-alt2
- Changed Group tag.

* Tue Oct 07 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0-alt1
- 4.0

* Fri Sep 12 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.4-alt1
- 3.99.4

* Tue Sep 11 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.3-alt1
- Doesn't depends on packages version anymore.

* Fri Aug 29 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.3-alt0.9
- 3.99.3

* Mon Aug 18 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.2-alt0.9
- First version of RPM package for Sisyphus.
