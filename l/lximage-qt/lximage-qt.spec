# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lximage-qt
Version: 0.15.0
Release: alt1

Summary: Image viewer and screenshot tool
License: LGPL
Group: Graphical desktop/Other

Url: https://lxqt.org
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: libXdmcp-devel libXfixes-devel libexif-devel
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: libfm-devel libfm-qt-devel
BuildRequires: libmenu-cache-devel >= 0.5.0
BuildRequires: glib2-devel libpcre-devel

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
%_iconsdir/*/*/*/*
%_desktopdir/*.desktop
%_datadir/%name
%doc AUTHORS CHANGELOG README.md

%changelog
* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Mon Jan 28 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Fri May 25 2018 Anton Midyukov <antohami@altlinux.org> 0.7.0-alt1
- new version 0.7.0

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.6.0-alt1
- 0.6.0

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.5.0-alt1
- 0.5.0

* Tue Nov 03 2015 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1
- 0.4.0

* Mon Feb 09 2015 Michael Shigorin <mike@altlinux.org> 0.3.0-alt2.git62ce73d
- rebuilt against qt5 using git commit 62ce73d

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.3.0-alt1
- so it was 0.3.0 actually

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.2.0-alt3
- use commit ge1eb450

* Wed Aug 27 2014 Michael Shigorin <mike@altlinux.org> 0.2.0-alt2
- rebuilt against libfm-qt 0.8.0

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.2.0-alt1
- initial release

