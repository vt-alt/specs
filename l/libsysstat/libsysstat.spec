# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: libsysstat
Version: 0.4.3
Release: alt1

Summary: Library used to query system info and statistics
License: LGPL
Group: System/Libraries

Url: https://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: lxqt-build-tools qt5-base-devel qt5-tools-devel

%description
%summary

%package devel
Summary: Development headers for %name
Group: Development/C++
Requires: %name = %version

%description devel
This package provides the development files for %name
which is used to query system info and statistics.

%prep
%setup

%build
%ifarch e2k
%add_optflags -std=c++11
%endif
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*/
%_pkgconfigdir/*.pc
%_datadir/cmake/*/

%changelog
* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.4.3-alt1
- new version 0.4.3

* Sat Jan 26 2019 Anton Midyukov <antohami@altlinux.org> 0.4.2-alt1
- new version 0.4.2

* Sat Aug 25 2018 Anton Midyukov <antohami@altlinux.org> 0.4.1-alt1.1
- Rebuilt with qt 5.11

* Tue May 22 2018 Anton Midyukov <antohami@altlinux.org> 0.4.1-alt1
- new version 0.4.1

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1
- 0.4.0

* Fri Aug 25 2017 Michael Shigorin <mike@altlinux.org> 0.3.2-alt2
- E2K: add -std=c++11 explicitly

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.3.2-alt1
- 0.3.2

* Tue Nov 03 2015 Michael Shigorin <mike@altlinux.org> 0.3.1-alt1
- 0.3.1

* Mon Feb 09 2015 Michael Shigorin <mike@altlinux.org> 0.3.0-alt1
- 0.3.0 built against qt5

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt2
- use untagged upstream commit g151ef16 (NB: API change)

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt1
- initial release

