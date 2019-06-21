%set_verify_elf_method unresolved=relaxed

%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 3.32
%define api_ver 3.0
%define xdg_name org.gnome.SettingsDaemon

%def_enable smartcard
%def_enable systemd
%def_enable wayland
# tests require, as minimum, running colord
%def_disable check
%def_disable tests
# see NEWS 3.30.1.2
%def_disable suspend_then_hibernate

Name: gnome-settings-daemon
Version: %ver_major.1
Release: alt1

Summary: A program that manages general GNOME settings
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://www.gnome.org

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.54.0
%define gtk_ver 3.16
%define gnome_desktop_ver 3.29.90.1
%define notify_ver 0.7.3
%define pulse_ver 0.9.15
%define gsds_ver 3.23.3
%define colord_ver 0.1.9
%define dconf_ver 0.8
%define upower_ver 0.9.1
%define systemd_ver 40
%define wacom_ver 0.7
%define geocode_ver 3.10.0
%define geoclue_ver 2.3.1
%define gweather_ver 3.9.5
%define nm_ver 1.0
%define lcms_ver 2.2

Requires: dconf >= %dconf_ver
Requires: colord >= %colord_ver
Requires: system-config-printer
Requires: system-config-printer-udev
Requires: rfkill
Requires: geoclue2 >= %geoclue_ver
Requires: xkeyboard-config
Requires: iio-sensor-proxy

BuildRequires(pre): meson
BuildRequires: glib2-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgnome-desktop3-devel >= %gnome_desktop_ver
BuildRequires: libnotify-devel >= %notify_ver
BuildRequires: gsettings-desktop-schemas-devel >= %gsds_ver
BuildRequires: libpulseaudio-devel >= %pulse_ver libalsa-devel libcanberra-gtk3-devel
BuildRequires: libdbus-devel libpolkit1-devel
BuildRequires: xkeyboard-config-devel
%{?_enable_smartcard:BuildRequires: libnss-devel}
%{?_enable_systemd:BuildRequires: systemd-devel >= %systemd_ver libsystemd-login-devel}
%{?_enable_wayland:BuildRequires: libwayland-client-devel}
BuildRequires: libxkbfile-devel
BuildRequires: rpm-build-gnome docbook-style-xsl xsltproc
BuildRequires: gcc-c++ libcups-devel libgudev-devel libX11-devel libXi-devel libXext-devel libXfixes-devel
BuildRequires: libXrandr-devel xorg-proto-devel libICE-devel libSM-devel
BuildRequires: libupower-devel >= %upower_ver
BuildRequires: libcolord-devel >= %colord_ver liblcms2-devel >= %lcms_ver librsvg-devel
BuildRequires: libwacom-devel >= %wacom_ver xorg-drv-wacom-devel
BuildRequires: libgweather-devel >= %gweather_ver libgeocode-glib-devel >= %geocode_ver libgeoclue2-devel >= %geoclue_ver
BuildRequires: libnm-devel >= %nm_ver

# for check
%{?_enable_check:BuildRequires: /proc dbus gnome-color-manager}

%description
GNOME Settings Daemon is a program that organizes access to general GNOME
settings. Other GNOME programs may interact with gnome-settings-daemon to
obtain or change some settings. One of the most prominent examples of a g-s-d
client is GNOME Control Center, another one is Evolution.

%package devel
Summary: GNOME Settings Daemon development files
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package tests
Summary: GSD test programms
Group: Graphical desktop/GNOME
Requires: %name = %version-%release

%description tests
The %name-tests package provides programms for testing GSD plugins.

%prep
%setup

%build
%meson \
	%{?_disable_smartcard:-Dsmartcard=false} \
	%{?_enable_wayland:-Dwayland=true} \
	-Dudev_dir='/lib/udev' \
	%{?_enable_suspend_then_hibernate:-Dexperimental_suspend_then_hibernate=true}
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%dir %_libdir/%name-%api_ver
%_libdir/%name-%api_ver/libgsd.so
#%_libexecdir/gsd-a11y-keyboard
%_libexecdir/gsd-a11y-settings
%_libexecdir/gsd-backlight-helper
%_libexecdir/gsd-clipboard
%_libexecdir/gsd-color
%_libexecdir/gsd-datetime
%_libexecdir/gsd-dummy
%_libexecdir/gsd-housekeeping
%_libexecdir/gsd-keyboard
%_libexecdir/gsd-locate-pointer
%_libexecdir/gsd-media-keys
%_libexecdir/gsd-mouse
%_libexecdir/gsd-power
%_libexecdir/gsd-print-notifications
%_libexecdir/gsd-printer
%_libexecdir/gsd-rfkill
%_libexecdir/gsd-screensaver-proxy
%_libexecdir/gsd-sharing
%_libexecdir/gsd-smartcard
%_libexecdir/gsd-sound
%_libexecdir/gsd-wacom
%_libexecdir/gsd-wacom-led-helper
%_libexecdir/gsd-wacom-oled-helper
%_libexecdir/gsd-xsettings
%_datadir/%name/
%_sysconfdir/xdg/autostart/*.desktop
%config %_datadir/glib-2.0/schemas/*
%_datadir/GConf/gsettings/%name.convert
%_datadir/polkit-1/actions/org.gnome.settings-daemon.plugins.power.policy
%_datadir/polkit-1/actions/org.gnome.settings-daemon.plugins.wacom.policy
%_udevrulesdir/61-gnome-settings-daemon-rfkill.rules
%doc AUTHORS NEWS

%files devel
%_includedir/%name-%api_ver/
%_pkgconfigdir/%name.pc

%if_enabled tests
%files tests
%_libexecdir/gsd-test-a11y-keyboard
%_libexecdir/gsd-test-a11y-settings
%_libexecdir/gsd-test-datetime
%_libexecdir/gsd-test-housekeeping
%_libexecdir/gsd-test-input-helper
%_libexecdir/gsd-test-keyboard
%_libexecdir/gsd-test-media-keys
%_libexecdir/gsd-test-mouse
%_libexecdir/gsd-test-orientation
%_libexecdir/gsd-test-print-notifications
%_libexecdir/gsd-test-rfkill
%_libexecdir/gsd-test-screensaver-proxy
%_libexecdir/gsd-test-smartcard
%_libexecdir/gsd-test-sound
%_libexecdir/gsd-test-wacom
%_libexecdir/gsd-test-wacom-osd
%_libexecdir/gsd-test-xrandr
%_libexecdir/gsd-test-xsettings
%endif

%changelog
* Wed Jun 19 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Wed Jan 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Thu Oct 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1.2-alt1
- 3.30.1.2

* Thu Sep 27 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1.1-alt1
- 3.30.1.1

* Wed Sep 26 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Wed Jun 20 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt2
- fixed buildreqs

* Thu Apr 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Thu Nov 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Tue Oct 03 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Sun Sep 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt2
- updated to 3_24_3-8-g6e719ad (fixed BGO ##786164, 766067)

* Thu Jul 27 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3

* Tue May 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Wed Apr 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Wed Mar 15 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Tue Oct 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Wed Apr 13 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Fri Mar 18 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Tue Nov 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue Jul 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Tue May 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt2
- rebuilt against libupower-glib.so.3

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.3-alt1
- 3.12.3

* Sun Jun 08 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt2
- rebuilt against libcolord.so.2

* Mon May 05 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Wed Apr 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Thu Mar 27 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0.1-alt1
- 3.12.0.1

* Sat Feb 08 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt3
- updated to d4567273 (fixed BGO ##704167, 707790 722753, 712302)

* Wed Nov 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt2
- try to fix hotkey in non-latin layout (rosa patch)

* Wed Nov 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Wed Oct 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Fri Sep 06 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.5-alt1
- 3.8.5

* Sat Jul 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Sun Jul 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt2
- updated to 27e5804792 (fixed BGO 703048, 701322, 702047)

* Sat Jun 08 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Thu Apr 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1.1
- updated from upstream git (307f421)

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Sat Feb 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.4-alt2
- rebuilt against libcolord.so.2

* Fri Jan 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.4-alt1
- 3.6.4

* Mon Dec 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt2.1
- updated to 87b1afab07
- gnome-settings-daemon-3.6.3-xi-raw-events.patch (see BGO bug #685676)

* Wed Nov 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt1
- 3.6.3

* Thu Nov 08 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Oct 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Oct 03 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt2
- updated to 2184aa5
- built with ibus

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0
- new -tests subpackage

* Tue May 29 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt2
- updated from upstream git (4fb45d63a)

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Sat Dec 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt2
- updated from upstream git (fixed GNOME bugs ##664418,642489)

* Wed Nov 09 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2
- removed upstreamed patch
- fixed link

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Wed Oct 12 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt2
- updated from upstream git

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Thu Aug 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Wed Apr 06 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0.1-alt1
- 3.0.0.1

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Mar 31 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.93-alt2
- added dconf to reqs

* Sun Mar 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.93-alt1
- 2.91.93

* Mon Nov 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Tue Oct 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Wed Aug 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.6-alt1
- 2.31.6

* Wed Jul 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.4.2-alt1
- 2.31.4.2

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0
- enabled font plugin disabled by default in this version

* Wed Mar 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt2
- updated buildreqs

* Wed Mar 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91.1-alt1
- 2.29.91.1

* Mon Feb 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Tue Jan 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Tue Jan 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5-alt1
- 2.29.5

* Mon Oct 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 28 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt2
- updated buildreqs (shrek@)

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Fri Aug 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Tue Mar 03 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92
- removed upstreamed patches

* Fri Feb 06 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.90-alt1
- 2.25.90
- removed upstreamed patches

* Fri Jan 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.3-alt1
- 2.25.3
- applied current Fedora patches
- updated buildreqs
- updated schemas list

* Mon Dec 29 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt2
- updated buildreqs

* Tue Nov 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1
- updated buildreqs

* Sat Oct 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt4
- rebuild against libgnomekbd.so.3

* Thu Oct 02 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt3
- add apps_gnome_settings_daemon_xrandr to schemas list

* Wed Oct 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt2
- define libexec dir as /usr/libexec

* Sun Sep 28 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0
- new patchset from Fedora

* Wed Aug 13 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2.1-alt1
- 2.22.2.1
- import patches from fedora
- build with pulseaudio support

* Fri Mar 21 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt2
- check /desktop/gnome/sound/enable_esd for enable/disable esd (patch0)

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus
- patch2 from RH: don't set keyboard model on startup from gconf if evdev is being used.
  Evdev needs to use its own keyboard model to work right.

* Sun Mar 09 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.92-alt1
- First build for Sisyphus.

