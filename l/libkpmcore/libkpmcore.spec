%define _name kpmcore
%define xdg_name org.kde.%_name
%define _libexecdir %_prefix/libexec

Name: lib%_name
Version: 4.0.1
Release: alt1

Summary: Library for managing partitions
Group: System/Libraries
License: GPLv3
Url: https://github.com/KDE/%_name

Source: %url/archive/v%version/%_name-%version.tar.gz

Provides: %_name = %version-%release

%define blkid_ver 2.30

Requires: polkit

BuildRequires(pre): rpm-build-kf5
BuildRequires: gcc-c++ extra-cmake-modules %_bindir/appstreamcli
BuildRequires: libdbus-devel libatasmart-devel libblkid-devel >= %blkid_ver libparted-devel
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel libqca-qt5-devel

%description
%_name is a Library for managing partitions. Common code for KDE
Partition Manager and other projects.

%package devel
Summary: Development files for icclib
Group: Development/C
Requires: %name = %version-%release
Provides: %_name-devel = %version-%release

%description devel
%_name is a Library for managing partitions. Common code for KDE
Partition Manager and other projects.

This package provides headers and libraries for development applications
using %_name.

%prep
%setup -n %_name-%version

%build
%K5build

%install
%K5install

%files
%_libexecdir/kauth/kpmcore_externalcommand
%_datadir/dbus-1/system.d/%xdg_name.applicationinterface.conf
%_datadir/dbus-1/system.d/%xdg_name.helperinterface.conf
%_datadir/dbus-1/system.d/%xdg_name.externalcommand.conf
%_K5lib/*.so.*
%_K5plug/*.so
%_K5dbus_sys_srv/%xdg_name.externalcommand.service
%_datadir/polkit-1/actions/%xdg_name.externalcommand.policy

%files devel
%_includedir/%_name/
%_K5lib/cmake/KPMcore/
%_K5link/*.so


%changelog
* Mon Oct 07 2019 Yuri N. Sedunov <aris@altlinux.org> 4.0.1-alt1
- 4.0.1

* Thu May 02 2019 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Sun Mar 17 2019 Yuri N. Sedunov <aris@altlinux.org> 3.80.0-alt1
- 3.80.0

* Thu Dec 28 2017 Yuri N. Sedunov <aris@altlinux.org> 3.3.0-alt1
- 3.3.0

* Sat Nov 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Oct 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Thu Apr 06 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- first build for Sisyphus

