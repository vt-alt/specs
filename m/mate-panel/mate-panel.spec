Name: mate-panel
Version: 1.22.2
Release: alt1
Epoch: 2
Summary: MATE Desktop panel and applets
License: GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: mate-common gtk-doc libSM-devel libXi-devel libXrandr-devel libdbus-glib-devel libdconf-devel
BuildRequires: libmateweather-devel librsvg-devel libwnck3-devel mate-desktop-devel mate-menus-devel yelp-tools

%description
MATE Desktop panel applets

%package -n lib%name
Group: System/Libraries
Summary: Shared libraries for mate-panel
License: LGPLv2+
Provides: %name-libs = %version-%release
Obsoletes: %name-libs

%description -n lib%name
Shared libraries for libmate-desktop

%package devel
Group: Development/C
Summary: Development files for mate-panel

%description devel
Development files for mate-panel

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--disable-gtk-doc \
	--disable-schemas-compile \
	--enable-introspection \
	--with-in-process-applets=clock,notification-area,wncklet

%make_build

%install
%make DESTDIR=%buildroot install

rm -f %buildroot%_datadir/%name/applets/org.mate.panel.FishApplet.mate-panel-applet
rm -f %buildroot%_datadir/glib-2.0/schemas/org.mate.panel.applet.fish.gschema.xml
rm -fr %buildroot%_datadir/help/*/mate-fish
rm -fr %buildroot%_datadir/%name/fish

find %buildroot%_libdir -name \*.la -delete

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS COPYING README
%_bindir/mate-*
%_libdir/%name
%_datadir/%name
%_datadir/glib-2.0/schemas/org.mate.panel.*.xml
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/*
%_man1dir/mate-*.1*

%files -n lib%name
%doc COPYING.LIB
%_libdir/*.so.*
%_libdir/girepository-1.0/MatePanelApplet-4.0.typelib

%files devel
%_includedir/%name-*
%_libdir/*.so
%_pkgconfigdir/libmatepanelapplet-4.0.pc
%_datadir/gir-1.0/MatePanelApplet-4.0.gir

%changelog
* Tue Oct 15 2019 Valery Inozemtsev <shrek@altlinux.ru> 2:1.22.2-alt1
- 1.22.2

* Thu Apr 25 2019 Valery Inozemtsev <shrek@altlinux.ru> 2:1.22.1-alt1
- 1.22.1

* Mon Mar 04 2019 Valery Inozemtsev <shrek@altlinux.ru> 2:1.22.0-alt1
- 1.22.0

* Tue Feb 12 2019 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.5-alt1
- 1.20.5

* Mon Dec 24 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.4-alt1
- 1.20.4

* Mon Sep 03 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.3-alt1
- 1.20.3

* Fri Jun 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.2-alt1
- 1.20.2

* Tue Mar 27 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.1-alt1
- 1.20.1

* Mon Mar 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.0-alt1
- initial build from git.mate-desktop.org

* Tue Feb 20 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:1.20.0-alt1_2
- new fc release
