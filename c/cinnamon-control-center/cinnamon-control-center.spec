%define ver_major 4.2
%define api_ver 1.0

%def_disable debug
%def_disable static
%def_enable systemd
%def_enable ibus
%def_enable onlineaccounts

Name: cinnamon-control-center
Version: %ver_major.2
Release: alt1

Summary: Cinnamon Control Center
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://github.com/linuxmint/cinnamon-control-center

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# From configure.ac
%define gtk_ver 3.5.13
%define glib_ver 2.31.0
%define desktop_ver 1.9.0
#%define clutter_ver 1.11.3
%define fontconfig_ver 1.0.0
%define xft_ver 2.1.2
%define libmetacity_ver 2.30.0
%define gsds_ver 3.6.0
%define notify_ver 0.7.3
%define nm_ver 1.2.0
%define gnome_menus_ver 3.5.5
%define goa_ver 3.5.90
%define sett_daemon_ver 0.0.1
%define bt_ver 3.5.92
%define systemd_ver 40
%define ibus_ver 1.4.99

Requires: %name-data = %version-%release
Requires: %name-translations

# For /usr/share/gnome
Requires: gnome-filesystem
Requires: cinnamon-settings-daemon
# for graphical passwd changing apps
Requires: accountsservice
#Requires: userpasswd
Requires: gnome-online-accounts >= %goa_ver
BuildPreReq: rpm-build-gnome >= 0.9

# From configure.in
BuildPreReq: intltool >= 0.50 gnome-common desktop-file-utils gnome-doc-utils gtk-doc xsltproc
BuildPreReq: fontconfig-devel >= %fontconfig_ver
BuildPreReq: libXft-devel >= %xft_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libcinnamon-desktop-devel >= %desktop_ver
BuildPreReq: libnotify-devel >= %notify_ver
BuildPreReq: cinnamon-settings-daemon-devel >= %sett_daemon_ver
BuildRequires: libxkbfile-devel
%{?_enable_ibus:BuildPreReq: libibus-devel >= %ibus_ver}
BuildRequires: libGConf-devel libdbus-glib-devel libupower-devel libpolkit1-devel
BuildRequires: libgio-devel librsvg-devel libxml2-devel
BuildRequires: libX11-devel libXext-devel libSM-devel libXScrnSaver-devel libXt-devel
BuildRequires: libXft-devel libXi-devel libXrandr-devel libXrender-devel libXcursor-devel libXcomposite-devel
BuildRequires: libgtop-devel libcups-devel iso-codes-devel
BuildRequires: libpwquality-devel libkrb5-devel
BuildRequires: libgnomekbd-devel libxklavier-devel
BuildRequires: libwacom-devel
BuildRequires: libcinnamon-menus-devel

BuildRequires: glibc-i18ndata
BuildRequires: libnm-devel >= %nm_ver
BuildRequires: libnma-devel >= %nm_ver
BuildRequires: libmm-glib-devel
BuildRequires: libgnome-online-accounts-devel >= %goa_ver colord-devel
BuildRequires: libgnome-bluetooth-devel >= %bt_ver
BuildRequires: libclutter-gtk3-devel
%{?_enable_systemd:BuildRequires: systemd-devel >= %systemd_ver libsystemd-login-devel}

%description
Cinnamon is an attractive and easy-to-use GUI desktop environment. The control-center package
provides the Cinnamon Control Center utilities that allow you to setup
and configure your Cinnamon environment (things like the desktop
background and theme, the screensaver, the window manager, system
sounds, and mouse behavior).

If you install Cinnamon, you need to install control-center.

%package data
Summary: Arch independent files for Cinnamon Control Center
Group: Networking/Instant messaging
BuildArch: noarch

%description data
This package provides noarch data needed for Cinnamon Control Center to work.

%package devel
Summary: Cinnamon Control Center development files
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
If you're interested in developing panels for the Cinnamon control center,
you'll want to install this package.

%name-devel helps you create the panels for the control center.

%prep
%setup
%patch0 -p1

%build
[ -d m4 ] || mkdir m4
%autoreconf
%configure \
	%{subst_enable debug} \
	%{subst_enable static} \
	--disable-update-mimedb \
	%{subst_enable systemd} \
	%{subst_enable ibus} \
	%{subst_enable onlineaccounts}

# Fix build on beekeeper machines
export NPROCS=1
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name-timezones

%files
#cinnamon-control-center binary doesn't work at x64 so temporary disable it.
%exclude %_bindir/*
%dir %_libdir/%{name}-1/panels
%_libdir/%{name}-1/panels/libcolor.so
%_libdir/%{name}-1/panels/libdisplay.so
%_libdir/%{name}-1/panels/libnetwork.so
%_libdir/%{name}-1/panels/libregion.so
%_libdir/%{name}-1/panels/libwacom-properties.so
%_libdir/%{name}-1/panels/libdate_time.so
%{?_enable_onlineaccounts:%_libdir/%{name}-1/panels/libonline-accounts.so}
%_libdir/*.so.*

%exclude %_libdir/%{name}-1/panels/*.la

%files data -f %name-timezones.lang
%dir %_datadir/%name
%_datadir/%name/ui
%_datadir/%name/datetime
# This desktop files are outdated and not usable/useful anymore
# TODO: Notify upstream about this issue
%exclude %_desktopdir/*.desktop
%_sysconfdir/xdg/menus/cinnamoncc.menu
%_datadir/desktop-directories/*
%_iconsdir/hicolor/*/*/*
%_datadir/polkit-1/rules.d/cinnamon-control-center.rules
%_datadir/polkit-1/actions/org.cinnamon.controlcenter.datetime.policy
%doc AUTHORS NEWS README

%files devel
%_pkgconfigdir/*.pc
%dir %_includedir/%name-1/lib%{name}/
%_includedir/%name-1/lib%{name}/*
%_libdir/*.so


%changelog
* Wed Jul 31 2019 Vladimir Didenko <cow@altlinux.org> 4.2.2-alt1
- 4.2.2

* Wed Jul 10 2019 Vladimir Didenko <cow@altlinux.org> 4.2.1-alt1
- 4.2.1

* Tue Jun 25 2019 Vladimir Didenko <cow@altlinux.org> 4.2.0-alt1
- 4.2.0

* Sat Jun 15 2019 Michael Shigorin <mike@altlinux.org> 4.0.1-alt1.2
- fix onlineaccounts knob

* Mon Jan 28 2019 Vladimir Didenko <cow@altlinux.org> 4.0.1-alt1.1
- fix build on beekeeper machines

* Tue Dec 25 2018 Vladimir Didenko <cow@altlinux.org> 4.0.1-alt1
- 4.0.1

* Wed Oct 31 2018 Vladimir Didenko <cow@altlinux.org> 4.0.0-alt1
- 4.0.0

* Fri Sep 14 2018 Vladimir Didenko <cow@altlinux.org> 3.8.2-alt1
- 3.8.2

* Wed Sep 12 2018 Vladimir Didenko <cow@altlinux.org> 3.8.0-alt4
- don't pack outdated desktop files (closes: #35387)

* Thu Jun 21 2018 Vladimir Didenko <cow@altlinux.org> 3.8.0-alt3
- remove socialweb from buildrequires

* Wed Jun 20 2018 Vladimir Didenko <cow@altlinux.org> 3.8.0-alt2
- fix build requires for libnm

* Thu May 3 2018 Vladimir Didenko <cow@altlinux.org> 3.8.0-alt1
- 3.8.0

* Thu Nov 23 2017 Vladimir Didenko <cow@altlinux.org> 3.6.5-alt1
- 3.6.5-2-g3b28266

* Fri Oct 27 2017 Vladimir Didenko <cow@altlinux.org> 3.6.1-alt1
- 3.6.1

* Fri May 5 2017 Vladimir Didenko <cow@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Dec 13 2016 Vladimir Didenko <cow@altlinux.org> 3.2.1-alt1
- 3.2.1

* Fri Nov 11 2016 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt1
- 3.2.0-3-gf665a9c

* Fri Jun 24 2016 Vladimir Didenko <cow@altlinux.org> 3.0.1-alt1
- 3.0.1

* Mon Apr 25 2016 Vladimir Didenko <cow@altlinux.org> 3.0.0-alt1
- 3.0.0

* Mon Oct 19 2015 Vladimir Didenko <cow@altlinux.org> 2.8.0-alt1
- 2.8.0

* Tue May 19 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt1
- 2.6.0

* Tue Apr 14 2015 Vladimir Didenko <cow@altlinux.org> 2.5.0-alt1
- 2.5.0

* Wed Apr 1 2015 Vladimir Didenko <cow@altlinux.org> 2.4.2-alt2
- don't check NetworkManager version

* Thu Nov 27 2014 Vladimir Didenko <cow@altlinux.org> 2.4.2-alt1
- 2.4.2

* Wed Nov 5 2014 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt1
- 2.4.0-4-g19f5232

* Thu Oct 16 2014 Vladimir Didenko <cow@altlinux.org> 2.3.0-alt1
- git 20140923

* Wed Oct 15 2014 Vladimir Didenko <cow@altlinux.org> 2.2.10-alt2
- rebuild with new upower

* Tue Jul 22 2014 Vladimir Didenko <cow@altlinux.org> 2.2.10-alt1
- 2.2.10

* Mon Jun 9 2014 Vladimir Didenko <cow@altlinux.org> 2.2.8-alt3
- rebuild with new colord

* Thu May 29 2014 Vladimir Didenko <cow@altlinux.org> 2.2.8-alt2
- remove region panel

* Wed May 21 2014 Vladimir Didenko <cow@altlinux.org> 2.2.8-alt1
- 2.2.8

* Mon May 5 2014 Vladimir Didenko <cow@altlinux.org> 2.2.5-alt1
- 2.2.5

* Wed Apr 30 2014 Vladimir Didenko <cow@altlinux.org> 2.2.3-alt2
- 2.2.3-3-g453b9e0

* Fri Apr 18 2014 Vladimir Didenko <cow@altlinux.org> 2.2.3-alt1
- 2.2.3-1-gf566167

* Mon Apr 14 2014 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt1
- 2.2.2-1-g8867794

* Wed Apr 9 2014 Vladimir Didenko <cow@altlinux.org> 2.0.9-alt8
- renable locale configuring

* Tue Apr 8 2014 Vladimir Didenko <cow@altlinux.org> 2.0.9-alt7
- git20140329

* Fri Apr 5 2014 Vladimir Didenko <cow@altlinux.org> 2.0.9-alt6
- reenable power panel

* Tue Apr 1 2014 Vladimir Didenko <cow@altlinux.org> 2.0.9-alt5
- temporary disable power panel

* Tue Mar 5 2014 Vladimir Didenko <cow@altlinux.org> 2.0.9-alt4
- build with gnome-3.12

* Thu Feb 20 2014 Vladimir Didenko <cow@altlinux.org> 2.0.9-alt3
- reenable layouts configuring

* Mon Dec 9 2013 Vladimir Didenko <cow@altlinux.org> 2.0.9-alt2
- fix region panel using patch from Fedora

* Mon Nov 25 2013 Vladimir Didenko <cow@altlinux.org> 2.0.9-alt1
- 2.0.9

* Tue Nov 12 2013 Vladimir Didenko <cow@altlinux.org> 2.0.8-alt1
- 2.0.8

* Tue Oct 29 2013 Vladimir Didenko <cow@altlinux.org> 2.0.6-alt1
- 2.0.6

* Mon Oct 21 2013 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt1
- 2.0.3-1-gc637556

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.2-alt1
- 2.0.2

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt6
- rebuild for GNOME-3.10

* Tue Sep 17 2013 Vladimir Didenko <cow@altlinux.org> 1.8.2-alt5
- 1.8.2-51-gfb6a941
- reenable cheese
- disable region panel. g-c-c should be used instead

* Fri Sep 6 2013 Vladimir Didenko <cow@altlinux.org> 1.8.2-alt4
- temporary disable cheese

* Thu Aug 29 2013 Vladimir Didenko <cow@altlinux.org> 1.8.2-alt3
- 1.8.2-33-g0cdd9c6

* Mon Aug 5 2013 Vladimir Didenko <cow@altlinux.org> 1.8.2-alt2
- 1.8.2-23-g7d365d0

* Sat May 25 2013 Vladimir Didenko <cow@altlinux.org> 1.8.2-alt1
- 1.8.2

* Tue May 21 2013 Vladimir Didenko <cow@altlinux.org> 1.8.1-alt1
- 1.8.1

* Thu May 16 2013 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt2
- Replace gnome_rr_labeler calls by cc_rr_labeler
- Fix bluetooth panel

* Thu May 16 2013 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt1
- 1.8.0

* Fri Apr 26 2013 Vladimir Didenko <cow@altlinux.org> 1.7.3-alt1
- 1.7.3-9-g3526e0d

* Fri Feb 22 2013 Vladimir Didenko <cow@altlinux.org> 1.7.1-alt1
- Initial build for Alt Linux
