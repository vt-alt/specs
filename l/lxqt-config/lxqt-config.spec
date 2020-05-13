# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lxqt-config
Version: 0.15.0
Release: alt1

Summary: LXDE-Qt system configurations (control center)
License: LGPL
Group: Graphical desktop/Other

Url: https://lxqt.org
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: libXau-devel libXcursor-devel libXdmcp-devel libXfixes-devel
BuildRequires: liblxqt-devel libqtxdg-devel qt5-base-devel qt5-tools-devel
BuildRequires: kf5-kwindowsystem-devel kf5-libkscreen-devel qt5-svg-devel
BuildRequires: rpm-build-xdg
BuildRequires: zlib-devel
BuildRequires: pkgconfig(xorg-libinput)
BuildRequires: libudev-devel

Provides: razorqt-config = %version
Obsoletes: razorqt-config < 0.7.0

Provides: lxqt-config-randr = %version
Obsoletes: lxqt-config-randr < 0.8.0

%description
%summary

%prep
%setup

%build
# FIXME: 0.10.0 fiddling with liblxqt-config-cursor.so (thx palinek)
%cmake -DCMAKE_SKIP_RPATH:BOOL=OFF \
       -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%_libdir/%name/*.so
%_datadir/lxqt/*
%_man1dir/*
%_xdgconfigdir/*/*
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*
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

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.11.0-alt1
- 0.11.0

* Wed Mar 23 2016 Michael Shigorin <mike@altlinux.org> 0.10.0-alt2
- rebuilt against KF5 5.6.0

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 0.10.0-alt1
- 0.10.0

* Mon Feb 09 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0
- lxqt-config-monitor replaces lxqt-config-randr

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- replace razorqt-config

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

