Name: libco
Version: 20
Release: alt1
Summary: libco is a cross-platform implementation of cooperative-multithreading
License: ISC
Group: Development/C
URL: https://github.com/canonical/raft

Source0: %name-%version.tar

%define _unpackaged_files_terminate_build 1

%description
libco is a cross-platform, permissively licensed implementation of
cooperative-multithreading; a feature that is sorely lacking from the ISO C/C++
standard.
The library is designed for maximum speed and portability, and not for safety or
features. If safety or extra functionality is desired, a wrapper API can easily
be written to encapsulate all library functions.

%package devel
Summary: libco is a cross-platform implementation of cooperative-multithreading
Group: Development/C
Requires: %name = %version-%release

%description devel
libco is a cross-platform, permissively licensed implementation of
cooperative-multithreading; a feature that is sorely lacking from the ISO C/C++
standard.
The library is designed for maximum speed and portability, and not for safety or
features. If safety or extra functionality is desired, a wrapper API can easily
be written to encapsulate all library functions.

%package devel-static
Summary: Static %name library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
libco is a cross-platform, permissively licensed implementation of
cooperative-multithreading; a feature that is sorely lacking from the ISO C/C++
standard.

This package contains the static library needed to develop
statically linked programs that use the %name library.

%prep
%setup -q -n %name-%version

%build
%make_build

%install
%makeinstall_std LIBDIR=%_lib

%files
%doc LICENSE
%_libdir/%name.so.*

%files devel
%_includedir/*.h
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%files devel-static
%_libdir/%name.a

%changelog
* Fri Nov 15 2019 Denis Pynkin <dans@altlinux.org> 20-alt1
- Update

* Sun Sep 29 2019 Denis Pynkin <dans@altlinux.org> 19.1-alt1
- Initial version for ALTLinux
