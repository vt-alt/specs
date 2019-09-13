%define ver_major 2.8
%define api_ver 1.0
%define _libexecdir %_prefix/libexec

%def_enable gtk_doc
%def_disable gtk_tests
%def_enable check

Name: iio-sensor-proxy
Version: %ver_major
Release: alt1

Summary: IIO sensors to input device proxy
Group: System/Kernel and hardware
License: GPLv2+
Url: https://github.com/hadess/%name

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%define gudev_ver 232

BuildRequires: gnome-common gtk-doc
BuildRequires: libgio-devel systemd-devel
BuildRequires: libudev-devel libgudev-devel >= %gudev_ver
%{?_enable_gtk_tests:BuildRequires: libgtk+3-devel}
%{?_enable_check:BuildRequires: /proc dbus-tools-gui}

%description
%name is a framework for accessing the various environmental sensors
(e.g., accelerometer, magnetometer, proximity, or ambient-light sensors)
built in to recent laptops. The proxy is a daemon that listens to the
Industrial I/O (IIO) subsystem and provides access to the sensor readings
over D-Bus.

As of right now, support for ambient-light sensors and accelerometers is
working; other sensor types are in development. The current API is based
on those used by Android and iOS, but may be expanded in the future. "For
future versions, we'll want to export the raw accelerometer readings, so
that applications, including games, can make use of them, which might
bring up security issues. SDL, Firefox, WebKit could all do with being
adapted, in the near future."


%package devel-doc
Summary: Developer documentation for %name
Group: Development/C
Conflicts: %name < %version
BuildArch: noarch

%description devel-doc
Developer documentation for %name.

%prep
%setup
%patch -p1
[ ! -d m4 ] && mkdir m4

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%autoreconf
%configure \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{?_disable_gtk_tests:--disable-gtk-tests}
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_sbindir/%name
%_bindir/monitor-sensor
%_unitdir/%name.service
%_udevrulesdir/80-%name.rules
%_sysconfdir/dbus-1/system.d/net.hadess.SensorProxy.conf
%doc README.md NEWS

%files devel-doc
%_datadir/gtk-doc/html/%name/


%changelog
* Sun Sep 08 2019 Yuri N. Sedunov <aris@altlinux.org> 2.8-alt1
- 2.8

* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 2.7-alt1
- 2.7

* Thu Oct 25 2018 Yuri N. Sedunov <aris@altlinux.org> 2.5-alt1
- updated to 2.5-6-gbb35319

* Mon Nov 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4-alt1
- 2.4

* Sun Sep 24 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3-alt1
- 2.3

* Fri Feb 17 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2-alt1
- 2.2

* Sun Feb 05 2017 Yuri N. Sedunov <aris@altlinux.org> 2.1-alt1
- 2.1

* Thu Dec 15 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0-alt1
- 2.0

* Mon Sep 26 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt1
- 1.3

* Wed Aug 17 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt2
- updated to 1.1-28-gae82958

* Mon Jul 27 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- 1.1

* Sat May 23 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- first build for Sisyphus

