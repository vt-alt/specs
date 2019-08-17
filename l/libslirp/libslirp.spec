
Name: libslirp
Version: 4.0.0.0.16.g7646
Release: alt1
Summary: A general purpose TCP-IP emulator
Group: System/Libraries
License: BSD and MIT
Url: https://gitlab.freedesktop.org/slirp/%name
Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: glib2-devel

%description
A general purpose TCP-IP emulator used by virtual machine hypervisors
to provide virtual networking services.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md COPYRIGHT
%_libdir/%name.so.0*

%files devel
%_includedir/slirp
%_libdir/%name.so
%_pkgconfigdir/slirp.pc

%changelog
* Sun Aug 18 2019 Alexey Shabalin <shaba@altlinux.org> 4.0.0.0.16.g7646-alt1
- Initial package master snapshot
