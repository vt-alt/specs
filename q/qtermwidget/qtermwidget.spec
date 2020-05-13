# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: qtermwidget
Version: 0.15.0
Release: alt1

Summary: unicode-enabled, embeddable QT4 terminal widget
License: GPL
Group: Terminals

Url: https://github.com/lxqt/qtermwidget
Source: %name-%version.tar

# Automatically added by buildreq on Wed Mar 07 2012
# optimized out: cmake-modules fontconfig libqt4-core libqt4-designer libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libstdc++-devel
BuildRequires: cmake gcc-c++
BuildRequires: qt5-base-devel qt5-tools-devel
BuildRequires: lxqt-build-tools

%description
QTermWidget is an opensource project based on KDE Konsole
application. The main goal of this project is to provide
unicode-enabled, embeddable Qt5 widget for using as a built-in
console (or terminal emulation widget).

Of course I'm aware about embedding abilities of original
Konsole, but once I had Qt without KDE, and it was a serious
problem.

0.4.0+ is a friendly fork, the original project is still available
at http://qtermwidget.sourceforge.net/

%package data
Summary: unicode-enabled, embeddable Qt5 terminal widget shared data
Group: Terminals
BuildArch: noarch
Conflicts: qtermwidget-qt5-data < 0.8.0

%description data
QTermWidget is an opensource project based on KDE Konsole
application. The main goal of this project is to provide
unicode-enabled, embeddable Qt5 widget for using as a built-in
console (or terminal emulation widget).

This package contains the shared data.

%package -n lib%name
Summary: unicode-enabled, embeddable Qt5 terminal widget library
Group: System/Libraries
Requires: %name-data = %version-%release
Conflicts: libqtermwidget-qt5 < 0.8.0

%description -n lib%name
This package contains the shared library for %name.

%package -n lib%name-devel
Summary: unicode-enabled, embeddable Qt5 terminal widget library
Group: Development/KDE and QT

%description -n lib%name-devel
This package contains the development headers for %name library.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files

%files data
%_datadir/%{name}*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%doc AUTHORS LICENSE README*
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_libdir/cmake/*/

%changelog
* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Mon Jan 28 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Sat Aug 25 2018 Anton Midyukov <antohami@altlinux.org> 0.9.0-alt1.1
- Rebuilt with qt 5.11s

* Tue May 22 2018 Anton Midyukov <antohami@altlinux.org> 0.9.0-alt1
- 0.9.0

* Tue Oct 24 2017 Michael Shigorin <mike@altlinux.org> 0.8.0-alt2
- added conflicts with qtermwidget-qt5 package

* Tue Oct 24 2017 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0 built against Qt5

* Tue Oct 04 2016 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- 0.7.0

* Fri Nov 14 2014 Michael Shigorin <mike@altlinux.org> 0.6.0-alt1
- 0.6.0 (see also #30468)
- updated Url:

* Wed Mar 07 2012 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1
- initial build (loosely based on qterminal.spec and upstream one)

