%define rname caja
%define _libexecdir %_prefix/libexec

Name: mate-file-manager
Version: 1.22.1
Release: alt2
Epoch: 1
Summary: File manager for MATE
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: mate-file-manager-extensions mate-file-manager-schemas

Source: %rname-%version.tar
Patch: %rname-%version-%release.patch

BuildRequires: mate-common gtk-doc libSM-devel libexempi-devel libexif-devel libgail3-devel libnotify-devel libselinux-devel libxml2-devel mate-desktop-devel

%description
Caja (mate-file-manager) is the file manager and graphical shell
for the MATE desktop, that makes it easy to manage your files and
the rest of your system. It allows to browse directories on local
and remote file systems, preview files and launch applications
associated with them. It is also responsible for handling the
icons on the MATE desktop.

%package extensions
Group: Graphical desktop/MATE
Summary:  Mate-file-manager extensions library

%description extensions
This package provides the libraries used by caja extensions.

%package schemas
Group: Graphical desktop/MATE
Summary:  Mate-file-manager schemas
License:  LGPLv2+
BuildArch: noarch

%description schemas
This package provides the gsettings schemas for caja.

%package devel
Group: Development/C
Summary:  Support for developing mate-file-manager extensions

%description devel
This package provides libraries and header files needed
for developing caja extensions.

%prep
%setup -q -n %rname-%version
%patch -p1

%build
%autoreconf
%configure \
	--enable-gtk-doc \
	--disable-static \
	--disable-schemas-compile \
	--disable-update-mimedb

%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_libdir/caja/extensions-2.0

%find_lang %rname --with-gnome --all-name

%files
%doc AUTHORS COPYING COPYING.LIB NEWS README
%_bindir/*
%_libdir/%rname
%_datadir/%rname
%_datadir/pixmaps/%rname
%_datadir/metainfo/caja.appdata.xml
%_datadir/dbus-1/services/org.mate.freedesktop.FileManager1.service
%_datadir/mime/packages/caja.xml
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*
%_man1dir/*.1*

%files extensions
%_libdir/libcaja-extension.so.*
%_libdir/girepository-1.0/*.typelib

%files schemas -f %rname.lang
%_datadir/glib-2.0/schemas/org.mate.*.gschema.xml

%files devel
%_includedir/%rname
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/gir-1.0/*.gir
%_datadir/gtk-doc/html/libcaja-extension

%changelog
* Wed Jul 24 2019 Slava Aseev <ptrnine@altlinux.org> 1:1.22.1-alt2
- Support querying files by contained text

* Tue Apr 23 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Wed Mar 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Tue Dec 18 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.3-alt1
- 1.20.3

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.20.2-alt1.qa1
- NMU: applied repocop patch

* Mon Apr 09 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Tue Mar 27 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Tue Mar 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Tue Feb 20 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_3
- new fc release
