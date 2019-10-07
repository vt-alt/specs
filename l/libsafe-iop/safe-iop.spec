Name: libsafe-iop
Version: 0.3.1
Release: alt1

Summary: Safe integer operation library for C
Group: System/Libraries
License: Public
Url: https://code.google.com/p/safe-iop

Source: %name-%version.tar

Patch0: makefile-compile-libs.patch

%description
This library provides a collection of (macro-based) functions for performing
safe integer operations across platform and architecture with a straightforward
API.

This package provides the dynamically linked library. The dynamic library
supplies a format-string based interface which is in pre-alpha.

%package devel
Summary: Development package for safe-iop library
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides files for development using safe-iop library.

%prep
%setup
%patch0 -p1

%build
%make_build
ln -s libsafe_iop.so.0.3 libsafe_iop.so

%install
install -d -m 755 %buildroot%_libdir
install -d -m 755 %buildroot%_includedir
install -m 644 libsafe_iop.so* %buildroot%_libdir
install -m 644 include/safe_iop.h %buildroot%_includedir

%files
%_libdir/*.so.*
%doc README

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Tue Aug 06 2019 Pavel Nakonechnyi <zorg@altlinux.org> 0.3.1-alt1
- initial build
