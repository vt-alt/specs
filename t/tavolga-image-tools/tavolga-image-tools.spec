Name: tavolga-image-tools
Version: 3.0
Release: alt1
Summary: Helpers for building images for Tavolga Terminal
License: BSD (revised)
Group: System/Configuration/Other
Url: https://git.altlinux.org/people/jqt4/packages/generate-recovery-rc.git
BuildArch: noarch
Source0: generate-recovery-rc
Source1: recovery.rc
Source2: build-recovery-tar

%add_findreq_skiplist %_datadir/%name/*

%description
Helpers for building images for Tavolga Terminal 2BT1
and similar systems.

Install this package if you want to build recovery.tar
images for such systems via mkimage-profiles.

%install
install -Dpm 0755 %SOURCE0 %buildroot%_bindir/generate-recovery-rc
install -Dpm 0644 %SOURCE1 %buildroot%_datadir/%name/recovery.rc
install -Dpm 0755 %SOURCE2 %buildroot%_bindir/build-recovery-tar

%files
%_bindir/*
%_datadir/%name

%changelog
* Mon Sep 02 2019 Ivan A. Melnikov <iv@altlinux.org> 3.0-alt1
- add build-recovery-tar tool

* Mon Aug 26 2019 Ivan A. Melnikov <iv@altlinux.org> 2.0-alt1
- update recovery.rc template
- give package a less generic name
- minor coding style chages

* Thu Jun 20 2019 Dmitry Terekhin <jqt4@altlinux.org> 1.0-alt1
- Initial build
