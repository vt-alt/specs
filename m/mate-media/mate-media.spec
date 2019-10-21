%define _libexecdir %_prefix/libexec

Name: mate-media
Version: 1.22.2
Release: alt1
Epoch: 1
Summary: MATE media programs
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: mate-common libcanberra-gtk3-devel libmatemixer-devel libxml2-devel mate-desktop-devel mate-panel-devel

%description
This package contains a few media utilities for the MATE desktop,
including a volume control.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--libexecdir=%_libexecdir \
	--disable-static \
	--disable-schemas-compile

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS COPYING NEWS README
%_sysconfdir/xdg/autostart/mate-volume-control-*.desktop
%_bindir/mate-volume-control*
%_libexecdir/mate-volume-control*
%_datadir/%name
%_datadir/mate-panel/applets/*.mate-panel-applet
%_datadir/sounds/mate
%_datadir/dbus-1/services/*.service
%_desktopdir/mate-volume-control.desktop
%_man1dir/*.1*

%changelog
* Tue Oct 15 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.2-alt1
- 1.22.2

* Mon Apr 22 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Mon Mar 04 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Mon Dec 24 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Tue Mar 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
