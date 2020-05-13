Name:     lxqt-sudo
Version:  0.15.0
Release:  alt1

Summary:  GUI frontend for sudo/su
License:  LGPL-2.1
Group:    Other
Url:      https://github.com/lxqt/lxqt-sudo

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: liblxqt-devel
BuildRequires: qt5-tools-devel
BuildRequires: kf5-kwindowsystem-devel

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
%doc *.md
%_bindir/*
%_datadir/lxqt/translations/%name/
%_man1dir/*

%changelog
* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- Initial build for Sisyphus
