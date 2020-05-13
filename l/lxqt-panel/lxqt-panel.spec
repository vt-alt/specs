# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lxqt-panel
Version: 0.15.0
Release: alt1

Summary: Desktop panel
License: LGPL
Group: Graphical desktop/Other

Url: https://lxqt.org
Source: %name-%version.tar
Patch: alt-settings.patch

BuildRequires(pre): rpm-build-xdg
BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel
BuildRequires: libqtxdg-devel qt5-base-devel qt5-tools-devel
BuildRequires: kf5-solid-devel
BuildRequires: kf5-kwindowsystem-devel
#kf5-kguiaddons-devel
BuildRequires: libdbusmenu-qt5-devel
BuildRequires: lxqt-globalkeys-devel
BuildRequires: libalsa-devel
BuildRequires: libXdmcp-devel libXdamage-devel
BuildRequires: libXcomposite-devel libXrender-devel libxcbutil-devel
BuildRequires: libmenu-cache-devel libstatgrab-devel libsensors3-devel
BuildRequires: libxkbcommon-devel libxkbcommon-x11-devel
BuildRequires: libgio-devel

# see bug 34612
BuildRequires: pkgconfig(libpulse)

BuildRequires: libsysstat-devel >= 0.3.0

Provides: razorqt-panel = %version
Obsoletes: razorqt-panel < 0.7.0

Conflicts: lxqt-common <= 0.11.0

Requires: menu-cache
Requires: udisks2 gvfs

%description
%summary

%package devel
Summary: Development headers for %name
Group: Development/C++
BuildArch: noarch
Requires: %name = %EVR

%description devel
This package provides the development files for %name.

%prep
%setup
%patch -p1

%build
%cmake -DVOLUME_USE_PULSEAUDIO=ON
%cmake_build

%install
%cmakeinstall_std

%files
%_man1dir/*
%_bindir/*
%_libdir/*/*.so
%_xdgconfigdir/*/*
%_datadir/lxqt/*
%_datadir/desktop-directories/*
%doc AUTHORS CHANGELOG LICENSE README.md

%files devel
%_includedir/*/*.h

%changelog
* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Mon Mar 23 2020 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt2
- rebuilt with libqtxdg-0.2.0

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Sun Jan 27 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Sat Sep 08 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt2
- full date worldclock applet
- expanded panel for worldclock applet

* Fri Jul 13 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1.1
- fix buildrequires

* Thu May 24 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Sat Apr 14 2018 Anton Midyukov <antohami@altlinux.org> 0.12.0-alt5
- replaced qupzilla to falkon in initial settings

* Tue Mar 06 2018 Anton Midyukov <antohami@altlinux.org> 0.12.0-alt4
- rebuild with libpulseaudio (Closes: 34612)

* Sat Feb 24 2018 Anton Midyukov <antohami@altlinux.org> 0.12.0-alt3
- fix initial settings (replace applet clock to worldclock)

* Sun Feb 18 2018 Anton Midyukov <antohami@altlinux.org> 0.12.0-alt2
- fix initial settings

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- 0.12.0

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.11.0-alt1
- 0.11.0
- disabled pulseaudio for build

* Tue Nov 03 2015 Michael Shigorin <mike@altlinux.org> 0.10.0-alt2
- drop R: qt5-dbus (tosses dev tools into menu for no good reason)

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 0.10.0-alt1
- 0.10.0

* Sun Feb 08 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Thu Nov 27 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt3
- require media related packages (closes: #30516)

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt2
- bad ELF symbols still in libpanelkbindicator.so, sigh

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Thu May 15 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt7
- R: menu-cache (bails out otherwise)

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt6
- drop libpanelkbindicator.so for now (looks like broken linking)

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt5
- replace razorqt-panel

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt4
- turn off unresolved ELF symbols check (hi, razorqt-0.4.1.1-alt2)

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt3
- relax ELF check for plugins

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- devel subpackage made noarch

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

