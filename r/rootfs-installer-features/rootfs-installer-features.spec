
%define _unpackaged_files_terminate_build 1

Name: rootfs-installer-features
Version: 0.1
Release: alt1

Summary: Run installer features during install via rootfs
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

BuildRequires: rpm-macros-alterator
Requires: alterator-setup => 0.3.3
Conflicts: installer-common-stage2 livecd-installer-features

%description
%summary

%prep
%setup

%install
install -pDm644 -t %buildroot/%_sbindir scripts/install2-*-functions

mkdir -p %buildroot%_alterator_libdir
cp -a hooks %buildroot%_alterator_libdir/

%files
%_sbindir/install2-*-functions
%_alterator_libdir/hooks/*/*

%changelog
* Fri Dec 06 2019 Ivan A. Melnikov <iv@altlinux.org> 0.1-alt1
- initial build
