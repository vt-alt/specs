Name: libvariant
Version: 1.1.6
Release: alt2

Summary: C++11/C++14 Variant

Group: Development/C++
License: BSD

Url: https://github.com/mapbox/variant
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/mapbox/variant/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++

BuildArch: noarch

%description
An header-only alternative to boost::variant for C++11 and C++14.

%package devel
Group: Development/Other
Summary: Development files for %name

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%__subst "s|-O3|%optflags|" Makefile
# https://github.com/phoronix-test-suite/phoronix-test-suite/issues/333
%__subst "s|-march=native||" Makefile

%build
%make_build out/unit

%check
make test

%install
mkdir -p %buildroot%_includedir/%name/
cp -a include/mapbox %buildroot%_includedir/%name/

%files devel
%dir %_includedir/%name/
%_includedir/%name/mapbox/

%changelog
* Mon Oct 21 2019 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt2
- fix build at ppc64le (s/-march=native/-mcpu=native/)
- make package as noarch

* Tue Jun 11 2019 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt1
- new version 1.1.6 (with rpmrb script)

* Tue Jun 19 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1.5-alt2
- enable check

* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.5-alt1
- initial build for ALT Sisyphus
