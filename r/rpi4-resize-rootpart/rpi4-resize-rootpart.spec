%define rszr rpi4-resize-rootpart

Name: rpi4-resize-rootpart
Version: 0.1
Release: alt1
Summary: Enlarge the root partition as much as possible
License: GPL
Group: System/Configuration/Other
Packager: Dmitry Terekhin <jqt4@altlinux.org>
Url: https://git.altlinux.org/people/jqt4/packages/rpi4-resize-rootpart.git
BuildArch: noarch
Source0: %rszr

%description
%summary

%install
install -Dpm 0755 %SOURCE0 %buildroot%_sysconfdir/firsttime.d/%rszr

%files
%_sysconfdir/firsttime.d/%rszr

%changelog
* Fri Jun 05 2020 Dmitry Terekhin <jqt4@altlinux.org> 0.1-alt1
- Initial build
