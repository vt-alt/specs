Name: mate-desktop
Version: 1.22.2
Release: alt1
Epoch: 1
Summary: Shared code for mate-panel, mate-session, mate-file-manager, etc
License: GPLv2+ and LGPLv2+ and MIT
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: altlinux-freedesktop-menu-common mate-control-center mate-panel mate-notification-daemon mate-user-guide
Obsoletes: libmate libmate-devel libmatecanvas libmatecanvas-devel libmatecomponent libmatecomponent-devel libmatecomponentui
Obsoletes: libmatecomponentui-devel libmateui libmateui-devel mate-conf mate-conf-devel mate-conf-editor mate-conf-gtk
Obsoletes: mate-mime-data mate-mime-data-devel mate-vfs mate-vfs-devel mate-vfs-smb libmatekeyring libmatekeyring-devel
Obsoletes: mate-keyring mate-keyring-pam mate-keyring-devel mate-bluetooth mate-bluetooth-libs mate-bluetooth-devel
Obsoletes: mate-doc-utils mate-character-map mate-character-map-devel libmatewnck libmatewnck-devel mate-dialogs

BuildRequires: mate-common iso-codes-devel gtk-doc libXrandr-devel libdconf-devel libgtk+3-gir-devel librsvg-utils libstartup-notification-devel

%description
The mate-desktop package contains an internal library
(libmatedesktop) used to implement some portions of the MATE
desktop, and also some data files and other shared components of the
MATE user environment.

%package -n lib%name
Group: System/Libraries
Summary: Shared libraries for libmate-desktop
License: LGPLv2+

%description -n lib%name
Shared libraries for lib%name

%package devel
Group: Development/C
Summary: Libraries and headers for lib%name
License: LGPLv2+

%description devel
Libraries and header files for the MATE-internal private library
libmatedesktop.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--enable-gtk-doc \
	--disable-schemas-compile \
	--with-pnp-ids-path=%_datadir/misc/pnp.ids \
	--enable-gtk-doc-html \
	--enable-introspection \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

cat << __EOF__ > %buildroot%_datadir/glib-2.0/schemas/10_mate-alt.gschema.override
[org.mate.background]
picture-filename='/usr/share/design/current/backgrounds/default.png'
picture-options='stretched'

[org.mate.interface]
gtk-theme='BlueMenta'
icon-theme='mate'

[org.mate.Marco.general]
theme='BlueMenta'

[org.mate.peripherals-mouse]
cursor-theme='mate'
__EOF__

%find_lang %name --with-gnome --all-name

%files
%doc AUTHORS COPYING COPYING.LIB NEWS README
%_bindir/mate-*
%_datadir/mate-about
%_desktopdir/mate-*.desktop
%_iconsdir/hicolor/*/apps/*
%_man1dir/mate-*.1*

%files -n lib%name -f %name.lang
%_libdir/*.so.*
%_libdir/girepository-1.0/MateDesktop-2.0.typelib
%_datadir/glib-2.0/schemas/org.mate.*.gschema.xml
%_datadir/glib-2.0/schemas/10_mate-alt.gschema.override

%files devel
%doc %_datadir/gtk-doc/html/mate-desktop
%_includedir/mate-desktop-2.0
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/gir-1.0/MateDesktop-2.0.gir

%changelog
* Tue Oct 15 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.2-alt1
- 1.22.2

* Mon Apr 22 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Mon Mar 04 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Mon Dec 24 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.4-alt1
- 1.20.4

* Fri Jun 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.3-alt1
- 1.20.3

* Tue Mar 27 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Wed Feb 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Mon Feb 19 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
