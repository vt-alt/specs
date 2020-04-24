
Name: udev-rules-ioschedulers
Version: 0.1.0
Release: alt2

Group: System/Configuration/Hardware
Summary: Udev rules for setup I/O schedulers
License: GPL-3.0-or-later
Url: http://git.altlinux.org/gears/u/%{name}.git

Provides: udev-rules-ioschdulers = %EVR
Obsoletes: udev-rules-ioschdulers < %EVR

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
* Thu Apr 23 2020 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt2
- rename package

* Wed Apr 22 2020 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- inital build
