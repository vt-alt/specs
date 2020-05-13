# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: libfm-qt
Version: 0.15.0
Release: alt1

Summary: Core library of PCManFM-Qt file manager
License: LGPLv2+
Group: System/Libraries

Url: https://lxqt.org
Source: %name-%version.tar

BuildRequires: cmake rpm-macros-cmake
BuildRequires: rpm-build-xdg
BuildRequires: gcc-c++
BuildRequires: lxqt-build-tools >= 0.5.0
BuildRequires: libexif-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(libmenu-cache) >= 1.1.0

Obsoletes: libfm-qt3

%description
LibFM-Qt is a core library of PCManFM-Qt file manager.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: libexif-devel libmenu-cache-devel
Requires: %name = %EVR

%description devel
This package contains files needed to build applications using LibFM-Qt.

%prep
%setup
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -name '*.cpp' -o -name '*.hpp' -o -name '*.h' -print0 |
	xargs -r0 sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%cmake -DREQUIRED_QT_VERSION=5.9
%cmake_build

%install
%cmakeinstall_std

# We need to fix this upstream
find %buildroot -size 0 -delete

%files
%_libdir/*.so.*
%_datadir/%name/
%_xdgmimedir/*/*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%_datadir/cmake/fm-qt/*
%doc AUTHORS CHANGELOG LICENSE README.md

%changelog
* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Mon Jun 24 2019 Michael Shigorin <mike@altlinux.org> 0.14.1-alt2
- E2K: strip UTF-8 BOM for lcc < 1.24

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Mon Jan 28 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Sat Aug 25 2018 Anton Midyukov <antohami@altlinux.org> 0.13.1-alt1.1
- Rebuilt with qt 5.11

* Tue Jun 05 2018 Anton Midyukov <antohami@altlinux.org> 0.13.1-alt1
- new version 0.13.1

* Mon May 28 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt2
- obsoletes libfm-qt3

* Thu May 24 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- 0.12.0

* Tue Oct 04 2016 Michael Shigorin <mike@altlinux.org> 0.11.1-alt1
- built for sisyphus (partially based on fedora spec)

