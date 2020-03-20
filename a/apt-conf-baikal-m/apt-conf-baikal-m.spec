Name: apt-conf-baikal-m
Version: 1.0
Release: alt1
Packager: Dmitry Terekhin <jqt4@altlinux.org>
Summary: Config file for hold grub version on Baikal-M system
License: %pubdomain
Group: System/Configuration/Boot and Init
Source1: grub-hold.conf
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

%description
This package contains a configuration file for prohibiting
grub updates on a system with a Baikal-M processor

%install
install -Dm0644 %SOURCE1 %buildroot%_sysconfdir/apt/apt.conf.d/grub-hold.conf

%files
%config(noreplace) %_sysconfdir/apt/apt.conf.d/grub-hold.conf

%changelog
* Thu Mar 12 2020 Dmitry Terekhin <jqt4@altlinux.org> 1.0-alt1
- Initial build.
