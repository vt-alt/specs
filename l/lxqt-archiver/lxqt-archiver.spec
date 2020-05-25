# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lxqt-archiver
Version: 0.2.0
Release: alt1

Summary: A simple & lightweight desktop-agnostic Qt file archiver
License: GPLv2
Group: Graphical desktop/Other

Url: https://lxqt.org
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: qt5-base-devel qt5-tools-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: libfm-qt-devel
BuildRequires: lxqt-build-tools
BuildRequires: libgio-devel
BuildRequires: libjson-glib-devel

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
%_prefix/libexec/%name
%_datadir/%name
%_iconsdir/hicolor/*/apps/*
%_desktopdir/%name.desktop
%doc AUTHORS CHANGELOG LICENSE README.md

%changelog
* Fri May 22 2020 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt1
- new version 0.2.0

* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.1.1-alt1
- Initial build
