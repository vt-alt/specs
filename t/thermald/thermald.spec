# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define _localstatedir /var

%def_without monitor

Name: thermald
Version: 2.2
Release: alt1

Summary: Thermal daemon for IA

License: GPLv2+
Group: System/Kernel and hardware
Url: https://github.com/01org/thermal_daemon
# Source-url: https://github.com/01org/thermal_daemon/archive/v%version.tar.gz

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Source1: thermald.init
Source2: %name-monitor.svg

ExclusiveArch: x86_64

BuildRequires: gcc-c++ libgomp-devel
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: libdbus-glib-devel
BuildRequires: systemd-devel
BuildRequires: gtk-doc
BuildRequires: liblzma-devel
BuildRequires: libupower-devel
BuildRequires: libevdev-devel
BuildRequires: autoconf-archive
Requires: dbus

%description
Thermal issues are important to handle proactively to reduce performance impact.

The project provides a Linux user mode daemon to system developers, reducing
time to market with controlled thermal management using P-states, T-states, and
the Intel power clamp driver. The Thermal Daemon uses the existing Linux kernel
infrastructure and can be easily enhanced.

%description -l ru_RU.UTF-8
thermald представляет собой службу, которая управляет питанием с помощью
Р-состояний, Т-состояния и Intel power clamp driver. thermald использует
существующую инфраструктуру ядра Linux, и его возможности могут быть легко
расширены.

%if_with monitor
%package monitor
Summary: Application for monitoring %name
License: GPLv3+
Group: Monitoring
BuildRequires: qt5-base-devel
Requires: %name

%description monitor
This package contains an Application to monitor %name for system
developers who want to enable application developers and their
customers with the responsive and flexible thermal management,
supporting optimal performance in desktop, clam-shell, mobile and
embedded devices.
%endif

%prep
%setup

%build
./autogen.sh
%configure \
    --disable-option-checking \
    --disable-silent-rules
%make_build

%if_with monitor
# Build the monitor-app.
pushd tools/thermal_monitor
mkdir -p %_target_platform
pushd %_target_platform
%qmake_qt5 ..
%make_build
popd
popd
%endif

%install
%makeinstall_std
install -pD -m644 data/%name.service \
    %buildroot%_unitdir/%name.service
install -pD -m755 %SOURCE1 %buildroot%_initdir/%name

# Install management-script
install -Dpm 0755 tools/thermald_set_pref.sh \
    %buildroot%_bindir/%name-set-pref

# DBus config belongs into %%_datadir
mkdir -p %buildroot%_datadir/dbus-1
mv -f %buildroot%_sysconfdir/dbus-1/* %buildroot%_datadir/dbus-1/

# Install tmpfiles.d
mkdir -p alt_addons
cat << EOF > alt_addons/%name.conf
d /run/%name 0755 root root -
EOF

install -Dpm 0644 alt_addons/%name.conf \
    %buildroot%_tmpfilesdir/%name.conf

# Install config
install -Dpm 0644 data/thermal-conf.xml \
    %buildroot%_sysconfdir/%name/thermal-conf.xml

%if_with monitor
# Create desktop-file for the monitor-app
cat << EOF > alt_addons/%name-monitor.desktop
[Desktop Entry]
Name=%name Monitor
Comment=Application for monitoring %name
Icon=%name-monitor
Categories=System;Settings;
Exec=%_bindir/ThermalMonitor
Type=Application
StartupNotify=true
Terminal=false
EOF

# Install the monitor-app
install -Dpm 0755 tools/thermal_monitor/%_target_platform/ThermalMonitor \
    %buildroot%_bindir/ThermalMonitor
install -Dpm 0644 alt_addons/%name-monitor.desktop \
    %buildroot%_desktopdir/%name-monitor.desktop
install -Dpm 0644 %SOURCE2 \
    %buildroot%_iconsdir/hicolor/scalable/apps/%name-monitor.svg

# Create ReadMe.txt for the monitor-app
cat << EOF > alt_addons/ReadMe
Running the thermald-monitor-app
--------------------------------

To communicate with thermald via dbus, the user has to be member
of the "power" group. So make sure to add your user id to this
group before using the thermald-monitor-app.
EOF

%endif

%pre
%_bindir/getent group power >/dev/null || %_sbindir/groupadd -r power
exit 0

%post
%post_service thermald

%preun
%preun_service thermald

%files
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/thermal-conf.xml
%config(noreplace) %_sysconfdir/%name/thermal-cpu-cdev-order.xml
%doc README.txt thermal_daemon_usage.txt COPYING
%_tmpfilesdir/%name.conf
%_sbindir/%name
%_bindir/%name-set-pref
%_datadir/dbus-1/system-services/org.freedesktop.%name.service
%_datadir/dbus-1/system.d/org.freedesktop.%name.conf
%_unitdir/%name.service
%_initdir/%name
%_man5dir/*
%_man8dir/*

%if_with monitor
%files monitor
%doc alt_addons/ReadMe tools/thermal_monitor/qcustomplot/GPL.txt
%_bindir/ThermalMonitor
%_desktopdir/%name-monitor.desktop
%_iconsdir/hicolor/scalable/apps/%name-monitor.svg
%endif

%changelog
* Mon Nov 09 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.2-alt1
- new version 2.2
  + change packaging scheme to git subtree

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 1.8-alt2
- Update buildrequires (Fix FTBFS)

* Sun Oct 21 2018 Anton Midyukov <antohami@altlinux.org> 1.8-alt1
- new version 1.8
- exclusive arch x86_64

* Sun Jul 08 2018 Anton Midyukov <antohami@altlinux.org> 1.7.2-alt1
- new version 1.7.2
- exclusive arch ix86 and x86_64

* Sat Oct 28 2017 Anton Midyukov <antohami@altlinux.org> 1.7.1-alt1
- new version (1.7.1) with rpmgs script

* Fri Mar 10 2017 Anton Midyukov <antohami@altlinux.org> 1.6-alt1
- new version (1.6) with rpmgs script

* Sat Dec 10 2016 Anton Midyukov <antohami@altlinux.org> 1.5.4-alt1
- new version (1.5.4) with rpmgs script

* Wed Oct 05 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.3-alt2
- Fixed the adaption of the Debian-style .init for ALT:
  + .init: condrestart/condstop implemented in a simple way;
  + .init: status cmd added;
  + .init: do not print DONE when printing the usage.
- (.spec) Do not own dbus and systemd dirs.

* Fri May 27 2016 Anton Midyukov <antohami@altlinux.org> 1.5.3-alt1
- New version.

* Mon Mar 21 2016 Anton Midyukov <antohami@altlinux.org> 1.4.3-alt2
- Remove init-condrestart.

* Tue Feb 16 2016 Anton Midyukov <antohami@altlinux.org> 1.4.3-alt1
- Initial build for Altlinux Sisyphus.
