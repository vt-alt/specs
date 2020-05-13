# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: obconf-qt
Version: 0.15.0
Release: alt1

Summary: Openbox configuration tool
License: %gpl2plus
Group: Graphical desktop/Other

Url: https://lxqt.org
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel
BuildRequires: pkgconfig(expat)
BuildRequires: libopenbox-devel

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
%_datadir/%name
%_liconsdir/*
%doc AUTHORS CHANGELOG README.md

%changelog
* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Mon Jan 28 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Thu May 24 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Tue Sep 26 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- 0.12.0

* Mon May 29 2017 Michael Shigorin <mike@altlinux.org> 0.11.1-alt1
- 0.11.1

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.11.0-alt1
- 0.11.0
  + built against Qt5

* Tue Nov 03 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt2
- rebuilt against current libraries

* Mon Sep 14 2015 Aleksey Avdeev <solo@altlinux.org> 0.9.0-alt1
- 0.9.0
- Fix license

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt2
- rebuilt against current libraries

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt1
- initial release

