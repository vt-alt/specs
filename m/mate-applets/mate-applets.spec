%define _libexecdir %_prefix/libexec

Name: mate-applets
Version: 1.22.2
Release: alt1
Epoch: 1
Summary: MATE Desktop panel applets
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: mate-netspeed = %version-%release
Obsoletes: mate-netspeed

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: mate-common libSM-devel libdbus-glib-devel libgtksourceview3-devel
BuildRequires: libgtop-devel libgucharmap-devel libnotify-devel libpolkit-devel libupower-devel
BuildRequires: libwireless-devel libwnck3-devel libxml2-devel mate-panel-devel yelp-tools

%description
MATE Desktop panel applets

%prep
%setup
%patch -p1

rm -fr mateweather/docs/ru

%build
%autoreconf
%configure \
	--disable-schemas-compile \
	--disable-static \
	--enable-polkit \
	--enable-ipv6 \
	--libexecdir=%_libexecdir/%name \
	--disable-cpufreq \
	--disable-battstat \
	--disable-stickynotes \
	--enable-frequency-selector=no

%make_build

%install
%makeinstall_std

rm -fr %buildroot%_datadir/help/*/mate-stickynotes-applet

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS COPYING README
%_libexecdir/%name
%_datadir/%name
%_datadir/mate/ui/*.xml
%_datadir/mate-panel/applets/*
%_datadir/glib-2.0/schemas/*.xml
%_datadir/dbus-1/services/*.service
%_iconsdir/hicolor/*/*/*
%_man1dir/*.1*

%changelog
* Tue Oct 15 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.2-alt1
- 1.22.2

* Tue Apr 23 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Wed Mar 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Mon Dec 24 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.3-alt1
- 1.20.3

* Mon Sep 03 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2
- disable battstat (closes: #35336)

* Sat May 05 2018 Michael Shigorin <mike@altlinux.org> 1:1.20.1-alt2
- avoid apm on platforms without it

* Tue Mar 27 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Mon Mar 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org
- disabled cpufreq

* Wed Feb 21 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

