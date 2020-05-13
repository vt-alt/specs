# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lxqt-themes
Version: 0.15.0
Release: alt1

Summary: Themes, graphics and icons for LXQt
License: LGPL 2.1+ and 3.0, CC-BY-SA 3.0
Group: Graphical desktop/Other

Url: https://lxqt.org
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: lxqt-build-tools

Provides: lxqt-common = %version
Obsoletes: lxqt-common < 0.12.0

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
%_datadir/lxqt/*
%_iconsdir/*/*/*/*
%doc AUTHORS CHANGELOG README.md

%changelog
* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Sun Jan 27 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Fri May 25 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Mon Oct 23 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt3
- *noarch*

* Mon Oct 23 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt2
- noarch

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- initial release

