%define rname caja-extensions

Name: mate-file-manager-extensions
Version: 1.22.1
Release: alt1
Epoch: 1
Summary: Set of extensions for caja file manager
License: GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %rname-%version.tar
Patch: %rname-%version-%release.patch

BuildRequires: mate-common gtk-doc libdbus-glib-devel libgupnp-devel mate-desktop-devel mate-file-manager-devel

%description
Extensions for the caja file-browser, open-terminal, image-converter, sendto and share

%package common
Group: Graphical desktop/MATE
Summary: Common files for %rname
BuildArch: noarch

%description common
%summary

%package -n mate-file-manager-image-converter
Group: Graphical desktop/MATE
Summary: MATE file manager image converter extension
Requires: %name-common = %epoch:%version-%release

%description -n mate-file-manager-image-converter
The caja-image-converter extension allows you to
re-size/rotate images from Caja.

%package -n mate-file-manager-open-terminal
Group: Graphical desktop/MATE
Summary: Mate-file-manager extension for an open terminal shortcut
Requires: %name-common = %epoch:%version-%release

%description -n mate-file-manager-open-terminal
The caja-open-terminal extension provides a right-click "Open
Terminal" option for mate-file-manager users who prefer that option.

%package -n mate-file-manager-sendto
Group: Graphical desktop/MATE
Summary: MATE file manager sendto
Requires: %name-common = %epoch:%version-%release

%description -n mate-file-manager-sendto
The caja-sendto extension provides 'send to' functionality
to the MATE Desktop file-manager, Caja.

%package -n mate-file-manager-sendto-devel
Group: Graphical desktop/MATE
Summary: Development libraries and headers for caja-sendto

%description -n mate-file-manager-sendto-devel
Development libraries and headers for caja-sendto

%package -n mate-file-manager-share
Group: Graphical desktop/MATE
Summary: Easy sharing folder via Samba (CIFS protocol)
Requires: %name-common = %epoch:%version-%release samba

%description -n mate-file-manager-share
Caja extension designed for easier folders
sharing via Samba (CIFS protocol) in *NIX systems.

%package -n mate-file-manager-beesu
Group: Graphical desktop/MATE
Summary: MATE file manager beesu
Requires: %name-common = %epoch:%version-%release beesu

%description -n mate-file-manager-beesu
Caja beesu extension for open files as superuser

%package -n mate-file-manager-wallpaper
Group: Graphical desktop/MATE
Summary: MATE file manager wallpaper
Requires: %name-common = %epoch:%version-%release

%description -n mate-file-manager-wallpaper
Caja wallpaper extension, allows to quickly set wallpaper.

%package -n caja-xattr-tags
Group: Graphical desktop/MATE
Summary: MATE file manager xattr-tags
Requires: %name-common = %epoch:%version-%release

%description -n caja-xattr-tags
Caja xattr-tags extension, allows to quickly set xattr-tags

%prep
%setup -q -n %rname-%version
%patch -p1

%build
%autoreconf
%configure \
	--disable-schemas-compile \
	--disable-static \
	--enable-gtk-doc \
	--enable-xattr-tags=no \
	--enable-image-converter \
	--enable-open-terminal \
	--enable-sendto \
	--with-sendto-plugins=all \
	--enable-share \
	--enable-gksu \
	--enable-wallpaper

%make_build

%install
%make DESTDIR=%buildroot install

find %buildroot%_libdir -name \*.la -delete

%find_lang %rname --with-gnome --all-name

%files common -f %rname.lang
%doc AUTHORS COPYING README
%dir %_datadir/caja-extensions

%files -n mate-file-manager-image-converter
%_libdir/caja/extensions-2.0/libcaja-image-converter.so
%_datadir/caja-extensions/caja-image-resize.ui
%_datadir/caja-extensions/caja-image-rotate.ui
%_datadir/caja/extensions/libcaja-image-converter.caja-extension

%files -n mate-file-manager-open-terminal
%_libdir/caja/extensions-2.0/libcaja-open-terminal.so
%_datadir/glib-2.0/schemas/org.mate.caja-open-terminal.gschema.xml
%_datadir/caja/extensions/libcaja-open-terminal.caja-extension

%files -n mate-file-manager-sendto
%_bindir/caja-sendto
%_libdir/caja-sendto
%_libdir/caja/extensions-2.0/libcaja-sendto.so
%_datadir/glib-2.0/schemas/org.mate.Caja.Sendto.gschema.xml
%_datadir/caja-extensions/caja-sendto.ui
%_datadir/caja/extensions/libcaja-sendto.caja-extension
%_datadir/gtk-doc/html/caja-sendto
%_man1dir/*.1*

%files -n mate-file-manager-sendto-devel
%_includedir/caja-sendto
%_pkgconfigdir/caja-sendto.pc

%files -n mate-file-manager-share
%_libdir/caja/extensions-2.0/libcaja-share.so
%_datadir/caja-extensions/share-dialog.ui
%_datadir/caja/extensions/libcaja-share.caja-extension

%files -n mate-file-manager-beesu
%_libdir/caja/extensions-2.0/libcaja-gksu.so
%_datadir/caja/extensions/libcaja-gksu.caja-extension

%files -n mate-file-manager-wallpaper
%_libdir/caja/extensions-2.0/libcaja-wallpaper.so
%_datadir/caja/extensions/libcaja-wallpaper.caja-extension

#files -n caja-xattr-tags
#_libdir/caja/extensions-2.0/libcaja-xattr-tags.so
#_datadir/caja/extensions/libcaja-xattr-tags.caja-extension

%changelog
* Wed Oct 16 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Wed Mar 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Tue Dec 18 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.20.1-alt1.qa1
- NMU: applied repocop patch

* Fri Jun 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Wed Mar 21 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
