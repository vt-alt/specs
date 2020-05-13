# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lxqt-powermanagement
Version: 0.15.0
Release: alt1

Summary: Powermanagement module for LXQt
License: LGPL
Group: Graphical desktop/Other

Url: https://lxqt.org
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel qt5-svg-devel
BuildRequires: kf5-kwindowsystem-devel kf5-solid-devel kf5-kidletime-devel
BuildRequires: rpm-build-xdg libqtxdg-devel

Requires: upower

Provides: razorqt-autosuspend = %version
Obsoletes: razorqt-autosuspend < 0.7.0

Provides: razorqt-power = %version
Obsoletes: razorqt-power < 0.7.0

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
%_desktopdir/*.desktop
%doc AUTHORS CHANGELOG LICENSE README.md
%_iconsdir/*/*/*/*.svg
%_xdgconfigdir/*/*

%changelog
* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Sun Jan 27 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Fri May 25 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Mon Feb 19 2018 Anton Midyukov <antohami@altlinux.org> 0.12.0-alt0.M80P.1
- backport to ALT p8

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- 0.12.0

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.11.0-alt1
- 0.11.0

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 0.10.0-alt1
- 0.10.0

* Sun Feb 08 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Tue Nov 25 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt2
- added Requires: upower (closes: #30507)

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- replace razorqt-autosuspend, razorqt-power

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

