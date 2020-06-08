# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lxqt-qtplugin
Version: 0.15.1
Release: alt1

Summary: LxQt platform integration plugin for Qt
License: LGPL
Group: Graphical desktop/Other

Url: https://lxqt.org
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel libqtxdg-devel
BuildRequires: libdbusmenu-qt5-devel
BuildRequires: libfm-qt-devel

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
%_libdir/qt5/plugins/*/libqtlxqt.so
%doc AUTHORS CHANGELOG LICENSE README.md

%changelog
* Sat Jun 06 2020 Anton Midyukov <antohami@altlinux.org> 0.15.1-alt1
- new version 0.15.1

* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Sun Jan 27 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Tue Aug 14 2018 Sergey V Turchin <zerg@altlinux.org> 0.13.0-alt2
- rebuild with new Qt

* Thu May 24 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- 0.12.0

* Thu Oct 19 2017 Sergey V Turchin <zerg@altlinux.org> 0.11.0-alt3
- rebuilt against current qt

* Mon Aug 21 2017 Michael Shigorin <mike@altlinux.org> 0.11.0-alt2
- rebuilt against current qt (closes: #33756)

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.11.0-alt1
- 0.11.0

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 0.10.0-alt1
- 0.10.0

* Sun Feb 08 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0 built against qt5

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt2
- whoops, missed qtxdg somehow

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

