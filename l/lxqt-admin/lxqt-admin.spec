# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:     lxqt-admin
Version:  0.15.0
Release:  alt1

Summary:  LXQt system administration tool
License:  LGPL-2.1
Group:    Graphical desktop/Other
Url:      https://github.com/lxqt/lxqt-admin

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: lxqt-build-tools
BuildRequires: liblxqt-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: libpolkitqt5-qt5-devel

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
%_datadir/lxqt/translations/*
%_datadir/polkit-1/actions/
%doc AUTHORS CHANGELOG *.md

%changelog
* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Mon Jan 28 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
