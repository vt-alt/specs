
Name: libslirp
Version: 4.3.0
Release: alt1
Summary: A general purpose TCP-IP emulator
Group: System/Libraries
License: BSD-3-Clause
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
echo "%version" > .tarball-version

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
* Fri May 08 2020 Alexey Shabalin <shaba@altlinux.org> 4.3.0-alt1
- new version 4.3.0 (Fixes: CVE-2020-1983)

* Fri Mar 20 2020 Alexey Shabalin <shaba@altlinux.org> 4.2.0-alt1
- 4.2.0

* Sun Aug 18 2019 Alexey Shabalin <shaba@altlinux.org> 4.0.0.0.16.g7646-alt1
- Initial package master snapshot
