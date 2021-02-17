
Name: udev-rules-ioschedulers
Version: 0.2.0
Release: alt1

Group: System/Configuration/Hardware
Summary: Udev rules for setup I/O schedulers
License: FDL-1.3
Url: https://wiki.archlinux.org/index.php/improving_performance

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
* Thu Feb 11 2021 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt1
- update NVMe rules

* Thu Apr 23 2020 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt2
- rename package

* Wed Apr 22 2020 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- inital build
