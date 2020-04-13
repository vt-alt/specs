%define _libexecdir %_prefix/libexec
%define rname engrampa

Name: mate-file-archiver
Version: 1.22.1
Release: alt3
Epoch: 1
Summary: MATE Desktop file archiver
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: %rname = %epoch:%version-%release
Requires: p7zip zip

Source: %rname-%version.tar
Patch: %rname-%version-%release.patch

BuildRequires: mate-common libSM-devel libjson-glib-devel libmagic-devel mate-file-manager-devel yelp-tools

%description
Mate File Archiver is an application for creating and viewing archives files,
such as zip, xv, bzip2, cab, rar and other compress formats.

%package -n mate-file-manager-archiver
Summary: Mate-file-manager extension for mount archiver
Group: Graphical desktop/MATE
Requires: %name = %epoch:%version-%release

%description -n mate-file-manager-archiver
Mate-file-manager extension for mount archiver

%prep
%setup -q -n %rname-%version
%patch -p1

%build
%autoreconf
%configure \
	--disable-schemas-compile \
	--disable-static \
	--enable-caja-actions \
	--enable-magic \
	--disable-packagekit

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %rname --with-gnome --all-name

%files -f %rname.lang
%doc README COPYING NEWS AUTHORS
%_bindir/%rname
%_libexecdir/%rname
%_libexecdir/%rname-server
%_datadir/%rname
%_datadir/metainfo/engrampa.appdata.xml
%_desktopdir/%rname.desktop
%_datadir/dbus-1/services/org.mate.Engrampa.service
%_iconsdir/hicolor/*/apps/*
%_datadir/glib-2.0/schemas/org.mate.engrampa.gschema.xml
%_man1dir/*.1*

%files -n mate-file-manager-archiver
%_libdir/caja/extensions-2.0/libcaja-engrampa.so
%_datadir/caja/extensions/libcaja-engrampa.caja-extension

%changelog
* Fri Apr 10 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:1.22.1-alt3
- compresssion level selection added to batch-add dialog
- translations for compresssion level selection added

* Fri Apr 03 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:1.22.1-alt2
- alt specific compression level combobox added

* Tue Apr 23 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Wed Mar 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Tue Dec 18 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Fri Jun 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Mon Mar 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
