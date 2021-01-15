# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Summary: GTK+ based GUI for controlling CDEmu daemon
Summary(ru_RU.UTF-8): Основанная на GTK+ GUI для управления CDEmu
Name: gcdemu
Version: 3.2.4
Release: alt1
Group: Emulators
License: GPLv2+
Url: http://cdemu.sourceforge.net/
Packager: Anton Midyukov <antohami@altlinux.org>

Source: http://downloads.sourceforge.net/cdemu/%name-%version.tar.bz2
Patch1: autostart.patch
Patch3: fix_desktop.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-gir
BuildRequires: cmake intltool

Requires: cdemu-daemon >= %version
Requires: cdemu-client >= %version
Requires: typelib(Gtk) = 3.0
%filter_from_requires /^typelib(AppIndicator3)/d

BuildArch: noarch

%description
gCDEmu is a Gtk+ based GUI for controlling CDEmu daemon. It is part of the
userspace-cdemu suite, a free, GPL CD/DVD-ROM device emulator for linux.

It provides a graphic interface that allows performing the key tasks related to
controlling the CDEmu daemon, such as loading and unloading devices, displaying
devices' status and retrieving/setting devices' debug masks.

In addition, it listens to signals emitted by CDEmu daemon and provides
notifications via libnotify.

%description -l ru_RU.UTF-8
gCDEmu - базирующийся на Gtk+ и Appindicator апплет в области уведомлений для
управления службой CDEmu. Является частью проекта CDEmu, свободного (GPL)
эмулятора устройств CD/DVD-ROM для Линукс.

Обеспечивает графический интерфейс, который позволяет выполнять основные задачи,
связанные с управлением службой CDEmu, например монтирование и размонтирование
образов, отображение статуса виртуальных устройств CD/DVD-ROM.

Кроме того, он слушает сигналы, посылаемые службой CDEmu и обеспечивает вывод
уведомлений, используя библиотеку libnotify.

%prep
%setup
%patch1 -p1
%patch3 -p2

#fix PATH to python3
sed 's|/usr/bin/env python3|/usr/bin/python3|' -i src/%name

%build
%cmake_insource
%make_build

%install
%makeinstall_std
%find_lang %name
mkdir -p %buildroot/%_sysconfdir/xdg/autostart/
mv %buildroot/%_desktopdir/%name.desktop %buildroot/%_sysconfdir/xdg/autostart/

%files -f %name.lang
%doc README AUTHORS
%_bindir/%name
%_pixmapsdir/gcdemu*.svg
%_datadir/glib-2.0/schemas/net.sf.cdemu.gcdemu.gschema.xml
%_sysconfdir/xdg/autostart/%name.desktop

%changelog
* Thu Jan 07 2021 Anton Midyukov <antohami@altlinux.org> 3.2.4-alt1
- new version (3.2.4)
- Add requires typelib(Gtk) = 3.0
- Skip requires typelib(AppIndicator3)

* Mon Jul 30 2018 Anton Midyukov <antohami@altlinux.org> 3.2.0-alt1
- new version (3.2.0) with rpmgs script

* Thu Aug 03 2017 Anton Midyukov <antohami@altlinux.org> 3.1.0-alt1
- new version (3.1.0) with rpmgs script

* Sun Mar 12 2017 Anton Midyukov <antohami@altlinux.org> 3.0.2-alt2
- Added buildrequires rpm-build-gir.

* Fri Oct 14 2016 Anton Midyukov <antohami@altlinux.org> 3.0.2-alt1
- New version.

* Fri Sep 23 2016 Anton Midyukov <antohami@altlinux.org> 3.0.1-alt3
- Fix requires (Closes: 32518).

* Sun Apr 03 2016 Anton Midyukov <antohami@altlinux.org> 3.0.1-alt2
- Added russian translation of git
- fix desktop file

* Thu Jan 14 2016 Anton Midyukov <antohami@altlinux.org> 3.0.1-alt1
- New version;
- Added russian translation.

* Sun Oct 18 2015 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt2
- Added autostart.patch;
- Added requires: cdemu-client.

* Mon Sep 21 2015 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt1
- Initial build for ALT Linux Sisyphus.
