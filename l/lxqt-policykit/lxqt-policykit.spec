# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lxqt-policykit
Version: 0.15.0
Release: alt1

Summary: Policykit authentication agent
License: LGPL
Group: Graphical desktop/Other

Url: https://lxqt.org
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel
BuildRequires: rpm-build-xdg libqtxdg-devel
BuildRequires: libpolkit-devel libpolkitqt5-qt5-devel
BuildRequires: kf5-kwindowsystem-devel

Provides: razorqt-polkit-agent = %version
Obsoletes: razorqt-polkit-agent < 0.7.0

Conflicts: lxqt-common <= 0.11.0

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
%_datadir/lxqt/translations/*
%_man1dir/*
%_xdgconfigdir/*/*
%doc AUTHORS CHANGELOG LICENSE README.md

%changelog
* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Sun Jan 27 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Fri May 25 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- 0.12.0

* Mon Sep 18 2017 Michael Shigorin <mike@altlinux.org> 0.11.0-alt2
- built against polkit-qt5

* Wed Oct 05 2016 Michael Shigorin <mike@altlinux.org> 0.11.0-alt1
- 0.11.0

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 0.10.0-alt1
- 0.10.0

* Mon Feb 09 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Tue Oct 21 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt2
- no need to spoonfeed cmake anymore (upstream#114)

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- replace razorqt-polkit-agent

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

