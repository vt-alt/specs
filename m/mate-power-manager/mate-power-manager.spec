%define _libexecdir %_prefix/libexec

Name: mate-power-manager
Version: 1.22.2
Release: alt1
Epoch: 1
Summary: MATE power management service
License: GPLv3+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: upower

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: mate-common libXrandr-devel libcanberra-gtk3-devel libdbus-glib-devel
BuildRequires: libgnome-keyring-devel libnotify-devel libupower-devel mate-panel-devel yelp-tools

%description
MATE Power Manager uses the information and facilities provided by UPower
displaying icons and handling user callbacks in an interactive MATE session.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--enable-applets \
	--disable-schemas-compile

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS COPYING README
%_sysconfdir/xdg/autostart/mate-power-manager.desktop
%_bindir/mate-power-*
%_sbindir/mate-power-backlight-helper
%_libexecdir/mate-*-applet
%_desktopdir/mate-*.desktop
%_datadir/mate-power-manager
%_iconsdir/hicolor/*/apps/mate-*.*
%_datadir/mate-panel/applets/org.mate.BrightnessApplet.mate-panel-applet
%_datadir/mate-panel/applets/org.mate.InhibitApplet.mate-panel-applet
%_datadir/dbus-1/services/*.service
%_datadir/polkit-1/actions/org.mate.power.policy
%_datadir/glib-2.0/schemas/org.mate.power-manager.gschema.xml
%_man1dir/mate-power-*.1*

%changelog
* Wed Oct 16 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.2-alt1
- 1.22.2

* Tue Apr 23 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Tue Mar 05 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Mon Dec 24 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.3-alt1
- 1.20.3

* Tue Mar 27 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Thu Mar 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
