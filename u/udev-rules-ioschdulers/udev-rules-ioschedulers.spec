
Name: udev-rules-ioschdulers
Version: 0.1.0
Release: alt1

Group: System/Configuration/Hardware
Summary: Udev rules for setup I/O schedulers
License: GPL-3.0-or-later
Url: http://git.altlinux.org/gears/u/%{name}.git

BuildArch: noarch

Source: ioschedulers.rules

#BuildRequires:

%description
This package provides an UDEV rules for setup disks I/O schedulers to optimize filesystem performance.

%prep

%install
mkdir -p %buildroot/%_udevrulesdir
install -m 0644 %SOURCE0 %buildroot/%_udevrulesdir/50-ioschedulers.rules

%files
%_udevrulesdir/*ioschedulers*.rules

%changelog
* Wed Apr 22 2020 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- inital build
