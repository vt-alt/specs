%define rname eom

Name: mate-image-viewer
Version: 1.22.2
Release: alt1
Epoch: 1
Summary: Eye of MATE image viewer
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %rname-%version.tar
Patch: %rname-%version-%release.patch

BuildRequires: mate-common gtk-doc libdbus-glib-devel libexempi-devel libexif-devel libjpeg-devel liblcms2-devel
BuildRequires: libpeas-devel librsvg-devel libxml2-devel mate-desktop-devel yelp-tools

%description
The Eye of MATE (eom) is the official image viewer for the
MATE desktop. It can view single image files in a variety of formats, as
well as large image collections.
Eye of Mate is extensible through a plugin system.

%package devel
Summary: Support for developing plugins for the eom image viewer
Group: Development/Other

%description devel
Development files for eom

%prep
%setup -q -n %rname-%version
%patch -p1

%build
%autoreconf
%configure \
	--disable-schemas-compile \
	--enable-gtk-doc \
	--enable-introspection

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %rname --with-gnome --all-name

%files -f %rname.lang
%doc AUTHORS COPYING NEWS README
%_bindir/%rname
%_libdir/%rname
%_libdir/girepository-1.0/Eom-1.0.typelib
%_desktopdir/%rname.desktop
%_datadir/%rname
%_iconsdir/hicolor/*/*/*
%_datadir/glib-2.0/schemas/org.mate.eom.gschema.xml
%_datadir/glib-2.0/schemas/org.mate.eom.enums.xml
%_datadir/metainfo/eom.appdata.xml
%_man1dir/*.1*

%files devel
%_includedir/eom-2.20
%_pkgconfigdir/*.pc
%_datadir/gtk-doc/html/%rname
%_datadir/gir-1.0/*.gir

%changelog
* Thu Oct 17 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.2-alt1
- 1.22.2

* Fri Sep 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt2
- updated russian translation (closes: #37020)

* Tue Apr 23 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Wed Mar 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Mon Dec 24 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Fri Jun 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Mon Mar 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
