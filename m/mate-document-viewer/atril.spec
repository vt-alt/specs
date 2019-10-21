%def_enable epub
%def_enable xps

%define rname atril
%define _libexecdir %_prefix/libexec

Name: mate-document-viewer
Version: 1.22.2
Release: alt1
Epoch: 1
Summary: Document viewer
License: GPLv2+ and LGPLv2+ and MIT
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: mathjax

Source: %rname-%version.tar
Patch: %rname-%version-%release.patch

BuildRequires: mate-common
BuildRequires: gcc-c++ gtk-doc libdjvu-devel libgail3-devel libkpathsea-devel
BuildRequires: libpoppler-glib-devel libsecret-devel libspectre-devel libtiff-devel libSM-devel
BuildRequires: libxml2-devel mate-file-manager-devel yelp-tools

%if_enabled xps
BuildRequires: libgxps-devel libgxps-gir-devel
%endif

%if_enabled epub
BuildRequires: libwebkit2gtk-devel
%endif

%description
Mate-document-viewer is simple document viewer.
It can display and print Portable Document Format (PDF),
PostScript (PS), Encapsulated PostScript (EPS), DVI, DJVU%{?_enable_epub:, epub}%{?_enable_xps: and XPS} files.
When supported by the document format, mate-document-viewer
allows searching for text, copying text to the clipboard,
hypertext navigation, table-of-contents bookmarks and editing of forms.

%package -n lib%name
Group: System/Libraries
Summary: Libraries for the mate-document-viewer
Provides: %name-libs = %version-%release
Obsoletes: %name-libs

%description -n lib%name
This package contains shared libraries needed for mate-document-viewer.

%package devel
Group: Development/C
Summary: Support for developing back-ends for the mate-document-viewer

%description devel
This package contains libraries and header files needed for
mate-document-viewer back-ends development.

%package dvi
Summary: Atril backend for dvi files
Group: Graphical desktop/MATE

%description dvi
This package contains a backend to let atril display dvi files.

%package djvu
Summary: Atril backend for djvu files
Group: Graphical desktop/MATE

%description djvu
This package contains a backend to let atril display djvu files.

%package pixbuf
Summary: Atril backend for graphics files
Group: Graphical desktop/MATE

%description pixbuf
This package contains a backend to let atril display graphics files.

%package xps
Summary: Atril backend for xps files
Group: Graphical desktop/MATE

%description xps
This package contains a backend to let atril display xps files.

%package caja
Group: Graphical desktop/MATE
Summary: Mate-document-viewer extension for caja
Requires: mate-file-manager

%description caja
This package contains the mate-document-viewer extension for the
caja file manager.
It adds an additional tab called "Document" to the file properties dialog.

%package thumbnailer
Group: Graphical desktop/MATE
Summary: Atril thumbnailer extension for caja
Requires: mate-file-manager
BuildArch: noarch

%description thumbnailer
This package contains the atril extension for the
caja file manager.

%prep
%setup -q -n %rname-%version
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--disable-schemas-compile \
	--enable-introspection \
	--enable-gtk-doc \
	--enable-comics \
	--enable-dvi \
	--enable-djvu \
	--disable-t1lib \
	--enable-pixbuf \
	%{subst_enable xps} \
	%{subst_enable epub}

%make_build

%install
%make DESTDIR=%buildroot install

find %buildroot%_libdir -name \*.la -delete

%find_lang %rname --with-gnome --all-name

%files -f %rname.lang
%doc README COPYING NEWS AUTHORS
%_bindir/*
%_libexecdir/atrild
%_datadir/%rname
%_desktopdir/%rname.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/dbus-1/services/org.mate.atril.Daemon.service
%_datadir/glib-2.0/schemas/org.mate.Atril.gschema.xml
%_datadir/metainfo/atril.appdata.xml
%_man1dir/*.1*

%files -n lib%name
%_libdir/*.so.*
%_libdir/%rname/3/backends
%_libdir/girepository-1.0/AtrilDocument-1.5.0.typelib
%_libdir/girepository-1.0/AtrilView-1.5.0.typelib
%exclude %_libdir/atril/3/backends/libdvidocument.so*
%exclude %_libdir/atril/3/backends/dvidocument.atril-backend
%exclude %_libdir/atril/3/backends/libdjvudocument.so
%exclude %_libdir/atril/3/backends/djvudocument.atril-backend
%if_enabled xps
%exclude %_libdir/atril/3/backends/libxpsdocument.so*
%exclude %_libdir/atril/3/backends/xpsdocument.atril-backend
%endif
%exclude %_libdir/atril/3/backends/libpixbufdocument.so*
%exclude %_libdir/atril/3/backends/pixbufdocument.atril-backend

%files dvi
%_libdir/atril/3/backends/libdvidocument.so*
%_libdir/atril/3/backends/dvidocument.atril-backend

%files djvu
%_libdir/atril/3/backends/libdjvudocument.so
%_libdir/atril/3/backends/djvudocument.atril-backend

%if_enabled xps
%files xps
%_libdir/atril/3/backends/libxpsdocument.so*
%_libdir/atril/3/backends/xpsdocument.atril-backend
%endif

%files pixbuf
%_libdir/atril/3/backends/libpixbufdocument.so*
%_libdir/atril/3/backends/pixbufdocument.atril-backend

%files caja
%_libdir/caja/extensions-2.0/libatril-properties-page.so
%_datadir/caja/extensions/libatril-properties-page.caja-extension

%files thumbnailer
%_datadir/thumbnailers/atril.thumbnailer

%files devel
%_includedir/%rname
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/gir-1.0/Atril*.gir
%_datadir/gtk-doc/html/*

# TODO:
# -default subpackage to pull in backend deps

%changelog
* Wed Oct 16 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.2-alt1
- 1.22.2

* Tue Apr 23 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Wed Mar 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Tue Dec 18 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.3-alt1
- 1.20.3

* Wed Nov 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt2
- updated build dependencies

* Fri Jun 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Sat May 05 2018 Michael Shigorin <mike@altlinux.org> 1:1.20.1-alt2
- introduce epub, xps knobs (on by default)

* Tue Mar 27 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Fri Mar 16 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Sat Feb 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.19.4-alt2_1
- NMU: rebuild with texlive 2016
