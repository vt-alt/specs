Name: farmhash
Version: 1.1
Release: alt2
Summary: FarmHash, a family of hash functions 
Group: Development/C++
# https://github.com/google/farmhash
Source: %name-%version.tar
License: MIT
Url: http://code.google.com/p/farmhash 
BuildRequires: gcc-c++

%description
FarmHash provides hash functions for strings and other data.
The functions  mix the input bits thoroughly but are not suitable for
cryptography.

This package contains the shared library.

%package devel
Group: Development/C++
Summary: Developmen environment for %name
Requires: %name = %version
%description devel
Development environment for %name, %summary

%package devel-static
Group: Development/C++
Summary: Static developmen environment for %name
Requires: %name-devel = %version
%description devel-static
Static development environment for %name, %summary

%prep
%setup

%build
%autoreconf
%ifarch x86_64
export CXXFLAGS="-g -maes -mavx -msse4.2 -O3"
%else
export CXXFLAGS="-g -O3"
%endif

%configure  
%make

%install
%makeinstall

%files
%doc README NEWS
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%files devel-static
%_libdir/*.a

%changelog
* Tue Jun 25 2019 Anton Farygin <rider@altlinux.ru> 1.1-alt2
- enabled build for i586 and aarch64

* Mon Jun 24 2019 Anton Farygin <rider@altlinux.ru> 1.1-alt1
- first build for ALT


