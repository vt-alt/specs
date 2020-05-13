# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:    pcmanfm-qt
Version: 0.15.0
Release: alt1
Epoch: 1

Summary: PCManFM-Qt is the Qt port of the LXDE file manager PCManFM
License: GPLv2+
Group:   File tools

Url:     https://lxqt.org
Source0: %name-%version.tar
Source1: %name.desktop

# fix initial settigs
Patch: alt-settings.patch

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: qt5-base-devel qt5-tools-devel
BuildRequires: libfm-qt-devel >= 0.14.0
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: liblxqt-devel
BuildRequires: libmenu-cache-devel
BuildRequires: rpm-build-xdg

Requires: menu-cache

%description
PCManFM-Qt is the Qt port of the LXDE file manager PCManFM.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
install -pDm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/*
%_desktopdir/*.desktop
%_xdgconfigdir/*/*
%_datadir/%name
%_man1dir/*
%doc AUTHORS CHANGELOG LICENSE README.md

%changelog
* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 1:0.15.0-alt1
- new version 0.15.0

* Thu Jun 06 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt2
- set default background (design-current)

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Mon Jan 28 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Sat May 26 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Tue May 08 2018 Anton Midyukov <antohami@altlinux.org> 0.12.0-alt3
- Enabled quick execution in the file manager

* Sun Feb 18 2018 Anton Midyukov <antohami@altlinux.org> 0.12.0-alt2
- fix initial settigs

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- 0.12.0

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.11.1-alt1
- 0.11.1
  + libfm-qt is now a separate package

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 0.10.0-alt1
- 0.10.0

* Wed Sep 30 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt2
- added BR: qt5-svg-devel (thx george@)

* Mon Feb 09 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0 built against qt5

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt2
- rebuilt against 0.8.0 release libraries

* Wed Aug 27 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- 0.7.0

* Mon Mar 31 2014 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt4.gitf58b1b7
- Increase release number to backport to p7 branch

* Tue Mar 18 2014 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt3.gitf58b1b7
- New snapshot
- Fix requirement on development packages
- Link with libfm2

* Mon Apr 08 2013 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt2.gite99916f
- New snapshot

* Tue Mar 05 2013 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1
- Initial build in Sisyphus
