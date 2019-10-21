%define _libexecdir %_prefix/libexec

Name: mate-settings-daemon
Version: 1.22.1
Release: alt1
Epoch: 1
Summary: MATE Desktop settings daemon
License: GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: dconf

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: mate-common libSM-devel libXi-devel libXxf86misc-devel libcanberra-gtk3-devel
BuildRequires: libdbus-glib-devel libdconf-devel libmatekbd-devel libmatemixer-devel libnotify-devel
BuildRequires: libnss-devel libpolkit-devel libpulseaudio-devel mate-desktop-devel

%description
This package contains the daemon which is responsible for setting the
various parameters of a MATE session and the applications that run
under it.

%package devel
Group: Development/C
Summary: Development files for mate-settings-daemon

%description devel
This package contains the daemon which is responsible for setting the
various parameters of a MATE session and the applications that run
under it.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--enable-pulse \
	--enable-polkit \
	--with-nssdb \
	--disable-schemas-compile \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

find %buildroot%_libdir -name \*.la -delete

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS COPYING README
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/xrandr
%config %_sysconfdir/dbus-1/system.d/org.mate.SettingsDaemon.DateTimeMechanism.conf
%_sysconfdir/xdg/autostart/mate-settings-daemon.desktop
%_udevrulesdir/*.rules
%_sysconfdir/xrdb
%_libdir/%name
%_libexecdir/%name
%_libexecdir/msd-datetime-mechanism
%_libexecdir/msd-locate-pointer
%_datadir/mate-control-center/keybindings/50-accessibility.xml
%_datadir/dbus-1/services/org.mate.SettingsDaemon.service
%_datadir/dbus-1/system-services/org.mate.SettingsDaemon.DateTimeMechanism.service
%_iconsdir/hicolor/*/*/*
%_datadir/%name
%_datadir/glib-2.0/schemas/org.mate.*.xml
%_datadir/polkit-1/actions/org.mate.settingsdaemon.datetimemechanism.policy
%_man1dir/*.1*

%files devel
%_includedir/%name
%_pkgconfigdir/%name.pc

%changelog
* Tue Oct 15 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Mon Mar 04 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Mon Dec 24 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.4-alt1
- 1.20.4

* Fri Jun 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.3-alt1
- 1.20.3

* Tue Mar 27 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Thu Mar 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Wed Feb 21 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
