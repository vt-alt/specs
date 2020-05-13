# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: compton-conf
Version: 0.15.0
Release: alt1

Summary: GUI configuration tool for compton X composite manager
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake git-core
BuildRequires: lxqt-build-tools >= 0.6
BuildRequires: qt5-base-devel qt5-tools-devel
BuildRequires: pkgconfig(libconfig++) pkgconfig(libconfig)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(lxqt)

Requires: compton >= 5

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%_desktopdir/*
%_datadir/%name/
%_sysconfdir/xdg/autostart/*.desktop
%doc AUTHORS COPYING README.md

%changelog
* Mon Apr 27 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Mon Jan 28 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Tue Mar 20 2018 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- new version 0.3.0

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt2
- rebuilt against current libraries

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt1
- initial release

