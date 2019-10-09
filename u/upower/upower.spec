%define _libexecdir %_prefix/libexec/upower
%def_enable gtk_doc
%def_enable check

Name: upower
Version: 0.99.11
Release: alt1

Summary: Power Management Service
License: GPLv2+
Group: System/Libraries
URL: http://cgit.freedesktop.org/upower/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: DeviceKit-power = 016
Obsoletes: DeviceKit-power < 016
Requires: lib%name = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%define glib_ver 2.34
%define dbus_ver 1.9.18

Requires: dbus >= %dbus_ver

BuildRequires: libgio-devel >= %glib_ver
BuildRequires: gtk-doc libusb-devel libgudev-devel libdbus-devel >= %dbus_ver
BuildRequires: libpolkit-devel libudev-devel gobject-introspection-devel
BuildRequires: libimobiledevice-devel pkgconfig(systemd)
%{?_enable_check:BuildRequires: /proc python3 python3-module-dbusmock libumockdev-gir python3-module-dbus}

%description
UPower provides a daemon, API and command line tools for
managing power devices attached to the system.

%package -n lib%name
Summary: %name libraries
Group: System/Libraries
Provides: libdevkit-power = 016
Obsoletes: libdevkit-power < 016

%description -n lib%name
Libraries for %name

%package -n lib%name-devel
Summary: Development libraries and headers for %name
Group: Development/C
Requires: lib%name = %version-%release
Provides: libdevkit-power-devel = 016
Obsoletes: libdevkit-power-devel < 016

%description -n lib%name-devel
Headers, libraries and API docs for %name

%package -n lib%name-gir
Summary: GObject introspection data for the UPower library
Group: System/Libraries
Requires: lib%name = %version-%release
Provides: libdevkit-power-gir = 016
Obsoletes: libdevkit-power-gir < 016

%description -n lib%name-gir
GObject introspection data for the UPower library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the UPower library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release lib%name-devel = %version-%release
Provides: libdevkit-power-gir-devel = 016
Obsoletes: libdevkit-power-gir-devel < 016

%description -n lib%name-gir-devel
GObject introspection devel data for the UPower library

%prep
%setup
#%%patch -p1

rm -f acinclude.m4

%build
%autoreconf
%configure \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--libexecdir=%_libexecdir \
	--localstatedir=%_var \
	--disable-static
%make_build

%install
%makeinstall_std

%find_lang %name

%check
%ifnarch %ix86
PYTHON=%__python3 %make check
%endif

%files -f %name.lang
%doc AUTHORS NEWS README
%dir %_sysconfdir/UPower
%_sysconfdir/UPower/*.conf
%_unitdir/*
/lib/udev/rules.d/*.rules
%_bindir/*
%_libexecdir/*
%_datadir/dbus-1/system.d/*.conf
%_datadir/dbus-1/system-services/*.service
%_mandir/man?/*
%dir %_var/lib/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/dbus-1/interfaces/*.xml
%_datadir/gtk-doc/html/*

%files -n lib%name-gir
%_typelibdir/*.typelib

%files -n lib%name-gir-devel
%_girdir/*.gir

%changelog
* Fri Oct 04 2019 Yuri N. Sedunov <aris@altlinux.org> 0.99.11-alt1
- 0.99.11

* Thu Mar 21 2019 Yuri N. Sedunov <aris@altlinux.org> 0.99.10-alt1
- updated to UPOWER_0_99_10-5-ge06bfc6

* Tue Nov 06 2018 Yuri N. Sedunov <aris@altlinux.org> 0.99.9-alt1
- 0.99.9

* Tue Jul 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.99.8-alt1
- 0.99.8
- enabled %%check

* Mon Dec 25 2017 Yuri N. Sedunov <aris@altlinux.org> 0.99.7-alt1
- 0.99.7

* Mon Sep 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.99.6-alt1
- 0.99.6

* Wed Aug 30 2017 Yuri N. Sedunov <aris@altlinux.org> 0.99.5-alt2
- updated to UPOWER_0_99_5-2-g6aff8b3

* Tue Aug 01 2017 Yuri N. Sedunov <aris@altlinux.org> 0.99.5-alt1
- 0.99.5

* Tue Aug 02 2016 Yuri N. Sedunov <aris@altlinux.org> 0.99.4-alt2
- updated to 0.99.4-alt1-11-gee27a4c (ALT #32335)

* Sat Feb 20 2016 Yuri N. Sedunov <aris@altlinux.org> 0.99.4-alt1
- 0.99.4

* Sun May 31 2015 Yuri N. Sedunov <aris@altlinux.org> 0.99.3-alt1
- 0.99.3 release

* Tue May 12 2015 Yuri N. Sedunov <aris@altlinux.org> 0.99.2-alt3
- 0.99.3_bb415e27 (fixed FDO #89476)

* Mon Feb 23 2015 Yuri N. Sedunov <aris@altlinux.org> 0.99.2-alt2
- 0.99.3 snapshot with fixes for iDevice
- built against libimobiledevice.so.6

* Tue Dec 23 2014 Yuri N. Sedunov <aris@altlinux.org> 0.99.2-alt1
- 0.99.2

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 0.99.1-alt1
- 0.99.1
- built against libimobiledevice.so.5/libplist.so.3

* Fri Jun 20 2014 Yuri N. Sedunov <aris@altlinux.org> 0.99.0-alt2
- rebuilt against libplist.so.2

* Thu Feb 06 2014 Yuri N. Sedunov <aris@altlinux.org> 0.99.0-alt1
- 0.99.0

* Sat Nov 23 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.23-alt1
- 0.9.23

* Wed Apr 24 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.20-alt2
- rebuilt against libimobiledevice.so.4

* Tue Mar 19 2013 Valery Inozemtsev <shrek@altlinux.ru> 0.9.20-alt1
- 0.9.20

* Mon Jan 14 2013 Valery Inozemtsev <shrek@altlinux.ru> 0.9.19-alt1
- 0.9.19

* Tue Jun 26 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.9.17-alt1
- 0.9.17

* Wed May 02 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.9.16-alt1
- 0.9.16

* Mon Apr 09 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.9.15-alt2
- rebuild with libimobiledevice 1.1.3

* Mon Dec 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.15-alt1
- 0.9.15

* Mon Oct 03 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.14-alt1
- 0.9.14

* Tue Sep 06 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.13-alt1
- 0.9.13

* Tue Jul 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.12-alt1
- 0.9.12

* Sat May 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.11-alt1
- 0.9.11

* Wed May 04 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.10-alt1
- 0.9.10

* Mon Mar 21 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.9-alt1
- 0.9.9

* Fri Jan 07 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Fri Nov 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.7-alt3
- dropped unused DeviceKit

* Fri Nov 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.7-alt2
- packaged /var/lib/upower

* Thu Nov 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Wed Oct 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.6-alt2
- fixed building with gobject-introspection 0.9.10

* Mon Oct 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Fri Jul 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Wed May 12 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Thu May 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Wed Apr 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Thu Apr 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt3
- rebuild

* Wed Mar 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt2
- rebuild with rpm-build-gir

* Wed Mar 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Mon Feb 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 015-alt1
- UPower 0.9.0

* Sat Jan 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 014-alt1
- 014

* Mon Dec 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 013-alt2
- fised build gtk doc

* Wed Dec 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 013-alt1
- 013

* Fri Nov 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 012-alt2
- fixed incorrect battery recall warning for Lenovo T61

* Mon Oct 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 012-alt1
- 012

* Fri Oct 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 011-alt1
- 011

* Mon Aug 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 010-alt1
- 010

* Mon Jul 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 009-alt1
- 009

* Mon Jun 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 008-alt1
- 008

* Wed May 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 007-alt4
- git snapshot 2009-05-26 (cf9692f1e93fd32759530fa98ec7b5947795eb6d)
- relocated devel files

* Fri May 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 007-alt3
- git snapshot 2009-05-13 (296a09988bba71183635843f143979c7551fc0f3)

* Mon Apr 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 007-alt2
- added hibernate-script support

* Sat Apr 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 007-alt1
- 007

* Mon Dec 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 002-alt1
- initial release

