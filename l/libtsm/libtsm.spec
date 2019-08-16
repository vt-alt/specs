Name: libtsm
Version: 4.0.1
Release: alt1
Summary: Terminal-emulator State Machine
Group: System/Libraries
License: MIT
Url: https://github.com/Aetf/libtsm
Source: %name-%version.tar
BuildRequires: cmake
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(check)

%description
TSM is a state machine for DEC VT100-VT520 compatible terminal emulators.
It tries to support all common standards while keeping compatibility to
existing emulators like xterm, gnome-terminal, konsole...

TSM itself does not provide any rendering nor window management. It is a
simple plain state machine without any external dependencies. It can be
used to implement terminal emulators, but also to implement other applications
that need to interpret terminal escape sequences.

This library is very similar to libvte of the gnome project. However,
libvte is highly bound to GTK+, which makes it unsuitable for non-graphics
projects that need to parse escape sequences. Instead, TSM tries to restrict
its API to terminal emulation only. Furthermore, TSM does not try to
establish a new terminal emulation standard, but instead keeps compatibility
as close to xterm as possible. This is why the TERM variable can be set to
xterm-color256 with any TSM based terminal emulator.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo

%cmake_build

%install
%cmakeinstall_std

%files
%doc COPYING README
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Thu Aug 01 2019 Alexey Shabalin <shaba@altlinux.org> 4.0.1-alt1
- 4.0.1

* Tue Jun 17 2014 Alexey Shabalin <shaba@altlinux.ru> 3-alt1
- Initial Package.
