%define _libexecdir %_prefix/libexec

Name: mate-notification-daemon
Version: 1.22.1
Release: alt1
Epoch: 1
Summary: Notification daemon for MATE Desktop
License: GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: mate-common libcanberra-gtk3-devel libdbus-glib-devel libnotify-devel libwnck3-devel

%description
Notification daemon for MATE Desktop

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-schemas-compile

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS COPYING README
%_bindir/mate-notification-properties
%_libdir/mate-notification-daemon
%_libexecdir/mate-notification-daemon
%_desktopdir/mate-notification-properties.desktop
%_datadir/dbus-1/services/org.freedesktop.mate.Notifications.service
%_datadir/mate-notification-daemon/mate-notification-properties.ui
%_iconsdir/hicolor/*/apps/mate-notification-properties.*
%_datadir/glib-2.0/schemas/org.mate.NotificationDaemon.gschema.xml
%_man1dir/mate-notification-properties.1*

%changelog
* Tue Oct 15 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Mon Mar 04 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Mon Dec 24 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Thu Mar 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Fri Feb 23 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt2_1
- removed false rundep
