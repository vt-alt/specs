Name: mate-menus
Version: 1.22.1
Release: alt1
Epoch: 1
Summary: Displays menus for MATE Desktop
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Conflicts: altlinux-freedesktop-menu-mate

BuildRequires: mate-common gobject-introspection-devel

%description
Displays menus for MATE Desktop

%package -n libmate-menus
Group: System/Libraries
Summary: Shared libraries for mate-menus

%description -n libmate-menus
Shared libraries for mate-menus

%package devel
Group: Development/C
Summary: Development files for mate-menus

%description devel
Development files for mate-menus

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--enable-introspection

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS COPYING README
%_sysconfdir/xdg/menus/mate-preferences-categories.menu
%_sysconfdir/xdg/menus/mate-applications.menu
%_sysconfdir/xdg/menus/mate-settings.menu
%_datadir/mate-menus
%_datadir/mate/desktop-directories

%files -n libmate-menus
%_libdir/girepository-1.0/MateMenu-2.0.typelib
%_libdir/libmate-menu.so.*

%files devel
%_includedir/mate-menus
%_libdir/libmate-menu.so
%_pkgconfigdir/libmate-menu.pc
%_datadir/gir-1.0/MateMenu-2.0.gir

%changelog
* Tue Oct 15 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Mon Mar 04 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Mon Dec 24 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Mon Sep 10 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt2
- show generic name instead of full name

* Fri Sep 07 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Tue Mar 06 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Tue Feb 20 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
