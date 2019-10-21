Name: libmateweather
Version: 1.22.1
Release: alt1
Epoch: 1
Summary: Libraries to allow MATE Desktop to display weather information
License: GPLv2+ and LGPLv2+
Group: System/Libraries
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: %name-data = %epoch:%version-%release

BuildRequires: mate-common gtk-doc libgtk+3-devel libsoup-devel libxml2-devel

%description
Libraries to allow MATE Desktop to display weather information

%package data
Group: System/Libraries
Summary: Data files for the libmateweather
BuildArch: noarch

%description data
This package contains shared data needed for libmateweather

%package devel
Group: Development/C
Summary:  Development files for libmateweather

%description devel
Development files for libmateweather

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--enable-gtk-doc-html \
	--enable-locations-compression \
	--disable-static \
	--disable-schemas-compile

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name --with-gnome --all-name

%files
%doc AUTHORS COPYING README
%_libdir/%name.so.*
%_datadir/glib-2.0/schemas/org.mate.weather.gschema.xml

%files data -f %name.lang
%_iconsdir/mate/*/status/*
%_datadir/%name

%files devel
%_includedir/%name
%_libdir/%name.so
%_pkgconfigdir/*.pc

%changelog
* Tue Oct 15 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Mon Mar 04 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Tue Dec 18 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.20.1-alt1.qa1
- NMU: applied repocop patch

* Fri Jun 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Mon Mar 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Mon Feb 19 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
