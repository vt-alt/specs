%define _libexecdir %_prefix/libexec

Name: mate-screensaver
Version: 1.22.2
Release: alt1
Epoch: 2
Summary: MATE Screensaver
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: pam_gnome-keyring

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: mate-common libSM-devel libXScrnSaver-devel libXxf86misc-devel libXxf86vm-devel
BuildRequires: libdbus-glib-devel libmatekbd-devel libnotify-devel libpam-devel libsystemd-devel
BuildRequires: mate-desktop-devel mate-menus-devel xmlto

%description
mate-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.

%package devel
Group: Development/C
Summary: Development files for mate-screensaver

%description devel
Development files for mate-screensaver

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-schemas-compile \
	--enable-docbook-docs \
	--with-mit-ext \
	--with-xf86gamma-ext \
	--with-libgl \
	--with-shadow \
	--enable-pam  \
	--enable-authentication-scheme=helper \
	--with-passwd-helper=%_libexecdir/%name/%name-pam-helper \
	--enable-locking \
	--with-systemd \
	--without-console-kit

%make_build

%install
%make DESTDIR=%buildroot install
install -m644 -pD doc/mate-screensaver.html %buildroot%_datadir/doc/mate-screensaver/mate-screensaver.html

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS NEWS README COPYING
%_docdir/%name
%_sysconfdir/pam.d/%name
%_sysconfdir/xdg/menus/mate-screensavers.menu
%_sysconfdir/xdg/autostart/%name.desktop
%_bindir/mate-screensaver*
%_libexecdir/%name-*
%_libexecdir/%name/floaters
%_libexecdir/%name/popsquares
%_libexecdir/%name/slideshow
%attr(2511,root,chkpwd) %_libexecdir/%name/%name-pam-helper
%_desktopdir/%name-preferences.desktop
%_desktopdir/screensavers/*.desktop
%_datadir/%name
%_datadir/backgrounds/cosmos
%_datadir/pixmaps/mate-logo-white.svg
%_datadir/pixmaps/gnome-logo-white.svg
%_datadir/desktop-directories/mate-screensaver.directory
%_datadir/glib-2.0/schemas/org.mate.screensaver.gschema.xml
%_datadir/mate-background-properties/cosmos.xml
%_datadir/dbus-1/services/org.mate.ScreenSaver.service
%_man1dir/*.1*

%files devel
%_libdir/pkgconfig/*.pc

%changelog
* Tue Oct 15 2019 Valery Inozemtsev <shrek@altlinux.ru> 2:1.22.2-alt1
- 1.22.2

* Wed Apr 24 2019 Valery Inozemtsev <shrek@altlinux.ru> 2:1.22.1-alt1
- 1.22.1

* Mon Mar 04 2019 Valery Inozemtsev <shrek@altlinux.ru> 2:1.22.0-alt1
- 1.22.0

* Fri Jan 11 2019 Paul Wolneykien <manowar@altlinux.org> 2:1.20.3-alt2
- Added helper protocol library.
- Improved PAM helper (supports PAM conversation).

* Mon Dec 24 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.3-alt1
- 1.20.3

* Wed Dec 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.2-alt1
- 1.20.2

* Thu Mar 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
